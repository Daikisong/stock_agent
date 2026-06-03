# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R3
scheduled_loop: 12
completed_round: R3
completed_loop: 12
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R3_loop_12_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
research_scope: historical_trigger_level_residual_research_only
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
stock_web_price_atlas_access_required: true
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds **3** new independent cases, **2** counterexamples, and **2** residual errors for **R3 / L3_BATTERY_EV_GREEN_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING**.

## 1. Current Calibrated Profile Assumption

The current proxy profile is treated as `e2r_2_1_stock_web_calibrated_proxy`, not the old E2R 2.0 baseline. The already-applied global axes are not re-proposed here:

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

This file stress-tests those axes inside the battery cathode orderbook archetype. The core residual is simple: **a huge cathode supply contract is not always the same signal**. It behaves like a signed bridge only when customer quality, margin pass-through, visible capacity, and earnings revision move together. Without those, the same contract headline becomes a paper bridge over a river whose current has already changed.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 12 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE |
| loop_objective | coverage_gap_fill; counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression |
| rule_scope_target | canonical_archetype_specific |
| production_change | false |

R3 is valid because the selected large sector is battery / EV / green mobility. The selected canonical archetype is C11, not C14, because the tested trigger family is the **orderbook rerating trigger itself**, while 4B and 4C rows are used only as overlay / guardrail audits.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed `stock_agent` research artifact access was limited to registry / calibration reports only. The available registry did not show committed `e2r_stock_web_v12_residual_round_R*_loop_*` result files. The immediately prior generated v12 handoff in this conversation completed `R2 / Loop 12` and emitted `next_round = R3`, so this file follows `R3 / Loop 12`.

Duplicate avoidance conclusion:

```text
same_symbol_same_trigger_reuse: none
same_entry_group_reuse: none
previous_global_axis_repetition: avoided
new_symbol_count: 3
new_trigger_family_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
```

The case set deliberately separates one strong structural orderbook rerating from two superficially similar contract headlines that did not translate into clean rerating persistence.

## 4. Stock-Web OHLC Input / Price Source Validation

| Manifest field | Observed value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| raw_row_count | 15,214,118 |
| tradable_row_count | 14,354,401 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Price basis is `tradable_raw`. The OHLC rows are raw/unadjusted marcap rows; they are not split-adjusted. Corporate-action contamination was checked at symbol profile level.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | profile_path | corporate_action_candidate_dates | 180D status | calibration_usable |
|---|---:|---:|---|---|---|---|
| R3L12_C11_POSCO_FUTURE_M_202301 | 003670 | 2023-01-31 | atlas/symbol_profiles/003/003670.json | 2015-05-04; 2021-02-03 | clean_180D_window | true |
| R3L12_C11_LNF_202302 | 066970 | 2023-03-02 | atlas/symbol_profiles/066/066970.json | 2016-02-19; 2021-08-11 | clean_180D_window | true |
| R3L12_C11_ECOPROBM_202312 | 247540 | 2023-12-04 | atlas/symbol_profiles/247/247540.json | 2022-06-27; 2022-07-15 | clean_180D_window | true |

All representative triggers have at least 180 trading days available before the stock-web manifest max date of 2026-02-20.

## 6. Canonical Archetype Compression Map

| Fine trigger family | Canonical archetype | Interpretation |
|---|---|---|
| long_term_cathode_supply_contract | C11_BATTERY_ORDERBOOK_RERATING | Multi-year supply contract that can anchor revenue visibility. |
| customer_quality_plus_capacity_route | C11_BATTERY_ORDERBOOK_RERATING | Contract is stronger when customer, line allocation, and capacity path are visible together. |
| headline_contract_without_margin_bridge | C11_BATTERY_ORDERBOOK_RERATING | Same headline becomes weak when pass-through, utilization, or revision is not visible. |
| orderbook_late_cycle_counterexample | C11_BATTERY_ORDERBOOK_RERATING | A large order signed after sector overheat can fail to rerate. |

