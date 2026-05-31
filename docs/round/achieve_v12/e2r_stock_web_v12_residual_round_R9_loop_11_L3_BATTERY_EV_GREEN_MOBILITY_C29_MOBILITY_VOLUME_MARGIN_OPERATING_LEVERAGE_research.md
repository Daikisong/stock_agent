# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R9_loop_11_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round: R9
scheduled_loop: 11
completed_round: R9
completed_loop: 11
next_round: R10
next_loop: 11
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_patch_written: false
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **5 new independent cases**, **3 counterexamples**, and **3 current-profile residual errors** for `R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as existing guardrails, not re-proposed global changes:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is C29-specific: **when does mobility supplier volume evidence become a real margin/revision bridge, and when is it only a local-peak story wearing a volume mask?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 11 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD |
| round_sector_consistency | pass |

R9 uses the `L3_BATTERY_EV_GREEN_MOBILITY` branch because this run is about mobility / finished-auto supply chain names, not construction or real-estate transport infrastructure.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifact checked:

```text
reports/e2r_calibration/by_round/R9.md
```

The R9 report already contains `representative_triggers=122`, `unique_cases=28`, and a wide trigger mix including Stage2, Stage2-Actionable, Stage3-Green, Stage3-Yellow, Stage4B, Stage4C, and Stage4C-watch. Its accepted axes are cumulative/global, so this loop avoids re-arguing the global axes and adds C29-specific residual evidence instead.

Novelty gate:

```text
same canonical archetype allowed: true
same symbol + same trigger_date + same entry_date repeated: avoided
symbols already used in R9 loop10 and avoided here: 005380, 000270, 204320, 018880
new_symbol_count: 5
new_trigger_family_count: 5
minimum_new_independent_case_ratio: 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web source validation:

```text
source = Songdaiki/stock-web
source_url = https://github.com/Songdaiki/stock-web
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Manifest facts confirmed from this run:

```text
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
```

Schema facts used:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

| case_id | symbol | company | entry_date | shard | profile | forward_180D | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|---:|---|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 015750 | 성우하이텍 | 2023-02-16 | atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv | atlas/symbol_profiles/015/015750.json | 180+ | clean_180D_window | true |
| C29-SL-2023-LAMP-MARGIN-RERATING | 005850 | 에스엘 | 2023-04-25 | atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv | atlas/symbol_profiles/005/005850.json | 180+ | clean_180D_window | true |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 012330 | 현대모비스 | 2024-01-25 | atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv | atlas/symbol_profiles/012/012330.json | 180+ | clean_180D_window | true |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | 011210 | 현대위아 | 2023-06-27 | atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv | atlas/symbol_profiles/011/011210.json | 180+ | clean_180D_window | true |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | 064960 | SNT모티브 | 2023-04-12 | atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv | atlas/symbol_profiles/064/064960.json | 180+ | clean_180D_window; 2Y contaminated_or_unavailable_due_2025_corporate_action_candidate | true |

Profile caveat summary:

```text
012330 corporate_action_candidate_dates = 1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
011210 corporate_action_candidate_dates = []
015750 corporate_action_candidate_dates = 1996-07-30, 1999-05-21, 2000-04-24, 2000-07-19, 2000-08-14, 2000-08-22, 2006-04-05, 2010-09-27, 2011-11-24, 2014-06-02, 2018-07-09
005850 corporate_action_candidate_dates = 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16
064960 corporate_action_candidate_dates = 2002-12-24, 2012-12-26, 2025-01-24, 2025-02-26
```

The 064960 2023 trigger is quantitatively used through 180D only; its 2Y field is not used for calibration because later 2025 corporate-action candidates exist.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| BODY_LIGHTWEIGHT_MARGIN_CONVERSION | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Small/mid auto supplier where volume and mix only count if price action is followed by margin/revision conversion. |
| LAMP_MODULE_MIX_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Supplier margin bridge with positive MFE but meaningful local-peak drawdown. |
| MODULE_AS_LOCAL_PEAK_4B | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Large-cap parts rerating where local peak management matters more than extra Green promotion. |
| POWERTRAIN_VOLUME_FALSE_POSITIVE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Volume/relative strength without margin conversion becomes a false-positive trap. |
| EV_MOTOR_DEFENSIVE_FALSE_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV motor/defensive component narrative has narrow MFE and poor 180D asymmetry without revision support. |

## 7. Case Selection Summary

| case_id | role | positive_or_counterexample | trigger family | representative trigger | current_profile_verdict |
|---|---|---|---|---|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | structural_success | positive | body/lightweight auto parts margin conversion | TR-C29-SUNGWOO-S2A-20230216 | current_profile_missed_structural |
| C29-SL-2023-LAMP-MARGIN-RERATING | structural_success | positive | lamp/module mix margin bridge | TR-C29-SL-S2A-20230425 | current_profile_correct |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 4B_overlay_success | counterexample | module/A-S mix margin rerating with 4B local peak | TR-C29-MOBIS-S2A-20240125 | current_profile_correct |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | failed_rerating | counterexample | powertrain/machinery volume local peak | TR-C29-WIA-S2A-20230627 | current_profile_false_positive |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | false_positive_green | counterexample | EV motor/defensive component volume false bridge | TR-C29-SNTMOTIV-S2-20230412 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 2 watch-only labels
calibration_usable_case_count = 5
calibration_usable_trigger_count = 7
```

