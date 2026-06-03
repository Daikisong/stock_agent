# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 13
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT
output_file: e2r_stock_web_v12_residual_round_R1_loop_13_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
current_stock_discovery_allowed: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 8 new independent trigger/case rows, 4 counterexamples, and 4 current-profile residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C02_POWER_GRID_DATACENTER_CAPEX.

The previous generated residual file ended with `next_round = R1` and `next_loop = 13`; therefore this file uses `R1 / Loop 13`. Because R1 is hard-mapped to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`, the sector consistency gate passes.

## 1. Current Calibrated Profile Assumption

Current proxy profile:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The loop does not re-argue the global calibration. It stress-tests the remaining R1/C02 gap: in grid/datacenter-capex names, the system can still become too late on structural entries when early MAE is high, while price-only blowoff must remain an overlay rather than a positive-stage promoter or hard 4C trigger.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R1
loop = 13
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT
loop_objective =
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - yellow_threshold_stress_test
  - green_strictness_stress_test
  - 4B_non_price_requirement_stress_test
  - counterexample_mining
  - coverage_gap_fill
```

R1/C02 was chosen because the 2024 Korean power-grid equipment cycle supplies a clean basket of transformer, switchgear, and cable-related cases. It gives both sides of the calibration problem: structural winners that needed earlier recognition, and overheated local peaks that should not become full 4B/4C without non-price deterioration.

## 3. Previous Coverage / Duplicate Avoidance Check

The allowed stock_agent registry was accessible, but the visible registry entries were older `e2r_stock_web_historical_calibration_round_*` files rather than the current v12 residual naming pattern. No exact v12 residual file for `R1 / Loop 13 / C02` was found in the fetched registry slice.

Novelty gate:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
same_symbol_new_trigger_family = allowed_with_reuse_reason
minimum_new_symbol_count = 2
new_symbol_count = 4
positive_case_count = 4
counterexample_count = 4
calibration_usable_case_count = 8
```

The repeated symbols in the 4B overlay section are not reused Stage2 triggers. They are new trigger-family rows: the same company’s structural entry and later price-only local peak are different calibration questions.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web validation summary:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/Songdaiki/stock-web
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The Stock-Web manifest states that the atlas is raw/unadjusted marcap data, that the calibration shard root is `atlas/ohlcv_tradable_by_symbol_year`, that raw rows remain visible under `atlas/ohlcv_raw_by_symbol_year`, and that corporate-action contaminated windows should be blocked by default. The schema defines tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and the MFE/MAE formula used here.

## 5. Historical Eligibility Gate

All quantitative rows in this file satisfy:

```text
trigger_date is historical
entry_date exists in stock-web tradable shard
entry_date has at least 180 forward trading days available before manifest max_date
entry row has positive OHLCV
MFE_30D / 90D / 180D and MAE_30D / 90D / 180D are calculated
corporate-action-contaminated 180D window is false
```

One additional narrative-only candidate is retained for duplicate/coverage context but excluded from weight calibration:

```text
대한전선 / 001440 / 2024-01-03 candidate
profile corporate_action_candidate_dates includes 2024-04-02
entry~D+180 window is contaminated
calibration_usable = false
```

## 6. Canonical Archetype Compression Map

```text
C02_POWER_GRID_DATACENTER_CAPEX
  fine_archetype:
    GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT
  compressed evidence families:
    1. order/backlog visibility in transformer, switchgear, and grid equipment
    2. margin bridge from supply shortage and high-value export mix
    3. capacity or shipment route visible enough to convert narrative into earnings
    4. local price-only 4B overlay after rerating acceleration
    5. hard 4C only when thesis evidence breaks, not when price simply draws down
