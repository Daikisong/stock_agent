# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R9_loop_75_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round: R9
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OEM_AUTO_PARTS_VOLUME_MARGIN_OPERATING_LEVERAGE_AND_THEME_GUARD
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - counterexample_mining
  - yellow_threshold_stress_test
  - 4B_non_price_requirement_stress_test
  - coverage_gap_fill
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 5 new independent cases, 2 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

The current reference profile is `e2r_2_1_stock_web_calibrated_proxy`; `e2r_2_0_baseline_reference` is kept only as rollback/reference context.

Applied global axes assumed active:

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

This R9 residual run does not re-prove those global axes. It stress-tests whether C29 mobility cases need an extra gate that separates verified volume/margin operating leverage from EV/autonomous/IVI theme optionality.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 75 |
| allowed R9 sector route selected | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | OEM_AUTO_PARTS_VOLUME_MARGIN_OPERATING_LEVERAGE_AND_THEME_GUARD |
| scope note | Mobility/auto OEMs and auto-parts names where shipment mix, ASP, utilization, and operating leverage are the actual rerating engine. |

R9 permits L3 mobility/transport routing. This file intentionally avoids battery-cell/material C11/C12/C13 and focuses on mobility operating leverage.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifact access was used only as a coverage and duplicate-avoidance check. The visible registry is dominated by earlier R10 construction, R11 policy, R12 service/agri, and earlier R4/R5/R6 loops, while the active conversation state from the prior generated MD ended at `next_round=R9`, `next_loop=75`.

Duplicate gate outcome:

| duplicate dimension | result |
|---|---|
| same symbol + same trigger_date + same entry_date | no duplicate selected |
| same canonical_archetype_id | allowed, but this run uses new symbols and trigger families |
| repeated R1/R2 HBM/defense/grid set | not applicable |
| scheduled round violation | none |
| schema rematerialization only | false |

Selected symbols are 005380, 000270, 015750, 011210, 118990. All are used as new independent cases in this loop.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked for this run:

| manifest field | value |
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
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Tradable shard columns used: `d,o,h,l,c,v,a,mc,s,m`. Raw shard was not used for weight calibration.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D forward window | corporate-action overlap in 180D | calibration_usable |
|---|---:|---:|---:|---:|---:|
| C29_HMC_2023_RECORD_EARNINGS | 005380 | 2023-01-26 | available | none in 2023 window | true |
| C29_KIA_2023_RECORD_EARNINGS | 000270 | 2023-01-26 | available | none in 2023 window | true |
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | 015750 | 2023-05-16 | available | none after 2018 candidate dates | true |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | 011210 | 2021-01-21 | available | profile has no corporate-action candidates | true |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | 118990 | 2022-09-16 | available | 2022 CA candidates are before entry and do not overlap entry~D+180 | true |

Primary calibration window is 180 trading days. 1Y/2Y fields are included for schema compatibility where applicable, but shadow deltas below are based on the clean 180D window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| OEM_RECORD_EARNINGS_VOLUME_MIX_MARGIN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM volume/mix, ASP, FX, incentives, and utilization translate directly into OP leverage. |
| AUTO_PARTS_SUPPLIER_MARGIN_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Parts rerating requires own margin bridge, not only Hyundai/Kia parent-cycle halo. |
| EV_THERMAL_MANAGEMENT_OPTIONALITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Treated as C29 only when capacity/customer/earnings conversion exists; otherwise guard as theme optionality. |
| AUTONOMOUS_IVI_THEME_STOCK | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | IVI/autonomous keywords are mobility-adjacent, but without revenue bridge they should not promote positive stage. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | trigger_family | independent_evidence_weight |
|---|---:|---|---|---|---|---:|
| C29_HMC_2023_RECORD_EARNINGS | 005380 | 현대차 | structural_success | positive | OEM record earnings + margin bridge | 1.0 |
| C29_KIA_2023_RECORD_EARNINGS | 000270 | 기아 | structural_success | positive | OEM record earnings + margin bridge | 1.0 |
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | 015750 | 성우하이텍 | high_mae_success | positive | auto-parts supplier operating leverage | 1.0 |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | 011210 | 현대위아 | false_positive_green | counterexample | EV thermal-management theme without confirmed margin bridge | 1.0 |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | 118990 | 모트렉스 | high_mae_false_positive | counterexample | autonomous/IVI theme without clean earnings bridge | 1.0 |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 2 | C29_HMC_2023_RECORD_EARNINGS, C29_KIA_2023_RECORD_EARNINGS |
| high_mae_success / 4B overlay needed | 1 | C29_SUNGWOO_2023_SUPPLIER_LEVERAGE |
| counterexample_or_failed_rerating | 2 | C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE, C29_MOTREX_2022_AUTONOMOUS_IVI_THEME |
| 4B_or_4C_case | 2 | C29_SUNGWOO_2023_4B_OVERLAY, C29_MOTREX_2022_4B_LOCAL |