Compression rule: do not create separate production axes for every cathode customer name. Keep the scoring unit at C11, then use shadow gates for customer quality, margin bridge, and cycle phase.

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | best_trigger | why selected |
|---|---:|---|---|---|---|---|
| R3L12_C11_POSCO_FUTURE_M_202301 | 003670 | 포스코퓨처엠 / 포스코케미칼 | structural_success | positive | Stage2-Actionable on 2023-01-30 / entry 2023-01-31 | A clean example where a major cathode supply contract, domestic tier-1 customer, and capacity narrative aligned before a large 2023 rerating. |
| R3L12_C11_LNF_202302 | 066970 | 엘앤에프 | failed_rerating | counterexample | Stage2-Actionable on 2023-02-28 / entry 2023-03-02 | A large Tesla-linked supply contract produced initial upside but later high MAE and thesis stress; customer quality alone was not enough. |
| R3L12_C11_ECOPROBM_202312 | 247540 | 에코프로비엠 | failed_rerating | counterexample | Stage2-Actionable on 2023-12-01 / entry 2023-12-04 | Another very large cathode contract headline, but signed after sector overheat and EV-demand slowdown; current profile would likely over-promote without cycle-phase guard. |

## 8. Positive vs Counterexample Balance

| Metric | Count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 5 |
| representative_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

The target balance of two positives was not met, so no global upgrade is proposed. The file still meets the hard minimum because it has at least one positive, at least one counterexample, and at least three calibration-usable representative cases.

## 9. Evidence Source Map

| trigger_id | evidence source | evidence available at trigger date | evidence fields |
|---|---|---|---|
| R3L12_T_POSCO_STAGE2_20230131 | Public company disclosure / market news on POSCO Chemical cathode supply to Samsung SDI, 2023-01-30 | Major multi-year cathode supply contract; large orderbook expansion; tier-1 domestic cell customer | public_event_or_disclosure; customer_or_order_quality; backlog_or_delivery_visibility; capacity_or_volume_route |
| R3L12_T_LNF_STAGE2_20230302 | Public company disclosure / market news on L&F Tesla-linked cathode supply, 2023-02-28 | Large high-nickel cathode materials supply contract headline; single-customer concentration and 4680 ramp dependency remained unresolved | public_event_or_disclosure; customer_or_order_quality; backlog_or_delivery_visibility |
| R3L12_T_ECOPROBM_STAGE2_20231204 | Public company disclosure / market news on EcoPro BM cathode supply to Samsung SDI, 2023-12-01 | Large cathode supply contract after 2023 battery materials overheat and EV-demand concerns | public_event_or_disclosure; customer_or_order_quality; backlog_or_delivery_visibility |
| R3L12_T_POSCO_4B_20230726 | Stock-Web OHLC plus valuation / positioning context | Peak-day blowoff with extreme one-day high/low range; no thesis-break evidence on same date | valuation_blowoff; positioning_overheat; price_only_local_peak |
| R3L12_T_LNF_4C_20231107 | Public earnings / demand slowdown news plus Stock-Web OHLC | Earnings / demand stress after prior Tesla-linked orderbook narrative | thesis_evidence_broken; margin_or_backlog_slowdown; call_off_or_order_cut_watch |

## 10. Price Data Source Map

| symbol | shard path used | profile path | entry date source row |
|---:|---|---|---|
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | 2023-01-31 c=224000 |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | 2023-03-02 c=250500 |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv; atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json | 2023-12-04 c=323000 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | representative? | current_profile_verdict |
|---|---|---:|---|---:|---:|---:|---|---|
| R3L12_T_POSCO_STAGE2_20230131 | R3L12_C11_POSCO_FUTURE_M_202301 | 003670 | Stage2-Actionable | 2023-01-30 | 2023-01-31 | 224000 | yes | current_profile_correct |
| R3L12_T_LNF_STAGE2_20230302 | R3L12_C11_LNF_202302 | 066970 | Stage2-Actionable | 2023-02-28 | 2023-03-02 | 250500 | yes | current_profile_false_positive |
| R3L12_T_ECOPROBM_STAGE2_20231204 | R3L12_C11_ECOPROBM_202312 | 247540 | Stage2-Actionable | 2023-12-01 | 2023-12-04 | 323000 | yes | current_profile_false_positive |
| R3L12_T_POSCO_4B_20230726 | R3L12_C11_POSCO_FUTURE_M_202301 | 003670 | 4B overlay | 2023-07-26 | 2023-07-26 | 560000 | no | current_profile_4B_too_late |
| R3L12_T_LNF_4C_20231107 | R3L12_C11_LNF_202302 | 066970 | 4C overlay | 2023-11-07 | 2023-11-07 | 159000 | no | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative Stage2 / Stage2-Actionable rows

