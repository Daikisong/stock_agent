# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA
deep_sub_archetype_id = C10_DEEP_DRAM_NAND_RECOVERY_EQUIPMENT_ORDER_REVENUE_BRIDGE_AND_LATE_CYCLE_4B_OVERHEAT
loop_objective = coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery
output_file = e2r_stock_web_v12_residual_round_R2_loop_109_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 6 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual tested here is narrower than the global rules: C10 often starts as a **memory-cycle beta signal**, but only some names turn that beta into equipment order/revenue/margin bridge. A cycle beta is like a harbor tide; it can lift every boat, but only boats with engines actually leave the harbor.

## 2. Round / Large Sector / Canonical Archetype Scope

- `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` maps to `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS`.
- This is not C06 HBM memory customer capacity and not C07 HBM equipment relative-strength by default. C10 is the broader DRAM/NAND recovery-to-equipment-order cycle.
- Boundary compression: HBM handler/test winners can enter C10 only when the historical trigger is memory recovery/order-cycle conversion rather than pure HBM equipment relative strength.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for selection:

```text
Priority 0 row count before this loop:
C02 = 10
C09 = 10
C14 = 11
C10 = 13
C06 = 17
C07 = 18
C11 = 18
C01 = 19
C28 = 28
```

The immediate prior local session outputs already filled C02, C09, and C14 once. Therefore this run selects C10, the next still-underfilled Priority 0 canonical archetype. Existing visible `docs/round` C10 standard files include loops 100, 101, and 108; selected loop is 109.

Duplicate hard gate:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
same_canonical_duplicate_found = false
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 6
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Manifest fields used:

```text
source_name = FinanceData/marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
```

## 5. Historical Eligibility Gate

All representative and overlay trigger rows below use stock-web tradable shards and have at least 180 forward trading days. Corporate-action profile windows do not overlap the selected 180D forward windows.

| symbol | company | profile path | selected years | corporate-action overlap in 180D window | status |
|---:|---|---|---|---|---|
| 036930 | 주성엔지니어링 | atlas/symbol_profiles/036/036930.json | 2023 | no | usable |
| 039030 | 이오테크닉스 | atlas/symbol_profiles/039/039030.json | 2023 | no | usable |
| 089030 | 테크윙 | atlas/symbol_profiles/089/089030.json | 2023-2024 | no | usable |
| 240810 | 원익IPS | atlas/symbol_profiles/240/240810.json | 2024 | no | usable |
| 095610 | 테스 | atlas/symbol_profiles/095/095610.json | 2024 | no | usable |
| 084370 | 유진테크 | atlas/symbol_profiles/084/084370.json | 2024 | no | usable |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| MEMORY_SUPPLY_CUT_EQUIPMENT_BETA_TO_ORDER_EXPECTATION | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | early supply discipline creates equipment-cycle beta, but order/margin bridge is not yet Green |
| LASER_PROCESS_EQUIPMENT_MEMORY_RECOVERY_WITH_HBM_OPTIONALITY | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | HBM optionality is present, but trigger date is broader memory recovery/order cycle |
| DRAM_PROFITABILITY_TURN_HBM_HANDLER_ORDER_CONVERSION | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | customer/order conversion after DRAM recovery bridges C10 and C07, but C10 is the chosen scope |
| MEMORY_EQUIPMENT_RECOVERY_PRICE_BETA_WITHOUT_ORDER_MARGIN_BRIDGE | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | false-positive branch: memory recovery narrative without confirmed order/margin/revision bridge |
| MEMORY_EQUIPMENT_FAST_RALLY_4B_WATCH | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | 4B overlay branch after cycle beta has already been pulled forward |

## 7. Case Selection Summary

