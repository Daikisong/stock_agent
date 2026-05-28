# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R3
loop = 11
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN
output_file = e2r_stock_web_v12_residual_round_R3_loop_11_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not live candidate discovery, not an investment recommendation, not a repository patch, and not a production scoring change.

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

Existing global axes are treated as already applied. This loop does not re-propose them globally. It stress-tests the C11 battery orderbook/capacity branch and proposes only sector/canonical shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R3 |
| loop | 11 |
| sector | 2차전지·전기차·친환경 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN |
| loop_objective | counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test; sector_specific_rule_discovery; canonical_archetype_compression; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

The accessible calibration summary showed all R1~R13 sectors and loops 1~9 already ingested, with 1,376 aggregate representative trigger rows. The applied global axes are already calibrated and therefore are not re-proposed here. This loop adds a same-sector holdout for R3 rather than repeating R1/R2 HBM, defense, or grid cases.

```text
auto_selected_coverage_gap = R3/C11 battery orderbook rerating residual after R1/R2-heavy calibration
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = blocked
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

Novelty logic:
- 엔켐 is used as a capacity/orderbook success with extreme MFE but heavy post-peak drawdown.
- LG에너지솔루션 is used as an AMPC/JV support case where the current profile can become too early if utilization/revision is not closed.
- 에코프로비엠 is used as the cathode orderbook/call-off false-Green counterexample.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream source | FinanceData/marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| stock_web_manifest_max_date | 2026-02-20 |
| validation_status | usable_for_historical_calibration |

Manifest-level fields checked: source_name, source_repo_url, min_date, max_date, tradable_row_count, raw_row_count, symbol_count, active_like_symbol_count, inactive_or_delisted_like_symbol_count, markets, calibration_shard_root, raw_shard_root, schema_path, universe_path.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | entry rows present | 180D forward window | corporate action overlap in 180D | calibration_usable |
|---|---|---|---|---|---|---|
| 348370 | 엔켐 | atlas/symbol_profiles/348/348370.json | yes | yes | no | true |
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | yes | yes | no | true |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | yes | yes | no; profile corporate-action dates are 2022 only | true |

All quantitative rows use tradable shards only. Raw shards are not used for calibration weights.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression reason |
|---|---|---|
| electrolyte capacity/orderbook rerating | C11_BATTERY_ORDERBOOK_RERATING | capacity/orderbook bridge can create early rerating when customer conversion is credible |
| AMPC/JV policy support without utilization closure | C11_BATTERY_ORDERBOOK_RERATING | policy support is not a standalone Green; it must connect to utilization/revision |
| cathode call-off / margin slowdown false Green | C11_BATTERY_ORDERBOOK_RERATING | same C11 orderbook language can fail if delivery visibility breaks |

## 7. Case Selection Summary

| case_id | symbol | company | role | best trigger | reason selected |
|---|---|---|---|---|---|
| R3L11_C11_348370_ENCHEM | 348370 | 엔켐 | structural_success | 2024-01-08 Stage2-Actionable | capacity/orderbook route generated very high MFE; useful positive with high drawdown guard |
| R3L11_C11_373220_LGES | 373220 | LG에너지솔루션 | failed_rerating | 2024-04-26 Stage2-Actionable | AMPC/JV support existed but utilization/revision did not justify clean Green |
| R3L11_C11_247540_ECOPROBM | 247540 | 에코프로비엠 | false_positive_green | 2024-01-05 Stage2-Actionable | cathode orderbook narrative failed as call-off/margin slowdown dominated |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive_structural_success | 1 | 엔켐 |
| counterexample_or_failed_rerating | 2 | LG에너지솔루션, 에코프로비엠 |
| 4B_or_4C_case | 2 | 엔켐 4B-watch, 에코프로비엠 4C |
| calibration_usable_case_count | 3 | all representative cases |

This loop is intentionally guard-heavy. It does not claim a broad positive battery rule. It proposes a C11-specific split: capacity/orderbook can promote Stage2/Yellow, but Green requires realized utilization, revision, customer conversion, or margin bridge.

## 9. Evidence Source Map

| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 엔켐 | capacity_or_volume_route; customer_or_order_quality; relative_strength | financial_visibility partial | valuation_blowoff; positioning_overheat | watch only |
| LG에너지솔루션 | policy_or_regulatory_optionality; capacity_or_volume_route | not confirmed at trigger | margin_or_backlog_slowdown; revision_slowdown | false_break / watch |
| 에코프로비엠 | backlog_or_delivery_visibility; relative_strength | not confirmed at trigger | contract_delay; margin_or_backlog_slowdown | call_off_or_order_cut; thesis_evidence_broken |

## 10. Price Data Source Map

| symbol | shard_path | profile_path | clean 180D window |
|---|---|---|---|
| 348370 | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | atlas/symbol_profiles/348/348370.json | true |
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | atlas/symbol_profiles/373/373220.json | true |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | atlas/symbol_profiles/247/247540.json | true |

## 11. Case-by-Case Trigger Grid

| trigger_id | case | trigger_type | trigger_date | entry_date | entry_price | evidence summary | aggregate role |
|---|---|---|---|---|---:|---|---|
| R3L11_C11_348370_S2_2024-01-08 | 엔켐 | Stage2-Actionable | 2024-01-08 | 2024-01-08 | 84,300 | capacity/orderbook + relative strength before blowoff | representative |
| R3L11_C11_348370_4B_2024-04-08 | 엔켐 | 4B-Watch | 2024-04-08 | 2024-04-08 | 358,000 | valuation/positioning near peak | 4B_overlay_only |
| R3L11_C11_373220_S2_2024-04-26 | LG에너지솔루션 | Stage2-Actionable | 2024-04-26 | 2024-04-26 | 372,000 | AMPC/JV support, but weak utilization/revision bridge | representative |
| R3L11_C11_247540_S2_2024-01-05 | 에코프로비엠 | Stage2-Actionable | 2024-01-05 | 2024-01-05 | 315,000 | orderbook/rebound narrative without delivery conversion | representative |
| R3L11_C11_247540_4C_2024-06-24 | 에코프로비엠 | 4C | 2024-06-24 | 2024-06-24 | 182,100 | call-off/margin deterioration protection row | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative aggregate triggers

| case | entry | entry_price | peak_date | peak_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | drawdown_after_peak | outcome |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 엔켐 | 2024-01-08 | 84,300 | 2024-04-08 | 394,500 | 300.95 | 368.09 | 368.09 | -1.66 | -1.66 | -1.66 | -70.22 | structural success but needs 4B/watch |
| LG에너지솔루션 | 2024-04-26 | 372,000 | 2024-10-08 | 444,000 | 6.72 | 15.59 | 19.35 | -12.37 | -16.40 | -16.40 | -22.64 | partial rebound, not clean Green |
| 에코프로비엠 | 2024-01-05 | 315,000 | 2024-01-08 | 323,000 | 2.54 | 2.54 | 2.54 | -32.22 | -40.48 | -66.98 | -66.98 | false Green / hard 4C protected |

### 12.2 Overlay / protection triggers

| case | trigger | entry | entry_price | MFE90 | MAE90 | overlay verdict |
|---|---|---|---:|---:|---:|---|
| 엔켐 | 4B-Watch | 2024-04-08 | 358,000 | 10.20 | -58.35 | valuation/positioning watch was needed, not a positive entry row |
| 에코프로비엠 | 4C | 2024-06-24 | 182,100 | 10.93 | -35.48 | thesis-break row protects against continued positive training |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | profile verdict | axis tested |
|---|---|---|---|---|
| 엔켐 | Stage2/Yellow first, 4B-watch after blowoff | 368.09% MFE180, then -70.22% post-peak drawdown | current_profile_correct | stage2 bonus kept; 4B non-price guard kept |
| LG에너지솔루션 | Could over-promote AMPC/JV support as Green | only 19.35% MFE180 with -16.40% MAE180 | current_profile_too_early | C11 Green requires utilization/revision bridge |
| 에코프로비엠 | Could treat orderbook narrative as rerating | 2.54% MFE180 vs -66.98% MAE180 | current_profile_false_positive | C11 call-off/margin 4C guard needed |

Required stress-test answers:
1. Current calibrated profile handles Stage2 better than old baseline, but C11 still needs a branch that separates electrolyte capacity conversion from cathode call-off risk.
2. The judgment matches 엔켐 but is too early for LG에너지솔루션 and false-positive for 에코프로비엠.
3. Stage2 bonus is not excessive if non-price capacity/orderbook evidence is clean; it is excessive if the only bridge is policy/orderbook headline.
4. Yellow 75 remains useful as a staging label.
5. Green 87 / revision 55 should be strengthened only inside C11 for orderbook/capacity names without realized utilization/revision.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate; 엔켐 needed 4B/watch after valuation/positioning evidence, not a price-only label.
8. Hard 4C routing is appropriate for 에코프로비엠 because deterioration evidence, not price alone, broke the positive thesis.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 엔켐 | 84,300 | no clean Green row used | 394,500 | not_applicable | Stage2 was the useful signal; Green would mostly chase a blowoff |
| LG에너지솔루션 | 372,000 | not valid Green | 444,000 | not_applicable | AMPC/JV bridge supported watch but did not justify clean Green |
| 에코프로비엠 | 315,000 | not valid Green | 323,000 | not_applicable | Green should be capped by call-off/margin deterioration |

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | full observed peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---|---|
| 엔켐 | 394,500 | 394,500 | 0.88 | 0.88 | valuation_blowoff; positioning_overheat; price_only | good 4B-watch, not a positive entry row |
| LG에너지솔루션 | 444,000 | 444,000 | 0.42 | 0.42 | revision_slowdown; margin_or_backlog_slowdown | not full 4B; Stage2 watch with Green cap |
| 에코프로비엠 | 323,000 | 323,000 | 0.03 | 0.03 | margin_or_backlog_slowdown; contract_delay | early local 4B is less useful than later 4C deterioration |

## 16. 4C Protection Audit

| case | 4C label | reason |
|---|---|---|
| 엔켐 | thesis_break_watch_only | drawdown is severe but this research row uses 4B/watch rather than hard 4C |
| LG에너지솔루션 | false_break | weakness and rebound both occurred; no hard thesis break at Stage2 date |
| 에코프로비엠 | hard_4c_success | call-off / margin deterioration row stops positive training and protects against continued drawdown |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
axis = battery_orderbook_green_requires_utilization_revision_bridge
baseline_value = false
tested_value = true
delta = +1 sector guard
proposal_type = sector_shadow_only
confidence = medium
```

