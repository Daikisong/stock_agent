# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| round | loop | large_sector_id | canonical_archetype_id | fine_archetype_id | mode | research_session | production_scoring_changed | shadow_weight_only | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13 | 24 | L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 | post_calibrated_sector_archetype_residual_research | False | True | 2026-02-20 |

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = `e2r_2_1_stock_web_calibrated_proxy`.

Applied global axes treated as already active, not re-proposed: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

This loop tests whether C20 beauty/global distribution needs an archetype-specific distinction between **repeat-order/global-channel evidence** and **legacy China/domestic recovery narratives**.

## 2. Round / Large Sector / Canonical Archetype Scope

- round: `R13`
- loop: `24`
- large_sector_id: `L5_CONSUMER_BRAND_DISTRIBUTION`
- canonical_archetype_id: `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`
- fine_archetype_id: `K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY`
- loop_objective: `holdout_validation`, `residual_false_positive_mining`, `residual_missed_structural_mining`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `counterexample_mining`, `coverage_gap_fill`, `4B_non_price_requirement_stress_test`

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed `stock_agent` research artifact check showed the prior calibration ledger already contains 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows across R1–R13 / loop 1–9. This loop therefore avoids re-materializing a prior global-axis proof and uses four new C20 holdout symbols from the cosmetics/global-channel family. The previous chat-created L6/C21 bank capital-return loop is also not reused.

## 4. Stock-Web OHLC Input / Price Source Validation

| source | source_url | manifest_path | schema_path | universe_path | manifest_max_date | price_basis | price_adjustment_status | calibration_shard_root | raw_shard_root | validation_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Songdaiki/stock-web | https://github.com/Songdaiki/stock-web | atlas/manifest.json | atlas/schema.json | atlas/universe/all_symbols.csv | 2026-02-20 | tradable_raw | raw_unadjusted_marcap | atlas/ohlcv_tradable_by_symbol_year | atlas/ohlcv_raw_by_symbol_year | usable_for_historical_calibration |

Manifest facts used: source_name `FinanceData/marcap`; `price_adjustment_status=raw_unadjusted_marcap`; min_date `1995-05-02`; max_date `2026-02-20`; tradable_row_count `14354401`; raw_row_count `15214118`; symbol_count `5414`; active_like_symbol_count `2868`; inactive_or_delisted_like_symbol_count `2546`; markets `KONEX`, `KOSDAQ`, `KOSDAQ GLOBAL`, `KOSPI`; calibration_shard_root `atlas/ohlcv_tradable_by_symbol_year`; raw_shard_root `atlas/ohlcv_raw_by_symbol_year`.

## 5. Historical Eligibility Gate

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | calibration_usable | forward_window_trading_days | corporate_action_window_status | calibration_block_reasons |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001_T1_STAGE2_ACTIONABLE | 257720 | 실리콘투 | Stage2-Actionable | 2024-05-10 | 2024-05-10 | 26250 | True | 180 | clean_180D_window |  |
| R13L24_C20_002_T1_STAGE2_ACTIONABLE | 018290 | 브이티 | Stage2-Actionable | 2024-05-10 | 2024-05-10 | 25400 | True | 180 | clean_180D_window |  |
| R13L24_C20_003_T1_STAGE2_YELLOW | 090430 | 아모레퍼시픽 | Stage2-Yellow | 2024-05-10 | 2024-05-10 | 170800 | True | 180 | clean_180D_window |  |
| R13L24_C20_004_T1_STAGE2_YELLOW | 018250 | 애경산업 | Stage2-Yellow | 2024-05-10 | 2024-05-10 | 21400 | True | 180 | clean_180D_window |  |
| R13L24_C20_001_T2_STAGE3_GREEN_LATE | 257720 | 실리콘투 | Stage3-Green | 2024-06-12 | 2024-06-12 | 50300 | True | 180 | clean_180D_window |  |
| R13L24_C20_001_T3_4B_PRICE_ONLY | 257720 | 실리콘투 | 4B-Overlay | 2024-06-19 | 2024-06-19 | 50700 | True | 180 | clean_180D_window |  |
| R13L24_C20_002_T2_STAGE3_GREEN_LATE | 018290 | 브이티 | Stage3-Green | 2024-06-13 | 2024-06-13 | 38000 | True | 180 | clean_180D_window |  |
| R13L24_C20_003_T2_4C_THESIS_BREAK | 090430 | 아모레퍼시픽 | 4C-ThesisBreak | 2024-08-07 | 2024-08-07 | 124500 | True | 180 | clean_180D_window |  |

