# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R9_loop_10_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
scheduled_round: R9
scheduled_loop: 10
completed_round: R9
completed_loop: 10
next_round: R10
next_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: MOBILITY_VOLUME_MIX_MARGIN_CAPITAL_RETURN_BRIDGE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
current_default_profile_proxy: e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id: e2r_2_0_baseline_reference
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_patch_written: false
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
```

This loop adds **4 new independent cases**, **2 counterexamples**, and **2 current-profile residual errors** for `R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE`.

## 1. Current Calibrated Profile Assumption

This research assumes the already-calibrated proxy profile:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference   = e2r_2_0_baseline
```

Already-applied axes are treated as baseline facts, not re-proposed global changes:

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

The residual question is narrower: **in C29, when does mobility volume/mix/margin evidence behave like a durable rerating bridge, and when does it stay a headline or local-peak trap?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R9 |
| scheduled_loop | 10 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE |
| fine_archetype_id | MOBILITY_VOLUME_MIX_MARGIN_CAPITAL_RETURN_BRIDGE |
| round_sector_consistency | pass |

R9 allows `L3_BATTERY_EV_GREEN_MOBILITY` when the case is mobility / EV / auto-cycle in nature. This file uses that branch because the selected cases are finished vehicles, auto components, and EV thermal/ADAS supply chain names.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact checked:

```text
reports/e2r_calibration/by_round/R9.md
```

The R9 report already has a substantial body of accepted trigger rows: `representative_triggers=122`, `unique_cases=28`, with `Stage2=28`, `Stage2-Actionable=28`, `Stage3-Green=21`, `Stage4B=21`, and `Stage4C=3`. The accepted axes are cumulative/global, so this loop does **not** re-argue those global axes. It instead adds C29-specific compression around four families:

1. full OEM mix/margin/capital-return rerating,
2. OEM Green lateness after Stage2 actionability,
3. parts supplier local-peak vs durable margin bridge,
4. thermal/EV component false-positive where volume narrative does not convert into margin/FCF.

Novelty rule applied:

```text
same canonical archetype allowed: true
same symbol + same trigger_date + same entry_date repeated: avoided
new_symbol_count: 4
new_trigger_family_count: 4
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

Manifest facts used:

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
| C29-HYUNDAI-2024-VALUEUP-MIX | 005380 | 현대차 | 2024-01-25 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 180+ | clean_180D_window | true |
| C29-KIA-2024-MIX-CAPRETURN | 000270 | 기아 | 2024-01-25 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | atlas/symbol_profiles/000/000270.json | 180+ | clean_180D_window | true |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | 204320 | HL만도 | 2024-04-29 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | atlas/symbol_profiles/204/204320.json | 180+ | clean_180D_window | true |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | 018880 | 한온시스템 | 2023-01-25 | atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv | atlas/symbol_profiles/018/018880.json | 180+ | clean_180D_window | true |

Profile check summary:

```text
005380 corporate_action_candidate_dates = 1998-12-02, 1999-04-15, 1999-06-11, 1999-08-16, 1999-12-24
000270 corporate_action_candidate_dates = 1999-03-05, 1999-04-21, 1999-07-16
204320 corporate_action_candidate_dates = 2018-05-08
018880 corporate_action_candidate_dates = 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12
```

The 018880 2023 trigger is used only through 180D and does not overlap the 2025 corporate-action candidate. 1Y/2Y are marked `contaminated_or_unavailable` for that case because the longer window approaches the later raw discontinuity zone.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Completed vehicle OEM where mix, margin, shareholder return, and relative strength support rerating. |
| OEM_GREEN_LATENESS_AFTER_STAGE2 | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Green confirmation appears after price has already repriced much of the Stage2 upside. |
| ADAS_PARTS_ORDER_NARRATIVE_LOCAL_PEAK | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | Component supplier narrative can produce local MFE but requires margin bridge before Green. |
| EV_THERMAL_VOLUME_FALSE_BRIDGE | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV/thermal volume story without margin/FCF bridge creates false-positive risk. |

## 7. Case Selection Summary

| case_id | role | positive_or_counterexample | trigger family | representative trigger | reason selected |
|---|---|---|---|---|---|
| C29-HYUNDAI-2024-VALUEUP-MIX | structural_success + 4B_overlay_success | positive | OEM mix/margin/capital-return rerating | 2024-01-25 Stage2-Actionable | Clear early Stage2 before a large 180D MFE path; later full-window 4B can be separated from price-only local peaks. |
| C29-KIA-2024-MIX-CAPRETURN | high_mae_success | positive | OEM mix/capital-return with Green lateness | 2024-01-25 Stage2-Actionable | Stage2 captures large upside before Green; good stress test for C29 Green strictness. |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | 4B_too_early / failed_rerating guard | counterexample | parts supplier ADAS/local peak | 2024-04-29 Stage2-Actionable | Local MFE is strong, but Green after the move is fragile without margin/FCF confirmation. |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | failed_rerating / false_positive_green | counterexample | EV thermal component false bridge | 2023-01-25 Stage2 | Volume/thermal narrative alone does not rerate when margin/FCF evidence is thin. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
```

