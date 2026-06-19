# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: "v12_sector_archetype_residual"
research_session: "post_calibrated_sector_archetype_residual_research"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R2"
selected_loop: 112
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE"
fine_archetype_id: "C10_SEMI_EQUIPMENT_COMPONENT_MEMORY_RECOVERY_ORDER_REVENUE_MARGIN_BRIDGE_VS_LATE_CYCLE_RS_FADE"
deep_sub_archetype_id: "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
output_filename: "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md"
price_source: "Songdaiki/stock-web"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 3 counterexamples, and 4 residual errors for R2/L2/C10.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated_proxy`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- already-applied global axes tested here: `stage2_actionable_evidence_bonus`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `local_4b_watch_guard`.
- This MD does not patch production scoring. All rule language is shadow-only and canonical-archetype-scoped.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | `R2` |
| selected_loop | `112` |
| large_sector_id | `L2_AI_SEMICONDUCTOR_ELECTRONICS` |
| canonical_archetype_id | `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE` |
| fine_archetype_id | `C10_SEMI_EQUIPMENT_COMPONENT_MEMORY_RECOVERY_ORDER_REVENUE_MARGIN_BRIDGE_VS_LATE_CYCLE_RS_FADE` |
| deep_sub_archetype_id | `C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA` |

C10 is treated as a memory-recovery equipment-cycle archetype, not a generic semiconductor theme bucket. The row selection therefore separates equipment/component names that merely rode memory beta from those that created a verified recovery-band MFE with a tolerable MAE profile.

## 3. Previous Coverage / Duplicate Avoidance Check

- Published No-Repeat Index baseline: C10 has 13 representative rows and needs 17 more to 30 / 37 more to 50.
- Local session carry-forward before this loop: C10 loop109/110/111 added approximately 18 representative triggers, moving C10 to about 31. This loop adds 5 new C10 symbols relative to those local loops.
- Excluded prior local C10 symbols: `036930`, `039030`, `084370`, `089030`, `095610`, `240810`, `031980`, `036200`, `036810`, `039440`, `042700`, `079370`, `101490`, `074600`, `089890`, `166090`, `183300`, `319660`.
- Selected symbols: `049080`, `053610`, `083310`, `098460`, `159010`. They are all new within local C10 loops 109~111.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_window_trading_days | corporate_action_window_status | calibration_usable |
|---|---:|---:|---|---:|
| 053610 | 2025-01-02 | 180 | clean_180D_window | true |
| 098460 | 2025-01-02 | 180 | clean_180D_window | true |
| 049080 | 2024-03-04 | 180 | clean_180D_window | true |
| 083310 | 2024-05-02 | 180 | clean_180D_window | true |
| 159010 | 2024-05-02 | 180 | clean_180D_window | true |

All representative trigger rows have clean 180D windows against each symbol profile caveat set used in this loop. Corporate-action candidate dates exist in older windows for some symbols, but none overlaps each selected entry_date through D+180.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression reason |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | vacuum pump / RF equipment / dispensing-packaging / gasline component / AOI-SPI inspection | All routes test whether memory recovery beta becomes actual order/revenue/margin bridge or fades as late-cycle RS. |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | role | entry_date | outcome |
|---|---|---|---|---|---|---|
| R2L112-C10-001 | 053610 | 프로텍 | Stage2-Actionable | structural_success | 2025-01-02 | positive |
| R2L112-C10-002 | 098460 | 고영 | Stage2-Actionable | structural_success_high_mfe | 2025-01-02 | positive |
| R2L112-C10-003 | 049080 | 기가레인 | Stage4B | failed_rerating_price_only_beta | 2024-03-04 | counterexample |
| R2L112-C10-004 | 083310 | 엘오티베큠 | Stage4B | failed_rerating_vacuum_pump_late_cycle | 2024-05-02 | counterexample |
| R2L112-C10-005 | 159010 | 아스플로 | Stage4B | failed_rerating_gasline_component | 2024-05-02 | counterexample |

## 8. Positive vs Counterexample Balance

- positive_case_count: `2`
- counterexample_count: `3`
- 4B_case_count: `3`
- 4C_case_count: `0`
- The balance is deliberately counterexample-heavy because C10 published rows already show high Stage2 hit rates but still need guards against price-led beta that lacks order/revenue conversion.

## 9. Evidence Source Map

| symbol | evidence_available_at_that_date | evidence_source_status | URL repair status |
|---|---|---|---|
| 053610 | 2024 장비 cycle drawdown 이후 2025년 초 회복 band에서 고부가 패키징/dispensing equipment route가 다시 MFE를 만들었지만, Green은 order·revenue·margin bridge 확인 전에는 지연해야 한다. | source_proxy_only | promotion_blocked_until_url_repair |
| 098460 | 검사장비 platform은 2025년 초 강한 회복 MFE를 만들었지만 AI/robotics label 혼입이 크므로 C10에서는 memory-order revenue bridge가 없는 Green 승격을 막아야 한다. | source_proxy_only | promotion_blocked_until_url_repair |
| 049080 | RF/semiconductor equipment beta가 메모리 회복 기대에 먼저 반응했지만 30/90/180D MFE가 얕고 MAE가 깊어, order·revenue bridge가 없는 Stage2/Yellow는 false positive로 본다. | source_proxy_only | promotion_blocked_until_url_repair |
| 083310 | 진공펌프 equipment route는 메모리 회복 label만으로는 2024 하반기 drawdown을 방어하지 못했다. C10은 order/revenue/margin bridge가 없는 recovery beta를 4B-watch로 낮춰야 한다. | source_proxy_only | promotion_blocked_until_url_repair |
| 159010 | 반도체 gas line/component supplier는 memory capex beta와 설비투자 기대만으로는 2024년 깊은 drawdown을 피하지 못했다. 고객 order conversion 확인 전 Stage2-Actionable을 제한해야 한다. | source_proxy_only | promotion_blocked_until_url_repair |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path |
|---|---|---|
| 053610 | `atlas/ohlcv_tradable_by_symbol_year/053/053610/2025.csv` | `atlas/symbol_profiles/053/053610.json` |
| 098460 | `atlas/ohlcv_tradable_by_symbol_year/098/098460/2025.csv` | `atlas/symbol_profiles/098/098460.json` |
| 049080 | `atlas/ohlcv_tradable_by_symbol_year/049/049080/2024.csv` | `atlas/symbol_profiles/049/049080.json` |
| 083310 | `atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv` | `atlas/symbol_profiles/083/083310.json` |
| 159010 | `atlas/ohlcv_tradable_by_symbol_year/159/159010/2024.csv` | `atlas/symbol_profiles/159/159010.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
|---|---|---:|---:|---:|---:|---:|---|
| R2L112-C10-001-T1 | Stage2-Actionable | 2025-01-02 | 2025-01-02 | 22400 | 31.7 | -11.07 | current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band |
| R2L112-C10-002-T1 | Stage2-Actionable | 2025-01-02 | 2025-01-02 | 8890 | 150.28 | -8.32 | current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter |
| R2L112-C10-003-T1 | Stage4B | 2024-03-04 | 2024-03-04 | 1235 | 3.48 | -42.67 | current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge |
| R2L112-C10-004-T1 | Stage4B | 2024-05-02 | 2024-05-02 | 20000 | 4.5 | -50.95 | current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break |
| R2L112-C10-005-T1 | Stage4B | 2024-05-02 | 2024-05-02 | 11250 | 5.24 | -39.91 | current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 053610 | 22400 | 31.7 | -4.46 | 31.7 | -11.07 | 43.53 | -11.07 | 2025-09-25 | 32150 | -4.98 |
| 098460 | 8890 | 150.28 | -8.32 | 150.28 | -8.32 | 150.28 | -8.32 | 2025-02-18 | 22250 | -46.38 |
| 049080 | 1235 | 3.48 | -39.03 | 3.48 | -42.67 | 3.48 | -51.5 | 2024-03-14 | 1278 | -53.13 |
| 083310 | 20000 | 4.5 | -18.6 | 4.5 | -50.95 | 4.5 | -63.65 | 2024-05-09 | 20900 | -65.22 |
| 159010 | 11250 | 5.24 | -15.56 | 5.24 | -39.91 | 5.24 | -65.87 | 2024-05-09 | 11840 | -67.57 |