All representative rows have entry dates inside stock-web tradable shards and at least 180 trading days available before the manifest max date. 2Y fields are intentionally `null` because a full 504-trading-day window is unavailable for these 2024 triggers by the 2026-02-20 manifest max date.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression_rule |
| --- | --- | --- |
| K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | Treat global channel reorder / sell-through / margin bridge as C20 positive evidence; treat legacy China/domestic recovery as guarded C20 unless repeat-order proof appears. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | calibration_usable | is_new_independent_case | notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001 | 257720 | 실리콘투 | structural_success | positive | R13L24_C20_001_T1_STAGE2_ACTIONABLE | current_profile_missed_structural | True | True | Strong C20 positive. P0 Stage2 helps, but Green confirmation can still be late because channel reorder evidence behaves like a revision proxy before formal EPS consensus catches up. |
| R13L24_C20_002 | 018290 | 브이티 | structural_success | positive | R13L24_C20_002_T1_STAGE2_ACTIONABLE | current_profile_correct | True | True | C20 positive, but drawdown after local peak warns against using price-only 4B without non-price slowdown evidence. |
| R13L24_C20_003 | 090430 | 아모레퍼시픽 | false_positive_green | counterexample | R13L24_C20_003_T1_STAGE2_YELLOW | current_profile_false_positive | True | True | Counterexample: old large-brand recovery narrative must not be treated as the same evidence family as repeat reorder/export-platform evidence. |
| R13L24_C20_004 | 018250 | 애경산업 | failed_rerating | counterexample | R13L24_C20_004_T1_STAGE2_YELLOW | current_profile_false_positive | True | True | Counterexample: Stage2 bonus is too generous for C20 if the evidence is only China/domestic recovery without repeat-order/global-channel proof. |

## 8. Positive vs Counterexample Balance

- positive_structural_success: `2` (`257720`, `018290`)
- counterexample_or_failed_rerating: `2` (`090430`, `018250`)
- 4B_or_4C_case: `2` overlay rows (`257720` price-only/valuation 4B watch, `090430` thesis-break 4C)
- calibration_usable_case_count: `4`
- new_independent_case_ratio: `1.00`

## 9. Evidence Source Map

| case_id | symbol | stage2_evidence_fields | stage3_evidence_fields | stage4b_evidence_fields | stage4c_evidence_fields | evidence_source |
| --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001 | 257720 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility, repeat_order_or_conversion | valuation_blowoff, positioning_overheat, price_only_local_peak |  | public earnings disclosure / investor material / market reports around 2024-05-10; stock-web OHLC rows verified from 257720 2024 shard |
| R13L24_C20_002 | 018290 | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, repeat_order_or_conversion, low_red_team_risk | valuation_blowoff, positioning_overheat |  | public earnings disclosure / channel evidence around 2024-05-10; stock-web OHLC rows verified from 018290 2024 and 2025 shards |
| R13L24_C20_003 | 090430 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength | multiple_public_sources | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | thesis_evidence_broken | public earnings/news narrative around 2024-05-10 and later 2024 slowdown evidence; stock-web OHLC rows verified from 090430 2024 and 2025 shards |
| R13L24_C20_004 | 018250 | public_event_or_disclosure, policy_or_regulatory_optionality |  | price_only_local_peak, margin_or_backlog_slowdown | thesis_evidence_broken | public earnings/news narrative around 2024-05-10; stock-web OHLC rows verified from 018250 2024 shard |

## 10. Price Data Source Map