This loop meets the minimum balance rule. It does not propose a global scoring delta. It proposes only C29-specific bridge/guard behavior.

## 9. Evidence Source Map

Evidence source labels are research-proxy, point-in-time historical categories. They are not live recommendations and are not production scoring facts.

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|---|---|---|
| C29-HYUNDAI-2024-VALUEUP-MIX | 2024-01-25 | historical FY2023 result/capital-return/mix-margin discussion available by trigger window | public result/disclosure + contemporary analyst-note proxy | public_event_or_disclosure; relative_strength; early_revision_signal; capacity_or_volume_route | confirmed_revision; margin_bridge; financial_visibility; multiple_public_sources | valuation_blowoff; positioning_overheat; price_only_local_peak | [] |
| C29-KIA-2024-MIX-CAPRETURN | 2024-01-25 | historical FY2023 result/capital-return/mix-margin discussion available by trigger window | public result/disclosure + contemporary analyst-note proxy | public_event_or_disclosure; relative_strength; early_revision_signal; capacity_or_volume_route | confirmed_revision; margin_bridge; financial_visibility | valuation_blowoff; positioning_overheat | [] |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | 2024-04-29 | parts/ADAS/customer-order narrative and local relative strength visible | public event/report proxy + price-volume context | public_event_or_disclosure; customer_or_order_quality; relative_strength | partial_margin_bridge; incomplete_financial_visibility | price_only_local_peak; valuation_blowoff | [] |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | 2023-01-25 | EV thermal/volume narrative visible but margin bridge weak | public event/report proxy | public_event_or_disclosure; capacity_or_volume_route | unknown_or_not_supported | margin_or_backlog_slowdown; revision_slowdown | thesis_break_watch_only |

## 10. Price Data Source Map

