# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R3_loop_153_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
selected_round = R3
selected_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected_not_sequential
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set
loop_objective = coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This loop adds 6 new independent cases, 4 counterexamples, and 5 residual errors for L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

The current profile is assumed to already include the global Stage2 evidence bonus, stricter Yellow/Green thresholds, price-only blowoff blocking, non-price 4B requirement, and hard 4C thesis-break routing. This MD does not re-propose those global rules. It stress-tests them inside C12, where a customer name or supply-chain vocabulary can look like a contract but still fail if call-off, revenue timing and margin conversion are not visible.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R3 |
| selected_loop | 153 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK |
| fine_archetype_id | mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set |
| scope verdict | R3/L3/C12 valid |

C12 is not a generic battery-upcycle bucket. It is the narrow zone where a named customer, long-term contract, component exposure, approval process, or battery material ramp must be separated from actual call-off, shipment, revenue timing and margin conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index baseline shows C12 at 32 representative rows and Priority 1, with need-to-50 of 18. The previous session loops 151 and 152 already added 상신이디피, TCC스틸, 동원시스템즈, 나노팀, 삼기이브이, 에스피시스템스, 대주전자재료, 세아메카닉스, 알멕, 신흥에스이씨, 나라엠앤디, SNT모티브, 유일에너테크, 삼성SDI. This loop avoids those symbols and uses 101360, 365340, 055490, 317330, 093370, 220260.

```text
index_baseline_coverage_before = C12 rows 32
index_baseline_coverage_after_if_accepted = C12 rows 38
session_aware_after_loop151_loop152_loop153_if_accepted ≈ C12 rows 52
hard_duplicate_check = pass
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

The manifest confirms max_date 2026-02-20, tradable raw/unadjusted shards and corporate-action caveats. All entries here use manifest-bounded forward windows only.

## 5. Historical Eligibility Gate

| symbol | entry_date | forward_window | corporate_action_window_status | calibration_usable | profile caveat |
|---:|---|---:|---|---|---|
| 101360 | 2025-01-16 | 180 | clean_180D_window | true | profile corporate_action_candidate_dates includes 2024-08-01, but selected 2025-01-16 entry through D180 does not overlap it. |
| 365340 | 2024-03-11 | 180 | clean_180D_window | true | clean profile; no corporate-action candidate in 180D window. |
| 055490 | 2022-05-02 | 180 | clean_180D_window | true | clean profile; no corporate-action candidate in 180D window. |
| 317330 | 2024-04-16 | 180 | clean_180D_window | true | clean profile; no corporate-action candidate in 180D window. |
| 093370 | 2024-02-14 | 180 | clean_180D_window | true | clean profile; no corporate-action candidate in 180D window. |
| 220260 | 2023-11-03 | 180 | clean_180D_window | true | profile has 2017 SPAC-related corporate-action candidate only; no overlap with 2023-11 entry window. |


All six representative trigger rows have entry_date, entry_price, 30D/90D/180D MFE and MAE, clean 180D corporate-action status, and at least 180 forward trading rows.

## 6. Canonical Archetype Compression Map

| fine leaf | canonical compression | treatment |
|---|---|---|
| precursor long-term contract but fixed-cost ramp | C12 | require shipment/call-off and margin bridge; otherwise Stage2-Watch |
| recycling plant supply contract with customer approval step | C12 | contract language is incomplete until approval and offtake are confirmed |
| battery tape customer demand narrative | C12 | customer vocabulary alone is not call-off visibility |
| electrolyte additive mass production and secured customer | C12 | can promote if CAPA/ramp and conversion appear together |
| LiPF6 unique supplier but vertical integration risk | C12 | demote when customer self-supply or demand slowdown can cap orders |
| LFP additive expansion tied to domestic battery customer demand | C12 | positive if capex, customer demand and price path align |

## 7. Case Selection Summary

| case | symbol | company | role | trigger | entry | entry_price | MFE30/90/180 | MAE30/90/180 | current verdict |
|---|---:|---|---|---|---|---:|---:|---:|---|
| C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST | 101360 | 에코앤드림 | counterexample / failed_rerating | 2025-01-15 | 2025-01-16 | 28550 | 14.36/14.36/14.36 | -20.49/-29.42/-38.84 | current_profile_false_positive |
| C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL | 365340 | 성일하이텍 | counterexample / failed_rerating | 2024-03-08 | 2024-03-11 | 92500 | 3.24/3.24/3.24 | -21.51/-26.81/-57.03 | current_profile_false_positive |
| C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND | 055490 | 테이팩스 | counterexample / failed_rerating | 2022-04-29 | 2022-05-02 | 84000 | 4.40/4.40/4.40 | -13.45/-27.02/-42.74 | current_profile_false_positive |
| C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP | 317330 | 덕산테코피아 | positive / high_mae_success | 2024-04-15 | 2024-04-16 | 40150 | 12.58/68.12/68.12 | -17.81/-20.17/-33.75 | current_profile_too_late |
| C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK | 093370 | 후성 | counterexample / failed_rerating | 2024-02-13 | 2024-02-14 | 8950 | 3.24/3.24/3.24 | -12.29/-22.91/-41.90 | current_profile_false_positive |
| C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION | 220260 | 켐트로스 | positive / structural_success | 2023-11-02 | 2023-11-03 | 5710 | 17.51/58.32/58.32 | -2.10/-2.10/-4.55 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
positive_case_count = 2
counterexample_count = 4
4B_watch_or_overlay_count = 5
4C_or_thesis_break_watch_count = 4
current_profile_error_count = 5
```

