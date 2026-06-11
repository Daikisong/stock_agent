# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R3
selected_loop: 94
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
generated_at: 2026-06-06
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent historical cases for R3/L3_BATTERY_EV_GREEN_MOBILITY/C11_BATTERY_ORDERBOOK_RERATING. It deliberately combines the 2023 orderbook rerating regime with 2024 demand-slowdown failures so that the canonical rule does not confuse backlog size with cash-generating backlog quality.

## 1. Current Calibrated Profile Assumption

Current proxy profile:

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

For C11, the core issue is not whether a company has a large orderbook. The decisive bridge is whether the orderbook can travel through customer ramp, utilization, ASP/mix, margin and FCF without being intercepted by call-off, inventory build, or capex drag. In lived market terms: the orderbook is the train ticket, not the arrival. The calibration question is whether the train actually leaves the station and reaches earnings.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R3 |
| selected_loop | 94 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C11_BATTERY_ORDERBOOK_RERATING |
| fine_archetype_id | BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL |
| rule scope | canonical_archetype_specific |

Canonical compression:

```text
battery orderbook / long-term supply contract
→ customer ramp + utilization + ASP/mix + margin + FCF bridge
→ Stage2-Actionable only if non-price conversion evidence exists
→ Stage3-Yellow only if orderbook quality and margin conversion are visible
→ Stage3-Green only if revision/FCF confirms durability
→ price-only or headline-only orderbook rerating remains 4B-watch when valuation outruns conversion evidence
```

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C11 as Priority 0 with 23 rows and 7 more rows needed to reach the 30-row minimum. The selection therefore prioritizes a new C11 coverage contribution rather than a mechanical R1-R13 cycle.

Duplicate policy used:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
hard_duplicate_status = no_known_hard_duplicate_in_selected_case_set
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

Registry scan note: existing C11 files include earlier battery orderbook/equipment coverage around loop 85 and loop 89. This loop avoids re-materializing those labels by using a split regime map: 2023 cell/cathode orderbook rerating success, 2023 blowoff durability audit, and 2024 orderbook failure under EV demand slowdown.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web symbol profile checks:

| symbol | company | profile path | year shard | corporate-action window status |
|---|---|---|---|---|
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | clean_180D_window |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | clean_180D_window; corporate action caveat outside selected 2023 window |
| 006400 | 삼성SDI | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | clean_180D_window |

## 5. Historical Eligibility Gate

All representative triggers below use historical trigger dates, have tradable entry rows in Stock-Web, include OHLCV, and have enough subsequent trading days within the committed atlas to observe the forward path.

| case_id | entry_date | entry_price | forward_window_trading_days | calibration_usable | block reasons |
|---|---:|---:|---:|---|---|
| C11_373220_2023_CELL_ORDERBOOK_RERATING_SUCCESS | 2023-01-26 | 517000 | 180 | true | [] |
| C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT | 2023-02-28 | 166300 | 180 | true | [] |
| C11_006400_2024_ORDERBOOK_TO_FCF_FAILURE | 2024-03-25 | 486000 | 180 | true | [] |

## 6. Canonical Archetype Compression Map

