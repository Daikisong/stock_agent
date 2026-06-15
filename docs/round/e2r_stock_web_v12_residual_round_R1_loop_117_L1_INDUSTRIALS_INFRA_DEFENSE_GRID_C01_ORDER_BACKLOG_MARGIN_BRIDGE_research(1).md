# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
generated_at_kst: "2026-06-13"
main_execution_prompt: "docs/core/e2r_v12_prompt_round_scheduler_corrected.txt"
no_repeat_index: "docs/core/V12_Research_No_Repeat_Index.md"
selected_round: "R1"
selected_loop: 117
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C01_ORDER_BACKLOG_MARGIN_BRIDGE"
fine_archetype_id: "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE"
deep_sub_archetype_id: "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE"
loop_objective: "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 7 new independent C01 cases, 3 counterexamples, and 6 residual errors for R1/L1. It is not a live watchlist and contains no production scoring patch.

## 1. Current Calibrated Profile Assumption
- Current proxy: `e2r_2_1_stock_web_calibrated_proxy`.
- Rollback reference: `e2r_2_0_baseline_reference`.
- Existing global axes are treated as already applied: `stage2_required_bridge`, `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, and `hard_4c_thesis_break_routes_to_4c`.
- This file proposes only a C01/L1 shadow rule candidate, not a global production change.

## 2. Round / Large Sector / Canonical Archetype Scope
- selected_round: `R1`
- large_sector_id: `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`
- canonical_archetype_id: `C01_ORDER_BACKLOG_MARGIN_BRIDGE`
- fine_archetype_id: `C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE`
- deep_sub_archetype_id: `C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE`

## 3. Previous Coverage / Duplicate Avoidance Check
Published No-Repeat Index shows C01 at 19 representative rows, below the 50-row practical calibration band. Local same-session C01 loops 115 and 116 added shipbuilding, ship-engine, offshore-wind and supplier bridge rows, so this loop intentionally avoids those symbol groups: `009540`, `010140`, `010620`, `017960`, `071970`, `082740`, `100090`, `329180`, `042660`, `042670`, `075580`, `077970`, `097230`, `112610`, `241560`.

Hard duplicate key:
```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected new symbols: `064350`, `034020`, `100840`, `014620`, `013030`, `105740`, `086670`.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
|---|---|
| source | `Songdaiki/stock-web` |
| upstream_source | `FinanceData/marcap` |
| manifest_max_date | `2026-02-20` |
| price_basis | `tradable_raw` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |

All MFE/MAE values below were computed from the downloaded stock-web 2024/2025 tradable shards. Windows use entry-date close as entry_price and high/low paths through 30/90/180 trading days.

## 5. Historical Eligibility Gate
| symbol | entry_date | forward_180D | corporate action window | usable |
|---:|---|---:|---|---|
| 064350 | 2024-07-01 | 180 | clean or candidate outside selected window | true |
| 034020 | 2024-05-02 | 180 | clean or candidate outside selected window | true |
| 100840 | 2024-05-02 | 180 | clean or candidate outside selected window | true |
| 014620 | 2024-05-02 | 180 | clean or candidate outside selected window | true |
| 013030 | 2024-07-01 | 180 | clean or candidate outside selected window | true |
| 105740 | 2024-07-01 | 180 | clean or candidate outside selected window | true |
| 086670 | 2024-05-02 | 180 | clean or candidate outside selected window | true |

## 6. Canonical Archetype Compression Map
| fine/deep route | canonical compression | decision |
|---|---|---|
| rail/defense backlog revenue bridge | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | allowed as C01 only when evidence is order-to-margin conversion, not defense-framework headline |
| power equipment backlog mix bridge | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | allowed as C01 when margin/FCF conversion is the tested variable; policy-only nuclear optionality belongs to C04 |
| LNG/HRSG/air-cooler orderbook leverage | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | allowed as industrial orderbook operating leverage |
| industrial fitting/valve proxy | `C01_ORDER_BACKLOG_MARGIN_BRIDGE` | positive only with order + margin/FCF bridge; otherwise local 4B watch |

## 7. Case Selection Summary
| case_id | symbol | company | trigger_type | role | outcome | entry_price | MFE_90D | MAE_90D | current profile verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C01-R1-L117-01 | 064350 | 현대로템 | Stage2-Actionable | structural_success | positive | 40100 | 69.58% | -6.61% | current_profile_missed_structural |
| C01-R1-L117-02 | 034020 | 두산에너빌리티 | Stage2-Actionable | structural_success | positive | 16500 | 51.52% | -8.18% | current_profile_correct_but_scope_ambiguous_between_C01_and_C04 |
| C01-R1-L117-03 | 100840 | SNT에너지 | Stage3-Yellow | missed_structural | positive | 10420 | 54.51% | -9.31% | current_profile_missed_structural |
| C01-R1-L117-04 | 014620 | 성광벤드 | Stage2-Actionable | structural_success | positive | 11350 | 48.90% | -6.26% | current_profile_missed_structural |
| C01-R1-L117-05 | 013030 | 하이록코리아 | Stage4B | 4B_too_early | counterexample | 27600 | 6.34% | -18.84% | current_profile_false_positive |
| C01-R1-L117-06 | 105740 | 디케이락 | Stage4B | failed_rerating | counterexample | 9350 | 10.16% | -28.45% | current_profile_false_positive |
| C01-R1-L117-07 | 086670 | 비엠티 | Stage4B | failed_rerating | counterexample | 13530 | 5.69% | -33.70% | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
| bucket | count | symbols |
|---|---:|---|
| positive structural / missed structural | 4 | 064350, 034020, 100840, 014620 |
| counterexample / failed rerating / 4B watch | 3 | 013030, 105740, 086670 |
| 4B local-watch cases | 3 | 013030, 105740, 086670 |
| 4C cases | 0 | none in this loop |

