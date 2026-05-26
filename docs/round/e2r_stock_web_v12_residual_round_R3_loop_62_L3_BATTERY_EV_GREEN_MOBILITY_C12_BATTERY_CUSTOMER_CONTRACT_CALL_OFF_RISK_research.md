# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 62
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id = BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_web_price_atlas_access_required = true
```

This loop does **not** scan current candidates, does not recommend stocks, and does not patch `stock_agent`. It only produces a historical residual research file that can later be ingested by a separate coding agent.

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

The point of this loop is not to re-prove the global Stage2/Green/4B calibration. The target residual is narrower: in the battery chain, a large orderbook can look real while customer pull-in, inventory digestion, or qualification/call-off behavior quietly breaks the delivery bridge. The scoring question is whether C12 needs a separate customer-quality and utilization risk overlay, and where that overlay becomes too aggressive.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R3 |
| loop | 62 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK |
| fine_archetype_id | BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| representative symbols | 066970, 278280, 247540 |
| case mix | 2 risk-success cases, 1 false-risk / counterexample case, 1 4B overlay comparison trigger |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible artifact check was restricted to permitted research artifacts only. A repository search for `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK` returned no direct hit in the accessible `stock_agent` search index. The visible `md_registry.jsonl` sample showed repeated parsed loops in R10-R13 and early R1, but no visible C12 battery call-off research block in the returned slice.

Diversity decision:

```text
auto_selected_coverage_gap = C12 battery customer / call-off risk lacked visible direct coverage in accessible registry/search snapshot
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
same_symbol_new_trigger_family = allowed only because C12 is a different canonical risk axis from prior C11 orderbook-rerating work
minimum_new_independent_case_ratio = 1.00
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

The loop intentionally separates C11 orderbook rerating from C12 customer call-off risk. C11 asks whether backlog/customer/orderbook quality should promote rerating. C12 asks when the same apparent backlog should be discounted because the customer does not pull volume through the P&L.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used in this loop:

| field | value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
price_basis = tradable_raw
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
calibration_usable_rules = entry row exists, >=180 forward tradable days, positive OHLCV, clean 180D corporate-action window
```

## 5. Historical Eligibility Gate

| symbol | company_name | profile_path | profile last_date | corporate_action_candidate_dates | 180D status | calibration_usable |
|---|---|---|---:|---|---|---|
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | 2026-02-20 | 2016-02-19; 2021-08-11 | clean for 2023-07-26 window | true |
| 278280 | 천보 | atlas/symbol_profiles/278/278280.json | 2026-02-20 | none | clean for 2023-04-25 window | true |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | 2026-02-20 | 2022-06-27; 2022-07-15 | clean for 2023-04-25 and 2023-07-26 windows | true |

No 180D window used for quantitative calibration overlaps the profile-level corporate action candidate dates.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compression rule |
|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | customer concentration risk | customer concentration alone is not enough; it becomes scoring-negative only when paired with revision/margin/utilization stress |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | inventory digestion / customer pull-in risk | treat as Stage2-risk or 4B overlay if customer pull-in slows while orderbook narrative remains optically intact |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | call-off false alarm | if demand visibility and relative strength remain dominant, avoid hard negative routing before non-price call-off evidence appears |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | selected trigger | entry_date | entry_price | reason selected |
|---|---:|---|---|---|---|---|---:|---|
| C12-R3L62-066970 | 066970 | 엘앤에프 | 4B_overlay_success | positive | C12 customer concentration + call-off risk watch | 2023-07-26 | 263000 | high customer concentration / delivery-conversion risk became decisive after battery-material blowoff; 90D MAE dominated residual |
| C12-R3L62-278280 | 278280 | 천보 | failed_rerating | positive | electrolyte utilization / demand call-off risk | 2023-04-25 | 195000 | orderbook narrative did not close into margin/revision; 180D drawdown showed customer pull-in risk |
| C12-R3L62-247540 | 247540 | 에코프로비엠 | false_positive_green | counterexample | early customer-risk false alarm | 2023-04-25 | 253500 | customer/order concentration narrative alone would have blocked a major later move; non-price call-off evidence was not yet sufficient |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
```

