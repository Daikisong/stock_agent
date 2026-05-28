# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R3
scheduled_loop = 10
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_ORDERBOOK_MARGIN_FCF_UTILIZATION_BRIDGE
sector = 2차전지·전기차·친환경
primary_archetype = battery orderbook rerating with margin/FCF/utilization gate
loop_objective = coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove the global Stage2/Yellow/Green/4B rules. It stress-tests whether C11 battery orderbook rerating needs a narrower bridge: **orderbook headline alone should not promote Green unless margin, FCF, utilization, and customer demand visibility are confirmed**.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 10 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | BATTERY_ORDERBOOK_MARGIN_FCF_UTILIZATION_BRIDGE |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R3 maps to L3_BATTERY_EV_GREEN_MOBILITY. C11 is used because battery orderbook rerating can look like a simple backlog success on the surface, but the historical price path separates two species: orderbook plus margin/FCF conversion, versus orderbook headline without durable profit conversion.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts show R3 has historical coverage, but C11 support remains weaker than the broad R3 sector aggregate. This loop avoids repeating the R1 grid/power and R2 HBM/equipment sets. It also avoids using C14 EV-demand slowdown as a generic 4C label; the target here is specifically C11 orderbook rerating.

Duplicate avoidance rule applied:

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked unless 4B overlay or new trigger family
same_symbol_new_trigger_family = allowed with reuse_reason
minimum_new_independent_case_ratio = 0.60
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest fields verified for this run:

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
markets = KONEX|KOSDAQ|KOSDAQ GLOBAL|KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

## 5. Historical Eligibility Gate

All representative trigger rows below use tradable_raw OHLC rows, have at least 180 forward tradable days available under manifest_max_date=2026-02-20, and do not overlap corporate-action candidate windows inside the D+180 window.