## 9. Evidence Source Map
| symbol | evidence family | source proxy only | evidence URL pending | source |
|---:|---|---:|---:|---|
| 064350 | rail_defense_order_backlog_margin_bridge | false | false | BizWatch / KIS Rating / company-public performance-backlog sources |
| 034020 | energy_equipment_backlog_mix_profitability_bridge | true | true | company IR / public research describing backlog mix and profitability route |
| 100840 | lng_air_cooler_hrsg_backlog_operating_leverage | true | true | SNT Energy research and news on order backlog and operating leverage |
| 014620 | industrial_fitting_order_recovery_margin_bridge | true | true | sell-side/KRX materials on fitting order recovery and margin bridge |
| 013030 | fitting_quality_label_without_incremental_order_margin_bridge | false | false | company finance page and 2024 research noting steady but not explosive growth |
| 105740 | fitting_valve_order_headline_without_margin_conversion | false | false | KRX quarterly report / NewsPim note on 2024 margin weakness |
| 086670 | fitting_valve_diversification_without_margin_bridge | false | false | KIRS/company report on fitting/valve margin decline |

## 10. Price Data Source Map
| symbol | shard path | profile path |
|---:|---|---|
| 064350 | `atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv` + `2025.csv` | `atlas/symbol_profiles/064/064350.json` |
| 034020 | `atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv` + `2025.csv` | `atlas/symbol_profiles/034/034020.json` |
| 100840 | `atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv` + `2025.csv` | `atlas/symbol_profiles/100/100840.json` |
| 014620 | `atlas/ohlcv_tradable_by_symbol_year/014/014620/2024.csv` + `2025.csv` | `atlas/symbol_profiles/014/014620.json` |
| 013030 | `atlas/ohlcv_tradable_by_symbol_year/013/013030/2024.csv` + `2025.csv` | `atlas/symbol_profiles/013/013030.json` |
| 105740 | `atlas/ohlcv_tradable_by_symbol_year/105/105740/2024.csv` + `2025.csv` | `atlas/symbol_profiles/105/105740.json` |
| 086670 | `atlas/ohlcv_tradable_by_symbol_year/086/086670/2024.csv` + `2025.csv` | `atlas/symbol_profiles/086/086670.json` |

## 11. Case-by-Case Trigger Grid
### C01-R1-L117-01 — 현대로템 (064350)
- Trigger: `Stage2-Actionable` on `2024-07-01`, entry close `40100` on `2024-07-01`.
- Evidence route: `rail_defense_order_backlog_margin_bridge`.
- Profile verdict: `current_profile_missed_structural` — missed_structural_if_rail_defense_backlog_conversion_is_not_compressed_into_C01.

### C01-R1-L117-02 — 두산에너빌리티 (034020)
- Trigger: `Stage2-Actionable` on `2024-05-02`, entry close `16500` on `2024-05-02`.
- Evidence route: `energy_equipment_backlog_mix_profitability_bridge`.
- Profile verdict: `current_profile_correct_but_scope_ambiguous_between_C01_and_C04` — scope_ambiguity_if_nuclear_policy_optionalities_substitute_for_order_margin_bridge.

### C01-R1-L117-03 — SNT에너지 (100840)
- Trigger: `Stage3-Yellow` on `2024-05-02`, entry close `10420` on `2024-05-02`.
- Evidence route: `lng_air_cooler_hrsg_backlog_operating_leverage`.
- Profile verdict: `current_profile_missed_structural` — too_conservative_if_small_cap_orderbook_operating_leverage_is_not_allowed_to_reach_yellow.

### C01-R1-L117-04 — 성광벤드 (014620)
- Trigger: `Stage2-Actionable` on `2024-05-02`, entry close `11350` on `2024-05-02`.
- Evidence route: `industrial_fitting_order_recovery_margin_bridge`.
- Profile verdict: `current_profile_missed_structural` — missed_structural_if_fitting_supplier_order_recovery_is_filtered_as_generic_commodity_beta.

### C01-R1-L117-05 — 하이록코리아 (013030)
- Trigger: `Stage4B` on `2024-07-01`, entry close `27600` on `2024-07-01`.
- Evidence route: `fitting_quality_label_without_incremental_order_margin_bridge`.
- Profile verdict: `current_profile_false_positive` — false_positive_if_high_quality_fitting_business_is_promoted_without_incremental_order_or_revision_bridge.

### C01-R1-L117-06 — 디케이락 (105740)
- Trigger: `Stage4B` on `2024-07-01`, entry close `9350` on `2024-07-01`.
- Evidence route: `fitting_valve_order_headline_without_margin_conversion`.
- Profile verdict: `current_profile_false_positive` — false_positive_if_single_order_headline_is_used_despite_export_margin_and_revenue_weakness.