The positive cases show that C29 supplier names can be actionable before full Green when volume/mix evidence is visible. The counterexamples show that **volume route alone is too soft**: without margin bridge and revision support, the same score bucket over-promotes local peaks.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|---|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 2023-02-16 | auto lightweight/parts revenue leverage narrative converted into sharp relative strength before later confirmed margin evidence | historical public result/report proxy + stock-web price-volume row validation | public_event_or_disclosure; relative_strength; customer_or_order_quality; capacity_or_volume_route | margin_bridge; confirmed_revision; financial_visibility | valuation_blowoff; positioning_overheat | [] |
| C29-SL-2023-LAMP-MARGIN-RERATING | 2023-04-25 | component margin/mix bridge with visible price-volume confirmation before a July local peak | historical public result/report proxy + stock-web price-volume row validation | public_event_or_disclosure; relative_strength; customer_or_order_quality; early_revision_signal | margin_bridge; financial_visibility; multiple_public_sources | price_only_local_peak; valuation_blowoff | [] |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 2024-01-25 | module/A-S rerating was tradable, but the high-quality window was short and required 4B overlay discipline | historical public result/report proxy + stock-web price-volume row validation | public_event_or_disclosure; relative_strength; early_revision_signal | partial_margin_bridge; financial_visibility | valuation_blowoff; positioning_overheat; price_only_local_peak | [] |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | 2023-06-27 | local volume/relative-strength move did not convert into durable margin/revision expansion | historical public result/report proxy + stock-web price-volume row validation | public_event_or_disclosure; relative_strength; capacity_or_volume_route | unknown_or_not_supported | price_only_local_peak; margin_or_backlog_slowdown; revision_slowdown | thesis_break_watch_only |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | 2023-04-12 | EV motor/defensive component story produced only a narrow MFE and later undercut the entry path | historical public result/report proxy + stock-web price-volume row validation | public_event_or_disclosure; capacity_or_volume_route | unknown_or_not_supported | price_only_local_peak; revision_slowdown | thesis_break_watch_only |

## 10. Price Data Source Map