```

## 7. Case Selection Summary

| case_id | symbol | company | role | pos/counter | trigger | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R1L13_C02_HDHE_STAGE2_20240103 | 267260 | HD현대일렉트릭 | structural_success | positive | Stage2-Actionable | 2024-01-03 | 85800 | 219.93 | -5.24 | 336.48 | -5.24 | current_profile_too_late |
| R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | 효성중공업 | structural_success | positive | Stage2-Actionable | 2024-01-03 | 167900 | 112.63 | -7.03 | 179.33 | -7.03 | current_profile_too_late |
| R1L13_C02_LSE_STAGE2_20240103 | 010120 | LS ELECTRIC | high_mae_success | positive | Stage2-Actionable | 2024-01-03 | 73500 | 231.97 | -14.15 | 273.47 | -14.15 | current_profile_missed_structural |
| R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | 일진전기 | structural_success | positive | Stage2-Actionable | 2024-02-14 | 11780 | 156.79 | -12.48 | 156.79 | -12.48 | current_profile_missed_structural |
| R1L13_C02_HDHE_PRICE_ONLY_4B_20240724 | 267260 | HD현대일렉트릭 | 4B_overlay_success | counterexample | Stage4B-Overlay | 2024-07-24 | 365500 | 2.46 | -34.88 | 23.12 | -34.88 | current_profile_correct |
| R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528 | 298040 | 효성중공업 | 4B_overlay_success | counterexample | Stage4B-Overlay | 2024-05-28 | 449500 | 4.34 | -48.61 | 22.14 | -48.61 | current_profile_correct |
| R1L13_C02_LSE_PRICE_ONLY_4B_20240724 | 010120 | LS ELECTRIC | 4B_overlay_success | counterexample | Stage4B-Overlay | 2024-07-24 | 260000 | 5.58 | -44.23 | 16.73 | -44.23 | current_profile_correct |
| R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529 | 103590 | 일진전기 | 4B_overlay_success | counterexample | Stage4B-Overlay | 2024-05-29 | 28600 | 5.77 | -21.68 | 5.77 | -41.96 | current_profile_correct |

## 8. Positive vs Counterexample Balance

```text
positive_structural_success = 4
counterexample_or_failed_rerating = 4
4B_case_count = 4
4C_case_count = 0
calibration_usable_case_count = 8
narrative_only_blocked_case_count = 1
```

Interpretation:

* The positive rows argue that C02 should not wait for perfect Green confirmation when order/backlog quality and margin bridge are already visible.
* The counterexample rows argue the opposite edge: once the same stocks reach a price-only local blowoff, full 4B or hard 4C requires non-price evidence. A local peak is a warning light, not a thesis-break document.

## 9. Evidence Source Map

| evidence family | positive rows | counterexample rows | calibration meaning |
| --- | --- | --- | --- |
| public_event_or_disclosure | 4 | 0 | establishes non-price trigger availability |
| customer_or_order_quality | 4 | 0 | separates real grid CAPEX cycle from pure theme |
| backlog_or_delivery_visibility | 4 | 0 | C02 positive-stage bridge |
| margin_bridge | 4 | 0 | key difference between structural rerating and low-quality momentum |
| valuation_blowoff / positioning_overheat | 0 | 4 | 4B overlay only |
| price_only_local_peak | 0 | 4 | cannot promote Stage2/3 and cannot route to hard 4C |

## 10. Price Data Source Map

| symbol | company | profile path | price shard path | profile caveat |
| --- | --- | --- | --- | --- |
| 267260 | HD현대일렉트릭 | atlas/symbol_profiles/267/267260.json | atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv; 2025.csv | historical corporate action candidates exist before 2020, but 2024~180D window is clean |
| 298040 | 효성중공업 | atlas/symbol_profiles/298/298040.json | atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv; 2025.csv | corporate_action_candidate_count = 0 |
| 010120 | LS ELECTRIC | atlas/symbol_profiles/010/010120.json | atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv; 2025.csv | old corporate action candidates before 2004; 2024~180D window is clean |
| 103590 | 일진전기 | atlas/symbol_profiles/103/103590.json | atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv | 2024-02-13 candidate avoided by entry_date = 2024-02-14 |
| 001440 | 대한전선 | atlas/symbol_profiles/001/001440.json | not used quantitatively | 2024-04-02 candidate contaminates Jan-entry 180D window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B fields | corp_action_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRIG_R1L13_C02_HDHE_STAGE2_20240103 | 267260 | Stage2-Actionable | 2024-01-02 | 2024-01-03 | 85800 | public_event_or_disclosure,customer_or_order_quality,relative_strength,capacity_or_volume_route,backlog_or_delivery_visibility,early_revision_signal | confirmed_revision,margin_bridge,multiple_public_sources,financial_visibility,durable_customer_confirmation | - | clean_180D_window |
| TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103 | 298040 | Stage2-Actionable | 2024-01-02 | 2024-01-03 | 167900 | public_event_or_disclosure,customer_or_order_quality,relative_strength,capacity_or_volume_route,backlog_or_delivery_visibility | confirmed_revision,margin_bridge,multiple_public_sources,financial_visibility | - | clean_180D_window |
| TRIG_R1L13_C02_LSE_STAGE2_20240103 | 010120 | Stage2-Actionable | 2024-01-02 | 2024-01-03 | 73500 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,policy_or_regulatory_optionality,backlog_or_delivery_visibility | confirmed_revision,margin_bridge,multiple_public_sources,financial_visibility | - | clean_180D_window |
| TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 103590 | Stage2-Actionable | 2024-02-13 | 2024-02-14 | 11780 | public_event_or_disclosure,customer_or_order_quality,relative_strength,backlog_or_delivery_visibility,early_revision_signal | confirmed_revision,margin_bridge,multiple_public_sources,financial_visibility | - | clean_after_2024-02-13_corporate_action_candidate |
| TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724 | 267260 | Stage4B-Overlay | 2024-07-24 | 2024-07-24 | 365500 | - | - | valuation_blowoff,positioning_overheat,price_only_local_peak | clean_180D_window |
| TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528 | 298040 | Stage4B-Overlay | 2024-05-28 | 2024-05-28 | 449500 | - | - | valuation_blowoff,positioning_overheat,price_only_local_peak | clean_180D_window |
| TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724 | 010120 | Stage4B-Overlay | 2024-07-24 | 2024-07-24 | 260000 | - | - | valuation_blowoff,positioning_overheat,price_only_local_peak | clean_180D_window |
| TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529 | 103590 | Stage4B-Overlay | 2024-05-29 | 2024-05-29 | 28600 | - | - | valuation_blowoff,positioning_overheat,price_only_local_peak | clean_after_2024-02-13_corporate_action_candidate |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TRIG_R1L13_C02_HDHE_STAGE2_20240103 | 85800 | 39.04 | 219.93 | 336.48 | -5.24 | -5.24 | -5.24 | 2024-07-24 | 374500 | -36.45 | structural_grid_capex_rerating_success |
| TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103 | 167900 | 14.23 | 112.63 | 179.33 | -7.03 | -7.03 | -7.03 | 2024-05-28 | 469000 | -50.75 | transformer_order_backlog_rerating_success |
| TRIG_R1L13_C02_LSE_STAGE2_20240103 | 73500 | 6.12 | 231.97 | 273.47 | -12.52 | -14.15 | -14.15 | 2024-07-24 | 274500 | -47.18 | grid_capex_rerating_after_initial_drawdown |
| TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 11780 | 82.09 | 156.79 | 156.79 | -12.48 | -12.48 | -12.48 | 2024-05-29 | 30250 | -45.12 | post_ca_clean_entry_structural_success |
| TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724 | 365500 | 2.46 | 2.46 | 23.12 | -34.88 | -34.88 | -34.88 | 2025-01-24 | 450000 | -41.22 | price_only_local_4B_not_full_exit |
| TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528 | 449500 | 4.34 | 4.34 | 22.14 | -18.47 | -48.61 | -48.61 | 2025-02-06 | 549000 | -30.42 | local_peak_mae_shock_but_not_full_4c |
| TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724 | 260000 | 5.58 | 5.58 | 16.73 | -44.23 | -44.23 | -44.23 | 2025-02-19 | 303500 | -52.22 | high_MAE_local_4B_but_not_hard_4C |
| TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529 | 28600 | 5.77 | 5.77 | 5.77 | -17.83 | -21.68 | -41.96 | 2024-05-29 | 30250 | -45.12 | price_only_overheat_with_large_drawdown |

Important pattern:

```text
positive representative rows:
  avg MFE_90D = 180.33
  avg MAE_90D = -9.72
  avg MFE_180D = 236.52
  avg MAE_180D = -9.72