C12 is a risk archetype, so “positive” means the C12 risk rule would have helped timing or protection. The counterexample is equally important: customer concentration can look scary too early, while price and delivery-conversion still say the market is pulling the orderbook forward.

## 9. Evidence Source Map

This loop separates **research proxy evidence** from **price validation evidence**.

| case_id | evidence_available_at_that_date | evidence_source | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|---|
| C12-R3L62-066970 | 2023-07-26 | public sector/filing/report proxy; stock-web price row validated | customer concentration; capacity/customer pull-in risk; relative strength reversal | weak confirmed revision; margin bridge not closed | valuation/positioning overheat + later margin/revision slowdown watch |
| C12-R3L62-278280 | 2023-04-25 | public sector/filing/report proxy; stock-web price row validated | electrolyte demand sensitivity; utilization / customer pull-in risk | margin bridge not closed; revision stress | thesis-break watch, not hard 4C on trigger date |
| C12-R3L62-247540 | 2023-04-25 | public sector/filing/report proxy; stock-web price row validated | customer/order concentration narrative only | orderbook and relative strength still dominant | hard C12 block would be premature; 4B only after July blowoff |

Later ingestion should re-attach exact DART/report/news references before production promotion. The price metrics here are already stock-web validated; the qualitative evidence labels are conservative research proxies.

## 10. Price Data Source Map

| symbol | price_shard_path(s) | profile_path | source basis |
|---:|---|---|---|
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv; 2024.csv | atlas/symbol_profiles/066/066970.json | tradable_raw, raw_unadjusted_marcap |
| 278280 | atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv; 2024.csv | atlas/symbol_profiles/278/278280.json | tradable_raw, raw_unadjusted_marcap |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv; 2024.csv | atlas/symbol_profiles/247/247540.json | tradable_raw, raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | same_entry_group_id | aggregate role | current_profile_verdict |
|---|---|---|---|---|---:|---|---|---|
| C12-066970-20230726-RISK | C12-R3L62-066970 | Stage2-Risk-Actionable | 2023-07-26 | 2023-07-26 | 263000 | C12-066970-20230726 | representative | current_profile_4B_too_late |
| C12-278280-20230425-RISK | C12-R3L62-278280 | Stage2-Risk-Actionable | 2023-04-25 | 2023-04-25 | 195000 | C12-278280-20230425 | representative | current_profile_missed_structural |
| C12-247540-20230425-FALSE-RISK | C12-R3L62-247540 | Stage2-Risk-Counterexample | 2023-04-25 | 2023-04-25 | 253500 | C12-247540-20230425 | representative | current_profile_correct |
| C12-247540-20230726-4B | C12-R3L62-247540 | Stage4B-Overlay | 2023-07-26 | 2023-07-26 | 455000 | C12-247540-20230726 | 4B_overlay_only | current_profile_4B_too_late |

## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C12-066970-20230726-RISK | 263000 | 20.91% | -24.68% | 20.91% | -51.37% | 20.91% | -51.37% | 2023-07-26 | 318000 | -59.78% | risk_success; upside existed but drawdown dominated |
| C12-278280-20230425-RISK | 195000 | 5.38% | -7.64% | 7.44% | -29.90% | 7.44% | -57.54% | 2023-07-25 | 209500 | -60.48% | risk_success; customer/utilization risk should have blocked rerating |
| C12-247540-20230425-FALSE-RISK | 253500 | 11.44% | -14.79% | 130.37% | -14.79% | 130.37% | -26.00% | 2023-07-26 | 584000 | -67.88% | false_risk; early concentration risk alone would be too early |

