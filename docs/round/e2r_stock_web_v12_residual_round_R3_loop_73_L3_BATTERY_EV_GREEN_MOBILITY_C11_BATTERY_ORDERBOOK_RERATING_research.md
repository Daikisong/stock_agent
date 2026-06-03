# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R3
scheduled_loop = 73
completed_round = R3
completed_loop = 73
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD
loop_objective = sector_specific_rule_discovery | canonical_archetype_compression | residual_false_positive_mining | residual_missed_structural_mining | 4B_non_price_requirement_stress_test | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING.

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

The tested residual is not the already-applied global rule that Stage2 can be earlier than Green. The narrower C11 question is whether battery long-term supply/orderbook evidence should split into two paths: (1) named customer + margin/customer/relative-strength bridge, and (2) contract-size or capacity narrative without ASP/utilization confirmation.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 73 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD |
| round_sector_consistency | pass |

R3 maps to L3_BATTERY_EV_GREEN_MOBILITY. The file therefore does not use R13 cross-archetype naming and does not jump to another round.

## 3. Previous Coverage / Duplicate Avoidance Check

The local v12 ledger already contained R3/Loop72 for C14_EV_DEMAND_SLOWDOWN_4B_4C and R9 mobility cases. This run avoids the prior C14 generic EV slowdown/call-off split and selects C11_BATTERY_ORDERBOOK_RERATING instead. It uses four new independent C11 trigger families:

| duplicate axis | status |
|---|---|
| same canonical + same symbol + same trigger date + same entry date | no conflict |
| same evidence family as R3 Loop72 C14 | no; this run is orderbook/rerating, not slowdown/4C |
| same round-sector pair | valid R3/L3 |
| new_symbol_count | 4 |
| same_archetype_new_symbol_count | 4 |
| same_archetype_new_trigger_family_count | 4 |

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_data_repo | Songdaiki/stock-web |
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

The schema confirms the tradable columns `d,o,h,l,c,v,a,mc,s,m`, and that MFE/MAE are calculated from max high/min low over tradable rows. The source remains raw/unadjusted marcap; corporate-action windows are blocked by default.

## 5. Historical Eligibility Gate

| symbol | company | profile path | corporate-action candidate status | forward 180D | calibration_usable |
|---|---|---|---|---:|---|
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | candidate dates 2015-05-04, 2021-02-03; no overlap with 2023 window | 180 | true |
| 348370 | 엔켐 | atlas/symbol_profiles/348/348370.json | no candidate dates | 180 | true |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | candidate dates 2022-06-27, 2022-07-15; no overlap with 2023-12 entry window | 180 | true |
| 393890 | 더블유씨피 | atlas/symbol_profiles/393/393890.json | no candidate dates | 180 | true |

## 6. Canonical Archetype Compression Map

| canonical | fine split | scoring implication |
|---|---|---|
| C11_BATTERY_ORDERBOOK_RERATING | named_customer_long_term_supply_orderbook | can promote Stage2-Actionable before full revision if customer, order size, delivery window and margin bridge cohere |
| C11_BATTERY_ORDERBOOK_RERATING | capacity_or_theme_orderbook_without_margin | should stay Stage2-watch or be blocked from Green when utilization/ASP/customer quality is unconfirmed |
| C11_BATTERY_ORDERBOOK_RERATING | successful_orderbook_4B_overlay | after successful rerating, 4B requires valuation/positioning evidence, not price-only peak detection |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | entry | entry_price | outcome |
|---|---|---|---|---|---|---:|---|
| R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS | 003670 | 포스코퓨처엠 | structural_success | positive | 2023-01-31 | 224,000 | structural_orderbook_rerating_success |
| R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS | 348370 | 엔켐 | high_mae_success | positive | 2024-01-10 | 88,200 | orderbook_policy_capacity_rerating_success |
| R3L73_C11_247540_20231204_ORDERBOOK_COUNTER | 247540 | 에코프로비엠 | failed_rerating | counterexample | 2023-12-04 | 323,000 | contract_size_false_positive_without_margin_bridge |
| R3L73_C11_393890_20240105_SEPARATOR_COUNTER | 393890 | 더블유씨피 | failed_rerating | counterexample | 2024-01-05 | 49,000 | capacity_orderbook_theme_failed_rerating |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 4 |
| representative_trigger_count | 4 |
| calibration_usable_trigger_count | 5 |

