# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_72_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
selected_round: R2
selected_loop: 72
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id: SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND
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

This loop adds 3 new independent cases, 1 counterexample, and 3 current-profile stress findings for R2/L2/C08.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed globally. This loop only stress-tests them inside C08:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `stage3_green_total_min`
- `stage3_green_revision_min`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C08 -> C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

C08 is interpreted as semiconductor test socket / probe / test-board customer-quality work where the key bridge is:

```text
customer qualification -> repeat consumable/test demand -> revenue conversion -> margin durability
```

Price strength alone is not C08 Stage2/Stage3 evidence. A small-cap socket sympathy rally without named customer qualification, repeat shipment, margin bridge, or revision is treated as a false-positive or 4B-watch path.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C08 current rows | 14 |
| C08 current symbols | 11 |
| C08 good/bad Stage2 | 4 / 4 |
| C08 4B/4C | 2 / 2 |
| C08 URL pending/proxy | 14 / 9 |
| top covered symbols | 098120, 080580, 058470, 067310, 092870, 097800 |

Selected symbols for this loop:

| symbol | company | duplicate status |
|---|---|---|
| 095340 | ISC | new symbol versus top covered C08 list |
| 131290 | 티에스이 | new symbol versus top covered C08 list |
| 425420 | 티에프이 | new symbol versus top covered C08 list |

Hard duplicate rule checked against the available No-Repeat summary:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the index summary.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web atlas validation:

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream | FinanceData/marcap |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| manifest max_date | 2026-02-20 |
| calibration shard root | atlas/ohlcv_tradable_by_symbol_year |
| raw shard root | atlas/ohlcv_raw_by_symbol_year |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate action window | calibration usable |
|---|---:|---:|---|---:|
| 095340 / 2024-02-22 | true | true | clean_180D_window | true |
| 131290 / 2024-02-13 | true | true | clean_180D_window | true |
| 425420 / 2024-03-08 | true | true | clean_180D_window | true |

Corporate-action notes:

- ISC profile has corporate-action candidates on 2014-12-26 and 2023-10-20; the selected 2024-02-22 to 2024-180D window does not overlap.
- 티에스이 profile has candidates only in 2011; the selected 2024 window is clean.
- 티에프이 profile has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND | C08 | customer qualification / repeat socket demand / margin durability |
| PROBE_CARD_TEST_BOARD_SOCKET_CUSTOMER_QUALITY | C08 | probe/test board route is retained as C08 if customer quality and repeat demand are the core evidence |
| TEST_SOCKET_SMALL_CAP_CUSTOMER_BRIDGE_ABSENT | C08 | small-cap socket exposure without qualification bridge is C08 counterexample |

## 7. Case Selection Summary

| case_id | symbol | company | case role | polarity | why selected |
|---|---|---|---|---|---|
| C08_ISC_095340_2024_02_22_SOCKET_QUALIFICATION_RERATING | 095340 | ISC | 4B_overlay_success | positive | early C08 signal captured strong MFE, but full-cycle drawdown demands 4B audit |
| C08_TSE_131290_2024_02_13_PROBE_CARD_SOCKET_RERATING | 131290 | 티에스이 | high_mae_success | positive | strong 90D MFE with later high MAE; useful for 4B timing |
| C08_TFE_425420_2024_03_08_SOCKET_THEME_FALSE_POSITIVE | 425420 | 티에프이 | failed_rerating | counterexample | socket-theme sympathy without customer/revision bridge collapsed |

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

The evidence field is intentionally conservative because this loop uses source-proxy evidence and does not repair URLs.

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 095340 | source_proxy_only | socket/customer-quality route, relative-strength plus sector test-socket route | required before promotion |
| 131290 | source_proxy_only | probe/test board route, customer-quality route, relative-strength | required before promotion |
| 425420 | source_proxy_only | socket exposure but no named customer/revision bridge | required before promotion |