| symbol | profile_path | shard_paths_used | basis | adjustment |
|---:|---|---|---|---|
| 005380 | atlas/symbol_profiles/005/005380.json | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | tradable_raw | raw_unadjusted_marcap |
| 000270 | atlas/symbol_profiles/000/000270.json | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | tradable_raw | raw_unadjusted_marcap |
| 204320 | atlas/symbol_profiles/204/204320.json | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | tradable_raw | raw_unadjusted_marcap |
| 018880 | atlas/symbol_profiles/018/018880.json | atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | dedupe_for_aggregate | aggregate_group_role | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| TR-C29-HYUNDAI-S2A-20240125 | C29-HYUNDAI-2024-VALUEUP-MIX | 005380 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 188700 | G-C29-HYUNDAI-20240125 | true | representative | current_profile_correct |
| TR-C29-HYUNDAI-4B-20240627 | C29-HYUNDAI-2024-VALUEUP-MIX | 005380 | Stage4B | 2024-06-27 | 2024-06-27 | 298000 | G-C29-HYUNDAI-20240627 | false | 4B_overlay_only | current_profile_correct |
| TR-C29-KIA-S2A-20240125 | C29-KIA-2024-MIX-CAPRETURN | 000270 | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 93000 | G-C29-KIA-20240125 | true | representative | current_profile_correct |
| TR-C29-HLMANDO-S2A-20240429 | C29-HLMANDO-2024-ADAS-LOCALPEAK | 204320 | Stage2-Actionable | 2024-04-29 | 2024-04-29 | 38350 | G-C29-HLMANDO-20240429 | true | representative | current_profile_correct |
| TR-C29-HLMANDO-GREEN-20240605 | C29-HLMANDO-2024-ADAS-LOCALPEAK | 204320 | Stage3-Green | 2024-06-05 | 2024-06-05 | 49600 | G-C29-HLMANDO-20240605 | false | label_comparison_only | current_profile_false_positive |
| TR-C29-HANON-S2-20230125 | C29-HANON-2023-THERMAL-FALSEBRIDGE | 018880 | Stage2 | 2023-01-25 | 2023-01-25 | 9180 | G-C29-HANON-20230125 | true | representative | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative entry triggers

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | MAE_1Y_pct | below_entry_price_flag_30D | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|---:|---:|
| TR-C29-HYUNDAI-S2A-20240125 | 188700 | 38.31 | 47.06 | 58.72 | 58.72 | null | -2.76 | -2.76 | -2.76 | -2.76 | true | true | 2024-06-28 | 299500 | -16.19 |
| TR-C29-KIA-S2A-20240125 | 93000 | 36.45 | 41.61 | 45.16 | 45.16 | null | -7.42 | -7.42 | -7.42 | -7.42 | true | true | 2024-06-19 | 135000 | -18.52 |
| TR-C29-HLMANDO-S2A-20240429 | 38350 | 14.60 | 30.38 | 30.38 | null | null | -5.48 | -5.48 | -17.34 | null | true | true | 2024-06-05 | 50000 | -23.20 |
| TR-C29-HANON-S2-20230125 | 9180 | 6.43 | 10.78 | 10.78 | contaminated_or_unavailable | contaminated_or_unavailable | -2.72 | -10.57 | -11.66 | contaminated_or_unavailable | true | true | 2023-05-10 | 10170 | -20.26 |

### 12.2 Label comparison / overlay triggers

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | usage |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| TR-C29-HYUNDAI-4B-20240627 | 298000 | 0.50 | 0.50 | 0.50 | -14.43 | -15.60 | -16.19 | 2024-06-28 | 299500 | -16.19 | 4B_overlay_only |
| TR-C29-HLMANDO-GREEN-20240605 | 49600 | 0.81 | 0.81 | 0.81 | -15.22 | -22.48 | -22.48 | 2024-06-05 | 50000 | -23.20 | label_comparison_only |

Notes:

- 005380 uses 2024-01-25 close `188700`, 2024-06-28 high `299500`, and the same-row low `183500` for the initial adverse excursion.
- 000270 uses 2024-01-25 close `93000`, 2024-06-19 high `135000`, and same-row low `86100`.
- 204320 uses 2024-04-29 close `38350`, 2024-06-05 high `50000`, and later 180D representative low proxy `31700` after the local peak.
- 018880 uses 2023-01-25 close `9180`, 2023-05-10 high `10170`, and 2023-07-26 low `8110`.

## 13. Current Calibrated Profile Stress Test

