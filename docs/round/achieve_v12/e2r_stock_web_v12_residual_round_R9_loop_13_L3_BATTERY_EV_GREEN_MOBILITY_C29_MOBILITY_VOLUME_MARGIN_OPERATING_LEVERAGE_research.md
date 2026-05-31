# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 13
completed_round = R9
completed_loop = 13
next_round = R10
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE
output_file = e2r_stock_web_v12_residual_round_R9_loop_13_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R9/L3_BATTERY_EV_GREEN_MOBILITY/C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE.

## 1. Current Calibrated Profile Assumption

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

This MD does not re-prove the global Stage2 bonus. It stress-tests whether C29 should treat OEM margin-bridge cases, supplier volume-readthrough cases, and transport reopening-volume cases as the same signal. The residual answer is no: in C29, volume behaves like a throttle only when the transmission—margin bridge, ASP/mix, or yield-cost spread—is actually engaged.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
loop = 13
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

R9 is treated as mobility/transport. Because this file focuses on auto OEMs, auto parts, and transport operating leverage, the round-sector pair is valid under the R9 mapping.

## 3. Previous Coverage / Duplicate Avoidance Check

The local previous output ended at:

```text
completed_round = R8
completed_loop = 13
next_round = R9
next_loop = 13
```

A repository search for `e2r_stock_web_v12_residual_round_R9_loop_13` and `C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` returned no matching v12 result file. Therefore this file uses:

```text
scheduled_round = R9
scheduled_loop = 13
duplicate_file_found = false
```

Diversity governor result:

```text
new_independent_case_count = 5
reused_case_count = 0
new_symbol_count = 5
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
new_trigger_family_count = 5
minimum_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
price_basis = tradable_raw
```

Profile validation summary:

| symbol | company | profile_path | profile last_date | corporate_action_window_status |
| --- | --- | --- | --- | --- |
| 005380 | 현대차 | atlas/symbol_profiles/005/005380.json | 2026-02-20 | clean 2024 trigger windows; historical CA dates only in 1998-1999 |
| 000270 | 기아 | atlas/symbol_profiles/000/000270.json | 2026-02-20 | clean 2024 trigger windows; historical CA dates only in 1999 |
| 012330 | 현대모비스 | atlas/symbol_profiles/012/012330.json | 2026-02-20 | clean 2023 trigger window; historical CA dates only before 2000 |
| 204320 | HL만도 | atlas/symbol_profiles/204/204320.json | 2026-02-20 | clean 2023 trigger window; last CA candidate in 2018 |
| 003490 | 대한항공 | atlas/symbol_profiles/003/003490.json | 2026-02-20 | clean 2023 trigger window; last CA candidate in 2021 |

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180_trading_day_window_available_by_manifest_max_date = true
high_low_close_volume_present = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

Rows using 4B are overlay rows and are excluded from aggregate representative entry selection.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE
compression_map:
  auto_oem_volume_mix_margin_bridge -> C29
  auto_parts_supplier_customer_win_without_margin_bridge -> C29 counterexample branch
  air_transport_reopening_volume_without_yield_margin -> C29 counterexample branch
  4B_val_revision_plateau_after_oem_rerating -> C29 4B overlay branch
```

Interpretation: C29 is not simply “more units sold.” It is the gearbox where unit volume, ASP/mix, cost curve, FX, incentives, and operating leverage have to mesh. OEMs can pass the signal because price/mix and margin bridge are inside the same income statement. Suppliers and transport operators need extra proof because volume can leak away through pass-through contracts, fuel, cargo yield normalization, or legal overhang.

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_HMC_2024 | 005380 | 현대차 | structural_success | 2024-01-26 | 46.02 | -0.43 | 59.9 | -0.43 | current_profile_correct |
| R9L13_C29_KIA_2024 | 000270 | 기아 | structural_success | 2024-01-26 | 39.51 | -1.8 | 43.01 | -1.8 | current_profile_correct |
| R9L13_C29_MOBIS_2023 | 012330 | 현대모비스 | failed_rerating | 2023-04-27 | 12.87 | -2.26 | 12.87 | -6.32 | current_profile_false_positive |
| R9L13_C29_HLMANDO_2023 | 204320 | HL만도 | false_positive_green | 2023-05-24 | 13.07 | -17.12 | 13.07 | -32.78 | current_profile_false_positive |
| R9L13_C29_KAL_2023 | 003490 | 대한항공 | failed_rerating | 2023-06-13 | 11.97 | -7.26 | 11.97 | -17.86 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
representative_trigger_count = 5
```

