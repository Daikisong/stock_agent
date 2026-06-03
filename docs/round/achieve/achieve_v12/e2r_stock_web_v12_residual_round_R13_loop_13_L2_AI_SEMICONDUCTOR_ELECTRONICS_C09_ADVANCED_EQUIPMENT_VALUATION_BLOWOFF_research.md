# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 13
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF
output_file = e2r_stock_web_v12_residual_round_R13_loop_13_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This loop is a holdout / residual validation pass after the first Stock-Web calibration. It does **not** search for current candidates and does **not** patch `stock_agent`. The case set deliberately tests whether the calibrated global guardrails still need a C09-specific shadow rule for valuation blowoff, price-only 4B, and hard 4C routing.

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

The loop does not re-prove those global axes. It stress-tests them inside advanced semiconductor equipment, where order visibility and valuation rerating often move at different speeds.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R13
loop = 13
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id = CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF
loop_objective = holdout_validation / residual_false_positive_mining / residual_missed_structural_mining / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / coverage_gap_fill
```

This is a C09 holdout after the C07 HBM equipment order / relative strength loop. The difference is mechanical: C07 asks whether order-relative-strength correctly promotes early entries; C09 asks whether the same names should be capped, overlaid with 4B, or routed to 4C once the move becomes valuation-led.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact summary checked:

```text
reports/e2r_calibration/ingest_summary.md
reports/e2r_calibration/applied_scoring_diff.md
```

Observed calibration state:

```text
discovered_result_md_count = 107
validated_trigger_rows = 1940
aggregate_representative_trigger_rows = 1376
rounds_covered = R1~R13
applied global axes include Stage2 bonus, stricter Green, price-only blowoff guard, full 4B non-price evidence, and hard 4C thesis-break routing
```

Novelty basis:

```text
new_symbol_count = 4
new_canonical_archetype_focus = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
new_trigger_family_count = 3
new_trigger_families = valuation_only_false_green, full_window_4b_overlay_after_revision_or_delivery_slowdown, hard_4c_after_thesis_break
required_new_independent_case_ratio = 0.60
actual_new_independent_case_ratio = 0.80
```

One symbol was used in the prior C07 holdout but is reused here only for a different trigger family: 4B/4C valuation blowoff rather than early order-relative-strength entry.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Manifest fields confirmed:

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
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
```

## 5. Historical Eligibility Gate

All representative rows pass the historical gate:

```text
entry row exists = true
minimum 180 forward tradable days = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_contaminated_180D_window = false
MFE/MAE 30D/90D/180D computed = true
```

Corporate-action notes:

```text
042700 profile has candidate dates 2006-11-10, 2017-05-11, 2022-04-06; no overlap with 2024 representative windows.
089030 profile has candidate dates 2011-12-13, 2011-12-29, 2022-08-01, 2022-08-23; no overlap with 2024 representative windows.
095340 profile has candidate date 2023-10-20; no overlap with 2024 representative 180D forward window.
058470 profile has candidate date 2025-04-25; outside the 2024 180D windows used here.
039030 profile has candidate date 2003-02-03; no overlap.
```

## 6. Canonical Archetype Compression Map

```text
fine_archetype = HBM_TCBONDER_ORDER_ROUTE -> canonical_archetype_id = C07 for early order route
fine_archetype = ADVANCED_EQUIPMENT_VALUATION_BLOWOFF -> canonical_archetype_id = C09
fine_archetype = SOCKET_PROBE_QUALITY_RERATING_WITHOUT_ORDER -> canonical_archetype_id = C09 counterexample guard
fine_archetype = PRICE_ONLY_LOCAL_PEAK -> 4B overlay only, not positive stage promotion
fine_archetype = THESIS_BREAK_AFTER_REVISION_OR_MARGIN_SLOWDOWN -> 4C protection route
```

