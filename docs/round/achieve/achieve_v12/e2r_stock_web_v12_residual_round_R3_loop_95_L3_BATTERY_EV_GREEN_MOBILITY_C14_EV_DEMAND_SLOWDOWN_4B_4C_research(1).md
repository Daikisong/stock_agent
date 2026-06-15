# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
selected_round: R3
selected_loop: 95
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: mixed_C14_ev_demand_slowdown_4b_4c_set
research_file_name: e2r_stock_web_v12_residual_round_R3_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
previous_index_state: C14 rows 11 / symbols 11 / positive 0 / counterexample 11 / 4B 3 / 4C 4 / need_to_30 19
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_objective: coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
stock_web_price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
new_independent_case_count: 5
reused_case_count: 0
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_count: 3
4B_case_count: 3
4C_case_count: 2
current_profile_error_count: 3
source_proxy_only_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
```

## 1. Current Calibrated Profile Assumption

Active profile assumed: `e2r_2_2_rolling_calibrated`.

C14 is a protection-first canonical. The current problem is not whether EV demand slowdown matters; it obviously does. The calibration problem is **when the slowdown becomes a hard thesis break** versus when it remains a 4B watch item because volume, AMPC/JV, ESS, customer mix, or product-mix offsets still preserve recovery optionality.

## 2. Round / Large Sector / Canonical Archetype Scope

```yaml
round: R3
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
research_scope: historical trigger-level calibration only
```

Included: historical C14 EV slowdown triggers with stock-web tradable OHLC path. Excluded: live watchlist, current recommendation, production scoring patch, and price-only trigger construction.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index ledger state used only as a duplicate/coverage ledger. The current index shows C14 as a Priority 0 under-covered canonical with 11 rows and top covered symbols including `001570`, `002710`, `020150`, `051910`, `066970`, and `078600`.

This loop intentionally avoids those top-covered C14 symbols and adds five independent symbols:

```text
361610 SK아이이테크놀로지
006400 삼성SDI
003670 포스코퓨처엠
247540 에코프로비엠
373220 LG에너지솔루션
```

Duplicate hard-key check applied: `canonical_archetype_id + symbol + trigger_type + entry_date`.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest state used for all price rows:

```yaml
source_repo: https://github.com/Songdaiki/stock-web
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
mfe_mae_formula: high/low from entry_date through N trading days versus entry_date close
entry_price_rule: entry_date c column
```

## 5. Historical Eligibility Gate

```yaml
trigger_date_is_historical: true
entry_date_in_stock_web_tradable_shard: true
entry_price_is_entry_date_close: true
forward_window_trading_days_gte_180: true
MFE_30D_pct_present: true
MFE_90D_pct_present: true
MFE_180D_pct_present: true
MAE_30D_pct_present: true
MAE_90D_pct_present: true
MAE_180D_pct_present: true
corporate_action_window_status: no_overlap_180D_window
calibration_usable: true
```

## 6. Canonical Archetype Compression Map

```yaml
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
compression_question: Is EV slowdown a hard thesis break, a 4B watch, or merely a headline that should not block surviving offset routes?
positive_protection_family:
  - C14_SEPARATOR_UTILIZATION_COST_TRAP_4C_PROTECTION
  - C14_CELL_MAKER_EU_DEMAND_INVENTORY_4C_PROTECTION
counterexample_family:
  - C14_CATHODE_PROFITABILITY_DEFENSE_FALSE_STAGE2_COUNTEREXAMPLE
  - C14_MATERIAL_PRICE_AND_EV_DEMAND_4B_NOT_HARD_4C_COUNTEREXAMPLE
  - C14_AMPC_JV_OFFSET_4B_WATCH_NOT_HARD_4C_COUNTEREXAMPLE