### 4B overlay trigger

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C12-247540-20230726-4B | 455000 | 28.35% | -33.96% | 28.35% | -58.77% | 28.35% | -58.77% | 2023-07-26 | 584000 | -67.88% | good risk overlay only if paired with non-price evidence; price-only peak alone is not enough |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely treatment | actual OHLC result | verdict | interpretation |
|---|---|---|---|---|
| C12-R3L62-066970 | Stage2/Yellow promotion from sector orderbook/relative strength, 4B only after stronger non-price evidence | 90D MAE -51.37%; 180D MAE -51.37% | current_profile_4B_too_late | customer concentration + call-off risk needed earlier risk overlay once revision/margin bridge failed to close |
| C12-R3L62-278280 | weak Stage2 or watch, but not hard C12 risk | 90D MAE -29.90%; 180D MAE -57.54% | current_profile_missed_structural | utilization/customer pull-in risk should have blocked positive rerating despite battery-chain narrative |
| C12-R3L62-247540 | no hard C12 block in April unless non-price call-off evidence appears | 90D MFE +130.37% before later drawdown | current_profile_correct | customer concentration narrative alone must not block when delivery conversion/relative strength remain dominant |

Answers to v12 stress questions:

1. Current calibrated profile is broadly correct on price-only blowoff and non-price 4B requirement, but too slow for C12 when call-off risk is visible through margin/revision/utilization evidence.
2. Actual MFE/MAE alignment says C12 should be a risk overlay, not a generic bearish label.
3. Stage2 bonus is not the issue; C12 needs a negative/guard axis that can neutralize Stage2 when customers stop pulling volume.
4. Yellow 75 is acceptable globally, but C12 should require customer-quality support before Yellow promotion.
5. Green 87 / revision 55 is acceptable; C12 confirms that revision quality matters more than orderbook headline size.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened.
8. Hard 4C routing should remain strict; this loop supports earlier 4B risk overlay rather than careless hard 4C.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2/Actionable trigger | possible Green trigger | green_lateness_ratio | note |
|---|---|---|---:|---|
| C12-R3L62-066970 | 2023-07-26 risk-actionable | no clean Green after risk | not_applicable | C12 is a blocker/overlay, not a Green promotion axis |
| C12-R3L62-278280 | 2023-04-25 risk-actionable | no clean Green after risk | not_applicable | customer pull-in risk precedes later thesis deterioration |
| C12-R3L62-247540 | 2023-04-25 false-risk | 2023-07-26 blowoff/4B overlay | not_applicable | false-risk case shows why C12 must not be triggered by concentration narrative alone |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | stage2_actionable_entry | stage4b_entry | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| C12-247540-20230726-4B | 253500 | 455000 | 584000 | 584000 | 0.61 | 0.61 | price_only; positioning_overheat; valuation_blowoff | risk overlay useful, but full 4B requires non-price evidence; price-only alone can be too noisy |
| C12-066970-20230726-RISK | 263000 | 263000 | 318000 | 318000 | 0.00 | 0.00 | customer concentration; revision_slowdown; margin_or_backlog_slowdown | C12 is not a peak-timing label here; it is a drawdown-protection overlay |

## 16. 4C Protection Audit

No hard 4C trigger is promoted from this loop. C12 evidence usually begins as customer pull-in / utilization / margin bridge stress. It should become hard 4C only after explicit order cancellation, customer call-off confirmation, qualification failure, or thesis evidence break. The observed drawdowns support earlier 4B/risk protection, not a looser hard 4C rule.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_routing = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

### Rule S-L3-C12-01 — Battery customer pull-in risk overlay

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = customer_pull_in_calloff_risk_overlay
shadow_delta = +1 risk weight, not production
```

Candidate rule:

If a battery-chain company has customer concentration or large orderbook exposure, do not penalize it merely for concentration. Penalize only when at least two of the following are present near the trigger date:

```text
- revision_score weakens or consensus cannot support the orderbook narrative
- margin_bridge_score fails despite revenue/orderbook expansion
- utilization / inventory / customer pull-in proxy worsens
- customer_quality_score is narrow or single-customer dependent
- relative_strength_score breaks after a prior sector blowoff
```

Backtest reason: 066970 and 278280 show large negative MAE after risk trigger. 247540 shows that concentration narrative alone would have blocked a major move too early.

## 18. Canonical-Archetype Rule Candidate

### Rule C12-01 — Concentration is not call-off

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
new_axis_proposed = c12_concentration_requires_calloff_or_margin_confirmation
```