| trigger_id | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L12_T_POSCO_STAGE2_20230131 | 2023-01-31 | 224000 | 20.54% | -5.58% | 88.62% | -5.58% | 209.82% | -5.58% | 2023-07-26 | 694000 | -44.52% |
| R3L12_T_LNF_STAGE2_20230302 | 2023-03-02 | 250500 | 39.52% | -12.57% | 39.52% | -12.57% | 39.52% | -33.81% | 2023-04-03 | 349500 | -52.56% |
| R3L12_T_ECOPROBM_STAGE2_20231204 | 2023-12-04 | 323000 | 9.60% | -13.00% | 9.60% | -34.67% | 9.60% | -49.23% | 2023-12-04 | 354000 | -53.67% |

### 12.2 Notes on calculations

```text
POSCO Future M representative entry = 2023-01-31 c=224000.
Observed full-window peak inside the 180D window = 2023-07-26 high=694000.

L&F representative entry = 2023-03-02 c=250500.
Observed post-trigger peak = 2023-04-03 high=349500; later 180D low observed around 2023-09-27 low=165800.

EcoPro BM representative entry = 2023-12-04 c=323000.
Observed post-trigger peak = 2023-12-04 high=354000; later 180D low observed around 2024-08-05 low=164000.
```

The 1Y/2Y fields are intentionally not used for weight calibration in this loop. They are either unnecessary for the C11 residual being tested or more exposed to later macro / sector-wide drawdown contamination.

## 13. Current Calibrated Profile Stress Test

| case_id | current proxy likely label | actual return alignment | verdict | residual note |
|---|---|---|---|---|
| R3L12_C11_POSCO_FUTURE_M_202301 | Stage2-Actionable / Stage3-Yellow candidate, later Green after confirmation | MFE_180D +209.82%, MAE_180D -5.58% | current_profile_correct | Contract + customer + capacity narrative became a clean rerating bridge. |
| R3L12_C11_LNF_202302 | Stage2-Actionable, possibly Yellow if customer quality overweighted | MFE_30D +39.52%, but later MAE_180D -33.81% | current_profile_false_positive | Customer quality was real, but margin bridge / utilization / revision durability were not strong enough. |
| R3L12_C11_ECOPROBM_202312 | Stage2-Actionable headline, possible Yellow if order size overweighted | MFE_180D only +9.60%, MAE_180D -49.23% | current_profile_false_positive | Late-cycle mega contract after battery-materials overheat should not be treated like early-cycle rerating evidence. |

Axis answers:

```text
1. Stage2 bonus was useful for POSCO Future M, but too generous for late-cycle or single-customer headline cases.
2. Yellow threshold 75 is directionally fine, but C11 needs a margin_bridge/customer-capacity gate before Yellow.
3. Green threshold 87 / revision 55 is strengthened: C11 Green should require revision or margin visibility, not only order value.
4. Price-only blowoff guard is kept and strengthened by the POSCO 2023-07-26 overlay.
5. Full 4B non-price requirement is kept; price-only 4B can reduce risk but should not equal thesis exit.
6. Hard 4C routing is strengthened for L&F-like orderbook reversals when later evidence shows utilization / order cut / margin break.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3-Yellow candidate | Stage3-Green candidate | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R3L12_C11_POSCO_FUTURE_M_202301 | 224000 | ~272500 after early contract digestion / March name-change run | not assigned in this file | not_applicable | Stage2 captured the cleanest asymmetry. Green without revision-source confirmation is intentionally not force-labeled. |
| R3L12_C11_LNF_202302 | 250500 | 328000-349500 momentum zone | no confirmed Green | not_applicable | A Yellow/Green promotion would have been fragile; customer quality alone hid later MAE. |
| R3L12_C11_ECOPROBM_202312 | 323000 | no durable Yellow | no confirmed Green | not_applicable | Same headline size but wrong cycle phase; no Green promotion. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 entry price | 4B entry price | local peak | full-window peak | local proximity | full-window proximity | evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| R3L12_T_POSCO_4B_20230726 | 224000 | 560000 | 694000 | 694000 | 0.715 | 0.715 | price_only; valuation_blowoff; positioning_overheat | good_de_risk_overlay_but_not_full_4B_without_non_price_evidence |

Formula used:

```text
four_b_local_peak_proximity = (560000 - 224000) / (694000 - 224000) = 0.715
four_b_full_window_peak_proximity = (560000 - 224000) / (694000 - 224000) = 0.715
```

Interpretation: the price-only 4B row was useful as a de-risk overlay because the same day contained the 180D high. But because no same-day non-price thesis break was established, it should not be promoted to full 4B exit logic. This strengthens the already-applied `full_4b_requires_non_price_evidence` axis rather than replacing it.

## 16. 4C Protection Audit

| trigger_id | prior thesis | 4C evidence | entry_price | label | protection interpretation |
|---|---|---|---:|---|---|
| R3L12_T_LNF_4C_20231107 | Tesla-linked orderbook rerating from 2023-02-28 | earnings / demand / margin stress after contract optimism | 159000 | hard_4c_late_but_directionally_correct | The stronger protection would have been a C11 guard before Yellow/Green, not a late 4C after most drawdown had already occurred. |

The 4C row is not used as a new representative entry. It exists to mark the path by which a C11 orderbook story can migrate into thesis-break territory.

## 17. Sector-Specific Rule Candidate

```yaml
sector_specific_rule_candidate: false
reason: Only one large sector is tested in this loop. The rule is battery-cathode specific and should remain canonical-archetype scoped unless repeated in other sectors.
```

No L3-wide rule is proposed. Battery cell, cathode, separator, equipment, and recycling chains do not share identical contract economics. The proposed rule belongs to C11 only.

## 18. Canonical-Archetype Rule Candidate

```yaml
canonical_archetype_rule_candidate: true
rule_id: C11_orderbook_margin_bridge_and_cycle_phase_gate
scope: C11_BATTERY_ORDERBOOK_RERATING
proposal_type: archetype_shadow_only
confidence: medium_low
```

Proposed shadow rule:

```text
For C11_BATTERY_ORDERBOOK_RERATING, a large long-term supply contract can support Stage2-Actionable, but Stage3-Yellow/Green requires at least two of:
1. margin_bridge_score supported by pass-through, ASP/spread, or earnings revision evidence;
2. capacity_or_volume_route showing deliverable capacity and timing;
3. customer_quality_score plus reduced single-customer concentration risk;
4. cycle_phase_score not in late-cycle overheat / EV-demand-slowdown regime.

If order size is large but margin bridge and cycle phase are weak, cap promotion at Stage2-Actionable / Watch and add C11 headline_contract_without_margin_bridge penalty.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible reps | avg MFE_90D | avg MAE_90D | avg MFE_180D | avg MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | 45.91% | -17.61% | 86.31% | -29.54% | 66.7% | 0 | mixed_headline_overpromotion |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | 45.91% | -17.61% | 86.31% | -29.54% | 66.7% | 1 | too_blunt_late_or_early |
| P1_L3_sector_specific_candidate_profile | sector shadow | 3 | 45.91% | -17.61% | 86.31% | -29.54% | 66.7% | 0 | not_enough_sector_breadth |
| P2_C11_archetype_candidate_profile | archetype shadow | 3 | 45.91% | -17.61% | 86.31% | -29.54% | 0.0% for Yellow/Green promotion | 0 | better_stage_label_alignment |
| P3_C11_counterexample_guard_profile | guard profile | 3 | 45.91% | -17.61% | 86.31% | -29.54% | 0.0% for Green promotion | 0 | best_false_positive_control |