Balance requirement passes: positive_case_count >= 1, counterexample_count >= 1, calibration_usable_case_count >= 3.

## 9. Evidence Source Map

| case_id | trigger_date | evidence available at that date | evidence_source | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---:|---|---|---|---|---|
| C29_HMC_2023_RECORD_EARNINGS | 2023-01-26 | Record FY/Q4 earnings and margin bridge from volume/mix/ASP/FX; public earnings material was available by market reaction day. | company earnings release / public financial disclosure | public_event_or_disclosure; capacity_or_volume_route; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility | none at entry |
| C29_KIA_2023_RECORD_EARNINGS | 2023-01-26 | Record earnings and margin mix confirmation around same OEM cycle. | company earnings release / public financial disclosure | public_event_or_disclosure; capacity_or_volume_route; early_revision_signal | confirmed_revision; margin_bridge; financial_visibility | none at entry |
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | 2023-05-15 | Auto-parts supplier operating leverage visible in quarterly results and parent OEM cycle spillover. | quarterly disclosure / public financial data | public_event_or_disclosure; customer_or_order_quality; relative_strength | margin_bridge; financial_visibility; multiple_public_sources | valuation_blowoff after July spike |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | 2021-01-21 | EV thermal-management/parts optionality and relative strength without confirmed near-term margin bridge. | public news/theme flow and market reaction | policy_or_regulatory_optionality; relative_strength | none confirmed at trigger | price_only_local_peak; valuation_blowoff risk |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | 2022-09-16 | Autonomous/IVI/infotainment theme and momentum without clean earnings bridge at the spike date. | public news/theme flow and market reaction | public_event_or_disclosure; relative_strength | none confirmed at trigger | price_only_local_peak; positioning_overheat |

## 10. Price Data Source Map

| symbol | profile_path | tradable shard(s) used | profile caveat relevant to selected window |
|---:|---|---|---|
| 005380 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv | historical CA candidates are 1998~1999 only; selected 2023 window clean |
| 000270 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv | historical CA candidates are 1999 only; selected 2023 window clean |
| 015750 | atlas/symbol_profiles/015/015750.json | atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv | historical CA candidates end 2018; selected 2023 window clean |
| 011210 | atlas/symbol_profiles/011/011210.json | atlas/ohlcv_tradable_by_symbol_year/011/011210/2021.csv | no corporate-action candidate dates |
| 118990 | atlas/symbol_profiles/118/118990.json | atlas/ohlcv_tradable_by_symbol_year/118/118990/2022.csv; atlas/ohlcv_tradable_by_symbol_year/118/118990/2023.csv | 2022 CA candidates precede 2022-09-16 entry; entry~180D clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | aggregate role |
|---|---|---|---:|---:|---:|---|---|
| C29_HMC_2023_STAGE2 | C29_HMC_2023_RECORD_EARNINGS | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 174900 | C29_HMC_2023_20230126_174900 | representative |
| C29_KIA_2023_STAGE2 | C29_KIA_2023_RECORD_EARNINGS | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 69300 | C29_KIA_2023_20230126_69300 | representative |
| C29_SUNGWOO_2023_STAGE2 | C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | Stage2-Actionable | 2023-05-15 | 2023-05-16 | 9450 | C29_SUNGWOO_2023_20230516_9450 | representative |
| C29_SUNGWOO_2023_4B_OVERLAY | C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | Stage4B overlay | 2023-07-12 | 2023-07-12 | 14990 | C29_SUNGWOO_2023_20230516_9450 | 4B_overlay_only |
| C29_WIA_2021_STAGE2_FALSE | C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | Stage2 theme candidate | 2021-01-21 | 2021-01-21 | 108500 | C29_WIA_2021_20210121_108500 | representative |
| C29_MOTREX_2022_STAGE2_FALSE | C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | Stage2 theme candidate | 2022-09-16 | 2022-09-16 | 16450 | C29_MOTREX_2022_20220916_16450 | representative |
| C29_MOTREX_2022_4B_LOCAL | C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | Stage4B overlay | 2022-09-23 | 2022-09-23 | 18450 | C29_MOTREX_2022_20220916_16450 | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