The split is intentionally counterexample-heavy because C12's remaining error is not absence of Stage2 evidence. It is over-acceptance of customer/contract vocabulary before actual call-off and margin conversion.

## 9. Evidence Source Map

| symbol | company | trigger_date | evidence summary | evidence_source |
|---:|---|---|---|---|
| 101360 | 에코앤드림 | 2025-01-15 | 2024 contract-driven precursor sales growth, but fixed-cost burden and profitability timing remain unresolved | https://m.ibks.com/iko/IKO01/download.do?attatchCd=ATTATCH1&menuCode=IKO010201&seq=3912 |
| 365340 | 성일하이텍 | 2024-03-08 | 3공장, customer approval process, and 80% supply-contract comment; price path says approval/call-off timing mattered | https://dealsite.co.kr/articles/119201 |
| 055490 | 테이팩스 | 2022-04-29 | LGES-linked battery tape demand expectation; no sufficient shipment/call-off durability in subsequent path | https://ssl.pstatic.net/imgstock/upload/research/company/1659654218220.pdf |
| 317330 | 덕산테코피아 | 2024-04-15 | electrolyte subsidiary mass-production, customer base and CAPA route; upside appeared but exit risk was large | https://www.dstp.co.kr/board/board.php?bo_table=press&idx=12 |
| 093370 | 후성 | 2024-02-13 | LiPF6 domestic unique supplier and expected demand, offset by electrolyte customer vertical-integration risk | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240213000114&langTpCd=0&method=search&orgid=F&rcpno=20240213000057&tran=Y |
| 220260 | 켐트로스 | 2023-11-02 | electrolyte-additive/LFP demand and capacity expansion narrative aligned with price path | https://ssl.pstatic.net/imgstock/upload/research/company/1698966069712.pdf |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | entry year files checked |
|---:|---|---|---|---|
| 101360 | 에코앤드림 | atlas/ohlcv_tradable_by_symbol_year/101/101360/2025.csv | atlas/symbol_profiles/101/101360.json | atlas/ohlcv_tradable_by_symbol_year/101/101360/2025.csv; atlas/ohlcv_tradable_by_symbol_year/101/101360/2026.csv |
| 365340 | 성일하이텍 | atlas/ohlcv_tradable_by_symbol_year/365/365340/2024.csv | atlas/symbol_profiles/365/365340.json | atlas/ohlcv_tradable_by_symbol_year/365/365340/2024.csv; atlas/ohlcv_tradable_by_symbol_year/365/365340/2025.csv |
| 055490 | 테이팩스 | atlas/ohlcv_tradable_by_symbol_year/055/055490/2022.csv | atlas/symbol_profiles/055/055490.json | atlas/ohlcv_tradable_by_symbol_year/055/055490/2022.csv; atlas/ohlcv_tradable_by_symbol_year/055/055490/2023.csv |
| 317330 | 덕산테코피아 | atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv | atlas/symbol_profiles/317/317330.json | atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv; atlas/ohlcv_tradable_by_symbol_year/317/317330/2025.csv |
| 093370 | 후성 | atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv | atlas/symbol_profiles/093/093370.json | atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv; atlas/ohlcv_tradable_by_symbol_year/093/093370/2025.csv |
| 220260 | 켐트로스 | atlas/ohlcv_tradable_by_symbol_year/220/220260/2023.csv | atlas/symbol_profiles/220/220260.json | atlas/ohlcv_tradable_by_symbol_year/220/220260/2023.csv; atlas/ohlcv_tradable_by_symbol_year/220/220260/2024.csv |


## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | outcome label |
|---:|---|---|---|---|---|---|
| 101360 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | repeat_order_or_conversion | capital_raise_or_overhang, margin_or_backlog_slowdown, positioning_overheat | call_off_or_order_cut, thesis_evidence_broken | long_contract_capacity_ramp_but_fixed_cost_calloff_false_positive |
| 365340 | Stage2-Actionable | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route | - | contract_delay, margin_or_backlog_slowdown, valuation_blowoff | call_off_or_order_cut, thesis_evidence_broken | recycling_factory_supply_contract_but_customer_approval_and_metal_price_drag |
| 055490 | Stage2 | public_event_or_disclosure, customer_or_order_quality | - | positioning_overheat, margin_or_backlog_slowdown | call_off_or_order_cut | battery_tape_customer_demand_narrative_pre_chasm_but_no_calloff_visibility |
| 317330 | Stage2-Actionable | public_event_or_disclosure, capacity_or_volume_route, customer_or_order_quality | repeat_order_or_conversion, financial_visibility | positioning_overheat, price_only_local_peak, capital_raise_or_overhang | - | electrolyte_additive_mass_production_customer_ramp_success_with_4b_exit_guard |
| 093370 | Stage2 | public_event_or_disclosure, customer_or_order_quality | - | margin_or_backlog_slowdown, contract_delay | call_off_or_order_cut, thesis_evidence_broken | domestic_lipf6_unique_supplier_but_customer_vertical_integration_and_demand_risk |
| 220260 | Stage2-Actionable | public_event_or_disclosure, capacity_or_volume_route, customer_or_order_quality, early_revision_signal | financial_visibility, repeat_order_or_conversion | positioning_overheat | - | lfp_electrolyte_additive_capacity_expansion_customer_demand_positive |


## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 101360 | 2025-01-16 | 28550 | 14.36 | -20.49 | 14.36 | -29.42 | 14.36 | -38.84 | 2025-02-26 | 32650 | -46.52 |
| 365340 | 2024-03-11 | 92500 | 3.24 | -21.51 | 3.24 | -26.81 | 3.24 | -57.03 | 2024-03-13 | 95500 | -58.38 |
| 055490 | 2022-05-02 | 84000 | 4.40 | -13.45 | 4.40 | -27.02 | 4.40 | -42.74 | 2022-05-06 | 87700 | -45.15 |
| 317330 | 2024-04-16 | 40150 | 12.58 | -17.81 | 68.12 | -20.17 | 68.12 | -33.75 | 2024-06-24 | 67500 | -60.59 |
| 093370 | 2024-02-14 | 8950 | 3.24 | -12.29 | 3.24 | -22.91 | 3.24 | -41.90 | 2024-02-16 | 9240 | -43.72 |
| 220260 | 2023-11-03 | 5710 | 17.51 | -2.10 | 58.32 | -2.10 | 58.32 | -4.55 | 2024-02-20 | 9040 | -39.71 |