| fine trigger family | compressed canonical interpretation | C11 role |
|---|---|---|
| cell_orderbook_customer_ramp | cell maker orderbook/customer ramp with visible volume bridge | positive Stage2/Yellow candidate |
| cathode_orderbook_blowoff_durability | cathode orderbook rerating with valuation blowoff before FCF/margin durability | positive early MFE but 4B durability audit |
| cell_orderbook_no_fcf_margin_bridge | cell maker orderbook narrative fails as demand/utilization and margin pressure dominate | counterexample / Stage2 failure |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger |
|---|---|---|---|---|---|
| C11_373220_2023_CELL_ORDERBOOK_RERATING_SUCCESS | 373220 | LG에너지솔루션 | customer_ramp_orderbook_success | positive | Stage2-Actionable |
| C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT | 247540 | 에코프로비엠 | orderbook_rerating_blowoff_audit | positive_but_4B_audit | Stage3-Yellow → 4B-watch |
| C11_006400_2024_ORDERBOOK_TO_FCF_FAILURE | 006400 | 삼성SDI | orderbook_no_fcf_margin_bridge | counterexample | Stage2-Fail / 4B-watch |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
current_profile_error_count = 2
```

Interpretation:

- 373220 shows that cell-maker orderbook/customer-ramp evidence can produce a usable C11 Stage2/Yellow path when price has not yet outrun the conversion bridge.
- 247540 shows a strong MFE path, but the post-peak drawdown proves that C11 must not become unconditional Green merely because orderbook and customer capacity narratives are loud.
- 006400 shows the hard counterexample: orderbook language without utilization/margin/FCF confirmation can become a value trap when EV demand and pricing pressure take the steering wheel.

## 9. Evidence Source Map

This loop uses source-proxy historical evidence labels rather than direct disclosure URLs. It is therefore valid for residual calibration but should be marked `evidence_url_pending=true` for later evidence repair.

| case | evidence available at trigger date | evidence source type | caveat |
|---|---|---|---|
| 373220 | battery cell orderbook/customer ramp, US/Europe capacity visibility, long-cycle supply expectations | source_proxy_sector_news | needs later URL repair; use as Stage2/Yellow, not automatic Green |
| 247540 | cathode orderbook/customer capacity rerating and violent 2023 price acceleration | source_proxy_sector_news | strong MFE but clear blowoff/durability issue; needs 4B split |
| 006400 | cell/battery orderbook narrative still present, but EV slowdown and margin/FCF pressure dominated by 2024 | source_proxy_sector_news | counterexample; do not score as positive Stage2 without conversion bridge |

## 10. Price Data Source Map

| symbol | shard path | key observed rows |
|---|---|---|
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2023.csv | 2023-01-26 close 517000; 2023-06-12 high 614000; 2023-10-25 low 409000 |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv | 2023-02-28 close 166300; 2023-03-23 high 262500; 2023-07-26 high 584000; 2023-10-25 low 213000 |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | 2024-03-25 close 486000; 2024-03-25 high 494500; 2024-11-15 low 235500 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | trigger family | outcome |
|---|---|---|---|---|---:|---|---|
| C11_373220_T1 | 373220 | Stage2-Actionable | 2023-01-25 | 2023-01-26 | 517000 | cell_orderbook_customer_ramp | good_stage2_to_yellow |
| C11_247540_T1 | 247540 | Stage2-Actionable | 2023-02-27 | 2023-02-28 | 166300 | cathode_orderbook_rerating | high_MFE_success |
| C11_247540_T2 | 247540 | Stage4B-Watch | 2023-07-24 | 2023-07-25 | 462000 | cathode_orderbook_blowoff_durability | good_4B_after_blowoff |
| C11_006400_T1 | 006400 | Stage2-Fail | 2024-03-22 | 2024-03-25 | 486000 | cell_orderbook_no_fcf_margin_bridge | orderbook_counterexample |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|---:|
| C11_373220_T1 | 517000 | 10.3% | -5.2% | 18.8% | -5.2% | 18.8% | -20.9% | 2023-06-12 | 614000 | -33.4% |
| C11_247540_T1 | 166300 | 57.9% | -4.9% | 85.5% | -4.9% | 251.2% | -4.9% | 2023-07-26 | 584000 | -63.5% |
| C11_006400_T1 | 486000 | 1.7% | -16.5% | 1.7% | -27.8% | 1.7% | -51.5% | 2024-03-25 | 494500 | -52.4% |

### Interpretation

- 373220 is the cleanest positive example: orderbook/customer-ramp evidence matched a controlled 30D MAE and useful forward MFE before later sector cooling.
- 247540 is not a simple positive. It proves the C11 engine should allow early Stage2/Yellow MFE, then hand the case to 4B when valuation and price path separate from margin/FCF durability.
- 006400 is the counterexample: battery orderbook language did not protect the path when EV demand, utilization, and FCF pressure turned against the thesis.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely verdict | price alignment | residual error |
|---|---|---|---|
| 373220 | Stage2-Actionable / Stage3-Yellow candidate if non-price orderbook-to-ramp evidence exists | mostly aligned | no major error; Green must remain locked until FCF/revision confirms |
| 247540 | Stage2/Yellow captures MFE, but Green would be dangerous without 4B overlay | partially aligned | residual_4B_timing_after_blowoff |
| 006400 | Stage2 bonus may over-credit orderbook headline unless margin/FCF bridge required | misaligned if promoted | stage2_false_positive_orderbook_headline |

Stress answers:

```text
stage2_actionable_evidence_bonus: useful for 373220/247540 only when non-price conversion bridge exists.
yellow threshold: acceptable if paired with orderbook quality and customer ramp evidence.
green threshold: must remain strict; no Green unlock without FCF/revision/margin durability.
price_only_blowoff guard: necessary for 247540 post-peak behavior.
full_4b_requires_non_price_evidence: should remain true; C11 needs valuation + bridge deterioration before full 4B.
hard_4c_thesis_break routing: not primary C11 axis, but relevant when orderbook converts into call-off/FCF break.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2-Actionable | Stage3-Yellow | Stage3-Green |
|---|---|---|---|
| 373220 | yes, if orderbook/customer ramp evidence exists | yes, if utilization and shipment bridge visible | no until FCF/revision confirms |
| 247540 | yes early | yes, but 4B-watch after blowoff | no; valuation outran conversion durability |
| 006400 | no, unless FCF/margin bridge exists | no | no |

