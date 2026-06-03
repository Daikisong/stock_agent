# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 14
completed_round = R9
completed_loop = 14
next_round = R10
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE
output_file = e2r_stock_web_v12_residual_round_R9_loop_14_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
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

This MD does not re-prove the global Stage2 bonus. It stress-tests whether C29 should treat all transport volume recovery as equivalent. The residual finding is that transport volume is a throttle, not an engine: it only turns into rerating when freight rate, passenger yield, fuel cost, capital structure, and operating margin form a visible transmission.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R9
loop = 14
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE
loop_objective = coverage_gap_fill | counterexample_mining | residual_false_positive_mining | sector_specific_rule_discovery | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

R9 is treated as mobility/transport. Because this file focuses on shipping, dry-bulk, and LCC operating leverage, the R9/L3 pair is valid under the mobility/transport branch. It does not use construction/PF or real-estate C30 logic.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs already include R9 Loop 10~13 for OEMs, auto parts, tires, Korean Air, and logistics. The immediately preceding loop in this session ended at:

```text
completed_round = R8
completed_loop = 14
next_round = R9
next_loop = 14
```

Therefore this file uses:

```text
scheduled_round = R9
scheduled_loop = 14
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
positive_case_count = 2
counterexample_count = 3
current_profile_error_count = 3
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
| 011200 | HMM | atlas/symbol_profiles/011/011200.json | 2026-02-20 | 180D clean from 2020-11-16; 1Y/2Y blocked by 2021-11-16 CA candidate |
| 028670 | 팬오션 | atlas/symbol_profiles/028/028670.json | 2026-02-20 | clean 2021 trigger window; CA candidates are 2015 or earlier |
| 089590 | 제주항공 | atlas/symbol_profiles/089/089590.json | 2026-02-20 | clean 2023 trigger window; latest earlier CA candidate 2022-11-24 |
| 091810 | 티웨이항공 | atlas/symbol_profiles/091/091810.json | 2026-02-20 | clean after 2023-02-23 CA candidate; representative trigger starts 2023-03-29 |
| 272450 | 진에어 | atlas/symbol_profiles/272/272450.json | 2026-02-20 | clean 2023 trigger window; latest CA candidate 2020-11-16 |

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180_trading_day_window_available_by_manifest_max_date = true
high_low_close_volume_present = true
MFE_30D_90D_180D_and_MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

HMM is usable for 30D/90D/180D only. Its 1Y/2Y fields are marked `contaminated_or_unavailable` because the stock-web profile marks a 2021-11-16 corporate-action candidate.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE
compression_map:
  container_freight_rate_margin_bridge -> C29 positive branch
  drybulk_rate_operating_leverage -> C29 positive branch + 4B overlay branch
  airline_reopening_volume_without_yield_cost_bridge -> C29 counterexample branch
  route_capacity_growth_without_capital_fuel_bridge -> C29 counterexample branch
```

