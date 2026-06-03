# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R9
scheduled_loop: 15
completed_round: R9
completed_loop: 15
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD
output_file: e2r_stock_web_v12_residual_round_R9_loop_15_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds **4** new independent cases, **2** counterexamples, and **4** residual errors for **R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE**.

## 1. Current Calibrated Profile Assumption

| axis | assumed current value | status in this MD |
|---|---:|---|
| stage2_actionable_evidence_bonus | +2.0 | existing_axis_tested |
| stage3_yellow_total_min | 75.0 | existing_axis_kept |
| stage3_green_total_min | 87.0 | existing_axis_kept |
| stage3_green_revision_min | 55.0 | existing_axis_weakened_for_C29_shadow_only |
| stage3_cross_evidence_green_buffer | +1.5 | existing_axis_kept |
| price_only_blowoff_blocks_positive_stage | true | existing_axis_strengthened |
| full_4b_requires_non_price_evidence | true | existing_axis_strengthened |
| hard_4c_thesis_break_routes_to_4c | true | existing_axis_strengthened |

The study does not re-prove the global Stage2 bonus. It asks whether C29 needs a narrower supplier margin-conversion boost and a harsher guard for customer-concentration or platform-volume narratives that have no unit economics.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 15 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD |
| round_sector_consistency | pass |
| R9 mapping rationale | R9 permits L3 when the target is mobility/transport/EV movement rather than real-estate construction. |

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 registry files showed R9 Loop 10~14 already covered OEM margin mix, tires, modules, logistics, shipping and airlines. This loop therefore avoids the repeated symbols 005380, 000270, 204320, 161390, 012330, 011210, 018880, 011200, 086280, 089590, 091810, 000120, 028670, 003490 and 272450.

| previous R9 loop | dominant symbols / families | avoided? |
|---|---|---|
| Loop 10 | Hyundai/Kia OEM plus HL Mando supplier counterexample | yes |
| Loop 11 | tire, module, engine-parts, thermal supplier | yes |
| Loop 12 | HMM/PCC/LCC transport and dilution | yes |
| Loop 13 | parcel, dry bulk, FSC/LCC airline guard | yes |
| Loop 14 | repeated Hyundai/Kia plus Jeju Air guard | yes |
| this loop | 015750, 010690, 009900, 403550 | new symbols and new trigger families |

minimum_new_independent_case_ratio = 1.00; minimum_new_symbol_count = 4; same_archetype_new_trigger_family_count = 4.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The schema confirms tradable columns d,o,h,l,c,v,a,mc,s,m and the research formulas: MFE_N_pct = max(high)/entry_price - 1; MAE_N_pct = min(low)/entry_price - 1. All representative windows have at least 180 forward tradable rows before manifest max_date.

## 5. Historical Eligibility Gate

| symbol | profile path | profile status | representative entry | 180D usable? | corporate-action status |
|---|---|---|---|---|---|
| 015750 | atlas/symbol_profiles/015/015750.json | old corporate-action candidates end 2018-07-09 | 2023-02-17 | true | clean_180D_window |
| 010690 | atlas/symbol_profiles/010/010690.json | corporate-action candidates before 2002 | 2023-03-09 | true | clean_180D_window |
| 009900 | atlas/symbol_profiles/009/009900.json | corporate-action candidate 2021-06-18 only | 2023-08-11 | true | clean_180D_window |
| 403550 | atlas/symbol_profiles/403/403550.json | no corporate-action candidates | 2022-08-22 | true | clean_180D_window |

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| EV_BODY_LIGHTWEIGHT_PARTS_OPERATING_LEVERAGE | C29 | body/chassis suppliers monetize mobility volume only when mix and margin conversion appear |
| CHASSIS_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE | C29 | export/mix improvements are a C29 operating-leverage path, not a separate global axis |
| EV_CUSTOMER_CONCENTRATION_WITHOUT_MARGIN_PASS_THROUGH | C29 | customer-quality evidence is dangerous unless margin pass-through exists |
| MOBILITY_PLATFORM_VOLUME_WITHOUT_UNIT_ECONOMICS | C29 | platform volume belongs in C29 only when unit economics / operating leverage are visible |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | trigger family | new independent? |
|---|---:|---|---|---|---|---|
| R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN | 015750 | 성우하이텍 | structural_success | positive | EV_BODY_LIGHTWEIGHT_PARTS_OPERATING_LEVERAGE | true |
| R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION | 010690 | 화신 | structural_success | positive | CHASSIS_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE | true |
| R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2 | 009900 | 명신산업 | failed_rerating | counterexample | EV_CUSTOMER_CONCENTRATION_WITHOUT_MARGIN_PASS_THROUGH | true |
| R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE | 403550 | 쏘카 | false_positive_green | counterexample | MOBILITY_PLATFORM_VOLUME_WITHOUT_UNIT_ECONOMICS | true |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 4 |
| calibration_usable_trigger_count | 7 |