Aggregate read-through:

```text
all_cases_avg_MFE_90D_pct = 25.28
all_cases_avg_MAE_90D_pct = -21.41
positive_cases_avg_MFE_90D_pct = 63.22
positive_cases_avg_MAE_90D_pct = -11.14
counterexample_cases_avg_MFE_90D_pct = 6.31
counterexample_cases_avg_MAE_90D_pct = -26.54
```

## 13. Current Calibrated Profile Stress Test

| symbol | likely current profile behavior | actual path verdict | current_profile_verdict | residual error |
|---:|---|---|---|---|
| 101360 | Stage2-Actionable from long contract and revenue mix | +14.36 MFE but -38.84 180D MAE | current_profile_false_positive | missing call-off/margin bridge |
| 365340 | Stage2-Actionable from 80% supply-contract language | +3.24 MFE, -57.03 180D MAE | current_profile_false_positive | approval and metal-price risk underweighted |
| 055490 | Stage2 from customer demand narrative | +4.40 MFE, -42.74 180D MAE | current_profile_false_positive | no durable shipment/call-off confirmation |
| 317330 | Stage2-Watch or too-slow upgrade | +68.12 MFE with -33.75 180D MAE | current_profile_too_late | missed ramp, but exit guard needed |
| 093370 | Stage2 from unique LiPF6 supplier status | +3.24 MFE, -41.90 180D MAE | current_profile_false_positive | customer vertical integration risk too weak |
| 220260 | Stage2-Actionable from additive/capacity bridge | +58.32 MFE, -4.55 180D MAE | current_profile_correct | good C12 positive template |

## 14. Stage2 / Yellow / Green Comparison

No case has a clean Stage3-Green trigger that would be valid ex-ante without later evidence. The useful comparison is Stage2 vs Stage2-Actionable. In C12, Stage2-Actionable should not mean “customer name exists.” It should mean customer name plus one of call-off visibility, shipment/revenue timing, margin/revision bridge, or capacity already converting into sales.

```text
green_lateness_ratio = not_applicable_no_confirmed_Stage3_Green_trigger
Stage2_Actionable_false_positive_count = 4
Stage2_Actionable_missed_structural_count = 1
```

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence type | local/full-window audit | verdict |
|---:|---|---|---|
| 101360 | capital_raise_or_overhang, margin_or_backlog_slowdown | early MFE +14.36 followed by -46.52 post-peak drawdown | good watch overlay, not full positive |
| 365340 | approval delay, metal/spread drag | near-immediate peak then -58.38 drawdown | full 4B/4C watch should have been early |
| 055490 | margin/backlog slowdown, positioning overheat | +4.40 local MFE then -45.15 post-peak drawdown | Stage2 should stay watch |
| 317330 | price-only local peak, capital overhang | +68.12 MFE but -60.59 post-peak drawdown | high-MFE success with mandatory exit guard |
| 093370 | customer vertical integration, demand risk | +3.24 local MFE then -43.72 post-peak drawdown | false positive guard needed |
| 220260 | positioning overheat after success | +58.32 MFE then -39.71 post-peak drawdown | Stage2 was useful; 4B exit later needed |

## 16. 4C Protection Audit