| case_id | symbol | company | trigger | entry | role | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---|
| C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA | 036930 | 주성엔지니어링 | Stage2-Actionable | 2023-04-10 @ 17130 | positive | 74.55 | -13.78 | 121.83 | -13.78 | current_profile_missed_structural |
| C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY | 039030 | 이오테크닉스 | Stage2-Actionable | 2023-04-10 @ 86900 | positive | 103.34 | -9.21 | 110.47 | -9.21 | current_profile_too_late |
| C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY | 089030 | 테크윙 | Stage2-Actionable | 2023-10-27 @ 8400 | positive | 195.83 | -1.43 | 742.86 | -1.43 | current_profile_missed_structural |
| C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE | 240810 | 원익IPS | Stage3-Yellow | 2024-05-02 @ 36750 | counterexample | 9.66 | -24.35 | 9.66 | -43.13 | current_profile_false_positive |
| C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING | 095610 | 테스 | Stage3-Yellow | 2024-05-02 @ 24300 | counterexample | 14.4 | -34.65 | 14.4 | -46.13 | current_profile_false_positive |
| C10_R2_L109_084370_20240502_OVERHEAT_TO_4B | 084370 | 유진테크 | Stage3-Yellow | 2024-05-02 @ 53200 | counterexample | 12.78 | -33.55 | 12.78 | -43.05 | current_profile_4B_too_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 3
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 6
calibration_usable_trigger_count = 8
representative_trigger_count = 6
```

Positive pattern: memory recovery plus order/customer/revenue bridge produced convex MFE paths.

Counterexample pattern: memory recovery headline plus late-cycle price beta without fresh order/margin bridge produced low MFE and deep MAE.

## 9. Evidence Source Map

| case | evidence family | source status | use in scoring |
|---|---|---|---|
| 036930 / 039030 | Samsung 2023 memory production-cut cycle signal | public macro/customer-cycle proxy | Stage2-Actionable only, not Green |
| 089030 | SK hynix Q3 2023 DRAM recovery / HBM mix signal | public earnings-release proxy | Stage2-Actionable with customer-quality bridge |
| 240810 / 095610 / 084370 | 2024 memory equipment late-cycle rally without fresh bridge | source_proxy_only | counterexample / guardrail only |
| 089030 / 084370 4B overlays | positioning and valuation overheat after fast rally | source_proxy_only + price-path audit | 4B timing only, not promotion |

## 10. Price Data Source Map

| symbol | shard paths used | entry rows checked |
|---:|---|---|
| 036930 | atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv | 2023-04-10 |
| 039030 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv | 2023-04-10 |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2023.csv; 2024.csv | 2023-10-27; 2024-07-01 |
| 240810 | atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv | 2024-05-02 |
| 095610 | atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv | 2024-05-02 |
| 084370 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | 2024-05-02 |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | 4B local/full | aggregate_role |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|---|---|
| TRG_C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA | Stage2-Actionable | 036930 | 2023-04-10 @ 17130 | 17.34 | -13.78 | 74.55 | -13.78 | 121.83 | -13.78 | 2023-11-15 @ 38000 | n/a | representative |
| TRG_C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY | Stage2-Actionable | 039030 | 2023-04-10 @ 86900 | 5.41 | -9.21 | 103.34 | -9.21 | 110.47 | -9.21 | 2023-09-04 @ 182900 | n/a | representative |
| TRG_C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY | Stage2-Actionable | 089030 | 2023-10-27 @ 8400 | 20.12 | -1.43 | 195.83 | -1.43 | 742.86 | -1.43 | 2024-07-11 @ 70800 | n/a | representative |
| TRG_C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE | Stage3-Yellow | 240810 | 2024-05-02 @ 36750 | 5.58 | -8.84 | 9.66 | -24.35 | 9.66 | -43.13 | 2024-07-04 @ 40300 | n/a | representative |
| TRG_C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING | Stage3-Yellow | 095610 | 2024-05-02 @ 24300 | 4.12 | -9.05 | 14.4 | -34.65 | 14.4 | -46.13 | 2024-06-27 @ 27800 | n/a | representative |
| TRG_C10_R2_L109_084370_20240502_OVERHEAT_TO_4B | Stage3-Yellow | 084370 | 2024-05-02 @ 53200 | 12.78 | -12.22 | 12.78 | -33.55 | 12.78 | -43.05 | 2024-05-28 @ 60000 | n/a | representative |
| TRG_C10_R2_L109_089030_20240701_FULL_WINDOW_4B | Stage4B | 089030 | 2024-07-01 @ 57700 | 22.7 | -35.53 | 22.7 | -48.01 | 22.7 | -51.04 | 2024-07-11 @ 70800 | 0.79/0.79 | 4B_overlay_only |
| TRG_C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B | Stage4B | 084370 | 2024-05-02 @ 53200 | 12.78 | -12.22 | 12.78 | -33.55 | 12.78 | -43.05 | 2024-05-28 @ 60000 | 0.673/0.673 | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

All MFE/MAE values are computed from the entry close using stock-web raw/unadjusted tradable OHLC rows.

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
```