The positive side says that C11 can promote earlier than confirmed revision when customer/orderbook visibility is accompanied by margin, customer quality, policy or relative-strength evidence. The counterexample side says that contract size or capacity narrative alone can be a mirage: the orderbook headline may be real while the stock path behaves like a failed rerating because spread, utilization or customer concentration deteriorates.

## 9. Evidence Source Map

| symbol | trigger_date | evidence available at that date | tradable shard | profile path |
|---|---|---|---|---|
| 003670 | 2023-01-30 | Large cathode-material long-term supply/orderbook bridge moved from abstract EV demand to named customer, volume, and delivery visibility; the entry row is the next tradable close after the large contract/orderbook catalyst. | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | atlas/symbol_profiles/003/003670.json |
| 348370 | 2024-01-10 | Electrolyte supply-chain rerating and US/IRA localization narrative aligned with visible relative strength; the stock-web row shows the re-rating had already begun but the orderbook/capacity bridge was still ahead of confirmed revisions. | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | atlas/symbol_profiles/348/348370.json |
| 247540 | 2023-12-01 | Long-term supply contract/orderbook was visible, but it arrived after a prior sector blowoff and before the ASP/margin/utilization bridge repaired; the current profile can over-promote if contract size is scored without spread and demand guards. | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | atlas/symbol_profiles/247/247540.json |
| 393890 | 2024-01-05 | Separator capacity/orderbook narrative existed, but customer concentration, utilization and EV demand slowdown meant the evidence was not equivalent to a named high-quality orderbook rerating. | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | atlas/symbol_profiles/393/393890.json |

## 10. Price Data Source Map

| symbol | tradable shard | key stock-web rows checked |
|---|---|---|
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv | 2023-01-31 c=224000; 2023-07-26 h=694000 c=560000; 2023-10-31 low zone 232500 |
| 348370 | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | 2024-01-10 c=88200; 2024-04-08 h=394500; post-peak drawdown visible by 2024-07 |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv and 2024.csv | 2023-12-04 c=323000 h=354000; 2024-03/04 rebound failed; 2024 summer drawdown |
| 393890 | atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv | 2024-01-05 c=49000; 2024-01-08 h=49950; 2024-07-17 low zone 26600 |

## 11. Case-by-Case Trigger Grid

| symbol | company | trigger_type | trigger_date | entry_date | entry_price | Stage2 fields | Stage3 fields | current verdict |
|---|---|---|---|---|---:|---|---|---|
| 003670 | 포스코퓨처엠 | Stage2-Actionable | 2023-01-30 | 2023-01-31 | 224,000 | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility, durable_customer_confirmation | current_profile_missed_structural |
| 348370 | 엔켐 | Stage2-Actionable | 2024-01-10 | 2024-01-10 | 88,200 | public_event_or_disclosure, relative_strength, capacity_or_volume_route, policy_or_regulatory_optionality, backlog_or_delivery_visibility | multiple_public_sources, financial_visibility, durable_customer_confirmation | current_profile_too_late |
| 247540 | 에코프로비엠 | Stage2-Actionable/Orderbook-Without-Margin-Guard | 2023-12-01 | 2023-12-04 | 323,000 | public_event_or_disclosure, customer_or_order_quality, backlog_or_delivery_visibility | multiple_public_sources | current_profile_false_positive |
| 393890 | 더블유씨피 | Stage2-Theme/Capacity-Orderbook-Watch | 2024-01-05 | 2024-01-05 | 49,000 | public_event_or_disclosure, capacity_or_volume_route, backlog_or_delivery_visibility | - | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 003670 | 2023-01-31 | 224,000 | 22.77 | -5.58 | 88.62 | -5.58 | 209.82 | -5.58 | 2023-07-26 | 694,000 | -66.5 |
| 348370 | 2024-01-10 | 88,200 | 283.22 | -2.27 | 347.28 | -2.27 | 347.28 | -2.27 | 2024-04-08 | 394,500 | -54.75 |
| 247540 | 2023-12-04 | 323,000 | 9.6 | -13.0 | 9.6 | -34.67 | 9.6 | -53.97 | 2023-12-04 | 354,000 | -58.0 |
| 393890 | 2024-01-05 | 49,000 | 1.94 | -21.84 | 1.94 | -38.78 | 1.94 | -45.71 | 2024-01-08 | 49,950 | -46.75 |
| 003670 4B | 2023-07-26 | 560,000 | 23.93 | -28.75 | 23.93 | -58.48 | 23.93 | -58.48 | 2023-07-26 | 694,000 | -66.5 |

