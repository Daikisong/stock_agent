# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
selected_round: R2
selected_loop: 97
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_TC_BONDER_CUSTOMER_CAPACITY_ORDER_CAPA_4B_WATCH
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

This loop adds 3 new independent C06 rows and moves C06 from static 21 rows to local projected 24 after loop77, then to projected 27 after this loop.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C06:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C06 -> C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

C06 is the HBM customer-capacity archetype. It is not just “AI semiconductor is strong.” The bridge is customer allocation, HBM mix, capacity slot, ASP, order conversion, margin, and FCF. The theme is the heat; the bridge is the pipe that actually carries it into cash.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C06 rows | 21 |
| static C06 symbols | 16 |
| static C06 good/bad Stage2 | 6 / 4 |
| static C06 4B/4C | 2 / 2 |
| static C06 URL pending/proxy | 18 / 12 |
| static top covered symbols | 005290, 036540, 080220, 222800, 353200, 000660 |
| local C06 loop77 projected rows | 24 |
| this loop projected rows | 27 |

Selected symbols avoid the static C06 top-covered symbols and local loop77 C06 symbols `000660`, `005930`, and `000990`.

| symbol | company | status |
|---|---|---|
| 042700 | 한미반도체 | new C06 symbol versus static top-covered and local C06 loop |
| 089030 | 테크윙 | new C06 symbol versus static top-covered and local C06 loop |
| 095340 | ISC | new C06 symbol; cross-over with C08 but used here only as C06 bridge-failure counterexample |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C06 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 042700 / 2024-02-08 | true | true | clean_180D_window | true |
| 089030 / 2024-03-05 | true | true | clean_180D_window | true |
| 095340 / 2024-03-08 | true | true | clean_180D_window | true |

Corporate-action notes:

- 한미반도체 has corporate-action candidates before 2023; selected 2024 window is clean.
- 테크윙 has corporate-action candidates only in 2011 and 2022; selected 2024 window is clean.
- ISC has corporate-action candidates in 2014 and 2023; selected 2024 window is clean for this loop.
- 삼성전자 was not reused because it already appeared in local C06 loop77 and has a corporate-action caveat in its profile, although not in 2024.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_TC_BONDER_CUSTOMER_CAPACITY_ORDER_CAPA_4B_WATCH | C06 | HBM customer capacity / TC-bonder bottleneck route can open Stage2A, but needs 4B audit after rerating |
| HBM_TEST_HANDLER_CUSTOMER_CAPACITY_MIX_RERATING_4B_WATCH | C06 | HBM test-handler/customer capacity/mix rerating can work, but Green requires ASP/FCF conversion |
| HBM_SOCKET_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_REPEAT_DEMAND_BRIDGE | C06 | socket/customer capacity premium without repeat demand/margin bridge is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C06_HANMI_042700_2024_02_08_HBM_CUSTOMER_CAPACITY_TC_BONDER_RERATING | 042700 | 한미반도체 | 4B_overlay_success | positive | HBM customer/CAPA route produced extreme MFE, then large post-peak drawdown |
| C06_TECHWING_089030_2024_03_05_HBM_TEST_HANDLER_CUSTOMER_CAPACITY_RERATING | 089030 | 테크윙 | 4B_overlay_success | positive | HBM test-handler capacity/mix route produced >200% MFE, then cycle drawdown |
| C06_ISC_095340_2024_03_08_HBM_SOCKET_CUSTOMER_CAPACITY_FALSE_POSITIVE | 095340 | ISC | failed_rerating | counterexample | HBM socket/customer premium had limited MFE and severe MAE without repeat-demand bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 3 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 042700 | source_proxy_only | HBM customer capacity / TC-bonder order/CAPA route | required before promotion |
| 089030 | source_proxy_only | HBM test handler / customer capacity / HBM mix route | required before promotion |
| 095340 | source_proxy_only | HBM socket/customer capacity premium but qualification/repeat-demand bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 042700 | atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv | atlas/symbol_profiles/042/042700.json |
| 089030 | atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv | atlas/symbol_profiles/089/089030.json |
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY | Stage2-Actionable | 2024-02-08 | 2024-02-08 | 78500 | HBM customer capacity / TC-bonder bottleneck |
| TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY | Stage2-Actionable | 2024-03-05 | 2024-03-05 | 21950 | HBM test-handler / customer capacity / mix shift |
| ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY | Stage2 | 2024-03-08 | 2024-03-08 | 95000 | HBM socket/customer capacity premium without repeat-demand bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 042700 | 2024-02-08 | 78500 | 49.43 | -9.94 | 149.94 | -9.94 | 149.94 | -9.94 | 2024-06-14 | 196200 | -55.15 |
| 089030 | 2024-03-05 | 21950 | 78.13 | -4.56 | 222.55 | -4.56 | 222.55 | -4.56 | 2024-07-11 | 70800 | -57.63 |
| 095340 | 2024-03-08 | 95000 | 13.68 | -16.21 | 13.68 | -36.74 | 13.68 | -43.16 | 2024-03-28 | 108000 | -50.00 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 042700 | Stage2A/Yellow possible; 4B after extreme HBM rerating | extreme MFE and later large drawdown | current_profile_4B_too_late |
| 089030 | Stage2A/Yellow possible; 4B after HBM mix rerating | extreme MFE and later cycle drawdown | current_profile_4B_too_late |
| 095340 | Stage2 risk if socket/customer premium is over-credited | limited MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C06 interpretation:

- Stage2A can work when customer capacity, HBM mix, or capacity bottleneck evidence is visible before the full price rerating.
- Yellow/Green require customer conversion, HBM mix realization, ASP/margin bridge, revision, and FCF.
- HBM socket/test premium without repeat demand and margin bridge should not be promoted as C06 Stage2/Yellow.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 042700 | 1.00 | 1.00 | valuation rerating / positioning | extreme C06 rerating requires 4B audit |
| 089030 | 1.00 | 1.00 | HBM mix cycle peak | extreme MFE requires 4B audit |
| 095340 | 1.00 | 1.00 | event premium / customer bridge absent | not Stage3 without repeat-demand bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 042700 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 089030 | thesis_break_watch_only | not hard 4C, but HBM cycle/valuation cap needed |
| 095340 | hard_4c_late | qualification/repeat-demand/margin bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 AI/semiconductor names, HBM customer-capacity evidence can support Stage2A, but Stage3-Yellow/Green should require customer conversion, HBM mix realization, ASP/margin bridge, revision, and FCF. HBM-adjacent socket/test premiums without repeat-demand bridge should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C06_HBM_MEMORY_CUSTOMER_CAPACITY
confidence = medium
```

Candidate C06 rule:

```text
C06_hbm_customer_capacity_bridge_required =
  hbm_customer_capacity_or_mix_route
  AND (customer_conversion OR capacity_slot_lock OR asp_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if hbm_adjacent_premium and repeat_demand_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 80 and drawdown_after_peak < -40:
    add C06_peak_proximity_4B_audit = true

if MFE_90D < 20 and MAE_90D < -25:
    classify_as C06_hbm_bridge_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 128.72 | -17.08 | 128.72 | -19.22 | 1 | useful but C06 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 128.72 | -17.08 | 128.72 | -19.22 | 1 | over-credits HBM-adjacent premiums |
| P1 sector_specific_candidate_profile | L2 | 2 promoted + 1 guard | 186.25 | -7.25 | 186.25 | -7.25 | 0 | better after customer-capacity bridge gate |
| P2 canonical_archetype_candidate_profile | C06 | 2 promoted + 1 guard | 186.25 | -7.25 | 186.25 | -7.25 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C06 guard | 2 promoted + 1 guard | 186.25 | -7.25 | 186.25 | -7.25 | 0 | adds HBM bridge false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 042700 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 089030 | Stage2A aligned; 4B cycle audit late | current_profile_4B_too_late |
| 095340 | Stage2 false positive if repeat-demand bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | mixed C06 fine ids | 2 | 1 | 3 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> projected 27; still need 3 to reach 30 |

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
new_axis_proposed: C06_hbm_customer_capacity_bridge_required|C06_peak_proximity_4B_audit|C06_hbm_bridge_false_positive_guardrail
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
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
- Uses C06 Priority 0 coverage gap.
- Avoids static C06 top-covered symbols and local loop77 C06 symbols.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_hbm_customer_capacity_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"095340 shows HBM-adjacent premium can fail without repeat-demand/margin bridge while 042700/089030 work only as Stage2A with 4B audit","blocks 095340 false positive while preserving 042700/089030 Stage2A","HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY|TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY|ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C06_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"042700/089030 HBM customer-capacity reratings needed 4B audit after extreme MFE and peak drawdown","adds 4B audit after large C06 MFE without converting price-only peaks into Green","HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY|TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY",2,2,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C06_hbm_bridge_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"095340 had limited MFE and high MAE after HBM socket/customer premium","requires customer qualification/repeat demand/margin/FCF bridge before C06 Stage2/Yellow promotion","ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C06_HANMI_042700_2024_02_08_HBM_CUSTOMER_CAPACITY_TC_BONDER_RERATING","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TC_BONDER_CUSTOMER_CAPACITY_ORDER_CAPA_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM customer capacity and TC-bonder route captured extreme MFE, but later peak-to-drawdown required a C06 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C06 symbol versus static top-covered list and local C06 loop77 symbols; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C06_TECHWING_089030_2024_03_05_HBM_TEST_HANDLER_CUSTOMER_CAPACITY_RERATING","symbol":"089030","company_name":"테크윙","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_CUSTOMER_CAPACITY_MIX_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"HBM test-handler/customer capacity route captured >200% MFE, but cycle peak and later drawdown required C06 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C06 symbol; source_proxy_only evidence; not a pure C07 order-relative-strength case because this row emphasizes HBM capacity/mix conversion"}
{"row_type":"case","case_id":"C06_ISC_095340_2024_03_08_HBM_SOCKET_CUSTOMER_CAPACITY_FALSE_POSITIVE","symbol":"095340","company_name":"ISC","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_SOCKET_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_REPEAT_DEMAND_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"HBM socket/customer capacity premium produced limited MFE and then severe MAE when qualification/repeat-demand/margin bridge lagged","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"cross-over with C08; usable for C06 only as a customer-capacity bridge failure, not as pure socket/customer-quality promotion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY","case_id":"C06_HANMI_042700_2024_02_08_HBM_CUSTOMER_CAPACITY_TC_BONDER_RERATING","symbol":"042700","company_name":"한미반도체","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TC_BONDER_CUSTOMER_CAPACITY_ORDER_CAPA_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-08","entry_date":"2024-02-08","entry_price":78500.0,"evidence_available_at_that_date":"source_proxy_only: HBM customer capacity route, TC-bonder order/CAPA bottleneck, advanced packaging demand, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_customer_capacity_route","tc_bonder_order_route","advanced_packaging_bottleneck","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","order_conversion_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":49.43,"MFE_90D_pct":149.94,"MFE_180D_pct":149.94,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.94,"MAE_90D_pct":-9.94,"MAE_180D_pct":-9.94,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-14","peak_price":196200.0,"drawdown_after_peak_pct":-55.15,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"excellent_stage2a_but_extreme_peak_requires_C06_4B_audit","four_b_evidence_type":["valuation_rerating","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_042700_2024_02_08_78500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY","case_id":"C06_TECHWING_089030_2024_03_05_HBM_TEST_HANDLER_CUSTOMER_CAPACITY_RERATING","symbol":"089030","company_name":"테크윙","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_TEST_HANDLER_CUSTOMER_CAPACITY_MIX_RERATING_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":21950.0,"evidence_available_at_that_date":"source_proxy_only: HBM test-handler demand, customer capacity expansion, HBM mix shift, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_customer_capacity_route","hbm_test_handler_route","hbm_mix_shift","relative_strength"],"stage3_evidence_fields":["customer_capacity_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":78.13,"MFE_90D_pct":222.55,"MFE_180D_pct":222.55,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.56,"MAE_90D_pct":-4.56,"MAE_180D_pct":-4.56,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":70800.0,"drawdown_after_peak_pct":-57.63,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"excellent_stage2a_but_extreme_hbm_mix_rerating_requires_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_extreme_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_089030_2024_03_05_21950","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY","case_id":"C06_ISC_095340_2024_03_08_HBM_SOCKET_CUSTOMER_CAPACITY_FALSE_POSITIVE","symbol":"095340","company_name":"ISC","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_SOCKET_CUSTOMER_CAPACITY_PREMIUM_WITHOUT_REPEAT_DEMAND_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"hbm_memory_customer_capacity","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000.0,"evidence_available_at_that_date":"source_proxy_only: HBM socket/test customer capacity premium visible, but qualification, repeat demand, margin and FCF bridge were not confirmed; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["hbm_socket_premium","customer_capacity_expectation","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","weak_follow_through","customer_bridge_absent"],"stage4c_evidence_fields":["repeat_demand_bridge_absent","margin_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-16.21,"MAE_90D_pct":-36.74,"MAE_180D_pct":-43.16,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000.0,"drawdown_after_peak_pct":-50.0,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"hbm_socket_premium_not_C06_stage3_without_repeat_demand_margin_bridge","four_b_evidence_type":["event_premium","customer_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_limited_mfe_high_mae_customer_capacity_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C06_095340_2024_03_08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_HANMI_042700_2024_02_08_HBM_CUSTOMER_CAPACITY_TC_BONDER_RERATING","trigger_id":"HANMI_042700_2024_02_08_STAGE2A_HBM_CUSTOMER_CAPACITY","symbol":"042700","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":5,"relative_strength_score":10,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":75,"stage_label_after":"Stage2-Actionable with mandatory C06 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM customer/CAPA bridge worked, but extreme peak needs valuation decay unless margin/FCF conversion confirms Green.","MFE_90D_pct":149.94,"MAE_90D_pct":-9.94,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_TECHWING_089030_2024_03_05_HBM_TEST_HANDLER_CUSTOMER_CAPACITY_RERATING","trigger_id":"TECHWING_089030_2024_03_05_STAGE2A_HBM_TEST_HANDLER_CAPACITY","symbol":"089030","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow/Green-risk with 4B-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":5,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":10,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":72,"stage_label_after":"Stage2-Actionable with HBM mix/4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"HBM test-handler capacity rerating worked, but Green requires realized HBM mix, ASP, and FCF conversion.","MFE_90D_pct":222.55,"MAE_90D_pct":-4.56,"score_return_alignment_label":"positive_extreme_mfe_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_ISC_095340_2024_03_08_HBM_SOCKET_CUSTOMER_CAPACITY_FALSE_POSITIVE","trigger_id":"ISC_095340_2024_03_08_STAGE2_FALSE_POSITIVE_HBM_SOCKET_CAPACITY","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Stage2 false-positive / HBM socket capacity risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not C06 Stage2","changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Socket/customer capacity premium without qualification, repeat demand, margin, and FCF bridge should not receive C06 promotion.","MFE_90D_pct":13.68,"MAE_90D_pct":-36.74,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"97","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R2
completed_loop = 97
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

If this loop is accepted together with local loop77, C06 moves to projected 27 rows and still needs 3 more rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C06 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/042/042700.json
  - atlas/symbol_profiles/089/089030.json
  - atlas/symbol_profiles/095/095340.json
- Considered but not reused:
  - atlas/symbol_profiles/005/005930.json
  - atlas/symbol_profiles/007/007660.json
  - atlas/symbol_profiles/064/064760.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