Key observation:

- Positive C10 entries had average representative MFE_180D of 325.05% and average MAE_180D of -8.14%.
- Counterexample C10 entries had average representative MFE_180D of 12.28% and average MAE_180D of -44.1%.

## 13. Current Calibrated Profile Stress Test

| case | P0 likely decision | realized path | verdict |
|---|---|---|---|
| 036930 | Stage2 watch, likely too conservative before order bridge | MFE180 +121.83%, MAE180 -13.78% | current_profile_missed_structural |
| 039030 | Stage2-Actionable, Green delayed by revision strictness | MFE180 +110.47%, MAE180 -9.21% | current_profile_too_late |
| 089030 | likely Stage2 watch until later HBM evidence | MFE180 +742.86%, MAE180 -1.43% | current_profile_missed_structural |
| 240810 | price/recovery beta could incorrectly clear Yellow | MFE180 +9.66%, MAE180 -43.13% | current_profile_false_positive |
| 095610 | memory capex beta could incorrectly clear Yellow | MFE180 +14.40%, MAE180 -46.13% | current_profile_false_positive |
| 084370 | post-rally Yellow needed 4B-watch overlay | MFE180 +12.78%, MAE180 -43.05% | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

C10 should not loosen Stage3-Green globally. The sharper distinction is:

```text
Stage2-Actionable = memory recovery cycle signal + early order/customer/revenue plausibility
Stage3-Yellow = above + company-specific order intake / revenue conversion / margin or revision bridge
Stage3-Green = above + confirmed revision visibility and low red-team risk
```

This loop finds two opposite residuals. First, early winners can be missed if all equipment-cycle signals are treated as generic beta. Second, late-cycle Yellow becomes dangerous if relative strength is allowed to substitute for order/margin bridge.

## 15. 4B Local vs Full-window Timing Audit

| overlay trigger | prior Stage2 price | 4B entry | full peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| 089030 / 2024-07-01 | 8400 | 57700 | 70800 | 0.790 | 0.790 | good_full_window_4B_timing |
| 084370 / 2024-05-02 | 39200 | 53200 | 60000 | 0.673 | 0.673 | local_4B_watch_success |

The 4B signal here is not a thesis-break. It is the amber lamp on the dashboard: the engine still runs, but temperature is high enough that a fresh promotion is no longer clean.

## 16. 4C Protection Audit

No hard 4C thesis-break row is proposed. The counterexamples did not require a cancelled order or accounting/trust break; they required earlier 4B-watch / Yellow blocking. Therefore:

```text
four_c_protection_label = not_applicable
hard_4c_confirmation = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = L2_memory_equipment_cycle_requires_order_revenue_bridge_before_yellow
confidence = medium
```

Sector-level wording:

> In L2 semicap names, a memory-price or supply-cut recovery signal may unlock Stage2-Actionable, but Stage3-Yellow should require at least one of verified order intake, customer conversion, shipment/revenue bridge, or margin/revision bridge.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
new_axis_proposed = C10_order_revenue_bridge_required_before_yellow_and_late_cycle_overheat_to_4B_watch
```

Proposed C10 compression:

```text
if memory_recovery_beta == true and order_revenue_margin_bridge == false:
    max_stage = Stage2-watch_or_Stage2-Actionable
    if post_rally_positioning_overheat == true:
        route_to = Stage4B-watch

if memory_recovery_beta == true and order_revenue_margin_bridge == true:
    allow Stage3-Yellow candidate
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---|
| e2r_2_1_stock_web_calibrated_proxy | P0 | current calibrated proxy; no C10-specific bridge split | 6 | 68.43 | -19.5 | 168.67 | -26.12 | 0.5 | mixed: misses structural winners and allows late-cycle false positives |
| e2r_2_0_baseline_reference | P0b | rollback reference; weaker global guard | 6 | 68.43 | -19.5 | 168.67 | -26.12 | 0.67 | worse: more Stage3 false positives |
| L2_sector_specific_candidate_profile | P1 | semicap sector candidate requiring order/revenue bridge after recovery beta | 6 | 124.57 | -8.14 | 325.05 | -8.14 | 0.33 | better separation but sector scope still broad |
| C10_canonical_archetype_candidate_profile | P2 | C10-specific bridge split: memory recovery beta + confirmed order/revenue bridge | 6 | 124.57 | -8.14 | 325.05 | -8.14 | 0.17 | best: separates structural conversion from price-only beta |
| C10_counterexample_guard_profile | P3 | late-cycle C10 guard: valuation/positioning overheat blocks fresh Yellow | 3 | 12.28 | -30.85 | 12.28 | -44.1 | 0.0 | guardrail candidate only; no global promotion |