The balance is intentionally symmetric: two supplier positives show when volume becomes margin, while two counterexamples show that customer or platform volume without margin / unit economics should not be promoted.

## 9. Evidence Source Map

| symbol | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence validation note |
|---|---|---|---|---|
| 015750 | public_event_or_disclosure, relative_strength, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility | - | public historical evidence proxy; exact URL not used for production scoring |
| 010690 | public_event_or_disclosure, relative_strength, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, confirmed_revision | - | public historical evidence proxy; exact URL not used for production scoring |
| 009900 | public_event_or_disclosure, customer_or_order_quality, relative_strength | - | price_only_local_peak, margin_or_backlog_slowdown, thesis_evidence_broken | public historical evidence proxy; exact URL not used for production scoring |
| 403550 | public_event_or_disclosure, capacity_or_volume_route | - | valuation_blowoff, positioning_overheat, thesis_evidence_broken | public historical evidence proxy; exact URL not used for production scoring |

## 10. Price Data Source Map

| symbol | year shards used | profile path | anchor rows checked |
|---|---|---|---|
| 015750 | 2023 | atlas/symbol_profiles/015/015750.json | 2023-02-17 close 6,960; 2023-07-12 high 16,370; 2023-10-26 low 7,800 |
| 010690 | 2023 | atlas/symbol_profiles/010/010690.json | 2023-03-09 close 11,540; 2023-07-06 high 22,700; 2023-10-26 low 9,940 |
| 009900 | 2023, 2024 | atlas/symbol_profiles/009/009900.json | 2023-08-11 close 20,850; 2023-08-30 high 21,500; 2024-04-08 low 14,190 |
| 403550 | 2022, 2023 | atlas/symbol_profiles/403/403550.json | 2022-08-22 close 26,300; 2022-08-23 high 29,600; 2022-10-05 low 15,100 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | Stage2 | Stage3 | 4B | 4C | usable |
|---|---|---:|---|---|---|---:|---|---|---|---|---|
| T_R9L15_015750_STAGE2_20230216 | R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN | 015750 | Stage2-Actionable | 2023-02-16 | 2023-02-17 | 6,960 | public_event_or_disclosure, relative_strength, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility | - | - | True |
| T_R9L15_010690_STAGE2_20230309 | R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION | 010690 | Stage2-Actionable | 2023-03-09 | 2023-03-09 | 11,540 | public_event_or_disclosure, relative_strength, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, confirmed_revision | - | - | True |
| T_R9L15_009900_STAGE2_20230811 | R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2 | 009900 | Stage2-Actionable | 2023-08-11 | 2023-08-11 | 20,850 | public_event_or_disclosure, customer_or_order_quality, relative_strength | - | price_only_local_peak, margin_or_backlog_slowdown | thesis_evidence_broken | True |
| T_R9L15_403550_STAGE2_20220822 | R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE | 403550 | Stage2-Actionable | 2022-08-22 | 2022-08-22 | 26,300 | public_event_or_disclosure, capacity_or_volume_route | - | valuation_blowoff, positioning_overheat | thesis_evidence_broken | True |
| T_R9L15_015750_4B_20230712 | R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN | 015750 | Stage4B-Overlay | 2023-07-12 | 2023-07-12 | 14,990 | - | - | valuation_blowoff, positioning_overheat, price_only_local_peak | - | True |
| T_R9L15_010690_4B_20230706 | R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION | 010690 | Stage4B-Overlay | 2023-07-06 | 2023-07-06 | 21,000 | - | - | valuation_blowoff, positioning_overheat, price_only_local_peak | - | True |
| T_R9L15_009900_4C_20240117 | R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2 | 009900 | Stage4C | 2024-01-17 | 2024-01-17 | 16,880 | - | - | - | thesis_evidence_broken | True |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | representative? |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| T_R9L15_015750_STAGE2_20230216 | 6,960 | 14.08 | -10.49 | 61.35 | -10.49 | 135.2 | -10.49 | 2023-07-12 | 16,370 | -52.35 | True |
| T_R9L15_010690_STAGE2_20230309 | 11,540 | 40.73 | -10.49 | 96.71 | -10.49 | 96.71 | -13.86 | 2023-07-06 | 22,700 | -56.21 | True |
| T_R9L15_009900_STAGE2_20230811 | 20,850 | 3.12 | -11.99 | 3.12 | -24.99 | 3.12 | -31.94 | 2023-08-30 | 21,500 | -34.0 | True |
| T_R9L15_403550_STAGE2_20220822 | 26,300 | 12.55 | -42.59 | 12.55 | -42.59 | 12.55 | -42.59 | 2022-08-23 | 29,600 | -48.99 | True |
| T_R9L15_015750_4B_20230712 | 14,990 | 9.21 | -17.95 | 9.21 | -47.97 | 9.21 | -48.37 | 2023-07-12 | 16,370 | -52.72 | False |
| T_R9L15_010690_4B_20230706 | 21,000 | 8.1 | -40.9 | 8.1 | -52.67 | 8.1 | -52.67 | 2023-07-06 | 22,700 | -56.21 | False |
| T_R9L15_009900_4C_20240117 | 16,880 | 4.98 | -3.73 | 4.98 | -15.94 | 13.09 | -15.94 | 2024-02-02 | 17,720 | -19.92 | False |