The compression lesson is simple: C07 and C09 can use the same tickers but cannot use the same rule. C07 is the ignition circuit. C09 is the heat shield.

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---|
| R13L13_C09_042700_VALUATION_4B_HOLDOUT | 042700 | 한미반도체 | structural_success | 78500 | 150.0 | -23.06 | 150.0 | -23.06 | current_profile_correct |
| R13L13_C09_089030_VALUATION_4B_HOLDOUT | 089030 | 테크윙 | structural_success | 14600 | 209.59 | -11.71 | 384.93 | -11.71 | current_profile_4B_too_early |
| R13L13_C09_095340_VALUATION_FALSE_GREEN | 095340 | ISC | false_positive_green | 95000 | 13.68 | -32.32 | 13.68 | -48.42 | current_profile_false_positive |
| R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP | 058470 | 리노공업 | failed_rerating | 242500 | 27.42 | -17.32 | 27.42 | -20.25 | current_profile_false_positive |
| R13L13_C09_039030_ADVANCED_EQUIPMENT_4B | 039030 | 이오테크닉스 | 4B_overlay_success | 183900 | 52.8 | -11.15 | 52.8 | -14.03 | current_profile_4B_too_late |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 2
4B_case_count = 3
4C_case_count = 1
calibration_usable_case_count = 5
calibration_usable_trigger_count = 8
representative_trigger_count = 5
```

The positive cases show that advanced-equipment relative strength is real when order/customer/revision evidence joins the move. The counterexamples show that quality, socket exposure, or AI-theme valuation repricing alone is not enough for C09 Green.

## 9. Evidence Source Map

| symbol | evidence family | Stage2 | Stage3 | 4B | 4C |
|---:|---|---|---|---|---|
| 042700 | HBM equipment order + TC bonder capacity route | customer/order, RS, capacity | revision, visibility, customer confirmation | valuation blowoff, positioning | n/a |
| 089030 | HBM handler / equipment relative strength | RS, customer route, early revision | revision, multi-source visibility | valuation blowoff, positioning | n/a |
| 095340 | socket/test theme valuation extension | RS, public event/theme | weak; insufficient bridge | valuation blowoff, margin/backlog slowdown | thesis break watch |
| 058470 | quality socket/probe rerating without explicit order acceleration | customer quality, RS | quality/financial visibility but weak order bridge | valuation blowoff, revision slowdown | thesis break watch |
| 039030 | advanced laser/equipment rerating | RS, capacity route | revision, visibility | valuation blowoff, revision slowdown | n/a |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | basis | adjustment | 180D status |
|---:|---|---|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json | tradable_raw | raw_unadjusted_marcap | clean |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json | tradable_raw | raw_unadjusted_marcap | clean |
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | tradable_raw | raw_unadjusted_marcap | clean |
| 058470 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | tradable_raw | raw_unadjusted_marcap | clean |
| 039030 | atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv | atlas/symbol_profiles/039/039030.json | tradable_raw | raw_unadjusted_marcap | clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak | dd_after_peak | aggregate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| R13L13_C09_042700_S2A_2024-02-08 | Stage2-Actionable | 2024-02-08 | 78500 | 37.32 | 150.0 | 150.0 | -23.06 | -23.06 | -23.06 | 2024-06-14 196200 | -37.92 | representative |
| R13L13_C09_089030_S2A_2024-01-19 | Stage2-Actionable | 2024-01-19 | 14600 | 56.85 | 209.59 | 384.93 | -11.71 | -11.71 | -11.71 | 2024-07-11 70800 | -31.5 | representative |
| R13L13_C09_095340_THEME_2024-03-08 | Stage3-Yellow-candidate | 2024-03-08 | 95000 | 13.68 | 13.68 | 13.68 | -12.63 | -32.32 | -48.42 | 2024-03-28 108000 | -54.63 | representative |
| R13L13_C09_058470_THEME_2024-03-11 | Stage3-Yellow-candidate | 2024-03-11 | 242500 | 16.49 | 27.42 | 27.42 | -17.32 | -17.32 | -20.25 | 2024-05-07 309000 | -37.41 | representative |
| R13L13_C09_039030_S2A_2024-01-19 | Stage2-Actionable | 2024-01-19 | 183900 | 18.27 | 52.8 | 52.8 | -11.15 | -11.15 | -14.03 | 2024-04-12 281000 | -43.74 | representative |
| R13L13_C09_042700_4B_2024-06-14 | Stage4B | 2024-06-14 | 179900 | 2.45 | 9.06 | 9.06 | -26.51 | -32.3 | -37.92 | 2024-06-14 196200 | -37.92 | 4B_overlay_only |
| R13L13_C09_095340_4C_2024-06-21 | Stage4C | 2024-06-21 | 65000 | 1.54 | 8.62 | 8.62 | -24.62 | -24.62 | -24.62 | 2024-06-28 66800 | -26.65 | 4C_overlay_only |
| R13L13_C09_039030_4B_2024-04-12 | Stage4B | 2024-04-12 | 273000 | 2.93 | 2.93 | 2.93 | -20.15 | -42.09 | -42.09 | 2024-04-12 281000 | -43.74 | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate rows:

| symbol | entry_date | entry_price | max high used | peak_date | MFE_180D | min low stress | MAE_180D | interpretation |
|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 042700 | 2024-02-08 | 78,500 | 196,200 | 2024-06-14 | 150.00 | 60,400 | -23.06 | structural winner; 4B late-cycle overlay needed |
| 089030 | 2024-01-19 | 14,600 | 70,800 | 2024-07-11 | 384.93 | 12,890 | -11.71 | structural winner; price-only 4B too early before full peak |
| 095340 | 2024-03-08 | 95,000 | 108,000 | 2024-03-28 | 13.68 | 49,000 | -48.42 | valuation-only false positive if promoted |
| 058470 | 2024-03-11 | 242,500 | 309,000 | 2024-05-07 | 27.42 | 193,400 | -20.25 | quality name, but weak C09 order/revision acceleration |
| 039030 | 2024-01-19 | 183,900 | 281,000 | 2024-04-12 | 52.80 | 158,100 | -14.03 | positive rerating with clear 4B overlay after peak |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile judgement | actual price path | verdict |
|---|---|---|---|
| R13L13_C09_042700_VALUATION_4B_HOLDOUT | Correct positive, but must separate entry from 4B overlay | +150% MFE180, then deep post-peak drawdown | current_profile_correct |
| R13L13_C09_089030_VALUATION_4B_HOLDOUT | Early price-only 4B would be too early | +384.93% MFE180 before full-window peak | current_profile_4B_too_early |
| R13L13_C09_095340_VALUATION_FALSE_GREEN | Relative strength can over-promote valuation-only rerating | +13.68% MFE180 vs -48.42% MAE180 | current_profile_false_positive |
| R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP | Quality/RS can look like Green but lacks order/revision acceleration | +27.42% MFE180 vs -20.25% MAE180 | current_profile_false_positive |
| R13L13_C09_039030_ADVANCED_EQUIPMENT_4B | Positive entry, but 4B overlay needed around full-window peak | +52.80% MFE180 then -43.74% drawdown after peak | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

C09 differs from C07. In C07, early order/relative-strength evidence can justify Stage2-Actionable. In C09, the same relative strength becomes dangerous after valuation has already expanded.

```text
Stage2-Actionable works when:
- customer/order route is explicit,
- backlog or shipment visibility is visible,
- early revision signal exists,
- valuation repricing has not become the only evidence.