| case_id | current profile expected behavior | actual path | verdict | residual lesson |
|---|---|---|---|---|
| C29-HYUNDAI-2024-VALUEUP-MIX | Stage2-Actionable before Green, later 4B only with non-price evidence | Large MFE before and after Green; later 4B near full-window peak | current_profile_correct | Stage2 actionability is valuable when mix/margin/capital return line up. |
| C29-KIA-2024-MIX-CAPRETURN | Stage2-Actionable, Green after revision confirmation | Stage2 captured the better entry; Green was later but still acceptable | current_profile_correct | C29 should tolerate Stage2 entry when capital return + mix are already visible. |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | Stage2/watch first; Green only with confirmed margin/revision bridge | Stage2 made local MFE, but Green after the local peak had poor forward MFE/MAE | current_profile_false_positive | C29 supplier Green needs margin/FCF bridge, not just order/ADAS narrative. |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | Stage2/watch if only EV thermal volume story | Small MFE, persistent MAE, weak rerating | current_profile_false_positive | EV-volume label without margin/FCF conversion should be capped below Green. |

Stress-test answers:

```text
1. current calibrated profile judgement:
   - Correct for OEM Stage2 and 4B separation.
   - Too permissive if C29 supplier narratives are allowed to Green without margin/FCF bridge.

2. MFE/MAE alignment:
   - OEM cases align strongly with Stage2-Actionable.
   - supplier/thermal cases show local MFE but fragile or poor post-Green alignment.

3. Stage2 bonus:
   - useful for OEM mix/margin/capital-return cases.
   - should be capped for C29 supplier names when customer quality is not linked to margin bridge.

4. Yellow 75:
   - acceptable as watch/early confirmation.

5. Green 87 / revision 55:
   - too early for C29 suppliers unless confirmed revision + margin bridge exist.

6. price-only blowoff guard:
   - appropriate and strengthened for C29.

7. full 4B non-price requirement:
   - appropriate; 005380 near-peak 4B is usable only when valuation/positioning evidence is present.

8. hard 4C routing:
   - no hard 4C production change; C29 supplier failures should start as thesis-break watch / Green-block first.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | peak_after_Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| C29-HYUNDAI-2024-VALUEUP-MIX | 188700 | 227000 | 299500 | 0.346 | Green somewhat late but still acceptable; Stage2 captured the better asymmetry. |
| C29-KIA-2024-MIX-CAPRETURN | 93000 | 119500 | 135000 | 0.631 | Green captured much less upside; C29 OEM Stage2 should remain useful. |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | 38350 | 49600 | 50000 | 0.966 | Green would arrive almost at local peak; supplier Green needs stronger bridge. |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | 9180 | not_applicable | 10170 | not_applicable | no confirmed Green; Stage2/watch only. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry price | Stage4B entry price | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| TR-C29-HYUNDAI-4B-20240627 | 188700 | 298000 | 299500 | 299500 | 0.986 | 0.986 | valuation_blowoff; positioning_overheat; non_price_overlay | good_full_window_4B_timing |
| TR-C29-HLMANDO-GREEN-20240605 | 38350 | 49600 | 50000 | 50000 | 0.966 | 0.966 | price_only_local_peak; incomplete_margin_bridge | price_only_local_4B_too_early_if_no_non_price_evidence |

C29-specific distinction:

```text
OEM rerating 4B can be close to the true full-window peak when valuation/capital-return/positioning evidence is present.
Supplier local peak should not become full 4B or Green unless non-price margin/revision evidence confirms that the move is not just order narrative compression.
```

## 16. 4C Protection Audit

No hard 4C production change is proposed. C29 failures in this loop are better treated as **Green-block / thesis-break-watch** first.

| case_id | four_c_protection_label | rationale |
|---|---|---|
| C29-HYUNDAI-2024-VALUEUP-MIX | not_applicable | 4B overlay, not 4C. |
| C29-KIA-2024-MIX-CAPRETURN | not_applicable | high-MFE OEM case, not 4C. |
| C29-HLMANDO-2024-ADAS-LOCALPEAK | thesis_break_watch_only | post-peak drawdown from local high, but not hard thesis break. |
| C29-HANON-2023-THERMAL-FALSEBRIDGE | thesis_break_watch_only | weak bridge; no hard 4C trigger in 180D window. |

## 17. Sector-Specific Rule Candidate

```yaml
rule_id: R9_L3_C29_MOBILITY_STAGE2_GREEN_BRIDGE_SPLIT
rule_scope: canonical_archetype_specific
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
proposal_type: sector_shadow_only
confidence: medium
production_change_now: false
```

Rule candidate:

```text
For C29, Stage2-Actionable can be allowed when at least two of the following are visible:
- OEM volume/mix improvement,
- margin resilience or ASP/mix bridge,
- shareholder return / capital-return rerating,
- relative strength vs auto/market peers,
- early revision signal.