## 13. Current Calibrated Profile Stress Test

| case_id | current proxy likely decision | actual MFE/MAE | verdict | residual note |
|---|---|---|---|---|
| R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN | likely waits for confirmed revision / Green | MFE180 +135.20%, MAE180 -10.49% | current_profile_too_late | small supplier margin conversion was visible before Green-style confirmation |
| R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION | likely Yellow, later Green | MFE90 +96.71%, MAE90 -10.49% | current_profile_too_late | early margin/mix signal was tradable before strict revision confirmation |
| R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2 | customer-quality + EV volume may overpromote | MFE90 +3.12%, MAE90 -24.99% | current_profile_false_positive | customer concentration is not the same as margin conversion |
| R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE | platform-volume / IPO narrative may reach Yellow | MFE90 +12.55%, MAE90 -42.59% | current_profile_false_positive | unit economics missing; mobility volume did not convert into operating leverage |

Stress-test answers: Stage2 bonus was helpful for the two supplier positives but too permissive for the two volume-only counterexamples. Yellow 75 is acceptable only with a C29 margin-conversion or unit-economics gate. Green 87 / revision 55 is too strict for small supplier positives when margin conversion and price/volume confirmation arrive together. Price-only blowoff and full 4B non-price requirement remain appropriate. Hard 4C should fire earlier for customer concentration / platform unit-economics breaks.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3 proxy entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 015750 positive | 6,960 | 10,600 | 16,370 | 0.387 | Green somewhat late but not terminal; Stage2 captured most upside |
| 010690 positive | 11,540 | 16,900 | 22,700 | 0.480 | Green meaningfully late; revision threshold too strict for this C29 supplier path |
| 009900 counterexample | 20,850 | not_applicable | 21,500 | not_applicable | no confirmed Green; should be blocked by customer-concentration guard |
| 403550 counterexample | 26,300 | not_applicable | 29,600 | not_applicable | no confirmed Green; should be blocked by unit-economics guard |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 reference | 4B entry | local/full peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---:|---|---|
| T_R9L15_015750_4B_20230712 | 6,960 | 14,990 | 16,370 | 0.853 | 0.853 | price_only + valuation_blowoff + positioning_overheat | good overlay watch, not full 4B without non-price evidence |
| T_R9L15_010690_4B_20230706 | 11,540 | 21,000 | 22,700 | 0.848 | 0.848 | price_only + valuation_blowoff + positioning_overheat | good overlay watch, not full 4B without non-price evidence |