C29 should not be a generic “transport demand is back” rule. It should behave more like a gearbox: volume is the input shaft, but rerating appears only when pricing, cost, capital, and margin teeth catch. Shipping rates can make the gear engage quickly; airline passenger recovery can spin loudly while the wheels barely move.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN | 011200 | HMM | structural_success | 2020-11-16 | 153.19 | -14.54 | 262.41 | -14.54 | current_profile_correct |
| R9L14_C29_PAN_2021_DRYBULK_MARGIN | 028670 | 팬오션 | structural_success | 2021-02-22 | 55.94 | -7.34 | 55.94 | -7.34 | current_profile_correct |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE | 089590 | 제주항공 | failed_rerating | 2023-01-27 | 7.78 | -20.91 | 7.78 | -41.57 | current_profile_false_positive |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE | 091810 | 티웨이항공 | false_positive_green | 2023-03-29 | 6.0 | -30.4 | 6.0 | -41.42 | current_profile_false_positive |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE | 272450 | 진에어 | high_mae_success_or_false_positive | 2023-03-29 | 1.15 | -16.26 | 1.15 | -42.21 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 3
4B_case_count = 1
4C_case_count = 3
calibration_usable_case_count = 5
calibration_usable_trigger_count = 6
representative_trigger_count = 5
```

Positive cases are HMM and Pan Ocean, where freight-rate or dry-bulk rate recovery flowed through margin/yield-cost economics. Counterexamples are Jeju Air, T'way Air, and Jin Air, where reopening traffic or route expansion existed but the price path punished the absence of durable yield, fuel-cost, capital-structure, or dilution guardrails.

## 9. Evidence Source Map

| case_id | evidence available at trigger date | evidence family | C29 interpretation |
| --- | --- | --- | --- |
| R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN | Q3/FY2020 container freight-rate and operating-profit turnaround visible before/around 2020-11-16 | container freight-rate/yield-cost bridge | usable positive |
| R9L14_C29_PAN_2021_DRYBULK_MARGIN | dry-bulk rate recovery and fleet/charter leverage visible around 2021-02-22 | dry-bulk rate operating leverage | usable positive |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE | passenger reopening narrative visible around 2023-01-27 | airline reopening volume without yield-cost bridge | counterexample |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE | route expansion and travel recovery narrative visible around 2023-03-29 | route capacity growth without margin conversion | counterexample |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE | LCC passenger recovery visible around 2023-03-29 | reopening high-MAE guard | counterexample |

## 10. Price Data Source Map

| symbol | entry shard | profile |
| --- | --- | --- |
| 011200 | atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv and 2021.csv | atlas/symbol_profiles/011/011200.json |
| 028670 | atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv | atlas/symbol_profiles/028/028670.json |
| 089590 | atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv | atlas/symbol_profiles/089/089590.json |
| 091810 | atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv | atlas/symbol_profiles/091/091810.json |
| 272450 | atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv | atlas/symbol_profiles/272/272450.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE | 011200 | Stage2-Actionable | 2020-11-16 | 2020-11-16 | 14100 | positive_structural_margin_conversion | current_profile_correct | True |
| R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE | 028670 | Stage2-Actionable | 2021-02-22 | 2021-02-22 | 5720 | positive_structural_margin_conversion | current_profile_correct | True |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE | 089590 | Stage2-Actionable | 2023-01-27 | 2023-01-27 | 16070 | volume_without_margin_conversion_failed | current_profile_false_positive | True |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE | 091810 | Stage2-Actionable | 2023-03-29 | 2023-03-29 | 3585 | volume_without_margin_conversion_failed | current_profile_false_positive | True |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE | 272450 | Stage2-Actionable | 2023-03-29 | 2023-03-29 | 17340 | volume_without_margin_conversion_failed | current_profile_false_positive | True |
| R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY | 028670 | Stage4B | 2021-06-25 | 2021-06-25 | 8270 | 4B_overlay_success | current_profile_4B_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE | 2020-11-16 | 14100 | 6.03 | -14.54 | 153.19 | -14.54 | 262.41 | -14.54 | 2021-05-28 | 51100 | -28.47 |
| R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE | 2021-02-22 | 5720 | 29.2 | -7.34 | 55.94 | -7.34 | 55.94 | -7.34 | 2021-06-29 | 8920 | -38.23 |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE | 2023-01-27 | 16070 | 7.78 | -12.2 | 7.78 | -20.91 | 7.78 | -41.57 | 2023-02-17 | 17320 | -45.79 |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE | 2023-03-29 | 3585 | 6.0 | -13.25 | 6.0 | -30.4 | 6.0 | -41.42 | 2023-04-20 | 3800 | -44.74 |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE | 2023-03-29 | 17340 | 1.15 | -12.05 | 1.15 | -16.26 | 1.15 | -42.21 | 2023-03-30 | 17540 | -42.87 |
| R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY | 2021-06-25 | 8270 | 7.86 | -11.37 | 7.86 | -14.39 | 7.86 | -38.57 | 2021-06-29 | 8920 | -38.57 |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely label | actual path | verdict | residual lesson |
| --- | --- | --- | --- | --- |
| R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN | Stage3-Yellow / Actionable | +262.41% MFE180 with -14.54% MAE180 | current_profile_correct | Container rate + realized margin bridge can promote. |
| R9L14_C29_PAN_2021_DRYBULK_MARGIN | Stage2-Actionable / Stage3-Yellow | +55.94% MFE180 with -7.34% MAE180 | current_profile_correct | Dry-bulk rate conversion is valid, but later 4B needs crowding/rate saturation evidence. |
| R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE | Stage2-Actionable or Yellow if volume overweighted | +7.78% MFE180 / -41.57% MAE180 | current_profile_false_positive | Reopening volume without yield-cost bridge should not promote. |
| R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE | High Stage2 or false Yellow | +6.00% MFE180 / -41.42% MAE180 | current_profile_false_positive | Route growth plus weak balance-sheet/cost bridge is a trap. |
| R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE | High Stage2 or false Yellow | +1.15% MFE180 / -42.21% MAE180 | current_profile_false_positive | Passenger volume alone generated almost no upside and large drawdown. |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept, but C29 transport branch requires margin/yield-cost bridge.
yellow_threshold_75 = kept; airline reopening rows must be prevented from reaching it without yield/fuel/capital evidence.
green_threshold_87 = kept; no airline row deserves Green from volume alone.
price_only_blowoff_guard = strengthened; Pan Ocean 4B works because non-price rate/crowding evidence exists.
full_4b_non_price_requirement = strengthened.
hard_4c_routing = kept; Jeju/Tway/Jin Air should route to thesis-break watch once yield-cost bridge fails.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | possible late confirmation | green_lateness_ratio | interpretation |
| --- | --- | --- | --- | --- |
| HMM | 2020-11-16 / 14100 | 2021-03-26 / 34150 | 0.54 | Confirmation was meaningfully late but still before full peak. |
| 팬오션 | 2021-02-22 / 5720 | 2021-06-25 / 8270 | 0.80 | Late confirmation near rate-crowding zone; better treated as 4B watch than fresh Green. |
| 제주항공 | 2023-01-27 / 16070 | no supported Green | not_applicable | Reopening traffic did not become durable margin confirmation. |
| 티웨이항공 | 2023-03-29 / 3585 | no supported Green | not_applicable | Route volume did not survive cost/capital red-team. |
| 진에어 | 2023-03-29 / 17340 | no supported Green | not_applicable | Reopening volume generated high MAE, not rerating. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
| --- | --- | --- | --- | --- |
| R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY | 0.80 | 0.80 | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | good_full_window_4B_timing |

This loop strengthens the existing 4B rule rather than replacing it. A full 4B label requires freight-rate or margin-cycle crowding evidence. A local price peak alone is not enough.

## 16. 4C Protection Audit

| case_id | prior peak | later low used | label | practical protection note |
| --- | --- | --- | --- | --- |
| 제주항공 | 17320 | 9390 | hard_4c_success | Yield/cost bridge failure would have avoided most of the later airline drawdown. |
| 티웨이항공 | 3800 | 2100 | hard_4c_success | Route expansion without balance-sheet/fuel bridge should route to thesis-break watch. |
| 진에어 | 17540 | 10020 | hard_4c_success | Reopening beta was not enough to protect capital after peak. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = C29_TRANSPORT_VOLUME_YIELD_COST_BRIDGE_GATE
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
condition:
  transport / shipping / airline volume signal can promote above Stage2 only if at least two of the following are present:
    - realized or high-confidence margin bridge
    - rate/yield-cost spread improvement
    - fuel/cost headwind contained
    - capital raise/dilution risk contained
    - non-price evidence from earnings or public rate data
positive examples:
  - HMM 2020 container freight-rate margin bridge
  - Pan Ocean 2021 dry-bulk rate operating leverage
counterexamples:
  - Jeju Air 2023 reopening volume
  - T'way Air 2023 route expansion
  - Jin Air 2023 reopening high-MAE path
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C29_VOLUME_IS_NOT_MARGIN_CONVERSION
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
shadow_delta = +1 guard / +1 positive bonus split
positive_bonus_axis = shipping_rate_margin_conversion_bonus
negative_guard_axis = reopening_volume_without_yield_cost_bridge_guard
```

