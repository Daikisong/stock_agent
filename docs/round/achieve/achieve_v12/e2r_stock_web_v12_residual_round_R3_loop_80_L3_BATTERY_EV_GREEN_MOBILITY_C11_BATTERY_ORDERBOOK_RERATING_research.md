# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R3_loop_80_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
selected_round: R3
selected_loop: 80
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: ELECTROLYTE_ORDERBOOK_CAPACITY_CONVERSION_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent cases, 2 orderbook-rerating success paths, and 1 margin/FCF bridge counterexample for R3/L3/C11.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C11:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R3 -> L3_BATTERY_EV_GREEN_MOBILITY
C11 -> C11_BATTERY_ORDERBOOK_RERATING
```

C11 is not simply “battery stock with contracts.” It asks whether a battery orderbook, customer route, or long-term supply story becomes revenue conversion, margin bridge, EPS revision, and FCF. Orderbook is the door handle; margin/FCF is the door actually opening.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C11 current rows | 23 |
| C11 need to 30 | 7 |
| C11 need to 50 | 27 |
| C11 조사 포인트 | 배터리 orderbook이 FCF/마진으로 전환되는지 검증 |

This session locally generated C08/C09/C01/C07/C06/C10/C14 loops before this file, so C11 is selected as the next under-covered Priority 0 archetype.

Selected symbols:

| symbol | company | status |
|---|---|---|
| 348370 | 엔켐 | new local C11 symbol |
| 078600 | 대주전자재료 | new local C11 symbol |
| 003670 | 포스코퓨처엠 | new local C11 symbol |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 348370 / 2024-01-29 | true | true | clean_180D_window | true |
| 078600 / 2024-02-21 | true | true | clean_180D_window | true |
| 003670 / 2024-02-15 | true | true | clean_180D_window | true |

Corporate-action notes:

- 엔켐 has zero corporate-action candidates.
- 대주전자재료 has zero corporate-action candidates.
- 포스코퓨처엠 has corporate-action candidates in 2015 and 2021 only; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| ELECTROLYTE_ORDERBOOK_CAPACITY_CONVERSION_4B_WATCH | C11 | electrolyte orderbook / capacity expansion route; 4B audit after rerating |
| SILICON_ANODE_ORDERBOOK_CUSTOMER_CONVERSION_4B_WATCH | C11 | silicon-anode customer conversion and orderbook route |
| CATHODE_ORDERBOOK_MARGIN_FCF_BRIDGE_FAIL | C11 | long-term cathode orderbook without margin/FCF bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C11_ENCHEM_348370_2024_01_29_ELECTROLYTE_ORDERBOOK_RERATING_4B | 348370 | 엔켐 | 4B_overlay_success | positive | orderbook/capacity route produced extreme MFE, then large post-peak drawdown |
| C11_DAEJOO_078600_2024_02_21_SILICON_ANODE_ORDERBOOK_RERATING | 078600 | 대주전자재료 | high_mfe_success | positive | silicon-anode customer/orderbook route produced >100% MFE |
| C11_POSCOFM_003670_2024_02_15_CATHODE_ORDERBOOK_MARGIN_BRIDGE_FAIL | 003670 | 포스코퓨처엠 | failed_rerating | counterexample | cathode orderbook story lacked margin/FCF bridge and failed after low-teens MFE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 348370 | source_proxy_only | electrolyte orderbook/capacity route; margin bridge pending | required before promotion |
| 078600 | source_proxy_only | silicon-anode orderbook/customer conversion route; FCF bridge pending | required before promotion |
| 003670 | source_proxy_only | cathode orderbook narrative, but margin/FCF conversion absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 348370 | atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv | atlas/symbol_profiles/348/348370.json |
| 078600 | atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv | atlas/symbol_profiles/078/078600.json |
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv | atlas/symbol_profiles/003/003670.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING | Stage2-Actionable | 2024-01-29 | 2024-01-29 | 169500 | electrolyte orderbook/capacity conversion |
| DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING | Stage2-Actionable | 2024-02-21 | 2024-02-21 | 76000 | silicon-anode orderbook/customer conversion |
| POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL | Stage2 | 2024-02-15 | 2024-02-15 | 300500 | cathode orderbook without margin/FCF bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 348370 | 2024-01-29 | 169500 | 111.50 | -17.70 | 132.74 | -17.70 | 132.74 | -17.70 | 2024-04-08 | 394500 | -62.23 |
| 078600 | 2024-02-21 | 76000 | 34.21 | -7.76 | 115.00 | -7.76 | 115.00 | -7.76 | 2024-06-12 | 163400 | -45.29 |
| 003670 | 2024-02-15 | 300500 | 13.48 | -2.83 | 13.48 | -17.64 | 13.48 | -34.94 | 2024-03-13 | 341000 | -42.67 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 348370 | Stage2A/Yellow possible; 4B after rerating | extreme MFE then deep drawdown | current_profile_4B_too_late |
| 078600 | Stage2A/Yellow possible; 4B after customer/orderbook rerating | >100% MFE then -45% peak drawdown | current_profile_4B_too_late |
| 003670 | Stage2 risk if orderbook narrative over-credited | low MFE and high 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C11 interpretation:

- Stage2A can work when orderbook plus capacity/customer conversion appears early.
- Yellow/Green require margin bridge, revenue conversion, revision, and FCF conversion.
- Long-term orderbook alone should be capped if ASP/margin/FCF bridge is absent.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 348370 | 1.00 | 1.00 | valuation / positioning | good 4B audit after orderbook/capacity rerating |
| 078600 | 1.00 | 1.00 | valuation / positioning | good 4B audit after silicon-anode customer rerating |
| 003670 | 1.00 | 1.00 | weak follow-through / margin bridge fail | orderbook narrative was not enough for Stage2/Yellow |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 348370 | thesis_break_watch_only | not hard 4C, but 4B cap needed after extreme MFE |
| 078600 | thesis_break_watch_only | not hard 4C, but 4B/FCF audit needed |
| 003670 | hard_4c_late | missing margin/FCF bridge should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L3_BATTERY_EV_GREEN_MOBILITY
confidence = low_to_medium
```

