# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R2_loop_101_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
selected_round: R2
selected_loop: 101
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_ALD_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH
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

This loop adds 3 new independent C10 rows and moves C10 from static 21 rows to local projected 24 after loop99, 27 after loop100, and 30 after this loop. The minimum 30-row stability threshold is reached.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C10:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R2 -> L2_AI_SEMICONDUCTOR_ELECTRONICS
C10 -> C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

C10 is the memory recovery / equipment-cycle archetype. The usable bridge is the conversion chain:

```text
memory recovery / capex restart -> order conversion -> utilization -> OPM/revision -> FCF
```

The cycle label is the weather. The conversion bridge is the actual road.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| static C10 rows | 21 |
| static C10 symbols | 18 |
| static C10 good/bad Stage2 | 6 / 6 |
| static C10 4B/4C | 3 / 3 |
| static C10 URL pending/proxy | 18 / 12 |
| static top covered symbols | 036930, 074600, 003160, 031980, 036540, 039030 |
| local C10 loop99 projected rows | 24 |
| local C10 loop100 projected rows | 27 |
| this loop projected rows | 30 |

Selected symbols avoid the static top-covered symbols, loop99 symbols `095610`, `166090`, `083310`, and loop100 symbols `240810`, `319660`, `014680`.

| symbol | company | status |
|---|---|---|
| 084370 | 유진테크 | new C10 symbol versus static and local loops |
| 039440 | 에스티아이 | new C10 symbol versus static and local loops |
| 131290 | 티에스이 | new C10 symbol; reduced weight due to C10/C08 boundary |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary or local generated C10 memory.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 084370 / 2024-03-06 | true | true | clean_180D_window | true |
| 039440 / 2024-03-06 | true | true | clean_180D_window | true |
| 131290 / 2024-03-06 | true | true | clean_180D_window | true |

Corporate-action notes:

- 유진테크 has corporate-action candidates only in 2007, 2010, and 2012.
- 에스티아이 has corporate-action candidates only in 2002, 2006, and 2018.
- 티에스이 has corporate-action candidates only in 2011.
- 제우스(079370) was considered but rejected because its profile has 2024 corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| MEMORY_ALD_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH | C10 | ALD/equipment recovery can open Stage2A, but order/margin/FCF must follow |
| MEMORY_INFRA_EQUIPMENT_RECOVERY_PREMIUM_ORDER_MARGIN_BRIDGE_FAIL | C10 | infra/equipment recovery spike without bridge is false-positive risk |
| MEMORY_TEST_INTERFACE_RECOVERY_PREMIUM_WITHOUT_MARGIN_REVISION_BRIDGE | C10 | test-interface premium needs margin/revision bridge; otherwise false-positive |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C10_EUGENETECH_084370_2024_03_06_MEMORY_ALD_EQUIPMENT_RECOVERY_4B | 084370 | 유진테크 | 4B_overlay_success | positive | ALD/equipment recovery produced 65% MFE and later cycle drawdown |
| C10_STI_039440_2024_03_06_MEMORY_INFRA_EQUIPMENT_PREMIUM_FALSE_POSITIVE | 039440 | 에스티아이 | failed_rerating | counterexample | recovery premium had mid-MFE but severe MAE without order/margin bridge |
| C10_TSE_131290_2024_03_06_MEMORY_TEST_INTERFACE_RECOVERY_FALSE_POSITIVE | 131290 | 티에스이 | failed_rerating | counterexample | test-interface premium had mid-MFE and high MAE without margin/revision bridge |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 1 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 084370 | source_proxy_only | ALD/memory equipment recovery and order-cycle route | required before promotion |
| 039440 | source_proxy_only | memory infra equipment premium but order/margin bridge absent | required; useful as counterexample |
| 131290 | source_proxy_only | memory test-interface premium but margin/revision bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 084370 | atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv | atlas/symbol_profiles/084/084370.json |
| 039440 | atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv | atlas/symbol_profiles/039/039440.json |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 36250 | memory ALD/equipment recovery |
| STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY | Stage2 | 2024-03-06 | 2024-03-06 | 35850 | memory infra-equipment premium without bridge |
| TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE | Stage2 | 2024-03-06 | 2024-03-06 | 57500 | memory test-interface recovery premium without bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 084370 | 2024-03-06 | 36250 | 51.45 | -4.97 | 65.52 | -4.97 | 65.52 | -5.52 | 2024-05-28 | 60000 | -42.92 |
| 039440 | 2024-03-06 | 35850 | 20.64 | -13.25 | 20.64 | -25.94 | 20.64 | -48.12 | 2024-03-13 | 43250 | -56.99 |
| 131290 | 2024-03-06 | 57500 | 20.35 | -4.35 | 20.35 | -27.83 | 20.35 | -33.83 | 2024-04-04 | 69200 | -45.01 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 084370 | Stage2A/Yellow possible; 4B after ALD recovery rerating | high MFE, controlled MAE, later drawdown | current_profile_4B_too_late |
| 039440 | Stage2 risk if recovery premium is over-credited | mid-MFE and high 180D MAE | current_profile_false_positive |
| 131290 | Stage2 risk if test-interface recovery premium is over-credited | mid-MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C10 interpretation:

- Stage2A can work when equipment recovery is tied to order conversion and the first recovery leg is not already pure event premium.
- Yellow/Green require realized order, OPM, revision, and FCF.
- Infra/test-interface recovery premium without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 084370 | 1.00 | 1.00 | memory equipment cycle / valuation rerating | 4B audit required after recovery peak |
| 039440 | 1.00 | 1.00 | event premium / weak follow-through | not Stage3 without order/margin bridge |
| 131290 | 1.00 | 1.00 | test-interface premium / bridge absent | not Stage3 without margin/revision bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 084370 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 039440 | hard_4c_late | order/margin bridge absence should have capped Stage2 earlier |
| 131290 | hard_4c_late | margin/revision bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L2_AI_SEMICONDUCTOR_ELECTRONICS
confidence = medium
```

Candidate:

> In L2 semiconductor names, memory recovery can support Stage2A only when tied to order conversion, utilization, margin bridge, revision, or FCF. Event-like equipment/test-interface premiums without that bridge should not become Yellow/Green.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
confidence = medium
```

Candidate C10 rule:

```text
C10_memory_cycle_conversion_bridge_required =
  memory_recovery_or_equipment_cycle_route
  AND (order_conversion OR utilization_bridge OR margin_bridge OR confirmed_revision OR fcf_conversion)

if recovery_premium and conversion_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 25 and drawdown_after_peak < -35:
    add C10_peak_proximity_4B_audit = true

if MFE_90D < 25 and MAE_90D < -20:
    classify_as C10_memory_equipment_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 35.5 | -19.58 | 35.5 | -29.16 | 2 | useful but C10 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 35.5 | -19.58 | 35.5 | -29.16 | 2 | over-credits recovery premiums |
| P1 sector_specific_candidate_profile | L2 | 1 promoted + 2 guard | 65.52 | -4.97 | 65.52 | -5.52 | 0 | better after conversion bridge gate |
| P2 canonical_archetype_candidate_profile | C10 | 1 promoted + 2 guard | 65.52 | -4.97 | 65.52 | -5.52 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C10 guard | 1 promoted + 2 guard | 65.52 | -4.97 | 65.52 | -5.52 | 0 | adds recovery-premium false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 084370 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 039440 | Stage2 false positive if order/margin bridge not enforced | current_profile_false_positive |
| 131290 | Stage2 false positive if margin/revision bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | mixed C10 fine ids | 1 | 2 | 1 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 21 -> local 24 -> local 27 -> projected 30; reaches minimum stability threshold |

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
new_axis_proposed: C10_memory_cycle_conversion_bridge_required|C10_peak_proximity_4B_audit|C10_memory_equipment_false_positive_guardrail
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
- Uses C10 Priority 0 coverage gap.
- Avoids static C10 top-covered symbols and local loop99/100 symbols.
- Rejects 079370 because of 2024 corporate-action candidate contamination risk.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_memory_cycle_conversion_bridge_required,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"039440/131290 show recovery premiums can fail without order/margin/revision bridge while 084370 works only as Stage2A with 4B audit","blocks two false positives while preserving 084370 Stage2A","EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY|STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY|TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C10_peak_proximity_4B_audit,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"084370 memory ALD/equipment recovery needed 4B audit after 65% MFE and drawdown","adds 4B audit after large C10 MFE without converting price-only cycle peaks into Green","EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY",1,1,0,medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C10_memory_equipment_false_positive_guardrail,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"039440/131290 had mid-MFE but high MAE after memory recovery premiums","requires order/margin/revision/FCF bridge before Stage2/Yellow promotion","STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY|TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C10_EUGENETECH_084370_2024_03_06_MEMORY_ALD_EQUIPMENT_RECOVERY_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_ALD_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"memory ALD/equipment recovery route captured 65% MFE with contained early MAE, but later cycle drawdown required C10 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C10 symbol versus static top-covered list and local loop99/100 symbols; 2024 window clean"}
{"row_type":"case","case_id":"C10_STI_039440_2024_03_06_MEMORY_INFRA_EQUIPMENT_PREMIUM_FALSE_POSITIVE","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_INFRA_EQUIPMENT_RECOVERY_PREMIUM_ORDER_MARGIN_BRIDGE_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"memory/infrastructure equipment recovery premium had only ~21% MFE and then severe MAE without sustained order/margin bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C10 symbol; counterexample for memory equipment premium with weak conversion bridge"}
{"row_type":"case","case_id":"C10_TSE_131290_2024_03_06_MEMORY_TEST_INTERFACE_RECOVERY_FALSE_POSITIVE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_INTERFACE_RECOVERY_PREMIUM_WITHOUT_MARGIN_REVISION_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.9,"score_price_alignment":"memory test-interface recovery premium produced only ~20% MFE and then high MAE without margin/revision bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"borderline C10/C08 case; counted with reduced weight because test-interface customer-quality could belong to C08"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY","case_id":"C10_EUGENETECH_084370_2024_03_06_MEMORY_ALD_EQUIPMENT_RECOVERY_4B","symbol":"084370","company_name":"유진테크","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_ALD_EQUIPMENT_RECOVERY_ORDER_MARGIN_4B_WATCH","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":36250.0,"evidence_available_at_that_date":"source_proxy_only: memory capex recovery, ALD/equipment order-cycle route, customer capex restart, and relative strength visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_capex_recovery","ald_equipment_order_route","customer_capex_restart","relative_strength"],"stage3_evidence_fields":["order_conversion_partial","margin_bridge_pending","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":51.45,"MFE_90D_pct":65.52,"MFE_180D_pct":65.52,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.97,"MAE_90D_pct":-4.97,"MAE_180D_pct":-5.52,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-42.92,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_stage2a_but_memory_equipment_cycle_peak_requires_4B_audit","four_b_evidence_type":["valuation_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_084370_2024_03_06_36250","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY","case_id":"C10_STI_039440_2024_03_06_MEMORY_INFRA_EQUIPMENT_PREMIUM_FALSE_POSITIVE","symbol":"039440","company_name":"에스티아이","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_INFRA_EQUIPMENT_RECOVERY_PREMIUM_ORDER_MARGIN_BRIDGE_FAIL","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":35850.0,"evidence_available_at_that_date":"source_proxy_only: memory infrastructure/equipment recovery premium and relative strength visible, but realized order, margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_equipment_recovery_premium","infra_equipment_theme","relative_strength_spike"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_spike","weak_follow_through","order_margin_bridge_absent"],"stage4c_evidence_fields":["order_conversion_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv","profile_path":"atlas/symbol_profiles/039/039440.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.64,"MFE_90D_pct":20.64,"MFE_180D_pct":20.64,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-13.25,"MAE_90D_pct":-25.94,"MAE_180D_pct":-48.12,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-13","peak_price":43250.0,"drawdown_after_peak_pct":-56.99,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"memory_infra_recovery_spike_not_stage3_without_order_margin_revision_bridge","four_b_evidence_type":["event_spike","weak_follow_through"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_order_margin_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_039440_2024_03_06_35850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE","case_id":"C10_TSE_131290_2024_03_06_MEMORY_TEST_INTERFACE_RECOVERY_FALSE_POSITIVE","symbol":"131290","company_name":"티에스이","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_TEST_INTERFACE_RECOVERY_PREMIUM_WITHOUT_MARGIN_REVISION_BRIDGE","sector":"AI / semiconductor / electronics","primary_archetype":"memory_recovery_equipment_cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":57500.0,"evidence_available_at_that_date":"source_proxy_only: memory test-interface recovery premium and semiconductor cycle rebound visible, but realized margin, revision, repeat-demand, and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["memory_test_interface_recovery_premium","semiconductor_cycle_rebound"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["event_premium","bridge_absent","weak_follow_through"],"stage4c_evidence_fields":["repeat_demand_bridge_absent","margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":20.35,"MFE_90D_pct":20.35,"MFE_180D_pct":20.35,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-4.35,"MAE_90D_pct":-27.83,"MAE_180D_pct":-33.83,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-04","peak_price":69200.0,"drawdown_after_peak_pct":-45.01,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"test_interface_recovery_premium_not_C10_stage3_without_margin_revision_bridge","four_b_evidence_type":["event_premium","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_high_mae_margin_revision_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C10_131290_2024_03_06_57500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"borderline C10/C08 case; counted with reduced weight","independent_evidence_weight":0.9,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_EUGENETECH_084370_2024_03_06_MEMORY_ALD_EQUIPMENT_RECOVERY_4B","trigger_id":"EUGENETECH_084370_2024_03_06_STAGE2A_MEMORY_ALD_RECOVERY","symbol":"084370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable / Yellow-watch","raw_component_scores_after":{"contract_score":1,"backlog_visibility_score":3,"margin_bridge_score":4,"revision_score":4,"relative_strength_score":8,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable with C10 4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"ALD/memory equipment recovery worked, but Yellow/Green needs realized order, margin, revision, and FCF confirmation.","MFE_90D_pct":65.52,"MAE_90D_pct":-4.97,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_STI_039440_2024_03_06_MEMORY_INFRA_EQUIPMENT_PREMIUM_FALSE_POSITIVE","trigger_id":"STI_039440_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_INFRA_RECOVERY","symbol":"039440","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":7,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory-infra recovery spike without realized order/margin bridge led to high MAE.","MFE_90D_pct":20.64,"MAE_90D_pct":-25.94,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C10_TSE_131290_2024_03_06_MEMORY_TEST_INTERFACE_RECOVERY_FALSE_POSITIVE","trigger_id":"TSE_131290_2024_03_06_STAGE2_FALSE_POSITIVE_MEMORY_TEST_INTERFACE","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage2 false-positive / C10-C08 boundary","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":3,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not C10 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Memory test-interface premium without margin/revision bridge should not receive C10 Stage2 promotion.","MFE_90D_pct":20.35,"MAE_90D_pct":-27.83,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"101","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C01_ORDER_BACKLOG_MARGIN_BRIDGE, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF, C15_MATERIAL_SPREAD_SUPERCYCLE
```

If this loop is accepted together with loop99 and loop100, C10 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C10 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/039/039440/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/084/084370.json
  - atlas/symbol_profiles/039/039440.json
  - atlas/symbol_profiles/131/131290.json
- Considered but rejected:
  - atlas/symbol_profiles/079/079370.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