This loop does not use price action alone to promote Stage2/Stage3. The counterexample explicitly shows why C08 requires a customer-quality bridge.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json |
| 425420 | atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv | atlas/symbol_profiles/425/425420.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION | Stage2-Actionable | 2024-02-22 | 2024-02-22 | 75000 | socket/customer-quality route and sector HBM test-socket beta; source proxy |
| TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION | Stage2-Actionable | 2024-02-13 | 2024-02-13 | 57000 | probe/test board and socket route; source proxy |
| TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME | Stage2 | 2024-03-08 | 2024-03-08 | 38850 | socket exposure but customer/revision bridge absent; source proxy |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 095340 | 2024-02-22 | 75000 | 44.00 | -8.13 | 44.00 | -19.87 | 44.00 | -40.40 | 2024-03-28 | 108000 | -58.61 |
| 131290 | 2024-02-13 | 57000 | 15.09 | -13.07 | 54.04 | -13.07 | 54.04 | -31.84 | 2024-05-03 | 87800 | -55.75 |
| 425420 | 2024-03-08 | 38850 | 13.13 | -15.96 | 13.13 | -29.21 | 13.13 | -70.68 | 2024-03-21 | 43950 | -74.08 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 095340 | Stage2A/Yellow possible; 4B only if non-price evidence appears | strong MFE but deep full-cycle drawdown | current_profile_4B_too_late |
| 131290 | Stage2A/Yellow possible | strong MFE90 but high post-peak drawdown | current_profile_4B_too_late |
| 425420 | Stage2 risk if relative-strength/socket exposure over-credited | 13% local MFE then -70% 180D MAE | current_profile_false_positive |

Answers to required stress-test questions:

1. Stage2 bonus was useful for 095340 and 131290, but too generous for 425420 without a customer-quality bridge.
2. Yellow threshold 75 is acceptable only when repeat demand or margin bridge is visible.
3. Green threshold 87 / revision 55 should remain strict for C08.
4. Price-only blowoff guard is correct but needs C08-specific customer bridge language.
5. Full 4B non-price requirement is directionally correct; however C08 needs a “peak-proximity audit” even when only price evidence exists.
6. Hard 4C routing should not wait for catastrophic MAE in small-cap socket cases if qualification/revision evidence fails to appear.

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C08 interpretation:

- Stage2A can be early and useful when customer quality / socket demand / repeat consumable route is present.
- Stage3-Yellow must wait for margin bridge or revision confirmation.
- Stage3-Green should require customer qualification, repeat demand, revenue conversion, and margin durability.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 095340 | 1.00 | 1.00 | price_only / valuation_blowoff | price peak was useful but requires non-price 4B confirmation |
| 131290 | 1.00 | 1.00 | price_only / valuation_blowoff | full-window peak identified, but non-price 4B evidence missing |
| 425420 | 1.00 | 1.00 | price_only / valuation_blowoff | local 4B was too price-only; better treated as Stage2 false-positive guard |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 095340 | thesis_break_watch_only | no explicit 4C trigger; 4B watch should have capped optimism |
| 131290 | thesis_break_watch_only | no explicit 4C trigger; post-peak drawdown argues for earlier 4B |
| 425420 | hard_4c_late | customer-quality bridge absence should have blocked Stage2 before large drawdown |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = low_to_medium
```

Candidate:

> In L2 semiconductor test/socket names, relative strength and HBM beta can open Stage2A, but Stage3-Yellow/Green requires either customer qualification evidence, repeat consumable demand, margin bridge, or confirmed revision. Without that bridge, local price MFE should be treated as 4B-watch or false-positive stress evidence, not as structural Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
confidence = low_to_medium
```

Candidate C08 rule:

```text
C08_stage2_bridge_required =
  customer_qualification
  OR repeat_socket_consumable_demand
  OR named_customer_test_socket_route
  OR margin/revision bridge

if relative_strength_only and no customer_quality_bridge:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -50:
    add C08_peak_proximity_4B_audit = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 37.06 | -20.72 | 37.06 | -47.64 | 1 | useful but C08 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 37.06 | -20.72 | 37.06 | -47.64 | 1 | too price/relative-strength sensitive |
| P1 sector_specific_candidate_profile | L2 | 3 | 49.02 | -16.47 | 49.02 | -36.12 | 0 | better if TFE is blocked |
| P2 canonical_archetype_candidate_profile | C08 | 3 | 49.02 | -16.47 | 49.02 | -36.12 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C08 guard | 3 | 49.02 | -16.47 | 49.02 | -36.12 | 0 | same as P2 plus hard bridge gate |

P1/P2/P3 averages exclude the TFE false-positive from positive promotion while keeping it as a counterexample/guardrail row.

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 095340 | Stage2A aligned; Green blocked; 4B watch needed | current_profile_4B_too_late |
| 131290 | Stage2A aligned; 4B watch late | current_profile_4B_too_late |
| 425420 | Stage2 false positive if bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | mixed C08 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 14 -> 17 rows, need 13 to reach 30 |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - stage2_actionable_evidence_bonus
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C08_stage2_customer_quality_bridge_required
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
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
- Uses C08 Priority 0 coverage gap.
- Uses three new symbols versus the C08 top-covered list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence is source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C08_stage2_customer_quality_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 false positive appears when socket exposure lacks customer qualification/repeat demand/revision bridge","blocks 425420 false positive while preserving 095340/131290 Stage2A","ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION|TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION|TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C08_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 winners can show high MFE then >50% drawdown; require peak-proximity audit when non-price 4B evidence is absent","captures 095340/131290 high-MAE success as 4B-watch rather than Green","ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION|TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION",2,2,0,low_to_medium,canonical_shadow_only,"do not convert price-only peak into full 4B without non-price evidence"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C08_ISC_095340_2024_02_22_SOCKET_QUALIFICATION_RERATING","symbol":"095340","company_name":"ISC","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early Stage2A captured 44% MFE before later 4B/drawdown","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C08 symbol versus top covered C08 list; source_proxy_only evidence needs URL repair before promotion"}
{"row_type":"case","case_id":"C08_TSE_131290_2024_02_13_PROBE_CARD_SOCKET_RERATING","symbol":"131290","company_name":"티에스이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_TEST_BOARD_SOCKET_CUSTOMER_QUALITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"MFE90 > 50% but full-cycle drawdown after peak exceeded 55%","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C08 symbol; useful as positive plus 4B timing stress case"}
{"row_type":"case","case_id":"C08_TFE_425420_2024_03_08_SOCKET_THEME_FALSE_POSITIVE","symbol":"425420","company_name":"티에프이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_SMALL_CAP_CUSTOMER_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"local MFE faded into -70% 180D MAE; customer/revision bridge was missing","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C08 symbol; counterexample for socket-theme beta without customer-quality bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION","case_id":"C08_ISC_095340_2024_02_22_SOCKET_QUALIFICATION_RERATING","symbol":"095340","company_name":"ISC","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_CUSTOMER_QUALIFICATION_REPEAT_DEMAND","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":75000.0,"evidence_available_at_that_date":"source_proxy_only: semi test socket/customer qualification narrative, sector HBM/test-socket re-rating, and tradable OHLC reaction available by entry date; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["customer_quality_route","test_socket_exposure","relative_strength","sector_hbm_test_socket_beta"],"stage3_evidence_fields":["repeat_demand_unconfirmed","margin_bridge_partial","revision_confirmation_pending"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.0,"MFE_90D_pct":44.0,"MFE_180D_pct":44.0,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.13,"MAE_90D_pct":-19.87,"MAE_180D_pct":-40.4,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000.0,"drawdown_after_peak_pct":-58.61,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_peak_requires_non_price_4B_confirmation","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_but_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_095340_2024_02_22_75000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION","case_id":"C08_TSE_131290_2024_02_13_PROBE_CARD_SOCKET_RERATING","symbol":"131290","company_name":"티에스이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"PROBE_CARD_TEST_BOARD_SOCKET_CUSTOMER_QUALITY","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":57000.0,"evidence_available_at_that_date":"source_proxy_only: probe/test board and socket exposure with HBM/advanced package test demand route; URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["probe_card_test_board_route","relative_strength","customer_quality_route"],"stage3_evidence_fields":["margin_bridge_pending","repeat_order_or_conversion_pending"],"stage4b_evidence_fields":["price_extension","full_window_peak_then_drawdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.09,"MFE_90D_pct":54.04,"MFE_180D_pct":54.04,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-13.07,"MAE_90D_pct":-13.07,"MAE_180D_pct":-31.84,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800.0,"drawdown_after_peak_pct":-55.75,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_price_peak_but_non_price_4B_evidence_missing","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_high_mae","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_131290_2024_02_13_57000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME","case_id":"C08_TFE_425420_2024_03_08_SOCKET_THEME_FALSE_POSITIVE","symbol":"425420","company_name":"티에프이","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_SMALL_CAP_CUSTOMER_BRIDGE_ABSENT","sector":"AI/semiconductor/electronics","primary_archetype":"semi_test_socket_customer_quality","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":38850.0,"evidence_available_at_that_date":"source_proxy_only: test socket exposure and sector sympathy visible, but named customer qualification / repeat consumable / revision bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["test_socket_exposure","relative_strength"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv","profile_path":"atlas/symbol_profiles/425/425420.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.13,"MFE_90D_pct":13.13,"MFE_180D_pct":13.13,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.96,"MAE_90D_pct":-29.21,"MAE_180D_pct":-70.68,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":43950.0,"drawdown_after_peak_pct":-74.08,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_bridge","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_high_mae_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C08_425420_2024_03_08_38850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_ISC_095340_2024_02_22_SOCKET_QUALIFICATION_RERATING","trigger_id":"ISC_095340_2024_02_22_STAGE2A_SOCKET_QUALIFICATION","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow/4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with early 4B-watch","changed_components":["valuation_repricing_score","execution_risk_score","revision_score"],"component_delta_explanation":"C08 customer-quality route deserves Stage2A credit, but price peak without non-price 4B evidence should cap Green and add 4B watch.","MFE_90D_pct":44.0,"MAE_90D_pct":-19.87,"score_return_alignment_label":"stage2_good_green_guard_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_TSE_131290_2024_02_13_PROBE_CARD_SOCKET_RERATING","trigger_id":"TSE_131290_2024_02_13_STAGE2A_PROBE_TEST_REACCELERATION","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable/Yellow candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":3,"revision_score":4,"relative_strength_score":8,"customer_quality_score":7,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable with peak-proximity 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Large MFE proves C08 can work, but post-peak drawdown says valuation room must decay quickly unless repeat order/revision bridge is visible.","MFE_90D_pct":54.04,"MAE_90D_pct":-13.07,"score_return_alignment_label":"positive_but_high_mae_4b_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C08_TFE_425420_2024_03_08_SOCKET_THEME_FALSE_POSITIVE","trigger_id":"TFE_425420_2024_03_08_STAGE2_FALSE_POSITIVE_SOCKET_THEME","symbol":"425420","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":1,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1/4B-watch, not Stage2","changed_components":["customer_quality_score","valuation_repricing_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"Socket exposure alone is not customer-quality evidence; no named qualification/repeat demand/revision bridge, so C08 Stage2 bridge should be required.","MFE_90D_pct":13.13,"MAE_90D_pct":-29.21,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"72","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage2_actionable_evidence_bonus"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 72
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

After this loop, C08 moves from 14 to a projected 17 rows if all three representative rows are accepted. It remains below 30-row minimum stability, so C08 can still be selected again, but the next C08 run should prefer new symbols or verified URL repair.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/095/095340.json
  - atlas/symbol_profiles/131/131290.json
  - atlas/symbol_profiles/425/425420.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
