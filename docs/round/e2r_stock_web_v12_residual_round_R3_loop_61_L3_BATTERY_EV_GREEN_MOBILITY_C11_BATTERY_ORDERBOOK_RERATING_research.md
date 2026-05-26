# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R3
loop = 61
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a current stock recommendation, not a live watchlist, not an auto-trading workflow, and not a `stock_agent` code patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual tested here is narrow. It does not re-prove that Stage2 is earlier than Green. It asks whether C11 battery orderbook rerating should reward every contract headline equally. The answer from this small holdout is no: the scoring needs to separate **durable orderbook + capacity conversion** from **single-customer headline contract + call-off risk**.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R3 |
| loop | 61 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE |
| sector | 2차전지·전기차·친환경 |
| loop_objective | coverage_gap_fill / sector_specific_rule_discovery / canonical_archetype_compression / counterexample_mining / 4B_non_price_requirement_stress_test |
| selection_mode | auto_coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts and the local generated-MD snapshot were used only for coverage and duplicate avoidance. Existing local outputs already cover many R13 later loops, but `C11_BATTERY_ORDERBOOK_RERATING` was not present in the local generated snapshot that was inspected. Therefore the run selected C11 instead of repeating the immediately preceding C21 financial-capital-return work.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = not used
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_count = 3
reused_case_count = 0
new_independent_case_ratio = 1.00
diversity_score_summary = avg=27.3; no same symbol+trigger-date+entry-date repetition
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

| Manifest field | Observed value |
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

Schema confirmation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

| case_id | symbol | profile_path | profile caveat | corporate_action_window_status | forward_180D | calibration_usable |
|---|---:|---|---|---|---:|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 003670 | atlas/symbol_profiles/003/003670.json | corporate-action candidates exist in 2015/2021, outside 2023 180D window | clean_180D_window | 180 | true |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 247540 | atlas/symbol_profiles/247/247540.json | corporate-action candidates exist in 2022, outside 2023 180D window | clean_180D_window | 180 | true |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 066970 | atlas/symbol_profiles/066/066970.json | corporate-action candidates exist in 2016/2021, outside 2023 180D window | clean_180D_window | 180 | true |