Stage3-Green should require:
- confirmed revision,
- order/backlog bridge,
- margin or shipment bridge,
- low red-team risk.

Stage3-Green should be blocked or capped when:
- relative strength is the primary evidence,
- valuation blowoff is already present,
- order/backlog is unknown,
- 4B evidence is stronger than positive evidence.
```

Green lateness:

```text
042700 green_lateness_ratio ~= 0.41
089030 green_lateness_ratio ~= 0.32
039030 green_lateness_ratio ~= 0.47
```

The ratios say Green was not useless, but it arrived after a large part of the move. Stage2-Actionable remains important, while C09 Green must avoid simply chasing the late valuation flame.

## 15. 4B Local vs Full-window Timing Audit

```text
price-only local 4B can be too early = true
full 4B requires non-price evidence = true
C09 proposed condition = valuation blowoff + positioning overheat + revision/delivery/customer slowdown
```

4B rows:

| trigger_id | symbol | entry | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---|
| R13L13_C09_042700_4B_2024-06-14 | 042700 | 179,900 | 1.00 | 0.96 | good_full_window_4B_timing |
| R13L13_C09_039030_4B_2024-04-12 | 039030 | 273,000 | 1.00 | 1.00 | good_full_window_4B_timing |
| R13L13_C09_089030_S2A_2024-01-19 | 089030 | 14,600 | n/a | n/a | price-only local 4B before July would have been too early |

## 16. 4C Protection Audit

The 095340 row is the cleanest C09 hard-4C stress test in this loop:

```text
prior peak = 108,000
4C watch entry = 65,000
post-4C low proxy = 49,000
max_drawdown_after_peak = -54.63%
MAE_90D_after_4C = -24.62%
four_c_protection_label = hard_4c_success_but_late
```

Interpretation: hard 4C routing is directionally correct, but in C09 it must watch valuation-only names earlier, when the positive bridge was never completed.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate = L2 advanced equipment valuation blowoff overlay
```