| symbol | profile_path | shard_paths_used | basis | adjustment |
|---:|---|---|---|---|
| 015750 | atlas/symbol_profiles/015/015750.json | atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv | tradable_raw | raw_unadjusted_marcap |
| 005850 | atlas/symbol_profiles/005/005850.json | atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv | tradable_raw | raw_unadjusted_marcap |
| 012330 | atlas/symbol_profiles/012/012330.json | atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv | tradable_raw | raw_unadjusted_marcap |
| 011210 | atlas/symbol_profiles/011/011210.json | atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv | tradable_raw | raw_unadjusted_marcap |
| 064960 | atlas/symbol_profiles/064/064960.json | atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | dedupe_for_aggregate | aggregate_group_role | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| TR-C29-SUNGWOO-S2A-20230216 | C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 015750 | Stage2-Actionable | 2023-02-16 | 2023-02-16 | 6230 | G-C29-015750-20230216 | true | representative | current_profile_missed_structural |
| TR-C29-SL-S2A-20230425 | C29-SL-2023-LAMP-MARGIN-RERATING | 005850 | Stage2-Actionable | 2023-04-25 | 2023-04-25 | 32650 | G-C29-005850-20230425 | true | representative | current_profile_correct |
| TR-C29-MOBIS-S2A-20240125 | C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 012330 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 209500 | G-C29-012330-20240125 | true | representative | current_profile_correct |
| TR-C29-WIA-S2A-20230627 | C29-WIA-2023-POWERTRAIN-LOCALPEAK | 011210 | Stage2-Actionable | 2023-06-27 | 2023-06-27 | 64100 | G-C29-011210-20230627 | true | representative | current_profile_false_positive |
| TR-C29-SNTMOTIV-S2-20230412 | C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | 064960 | Stage2 | 2023-04-12 | 2023-04-12 | 52000 | G-C29-064960-20230412 | true | representative | current_profile_false_positive |
| TR-C29-SUNGWOO-4B-20230712 | C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 015750 | Stage4B | 2023-07-12 | 2023-07-12 | 14990 | G-C29-SUNGWOO-20230712 | false | 4B_overlay_only | current_profile_correct |
| TR-C29-MOBIS-4B-20240315 | C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 012330 | Stage4B | 2024-03-15 | 2024-03-15 | 269000 | G-C29-MOBIS-20240315 | false | 4B_overlay_only | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_price_flag_30D | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct | usage |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|---:|---|
| TR-C29-SUNGWOO-S2A-20230216 | 6230 | 27.45 | 80.26 | 162.76 | null | null | -11.72 | -11.72 | -11.72 | null | false | false | 2023-07-12 | 16370 | -52.35 | representative |
| TR-C29-SL-S2A-20230425 | 32650 | 22.21 | 29.86 | 29.86 | null | null | -9.19 | -9.19 | -12.71 | null | true | true | 2023-07-17 | 42400 | -32.78 | representative |
| TR-C29-MOBIS-S2A-20240125 | 209500 | 23.15 | 28.88 | 28.88 | null | null | -3.82 | -3.82 | -4.3 | null | true | true | 2024-03-18 | 270000 | -25.74 | representative |
| TR-C29-WIA-S2A-20230627 | 64100 | 9.98 | 9.98 | 9.98 | null | null | -4.84 | -15.29 | -19.66 | null | true | true | 2023-07-06 | 70500 | -26.95 | representative |
| TR-C29-SNTMOTIV-S2-20230412 | 52000 | 5.77 | 7.5 | 8.65 | null | null | -9.42 | -9.42 | -20.38 | null | true | true | 2023-08-29 | 56500 | -26.73 | representative |
| TR-C29-SUNGWOO-4B-20230712 | 14990 | 9.21 | 9.21 | 9.21 | null | null | -22.68 | -47.97 | -47.97 | null | true | true | 2023-07-12 | 16370 | -52.35 | 4B_overlay_only |
| TR-C29-MOBIS-4B-20240315 | 269000 | 0.37 | 0.37 | 0.37 | null | null | -11.34 | -11.34 | -25.47 | null | true | true | 2024-03-18 | 270000 | -25.74 | 4B_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual path | verdict |
|---|---|---|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | Stage2/Yellow but Green delayed until margin proof | 180D MFE was very large before full confirmation; Stage2 evidence was useful | current_profile_missed_structural |
| C29-SL-2023-LAMP-MARGIN-RERATING | Stage2/Yelllow, no forced Green | Positive but drawdown after local peak justifies caution | current_profile_correct |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | Stage2/Yelllow plus later 4B overlay | Moderate rerating but local peak needed overlay discipline | current_profile_correct |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | Stage2/Yellow risk if volume route over-weighted | MFE capped near 10%, MAE widened materially | current_profile_false_positive |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | Stage2-Actionable risk if EV motor story over-weighted | Narrow MFE, poor 180D asymmetry | current_profile_false_positive |

Answers to required stress-test questions:

```text
1. current calibrated profile catches broad Stage2 actionability, but in C29 it can over-read supplier volume stories.
2. It matches Sungwoo/SL directionally, but Wia/SNT show poor score-return alignment without margin/revision conversion.
3. Stage2 bonus is useful for true conversion cases; too generous for pure volume-route suppliers.
4. Yellow threshold 75 is acceptable but needs C29 component guard.
5. Green threshold 87/revision 55 is directionally correct; for C29 suppliers, direct margin conversion can allow Yellow+ patience before Green.
6. price-only blowoff guard remains appropriate.
7. full 4B non-price requirement is strengthened by Sungwoo/Mobis overlay rows.
8. hard 4C routing should remain thesis-break based; Wia/SNT are watch-only, not hard 4C.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | later Green/confirmation proxy | peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 6230 | 10060 | 16370 | 0.38 | Green somewhat late; Stage2 captured the better asymmetric entry. |
| C29-SL-2023-LAMP-MARGIN-RERATING | 32650 | 37500 | 42400 | 0.50 | Green/confirmation is useful but gives up about half the available upside. |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 209500 | 269000 | 270000 | 0.98 | Green at the local peak is too late; use 4B overlay rather than extra promotion. |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | 64100 | not_applicable | 70500 | not_applicable | No confirmed Green; local MFE faded. |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | 52000 | not_applicable | 56500 | not_applicable | No confirmed Green; watch-only thesis break. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| TR-C29-SUNGWOO-4B-20230712 | 0.86 | 0.86 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TR-C29-MOBIS-4B-20240315 | 0.98 | 0.98 | valuation_blowoff; positioning_overheat | good_full_window_4B_timing |
| TR-C29-WIA-S2A-20230627 | null | null | price_only_local_peak | do_not_treat_as_full_4B; local peak without non-price confirmation |
| TR-C29-SNTMOTIV-S2-20230412 | null | null | price_only_local_peak | do_not_treat_as_full_4B; later thesis watch only |

## 16. 4C Protection Audit

Hard 4C is not promoted in this loop. Wia and SNT Motiv are `thesis_break_watch_only` because their evidence weakens, but there is no hard cancellation, forced liquidation, or accounting/trust break in the selected trigger window.

| case_id | four_c_protection_label | reason |
|---|---|---|
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | thesis_break_watch_only | supplier volume route did not convert into durable margin/revision evidence |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | thesis_break_watch_only | narrow MFE and widening 180D MAE justify watch-only demotion |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = supplier_volume_route_requires_margin_or_revision_confirmation
sector = L3_BATTERY_EV_GREEN_MOBILITY
proposal_type = sector_shadow_only
production_scoring_changed = false
```

Rule candidate:

```text
For L3/C29 supplier names, capacity_or_volume_route can support Stage2-Actionable,
but it cannot promote Stage3-Green unless at least one of the following is present:
1. margin_bridge_score >= 60,
2. revision_score >= 55,
3. repeat order/conversion evidence from durable customer or visible mix improvement.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
axis = mix_margin_conversion_required_for_C29_supplier_green
```

This rule separates **volume as a doorbell** from **margin/revision as the door opening**. In C29, volume headlines knock loudly, but the rerating only enters the room when margin and revision evidence follow.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 5 | 31.3 | -9.89 | 48.03 | -13.75 | 0.60 | 1 | mixed; catches Stage2 but over-promotes supplier volume stories |
| P0b_e2r_2_0_baseline_reference | rollback | 5 | 29.10 | -10.40 | 44.20 | -14.00 | 0.60 | 2 | weaker Stage2 capture; not preferred |
| P1_L3_supplier_volume_guard_profile | sector_shadow | 5 | 37.06 | -9.30 | 64.17 | -12.24 | 0.20 | 1 | better: keeps Sungwoo/SL, demotes Wia/SNT |
| P2_C29_mix_margin_conversion_profile | canonical_shadow | 5 | 37.06 | -9.30 | 64.17 | -12.24 | 0.20 | 0 | best balance for C29 supplier compression |
| P3_counterexample_guard_profile | guard_shadow | 5 | 29.86 | -9.19 | 29.86 | -12.71 | 0.00 | 1 | too defensive; may miss high-beta supplier reratings |

## 20. Score-Return Alignment Matrix

