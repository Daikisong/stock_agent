# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | PF_cashflow_bridge_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_97_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This file is the corrected final output for this execution. The scheduler state after R9 loop 97 is R10 / loop 97. R10 is the L9 construction / real-estate / housing round, and this run fills C30 construction PF balance-sheet break behavior rather than repeating the immediately preceding R10 loop 96 C30 symbols or top-covered PF/building names.

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
PF_cashflow_bridge_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R10
scheduled_loop = 97
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 97
```

C30 is a PF/cashflow repair archetype. A construction recovery headline is the crane silhouette; the building only stands when order quality, cash conversion, funding repair, balance-sheet safety, margin and revision hold together.

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
previous R10 loop-96 symbols avoided: 010960, 017000, 091590
previous R9 loop-97 C29 symbols avoided: 064960, 092200, 370090
```

Selected rows avoid hard duplicates and top repeated C30 symbols:

```text
097230 / Stage2-Actionable / 2024-04-18
016250 / Stage2-Actionable / 2024-02-19
046940 / Stage4B / 2024-01-30
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
| 097230 | atlas/symbol_profiles/097/097230.json | selected 2024/2025 180D window clean after old 2013/2014/2019 CA candidates |
| 016250 | atlas/symbol_profiles/016/016250.json | selected 2024 window clean after old 2020~2023 CA candidates and before 2025 CA candidate |
| 046940 | atlas/symbol_profiles/046/046940.json | selected 2024 window clean after old 2006/2008/2010 CA/name-history candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE | 097230 | 2024-04-18 | yes | 180 | yes | yes | true |
| R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2 | 016250 | 2024-02-19 | yes | 180 | yes | yes | true |
| R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B | 046940 | 2024-01-30 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE | Positive Stage2 requires order quality, cashflow repair, funding visibility, balance-sheet safety, margin and revision bridge. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MIDCAP_EPC_PF_FALSE_STAGE2 | Mid-cap EPC/PF recovery watch without cashflow/funding bridge can become false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LOCAL_CIVIL_INFRA_EVENT_CAP_4B | Local civil-infra / construction-recovery event premium should route to 4B when cashflow, funding and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE | 097230 | HJ중공업 | positive | Heavy-civil/infrastructure order/cashflow bridge produced strong MFE, but later drawdown requires 4B valuation watch. |
| R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2 | 016250 | SGC E&C | counterexample | Mid-cap EPC/PF recovery watch had minimal MFE and persistent MAE. |
| R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B | 046940 | 우원개발 | counterexample / 4B | Local civil-infra event premium capped on the January spike and then de-rated. |

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
| HJ Heavy Industries heavy-civil order/cashflow bridge | historical public/report proxy | true | true | shadow-only positive |
| SGC E&C mid-cap EPC/PF false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Woowon Development local civil-infra event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 097230 | atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv and 2025.csv | atlas/symbol_profiles/097/097230.json |
| 016250 | atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv | atlas/symbol_profiles/016/016250.json |
| 046940 | atlas/ohlcv_tradable_by_symbol_year/046/046940/2024.csv | atlas/symbol_profiles/046/046940.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE | 097230 | Stage2-Actionable | 2024-04-18 | 3005 | positive | heavy-civil order/cashflow bridge worked |
| R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH | 016250 | Stage2-Actionable | 2024-02-19 | 18710 | counterexample | mid-cap EPC/PF false Stage2 |
| R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP | 046940 | Stage4B | 2024-01-30 | 3540 | counterexample/4B | local civil-infra event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE | 3005 | 18.80 | -3.83 | 25.96 | -10.15 | 157.90 | -26.79 | 2025-01-08 | 7750 | -25.29 |
| R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH | 18710 | 1.23 | -15.02 | 1.23 | -21.11 | 1.23 | -25.17 | 2024-02-19 | 18940 | -26.08 |
| R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP | 3540 | 0.14 | -16.24 | 0.14 | -22.60 | 0.14 | -22.60 | 2024-01-30 | 3545 | -22.71 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs order quality / cashflow / funding / balance-sheet / cost-to-complete / margin / revision bridge |
| PF_cashflow_bridge_guardrail | strengthen: PF recovery labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing mid-cap EPC and local civil-infra event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE construction/PF rows cannot promote without durable cashflow bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether construction/PF narrative becomes order/cashflow repair.

| symbol | stage quality | explanation |
|---|---|---|
| 097230 | good_stage2_with_later_watch | Order/cashflow bridge produced strong MFE, but later balance-sheet and valuation watch remains necessary. |
| 016250 | bad_stage2 | Mid-cap EPC/PF watch lacked cashflow/funding bridge and produced minimal MFE with persistent MAE. |
| 046940 | good_4B | Local civil-infra event premium peaked immediately and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 016250 mid-cap EPC/PF false Stage2 | 0.99 | 0.99 | false Stage2 due missing cashflow/funding/order-quality/margin bridge |
| 046940 local civil-infra cap | 1.00 | 1.00 | good full-window 4B timing after local civil-infra event premium |
| 097230 heavy-civil bridge | n/a | n/a | positive Stage2, but later balance-sheet valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 016250 / 046940
```

