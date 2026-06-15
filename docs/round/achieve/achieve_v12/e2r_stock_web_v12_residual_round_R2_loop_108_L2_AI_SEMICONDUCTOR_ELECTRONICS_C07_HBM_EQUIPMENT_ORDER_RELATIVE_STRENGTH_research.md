# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_id: "R2_L108_L2_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_SECOND_PASS"
selected_round: "R2"
selected_loop: 108
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 0 / under 30 rows — C07 rows 18, need-to-30 12 in the ledger; this loop uses five C07-boundary symbols not used in the prior current-session C07 case set."
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
fine_archetype_id: "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation"
loop_objective: "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

## 1. Current Calibrated Profile Assumption

- `before_profile_id = e2r_2_1_stock_web_calibrated_proxy`
- `rollback_reference_profile_id = e2r_2_0_baseline_reference`
- `after_profile_id = proposed_L2_C07_order_conversion_shadow_profile`
- Existing global axes are stress-tested only: `stage2_required_bridge`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `local_4b_watch_guard`.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | `R2` |
| selected_loop | `108` |
| large_sector_id | `L2_AI_SEMICONDUCTOR_ELECTRONICS` |
| canonical_archetype_id | `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` |
| fine_archetype_id | `mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation` |
| round_sector_consistency | `pass` |

This is an R2 / L2 semiconductor-equipment residual calibration pass. The canonical focus is not broad semiconductor beta. It is the C07 question: whether HBM equipment relative strength is backed by named customer/order evidence and revenue conversion, or whether it is merely optionality/valuation blowoff.

## 3. Previous Coverage / Duplicate Avoidance Check

