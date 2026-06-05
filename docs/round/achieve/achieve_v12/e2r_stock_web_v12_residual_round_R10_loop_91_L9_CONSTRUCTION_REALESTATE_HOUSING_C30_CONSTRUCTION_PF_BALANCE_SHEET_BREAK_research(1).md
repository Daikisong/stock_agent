# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_91_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 91 is R10 / loop 91. R10 is the L9 construction/PF round, so this run uses C30 and avoids the R10 loop 88/89/90 symbol sets.

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
scheduled_loop = 91
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 91
```

R10 permits L9 construction / real-estate / housing research. Previous R10 loop 90 used Hyundai Construction / HS Hwasung / Ilsung Construction, so this loop uses a different mid-builder and regional-construction split.

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
previous R9 loop-91 C29 symbols avoided: 200880, 038110, 033530
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
003070 / Stage2-Actionable / 2024-01-24
001260 / Stage2-Actionable / 2024-02-14
021320 / Stage4B / 2024-04-08
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
| 003070 | atlas/symbol_profiles/003/003070.json | selected 2024 window clean after old CA candidates |
| 001260 | atlas/symbol_profiles/001/001260.json | selected 2024 window clean after old 2013-or-earlier CA candidates |
| 021320 | atlas/symbol_profiles/021/021320.json | selected 2024 window clean after old 2014 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L91_C30_KOLONGLOBAL_2024_MID_BUILDER_PF_ORDER_RECOVERY_POSITIVE | 003070 | 2024-01-24 | yes | 180 | yes | yes | true |
| R10L91_C30_NAMKWANG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2 | 001260 | 2024-02-14 | yes | 180 | yes | yes | true |
| R10L91_C30_KCCCONST_2024_CONSTRUCTION_PF_EVENT_CAP_4B | 021320 | 2024-04-08 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE | Positive Stage2 requires PF/cashflow repair, funding capacity, order quality, and balance-sheet bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_CONSTRUCTION_FALSE_STAGE2 | Regional construction recovery label without PF/cashflow bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | CONSTRUCTION_PF_EVENT_CAP_4B | PF event premium should route to 4B when cashflow/balance evidence is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L91_C30_KOLONGLOBAL_2024_MID_BUILDER_PF_ORDER_RECOVERY_POSITIVE | 003070 | 코오롱글로벌 | positive | Mid-builder PF/order recovery produced high MFE with controlled 90D MAE. |
| R10L91_C30_NAMKWANG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2 | 001260 | 남광토건 | counterexample | Regional construction/PF watch had almost no 90D MFE and meaningful MAE. |
| R10L91_C30_KCCCONST_2024_CONSTRUCTION_PF_EVENT_CAP_4B | 021320 | KCC건설 | counterexample / 4B | Construction/PF event premium capped at the April spike and failed to sustain. |

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
| Kolon Global PF/order recovery | historical public/report proxy | true | true | shadow-only positive |
| Namkwang regional construction false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| KCC Construction PF event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 003070 | atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv | atlas/symbol_profiles/003/003070.json |
| 001260 | atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv | atlas/symbol_profiles/001/001260.json |
| 021320 | atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv | atlas/symbol_profiles/021/021320.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY | 003070 | Stage2-Actionable | 2024-01-24 | 9030 | positive | PF/order recovery bridge worked |
| R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH | 001260 | Stage2-Actionable | 2024-02-14 | 7570 | counterexample | regional construction false Stage2 |
| R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP | 021320 | Stage4B | 2024-04-08 | 4615 | counterexample/4B | construction/PF event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY | 9030 | 18.49 | -2.55 | 34.00 | -9.52 | 78.41 | -9.52 | 2024-06-21 | 16110 | -47.24 |
| R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH | 7570 | 1.19 | -16.38 | 1.19 | -20.48 | 12.95 | -21.40 | 2024-07-30 | 8550 | -30.41 |
| R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP | 4615 | 24.59 | -11.70 | 24.59 | -11.70 | 24.59 | -11.70 | 2024-04-08 | 5750 | -27.48 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF/cashflow/order-quality/balance-sheet bridge |
| local_4b_watch_guard | strengthen: regional construction and PF event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: high/persistent MAE construction rows cannot promote without PF/cashflow bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is PF/cashflow bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 003070 | good_stage2 | PF/order bridge produced large MFE with controlled 90D drawdown. |
| 001260 | bad_stage2 | Regional construction watch lacked PF/cashflow bridge and had low 90D MFE. |
| 021320 | good_4B | PF event premium spiked and then failed to sustain a broad rerating. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 001260 regional false Stage2 | 0.90 | 0.89 | false Stage2 due missing PF/cashflow bridge |
| 021320 construction/PF cap | 1.00 | 1.00 | good full-window 4B timing |
| 003070 PF/order bridge | n/a | n/a | positive Stage2, but later event/valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 001260 / 021320
```