## 13. Current Calibrated Profile Stress Test

| symbol | company | current_profile_verdict | Stage2 bonus test | Yellow 75 test | Green 87/rev55 test | 4B/4C test |
|---|---|---|---|---|---|---|
| 003670 | 포스코퓨처엠 | current_profile_missed_structural | Stage2 bonus insufficient | Yellow 75 too strict | Green 87/rev55 too late for early orderbook | 4B/4C note: not_applicable / not_applicable |
| 348370 | 엔켐 | current_profile_too_late | Stage2 bonus insufficient | Yellow 75 too strict | Green 87/rev55 too late for early orderbook | 4B/4C note: good_full_window_4B_timing_if_non_price_overheat_present / thesis_break_watch_only |
| 247540 | 에코프로비엠 | current_profile_false_positive | Stage2 bonus too strong without guard | Yellow 75 too loose without margin guard | Green 87/rev55 must stay blocked | 4B/4C note: good_full_window_4B_timing_with_non_price_margin_guard / hard_4c_success_after_margin_bridge_break |
| 393890 | 더블유씨피 | current_profile_false_positive | Stage2 bonus too strong without guard | Yellow 75 too loose without margin guard | Green 87/rev55 must stay blocked | 4B/4C note: early_warning_not_full_4B_until_utilization_margin_evidence / hard_4c_success_after_utilization_break |

Result: current_profile_error_count = 4. The profile is directionally correct on global anti-price-only axes, but C11 needs a narrower orderbook-quality split.

## 14. Stage2 / Yellow / Green Comparison

| symbol | Stage2/Actionable entry | plausible Green trigger | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| 003670 | 2023-01-31 c=224000 | after confirmed revision / market consensus catch-up near March-April | 0.22 | Green not catastrophically late, but Stage2-Actionable captured most of the structural move |
| 348370 | 2024-01-10 c=88200 | after the price already repriced through February/March | 0.41 | Green was materially late; C11+policy+RS bridge matters |
| 247540 | 2023-12-04 c=323000 | no clean Green; margin bridge never repaired in window | not_applicable | contract headline should not force Green |
| 393890 | 2024-01-05 c=49000 | no clean Green; capacity narrative failed | not_applicable | orderbook/capacity theme remains watch-only |

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| 003670 representative | not_applicable | not_applicable | entry was Stage2/Actionable, not 4B |
| 003670 4B overlay | 0.715 | 0.715 | good_full_window_4B_timing with valuation/positioning evidence |
| 348370 | 0.86 | 0.86 | good_full_window_4B_timing_if_non_price_overheat_present |
| 247540 | 0.98 | 0.98 | full 4B/4C guard should block positive rerating because non-price margin/ASP evidence was weak |
| 393890 | 0.30 | 0.30 | early warning, but full positive block needs utilization/margin evidence |

## 16. 4C Protection Audit