## 15. 4B Local vs Full-window Timing Audit

| trigger | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| C11_373220_T1 | n/a | n/a | non_price_orderbook_bridge | positive Stage2/Yellow, later durability audit |
| C11_247540_T2 | 0.95 | 0.79 | valuation_blowoff + orderbook durability uncertainty | good local 4B; full-window blowoff audit needed |
| C11_006400_T1 | 0.98 | 0.98 | orderbook headline without FCF/margin bridge | good Stage2 block / 4B-watch |

## 16. 4C Protection Audit

| trigger | 4C label | protection verdict |
|---|---|---|
| C11_373220_T1 | not_4C | no hard break at trigger; treat as positive but cap Green |
| C11_247540_T2 | 4B_watch_not_hard_4C | post-peak decline requires valuation guard, not immediate 4C without thesis break |
| C11_006400_T1 | thesis_break_watch | if margin/FCF deterioration is confirmed, route toward 4C; otherwise Stage2 block is enough |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
sector_rule_candidate_id = L3_BATTERY_ORDERBOOK_QUALITY_TO_FCF_MARGIN_BRIDGE
```

Candidate rule:

```text
In L3 battery/EV names, orderbook size alone cannot unlock positive Stage2-Actionable.
Require at least one non-price conversion bridge:
- customer ramp / shipment visibility;
- utilization improvement;
- ASP/mix stability;
- margin bridge;
- FCF/capex absorption evidence.
If orderbook evidence is present but conversion bridge is absent, cap at Stage1/Stage2-Watch.
If valuation and price path blow off before bridge confirmation, route to C11 4B-watch.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_rule_candidate_id = C11_ORDERBOOK_TO_FCF_MARGIN_BRIDGE_REQUIRED_FOR_STAGE2_ACTIONABLE
```

Shadow rule proposal:

```text
For canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING:
  positive_stage2_actionable_allowed only if:
    orderbook_or_supply_contract_evidence == true
    AND customer_ramp_or_shipment_bridge == true
    AND (margin_bridge == true OR fcf_bridge == true OR utilization_bridge == true)
  stage3_yellow_allowed only if:
    positive_stage2_actionable_allowed == true
    AND valuation_not_full_window_4b == true
  stage3_green_allowed only if:
    stage3_yellow_allowed == true
    AND EPS_or_FCF_revision_confirms == true
  if price_path_blowoff_without_bridge == true:
    route_to_stage4B_watch