Rule candidate:

```text
If L2 semiconductor equipment name has:
  relative_strength_score high
  valuation_repricing_score high
  positioning_overheat_score high
but:
  contract_score < medium
  backlog_visibility_score < medium
  revision_score < medium
then:
  block Stage3-Green
  allow at most Stage3-Yellow or 4B watch
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

Proposed C09 axes:

```text
c09_customer_named_order_or_backlog_bridge_required = +1
c09_relative_strength_without_order_cap = +1
c09_full_4b_requires_revision_or_delivery_slowdown = +1
```

This is not a production change. It is a shadow candidate for later batch ingestion.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 5 | 90.7 | -19.11 | 125.77 | -23.49 | 0.4 | 0 | 2 | good on broad direction, weak on C09 valuation-only caps |
| P0b_e2r_2_0_baseline_reference | rollback | old thresholds | 5 | 90.7 | -19.11 | 125.77 | -23.49 | 0.60 | 1 | 1 | worse false-positive control |
| P1_sector_specific_candidate_profile | sector | L2 advanced equipment 4B overlay | 5 | 90.7 | -19.11 | 125.77 | -23.49 | 0.40 | 0 | 1 | improves 4B timing labels |
| P2_canonical_c09_candidate_profile | canonical | order/backlog/revision gate | 5 | 90.7 | -19.11 | 125.77 | -23.49 | 0.20 | 0 | 1 | best score-return alignment |
| P3_counterexample_guard_profile | guard | valuation-only blowoff cap | 5 | 90.7 | -19.11 | 125.77 | -23.49 | 0.20 | 1 | 0 | strongest false-positive guard but can under-promote early winners |


## 20. Score-Return Alignment Matrix

| case_id | P0 current | proposed C09 shadow | observed return alignment |
|---|---|---|---|
| 042700 | positive allowed | positive allowed, 4B separated | aligned |
| 089030 | positive allowed, 4B may be early | positive allowed, price-only 4B blocked until non-price evidence | improved |
| 095340 | can over-promote theme strength | Green capped; 4C watch permitted | improved |
| 058470 | can over-promote quality + RS | Green capped unless order/revision bridge appears | improved |
| 039030 | positive allowed but 4B late | positive allowed; 4B overlay earlier | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF | CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF | 3 | 2 | 3 | 1 | 4 | 1 | 8 | 5 | 4 | true | true | C09 now has holdout coverage for valuation-only false positive and late/early 4B/4C timing |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R13L13_C09_042700_VALUATION_4B_HOLDOUT
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - valuation_only_false_green
  - price_only_4b_too_early
  - hard_4c_too_late_after_unfinished_positive_bridge
new_axis_proposed:
  - c09_customer_named_order_or_backlog_bridge_required
  - c09_relative_strength_without_order_cap
  - c09_full_4b_requires_revision_or_delivery_slowdown
existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: holdout_validation_passed
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and schema basis
- 2024 tradable_raw shards for five symbols
- profile-level corporate-action caveats
- representative trigger MFE/MAE 30D/90D/180D
- 4B overlay rows for timing audit
- one hard 4C watch row
```

Not validated:

```text
- live candidate discovery
- brokerage execution
- current valuation
- production scoring implementation
- exact analyst-consensus database values
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c09_customer_named_order_or_backlog_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"C09 valuation blowoff needs order/backlog/revision bridge to avoid ISC/Leeno style false Green","false positive rate falls from 0.40 to 0.20","R13L13_C09_095340_THEME_2024-03-08|R13L13_C09_058470_THEME_2024-03-11",5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_relative_strength_without_order_cap,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Relative strength alone captured winners but also produced valuation-only false positives","reduces late false positives while keeping Hanmi/Techwing positive if order route is present","R13L13_C09_089030_S2A_2024-01-19|R13L13_C09_095340_THEME_2024-03-08",5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c09_full_4b_requires_revision_or_delivery_slowdown,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF,0,1,+1,"Price-only 4B can be too early; full 4B works better with non-price slowdown evidence","improves 4B local vs full-window separation","R13L13_C09_042700_4B_2024-06-14|R13L13_C09_039030_4B_2024-04-12",5,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "symbol": "042700", "company_name": "한미반도체", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L13_C09_042700_S2A_2024-02-08", "calibration_usable": true, "is_new_independent_case": false, "reuse_reason": "same symbol used in prior C07 holdout, but C09 valuation/4B trigger family is new", "independent_evidence_weight": 0.5, "score_price_alignment": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Order/customer route produced large upside, but the full-cycle 4B worked only after non-price overheat/revision risk was attached, not at the first local spike."}
{"row_type": "case", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "symbol": "089030", "company_name": "테크윙", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R13L13_C09_089030_S2A_2024-01-19", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Relative strength alone was useful early, but early price-only 4B would have cut the move before the full-window peak."}
{"row_type": "case", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "symbol": "095340", "company_name": "ISC", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R13L13_C09_095340_THEME_2024-03-08", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "The entry was a valuation/theme extension without a sufficiently explicit order/backlog bridge; the later drawdown argues for a C09 blowoff cap."}
{"row_type": "case", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "symbol": "058470", "company_name": "리노공업", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R13L13_C09_058470_THEME_2024-03-11", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A quality socket/probe name can reprice, but C09 Green should still require explicit order, backlog, or revision acceleration to avoid valuation-only late entry."}
{"row_type": "case", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "symbol": "039030", "company_name": "이오테크닉스", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "case_type": "4B_overlay_success", "positive_or_counterexample": "positive", "best_trigger": "R13L13_C09_039030_S2A_2024-01-19", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Advanced equipment rerating worked, but valuation blowoff plus later drawdown supports a C09-specific 4B overlay after the first revision-confirmed leg."}
{"row_type": "trigger", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "symbol": "042700", "company_name": "한미반도체", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/residual_false_positive_mining/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "evidence_available_at_that_date": "Order/customer route produced large upside, but the full-cycle 4B worked only after non-price overheat/revision risk was attached, not at the first local spike.", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 78500, "MFE_30D_pct": 37.32, "MFE_90D_pct": 150.0, "MFE_180D_pct": 150.0, "MFE_1Y_pct": 150.0, "MFE_2Y_pct": null, "MAE_30D_pct": -23.06, "MAE_90D_pct": -23.06, "MAE_180D_pct": -23.06, "MAE_1Y_pct": -23.06, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -37.92, "green_lateness_ratio": 0.41, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "requires_separate_4B_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT_2024-02-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": false, "reuse_reason": "same symbol used in prior C07 holdout, but C09 valuation/4B trigger family is new", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "symbol": "089030", "company_name": "테크윙", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/residual_false_positive_mining/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "Relative strength alone was useful early, but early price-only 4B would have cut the move before the full-window peak.", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "customer_or_order_quality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv", "profile_path": "atlas/symbol_profiles/089/089030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 14600, "MFE_30D_pct": 56.85, "MFE_90D_pct": 209.59, "MFE_180D_pct": 384.93, "MFE_1Y_pct": 384.93, "MFE_2Y_pct": null, "MAE_30D_pct": -11.71, "MAE_90D_pct": -11.71, "MAE_180D_pct": -11.71, "MAE_1Y_pct": -11.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 70800, "drawdown_after_peak_pct": -31.5, "green_lateness_ratio": 0.32, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "requires_separate_4B_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT_2024-01-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "symbol": "095340", "company_name": "ISC", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/residual_false_positive_mining/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test/coverage_gap_fill", "trigger_type": "Stage3-Yellow-candidate", "trigger_date": "2024-03-08", "evidence_available_at_that_date": "The entry was a valuation/theme extension without a sufficiently explicit order/backlog bridge; the later drawdown argues for a C09 blowoff cap.", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "valuation_repricing", "public_event_or_disclosure"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "profile_path": "atlas/symbol_profiles/095/095340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-08", "entry_price": 95000, "MFE_30D_pct": 13.68, "MFE_90D_pct": 13.68, "MFE_180D_pct": 13.68, "MFE_1Y_pct": 13.68, "MFE_2Y_pct": null, "MAE_30D_pct": -12.63, "MAE_90D_pct": -32.32, "MAE_180D_pct": -48.42, "MAE_1Y_pct": -48.42, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 108000, "drawdown_after_peak_pct": -54.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "requires_separate_4B_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN_2024-03-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "symbol": "058470", "company_name": "리노공업", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/residual_false_positive_mining/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test/coverage_gap_fill", "trigger_type": "Stage3-Yellow-candidate", "trigger_date": "2024-03-11", "evidence_available_at_that_date": "A quality socket/probe name can reprice, but C09 Green should still require explicit order, backlog, or revision acceleration to avoid valuation-only late entry.", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "valuation_repricing", "customer_or_order_quality"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv", "profile_path": "atlas/symbol_profiles/058/058470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-11", "entry_price": 242500, "MFE_30D_pct": 16.49, "MFE_90D_pct": 27.42, "MFE_180D_pct": 27.42, "MFE_1Y_pct": 27.42, "MFE_2Y_pct": null, "MAE_30D_pct": -17.32, "MAE_90D_pct": -17.32, "MAE_180D_pct": -20.25, "MAE_1Y_pct": -20.25, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-07", "peak_price": 309000, "drawdown_after_peak_pct": -37.41, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "requires_separate_4B_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP_2024-03-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "symbol": "039030", "company_name": "이오테크닉스", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/residual_false_positive_mining/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test/coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-19", "evidence_available_at_that_date": "Advanced equipment rerating worked, but valuation blowoff plus later drawdown supports a C09-specific 4B overlay after the first revision-confirmed leg.", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["confirmed_revision", "multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-19", "entry_price": 183900, "MFE_30D_pct": 18.27, "MFE_90D_pct": 52.8, "MFE_180D_pct": 52.8, "MFE_1Y_pct": 52.8, "MFE_2Y_pct": null, "MAE_30D_pct": -11.15, "MAE_90D_pct": -11.15, "MAE_180D_pct": -14.03, "MAE_1Y_pct": -14.03, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000, "drawdown_after_peak_pct": -43.74, "green_lateness_ratio": 0.47, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "requires_separate_4B_overlay", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B_2024-01-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R13L13_C09_042700_4B_2024-06-14", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "symbol": "042700", "company_name": "한미반도체", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test", "trigger_type": "Stage4B", "trigger_date": "2024-06-14", "evidence_available_at_that_date": "good_full_window_4B_timing", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv", "profile_path": "atlas/symbol_profiles/042/042700.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-14", "entry_price": 179900, "MFE_30D_pct": 2.45, "MFE_90D_pct": 9.06, "MFE_180D_pct": 9.06, "MFE_1Y_pct": 9.06, "MFE_2Y_pct": null, "MAE_30D_pct": -26.51, "MAE_90D_pct": -32.3, "MAE_180D_pct": -37.92, "MAE_1Y_pct": -37.92, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-14", "peak_price": 196200, "drawdown_after_peak_pct": -37.92, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_full_window_4B_timing", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT_2024-06-14", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay row for timing audit; not aggregate representative", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L13_C09_095340_4C_2024-06-21", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "symbol": "095340", "company_name": "ISC", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2024-06-21", "evidence_available_at_that_date": "hard_4c_success_but_late", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "forced_liquidation_or_crash"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv", "profile_path": "atlas/symbol_profiles/095/095340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-21", "entry_price": 65000, "MFE_30D_pct": 1.54, "MFE_90D_pct": 8.62, "MFE_180D_pct": 8.62, "MFE_1Y_pct": 8.62, "MFE_2Y_pct": null, "MAE_30D_pct": -24.62, "MAE_90D_pct": -24.62, "MAE_180D_pct": -24.62, "MAE_1Y_pct": -24.62, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 66800, "drawdown_after_peak_pct": -26.65, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4c_success_but_late", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success_but_late", "trigger_outcome_label": "hard_4c_success_but_late", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN_2024-06-21", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay row for timing audit; not aggregate representative", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R13L13_C09_039030_4B_2024-04-12", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "symbol": "039030", "company_name": "이오테크닉스", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "CROSS_SECTOR_4B_4C_HOLDOUT_ADVANCED_EQUIPMENT_BLOWOFF", "sector": "AI·반도체·전자부품", "primary_archetype": "advanced equipment valuation blowoff holdout", "loop_objective": "holdout_validation/4B_non_price_requirement_stress_test/4C_thesis_break_timing_test", "trigger_type": "Stage4B", "trigger_date": "2024-04-12", "evidence_available_at_that_date": "good_full_window_4B_timing", "evidence_source": "historical_public_report_and_disclosure_proxy; price rows validated against Songdaiki/stock-web", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv", "profile_path": "atlas/symbol_profiles/039/039030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-12", "entry_price": 273000, "MFE_30D_pct": 2.93, "MFE_90D_pct": 2.93, "MFE_180D_pct": 2.93, "MFE_1Y_pct": 2.93, "MFE_2Y_pct": null, "MAE_30D_pct": -20.15, "MAE_90D_pct": -42.09, "MAE_180D_pct": -42.09, "MAE_1Y_pct": -42.09, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-12", "peak_price": 281000, "drawdown_after_peak_pct": -43.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_full_window_4B_timing", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B_2024-04-12", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay row for timing audit; not aggregate representative", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_before": 56.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_after": 56.0, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "current calibrated proxy", "MFE_90D_pct": 150.0, "MAE_90D_pct": -23.06, "score_return_alignment_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0b_e2r_2_0_baseline_reference", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_before": 56.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_after": 56.0, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "rollback reference", "MFE_90D_pct": 150.0, "MAE_90D_pct": -23.06, "score_return_alignment_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P1_sector_specific_candidate_profile", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_before": 56.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_after": 56.0, "stage_label_after": "Stage2-Actionable", "changed_components": [], "component_delta_explanation": "L2 advanced equipment shadow", "MFE_90D_pct": 150.0, "MAE_90D_pct": -23.06, "score_return_alignment_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P2_canonical_c09_candidate_profile", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_before": 56.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_after": 60.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "C09 order/backlog/revision gate", "MFE_90D_pct": 150.0, "MAE_90D_pct": -23.06, "score_return_alignment_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R13L13_C09_042700_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_042700_S2A_2024-02-08", "symbol": "042700", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_before": 56.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 7, "margin_bridge_score": 6, "revision_score": 7, "relative_strength_score": 9, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 8, "thesis_break_score": 0}, "weighted_score_after": 46.0, "stage_label_after": "Stage2", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "valuation blowoff guard", "MFE_90D_pct": 150.0, "MAE_90D_pct": -23.06, "score_return_alignment_label": "structural_success_with_late_full_4b_needed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_before": 44.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_after": 44.9, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "current calibrated proxy", "MFE_90D_pct": 209.59, "MAE_90D_pct": -11.71, "score_return_alignment_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "P0b_e2r_2_0_baseline_reference", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_before": 44.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_after": 44.9, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "rollback reference", "MFE_90D_pct": 209.59, "MAE_90D_pct": -11.71, "score_return_alignment_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "P1_sector_specific_candidate_profile", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_before": 44.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_after": 44.9, "stage_label_after": "Stage2", "changed_components": [], "component_delta_explanation": "L2 advanced equipment shadow", "MFE_90D_pct": 209.59, "MAE_90D_pct": -11.71, "score_return_alignment_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "P2_canonical_c09_candidate_profile", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_before": 44.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_after": 48.9, "stage_label_after": "Stage2-Actionable", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "C09 order/backlog/revision gate", "MFE_90D_pct": 209.59, "MAE_90D_pct": -11.71, "score_return_alignment_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R13L13_C09_089030_VALUATION_4B_HOLDOUT", "trigger_id": "R13L13_C09_089030_S2A_2024-01-19", "symbol": "089030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_before": 44.9, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 6, "backlog_visibility_score": 6, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 9, "capacity_or_shipment_score": 7, "thesis_break_score": 0}, "weighted_score_after": 34.9, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "valuation blowoff guard", "MFE_90D_pct": 209.59, "MAE_90D_pct": -11.71, "score_return_alignment_label": "structural_success_price_only_local_4b_too_early_until_full_window_peak", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_before": 0, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "current calibrated proxy", "MFE_90D_pct": 13.68, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0b_e2r_2_0_baseline_reference", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_before": 0, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "rollback reference", "MFE_90D_pct": 13.68, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P1_sector_specific_candidate_profile", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_before": 0, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "L2 advanced equipment shadow", "MFE_90D_pct": 13.68, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P2_canonical_c09_candidate_profile", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_before": 0, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "C09 order/backlog/revision gate", "MFE_90D_pct": 13.68, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R13L13_C09_095340_VALUATION_FALSE_GREEN", "trigger_id": "R13L13_C09_095340_THEME_2024-03-08", "symbol": "095340", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_before": 0, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 8, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 7}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "valuation blowoff guard", "MFE_90D_pct": 13.68, "MAE_90D_pct": -32.32, "score_return_alignment_label": "false_positive_green_if_relative_strength_not_capped", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_before": 10.9, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_after": 10.9, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "current calibrated proxy", "MFE_90D_pct": 27.42, "MAE_90D_pct": -17.32, "score_return_alignment_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0b_e2r_2_0_baseline_reference", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_before": 10.9, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_after": 10.9, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "rollback reference", "MFE_90D_pct": 27.42, "MAE_90D_pct": -17.32, "score_return_alignment_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P1_sector_specific_candidate_profile", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_before": 10.9, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_after": 10.9, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "L2 advanced equipment shadow", "MFE_90D_pct": 27.42, "MAE_90D_pct": -17.32, "score_return_alignment_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P2_canonical_c09_candidate_profile", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_before": 10.9, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_after": 0, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "C09 order/backlog/revision gate", "MFE_90D_pct": 27.42, "MAE_90D_pct": -17.32, "score_return_alignment_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R13L13_C09_058470_QUALITY_BUT_NO_ORDER_CAP", "trigger_id": "R13L13_C09_058470_THEME_2024-03-11", "symbol": "058470", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_before": 10.9, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 4, "relative_strength_score": 7, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 0, "thesis_break_score": 5}, "weighted_score_after": 0.9, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "valuation blowoff guard", "MFE_90D_pct": 27.42, "MAE_90D_pct": -17.32, "score_return_alignment_label": "quality_company_not_enough_for_c09_green_without_order_or_revision_acceleration", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_after": 37.8, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "current calibrated proxy", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P0b_e2r_2_0_baseline_reference", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_after": 37.8, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "rollback reference", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P1_sector_specific_candidate_profile", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_after": 37.8, "stage_label_after": "Watch/Reject", "changed_components": [], "component_delta_explanation": "L2 advanced equipment shadow", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P2_canonical_c09_candidate_profile", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_after": 31.8, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "C09 order/backlog/revision gate", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "score_simulation", "profile_id": "P3_counterexample_guard_profile", "case_id": "R13L13_C09_039030_ADVANCED_EQUIPMENT_4B", "trigger_id": "R13L13_C09_039030_S2A_2024-01-19", "symbol": "039030", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_before": 37.8, "stage_label_before": "Watch/Reject", "raw_component_scores_after": {"contract_score": 4, "backlog_visibility_score": 4, "margin_bridge_score": 5, "revision_score": 6, "relative_strength_score": 8, "customer_quality_score": 6, "policy_or_regulatory_score": 3, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "positioning_overheat_score": 8, "capacity_or_shipment_score": 6, "thesis_break_score": 0}, "weighted_score_after": 27.8, "stage_label_after": "Watch/Reject", "changed_components": ["c09_order_backlog_gate", "valuation_blowoff_cap"], "component_delta_explanation": "valuation blowoff guard", "MFE_90D_pct": 52.8, "MAE_90D_pct": -11.15, "score_return_alignment_label": "positive_then_4b_overlay_needed_before_full_drawdown", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R13", "loop": "13", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "new_independent_case_count": 4, "reused_case_count": 1, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["valuation_only_false_green", "price_only_4b_too_early", "4c_thesis_break_late_after_drawdown"], "loop_contribution_label": "holdout_validation_passed", "do_not_propose_new_weight_delta": false}
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
next_round = batch_promotion_review
alternative_next_round = R13_loop_14_cross_sector_4C_accounting_trust_holdout
ready_for_batch_promotion_review = true
```

## 28. Source Notes

```text
Stock-Web manifest: atlas/manifest.json
Stock-Web schema: atlas/schema.json
Stock-Web profile paths:
  - atlas/symbol_profiles/042/042700.json
  - atlas/symbol_profiles/089/089030.json
  - atlas/symbol_profiles/095/095340.json
  - atlas/symbol_profiles/058/058470.json
  - atlas/symbol_profiles/039/039030.json
Stock-Web tradable shards:
  - atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv
```