But Stage3-Green should require confirmed margin/revision/FCF bridge.
Supplier names with customer/order/ADAS/EV-volume narrative but weak margin bridge should be capped at Stage2/watch or Yellow, not Green.
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_id: C29_GREEN_SUPPLIER_MARGIN_FCF_GATE
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
changed_axes:
  - C29_supplier_green_margin_bridge_required
  - C29_OEM_stage2_actionability_allowed_with_capital_return
  - C29_price_only_local_peak_not_full_4B_without_non_price_evidence
```

Suggested shadow behavior:

```text
if canonical_archetype_id == C29 and company_subtype == OEM:
    Stage2_Actionable may receive +1 C29 bridge credit when mix/margin/capital-return evidence coexists.

if canonical_archetype_id == C29 and company_subtype == supplier:
    Green requires confirmed margin_bridge_score and revision_score.
    Customer/order narrative alone cannot promote to Green.

if C29 local peak follows sharp price move but lacks valuation/revision/positioning evidence:
    classify as price_only_local_peak_watch, not full_4B.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_trigger_count | selected representatives | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | alignment verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline_current | 4 | 4 | 32.46 | -6.56 | 36.26 | -9.30 | 0.50 | 0 | 2 | 0.636 | mixed: OEM good, supplier too permissive |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 4 | 32.46 | -6.56 | 36.26 | -9.30 | 0.50 | 1 | 1 | 0.636 | weaker Stage2 capture for OEM |
| P1_R9_sector_specific_candidate | sector_shadow | 4 | 4 | 32.46 | -6.56 | 36.26 | -9.30 | 0.25 | 0 | 1 | 0.471 | better split between OEM and supplier |
| P2_C29_canonical_candidate | canonical_shadow | 4 | 4 | 32.46 | -6.56 | 36.26 | -9.30 | 0.25 | 0 | 1 | 0.471 | best C29 compression |
| P3_C29_counterexample_guard | guard_shadow | 4 | 4 | 30.86 | -6.56 | 34.66 | -9.30 | 0.00 | 1 | 1 | 0.471 | safer, slightly more missed supplier upside |

## 20. Score-Return Alignment Matrix

### 20.1 Raw component score proxy

Scores are research proxies, not production scores.

| trigger_id | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | relative_strength_score | customer_quality_score | policy_or_regulatory_score | valuation_repricing_score | execution_risk_score | legal_or_contract_risk_score | dilution_cb_risk_score | accounting_trust_risk_score | weighted_before | stage_before | weighted_after | stage_after | score_return_alignment_label |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| TR-C29-HYUNDAI-S2A-20240125 | 2 | 2 | 8 | 8 | 9 | 7 | 1 | 8 | -1 | 0 | 0 | 0 | 82 | Stage2-Actionable | 84 | Stage2-Actionable | strong_positive_alignment |
| TR-C29-KIA-S2A-20240125 | 2 | 2 | 8 | 8 | 9 | 7 | 1 | 7 | -1 | 0 | 0 | 0 | 81 | Stage2-Actionable | 83 | Stage2-Actionable | strong_positive_alignment |
| TR-C29-HLMANDO-S2A-20240429 | 4 | 3 | 4 | 3 | 8 | 6 | 1 | 5 | -4 | 0 | 0 | 0 | 74 | Stage2-Actionable | 72 | Stage2/watch | local_mfe_but_green_guard_needed |
| TR-C29-HLMANDO-GREEN-20240605 | 4 | 3 | 4 | 4 | 9 | 6 | 1 | 6 | -5 | 0 | 0 | 0 | 87 | Stage3-Green | 78 | Stage3-Yellow/watch | false_green_reduced |
| TR-C29-HANON-S2-20230125 | 2 | 2 | 2 | 2 | 5 | 5 | 1 | 4 | -6 | 0 | 0 | 0 | 76 | Stage2-Actionable/Yellow | 68 | Stage2/watch | false_positive_reduced |