4B overlay rows:
  avg MFE_90D = 4.54
  avg MAE_90D = -37.35
  avg MFE_180D = 16.94
  avg MAE_180D = -42.42
```

The positive entries have high upside even when early MAE exists. The 4B rows have limited near-term MFE and very large MAE, but several later retest or exceed the local peak. Therefore, C02 needs a two-door model: one door for structural entry, another door for local risk overlay.

## 13. Current Calibrated Profile Stress Test

| case_id | company | current_profile_verdict | before_label | after_shadow_label | MFE180 | MAE90 | stress_result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1L13_C02_HDHE_STAGE2_20240103 | HD현대일렉트릭 | current_profile_too_late | Stage3-Yellow | Stage3-Green | 336.48 | -5.24 | residual_error |
| R1L13_C02_HYOSUNG_STAGE2_20240103 | 효성중공업 | current_profile_too_late | Stage3-Yellow | Stage3-Green | 179.33 | -7.03 | residual_error |
| R1L13_C02_LSE_STAGE2_20240103 | LS ELECTRIC | current_profile_missed_structural | Stage2-Actionable | Stage3-Yellow | 273.47 | -14.15 | residual_error |
| R1L13_C02_ILJIN_POST_CA_STAGE2_20240214 | 일진전기 | current_profile_missed_structural | Stage2-Actionable | Stage3-Yellow | 156.79 | -12.48 | residual_error |
| R1L13_C02_HDHE_PRICE_ONLY_4B_20240724 | HD현대일렉트릭 | current_profile_correct | Stage3-Green | Stage4B-Overlay | 23.12 | -34.88 | correct |
| R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528 | 효성중공업 | current_profile_correct | Stage3-Green | Stage4B-Overlay | 22.14 | -48.61 | correct |
| R1L13_C02_LSE_PRICE_ONLY_4B_20240724 | LS ELECTRIC | current_profile_correct | Stage3-Green | Stage4B-Overlay | 16.73 | -44.23 | correct |
| R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529 | 일진전기 | current_profile_correct | Stage3-Yellow | Stage4B-Overlay | 5.77 | -21.68 | correct |

Answers to the calibrated-profile questions:

1. Current profile would generally promote HD현대일렉트릭 and 효성중공업, but it is still likely late because strict Green waits for visible revision confirmation after a large part of the move.
2. For LS ELECTRIC and 일진전기, the high early MAE can cause under-promotion even though the 180D MFE is very strong.
3. The existing Stage2 bonus is useful but insufficient when C02 order quality and margin bridge are present together.
4. Yellow 75 is acceptable globally, but in C02 the evidence composition matters more than the raw total.
5. Green 87 / revision 55 is too strict for some C02 entries if margin bridge is already visible and the forward MFE validates the thesis.
6. The price-only blowoff guard remains appropriate.
7. The full 4B non-price requirement remains appropriate and is strengthened by this loop.
8. Hard 4C should not route on price drawdown alone in these examples; no hard 4C evidence appeared in the tested rows.

## 14. Stage2 / Yellow / Green Comparison

For the four representative positive cases, Stage2-Actionable was the best entry family. Stage3-Green, where simulated, was not wrong but later.

| case | Stage2_Actionable entry | simulated Green tendency | green_lateness_ratio | verdict |
| --- | --- | --- | --- | --- |
| HD현대일렉트릭 | 2024-01-03 / 85,800 | likely after revision confirmation | 0.24 | Green not fatal but late |
| 효성중공업 | 2024-01-03 / 167,900 | likely after rerating became obvious | 0.32 | Green loses material upside |
| LS ELECTRIC | 2024-01-03 / 73,500 | likely delayed by early MAE and revision strictness | 0.45 | Stage2 bridge needed |
| 일진전기 | 2024-02-14 / 11,780 | likely delayed by post-CA and smaller-cap risk | 0.40 | Stage2 bridge needed |

## 15. 4B Local vs Full-window Timing Audit

| case | local 4B entry | local peak proximity | full-window peak proximity | verdict |
| --- | ---: | ---: | ---: | --- |
| HD현대일렉트릭 | 365,500 | 0.97 | 0.77 | local 4B is useful, but full exit still needs non-price deterioration |
| 효성중공업 | 449,500 | 0.94 | 0.74 | price-only local 4B too early for full-cycle exit |
| LS ELECTRIC | 260,000 | 0.93 | 0.81 | high MAE warning, not hard 4C |
| 일진전기 | 28,600 | 0.91 | 0.91 | good local 4B overlay, but still not thesis break |

The split matters because a local peak behaves like a fever. It says the body is hot; it does not diagnose the disease. Full 4B needs non-price deterioration such as revision slowdown, order delay, margin reversal, dilution, legal block, or explicit event cap.

## 16. 4C Protection Audit

No quantitative hard-4C row is promoted in this loop.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = 0
hard_4c_late = 0
false_break = 0
```