| symbol | company_name | profile_path | corporate_action_window_status | eligibility |
|---|---|---|---|---|
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | clean_180D_window; profile CA dates are 2022-06-27, 2022-07-15 | usable |
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | clean_180D_window; profile CA dates are 2015-05-04, 2021-02-03 | usable |
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | clean_180D_window; profile CA dates are 2016-02-19, 2021-08-11 | usable |
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | clean_180D_window; no corporate-action candidates | usable |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | inclusion logic |
|---|---|---|
| CATHODE_ORDERBOOK_REVENUE_RERATING | C11_BATTERY_ORDERBOOK_RERATING | orderbook + shipment + margin conversion |
| CATHODE_ORDERBOOK_VALUATION_BLOWOFF | C11_BATTERY_ORDERBOOK_RERATING | orderbook success but 4B overlay needed |
| BATTERY_ORDERBOOK_NO_FCF_BRIDGE | C11_BATTERY_ORDERBOOK_RERATING | orderbook headline without FCF/margin proof |
| CELL_ORDERBOOK_AMPC_UTILIZATION_LAG | C11_BATTERY_ORDERBOOK_RERATING | capacity/AMPC visibility without equity rerating confirmation |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | trigger_family | why selected |
|---|---|---|---|---|---|
| R3L10-C11-001 | 247540 | 에코프로비엠 | structural_success + 4B overlay | cathode orderbook + rerating blowoff | orderbook narrative converted into explosive upside, then valuation/positioning overlay mattered |
| R3L10-C11-002 | 003670 | 포스코퓨처엠 | structural_success + 4B overlay | integrated cathode/anode orderbook rerating | similar orderbook rerating, but also highlights late Green risk |
| R3L10-C11-003 | 066970 | 엘앤에프 | false_positive_green | orderbook headline without durable margin/FCF | Green-like score after price move would have been too late/fragile |
| R3L10-C11-004 | 373220 | LG에너지솔루션 | failed_rerating | cell orderbook/AMPC but utilization lag | large orderbook/capacity story did not translate into strong stock-web forward path |
| R3L10-C11-005 | 247540 | 에코프로비엠 | 4B_overlay_success | valuation blowoff / positioning overheat | reused symbol, different trigger family; not counted as a new independent case |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
new_independent_case_count = 4
reused_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
```

The balance is sufficient for a C11 canonical-archetype-specific shadow rule. It is not sufficient for a global rule.

## 9. Evidence Source Map

The evidence map is historical-research proxy, not a live data pull. Evidence is separated by stage family.

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R3L10-C11-001 | public orderbook/contract narrative, relative strength, cathode demand | repeated public rerating, financial visibility improving | valuation blowoff, positioning overheat | none |
| R3L10-C11-002 | cathode/anode orderbook, group battery material expansion | margin bridge expectation, multiple public sources | valuation blowoff after rapid repricing | none |
| R3L10-C11-003 | customer/order headline, relative strength | weak/late margin bridge; FCF not confirmed | price-only local peak | thesis not hard-broken but rerating failed |
| R3L10-C11-004 | capacity/orderbook/AMPC story | insufficient margin/FCF utilization confirmation | none | thesis-break watch only |
| R3L10-C11-005 | not applicable; 4B overlay | not applicable | valuation blowoff + positioning overheat | none |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_years_used |
|---|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json | 2023 |
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json | 2023 |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv | atlas/symbol_profiles/066/066970.json | 2023 |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | atlas/symbol_profiles/373/373220.json | 2023 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | dedupe_for_aggregate | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|
| R3L10-C11-001-T1 | R3L10-C11-001 | 247540 | Stage2-Actionable | 2023-02-09 | 2023-02-09 | 130700 | true | current_profile_correct |
| R3L10-C11-002-T1 | R3L10-C11-002 | 003670 | Stage2-Actionable | 2023-01-26 | 2023-01-26 | 208500 | true | current_profile_correct |
| R3L10-C11-003-T1 | R3L10-C11-003 | 066970 | Stage3-Green | 2023-04-03 | 2023-04-03 | 328000 | true | current_profile_false_positive |
| R3L10-C11-004-T1 | R3L10-C11-004 | 373220 | Stage3-Yellow | 2023-04-11 | 2023-04-11 | 610000 | true | current_profile_too_early |
| R3L10-C11-005-T1 | R3L10-C11-005 | 247540 | Stage4B | 2023-07-26 | 2023-07-26 | 455000 | false | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE use high/low from entry_date through N tradable rows. Values are rounded research calculations from stock-web tradable shards.

| trigger_id | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| R3L10-C11-001-T1 | 130700 | 100.84 | 141.39 | 346.82 | -7.65 | -7.65 | -7.65 | 2023-07-26 | 584000 | -67.88 | true |
| R3L10-C11-002-T1 | 208500 | 29.50 | 102.64 | 232.85 | -12.33 | -12.33 | -12.33 | 2023-07-26 | 694000 | -33.00 | true |
| R3L10-C11-003-T1 | 328000 | 6.55 | 6.55 | 6.55 | -19.51 | -32.62 | -32.62 | 2023-04-03 | 349500 | -36.77 | true |
| R3L10-C11-004-T1 | 610000 | 0.66 | 0.66 | 0.66 | -10.16 | -13.11 | -17.38 | 2023-04-11 | 614000 | -24.43 | true |
| R3L10-C11-005-T1 | 455000 | 28.35 | 28.35 | 28.35 | -19.12 | -58.77 | -58.77 | 2023-07-26 | 584000 | -67.88 | true |

## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely judgment | actual path | verdict |
|---|---|---|---|
| R3L10-C11-001 | Stage2-Actionable correct; Green should wait for revision/margin proof | huge MFE and later severe drawdown | current_profile_correct for entry, 4B needed |
| R3L10-C11-002 | Stage2-Actionable correct; Yellow/Green may lag but still positive | huge MFE, high MAE manageable vs upside | current_profile_correct |
| R3L10-C11-003 | Green-like label after orderbook/price confirmation would be tempting | low upside, large drawdown | current_profile_false_positive |
| R3L10-C11-004 | Yellow/Green could trigger from orderbook + AMPC story | low upside, weak MAE | current_profile_too_early |
| R3L10-C11-005 | 4B overlay after valuation blowoff should not wait for full thesis break | rapid peak proximity, later severe drawdown | current_profile_4B_too_late |

Answers to required stress-test questions:

1. The current profile catches early positive C11 cases when orderbook plus relative strength is present.
2. It is directionally correct for 247540 and 003670, but too permissive for Green-like labels when margin/FCF is absent.
3. Stage2 bonus is not globally too high, but for C11 it should require at least one non-price bridge: order quality, margin visibility, or utilization.
4. Yellow threshold 75 is acceptable as watch state.
5. Green threshold 87 / revision 55 is still necessary; for C11 it should require a battery-specific margin/FCF/utilization bridge.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate, but C11 should allow valuation/positioning blowoff as 4B overlay even before hard thesis break.
8. Hard 4C routing is not the main issue in this loop; the residual is 4B too late and Green too permissive without margin/FCF.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 entry | Green-like entry | peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R3L10-C11-001 | 130700 | 255000 proxy | 584000 | 0.38 | Green somewhat late but still left upside |
| R3L10-C11-002 | 208500 | 342500 proxy | 694000 | 0.28 | Green not fatally late |
| R3L10-C11-003 | 229500 early watch | 328000 | 349500 | 0.88 | Green would capture little upside and large drawdown |
| R3L10-C11-004 | 550000 watch | 610000 | 614000 | 0.94 | Green/Yellow nearly at local peak |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local_peak_price | full_window_peak_price | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---|---:|---:|---:|---:|---|
| R3L10-C11-005-T1 | valuation_blowoff|positioning_overheat | 584000 | 584000 | 0.716 | 0.716 | good_full_window_4B_timing |
| R3L10-C11-003-T1 | price_only_local_peak | 349500 | 349500 | 0.878 | 0.878 | price_only_local_4B_watch_only |
| R3L10-C11-004-T1 | none | 614000 | 614000 | null | null | not_a_4B_overlay |

For C11, the overlay should be **watch-only** if it is merely price-only. It becomes a credible 4B overlay when valuation blowoff and positioning overheat are paired with weakening margin/FCF visibility.

## 16. 4C Protection Audit

No hard 4C trigger is promoted in this loop. The C11 lesson is earlier 4B overlay, not automatic 4C. Counterexample cases are labeled thesis-break-watch-only unless explicit order cut, contract cancellation, accounting break, or customer qualification failure appears.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_axis = battery_orderbook_requires_margin_fcf_utilization_bridge_for_green
baseline_value = not explicit
shadow_value = require_one_of_margin_bridge_or_fcf_conversion_or_utilization_confirmation
confidence = medium
```