```

## 7. Case Selection Summary

| # | symbol | company | fine archetype | trigger | case label | 180D MFE | 180D MAE | verdict |
|---:|---|---|---|---|---|---:|---:|---|
| 1 | 361610 | SK아이이테크놀로지 | C14_SEPARATOR_UTILIZATION_COST_TRAP_4C_PROTECTION | Stage4C 2023-11-03 | positive | 18.12 | -50.94 | current_profile_correct |
| 2 | 006400 | 삼성SDI | C14_CELL_MAKER_EU_DEMAND_INVENTORY_4C_PROTECTION | Stage4C 2024-10-30 | positive | 4.28 | -51.77 | current_profile_correct |
| 3 | 003670 | 포스코퓨처엠 | C14_CATHODE_PROFITABILITY_DEFENSE_FALSE_STAGE2_COUNTEREXAMPLE | Stage2-Actionable 2024-04-24 | counterexample | 5.7 | -51.41 | current_profile_false_positive |
| 4 | 247540 | 에코프로비엠 | C14_MATERIAL_PRICE_AND_EV_DEMAND_4B_NOT_HARD_4C_COUNTEREXAMPLE | Stage4B 2024-02-07 | counterexample | 22.59 | -38.93 | current_profile_4C_too_early_if_hard_routed |
| 5 | 373220 | LG에너지솔루션 | C14_AMPC_JV_OFFSET_4B_WATCH_NOT_HARD_4C_COUNTEREXAMPLE | Stage4B 2024-04-25 | counterexample | 19.35 | -16.4 | current_profile_4C_too_early_if_hard_routed |


## 8. Positive vs Counterexample Balance

| bucket | count | symbols | average MFE180 | average MAE180 | interpretation |
|---|---:|---|---:|---:|---|
| positive / protection success | 2 | 361610, 006400 | 11.2 | -51.36 | hard 4C correctly protects when utilization/customer/OP evidence breaks |
| counterexample | 3 | 003670, 247540, 373220 | 15.88 | -35.58 | slowdown headline or ASP/inventory pain needs 4B watch / Stage2 block, not automatic hard 4C |


## 9. Evidence Source Map

| symbol | source | as-of evidence compression | stage split |
|---|---|---|---|
| 361610 | https://en.yna.co.kr/view/AEN20231103002151320 | 2023-11-03 Yonhap article reported SKIET Q3 net loss widened due to slowing EV demand, decreased demand from EV companies, and Poland separator plant construction cost burden. | 2=separator_capacity_expansion;battery_separator_leader;operating_profit_turnaround_yoy_visible / 4B=decreased_EV_company_demand;fixed_cost_burden_from_Poland_separator_plants;180D_MAE_minus_50_94 / 4C=demand_shortfall_hits_bottom_line;customer_demand_decrease_confirmed;separator_fixed_cost_trap |
| 006400 | https://www.samsungsdi.com/sdi-now/sdi-news/4082.html | 2024-10-30 company release reported battery revenue down 31% YoY, operating profit down 85% YoY, prismatic revenue decline from slowing European EV demand, lower cylindrical utilization, customer inventory adjustments, and delayed demand recovery. | 2=premium_prismatic_mid_long_growth;GM_JV_contract;ESS_growth_offset / 4B=European_EV_demand_slowdown;customer_inventory_adjustment;lower_utilization;delayed_demand_recovery / 4C=battery_OP_down_85pct_yoy;lower_utilization_due_to_decreasing_EV_sales;peak_same_day_then_180D_MAE_minus_51_77 |
| 003670 | https://www.asiae.co.kr/en/article/2024042408020731975 ; https://www.poscofuturem.com/en/pr/view.do?num=899 | 2024-04-24 Asiae article reported securities view that profitability was relatively defended despite continued EV demand slowdown, with cathode binding contracts and expected Q1 volume increase, but ASP pressure and inventory revaluation effects remained central. Later official 2024 results confirmed revenue down 22.3% and operating profit down 98.0%. | 2=profitability_defense_claim;binding_contract_ratio;Q1_volume_recovery;target_price_maintained / 4B=continued_EV_demand_slowdown;ASP_drop;lithium_price_lag;90D_MAE_minus_30_30;180D_MAE_minus_51_41 / 4C=not_at_trigger;later_2024_profit_collapse_confirms_risk_but_not_asof_hard_break |
| 247540 | https://www.ecopro.co.kr/sub0401/view/id/1432 ; https://www.thelec.kr/news/articleView.html?idxno=25844 | 2024-02-07 EcoPro release and conference-call coverage reported 2023 revenue growth but EcoPro BM operating profit down 60%, Q4 operating loss, metal-price fall, front-end demand weakness, and EV cathode demand slowdown; at the same time EV cathode volume/revenue growth and non-EV power-tool/ESS offsets remained. | 2=EV_cathode_annual_sales_growth;volume_growth;product_mix_upgrade;non_EV_power_tool_ESS_offset / 4B=Q4_operating_loss;metal_price_drop;front_end_demand_weakness;ASP_and_inventory_loss;later_180D_MAE_minus_38_93 / 4C=not_hard_at_trigger;annual_sales_and_volume_growth_survived;subsequent_30D_90D_MFE_above_20pct |
| 373220 | https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/ | 2024-04-25 company release reported Q1 revenue down 23.4% QoQ and operating profit down 75.2% YoY, fixed-cost burden and utilization adjustment caused by EV demand slowdown, and IRA tax credit decline; it also cited GM JV production, Arizona/ESS expansion, LFP cathode agreement, and investment-efficiency response. | 2=GM_JV_first_shipment;North_America_capacity_expansion;LFP_cathode_supply_agreement;ESS_and_software_optionalities / 4B=utilization_adjustment;fixed_cost_burden;ASP_metal_price_lag;IRA_tax_credit_decline;demand_slowdown / 4C=not_hard_at_trigger;AMPC_JV_ESS_offsets_and_subsequent_MFE_19_35_with_MAE_only_minus_16_40 |


## 10. Price Data Source Map

| symbol | price shard | profile path | entry row status |
|---|---|---|---|
| 361610 | `atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv + 2024.csv + 2025.csv` | `atlas/symbol_profiles/361/361610.json` | entry_date=2023-11-06 / c=74,500 / 180D usable |
| 006400 | `atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv + 2025.csv` | `atlas/symbol_profiles/006/006400.json` | entry_date=2024-10-31 / c=327,000 / 180D usable |
| 003670 | `atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv + 2025.csv` | `atlas/symbol_profiles/003/003670.json` | entry_date=2024-04-25 / c=280,500 / 180D usable |
| 247540 | `atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv + 2025.csv` | `atlas/symbol_profiles/247/247540.json` | entry_date=2024-02-08 / c=243,500 / 180D usable |
| 373220 | `atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv + 2025.csv` | `atlas/symbol_profiles/373/373220.json` | entry_date=2024-04-26 / c=372,000 / 180D usable |


## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | stage2 evidence | stage4b evidence | stage4c evidence |
|---|---|---|---|---|---|---|
| 361610 | Stage4C | 2023-11-03 | 2023-11-06 | separator_capacity_expansion; battery_separator_leader; operating_profit_turnaround_yoy_visible | decreased_EV_company_demand; fixed_cost_burden_from_Poland_separator_plants; 180D_MAE_minus_50_94 | demand_shortfall_hits_bottom_line; customer_demand_decrease_confirmed; separator_fixed_cost_trap |
| 006400 | Stage4C | 2024-10-30 | 2024-10-31 | premium_prismatic_mid_long_growth; GM_JV_contract; ESS_growth_offset | European_EV_demand_slowdown; customer_inventory_adjustment; lower_utilization; delayed_demand_recovery | battery_OP_down_85pct_yoy; lower_utilization_due_to_decreasing_EV_sales; peak_same_day_then_180D_MAE_minus_51_77 |
| 003670 | Stage2-Actionable | 2024-04-24 | 2024-04-25 | profitability_defense_claim; binding_contract_ratio; Q1_volume_recovery; target_price_maintained | continued_EV_demand_slowdown; ASP_drop; lithium_price_lag; 90D_MAE_minus_30_30; 180D_MAE_minus_51_41 | not_at_trigger; later_2024_profit_collapse_confirms_risk_but_not_asof_hard_break |
| 247540 | Stage4B | 2024-02-07 | 2024-02-08 | EV_cathode_annual_sales_growth; volume_growth; product_mix_upgrade; non_EV_power_tool_ESS_offset | Q4_operating_loss; metal_price_drop; front_end_demand_weakness; ASP_and_inventory_loss; later_180D_MAE_minus_38_93 | not_hard_at_trigger; annual_sales_and_volume_growth_survived; subsequent_30D_90D_MFE_above_20pct |
| 373220 | Stage4B | 2024-04-25 | 2024-04-26 | GM_JV_first_shipment; North_America_capacity_expansion; LFP_cathode_supply_agreement; ESS_and_software_optionalities | utilization_adjustment; fixed_cost_burden; ASP_metal_price_lag; IRA_tax_credit_decline; demand_slowdown | not_hard_at_trigger; AMPC_JV_ESS_offsets_and_subsequent_MFE_19_35_with_MAE_only_minus_16_40 |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | post-peak DD |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 361610 | 2023-11-06 | 74,500 | 18.12 | -14.23 | 18.12 | -14.23 | 18.12 | -50.94 | 2023-12-08 | 88,000 | -58.47 |
| 006400 | 2024-10-31 | 327,000 | 4.28 | -27.98 | 4.28 | -42.87 | 4.28 | -51.77 | 2024-10-31 | 341,000 | -53.75 |
| 003670 | 2024-04-25 | 280,500 | 5.7 | -11.05 | 5.7 | -30.3 | 5.7 | -51.41 | 2024-04-25 | 296,500 | -54.03 |
| 247540 | 2024-02-08 | 243,500 | 21.77 | -6.57 | 22.59 | -25.46 | 22.59 | -38.93 | 2024-03-27 | 298,500 | -50.18 |
| 373220 | 2024-04-26 | 372,000 | 6.72 | -12.37 | 12.63 | -16.4 | 19.35 | -16.4 | 2024-10-08 | 444,000 | -23.31 |


Aggregate price-path summary:

```yaml
avg_MFE_90D_pct: 12.66
avg_MAE_90D_pct: -25.85
avg_MFE_180D_pct: 14.01
avg_MAE_180D_pct: -41.89
median_MFE_180D_pct: 18.12
median_MAE_180D_pct: -50.94
positive_protection_MFE180_avg: 11.2
positive_protection_MAE180_avg: -51.36
counterexample_MFE180_avg: 15.88
counterexample_MAE180_avg: -35.58
```

## 13. Current Calibrated Profile Stress Test

```yaml
current_profile_correct_cases:
  - 361610_SK아이이테크놀로지_hard_4C_protection
  - 006400_삼성SDI_hard_4C_protection