Positive cases are Hyundai Motor and Kia, where the price path rewarded a clear margin bridge and shareholder-return / value-up rerating. Counterexamples are Hyundai Mobis, HL Mando, and Korean Air, where a volume or customer-quality narrative existed but the margin bridge was incomplete.

## 9. Evidence Source Map

| case_id | evidence available at trigger date | evidence family | C29 interpretation |
| --- | --- | --- | --- |
| R9L13_C29_HMC_2024 | 2023 full-year / 4Q earnings, margin quality, value-up/shareholder-return expectation | OEM margin bridge | usable positive |
| R9L13_C29_KIA_2024 | 2023 full-year / 4Q earnings, high-margin mix, shareholder return | OEM margin bridge | usable positive |
| R9L13_C29_MOBIS_2023 | OEM volume readthrough and customer exposure | supplier beta without margin bridge | counterexample |
| R9L13_C29_HLMANDO_2023 | customer/order narrative and short relative strength | customer win without pass-through | counterexample |
| R9L13_C29_KAL_2023 | passenger recovery / reopening volume | transport volume without yield-cost bridge | counterexample |

Evidence source class: public earnings disclosures, company IR, and market reports available around each trigger date. Quantitative calibration relies only on stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | entry shard | profile |
| --- | --- | --- |
| 005380 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json |
| 000270 | atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv | atlas/symbol_profiles/000/000270.json |
| 012330 | atlas/ohlcv_tradable_by_symbol_year/012/012330/2023.csv | atlas/symbol_profiles/012/012330.json |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv | atlas/symbol_profiles/204/204320.json |
| 003490 | atlas/ohlcv_tradable_by_symbol_year/003/003490/2023.csv | atlas/symbol_profiles/003/003490.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | evidence_fields | role | dedupe |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_HMC_2024_STAGE2_ACTIONABLE | 005380 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 187300 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,early_revision_signa | structural_success | True |
| R9L13_C29_HMC_2024_STAGE4B_OVERLAY | 005380 | Stage4B | 2024-06-27 | 2024-06-27 | 298000 | valuation_blowoff,positioning_overheat,revision_slowdown | 4B_overlay_success | False |
| R9L13_C29_KIA_2024_STAGE2_ACTIONABLE | 000270 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 94400 | public_event_or_disclosure,relative_strength,capacity_or_volume_route,early_revision_signa | structural_success | True |
| R9L13_C29_KIA_2024_STAGE4B_OVERLAY | 000270 | Stage4B | 2024-06-19 | 2024-06-19 | 132300 | valuation_blowoff,positioning_overheat,revision_slowdown | 4B_overlay_success | False |
| R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH | 012330 | Stage2-Actionable | 2023-04-26 | 2023-04-27 | 221500 | customer_or_order_quality,capacity_or_volume_route,relative_strength,financial_visibility, | failed_rerating | True |
| R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE | 204320 | Stage2-Actionable | 2023-05-24 | 2023-05-24 | 48200 | customer_or_order_quality,relative_strength,capacity_or_volume_route,margin_or_backlog_slo | false_positive_green | True |
| R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER | 003490 | Stage2-Actionable | 2023-06-13 | 2023-06-13 | 23400 | capacity_or_volume_route,relative_strength,public_event_or_disclosure,margin_or_backlog_sl | failed_rerating | True |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | drawdown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_HMC_2024_STAGE2_ACTIONABLE | 2024-01-26 | 187300 | 39.35 | -0.43 | 46.02 | -0.43 | 59.9 | -0.43 | 2024-06-28/299500 | -27.71 |
| R9L13_C29_HMC_2024_STAGE4B_OVERLAY | 2024-06-27 | 298000 | 0.5 | -22.15 | 0.5 | -27.35 | 0.5 | -27.35 | 2024-06-28/299500 | -27.71 |
| R9L13_C29_KIA_2024_STAGE2_ACTIONABLE | 2024-01-26 | 94400 | 29.13 | -1.8 | 39.51 | -1.8 | 43.01 | -1.8 | 2024-06-19/135000 | -29.63 |
| R9L13_C29_KIA_2024_STAGE4B_OVERLAY | 2024-06-19 | 132300 | 2.04 | -16.86 | 2.04 | -28.19 | 2.04 | -28.19 | 2024-06-19/135000 | -29.63 |
| R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH | 2023-04-27 | 221500 | 4.06 | -2.26 | 12.87 | -2.26 | 12.87 | -6.32 | 2023-07-17/250000 | -17.0 |
| R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE | 2023-05-24 | 48200 | 13.07 | -3.42 | 13.07 | -17.12 | 13.07 | -32.78 | 2023-06-30/54500 | -40.55 |
| R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER | 2023-06-13 | 23400 | 11.97 | -1.28 | 11.97 | -7.26 | 11.97 | -17.86 | 2023-07-14/26200 | -26.64 |


Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
peak_price = max(high over observed window after entry_date)
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely decision | actual price result | residual verdict |
| --- | --- | --- | --- |
| R9L13_C29_HMC_2024 | Stage2/Yellow early, Green after revision confirmation | MFE180 +59.90%, MAE180 -0.43% | current_profile_correct |
| R9L13_C29_KIA_2024 | Stage2/Green acceptable after earnings and margin bridge | MFE180 +43.01%, MAE180 -1.80% | current_profile_correct |
| R9L13_C29_MOBIS_2023 | Could overpromote via OEM volume readthrough | MFE180 +12.87%, MAE180 -6.32% | current_profile_false_positive |
| R9L13_C29_HLMANDO_2023 | Could overpromote via customer/order narrative | MFE180 +13.07%, MAE180 -32.78% | current_profile_false_positive |
| R9L13_C29_KAL_2023 | Could overpromote via reopening volume | MFE180 +11.97%, MAE180 -17.86% | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C29 requires branch-specific haircuts.
yellow_threshold_75 = too permissive for supplier/transport volume-only cases.
green_threshold_87 = correct for OEM margin bridge, but supplier/transport cases need margin bridge gating.
stage3_green_revision_min_55 = kept.
price_only_blowoff_guard = strengthened for 4B overlay rows.
full_4b_non_price_requirement = kept but C29 should allow valuation + revision plateau + peak proximity as overlay, not thesis break.
hard_4c_routing = kept for HL Mando / Korean Air style thesis-evidence breaks.
```

## 14. Stage2 / Yellow / Green Comparison

For Hyundai and Kia, Stage2-Actionable was not just a premature price chase. It behaved like a loaded spring: earnings, mix, margin, and shareholder-return expectations were already compressing into one signal. Waiting for a late Green would have sacrificed a large part of the move.

For Hyundai Mobis, HL Mando, and Korean Air, the same Stage2 logic is dangerous. Volume was the visible flame, but the fuel line was not connected to margin. C29 therefore needs a split:

```text
OEM with margin bridge -> Stage2/Yellow can promote.
Supplier/transport with volume only -> cap at Stage2-Watch or Stage2-Actionable until margin bridge appears.
```

Green lateness ratio:

```text
HMC: not_applicable because Stage2 representative trigger is the calibrated entry and Green is treated as confirmation.
KIA: not_applicable for same reason.
Counterexamples: no confirmed Stage3-Green trigger should be used.
```

## 15. 4B Local vs Full-window Timing Audit

| case_id | 4B trigger | Stage2 price | 4B price | full peak | local proximity | full-window proximity | verdict |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- |
| R9L13_C29_HMC_2024 | 2024-06-27 | 187300 | 298000 | 299500 | 0.99 | 0.99 | good_full_window_4B_timing |
| R9L13_C29_KIA_2024 | 2024-06-19 | 94400 | 132300 | 135000 | 0.93 | 0.93 | good_full_window_4B_timing |

4B interpretation: the overlay did not say “thesis broken.” It said the vehicle had reached the redline. When peak proximity is above 0.9 and revision/valuation plateau evidence appears, C29 should mark risk overlay even if Stage3 thesis still exists.

## 16. 4C Protection Audit

| case_id | 4C label | rationale |
| --- | --- | --- |
| R9L13_C29_HLMANDO_2023 | hard_4c_success | MAE180 -32.78% after customer-win narrative failed to convert into margin |
| R9L13_C29_KAL_2023 | hard_4c_success | MAE180 -17.86% as passenger volume did not overcome cargo/fuel/overhang pressure |
| R9L13_C29_HMC_2024 | thesis_break_watch_only | drawdown after peak occurred, but thesis break was not proven in the representative window |
| R9L13_C29_KIA_2024 | thesis_break_watch_only | drawdown after peak occurred, but thesis break was not proven in the representative window |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_rule = L3_mobility_volume_signal_requires_margin_conversion
```