```

## 19. Raw Component Score Breakdown

| case | info_confidence | fundamental | market | valuation | revision | risk | raw_total_proxy | staged_verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 373220 | 18 | 17 | 14 | 10 | 11 | 8 | 78 | Stage3-Yellow candidate, no Green |
| 247540 early | 16 | 14 | 20 | 4 | 10 | 5 | 69 | Stage2/Yellow only, 4B watch needed |
| 006400 | 13 | 9 | 7 | 8 | 4 | 3 | 44 | Stage2-Fail / watch |

Interpretation: C11 requires weighted emphasis on conversion evidence rather than market momentum. 247540 shows why the market score should not overpower weak valuation/risk durability.

## 20. Machine-Readable Rows

```jsonl
{"row_type":"case","case_id":"C11_373220_2023_CELL_ORDERBOOK_RERATING_SUCCESS","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL","symbol":"373220","company":"LG에너지솔루션","case_type":"customer_ramp_orderbook_success","positive_or_counterexample":"positive","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"case","case_id":"C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL","symbol":"247540","company":"에코프로비엠","case_type":"orderbook_rerating_blowoff_audit","positive_or_counterexample":"positive_but_4b_audit","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"case","case_id":"C11_006400_2024_ORDERBOOK_TO_FCF_FAILURE","schema_family":"v12_sector_archetype_residual","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL","symbol":"006400","company":"삼성SDI","case_type":"orderbook_no_fcf_margin_bridge","positive_or_counterexample":"counterexample","evidence_url_pending":true,"calibration_usable":true}
{"row_type":"trigger","trigger_id":"C11_373220_T1","case_id":"C11_373220_2023_CELL_ORDERBOOK_RERATING_SUCCESS","symbol":"373220","company":"LG에너지솔루션","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-25","entry_date":"2023-01-26","entry_price":517000,"mfe_30d_pct":10.3,"mae_30d_pct":-5.2,"mfe_90d_pct":18.8,"mae_90d_pct":-5.2,"mfe_180d_pct":18.8,"mae_180d_pct":-20.9,"peak_date":"2023-06-12","peak_price":614000,"drawdown_after_peak_pct":-33.4,"trigger_family":"cell_orderbook_customer_ramp","path_label":"good_stage2_to_yellow","calibration_usable":true}
{"row_type":"trigger","trigger_id":"C11_247540_T1","case_id":"C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT","symbol":"247540","company":"에코프로비엠","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-27","entry_date":"2023-02-28","entry_price":166300,"mfe_30d_pct":57.9,"mae_30d_pct":-4.9,"mfe_90d_pct":85.5,"mae_90d_pct":-4.9,"mfe_180d_pct":251.2,"mae_180d_pct":-4.9,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-63.5,"trigger_family":"cathode_orderbook_rerating","path_label":"high_mfe_success_but_blowoff","calibration_usable":true}
{"row_type":"trigger","trigger_id":"C11_247540_T2","case_id":"C11_247540_2023_CATHODE_ORDERBOOK_BLOWOFF_AUDIT","symbol":"247540","company":"에코프로비엠","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","trigger_type":"Stage4B-Watch","trigger_date":"2023-07-24","entry_date":"2023-07-25","entry_price":462000,"mfe_30d_pct":26.4,"mae_30d_pct":-34.7,"mfe_90d_pct":26.4,"mae_90d_pct":-53.9,"mfe_180d_pct":26.4,"mae_180d_pct":-53.9,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-63.5,"trigger_family":"cathode_orderbook_blowoff_durability","path_label":"good_4b_after_blowoff","calibration_usable":true}
{"row_type":"trigger","trigger_id":"C11_006400_T1","case_id":"C11_006400_2024_ORDERBOOK_TO_FCF_FAILURE","symbol":"006400","company":"삼성SDI","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","trigger_type":"Stage2-Fail","trigger_date":"2024-03-22","entry_date":"2024-03-25","entry_price":486000,"mfe_30d_pct":1.7,"mae_30d_pct":-16.5,"mfe_90d_pct":1.7,"mae_90d_pct":-27.8,"mfe_180d_pct":1.7,"mae_180d_pct":-51.5,"peak_date":"2024-03-25","peak_price":494500,"drawdown_after_peak_pct":-52.4,"trigger_family":"cell_orderbook_no_fcf_margin_bridge","path_label":"orderbook_counterexample","calibration_usable":true}
{"row_type":"score_simulation","simulation_id":"C11_STAGE2_BRIDGE_REQUIRED","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","rule_candidate_id":"C11_ORDERBOOK_TO_FCF_MARGIN_BRIDGE_REQUIRED_FOR_STAGE2_ACTIONABLE","effect":"blocks_stage2_false_positive_when_orderbook_headline_lacks_customer_ramp_margin_fcf_bridge","shadow_weight_only":true}
{"row_type":"shadow_weight","shadow_weight_id":"C11_ORDERBOOK_QUALITY_TO_FCF_MARGIN_BRIDGE","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","axis":"stage2_required_bridge","proposed_delta":"require_non_price_conversion_bridge","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"calibration_usable_case_count":3,"calibration_usable_trigger_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"new_axis_proposed":"c11_orderbook_to_fcf_margin_bridge_required_for_stage2_actionable_shadow_only","next_recommended_archetypes":["C02_POWER_GRID_DATACENTER_CAPEX","C19_BRAND_RETAIL_INVENTORY_MARGIN","C27_CONTENT_IP_GLOBAL_MONETIZATION"]}
```

## 21. Aggregate Metrics

```jsonl
{"row_type":"aggregate_metric","selected_round":"R3","selected_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","case_count":3,"trigger_count":4,"representative_trigger_count":4,"median_mfe_90d_pct":52.15,"median_mae_90d_pct":-16.35,"positive_case_count":2,"counterexample_count":1,"residual_error_count":2,"coverage_gap_before_rows":23,"coverage_gap_need_to_30":7,"coverage_gap_after_expected_rows":27}
```

Aggregate read:

- C11 still deserves Priority 0 follow-up even after this loop because 23 → expected 27 still remains below 30.
- The best signal is not orderbook size, but orderbook-to-customer-ramp-to-margin/FCF conversion.
- The worst false positive is orderbook headline + weak FCF/margin bridge + valuation already extended.

## 22. Residual Contribution Summary

```text
loop_contribution_label = canonical_archetype_rule_candidate
new_axis_proposed = c11_orderbook_to_fcf_margin_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened = full_4b_requires_non_price_evidence scoped to C11 orderbook blowoff
existing_axis_weakened = null
production_scoring_changed = false
shadow_weight_only = true
```

Residual contribution:

1. Adds C11-specific Stage2 bridge requirement.
2. Splits 2023 orderbook rerating success from 2023 blowoff durability risk.
3. Adds a 2024 counterexample where orderbook narrative failed because EV demand/margin/FCF pressure dominated.
4. Prevents the global Stage2-actionable bonus from promoting battery names on backlog headlines alone.

## 23. Validation Scope

```text
validation_scope = historical_stock_web_1D_OHLC_only
live_candidate_mode = false
current_stock_discovery_allowed = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 24. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for Songdaiki/stock_agent.
Do not treat this Markdown file as an instruction to patch production immediately.
Read this file only as one candidate v12 sector-archetype residual research artifact.