Representative trigger rows, using actual Stock-Web tradable OHLC fields:

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C29_HMC_2023_STAGE2 | 174900 | 3.14 | -4.52 | 20.93 | -4.52 | 20.93 | -4.52 | 2023-05-11 | 211500 | -13.24 | structural_success |
| C29_KIA_2023_STAGE2 | 69300 | 15.44 | -3.61 | 32.61 | -3.61 | 32.61 | -3.61 | 2023-05-11 | 91900 | -12.95 | structural_success |
| C29_SUNGWOO_2023_STAGE2 | 9450 | 18.84 | -6.56 | 73.23 | -6.56 | 73.23 | -18.10 | 2023-07-12 | 16370 | -52.72 | high_mae_success |
| C29_WIA_2021_STAGE2_FALSE | 108500 | 0.00 | -30.32 | 0.00 | -30.32 | 0.00 | -32.63 | 2021-01-21 | 108500 | -32.63 | false_positive_green |
| C29_MOTREX_2022_STAGE2_FALSE | 16450 | 14.29 | -20.36 | 14.29 | -20.36 | 25.23 | -20.36 | 2023-03-08 | 20600 | -19.85 | high_mae_false_positive |

4B overlay rows:

| trigger_id | overlay entry | local peak basis | full window peak basis | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---|
| C29_SUNGWOO_2023_4B_OVERLAY | 14990 | 16370 | 16370 | 0.80 | 0.80 | good_full_window_4B_timing_if_supported_by_valuation_overheat |
| C29_MOTREX_2022_4B_LOCAL | 18450 | 18800 | 20600 | 1.15 | 1.05 | price_only_local_peak_needs_non_price_confirmation |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual alignment | verdict |
|---|---|---|---|
| C29_HMC_2023_RECORD_EARNINGS | Stage3-Yellow / near Green because margin bridge and earnings visibility are confirmed | aligned; 90D MFE 20.93% with limited MAE | current_profile_correct |
| C29_KIA_2023_RECORD_EARNINGS | Stage3-Yellow / near Green because same OEM margin cycle is visible | aligned; 90D MFE 32.61% with limited MAE | current_profile_correct |
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | likely delayed if supplier evidence is underweighted versus OEM evidence | underweights the supplier margin bridge; MFE arrives before conservative Green | current_profile_too_late |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | vulnerable if EV optionality + relative strength is treated as Stage2-actionable | badly misaligned if promoted; 180D MFE 0.00%, MAE -32.63% | current_profile_false_positive |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | vulnerable if autonomous/IVI theme and momentum are treated as sufficient | high MAE and unstable outcome; no clean margin bridge | current_profile_false_positive |

Axis stress results:

| applied axis | R9/C29 result |
|---|---|
| stage2_actionable_evidence_bonus | useful for confirmed OEM/supplier earnings, over-permissive for keyword themes |
| stage3_yellow_total_min=75 | acceptable for OEMs, too late for smaller supplier operating leverage after margin bridge is confirmed |
| stage3_green_total_min=87 / revision_min=55 | should not be relaxed globally; C29 needs a supplier margin bridge override only when own financials confirm leverage |
| price_only_blowoff_blocks_positive_stage | strengthened by WIA/Motrex |
| full_4b_requires_non_price_evidence | strengthened by Motrex local-peak example |
| hard_4c routing | not a primary discovery axis in this loop |

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 actionable timing | Stage3-Yellow timing | Stage3-Green timing | green_lateness_ratio |
|---|---|---|---|---:|
| C29_HMC_2023_RECORD_EARNINGS | timely at earnings day | timely after earnings confirmation | not materially late if Green waits for guidance/revision | 0.24 |
| C29_KIA_2023_RECORD_EARNINGS | timely at earnings day | timely after earnings confirmation | not materially late if Green waits for follow-through | 0.18 |
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | timely after quarterly result | Yellow likely late if OEM halo is discounted too much | Green likely late after July spike | 0.73 |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | should be blocked or watch-only | Yellow should not trigger without margin bridge | Green should not trigger | not_applicable |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | should be watch-only unless earnings bridge confirms | Yellow should be guarded | Green should be blocked | not_applicable |

## 15. 4B Local vs Full-window Timing Audit

| case_id | four_b_evidence_type | local proximity | full-window proximity | timing verdict |
|---|---|---:|---:|---|
| C29_SUNGWOO_2023_SUPPLIER_LEVERAGE | valuation_blowoff; positioning_overheat; price_only_local_peak | 0.80 | 0.80 | good_full_window_4B_timing if combined with valuation/positioning evidence |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | price_only; positioning_overheat | 1.15 | 1.05 | do_not_treat_as_full_4B without non-price evidence; use as risk overlay only |
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | price_only_local_peak; valuation_blowoff | 1.00 | 1.00 | local peak coincided with trigger; this is not a buyable Stage2 |

## 16. 4C Protection Audit

No hard 4C thesis-break row is proposed for production. The loop is about 4B/false-positive gating. Protection labels:

| case_id | four_c_protection_label | reason |
|---|---|---|
| C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE | thesis_break_watch_only | No explicit contract cancellation; the failure is lack of confirmed conversion from theme to margin. |
| C29_MOTREX_2022_AUTONOMOUS_IVI_THEME | thesis_break_watch_only | No hard cancellation; high-MAE theme path should be blocked earlier by the C29 guard. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

Proposed R9/L3 C29 shadow-only rule:

```text
C29_mobility_operating_leverage_gate:
  promote Stage2-Actionable only when at least one non-price field confirms revenue/margin conversion:
    - OEM record earnings or guidance with volume/mix/margin bridge
    - supplier own quarterly margin bridge or backlog/delivery visibility
    - confirmed customer program with production ramp and financial visibility
  do not promote from:
    - EV/autonomous/IVI keyword alone
    - one-day relative strength alone
    - local blowoff with no non-price confirmation
```

Expected effect: keep Hyundai/Kia/Sungwoo-style structural cases, block WIA/Motrex-style theme spikes.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Candidate canonical compression:

```text
C29 requires a two-part bridge:
  1. volume route: shipments, orderbook, capacity utilization, or customer production ramp
  2. margin route: ASP/mix/FX/operating leverage or own quarterly margin bridge

If only the volume/optionality story exists and margin route is unknown, cap at watch-only Stage2 and require later confirmation for Yellow/Green.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | selected representative cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 5 | 28.21 | -13.87 | 30.40 | -15.04 | 40% | 1 | mixed; positive cases work but theme spikes leak through |
| P0b_e2r_2_0_baseline_reference | rollback reference | 5 | 28.21 | -13.87 | 30.40 | -15.04 | 40%+ | 1 | worse precision because global guards are weaker |
| P1_sector_specific_candidate_profile | L3 sector shadow | 3 | 42.26 | -4.90 | 42.26 | -8.93 | 0% | 0 | improved precision; keeps verified operating leverage |
| P2_canonical_archetype_candidate_profile | C29 archetype shadow | 3 | 42.26 | -4.90 | 42.26 | -8.93 | 0% | 0 | best alignment for C29 |
| P3_counterexample_guard_profile | strict guard | 2 | 26.77 | -4.07 | 26.77 | -4.07 | 0% | 1 | too strict; misses smaller supplier operating leverage |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment label |
|---|---:|---|---:|---|---:|---:|---|
| C29_HMC_2023_STAGE2 | 83 | Stage3-Yellow | 88 | Stage3-Green | 20.93 | -4.52 | score_return_aligned |
| C29_KIA_2023_STAGE2 | 84 | Stage3-Yellow | 89 | Stage3-Green | 32.61 | -3.61 | score_return_aligned |
| C29_SUNGWOO_2023_STAGE2 | 72 | Stage2-Actionable | 82 | Stage3-Yellow | 73.23 | -6.56 | current_profile_missed_structural |
| C29_WIA_2021_STAGE2_FALSE | 77 | Stage3-Yellow | 63 | WatchOnly | 0.00 | -30.32 | current_profile_false_positive_fixed |
| C29_MOTREX_2022_STAGE2_FALSE | 76 | Stage3-Yellow | 61 | WatchOnly | 14.29 | -20.36 | current_profile_false_positive_fixed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_AUTO_PARTS_VOLUME_MARGIN_OPERATING_LEVERAGE_AND_THEME_GUARD | 3 | 2 | 2 | 0 | 5 | 0 | 7 | 5 | 3 | true | true | supplier margin bridge still needs more holdout cases; theme guard now has two counterexamples |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - supplier_operating_leverage_underweighted
  - EV_autonomous_theme_false_positive
  - price_only_local_peak_too_early
new_axis_proposed:
  - C29_mobility_operating_leverage_gate
  - C29_theme_optional_watch_only_cap
  - C29_supplier_margin_bridge_override
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest max_date = 2026-02-20.
- Tradable OHLC rows exist for every entry_date.
- Forward 180 trading-day windows are available.
- Corporate-action candidate dates do not overlap selected entry~180D windows.
- MFE/MAE/peak/drawdown are calculated from tradable raw OHLC windows.
- Positive and counterexample balance is satisfied.
```

Not validated:

```text
- No live/current candidate scan.
- No stock_agent source code opened.
- No production scoring patch written.
- No brokerage API or automated trading action.
- Evidence-source timestamps are used as historical trigger proxies and should be rechecked in batch implementation if the coding agent ingests exact disclosure timestamps.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_margin_bridge_required_for_positive_stage,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Require margin bridge before positive Stage2/Yellow promotion","Blocks WIA/Motrex while retaining OEM and supplier earnings cases","C29_HMC_2023_STAGE2|C29_KIA_2023_STAGE2|C29_SUNGWOO_2023_STAGE2|C29_WIA_2021_STAGE2_FALSE|C29_MOTREX_2022_STAGE2_FALSE",5,5,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_margin_bridge_override,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Supplier own quarterly margin bridge should offset lack of direct OEM-level disclosure","Catches Sungwoo before most rerating while still needing 4B overlay","C29_SUNGWOO_2023_STAGE2",1,1,0,low,sector_shadow_only,"needs more holdout supplier cases"
shadow_weight,C29_theme_optional_watch_only_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"EV/autonomous/IVI keywords without financial bridge capped at watch-only","Reduces high-MAE false positives","C29_WIA_2021_STAGE2_FALSE|C29_MOTREX_2022_STAGE2_FALSE",2,2,2,medium,counterexample_guard,"not production; strengthens existing price-only guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29_HMC_2023_RECORD_EARNINGS","symbol":"005380","company_name":"현대차","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_EARNINGS_VOLUME_MIX_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C29_HMC_2023_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM record earnings and margin bridge."}
{"row_type":"case","case_id":"C29_KIA_2023_RECORD_EARNINGS","symbol":"000270","company_name":"기아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_EARNINGS_VOLUME_MIX_MARGIN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C29_KIA_2023_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM margin and mix leverage."}
{"row_type":"case","case_id":"C29_SUNGWOO_2023_SUPPLIER_LEVERAGE","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_SUPPLIER_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"C29_SUNGWOO_2023_STAGE2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_too_late_but_positive","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Supplier bridge needs archetype-specific boost and later 4B overlay."}
{"row_type":"case","case_id":"C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_MANAGEMENT_OPTIONALITY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C29_WIA_2021_STAGE2_FALSE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Theme and relative strength without confirmed margin bridge."}
{"row_type":"case","case_id":"C29_MOTREX_2022_AUTONOMOUS_IVI_THEME","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTONOMOUS_IVI_THEME_STOCK","case_type":"high_mae_false_positive","positive_or_counterexample":"counterexample","best_trigger":"C29_MOTREX_2022_STAGE2_FALSE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Momentum theme with high MAE and insufficient financial bridge."}
{"row_type":"trigger","trigger_id":"C29_HMC_2023_STAGE2","case_id":"C29_HMC_2023_RECORD_EARNINGS","symbol":"005380","company_name":"현대차","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_EARNINGS_VOLUME_MIX_MARGIN","sector":"mobility_auto_oem","primary_archetype":"volume_margin_operating_leverage","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"record earnings and margin bridge visible","evidence_source":"company earnings release/public disclosure","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2023.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":174900,"MFE_30D_pct":3.14,"MFE_90D_pct":20.93,"MFE_180D_pct":20.93,"MFE_1Y_pct":20.93,"MFE_2Y_pct":null,"MAE_30D_pct":-4.52,"MAE_90D_pct":-4.52,"MAE_180D_pct":-4.52,"MAE_1Y_pct":-4.52,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":211500,"drawdown_after_peak_pct":-13.24,"green_lateness_ratio":0.24,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_HMC_2023_20230126_174900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_KIA_2023_STAGE2","case_id":"C29_KIA_2023_RECORD_EARNINGS","symbol":"000270","company_name":"기아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_RECORD_EARNINGS_VOLUME_MIX_MARGIN","sector":"mobility_auto_oem","primary_archetype":"volume_margin_operating_leverage","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","evidence_available_at_that_date":"record earnings and margin bridge visible","evidence_source":"company earnings release/public disclosure","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2023.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-26","entry_price":69300,"MFE_30D_pct":15.44,"MFE_90D_pct":32.61,"MFE_180D_pct":32.61,"MFE_1Y_pct":32.61,"MFE_2Y_pct":null,"MAE_30D_pct":-3.61,"MAE_90D_pct":-3.61,"MAE_180D_pct":-3.61,"MAE_1Y_pct":-3.61,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-11","peak_price":91900,"drawdown_after_peak_pct":-12.95,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_KIA_2023_20230126_69300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_SUNGWOO_2023_STAGE2","case_id":"C29_SUNGWOO_2023_SUPPLIER_LEVERAGE","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_SUPPLIER_MARGIN_BRIDGE","sector":"mobility_auto_parts","primary_archetype":"supplier_margin_bridge","loop_objective":"sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-15","evidence_available_at_that_date":"quarterly supplier leverage and OEM halo","evidence_source":"quarterly disclosure/public financial data","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-16","entry_price":9450,"MFE_30D_pct":18.84,"MFE_90D_pct":73.23,"MFE_180D_pct":73.23,"MFE_1Y_pct":73.23,"MFE_2Y_pct":null,"MAE_30D_pct":-6.56,"MAE_90D_pct":-6.56,"MAE_180D_pct":-18.1,"MAE_1Y_pct":-18.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.72,"green_lateness_ratio":0.73,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_SUNGWOO_2023_20230516_9450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_SUNGWOO_2023_4B_OVERLAY","case_id":"C29_SUNGWOO_2023_SUPPLIER_LEVERAGE","symbol":"015750","company_name":"성우하이텍","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_SUPPLIER_MARGIN_BRIDGE","sector":"mobility_auto_parts","primary_archetype":"supplier_margin_bridge","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B overlay","trigger_date":"2023-07-12","evidence_available_at_that_date":"valuation and positioning overheat after rapid supplier rerating","evidence_source":"Stock-Web price path + valuation/positioning narrative","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015750/2023.csv","profile_path":"atlas/symbol_profiles/015/015750.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-12","entry_price":14990,"MFE_30D_pct":9.21,"MFE_90D_pct":9.21,"MFE_180D_pct":9.21,"MFE_1Y_pct":9.21,"MFE_2Y_pct":null,"MAE_30D_pct":-8.07,"MAE_90D_pct":-38.76,"MAE_180D_pct":-48.37,"MAE_1Y_pct":-48.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-12","peak_price":16370,"drawdown_after_peak_pct":-52.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":0.8,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_SUNGWOO_2023_20230516_9450","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case as representative; used for 4B overlay timing only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C29_WIA_2021_STAGE2_FALSE","case_id":"C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE","symbol":"011210","company_name":"현대위아","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_MANAGEMENT_OPTIONALITY","sector":"mobility_auto_parts","primary_archetype":"theme_without_margin_bridge","loop_objective":"counterexample_mining","trigger_type":"Stage2 theme candidate","trigger_date":"2021-01-21","evidence_available_at_that_date":"EV thermal optionality and relative strength but no confirmed margin bridge","evidence_source":"public news/theme flow and market reaction","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011210/2021.csv","profile_path":"atlas/symbol_profiles/011/011210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-21","entry_price":108500,"MFE_30D_pct":0.0,"MFE_90D_pct":0.0,"MFE_180D_pct":0.0,"MFE_1Y_pct":0.0,"MFE_2Y_pct":null,"MAE_30D_pct":-30.32,"MAE_90D_pct":-30.32,"MAE_180D_pct":-32.63,"MAE_1Y_pct":-32.63,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-01-21","peak_price":108500,"drawdown_after_peak_pct":-32.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"theme_peak_not_stage2","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_WIA_2021_20210121_108500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_MOTREX_2022_STAGE2_FALSE","case_id":"C29_MOTREX_2022_AUTONOMOUS_IVI_THEME","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTONOMOUS_IVI_THEME_STOCK","sector":"mobility_auto_parts","primary_archetype":"theme_without_margin_bridge","loop_objective":"counterexample_mining","trigger_type":"Stage2 theme candidate","trigger_date":"2022-09-16","evidence_available_at_that_date":"autonomous/IVI theme and relative strength without confirmed financial bridge","evidence_source":"public news/theme flow and market reaction","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/118/118990/2022.csv","profile_path":"atlas/symbol_profiles/118/118990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-09-16","entry_price":16450,"MFE_30D_pct":14.29,"MFE_90D_pct":14.29,"MFE_180D_pct":25.23,"MFE_1Y_pct":25.23,"MFE_2Y_pct":null,"MAE_30D_pct":-20.36,"MAE_90D_pct":-20.36,"MAE_180D_pct":-20.36,"MAE_1Y_pct":-20.36,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":20600,"drawdown_after_peak_pct":-19.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"theme_high_mae_false_positive","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOTREX_2022_20220916_16450","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C29_MOTREX_2022_4B_LOCAL","case_id":"C29_MOTREX_2022_AUTONOMOUS_IVI_THEME","symbol":"118990","company_name":"모트렉스","round":"R9","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTONOMOUS_IVI_THEME_STOCK","sector":"mobility_auto_parts","primary_archetype":"theme_without_margin_bridge","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B overlay","trigger_date":"2022-09-23","evidence_available_at_that_date":"local price peak after theme spike","evidence_source":"Stock-Web price path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/118/118990/2022.csv","profile_path":"atlas/symbol_profiles/118/118990.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2022-09-23","entry_price":18450,"MFE_30D_pct":1.9,"MFE_90D_pct":1.9,"MFE_180D_pct":11.65,"MFE_1Y_pct":11.65,"MFE_2Y_pct":null,"MAE_30D_pct":-28.99,"MAE_90D_pct":-28.99,"MAE_180D_pct":-28.99,"MAE_1Y_pct":-28.99,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-08","peak_price":20600,"drawdown_after_peak_pct":-19.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.15,"four_b_full_window_peak_proximity":1.05,"four_b_timing_verdict":"price_only_local_4B_requires_non_price_confirmation","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C29_MOTREX_2022_20220916_16450","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same case as representative; used for 4B local/full split","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_HMC_2023_RECORD_EARNINGS","trigger_id":"C29_HMC_2023_STAGE2","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":30,"margin_bridge_score":80,"revision_score":75,"relative_strength_score":55,"customer_quality_score":80,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":35,"margin_bridge_score":85,"revision_score":80,"relative_strength_score":55,"customer_quality_score":85,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"OEM earnings bridge qualifies for C29 margin/volume gate.","MFE_90D_pct":20.93,"MAE_90D_pct":-4.52,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_KIA_2023_RECORD_EARNINGS","trigger_id":"C29_KIA_2023_STAGE2","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":35,"margin_bridge_score":82,"revision_score":78,"relative_strength_score":60,"customer_quality_score":80,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":40,"margin_bridge_score":87,"revision_score":82,"relative_strength_score":60,"customer_quality_score":85,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","customer_quality_score"],"component_delta_explanation":"OEM margin/volume confirmation.","MFE_90D_pct":32.61,"MAE_90D_pct":-3.61,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_SUNGWOO_2023_SUPPLIER_LEVERAGE","trigger_id":"C29_SUNGWOO_2023_STAGE2","symbol":"015750","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":20,"backlog_visibility_score":35,"margin_bridge_score":60,"revision_score":45,"relative_strength_score":70,"customer_quality_score":65,"policy_or_regulatory_score":20,"valuation_repricing_score":65,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":45,"margin_bridge_score":80,"revision_score":55,"relative_strength_score":70,"customer_quality_score":70,"policy_or_regulatory_score":20,"valuation_repricing_score":65,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","backlog_visibility_score"],"component_delta_explanation":"Supplier own margin bridge receives C29-specific boost, not broad global boost.","MFE_90D_pct":73.23,"MAE_90D_pct":-6.56,"score_return_alignment_label":"missed_structural_before_after_aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_WIA_2021_THERMAL_THEME_FALSE_POSITIVE","trigger_id":"C29_WIA_2021_STAGE2_FALSE","symbol":"011210","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":90,"customer_quality_score":45,"policy_or_regulatory_score":60,"valuation_repricing_score":80,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":90,"customer_quality_score":35,"policy_or_regulatory_score":45,"valuation_repricing_score":80,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":63,"stage_label_after":"WatchOnly","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"EV optionality without margin route is capped by C29 theme guard.","MFE_90D_pct":0.0,"MAE_90D_pct":-30.32,"score_return_alignment_label":"false_positive_fixed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29_MOTREX_2022_AUTONOMOUS_IVI_THEME","trigger_id":"C29_MOTREX_2022_STAGE2_FALSE","symbol":"118990","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":15,"revision_score":10,"relative_strength_score":85,"customer_quality_score":45,"policy_or_regulatory_score":60,"valuation_repricing_score":75,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":85,"customer_quality_score":35,"policy_or_regulatory_score":45,"valuation_repricing_score":75,"execution_risk_score":75,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"WatchOnly","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Autonomous/IVI theme lacks financial bridge and remains high-MAE.","MFE_90D_pct":14.29,"MAE_90D_pct":-20.36,"score_return_alignment_label":"false_positive_fixed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"75","scheduled_round":"R9","scheduled_loop":"75","round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":3,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["supplier_operating_leverage_underweighted","EV_autonomous_theme_false_positive","price_only_local_peak_too_early"],"diversity_score_summary":"new_symbols=5; new_trigger_families=4; counterexamples=2; residual_errors=3; wrong_round_penalty=0","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

```text
completed_round = R9
completed_loop = 75
next_round = R10
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Primary price source: Songdaiki/stock-web
Manifest max_date: 2026-02-20
Price basis: tradable_raw
Adjustment: raw_unadjusted_marcap
Used only historical OHLC rows; no live scan; no stock_agent code opened; no production patch written.
```