The raw return averages are unchanged across profiles because the historical OHLC does not change. What changes is which trigger is allowed to become Yellow/Green. The proposed profile improves score-return alignment by keeping L&F 2023 and EcoPro BM 2023-12 as Stage2/watch or failed-rerating examples rather than clean Green candidates.

## 20. Score-Return Alignment Matrix

| case_id | contract_score | customer_quality | margin_bridge | revision | capacity_route | cycle_phase | P0 label | P2 label | outcome alignment |
|---|---:|---:|---:|---:|---:|---:|---|---|---|
| R3L12_C11_POSCO_FUTURE_M_202301 | 90 | 85 | 70 | 55 | 75 | 65 | Stage2/Y | Stage2/Y, later Green only with revision | aligned |
| R3L12_C11_LNF_202302 | 88 | 90 | 35 | 30 | 45 | 45 | Stage2/Y risk | Stage2/watch; no Green | improved |
| R3L12_C11_ECOPROBM_202312 | 95 | 85 | 30 | 25 | 50 | 20 | Stage2/Y risk | Stage2/watch; no Green | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE | 1 | 2 | 1 | 1 | 3 | 0 | 5 | 3 | 2 | false | true | Need additional positive cases outside cathode chain and at least one separator/cell orderbook counterexample. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - headline_contract_without_margin_bridge_false_positive
  - late_cycle_orderbook_overpromotion
  - 4C_late_after_stage_label_overpromotion
