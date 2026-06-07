# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
schema_family = v12_sector_archetype_residual
selected_round = R1
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source = Songdaiki/stock-web
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. The already-applied global axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop tests whether C01 needs a **fresh margin/cash bridge requirement** before order/backlog labels can receive Stage2-Actionable treatment.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R1 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C01_ORDER_BACKLOG_MARGIN_BRIDGE |
| fine_archetype_id | SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE |
| scope logic | C01 belongs to R1/L1. Scope consistency passes. |

## 3. Previous Coverage / Duplicate Avoidance Check

`V12_Research_No_Repeat_Index.md` marks C01 as Priority 0 with 16 rows, 12 symbols, and top-covered symbols `082740`, `267270`, `010660`, `044450`, `054540`, `064820`.

This loop avoids those top-covered symbols and adds three C01 entries:

| symbol | name | novelty |
|---|---|---|
| 071970 | HD현대마린엔진 | new symbol for C01 table, ship-engine backlog + parent integration margin bridge |
| 077970 | STX엔진 | new symbol for C01 table, marine/defense engine order-to-delivery bridge |
| 010140 | 삼성중공업 | new C01 large-cap backlog late-chase counterexample |

Hard duplicate rule checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is intentionally a repeat of the top-covered C01 rows.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| manifest | atlas/manifest.json |
| schema | atlas/schema.json |
| universe | atlas/universe/all_symbols.csv |
| manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

## 5. Historical Eligibility Gate

All selected entries are historical, have entry rows in stock-web tradable shards, have 180D forward windows before the manifest max date, and are treated as calibration usable. Source URL detail is pending, so evidence is marked source-proxy-only, but price-path calibration is based on actual stock-web rows.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | compression logic |
|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | ship_engine_backlog_parent_integration_margin_bridge | backlog must connect to delivery, margin, and cash route |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | defense_marine_engine_order_backlog_delivery_bridge | order visibility is useful only if delivery acceptance and margin conversion are plausible |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | largecap_shipbuilder_backlog_late_chase_without_fresh_margin_bridge | backlog label alone after price extension should be weak-watch/4B-watch |

## 7. Case Selection Summary

| case_id | symbol | name | role | trigger | entry | price |
|---|---:|---|---|---|---|---:|
| C01_R1L100_071970_20240424 | 071970 | HD현대마린엔진 | structural_success | Stage2-Actionable | 2024-04-24 | 16500 |
| C01_R1L100_077970_20240424 | 077970 | STX엔진 | structural_success | Stage2-Actionable | 2024-04-24 | 14860 |
| C01_R1L100_010140_20240726 | 010140 | 삼성중공업 | failed_rerating | Stage2 | 2024-07-26 | 11870 |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| calibration_usable_case_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| new_symbol_count | 3 |
| new_trigger_family_count | 3 |

## 9. Evidence Source Map

| case_id | evidence family | evidence source status |
|---|---|---|
| C01_R1L100_071970_20240424 | ship engine backlog + HD Hyundai integration + delivery margin route | source_proxy_only / URL pending |
| C01_R1L100_077970_20240424 | marine/defense engine order backlog to delivery bridge | source_proxy_only / URL pending |
| C01_R1L100_010140_20240726 | large-cap shipbuilder backlog label late chase without fresh margin bridge | source_proxy_only / URL pending |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | caveat |
|---:|---|---|---|
| 071970 | atlas/symbol_profiles/071/071970.json | atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv | corporate action candidates are historical pre-2024; 2024/180D window treated clean |
| 077970 | atlas/symbol_profiles/077/077970.json | atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv | 2025-04-21 corporate-action candidate exists; selected 180D window ends before it |
| 010140 | atlas/symbol_profiles/010/010140.json | atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv | no selected 180D corporate-action contamination noted |

## 11. Case-by-Case Trigger Grid

| case_id | trigger_type | trigger_family | stage2 fields | current profile verdict |
|---|---|---|---|---|
| C01_R1L100_071970_20240424 | Stage2-Actionable | ship_engine_backlog_parent_integration_margin_bridge | backlog, delivery, customer/order quality, capacity route | current_profile_correct |
| C01_R1L100_077970_20240424 | Stage2-Actionable | defense_marine_engine_order_backlog_delivery_bridge | backlog, delivery, customer/order quality | current_profile_correct |
| C01_R1L100_010140_20240726 | Stage2 | largecap_shipbuilder_backlog_late_chase_without_fresh_margin_bridge | public event, relative strength, backlog label | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 071970 | 2024-04-24 | 16500 | 7.88 | -14.55 | 50.61 | -14.55 | 78.18 | -14.55 | 2025-01-15 | 29400 |
| 077970 | 2024-04-24 | 14860 | 5.85 | -12.45 | 64.20 | -13.26 | 71.94 | -13.26 | 2025-01-22 | 25550 |
| 010140 | 2024-07-26 | 11870 | 3.45 | -19.63 | 3.45 | -21.40 | 31.59 | -21.40 | 2025-02-19 | 15220 |