Reason: In battery orderbook/capacity names, the same words — orderbook, customer, capacity, IRA/AMPC — can either be a genuine rerating bridge or a stale boom-cycle residue. The branch must ask whether the evidence has converted into utilization, margin, customer call-off stability, or revision.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
new_axis_proposed:
  - c11_orderbook_green_requires_realized_revision
  - c11_capacity_orderbook_stage2_bonus
  - c11_calloff_margin_slowdown_4c_guard
```

Interpretation:
- Capacity/orderbook evidence can support Stage2/Yellow when the price window is clean and the evidence is not purely price beta.
- Green should require realized utilization, confirmed revision, margin bridge, or durable customer conversion.
- If call-off/order-cut or margin deterioration appears, route to 4C/protection and stop using the row for positive entry calibration.

## 19. Before / After Backtest Comparison

| profile | selected triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 128.74 | -19.51 | 129.99 | -28.35 | 0.67 | mixed |
| P0b e2r_2_0_baseline_reference | 3 | 128.74 | -19.51 | 129.99 | -28.35 | 0.67 | worse; likely over-weights orderbook headline |
| P1 sector_specific_candidate_profile | 3 | 128.74 | -19.51 | 129.99 | -28.35 | 0.33 | better; LGES/EcoproBM Green capped |
| P2 canonical_archetype_candidate_profile | 3 | 128.74 | -19.51 | 129.99 | -28.35 | 0.00 | best alignment; preserves Enchem but blocks false Green |
| P3 counterexample_guard_profile | 3 | 128.74 | -19.51 | 129.99 | -28.35 | 0.00 | best for risk control; may under-promote future positives |

## 20. Score-Return Alignment Matrix

| case | before label | after label | return alignment |
|---|---|---|---|
| 엔켐 | Stage3-Yellow | Stage3-Green-with-4B-watch | aligned if 4B/watch is attached |
| LG에너지솔루션 | Stage3-Yellow | Stage2-Watch | guard improves alignment |
| 에코프로비엠 | Stage3-Yellow/false-Green-risk | 4C/No-positive-promotion | guard improves alignment |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN | 1 | 2 | 1 | 1 | 3 | 0 | 5 | 3 | 2 | true | true | C11 now has positive/counterexample/4B/4C balance; needs holdout positives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 2
tested_existing_calibrated_axes: stage3_green_revision_min; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: orderbook_headline_false_green; AMPC_policy_support_without_utilization; calloff_margin_slowdown_4c
new_axis_proposed: c11_orderbook_green_requires_realized_revision; c11_capacity_orderbook_stage2_bonus; c11_calloff_margin_slowdown_4c_guard
existing_axis_strengthened: stage3_green_revision_min in C11 only; full_4b_requires_non_price_evidence in C11 only; hard_4c_thesis_break_routes_to_4c in C11 only
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high_total_58_avg_19.3
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R3/C11 battery orderbook rerating residual after R1/R2-heavy calibration
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-Web manifest/schema basis.
- Symbol profile availability and corporate-action candidate dates.
- Tradable OHLC rows for selected entry windows.
- 30D/90D/180D MFE/MAE proxy calculations from actual OHLC rows.
- Representative trigger dedupe and overlay row separation.

Not validated:
- Live 2026 candidate status.
- Production scoring code.
- Broker/API execution.
- Whether future battery cycle conditions will repeat this exact path.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_green_requires_realized_revision,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,false,true,+1,"Orderbook/capacity headline alone produced false Green in cathode/cell names; realized revision/margin/customer conversion needed.","reduces false positive from 2/3 to 0/3 while preserving Enchem Stage2/Yellow",R3L11_C11_348370_S2_2024-01-08|R3L11_C11_373220_S2_2024-04-26|R3L11_C11_247540_S2_2024-01-05,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_capacity_orderbook_stage2_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,+1,+1,"Capacity/orderbook evidence can be early if it is not merely price beta and if corporate-action window is clean.","keeps structural Enchem row as Stage2/Yellow without broad Green relaxation",R3L11_C11_348370_S2_2024-01-08,1,1,0,low,canonical_shadow_only,"positive promotion remains shadow-only"
shadow_weight,c11_calloff_margin_slowdown_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,false,true,+1,"When call-off/order-cut and margin slowdown appear, route to 4C/protection and stop positive training.","blocks EcoproBM false Green and converts drawdown into protection evidence",R3L11_C11_247540_4C_2024-06-24,1,1,1,medium,canonical_shadow_only,"4C rows are not positive entry weights
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L11_C11_348370_ENCHEM","symbol":"348370","company_name":"엔켐","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L11_C11_348370_S2_2024-01-08","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Electrolyte capacity/orderbook route had non-price evidence and very large MFE, but drawdown after peak requires 4B/watch discipline.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Electrolyte capacity/orderbook route had non-price evidence and very large MFE, but drawdown after peak requires 4B/watch discipline."}
{"row_type":"case","case_id":"R3L11_C11_373220_LGES","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L11_C11_373220_S2_2024-04-26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"AMPC/JV support helped a later rebound, but utilization and EV-demand drag meant the early orderbook/AMPC bridge was not clean Green.","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"AMPC/JV support helped a later rebound, but utilization and EV-demand drag meant the early orderbook/AMPC bridge was not clean Green."}
{"row_type":"case","case_id":"R3L11_C11_247540_ECOPROBM","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R3L11_C11_247540_S2_2024-01-05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Cathode orderbook narrative and rebound beta failed to convert into durable revision; MAE dominated MFE.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Cathode orderbook narrative and rebound beta failed to convert into durable revision; MAE dominated MFE."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R3L11_C11_348370_S2_2024-01-08","case_id":"R3L11_C11_348370_ENCHEM","symbol":"348370","company_name":"엔켐","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","sector":"2차전지·전기차·친환경","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-08","evidence_available_at_that_date":"capacity/orderbook expansion narrative; electrolyte supply route; early relative strength before realized peak","evidence_source":"company/news/research evidence family; stock-web OHLC validated","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-08","entry_price":84300,"MFE_30D_pct":300.95,"MFE_90D_pct":368.09,"MFE_180D_pct":368.09,"MFE_1Y_pct":368.09,"MFE_2Y_pct":null,"MAE_30D_pct":-1.66,"MAE_90D_pct":-1.66,"MAE_180D_pct":-1.66,"MAE_1Y_pct":-1.66,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-04-08","peak_price":394500,"drawdown_after_peak_pct":-70.22,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B_entry","four_b_evidence_type":["none"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_drawdown_after_peak","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_C11_348370_2024-01-08_84300","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_C11_348370_4B_2024-04-08","case_id":"R3L11_C11_348370_ENCHEM","symbol":"348370","company_name":"엔켐","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","sector":"2차전지·전기차·친환경","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"4B-Watch","trigger_date":"2024-04-08","evidence_available_at_that_date":"valuation/positioning overheat near local and full observed peak; not a positive entry row","evidence_source":"stock-web OHLC; valuation/positioning evidence family","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-08","entry_price":358000,"MFE_30D_pct":10.2,"MFE_90D_pct":10.2,"MFE_180D_pct":10.2,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-23.6,"MAE_90D_pct":-58.35,"MAE_180D_pct":-69.83,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":394500,"drawdown_after_peak_pct":-70.22,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_watch_not_positive_entry","four_b_evidence_type":["valuation_blowoff","positioning_overheat","price_only"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_C11_348370_2024-04-08_358000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_C11_373220_S2_2024-04-26","case_id":"R3L11_C11_373220_LGES","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","sector":"2차전지·전기차·친환경","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-26","evidence_available_at_that_date":"AMPC/JV support and large-cap battery stabilization narrative, but utilization/revision bridge not yet closed","evidence_source":"company earnings/AMPC evidence family; stock-web OHLC validated","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":372000,"MFE_30D_pct":6.72,"MFE_90D_pct":15.59,"MFE_180D_pct":19.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.37,"MAE_90D_pct":-16.4,"MAE_180D_pct":-16.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-22.64,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.42,"four_b_full_window_peak_proximity":0.42,"four_b_timing_verdict":"stage2_watch_but_green_too_early","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown"],"four_c_protection_label":"false_break","trigger_outcome_label":"failed_rerating_partial_rebound","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_C11_373220_2024-04-26_372000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_C11_247540_S2_2024-01-05","case_id":"R3L11_C11_247540_ECOPROBM","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","sector":"2차전지·전기차·친환경","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-05","evidence_available_at_that_date":"cathode orderbook/rebound narrative after prior boom, but call-off/utilization/revision deterioration not resolved","evidence_source":"company/news/research evidence family; stock-web OHLC validated","stage2_evidence_fields":["public_event_or_disclosure","backlog_or_delivery_visibility","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-05","entry_price":315000,"MFE_30D_pct":2.54,"MFE_90D_pct":2.54,"MFE_180D_pct":2.54,"MFE_1Y_pct":-52.57,"MFE_2Y_pct":null,"MAE_30D_pct":-32.22,"MAE_90D_pct":-40.48,"MAE_180D_pct":-66.98,"MAE_1Y_pct":-66.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-08","peak_price":323000,"drawdown_after_peak_pct":-66.98,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.03,"four_b_full_window_peak_proximity":0.03,"four_b_timing_verdict":"not_full_4B_until_non_price_deterioration","four_b_evidence_type":["margin_or_backlog_slowdown","contract_delay"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"false_positive_green_hard_4c_protected","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_C11_247540_2024-01-05_315000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_C11_247540_4C_2024-06-24","case_id":"R3L11_C11_247540_ECOPROBM","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_CAPACITY_ORDERBOOK_VS_CATHODE_CALL_OFF_FALSE_GREEN","sector":"2차전지·전기차·친환경","primary_archetype":"battery_orderbook_rerating","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","trigger_type":"4C","trigger_date":"2024-06-24","evidence_available_at_that_date":"delivery/call-off and margin deterioration visible enough to stop positive training; this is protection row only","evidence_source":"non-price deterioration evidence family; stock-web OHLC validated","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown","contract_delay"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-06-24","entry_price":182100,"MFE_30D_pct":10.93,"MFE_90D_pct":10.93,"MFE_180D_pct":10.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-6.31,"MAE_90D_pct":-35.48,"MAE_180D_pct":-41.46,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-08","peak_price":202000,"drawdown_after_peak_pct":-41.53,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"4C_protection_not_positive_entry","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_C11_247540_2024-06-24_182100","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C11_348370_ENCHEM","trigger_id":"R3L11_C11_348370_S2_2024-01-08","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":22,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green-with-4B-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 gives bonus only because capacity/orderbook evidence is paired with realized price validation; 4B watch is added because post-peak drawdown is severe.","MFE_90D_pct":368.09,"MAE_90D_pct":-1.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"R3L11_C11_348370_ENCHEM","trigger_id":"R3L11_C11_348370_S2_2024-01-08","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":22,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green-with-4B-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 gives bonus only because capacity/orderbook evidence is paired with realized price validation; 4B watch is added because post-peak drawdown is severe.","MFE_90D_pct":368.09,"MAE_90D_pct":-1.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P1_L3_battery_orderbook_sector_shadow","case_id":"R3L11_C11_348370_ENCHEM","trigger_id":"R3L11_C11_348370_S2_2024-01-08","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":22,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green-with-4B-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 gives bonus only because capacity/orderbook evidence is paired with realized price validation; 4B watch is added because post-peak drawdown is severe.","MFE_90D_pct":368.09,"MAE_90D_pct":-1.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P2_C11_battery_orderbook_archetype_shadow","case_id":"R3L11_C11_348370_ENCHEM","trigger_id":"R3L11_C11_348370_S2_2024-01-08","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":22,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green-with-4B-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 gives bonus only because capacity/orderbook evidence is paired with realized price validation; 4B watch is added because post-peak drawdown is severe.","MFE_90D_pct":368.09,"MAE_90D_pct":-1.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P3_C11_counterexample_guard_profile","case_id":"R3L11_C11_348370_ENCHEM","trigger_id":"R3L11_C11_348370_S2_2024-01-08","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":0,"revision_score":8,"relative_strength_score":20,"customer_quality_score":14,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":22,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":20,"customer_quality_score":18,"policy_or_regulatory_score":0,"valuation_repricing_score":12,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":89,"stage_label_after":"Stage3-Green-with-4B-watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C11 gives bonus only because capacity/orderbook evidence is paired with realized price validation; 4B watch is added because post-peak drawdown is severe.","MFE_90D_pct":368.09,"MAE_90D_pct":-1.66,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C11_373220_LGES","trigger_id":"R3L11_C11_373220_S2_2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"AMPC/JV policy support is capped when utilization and revision do not close; not a clean Green.","MFE_90D_pct":15.59,"MAE_90D_pct":-16.4,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"R3L11_C11_373220_LGES","trigger_id":"R3L11_C11_373220_S2_2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"AMPC/JV policy support is capped when utilization and revision do not close; not a clean Green.","MFE_90D_pct":15.59,"MAE_90D_pct":-16.4,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"P1_L3_battery_orderbook_sector_shadow","case_id":"R3L11_C11_373220_LGES","trigger_id":"R3L11_C11_373220_S2_2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"AMPC/JV policy support is capped when utilization and revision do not close; not a clean Green.","MFE_90D_pct":15.59,"MAE_90D_pct":-16.4,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"P2_C11_battery_orderbook_archetype_shadow","case_id":"R3L11_C11_373220_LGES","trigger_id":"R3L11_C11_373220_S2_2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"AMPC/JV policy support is capped when utilization and revision do not close; not a clean Green.","MFE_90D_pct":15.59,"MAE_90D_pct":-16.4,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"P3_C11_counterexample_guard_profile","case_id":"R3L11_C11_373220_LGES","trigger_id":"R3L11_C11_373220_S2_2024-04-26","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":8,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":12,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":16,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"AMPC/JV policy support is capped when utilization and revision do not close; not a clean Green.","MFE_90D_pct":15.59,"MAE_90D_pct":-16.4,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C11_247540_ECOPROBM","trigger_id":"R3L11_C11_247540_S2_2024-01-05","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":26,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4C/No-positive-promotion","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Orderbook narrative is capped by call-off/margin deterioration; hard 4C rows are protection only.","MFE_90D_pct":2.54,"MAE_90D_pct":-40.48,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P0b_e2r_2_0_baseline_reference","case_id":"R3L11_C11_247540_ECOPROBM","trigger_id":"R3L11_C11_247540_S2_2024-01-05","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":26,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4C/No-positive-promotion","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Orderbook narrative is capped by call-off/margin deterioration; hard 4C rows are protection only.","MFE_90D_pct":2.54,"MAE_90D_pct":-40.48,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P1_L3_battery_orderbook_sector_shadow","case_id":"R3L11_C11_247540_ECOPROBM","trigger_id":"R3L11_C11_247540_S2_2024-01-05","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":26,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4C/No-positive-promotion","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Orderbook narrative is capped by call-off/margin deterioration; hard 4C rows are protection only.","MFE_90D_pct":2.54,"MAE_90D_pct":-40.48,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P2_C11_battery_orderbook_archetype_shadow","case_id":"R3L11_C11_247540_ECOPROBM","trigger_id":"R3L11_C11_247540_S2_2024-01-05","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":26,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4C/No-positive-promotion","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Orderbook narrative is capped by call-off/margin deterioration; hard 4C rows are protection only.","MFE_90D_pct":2.54,"MAE_90D_pct":-40.48,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P3_C11_counterexample_guard_profile","case_id":"R3L11_C11_247540_ECOPROBM","trigger_id":"R3L11_C11_247540_S2_2024-01-05","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow/false-Green-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":26,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"4C/No-positive-promotion","changed_components":["backlog_visibility_score","revision_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"Orderbook narrative is capped by call-off/margin deterioration; hard 4C rows are protection only.","MFE_90D_pct":2.54,"MAE_90D_pct":-40.48,"score_return_alignment_label":"guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c11_orderbook_green_requires_realized_revision,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,false,true,+1,"Orderbook/capacity headline alone produced false Green in cathode/cell names; realized revision/margin/customer conversion needed.","reduces false positive from 2/3 to 0/3 while preserving Enchem Stage2/Yellow",R3L11_C11_348370_S2_2024-01-08|R3L11_C11_373220_S2_2024-04-26|R3L11_C11_247540_S2_2024-01-05,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c11_capacity_orderbook_stage2_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,+1,+1,"Capacity/orderbook evidence can be early if it is not merely price beta and if corporate-action window is clean.","keeps structural Enchem row as Stage2/Yellow without broad Green relaxation",R3L11_C11_348370_S2_2024-01-08,1,1,0,low,canonical_shadow_only,"positive promotion remains shadow-only"
shadow_weight,c11_calloff_margin_slowdown_4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,false,true,+1,"When call-off/order-cut and margin slowdown appear, route to 4C/protection and stop positive training.","blocks EcoproBM false Green and converts drawdown into protection evidence",R3L11_C11_247540_4C_2024-06-24,1,1,1,medium,canonical_shadow_only,"4C rows are not positive entry weights
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["orderbook_headline_false_green","AMPC_policy_support_without_utilization","calloff_margin_slowdown_4c"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R3/C11 battery orderbook rerating residual after R1/R2-heavy calibration"}
```

### 25.7 narrative_only rows

```jsonl

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
next_round = R3_holdout_or_R4_loop11
preferred_next_objective = add_one_more_C11_positive_holdout_or_move_to_R4_materials_spread
avoid_repeating = 엔켐_2024-01-08, LGES_2024-04-26, 에코프로비엠_2024-01-05
```

## 28. Source Notes

- Stock-Web manifest/schema: raw/unadjusted FinanceData/marcap tradable shards, max_date 2026-02-20.
- Symbol profiles checked: 348370, 373220, 247540.
- Tradable OHLC rows checked directly from Stock-Web 2024 shards for all entry and forward windows.
- All proposed rules are shadow-only and do not modify production scoring.