Mechanism:

A customer-concentrated battery orderbook is like a reservoir above the factory: the visible water level is large, but the scoring question is whether the valve is open. C12 should score the valve, not the reservoir. If customers keep pulling volume, concentration can amplify upside. If customer pull-in stalls, the same concentration compresses margins and breaks revisions.

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | current profile handles price-only blowoff but lacks C12 pull-in specificity | 3 | 52.91% | -32.02% | 52.91% | -44.97% | 0.33 | 2 | mixed; too slow on C12 risk-success cases |
| P0b_e2r_2_0_baseline_reference | rollback | older baseline overpromotes orderbook and relative strength | 3 | 52.91% | -32.02% | 52.91% | -44.97% | 0.33 | 2 | worse; cannot distinguish orderbook from pull-in |
| P1_L3_customer_pull_in_shadow | sector_specific | add L3 battery customer pull-in overlay | 3 | 52.91% | -32.02% | 52.91% | -44.97% | 0.00 | 0 | improved; avoids two late-risk misses without blocking 247540 early |
| P2_C12_concentration_requires_calloff | canonical_archetype_specific | concentration only counts when call-off/margin/revision evidence exists | 3 | 52.91% | -32.02% | 52.91% | -44.97% | 0.00 | 0 | best explanatory fit |
| P3_C12_counterexample_guard | guard | do not penalize concentration narrative alone | 3 | 52.91% | -32.02% | 52.91% | -44.97% | 0.00 | 1 | protects false-risk case; slightly weaker on early risk cases |

## 20. Score-Return Alignment Matrix