No hard 4C candidate is introduced in this R10 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF balance-sheet cases, Stage2 requires verified order quality, cashflow repair, funding capacity, balance-sheet safety, cost-to-complete visibility, margin, or revision bridge. Construction, PF recovery, civil infra, EPC, local builder, housing recovery or relative-strength label alone remains watch/4B/4C.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split true order/cashflow/funding positives from mid-cap EPC/PF false Stage2 and local civil-infra event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 9.11 | -17.95 | 0.67 | mixed; C30 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 9.11 | -17.95 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L9 order/cashflow/funding bridge required | 2 | 13.60 | -16.38 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 bridge vs event-cap split | 2 | 13.60 | -16.38 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction/PF themes as positive | 1 | 25.96 | -10.15 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 097230 heavy-civil bridge | 64 | Stage2-Watch | 76 | Stage2-Actionable | 25.96 | -10.15 | heavy_civil_infra_order_cashflow_positive |
| 016250 mid-cap EPC/PF false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.23 | -21.11 | midcap_EPC_PF_false_stage2 |
| 046940 local civil-infra cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 0.14 | -22.60 | local_civil_infra_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 HJ Heavy Industries heavy-civil order/cashflow positive, SGC E&C mid-cap EPC/PF false Stage2, and Woowon Development local civil-infra event-cap 4B while avoiding top repeated C30 and previous R10/R9 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, PF_cashflow_bridge_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: heavy_civil_infra_order_cashflow_positive, midcap_EPC_PF_false_stage2, local_civil_infra_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, PF_cashflow_bridge_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_order_quality_cashflow_funding_balance_sheet_margin_revision_bridge,0,"C30 Stage2 should require order quality, cashflow repair, funding capacity, balance-sheet safety, cost-to-complete visibility, margin, or revision bridge, not construction/PF recovery label alone","HJ Heavy Industries positive worked; SGC E&C and Woowon Development event/watch rows failed positive-stage promotion","R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE|R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH|R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_bridge_missing_midcap_EPC_and_local_civil_infra_event_premiums_as_4B_watch,0,"Mid-cap EPC/PF and local civil-infra premiums can peak before funding, cashflow and margin bridge is proven","SGC E&C had minimal MFE and persistent MAE; Woowon Development showed 4B event-cap behavior after the January civil-infra spike","R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH|R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_PF_theme_has_high_or_persistent_MAE_without_cashflow_bridge,0,"High or persistent MAE after bridge-missing C30 entries should block Stage2/Stage3 promotion unless order, cashflow, funding and margin evidence survives","SGC E&C MAE90=-21.11 and Woowon Development MAE90=-22.60","R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH|R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "097230", "company_name": "HJ중공업", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "case_type": "structural_success_with_later_construction_balance_sheet_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Heavy civil / infrastructure order and cashflow bridge produced strong MFE after the April retest, but later high drawdown means C30 positives still need balance-sheet and valuation watch. C30 works only when construction/PF narrative maps into order quality, cash conversion, funding visibility, balance-sheet safety, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_order_quality_cashflow_funding_balance_sheet_margin_revision_bridge_not_construction_theme_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2013/2014/2019 corporate-action candidates. Mixed civil/heavy-industry exposure noted; used as L9 heavy-civil bridge row, not pure shipbuilding row."}
{"row_type": "case", "case_id": "R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2", "symbol": "016250", "company_name": "SGC E&C", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "case_type": "failed_rerating_midcap_EPC_PF_recovery_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Mid-cap EPC/PF recovery watch had minimal MFE and persistent MAE before a later short rebound. C30 Stage2 should not be awarded without verified PF cashflow repair, funding capacity, order-quality visibility, cost-to-complete control, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_midcap_EPC_PF_watch_counts_without_cashflow_funding_order_quality_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020~2023 CA candidates and before 2025 CA candidate. Source-proxy only."}
{"row_type": "case", "case_id": "R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B", "symbol": "046940", "company_name": "우원개발", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Local civil-infrastructure / construction-recovery event premium capped on the January spike and then bled into a long drawdown. C30 should route bridge-missing civil/PF event premiums to 4B unless order quality, funding repair, cash conversion, balance-sheet safety, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_local_civil_infra_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2006/2008/2010 corporate-action and name-history candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE", "case_id": "R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE", "symbol": "097230", "company_name": "HJ중공업", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "sector": "heavy_civil_infrastructure_order_cashflow_balance_sheet", "primary_archetype": "order_quality_cashflow_funding_balance_sheet_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | PF_cashflow_bridge_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 3005.0, "evidence_available_at_that_date": "heavy-civil/infrastructure order-quality, cashflow repair, funding visibility, balance-sheet safety and margin/revision bridge proxy after April retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["order_quality_proxy", "cashflow_repair_proxy", "funding_visibility_proxy", "balance_sheet_safety_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "very_strong_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_construction_balance_sheet_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097230/2024.csv; atlas/ohlcv_tradable_by_symbol_year/097/097230/2025.csv", "profile_path": "atlas/symbol_profiles/097/097230.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.8, "MFE_90D_pct": 25.96, "MFE_180D_pct": 157.9, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.83, "MAE_90D_pct": -10.15, "MAE_180D_pct": -26.79, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-08", "peak_price": 7750.0, "drawdown_after_peak_pct": -25.29, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_balance_sheet_and_construction_valuation_4B_watch_needed", "four_b_evidence_type": ["order_cashflow_bridge", "balance_sheet_safety", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_heavy_civil_infra_order_cashflow_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2013_2014_2019_CA", "same_entry_group_id": "R10L97_C30_097230_2024-04-18_3005", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH", "case_id": "R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2", "symbol": "016250", "company_name": "SGC E&C", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "sector": "midcap_EPC_PF_recovery_cashflow_watch", "primary_archetype": "midcap_EPC_PF_watch_without_cashflow_funding_order_quality_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | PF_cashflow_bridge_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 18710.0, "evidence_available_at_that_date": "mid-cap EPC / construction PF recovery watch without confirmed cashflow repair, funding capacity, order-quality visibility, cost-to-complete control or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["midcap_EPC_PF_recovery_watch", "construction_recovery_sympathy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["minimal_MFE90", "persistent_MAE90", "cashflow_funding_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv", "profile_path": "atlas/symbol_profiles/016/016250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.23, "MFE_90D_pct": 1.23, "MFE_180D_pct": 1.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.02, "MAE_90D_pct": -21.11, "MAE_180D_pct": -25.17, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 18940.0, "drawdown_after_peak_pct": -26.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "midcap_EPC_PF_recovery_watch_was_false_stage2_due_missing_cashflow_funding_order_quality_margin_bridge", "four_b_evidence_type": ["midcap_EPC_PF_premium", "bridge_missing", "minimal_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_midcap_EPC_PF_watch_without_cashflow_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_midcap_EPC_PF_watch_counts_without_cashflow_funding_order_quality_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_2021_2022_2023_CA_and_before_2025_CA", "same_entry_group_id": "R10L97_C30_016250_2024-02-19_18710", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP", "case_id": "R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B", "symbol": "046940", "company_name": "우원개발", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "sector": "local_civil_infrastructure_construction_recovery_event_premium", "primary_archetype": "local_civil_infra_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_4C_guardrail_stress_test | high_MAE_guardrail | PF_cashflow_bridge_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-30", "entry_date": "2024-01-30", "entry_price": 3540.0, "evidence_available_at_that_date": "local civil-infrastructure / construction recovery event premium without visible order-quality, funding repair, cash conversion, margin or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["local_civil_infra_event", "construction_recovery_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "minimal_MFE30", "persistent_MAE90", "cashflow_funding_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046940/2024.csv", "profile_path": "atlas/symbol_profiles/046/046940.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.14, "MFE_90D_pct": 0.14, "MFE_180D_pct": 0.14, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.24, "MAE_90D_pct": -22.6, "MAE_180D_pct": -22.6, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-30", "peak_price": 3545.0, "drawdown_after_peak_pct": -22.71, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_local_civil_infra_event_cap", "four_b_evidence_type": ["local_civil_infra_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_local_civil_infra_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_local_civil_infra_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2006_2008_2010_CA_and_name_history_candidates", "same_entry_group_id": "R10L97_C30_046940_2024-01-30_3540", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L97_C30_HJSC_2024_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_POSITIVE", "trigger_id": "R10L97_C30_HJSC_2024_STAGE2_ACTIONABLE_HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE", "symbol": "097230", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 55, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 50, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 64, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "heavy_civil_infra_order_cashflow_positive", "MFE_90D_pct": 25.96, "MAE_90D_pct": -10.15, "score_return_alignment_label": "heavy_civil_infra_order_cashflow_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L97_C30_SGCEC_2024_MIDCAP_EPC_PF_FALSE_STAGE2", "trigger_id": "R10L97_C30_SGCEC_2024_STAGE2_FALSE_POSITIVE_MIDCAP_EPC_PF_RECOVERY_WATCH", "symbol": "016250", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 60, "customer_quality_score": 20, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 15}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "midcap_EPC_PF_false_stage2", "MFE_90D_pct": 1.23, "MAE_90D_pct": -21.11, "score_return_alignment_label": "midcap_EPC_PF_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_midcap_EPC_PF_watch_counts_without_cashflow_funding_order_quality_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L97_C30_WOOWONDEV_2024_LOCAL_CIVIL_INFRA_EVENT_CAP_4B", "trigger_id": "R10L97_C30_WOOWONDEV_2024_STAGE4B_LOCAL_CIVIL_INFRA_EVENT_CAP", "symbol": "046940", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 15}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "local_civil_infra_event_cap_4B_guard", "MFE_90D_pct": 0.14, "MAE_90D_pct": -22.6, "score_return_alignment_label": "local_civil_infra_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_local_civil_infra_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "97", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "HEAVY_CIVIL_INFRA_ORDER_CASHFLOW_BRIDGE_VS_MIDCAP_EPC_PF_FALSE_STAGE2_AND_LOCAL_CIVIL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "PF_cashflow_bridge_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["heavy_civil_infra_order_cashflow_positive", "midcap_EPC_PF_false_stage2", "local_civil_infra_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C30 rows need explicit order quality, cashflow repair, funding capacity, balance-sheet safety, cost-to-complete visibility, margin or revision bridge before positive promotion.
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
completed_loop = 97
next_round = R11
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