Reason: every tested 4B row is price/valuation/positioning driven. There is no contract cancellation, qualification failure, accounting trust break, forced liquidation, or explicit thesis evidence break in the selected rows. Therefore, hard 4C routing would be too aggressive.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

The evidence is strong inside R1, but the proposed rule is more naturally canonical-archetype-specific than sector-wide. R1 also contains defense, nuclear, EPC, and industrial orders. The C02 grid/datacenter-capex pattern should not automatically spill into all R1 names.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
proposal = C02_order_quality_margin_bridge_bonus + C02_price_only_local_4B_overlay_only
```

Proposed C02 shadow rules:

```text
1. If customer/order quality + backlog visibility + margin bridge are all present,
   allow a C02 bridge bonus before full Green confirmation.

2. If early MAE is high but there is no thesis break and the order/margin bridge is intact,
   do not discard the row as a false positive solely because MAE_30D or MAE_90D is ugly.

3. If the trigger is price-only local blowoff,
   keep it as Stage4B-Overlay only.
   Do not treat it as a positive-stage promoter.
   Do not route to hard 4C unless thesis evidence breaks.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 8 | 92.43 | -23.54 | 126.73 | -26.07 | 2/8 | 2 | 2 | usable_but_misses_high_MAE_structural_entries |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 8 | 92.43 | -23.54 | 126.73 | -26.07 | 4/8 | 1 | 3 | too_price_momentum_sensitive |