Rule candidate:

```text
In L3/R9 mobility cases, volume, deliveries, customer exposure, or reopening traffic can create Stage2-Actionable only. Stage3-Yellow/Green promotion requires at least one of:
- visible margin bridge,
- ASP/mix improvement,
- cost/FX/incentive tailwind,
- contract pass-through proof,
- yield/freight/fuel spread improvement,
- shareholder-return or capital-return rerating tied to durable earnings.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
candidate_rule = C29_margin_bridge_required_for_green
```

Specific rule:

```text
if canonical_archetype_id == C29 and margin_bridge_score < 15:
    cap positive label at Stage2-Actionable
    block Stage3-Green unless revision_score is very high and volume-to-margin conversion is explicit

if case is auto_parts_supplier and evidence is customer/order narrative without pass-through:
    apply supplier_pass_through_haircut

if case is transport/air/shipping and evidence is volume/reopening without yield-cost bridge:
    apply transport_yield_cost_guard
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible_triggers | selected_cases | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | late_green_count | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | global current proxy | 5 | all representative triggers | 24.69 | -5.77 | 28.16 | -11.84 | 3/5 | 0 | 0 | weak: volume-only cases overpromoted |
| P0b e2r_2_0_baseline_reference | rollback reference | 5 | all representative triggers | 24.69 | -5.77 | 28.16 | -11.84 | 3/5 | 0 | 1 | weaker: no C29 distinction |
| P1 sector_specific_candidate_profile | L3 sector shadow | 5 | OEM positives + guarded supplier/transport | 42.77 | -1.12 | 51.46 | -1.12 | 0/2 | 0 | 0 | better: margin bridge required |
| P2 canonical_archetype_candidate_profile | C29 shadow | 5 | Hyundai/Kia as Green; Mobis/Mando/KAL as watch/yellow max | 42.77 | -1.12 | 51.46 | -1.12 | 0/2 | 0 | 0 | best current fit |
| P3 counterexample_guard_profile | guard-only | 5 | all cases scored with supplier/transport haircut | 24.69 | -5.77 | 28.16 | -11.84 | 0 Green false positives | 0 | 0 | good guard but may underpromote future parts winners |


## 20. Score-Return Alignment Matrix

| case | before_score | before_label | after_score | after_label | MFE90 | MAE90 | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R9L13_C29_HMC_2024 | 86 | Stage3-Yellow | 89 | Stage3-Green | 46.02 | -0.43 | aligned_positive |
| R9L13_C29_KIA_2024 | 88 | Stage3-Green | 91 | Stage3-Green | 39.51 | -1.8 | aligned_positive |
| R9L13_C29_MOBIS_2023 | 77 | Stage3-Yellow | 68 | Stage2-Actionable | 12.87 | -2.26 | false_positive_reduced |
| R9L13_C29_HLMANDO_2023 | 78 | Stage3-Yellow | 62 | Stage2-Watch | 13.07 | -17.12 | false_positive_reduced |
| R9L13_C29_KAL_2023 | 76 | Stage3-Yellow | 59 | Stage2-Watch | 11.97 | -7.26 | false_positive_reduced |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE | 2 | 3 | 2 | 2 | 5 | 0 | 8 | 5 | 3 | True | True | Need more non-OEM transport and parts supplier positives in future R9 loops |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - supplier_volume_readthrough_false_positive
  - customer_win_without_margin_bridge_false_positive
  - transport_reopening_volume_without_yield_cost_bridge
  - C29_4B_overlay_late_if_non_price_requirement_too_strict
new_axis_proposed:
  - C29_margin_bridge_required_for_green
  - C29_supplier_pass_through_haircut
  - C29_transport_yield_cost_guard
  - C29_4B_val_revision_plateau_overlay
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical OHLC backtest using Songdaiki/stock-web tradable shards.
- 5 calibration-usable representative triggers.
- 2 C29 OEM positive cases.
- 3 C29 counterexamples across supplier and transport branches.
- 2 4B overlay rows with local/full-window proximity split.
```