| case_id | symbol | company_name | price_shard_path | profile_path | price_basis | price_adjustment_status | manifest_max_date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001 | 257720 | 실리콘투 | atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv | atlas/symbol_profiles/257/257720.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L24_C20_002 | 018290 | 브이티 | atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv | atlas/symbol_profiles/018/018290.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L24_C20_003 | 090430 | 아모레퍼시픽 | atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv | atlas/symbol_profiles/090/090430.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |
| R13L24_C20_004 | 018250 | 애경산업 | atlas/ohlcv_tradable_by_symbol_year/018/018250/2024.csv | atlas/symbol_profiles/018/018250.json | tradable_raw | raw_unadjusted_marcap | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | dedupe_for_aggregate | aggregate_group_role | trigger_outcome_label | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001_T1_STAGE2_ACTIONABLE | R13L24_C20_001 | 257720 | 실리콘투 | Stage2-Actionable | 2024-05-10 | 2024-05-10 | 26250 | True | representative | structural_success_high_mfe_green_late | current_profile_missed_structural |
| R13L24_C20_002_T1_STAGE2_ACTIONABLE | R13L24_C20_002 | 018290 | 브이티 | Stage2-Actionable | 2024-05-10 | 2024-05-10 | 25400 | True | representative | structural_success_with_high_mae_but_positive_mfe | current_profile_correct |
| R13L24_C20_003_T1_STAGE2_YELLOW | R13L24_C20_003 | 090430 | 아모레퍼시픽 | Stage2-Yellow | 2024-05-10 | 2024-05-10 | 170800 | True | representative | legacy_brand_recovery_narrative_failed_rerating | current_profile_false_positive |
| R13L24_C20_004_T1_STAGE2_YELLOW | R13L24_C20_004 | 018250 | 애경산업 | Stage2-Yellow | 2024-05-10 | 2024-05-10 | 21400 | True | representative | failed_rerating_after_local_peak | current_profile_false_positive |
| R13L24_C20_001_T2_STAGE3_GREEN_LATE | R13L24_C20_001 | 257720 | 실리콘투 | Stage3-Green | 2024-06-12 | 2024-06-12 | 50300 | False | label_comparison_only | green_late_positive | current_profile_too_late |
| R13L24_C20_001_T3_4B_PRICE_ONLY | R13L24_C20_001 | 257720 | 실리콘투 | 4B-Overlay | 2024-06-19 | 2024-06-19 | 50700 | False | 4B_overlay_only | price_only_local_4B_watch | current_profile_4B_too_early |
| R13L24_C20_002_T2_STAGE3_GREEN_LATE | R13L24_C20_002 | 018290 | 브이티 | Stage3-Green | 2024-06-13 | 2024-06-13 | 38000 | False | label_comparison_only | green_late_positive | current_profile_too_late |
| R13L24_C20_003_T2_4C_THESIS_BREAK | R13L24_C20_003 | 090430 | 아모레퍼시픽 | 4C-ThesisBreak | 2024-08-07 | 2024-08-07 | 124500 | False | 4C_overlay_only | hard_4c_success_partial | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_price_flag_30D | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001_T1_STAGE2_ACTIONABLE | 257720 | 2024-05-10 | 26250 | 106.48 | 106.48 | 106.48 | 106.48 | -17.9 | -17.9 | -17.9 | -17.9 | True | True | 2024-06-19 | 54200 | -55.35 |
| R13L24_C20_002_T1_STAGE2_ACTIONABLE | 018290 | 2024-05-10 | 25400 | 57.48 | 57.48 | 71.65 | 71.65 | -12.6 | -12.6 | -12.6 | -12.6 | True | True | 2024-12-11 | 43600 | -28.67 |
| R13L24_C20_003_T1_STAGE2_YELLOW | 090430 | 2024-05-10 | 170800 | 17.39 | 17.39 | 17.39 | 17.39 | -1.29 | -32.14 | -41.74 | -41.74 | True | True | 2024-05-31 | 200500 | -50.37 |
| R13L24_C20_004_T1_STAGE2_YELLOW | 018250 | 2024-05-10 | 21400 | 24.53 | 24.53 | 24.53 | 24.53 | -8.64 | -25.23 | -43.36 | -43.36 | True | True | 2024-05-31 | 26650 | -54.52 |
| R13L24_C20_001_T2_STAGE3_GREEN_LATE | 257720 | 2024-06-12 | 50300 | 7.75 | 7.75 | 7.75 | 7.75 | -12.03 | -36.08 | -51.89 | -51.89 | True | True | 2024-06-19 | 54200 | -55.35 |
| R13L24_C20_001_T3_4B_PRICE_ONLY | 257720 | 2024-06-19 | 50700 | 6.9 | 6.9 | 6.9 | 6.9 | -16.27 | -36.59 | -52.27 | -52.27 | True | True | 2024-06-19 | 54200 | -55.35 |
| R13L24_C20_002_T2_STAGE3_GREEN_LATE | 018290 | 2024-06-13 | 38000 | 5.26 | 5.26 | 14.74 | 14.74 | -16.71 | -31.58 | -28.42 | -28.42 | True | True | 2024-12-11 | 43600 | -28.67 |
| R13L24_C20_003_T2_4C_THESIS_BREAK | 090430 | 2024-08-07 | 124500 | 4.74 | 26.91 | 26.91 | 26.91 | -6.91 | -20.08 | -20.08 | -20.08 | True | True | 2024-09-27 | 158000 | -37.03 |

## 13. Current Calibrated Profile Stress Test

| case_id | symbol | current_profile_verdict | stage2_bonus_test | yellow_threshold_75_test | green_threshold_87_revision55_test | price_only_blowoff_guard | full_4b_non_price_requirement | hard_4c_routing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001 | 257720 | current_profile_missed_structural | useful | acceptable | too_late_when_reorder_precedes_consensus | kept | strengthened | not_primary |
| R13L24_C20_002 | 018290 | current_profile_correct | useful | acceptable | acceptable | kept | strengthened | not_primary |
| R13L24_C20_003 | 090430 | current_profile_false_positive | kept_but_needs_C20_guard | too_generous_for_legacy_recovery | should_not_green | kept | strengthened | kept_but_090430_should_route_earlier |
| R13L24_C20_004 | 018250 | current_profile_false_positive | kept_but_needs_C20_guard | too_generous_for_legacy_recovery | should_not_green | kept | strengthened | not_primary |

## 14. Stage2 / Yellow / Green Comparison

| trigger_id | symbol | trigger_type | entry_price | peak_price | green_lateness_ratio | MFE_90D_pct | MAE_90D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001_T1_STAGE2_ACTIONABLE | 257720 | Stage2-Actionable | 26250 | 54200 | not_applicable | 106.48 | -17.9 |
| R13L24_C20_002_T1_STAGE2_ACTIONABLE | 018290 | Stage2-Actionable | 25400 | 43600 | not_applicable | 57.48 | -12.6 |
| R13L24_C20_003_T1_STAGE2_YELLOW | 090430 | Stage2-Yellow | 170800 | 200500 | not_applicable | 17.39 | -32.14 |
| R13L24_C20_004_T1_STAGE2_YELLOW | 018250 | Stage2-Yellow | 21400 | 26650 | not_applicable | 24.53 | -25.23 |
| R13L24_C20_001_T2_STAGE3_GREEN_LATE | 257720 | Stage3-Green | 50300 | 54200 | 0.86 | 7.75 | -36.08 |
| R13L24_C20_002_T2_STAGE3_GREEN_LATE | 018290 | Stage3-Green | 38000 | 43600 | 0.692 | 5.26 | -31.58 |