### 20.2 Component delta explanation

```text
C29 OEM cases retain Stage2-Actionable because margin_bridge_score + revision_score + valuation/capital-return evidence line up.
C29 supplier cases lose Green credit unless margin_bridge_score and revision_score are confirmed.
C29 EV/thermal headline cases lose actionability credit when execution_risk_score is high and margin_bridge_score is weak.
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | MOBILITY_VOLUME_MIX_MARGIN_CAPITAL_RETURN_BRIDGE | 2 | 2 | 2 | 0 | 4 | 1 | 6 | 4 | 2 | true | true | supplier margin/FCF bridge now covered; still need logistics/leisure subcases in future R9 loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids:
  - C29-HYUNDAI-2024-VALUEUP-MIX as 4B overlay reuse within same case
new_symbol_count: 4
same_archetype_new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
same_archetype_new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - C29_supplier_green_false_positive
  - C29_volume_headline_without_margin_bridge
new_axis_proposed: null
existing_axis_strengthened:
  - C29-specific Stage2 bridge for OEM mix/margin/capital return
  - C29-specific Green margin/revision gate for suppliers
  - full_4b_requires_non_price_evidence kept and clarified for C29 local peaks
existing_axis_weakened: null
existing_axis_kept:
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled_round / scheduled_loop / filename consistency
- R9 large-sector consistency using the mobility/EV branch
- stock-web manifest/schema/profile paths
- tradable_raw OHLC rows for representative triggers
- 30D/90D/180D MFE/MAE approximations from actual visible OHLC rows
- positive/counterexample balance
- same_entry_group dedupe policy
- local vs full-window 4B separation
```

Not validated in this MD:

```text
- no stock_agent src/e2r code opened
- no production scoring patch
- no live candidate scan
- no brokerage/API execution
- no full 2Y adjusted-return calculation, because price basis is raw_unadjusted_marcap
- no hard 4C scoring change
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_OEM_mix_margin_capital_return_stage2_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"OEM mix/margin/capital-return cases showed strong 90D/180D MFE from Stage2 entries","improves early capture without global threshold change","TR-C29-HYUNDAI-S2A-20240125|TR-C29-KIA-S2A-20240125",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_green_margin_fcf_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Supplier/thermal narratives had weak post-Green or weak rerating unless margin/FCF bridge was visible","reduces false Green in HL Mando / Hanon-like cases","TR-C29-HLMANDO-GREEN-20240605|TR-C29-HANON-S2-20230125",2,2,2,medium,canonical_shadow_only,"not production; strengthens existing Green strictness only for C29"
shadow_weight,C29_price_only_local_peak_not_full_4B,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,1,1,0,"Existing full_4b_requires_non_price_evidence is kept; C29 local peak must be split from full-window 4B","prevents local-top over-labeling","TR-C29-HYUNDAI-4B-20240627|TR-C29-HLMANDO-GREEN-20240605",2,1,1,medium,axis_strengthened,"not new global axis"
```

## 25. Machine-Readable Rows