## 13. Current Calibrated Profile Stress Test

The current calibrated profile works for C01 when backlog has a clear order-to-delivery-to-margin route. It is too permissive when a large-cap backlog label is used after a local price extension without a fresh margin/cash bridge.

| case_id | profile verdict | actual path | stress result |
|---|---|---|---|
| 071970 | correct | strong 90D/180D MFE after early MAE | keep Stage2-Actionable if margin bridge exists |
| 077970 | correct | strong 90D/180D MFE after delivery/order route | keep Stage2-Actionable if delivery bridge exists |
| 010140 | false positive | high 90D MAE and delayed recovery | demote late-chase backlog label to weak-watch or 4B-watch |

## 14. Stage2 / Yellow / Green Comparison

No Stage3-Green trigger is used as representative. The audit is Stage2/Stage2-Actionable quality rather than Green lateness.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

For 010140, the local price extension around 2024-07-26 behaves like a C01 price-only 4B watch. It is not a full 4B thesis break because there was no non-price thesis deterioration, but it is enough to block fresh Stage2-Actionable promotion.

| symbol | local 4B proximity | full-window 4B proximity | verdict |
|---:|---:|---:|---|
| 010140 | 1.00 | 0.10 | price_only_local_4B_too_early_if_used_as_full_4B; valid as Stage2 promotion blocker |

## 16. 4C Protection Audit

No hard 4C is proposed. The C01 adjustment is a Stage2/4B-watch guard, not a thesis-break route.

```text
four_c_protection_score = not_applicable
hard_4c_verdict = thesis_break_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
candidate = L1 industrial order/backlog cases should require delivery/margin bridge for Stage2-Actionable when the entry follows a sector-wide price extension.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
candidate = C01 Stage2-Actionable requires at least two of:
  - signed or repeat order/backlog visibility
  - delivery/acceptance schedule
  - margin or cash conversion bridge
  - customer/parent integration quality
If only backlog label + relative strength exists after a local price extension, classify as Stage1/weak-watch or 4B-watch, not Stage2-Actionable.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive count | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 39.42 | -16.40 | 1 | useful but too permissive for backlog label late-chase |
| P1 sector_specific_candidate_profile | 2 | 57.41 | -13.91 | 0 | filters weak late chase |
| P2 canonical_archetype_candidate_profile | 2 | 57.41 | -13.91 | 0 | best C01 compression |
| P3 counterexample_guard_profile | 2 | 57.41 | -13.91 | 0 | strongest guard, may miss later-recovery large-cap case |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| C01_R1L100_071970_20240424 | 76 | Stage2-Actionable | 79 | Stage2-Actionable | correct positive |
| C01_R1L100_077970_20240424 | 76 | Stage2-Actionable | 79 | Stage2-Actionable | correct positive |
| C01_R1L100_010140_20240726 | 70 | Stage2 | 61 | Stage1/weak-watch | false positive reduced |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE | 2 | 1 | 1 | 0 | 3 | 0 | 3 | 3 | 1 | true | true | C01 16→19 rows if accepted; still below 30-row minimum |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: largecap_shipbuilder_backlog_label_late_chase, margin_bridge_missing_under_C01
new_axis_proposed: c01_margin_cash_bridge_required_for_stage2_actionable_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C01 local backlog-label blowoff
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
```