## 13. Current Calibrated Profile Stress Test

| symbol | current_profile_verdict | stress-test interpretation | shadow route |
|---|---|---|---|
| 053610 | current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band | Stage2-Actionable can be allowed, but Yellow/Green must wait for verified order/revenue/margin bridge. | Stage2-Actionable_guarded |
| 098460 | current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter | Stage2-Actionable can be allowed, but Yellow/Green must wait for verified order/revenue/margin bridge. | Stage2-Actionable_with_Green_bridge_guard |
| 049080 | current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge | Memory recovery beta without bridge becomes late-cycle 4B watch; price-only RS should not promote positive stage. | Stage4B_watch |
| 083310 | current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break | Memory recovery beta without bridge becomes late-cycle 4B watch; price-only RS should not promote positive stage. | Stage4B_watch |
| 159010 | current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion | Memory recovery beta without bridge becomes late-cycle 4B watch; price-only RS should not promote positive stage. | Stage4B_watch |

## 14. Stage2 / Yellow / Green Comparison

- Stage2-Actionable positives: 053610, 098460. These produce strong 180D MFE, but both remain `guarded` because URL-level order/revenue evidence is pending.
- Yellow/Green blocked positives: both positives lack enough verified bridge fields in this MD, so the proposed C10 shadow rule does not relax Stage3-Yellow or Stage3-Green.
- Counterexamples: 049080, 083310, 159010 show low 180D MFE and deep MAE when C10 is treated as memory beta rather than confirmed order cycle.
- green_lateness_ratio: not_applicable for all rows because this loop uses one representative trigger per case and no confirmed Stage3-Green trigger.