No hard 4C candidate is proposed. R10 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF cases, Stage2 requires verified PF cashflow repair, funding capacity, debt maturity relief, order quality, balance-sheet repair, or margin/revision bridge. Regional construction beta, PF event premium, or builder label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split real PF/cashflow/order-quality repair positives from regional construction false Stage2 and PF event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 19.93 | -13.90 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 19.93 | -13.90 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/cashflow bridge required | 2 | 17.60 | -15.00 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 17.60 | -15.00 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction themes as positive | 1 | 34.00 | -9.52 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 003070 PF/order bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 34.00 | -9.52 | mid_builder_PF_order_recovery_positive |
| 001260 regional false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 1.19 | -20.48 | regional_construction_PF_false_stage2 |
| 021320 PF event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 24.59 | -11.70 | construction_PF_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 mid-builder PF/order recovery positive, regional construction false Stage2, and construction PF event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: mid_builder_PF_order_recovery_positive, regional_construction_PF_false_stage2, construction_PF_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_PF_cashflow_order_quality_balance_bridge,0,"C30 Stage2 should require PF/cashflow repair, funding capacity, order quality, debt maturity relief, balance-sheet repair, or margin/revision bridge, not construction beta label alone","Kolon Global positive worked; Namkwang and KCC Construction event/theme rows failed positive-stage promotion","R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY|R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH|R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_regional_construction_and_PF_event_premiums_as_4B_watch,0,"Regional construction and PF event premiums can peak before durable cashflow/balance repair appears","Namkwang had low 90D MFE; KCC Construction showed full-window event-cap behavior after April spike","R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH|R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_watch_has_high_or_persistent_MAE_without_PF_bridge,0,"High or persistent MAE after bridge-missing construction entries should block Stage2/Stage3 promotion unless PF/cashflow evidence survives","Namkwang MAE90=-20.48 and KCC Construction event cap failed to sustain beyond spike","R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH|R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L91_C30_KOLONGLOBAL_2024_MID_BUILDER_PF_ORDER_RECOVERY_POSITIVE", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "structural_success_with_later_event_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Mid-builder PF discount repair / order-quality recovery bridge produced strong MFE with controlled 90D MAE. C30 works when PF/cashflow repair is connected to funding capacity, order quality, and balance-sheet bridge, not construction beta alone.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_PF_cashflow_order_quality_bridge_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L91_C30_NAMKWANG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "symbol": "001260", "company_name": "남광토건", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "failed_rerating_regional_construction_beta", "positive_or_counterexample": "counterexample", "best_trigger": "R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional construction/PF normalization watch had almost no 90D forward MFE and then meaningful MAE. C30 Stage2 should not be awarded without PF/cashflow repair, debt-maturity relief, order quality, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_recovery_counts_without_PF_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2013-or-earlier CA candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R10L91_C30_KCCCONST_2024_CONSTRUCTION_PF_EVENT_CAP_4B", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Construction/PF event premium spiked intraday and then failed to sustain a full-window rerating. C30 event premiums should route to 4B/watch unless PF/cashflow repair and balance-sheet evidence survive beyond the spike.", "current_profile_verdict": "current_profile_4B_too_late_if_construction_PF_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2014 CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY", "case_id": "R10L91_C30_KOLONGLOBAL_2024_MID_BUILDER_PF_ORDER_RECOVERY_POSITIVE", "symbol": "003070", "company_name": "코오롱글로벌", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "sector": "mid_builder_PF_order_quality_recovery", "primary_archetype": "mid_builder_PF_cashflow_order_quality_balance_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 9030.0, "evidence_available_at_that_date": "mid-builder PF discount repair, funding/cashflow stabilization, order-quality and balance-sheet bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["PF_discount_repair_proxy", "cashflow_bridge_proxy", "order_quality_backlog_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "high_MFE90", "very_high_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_construction_event_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv", "profile_path": "atlas/symbol_profiles/003/003070.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.49, "MFE_90D_pct": 34.0, "MFE_180D_pct": 78.41, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.55, "MAE_90D_pct": -9.52, "MAE_180D_pct": -9.52, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-21", "peak_price": 16110.0, "drawdown_after_peak_pct": -47.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_construction_event_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "PF_repair_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_mid_builder_PF_order_recovery_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R10L91_C30_003070_2024-01-24_9030", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH", "case_id": "R10L91_C30_NAMKWANG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "symbol": "001260", "company_name": "남광토건", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "sector": "regional_construction_PF_normalization_watch", "primary_archetype": "regional_construction_watch_without_PF_cashflow_balance_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 7570.0, "evidence_available_at_that_date": "regional construction PF normalization watch and sector-beta recovery proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["regional_construction_recovery_watch", "PF_normalization_theme", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["low_MFE90", "PF_cashflow_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv", "profile_path": "atlas/symbol_profiles/001/001260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.19, "MFE_90D_pct": 1.19, "MFE_180D_pct": 12.95, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.38, "MAE_90D_pct": -20.48, "MAE_180D_pct": -21.4, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-30", "peak_price": 8550.0, "drawdown_after_peak_pct": -30.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.89, "four_b_timing_verdict": "regional_construction_PF_watch_was_false_stage2_due_missing_cashflow_balance_bridge", "four_b_evidence_type": ["regional_construction_beta", "positioning_overheat_watch", "PF_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_regional_construction_PF_watch_without_balance_bridge", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_recovery_counts_without_PF_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R10L91_C30_001260_2024-02-14_7570", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP", "case_id": "R10L91_C30_KCCCONST_2024_CONSTRUCTION_PF_EVENT_CAP_4B", "symbol": "021320", "company_name": "KCC건설", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "sector": "construction_PF_event_premium", "primary_archetype": "construction_PF_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-08", "entry_date": "2024-04-08", "entry_price": 4615.0, "evidence_available_at_that_date": "construction PF event premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["construction_PF_event_premium", "regional_builder_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "PF_cashflow_bridge_unverified", "post_event_range_failure"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/021/021320/2024.csv", "profile_path": "atlas/symbol_profiles/021/021320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.59, "MFE_90D_pct": 24.59, "MFE_180D_pct": 24.59, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.7, "MAE_90D_pct": -11.7, "MAE_180D_pct": -11.7, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-08", "peak_price": 5750.0, "drawdown_after_peak_pct": -27.48, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_construction_PF_event_cap", "four_b_evidence_type": ["PF_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_construction_PF_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_construction_PF_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2014_CA", "same_entry_group_id": "R10L91_C30_021320_2024-04-08_4615", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L91_C30_KOLONGLOBAL_2024_MID_BUILDER_PF_ORDER_RECOVERY_POSITIVE", "trigger_id": "R10L91_C30_KOLONGLOBAL_2024_STAGE2_ACTIONABLE_MID_BUILDER_PF_ORDER_RECOVERY", "symbol": "003070", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "mid_builder_PF_order_recovery_positive", "MFE_90D_pct": 34.0, "MAE_90D_pct": -9.52, "score_return_alignment_label": "mid_builder_PF_order_recovery_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L91_C30_NAMKWANG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "trigger_id": "R10L91_C30_NAMKWANG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION_PF_WATCH", "symbol": "001260", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_construction_PF_false_stage2", "MFE_90D_pct": 1.19, "MAE_90D_pct": -20.48, "score_return_alignment_label": "regional_construction_PF_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_recovery_counts_without_PF_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L91_C30_KCCCONST_2024_CONSTRUCTION_PF_EVENT_CAP_4B", "trigger_id": "R10L91_C30_KCCCONST_2024_STAGE4B_CONSTRUCTION_PF_EVENT_CAP", "symbol": "021320", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "construction_PF_event_cap_4B_guard", "MFE_90D_pct": 24.59, "MAE_90D_pct": -11.7, "score_return_alignment_label": "construction_PF_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_construction_PF_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "91", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_ORDER_RECOVERY_BRIDGE_VS_REGIONAL_CONSTRUCTION_FALSE_STAGE2_AND_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["mid_builder_PF_order_recovery_positive", "regional_construction_PF_false_stage2", "construction_PF_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 91
next_round = R11
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