C12 hard 4C should not fire merely because EV demand slows. It should fire when the customer program, call-off, qualification, or supply standing breaks. In this loop, 성일하이텍 and 후성 are thesis-break watch cases, while 테이팩스 is a slow false-positive decay case. 덕산테코피아 and 켐트로스 were not 4C at trigger; they were Stage2 positives that needed later 4B exit handling.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = L3_BATTERY_CUSTOMER_CALLOFF_REVENUE_TIMING_AND_EXIT_GATE_V3
rule_scope = sector_specific
hypothesis = In L3 battery component/material suppliers, customer vocabulary should promote only to watch unless call-off, shipment/revenue timing, or margin bridge is visible. High-MFE positives still require 4B exit guard when post-peak drawdown exceeds 30%.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C12_CALLOFF_VISIBILITY_REVENUE_TIMING_AND_CUSTOMER_APPROVAL_GATE_V3
new_axis_proposed = c12_calloff_visibility_revenue_timing_and_customer_approval_gate_v3
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_should_not_fire_on_customer_inventory_language_alone
```

Rule mechanics:

1. Customer/contract vocabulary alone: maximum Stage2-Watch.
2. Named customer + call-off or shipment visibility: Stage2.
3. Named customer + call-off/shipment + margin/revision bridge: Stage2-Actionable.
4. Approval step, customer inventory adjustment, vertical integration, capex delay, or heavy fixed-cost ramp: add execution-risk penalty.
5. If MFE90 is strong but post-peak drawdown exceeds 30%, mark `positive_with_4B_exit_guard`, not clean Green.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | customer/contract evidence often lifts Stage2 too early in C12 | 6 | 6 | 25.28 | -21.41 | 25.28 | -36.47 | 0.67 | high MAE and four false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | older baseline is slower and misses some material/ramp winners | 6 | 4 | 63.22 | -11.14 | 63.22 | -19.15 | 0.25 | lower false positives but missed structural paths |
| P1_L3_sector_candidate_profile | sector_specific | battery component Stage2 requires named customer plus shipment/call-off bridge | 6 | 3 | 46.33 | -8.12 | 46.33 | -18.03 | 0.33 | better but still needs canonical gate |
| P2_C12_canonical_candidate_profile | canonical_archetype_specific | add call-off/revenue timing/margin bridge before actionable promotion | 6 | 2 | 63.22 | -11.14 | 63.22 | -19.15 | 0.00 | best alignment for this loop |
| P3_counterexample_guard_profile | guard | demote forecast-only/customer-vocabulary rows to Stage2-Watch or 4B-watch | 6 | 2 | 63.22 | -11.14 | 63.22 | -19.15 | 0.00 | strongest false-positive control |


## 20. Score-Return Alignment Matrix

| symbol | current profile score alignment | proposed C12 gate alignment |
|---:|---|---|
| 101360 | over-promoted contract/revenue mix | demoted to Stage2-Watch until fixed-cost/margin bridge clears |
| 365340 | over-promoted supply-contract comment | demoted until customer approval and actual offtake confirmed |
| 055490 | over-promoted customer demand narrative | watch only without call-off visibility |
| 317330 | too late on electrolyte ramp | promote but attach 4B exit guard |
| 093370 | over-promoted unique LiPF6 supplier status | demote for vertical-integration/customer-demand risk |
| 220260 | correct | keep as positive template |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set | 2 | 4 | 5 | 4 | 6 | 0 | 6 | 6 | 5 | L3_BATTERY_CUSTOMER_CALLOFF_REVENUE_TIMING_AND_EXIT_GATE_V3 | C12_CALLOFF_VISIBILITY_REVENUE_TIMING_AND_CUSTOMER_APPROVAL_GATE_V3 | index baseline 32→38; session-aware ≈46→52 |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 6
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 6
new_canonical_archetype_count: 0
new_fine_archetype_count: 6
new_trigger_family_count: 6
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence|hard_4c_thesis_break_routes_to_4c
residual_error_types_found: contract_vocabulary_false_positive|capacity_ramp_without_calloff_visibility|customer_approval_timing_risk|liPF6_vertical_integration_risk|high_MAE_success_requires_exit_guard
new_axis_proposed: c12_calloff_visibility_revenue_timing_and_customer_approval_gate_v3
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage|full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c_should_not_fire_on_customer_inventory_language_alone
existing_axis_kept: stage2_actionable_evidence_bonus|stage3_yellow_total_min|stage3_green_total_min|stage3_green_revision_min
sector_specific_rule_candidate: L3_BATTERY_CUSTOMER_CALLOFF_REVENUE_TIMING_AND_EXIT_GATE_V3
canonical_archetype_rule_candidate: C12_CALLOFF_VISIBILITY_REVENUE_TIMING_AND_CUSTOMER_APPROVAL_GATE_V3
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical C12 L3 battery customer/contract/call-off cases with confirmed stock-web 30D/90D/180D MFE/MAE.

Non-validation scope: live stock discovery, brokerage/API, production scoring changes, future catalyst prediction, and non-stock-web price routes.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_calloff_visibility_revenue_timing_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"Require call-off/shipment/revenue timing before Stage2-Actionable in C12","reduced 4 false positives while retaining 2 positives","TRG_C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST|TRG_C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL|TRG_C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND|TRG_C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP|TRG_C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK|TRG_C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION",6,6,4,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_high_mfe_exit_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"High-MFE positives in C12 still need post-peak 4B exit guard when drawdown exceeds 30%","protects Duksan/Chemtros style positives after peak","TRG_C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP|TRG_C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION",2,2,0,low,canonical_shadow_only,"exit overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"contract evidence real but call-off/margin bridge too thin; high MAE dominates","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"long_contract_capacity_ramp_but_fixed_cost_calloff_false_positive"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","case_id":"C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","symbol":"101360","company_name":"에코앤드림","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-15","entry_date":"2025-01-16","entry_price":28550.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://m.ibks.com/iko/IKO01/download.do?attatchCd=ATTATCH1&menuCode=IKO010201&seq=3912","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["repeat_order_or_conversion"],"stage4b_evidence_fields":["capital_raise_or_overhang","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/101/101360/2025.csv","profile_path":"atlas/symbol_profiles/101/101360.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.36,"MFE_90D_pct":14.36,"MFE_180D_pct":14.36,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.49,"MAE_90D_pct":-29.42,"MAE_180D_pct":-38.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-26","peak_price":32650.0,"drawdown_after_peak_pct":-46.52,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["capital_raise_or_overhang","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"long_contract_capacity_ramp_but_fixed_cost_calloff_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","trigger_id":"TRG_C12_L153_101360_ECODREAM_20250115_CONTRACT_RAMP_FIXED_COST","symbol":"101360","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":8,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":9,"accounting_trust_risk_score":2},"weighted_score_after":61,"stage_label_after":"Stage2-Watch","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":14.36,"MAE_90D_pct":-29.42,"score_return_alignment_label":"contract evidence real but call-off/margin bridge too thin; high MAE dominates","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","symbol":"365340","company_name":"성일하이텍","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"80% supply-contract language was not enough without product approval, price/spread and shipment conversion","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"recycling_factory_supply_contract_but_customer_approval_and_metal_price_drag"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","case_id":"C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","symbol":"365340","company_name":"성일하이텍","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-11","entry_price":92500.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://dealsite.co.kr/articles/119201","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","valuation_blowoff"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/365/365340/2024.csv","profile_path":"atlas/symbol_profiles/365/365340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MFE_90D_pct":3.24,"MFE_180D_pct":3.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.51,"MAE_90D_pct":-26.81,"MAE_180D_pct":-57.03,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":95500.0,"drawdown_after_peak_pct":-58.38,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"recycling_factory_supply_contract_but_customer_approval_and_metal_price_drag","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","trigger_id":"TRG_C12_L153_365340_SUNGIL_20240308_FACTORY_SUPPLY_APPROVAL","symbol":"365340","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":9,"accounting_trust_risk_score":2},"weighted_score_after":58,"stage_label_after":"Stage2-Watch","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":3.24,"MAE_90D_pct":-26.81,"score_return_alignment_label":"80% supply-contract language was not enough without product approval, price/spread and shipment conversion","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","symbol":"055490","company_name":"테이팩스","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"customer demand vocabulary could trigger Stage2 but should remain watch without call-off and margin durability","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"battery_tape_customer_demand_narrative_pre_chasm_but_no_calloff_visibility"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","case_id":"C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","symbol":"055490","company_name":"테이팩스","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2022-04-29","entry_date":"2022-05-02","entry_price":84000.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1659654218220.pdf","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/055/055490/2022.csv","profile_path":"atlas/symbol_profiles/055/055490.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.4,"MFE_90D_pct":4.4,"MFE_180D_pct":4.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-13.45,"MAE_90D_pct":-27.02,"MAE_180D_pct":-42.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2022-05-06","peak_price":87700.0,"drawdown_after_peak_pct":-45.15,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["positioning_overheat","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"battery_tape_customer_demand_narrative_pre_chasm_but_no_calloff_visibility","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","trigger_id":"TRG_C12_L153_055490_TAPEX_20220429_LGES_TAPE_DEMAND","symbol":"055490","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":9,"accounting_trust_risk_score":2},"weighted_score_after":56,"stage_label_after":"Stage2-Watch","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":4.4,"MAE_90D_pct":-27.02,"score_return_alignment_label":"customer demand vocabulary could trigger Stage2 but should remain watch without call-off and margin durability","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","symbol":"317330","company_name":"덕산테코피아","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"mass production + secured customer/CAPA bridge caught upside but needed exit guard after peak","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"electrolyte_additive_mass_production_customer_ramp_success_with_4b_exit_guard"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","case_id":"C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","symbol":"317330","company_name":"덕산테코피아","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-15","entry_date":"2024-04-16","entry_price":40150.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://www.dstp.co.kr/board/board.php?bo_table=press&idx=12","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality"],"stage3_evidence_fields":["repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat","price_only_local_peak","capital_raise_or_overhang"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/317/317330/2024.csv","profile_path":"atlas/symbol_profiles/317/317330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.58,"MFE_90D_pct":68.12,"MFE_180D_pct":68.12,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.81,"MAE_90D_pct":-20.17,"MAE_180D_pct":-33.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-24","peak_price":67500.0,"drawdown_after_peak_pct":-60.59,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["positioning_overheat","price_only_local_peak","capital_raise_or_overhang"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"electrolyte_additive_mass_production_customer_ramp_success_with_4b_exit_guard","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","trigger_id":"TRG_C12_L153_317330_DUKSAN_20240415_ELECTROLYTE_RAMP","symbol":"317330","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":7,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":64,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":12,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":10,"customer_quality_score":16,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable+4B-Watch","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":68.12,"MAE_90D_pct":-20.17,"score_return_alignment_label":"mass production + secured customer/CAPA bridge caught upside but needed exit guard after peak","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","symbol":"093370","company_name":"후성","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"unique supplier status was offset by electrolyte-maker vertical integration and weak EV demand path","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"domestic_lipf6_unique_supplier_but_customer_vertical_integration_and_demand_risk"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","case_id":"C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","symbol":"093370","company_name":"후성","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2","trigger_date":"2024-02-13","entry_date":"2024-02-14","entry_price":8950.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240213000114&langTpCd=0&method=search&orgid=F&rcpno=20240213000057&tran=Y","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.24,"MFE_90D_pct":3.24,"MFE_180D_pct":3.24,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.29,"MAE_90D_pct":-22.91,"MAE_180D_pct":-41.9,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":9240.0,"drawdown_after_peak_pct":-43.72,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"domestic_lipf6_unique_supplier_but_customer_vertical_integration_and_demand_risk","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","trigger_id":"TRG_C12_L153_093370_FOOSUNG_20240213_LIPF6_VERTICAL_INTEGRATION_RISK","symbol":"093370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":12,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":10,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":5,"customer_quality_score":8,"policy_or_regulatory_score":4,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":14,"dilution_cb_risk_score":9,"accounting_trust_risk_score":2},"weighted_score_after":54,"stage_label_after":"Stage4B-Watch","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":3.24,"MAE_90D_pct":-22.91,"score_return_alignment_label":"unique supplier status was offset by electrolyte-maker vertical integration and weak EV demand path","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"case","case_id":"C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","symbol":"220260","company_name":"켐트로스","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"capacity expansion and domestic battery customer demand bridge aligned with strong MFE and low MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"lfp_electrolyte_additive_capacity_expansion_customer_demand_positive"}
{"row_type":"trigger","trigger_id":"TRG_C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","case_id":"C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","symbol":"220260","company_name":"켐트로스","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"mixed_c12_customer_calloff_approval_ramp_electrolyte_recycling_leaf_set","sector":"battery_ev_green_mobility","primary_archetype":"battery_customer_contract_call_off_risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-11-02","entry_date":"2023-11-03","entry_price":5710.0,"evidence_available_at_that_date":"yes_public_source_available_by_trigger_date_or_report_date","evidence_source":"https://ssl.pstatic.net/imgstock/upload/research/company/1698966069712.pdf","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","customer_or_order_quality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/220/220260/2023.csv","profile_path":"atlas/symbol_profiles/220/220260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.51,"MFE_90D_pct":58.32,"MFE_180D_pct":58.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.1,"MAE_90D_pct":-2.1,"MAE_180D_pct":-4.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-20","peak_price":9040.0,"drawdown_after_peak_pct":-39.71,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4B_overlay_watch_not_full_4B","four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"lfp_electrolyte_additive_capacity_expansion_customer_demand_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"SEG_C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","trigger_id":"TRG_C12_L153_220260_CHEMTROS_20231102_LFP_ADDITIVE_EXPANSION","symbol":"220260","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":16,"backlog_visibility_score":8,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":10,"customer_quality_score":14,"policy_or_regulatory_score":4,"valuation_repricing_score":9,"execution_risk_score":7,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":6,"accounting_trust_risk_score":3},"weighted_score_before":65,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":12,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":10,"customer_quality_score":16,"policy_or_regulatory_score":4,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":4,"accounting_trust_risk_score":2},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable","changed_components":["calloff_visibility_gate","revenue_timing_gate","margin_bridge_gate","execution_risk_penalty"],"component_delta_explanation":"C12-specific shadow profile demands call-off visibility, revenue timing and margin bridge; otherwise contract/customer vocabulary is demoted to watch.","MFE_90D_pct":58.32,"MAE_90D_pct":-2.1,"score_return_alignment_label":"capacity expansion and domestic battery customer demand bridge aligned with strong MFE and low MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R3","loop":"153","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":6,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["contract_vocabulary_false_positive","capacity_ramp_without_calloff_visibility","customer_approval_timing_risk","liPF6_vertical_integration_risk","high_MAE_success_requires_exit_guard"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 6
calibration_usable_trigger_count: 6
representative_trigger_count: 6
new_weight_evidence_candidate_count: 6
guardrail_candidate_count: 5
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
completed_round = R3
completed_loop = 153
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1
next_recommended_archetypes = C05_EPC_MEGA_CONTRACT_MARGIN_GAP|C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION|C27_CONTENT_IP_GLOBAL_MONETIZATION|C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|C19_BRAND_RETAIL_INVENTORY_MARGIN
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest max date: 2026-02-20.
- All trigger rows use `tradable_raw` / `raw_unadjusted_marcap`.
- Entry price is the `c` column of the selected entry date.
- MFE/MAE windows are computed from the post-entry 30/90/180 stock-web tradable rows.
- No current/live stock recommendation is made.