No row is blocked for the 180D calibration window. All representative triggers use tradable shard rows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE | C11_BATTERY_ORDERBOOK_RERATING | multi-year cathode orderbook plus customer quality plus capacity conversion |
| SINGLE_CUSTOMER_HEADLINE_CONTRACT_CALLOFF_RISK | C11_BATTERY_ORDERBOOK_RERATING | same headline-orderbook family, but capped by concentration/call-off risk |
| PRICE_ONLY_BLOWOFF_AFTER_ORDERBOOK_RERATING | C11_BATTERY_ORDERBOOK_RERATING | 4B overlay only; not a positive entry axis |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 003670 | 포스코퓨처엠 | structural_success | Stage2-Actionable | 2023-01-31 | 224,000 | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_too_late |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 247540 | 에코프로비엠 | structural_success | Stage2-Actionable | 2023-02-01 | 109,200 | 188.92 | -7.69 | 434.8 | -7.69 | current_profile_correct |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 066970 | 엘앤에프 | high_mae_success_or_failed_rerating | Stage2-Actionable-stress | 2023-02-28 | 262,000 | 33.4 | -16.41 | 33.4 | -51.18 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
representative_trigger_count = 3
```

The positive cases show the same mechanism: orderbook was not just a headline. It carried a visible bridge from customer demand to capacity utilization and valuation repricing. The counterexample shows the opposite: the contract headline produced a tradable pop, but single-customer/call-off risk made the return path brittle.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | stage2 evidence | stage3 evidence | 4B/4C evidence |
|---|---|---|---|---|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 2023-01-30 | Samsung SDI / long-duration cathode-material orderbook shock | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, capacity_or_volume_route | multiple_public_sources, durable_customer_confirmation, financial_visibility | none at entry |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 2023-02-01 | cathode orderbook/capacity rerating plus strong relative strength | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, relative_strength | financial_visibility, multiple_public_sources, durable_customer_confirmation | price-only 4B overlay later |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 2023-02-28 | Tesla/high-nickel cathode supply headline, but concentrated and conversion-risky | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility | multiple_public_sources only | later margin/backlog slowdown and call-off watch |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis | adjustment |
|---:|---|---|---|---|---|
| 003670 | 포스코퓨처엠 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | tradable_raw | raw_unadjusted_marcap |
| 247540 | 에코프로비엠 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | tradable_raw | raw_unadjusted_marcap |
| 066970 | 엘앤에프 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | drawdown_after_peak | current_profile_verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| T_C11_POSCOFUTUREM_STAGE2A_2023_01_30 | 003670 | 2023-01-30 | 2023-01-31 | 224,000 | 20.54 | 88.62 | 209.82 | -5.58 | -5.58 | -5.58 | 2023-07-26 | 694,000 | -64.12 | current_profile_too_late |
| T_C11_ECOPROBM_STAGE2A_2023_02_01 | 247540 | 2023-02-01 | 2023-02-01 | 109,200 | 110.16 | 188.92 | 434.8 | -7.69 | -7.69 | -7.69 | 2023-07-26 | 584,000 | -66.03 | current_profile_correct |
| T_C11_LNF_STAGE2A_2023_02_28 | 066970 | 2023-02-28 | 2023-02-28 | 262,000 | 33.4 | 33.4 | 33.4 | -16.41 | -16.41 | -51.18 | 2023-04-03 | 349,500 | -63.4 | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate inclusion rule:

```text
aggregate_metric_inclusion =
  calibration_usable == true
  AND dedupe_for_aggregate == true
  AND aggregate_group_role == representative
  AND do_not_count_as_new_case != true
```

| Metric | Representative triggers | Positive-only selected triggers | Counterexample |
|---|---:|---:|---:|
| avg_MFE_90D_pct | 103.65 | 138.77 | 33.40 |
| avg_MAE_90D_pct | -9.89 | -6.63 | -16.41 |
| avg_MFE_180D_pct | 226.01 | 322.31 | 33.40 |
| avg_MAE_180D_pct | -21.48 | -6.63 | -51.18 |
| false_positive_rate under P0 | 33.3% | 0.0% | 100.0% |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely decision | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | Stage3-Yellow, Green delayed until revisions/capacity visibility | actual 180D MFE was 209.82% with shallow early MAE | current_profile_too_late |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | Stage3-Yellow/Green possible from relative strength plus orderbook context | actual 180D MFE was 434.80%; high later drawdown is 4B overlay, not entry failure | current_profile_correct |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | near-Green possible if headline contract is over-weighted | actual 180D MAE was -51.18%; headline did not protect the path | current_profile_false_positive |

Stress-test answers:

```text
stage2_actionable_evidence_bonus = kept
stage3_yellow_total_min = kept
stage3_green_total_min = kept
stage3_green_revision_min = strengthened within C11 via orderbook-quality/call-off split
price_only_blowoff_guard = kept
full_4b_requires_non_price_evidence = strengthened
hard_4c_thesis_break_routes_to_4c = kept, with L&F marked thesis_break_watch_only rather than entry calibration
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Stage3/Green proxy entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 224,000 | approx. after later capacity/revision confirmation | 0.43 | Green somewhat late; orderbook-quality bridge would have improved timing |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 109,200 | early relative-strength/capacity confirmation | 0.18 | Green not materially late |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 262,000 | no supported Green | not_applicable | headline contract should not force Green |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | 4B entry_date | 4B entry_price | full_window_peak | local_peak_proximity | full_window_peak_proximity | verdict | evidence_type |
|---|---:|---|---:|---:|---:|---:|---|---|
| T_C11_POSCOFUTUREM_4B_PRICE_ONLY_2023_07_26 | 003670 | 2023-07-26 | 560,000 | 694,000 | 0.7149 | 0.7149 | price_only_local_4B_not_full_4B | price_only, valuation_blowoff, positioning_overheat |
| T_C11_ECOPROBM_4B_PRICE_ONLY_2023_07_26 | 247540 | 2023-07-26 | 455,000 | 584,000 | 0.7283 | 0.7283 | price_only_local_4B_not_full_4B | price_only, valuation_blowoff, positioning_overheat |