Rule candidate:

> In L3 battery/EV, orderbook or capacity expansion may promote Stage2/Yellow, but Stage3-Green should require at least one non-price bridge: margin bridge, FCF conversion, utilization confirmation, customer demand durability, or confirmed revision. Otherwise the label stays Yellow/watch even if relative strength is high.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
candidate_axis = C11_green_bridge_gate
shadow_delta = tighten_green_gate_when_orderbook_lacks_margin_fcf
confidence = medium
```

C11-specific rule:

```text
if canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:
    Stage2_Actionable allowed when orderbook + relative_strength + customer/order quality exist
    Stage3_Yellow allowed when orderbook + one early revision/margin clue exists
    Stage3_Green allowed only when confirmed_revision >= medium AND one of margin_bridge, FCF conversion, utilization, or customer demand durability is present
    price-only blowoff remains blocked from positive stage promotion
    valuation/positioning blowoff can create 4B overlay, not 4C, unless thesis evidence breaks
```

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | 4 | 62.81 | -16.93 | 96.72 | -17.95 | 0.50 | 0 | 2 | mixed; too permissive for Green without margin/FCF |
| P0b_e2r_2_0_baseline_reference | 4 | 62.81 | -16.93 | 96.72 | -17.95 | 0.25 | 1 | 3 | safer but missed early positives |
| P1_sector_specific_candidate_profile | 4 | 62.81 | -16.93 | 96.72 | -17.95 | 0.25 | 0 | 1 | improved balance |
| P2_C11_canonical_candidate_profile | 4 | 62.81 | -16.93 | 96.72 | -17.95 | 0.25 | 0 | 1 | best explanatory fit |
| P3_counterexample_guard_profile | 4 | 62.81 | -16.93 | 96.72 | -17.95 | 0.00 | 1 | 2 | too conservative for positive C11 winners |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R3L10-C11-001-T1 | 78 | Stage2-Actionable | 82 | Stage3-Yellow | 141.39 | -7.65 | strong positive |
| R3L10-C11-002-T1 | 80 | Stage3-Yellow | 83 | Stage3-Yellow | 102.64 | -12.33 | strong positive |
| R3L10-C11-003-T1 | 88 | Stage3-Green | 72 | Stage2/Yellow watch | 6.55 | -32.62 | before false positive; after corrected |
| R3L10-C11-004-T1 | 82 | Stage3-Yellow | 68 | Stage1/Stage2 watch | 0.66 | -13.11 | before too early; after corrected |
| R3L10-C11-005-T1 | 0 | 4B overlay late | 0 | 4B overlay | 28.35 | -58.77 | 4B risk timing improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_ORDERBOOK_MARGIN_FCF_UTILIZATION_BRIDGE | 2 | 2 | 1 | 0 | 4 | 1 | 5 | 4 | 2 | true | true | needs more post-2024 holdout and hard 4C cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 1
reused_case_ids: R3L10-C11-005
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus|stage3_green_total_min|stage3_green_revision_min|full_4b_requires_non_price_evidence|price_only_blowoff_blocks_positive_stage
residual_error_types_found: Green_without_margin_FCF_bridge_false_positive|4B_overlay_too_late_after_valuation_blowoff
new_axis_proposed: null
existing_axis_strengthened: C11-specific Green bridge gate; C11 4B overlay timing with valuation/positioning evidence
existing_axis_weakened: null
existing_axis_kept: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest/schema/profile/shard path usage
- 180D forward window eligibility
- representative trigger MFE/MAE/peak/drawdown
- C11 positive/counterexample split
- C11 Stage2/Yellow/Green/4B interaction
```