## 16. 4C Protection Audit

| trigger_id | prior peak | 4C entry | post-4C MAE90 | max drawdown from prior peak | protection score | label |
|---|---:|---:|---:|---:|---:|---|
| T_R9L15_009900_4C_20240117 | 21,500 | 16,880 | -15.94 | -34.00 | 0.531 | hard_4c_late_partial |

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate = false. This loop is all inside one canonical archetype and does not span enough distinct L3 sub-families to justify an L3-wide sector rule beyond C29.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate = true.

Proposed C29 shadow rule: **Volume is promotable only when it visibly converts into margin or unit economics.** Auto-parts suppliers may receive a C29 margin-conversion boost when relative strength, volume route, and early revision/margin bridge appear together. Customer concentration and mobility-platform volume receive a hard cap unless margin pass-through, diversified customer quality, or unit economics are independently visible.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current proxy | Stage2 bonus helps but still overweights customer-quality / platform-volume narratives and waits too long for smaller parts margin conversion | none | 4 | 43.43 | -22.14 | 61.89 | -24.72 | 50% | 0 | 2 | 0.433 | mixed; positives delayed and counterexamples overpromoted |
| P0b e2r_2_0_baseline_reference | rollback reference | looser profile would admit more volume-only mobility narratives | reference only | 4 | 43.43 | -22.14 | 61.89 | -24.72 | 50%+ | 0 | 2 | 0.433 | worse false-positive control |
| P1 sector_specific_candidate_profile | sector shadow | L3/C29 needs supplier margin-conversion boost plus customer-concentration/unit-economics guard | margin_conversion +1; customer_concentration guard +1 | 4 | 79.03 | -10.49 | 115.95 | -12.18 | 0% | 0 | 0 | 0.433 | better score-return alignment |
| P2 canonical_archetype_candidate_profile | canonical shadow | C29 compresses auto parts, logistics and mobility platforms only if volume converts into margin or unit economics | C29_margin_conversion_gate + C29_volume_without_margin_cap | 4 | 79.03 | -10.49 | 115.95 | -12.18 | 0% | 0 | 0 | 0.433 | candidate canonical rule |
| P3 counterexample_guard_profile | guard shadow | customer concentration / fresh platform volume narratives stay Stage2-Watch until unit economics or margin bridge appears | hard cap for unit-economics missing | 4 | 79.03 | -10.49 | 115.95 | -12.18 | 0% | 0 | 0 | 0.433 | best guard profile |

## 20. Score-Return Alignment Matrix

| case_id | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN | 78.0 | Stage3-Yellow | 84.0 | Stage3-Yellow+ | 61.35 | -10.49 | aligned positive |
| R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION | 80.0 | Stage3-Yellow | 86.0 | Stage3-Yellow+ | 96.71 | -10.49 | aligned positive |
| R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2 | 76.0 | Stage3-Yellow | 62.0 | Stage2-Watch/Blocked | 3.12 | -24.99 | false positive reduced |
| R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE | 75.5 | Stage3-Yellow | 58.0 | Stage2-Watch/Blocked | 12.55 | -42.59 | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD | 2 | 2 | 2 | 1 | 4 | 0 | 7 | 4 | 4 | false | true | EV/body/chassis supplier positives added; customer-concentration and mobility-platform unit-economics guards added; still needs future holdout in charging/infrastructure-adjacent mobility |

## 22. Residual Contribution Summary