## 15. 4B Local vs Full-window Timing Audit

| symbol | trigger_type | four_b_evidence_type | four_b_timing_verdict |
|---|---|---|---|
| 053610 | Stage2-Actionable | bridge_required_before_full_4B_or_Green | Stage2_allowed_but_local_4B_watch_if_price_rerates_without_bridge |
| 098460 | Stage2-Actionable | bridge_required_before_full_4B_or_Green | Stage2_allowed_but_local_4B_watch_if_price_rerates_without_bridge |
| 049080 | Stage4B | price_only|positioning_overheat|missing_order_revenue_bridge | local_4B_watch_after_price_beta_fades_without_order_bridge |
| 083310 | Stage4B | price_only|positioning_overheat|missing_order_revenue_bridge | local_4B_watch_after_price_beta_fades_without_order_bridge |
| 159010 | Stage4B | price_only|positioning_overheat|missing_order_revenue_bridge | local_4B_watch_after_price_beta_fades_without_order_bridge |

## 16. 4C Protection Audit

- No trigger row is promoted directly to Stage4C in this loop because the non-price evidence is source-proxy-only. Deep MAE cases are used for `Stage4B-watch` guardrail calibration rather than hard thesis-break routing.
- 4C label: `thesis_break_watch_only` until confirmed order cut, customer cancellation, or margin/revision break is URL repaired.

## 17. Sector-Specific Rule Candidate

- rule_scope: `sector_specific`
- candidate: In L2 semiconductor equipment, memory-recovery beta should not reach Yellow unless order/revenue/margin bridge exists; however, post-reset recovery-band entries may remain Stage2-Actionable if MAE is controlled and subsequent MFE confirms recovery.
- confidence: `medium_after_url_repair`, `low_for_immediate_promotion`.

## 18. Canonical-Archetype Rule Candidate