| case_id | symbol | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
|---|---:|---:|---|---:|---|---:|---:|---|
| C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING | 015750 | 74 | Stage2-Actionable | 86 | Stage3-Yellow+ | 80.26 | -11.72 | current_profile_missed_structural |
| C29-SL-2023-LAMP-MARGIN-RERATING | 005850 | 76 | Stage3-Yellow | 82 | Stage3-Yellow+ | 29.86 | -9.19 | current_profile_correct |
| C29-MOBIS-2024-MODULE-AS-LOCALPEAK | 012330 | 78 | Stage3-Yellow | 73 | Stage2-Actionable+4B-watch | 28.88 | -3.82 | current_profile_correct |
| C29-WIA-2023-POWERTRAIN-LOCALPEAK | 011210 | 76 | Stage3-Yellow | 63 | Stage2-watch | 9.98 | -15.29 | current_profile_false_positive |
| C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE | 064960 | 72 | Stage2-Actionable | 58 | Stage2-watch | 7.5 | -9.42 | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD | 2 | 3 | 2 | 2 watch-only | 5 | 0 | 7 | 5 | 3 | true | true | supplier-volume false-positive gap reduced; more 2024-2025 holdout still needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - supplier_local_peak_4B_needed
new_axis_proposed: null
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c as watch-only restraint
existing_axis_weakened:
  - none globally
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round = R9 and scheduled_loop = 11
- R9/L3/C29 consistency
- stock-web manifest max_date = 2026-02-20
- selected symbols have tradable rows and profile files
- representative trigger entry prices and MFE/MAE are based on stock-web 1D OHLC rows
- corporate-action candidates do not contaminate the selected 180D windows
- same_entry_group dedupe separates representative entries from 4B overlays
```

Not validated / not performed:

```text
- no live scan
- no current recommendation
- no brokerage API
- no stock_agent source-code access
- no production scoring patch
- no global calibration promotion
- no FinanceDataReader / pykrx / KRX / Naver route discovery
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,mix_margin_conversion_required_for_C29_supplier_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"supplier volume route must be paired with margin/revision conversion before Green","false positives in WIA/SNT are demoted while Sungwoo/SL remain actionable",TR-C29-SUNGWOO-S2A-20230216|TR-C29-WIA-S2A-20230627|TR-C29-SNTMOTIV-S2-20230412,5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,non_price_4b_required_for_supplier_local_peak,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"keeps already-applied 4B non-price requirement but adds C29 supplier local-peak examples","4B overlays captured Sungwoo/Mobis local peaks without turning price-only moves into full thesis breaks",TR-C29-SUNGWOO-4B-20230712|TR-C29-MOBIS-4B-20240315,5,5,3,medium,sector_shadow_only,"existing axis strengthened, not global re-proposal"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-SUNGWOO-S2A-20230216","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"auto lightweight/parts revenue leverage narrative converted into sharp relative strength before later confirmed margin evidence"}
{"row_type":"case","case_id":"C29-SL-2023-LAMP-MARGIN-RERATING","symbol":"005850","company_name":"에스엘","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-SL-S2A-20230425","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"component margin/mix bridge with visible price-volume confirmation before a July local peak"}
{"row_type":"case","case_id":"C29-MOBIS-2024-MODULE-AS-LOCALPEAK","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-MOBIS-S2A-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_needed","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"module/A-S rerating was tradable, but the high-quality window was short and required 4B overlay discipline"}
{"row_type":"case","case_id":"C29-WIA-2023-POWERTRAIN-LOCALPEAK","symbol":"011210","company_name":"현대위아","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-WIA-S2A-20230627","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"local volume/relative-strength move did not convert into durable margin/revision expansion"}
{"row_type":"case","case_id":"C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-SNTMOTIV-S2-20230412","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EV motor/defensive component story produced only a narrow MFE and later undercut the entry path"}
{"row_type":"trigger","trigger_id":"TR-C29-SUNGWOO-S2A-20230216","case_id":"C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-16","evidence_available_at_that_date":"auto lightweight/parts revenue leverage narrative converted into sharp relative strength before later confirmed margin evidence","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":["margin_bridge","confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-16","entry_price":6230,"MFE_30D_pct":27.45,"MFE_90D_pct":80.26,"MFE_180D_pct":162.76,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.72,"MAE_90D_pct":-11.72,"MAE_180D_pct":-11.72,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.35,"green_lateness_ratio":"not_applicable_or_case_level","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-015750-20230216","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-SL-S2A-20230425","case_id":"C29-SL-2023-LAMP-MARGIN-RERATING","symbol":"005850","company_name":"에스엘","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-25","evidence_available_at_that_date":"component margin/mix bridge with visible price-volume confirmation before a July local peak","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005850/2023.csv","profile_path":"atlas/symbol_profiles/005/005850.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-25","entry_price":32650,"MFE_30D_pct":22.21,"MFE_90D_pct":29.86,"MFE_180D_pct":29.86,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.19,"MAE_90D_pct":-9.19,"MAE_180D_pct":-12.71,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":42400,"drawdown_after_peak_pct":-32.78,"green_lateness_ratio":"not_applicable_or_case_level","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-005850-20230425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-MOBIS-S2A-20240125","case_id":"C29-MOBIS-2024-MODULE-AS-LOCALPEAK","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"module/A-S rerating was tradable, but the high-quality window was short and required 4B overlay discipline","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["partial_margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv","profile_path":"atlas/symbol_profiles/012/012330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-25","entry_price":209500,"MFE_30D_pct":23.15,"MFE_90D_pct":28.88,"MFE_180D_pct":28.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.82,"MAE_90D_pct":-3.82,"MAE_180D_pct":-4.3,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":270000,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":"not_applicable_or_case_level","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_or_overlay_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-012330-20240125","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-WIA-S2A-20230627","case_id":"C29-WIA-2023-POWERTRAIN-LOCALPEAK","symbol":"011210","company_name":"현대위아","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-27","evidence_available_at_that_date":"local volume/relative-strength move did not convert into durable margin/revision expansion","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown","revision_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2023.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-27","entry_price":64100,"MFE_30D_pct":9.98,"MFE_90D_pct":9.98,"MFE_180D_pct":9.98,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.84,"MAE_90D_pct":-15.29,"MAE_180D_pct":-19.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-06","peak_price":70500,"drawdown_after_peak_pct":-26.95,"green_lateness_ratio":"not_applicable_or_case_level","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_or_overlay_needed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-011210-20230627","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-SNTMOTIV-S2-20230412","case_id":"C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE","symbol":"064960","company_name":"SNT모티브","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2023-04-12","evidence_available_at_that_date":"EV motor/defensive component story produced only a narrow MFE and later undercut the entry path","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":["unknown_or_not_supported"],"stage4b_evidence_fields":["price_only_local_peak","revision_slowdown"],"stage4c_evidence_fields":["thesis_break_watch_only"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064960/2023.csv","profile_path":"atlas/symbol_profiles/064/064960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-12","entry_price":52000,"MFE_30D_pct":5.77,"MFE_90D_pct":7.5,"MFE_180D_pct":8.65,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-9.42,"MAE_90D_pct":-9.42,"MAE_180D_pct":-20.38,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-29","peak_price":56500,"drawdown_after_peak_pct":-26.73,"green_lateness_ratio":"not_applicable_or_case_level","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_for_representative_entry","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_or_overlay_needed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 2Y contaminated_or_unavailable_due_2025_corporate_action_candidate","same_entry_group_id":"G-C29-064960-20230412","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-SUNGWOO-4B-20230712","case_id":"C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-07-12","evidence_available_at_that_date":"non-price 4B overlay evidence is used only as risk overlay, not positive promotion","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-12","entry_price":14990,"MFE_30D_pct":9.21,"MFE_90D_pct":9.21,"MFE_180D_pct":9.21,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.68,"MAE_90D_pct":-47.97,"MAE_180D_pct":-47.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":0.86,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-SUNGWOO-20230712","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-MOBIS-4B-20240315","case_id":"C29-MOBIS-2024-MODULE-AS-LOCALPEAK","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"MOBILITY_SUPPLIER_VOLUME_MARGIN_LOCAL_PEAK_GUARD","sector":"mobility_auto_parts","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-03-15","evidence_available_at_that_date":"non-price 4B overlay evidence is used only as risk overlay, not positive promotion","evidence_source":"historical public result/report proxy + stock-web price-volume row validation","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv","profile_path":"atlas/symbol_profiles/012/012330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-15","entry_price":269000,"MFE_30D_pct":0.37,"MFE_90D_pct":0.37,"MFE_180D_pct":0.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.34,"MAE_90D_pct":-11.34,"MAE_180D_pct":-25.47,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-18","peak_price":270000,"drawdown_after_peak_pct":-25.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-MOBIS-20240315","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING","trigger_id":"TR-C29-SUNGWOO-S2A-20230216","symbol":"015750","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":40,"margin_bridge_score":42,"revision_score":48,"relative_strength_score":86,"customer_quality_score":62,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":68,"mix_margin_conversion_score":45},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":40,"margin_bridge_score":65,"revision_score":60,"relative_strength_score":86,"customer_quality_score":62,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":72,"mix_margin_conversion_score":68},"weighted_score_after":74,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"C29 supplier conversion rule raises margin_bridge/revision only after volume thesis is paired with actual price-volume confirmation and margin evidence.","MFE_90D_pct":80.26,"MAE_90D_pct":-11.72,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"C29_supplier_margin_conversion_guard_profile","case_id":"C29-SUNGWOO-2023-LIGHTWEIGHT-RERATING","trigger_id":"TR-C29-SUNGWOO-S2A-20230216","symbol":"015750","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":40,"margin_bridge_score":42,"revision_score":48,"relative_strength_score":86,"customer_quality_score":62,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":68,"mix_margin_conversion_score":45},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":40,"margin_bridge_score":65,"revision_score":60,"relative_strength_score":86,"customer_quality_score":62,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":72,"mix_margin_conversion_score":68},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"C29 supplier conversion rule raises margin_bridge/revision only after volume thesis is paired with actual price-volume confirmation and margin evidence.","MFE_90D_pct":80.26,"MAE_90D_pct":-11.72,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-SL-2023-LAMP-MARGIN-RERATING","trigger_id":"TR-C29-SL-S2A-20230425","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":55,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":60,"mix_margin_conversion_score":58},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":68,"revision_score":62,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":24,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":62,"mix_margin_conversion_score":70},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Keeps Yellow/Actionable rather than forcing Green; upside existed, but drawdown after local peak argues against pure price-only promotion.","MFE_90D_pct":29.86,"MAE_90D_pct":-9.19,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C29_supplier_margin_conversion_guard_profile","case_id":"C29-SL-2023-LAMP-MARGIN-RERATING","trigger_id":"TR-C29-SL-S2A-20230425","symbol":"005850","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":58,"revision_score":55,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":60,"mix_margin_conversion_score":58},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":45,"backlog_visibility_score":35,"margin_bridge_score":68,"revision_score":62,"relative_strength_score":72,"customer_quality_score":58,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":24,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":62,"mix_margin_conversion_score":70},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow+","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Keeps Yellow/Actionable rather than forcing Green; upside existed, but drawdown after local peak argues against pure price-only promotion.","MFE_90D_pct":29.86,"MAE_90D_pct":-9.19,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-MOBIS-2024-MODULE-AS-LOCALPEAK","trigger_id":"TR-C29-MOBIS-S2A-20240125","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":80,"customer_quality_score":70,"policy_or_regulatory_score":5,"valuation_repricing_score":60,"execution_risk_score":22,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":55},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":50,"revision_score":46,"relative_strength_score":80,"customer_quality_score":70,"policy_or_regulatory_score":5,"valuation_repricing_score":68,"execution_risk_score":32,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":48},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Adds C29 local-peak guard: large cap parts rerating without accelerating margin/revision remains overlay-managed, not full Green.","MFE_90D_pct":28.88,"MAE_90D_pct":-3.82,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C29_supplier_margin_conversion_guard_profile","case_id":"C29-MOBIS-2024-MODULE-AS-LOCALPEAK","trigger_id":"TR-C29-MOBIS-S2A-20240125","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":55,"revision_score":50,"relative_strength_score":80,"customer_quality_score":70,"policy_or_regulatory_score":5,"valuation_repricing_score":60,"execution_risk_score":22,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":55},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":50,"backlog_visibility_score":45,"margin_bridge_score":50,"revision_score":46,"relative_strength_score":80,"customer_quality_score":70,"policy_or_regulatory_score":5,"valuation_repricing_score":68,"execution_risk_score":32,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":48},"weighted_score_after":73,"stage_label_after":"Stage2-Actionable+4B-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Adds C29 local-peak guard: large cap parts rerating without accelerating margin/revision remains overlay-managed, not full Green.","MFE_90D_pct":28.88,"MAE_90D_pct":-3.82,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-WIA-2023-POWERTRAIN-LOCALPEAK","trigger_id":"TR-C29-WIA-S2A-20230627","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":42,"revision_score":45,"relative_strength_score":75,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":62,"mix_margin_conversion_score":35},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":30,"revision_score":32,"relative_strength_score":65,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":48,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":25},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Penalizes supplier volume narratives when margin_bridge_score and revision_score fail to rise with the price move.","MFE_90D_pct":9.98,"MAE_90D_pct":-15.29,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C29_supplier_margin_conversion_guard_profile","case_id":"C29-WIA-2023-POWERTRAIN-LOCALPEAK","trigger_id":"TR-C29-WIA-S2A-20230627","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":42,"revision_score":45,"relative_strength_score":75,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":35,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":62,"mix_margin_conversion_score":35},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":30,"revision_score":32,"relative_strength_score":65,"customer_quality_score":55,"policy_or_regulatory_score":5,"valuation_repricing_score":50,"execution_risk_score":48,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":55,"mix_margin_conversion_score":25},"weighted_score_after":63,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Penalizes supplier volume narratives when margin_bridge_score and revision_score fail to rise with the price move.","MFE_90D_pct":9.98,"MAE_90D_pct":-15.29,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE","trigger_id":"TR-C29-SNTMOTIV-S2-20230412","symbol":"064960","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":38,"revision_score":40,"relative_strength_score":58,"customer_quality_score":50,"policy_or_regulatory_score":5,"valuation_repricing_score":45,"execution_risk_score":38,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":60,"mix_margin_conversion_score":30},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":24,"revision_score":25,"relative_strength_score":50,"customer_quality_score":50,"policy_or_regulatory_score":5,"valuation_repricing_score":45,"execution_risk_score":52,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":45,"mix_margin_conversion_score":18},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Blocks promotion when capacity/volume route is not accompanied by gross margin or order conversion evidence.","MFE_90D_pct":7.5,"MAE_90D_pct":-9.42,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C29_supplier_margin_conversion_guard_profile","case_id":"C29-SNTMOTIV-2023-EV-MOTOR-FALSEBRIDGE","trigger_id":"TR-C29-SNTMOTIV-S2-20230412","symbol":"064960","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":38,"revision_score":40,"relative_strength_score":58,"customer_quality_score":50,"policy_or_regulatory_score":5,"valuation_repricing_score":45,"execution_risk_score":38,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":60,"mix_margin_conversion_score":30},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":35,"margin_bridge_score":24,"revision_score":25,"relative_strength_score":50,"customer_quality_score":50,"policy_or_regulatory_score":5,"valuation_repricing_score":45,"execution_risk_score":52,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5,"capacity_or_shipment_score":45,"mix_margin_conversion_score":18},"weighted_score_after":58,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","mix_margin_conversion_score"],"component_delta_explanation":"Blocks promotion when capacity/volume route is not accompanied by gross margin or order conversion evidence.","MFE_90D_pct":7.5,"MAE_90D_pct":-9.42,"score_return_alignment_label":"guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","scheduled_round":"R9","scheduled_loop":"11","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","supplier_local_peak_4B_needed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

```text
completed_round = R9
completed_loop = 11
next_round = R10
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Key source files checked in this run:

```text
stock_agent: reports/e2r_calibration/by_round/R9.md
stock-web: atlas/manifest.json
stock-web: atlas/schema.json
stock-web profiles: 012330, 011210, 015750, 005850, 064960
stock-web tradable shards: 012330/2024, 011210/2023, 015750/2023, 005850/2023, 064960/2023
```

Citation anchors from tool-visible source checks:

```text
R9 artifact: representative_triggers/unique_cases/trigger-type summary checked.
Manifest: source_name, max_date, row counts, shard roots, raw/unadjusted caveats checked.
Schema: tradable columns, formula, and calibration usable rules checked.
Profiles: name/date/trading_day/corporate_action_candidate fields checked for all selected symbols.
```