Interpretation: `257720` and `018290` show that formal Green confirmation can become late when the market prices overseas reorder evidence before consensus revision fully lands. That is **not** a global Green relaxation; it is a C20-specific candidate where repeat-order + sell-through + margin bridge can be treated as a shadow revision proxy.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | entry_date | entry_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type | MFE_30D_pct | MAE_90D_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001_T3_4B_PRICE_ONLY | 257720 | 2024-06-19 | 50700 | 0.875 | 0.875 | price_only_local_4B_watch_only | price_only, valuation_blowoff, positioning_overheat | 6.9 | -36.59 |

The 4B row is overlay-only. It strengthens the already-applied rule that price-only local peaks should not become full 4B without non-price evidence such as revision slowdown, channel inventory saturation, margin slowdown, dilution, or explicit event cap.

## 16. 4C Protection Audit

| trigger_id | symbol | entry_date | entry_price | four_c_protection_label | MFE_90D_pct | MAE_90D_pct | drawdown_after_peak_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_003_T2_4C_THESIS_BREAK | 090430 | 2024-08-07 | 124500 | hard_4c_success | 26.91 | -20.08 | -37.03 | current_profile_4C_too_late |

`090430` shows that a legacy-brand recovery thesis can fail even after a temporary rebound. The 4C row is not an entry-weight row; it is a thesis-break/protection row.

## 17. Sector-Specific Rule Candidate

**Rule candidate: `l5_export_channel_reorder_bonus_with_legacy_guard`**

Within L5, positive promotion should require more than general consumer recovery. Add a shadow bonus when all three appear together:

1. overseas channel or distributor route evidence,
2. repeat order / sell-through / inventory-turn evidence,
3. margin bridge or financial visibility evidence.

Add a guard when the evidence is only China reopening, duty-free, domestic recovery, or large-brand narrative without repeat-order proof. This is sector-specific because consumer-brand rallies often begin with narrative heat, but only some convert into reorder economics.

## 18. Canonical-Archetype Rule Candidate

**Rule candidate: `c20_reorder_revision_proxy_and_legacy_china_guard`**

For `C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION`, channel reorder evidence can function as an early revision proxy **only** when paired with OP margin bridge and multiple public evidence families. The rule should not apply to old large-brand recovery, China reopening, or domestic mix-shift narratives unless distributor sell-through/repeat order evidence is present.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | changed_thresholds | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy |  |  | {} | 4 | 51.47 | -21.97 | 55.01 | -28.9 | 0.5 | 1 | 2 | 0.78 | mixed_positive_capture_but_false_positive_residual |
| P0b_e2r_2_0_baseline_reference | rollback_reference |  | rollback_reference_only | {} | 4 | 51.47 | -21.97 | 55.01 | -28.9 | 0.75 | 2 | 2 | 0.78 | worse_false_positive_and_late_green |
| P1_L5_sector_specific_candidate_profile | sector_specific |  | l5_channel_reorder_bonus, +l5_legacy_china_recovery_guard | {} | 4 | 81.98 | -15.25 | 89.06 | -15.25 | 0.0 | 0 | 1 | 0.776 | improved |
| P2_C20_canonical_archetype_candidate_profile | canonical_archetype_specific |  | c20_reorder_revision_proxy, +c20_margin_bridge_gate, +c20_legacy_brand_guard | {'stage3_green_revision_substitute': 'channel_reorder+inventory_sellthrough+margin_bridge'} | 4 | 81.98 | -15.25 | 89.06 | -15.25 | 0.0 | 0 | 1 | 0.776 | best_for_this_holdout |
| P3_counterexample_guard_profile | counterexample_guard |  | c20_no_reorder_no_green, c20_legacy_china_recovery_penalty | {} | 4 | 20.96 | -28.69 | 20.96 | -42.55 | 0.0 | 0 | 0 | null | guard_success |

## 20. Score-Return Alignment Matrix

| case_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R13L24_C20_001 | 257720 | 84.0 | Stage3-Yellow | 88.0 | Stage3-Green-shadow | 106.48 | -17.9 | aligned_positive |
| R13L24_C20_002 | 018290 | 82.0 | Stage3-Yellow | 86.0 | Stage3-Yellow-plus | 57.48 | -12.6 | aligned_positive |
| R13L24_C20_003 | 090430 | 77.0 | Stage3-Yellow | 68.0 | Stage2-Watch | 17.39 | -32.14 | aligned_guarded_counterexample |
| R13L24_C20_004 | 018250 | 74.0 | Stage2-Actionable | 63.0 | Stage2-Watch | 24.53 | -25.23 | aligned_guarded_counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION | K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY | 2 | 2 | 1 | 1 | 4 | 0 | 8 | 4 | 3 | True | True | C20 now has a clearer positive/counterexample split, but needs more food/beauty holdouts outside cosmetics pure-plays. |