- No-Repeat Index current ledger: C07 has `18 rows`, `18 symbols`, `need to 30 = 12`.
- Prior current-session C07 loop used `089030`, `110990`, `232140`, `079370`, `039440`. This loop uses `095610`, `089970`, `322310`, `064290`, `092870`.
- Several cases are boundary holdouts previously observed in C09/C10, but this file changes the canonical question to C07 order/revenue conversion. Therefore `reuse_reason` is explicitly marked and `independent_evidence_weight` remains positive because the canonical trigger family is new.
- Hard duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`. No duplicate key is repeated inside C07 for this session.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| source_url | https://github.com/Songdaiki/stock-web |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| validation_status | usable_for_historical_calibration |

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_window_trading_days | corporate_action_window_status | calibration_usable |
|---|---:|---:|---|---|
| 095610 테스 | 2024-11-22 | 180 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 089970 브이엠 | 2025-03-19 | 180 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 322310 오로스테크놀로지 | 2024-01-17 | 475 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 064290 인텍플러스 | 2024-03-13 | 180 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |
| 092870 엑시콘 | 2024-10-25 | 180 | clean_180D_window_by_tradable_shard_and_share_continuity_proxy | true |

## 6. Canonical Archetype Compression Map

| C07 sub-path | Positive gate | Failure / 4B gate |
|---|---|---|
| named HBM/memory equipment order | named customer, delivery timing, revenue recognition | cap to Stage2/Watch if only capex theme |
| inspection/metrology HBM optionality | customer expansion plus order conversion | local 4B if fast MFE then deep MAE |
| tester / advanced packaging equipment | actual purchase order and margin bridge | Stage4B if HBM focus delays legacy tester stream or no named order |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_type | trigger_date | entry_date | entry_price | verdict |
|---|---|---|---|---|---|---|---:|---|
| `C07_R2L108_095610_DRAM_HBM_EQUIPMENT_ORDER_RECOGNITION_POSITIVE_20241122` | 095610 | 테스 | structural_success/positive | Stage3-Yellow | 2024-11-21 | 2024-11-22 | 14820 | current_profile_correct |
| `C07_R2L108_089970_HYNIX_ETCH_ORDER_UNLOCK_MISSED_STRUCTURAL_20250319` | 089970 | 브이엠 | missed_structural/positive | Stage3-Yellow | 2025-03-18 | 2025-03-19 | 10860 | current_profile_missed_structural |
| `C07_R2L108_322310_OVERLAY_METROLOGY_CUSTOMER_EXPANSION_HIGH_MAE_20240117` | 322310 | 오로스테크놀로지 | high_mae_success/positive | Stage2-Actionable | 2024-01-16 | 2024-01-17 | 26950 | current_profile_4B_too_late |
| `C07_R2L108_064290_ADV_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY_20240313` | 064290 | 인텍플러스 | failed_rerating/counterexample | Stage4B | 2024-03-12 | 2024-03-13 | 36500 | current_profile_false_positive |
| `C07_R2L108_092870_HBM_FOCUS_TESTER_ORDER_MIX_GAP_20241025` | 092870 | 엑시콘 | 4B_overlay_success/counterexample | Stage4B | 2024-10-24 | 2024-10-25 | 11450 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: `3`
- counterexample_count: `2`
- 4B_case_count: `3`
- 4C_case_count: `0`
- The sample is deliberately mixed: TES and VM test the missed-structural / named-order unlock path; Intekplus and Exicon test no-clean-order or order-mix gap; Oros tests fast-MFE/high-MAE local 4B timing.

## 9. Evidence Source Map

| symbol | evidence URL | evidence used |
|---|---|---|
| 095610 | https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf | 2024-11-22 report framed TES as DRAM equipment recovery beneficiary with order/revenue recognition path rather than a pure HBM theme. |
| 089970 | https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf | 2025-03-18 report tied VM to SK hynix vendor share, memory capex and order unlock; actual path showed strong 180D MFE with controlled MAE. |
| 322310 | https://www.sisajournal-e.com/news/articleView.html?idxno=307121 ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf | 2024-01-16 article and follow-up report pointed to overlay metrology customer expansion and advanced packaging/HBM inspection demand, but price path required local 4B after fast MFE. |
| 064290 | https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9D%B8%ED%85%8D%ED%94%8C%EB%9F%AC%EC%8A%A4.pdf | 2024-03-12 reports described advanced packaging / HBM inspection optionality, but not a named order-to-revenue conversion; this became a high-MAE counterexample. |
| 092870 | https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf | 2024-10-24 report framed Samsung HBM focus as lowering DRAM burn-in tester investment; equipment order mix gap created 4B/watch rather than clean Stage3. |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path |
|---|---|---|
| 095610 | `atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv` | `atlas/symbol_profiles/095/095610.json` |
| 089970 | `atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv` | `atlas/symbol_profiles/089/089970.json` |
| 322310 | `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv` | `atlas/symbol_profiles/322/322310.json` |
| 064290 | `atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv` | `atlas/symbol_profiles/064/064290.json` |
| 092870 | `atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv` | `atlas/symbol_profiles/092/092870.json` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | Stage2 evidence | Stage3 evidence | 4B evidence | outcome |
|---|---|---|---|---|---|
| 095610 | Stage3-Yellow | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation | none | named_memory_equipment_order_revenue_bridge_positive |
| 089970 | Stage3-Yellow | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, durable_customer_confirmation, repeat_order_or_conversion | none | hynix_memory_equipment_vendor_share_order_unlock_positive |
| 322310 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route | financial_visibility, multiple_public_sources | valuation_blowoff, positioning_overheat, price_only_local_peak | inspection_metrology_customer_expansion_fast_mfe_high_mae_4b_watch |
| 064290 | Stage4B | public_event_or_disclosure, relative_strength, capacity_or_volume_route | none | valuation_blowoff, explicit_event_cap, margin_or_backlog_slowdown | hbm_inspection_optionality_no_named_order_high_mae_counterexample |
| 092870 | Stage4B | public_event_or_disclosure, customer_or_order_quality | none | contract_delay, margin_or_backlog_slowdown, explicit_event_cap, price_only_local_peak | tester_order_mix_gap_hbm_focus_not_clean_order_conversion |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 095610 | 2024-11-22 | 14820 | 20.11 | -11.67 | 65.65 | -11.67 | 100.40 | -11.67 | 2025-08-19 | 29700 | -6.06 |
| 089970 | 2025-03-19 | 10860 | 18.32 | -13.17 | 25.51 | -13.17 | 190.06 | -13.17 | 2025-12-10 | 31500 | -7.62 |
| 322310 | 2024-01-17 | 26950 | 51.21 | -2.23 | 51.21 | -14.29 | 51.21 | -43.86 | 2024-02-27 | 40750 | -62.87 |
| 064290 | 2024-03-13 | 36500 | 6.58 | -19.73 | 6.58 | -47.97 | 6.58 | -76.00 | 2024-03-13 | 38900 | -77.48 |
| 092870 | 2024-10-25 | 11450 | 19.13 | -20.09 | 37.64 | -26.55 | 37.64 | -26.55 | 2025-02-14 | 15760 | -37.88 |

## 13. Current Calibrated Profile Stress Test

| symbol | current profile likely action | actual path | verdict |
|---|---|---|---|
| 095610 | promote or keep Stage3-Yellow | MFE90 65.65 / MAE90 -11.67; MFE180 100.40 / MAE180 -11.67 | current_profile_correct |
| 089970 | promote or keep Stage3-Yellow | MFE90 25.51 / MAE90 -13.17; MFE180 190.06 / MAE180 -13.17 | current_profile_missed_structural |
| 322310 | Stage2-Actionable but 4B watch too late | MFE90 51.21 / MAE90 -14.29; MFE180 51.21 / MAE180 -43.86 | current_profile_4B_too_late |
| 064290 | would overpromote if order-conversion gate is loose | MFE90 6.58 / MAE90 -47.97; MFE180 6.58 / MAE180 -76.00 | current_profile_false_positive |
| 092870 | would overpromote if order-conversion gate is loose | MFE90 37.64 / MAE90 -26.55; MFE180 37.64 / MAE180 -26.55 | current_profile_false_positive |

Stress-test answers: Stage2 bonus is not the issue for clean TES/VM entries; the residual error is C07-specific. The existing profile still needs a named-order/revenue-recognition gate to stop HBM equipment optionality from becoming Stage3 too early. Yellow/Green thresholds are adequate, but evidence composition inside C07 needs tightening. Price-only local 4B remains useful, but Oros shows that a fast-MFE/high-MAE path needs a C07-specific local watch even when the initial Stage2 entry was justified.

## 14. Stage2 / Yellow / Green Comparison

- TES and VM justify Stage3-Yellow because customer/order and revenue path exist.
- Oros remains Stage2-Actionable / Stage3-Yellow candidate, but Green should be blocked until repeat order and margin bridge are visible.
- Intekplus and Exicon should not move past Stage2/Watch because optionality or order-mix gap dominates.
- `green_lateness_ratio = not_applicable` for this loop because no clean Stage3-Green trigger is asserted.

## 15. 4B Local vs Full-window Timing Audit

| symbol | four_b_evidence_type | local_peak_proximity | full_window_peak_proximity | timing_verdict |
|---|---|---:|---:|---|
| 095610 | not_applicable | null | null | not_applicable |
| 089970 | not_applicable | null | null | not_applicable |
| 322310 | valuation_blowoff, positioning_overheat, price_only_local_peak | 0.95 | 0.95 | fast_mfe_high_mae_local_4B_watch_needed |
| 064290 | valuation_blowoff, explicit_event_cap, margin_or_backlog_slowdown | 1.00 | 1.00 | good_full_window_4B_timing |
| 092870 | contract_delay, margin_or_backlog_slowdown, explicit_event_cap, price_only_local_peak | 0.15 | 0.15 | watch_needed_before_clean_stage3 |

## 16. 4C Protection Audit

No hard 4C trigger is asserted. There is no contract cancellation, qualification failure, regulatory rejection, accounting break, or forced liquidation in this C07 loop. The right routing is Stage2/Stage3 gating plus Stage4B watch, not hard 4C.

## 17. Sector-Specific Rule Candidate

`L2_C07_HBM_EQUIPMENT_ORDER_TO_REVENUE_CONVERSION_GATE`

L2 semiconductor-equipment names should receive positive C07 weight only when HBM equipment relative strength is connected to named customer order, shipment/delivery timing, and revenue recognition. If the evidence is advanced packaging/HBM optionality without named order or if HBM focus delays the legacy tester stream, the case should stay Stage2/Watch or Stage4B overlay.

## 18. Canonical-Archetype Rule Candidate

`C07_NAMED_CUSTOMER_ORDER_REVENUE_CONVERSION_GATE_WITH_HIGH_MAE_4B_WATCH`

Positive unlock requires at least two of: named customer, purchase order/supply contract, delivery timing, revenue recognition visibility, or confirmed margin bridge. If these are absent and 30D/90D MAE breaches -20%, force local 4B watch even when HBM relative strength remains strong.

## 19. Before / After Backtest Comparison

| profile | scope | hypothesis | changed_axes | eligible | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| e2r_2_1_stock_web_calibrated_proxy | P0 | current calibrated proxy | no changes | 5 | 37.32 | -22.73 | 77.18 | -34.25 | 0.40 | 1 | 0 | mixed: positives found, but no-named-order false positives remain |
| e2r_2_0_baseline_reference | P0b | rollback reference | less strict bridge / higher theme beta | 5 | 37.32 | -22.73 | 77.18 | -34.25 | 0.60 | 1 | 1 | worse: would overpromote inspection/tester optionality |
| sector_specific_candidate_profile | P1 | L2 equipment order conversion gate | increase named-customer order and revenue conversion; add high-MAE 4B watch | 5 | 47.46 | -13.04 | 113.89 | -22.90 | 0.20 | 0 | 0 | better: keeps TES/VM/Oros, blocks Intekplus/Exicon |
| canonical_archetype_candidate_profile | P2 | C07 signed/named order to revenue bridge | cap optional inspection/tester stories without delivery timing | 5 | 47.46 | -13.04 | 113.89 | -22.90 | 0.20 | 0 | 0 | best shadow fit for this sample |
| counterexample_guard_profile | P3 | strict no-named-order guard | only TES/VM enter; Oros watch only | 2 | 45.58 | -12.42 | 145.23 | -12.42 | 0.00 | 1 | 0 | conservative: cleaner MAE but may miss metrology upside |

## 20. Score-Return Alignment Matrix

| symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 095610 | 78 | Stage3-Yellow | 81 | Stage3-Yellow | 65.65 | -11.67 | aligned |
| 089970 | 73 | Stage2-Actionable | 80 | Stage3-Yellow | 25.51 | -13.17 | aligned |
| 322310 | 74 | Stage2-Actionable | 70 | Stage2-Actionable + 4B Watch | 51.21 | -14.29 | aligned |
| 064290 | 67 | Stage2-Actionable | 52 | Stage1/Watch + Stage4B Overlay | 6.58 | -47.97 | misaligned_false_positive_blocked |
| 092870 | 66 | Stage2-Actionable | 54 | Stage1/Watch + Stage4B Overlay | 37.64 | -26.55 | misaligned_false_positive_blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH | mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation | 3 | 2 | 3 | 0 | 5 | 0 | 5 | 5 | 4 | L2_C07_HBM_EQUIPMENT_ORDER_TO_REVENUE_CONVERSION_GATE | C07_NAMED_CUSTOMER_ORDER_REVENUE_CONVERSION_GATE_WITH_HIGH_MAE_4B_WATCH | No-Repeat ledger C07 18 → 23 after acceptance; current-session adjusted C07 loop_107 + loop_108 = 18 → 28 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: [stage2_required_bridge, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, local_4b_watch_guard]
residual_error_types_found: [C07_missed_structural_named_order, C07_optional_inspection_false_positive, C07_order_mix_gap_4B_watch, C07_fast_MFE_high_MAE_local_4B]
new_axis_proposed: C07_NAMED_CUSTOMER_ORDER_REVENUE_CONVERSION_GATE_WITH_HIGH_MAE_4B_WATCH
existing_axis_strengthened: [stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [price_only_blowoff_blocks_positive_stage]
sector_specific_rule_candidate: L2_C07_HBM_EQUIPMENT_ORDER_TO_REVENUE_CONVERSION_GATE
canonical_archetype_rule_candidate: C07_NAMED_CUSTOMER_ORDER_REVENUE_CONVERSION_GATE_WITH_HIGH_MAE_4B_WATCH
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH.

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C07 trigger-level calibration using Stock-Web tradable OHLCV, clean 180D MFE/MAE fields, and non-price evidence available at trigger date. Non-validation scope: live stock recommendation, production score patch, brokerage execution, current watchlist construction, or live Stage3 scan.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C07_named_customer_order_revenue_conversion_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"TES/VM positive paths need named/order revenue conversion while Intekplus/Exicon fail without it","lower false positives while keeping missed structural TES/VM",C07_R2L108_095610_T1|C07_R2L108_089970_T1|C07_R2L108_322310_T1|C07_R2L108_064290_T1|C07_R2L108_092870_T1,5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C07_high_MAE_local_4B_watch,sector_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH,0,1,+1,"Oros and Intekplus show fast MFE or optionality can hide deep 90/180D MAE","route to Stage4B watch unless order and margin bridge persist",C07_R2L108_095610_T1|C07_R2L108_089970_T1|C07_R2L108_322310_T1|C07_R2L108_064290_T1|C07_R2L108_092870_T1,5,5,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C07_R2L108_095610_DRAM_HBM_EQUIPMENT_ORDER_RECOGNITION_POSITIVE_20241122", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "C07_R2L108_095610_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C10 holdout reused as C07 order-conversion boundary, new canonical trigger family"}
{"row_type": "trigger", "trigger_id": "C07_R2L108_095610_T1", "case_id": "C07_R2L108_095610_DRAM_HBM_EQUIPMENT_ORDER_RECOGNITION_POSITIVE_20241122", "symbol": "095610", "company_name": "테스", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "primary_archetype": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop_objective": "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2024-11-21", "entry_date": "2024-11-22", "entry_price": 14820.0, "evidence_available_at_that_date": "2024-11-22 report framed TES as DRAM equipment recovery beneficiary with order/revenue recognition path rather than a pure HBM theme.", "evidence_source": "https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095610/2024.csv", "profile_path": "atlas/symbol_profiles/095/095610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.11, "MFE_90D_pct": 65.65, "MFE_180D_pct": 100.4, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.67, "MAE_90D_pct": -11.67, "MAE_180D_pct": -11.67, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-08-19", "peak_price": 29700.0, "drawdown_after_peak_pct": -6.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "named_memory_equipment_order_revenue_bridge_positive", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_tradable_shard_and_share_continuity_proxy", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|095610|2024-11-22|14820.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C07_R2L108_095610_DRAM_HBM_EQUIPMENT_ORDER_RECOGNITION_POSITIVE_20241122", "trigger_id": "C07_R2L108_095610_T1", "symbol": "095610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 68, "backlog_visibility_score": 66, "margin_bridge_score": 72, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 82, "policy_or_regulatory_score": 0, "valuation_repricing_score": 62, "execution_risk_score": 35, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 74, "backlog_visibility_score": 72, "margin_bridge_score": 76, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 82, "policy_or_regulatory_score": 0, "valuation_repricing_score": 62, "execution_risk_score": 30, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 81, "stage_label_after": "Stage3-Yellow", "changed_components": ["contract_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards named customer/order-to-revenue conversion and penalizes optionality without shipment/margin bridge.", "MFE_90D_pct": 65.65, "MAE_90D_pct": -11.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "case", "case_id": "C07_R2L108_089970_HYNIX_ETCH_ORDER_UNLOCK_MISSED_STRUCTURAL_20250319", "symbol": "089970", "company_name": "브이엠", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "C07_R2L108_089970_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "C10 holdout reused as C07 HBM equipment order relative-strength missed-structural test"}
{"row_type": "trigger", "trigger_id": "C07_R2L108_089970_T1", "case_id": "C07_R2L108_089970_HYNIX_ETCH_ORDER_UNLOCK_MISSED_STRUCTURAL_20250319", "symbol": "089970", "company_name": "브이엠", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "primary_archetype": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop_objective": "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2025-03-18", "entry_date": "2025-03-19", "entry_price": 10860.0, "evidence_available_at_that_date": "2025-03-18 report tied VM to SK hynix vendor share, memory capex and order unlock; actual path showed strong 180D MFE with controlled MAE.", "evidence_source": "https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089970/2025.csv", "profile_path": "atlas/symbol_profiles/089/089970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.32, "MFE_90D_pct": 25.51, "MFE_180D_pct": 190.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.17, "MAE_90D_pct": -13.17, "MAE_180D_pct": -13.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-12-10", "peak_price": 31500.0, "drawdown_after_peak_pct": -7.62, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "hynix_memory_equipment_vendor_share_order_unlock_positive", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_tradable_shard_and_share_continuity_proxy", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089970|2025-03-19|10860.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C07_R2L108_089970_HYNIX_ETCH_ORDER_UNLOCK_MISSED_STRUCTURAL_20250319", "trigger_id": "C07_R2L108_089970_T1", "symbol": "089970", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 68, "backlog_visibility_score": 66, "margin_bridge_score": 72, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 82, "policy_or_regulatory_score": 0, "valuation_repricing_score": 62, "execution_risk_score": 35, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 78, "backlog_visibility_score": 76, "margin_bridge_score": 74, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 88, "policy_or_regulatory_score": 0, "valuation_repricing_score": 62, "execution_risk_score": 28, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow", "changed_components": ["contract_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards named customer/order-to-revenue conversion and penalizes optionality without shipment/margin bridge.", "MFE_90D_pct": 25.51, "MAE_90D_pct": -13.17, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "case", "case_id": "C07_R2L108_322310_OVERLAY_METROLOGY_CUSTOMER_EXPANSION_HIGH_MAE_20240117", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "C07_R2L108_322310_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "C09 holdout reused as C07 inspection/metrology order quality boundary"}
{"row_type": "trigger", "trigger_id": "C07_R2L108_322310_T1", "case_id": "C07_R2L108_322310_OVERLAY_METROLOGY_CUSTOMER_EXPANSION_HIGH_MAE_20240117", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "primary_archetype": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop_objective": "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-16", "entry_date": "2024-01-17", "entry_price": 26950.0, "evidence_available_at_that_date": "2024-01-16 article and follow-up report pointed to overlay metrology customer expansion and advanced packaging/HBM inspection demand, but price path required local 4B after fast MFE.", "evidence_source": "https://www.sisajournal-e.com/news/articleView.html?idxno=307121 ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "profile_path": "atlas/symbol_profiles/322/322310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 51.21, "MFE_90D_pct": 51.21, "MFE_180D_pct": 51.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.23, "MAE_90D_pct": -14.29, "MAE_180D_pct": -43.86, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-27", "peak_price": 40750.0, "drawdown_after_peak_pct": -62.87, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "fast_mfe_high_mae_local_4B_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "inspection_metrology_customer_expansion_fast_mfe_high_mae_4b_watch", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 475, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_tradable_shard_and_share_continuity_proxy", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|322310|2024-01-17|26950.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C07_R2L108_322310_OVERLAY_METROLOGY_CUSTOMER_EXPANSION_HIGH_MAE_20240117", "trigger_id": "C07_R2L108_322310_T1", "symbol": "322310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 68, "backlog_visibility_score": 66, "margin_bridge_score": 55, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 82, "policy_or_regulatory_score": 0, "valuation_repricing_score": 62, "execution_risk_score": 35, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 58, "backlog_visibility_score": 66, "margin_bridge_score": 48, "revision_score": 72, "relative_strength_score": 78, "customer_quality_score": 82, "policy_or_regulatory_score": 0, "valuation_repricing_score": 52, "execution_risk_score": 58, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable + 4B Watch", "changed_components": ["contract_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards named customer/order-to-revenue conversion and penalizes optionality without shipment/margin bridge.", "MFE_90D_pct": 51.21, "MAE_90D_pct": -14.29, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "case", "case_id": "C07_R2L108_064290_ADV_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY_20240313", "symbol": "064290", "company_name": "인텍플러스", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "C07_R2L108_064290_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C09 holdout reused as C07 no-named-order 4B guard"}
{"row_type": "trigger", "trigger_id": "C07_R2L108_064290_T1", "case_id": "C07_R2L108_064290_ADV_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY_20240313", "symbol": "064290", "company_name": "인텍플러스", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "primary_archetype": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop_objective": "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-03-12", "entry_date": "2024-03-13", "entry_price": 36500.0, "evidence_available_at_that_date": "2024-03-12 reports described advanced packaging / HBM inspection optionality, but not a named order-to-revenue conversion; this became a high-MAE counterexample.", "evidence_source": "https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9D%B8%ED%85%8D%ED%94%8C%EB%9F%AC%EC%8A%A4.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "explicit_event_cap", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv", "profile_path": "atlas/symbol_profiles/064/064290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.58, "MFE_90D_pct": 6.58, "MFE_180D_pct": 6.58, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.73, "MAE_90D_pct": -47.97, "MAE_180D_pct": -76.0, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 38900.0, "drawdown_after_peak_pct": -77.48, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "explicit_event_cap", "margin_or_backlog_slowdown"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "hbm_inspection_optionality_no_named_order_high_mae_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_tradable_shard_and_share_continuity_proxy", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|064290|2024-03-13|36500.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C07_R2L108_064290_ADV_PACKAGING_INSPECTION_OPTIONAL_ORDER_DELAY_20240313", "trigger_id": "C07_R2L108_064290_T1", "symbol": "064290", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 38, "margin_bridge_score": 25, "revision_score": 42, "relative_strength_score": 62, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 82, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 38, "margin_bridge_score": 18, "revision_score": 42, "relative_strength_score": 62, "customer_quality_score": 28, "policy_or_regulatory_score": 0, "valuation_repricing_score": 32, "execution_risk_score": 88, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch + Stage4B Overlay", "changed_components": ["contract_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards named customer/order-to-revenue conversion and penalizes optionality without shipment/margin bridge.", "MFE_90D_pct": 6.58, "MAE_90D_pct": -47.97, "score_return_alignment_label": "misaligned_blocked", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "C07_R2L108_092870_HBM_FOCUS_TESTER_ORDER_MIX_GAP_20241025", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "C07_R2L108_092870_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C10 holdout reused as C07 customer order mix gap"}
{"row_type": "trigger", "trigger_id": "C07_R2L108_092870_T1", "case_id": "C07_R2L108_092870_HBM_FOCUS_TESTER_ORDER_MIX_GAP_20241025", "symbol": "092870", "company_name": "엑시콘", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "mixed_C07_hbm_equipment_order_relative_strength_second_pass_boundary_validation", "sector": "AI_SEMICONDUCTOR_ELECTRONICS", "primary_archetype": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "loop_objective": "coverage_gap_fill | counterexample_mining | C07_C09_C10_boundary_validation | order_to_revenue_conversion_gate | 4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-10-24", "entry_date": "2024-10-25", "entry_price": 11450.0, "evidence_available_at_that_date": "2024-10-24 report framed Samsung HBM focus as lowering DRAM burn-in tester investment; equipment order mix gap created 4B/watch rather than clean Stage3.", "evidence_source": "https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["contract_delay", "margin_or_backlog_slowdown", "explicit_event_cap", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092870/2024.csv", "profile_path": "atlas/symbol_profiles/092/092870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.13, "MFE_90D_pct": 37.64, "MFE_180D_pct": 37.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.09, "MAE_90D_pct": -26.55, "MAE_180D_pct": -26.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-14", "peak_price": 15760.0, "drawdown_after_peak_pct": -37.88, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "watch_needed_before_clean_stage3", "four_b_evidence_type": ["contract_delay", "margin_or_backlog_slowdown", "explicit_event_cap", "price_only_local_peak"], "four_c_protection_label": "not_applicable_no_hard_4c", "trigger_outcome_label": "tester_order_mix_gap_hbm_focus_not_clean_order_conversion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_tradable_shard_and_share_continuity_proxy", "same_entry_group_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|092870|2024-10-25|11450.0", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C07_R2L108_092870_HBM_FOCUS_TESTER_ORDER_MIX_GAP_20241025", "trigger_id": "C07_R2L108_092870_T1", "symbol": "092870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 38, "margin_bridge_score": 25, "revision_score": 42, "relative_strength_score": 62, "customer_quality_score": 45, "policy_or_regulatory_score": 0, "valuation_repricing_score": 45, "execution_risk_score": 82, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 25, "backlog_visibility_score": 38, "margin_bridge_score": 18, "revision_score": 42, "relative_strength_score": 62, "customer_quality_score": 28, "policy_or_regulatory_score": 0, "valuation_repricing_score": 32, "execution_risk_score": 88, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch + Stage4B Overlay", "changed_components": ["contract_score", "margin_bridge_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "C07 shadow profile rewards named customer/order-to-revenue conversion and penalizes optionality without shipment/margin bridge.", "MFE_90D_pct": 37.64, "MAE_90D_pct": -26.55, "score_return_alignment_label": "misaligned_blocked", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R2", "loop": "108", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "local_4b_watch_guard"], "residual_error_types_found": ["C07_missed_structural_named_order", "C07_optional_inspection_false_positive", "C07_order_mix_gap_4B_watch", "C07_fast_MFE_high_MAE_local_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## Batch Ingest Self-Audit

```yaml
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 5
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