| case_id | raw component weakness | P0 score-return alignment | proposed alignment | verdict |
|---|---|---|---|---|
| C12-R3L62-066970 | customer_quality weak; revision/margin not closing; execution risk high | score stayed too constructive until drawdown evidence | earlier risk overlay neutralizes promotion | improved |
| C12-R3L62-278280 | margin bridge and utilization pull-in weak | risk not hard enough | blocks Stage3 promotion, flags failed rerating | improved |
| C12-R3L62-247540 | concentration narrative, but relative strength/orderbook conversion strong | correct if not over-penalized | counterexample guard preserves upside until non-price deterioration | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 2 | true | true | still needs C12 4C explicit cancellation/call-off cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
tested_existing_calibrated_axes: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [customer_pull_in_risk_too_late, concentration_false_alarm]
new_axis_proposed: [c12_concentration_requires_calloff_or_margin_confirmation, l3_customer_pull_in_calloff_risk_overlay]
existing_axis_strengthened: [full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C12 customer/call-off risk direct coverage gap in accessible search snapshot
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profile paths and corporate-action candidate windows
- entry_date and entry_price from tradable shards
- 30D / 90D / 180D MFE and MAE from actual stock-web OHLC rows
- representative-trigger dedupe logic
- C12-specific positive/counterexample balance
```

Not validated in this loop:

```text
- exact DART filing IDs or full analyst-report source parsing
- production score implementation details
- live candidate status
- current recommendation language
- broker/API execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_concentration_requires_calloff_or_margin_confirmation,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"customer concentration alone caused false-risk risk, but concentration+revision/margin/utilization stress caught drawdowns","reduced late-risk errors in 066970 and 278280 while preserving 247540 counterexample","C12-066970-20230726-RISK|C12-278280-20230425-RISK|C12-247540-20230425-FALSE-RISK",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,l3_customer_pull_in_calloff_risk_overlay,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"battery chain orderbook needs pull-in confirmation before rerating promotion","improves score-return alignment by converting two late-risk cases into risk overlay","C12-066970-20230726-RISK|C12-278280-20230425-RISK",2,2,0,low_to_medium,sector_shadow_only,"needs more explicit 4C/cancellation cases before production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C12-R3L62-066970","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"C12-066970-20230726-RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"risk overlay aligned with subsequent MAE","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Customer concentration/pull-in risk needed earlier overlay once margin and revision bridge failed to close."}
{"row_type":"case","case_id":"C12-R3L62-278280","symbol":"278280","company_name":"천보","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","case_type":"failed_rerating","positive_or_counterexample":"positive","best_trigger":"C12-278280-20230425-RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"risk overlay aligned with 90D/180D drawdown","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Electrolyte orderbook narrative failed to convert into margin/revision support."}
{"row_type":"case","case_id":"C12-R3L62-247540","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C12-247540-20230425-FALSE-RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"concentration-only risk would have been too early","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Customer concentration narrative alone was insufficient before the later July blowoff."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"C12-066970-20230726-RISK","case_id":"C12-R3L62-066970","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","sector":"battery_materials","primary_archetype":"customer_calloff_risk","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery","trigger_type":"Stage2-Risk-Actionable","trigger_date":"2023-07-26","evidence_available_at_that_date":"customer concentration plus call-off / margin bridge risk watch; conservative public-proxy evidence","evidence_source":"public filing/report proxy; price validated by stock-web","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route"],"stage3_evidence_fields":["confirmed_revision_weak_or_missing","margin_bridge_not_closed"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":263000,"MFE_30D_pct":20.91,"MFE_90D_pct":20.91,"MFE_180D_pct":20.91,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.68,"MAE_90D_pct":-51.37,"MAE_180D_pct":-51.37,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":318000,"drawdown_after_peak_pct":-59.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.0,"four_b_full_window_peak_proximity":0.0,"four_b_timing_verdict":"risk_overlay_not_peak_timing","four_b_evidence_type":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"risk_success_high_MAE","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-066970-20230726","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C12-278280-20230425-RISK","case_id":"C12-R3L62-278280","symbol":"278280","company_name":"천보","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","sector":"battery_materials","primary_archetype":"customer_calloff_risk","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery","trigger_type":"Stage2-Risk-Actionable","trigger_date":"2023-04-25","evidence_available_at_that_date":"utilization/customer pull-in risk and margin bridge weakness; conservative public-proxy evidence","evidence_source":"public filing/report proxy; price validated by stock-web","stage2_evidence_fields":["capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge_not_closed","financial_visibility_weak"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-25","entry_price":195000,"MFE_30D_pct":5.38,"MFE_90D_pct":7.44,"MFE_180D_pct":7.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.64,"MAE_90D_pct":-29.90,"MAE_180D_pct":-57.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-25","peak_price":209500,"drawdown_after_peak_pct":-60.48,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"risk_success_failed_rerating","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-278280-20230425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C12-247540-20230425-FALSE-RISK","case_id":"C12-R3L62-247540","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","sector":"battery_materials","primary_archetype":"customer_calloff_false_alarm","loop_objective":"counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Risk-Counterexample","trigger_date":"2023-04-25","evidence_available_at_that_date":"customer concentration narrative only; no sufficient call-off/margin break evidence","evidence_source":"public filing/report proxy; price validated by stock-web","stage2_evidence_fields":["customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-25","entry_price":253500,"MFE_30D_pct":11.44,"MFE_90D_pct":130.37,"MFE_180D_pct":130.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.79,"MAE_90D_pct":-14.79,"MAE_180D_pct":-26.00,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"early_C12_false_alarm","four_b_evidence_type":[],"four_c_protection_label":"false_break","trigger_outcome_label":"counterexample_false_risk","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-247540-20230425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C12-247540-20230726-4B","case_id":"C12-R3L62-247540","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_CUSTOMER_CONCENTRATION_CALLOFF_MARGIN_REVISION_RISK","sector":"battery_materials","primary_archetype":"4B_overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B-Overlay","trigger_date":"2023-07-26","evidence_available_at_that_date":"price blowoff plus positioning/valuation overheat; non-price evidence still required for full 4B","evidence_source":"stock-web price row plus conservative public-proxy evidence","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":455000,"MFE_30D_pct":28.35,"MFE_90D_pct":28.35,"MFE_180D_pct":28.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-33.96,"MAE_90D_pct":-58.77,"MAE_180D_pct":-58.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.61,"four_b_full_window_peak_proximity":0.61,"four_b_timing_verdict":"good_risk_overlay_but_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_after_counterexample","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C12-247540-20230726","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_case_new_trigger_family_4B_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L62-066970","trigger_id":"C12-066970-20230726-RISK","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":6,"backlog_visibility_score":6,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":7,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow-watch","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":5,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":3,"valuation_repricing_score":7,"execution_risk_score":9,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"customer_pull_in_calloff_risk_score":9},"weighted_score_after":68,"stage_label_after":"Stage2-Risk / 4B-watch","changed_components":["customer_quality_score","execution_risk_score","customer_pull_in_calloff_risk_score"],"component_delta_explanation":"C12 overlay discounts customer concentration once margin/revision bridge fails to close.","MFE_90D_pct":20.91,"MAE_90D_pct":-51.37,"score_return_alignment_label":"after_profile_better","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L62-278280","trigger_id":"C12-278280-20230425-RISK","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":4,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"customer_pull_in_calloff_risk_score":9},"weighted_score_after":56,"stage_label_after":"Stage2-Risk / failed-rerating","changed_components":["margin_bridge_score","revision_score","execution_risk_score","customer_pull_in_calloff_risk_score"],"component_delta_explanation":"Utilization/customer pull-in weakness prevents orderbook rerating despite sector narrative.","MFE_90D_pct":7.44,"MAE_90D_pct":-29.90,"score_return_alignment_label":"after_profile_better","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C12-R3L62-247540","trigger_id":"C12-247540-20230425-FALSE-RISK","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow / not Green","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":8,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":8,"customer_quality_score":5,"policy_or_regulatory_score":4,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"customer_pull_in_calloff_risk_score":2},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow / C12 guard not triggered","changed_components":["customer_pull_in_calloff_risk_score"],"component_delta_explanation":"Concentration narrative alone is not call-off evidence, so no negative C12 delta is applied.","MFE_90D_pct":130.37,"MAE_90D_pct":-14.79,"score_return_alignment_label":"guard_profile_better","current_profile_verdict":"current_profile_correct"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"62","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"avg=27.0; new canonical direct coverage; no repeated same symbol+trigger+entry group within C12","tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["customer_pull_in_risk_too_late","concentration_false_alarm"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C12 direct coverage gap"}
```

### 25.6 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"C12-FUTURE-EXPLICIT-CANCEL","symbol":"000000","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","reason":"explicit cancellation/call-off cases still needed for hard 4C calibration","price_source":"Songdaiki/stock-web","usage":"future_validation_needed"}
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
next_round = R3_loop_63_C13_BATTERY_JV_UTILIZATION_AMPC_IRA
carry_forward_gap = explicit C12 hard 4C cancellation / qualification failure cases still needed
preferred_next_case_mix = 2 positive risk-success + 1 false-risk + 1 explicit 4C if historical OHLC window is clean
```

## 28. Source Notes

Stock-Web files read or referenced:

```text
atlas/manifest.json
atlas/schema.json
atlas/universe/all_symbols.csv
atlas/symbol_profiles/066/066970.json
atlas/symbol_profiles/278/278280.json
atlas/symbol_profiles/247/247540.json
atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/278/278280/2023.csv
atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
```

Research artifact access used for duplicate avoidance only:

```text
data/e2r/calibration/md_registry.jsonl
repository search: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

No `src/e2r` code was opened or inferred. No production scoring was changed.