current_profile_error_cases:
  - 003670_포스코퓨처엠_false_Stage2_if_profitability_defense_overcredited
  - 247540_에코프로비엠_hard_4C_too_early_if_ASP_inventory_loss_treated_as_thesis_break
  - 373220_LG에너지솔루션_hard_4C_too_early_if_AMPC_JV_ESS_offsets_ignored
```

C14 needs a split gate. The phrase “EV demand slowdown” is a dashboard warning light, not the engine seizure itself. The seizure is confirmed when slowdown reaches utilization, customer orders, margin collapse, operating loss, or balance-sheet stress. If offsets remain alive, the proper state is 4B watch, not automatic 4C.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Yellow or Stage3-Green row is intentionally included in this C14 loop. The relevant comparison is Stage2/Stage2-Actionable versus 4B/4C downrouting.

```yaml
green_lateness_ratio: null
green_lateness_reason: no_confirmed_Stage3_Green_trigger_in_this_C14_loop
stage2_false_positive_case: 003670_POSCO_Future_M
stage4b_not_4c_cases:
  - 247540_EcoPro_BM
  - 373220_LG_Energy_Solution
hard_4c_success_cases:
  - 361610_SK_IET
  - 006400_Samsung_SDI
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | desired routing | four_b_local_peak_proximity | four_b_full_window_peak_proximity | timing verdict |
|---|---|---:|---:|---|
| 003670 | Stage2 blocked / 4B watch | 0.0 | 0.0 | 4B watch should override profitability-defense Stage2; hard 4C not available as-of trigger |
| 247540 | 4B watch, not hard 4C | 0.0 | 0.0 | hard 4C too early because rebound MFE >20% arrived before later drawdown |
| 373220 | 4B watch, not hard 4C | 0.0 | 0.0 | hard 4C too early due to AMPC/JV/ESS offsets and contained 180D MAE |

4B is not a price-only sell signal here. It is a non-price overlay triggered by ASP/inventory lag, utilization pressure, fixed-cost burden, or customer demand weakness.

## 16. 4C Protection Audit

| symbol | hard 4C label | 90D MAE | 180D MAE | protection verdict |
|---|---|---:|---:|---|
| 361610 | separator demand/fixed-cost break | -14.23 | -50.94 | hard_4c_success |
| 006400 | cell maker demand/utilization/OP break | -42.87 | -51.77 | hard_4c_success |

Hard 4C is justified when demand weakness already appears in customer demand, utilization, operating profit collapse, or fixed-cost absorption. It is not justified by the mere phrase “EV slowdown.”