```text
completed_round = R2
completed_loop = 108
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / under 30 rows
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY | C02_POWER_GRID_DATACENTER_CAPEX | C14_EV_DEMAND_SLOWDOWN_4B_4C | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- No-Repeat Index: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- Stock-Web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- Stock-Web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- 095610 테스 evidence: https://file.alphasquare.co.kr/media/pdfs/company-report/%ED%95%9C%ED%99%9420241122%ED%85%8C%EC%8A%A4.pdf
- 089970 브이엠 evidence: https://www.sks.co.kr/data1/research/qna_file/20250317133336654_0_ko.pdf
- 322310 오로스테크놀로지 evidence: https://www.sisajournal-e.com/news/articleView.html?idxno=307121 ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%98%A4%EB%A1%9C%EC%8A%A4%ED%85%8C%ED%81%AC%EB%86%80%EB%A1%9C%EC%A7%80.pdf
- 064290 인텍플러스 evidence: https://files-scs.pstatic.net/2024/03/12/v2v0YGr2Ki/240312%28%ED%99%94%29%20%EC%A6%9D%EA%B6%8C%EC%82%AC%EB%A6%AC%ED%8F%AC%ED%8A%B8.pdf ; https://file.alphasquare.co.kr/media/pdfs/company-report/%EC%9D%B8%ED%85%8D%ED%94%8C%EB%9F%AC%EC%8A%A4.pdf
- 092870 엑시콘 evidence: https://stock.pstatic.net/stock-research/company/74/20241024_company_298701000.pdf