Non-validation scope:

```text
- No current stock discovery.
- No live candidate scan.
- No trading recommendation.
- No production scoring change.
- No stock_agent source-code inspection.
- No brokerage or auto-trading integration.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_margin_bridge_required_for_green,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Volume/mix signal should not reach Green without margin_bridge_score >= 15 or equivalent ASP/fx/cost proof.","kept Hyundai/Kia positives and demoted Mobis/HL Mando/KAL false positives","R9L13_C29_HMC_2024_STAGE2_ACTIONABLE|R9L13_C29_KIA_2024_STAGE2_ACTIONABLE|R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH|R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE|R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_supplier_pass_through_haircut,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,-1,"Auto-parts supplier volume readthrough needs customer pass-through, unit economics, or explicit margin bridge.","reduced false positives in Mobis and HL Mando","R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH|R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE",2,2,2,medium,canonical_shadow_only,"supplier beta should not borrow OEM Green label"
shadow_weight,C29_transport_yield_cost_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,-1,"Passenger/traffic volume recovery must be accompanied by yield/cargo/fuel/fx margin evidence.","reduced 대한항공 reopening-volume false positive","R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER",1,1,1,low,canonical_shadow_only,"needs more transport cases in later loops"
shadow_weight,C29_4B_val_revision_plateau_overlay,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"For auto OEMs, full-window peak proximity >0.9 plus valuation/revision plateau can mark 4B overlay even before thesis break.","captured Hyundai/Kia peak-adjacent overlays before -27% to -30% drawdowns","R9L13_C29_HMC_2024_STAGE4B_OVERLAY|R9L13_C29_KIA_2024_STAGE4B_OVERLAY",2,2,0,medium,canonical_shadow_only,"risk overlay only; not a sell recommendation"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L13_C29_HMC_2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L13_C29_HMC_2024_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive if clean margin bridge; counterexample if volume-only or supplier/transport beta","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"OEM margin bridge and shareholder return pulled Stage2 forward without high MAE."}
{"row_type":"case","case_id":"R9L13_C29_KIA_2024","symbol":"000270","company_name":"기아","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L13_C29_KIA_2024_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive if clean margin bridge; counterexample if volume-only or supplier/transport beta","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Volume/mix/margin bridge validated; 4B overlay useful near June peak."}
{"row_type":"case","case_id":"R9L13_C29_MOBIS_2023","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive if clean margin bridge; counterexample if volume-only or supplier/transport beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Supplier readthrough needs margin bridge haircut."}
{"row_type":"case","case_id":"R9L13_C29_HLMANDO_2023","symbol":"204320","company_name":"HL만도","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive if clean margin bridge; counterexample if volume-only or supplier/transport beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer/order narrative without pass-through produced high MAE."}
{"row_type":"case","case_id":"R9L13_C29_KAL_2023","symbol":"003490","company_name":"대한항공","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive if clean margin bridge; counterexample if volume-only or supplier/transport beta","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Passenger volume narrative failed against cargo-yield/fuel/overhang risks."}
{"row_type":"trigger","trigger_id":"R9L13_C29_HMC_2024_STAGE2_ACTIONABLE","case_id":"R9L13_C29_HMC_2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_oem","primary_archetype":"volume_mix_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"2023년 연간/4Q 실적 발표 후 고마진 SUV·제네시스·환율·원가 안정의 margin bridge와 주주환원 기대가 동시에 작동한 auto OEM operating leverage trigger.","evidence_source":"public earnings disclosure / company IR / market earnings reports available at trigger date","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":187300,"MFE_30D_pct":39.35,"MFE_90D_pct":46.02,"MFE_180D_pct":59.9,"MFE_1Y_pct":59.9,"MFE_2Y_pct":null,"MAE_30D_pct":-0.43,"MAE_90D_pct":-0.43,"MAE_180D_pct":-0.43,"MAE_1Y_pct":-0.43,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_HMC_2024_2024-01-26_187300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L13_C29_HMC_2024_STAGE4B_OVERLAY","case_id":"R9L13_C29_HMC_2024","symbol":"005380","company_name":"현대차","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_oem","primary_archetype":"4B_val_revision_plateau","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-27","evidence_available_at_that_date":"Stage3 thesis는 유지되었지만, 단기 리레이팅이 full-window peak에 거의 도달했고 valuation/revision plateau risk가 관측된 4B overlay.","evidence_source":"observed price window plus valuation/revision plateau narrative; not a positive-stage promotion row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-27","entry_price":298000,"MFE_30D_pct":0.5,"MFE_90D_pct":0.5,"MFE_180D_pct":0.5,"MFE_1Y_pct":0.5,"MFE_2Y_pct":null,"MAE_30D_pct":-22.15,"MAE_90D_pct":-27.35,"MAE_180D_pct":-27.35,"MAE_1Y_pct":-27.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-27.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":0.99,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","revision_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_HMC_2024_2024-06-27_298000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R9L13_C29_KIA_2024_STAGE2_ACTIONABLE","case_id":"R9L13_C29_KIA_2024","symbol":"000270","company_name":"기아","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_oem","primary_archetype":"volume_mix_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","evidence_available_at_that_date":"2023년 4Q/연간 실적 이후 고수익 차종·미국 판매·원가/환율 조합이 visible margin bridge로 확인된 auto OEM operating leverage trigger.","evidence_source":"public earnings disclosure / company IR / market earnings reports available at trigger date","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-26","entry_price":94400,"MFE_30D_pct":29.13,"MFE_90D_pct":39.51,"MFE_180D_pct":43.01,"MFE_1Y_pct":43.01,"MFE_2Y_pct":null,"MAE_30D_pct":-1.8,"MAE_90D_pct":-1.8,"MAE_180D_pct":-1.8,"MAE_1Y_pct":-1.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-29.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_KIA_2024_2024-01-26_94400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L13_C29_KIA_2024_STAGE4B_OVERLAY","case_id":"R9L13_C29_KIA_2024","symbol":"000270","company_name":"기아","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_oem","primary_archetype":"4B_val_revision_plateau","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2024-06-19","evidence_available_at_that_date":"Stage3 thesis 자체는 훼손되지 않았지만, 단기 multiple/revision이 peak proximity 0.93까지 소진된 4B overlay.","evidence_source":"observed price window plus valuation/revision plateau narrative; not a positive-stage promotion row","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","revision_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv","profile_path":"atlas/symbol_profiles/000/000270.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-19","entry_price":132300,"MFE_30D_pct":2.04,"MFE_90D_pct":2.04,"MFE_180D_pct":2.04,"MFE_1Y_pct":2.04,"MFE_2Y_pct":null,"MAE_30D_pct":-16.86,"MAE_90D_pct":-28.19,"MAE_180D_pct":-28.19,"MAE_1Y_pct":-28.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-19","peak_price":135000,"drawdown_after_peak_pct":-29.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","revision_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_KIA_2024_2024-06-19_132300","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B overlay timing audit","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH","case_id":"R9L13_C29_MOBIS_2023","symbol":"012330","company_name":"현대모비스","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_parts_supplier","primary_archetype":"supplier_volume_readthrough_without_margin","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-04-26","evidence_available_at_that_date":"OEM volume readthrough는 있었지만 module/A/S/margin conversion이 명확하지 않아 C29 Green으로 올리면 residual false positive가 되는 supplier beta case.","evidence_source":"public earnings disclosure / supplier margin discussion available at trigger date","stage2_evidence_fields":["customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012330/2023.csv","profile_path":"atlas/symbol_profiles/012/012330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-27","entry_price":221500,"MFE_30D_pct":4.06,"MFE_90D_pct":12.87,"MFE_180D_pct":12.87,"MFE_1Y_pct":12.87,"MFE_2Y_pct":null,"MAE_30D_pct":-2.26,"MAE_90D_pct":-2.26,"MAE_180D_pct":-6.32,"MAE_1Y_pct":-6.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-17","peak_price":250000,"drawdown_after_peak_pct":-17.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_MOBIS_2023_2023-04-27_221500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE","case_id":"R9L13_C29_HLMANDO_2023","symbol":"204320","company_name":"HL만도","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"auto_parts_supplier","primary_archetype":"customer_win_without_margin_bridge","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-24","evidence_available_at_that_date":"EV/ADAS 고객·수주 narrative와 단기 상대강도는 있었지만 price-cost pass-through와 margin bridge가 약해 90D 이후 MAE가 확대된 false positive.","evidence_source":"public earnings disclosure / customer-win narrative / subsequent margin disappointment","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv","profile_path":"atlas/symbol_profiles/204/204320.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-05-24","entry_price":48200,"MFE_30D_pct":13.07,"MFE_90D_pct":13.07,"MFE_180D_pct":13.07,"MFE_1Y_pct":13.07,"MFE_2Y_pct":null,"MAE_30D_pct":-3.42,"MAE_90D_pct":-17.12,"MAE_180D_pct":-32.78,"MAE_1Y_pct":-32.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-30","peak_price":54500,"drawdown_after_peak_pct":-40.55,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_HLMANDO_2023_2023-05-24_48200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER","case_id":"R9L13_C29_KAL_2023","symbol":"003490","company_name":"대한항공","round":"R9","loop":"13","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_EXPORT_HYBRID_VOLUME_MARGIN_LEVERAGE","sector":"air_transport","primary_archetype":"volume_reopening_without_yield_margin","loop_objective":"coverage_gap_fill|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-13","evidence_available_at_that_date":"여객 회복 volume narrative만으로는 cargo yield normalization, fuel/fx cost, merger overhang을 이기지 못해 operating leverage가 지속되지 않은 transport counterexample.","evidence_source":"public traffic recovery / earnings discussion available at trigger date","stage2_evidence_fields":["capacity_or_volume_route","relative_strength","public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","legal_or_regulatory_block"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003490/2023.csv","profile_path":"atlas/symbol_profiles/003/003490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-06-13","entry_price":23400,"MFE_30D_pct":11.97,"MFE_90D_pct":11.97,"MFE_180D_pct":11.97,"MFE_1Y_pct":11.97,"MFE_2Y_pct":null,"MAE_30D_pct":-1.28,"MAE_90D_pct":-7.26,"MAE_180D_pct":-17.86,"MAE_1Y_pct":-17.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-14","peak_price":26200,"drawdown_after_peak_pct":-26.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L13_C29_KAL_2023_2023-06-13_23400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C29_shadow","case_id":"R9L13_C29_HMC_2024","trigger_id":"R9L13_C29_HMC_2024_STAGE2_ACTIONABLE","symbol":"005380","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":17,"relative_strength_score":14,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":21,"revision_score":18,"relative_strength_score":14,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+C29_margin_bridge_green_confirmation"],"component_delta_explanation":"C29 shadow separates OEM margin-bridge positives from supplier/transport volume-only false positives.","MFE_90D_pct":46.02,"MAE_90D_pct":-0.43,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C29_shadow","case_id":"R9L13_C29_KIA_2024","trigger_id":"R9L13_C29_KIA_2024_STAGE2_ACTIONABLE","symbol":"000270","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":17,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":22,"revision_score":18,"relative_strength_score":15,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":13,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","+C29_margin_bridge_green_confirmation"],"component_delta_explanation":"C29 shadow separates OEM margin-bridge positives from supplier/transport volume-only false positives.","MFE_90D_pct":39.51,"MAE_90D_pct":-1.8,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C29_shadow","case_id":"R9L13_C29_MOBIS_2023","trigger_id":"R9L13_C29_MOBIS_2023_VOLUME_READTHROUGH","symbol":"012330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":8,"relative_strength_score":13,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":6,"relative_strength_score":10,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["-supplier_readthrough_haircut","-margin_bridge_missing"],"component_delta_explanation":"C29 shadow separates OEM margin-bridge positives from supplier/transport volume-only false positives.","MFE_90D_pct":12.87,"MAE_90D_pct":-2.26,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C29_shadow","case_id":"R9L13_C29_HLMANDO_2023","trigger_id":"R9L13_C29_HLMANDO_2023_CUSTOMER_WIN_FALSE_POSITIVE","symbol":"204320","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":10,"relative_strength_score":16,"customer_quality_score":16,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":7,"relative_strength_score":11,"customer_quality_score":12,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","changed_components":["-customer_win_without_pass_through_haircut","-MAE_guard"],"component_delta_explanation":"C29 shadow separates OEM margin-bridge positives from supplier/transport volume-only false positives.","MFE_90D_pct":13.07,"MAE_90D_pct":-17.12,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C29_shadow","case_id":"R9L13_C29_KAL_2023","trigger_id":"R9L13_C29_KAL_2023_REOPENING_VOLUME_COUNTER","symbol":"003490","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":9,"relative_strength_score":12,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-5,"legal_or_contract_risk_score":-4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":5,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":-10,"legal_or_contract_risk_score":-7,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":59,"stage_label_after":"Stage2-Watch","changed_components":["-transport_volume_without_yield_guard","-legal_fuel_cost_overhang"],"component_delta_explanation":"C29 shadow separates OEM margin-bridge positives from supplier/transport volume-only false positives.","MFE_90D_pct":11.97,"MAE_90D_pct":-7.26,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"13","scheduled_round":"R9","scheduled_loop":13,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"same_archetype_new_symbol_count":5,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":3,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["supplier_volume_readthrough_false_positive","transport_volume_without_yield_margin","late_4B_overlay_after_peak_proximity"],"diversity_score_summary":"five new C29 symbols, five new trigger families, two OEM positives, three supplier/transport counterexamples","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 13
next_round = R10
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web price rows were read from these paths:

```text
atlas/manifest.json
atlas/symbol_profiles/005/005380.json
atlas/symbol_profiles/000/000270.json
atlas/symbol_profiles/012/012330.json
atlas/symbol_profiles/204/204320.json
atlas/symbol_profiles/003/003490.json
atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv
atlas/ohlcv_tradable_by_symbol_year/000/000270/2024.csv
atlas/ohlcv_tradable_by_symbol_year/012/012330/2023.csv
atlas/ohlcv_tradable_by_symbol_year/204/204320/2023.csv
atlas/ohlcv_tradable_by_symbol_year/003/003490/2023.csv
```

Important caveat:

```text
price_adjustment_status = raw_unadjusted_marcap
corporate_action_contaminated_windows = blocked
all representative windows in this MD = clean_180D_window
investment_recommendation_language = none
```