Not validated:

```text
- live 2026 candidates
- current recommendation
- exact production score implementation
- brokerage execution
- global calibration promotion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_green_bridge_gate,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,not_explicit,require_margin_or_fcf_or_utilization_bridge,NA,"C11 Green false positives cluster when orderbook headlines lack margin/FCF/utilization confirmation","reduced false-positive Green in 066970 and 373220 while preserving 247540/003670 Stage2/Yellow",R3L10-C11-001-T1|R3L10-C11-002-T1|R3L10-C11-003-T1|R3L10-C11-004-T1,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_4B_overlay_valuation_positioning,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,not_explicit,allow_4B_overlay_when_valuation_and_positioning_overheat,NA,"C11 winners can become full-window 4B before hard thesis break","captures 247540 July 2023 overlay as risk calibration, not positive entry",R3L10-C11-005-T1,1,0,0,low_medium,canonical_shadow_only,"4B rows are overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L10-C11-001","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_REVENUE_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L10-C11-001-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Stage2/Actionable worked; 4B overlay later required."}
{"row_type":"case","case_id":"R3L10-C11-002","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"INTEGRATED_CATHODE_ANODE_ORDERBOOK_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L10-C11-002-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Orderbook rerating worked but required later 4B overlay."}
{"row_type":"case","case_id":"R3L10-C11-003","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_NO_FCF_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R3L10-C11-003-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative_after_late_green","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Green-like score after price and orderbook headline had poor forward asymmetry."}
{"row_type":"case","case_id":"R3L10-C11-004","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CELL_ORDERBOOK_AMPC_UTILIZATION_LAG","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L10-C11-004-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"weak_return_after_orderbook_story","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Large orderbook/capacity story lacked equity rerating without utilization/margin confirmation."}
{"row_type":"case","case_id":"R3L10-C11-005","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_VALUATION_BLOWOFF","case_type":"4B_overlay_success","positive_or_counterexample":"risk_overlay","best_trigger":"R3L10-C11-005-T1","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same symbol as R3L10-C11-001 but new 4B valuation/positioning trigger family","independent_evidence_weight":0.25,"score_price_alignment":"risk_overlay_success","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Reused symbol, not counted as new independent case."}
{"row_type":"trigger","trigger_id":"R3L10-C11-001-T1","case_id":"R3L10-C11-001","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_REVENUE_RERATING","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-09","entry_date":"2023-02-09","entry_price":130700,"evidence_available_at_that_date":"orderbook/relative strength/revision narrative available by trigger proxy","evidence_source":"historical public evidence proxy; stock-web price path","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":100.84,"MFE_90D_pct":141.39,"MFE_180D_pct":346.82,"MFE_1Y_pct":346.82,"MFE_2Y_pct":346.82,"MAE_30D_pct":-7.65,"MAE_90D_pct":-7.65,"MAE_180D_pct":-7.65,"MAE_1Y_pct":-7.65,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":0.38,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_then_4B_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"247540_2023-02-09_130700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L10-C11-002-T1","case_id":"R3L10-C11-002","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"INTEGRATED_CATHODE_ANODE_ORDERBOOK_RERATING","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-26","entry_date":"2023-01-26","entry_price":208500,"evidence_available_at_that_date":"orderbook/relative strength proxy","evidence_source":"historical public evidence proxy; stock-web price path","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":["margin_bridge","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.5,"MFE_90D_pct":102.64,"MFE_180D_pct":232.85,"MFE_1Y_pct":232.85,"MFE_2Y_pct":232.85,"MAE_30D_pct":-12.33,"MAE_90D_pct":-12.33,"MAE_180D_pct":-12.33,"MAE_1Y_pct":-12.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-33.0,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_then_4B_needed","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"003670_2023-01-26_208500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L10-C11-003-T1","case_id":"R3L10-C11-003","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_NO_FCF_BRIDGE","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage3-Green","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":328000,"evidence_available_at_that_date":"orderbook/price confirmation but margin and FCF bridge weak","evidence_source":"historical public evidence proxy; stock-web price path","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.55,"MFE_90D_pct":6.55,"MFE_180D_pct":6.55,"MFE_1Y_pct":6.55,"MFE_2Y_pct":6.55,"MAE_30D_pct":-19.51,"MAE_90D_pct":-32.62,"MAE_180D_pct":-32.62,"MAE_1Y_pct":-32.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-03","peak_price":349500,"drawdown_after_peak_pct":-36.77,"green_lateness_ratio":0.88,"four_b_local_peak_proximity":0.878,"four_b_full_window_peak_proximity":0.878,"four_b_timing_verdict":"price_only_local_4B_watch_only","four_b_evidence_type":["price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"066970_2023-04-03_328000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L10-C11-004-T1","case_id":"R3L10-C11-004","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CELL_ORDERBOOK_AMPC_UTILIZATION_LAG","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage3-Yellow","trigger_date":"2023-04-11","entry_date":"2023-04-11","entry_price":610000,"evidence_available_at_that_date":"cell orderbook/AMPC/capacity narrative but utilization and margin conversion unconfirmed","evidence_source":"historical public evidence proxy; stock-web price path","stage2_evidence_fields":["capacity_or_volume_route","policy_or_regulatory_optionality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.66,"MFE_90D_pct":0.66,"MFE_180D_pct":0.66,"MFE_1Y_pct":0.66,"MFE_2Y_pct":0.66,"MAE_30D_pct":-10.16,"MAE_90D_pct":-13.11,"MAE_180D_pct":-17.38,"MAE_1Y_pct":-17.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-11","peak_price":614000,"drawdown_after_peak_pct":-24.43,"green_lateness_ratio":0.94,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_overlay","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"373220_2023-04-11_610000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L10-C11-005-T1","case_id":"R3L10-C11-005","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_VALUATION_BLOWOFF","sector":"2차전지·전기차·친환경","primary_archetype":"battery orderbook rerating","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-07-26","entry_date":"2023-07-26","entry_price":455000,"evidence_available_at_that_date":"valuation blowoff and positioning overheat after orderbook rerating","evidence_source":"historical public evidence proxy; stock-web price path","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":28.35,"MFE_90D_pct":28.35,"MFE_180D_pct":28.35,"MFE_1Y_pct":28.35,"MFE_2Y_pct":28.35,"MAE_30D_pct":-19.12,"MAE_90D_pct":-58.77,"MAE_180D_pct":-58.77,"MAE_1Y_pct":-58.77,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.716,"four_b_full_window_peak_proximity":0.716,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"247540_2023-07-26_455000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same symbol as positive case but distinct 4B valuation/positioning trigger family","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L10-C11-001","trigger_id":"R3L10-C11-001-T1","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":65,"margin_bridge_score":45,"revision_score":50,"relative_strength_score":85,"customer_quality_score":70,"policy_or_regulatory_score":45,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":70,"margin_bridge_score":55,"revision_score":55,"relative_strength_score":85,"customer_quality_score":70,"policy_or_regulatory_score":45,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score"],"component_delta_explanation":"C11 allows stronger Yellow when orderbook is paired with margin/revision bridge; Green still waits.","MFE_90D_pct":141.39,"MAE_90D_pct":-7.65,"score_return_alignment_label":"strong_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L10-C11-003","trigger_id":"R3L10-C11-003-T1","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":65,"backlog_visibility_score":60,"margin_bridge_score":30,"revision_score":35,"relative_strength_score":80,"customer_quality_score":50,"policy_or_regulatory_score":20,"valuation_repricing_score":65,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":65,"backlog_visibility_score":55,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":20,"valuation_repricing_score":55,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2/Yellow watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Orderbook without margin/FCF bridge is downgraded from Green to watch.","MFE_90D_pct":6.55,"MAE_90D_pct":-32.62,"score_return_alignment_label":"false_positive_removed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"10","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":4,"reused_case_count":1,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["Green_without_margin_FCF_bridge_false_positive","4B_overlay_too_late_after_valuation_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 10
next_round = R4
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web files used:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/247/247540.json
atlas/symbol_profiles/003/003670.json
atlas/symbol_profiles/066/066970.json
atlas/symbol_profiles/373/373220.json
atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv
```

No live scan, no current recommendation, no production scoring change.