### 25.1 JSONL rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C29-HYUNDAI-2024-VALUEUP-MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-HYUNDAI-S2A-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 captured OEM mix/margin/capital-return rerating before full-window peak."}
{"row_type":"case","case_id":"C29-KIA-2024-MIX-CAPRETURN","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TR-C29-KIA-S2A-20240125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2 captured better asymmetry than later Green."}
{"row_type":"case","case_id":"C29-HLMANDO-2024-ADAS-LOCALPEAK","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_PARTS_ORDER_NARRATIVE_LOCAL_PEAK","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-HLMANDO-S2A-20240429","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local_mfe_but_green_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Supplier narrative gave local MFE but Green after peak had poor forward asymmetry."}
{"row_type":"case","case_id":"C29-HANON-2023-THERMAL-FALSEBRIDGE","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_VOLUME_FALSE_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TR-C29-HANON-S2-20230125","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_rerating_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"EV thermal/volume story without margin/FCF bridge produced limited MFE and persistent MAE."}
{"row_type":"trigger","trigger_id":"TR-C29-HYUNDAI-S2A-20240125","case_id":"C29-HYUNDAI-2024-VALUEUP-MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN","sector":"mobility_auto_oem","primary_archetype":"OEM mix/margin/capital-return rerating","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":188700,"evidence_available_at_that_date":"FY2023 result/capital-return/mix-margin discussion visible by trigger window","evidence_source":"historical public result/disclosure proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":38.31,"MFE_90D_pct":47.06,"MFE_180D_pct":58.72,"MFE_1Y_pct":58.72,"MFE_2Y_pct":null,"MAE_30D_pct":-2.76,"MAE_90D_pct":-2.76,"MAE_180D_pct":-2.76,"MAE_1Y_pct":-2.76,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-16.19,"green_lateness_ratio":0.346,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-HYUNDAI-20240125","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-HYUNDAI-4B-20240627","case_id":"C29-HYUNDAI-2024-VALUEUP-MIX","symbol":"005380","company_name":"현대차","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN","sector":"mobility_auto_oem","primary_archetype":"OEM full-window 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-27","entry_date":"2024-06-27","entry_price":298000,"evidence_available_at_that_date":"valuation/positioning overheat proxy near observed full-window high","evidence_source":"historical valuation/positioning overlay proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.50,"MFE_90D_pct":0.50,"MFE_180D_pct":0.50,"MFE_1Y_pct":0.50,"MFE_2Y_pct":null,"MAE_30D_pct":-14.43,"MAE_90D_pct":-15.60,"MAE_180D_pct":-16.19,"MAE_1Y_pct":-16.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-16.19,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.986,"four_b_full_window_peak_proximity":0.986,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-HYUNDAI-20240627","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same Hyundai case reused only for 4B overlay timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR-C29-KIA-S2A-20240125","case_id":"C29-KIA-2024-MIX-CAPRETURN","symbol":"000270","company_name":"기아","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_VALUEUP_MIX_MARGIN_CAPITAL_RETURN","sector":"mobility_auto_oem","primary_archetype":"OEM mix/capital-return rerating","loop_objective":"coverage_gap_fill|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":93000,"evidence_available_at_that_date":"FY2023 result/capital-return/mix-margin discussion visible by trigger window","evidence_source":"historical public result/disclosure proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.45,"MFE_90D_pct":41.61,"MFE_180D_pct":45.16,"MFE_1Y_pct":45.16,"MFE_2Y_pct":null,"MAE_30D_pct":-7.42,"MAE_90D_pct":-7.42,"MAE_180D_pct":-7.42,"MAE_1Y_pct":-7.42,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-18.52,"green_lateness_ratio":0.631,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-KIA-20240125","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-HLMANDO-S2A-20240429","case_id":"C29-HLMANDO-2024-ADAS-LOCALPEAK","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_PARTS_ORDER_NARRATIVE_LOCAL_PEAK","sector":"mobility_auto_parts","primary_archetype":"supplier order/ADAS narrative local peak","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-29","entry_date":"2024-04-29","entry_price":38350,"evidence_available_at_that_date":"ADAS/order/customer narrative plus relative strength visible","evidence_source":"historical public/report proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["partial_margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.60,"MFE_90D_pct":30.38,"MFE_180D_pct":30.38,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.48,"MAE_90D_pct":-5.48,"MAE_180D_pct":-17.34,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-23.20,"green_lateness_ratio":0.966,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_guard","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-HLMANDO-20240429","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TR-C29-HLMANDO-GREEN-20240605","case_id":"C29-HLMANDO-2024-ADAS-LOCALPEAK","symbol":"204320","company_name":"HL만도","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_PARTS_ORDER_NARRATIVE_LOCAL_PEAK","sector":"mobility_auto_parts","primary_archetype":"supplier late Green false positive","loop_objective":"green_strictness_stress_test|4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":49600,"evidence_available_at_that_date":"price/local peak plus supplier narrative; margin bridge incomplete","evidence_source":"historical public/report proxy + stock-web price path","stage2_evidence_fields":[],"stage3_evidence_fields":["partial_margin_bridge"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.81,"MFE_90D_pct":0.81,"MFE_180D_pct":0.81,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.22,"MAE_90D_pct":-22.48,"MAE_180D_pct":-22.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-05","peak_price":50000,"drawdown_after_peak_pct":-23.20,"green_lateness_ratio":0.966,"four_b_local_peak_proximity":0.966,"four_b_full_window_peak_proximity":0.966,"four_b_timing_verdict":"price_only_local_4B_too_early_if_no_non_price_evidence","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-HLMANDO-20240605","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same HL Mando case reused to test Green lateness and local peak after Stage2","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"TR-C29-HANON-S2-20230125","case_id":"C29-HANON-2023-THERMAL-FALSEBRIDGE","symbol":"018880","company_name":"한온시스템","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"EV_THERMAL_VOLUME_FALSE_BRIDGE","sector":"mobility_auto_parts_thermal","primary_archetype":"EV thermal volume false bridge","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2","trigger_date":"2023-01-25","entry_date":"2023-01-25","entry_price":9180,"evidence_available_at_that_date":"thermal/EV volume narrative visible but margin/FCF bridge weak","evidence_source":"historical public/report proxy","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv","profile_path":"atlas/symbol_profiles/018/018880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.43,"MFE_90D_pct":10.78,"MFE_180D_pct":10.78,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-2.72,"MAE_90D_pct":-10.57,"MAE_180D_pct":-11.66,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-05-10","peak_price":10170,"drawdown_after_peak_pct":-20.26,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"G-C29-HANON-20230125","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C29-HLMANDO-2024-ADAS-LOCALPEAK","trigger_id":"TR-C29-HLMANDO-GREEN-20240605","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":87,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":6,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow/watch","changed_components":["C29_supplier_green_margin_fcf_gate"],"component_delta_explanation":"Supplier Green blocked without confirmed margin/FCF bridge; relative strength no longer substitutes for margin bridge.","MFE_90D_pct":0.81,"MAE_90D_pct":-22.48,"score_return_alignment_label":"false_green_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C29_canonical_shadow_profile","case_id":"C29-HYUNDAI-2024-VALUEUP-MIX","trigger_id":"TR-C29-HYUNDAI-S2A-20240125","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":9,"customer_quality_score":7,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable","changed_components":["C29_OEM_mix_margin_capital_return_stage2_bridge"],"component_delta_explanation":"OEM Stage2 bridge preserved because mix/margin/capital-return evidence supports early rerating.","MFE_90D_pct":47.06,"MAE_90D_pct":-2.76,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R9","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["C29_supplier_green_false_positive","C29_volume_headline_without_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.2 Narrative-only rows

No narrative-only case is used for quantitative calibration in this file.

```jsonl
{"row_type":"narrative_only","case_id":"none","reason":"no blocked historical case used","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 10
next_round = R10
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files inspected for this MD:

```text
stock_agent research artifact:
- reports/e2r_calibration/by_round/R9.md

stock-web atlas:
- atlas/manifest.json
- atlas/schema.json
- atlas/symbol_profiles/005/005380.json
- atlas/symbol_profiles/000/000270.json
- atlas/symbol_profiles/204/204320.json
- atlas/symbol_profiles/018/018880.json
- atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/018/018880/2023.csv
```

External / live sources intentionally not used.