The price-only 4B overlay was useful as a warning, but it should not become a full 4B unless a non-price exhaustion signal appears. This strengthens the existing `full_4b_requires_non_price_evidence` axis rather than proposing a new global rule.

## 16. 4C Protection Audit

| case_id | 4C label | comment |
|---|---|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | not_4C_trigger | drawdown after peak was severe, but no entry-date thesis break |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | not_4C_trigger | drawdown after peak belongs to 4B/positioning risk, not entry evidence failure |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | thesis_break_watch_only | later call-off/conversion weakness validates a guard, but should not retroactively change entry evidence |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c11_orderbook_quality_capacity_bridge_bonus
delta = +1
scope = L3_BATTERY_EV_GREEN_MOBILITY / C11_BATTERY_ORDERBOOK_RERATING
condition =
  public contract/orderbook evidence
  AND durable customer quality
  AND capacity/volume conversion route
  AND no major call-off/concentration penalty
```

Mechanism: a battery orderbook is like a bridge. The headline contract is the bridge sign; customer quality and capacity conversion are the pillars. Without pillars, the sign may be bright, but the bridge cannot carry rerating weight.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis = c11_customer_concentration_calloff_guard
delta = -2
condition =
  contract/customer headline exists
  BUT customer concentration is high
  AND margin bridge/capacity conversion evidence is weak
  OR call-off/conversion risk is visible
```

This is not a global weakening of contract evidence. It is a C11-specific compression rule: orderbook quality must be judged as a bundle of contract + customer + capacity + margin bridge.

## 19. Before / After Backtest Comparison

| profile | profile_id | hypothesis | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | verdict |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | current global calibrated proxy | none | 3 | 103.65 | -9.89 | 226.01 | -21.48 | 33.3% | 0 | 1 | P0 still over-scores single-customer headline orderbook |
| P0b | e2r_2_0_baseline_reference | rollback reference | pre-calibration thresholds | 3 | 103.65 | -9.89 | 226.01 | -21.48 | 33.3% | 1 | 1 | baseline misses some early non-price orderbook rerating |
| P1 | sector_specific_candidate_profile | L3 orderbook-quality bridge | +capacity_conversion, -calloff risk | 2 selected, 1 blocked | 138.77 | -6.63 | 322.31 | -6.63 | 0.0% | 0 | 0 | better selection quality, but high volatility remains |
| P2 | canonical_archetype_candidate_profile | C11 contract/backlog/customer-quality compression | same as P1 within C11 | 2 selected, 1 blocked | 138.77 | -6.63 | 322.31 | -6.63 | 0.0% | 0 | 0 | best score-return alignment |
| P3 | counterexample_guard_profile | single-customer/call-off guard | headline contract cap unless conversion risk clears | 2 selected, 1 blocked | 138.77 | -6.63 | 322.31 | -6.63 | 0.0% | 0 | 0 | blocks L&F false positive without weakening positives |

## 20. Score-Return Alignment Matrix

| case_id | score_before | label_before | score_after | label_after | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
|---|---:|---|---:|---|---:|---:|---:|---:|---|
| C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK | 82 | Stage3-Yellow | 89 | Stage3-Green | 88.62 | -5.58 | 209.82 | -5.58 | current_profile_too_late |
| C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING | 84 | Stage3-Yellow | 88 | Stage3-Green | 188.92 | -7.69 | 434.8 | -7.69 | current_profile_correct |
| C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK | 86 | Stage3-Yellow/near-Green | 69 | Stage2-Watch / no Green promotion | 33.4 | -16.41 | 33.4 | -51.18 | current_profile_false_positive |