| P1_L1_grid_capex_shadow_profile | sector_specific | margin_bridge_floor +2; high_MAE_structural_exception; no production change | 8 | 180.33 | -9.72 | 236.52 | -9.72 | 0/4 representative | 0 | 1 | better_positive_entry_alignment |
| P2_C02_archetype_shadow_profile | canonical_archetype_specific | C02_order_quality_margin_bridge_bonus +1.5; C02_price_only_4B_stays_overlay | 8 | 92.43 | -23.54 | 126.73 | -26.07 | 1/8 | 0 | 1 | best_balance |
| P3_counterexample_guard_profile | guardrail | keep price_only_blowoff_blocks_positive_stage; strengthen local/full 4B split | 4 | 4.54 | -37.35 | 16.94 | -42.42 | 0/4 if overlay-only | 0 | 0 | protects_against_full_exit_false_positive |

## 20. Score-Return Alignment Matrix

| alignment type | rows | score behavior | return behavior | conclusion |
| --- | ---: | --- | --- | --- |
| structural bridge success | 4 | after-shadow score rises to Yellow/Green bridge | avg 180D MFE > 236% | positive C02 bridge valid |
| high-MAE structural success | 2 | current profile can hesitate | MAE around -12% to -14%, but 180D MFE > 150% | high MAE alone should not kill C02 if evidence bridge remains |
| price-only 4B overlay | 4 | after-shadow lowers positive label to overlay | avg 90D MAE around -37% | local risk warning valid |
| hard 4C | 0 | not triggered | no thesis break evidence | hard 4C kept inactive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C02_POWER_GRID_DATACENTER_CAPEX | GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT | 4 | 4 | 4 | 0 | 8 | 4 | 8 | 4 | 4 | False | True | C02 now has 4 positive structural entries, 4 price-only 4B overlay counterexamples, and one narrative-only CA-blocked symbol. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 8
reused_case_count: 4
reused_case_ids:
  - R1L13_C02_HDHE_PRICE_ONLY_4B_20240724
  - R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528
  - R1L13_C02_LSE_PRICE_ONLY_4B_20240724
  - R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529
new_symbol_count: 4
new_canonical_archetype_count: 1
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
  - current_profile_missed_structural
  - current_profile_too_late
  - price_only_local_4B_can_be_too_early_for_full_exit