This loop adds 3 new independent cases, 1 counterexamples, and 1 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- actual stock-web 1D OHLC row path check
- entry_date / entry_price / MFE / MAE / peak / drawdown audit
- C01 canonical compression
- current calibrated profile stress test
```

Non-validation scope:

```text
- live candidate search
- current investment recommendation
- production scoring patch
- brokerage or trading API
- exact URL-level evidence verification
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_margin_cash_bridge_required_for_stage2_actionable,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 needs backlog to delivery/margin/cash bridge rather than backlog label alone","2 positives preserve Stage2-Actionable; late-chase counterexample is demoted","TRG_C01_R1L100_071970_20240424|TRG_C01_R1L100_077970_20240424|TRG_C01_R1L100_010140_20240726",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_late_chase_price_only_4b_watch,sector_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"large-cap shipbuilder backlog label after local blowoff should be 4B watch until fresh margin evidence arrives","reduces high-MAE Stage2 false positives","TRG_C01_R1L100_010140_20240726",1,1,1,low,sector_shadow_only,"not production; strengthens existing full_4b_requires_non_price_evidence for C01"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C01_R1L100_071970_20240424","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"ship_engine_backlog_parent_integration_margin_bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive MFE with tolerable early MAE; Stage2-Actionable worked only because non-price backlog/capacity bridge was present","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"STX중공업/HD현대마린엔진의 선박엔진 병목, HD현대 편입 기대, 엔진 납품/수주잔고가 납기·마진 bridge로 연결되는 구조. 가격만이 아니라 고객·인수·납품 capacity route가 같이 존재."}
{"row_type":"case","case_id":"C01_R1L100_077970_20240424","symbol":"077970","company_name":"STX엔진","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"defense_marine_engine_order_backlog_delivery_bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 entry had moderate early drawdown but strong 90D/180D MFE after order-to-delivery bridge became visible","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"엔진/방산/선박 부품 order backlog가 수주명목에서 납품·매출 전환으로 이어지는 C01형 사례. 2024년 중반 후반부 상대강도만이 아니라 엔진 수요·납품 visibility가 함께 존재."}
{"row_type":"case","case_id":"C01_R1L100_010140_20240726","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"largecap_shipbuilder_backlog_late_chase_without_fresh_margin_bridge","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"event/backlog label eventually recovered but entry quality was poor; early 90D MFE/MAE profile argues for fresh margin-cash bridge requirement","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"대형 조선 backlog headline과 sector beta는 있었지만, 해당 entry는 fresh order-to-margin bridge보다는 이미 진행된 가격 추격 성격이 강했다. Stage2 보너스만으로는 high-MAE late chase를 막기 어렵다."}
{"row_type":"trigger","trigger_id":"TRG_C01_R1L100_071970_20240424","case_id":"C01_R1L100_071970_20240424","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":16500,"evidence_available_at_that_date":"STX중공업/HD현대마린엔진의 선박엔진 병목, HD현대 편입 기대, 엔진 납품/수주잔고가 납기·마진 bridge로 연결되는 구조. 가격만이 아니라 고객·인수·납품 capacity route가 같이 존재.","evidence_source":"historical public-event proxy: ship-engine capacity/backlog and HD Hyundai integration route; source-url pending","trigger_family":"ship_engine_backlog_parent_integration_margin_bridge","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","capacity_or_volume_route","relative_strength"],"stage3_evidence_fields":["margin_bridge","repeat_order_or_conversion","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv","profile_path":"atlas/symbol_profiles/071/071970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.88,"MFE_90D_pct":50.61,"MFE_180D_pct":78.18,"MAE_30D_pct":-14.55,"MAE_90D_pct":-14.55,"MAE_180D_pct":-14.55,"peak_date":"2025-01-15","peak_price":29400,"drawdown_after_peak_pct":-22.96,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"071970_2024-04-24_16500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C01_R1L100_077970_20240424","case_id":"C01_R1L100_077970_20240424","symbol":"077970","company_name":"STX엔진","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":14860,"evidence_available_at_that_date":"엔진/방산/선박 부품 order backlog가 수주명목에서 납품·매출 전환으로 이어지는 C01형 사례. 2024년 중반 후반부 상대강도만이 아니라 엔진 수요·납품 visibility가 함께 존재.","evidence_source":"historical public-event proxy: defense/marine engine order and delivery bridge; source-url pending","trigger_family":"defense_marine_engine_order_backlog_delivery_bridge","stage2_evidence_fields":["backlog_or_delivery_visibility","customer_or_order_quality","relative_strength"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","margin_bridge"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv","profile_path":"atlas/symbol_profiles/077/077970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.85,"MFE_90D_pct":64.2,"MFE_180D_pct":71.94,"MAE_30D_pct":-12.45,"MAE_90D_pct":-13.26,"MAE_180D_pct":-13.26,"peak_date":"2025-01-22","peak_price":25550,"drawdown_after_peak_pct":-21.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"077970_2024-04-24_14860","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_C01_R1L100_010140_20240726","case_id":"C01_R1L100_010140_20240726","symbol":"010140","company_name":"삼성중공업","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","loop_objective":"coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-07-26","entry_date":"2024-07-26","entry_price":11870,"evidence_available_at_that_date":"대형 조선 backlog headline과 sector beta는 있었지만, 해당 entry는 fresh order-to-margin bridge보다는 이미 진행된 가격 추격 성격이 강했다. Stage2 보너스만으로는 high-MAE late chase를 막기 어렵다.","evidence_source":"historical public-event proxy: shipbuilding backlog label and sector beta without fresh company-specific margin bridge; source-url pending","trigger_family":"largecap_shipbuilder_backlog_late_chase_without_fresh_margin_bridge","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","backlog_or_delivery_visibility"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv","profile_path":"atlas/symbol_profiles/010/010140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.45,"MFE_90D_pct":3.45,"MFE_180D_pct":31.59,"MAE_30D_pct":-19.63,"MAE_90D_pct":-21.4,"MAE_180D_pct":-21.4,"peak_date":"2025-02-19","peak_price":15220,"drawdown_after_peak_pct":-19.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":0.1,"trigger_outcome_label":"counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"010140_2024-07-26_11870","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L100_071970_20240424","trigger_id":"TRG_C01_R1L100_071970_20240424","symbol":"071970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":15,"margin_bridge_score":13,"revision_score":8,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":9,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"C01 shadow profile requires order/backlog to delivery+margin+cash bridge; price-only/sector-beta late chase loses Stage2-Actionable eligibility.","MFE_90D_pct":50.61,"MAE_90D_pct":-14.55,"score_return_alignment_label":"positive MFE with tolerable early MAE; Stage2-Actionable worked only because non-price backlog/capacity bridge was present","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L100_077970_20240424","trigger_id":"TRG_C01_R1L100_077970_20240424","symbol":"077970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":12,"backlog_visibility_score":15,"margin_bridge_score":13,"revision_score":8,"relative_strength_score":9,"customer_quality_score":9,"policy_or_regulatory_score":2,"valuation_repricing_score":5,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":12,"backlog_visibility_score":15,"margin_bridge_score":15,"revision_score":9,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":4,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":1},"weighted_score_after":79,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"C01 shadow profile requires order/backlog to delivery+margin+cash bridge; price-only/sector-beta late chase loses Stage2-Actionable eligibility.","MFE_90D_pct":64.2,"MAE_90D_pct":-13.26,"score_return_alignment_label":"Stage2 entry had moderate early drawdown but strong 90D/180D MFE after order-to-delivery bridge became visible","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C01_R1L100_010140_20240726","trigger_id":"TRG_C01_R1L100_010140_20240726","symbol":"010140","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":12,"customer_quality_score":4,"policy_or_regulatory_score":2,"valuation_repricing_score":8,"execution_risk_score":10,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":3},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":8,"backlog_visibility_score":10,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":4,"execution_risk_score":13,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":61,"stage_label_after":"Stage1/weak-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","relative_strength_score"],"component_delta_explanation":"C01 shadow profile requires order/backlog to delivery+margin+cash bridge; price-only/sector-beta late chase loses Stage2-Actionable eligibility.","MFE_90D_pct":3.45,"MAE_90D_pct":-21.4,"score_return_alignment_label":"event/backlog label eventually recovered but entry quality was poor; early 90D MFE/MAE profile argues for fresh margin-cash bridge requirement","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["largecap_shipbuilder_backlog_label_late_chase","margin_bridge_missing_under_C01"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"coverage_matrix","round":"R1","loop":"100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_AND_OFFSHORE_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_LARGECAP_SHIPBUILDER_LATE_CHASE","positive_case_count":2,"counterexample_count":1,"4B_case_count":1,"4C_case_count":0,"new_independent_case_count":3,"reused_case_count":0,"calibration_usable_trigger_count":3,"representative_trigger_count":3,"current_profile_error_count":1,"sector_rule_candidate":true,"canonical_rule_candidate":true,"coverage_gap_after_this_loop":"C01 16→19 rows if accepted; still below 30-row minimum"}
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
completed_round = R1
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was treated as the main execution procedure.
- `docs/core/V12_Research_No_Repeat_Index.md` was treated only as duplicate-prevention and coverage-selection ledger.
- `Songdaiki/stock-web` manifest confirms `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`.
- Case price rows were read from:
  - `atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/071/071970/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/077/077970/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv`