### C01-R1-L117-07 — 비엠티 (086670)
- Trigger: `Stage4B` on `2024-05-02`, entry close `13530` on `2024-05-02`.
- Evidence route: `fitting_valve_diversification_without_margin_bridge`.
- Profile verdict: `current_profile_false_positive` — false_positive_if_diversified_fitting_valve_exposure_is_treated_as_backlog_margin_bridge.

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | DD after peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R1L117-C01-001 | 064350 | 2024-07-01 | 40100 | 30.42% | -6.61% | 69.58% | -6.61% | 191.27% | -6.61% | 2025-03-19 | 116800 | -14.98% |
| R1L117-C01-002 | 034020 | 2024-05-02 | 16500 | 33.33% | -1.27% | 51.52% | -8.18% | 52.42% | -8.18% | 2025-01-24 | 25150 | -8.15% |
| R1L117-C01-003 | 100840 | 2024-05-02 | 10420 | 38.00% | -9.31% | 54.51% | -9.31% | 197.50% | -9.31% | 2025-01-24 | 31000 | -12.74% |
| R1L117-C01-004 | 014620 | 2024-05-02 | 11350 | 10.75% | -6.26% | 48.90% | -6.26% | 186.34% | -6.26% | 2025-01-17 | 32500 | -13.23% |
| R1L117-C01-005 | 013030 | 2024-07-01 | 27600 | 6.34% | -15.22% | 6.34% | -18.84% | 17.57% | -18.84% | 2025-01-22 | 32450 | -19.57% |
| R1L117-C01-006 | 105740 | 2024-07-01 | 9350 | 10.16% | -28.45% | 10.16% | -28.45% | 10.16% | -35.61% | 2024-07-29 | 10300 | -41.55% |
| R1L117-C01-007 | 086670 | 2024-05-02 | 13530 | 5.69% | -11.46% | 5.69% | -33.70% | 5.69% | -49.00% | 2024-05-08 | 14300 | -51.75% |

## 13. Current Calibrated Profile Stress Test
- C01 positives show that pure backlog visibility is not enough, but backlog plus margin/FCF bridge can still be too conservative if supplier or small-cap industrial order conversion is ignored.
- C01 counterexamples show the opposite: industrial fitting/valve label, customer breadth, or one-off order headlines should not unlock Yellow when 90D MAE is severe and margin bridge is absent.
- Residual error count: `6` out of `7`. The errors are scope-specific, not global threshold failures.

## 14. Stage2 / Yellow / Green Comparison
| profile | Stage2/Yellow behavior | Green behavior | verdict |
|---|---|---|---|
| current P0 | catches some large-cap backlog bridges but misses supplier conversion and may over-score component proxy labels | Green remains strict; not challenged here | keep global Green strictness |
| proposed C01 shadow | requires backlog + margin/FCF bridge before Yellow; allows supplier conversion only if revenue/margin bridge is visible | no Green loosening | better C01 separation |

## 15. 4B Local vs Full-window Timing Audit
| symbol | 4B evidence | local/full verdict | price path support |
|---:|---|---|---|
| 013030 | margin/order acceleration absent, fitting quality label only | local 4B watch | MFE90 6.34% vs MAE90 -18.84% |
| 105740 | order headline without export-margin conversion | local 4B watch | MFE180 10.16% vs MAE180 -35.61% |
| 086670 | diversification narrative without margin bridge | local 4B watch | MFE180 5.69% vs MAE180 -49.00% |

## 16. 4C Protection Audit
No hard Stage4C trigger is promoted in this loop. The counterexamples remain `Stage4B local watch` because the failure mode is weak conversion evidence rather than confirmed contract cancellation, accounting break, forced liquidation, or thesis evidence broken.

## 17. Sector-Specific Rule Candidate
Rule scope: `sector_specific`. For L1 industrial backlog cases, Stage2-Actionable can recognize supplier conversion earlier than mega-cap-only logic, but Yellow requires at least one of: entity-level OPM bridge, confirmed revenue conversion, FCF/working-capital improvement, or repeated order conversion. Component labels without those fields route to local 4B watch.

## 18. Canonical-Archetype Rule Candidate
Rule scope: `canonical_archetype_specific`. Proposed C01 axis: `C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_component_order_proxy_to_local_4B_watch`.

## 19. Before / After Backtest Comparison
| profile_id | scope | hypothesis | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated profile | 7 | 35.24% | -15.91% | 94.42% | -19.12% | 6/7 residual errors: misses supplier positives and over-promotes weak component proxies |
| P0b | e2r_2_0_baseline_reference | pre-stock-web baseline | 7 | 35.24% | -15.91% | 94.42% | -19.12% | more price-chasing false positives; weaker 4B watch separation |
| P1 | L1 sector shadow profile | L1 backlog conversion guard | 7 | 56.13% | -27.0% | 156.88% | -34.48% | better separation between real backlog conversion and proxy labels |
| P2 | C01 canonical shadow profile | C01 verified backlog-margin-FCF bridge | 7 | 56.13% | -27.0% | 156.88% | -34.48% | best scope; keeps positives while demoting low-bridge fittings |
| P3 | counterexample guard profile | component-order proxy 4B watch | 3 | 7.4% | -27.0% | 11.14% | -34.48% | strong guardrail alignment for 013030/105740/086670 |