Candidate:

> In L3 battery names, orderbook and customer capacity narratives can support Stage2A, but Stage3-Yellow/Green should require company-level revenue conversion, margin bridge, revision, and FCF. If long-term orderbook remains disconnected from ASP/margin/FCF, cap at Stage1/Stage2-watch and route to C11 false-positive or 4C-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C11_BATTERY_ORDERBOOK_RERATING
confidence = low_to_medium
```

Candidate C11 rule:

```text
C11_orderbook_conversion_bridge_required =
  orderbook_or_customer_route
  AND (revenue_conversion OR margin_bridge OR confirmed_revision OR fcf_conversion)

if orderbook_narrative and margin_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 80 and drawdown_after_peak < -40:
    add C11_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_180D < -30:
    classify_as C11_orderbook_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 87.07 | -14.37 | 87.07 | -20.13 | 1 | useful but C11 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 87.07 | -14.37 | 87.07 | -20.13 | 1 | over-credits orderbook narrative |
| P1 sector_specific_candidate_profile | L3 | 2 promoted + 1 guard | 123.87 | -12.73 | 123.87 | -12.73 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C11 | 2 promoted + 1 guard | 123.87 | -12.73 | 123.87 | -12.73 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C11 guard | 2 promoted + 1 guard | 123.87 | -12.73 | 123.87 | -12.73 | 0 | adds orderbook-to-margin bridge requirement |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 348370 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 078600 | Stage2A aligned; 4B/FCF audit late | current_profile_4B_too_late |
| 003670 | Stage2 false positive if orderbook bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C11_BATTERY_ORDERBOOK_RERATING | mixed C11 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 23 -> projected 26 rows; still need 4 to reach 30 |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C11_orderbook_conversion_bridge_required|C11_peak_proximity_4B_audit|C11_orderbook_false_positive_guardrail
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses clean 180D windows.
- Uses C11 Priority 0 coverage gap.
- Uses three local-new C11 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C11_orderbook_conversion_bridge_required,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"003670 shows long-term orderbook narrative can fail without margin/FCF bridge","blocks 003670 false positive while preserving 348370/078600 Stage2A","ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING|DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING|POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C11_peak_proximity_4B_audit,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"348370/078600 high-MFE orderbook reratings still needed 4B audit after valuation extension","adds 4B audit after large C11 MFE without converting price-only peaks into full 4B","ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING|DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C11_orderbook_false_positive_guardrail,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C11_BATTERY_ORDERBOOK_RERATING,0,1,+1,"003670 had low MFE and high 180D MAE despite orderbook narrative","requires orderbook-to-margin/FCF bridge before Stage2/Yellow promotion","POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C11_ENCHEM_348370_2024_01_29_ELECTROLYTE_ORDERBOOK_RERATING_4B","symbol":"348370","company_name":"엔켐","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_ORDERBOOK_CAPACITY_CONVERSION_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook/capacity narrative captured >130% MFE, but post-peak drawdown exceeded 60%, requiring 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; URL repair required before promotion"}
{"row_type":"case","case_id":"C11_DAEJOO_078600_2024_02_21_SILICON_ANODE_ORDERBOOK_RERATING","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SILICON_ANODE_ORDERBOOK_CUSTOMER_CONVERSION_4B_WATCH","case_type":"high_mfe_success","positive_or_counterexample":"positive","best_trigger":"DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"silicon-anode orderbook/customer conversion route captured >100% MFE, but later drawdown requires 4B/FCF check","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"source_proxy_only; useful positive C11 route with later 4B audit"}
{"row_type":"case","case_id":"C11_POSCOFM_003670_2024_02_15_CATHODE_ORDERBOOK_MARGIN_BRIDGE_FAIL","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_MARGIN_FCF_BRIDGE_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"orderbook narrative produced only low-teens MFE and then -35% 180D MAE when margin/FCF bridge failed","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"counterexample for long-term cathode orderbook without margin/FCF conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING","case_id":"C11_ENCHEM_348370_2024_01_29_ELECTROLYTE_ORDERBOOK_RERATING_4B","symbol":"348370","company_name":"엔켐","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"ELECTROLYTE_ORDERBOOK_CAPACITY_CONVERSION_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":169500.0,"evidence_available_at_that_date":"source_proxy_only: electrolyte orderbook/capacity expansion and customer demand route were visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["electrolyte_orderbook_route","capacity_expansion_route","customer_conversion_route","relative_strength"],"stage3_evidence_fields":["capacity_conversion_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":111.5,"MFE_90D_pct":132.74,"MFE_180D_pct":132.74,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.7,"MAE_90D_pct":-17.7,"MAE_180D_pct":-17.7,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":394500.0,"drawdown_after_peak_pct":-62.23,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_orderbook_capacity_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_348370_2024_01_29_169500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING","case_id":"C11_DAEJOO_078600_2024_02_21_SILICON_ANODE_ORDERBOOK_RERATING","symbol":"078600","company_name":"대주전자재료","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"SILICON_ANODE_ORDERBOOK_CUSTOMER_CONVERSION_4B_WATCH","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":76000.0,"evidence_available_at_that_date":"source_proxy_only: silicon anode customer/orderbook conversion narrative and battery material rerating route; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["silicon_anode_orderbook_route","customer_conversion_route","relative_strength"],"stage3_evidence_fields":["orderbook_conversion_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_extension","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv","profile_path":"atlas/symbol_profiles/078/078600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.21,"MFE_90D_pct":115.0,"MFE_180D_pct":115.0,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.76,"MAE_90D_pct":-7.76,"MAE_180D_pct":-7.76,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":163400.0,"drawdown_after_peak_pct":-45.29,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_silicon_anode_orderbook_rerating","four_b_evidence_type":["valuation_extension","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_078600_2024_02_21_76000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL","case_id":"C11_POSCOFM_003670_2024_02_15_CATHODE_ORDERBOOK_MARGIN_BRIDGE_FAIL","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"CATHODE_ORDERBOOK_MARGIN_FCF_BRIDGE_FAIL","sector":"battery / EV / green mobility","primary_archetype":"battery_orderbook_rerating","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":300500.0,"evidence_available_at_that_date":"source_proxy_only: cathode long-term orderbook narrative existed, but margin/FCF bridge and ASP conversion were not confirmed","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["cathode_orderbook_narrative","long_term_contract_route"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["valuation_overhang","weak_follow_through"],"stage4c_evidence_fields":["margin_bridge_absent","fcf_conversion_absent","ev_demand_slowdown_overlay"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.48,"MFE_90D_pct":13.48,"MFE_180D_pct":13.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-2.83,"MAE_90D_pct":-17.64,"MAE_180D_pct":-34.94,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":341000.0,"drawdown_after_peak_pct":-42.67,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"orderbook_price_followthrough_failed_without_margin_fcf_bridge","four_b_evidence_type":["valuation_overhang","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_orderbook_margin_bridge_fail","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C11_003670_2024_02_15_300500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_ENCHEM_348370_2024_01_29_ELECTROLYTE_ORDERBOOK_RERATING_4B","trigger_id":"ENCHEM_348370_2024_01_29_STAGE2A_ELECTROLYTE_ORDERBOOK_RERATING","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":3,"backlog_visibility_score":6,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":10,"customer_quality_score":5,"policy_or_regulatory_score":1,"valuation_repricing_score":3,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with mandatory 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Extreme MFE validates C11 orderbook route, but valuation score must decay after peak proximity unless margin/FCF bridge appears.","MFE_90D_pct":132.74,"MAE_90D_pct":-17.7,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_DAEJOO_078600_2024_02_21_SILICON_ANODE_ORDERBOOK_RERATING","trigger_id":"DAEJOO_078600_2024_02_21_STAGE2A_SILICON_ANODE_ORDERBOOK_RERATING","symbol":"078600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":5,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":9,"customer_quality_score":6,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with 4B/FCF audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Silicon-anode orderbook route was effective, but later drawdown says Green requires margin/FCF conversion.","MFE_90D_pct":115.0,"MAE_90D_pct":-7.76,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C11_POSCOFM_003670_2024_02_15_CATHODE_ORDERBOOK_MARGIN_BRIDGE_FAIL","trigger_id":"POSCOFM_003670_2024_02_15_STAGE2_FALSE_POSITIVE_CATHODE_ORDERBOOK_MARGIN_FAIL","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":6,"customer_quality_score":4,"policy_or_regulatory_score":1,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":3,"policy_or_regulatory_score":1,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":52,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Long-term orderbook narrative without margin/FCF bridge should not receive C11 Stage2 promotion.","MFE_90D_pct":13.48,"MAE_90D_pct":-17.64,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"80","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 80
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

If this loop is accepted, C11 moves from 23 to a projected 26 rows. It remains below 30-row minimum stability, but the next run should re-read the latest No-Repeat Index before selecting another C11 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/348/348370.json
  - atlas/symbol_profiles/078/078600.json
  - atlas/symbol_profiles/003/003670.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