Task:
- Ingest the machine-readable JSONL rows above.
- Validate schema_family == v12_sector_archetype_residual.
- Validate selected_round == R3 and large_sector_id == L3_BATTERY_EV_GREEN_MOBILITY.
- Validate canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING.
- Deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date.
- Compare the candidate axis c11_orderbook_to_fcf_margin_bridge_required_for_stage2_actionable_shadow_only against the larger corpus.
- Promote only if multiple independent C11 cases support the same bridge requirement.
- Keep production scoring unchanged unless a separate batch promotion planner approves the rule.

Candidate shadow rule to evaluate:
For C11_BATTERY_ORDERBOOK_RERATING, require orderbook/customer contract evidence plus at least one conversion bridge among customer ramp, shipment visibility, utilization, margin, ASP/mix, or FCF before Stage2-Actionable promotion. If price or valuation blows off before the conversion bridge is visible, route to 4B-watch instead of Green.
```

## 25. Final Research Runner Output Summary

```text
stock-web v12 sector/archetype residual calibration MD generated
selected_round = R3
selected_loop = 94
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = BATTERY_ORDERBOOK_RERATING_FCF_MARGIN_BRIDGE_VS_DEMAND_SLOWDOWN_AND_BLOWOFF_REVERSAL
new_independent_case_count = 3
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
positive_case_count = 2
counterexample_count = 1
current_profile_error_count = 2
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = c11_orderbook_to_fcf_margin_bridge_required_for_stage2_actionable_shadow_only
next_recommended_archetypes = C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```