new_axis_proposed:
  - C02_order_quality_margin_bridge_bonus
  - C02_high_MAE_structural_exception
  - C02_price_only_local_4B_overlay_only
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest/schema fields
- ticker normalization as six-digit code
- profile availability and corporate-action windows
- actual tradable OHLC rows for entry and observed peak/low points
- 30D/90D/180D MFE/MAE
- R1 round-sector consistency
- positive/counterexample balance
- same-symbol new-trigger-family reuse logic
```

Not validated:

```text
- live 2026 candidate status
- current recommendation
- brokerage API or auto-trading route
- stock_agent production code
- exact production score internals
- global profile promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C02_order_quality_margin_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1.5,+1.5,C02 positives with order/backlog + margin bridge showed high 90D/180D MFE even when Green was late,reduced missed_structural_count from 2 to 0,TRIG_R1L13_C02_HDHE_STAGE2_20240103|TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103|TRIG_R1L13_C02_LSE_STAGE2_20240103|TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214,4,4,0,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C02_high_MAE_structural_exception,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,0,1,+1,LS ELECTRIC/일진전기 show early MAE below -12% but strong 180D rerating when order-quality and margin bridge persist,prevents high-MAE structural successes from being discarded,TRIG_R1L13_C02_LSE_STAGE2_20240103|TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214,2,2,0,low_to_medium,canonical_shadow_only,needs more holdout
shadow_weight,C02_price_only_local_4B_overlay_only,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,1,1.5,+0.5,four 4B overlay rows show price-only local peaks had large MAE but several later recovered to new full-window highs,separates local risk from hard 4C or full exit,TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724|TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528|TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724|TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529,4,4,4,medium,canonical_shadow_only,strengthens existing full_4b_requires_non_price_evidence
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L13_C02_HDHE_STAGE2_20240103","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRIG_R1L13_C02_HDHE_STAGE2_20240103","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_grid_capex_rerating_success","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2024년 초 이미 공개되어 있던 북미·중동 전력기기 수요, 변압기 공급부족, 수주잔고/마진 개선 기대를 새해 첫 거래가능 구간에 고정한 holdout trigger."}
{"row_type":"case","case_id":"R1L13_C02_HYOSUNG_STAGE2_20240103","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"transformer_order_backlog_rerating_success","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"2024년 초 중공업 부문의 변압기/전력설비 수요와 수익성 개선이 이미 시장 내 공개 narrative로 존재한 상태에서 고정한 holdout trigger."}
{"row_type":"case","case_id":"R1L13_C02_LSE_STAGE2_20240103","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TRIG_R1L13_C02_LSE_STAGE2_20240103","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"grid_capex_rerating_after_initial_drawdown","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"2024년 초 전력기기/전력자동화 수요와 데이터센터·배전망 투자 narrative가 열려 있었지만, 초기 MAE가 큰 high-MAE success 표본."}
{"row_type":"case","case_id":"R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","symbol":"103590","company_name":"일진전기","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"post_ca_clean_entry_structural_success","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"2024-02-13 주식수 변동 candidate 이후 다음 거래일을 entry로 고정해, corporate-action contaminated day를 피한 전력기기/전선 order-quality 표본."}
{"row_type":"case","case_id":"R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"score_price_alignment":"price_only_local_4B_not_full_exit","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024-07-24 고가 374,500 / 종가 365,500의 local price-only blowoff. non-price 4B evidence가 충분하지 않으면 full 4B가 아니라 risk overlay로만 취급해야 하는 표본."}
{"row_type":"case","case_id":"R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"score_price_alignment":"local_peak_mae_shock_but_not_full_4c","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024-05-28 고가 469,000 / 종가 449,500의 price-only local peak. 이후 90D MAE가 매우 크지만 180D에는 재상승해, full 4B와 local risk를 분리해야 한다."}
{"row_type":"case","case_id":"R1L13_C02_LSE_PRICE_ONLY_4B_20240724","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"score_price_alignment":"high_MAE_local_4B_but_not_hard_4C","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024-07-24 고가 274,500 / 종가 260,000. 이후 급락했지만 2025-02-19 303,500까지 재상승했다. price-only 4B를 full exit로 쓰면 구조적 rerating 잔여분을 잃는다."}
{"row_type":"case","case_id":"R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","symbol":"103590","company_name":"일진전기","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"score_price_alignment":"price_only_overheat_with_large_drawdown","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"2024-05-29 고가 30,250 / 종가 28,600의 local blowoff. 180D MAE가 -41.96%라 risk overlay는 필요하지만, non-price thesis break가 없으면 hard 4C로 routing하지 않는다."}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_HDHE_STAGE2_20240103","case_id":"R1L13_C02_HDHE_STAGE2_20240103","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":85800,"evidence_available_at_that_date":"2024년 초 이미 공개되어 있던 북미·중동 전력기기 수요, 변압기 공급부족, 수주잔고/마진 개선 기대를 새해 첫 거래가능 구간에 고정한 holdout trigger.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":39.04,"MFE_90D_pct":219.93,"MFE_180D_pct":336.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.24,"MAE_90D_pct":-5.24,"MAE_180D_pct":-5.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":374500,"drawdown_after_peak_pct":-36.45,"green_lateness_ratio":0.24,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"structural_grid_capex_rerating_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_HDHE_STAGE2_20240103_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103","case_id":"R1L13_C02_HYOSUNG_STAGE2_20240103","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":167900,"evidence_available_at_that_date":"2024년 초 중공업 부문의 변압기/전력설비 수요와 수익성 개선이 이미 시장 내 공개 narrative로 존재한 상태에서 고정한 holdout trigger.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","capacity_or_volume_route","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.23,"MFE_90D_pct":112.63,"MFE_180D_pct":179.33,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.03,"MAE_90D_pct":-7.03,"MAE_180D_pct":-7.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":469000,"drawdown_after_peak_pct":-50.75,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"transformer_order_backlog_rerating_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_HYOSUNG_STAGE2_20240103_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_LSE_STAGE2_20240103","case_id":"R1L13_C02_LSE_STAGE2_20240103","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-02","entry_date":"2024-01-03","entry_price":73500,"evidence_available_at_that_date":"2024년 초 전력기기/전력자동화 수요와 데이터센터·배전망 투자 narrative가 열려 있었지만, 초기 MAE가 큰 high-MAE success 표본.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","policy_or_regulatory_optionality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.12,"MFE_90D_pct":231.97,"MFE_180D_pct":273.47,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.52,"MAE_90D_pct":-14.15,"MAE_180D_pct":-14.15,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-24","peak_price":274500,"drawdown_after_peak_pct":-47.18,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"grid_capex_rerating_after_initial_drawdown","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_LSE_STAGE2_20240103_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","case_id":"R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","symbol":"103590","company_name":"일진전기","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":11780,"evidence_available_at_that_date":"2024-02-13 주식수 변동 candidate 이후 다음 거래일을 entry로 고정해, corporate-action contaminated day를 피한 전력기기/전선 order-quality 표본.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","relative_strength","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":82.09,"MFE_90D_pct":156.79,"MFE_180D_pct":156.79,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.48,"MAE_90D_pct":-12.48,"MAE_180D_pct":-12.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":30250,"drawdown_after_peak_pct":-45.12,"green_lateness_ratio":0.4,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"post_ca_clean_entry_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2024-02-13_corporate_action_candidate","same_entry_group_id":"R1L13_C02_ILJIN_POST_CA_STAGE2_20240214_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","case_id":"R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":365500,"evidence_available_at_that_date":"2024-07-24 고가 374,500 / 종가 365,500의 local price-only blowoff. non-price 4B evidence가 충분하지 않으면 full 4B가 아니라 risk overlay로만 취급해야 하는 표본.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv|atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.46,"MFE_90D_pct":2.46,"MFE_180D_pct":23.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.88,"MAE_90D_pct":-34.88,"MAE_180D_pct":-34.88,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-24","peak_price":450000,"drawdown_after_peak_pct":-41.22,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"price_only_local_4B_not_full_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"price_only_local_4B_not_full_exit","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_HDHE_PRICE_ONLY_4B_20240724_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","case_id":"R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-28","entry_date":"2024-05-28","entry_price":449500,"evidence_available_at_that_date":"2024-05-28 고가 469,000 / 종가 449,500의 price-only local peak. 이후 90D MAE가 매우 크지만 180D에는 재상승해, full 4B와 local risk를 분리해야 한다.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.34,"MFE_90D_pct":4.34,"MFE_180D_pct":22.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.47,"MAE_90D_pct":-48.61,"MAE_180D_pct":-48.61,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-06","peak_price":549000,"drawdown_after_peak_pct":-30.42,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"price_only_local_4B_too_early_for_full_exit","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"local_peak_mae_shock_but_not_full_4c","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724","case_id":"R1L13_C02_LSE_PRICE_ONLY_4B_20240724","symbol":"010120","company_name":"LS ELECTRIC","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":260000,"evidence_available_at_that_date":"2024-07-24 고가 274,500 / 종가 260,000. 이후 급락했지만 2025-02-19 303,500까지 재상승했다. price-only 4B를 full exit로 쓰면 구조적 rerating 잔여분을 잃는다.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv|atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv","profile_path":"atlas/symbol_profiles/010/010120.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.58,"MFE_90D_pct":5.58,"MFE_180D_pct":16.73,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-44.23,"MAE_90D_pct":-44.23,"MAE_180D_pct":-44.23,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":303500,"drawdown_after_peak_pct":-52.22,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.81,"four_b_timing_verdict":"local_4B_risk_overlay_not_thesis_break","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"high_MAE_local_4B_but_not_hard_4C","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L13_C02_LSE_PRICE_ONLY_4B_20240724_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","case_id":"R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","symbol":"103590","company_name":"일진전기","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"GRID_EQUIPMENT_DATACENTER_CAPEX_ORDER_MARGIN_BRIDGE_WITH_4B_LOCAL_PEAK_AUDIT","sector":"industrials_infra_defense_grid","primary_archetype":"power_grid_datacenter_capex","loop_objective":"sector_specific_rule_discovery|4B_non_price_requirement_stress_test|counterexample_mining|coverage_gap_fill","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-29","entry_date":"2024-05-29","entry_price":28600,"evidence_available_at_that_date":"2024-05-29 고가 30,250 / 종가 28,600의 local blowoff. 180D MAE가 -41.96%라 risk overlay는 필요하지만, non-price thesis break가 없으면 hard 4C로 routing하지 않는다.","evidence_source":"public_disclosure_or_market_evidence_at_or_before_trigger_date; stock-web OHLC rows cited in Source Notes","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.77,"MFE_90D_pct":5.77,"MFE_180D_pct":5.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.83,"MAE_90D_pct":-21.68,"MAE_180D_pct":-41.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":30250,"drawdown_after_peak_pct":-45.12,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"good_local_4B_overlay_but_not_4C_without_thesis_break","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"four_c_protection_label":"not_applicable_or_thesis_break_watch_only","trigger_outcome_label":"price_only_overheat_with_large_drawdown","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_after_2024-02-13_corporate_action_candidate","same_entry_group_id":"R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529_ENTRY","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_trigger_family_4B_overlay","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_HDHE_STAGE2_20240103","trigger_id":"TRIG_R1L13_C02_HDHE_STAGE2_20240103","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":9,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":5,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":9},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":219.93,"MAE_90D_pct":-5.24,"score_return_alignment_label":"structural_grid_capex_rerating_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_HYOSUNG_STAGE2_20240103","trigger_id":"TRIG_R1L13_C02_HYOSUNG_STAGE2_20240103","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":7,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7},"weighted_score_before":81.5,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":8},"weighted_score_after":87.5,"stage_label_after":"Stage3-Green","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":112.63,"MAE_90D_pct":-7.03,"score_return_alignment_label":"transformer_order_backlog_rerating_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_LSE_STAGE2_20240103","trigger_id":"TRIG_R1L13_C02_LSE_STAGE2_20240103","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":7,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":6},"weighted_score_before":74.5,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":6,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7},"weighted_score_after":78.5,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":231.97,"MAE_90D_pct":-14.15,"score_return_alignment_label":"grid_capex_rerating_after_initial_drawdown","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","trigger_id":"TRIG_R1L13_C02_ILJIN_POST_CA_STAGE2_20240214","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":7,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":6,"customer_quality_score":6,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":6},"weighted_score_before":73.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":7},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":156.79,"MAE_90D_pct":-12.48,"score_return_alignment_label":"post_ca_clean_entry_structural_success","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","trigger_id":"TRIG_R1L13_C02_HDHE_PRICE_ONLY_4B_20240724","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":10,"customer_quality_score":8,"policy_or_regulatory_score":5,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":8},"weighted_score_before":91.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":7,"customer_quality_score":8,"policy_or_regulatory_score":5,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":8},"weighted_score_after":84.0,"stage_label_after":"Stage4B-Overlay","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":2.46,"MAE_90D_pct":-34.88,"score_return_alignment_label":"price_only_local_4B_not_full_exit","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","trigger_id":"TRIG_R1L13_C02_HYOSUNG_PRICE_ONLY_4B_20240528","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":9},"weighted_score_before":90.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":7,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":8,"relative_strength_score":7,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":9},"weighted_score_after":83.0,"stage_label_after":"Stage4B-Overlay","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":4.34,"MAE_90D_pct":-48.61,"score_return_alignment_label":"local_peak_mae_shock_but_not_full_4c","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_LSE_PRICE_ONLY_4B_20240724","trigger_id":"TRIG_R1L13_C02_LSE_PRICE_ONLY_4B_20240724","symbol":"010120","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":6,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":9},"weighted_score_before":89.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":7,"customer_quality_score":6,"policy_or_regulatory_score":6,"valuation_repricing_score":9,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":9},"weighted_score_after":82.0,"stage_label_after":"Stage4B-Overlay","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":5.58,"MAE_90D_pct":-44.23,"score_return_alignment_label":"high_MAE_local_4B_but_not_hard_4C","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","trigger_id":"TRIG_R1L13_C02_ILJIN_PRICE_ONLY_4B_20240529","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":10},"weighted_score_before":86.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":6,"customer_quality_score":7,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":10},"weighted_score_after":78.0,"stage_label_after":"Stage4B-Overlay","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","positioning_overheat_score"],"component_delta_explanation":"R1/C02 shadow profile rewards order-quality plus margin bridge, but separates price-only local 4B from full 4B/4C.","MFE_90D_pct":5.77,"MAE_90D_pct":-21.68,"score_return_alignment_label":"price_only_overheat_with_large_drawdown","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R1","loop":"13","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","scheduled_round":"R1","scheduled_loop":"13","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":8,"reused_case_count":4,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_trigger_family_count":4,"positive_case_count":4,"counterexample_count":4,"current_profile_error_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_missed_structural","current_profile_too_late","price_only_local_4B_can_be_too_early_for_full_exit"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R1L13_C02_DAEHAN_CA_BLOCKED_20240103","symbol":"001440","company_name":"대한전선","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"2024-01-03 entry would have corporate_action_candidate_dates overlap within 180D because profile marks 2024-04-02 as corporate_action_candidate; therefore not used for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R1
completed_loop = 13
next_round = R2
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web files directly inspected during this run:

```text
atlas/manifest.json
atlas/schema.json
diagnostics/chatgpt_bundle.txt
data/e2r/calibration/md_registry.jsonl from stock_agent, coverage/duplicate context only
atlas/symbol_profiles/267/267260.json
atlas/symbol_profiles/298/298040.json
atlas/symbol_profiles/010/010120.json
atlas/symbol_profiles/103/103590.json
atlas/symbol_profiles/001/001440.json
atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv
atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv
atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv
atlas/ohlcv_tradable_by_symbol_year/010/010120/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010120/2025.csv
atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv
```

Key line-grounded observations from the fetched files:

```text
- manifest max_date = 2026-02-20; price_adjustment_status = raw_unadjusted_marcap.
- schema MFE_N_pct and MAE_N_pct formulas match the formulas used in this MD.
- diagnostics bundle includes selftest MFE/MAE for 267260 and 298040 from 2024-01-02/2024-01-03 anchor.
- 267260 2024-01-03 close = 85,800; 2024-07-24 high = 374,500; 2025-01-24 high = 450,000.
- 298040 2024-01-03 close = 167,900; 2024-05-28 high = 469,000; 2025-02-06 high = 549,000.
- 010120 2024-01-03 close = 73,500; 2024-07-24 high = 274,500; 2025-02-19 high = 303,500.
- 103590 profile marks 2024-02-13 as a corporate-action candidate, so the quantitative entry is next trading day 2024-02-14.
- 001440 profile marks 2024-04-02 as a corporate-action candidate, so a 2024-01-03 entry is blocked from weight calibration.
```