new_axis_proposed: C11_orderbook_margin_bridge_and_cycle_phase_gate
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual stock-web tradable OHLC rows for 003670 / 066970 / 247540
- trigger_date / entry_date separation
- 30D / 90D / 180D MFE and MAE for representative rows
- corporate action window check by symbol profile
- current calibrated profile stress test
- 4B local vs full-window split for POSCO Future M 2023-07-26
- C11-specific residual rule proposal
```

Not validated:

```text
- no live 2026 candidate scan
- no investment recommendation
- no stock_agent source code inspection
- no production scoring patch
- no brokerage or execution logic
- no 1Y / 2Y weight calibration in this loop
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_contract_size_weight,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,1.0,0.75,-0.25,"contract size alone overpromoted L&F and EcoPro BM late-cycle cases","lower false positive Green risk",R3L12_T_LNF_STAGE2_20230302|R3L12_T_ECOPROBM_STAGE2_20231204,3,3,2,medium_low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_margin_bridge_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"orderbook rerating needed margin/pass-through/revision support","separates POSCO positive from L&F/EcoProBM false positives",R3L12_T_POSCO_STAGE2_20230131|R3L12_T_LNF_STAGE2_20230302|R3L12_T_ECOPROBM_STAGE2_20231204,3,3,2,medium_low,archetype_shadow_only,"not production; requires later batch validation"
shadow_weight,C11_late_cycle_orderbook_penalty,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"late-cycle orderbook headline after sector overheat had weak forward returns","blocks late-cycle headline Green",R3L12_T_ECOPROBM_STAGE2_20231204,1,1,1,low,archetype_shadow_only,"single case, do not globalize"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L12_C11_POSCO_FUTURE_M_202301","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L12_T_POSCO_STAGE2_20230131","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_large_mfe_low_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Contract/customer/capacity narrative aligned; MFE_180D +209.82%."}
{"row_type":"case","case_id":"R3L12_C11_LNF_202302","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L12_T_LNF_STAGE2_20230302","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"initial_mfe_but_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Customer quality headline needed margin/revision guard."}
{"row_type":"case","case_id":"R3L12_C11_ECOPROBM_202312","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L12_T_ECOPROBM_STAGE2_20231204","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late_cycle_contract_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Mega orderbook headline after sector overheat had MFE_180D only +9.60% and MAE_180D -49.23%."}
{"row_type":"trigger","trigger_id":"R3L12_T_POSCO_STAGE2_20230131","case_id":"R3L12_C11_POSCO_FUTURE_M_202301","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-30","evidence_available_at_that_date":"major cathode supply contract with Samsung SDI; customer and capacity narrative visible","evidence_source":"public disclosure/news","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-31","entry_price":224000,"MFE_30D_pct":20.54,"MFE_90D_pct":88.62,"MFE_180D_pct":209.82,"MFE_1Y_pct":209.82,"MFE_2Y_pct":209.82,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-5.58,"MAE_1Y_pct":-5.58,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-44.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12_G_POSCO_20230131","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L12_T_LNF_STAGE2_20230302","case_id":"R3L12_C11_LNF_202302","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-28","evidence_available_at_that_date":"Tesla-linked high-nickel cathode supply contract headline; margin bridge and customer concentration unresolved","evidence_source":"public disclosure/news","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-03-02","entry_price":250500,"MFE_30D_pct":39.52,"MFE_90D_pct":39.52,"MFE_180D_pct":39.52,"MFE_1Y_pct":39.52,"MFE_2Y_pct":39.52,"MAE_30D_pct":-12.57,"MAE_90D_pct":-12.57,"MAE_180D_pct":-33.81,"MAE_1Y_pct":-44.31,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-52.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"failed_rerating_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12_G_LNF_20230302","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L12_T_ECOPROBM_STAGE2_20231204","case_id":"R3L12_C11_ECOPROBM_202312","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","sector":"battery_ev_green_mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-12-01","evidence_available_at_that_date":"large cathode supply contract headline after 2023 battery-materials overheat and EV-demand slowdown concerns","evidence_source":"public disclosure/news","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv|atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-12-04","entry_price":323000,"MFE_30D_pct":9.60,"MFE_90D_pct":9.60,"MFE_180D_pct":9.60,"MFE_1Y_pct":9.60,"MFE_2Y_pct":9.60,"MAE_30D_pct":-13.00,"MAE_90D_pct":-34.67,"MAE_180D_pct":-49.23,"MAE_1Y_pct":-53.96,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-12-04","peak_price":354000,"drawdown_after_peak_pct":-53.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"late_cycle_orderbook_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12_G_ECOPROBM_20231204","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L12_T_POSCO_4B_20230726","case_id":"R3L12_C11_POSCO_FUTURE_M_202301","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","trigger_type":"4B_overlay","trigger_date":"2023-07-26","entry_date":"2023-07-26","entry_price":560000,"evidence_available_at_that_date":"price-only blowoff / positioning overheat; no same-day thesis-break evidence","evidence_source":"Songdaiki/stock-web OHLC + valuation context","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":23.93,"MFE_90D_pct":23.93,"MFE_180D_pct":23.93,"MAE_30D_pct":-26.79,"MAE_90D_pct":-31.25,"MAE_180D_pct":-44.52,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-44.52,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.715,"four_b_full_window_peak_proximity":0.715,"four_b_timing_verdict":"good_de_risk_overlay_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":null,"trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12_G_POSCO_4B_20230726","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case used for overlay timing only","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R3L12_T_LNF_4C_20231107","case_id":"R3L12_C11_LNF_202302","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_CATHODE_LONG_TERM_CONTRACT_ORDERBOOK_MARGIN_BRIDGE","trigger_type":"4C_overlay","trigger_date":"2023-11-07","entry_date":"2023-11-07","entry_price":159000,"evidence_available_at_that_date":"earnings / demand / margin stress after prior contract optimism","evidence_source":"public earnings/news + stock-web OHLC","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken","call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.25,"MFE_90D_pct":30.50,"MFE_180D_pct":30.50,"MAE_30D_pct":-12.26,"MAE_90D_pct":-12.26,"MAE_180D_pct":-12.26,"peak_date":"2023-12-28","peak_price":207500,"drawdown_after_peak_pct":-20.0,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late_but_directionally_correct","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L12_G_LNF_4C_20231107","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol but new 4C trigger family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12_C11_POSCO_FUTURE_M_202301","trigger_id":"R3L12_T_POSCO_STAGE2_20230131","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":90,"backlog_visibility_score":85,"margin_bridge_score":70,"revision_score":55,"relative_strength_score":60,"customer_quality_score":85,"policy_or_regulatory_score":20,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage2-Actionable / Yellow watch","raw_component_scores_after":{"contract_score":90,"backlog_visibility_score":85,"margin_bridge_score":75,"revision_score":60,"relative_strength_score":60,"customer_quality_score":85,"policy_or_regulatory_score":20,"valuation_repricing_score":65,"execution_risk_score":25,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":75,"cycle_phase_score":65},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable / Yellow, Green only after revision confirmation","changed_components":["margin_bridge_score","capacity_or_shipment_score","cycle_phase_score"],"component_delta_explanation":"C11 positive requires orderbook plus margin/capacity bridge.","MFE_90D_pct":88.62,"MAE_90D_pct":-5.58,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12_C11_LNF_202302","trigger_id":"R3L12_T_LNF_STAGE2_20230302","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":88,"backlog_visibility_score":75,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":70,"customer_quality_score":90,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":45,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage2-Actionable / possible Yellow false positive","raw_component_scores_after":{"contract_score":80,"backlog_visibility_score":65,"margin_bridge_score":35,"revision_score":30,"relative_strength_score":70,"customer_quality_score":75,"policy_or_regulatory_score":10,"valuation_repricing_score":55,"execution_risk_score":50,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":45,"cycle_phase_score":45},"weighted_score_after":68,"stage_label_after":"Stage2-watch; no Yellow/Green without margin bridge","changed_components":["contract_score","customer_quality_score","capacity_or_shipment_score","cycle_phase_score"],"component_delta_explanation":"Customer quality cannot offset missing margin/revision bridge.","MFE_90D_pct":39.52,"MAE_90D_pct":-12.57,"score_return_alignment_label":"improved_false_positive_control","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L12_C11_ECOPROBM_202312","trigger_id":"R3L12_T_ECOPROBM_STAGE2_20231204","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":95,"backlog_visibility_score":80,"margin_bridge_score":30,"revision_score":25,"relative_strength_score":50,"customer_quality_score":85,"policy_or_regulatory_score":10,"valuation_repricing_score":35,"execution_risk_score":55,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable / possible Yellow false positive","raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":70,"margin_bridge_score":30,"revision_score":25,"relative_strength_score":45,"customer_quality_score":80,"policy_or_regulatory_score":10,"valuation_repricing_score":30,"execution_risk_score":65,"legal_or_contract_risk_score":20,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":50,"cycle_phase_score":20},"weighted_score_after":64,"stage_label_after":"Stage2-watch; late-cycle orderbook penalty","changed_components":["contract_score","cycle_phase_score","execution_risk_score"],"component_delta_explanation":"Large contract after sector overheat receives late-cycle penalty.","MFE_90D_pct":9.60,"MAE_90D_pct":-34.67,"score_return_alignment_label":"improved_false_positive_control","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"12","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","scheduled_round":"R3","scheduled_loop":"12","round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["headline_contract_without_margin_bridge_false_positive","late_cycle_orderbook_overpromotion","4C_late_after_stage_label_overpromotion"],"diversity_score_summary":"3 new symbols, 3 new trigger families, 2 counterexamples; no same entry-group reuse","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R3
completed_loop = 12
next_round = R4
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
stock_web_manifest: atlas/manifest.json, generated_at 2026-05-21T16:28:39.421691+00:00, max_date 2026-02-20.
stock_web_profiles_checked:
  - atlas/symbol_profiles/003/003670.json
  - atlas/symbol_profiles/066/066970.json
  - atlas/symbol_profiles/247/247540.json
stock_web_price_shards_checked:
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
  - atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
external_evidence_notes:
  - Public disclosure / news references were used only to identify historical trigger families and dates.
  - Quantitative calibration is based on stock-web OHLC rows, not external price services.
  - No stock_agent source code was opened; no production scoring was changed.
```