## 22. Residual Contribution Summary

```json
{
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "reused_case_ids": [],
  "new_symbol_count": 4,
  "new_canonical_archetype_count": 0,
  "new_fine_archetype_count": 1,
  "new_trigger_family_count": 4,
  "tested_existing_calibrated_axes": [
    "stage2_actionable_evidence_bonus",
    "stage3_green_revision_min",
    "stage3_cross_evidence_green_buffer",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "residual_error_types_found": [
    "legacy_brand_false_positive",
    "green_late_when_channel_reorder_precedes_revision",
    "price_only_local_4b_watch_not_full_4b"
  ],
  "new_axis_proposed": [
    "c20_channel_reorder_revision_proxy",
    "c20_legacy_china_recovery_guard",
    "l5_price_only_local_4b_watch_guard"
  ],
  "existing_axis_strengthened": [
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence",
    "hard_4c_thesis_break_routes_to_4c"
  ],
  "existing_axis_weakened": [],
  "existing_axis_kept": [
    "stage2_actionable_evidence_bonus",
    "stage3_green_revision_min",
    "stage3_green_total_min"
  ],
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "no_new_signal_reason": null,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest fields and price-basis assumptions,
- symbol profile availability / corporate-action caveat status,
- actual OHLC trigger rows and observed extrema from stock-web tradable shards,
- 30D/90D/180D MFE/MAE proxy calculations,
- dedupe grouping and representative-trigger separation.

Not validated:
- live/current candidate scan,
- investment recommendation,
- production scoring code,
- broker/API execution,
- exact formal consensus revision database values.


## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_reorder_revision_proxy,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Channel reorder + sell-through + OP margin bridge acted like early revision evidence before consensus Green caught up.","Improved positives while preserving non-price evidence requirement","R13L24_C20_001_T1_STAGE2_ACTIONABLE|R13L24_C20_002_T1_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; v12 residual"
shadow_weight,c20_legacy_china_recovery_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Legacy China/domestic recovery narratives lacked durable global reorder evidence and produced high MAE/fade.","Blocked 090430/018250 false promotion","R13L24_C20_003_T1_STAGE2_YELLOW|R13L24_C20_004_T1_STAGE2_YELLOW",4,4,2,medium,counterexample_guard_shadow_only,"not production; v12 residual"
shadow_weight,l5_price_only_local_4b_watch_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Local peak proximity was high but not enough for full 4B without non-price slowdown.","Keeps existing 4B non-price guard","R13L24_C20_001_T3_4B_PRICE_ONLY",1,1,0,low,sector_shadow_only,"overlay only; not positive entry"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "R13L24_C20_001", "symbol": "257720", "company_name": "실리콘투", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L24_C20_001_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Strong C20 positive. P0 Stage2 helps, but Green confirmation can still be late because channel reorder evidence behaves like a revision proxy before formal EPS consensus catches up."}
{"row_type": "case", "case_id": "R13L24_C20_002", "symbol": "018290", "company_name": "브이티", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L24_C20_002_T1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "C20 positive, but drawdown after local peak warns against using price-only 4B without non-price slowdown evidence."}
{"row_type": "case", "case_id": "R13L24_C20_003", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L24_C20_003_T1_STAGE2_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: old large-brand recovery narrative must not be treated as the same evidence family as repeat reorder/export-platform evidence."}
{"row_type": "case", "case_id": "R13L24_C20_004", "symbol": "018250", "company_name": "애경산업", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L24_C20_004_T1_STAGE2_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "guard_needed", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample: Stage2 bonus is too generous for C20 if the evidence is only China/domestic recovery without repeat-order/global-channel proof."}
```

### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "R13L24_C20_001_T1_STAGE2_ACTIONABLE", "case_id": "R13L24_C20_001", "symbol": "257720", "company_name": "실리콘투", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "residual_missed_structural_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 26250, "evidence_available_at_that_date": "Q1 2024 evidence window: distributor platform sales acceleration, overseas channel expansion, and visible post-event order/revenue conversion. The trigger uses the close after public earnings/event evidence rather than later peak hindsight.", "evidence_source": "public earnings disclosure / investor material / market reports around 2024-05-10; stock-web OHLC rows verified from 257720 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 106.48, "MFE_90D_pct": 106.48, "MFE_180D_pct": 106.48, "MFE_1Y_pct": 106.48, "MFE_2Y_pct": null, "MAE_30D_pct": -17.9, "MAE_90D_pct": -17.9, "MAE_180D_pct": -17.9, "MAE_1Y_pct": -17.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -55.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_mfe_green_late", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_001_2024-05-10_26250", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L24_C20_002_T1_STAGE2_ACTIONABLE", "case_id": "R13L24_C20_002", "symbol": "018290", "company_name": "브이티", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "residual_missed_structural_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 25400, "evidence_available_at_that_date": "Q1 2024 evidence window: overseas cosmetics sell-through, repeat order route, viral product line conversion, and OP leverage evidence. The entry is anchored to public evidence availability, not to the later December rebound.", "evidence_source": "public earnings disclosure / channel evidence around 2024-05-10; stock-web OHLC rows verified from 018290 2024 and 2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 57.48, "MFE_90D_pct": 57.48, "MFE_180D_pct": 71.65, "MFE_1Y_pct": 71.65, "MFE_2Y_pct": null, "MAE_30D_pct": -12.6, "MAE_90D_pct": -12.6, "MAE_180D_pct": -12.6, "MAE_1Y_pct": -12.6, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-11", "peak_price": 43600, "drawdown_after_peak_pct": -28.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_high_mae_but_positive_mfe", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_002_2024-05-10_25400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L24_C20_003_T1_STAGE2_YELLOW", "case_id": "R13L24_C20_003", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "residual_missed_structural_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Yellow", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 170800, "evidence_available_at_that_date": "Q1 2024 evidence window: large-brand China/overseas recovery narrative existed, but durable reorder and distributor sell-through were weaker than the pure-play C20 cases. Later drawdown shows that brand recovery alone did not deserve Green-like promotion.", "evidence_source": "public earnings/news narrative around 2024-05-10 and later 2024 slowdown evidence; stock-web OHLC rows verified from 090430 2024 and 2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.39, "MFE_90D_pct": 17.39, "MFE_180D_pct": 17.39, "MFE_1Y_pct": 17.39, "MFE_2Y_pct": null, "MAE_30D_pct": -1.29, "MAE_90D_pct": -32.14, "MAE_180D_pct": -41.74, "MAE_1Y_pct": -41.74, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 200500, "drawdown_after_peak_pct": -50.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "legacy_brand_recovery_narrative_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_003_2024-05-10_170800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L24_C20_004_T1_STAGE2_YELLOW", "case_id": "R13L24_C20_004", "symbol": "018250", "company_name": "애경산업", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "residual_false_positive_mining", "residual_missed_structural_mining", "sector_specific_rule_discovery", "canonical_archetype_compression", "counterexample_mining", "coverage_gap_fill"], "trigger_type": "Stage2-Yellow", "trigger_date": "2024-05-10", "entry_date": "2024-05-10", "entry_price": 21400, "evidence_available_at_that_date": "Q1 2024 evidence window: cosmetics/household mixed narrative and China/domestic recovery optionality were present, but durable global distribution/reorder evidence and margin bridge were not strong enough. Price path faded after a short local move.", "evidence_source": "public earnings/news narrative around 2024-05-10; stock-web OHLC rows verified from 018250 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018250/2024.csv", "profile_path": "atlas/symbol_profiles/018/018250.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.53, "MFE_90D_pct": 24.53, "MFE_180D_pct": 24.53, "MFE_1Y_pct": 24.53, "MFE_2Y_pct": null, "MAE_30D_pct": -8.64, "MAE_90D_pct": -25.23, "MAE_180D_pct": -43.36, "MAE_1Y_pct": -43.36, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-31", "peak_price": 26650, "drawdown_after_peak_pct": -54.52, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating_after_local_peak", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_004_2024-05-10_21400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L24_C20_001_T2_STAGE3_GREEN_LATE", "case_id": "R13L24_C20_001", "symbol": "257720", "company_name": "실리콘투", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage3-Green", "trigger_date": "2024-06-12", "entry_date": "2024-06-12", "entry_price": 50300, "evidence_available_at_that_date": "Confirmed revision/visibility evidence was stronger by mid-June, but most upside from the Stage2 evidence had already been captured.", "evidence_source": "public earnings disclosure / investor material / market reports around 2024-05-10; stock-web OHLC rows verified from 257720 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.75, "MFE_90D_pct": 7.75, "MFE_180D_pct": 7.75, "MFE_1Y_pct": 7.75, "MFE_2Y_pct": null, "MAE_30D_pct": -12.03, "MAE_90D_pct": -36.08, "MAE_180D_pct": -51.89, "MAE_1Y_pct": -51.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -55.35, "green_lateness_ratio": 0.86, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_001_2024-06-12_50300", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_label_or_overlay_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L24_C20_001_T3_4B_PRICE_ONLY", "case_id": "R13L24_C20_001", "symbol": "257720", "company_name": "실리콘투", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "4B-Overlay", "trigger_date": "2024-06-19", "entry_date": "2024-06-19", "entry_price": 50700, "evidence_available_at_that_date": "Local/full-window peak was visible in price and valuation heat, but the row is not positive-entry calibration and should not become full 4B without non-price slowdown.", "evidence_source": "public earnings disclosure / investor material / market reports around 2024-05-10; stock-web OHLC rows verified from 257720 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/257/257720/2024.csv", "profile_path": "atlas/symbol_profiles/257/257720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.9, "MFE_90D_pct": 6.9, "MFE_180D_pct": 6.9, "MFE_1Y_pct": 6.9, "MFE_2Y_pct": null, "MAE_30D_pct": -16.27, "MAE_90D_pct": -36.59, "MAE_180D_pct": -52.27, "MAE_1Y_pct": -52.27, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-19", "peak_price": 54200, "drawdown_after_peak_pct": -55.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.875, "four_b_full_window_peak_proximity": 0.875, "four_b_timing_verdict": "price_only_local_4B_watch_only", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "price_only_local_4B_watch", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_001_2024-06-19_50700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_label_or_overlay_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L24_C20_002_T2_STAGE3_GREEN_LATE", "case_id": "R13L24_C20_002", "symbol": "018290", "company_name": "브이티", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "Stage3-Green", "trigger_date": "2024-06-13", "entry_date": "2024-06-13", "entry_price": 38000, "evidence_available_at_that_date": "Green confirmation after visible margin/channel evidence was cleaner, but occurred after a large fraction of the Stage2-to-peak move.", "evidence_source": "public earnings disclosure / channel evidence around 2024-05-10; stock-web OHLC rows verified from 018290 2024 and 2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "repeat_order_or_conversion", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018290/2024.csv", "profile_path": "atlas/symbol_profiles/018/018290.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.26, "MFE_90D_pct": 5.26, "MFE_180D_pct": 14.74, "MFE_1Y_pct": 14.74, "MFE_2Y_pct": null, "MAE_30D_pct": -16.71, "MAE_90D_pct": -31.58, "MAE_180D_pct": -28.42, "MAE_1Y_pct": -28.42, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-11", "peak_price": 43600, "drawdown_after_peak_pct": -28.67, "green_lateness_ratio": 0.692, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_positive", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_002_2024-06-13_38000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same_case_label_or_overlay_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L24_C20_003_T2_4C_THESIS_BREAK", "case_id": "R13L24_C20_003", "symbol": "090430", "company_name": "아모레퍼시픽", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "fine_archetype_id": "K_BEAUTY_GLOBAL_CHANNEL_REORDER_VS_LEGACY_CHINA_RECOVERY", "sector": "소비재·유통·브랜드", "primary_archetype": "K-beauty global distribution / reorder residual", "loop_objective": ["holdout_validation", "green_strictness_stress_test", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test"], "trigger_type": "4C-ThesisBreak", "trigger_date": "2024-08-07", "entry_date": "2024-08-07", "entry_price": 124500, "evidence_available_at_that_date": "The large-brand recovery thesis broke after the price path and follow-up evidence no longer supported durable channel/reorder conversion.", "evidence_source": "public earnings/news narrative around 2024-05-10 and later 2024 slowdown evidence; stock-web OHLC rows verified from 090430 2024 and 2025 shards", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/090/090430/2024.csv", "profile_path": "atlas/symbol_profiles/090/090430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.74, "MFE_90D_pct": 26.91, "MFE_180D_pct": 26.91, "MFE_1Y_pct": 26.91, "MFE_2Y_pct": null, "MAE_30D_pct": -6.91, "MAE_90D_pct": -20.08, "MAE_180D_pct": -20.08, "MAE_1Y_pct": -20.08, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-27", "peak_price": 158000, "drawdown_after_peak_pct": -37.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success_partial", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L24_C20_003_2024-08-07_124500", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_case_label_or_overlay_comparison", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```

### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "P2_C20_canonical_archetype_candidate_profile", "case_id": "R13L24_C20_001", "trigger_id": "R13L24_C20_001_T1_STAGE2_ACTIONABLE", "symbol": "257720", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 7, "margin_bridge_score": 14, "revision_score": 48, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 1, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 16, "global_distribution_score": 15, "legacy_china_recovery_risk_score": 0, "inventory_or_sellthrough_score": 12}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 7, "margin_bridge_score": 14, "revision_score": 48, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 1, "valuation_repricing_score": 10, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 19, "global_distribution_score": 17, "legacy_china_recovery_risk_score": 0, "inventory_or_sellthrough_score": 14}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["channel_reorder_score", "global_distribution_score", "inventory_or_sellthrough_score", "legacy_china_recovery_risk_score", "execution_risk_score"], "component_delta_explanation": "Positive pure-play export/reorder rows gain early-revision proxy credit; legacy China/domestic recovery rows lose promotion credit without repeat order or sell-through proof.", "MFE_90D_pct": 106.48, "MAE_90D_pct": -17.9, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "P2_C20_canonical_archetype_candidate_profile", "case_id": "R13L24_C20_002", "trigger_id": "R13L24_C20_002_T1_STAGE2_ACTIONABLE", "symbol": "018290", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 6, "margin_bridge_score": 13, "revision_score": 47, "relative_strength_score": 12, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 15, "global_distribution_score": 13, "legacy_china_recovery_risk_score": 0, "inventory_or_sellthrough_score": 11}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 6, "margin_bridge_score": 13, "revision_score": 47, "relative_strength_score": 12, "customer_quality_score": 11, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 18, "global_distribution_score": 15, "legacy_china_recovery_risk_score": 0, "inventory_or_sellthrough_score": 13}, "weighted_score_after": 86.0, "stage_label_after": "Stage3-Yellow-plus", "changed_components": ["channel_reorder_score", "global_distribution_score", "inventory_or_sellthrough_score", "legacy_china_recovery_risk_score", "execution_risk_score"], "component_delta_explanation": "Positive pure-play export/reorder rows gain early-revision proxy credit; legacy China/domestic recovery rows lose promotion credit without repeat order or sell-through proof.", "MFE_90D_pct": 57.48, "MAE_90D_pct": -12.6, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P2_C20_canonical_archetype_candidate_profile", "case_id": "R13L24_C20_003", "trigger_id": "R13L24_C20_003_T1_STAGE2_YELLOW", "symbol": "090430", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 6, "revision_score": 33, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "global_distribution_score": 4, "legacy_china_recovery_risk_score": -10, "inventory_or_sellthrough_score": 1}, "weighted_score_before": 77.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 6, "revision_score": 33, "relative_strength_score": 10, "customer_quality_score": 5, "policy_or_regulatory_score": 4, "valuation_repricing_score": 6, "execution_risk_score": -9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "global_distribution_score": 4, "legacy_china_recovery_risk_score": -14, "inventory_or_sellthrough_score": 1}, "weighted_score_after": 68.0, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "global_distribution_score", "inventory_or_sellthrough_score", "legacy_china_recovery_risk_score", "execution_risk_score"], "component_delta_explanation": "Positive pure-play export/reorder rows gain early-revision proxy credit; legacy China/domestic recovery rows lose promotion credit without repeat order or sell-through proof.", "MFE_90D_pct": 17.39, "MAE_90D_pct": -32.14, "score_return_alignment_label": "aligned_guarded_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P2_C20_canonical_archetype_candidate_profile", "case_id": "R13L24_C20_004", "trigger_id": "R13L24_C20_004_T1_STAGE2_YELLOW", "symbol": "018250", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 25, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 3, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "global_distribution_score": 2, "legacy_china_recovery_risk_score": -9, "inventory_or_sellthrough_score": 0}, "weighted_score_before": 74.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 1, "margin_bridge_score": 3, "revision_score": 25, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 3, "valuation_repricing_score": 3, "execution_risk_score": -10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "global_distribution_score": 2, "legacy_china_recovery_risk_score": -13, "inventory_or_sellthrough_score": 0}, "weighted_score_after": 63.0, "stage_label_after": "Stage2-Watch", "changed_components": ["channel_reorder_score", "global_distribution_score", "inventory_or_sellthrough_score", "legacy_china_recovery_risk_score", "execution_risk_score"], "component_delta_explanation": "Positive pure-play export/reorder rows gain early-revision proxy credit; legacy China/domestic recovery rows lose promotion credit without repeat order or sell-through proof.", "MFE_90D_pct": 24.53, "MAE_90D_pct": -25.23, "score_return_alignment_label": "aligned_guarded_counterexample", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c20_channel_reorder_revision_proxy,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Channel reorder + sell-through + OP margin bridge acted like early revision evidence before consensus Green caught up.","Improved positives while preserving non-price evidence requirement","R13L24_C20_001_T1_STAGE2_ACTIONABLE|R13L24_C20_002_T1_STAGE2_ACTIONABLE",4,4,2,medium,canonical_shadow_only,"not production; v12 residual"
shadow_weight,c20_legacy_china_recovery_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Legacy China/domestic recovery narratives lacked durable global reorder evidence and produced high MAE/fade.","Blocked 090430/018250 false promotion","R13L24_C20_003_T1_STAGE2_YELLOW|R13L24_C20_004_T1_STAGE2_YELLOW",4,4,2,medium,counterexample_guard_shadow_only,"not production; v12 residual"
shadow_weight,l5_price_only_local_4b_watch_guard,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION,0,1,+1,"Local peak proximity was high but not enough for full 4B without non-price slowdown.","Keeps existing 4B non-price guard","R13L24_C20_001_T3_4B_PRICE_ONLY",1,1,0,low,sector_shadow_only,"overlay only; not positive entry"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R13", "loop": "24", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["legacy_brand_false_positive", "green_late_when_channel_reorder_precedes_revision", "price_only_local_4b_watch_not_full_4b"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

- next_round: `R13_loop_25`
- suggested_next_scope: `L5_CONSUMER_BRAND_DISTRIBUTION / C18_CONSUMER_EXPORT_CHANNEL_REORDER` or `L5 / C19_BRAND_RETAIL_INVENTORY_MARGIN`
- next_gap: test whether the same reorder-vs-inventory distinction generalizes from beauty to fashion/food/export-channel cases.

## 28. Source Notes

- Stock-Web manifest: `Songdaiki/stock-web: atlas/manifest.json`.
- Symbol profiles checked: `257720`, `018290`, `090430`, `018250`.
- Tradable OHLC shards checked: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`; 2025 continuation rows checked where the 180D/1Y window crossed year boundary.
- Research-artifact duplicate check: `Songdaiki/stock_agent: reports/e2r_calibration/ingest_summary.md`.
- All scoring is research proxy scoring. No `stock_agent` production code was opened or changed.