new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [current_profile_too_late, current_profile_false_positive, current_profile_4C_too_late]
new_axis_proposed: c29_margin_conversion_boost_and_customer_concentration_unit_economics_guard
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: stage3_green_revision_min_for_C29_supplier_margin_conversion_shadow_only
existing_axis_kept: stage3_yellow_total_min; stage3_green_total_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest, schema columns, selected symbol profiles, selected tradable OHLC rows, entry dates, MFE/MAE/peak/drawdown, corporate-action window status, same-entry dedupe, R9/L3/C29 consistency, novelty against local R9 Loop 10~14 outputs.

Not validated: exact DART filing URLs, broker-report text extraction, production scoring code, live candidate status, current investment attractiveness, brokerage API execution. Evidence labels are research proxies and must not be promoted without a later implementation/ingestion pass.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_supplier_margin_conversion_boost,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"EV/body/chassis suppliers with relative strength plus margin conversion produced high MFE and manageable MAE","keeps 015750/010690 positives while not loosening global Green","T_R9L15_015750_STAGE2_20230216|T_R9L15_010690_STAGE2_20230309",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_customer_concentration_without_margin_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"EV customer-quality/volume without margin pass-through produced low MFE and high MAE","blocks 009900-style false positives","T_R9L15_009900_STAGE2_20230811",1,1,1,medium,canonical_shadow_only,"not production; strengthens existing non-price evidence requirement"
shadow_weight,c29_mobility_platform_unit_economics_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"mobility-platform volume without unit economics produced deep MAE after IPO trigger","blocks 403550-style volume-only platform promotion","T_R9L15_403550_STAGE2_20220822",1,1,1,medium,canonical_shadow_only,"not production; platform volume requires unit economics"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_LIGHTWEIGHT_PARTS_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L15_015750_STAGE2_20230216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2023-02-17 close 6,960; 2023-07-12 high 16,370; 180D low did not breach entry after the initial entry-day low."}
{"row_type":"case","case_id":"R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION","symbol":"010690","company_name":"화신","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CHASSIS_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_R9L15_010690_STAGE2_20230309","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2023-03-09 close 11,540; 2023-07-06 high 22,700; 2023-10-26 low 9,940 inside 180D after peak."}
{"row_type":"case","case_id":"R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2","symbol":"009900","company_name":"명신산업","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_CUSTOMER_CONCENTRATION_WITHOUT_MARGIN_PASS_THROUGH","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_R9L15_009900_STAGE2_20230811","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_corrected_by_shadow_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2023-08-11 close 20,850; 2023-08-30 high 21,500; 2023-10-31 low 15,640; 2024-04-08 low 14,190."}
{"row_type":"case","case_id":"R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE","symbol":"403550","company_name":"쏘카","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_PLATFORM_VOLUME_WITHOUT_UNIT_ECONOMICS","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"T_R9L15_403550_STAGE2_20220822","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_corrected_by_shadow_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2022-08-22 close 26,300; 2022-08-23 high 29,600; 2022-10-05 low 15,100 within first 30 trading days."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"T_R9L15_015750_STAGE2_20230216","case_id":"R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_BODY_LIGHTWEIGHT_PARTS_OPERATING_LEVERAGE","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_missed_structural_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-16","evidence_available_at_that_date":"EV body/lightweight parts rerating plus same-day volume expansion; evidence timing is treated as public/same-day market-digest available, not a later outcome label.","evidence_source":"stock-web OHLC rows + public historical earnings/order narrative proxy; exact disclosure URL not promoted in this standalone residual file","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-17","entry_price":6960,"MFE_30D_pct":14.08,"MFE_90D_pct":61.35,"MFE_180D_pct":135.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.49,"MAE_90D_pct":-10.49,"MAE_180D_pct":-10.49,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.35,"green_lateness_ratio":0.387,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_015750_2023-02-17_6960","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_010690_STAGE2_20230309","case_id":"R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION","symbol":"010690","company_name":"화신","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CHASSIS_EXPORT_MIX_MARGIN_OPERATING_LEVERAGE","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_missed_structural_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-09","evidence_available_at_that_date":"chassis/EV-platform supplier rerating with visible relative strength and later margin conversion; entry is same-day close because the signal is a market-session public trigger, not a hindsight Green label.","evidence_source":"stock-web OHLC rows + public historical auto-parts margin/EV platform narrative proxy; exact disclosure URL not promoted in this standalone residual file","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","confirmed_revision"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-09","entry_price":11540,"MFE_30D_pct":40.73,"MFE_90D_pct":96.71,"MFE_180D_pct":96.71,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.49,"MAE_90D_pct":-10.49,"MAE_180D_pct":-13.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":22700,"drawdown_after_peak_pct":-56.21,"green_lateness_ratio":0.48,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_010690_2023-03-09_11540","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_009900_STAGE2_20230811","case_id":"R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2","symbol":"009900","company_name":"명신산업","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_CUSTOMER_CONCENTRATION_WITHOUT_MARGIN_PASS_THROUGH","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_missed_structural_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-08-11","evidence_available_at_that_date":"EV customer volume headline/relative-strength burst without durable margin bridge; this is a residual false-positive test for C29 customer-quality scoring.","evidence_source":"stock-web OHLC rows + public historical Tesla/EV customer-concentration narrative proxy; exact disclosure URL not promoted in this standalone residual file","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009900/2023.csv and 2024.csv","profile_path":"atlas/symbol_profiles/009/009900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-08-11","entry_price":20850,"MFE_30D_pct":3.12,"MFE_90D_pct":3.12,"MFE_180D_pct":3.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.99,"MAE_90D_pct":-24.99,"MAE_180D_pct":-31.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-30","peak_price":21500,"drawdown_after_peak_pct":-34.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_009900_2023-08-11_20850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_403550_STAGE2_20220822","case_id":"R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE","symbol":"403550","company_name":"쏘카","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_PLATFORM_VOLUME_WITHOUT_UNIT_ECONOMICS","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|residual_missed_structural_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2022-08-22","evidence_available_at_that_date":"fresh mobility-platform listing/scale narrative without demonstrated unit-economics and operating leverage; tests whether platform-like mobility should be compressed into C29 with a hard unit-economics guard.","evidence_source":"stock-web OHLC rows + public IPO/listing narrative proxy; exact prospectus URL not promoted in this standalone residual file","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403550/2022.csv and 2023.csv","profile_path":"atlas/symbol_profiles/403/403550.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-08-22","entry_price":26300,"MFE_30D_pct":12.55,"MFE_90D_pct":12.55,"MFE_180D_pct":12.55,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-42.59,"MAE_90D_pct":-42.59,"MAE_180D_pct":-42.59,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-08-23","peak_price":29600,"drawdown_after_peak_pct":-48.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_403550_2022-08-22_26300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_015750_4B_20230712","case_id":"R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-12","evidence_available_at_that_date":"local/full-window peak proximity after large EV parts rerating; price-dominated risk overlay only.","evidence_source":"stock-web price path; non-price 4B evidence not independently validated","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-12","entry_price":14990,"MFE_30D_pct":9.21,"MFE_90D_pct":9.21,"MFE_180D_pct":9.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.95,"MAE_90D_pct":-47.97,"MAE_180D_pct":-48.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.853,"four_b_full_window_peak_proximity":0.853,"four_b_timing_verdict":"good_overlay_watch_but_price_dominated_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_015750_4B_2023-07-12_14990","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case; distinct overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_010690_4B_20230706","case_id":"R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION","symbol":"010690","company_name":"화신","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-06","evidence_available_at_that_date":"local/full-window peak proximity after chassis supplier rerating; price-dominated risk overlay only.","evidence_source":"stock-web price path; non-price 4B evidence not independently validated","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010690/2023.csv","profile_path":"atlas/symbol_profiles/010/010690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-06","entry_price":21000,"MFE_30D_pct":8.1,"MFE_90D_pct":8.1,"MFE_180D_pct":8.1,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-40.9,"MAE_90D_pct":-52.67,"MAE_180D_pct":-52.67,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":22700,"drawdown_after_peak_pct":-56.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.848,"four_b_full_window_peak_proximity":0.848,"four_b_timing_verdict":"good_overlay_watch_but_price_dominated_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_010690_4B_2023-07-06_21000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case; distinct overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"T_R9L15_009900_4C_20240117","case_id":"R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2","symbol":"009900","company_name":"명신산업","round":"R9","loop":"15","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_LIGHTWEIGHT_BODY_LAMP_MARGIN_CONVERSION_VS_CUSTOMER_CONCENTRATION_UNIT_ECONOMICS_GUARD","sector":"Mobility / EV auto parts / mobility platform","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2024-01-17","evidence_available_at_that_date":"customer concentration / margin pass-through thesis had already failed to produce durable rerating; 4C was late but still protected part of remaining drawdown.","evidence_source":"stock-web price path plus thesis-break watch proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv","profile_path":"atlas/symbol_profiles/009/009900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-17","entry_price":16880,"MFE_30D_pct":4.98,"MFE_90D_pct":4.98,"MFE_180D_pct":13.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.73,"MAE_90D_pct":-15.94,"MAE_180D_pct":-15.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":17720,"drawdown_after_peak_pct":-19.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"hard_4c_late_partial; protection_score=0.531","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L15_009900_4C_2024-01-17_16880","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same case; distinct overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_015750_2023_EV_BODY_LIGHTWEIGHT_MARGIN","trigger_id":"T_R9L15_015750_STAGE2_20230216","symbol":"015750","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":20,"margin_bridge_score":52,"revision_score":45,"relative_strength_score":62,"customer_quality_score":48,"policy_or_regulatory_score":14,"valuation_repricing_score":42,"execution_risk_score":18,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"volume_route_score":58,"mix_asp_score":54,"margin_conversion_score":54,"customer_concentration_penalty":8,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":20,"margin_bridge_score":59,"revision_score":50,"relative_strength_score":62,"customer_quality_score":48,"policy_or_regulatory_score":14,"valuation_repricing_score":42,"execution_risk_score":15,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"volume_route_score":58,"mix_asp_score":60,"margin_conversion_score":64,"customer_concentration_penalty":8,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_after":84.0,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score","customer_concentration_penalty","unit_economics_score","margin_conversion_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin conversion in EV/body/chassis suppliers and blocks customer-concentration or platform-volume narratives without margin pass-through / unit economics.","MFE_90D_pct":61.35,"MAE_90D_pct":-10.49,"score_return_alignment_label":"aligned_positive_margin_conversion","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_010690_2023_CHASSIS_MARGIN_CONVERSION","trigger_id":"T_R9L15_010690_STAGE2_20230309","symbol":"010690","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":18,"margin_bridge_score":55,"revision_score":48,"relative_strength_score":64,"customer_quality_score":50,"policy_or_regulatory_score":14,"valuation_repricing_score":44,"execution_risk_score":18,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"volume_route_score":60,"mix_asp_score":58,"margin_conversion_score":58,"customer_concentration_penalty":8,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":18,"margin_bridge_score":62,"revision_score":53,"relative_strength_score":64,"customer_quality_score":50,"policy_or_regulatory_score":14,"valuation_repricing_score":44,"execution_risk_score":15,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3,"volume_route_score":60,"mix_asp_score":64,"margin_conversion_score":68,"customer_concentration_penalty":8,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_after":86.0,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score","customer_concentration_penalty","unit_economics_score","margin_conversion_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin conversion in EV/body/chassis suppliers and blocks customer-concentration or platform-volume narratives without margin pass-through / unit economics.","MFE_90D_pct":96.71,"MAE_90D_pct":-10.49,"score_return_alignment_label":"aligned_positive_margin_conversion","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_009900_2023_CUSTOMER_CONCENTRATION_FALSE_STAGE2","trigger_id":"T_R9L15_009900_STAGE2_20230811","symbol":"009900","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":12,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":58,"customer_quality_score":62,"policy_or_regulatory_score":8,"valuation_repricing_score":46,"execution_risk_score":36,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"volume_route_score":54,"mix_asp_score":20,"margin_conversion_score":18,"customer_concentration_penalty":42,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":12,"margin_bridge_score":12,"revision_score":12,"relative_strength_score":42,"customer_quality_score":62,"policy_or_regulatory_score":8,"valuation_repricing_score":30,"execution_risk_score":52,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"volume_route_score":54,"mix_asp_score":20,"margin_conversion_score":8,"customer_concentration_penalty":62,"unit_economics_score":"unknown_or_not_supported"},"weighted_score_after":62.0,"stage_label_after":"Stage2-Watch/Blocked","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score","customer_concentration_penalty","unit_economics_score","margin_conversion_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin conversion in EV/body/chassis suppliers and blocks customer-concentration or platform-volume narratives without margin pass-through / unit economics.","MFE_90D_pct":3.12,"MAE_90D_pct":-24.99,"score_return_alignment_label":"corrected_false_positive_or_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L15_C29_403550_2022_MOBILITY_PLATFORM_IPO_UNIT_ECONOMICS_FALSE","trigger_id":"T_R9L15_403550_STAGE2_20220822","symbol":"403550","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":44,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":58,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"volume_route_score":50,"mix_asp_score":"unknown_or_not_supported","margin_conversion_score":4,"customer_concentration_penalty":"unknown_or_not_supported","unit_economics_score":8},"weighted_score_before":75.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":3,"relative_strength_score":28,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":30,"execution_risk_score":76,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"volume_route_score":50,"mix_asp_score":"unknown_or_not_supported","margin_conversion_score":4,"customer_concentration_penalty":"unknown_or_not_supported","unit_economics_score":0},"weighted_score_after":58.0,"stage_label_after":"Stage2-Watch/Blocked","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score","customer_concentration_penalty","unit_economics_score","margin_conversion_score"],"component_delta_explanation":"C29 shadow profile rewards actual margin conversion in EV/body/chassis suppliers and blocks customer-concentration or platform-volume narratives without margin pass-through / unit economics.","MFE_90D_pct":12.55,"MAE_90D_pct":-42.59,"score_return_alignment_label":"corrected_false_positive_or_high_MAE","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c29_supplier_margin_conversion_boost,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"EV/body/chassis suppliers with relative strength plus margin conversion produced high MFE and manageable MAE","keeps 015750/010690 positives while not loosening global Green","T_R9L15_015750_STAGE2_20230216|T_R9L15_010690_STAGE2_20230309",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c29_customer_concentration_without_margin_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"EV customer-quality/volume without margin pass-through produced low MFE and high MAE","blocks 009900-style false positives","T_R9L15_009900_STAGE2_20230811",1,1,1,medium,canonical_shadow_only,"not production; strengthens existing non-price evidence requirement"
shadow_weight,c29_mobility_platform_unit_economics_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"mobility-platform volume without unit economics produced deep MAE after IPO trigger","blocks 403550-style volume-only platform promotion","T_R9L15_403550_STAGE2_20220822",1,1,1,medium,canonical_shadow_only,"not production; platform volume requires unit economics"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"15","scheduled_round":"R9","scheduled_loop":"15","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":4,"diversity_score_summary":"same_archetype_new_symbol +16; new_symbol +12; new_trigger_family +16; counterexample_gap +4; residual_error +20; wrong_round_penalty 0; estimated +68","tested_existing_calibrated_axes":["stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","current_profile_4C_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all representative cases have forward 180D windows and clean calibration rows; evidence URL extraction deferred","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
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

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

completed_round = R9
completed_loop = 15
next_round = R10
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass

## 28. Source Notes

- Manifest validated: atlas/manifest.json; max_date 2026-02-20; raw_unadjusted_marcap; tradable shard root atlas/ohlcv_tradable_by_symbol_year.
- Schema validated: atlas/schema.json; tradable columns d,o,h,l,c,v,a,mc,s,m; MFE/MAE formulas confirmed.
- Profiles validated: 015750, 010690, 009900, 403550. Corporate-action candidate dates do not overlap representative 180D windows, and 403550 has no corporate-action candidates.
- OHLC rows used: 015750 2023; 010690 2023; 009900 2023/2024; 403550 2022/2023.
- This MD is a historical calibration artifact. It is not a live candidate scan, recommendation, or production scoring patch.