For C29, “volume” is treated like a river. The score should ask whether there is a turbine attached. Freight rates and margin bridge make the turbine spin; passenger traffic alone can simply flood the income statement with fuel, lease, and debt costs.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 5 | 44.81 | -17.89 | 66.66 | -29.42 | 0.60 | 0 | 1 | mixed; airline reopening false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback reference | 5 | 44.81 | -17.89 | 66.66 | -29.42 | 0.80 | 1 | 2 | worse; does not separate rate bridge from volume beta |
| P1_sector_specific_candidate_profile | sector shadow | 5 | 104.57 positive subset / 4.98 counter subset | -10.94 positive subset / -22.52 counter subset | 159.18 positive subset / 4.98 counter subset | -10.94 positive subset / -41.73 counter subset | 0.20 | 0 | 1 | improved transport precision |
| P2_canonical_archetype_candidate_profile | C29 shadow | 5 | 104.57 positive subset / 4.98 counter subset | -10.94 positive subset / -22.52 counter subset | 159.18 positive subset / 4.98 counter subset | -10.94 positive subset / -41.73 counter subset | 0.20 | 0 | 1 | best explanatory compression |
| P3_counterexample_guard_profile | C29 guard | 3 counterexamples | 4.98 | -22.52 | 4.98 | -41.73 | 0.00 after guard | 0 | 0 | prevents reopening-volume false Green |