- rule_scope: `canonical_archetype_specific`
- new_axis_proposed: `C10_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_component_RS_to_4B_watch_v2`
- existing_axis_strengthened: `stage2_required_bridge`, `local_4b_watch_guard`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`
- existing_axis_weakened: `null`

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 5 | 39.04 | -30.58 | 41.41 | -40.08 | 0.6 | too permissive if all memory beta is allowed as Actionable/Yellow |
| P0b_e2r_2_0_baseline_reference | 5 | 39.04 | -30.58 | 41.41 | -40.08 | 0.6 | misses bridge distinction; more theme-beta exposure |
| P1_L2_sector_specific_candidate | 2 | 90.99 | -9.7 | 96.91 | -9.7 | 0.0 | better alignment after bridge filter |
| P2_C10_canonical_candidate | 2 | 90.99 | -9.7 | 96.91 | -9.7 | 0.0 | best canonical compression for C10 |
| P3_counterexample_guard_profile | 3 | 4.41 | -44.51 | 4.41 | -60.34 | 1.0 | blocks deep-MAE beta traps into 4B-watch |

## 20. Score-Return Alignment Matrix

| case_id | before_score/stage | after_score/stage | MFE_180D_pct | MAE_180D_pct | alignment |
|---|---|---|---:|---:|---|
| R2L112-C10-001 | 68/Stage4B_watch_or_blocked_proxy | 78/Stage2-Actionable_guarded | 43.53 | -11.07 | actionable_recovery_kept_but_green_blocked_without_bridge |
| R2L112-C10-002 | 77/Stage2-Actionable_proxy | 79/Stage2-Actionable_with_Green_bridge_guard | 150.28 | -8.32 | actionable_recovery_kept_but_green_blocked_without_bridge |
| R2L112-C10-003 | 76/Stage2-Actionable_or_Yellow_proxy | 45/Stage4B_watch | 3.48 | -51.5 | shadow_filter_improves_alignment |
| R2L112-C10-004 | 74/Stage2-Actionable_proxy | 42/Stage4B_watch | 4.5 | -63.65 | shadow_filter_improves_alignment |
| R2L112-C10-005 | 73/Stage2-Actionable_proxy | 41/Stage4B_watch | 5.24 | -65.87 | shadow_filter_improves_alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | C10_SEMI_EQUIPMENT_COMPONENT_MEMORY_RECOVERY_ORDER_REVENUE_MARGIN_BRIDGE_VS_LATE_CYCLE_RS_FADE | 2 | 3 | 3 | 0 | 5 | 0 | 5 | 5 | 4 | true | true | C10 base index 13 + local loop109/110/111 approx 18 + loop112 5 = approx 36; above 30, below 50 |

## 22. Residual Contribution Summary

new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
residual_error_types_found: ["memory_beta_false_positive", "late_cycle_component_RS_fade", "recovery_band_missed_structural"]
new_axis_proposed: C10_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_component_RS_to_4B_watch_v2
existing_axis_strengthened: ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"]
existing_axis_weakened: null
existing_axis_kept: ["stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min"]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

- Validation scope: stock-web tradable_raw OHLC path, 30/90/180D MFE/MAE, clean 180D corporate-action window, duplicate avoidance against local C10 loops 109~111.
- Non-validation scope: production scoring change, live stock recommendation, current watchlist creation, brokerage/API action.
- Data-quality caveat: evidence_source is source_proxy_only for all cases, so positive promotion is blocked until URL repair even though price-path fields are calibration-complete.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_component_RS_to_4B_watch_v2,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 needs order/revenue/margin bridge before Yellow; price-only memory beta becomes local 4B watch","blocked 049080/083310/159010 beta traps; retained guarded Stage2 for 053610/098460","R2L112-C10-001-T1|R2L112-C10-002-T1|R2L112-C10-003-T1|R2L112-C10-004-T1|R2L112-C10-005-T1",5,5,3,medium_after_url_repair,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L112-C10-001", "symbol": "053610", "company_name": "프로텍", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_DISPENSING_PACKAGING_EQUIPMENT_2025_RECOVERY_ORDER_REVENUE_BRIDGE", "deep_sub_archetype_id": "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_after_C10_bridge_filter", "current_profile_verdict": "current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "2024 장비 cycle drawdown 이후 2025년 초 회복 band에서 고부가 패키징/dispensing equipment route가 다시 MFE를 만들었지만, Green은 order·revenue·margin bridge 확인 전에는 지연해야 한다."}
{"row_type": "case", "case_id": "R2L112-C10-002", "symbol": "098460", "company_name": "고영", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_INSPECTION_PLATFORM_RECOVERY_BAND_WITH_LABEL_MIX_GUARD", "deep_sub_archetype_id": "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA", "case_type": "structural_success_high_mfe", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_after_C10_bridge_filter", "current_profile_verdict": "current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "검사장비 platform은 2025년 초 강한 회복 MFE를 만들었지만 AI/robotics label 혼입이 크므로 C10에서는 memory-order revenue bridge가 없는 Green 승격을 막아야 한다."}
{"row_type": "case", "case_id": "R2L112-C10-003", "symbol": "049080", "company_name": "기가레인", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_RF_COMPONENT_EQUIPMENT_PRICE_BETA_LOCAL_4B_WATCH", "deep_sub_archetype_id": "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA", "case_type": "failed_rerating_price_only_beta", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_after_C10_bridge_filter", "current_profile_verdict": "current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "RF/semiconductor equipment beta가 메모리 회복 기대에 먼저 반응했지만 30/90/180D MFE가 얕고 MAE가 깊어, order·revenue bridge가 없는 Stage2/Yellow는 false positive로 본다."}
{"row_type": "case", "case_id": "R2L112-C10-004", "symbol": "083310", "company_name": "엘오티베큠", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_VACUUM_PUMP_EQUIPMENT_LATE_CYCLE_4B_WATCH", "deep_sub_archetype_id": "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA", "case_type": "failed_rerating_vacuum_pump_late_cycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_after_C10_bridge_filter", "current_profile_verdict": "current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "진공펌프 equipment route는 메모리 회복 label만으로는 2024 하반기 drawdown을 방어하지 못했다. C10은 order/revenue/margin bridge가 없는 recovery beta를 4B-watch로 낮춰야 한다."}
{"row_type": "case", "case_id": "R2L112-C10-005", "symbol": "159010", "company_name": "아스플로", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_GASLINE_COMPONENT_CAPEX_BETA_TO_4B_WATCH", "deep_sub_archetype_id": "C10_DEEP_VACUUM_RF_DISPENSING_GASLINE_INSPECTION_COMPONENT_RECOVERY_VS_PRICE_ONLY_MEMORY_BETA", "case_type": "failed_rerating_gasline_component", "positive_or_counterexample": "counterexample", "best_trigger": "Stage4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "score_price_alignment": "aligned_after_C10_bridge_filter", "current_profile_verdict": "current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion", "price_source": "Songdaiki/stock-web", "source_proxy_only": true, "evidence_url_pending": true, "notes": "반도체 gas line/component supplier는 memory capex beta와 설비투자 기대만으로는 2024년 깊은 drawdown을 피하지 못했다. 고객 order conversion 확인 전 Stage2-Actionable을 제한해야 한다."}
{"row_type": "trigger", "trigger_id": "R2L112-C10-001-T1", "case_id": "R2L112-C10-001", "symbol": "053610", "company_name": "프로텍", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_DISPENSING_PACKAGING_EQUIPMENT_2025_RECOVERY_ORDER_REVENUE_BRIDGE", "sector": "AI_semiconductor_electronics", "primary_archetype": "memory_recovery_equipment_cycle", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-02", "evidence_available_at_that_date": "2024 장비 cycle drawdown 이후 2025년 초 회복 band에서 고부가 패키징/dispensing equipment route가 다시 MFE를 만들었지만, Green은 order·revenue·margin bridge 확인 전에는 지연해야 한다.", "evidence_source": "source_proxy_only; URL repair pending", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "early_revision_signal_proxy", "equipment_order_recovery_proxy"], "stage3_evidence_fields": ["confirmed_margin_bridge_required", "order_to_revenue_conversion_required"], "stage4b_evidence_fields": ["late_cycle_overheat_watch_if_price_runs_without_order_revenue_bridge"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053610/2025.csv", "profile_path": "atlas/symbol_profiles/053/053610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-02", "entry_price": 22400.0, "MFE_30D_pct": 31.7, "MFE_90D_pct": 31.7, "MFE_180D_pct": 43.53, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.46, "MAE_90D_pct": -11.07, "MAE_180D_pct": -11.07, "MAE_1Y_pct": null, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": true, "peak_date": "2025-09-25", "peak_price": 32150.0, "drawdown_after_peak_pct": -4.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_if_no_verified_order_revenue_margin_bridge", "four_b_evidence_type": "watch_only_if_later_label_spike_without_bridge", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "dispensing_packaging_equipment_recovery_after_memory_capex_reset_with_revenue_bridge_needed", "current_profile_verdict": "current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|053610|Stage2-Actionable|2025-01-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true}
{"row_type": "trigger", "trigger_id": "R2L112-C10-002-T1", "case_id": "R2L112-C10-002", "symbol": "098460", "company_name": "고영", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_INSPECTION_PLATFORM_RECOVERY_BAND_WITH_LABEL_MIX_GUARD", "sector": "AI_semiconductor_electronics", "primary_archetype": "memory_recovery_equipment_cycle", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2025-01-02", "evidence_available_at_that_date": "검사장비 platform은 2025년 초 강한 회복 MFE를 만들었지만 AI/robotics label 혼입이 크므로 C10에서는 memory-order revenue bridge가 없는 Green 승격을 막아야 한다.", "evidence_source": "source_proxy_only; URL repair pending", "stage2_evidence_fields": ["relative_strength", "inspection_equipment_recovery_proxy", "capacity_or_volume_route"], "stage3_evidence_fields": ["confirmed_revision_required", "memory_customer_order_revenue_bridge_required"], "stage4b_evidence_fields": ["label_spike_or_positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098460/2025.csv", "profile_path": "atlas/symbol_profiles/098/098460.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-01-02", "entry_price": 8890.0, "MFE_30D_pct": 150.28, "MFE_90D_pct": 150.28, "MFE_180D_pct": 150.28, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.32, "MAE_90D_pct": -8.32, "MAE_180D_pct": -8.32, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-18", "peak_price": 22250.0, "drawdown_after_peak_pct": -46.38, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_if_no_verified_order_revenue_margin_bridge", "four_b_evidence_type": "watch_only_if_later_label_spike_without_bridge", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "inspection_AOI_SPI_platform_recovery_with_non_memory_AI_label_requires_bridge_filter", "current_profile_verdict": "current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|098460|Stage2-Actionable|2025-01-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true}
{"row_type": "trigger", "trigger_id": "R2L112-C10-003-T1", "case_id": "R2L112-C10-003", "symbol": "049080", "company_name": "기가레인", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_RF_COMPONENT_EQUIPMENT_PRICE_BETA_LOCAL_4B_WATCH", "sector": "AI_semiconductor_electronics", "primary_archetype": "memory_recovery_equipment_cycle", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-03-04", "evidence_available_at_that_date": "RF/semiconductor equipment beta가 메모리 회복 기대에 먼저 반응했지만 30/90/180D MFE가 얕고 MAE가 깊어, order·revenue bridge가 없는 Stage2/Yellow는 false positive로 본다.", "evidence_source": "source_proxy_only; URL repair pending", "stage2_evidence_fields": ["relative_strength_only", "memory_recovery_label_proxy"], "stage3_evidence_fields": ["no_confirmed_margin_bridge", "no_confirmed_order_revenue_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_or_positioning_overheat", "missing_order_revenue_bridge"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/049/049080/2024.csv", "profile_path": "atlas/symbol_profiles/049/049080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-04", "entry_price": 1235.0, "MFE_30D_pct": 3.48, "MFE_90D_pct": 3.48, "MFE_180D_pct": 3.48, "MFE_1Y_pct": 3.48, "MFE_2Y_pct": null, "MAE_30D_pct": -39.03, "MAE_90D_pct": -42.67, "MAE_180D_pct": -51.5, "MAE_1Y_pct": -61.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 1278.0, "drawdown_after_peak_pct": -53.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_if_no_verified_order_revenue_margin_bridge", "four_b_evidence_type": "price_only|positioning_overheat|missing_order_revenue_bridge", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "RF_substrate_equipment_price_beta_without_memory_order_revenue_bridge", "current_profile_verdict": "current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|049080|Stage4B|2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true}
{"row_type": "trigger", "trigger_id": "R2L112-C10-004-T1", "case_id": "R2L112-C10-004", "symbol": "083310", "company_name": "엘오티베큠", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_VACUUM_PUMP_EQUIPMENT_LATE_CYCLE_4B_WATCH", "sector": "AI_semiconductor_electronics", "primary_archetype": "memory_recovery_equipment_cycle", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-05-02", "evidence_available_at_that_date": "진공펌프 equipment route는 메모리 회복 label만으로는 2024 하반기 drawdown을 방어하지 못했다. C10은 order/revenue/margin bridge가 없는 recovery beta를 4B-watch로 낮춰야 한다.", "evidence_source": "source_proxy_only; URL repair pending", "stage2_evidence_fields": ["equipment_label_proxy", "relative_strength_faded"], "stage3_evidence_fields": ["no_margin_bridge", "no_revision_confirmation"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak", "execution_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/083/083310/2024.csv", "profile_path": "atlas/symbol_profiles/083/083310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-02", "entry_price": 20000.0, "MFE_30D_pct": 4.5, "MFE_90D_pct": 4.5, "MFE_180D_pct": 4.5, "MFE_1Y_pct": 4.5, "MFE_2Y_pct": null, "MAE_30D_pct": -18.6, "MAE_90D_pct": -50.95, "MAE_180D_pct": -63.65, "MAE_1Y_pct": -63.65, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 20900.0, "drawdown_after_peak_pct": -65.22, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_if_no_verified_order_revenue_margin_bridge", "four_b_evidence_type": "price_only|positioning_overheat|missing_order_revenue_bridge", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "vacuum_pump_memory_recovery_label_without_margin_revision_bridge", "current_profile_verdict": "current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|083310|Stage4B|2024-05-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true}
{"row_type": "trigger", "trigger_id": "R2L112-C10-005-T1", "case_id": "R2L112-C10-005", "symbol": "159010", "company_name": "아스플로", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "C10_GASLINE_COMPONENT_CAPEX_BETA_TO_4B_WATCH", "sector": "AI_semiconductor_electronics", "primary_archetype": "memory_recovery_equipment_cycle", "loop_objective": "coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery", "trigger_type": "Stage4B", "trigger_date": "2024-05-02", "evidence_available_at_that_date": "반도체 gas line/component supplier는 memory capex beta와 설비투자 기대만으로는 2024년 깊은 drawdown을 피하지 못했다. 고객 order conversion 확인 전 Stage2-Actionable을 제한해야 한다.", "evidence_source": "source_proxy_only; URL repair pending", "stage2_evidence_fields": ["capacity_or_volume_route_proxy", "relative_strength_only"], "stage3_evidence_fields": ["no_customer_quality_confirmation", "no_margin_bridge"], "stage4b_evidence_fields": ["price_only_local_peak", "execution_risk", "missing_customer_order_conversion"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/159/159010/2024.csv", "profile_path": "atlas/symbol_profiles/159/159010.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-05-02", "entry_price": 11250.0, "MFE_30D_pct": 5.24, "MFE_90D_pct": 5.24, "MFE_180D_pct": 5.24, "MFE_1Y_pct": 5.24, "MFE_2Y_pct": null, "MAE_30D_pct": -15.56, "MAE_90D_pct": -39.91, "MAE_180D_pct": -65.87, "MAE_1Y_pct": -65.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 11840.0, "drawdown_after_peak_pct": -67.57, "green_lateness_ratio": null, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "local_4B_watch_if_no_verified_order_revenue_margin_bridge", "four_b_evidence_type": "price_only|positioning_overheat|missing_order_revenue_bridge", "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "gasline_component_memory_capex_beta_without_customer_order_conversion", "current_profile_verdict": "current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|159010|Stage4B|2024-05-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true, "promotion_blocked_until_url_repair": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L112-C10-001", "trigger_id": "R2L112-C10-001-T1", "symbol": "053610", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 16, "order_intake_quality_score": 8, "fcf_conversion_score": 4, "positioning_overheat_score": 6}, "weighted_score_before": 68, "stage_label_before": "Stage4B_watch_or_blocked_proxy", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 16, "order_intake_quality_score": 12, "fcf_conversion_score": 8, "positioning_overheat_score": 6}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable_guarded", "changed_components": ["order_revenue_margin_bridge", "local_4b_watch_guard", "late_cycle_component_RS_filter"], "component_delta_explanation": "C10 shadow candidate separates memory recovery order/revenue bridge from price-only equipment/component beta. Positive rows remain guarded Stage2; beta traps move to local 4B watch.", "MFE_90D_pct": 31.7, "MAE_90D_pct": -11.07, "score_return_alignment_label": "candidate_better", "current_profile_verdict": "current_profile_missed_structural_if_2024_memory_drawdown_blocks_2025_recovery_band"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L112-C10-002", "trigger_id": "R2L112-C10-002-T1", "symbol": "098460", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 16, "order_intake_quality_score": 8, "fcf_conversion_score": 4, "positioning_overheat_score": 6}, "weighted_score_before": 77, "stage_label_before": "Stage2-Actionable_proxy", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 9, "relative_strength_score": 18, "customer_quality_score": 12, "policy_or_regulatory_score": 2, "valuation_repricing_score": 10, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 16, "order_intake_quality_score": 12, "fcf_conversion_score": 8, "positioning_overheat_score": 6}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable_with_Green_bridge_guard", "changed_components": ["order_revenue_margin_bridge", "local_4b_watch_guard", "late_cycle_component_RS_filter"], "component_delta_explanation": "C10 shadow candidate separates memory recovery order/revenue bridge from price-only equipment/component beta. Positive rows remain guarded Stage2; beta traps move to local 4B watch.", "MFE_90D_pct": 150.28, "MAE_90D_pct": -8.32, "score_return_alignment_label": "candidate_better", "current_profile_verdict": "current_profile_correct_on_stage2_but_green_requires_memory_order_bridge_filter"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L112-C10-003", "trigger_id": "R2L112-C10-003-T1", "symbol": "049080", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 10, "order_intake_quality_score": 8, "fcf_conversion_score": 4, "positioning_overheat_score": 16}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_or_Yellow_proxy", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "order_intake_quality_score": 2, "fcf_conversion_score": 1, "positioning_overheat_score": 20}, "weighted_score_after": 45, "stage_label_after": "Stage4B_watch", "changed_components": ["order_revenue_margin_bridge", "local_4b_watch_guard", "late_cycle_component_RS_filter"], "component_delta_explanation": "C10 shadow candidate separates memory recovery order/revenue bridge from price-only equipment/component beta. Positive rows remain guarded Stage2; beta traps move to local 4B watch.", "MFE_90D_pct": 3.48, "MAE_90D_pct": -42.67, "score_return_alignment_label": "candidate_better", "current_profile_verdict": "current_profile_false_positive_if_memory_beta_relative_strength_overrides_missing_order_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L112-C10-004", "trigger_id": "R2L112-C10-004-T1", "symbol": "083310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 10, "order_intake_quality_score": 8, "fcf_conversion_score": 4, "positioning_overheat_score": 16}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable_proxy", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "order_intake_quality_score": 2, "fcf_conversion_score": 1, "positioning_overheat_score": 20}, "weighted_score_after": 42, "stage_label_after": "Stage4B_watch", "changed_components": ["order_revenue_margin_bridge", "local_4b_watch_guard", "late_cycle_component_RS_filter"], "component_delta_explanation": "C10 shadow candidate separates memory recovery order/revenue bridge from price-only equipment/component beta. Positive rows remain guarded Stage2; beta traps move to local 4B watch.", "MFE_90D_pct": 4.5, "MAE_90D_pct": -50.95, "score_return_alignment_label": "candidate_better", "current_profile_verdict": "current_profile_false_positive_if_equipment_label_stays_actionable_after_MAE_break"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L112-C10-005", "trigger_id": "R2L112-C10-005-T1", "symbol": "159010", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 4, "revision_score": 5, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 10, "order_intake_quality_score": 8, "fcf_conversion_score": 4, "positioning_overheat_score": 16}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable_proxy", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 4, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 2, "valuation_repricing_score": 5, "execution_risk_score": 22, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 6, "order_intake_quality_score": 2, "fcf_conversion_score": 1, "positioning_overheat_score": 20}, "weighted_score_after": 41, "stage_label_after": "Stage4B_watch", "changed_components": ["order_revenue_margin_bridge", "local_4b_watch_guard", "late_cycle_component_RS_filter"], "component_delta_explanation": "C10 shadow candidate separates memory recovery order/revenue bridge from price-only equipment/component beta. Positive rows remain guarded Stage2; beta traps move to local 4B watch.", "MFE_90D_pct": 5.24, "MAE_90D_pct": -39.91, "score_return_alignment_label": "candidate_better", "current_profile_verdict": "current_profile_false_positive_if_component_capex_beta_promotes_without_customer_order_conversion"}
{"row_type": "shadow_weight", "axis": "C10_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_component_RS_to_4B_watch_v2", "scope": "canonical_archetype_specific", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "baseline_value": 0, "tested_value": 1, "delta": 1, "reason": "Memory recovery equipment/component beta needs order/revenue/margin bridge before Yellow; beta traps route to local 4B watch.", "backtest_effect": "Positive rows 053610/098460 retained as guarded Stage2; 049080/083310/159010 blocked from positive stage after deep MAE.", "trigger_ids": "R2L112-C10-001-T1|R2L112-C10-002-T1|R2L112-C10-003-T1|R2L112-C10-004-T1|R2L112-C10-005-T1", "calibration_usable_count": 5, "new_independent_case_count": 5, "counterexample_count": 3, "confidence": "medium_after_url_repair", "proposal_type": "canonical_shadow_only", "notes": "not production; source_proxy_only evidence requires URL repair"}
{"row_type": "residual_contribution", "round": "R2", "loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "stage4b_case_count": 3, "stage4c_case_count": 0, "current_profile_error_count": 4, "source_proxy_only_count": 5, "evidence_url_pending_count": 5, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["memory_beta_false_positive", "late_cycle_component_RS_fade", "recovery_band_missed_structural"], "new_axis_proposed": "C10_order_revenue_margin_bridge_required_before_Yellow_plus_late_cycle_component_RS_to_4B_watch_v2", "existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": [], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "promotion_blocked_until_url_repair": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<symbol>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<symbol>.json.

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

completed_round = R2
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = ["C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "C14_EV_DEMAND_SLOWDOWN_4B_4C", "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "C11_BATTERY_ORDERBOOK_RERATING", "C02_POWER_GRID_DATACENTER_CAPEX", "C01_ORDER_BACKLOG_MARGIN_BRIDGE"]
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

## 28. Source Notes

- Main execution prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- Duplicate/coverage ledger: docs/core/V12_Research_No_Repeat_Index.md
- Price atlas manifest: Songdaiki/stock-web/atlas/manifest.json
- Symbol profile checks used: 049080, 053610, 083310, 098460, 159010.

## Batch Ingest Self-Audit

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