## 20. Score-Return Alignment Matrix
| symbol | score_before | score_after | stage_after | MFE90/MAE90 | alignment |
|---:|---:|---:|---|---|---|
| 064350 | 79 | 83 | Stage3-Yellow guarded | 69.58% / -6.61% | positive_alignment |
| 034020 | 77 | 81 | Stage3-Yellow guarded | 51.52% / -8.18% | positive_alignment |
| 100840 | 84 | 89 | Stage3-Green watch but not production Green | 54.51% / -9.31% | positive_alignment |
| 014620 | 72 | 80 | Stage3-Yellow guarded | 48.90% / -6.26% | positive_alignment |
| 013030 | 68 | 58 | Stage4B local watch | 6.34% / -18.84% | guardrail_alignment |
| 105740 | 62 | 47 | Stage4B local watch | 10.16% / -28.45% | guardrail_alignment |
| 086670 | 58 | 40 | Stage4B local watch | 5.69% / -33.70% | guardrail_alignment |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE | 4 | 3 | 3 | 0 | 7 | 0 | 7 | 7 | 6 | true | true | C01 base 19 + local loop115/116 15 + loop117 7 = about 41; still about 9 short of 50 |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 7
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 7
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 7
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: missed_structural_supplier_bridge, false_positive_component_order_proxy_without_margin_bridge, scope_ambiguity_C01_vs_C04_or_C03
new_axis_proposed: C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_component_order_proxy_to_local_4B_watch
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min, stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope
Validated: historical stock-web price path, trigger entry dates, 30/90/180D MFE and MAE, large-sector/canonical consistency, same-entry duplicate avoidance, and C01-specific residual rule fit. Not validated: live investability, current valuation, broker API routing, production scoring change, or any present-day recommendation.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 positives need backlog plus margin/FCF bridge; weak component proxies need 4B watch","avg positive MFE90 56.13% vs counterexample avg MAE90 -27.0%","R1L117-C01-001|R1L117-C01-002|R1L117-C01-003|R1L117-C01-004|R1L117-C01-005|R1L117-C01-006|R1L117-C01-007",7,7,3,medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C01_component_order_proxy_to_local_4B_watch,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Fitting/valve proxy label without margin bridge produced severe MAE","013030/105740/086670 guardrail alignment","R1L117-C01-005|R1L117-C01-006|R1L117-C01-007",3,3,3,medium,guardrail_shadow_only,"4B overlay only"
```

## 25. Machine-Readable Rows
```jsonl
{"calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "manifest_max_date": "2026-02-20", "manifest_path": "atlas/manifest.json", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "row_type": "price_source_validation", "schema_path": "atlas/schema.json", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "universe_path": "atlas/universe/all_symbols.csv", "validation_status": "usable_for_historical_calibration"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-01", "case_type": "structural_success", "company_name": "현대로템", "current_profile_verdict": "current_profile_missed_structural", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "missed_structural_if_rail_defense_backlog_conversion_is_not_compressed_into_C01", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "positive_alignment", "symbol": "064350"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-02", "case_type": "structural_success", "company_name": "두산에너빌리티", "current_profile_verdict": "current_profile_correct_but_scope_ambiguous_between_C01_and_C04", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "scope_ambiguity_if_nuclear_policy_optionalities_substitute_for_order_margin_bridge", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "positive_alignment", "symbol": "034020"}
{"best_trigger": "Stage3-Yellow", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-03", "case_type": "missed_structural", "company_name": "SNT에너지", "current_profile_verdict": "current_profile_missed_structural", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "too_conservative_if_small_cap_orderbook_operating_leverage_is_not_allowed_to_reach_yellow", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "positive_alignment", "symbol": "100840"}
{"best_trigger": "Stage2-Actionable", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-04", "case_type": "structural_success", "company_name": "성광벤드", "current_profile_verdict": "current_profile_missed_structural", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "missed_structural_if_fitting_supplier_order_recovery_is_filtered_as_generic_commodity_beta", "positive_or_counterexample": "positive", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "positive_alignment", "symbol": "014620"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-05", "case_type": "4B_too_early", "company_name": "하이록코리아", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "false_positive_if_high_quality_fitting_business_is_promoted_without_incremental_order_or_revision_bridge", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "guardrail_alignment", "symbol": "013030"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-06", "case_type": "failed_rerating", "company_name": "디케이락", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "false_positive_if_single_order_headline_is_used_despite_export_margin_and_revenue_weakness", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "guardrail_alignment", "symbol": "105740"}
{"best_trigger": "Stage4B", "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-07", "case_type": "failed_rerating", "company_name": "비엠티", "current_profile_verdict": "current_profile_false_positive", "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "notes": "false_positive_if_diversified_fitting_valve_exposure_is_treated_as_backlog_margin_bridge", "positive_or_counterexample": "counterexample", "price_source": "Songdaiki/stock-web", "reuse_reason": null, "round": "R1", "row_type": "case", "score_price_alignment": "guardrail_alignment", "symbol": "086670"}
{"MAE_180D_pct": -6.61, "MAE_1Y_pct": null, "MAE_30D_pct": -6.61, "MAE_90D_pct": -6.61, "MFE_180D_pct": 191.27, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 30.42, "MFE_90D_pct": 69.58, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-01", "company_name": "현대로템", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -14.98, "entry_date": "2024-07-01", "entry_price": 40100.0, "evidence_available_at_that_date": "rail_defense_backlog_revenue_margin_bridge", "evidence_family": "rail_defense_order_backlog_margin_bridge", "evidence_source": "BizWatch / KIS Rating / company-public performance-backlog sources", "evidence_url": "https://news.bizwatch.co.kr/article/industry/2025/08/05/0031", "evidence_url_pending": false, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-03-19", "peak_price": 116800.0, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv|atlas/ohlcv_tradable_by_symbol_year/064/064350/2025.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "promotion_block_reason": null, "promotion_usable": true, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|064350|Stage2-Actionable|2024-07-01", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "064350", "trigger_date": "2024-07-01", "trigger_id": "R1L117-C01-001", "trigger_outcome_label": "rail_defense_backlog_revenue_margin_bridge_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -8.18, "MAE_1Y_pct": null, "MAE_30D_pct": -1.27, "MAE_90D_pct": -8.18, "MFE_180D_pct": 52.42, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 33.33, "MFE_90D_pct": 51.52, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-02", "company_name": "두산에너빌리티", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_correct_but_scope_ambiguous_between_C01_and_C04", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -8.15, "entry_date": "2024-05-02", "entry_price": 16500.0, "evidence_available_at_that_date": "power_equipment_backlog_mix_margin_bridge", "evidence_family": "energy_equipment_backlog_mix_profitability_bridge", "evidence_source": "company IR / public research describing backlog mix and profitability route", "evidence_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20260406%EB%91%90%EC%82%B0%EC%97%90%EB%84%88%EB%B9%8C%EB%A6%AC%ED%8B%B0_%ED%95%B4%EC%99%B8%EC%A7%80%EC%97%AD_%EB%B0%A9%EB%AC%B8_IR%28Non-Deal_Roadshow%29_%EC%8B%A4%EC%8B%9C.pdf", "evidence_url_pending": true, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-01-24", "peak_price": 25150.0, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv|atlas/ohlcv_tradable_by_symbol_year/034/034020/2025.csv", "profile_path": "atlas/symbol_profiles/034/034020.json", "promotion_block_reason": "source_proxy_only_evidence_url_repair_required", "promotion_usable": false, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|034020|Stage2-Actionable|2024-05-02", "source_proxy_only": true, "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "034020", "trigger_date": "2024-05-02", "trigger_id": "R1L117-C01-002", "trigger_outcome_label": "power_equipment_backlog_mix_margin_bridge_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -9.31, "MAE_1Y_pct": null, "MAE_30D_pct": -9.31, "MAE_90D_pct": -9.31, "MFE_180D_pct": 197.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 38.0, "MFE_90D_pct": 54.51, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-03", "company_name": "SNT에너지", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -12.74, "entry_date": "2024-05-02", "entry_price": 10420.0, "evidence_available_at_that_date": "lng_air_cooler_hrsg_orderbook_operating_leverage", "evidence_family": "lng_air_cooler_hrsg_backlog_operating_leverage", "evidence_source": "SNT Energy research and news on order backlog and operating leverage", "evidence_url": "https://www.bondweb.co.kr/_research/downloadPage.asp?gn=1&number=856417", "evidence_url_pending": true, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-01-24", "peak_price": 31000.0, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100840/2024.csv|atlas/ohlcv_tradable_by_symbol_year/100/100840/2025.csv", "profile_path": "atlas/symbol_profiles/100/100840.json", "promotion_block_reason": "source_proxy_only_evidence_url_repair_required", "promotion_usable": false, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|100840|Stage3-Yellow|2024-05-02", "source_proxy_only": true, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "100840", "trigger_date": "2024-05-02", "trigger_id": "R1L117-C01-003", "trigger_outcome_label": "lng_air_cooler_hrsg_orderbook_operating_leverage_positive", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -6.26, "MAE_1Y_pct": null, "MAE_30D_pct": -6.26, "MAE_90D_pct": -6.26, "MFE_180D_pct": 186.34, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 10.75, "MFE_90D_pct": 48.9, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-04", "company_name": "성광벤드", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_missed_structural", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -13.23, "entry_date": "2024-05-02", "entry_price": 11350.0, "evidence_available_at_that_date": "industrial_fitting_shipbuilding_lng_order_recovery_margin_bridge", "evidence_family": "industrial_fitting_order_recovery_margin_bridge", "evidence_source": "sell-side/KRX materials on fitting order recovery and margin bridge", "evidence_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1710458815306.pdf", "evidence_url_pending": true, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": [], "four_b_full_window_peak_proximity": null, "four_b_local_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-01-17", "peak_price": 32500.0, "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014620/2024.csv|atlas/ohlcv_tradable_by_symbol_year/014/014620/2025.csv", "profile_path": "atlas/symbol_profiles/014/014620.json", "promotion_block_reason": "source_proxy_only_evidence_url_repair_required", "promotion_usable": false, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|014620|Stage2-Actionable|2024-05-02", "source_proxy_only": true, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "014620", "trigger_date": "2024-05-02", "trigger_id": "R1L117-C01-004", "trigger_outcome_label": "industrial_fitting_shipbuilding_lng_order_recovery_margin_bridge_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.84, "MAE_1Y_pct": null, "MAE_30D_pct": -15.22, "MAE_90D_pct": -18.84, "MFE_180D_pct": 17.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 6.34, "MFE_90D_pct": 6.34, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-05", "company_name": "하이록코리아", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -19.57, "entry_date": "2024-07-01", "entry_price": 27600.0, "evidence_available_at_that_date": "high_quality_fitting_label_without_near_term_order_acceleration", "evidence_family": "fitting_quality_label_without_incremental_order_margin_bridge", "evidence_source": "company finance page and 2024 research noting steady but not explosive growth", "evidence_url": "https://www.hy-lok.com/about/FinanceInfo.hylok", "evidence_url_pending": false, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak", "positioning_overheat"], "four_b_full_window_peak_proximity": 0.82, "four_b_local_peak_proximity": 0.82, "four_b_timing_verdict": "non_price_local_4B_watch_supported", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2025-01-22", "peak_price": 32450.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013030/2024.csv|atlas/ohlcv_tradable_by_symbol_year/013/013030/2025.csv", "profile_path": "atlas/symbol_profiles/013/013030.json", "promotion_block_reason": null, "promotion_usable": true, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|013030|Stage4B|2024-07-01", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "013030", "trigger_date": "2024-07-01", "trigger_id": "R1L117-C01-005", "trigger_outcome_label": "high_quality_fitting_label_without_near_term_order_acceleration_counterexample", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -35.61, "MAE_1Y_pct": null, "MAE_30D_pct": -28.45, "MAE_90D_pct": -28.45, "MFE_180D_pct": 10.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 10.16, "MFE_90D_pct": 10.16, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-06", "company_name": "디케이락", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -41.55, "entry_date": "2024-07-01", "entry_price": 9350.0, "evidence_available_at_that_date": "fitting_valve_order_headline_without_export_margin_conversion", "evidence_family": "fitting_valve_order_headline_without_margin_conversion", "evidence_source": "KRX quarterly report / NewsPim note on 2024 margin weakness", "evidence_url": "https://www.newspim.com/news/view/20250120000158", "evidence_url_pending": false, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak", "execution_risk"], "four_b_full_window_peak_proximity": 0.82, "four_b_local_peak_proximity": 0.82, "four_b_timing_verdict": "non_price_local_4B_watch_supported", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-07-29", "peak_price": 10300.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105740/2024.csv|atlas/ohlcv_tradable_by_symbol_year/105/105740/2025.csv", "profile_path": "atlas/symbol_profiles/105/105740.json", "promotion_block_reason": null, "promotion_usable": true, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|105740|Stage4B|2024-07-01", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak", "execution_risk"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "105740", "trigger_date": "2024-07-01", "trigger_id": "R1L117-C01-006", "trigger_outcome_label": "fitting_valve_order_headline_without_export_margin_conversion_counterexample", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.0, "MAE_1Y_pct": null, "MAE_30D_pct": -11.46, "MAE_90D_pct": -33.7, "MFE_180D_pct": 5.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MFE_30D_pct": 5.69, "MFE_90D_pct": 5.69, "aggregate_group_role": "representative", "below_entry_price_flag_180D": true, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "calibration_block_reasons": [], "calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-07", "company_name": "비엠티", "corporate_action_window_status": "clean_180D_window_or_candidate_outside_selected_180D", "current_profile_verdict": "current_profile_false_positive", "dedupe_for_aggregate": true, "deep_sub_archetype_id": "C01_DEEP_RAIL_DEFENSE_POWER_EQUIPMENT_AND_INDUSTRIAL_FITTING_BACKLOG_TO_MARGIN_BRIDGE", "do_not_count_as_new_case": false, "drawdown_after_peak_pct": -51.75, "entry_date": "2024-05-02", "entry_price": 13530.0, "evidence_available_at_that_date": "industrial_fitting_valve_diversification_without_margin_bridge", "evidence_family": "fitting_valve_diversification_without_margin_bridge", "evidence_source": "KIRS/company report on fitting/valve margin decline", "evidence_url": "https://w4.kirs.or.kr/download/research/240528_%EB%B9%84%EC%97%A0%ED%8B%B0.pdf", "evidence_url_pending": false, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "forward_window_trading_days": 180, "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only_local_peak", "execution_risk"], "four_b_full_window_peak_proximity": 0.82, "four_b_local_peak_proximity": 0.82, "four_b_timing_verdict": "non_price_local_4B_watch_supported", "four_c_protection_label": "thesis_break_watch_only", "green_lateness_ratio": null, "green_lateness_reason": "no confirmed Stage3-Green trigger in this C01 holdout set", "independent_evidence_weight": 1.0, "is_new_independent_case": true, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "peak_date": "2024-05-08", "peak_price": 14300.0, "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "Songdaiki/stock-web", "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086670/2024.csv|atlas/ohlcv_tradable_by_symbol_year/086/086670/2025.csv", "profile_path": "atlas/symbol_profiles/086/086670.json", "promotion_block_reason": null, "promotion_usable": true, "reuse_reason": null, "round": "R1", "row_type": "trigger", "same_entry_group_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|086670|Stage4B|2024-05-02", "source_proxy_only": false, "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak", "execution_risk"], "stage4c_evidence_fields": [], "stock_web_manifest_max_date": "2026-02-20", "symbol": "086670", "trigger_date": "2024-05-02", "trigger_id": "R1L117-C01-007", "trigger_outcome_label": "industrial_fitting_valve_diversification_without_margin_bridge_counterexample", "trigger_type": "Stage4B", "upstream_source": "FinanceData/marcap"}
{"MAE_90D_pct": -6.61, "MFE_90D_pct": 69.58, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-01", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "missed_structural_if_rail_defense_backlog_conversion_is_not_compressed_into_C01", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 19, "contract_score": 18, "customer_quality_score": 12, "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -1, "margin_bridge_score": 16, "policy_or_regulatory_score": 2, "relative_strength_score": 14, "revision_score": 13, "valuation_repricing_score": 3}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 18, "contract_score": 17, "customer_quality_score": 12, "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -1, "margin_bridge_score": 14, "policy_or_regulatory_score": 2, "relative_strength_score": 14, "revision_score": 12, "valuation_repricing_score": 3}, "row_type": "score_simulation", "score_return_alignment_label": "positive_alignment", "stage_label_after": "Stage3-Yellow guarded", "stage_label_before": "Stage2-Actionable", "symbol": "064350", "trigger_id": "R1L117-C01-001", "weighted_score_after": 83, "weighted_score_before": 79}
{"MAE_90D_pct": -8.18, "MFE_90D_pct": 51.52, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-02", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "scope_ambiguity_if_nuclear_policy_optionalities_substitute_for_order_margin_bridge", "current_profile_verdict": "current_profile_correct_but_scope_ambiguous_between_C01_and_C04", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 18, "contract_score": 15, "customer_quality_score": 10, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": -2, "margin_bridge_score": 14, "policy_or_regulatory_score": 5, "relative_strength_score": 12, "revision_score": 11, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 17, "contract_score": 15, "customer_quality_score": 10, "dilution_cb_risk_score": 0, "execution_risk_score": -5, "legal_or_contract_risk_score": -2, "margin_bridge_score": 12, "policy_or_regulatory_score": 5, "relative_strength_score": 12, "revision_score": 10, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "positive_alignment", "stage_label_after": "Stage3-Yellow guarded", "stage_label_before": "Stage2-Actionable", "symbol": "034020", "trigger_id": "R1L117-C01-002", "weighted_score_after": 81, "weighted_score_before": 77}
{"MAE_90D_pct": -9.31, "MFE_90D_pct": 54.51, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-03", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "too_conservative_if_small_cap_orderbook_operating_leverage_is_not_allowed_to_reach_yellow", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 19, "contract_score": 16, "customer_quality_score": 11, "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -1, "margin_bridge_score": 17, "policy_or_regulatory_score": 1, "relative_strength_score": 13, "revision_score": 14, "valuation_repricing_score": 4}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 18, "contract_score": 16, "customer_quality_score": 11, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": -1, "margin_bridge_score": 15, "policy_or_regulatory_score": 1, "relative_strength_score": 13, "revision_score": 13, "valuation_repricing_score": 4}, "row_type": "score_simulation", "score_return_alignment_label": "positive_alignment", "stage_label_after": "Stage3-Green watch but not production Green", "stage_label_before": "Stage3-Yellow", "symbol": "100840", "trigger_id": "R1L117-C01-003", "weighted_score_after": 89, "weighted_score_before": 84}
{"MAE_90D_pct": -6.26, "MFE_90D_pct": 48.9, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-04", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "missed_structural_if_fitting_supplier_order_recovery_is_filtered_as_generic_commodity_beta", "current_profile_verdict": "current_profile_missed_structural", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 18, "contract_score": 15, "customer_quality_score": 9, "dilution_cb_risk_score": 0, "execution_risk_score": -3, "legal_or_contract_risk_score": -1, "margin_bridge_score": 16, "policy_or_regulatory_score": 1, "relative_strength_score": 10, "revision_score": 12, "valuation_repricing_score": 3}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 16, "contract_score": 15, "customer_quality_score": 9, "dilution_cb_risk_score": 0, "execution_risk_score": -4, "legal_or_contract_risk_score": -1, "margin_bridge_score": 13, "policy_or_regulatory_score": 1, "relative_strength_score": 10, "revision_score": 10, "valuation_repricing_score": 3}, "row_type": "score_simulation", "score_return_alignment_label": "positive_alignment", "stage_label_after": "Stage3-Yellow guarded", "stage_label_before": "Stage2 watch", "symbol": "014620", "trigger_id": "R1L117-C01-004", "weighted_score_after": 80, "weighted_score_before": 72}
{"MAE_90D_pct": -18.84, "MFE_90D_pct": 6.34, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-05", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "false_positive_if_high_quality_fitting_business_is_promoted_without_incremental_order_or_revision_bridge", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 10, "contract_score": 10, "customer_quality_score": 12, "dilution_cb_risk_score": 0, "execution_risk_score": -10, "legal_or_contract_risk_score": -1, "margin_bridge_score": 5, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 4, "valuation_repricing_score": 1}, "raw_component_scores_before": {"accounting_trust_risk_score": 1, "backlog_visibility_score": 11, "contract_score": 10, "customer_quality_score": 12, "dilution_cb_risk_score": 0, "execution_risk_score": -7, "legal_or_contract_risk_score": -1, "margin_bridge_score": 8, "policy_or_regulatory_score": 0, "relative_strength_score": 6, "revision_score": 5, "valuation_repricing_score": 2}, "row_type": "score_simulation", "score_return_alignment_label": "guardrail_alignment", "stage_label_after": "Stage4B local watch", "stage_label_before": "Stage2 watch", "symbol": "013030", "trigger_id": "R1L117-C01-005", "weighted_score_after": 58, "weighted_score_before": 68}
{"MAE_90D_pct": -28.45, "MFE_90D_pct": 10.16, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-06", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "false_positive_if_single_order_headline_is_used_despite_export_margin_and_revenue_weakness", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 9, "contract_score": 11, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -15, "legal_or_contract_risk_score": -1, "margin_bridge_score": 2, "policy_or_regulatory_score": 0, "relative_strength_score": 4, "revision_score": 2, "valuation_repricing_score": 1}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 10, "contract_score": 11, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -12, "legal_or_contract_risk_score": -1, "margin_bridge_score": 4, "policy_or_regulatory_score": 0, "relative_strength_score": 5, "revision_score": 3, "valuation_repricing_score": 2}, "row_type": "score_simulation", "score_return_alignment_label": "guardrail_alignment", "stage_label_after": "Stage4B local watch", "stage_label_before": "Stage2 watch", "symbol": "105740", "trigger_id": "R1L117-C01-006", "weighted_score_after": 47, "weighted_score_before": 62}
{"MAE_90D_pct": -33.7, "MFE_90D_pct": 5.69, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01-R1-L117-07", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "false_positive_if_diversified_fitting_valve_exposure_is_treated_as_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "raw_component_scores_after": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 8, "contract_score": 10, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -16, "legal_or_contract_risk_score": -1, "margin_bridge_score": 1, "policy_or_regulatory_score": 0, "relative_strength_score": 4, "revision_score": 2, "valuation_repricing_score": 1}, "raw_component_scores_before": {"accounting_trust_risk_score": -1, "backlog_visibility_score": 9, "contract_score": 10, "customer_quality_score": 8, "dilution_cb_risk_score": 0, "execution_risk_score": -13, "legal_or_contract_risk_score": -1, "margin_bridge_score": 3, "policy_or_regulatory_score": 0, "relative_strength_score": 4, "revision_score": 3, "valuation_repricing_score": 1}, "row_type": "score_simulation", "score_return_alignment_label": "guardrail_alignment", "stage_label_after": "Stage4B local watch", "stage_label_before": "Stage2 watch", "symbol": "086670", "trigger_id": "R1L117-C01-007", "weighted_score_after": 40, "weighted_score_before": 58}
{"calibration_usable_trigger_count": 7, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_count": 7, "counterexample_count": 3, "current_profile_error_count": 6, "evidence_url_pending_count": 4, "fine_archetype_id": "C01_RAIL_POWER_EQUIPMENT_FITTING_BACKLOG_MARGIN_FCF_BRIDGE", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "new_independent_case_count": 7, "new_symbol_count_estimate": 7, "positive_case_count": 4, "proposed_axis": "C01_verified_backlog_margin_fcf_bridge_required_before_Yellow_or_Green_plus_component_order_proxy_to_local_4B_watch", "representative_trigger_count": 7, "reused_case_count": 0, "row_type": "aggregate", "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 7, "selected_loop": 117, "selected_round": "R1", "source_proxy_only_count": 4, "stage4b_case_count": 3, "stage4c_case_count": 0}
{"canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "do_not_propose_new_weight_delta": false, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "loop": "117", "loop_contribution_label": "canonical_archetype_rule_candidate", "new_independent_case_count": 7, "new_symbol_count": 7, "new_trigger_family_count": 7, "residual_error_types_found": ["missed_structural_supplier_bridge", "false_positive_component_order_proxy_without_margin_bridge", "scope_ambiguity_C01_vs_C04_or_C03"], "reused_case_count": 0, "round": "R1", "row_type": "residual_contribution", "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"]}
```

## Batch Ingest Self-Audit
```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 7
calibration_usable_trigger_count: 7
representative_trigger_count: 7
new_weight_evidence_candidate_count: 7
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 26. Deferred Coding Agent Handoff Prompt
### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- price-only rows cannot promote Stage2/Stage3.
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

## 27. Next Round State
```text
completed_round = R1
completed_loop = 117
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C11_BATTERY_ORDERBOOK_RERATING, C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as coverage and no-repeat ledger.
- `Songdaiki/stock-web` manifest was used as the price-source authority; manifest max date is 2026-02-20.
- Evidence URLs are used as historical context anchors. Rows with `source_proxy_only=true` are quantitatively usable for backtest but should be blocked from promotion until URL/source repair confirms the non-price bridge.