## 20. Score-Return Alignment Matrix

| case_id | raw score problem | proposed score behavior | MFE/MAE alignment |
| --- | --- | --- | --- |
| HMM | High volume signal needs actual margin bridge | promote to actionable/Yellow | aligned with huge MFE and acceptable early MAE |
| 팬오션 | Dry-bulk rate signal works, but late confirmation becomes 4B risk | promote early, overlay late | aligned with MFE then drawdown |
| 제주항공 | Passenger volume could be over-scored | cap at Stage2-Watch | aligned with low MFE and high MAE |
| 티웨이항공 | Route expansion could be over-scored | cap at Stage2-Watch / RedTeam | aligned with high drawdown |
| 진에어 | Reopening beta could be over-scored | cap at Stage2-Watch | aligned with almost no upside |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L3_BATTERY_EV_GREEN_MOBILITY | C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE | 2 | 3 | 1 | 3 | 5 | 0 | 6 | 5 | 3 | true | true | Remaining C29 gap is rail/shipbuilder/port-logistics cross-readthrough, not generic auto OEM volume. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: airline_reopening_volume_false_positive, transport_volume_without_yield_cost_bridge, 4B_late_after_shipping_rate_crowding
new_axis_proposed: C29_transport_yield_cost_bridge_gate, C29_airline_reopening_volume_guard, C29_shipping_4B_non_price_overheat
existing_axis_strengthened: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- Stock-Web manifest and schema fields.
- Symbol profile presence and corporate-action candidate windows.
- Entry dates and entry prices from tradable shards.
- 30D / 90D / 180D MFE and MAE from stock-web OHLC rows.
- Same-entry representative dedupe.
- Current-profile stress test at research-proxy level.
```

Not validated:

```text
- No live candidate scan.
- No current 2026 watchlist.
- No brokerage API.
- No stock_agent src/e2r code inspection.
- No production scoring patch.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C29_transport_yield_cost_bridge_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Promote transport volume only when rate/yield-cost bridge and margin conversion are both visible","Raised positive precision: shipping positives keep upside while airline reopening false positives are downgraded","R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE|R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE|R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE|R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE|R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_airline_reopening_volume_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Passenger recovery without yield/fuel/capital bridge produced high MAE and poor MFE","Downgrades reopening-volume false positives before Green","R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE|R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE|R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE",3,3,3,medium,sector_shadow_only,"not production; post-calibrated residual"
shadow_weight,C29_shipping_4B_non_price_overheat,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,0,1,+1,"Dry-bulk 4B worked only when non-price freight-rate crowding/expectation saturation was visible","Separates full-window 4B from local price-only pullback","R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY",1,0,0,low,4B_overlay_shadow_only,"not production; overlay calibration"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN","symbol":"011200","company_name":"HMM","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Q3/FY2020 container freight-rate and profitability turn; public earnings + freight-rate spread visibility"}
{"row_type":"case","case_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN","symbol":"028670","company_name":"팬오션","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"dry-bulk rate recovery + fleet/charter operating leverage; public shipping-rate and earnings visibility"}
{"row_type":"case","case_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"passenger reopening volume visible, but yield/fuel/capital structure bridge not yet secured"}
{"row_type":"case","case_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"route expansion/reopening demand narrative, but dilution/fuel/yield risk dominated"}
{"row_type":"case","case_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE","symbol":"272450","company_name":"진에어","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","case_type":"high_mae_success_or_false_positive","positive_or_counterexample":"counterexample","best_trigger":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"LCC passenger recovery visible, but no durable operating-margin bridge at trigger"}
{"row_type":"trigger","trigger_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE","case_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN","symbol":"011200","company_name":"HMM","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-16","evidence_available_at_that_date":"Q3/FY2020 container freight-rate and profitability turn; public earnings + freight-rate spread visibility","evidence_source":"public earnings disclosure / company IR / public industry rate or traffic data available by trigger date","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv","profile_path":"atlas/symbol_profiles/011/011200.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-11-16","entry_price":14100,"MFE_30D_pct":6.03,"MFE_90D_pct":153.19,"MFE_180D_pct":262.41,"MFE_1Y_pct":"contaminated_or_unavailable","MFE_2Y_pct":"contaminated_or_unavailable","MAE_30D_pct":-14.54,"MAE_90D_pct":-14.54,"MAE_180D_pct":-14.54,"MAE_1Y_pct":"contaminated_or_unavailable","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-28","peak_price":51100,"drawdown_after_peak_pct":-28.47,"green_lateness_ratio":0.54,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_margin_conversion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; 1Y/2Y blocked by 2021-11-16 corporate_action_candidate","same_entry_group_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE","case_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN","symbol":"028670","company_name":"팬오션","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-22","evidence_available_at_that_date":"dry-bulk rate recovery + fleet/charter operating leverage; public shipping-rate and earnings visibility","evidence_source":"public earnings disclosure / company IR / public industry rate or traffic data available by trigger date","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv","profile_path":"atlas/symbol_profiles/028/028670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-22","entry_price":5720,"MFE_30D_pct":29.2,"MFE_90D_pct":55.94,"MFE_180D_pct":55.94,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-7.34,"MAE_90D_pct":-7.34,"MAE_180D_pct":-7.34,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-29","peak_price":8920,"drawdown_after_peak_pct":-38.23,"green_lateness_ratio":0.8,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_structural_margin_conversion","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE","case_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE","symbol":"089590","company_name":"제주항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-27","evidence_available_at_that_date":"passenger reopening volume visible, but yield/fuel/capital structure bridge not yet secured","evidence_source":"public earnings disclosure / company IR / public industry rate or traffic data available by trigger date","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility_missing_or_weak"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv","profile_path":"atlas/symbol_profiles/089/089590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-27","entry_price":16070,"MFE_30D_pct":7.78,"MFE_90D_pct":7.78,"MFE_180D_pct":7.78,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-12.2,"MAE_90D_pct":-20.91,"MAE_180D_pct":-41.57,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-17","peak_price":17320,"drawdown_after_peak_pct":-45.79,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"volume_without_margin_conversion_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE","case_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE","symbol":"091810","company_name":"티웨이항공","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-29","evidence_available_at_that_date":"route expansion/reopening demand narrative, but dilution/fuel/yield risk dominated","evidence_source":"public earnings disclosure / company IR / public industry rate or traffic data available by trigger date","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility_missing_or_weak"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv","profile_path":"atlas/symbol_profiles/091/091810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-29","entry_price":3585,"MFE_30D_pct":6.0,"MFE_90D_pct":6.0,"MFE_180D_pct":6.0,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-13.25,"MAE_90D_pct":-30.4,"MAE_180D_pct":-41.42,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-20","peak_price":3800,"drawdown_after_peak_pct":-44.74,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"volume_without_margin_conversion_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE","case_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE","symbol":"272450","company_name":"진에어","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-29","evidence_available_at_that_date":"LCC passenger recovery visible, but no durable operating-margin bridge at trigger","evidence_source":"public earnings disclosure / company IR / public industry rate or traffic data available by trigger date","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility_missing_or_weak"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv","profile_path":"atlas/symbol_profiles/272/272450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-29","entry_price":17340,"MFE_30D_pct":1.15,"MFE_90D_pct":1.15,"MFE_180D_pct":1.15,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-12.05,"MAE_90D_pct":-16.26,"MAE_180D_pct":-42.21,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-30","peak_price":17540,"drawdown_after_peak_pct":-42.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_row","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"volume_without_margin_conversion_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_ENTRY","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R9L14_C29_PAN_2021_DRYBULK_4B_OVERLAY","case_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN","symbol":"028670","company_name":"팬오션","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"TRANSPORT_SHIPPING_AIRLINE_VOLUME_YIELD_MARGIN_LEVERAGE","sector":"mobility_transport_shipping_airline","primary_archetype":"mobility_volume_margin_operating_leverage","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2021-06-25","evidence_available_at_that_date":"dry-bulk rate momentum already crowded; price near full-window peak while rate/margin expectation was consensus","evidence_source":"public shipping-rate data + market reports + stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv","profile_path":"atlas/symbol_profiles/028/028670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-06-25","entry_price":8270,"MFE_30D_pct":7.86,"MFE_90D_pct":7.86,"MFE_180D_pct":7.86,"MFE_1Y_pct":"not_computed","MFE_2Y_pct":"not_computed","MAE_30D_pct":-11.37,"MAE_90D_pct":-14.39,"MAE_180D_pct":-38.57,"MAE_1Y_pct":"not_computed","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-29","peak_price":8920,"drawdown_after_peak_pct":-38.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.8,"four_b_full_window_peak_proximity":0.8,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN_4B","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, different 4B timing family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN","trigger_id":"R9L14_C29_HMM_2020_CONTAINER_RATE_MARGIN_STAGE2_ACTIONABLE","symbol":"011200","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":9,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":21,"revision_score":11,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"shipping-rate or freight-rate signal is allowed to contribute only when it appears with realized margin/yield-cost bridge and clean OHLC confirmation.","MFE_90D_pct":153.19,"MAE_90D_pct":-14.54,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN","trigger_id":"R9L14_C29_PAN_2021_DRYBULK_MARGIN_STAGE2_ACTIONABLE","symbol":"028670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":9,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":21,"revision_score":11,"relative_strength_score":12,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":2,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"shipping-rate or freight-rate signal is allowed to contribute only when it appears with realized margin/yield-cost bridge and clean OHLC confirmation.","MFE_90D_pct":55.94,"MAE_90D_pct":-7.34,"score_return_alignment_label":"score_return_aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE","trigger_id":"R9L14_C29_JEJUAIR_2023_REOPENING_FALSEBRIDGE_STAGE2_ACTIONABLE","symbol":"089590","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":4,"accounting_trust_risk_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow_or_high_Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":7,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"airline reopening traffic volume is downgraded when yield/fuel/capital-structure bridge is unsupported; volume alone is not C29 conversion.","MFE_90D_pct":7.78,"MAE_90D_pct":-20.91,"score_return_alignment_label":"score_return_false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE","trigger_id":"R9L14_C29_TWAY_2023_ROUTE_VOLUME_FALSEBRIDGE_STAGE2_ACTIONABLE","symbol":"091810","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":4,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage3-Yellow_or_high_Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":7,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"airline reopening traffic volume is downgraded when yield/fuel/capital-structure bridge is unsupported; volume alone is not C29 conversion.","MFE_90D_pct":6.0,"MAE_90D_pct":-30.4,"score_return_alignment_label":"score_return_false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE","trigger_id":"R9L14_C29_JINAIR_2023_REOPENING_HIGHMAE_STAGE2_ACTIONABLE","symbol":"272450","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":11,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":8,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":4,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage3-Yellow_or_high_Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":13,"legal_or_contract_risk_score":3,"dilution_cb_risk_score":7,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"airline reopening traffic volume is downgraded when yield/fuel/capital-structure bridge is unsupported; volume alone is not C29 conversion.","MFE_90D_pct":1.15,"MAE_90D_pct":-16.26,"score_return_alignment_label":"score_return_false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R9","loop":"14","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["airline_reopening_volume_false_positive","transport_volume_without_yield_cost_bridge","4B_late_after_shipping_rate_crowding"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 14
next_round = R10
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
manifest_path = atlas/manifest.json
schema_path = atlas/schema.json
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20

primary_stock_web_paths_checked:
  - atlas/manifest.json
  - atlas/schema.json
  - atlas/symbol_profiles/011/011200.json
  - atlas/symbol_profiles/028/028670.json
  - atlas/symbol_profiles/089/089590.json
  - atlas/symbol_profiles/091/091810.json
  - atlas/symbol_profiles/272/272450.json
  - atlas/ohlcv_tradable_by_symbol_year/011/011200/2020.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011200/2021.csv
  - atlas/ohlcv_tradable_by_symbol_year/028/028670/2021.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089590/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/091/091810/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/272/272450/2023.csv
```