### Raw component score breakdown

### C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK

```json
{
  "raw_component_scores_before": {
    "contract_score": 18,
    "backlog_visibility_score": 17,
    "margin_bridge_score": 6,
    "revision_score": 37,
    "relative_strength_score": 12,
    "customer_quality_score": 20,
    "policy_or_regulatory_score": 5,
    "valuation_repricing_score": 16,
    "execution_risk_score": -4,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0
  },
  "weighted_score_before": 82,
  "stage_label_before": "Stage3-Yellow",
  "raw_component_scores_after": {
    "contract_score": 20,
    "backlog_visibility_score": 23,
    "margin_bridge_score": 8,
    "revision_score": 42,
    "relative_strength_score": 12,
    "customer_quality_score": 23,
    "policy_or_regulatory_score": 5,
    "valuation_repricing_score": 16,
    "execution_risk_score": -3,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "orderbook_quality_score": 10,
    "customer_concentration_risk_adjustment": 0,
    "capacity_conversion_score": 7
  },
  "weighted_score_after": 89,
  "stage_label_after": "Stage3-Green"
}
```
### C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING

```json
{
  "raw_component_scores_before": {
    "contract_score": 14,
    "backlog_visibility_score": 16,
    "margin_bridge_score": 5,
    "revision_score": 36,
    "relative_strength_score": 24,
    "customer_quality_score": 15,
    "policy_or_regulatory_score": 6,
    "valuation_repricing_score": 18,
    "execution_risk_score": -5,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0
  },
  "weighted_score_before": 84,
  "stage_label_before": "Stage3-Yellow",
  "raw_component_scores_after": {
    "contract_score": 16,
    "backlog_visibility_score": 22,
    "margin_bridge_score": 7,
    "revision_score": 41,
    "relative_strength_score": 24,
    "customer_quality_score": 18,
    "policy_or_regulatory_score": 6,
    "valuation_repricing_score": 18,
    "execution_risk_score": -5,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "orderbook_quality_score": 8,
    "customer_concentration_risk_adjustment": 0,
    "capacity_conversion_score": 8
  },
  "weighted_score_after": 88,
  "stage_label_after": "Stage3-Green"
}
```
### C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK

```json
{
  "raw_component_scores_before": {
    "contract_score": 21,
    "backlog_visibility_score": 18,
    "margin_bridge_score": 4,
    "revision_score": 34,
    "relative_strength_score": 18,
    "customer_quality_score": 18,
    "policy_or_regulatory_score": 3,
    "valuation_repricing_score": 18,
    "execution_risk_score": -6,
    "legal_or_contract_risk_score": 0,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0
  },
  "weighted_score_before": 86,
  "stage_label_before": "Stage3-Yellow/near-Green",
  "raw_component_scores_after": {
    "contract_score": 18,
    "backlog_visibility_score": 14,
    "margin_bridge_score": 3,
    "revision_score": 30,
    "relative_strength_score": 15,
    "customer_quality_score": 13,
    "policy_or_regulatory_score": 3,
    "valuation_repricing_score": 15,
    "execution_risk_score": -10,
    "legal_or_contract_risk_score": -5,
    "dilution_cb_risk_score": 0,
    "accounting_trust_risk_score": 0,
    "orderbook_quality_score": 3,
    "customer_concentration_risk_adjustment": -8,
    "call_off_or_conversion_risk_score": -10
  },
  "weighted_score_after": 69,
  "stage_label_after": "Stage2-Watch / no Green promotion"
}
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE | 2 | 1 | 2 | 0 | 3 | 0 | 5 | 3 | 2 | true | true | C12 call-off risk and C13 AMPC/JV utilization remain logical next gaps |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 2
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - price_only_local_4B_not_full_4B
new_axis_proposed:
  - c11_orderbook_quality_capacity_bridge_bonus
  - c11_customer_concentration_calloff_guard
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C11 battery orderbook rerating lacked explicit residual coverage in local snapshot
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual Stock-Web OHLC rows for entry/peak/forward windows
- 30D/90D/180D MFE and MAE
- representative trigger dedupe
- clean 180D corporate-action window
- C11 positive/counterexample balance
- 4B local vs full-window proximity split
```