## 17. Sector-Specific Rule Candidate

```yaml
rule_scope: sector_specific
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_UTILIZATION_ORDER_CUT_GATE
rule_intent: Split macro EV slowdown headlines from hard L3 battery/EV thesis breaks.
positive_condition:
  hard_4C_allowed_if_any_two:
    - confirmed utilization reduction or lower production rate
    - customer inventory adjustment / call-off / demand decrease
    - core battery/material operating profit collapse or operating loss
    - fixed-cost absorption trap from underutilized capacity
    - balance-sheet or funding stress caused by slowdown
```

## 18. Canonical-Archetype Rule Candidate

```yaml
rule_scope: canonical_archetype_specific
canonical_archetype_rule_candidate: C14_DEMAND_SLOWDOWN_4C_REQUIRES_UTILIZATION_AND_ORDER_CUT_CONFIRMATION
rule_downroute_condition:
  route_to_4B_not_4C_if:
    - AMPC/JV/ESS/customer offset remains active
    - annual volume or customer thesis survives
    - weakness is mostly lithium/ASP/inventory lag without call-off confirmation
    - price path shows material rebound MFE before thesis collapse
rule_stage2_block_condition:
  block_positive_stage_if:
    - evidence is only profitability-defense language under continued EV slowdown
    - margin bridge is not confirmed
    - ASP and inventory lag are active
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|---|---|
| P0 | current_proxy | broad hard-4C thesis-break routing | none | 5 | representative | 12.66 | -25.85 | 14.01 | -41.89 | 0.20 | 0 | 0 | n/a | mixed | mixed | correct protection but too broad for offset cases |
| P0b | baseline_reference | lower archetype-specific split | none | 5 | representative | 12.66 | -25.85 | 14.01 | -41.89 | 0.40 | 0 | 0 | n/a | mixed | mixed | more false positives from profitability-defense narratives |
| P1 | sector_specific_candidate | L3 EV slowdown requires utilization/order evidence | utilization/customer/order gate | 5 | representative | 12.66 | -25.85 | 14.01 | -41.89 | 0.10 | 0 | 0 | n/a | 0.0 on watch cases | 0.0 on watch cases | improved |
| P2 | canonical_archetype_candidate | C14 hard 4C requires utilization/order/OP break; offsets downroute | thesis_break_score, utilization_score, margin_bridge_score | 5 | representative | 12.66 | -25.85 | 14.01 | -41.89 | 0.00 | 0 | 0 | n/a | 0.0 on watch cases | 0.0 on watch cases | best fit |
| P3 | counterexample_guard | no hard 4C until multi-quarter confirmation | over-strict protection delay | 5 | representative | 12.66 | -25.85 | 14.01 | -41.89 | 0.00 | 2 | 0 | n/a | n/a | n/a | misses SKIET/SDI protection |


## 20. Score-Return Alignment Matrix

| axis | current residual | proposed adjustment |
|---|---|---|
| earnings_visibility | false positive when relative profit-defense language is overcredited | require margin bridge after ASP/inventory lag |
| information_confidence | EV slowdown headline over-compresses multiple mechanisms | require utilization/customer/order evidence for hard 4C |
| market_mispricing | rebound MFE exists even in negative material cases | do not erase all mispricing credit when volume/customer route survives |
| valuation_rerating | should not rescue C14 positives without evidence | keep low unless slowdown is demonstrably priced with offset route |
| bottleneck_pricing | mostly irrelevant in slowdown regime | do not use capacity scarcity language to override demand break |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---:|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | mixed_C14_ev_demand_slowdown_4b_4c_set | 2 | 3 | 3 | 2 | 5 | 0 | 5 | 5 | 3 | L3_C14_EV_SLOWDOWN_UTILIZATION_ORDER_CUT_GATE | C14_DEMAND_SLOWDOWN_4C_REQUIRES_UTILIZATION_AND_ORDER_CUT_CONFIRMATION | 14 |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes: hard_4c_thesis_break_routes_to_4c | full_4b_requires_non_price_evidence
residual_error_types_found: false_positive_stage2_profitability_defense | hard_4c_too_early_when_offsets_survive | correct_4c_protection_when_utilization_order_OP_break_confirmed
new_axis_proposed: C14_HARD_4C_REQUIRES_UTILIZATION_ORDER_CUT_OR_OPERATING_LOSS_CONFIRMATION | C14_MATERIAL_PRICE_LAG_FALSE_4C_BUFFER | C14_AMPC_JV_ESS_OFFSET_DOWNROUTE_CAP
existing_axis_strengthened: hard_4c_thesis_break_routes_to_4c | full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: L3_C14_EV_SLOWDOWN_UTILIZATION_ORDER_CUT_GATE
canonical_archetype_rule_candidate: C14_DEMAND_SLOWDOWN_4C_REQUIRES_UTILIZATION_AND_ORDER_CUT_CONFIRMATION
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable shard entry date
- entry price as entry-date close
- 30D/90D/180D MFE and MAE
- canonical/round/large-sector consistency
- historical trigger dates before stock_web_manifest_max_date
```

Not validated:

```text
- intraday publication time for same-day entry eligibility
- adjusted-price restatement after future corporate-action logic
- production scoring impact
- current live attractiveness of any symbol
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,information_confidence,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+0.04,"Hard 4C requires utilization/customer/order/OP evidence rather than EV slowdown headline alone.","reduced hard-4C-too-early errors on 247540 and 373220","T-C14-R3-L95-04-247540-2024-02-08|T-C14-R3-L95-05-373220-2024-04-26",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,earnings_visibility,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+0.03,"Stage2/4B split should depend on margin bridge or OP collapse under ASP and inventory lag.","blocked 003670 profitability-defense false Stage2","T-C14-R3-L95-03-003670-2024-04-25",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,valuation_rerating,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,-0.02,"Relative profitability-defense narratives under slowdown should not receive valuation rerating credit without confirmed margin conversion.","lower false-positive rerating credit","T-C14-R3-L95-03-003670-2024-04-25",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation.jsonl

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case_rows.jsonl

```jsonl
{"row_type":"case","case_id":"C14_R3_L95_361610_20231106","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SEPARATOR_UTILIZATION_COST_TRAP_4C_PROTECTION","case_type":"4c_protection_success","positive_or_counterexample":"positive","best_trigger":"T-C14-R3-L95-01-361610-2023-11-06","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"correct_protection_high_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C14 hard 4C is valid when EV demand decrease is already visible in customer demand and fixed-cost absorption rather than only in macro headlines."}
{"row_type":"case","case_id":"C14_R3_L95_006400_20241031","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CELL_MAKER_EU_DEMAND_INVENTORY_4C_PROTECTION","case_type":"4c_protection_success","positive_or_counterexample":"positive","best_trigger":"T-C14-R3-L95-02-006400-2024-10-31","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"correct_protection_high_MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C14 hard 4C is valid when demand slowdown is translated into utilization, core battery operating profit collapse, and customer inventory adjustment."}
{"row_type":"case","case_id":"C14_R3_L95_003670_20240425","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CATHODE_PROFITABILITY_DEFENSE_FALSE_STAGE2_COUNTEREXAMPLE","case_type":"false_positive","positive_or_counterexample":"counterexample","best_trigger":"T-C14-R3-L95-03-003670-2024-04-25","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C14 should cap profitability-defense narratives when ASP/lithium lag and EV slowdown are still active; Stage2-Actionable needs confirmed margin bridge, not relative-defense language."}
{"row_type":"case","case_id":"C14_R3_L95_247540_20240208","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_MATERIAL_PRICE_AND_EV_DEMAND_4B_NOT_HARD_4C_COUNTEREXAMPLE","case_type":"hard_4c_too_early","positive_or_counterexample":"counterexample","best_trigger":"T-C14-R3-L95-04-247540-2024-02-08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4B_watch_correct_hard_4C_too_early","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed","price_source":"Songdaiki/stock-web","notes":"C14 hard 4C should not trigger from inventory/ASP pain alone when volume/customer thesis still produces material rebound MFE before later drawdown."}
{"row_type":"case","case_id":"C14_R3_L95_373220_20240426","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_AMPC_JV_OFFSET_4B_WATCH_NOT_HARD_4C_COUNTEREXAMPLE","case_type":"hard_4c_too_early","positive_or_counterexample":"counterexample","best_trigger":"T-C14-R3-L95-05-373220-2024-04-26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"offset_aware_4B_watch_correct","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed","price_source":"Songdaiki/stock-web","notes":"C14 needs offset-aware downrouting: AMPC/JV/ESS customer evidence can keep EV slowdown in 4B watch rather than hard 4C."}
```

### 25.3 trigger_rows_representative.jsonl

```jsonl
{"row_type":"trigger","trigger_id":"T-C14-R3-L95-01-361610-2023-11-06","case_id":"C14_R3_L95_361610_20231106","symbol":"361610","company_name":"SK아이이테크놀로지","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_SEPARATOR_UTILIZATION_COST_TRAP_4C_PROTECTION","sector":"battery_separator","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2023-11-03","evidence_available_at_that_date":"2023-11-03 Yonhap article reported SKIET Q3 net loss widened due to slowing EV demand, decreased demand from EV companies, and Poland separator plant construction cost burden.","evidence_source":"https://en.yna.co.kr/view/AEN20231103002151320","stage2_evidence_fields":["separator_capacity_expansion","battery_separator_leader","operating_profit_turnaround_yoy_visible"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["decreased_EV_company_demand","fixed_cost_burden_from_Poland_separator_plants","180D_MAE_minus_50_94"],"stage4c_evidence_fields":["demand_shortfall_hits_bottom_line","customer_demand_decrease_confirmed","separator_fixed_cost_trap"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/361/361610/2023.csv + 2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/361/361610.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-11-06","entry_price":74500.0,"MFE_30D_pct":18.12,"MFE_90D_pct":18.12,"MFE_180D_pct":18.12,"MFE_1Y_pct":18.12,"MFE_2Y_pct":null,"MAE_30D_pct":-14.23,"MAE_90D_pct":-14.23,"MAE_180D_pct":-50.94,"MAE_1Y_pct":-67.32,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-08","peak_price":88000.0,"drawdown_after_peak_pct":-58.47,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_C14_loop","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_hard_4c_trigger","four_b_evidence_type":"revision_slowdown; margin_or_backlog_slowdown; customer_demand_or_utilization; non_price_required","four_c_protection_label":"hard_4C_protection_success","trigger_outcome_label":"separator_EV_demand_slowdown_hard_4C_protection_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":586,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"361610_2023-11-06_74500.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","residual_contribution":"C14 hard 4C is valid when EV demand decrease is already visible in customer demand and fixed-cost absorption rather than only in macro headlines.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C14-R3-L95-02-006400-2024-10-31","case_id":"C14_R3_L95_006400_20241031","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CELL_MAKER_EU_DEMAND_INVENTORY_4C_PROTECTION","sector":"battery_cell","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-10-30","evidence_available_at_that_date":"2024-10-30 company release reported battery revenue down 31% YoY, operating profit down 85% YoY, prismatic revenue decline from slowing European EV demand, lower cylindrical utilization, customer inventory adjustments, and delayed demand recovery.","evidence_source":"https://www.samsungsdi.com/sdi-now/sdi-news/4082.html","stage2_evidence_fields":["premium_prismatic_mid_long_growth","GM_JV_contract","ESS_growth_offset"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["European_EV_demand_slowdown","customer_inventory_adjustment","lower_utilization","delayed_demand_recovery"],"stage4c_evidence_fields":["battery_OP_down_85pct_yoy","lower_utilization_due_to_decreasing_EV_sales","peak_same_day_then_180D_MAE_minus_51_77"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-31","entry_price":327000.0,"MFE_30D_pct":4.28,"MFE_90D_pct":4.28,"MFE_180D_pct":4.28,"MFE_1Y_pct":8.41,"MFE_2Y_pct":null,"MAE_30D_pct":-27.98,"MAE_90D_pct":-42.87,"MAE_180D_pct":-51.77,"MAE_1Y_pct":-51.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-31","peak_price":341000.0,"drawdown_after_peak_pct":-53.75,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_C14_loop","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_hard_4c_trigger","four_b_evidence_type":"revision_slowdown; margin_or_backlog_slowdown; customer_demand_or_utilization; non_price_required","four_c_protection_label":"hard_4C_protection_success","trigger_outcome_label":"cell_maker_EV_demand_inventory_hard_4C_protection_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":283,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"006400_2024-10-31_327000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"positive","residual_contribution":"C14 hard 4C is valid when demand slowdown is translated into utilization, core battery operating profit collapse, and customer inventory adjustment.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C14-R3-L95-03-003670-2024-04-25","case_id":"C14_R3_L95_003670_20240425","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_CATHODE_PROFITABILITY_DEFENSE_FALSE_STAGE2_COUNTEREXAMPLE","sector":"battery_materials_cathode_anode","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","evidence_available_at_that_date":"2024-04-24 Asiae article reported securities view that profitability was relatively defended despite continued EV demand slowdown, with cathode binding contracts and expected Q1 volume increase, but ASP pressure and inventory revaluation effects remained central. Later official 2024 results confirmed revenue down 22.3% and operating profit down 98.0%.","evidence_source":"https://www.asiae.co.kr/en/article/2024042408020731975 ; https://www.poscofuturem.com/en/pr/view.do?num=899","stage2_evidence_fields":["profitability_defense_claim","binding_contract_ratio","Q1_volume_recovery","target_price_maintained"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["continued_EV_demand_slowdown","ASP_drop","lithium_price_lag","90D_MAE_minus_30_30","180D_MAE_minus_51_41"],"stage4c_evidence_fields":["not_at_trigger","later_2024_profit_collapse_confirms_risk_but_not_asof_hard_break"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":280500.0,"MFE_30D_pct":5.7,"MFE_90D_pct":5.7,"MFE_180D_pct":5.7,"MFE_1Y_pct":5.7,"MFE_2Y_pct":null,"MAE_30D_pct":-11.05,"MAE_90D_pct":-30.3,"MAE_180D_pct":-51.41,"MAE_1Y_pct":-61.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-25","peak_price":296500.0,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_C14_loop","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"4B_watch_should_override_profitability_defense_Stage2; full hard 4C not yet available at trigger","four_b_evidence_type":"revision_slowdown; margin_or_backlog_slowdown; customer_demand_or_utilization; non_price_required","four_c_protection_label":"not_4C_at_trigger_asof_only_later_validated","trigger_outcome_label":"profitability_defense_false_Stage2_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":408,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"003670_2024-04-25_280500.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"C14 should cap profitability-defense narratives when ASP/lithium lag and EV slowdown are still active; Stage2-Actionable needs confirmed margin bridge, not relative-defense language.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C14-R3-L95-04-247540-2024-02-08","case_id":"C14_R3_L95_247540_20240208","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_MATERIAL_PRICE_AND_EV_DEMAND_4B_NOT_HARD_4C_COUNTEREXAMPLE","sector":"battery_materials_cathode","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-02-07","evidence_available_at_that_date":"2024-02-07 EcoPro release and conference-call coverage reported 2023 revenue growth but EcoPro BM operating profit down 60%, Q4 operating loss, metal-price fall, front-end demand weakness, and EV cathode demand slowdown; at the same time EV cathode volume/revenue growth and non-EV power-tool/ESS offsets remained.","evidence_source":"https://www.ecopro.co.kr/sub0401/view/id/1432 ; https://www.thelec.kr/news/articleView.html?idxno=25844","stage2_evidence_fields":["EV_cathode_annual_sales_growth","volume_growth","product_mix_upgrade","non_EV_power_tool_ESS_offset"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["Q4_operating_loss","metal_price_drop","front_end_demand_weakness","ASP_and_inventory_loss","later_180D_MAE_minus_38_93"],"stage4c_evidence_fields":["not_hard_at_trigger","annual_sales_and_volume_growth_survived","subsequent_30D_90D_MFE_above_20pct"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-08","entry_price":243500.0,"MFE_30D_pct":21.77,"MFE_90D_pct":22.59,"MFE_180D_pct":22.59,"MFE_1Y_pct":22.59,"MFE_2Y_pct":null,"MAE_30D_pct":-6.57,"MAE_90D_pct":-25.46,"MAE_180D_pct":-38.93,"MAE_1Y_pct":-56.88,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":298500.0,"drawdown_after_peak_pct":-50.18,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_C14_loop","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"4B_watch_valid_but_hard_4C_too_early_before_volume_or_customer_call_off_break","four_b_evidence_type":"revision_slowdown; margin_or_backlog_slowdown; customer_demand_or_utilization; non_price_required","four_c_protection_label":"hard_4C_too_early_counterexample","trigger_outcome_label":"cathode_material_price_lag_4B_not_hard_4C_counterexample","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed","calibration_usable":true,"forward_window_trading_days":459,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"247540_2024-02-08_243500.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"C14 hard 4C should not trigger from inventory/ASP pain alone when volume/customer thesis still produces material rebound MFE before later drawdown.","aggregate_metric_inclusion":true}
{"row_type":"trigger","trigger_id":"T-C14-R3-L95-05-373220-2024-04-26","case_id":"C14_R3_L95_373220_20240426","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"C14_AMPC_JV_OFFSET_4B_WATCH_NOT_HARD_4C_COUNTEREXAMPLE","sector":"battery_cell","primary_archetype":"C14_EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":"coverage_gap_fill | counterexample_mining | 4B_4C_guardrail | canonical_archetype_compression | sector_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-04-25","evidence_available_at_that_date":"2024-04-25 company release reported Q1 revenue down 23.4% QoQ and operating profit down 75.2% YoY, fixed-cost burden and utilization adjustment caused by EV demand slowdown, and IRA tax credit decline; it also cited GM JV production, Arizona/ESS expansion, LFP cathode agreement, and investment-efficiency response.","evidence_source":"https://inside.lgensol.com/en/2024/04/lg-energy-solution-makes-progress-amid-market-uncertainties-aims-to-strengthen-fundamental-competitiveness-this-year/","stage2_evidence_fields":["GM_JV_first_shipment","North_America_capacity_expansion","LFP_cathode_supply_agreement","ESS_and_software_optionalities"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["utilization_adjustment","fixed_cost_burden","ASP_metal_price_lag","IRA_tax_credit_decline","demand_slowdown"],"stage4c_evidence_fields":["not_hard_at_trigger","AMPC_JV_ESS_offsets_and_subsequent_MFE_19_35_with_MAE_only_minus_16_40"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv + 2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":372000.0,"MFE_30D_pct":6.72,"MFE_90D_pct":12.63,"MFE_180D_pct":19.35,"MFE_1Y_pct":19.35,"MFE_2Y_pct":null,"MAE_30D_pct":-12.37,"MAE_90D_pct":-16.4,"MAE_180D_pct":-16.4,"MAE_1Y_pct":-17.74,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000.0,"drawdown_after_peak_pct":-23.31,"green_lateness_ratio":null,"green_lateness_reason":"no_confirmed_Stage3_Green_trigger_in_this_C14_loop","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"4B_watch_valid; hard_4C_too_early_due_to_AMPC_JV_ESS_offsets_and_contained_180D_MAE","four_b_evidence_type":"revision_slowdown; margin_or_backlog_slowdown; customer_demand_or_utilization; non_price_required","four_c_protection_label":"hard_4C_too_early_counterexample","trigger_outcome_label":"cell_maker_EV_slowdown_4B_watch_with_offset_counterexample","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed","calibration_usable":true,"forward_window_trading_days":407,"calibration_block_reasons":[],"corporate_action_window_status":"no_overlap_180D_window","same_entry_group_id":"373220_2024-04-26_372000.0","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"positive_or_counterexample":"counterexample","residual_contribution":"C14 needs offset-aware downrouting: AMPC/JV/ESS customer evidence can keep EV slowdown in 4B watch rather than hard 4C.","aggregate_metric_inclusion":true}
```

### 25.4 score_simulation_rows.jsonl

```jsonl
{"row_type":"score_simulation","profile_id":"C14_canonical_archetype_candidate_profile_P2","case_id":"C14_R3_L95_361610_20231106","trigger_id":"T-C14-R3-L95-01-361610-2023-11-06","symbol":"361610","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":4,"asp_or_spread_score":1,"thesis_break_score":4},"weighted_score_before":48,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":5,"asp_or_spread_score":1,"thesis_break_score":5},"weighted_score_after":30,"stage_label_after":"Stage4C","changed_components":["utilization_score","thesis_break_score","execution_risk_score"],"component_delta_explanation":"Customer demand decrease and separator fixed-cost absorption upgrade 4B watch to hard 4C protection.","MFE_90D_pct":18.12,"MAE_90D_pct":-14.23,"MFE_180D_pct":18.12,"MAE_180D_pct":-50.94,"score_return_alignment_label":"correct_protection_high_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C14_canonical_archetype_candidate_profile_P2","case_id":"C14_R3_L95_006400_20241031","trigger_id":"T-C14-R3-L95-02-006400-2024-10-31","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":4,"asp_or_spread_score":2,"thesis_break_score":4},"weighted_score_before":52,"stage_label_before":"Stage4B","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":5,"asp_or_spread_score":2,"thesis_break_score":5},"weighted_score_after":32,"stage_label_after":"Stage4C","changed_components":["utilization_score","thesis_break_score","customer_quality_score"],"component_delta_explanation":"Battery OP collapse, lower utilization, and customer inventory adjustment confirm a hard 4C route despite some ESS/JV offsets.","MFE_90D_pct":4.28,"MAE_90D_pct":-42.87,"MFE_180D_pct":4.28,"MAE_180D_pct":-51.77,"score_return_alignment_label":"correct_protection_high_MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"C14_canonical_archetype_candidate_profile_P2","case_id":"C14_R3_L95_003670_20240425","trigger_id":"T-C14-R3-L95-03-003670-2024-04-25","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":2,"asp_or_spread_score":4,"thesis_break_score":2},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":3,"asp_or_spread_score":5,"thesis_break_score":3},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["margin_bridge_score","valuation_repricing_score","asp_or_spread_score","execution_risk_score"],"component_delta_explanation":"Relative profitability-defense evidence is downgraded because ASP/lithium lag and EV slowdown were still active and no durable margin bridge was confirmed.","MFE_90D_pct":5.7,"MAE_90D_pct":-30.3,"MFE_180D_pct":5.7,"MAE_180D_pct":-51.41,"score_return_alignment_label":"false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"C14_canonical_archetype_candidate_profile_P2","case_id":"C14_R3_L95_247540_20240208","trigger_id":"T-C14-R3-L95-04-247540-2024-02-08","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":3,"asp_or_spread_score":5,"thesis_break_score":5},"weighted_score_before":40,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":3,"asp_or_spread_score":5,"thesis_break_score":3},"weighted_score_after":60,"stage_label_after":"Stage4B-Watch","changed_components":["thesis_break_score","relative_strength_score","valuation_repricing_score"],"component_delta_explanation":"Inventory/ASP loss and Q4 operating loss create 4B watch, but surviving annual volume/revenue and 20%+ rebound MFE make hard 4C too early.","MFE_90D_pct":22.59,"MAE_90D_pct":-25.46,"MFE_180D_pct":22.59,"MAE_180D_pct":-38.93,"score_return_alignment_label":"4B_watch_correct_hard_4C_too_early","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed"}
{"row_type":"score_simulation","profile_id":"C14_canonical_archetype_candidate_profile_P2","case_id":"C14_R3_L95_373220_20240426","trigger_id":"T-C14-R3-L95-05-373220-2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":4,"asp_or_spread_score":3,"thesis_break_score":5},"weighted_score_before":45,"stage_label_before":"Stage4C","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":2,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":3,"valuation_repricing_score":1,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"utilization_score":4,"asp_or_spread_score":3,"thesis_break_score":3},"weighted_score_after":62,"stage_label_after":"Stage4B-Watch","changed_components":["thesis_break_score","contract_score","customer_quality_score","policy_or_regulatory_score"],"component_delta_explanation":"AMPC/JV/ESS and supply-agreement offsets downroute the slowdown signal from hard 4C to 4B watch.","MFE_90D_pct":12.63,"MAE_90D_pct":-16.4,"MFE_180D_pct":19.35,"MAE_180D_pct":-16.4,"score_return_alignment_label":"offset_aware_4B_watch_correct","current_profile_verdict":"current_profile_4C_too_early_if_hard_routed"}
```

### 25.5 shadow_weight.csv

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,information_confidence,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+0.04,"Hard 4C requires utilization/customer/order/OP evidence rather than EV slowdown headline alone.","reduced hard-4C-too-early errors on 247540 and 373220","T-C14-R3-L95-04-247540-2024-02-08|T-C14-R3-L95-05-373220-2024-04-26",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,earnings_visibility,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+0.03,"Stage2/4B split should depend on margin bridge or OP collapse under ASP and inventory lag.","blocked 003670 profitability-defense false Stage2","T-C14-R3-L95-03-003670-2024-04-25",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,valuation_rerating,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,-0.02,"Relative profitability-defense narratives under slowdown should not receive valuation rerating credit without confirmed margin conversion.","lower false-positive rerating credit","T-C14-R3-L95-03-003670-2024-04-25",5,5,3,low,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 aggregate.jsonl

```jsonl
{"row_type":"aggregate","aggregate_id":"AGG-C14-R3-L95","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","representative_trigger_count":5,"positive_case_count":2,"counterexample_count":3,"stage4b_case_count":3,"stage4c_case_count":2,"current_profile_error_count":3,"current_profile_false_positive_count":1,"current_profile_4c_too_early_count":2,"median_MFE_180D_pct":18.12,"median_MAE_180D_pct":-50.94,"avg_MFE_180D_pct":14.01,"avg_MAE_180D_pct":-41.89,"rule_candidate":"C14_DEMAND_SLOWDOWN_4C_REQUIRES_UTILIZATION_AND_ORDER_CUT_CONFIRMATION","calibration_usable_rows":5}
```

### 25.7 residual_contribution.jsonl

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":5,"new_trigger_family_count":5,"tested_existing_calibrated_axes":["hard_4c_thesis_break_routes_to_4c","full_4b_requires_non_price_evidence"],"residual_error_types_found":["false_positive_stage2_profitability_defense","hard_4c_too_early_when_offsets_survive","correct_4c_protection_when_utilization_order_OP_break_confirmed"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C14_HARD_4C_REQUIRES_UTILIZATION_ORDER_CUT_OR_OPERATING_LOSS_CONFIRMATION | C14_MATERIAL_PRICE_LAG_FALSE_4C_BUFFER | C14_AMPC_JV_ESS_OFFSET_DOWNROUTE_CAP","existing_axis_strengthened":"hard_4c_thesis_break_routes_to_4c | full_4b_requires_non_price_evidence","existing_axis_weakened":"none","summary":"C14 should split hard EV-demand thesis breaks from ASP/inventory/profitability narratives that need 4B watch rather than automatic 4C routing."}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose
You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas. This MD is not live candidate research. It is historical calibration research designed to extend the already-applied calibrated profile. Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context
- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/{prefix}/{symbol}/{year}.csv.
- Symbol profile pattern: atlas/symbol_profiles/{prefix}/{symbol}.json.

### Rules
- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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

## 27. Next Round State

```yaml
completed_round: R3
completed_loop: 95
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under 30 rows
next_recommended_archetype: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
supplementary_next:
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
  - C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
reason: C14 would move from 11 to 16 expected rows after acceptance; C10/C06/C07 remain Priority 0 under-covered and are suitable for next coverage-gap mining.
```

## 28. Source Notes

Primary procedure sources:

```text
MAIN EXECUTION PROMPT:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md

STOCK-WEB MANIFEST:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json

STOCK-WEB SCHEMA:
https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
```

Evidence sources are listed in Sections 9 and 25. Price rows were computed directly from stock-web tradable CSV shards downloaded from `atlas/ohlcv_tradable_by_symbol_year`.

## Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
metadata_round_loop_matches_filename: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 5
representative_rows: 5
source_proxy_only_rows: 0
future_data_leakage_detected: false
production_code_patch_included: false
production_scoring_patch_applied: false
```