## 20. Score-Return Alignment Matrix

| bucket | selected cases | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---|
| C10 positives with bridge | 3 | 124.57 | -8.14 | 325.05 | -8.14 | structural cycle conversion |
| C10 late-cycle beta without bridge | 3 | 12.28 | -30.85 | 12.28 | -44.1 | false positive / high-MAE guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA | 3 | 3 | 2 | 0 | 6 | 0 | 8 | 6 | 6 | true | true | 11 rows to 30 by original index count; lower if local outputs are later committed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [missed_structural_memory_equipment_order_conversion, late_cycle_price_only_stage3_false_positive, 4B_too_late_after_fast_semicap_rally]
new_axis_proposed: C10_order_revenue_bridge_required_before_yellow_and_late_cycle_overheat_to_4B_watch
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage2_actionable_evidence_bonus
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web tradable raw OHLC rows for entry dates and 30/90/180D windows.
- symbol profile corporate-action candidate dates are outside selected 180D windows.
- canonical trigger labels are limited to Stage2-Actionable, Stage3-Yellow, and Stage4B.

Not validated:

- No live watchlist or present-day candidate scan.
- No production scoring code opened or patched.
- Some non-price evidence rows are source-proxy-only and should be URL-repaired before high-confidence promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_revenue_bridge_required_before_yellow,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Memory recovery beta alone created false positives; winners showed order/revenue/customer bridge.","Cuts 3 late-cycle false positives while preserving 3 structural positives.","TRG_C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA|TRG_C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY|TRG_C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY",6,6,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C10_late_cycle_positioning_overheat_to_4b_watch,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"Fast semicap rally without incremental order/margin bridge should be 4B-watch, not fresh Yellow.","Flags 084370/089030 overlay rows before deep drawdown.","TRG_C10_R2_L109_089030_20240701_FULL_WINDOW_4B|TRG_C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B",8,6,3,medium,guardrail_shadow_only,"not production; 4B overlay calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Deposition/equipment beta moved early; C10 should recognize supply-cut cycle reversal as watch-to-actionable only when later order/revenue bridge appears."}
{"row_type":"case","case_id":"C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"High-MFE winner, but the useful rule is not global Green loosening; it is C10 watch/actionable with later order-revenue bridge requirement."}
{"row_type":"case","case_id":"C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","symbol":"089030","company_name":"테크윙","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"This is the cleanest C10/C07 boundary case: memory recovery alone is insufficient, but customer/order conversion made the price path unusually asymmetric."}
{"row_type":"case","case_id":"C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_mae_or_low_mfe","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Price-only memory equipment beta should remain watch/4B-risk unless order intake and margin/revision bridge are visible."}
{"row_type":"case","case_id":"C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","symbol":"095610","company_name":"테스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_mae_or_low_mfe","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C10 late-cycle promotion needs a negative override when equipment beta leads order confirmation by too much."}
{"row_type":"case","case_id":"C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","case_type":"4B_too_early_or_late_review","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_high_mae_or_low_mfe","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Useful for local-vs-full 4B: not a hard thesis break, but a guardrail that prevents fresh Yellow at the wrong side of the cycle."}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","case_id":"C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","symbol":"036930","company_name":"주성엔지니어링","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-07","entry_date":"2023-04-10","entry_price":17130.0,"evidence_available_at_that_date":"Samsung memory production-cut acknowledgement and memory inventory downcycle repair narrative were public before the next KRX session; company-specific confirmed order bridge was still incomplete.","evidence_source":"public_memory_cycle_proxy:SAMSUNG_2023Q1_PRELIM_PRODUCTION_CUT; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility_pending","margin_bridge_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036930/2023.csv","profile_path":"atlas/symbol_profiles/036/036930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.34,"MFE_90D_pct":74.55,"MFE_180D_pct":121.83,"MFE_1Y_pct":141.97,"MFE_2Y_pct":153.36,"MAE_30D_pct":-13.78,"MAE_90D_pct":-13.78,"MAE_180D_pct":-13.78,"MAE_1Y_pct":-13.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-11-15","peak_price":38000.0,"drawdown_after_peak_pct":-18.03,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_equipment_beta_positive_but_requires_later_order_margin_bridge","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_036930_2023-04-10_17130","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","case_id":"C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-07","entry_date":"2023-04-10","entry_price":86900.0,"evidence_available_at_that_date":"Memory supply discipline plus early AI/HBM equipment optionality was public; company-specific revision confirmation was not yet a Green-quality bridge.","evidence_source":"public_memory_cycle_proxy:SAMSUNG_2023Q1_PRELIM_PRODUCTION_CUT; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["margin_bridge_pending","confirmed_revision_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.41,"MFE_90D_pct":103.34,"MFE_180D_pct":110.47,"MFE_1Y_pct":223.36,"MFE_2Y_pct":223.36,"MAE_30D_pct":-9.21,"MAE_90D_pct":-9.21,"MAE_180D_pct":-9.21,"MAE_1Y_pct":-9.21,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-09-04","peak_price":182900.0,"drawdown_after_peak_pct":-28.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"laser_equipment_memory_recovery_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_039030_2023-04-10_86900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","case_id":"C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","symbol":"089030","company_name":"테크윙","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-26","entry_date":"2023-10-27","entry_price":8400.0,"evidence_available_at_that_date":"SK hynix Q3 2023 showed DRAM-side recovery and HBM product mix momentum; for equipment suppliers this was a cycle-to-order conversion watch, not pure price chase.","evidence_source":"SK hynix Q3 2023 earnings release / public media summary; source_proxy_only=false","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion_pending","confirmed_revision_pending"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2023.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.12,"MFE_90D_pct":195.83,"MFE_180D_pct":742.86,"MFE_1Y_pct":742.86,"MFE_2Y_pct":742.86,"MAE_30D_pct":-1.43,"MAE_90D_pct":-1.43,"MAE_180D_pct":-1.43,"MAE_1Y_pct":-1.43,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-31.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"hbm_handler_cycle_conversion_major_positive","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_089030_2023-10-27_8400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","case_id":"C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","symbol":"240810","company_name":"원익IPS","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":36750.0,"evidence_available_at_that_date":"After the 2024 semicap rally, market memory-cycle optimism was visible but fresh company-specific order, margin, or revision bridge was not strong enough for Yellow promotion.","evidence_source":"market_cycle_proxy:memory_recovery_equipment_beta; source_proxy_only=true","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["confirmed_revision_missing","margin_bridge_missing","durable_customer_confirmation_missing"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv","profile_path":"atlas/symbol_profiles/240/240810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.58,"MFE_90D_pct":9.66,"MFE_180D_pct":9.66,"MFE_1Y_pct":9.66,"MFE_2Y_pct":null,"MAE_30D_pct":-8.84,"MAE_90D_pct":-24.35,"MAE_180D_pct":-43.13,"MAE_1Y_pct":-43.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-04","peak_price":40300.0,"drawdown_after_peak_pct":-48.14,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_cycle_memory_equipment_false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_240810_2024-05-02_36750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","case_id":"C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","symbol":"095610","company_name":"테스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":24300.0,"evidence_available_at_that_date":"Memory recovery narrative was public, but order-intake, margin, and revision bridges were not clean enough to distinguish beta from structural rerating.","evidence_source":"market_cycle_proxy:memory_capex_recovery; source_proxy_only=true","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["order_intake_quality_missing","margin_bridge_missing","confirmed_revision_missing"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv","profile_path":"atlas/symbol_profiles/095/095610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.12,"MFE_90D_pct":14.4,"MFE_180D_pct":14.4,"MFE_1Y_pct":14.4,"MFE_2Y_pct":null,"MAE_30D_pct":-9.05,"MAE_90D_pct":-34.65,"MAE_180D_pct":-46.13,"MAE_1Y_pct":-46.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":27800.0,"drawdown_after_peak_pct":-52.91,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["price_only_local_peak","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"memory_recovery_beta_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_095610_2024-05-02_24300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","case_id":"C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":53200.0,"evidence_available_at_that_date":"Equipment rally had already front-run the memory recovery; lack of incremental order/margin evidence turned Yellow into 4B-watch rather than fresh promotion.","evidence_source":"market_cycle_proxy:semicap_rally_positioning_overheat; source_proxy_only=true","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["fresh_revision_missing","margin_bridge_missing"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.78,"MFE_90D_pct":12.78,"MFE_180D_pct":12.78,"MFE_1Y_pct":12.78,"MFE_2Y_pct":null,"MAE_30D_pct":-12.22,"MAE_90D_pct":-33.55,"MAE_180D_pct":-43.05,"MAE_1Y_pct":-43.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-49.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"fast_rally_yellow_should_have_been_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_084370_2024-05-02_53200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_089030_20240701_FULL_WINDOW_4B","case_id":"C10_R2_L109_089030_20240701_FULL_WINDOW_4B","symbol":"089030","company_name":"테크윙","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-07-01","entry_date":"2024-07-01","entry_price":57700.0,"evidence_available_at_that_date":"After a multi-bagger move from the prior C10 entry, forward risk/reward turned into full-window 4B overlay; non-price thesis remained alive but upside was compressed by positioning.","evidence_source":"price_path_plus_positioning_proxy; non_price_4b_evidence=positioning_overheat; source_proxy_only=true","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.7,"MFE_90D_pct":22.7,"MFE_180D_pct":22.7,"MFE_1Y_pct":22.7,"MFE_2Y_pct":null,"MAE_30D_pct":-35.53,"MAE_90D_pct":-48.01,"MAE_180D_pct":-51.04,"MAE_1Y_pct":-54.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-60.1,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.79,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"good_full_window_4B_timing_after_structural_winner","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_089030_2024-07-01_57700","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_overlay_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TRG_C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B","case_id":"C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_ORDER_CYCLE_REVERSAL_VS_PRICE_ONLY_CAPEX_BETA","sector":"AI/semiconductor/electronics","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":53200.0,"evidence_available_at_that_date":"Local 4B watch was warranted because equipment-cycle price had front-run confirmed order/margin bridge; subsequent MAE confirms drawdown guard value.","evidence_source":"price_path_plus_positioning_proxy; source_proxy_only=true","stage2_evidence_fields":["relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":["confirmed_revision_missing","margin_bridge_missing"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.78,"MFE_90D_pct":12.78,"MFE_180D_pct":12.78,"MFE_1Y_pct":12.78,"MFE_2Y_pct":null,"MAE_30D_pct":-12.22,"MAE_90D_pct":-33.55,"MAE_180D_pct":-43.05,"MAE_1Y_pct":-43.05,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-49.5,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.673,"four_b_full_window_peak_proximity":0.673,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"local_4B_watch_success_high_MAE_after_peak","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_084370_2024-05-02_53200","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_4B_overlay_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","trigger_id":"TRG_C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":74.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_after":74.0,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":74.55,"MAE_90D_pct":-13.78,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","trigger_id":"TRG_C10_R2_L109_036930_20230410_MEMORY_CUT_EQUIPMENT_BETA","symbol":"036930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":74.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":58,"margin_bridge_score":55,"revision_score":54,"relative_strength_score":72,"customer_quality_score":70,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":66,"order_intake_quality_score":62,"positioning_overheat_score":25},"weighted_score_after":79.0,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":74.55,"MAE_90D_pct":-13.78,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","trigger_id":"TRG_C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_after":76.0,"stage_label_after":"Stage2-Actionable","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":103.34,"MAE_90D_pct":-9.21,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","trigger_id":"TRG_C10_R2_L109_039030_20230410_LASER_MEMORY_RECOVERY","symbol":"039030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":58,"margin_bridge_score":55,"revision_score":54,"relative_strength_score":72,"customer_quality_score":70,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":66,"order_intake_quality_score":62,"positioning_overheat_score":25},"weighted_score_after":81.0,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":103.34,"MAE_90D_pct":-9.21,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","trigger_id":"TRG_C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":73.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_after":73.0,"stage_label_after":"Stage2","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":195.83,"MAE_90D_pct":-1.43,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","trigger_id":"TRG_C10_R2_L109_089030_20231027_HBM_HANDLER_MEMORY_RECOVERY","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":50,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":72,"customer_quality_score":62,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":58,"order_intake_quality_score":50,"positioning_overheat_score":25},"weighted_score_before":73.0,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":55,"backlog_visibility_score":58,"margin_bridge_score":55,"revision_score":54,"relative_strength_score":72,"customer_quality_score":70,"policy_or_regulatory_score":25,"valuation_repricing_score":65,"execution_risk_score":38,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":10,"accounting_trust_risk_score":15,"capacity_or_shipment_score":66,"order_intake_quality_score":62,"positioning_overheat_score":25},"weighted_score_after":82.0,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":195.83,"MAE_90D_pct":-1.43,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","trigger_id":"TRG_C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":9.66,"MAE_90D_pct":-24.35,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","trigger_id":"TRG_C10_R2_L109_240810_20240502_LATE_CYCLE_FALSE_POSITIVE","symbol":"240810","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":22,"revision_score":24,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":88},"weighted_score_after":66.0,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":9.66,"MAE_90D_pct":-24.35,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","trigger_id":"TRG_C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_after":75.5,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":14.4,"MAE_90D_pct":-34.65,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","trigger_id":"TRG_C10_R2_L109_095610_20240502_ORDER_BRIDGE_MISSING","symbol":"095610","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":22,"revision_score":24,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":88},"weighted_score_after":64.5,"stage_label_after":"Stage2","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":14.4,"MAE_90D_pct":-34.65,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","trigger_id":"TRG_C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_after":80.0,"stage_label_after":"Stage3-Yellow","changed_components":[],"component_delta_explanation":"Current calibrated proxy before C10-specific bridge/overheat adjustment.","MFE_90D_pct":12.78,"MAE_90D_pct":-33.55,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C10_canonical_shadow_profile","case_id":"C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","trigger_id":"TRG_C10_R2_L109_084370_20240502_OVERHEAT_TO_4B","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":72,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":70},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":22,"revision_score":24,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":88},"weighted_score_after":68.0,"stage_label_after":"Stage4B-watch","changed_components":["margin_bridge_score","revision_score","order_intake_quality_score","positioning_overheat_score"],"component_delta_explanation":"C10 shadow profile rewards memory equipment recovery only when order/revenue bridge improves, and subtracts late-cycle price-only overheat.","MFE_90D_pct":12.78,"MAE_90D_pct":-33.55,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C10_counterexample_guard_profile","case_id":"C10_R2_L109_089030_20240701_FULL_WINDOW_4B","trigger_id":"TRG_C10_R2_L109_089030_20240701_FULL_WINDOW_4B","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":80,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":90},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":22,"revision_score":24,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":80,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":90},"weighted_score_after":72.0,"stage_label_after":"Stage4B","changed_components":["positioning_overheat_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Counterexample guard routes fast-rally memory equipment names to 4B-watch when order/margin bridge lags price.","MFE_90D_pct":22.7,"MAE_90D_pct":-48.01,"score_return_alignment_label":"aligned_4B_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"C10_counterexample_guard_profile","case_id":"C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B","trigger_id":"TRG_C10_R2_L109_084370_20240502_VALUATION_POSITIONING_4B","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":28,"revision_score":30,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":80,"execution_risk_score":62,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":90},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":22,"revision_score":24,"relative_strength_score":76,"customer_quality_score":42,"policy_or_regulatory_score":20,"valuation_repricing_score":80,"execution_risk_score":76,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":15,"accounting_trust_risk_score":15,"capacity_or_shipment_score":40,"order_intake_quality_score":28,"positioning_overheat_score":90},"weighted_score_after":68.0,"stage_label_after":"Stage4B-watch","changed_components":["positioning_overheat_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Counterexample guard routes fast-rally memory equipment names to 4B-watch when order/margin bridge lags price.","MFE_90D_pct":12.78,"MAE_90D_pct":-33.55,"score_return_alignment_label":"aligned_4B_guard","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus","stage3_yellow_total_min"],"residual_error_types_found":["missed_structural_memory_equipment_order_conversion","late_cycle_price_only_stage3_false_positive","4B_too_late_after_fast_semicap_rally"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{ticker}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{ticker}.json.

### Rules
- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output
- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R2
completed_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web profile examples used: atlas/symbol_profiles/036/036930.json; atlas/symbol_profiles/039/039030.json; atlas/symbol_profiles/089/089030.json; atlas/symbol_profiles/240/240810.json; atlas/symbol_profiles/095/095610.json; atlas/symbol_profiles/084/084370.json

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 8
calibration_usable_trigger_count: 8
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```