Not validated:

```text
- no live 2026 candidate scan
- no current recommendation
- no stock_agent source code inspection
- no production scoring patch
- no brokerage or auto-trading logic
- no new price route discovery
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_quality_capacity_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,+1,+1,Multi-year orderbook plus customer quality plus capacity conversion separated POSCO Future M/EcoPro BM positives from headline-only risk,Improved score-return alignment while preserving high-upside entries,T_C11_POSCOFUTUREM_STAGE2A_2023_01_30|T_C11_ECOPROBM_STAGE2A_2023_02_01,3,3,1,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c11_customer_concentration_calloff_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,-2,-2,Single-customer headline contract without margin/capacity conversion created high MAE counterexample,Reduced false positive Green/Yelow promotion,T_C11_LNF_STAGE2A_2023_02_28,3,3,1,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c11_price_only_4b_not_full_4b,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,false,true,+0,Price-only local/full-window peak was useful as overlay but not sufficient for full 4B without non-price evidence,Strengthened existing full_4b_requires_non_price_evidence,T_C11_POSCOFUTUREM_4B_PRICE_ONLY_2023_07_26|T_C11_ECOPROBM_4B_PRICE_ONLY_2023_07_26,2,2,0,medium,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C11_POSCOFUTUREM_STAGE2A_2023_01_30","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook_quality_and_capacity_bridge_separated_positive_rerating_from_customer_concentration_counterexample","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"C11 sector/canonical residual research; no production scoring changed."}
{"row_type":"trigger","trigger_id":"T_C11_POSCOFUTUREM_STAGE2A_2023_01_30","case_id":"C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-30","evidence_available_at_that_date":"Samsung SDI / long-duration cathode-material orderbook shock was public by the trigger date; market could price a multi-year non-price backlog bridge from the next tradable close.","evidence_source":"Company disclosure / press-report family around 2023-01-30 Samsung SDI cathode material supply contract; not a live candidate scan.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility","capacity_or_volume_route"],"stage3_evidence_fields":["multiple_public_sources","durable_customer_confirmation","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-01-31","entry_price":224000,"MFE_30D_pct":20.54,"MFE_90D_pct":88.62,"MFE_180D_pct":209.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.58,"MAE_90D_pct":-5.58,"MAE_180D_pct":-5.58,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-64.12,"green_lateness_ratio":0.43,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_4C_trigger","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_003670_2023_01_31_224000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK","trigger_id":"T_C11_POSCOFUTUREM_STAGE2A_2023_01_30","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":18,"backlog_visibility_score":17,"margin_bridge_score":6,"revision_score":37,"relative_strength_score":12,"customer_quality_score":20,"policy_or_regulatory_score":5,"valuation_repricing_score":16,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":20,"backlog_visibility_score":23,"margin_bridge_score":8,"revision_score":42,"relative_strength_score":12,"customer_quality_score":23,"policy_or_regulatory_score":5,"valuation_repricing_score":16,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"orderbook_quality_score":10,"customer_concentration_risk_adjustment":0,"capacity_conversion_score":7},"weighted_score_after":89,"stage_label_after":"Stage3-Green","changed_components":["orderbook_quality_score","capacity_conversion_score","customer_concentration_risk_adjustment","call_off_or_conversion_risk_score"],"component_delta_explanation":"C11 should reward multi-year orderbook quality only when customer quality, capacity conversion, and margin bridge are present; single-customer headline contract needs call-off/conversion guard.","MFE_90D_pct":88.62,"MAE_90D_pct":-5.58,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"case","case_id":"C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"T_C11_ECOPROBM_STAGE2A_2023_02_01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook_quality_and_capacity_bridge_separated_positive_rerating_from_customer_concentration_counterexample","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C11 sector/canonical residual research; no production scoring changed."}
{"row_type":"trigger","trigger_id":"T_C11_ECOPROBM_STAGE2A_2023_02_01","case_id":"C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-01","evidence_available_at_that_date":"Battery cathode orderbook/capacity rerating became tradable through sector-level non-price evidence and relative strength; not a price-only trigger because the company already sat inside a visible cathode-material supply chain.","evidence_source":"Company/sector disclosure and public report family around early-2023 cathode orderbook expansion; not a live candidate scan.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-01","entry_price":109200,"MFE_30D_pct":110.16,"MFE_90D_pct":188.92,"MFE_180D_pct":434.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.69,"MAE_90D_pct":-7.69,"MAE_180D_pct":-7.69,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-66.03,"green_lateness_ratio":0.18,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_trigger","four_b_evidence_type":[],"four_c_protection_label":"not_4C_trigger","trigger_outcome_label":"structural_success_high_volatility","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_247540_2023_02_01_109200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING","trigger_id":"T_C11_ECOPROBM_STAGE2A_2023_02_01","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":14,"backlog_visibility_score":16,"margin_bridge_score":5,"revision_score":36,"relative_strength_score":24,"customer_quality_score":15,"policy_or_regulatory_score":6,"valuation_repricing_score":18,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":84,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":22,"margin_bridge_score":7,"revision_score":41,"relative_strength_score":24,"customer_quality_score":18,"policy_or_regulatory_score":6,"valuation_repricing_score":18,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"orderbook_quality_score":8,"customer_concentration_risk_adjustment":0,"capacity_conversion_score":8},"weighted_score_after":88,"stage_label_after":"Stage3-Green","changed_components":["orderbook_quality_score","capacity_conversion_score","customer_concentration_risk_adjustment","call_off_or_conversion_risk_score"],"component_delta_explanation":"C11 should reward multi-year orderbook quality only when customer quality, capacity conversion, and margin bridge are present; single-customer headline contract needs call-off/conversion guard.","MFE_90D_pct":188.92,"MAE_90D_pct":-7.69,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"case","case_id":"C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","case_type":"high_mae_success_or_failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"T_C11_LNF_STAGE2A_2023_02_28","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook_quality_and_capacity_bridge_separated_positive_rerating_from_customer_concentration_counterexample","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C11 sector/canonical residual research; no production scoring changed."}
{"row_type":"trigger","trigger_id":"T_C11_LNF_STAGE2A_2023_02_28","case_id":"C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-stress","trigger_date":"2023-02-28","evidence_available_at_that_date":"Tesla/high-nickel cathode supply contract shock produced a real 30D upside, but the trigger was customer-concentrated and had unresolved call-off / conversion risk. Later path delivered a severe MAE, so a naive C11 orderbook bonus would be too permissive.","evidence_source":"Company disclosure / public report family around 2023-02-28 Tesla cathode supply contract; later call-off weakness is ex-post validation, not trigger-date evidence.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","backlog_or_delivery_visibility"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay"],"stage4c_evidence_fields":["call_off_or_order_cut"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-02-28","entry_price":262000,"MFE_30D_pct":33.4,"MFE_90D_pct":33.4,"MFE_180D_pct":33.4,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-16.41,"MAE_90D_pct":-16.41,"MAE_180D_pct":-51.18,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-63.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"not_4B_trigger_at_entry_but_later_backlog_quality_risk_needed","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_066970_2023_02_28_262000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_LNF_2023_TESLA_SINGLE_CUSTOMER_CALLOFF_RISK","trigger_id":"T_C11_LNF_STAGE2A_2023_02_28","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":21,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":34,"relative_strength_score":18,"customer_quality_score":18,"policy_or_regulatory_score":3,"valuation_repricing_score":18,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":86,"stage_label_before":"Stage3-Yellow/near-Green","raw_component_scores_after":{"contract_score":18,"backlog_visibility_score":14,"margin_bridge_score":3,"revision_score":30,"relative_strength_score":15,"customer_quality_score":13,"policy_or_regulatory_score":3,"valuation_repricing_score":15,"execution_risk_score":-10,"legal_or_contract_risk_score":-5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"orderbook_quality_score":3,"customer_concentration_risk_adjustment":-8,"call_off_or_conversion_risk_score":-10},"weighted_score_after":69,"stage_label_after":"Stage2-Watch / no Green promotion","changed_components":["orderbook_quality_score","capacity_conversion_score","customer_concentration_risk_adjustment","call_off_or_conversion_risk_score"],"component_delta_explanation":"C11 should reward multi-year orderbook quality only when customer quality, capacity conversion, and margin bridge are present; single-customer headline contract needs call-off/conversion guard.","MFE_90D_pct":33.4,"MAE_90D_pct":-16.41,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"trigger","trigger_id":"T_C11_POSCOFUTUREM_4B_PRICE_ONLY_2023_07_26","case_id":"C11_POSCOFUTUREM_2023_SDI_CATHODE_ORDERBOOK","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B-price-only-overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"Local/full-window price blowoff around 2023-07-26 after prior Stage2 entry; no separate contract-delay or thesis-break evidence at the 4B timestamp.","evidence_source":"Stock-Web OHLC path only; not treated as full 4B because non-price evidence is absent.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":560000,"MFE_30D_pct":23.93,"MFE_90D_pct":23.93,"MFE_180D_pct":23.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.27,"MAE_90D_pct":-55.54,"MAE_180D_pct":-58.48,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-64.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.7149,"four_b_full_window_peak_proximity":0.7149,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_4C_trigger","trigger_outcome_label":"4B_overlay_price_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_003670_2023_07_26_560000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"T_C11_ECOPROBM_4B_PRICE_ONLY_2023_07_26","case_id":"C11_ECOPROBM_2023_VERTICAL_ORDERBOOK_RERATING","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_CUSTOMER_QUALITY_CAPACITY_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage4B-price-only-overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"Local/full-window price blowoff around 2023-07-26 after prior Stage2 entry; no separate non-price 4B evidence at that timestamp.","evidence_source":"Stock-Web OHLC path only; not treated as full 4B because non-price evidence is absent.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":455000,"MFE_30D_pct":28.35,"MFE_90D_pct":28.35,"MFE_180D_pct":28.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.4,"MAE_90D_pct":-58.77,"MAE_180D_pct":-58.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-66.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.7283,"four_b_full_window_peak_proximity":0.7283,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_4C_trigger","trigger_outcome_label":"4B_overlay_price_only","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_247540_2023_07_26_455000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":null,"independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"row_type":"residual_contribution","round":"R3","loop":"61","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["current_profile_too_late","current_profile_false_positive","price_only_local_4B_not_full_4B"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"diversity_score_summary":"avg=27.3; three new symbols; no same symbol+trigger repetition","auto_selected_coverage_gap":"C11 battery orderbook rerating lacked an explicit positive/counterexample residual MD in the local snapshot"}
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
recommended_next_round = R3_loop_62
recommended_next_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
recommended_next_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
reason = this loop found call-off/conversion risk as the C11 counterexample boundary; C12 should isolate that risk family directly
```

## 28. Source Notes

Stock-Web source paths used:

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
universe = atlas/universe/all_symbols.csv
003670 shard = atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
247540 shard = atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
066970 shard = atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv
003670 profile = atlas/symbol_profiles/003/003670.json
247540 profile = atlas/symbol_profiles/247/247540.json
066970 profile = atlas/symbol_profiles/066/066970.json
```

Evidence-source descriptions are historical event-family labels, not live discovery links. The calibration weight proposal is shadow-only and must be batch-reviewed before any production promotion.