| symbol | protection label | interpretation |
|---|---|---|
| 003670 | thesis_break_watch_only | 4B overlay was enough near the peak; hard 4C was not the Stage2 decision |
| 348370 | thesis_break_watch_only | successful rerating later needed overheat watch, not immediate thesis break |
| 247540 | hard_4c_success_after_margin_bridge_break | contract-size false positive was protected only after margin/ASP thesis break was visible |
| 393890 | hard_4c_success_after_utilization_break | capacity/orderbook theme should not remain Stage2-Actionable after utilization/demand evidence weakened |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = C11_battery_orderbook_quality_split
candidate = named_customer_orderbook_margin_customer_quality_bonus + capacity_theme_without_margin_stage_cap
```

Battery orderbook rerating behaves like a warehouse full of purchase orders: if the boxes have customer names, delivery dates, margin labels and utilization routes, the warehouse is valuable. If the boxes only say “future capacity” or “large contract” while ASP and utilization are leaking, the same warehouse becomes inventory risk.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
positive_condition = named_customer_or_order_quality + backlog_visibility + margin_or_ASP_bridge + relative_strength_or_policy_capacity_route
negative_guard = contract_size_without_margin_bridge OR capacity_theme_without_utilization OR post_blowoff_orderbook_without_customer_quality
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | avg_green_lateness_ratio | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current proxy | keeps global Stage2/4B/4C axes without C11-specific orderbook guard | none | 4 | 003670,348370,247540,393890 | 111.86 | -20.32 | 142.16 | -26.88 | 0.50 | 1 | 0.50 | 0.38 | mixed |
| P0b e2r_2_0_baseline_reference | rollback reference | lower Stage2/looser Green; over-accepts contract-size without guard | rollback only | 4 | same | 111.86 | -20.32 | 142.16 | -26.88 | 0.50 | 1 | 0.50 | 0.38 | weaker |
| P1 sector_specific_candidate_profile | sector_specific | battery orderbook needs margin/customer/utilization confirmation | +C11_orderbook_margin_customer_guard | 4 | 003670,348370 positive; 247540/393890 blocked | 217.95 | -3.92 | 278.55 | -3.92 | 0.00 | 0 | 0.50 | 0.38 | improved |
| P2 canonical_archetype_candidate_profile | canonical_archetype_specific | promote named customer/orderbook + relative strength + margin bridge; cap capacity-theme only | +named_orderbook_bonus/+capacity_theme_cap | 4 | same as P1 | 217.95 | -3.92 | 278.55 | -3.92 | 0.00 | 0 | 0.50 | 0.38 | best |
| P3 counterexample_guard_profile | guard | contract size alone cannot override ASP/utilization/positioning risk | orderbook_without_margin_stage_cap | 2 | 247540,393890 blocked | 5.77 | -36.73 | 5.77 | -49.84 | 0.00 | 0 | 0.50 | 0.38 | guardrail |

## 20. Score-Return Alignment Matrix

| symbol | current_profile_verdict | MFE_90D | MAE_90D | MFE_180D | MAE_180D | alignment | residual |
|---|---|---:|---:|---:|---:|---|---|
| 003670 | current_profile_missed_structural | 88.62 | -5.58 | 209.82 | -5.58 | aligned | C11 needs a named customer/orderbook bridge bonus because the current calibrated proxy can under-score pre-revision long-term cathode supply visibility. |
| 348370 | current_profile_too_late | 347.28 | -2.27 | 347.28 | -2.27 | aligned | C11 should allow earlier Stage2-Actionable when capacity route + policy localization + relative strength cohere before full earnings revision. |
| 247540 | current_profile_false_positive | 9.6 | -34.67 | 9.6 | -53.97 | guardrail_needed | C11 must subtract when orderbook evidence lacks ASP, margin, utilization, or demand call-off confirmation after a prior sector blowoff. |
| 393890 | current_profile_false_positive | 1.94 | -38.78 | 1.94 | -45.71 | guardrail_needed | C11 must distinguish supply-chain capacity narrative from customer-confirmed orderbook rerating. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD | 2 | 2 | 2 | 2 | 4 | 0 | 5 | 4 | 4 | true | true | C11 now has balanced orderbook-success and orderbook-false-positive coverage; more holdout cases needed for global promotion |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: orderbook_contract_size_false_positive_without_margin_bridge, orderbook_capacity_theme_false_positive, missed_structural_orderbook_before_revision, 4B_overlay_after_successful_orderbook_rerating
new_axis_proposed: C11_named_customer_orderbook_margin_bridge_bonus; C11_contract_size_without_margin_utilization_stage_cap
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical trigger dates only.
- Songdaiki/stock-web tradable raw OHLC rows only.
- Entry date / entry price / MFE / MAE / peak / drawdown calculated on raw unadjusted marcap basis.
- Corporate-action candidate windows checked against symbol profiles.
- Same-entry dedupe applied: four representative rows count in aggregate; the 003670 4B overlay is overlay-only.

Not validated:

- Production `stock_agent` code paths.
- Live candidate discovery or current recommendation.
- Broker/API execution.
- Exact intraday disclosure timing beyond next-tradable-close rule.
- Whether these shadow rows should be promoted globally.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_named_customer_orderbook_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Named customer/orderbook plus margin/customer/relative-strength bridge captured 003670 and 348370 before full revisions","improves missed-structural timing while retaining non-price evidence requirement",TRG_003670_20230131_STRUCTURAL_SUCCESS|TRG_348370_20240110_HIGH_MAE_SUCCESS,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_contract_size_without_margin_utilization_stage_cap,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"Large contract/capacity headline without ASP/utilization/customer quality produced 247540 and 393890 false positives","reduces false-positive contract-size rerating",TRG_247540_20231204_FAILED_RERATING|TRG_393890_20240105_FAILED_RERATING,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C11_successful_rerating_4B_non_price_overlay,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"After successful C11 rerating, 4B needs valuation/positioning evidence near full-window peak","keeps price-only blowoff guard but allows good full-window 4B timing",TRG_003670_20230726_4B_OVERLAY,4,4,2,low_to_medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "C11 needs a named customer/orderbook bridge bonus because the current calibrated proxy can under-score pre-revision long-term cathode supply visibility."}
{"row_type": "trigger", "trigger_id": "TRG_003670_20230131_STRUCTURAL_SUCCESS", "case_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "battery long-term supply orderbook rerating with margin/customer guard", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-01-30", "entry_date": "2023-01-31", "entry_price": 224000, "evidence_available_at_that_date": "Large cathode-material long-term supply/orderbook bridge moved from abstract EV demand to named customer, volume, and delivery visibility; the entry row is the next tradable close after the large contract/orderbook catalyst.", "evidence_source": "historical disclosure/news narrative cross-checked against stock-web price rows; see Source Notes", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.77, "MFE_90D_pct": 88.62, "MFE_180D_pct": 209.82, "MFE_1Y_pct": 209.82, "MFE_2Y_pct": null, "MAE_30D_pct": -5.58, "MAE_90D_pct": -5.58, "MAE_180D_pct": -5.58, "MAE_1Y_pct": -66.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": 0.22, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_orderbook_rerating_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS", "trigger_id": "TRG_003670_20230131_STRUCTURAL_SUCCESS", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 75, "backlog_visibility_score": 70, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 50, "customer_quality_score": 65, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 55, "asp_or_spread_score": 45, "utilization_score": 40, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Actionable", "raw_component_scores_after": {"contract_score": 85, "backlog_visibility_score": 82, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 75, "policy_or_regulatory_score": 15, "valuation_repricing_score": 50, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 65, "asp_or_spread_score": 55, "utilization_score": 48, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green-candidate", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 88.62, "MAE_90D_pct": -5.58, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "case", "case_id": "R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "C11 should allow earlier Stage2-Actionable when capacity route + policy localization + relative strength cohere before full earnings revision."}
{"row_type": "trigger", "trigger_id": "TRG_348370_20240110_HIGH_MAE_SUCCESS", "case_id": "R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS", "symbol": "348370", "company_name": "엔켐", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "battery long-term supply orderbook rerating with margin/customer guard", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 88200, "evidence_available_at_that_date": "Electrolyte supply-chain rerating and US/IRA localization narrative aligned with visible relative strength; the stock-web row shows the re-rating had already begun but the orderbook/capacity bridge was still ahead of confirmed revisions.", "evidence_source": "historical disclosure/news narrative cross-checked against stock-web price rows; see Source Notes", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route", "policy_or_regulatory_optionality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv", "profile_path": "atlas/symbol_profiles/348/348370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 283.22, "MFE_90D_pct": 347.28, "MFE_180D_pct": 347.28, "MFE_1Y_pct": 347.28, "MFE_2Y_pct": null, "MAE_30D_pct": -2.27, "MAE_90D_pct": -2.27, "MAE_180D_pct": -2.27, "MAE_1Y_pct": -10.2, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-04-08", "peak_price": 394500, "drawdown_after_peak_pct": -54.75, "green_lateness_ratio": 0.41, "four_b_local_peak_proximity": 0.86, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "good_full_window_4B_timing_if_non_price_overheat_present", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "orderbook_policy_capacity_rerating_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS", "trigger_id": "TRG_348370_20240110_HIGH_MAE_SUCCESS", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 25, "relative_strength_score": 80, "customer_quality_score": 50, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 70, "asp_or_spread_score": 40, "utilization_score": 35, "positioning_overheat_score": 25, "thesis_break_score": 0}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow/Actionable", "raw_component_scores_after": {"contract_score": 67, "backlog_visibility_score": 62, "margin_bridge_score": 38, "revision_score": 35, "relative_strength_score": 84, "customer_quality_score": 58, "policy_or_regulatory_score": 78, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 78, "asp_or_spread_score": 47, "utilization_score": 42, "positioning_overheat_score": 35, "thesis_break_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-candidate/4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 347.28, "MAE_90D_pct": -2.27, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "case", "case_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Actionable/Orderbook-Without-Margin-Guard", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C11 must subtract when orderbook evidence lacks ASP, margin, utilization, or demand call-off confirmation after a prior sector blowoff."}
{"row_type": "trigger", "trigger_id": "TRG_247540_20231204_FAILED_RERATING", "case_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER", "symbol": "247540", "company_name": "에코프로비엠", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "battery long-term supply orderbook rerating with margin/customer guard", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Actionable/Orderbook-Without-Margin-Guard", "trigger_date": "2023-12-01", "entry_date": "2023-12-04", "entry_price": 323000, "evidence_available_at_that_date": "Long-term supply contract/orderbook was visible, but it arrived after a prior sector blowoff and before the ASP/margin/utilization bridge repaired; the current profile can over-promote if contract size is scored without spread and demand guards.", "evidence_source": "historical disclosure/news narrative cross-checked against stock-web price rows; see Source Notes", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv", "profile_path": "atlas/symbol_profiles/247/247540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.6, "MFE_90D_pct": 9.6, "MFE_180D_pct": 9.6, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.0, "MAE_90D_pct": -34.67, "MAE_180D_pct": -53.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-12-04", "peak_price": 354000, "drawdown_after_peak_pct": -58.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_full_window_4B_timing_with_non_price_margin_guard", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success_after_margin_bridge_break", "trigger_outcome_label": "contract_size_false_positive_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER", "trigger_id": "TRG_247540_20231204_FAILED_RERATING", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 82, "backlog_visibility_score": 85, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 25, "customer_quality_score": 65, "policy_or_regulatory_score": 35, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 60, "asp_or_spread_score": 20, "utilization_score": 25, "positioning_overheat_score": 75, "thesis_break_score": 35}, "weighted_score_before": 83, "stage_label_before": "Stage3-Green-false-positive-risk", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 65, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 50, "asp_or_spread_score": 10, "utilization_score": 20, "positioning_overheat_score": 85, "thesis_break_score": 65}, "weighted_score_after": 70, "stage_label_after": "Stage4B/4C-watch-positive-blocked", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R3L73_C11_393890_20240105_SEPARATOR_COUNTER", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-Theme/Capacity-Orderbook-Watch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C11 must distinguish supply-chain capacity narrative from customer-confirmed orderbook rerating."}
{"row_type": "trigger", "trigger_id": "TRG_393890_20240105_FAILED_RERATING", "case_id": "R3L73_C11_393890_20240105_SEPARATOR_COUNTER", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "battery long-term supply orderbook rerating with margin/customer guard", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|residual_false_positive_mining|residual_missed_structural_mining|4B_non_price_requirement_stress_test|coverage_gap_fill", "trigger_type": "Stage2-Theme/Capacity-Orderbook-Watch", "trigger_date": "2024-01-05", "entry_date": "2024-01-05", "entry_price": 49000, "evidence_available_at_that_date": "Separator capacity/orderbook narrative existed, but customer concentration, utilization and EV demand slowdown meant the evidence was not equivalent to a named high-quality orderbook rerating.", "evidence_source": "historical disclosure/news narrative cross-checked against stock-web price rows; see Source Notes", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "backlog_or_delivery_visibility"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.94, "MFE_90D_pct": 1.94, "MFE_180D_pct": 1.94, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -21.84, "MAE_90D_pct": -38.78, "MAE_180D_pct": -45.71, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-08", "peak_price": 49950, "drawdown_after_peak_pct": -46.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "early_warning_not_full_4B_until_utilization_margin_evidence", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success_after_utilization_break", "trigger_outcome_label": "capacity_orderbook_theme_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L73_C11_393890_20240105_SEPARATOR_COUNTER_EG", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_393890_20240105_SEPARATOR_COUNTER", "trigger_id": "TRG_393890_20240105_FAILED_RERATING", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 15, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 25, "policy_or_regulatory_score": 35, "valuation_repricing_score": 20, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 55, "asp_or_spread_score": 10, "utilization_score": 15, "positioning_overheat_score": 35, "thesis_break_score": 25}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable-false-positive-risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 20, "policy_or_regulatory_score": 30, "valuation_repricing_score": 15, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 45, "asp_or_spread_score": 5, "utilization_score": 10, "positioning_overheat_score": 45, "thesis_break_score": 60}, "weighted_score_after": 62, "stage_label_after": "Stage2-watch/positive-blocked", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 1.94, "MAE_90D_pct": -38.78, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "trigger", "trigger_id": "TRG_003670_20230726_4B_OVERLAY", "case_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS", "symbol": "003670", "company_name": "포스코퓨처엠", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_LONG_TERM_SUPPLY_ORDERBOOK_RERATING_WITH_MARGIN_AND_CUSTOMER_GUARD", "sector": "battery_ev_green_mobility", "primary_archetype": "C11 successful rerating risk overlay", "loop_objective": "4B_non_price_requirement_stress_test|sector_specific_rule_discovery", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 560000, "evidence_available_at_that_date": "After the successful C11 rerating, price/valuation and positioning reached a peak-zone; because the 4B overlay has non-price valuation/positioning evidence, it is not treated as price-only.", "evidence_source": "stock-web observed peak zone plus valuation/positioning non-price overlay narrative", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv", "profile_path": "atlas/symbol_profiles/003/003670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.93, "MFE_90D_pct": 23.93, "MFE_180D_pct": 23.93, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -28.75, "MAE_90D_pct": -58.48, "MAE_180D_pct": -58.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 694000, "drawdown_after_peak_pct": -66.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.715, "four_b_full_window_peak_proximity": 0.715, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_after_successful_C11_rerating", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L73_C11_003670_20230726_4B_EG", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same case as representative; overlay row for 4B timing audit only", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "residual_contribution", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["orderbook_contract_size_false_positive_without_margin_bridge", "orderbook_capacity_theme_false_positive", "missed_structural_orderbook_before_revision", "4B_overlay_after_successful_orderbook_rerating"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### Score Simulation Rows Only

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_003670_20230131_ORDERBOOK_SUCCESS", "trigger_id": "TRG_003670_20230131_STRUCTURAL_SUCCESS", "symbol": "003670", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 75, "backlog_visibility_score": 70, "margin_bridge_score": 45, "revision_score": 35, "relative_strength_score": 50, "customer_quality_score": 65, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 55, "asp_or_spread_score": 45, "utilization_score": 40, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow/Actionable", "raw_component_scores_after": {"contract_score": 85, "backlog_visibility_score": 82, "margin_bridge_score": 55, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 75, "policy_or_regulatory_score": 15, "valuation_repricing_score": 50, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 65, "asp_or_spread_score": 55, "utilization_score": 48, "positioning_overheat_score": 10, "thesis_break_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green-candidate", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 88.62, "MAE_90D_pct": -5.58, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_348370_20240110_ORDERBOOK_RS_SUCCESS", "trigger_id": "TRG_348370_20240110_HIGH_MAE_SUCCESS", "symbol": "348370", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 60, "backlog_visibility_score": 55, "margin_bridge_score": 30, "revision_score": 25, "relative_strength_score": 80, "customer_quality_score": 50, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 70, "asp_or_spread_score": 40, "utilization_score": 35, "positioning_overheat_score": 25, "thesis_break_score": 0}, "weighted_score_before": 81, "stage_label_before": "Stage3-Yellow/Actionable", "raw_component_scores_after": {"contract_score": 67, "backlog_visibility_score": 62, "margin_bridge_score": 38, "revision_score": 35, "relative_strength_score": 84, "customer_quality_score": 58, "policy_or_regulatory_score": 78, "valuation_repricing_score": 60, "execution_risk_score": 35, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 78, "asp_or_spread_score": 47, "utilization_score": 42, "positioning_overheat_score": 35, "thesis_break_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green-candidate/4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 347.28, "MAE_90D_pct": -2.27, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_247540_20231204_ORDERBOOK_COUNTER", "trigger_id": "TRG_247540_20231204_FAILED_RERATING", "symbol": "247540", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 82, "backlog_visibility_score": 85, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 25, "customer_quality_score": 65, "policy_or_regulatory_score": 35, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 60, "asp_or_spread_score": 20, "utilization_score": 25, "positioning_overheat_score": 75, "thesis_break_score": 35}, "weighted_score_before": 83, "stage_label_before": "Stage3-Green-false-positive-risk", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 65, "margin_bridge_score": 15, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 55, "policy_or_regulatory_score": 30, "valuation_repricing_score": 55, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 50, "asp_or_spread_score": 10, "utilization_score": 20, "positioning_overheat_score": 85, "thesis_break_score": 65}, "weighted_score_after": 70, "stage_label_after": "Stage4B/4C-watch-positive-blocked", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 9.6, "MAE_90D_pct": -34.67, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73_C11_393890_20240105_SEPARATOR_COUNTER", "trigger_id": "TRG_393890_20240105_FAILED_RERATING", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 50, "backlog_visibility_score": 45, "margin_bridge_score": 15, "revision_score": 10, "relative_strength_score": 30, "customer_quality_score": 25, "policy_or_regulatory_score": 35, "valuation_repricing_score": 20, "execution_risk_score": 50, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 55, "asp_or_spread_score": 10, "utilization_score": 15, "positioning_overheat_score": 35, "thesis_break_score": 25}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable-false-positive-risk", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 30, "margin_bridge_score": 10, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 20, "policy_or_regulatory_score": 30, "valuation_repricing_score": 15, "execution_risk_score": 70, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 45, "asp_or_spread_score": 5, "utilization_score": 10, "positioning_overheat_score": 45, "thesis_break_score": 60}, "weighted_score_after": 62, "stage_label_after": "Stage2-watch/positive-blocked", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "asp_or_spread_score", "utilization_score", "positioning_overheat_score", "thesis_break_score"], "component_delta_explanation": "C11 shadow split promotes named customer/orderbook with margin/customer quality, but caps contract-size-only or capacity-theme rerating when spread/utilization/relative strength are weak.", "MFE_90D_pct": 1.94, "MAE_90D_pct": -38.78, "score_return_alignment_label": "guardrail_needed", "current_profile_verdict": "current_profile_false_positive"}
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
completed_round = R3
completed_loop = 73
next_round = R4
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest confirmed max_date = 2026-02-20; price basis = tradable_raw; adjustment status = raw_unadjusted_marcap.
- Schema confirms tradable shard columns d,o,h,l,c,v,a,mc,s,m and MFE/MAE max-high/min-low calculation.
- 003670 profile: active-like; corporate-action candidate dates 2015-05-04 and 2021-02-03; no 2023 entry-window contamination.
- 348370 profile: active-like; corporate-action candidate_count = 0.
- 247540 profile: active-like; corporate-action candidate dates 2022-06-27 and 2022-07-15; no 2023-12 entry-window contamination.
- 393890 profile: active-like; corporate-action candidate_count = 0.
- This MD is shadow-only research and contains no investment recommendation.

