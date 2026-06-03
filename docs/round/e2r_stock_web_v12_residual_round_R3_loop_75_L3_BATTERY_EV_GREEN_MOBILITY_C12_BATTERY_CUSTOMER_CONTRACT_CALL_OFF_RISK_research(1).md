# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R3
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R4
computed_next_loop: 75
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: C12_CUSTOMER_CONTRACT_VOLUME_UTILIZATION_MARGIN_CALLOFF_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

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

## 2. Round / Large Sector / Canonical Archetype Scope

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`. The previous R3 loop used C14 EV demand slowdown, so this run rotates to C12. The selected branch tests the customer-contract/call-off boundary: customer contract and capacity evidence can create a large rerating, but battery-material theme rows without volume, utilization, margin or call-off protection must be demoted.

| layer | id | definition |
|---|---|---|
| round | R3 | battery / EV / green mobility |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery, EV, green mobility, materials and supply chain |
| canonical | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | customer contract, call-off risk, volume/utilization/margin bridge |
| fine | C12_CUSTOMER_CONTRACT_VOLUME_UTILIZATION_MARGIN_CALLOFF_BRIDGE_GUARD | battery signal must become customer/volume/margin evidence |
| deep | ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_EXPANSION_TO_ORDERBOOK_RERATING_AND_POST_PEAK_CALLOFF_RISK | electrolyte contract positive |
| deep | ELECTROLYTE_ADDITIVE_CUSTOMER_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_UTILIZATION_RECOVERY | electrolyte additive false positive |
| deep | LIPF6_FLUOROCHEM_BATTERY_MATERIAL_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_RECOVERY | LiPF6/fluorochemical false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run avoids the most-covered R3 battery material cluster previously used for C14/C13 paths and does not reuse `006110`, `011790`, `095500`, `247540`, `003670`, `066970`, `361610`, `373220`, or `393890`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C12 | 348370 | new independent | electrolyte customer-contract/capacity bridge with post-peak call-off watch |
| C12 | 278280 | new independent | electrolyte additive demand/call-off false start |
| C12 | 093370 | new independent | LiPF6/fluorochemical demand/call-off margin-risk counterexample |

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-web assumptions:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
tradable columns = d,o,h,l,c,v,a,mc,s,m
```

## 5. Historical Eligibility Gate

```text
entry row exists = true
forward 180 trading days available = true
MFE/MAE 30D/90D/180D computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
348370 has no corporate-action candidate dates.
278280 has no corporate-action candidate dates.
093370 has no corporate-action candidate dates.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_calloff_watch | 348370 | 엔켐 | Stage2-Actionable | 2024-01-29 | 169500 | electrolyte customer-contract/capacity bridge worked, but post-peak call-off/high-MAE guard required |
| failed_electrolyte_additive_demand_margin_counterexample | 278280 | 천보 | Stage2-Actionable | 2024-01-29 | 87700 | electrolyte additive theme lacked volume/utilization/margin bridge |
| failed_fluorochemical_battery_material_high_MAE_counterexample | 093370 | 후성 | Stage2-Actionable | 2024-01-29 | 8750 | LiPF6/fluorochemical material theme lacked customer-volume/margin bridge |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 3
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 348370 | 엔켐 | Stage2-Actionable | 2024-01-29 | 169500 | 111.5 | 132.74 | 132.74 | -17.7 | -17.7 | -17.7 | 2024-04-08 | 394500 | -72.62 |
| 278280 | 천보 | Stage2-Actionable | 2024-01-29 | 87700 | 13.8 | 13.8 | 13.8 | -7.64 | -18.93 | -25.09 | 2024-02-21 | 99800 | -34.17 |
| 093370 | 후성 | Stage2-Actionable | 2024-01-29 | 8750 | 5.6 | 5.6 | 5.6 | -7.66 | -14.17 | -40.57 | 2024-02-16 | 9240 | -43.72 |

## 9. Case-by-Case Notes

### 9.1 348370 / 엔켐 — electrolyte customer-contract capacity bridge

The entry row is 2024-01-29 at 169,500. The 30D path reached 358,500 and the 90D/180D path reached 394,500. This is a valid C12 positive because the rerating was not just battery-material beta. The bridge is customer contract, electrolyte capacity expansion and orderbook visibility. But the post-peak low reached 108,000, so the right route is guarded Yellow plus 4B/call-off watch, not Green.

### 9.2 278280 / 천보 — electrolyte additive false start

The entry row is 2024-01-29 at 87,700. It reached 99,800, but the later path fell to 65,700. The row shows that electrolyte additive optionality without volume, utilization, margin and cashflow recovery should not survive as a Stage3-quality signal.

### 9.3 093370 / 후성 — LiPF6 / fluorochemical demand and margin risk

The entry row is 2024-01-29 at 8,750. The forward high was only 9,240, while the wider low fell to 5,200. This is the cleaner C12 false-positive shape: a battery-material label without customer-volume, utilization, margin and inventory normalization becomes call-off risk, not positive evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C12 treats battery-material/customer optionality as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C12 needs customer-contract/orderbook/volume/margin bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 348370 after peak and for 278280/093370. |
| Full 4B non-price requirement appropriate? | Yes. MFE alone cannot make 278280/093370 positive. |
| 4C timing issue? | High-MAE/call-off watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
348370:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer contract / capacity / orderbook bridge
  Stage3-Green = reject because post-peak call-off and high-MAE risk remain active

278280:
  Stage2-Actionable = too generous if based only on electrolyte-additive recovery theme
  Stage3-Yellow = reject without volume, utilization, margin and cashflow bridge
  Stage3-Green = reject despite MFE

093370:
  Stage2-Actionable = too generous if based only on LiPF6/fluorochemical battery-material theme
  Stage3-Yellow = reject without customer volume, margin and inventory normalization
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 348370 | 0.90 | 1.00 | contract/capacity bridge positive but 4B call-off/high-MAE watch |
| 278280 | 1.00 | 1.00 | electrolyte-additive recovery theme local 4B watch, not positive stage |
| 093370 | 1.00 | 1.00 | LiPF6 theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c12_requires_customer_contract_volume_utilization_margin_bridge

rule:
  For C12 battery customer-contract/call-off rows, do not promote electrolyte,
  additive, LiPF6, fluorochemical, cathode/anode or battery-material Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  customer contract, orderbook, volume pull-through, utilization, localization,
  inventory normalization, margin conversion, FCF/cash conversion, or earnings revision.
  Prior MFE remains 4B evidence only when call-off or demand/margin risk dominates.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 50.71 | -16.93 | 66.7% | too generous to battery-material optionality |
| P0b e2r_2_0_baseline_reference | 3 | 50.71 | -16.93 | 33.3% | safer but may miss 348370 |
| P1 sector_specific_candidate_profile | 3 | 50.71 | -16.93 | 66.7% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 132.74 | -17.7 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 9.7 | -16.55 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 348370 | current_profile_correct_but_no_green | customer-contract/capacity bridge aligned with MFE, but high-MAE blocks Green |
| 278280 | current_profile_false_positive | electrolyte additive MFE lacked durable volume/margin bridge |
| 093370 | current_profile_false_positive | LiPF6/fluorochemical row produced weak MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | C12_CUSTOMER_CONTRACT_VOLUME_UTILIZATION_MARGIN_CALLOFF_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R3/C12 non-top-covered customer-contract/call-off residual reduced |

## 17. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_guardrail
residual_error_types_found:
- battery material optionality without customer-volume/margin bridge
- electrolyte contract winner needs 4B call-off watch
- LiPF6 demand/call-off high-MAE path
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
- full_4b_requires_non_price_evidence
- local_4b_watch_guard
- high_MAE_watch_guard
existing_axis_weakened: null
existing_axis_kept:
- stage3_green_total_min
- stage3_green_revision_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
```

## 18. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web tradable_raw OHLC rows
- entry_date / entry_price
- MFE/MAE/peak/drawdown
- R3 direct L3 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact customer-contract announcement URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_requires_customer_contract_volume_utilization_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"C12 battery customer-contract/call-off rows should not promote toward Stage3-Yellow/Green unless battery-material signal converts into customer contract, orderbook, volume, utilization, localization, margin, inventory normalization, or cashflow bridge","348370 survives only as guarded positive after electrolyte customer-contract/capacity bridge; 278280 and 093370 are demoted because battery-material optionality lacked durable volume/margin and call-off protection","TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE|TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START|TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_battery_contract_4b_high_mae_calloff_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,1,1,0,"Battery-material winners and theme failures can peak before customer call-off, utilization and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 348370 guarded positive while preventing 278280/093370 battery-material false positives","TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE|TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START|TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE call-off watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE","symbol":"348370","company_name":"엔켐","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE_WITH_CALLOFF_GUARD","deep_sub_archetype_id":"ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_EXPANSION_TO_ORDERBOOK_RERATING_AND_POST_PEAK_CALLOFF_RISK","case_type":"structural_success_then_4B_calloff_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C12 battery contract/call-off rows require customer-contract-to-orderbook, volume, utilization, margin, inventory normalization, localization or cashflow bridge; battery-material theme or MFE alone is insufficient."}
{"row_type":"case","case_id":"R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START","symbol":"278280","company_name":"천보","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"ELECTROLYTE_ADDITIVE_CUSTOMER_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_UTILIZATION_RECOVERY","case_type":"failed_electrolyte_additive_demand_margin_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C12 battery contract/call-off rows require customer-contract-to-orderbook, volume, utilization, margin, inventory normalization, localization or cashflow bridge; battery-material theme or MFE alone is insufficient."}
{"row_type":"case","case_id":"R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK","symbol":"093370","company_name":"후성","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_LIPF6_FLUOROCHEM_CUSTOMER_CALLOFF_MARGIN_RISK","deep_sub_archetype_id":"LIPF6_FLUOROCHEM_BATTERY_MATERIAL_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_RECOVERY","case_type":"failed_fluorochemical_battery_material_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C12 battery contract/call-off rows require customer-contract-to-orderbook, volume, utilization, margin, inventory normalization, localization or cashflow bridge; battery-material theme or MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE","case_id":"R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE","symbol":"348370","company_name":"엔켐","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE_WITH_CALLOFF_GUARD","deep_sub_archetype_id":"ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_EXPANSION_TO_ORDERBOOK_RERATING_AND_POST_PEAK_CALLOFF_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":169500,"evidence_available_at_that_date":"source_proxy_electrolyte_customer_contract_capacity_expansion_orderbook_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_electrolyte_customer_contract_capacity_expansion_orderbook_margin_bridge; evidence_url_pending","bridge_summary":"electrolyte customer contract and overseas capacity expansion converted into orderbook/capacity bridge, but post-peak demand/call-off and valuation risk required 4B guard","stage2_evidence_fields":["electrolyte_customer_contract","capacity_expansion","relative_strength","battery_supply_chain_beta"],"stage3_evidence_fields":["customer_contract_to_orderbook_visibility","capacity_to_revenue_bridge","margin_or_localization_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","customer_calloff_or_utilization_risk","battery_material_crowding"],"stage4c_evidence_fields":["post_peak_high_MAE_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_path":"atlas/symbol_profiles/348/348370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":111.5,"MFE_90D_pct":132.74,"MFE_180D_pct":132.74,"MFE_1Y_pct":132.74,"MFE_2Y_pct":132.74,"MAE_30D_pct":-17.7,"MAE_90D_pct":-17.7,"MAE_180D_pct":-17.7,"MAE_1Y_pct":-17.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-08","peak_price":394500,"drawdown_after_peak_pct":-72.62,"green_lateness_ratio":"0.28","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"contract_capacity_bridge_positive_but_4B_calloff_high_MAE_watch","four_b_evidence_type":"non_price_customer_contract_capacity_bridge","four_c_protection_label":"post_peak_high_MAE_watch","trigger_outcome_label":"structural_success_then_4B_calloff_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START","case_id":"R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START","symbol":"278280","company_name":"천보","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"ELECTROLYTE_ADDITIVE_CUSTOMER_OPTIONALITY_WITHOUT_VOLUME_MARGIN_OR_UTILIZATION_RECOVERY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":87700,"evidence_available_at_that_date":"source_proxy_electrolyte_additive_customer_optionality_without_volume_margin_utilization_recovery; evidence_url_pending","evidence_source":"source_proxy_electrolyte_additive_customer_optionality_without_volume_margin_utilization_recovery; evidence_url_pending","bridge_summary":"electrolyte additive/customer optionality did not convert into durable customer call-off protection, volume, utilization, margin, or cashflow bridge","stage2_evidence_fields":["electrolyte_additive_theme","battery_material_recovery_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_recovery_peak","customer_calloff_risk","utilization_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_recovery"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.8,"MFE_90D_pct":13.8,"MFE_180D_pct":13.8,"MFE_1Y_pct":13.8,"MFE_2Y_pct":13.8,"MAE_30D_pct":-7.64,"MAE_90D_pct":-18.93,"MAE_180D_pct":-25.09,"MAE_1Y_pct":-25.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-21","peak_price":99800,"drawdown_after_peak_pct":-34.17,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"electrolyte_additive_recovery_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"battery_material_theme_without_customer_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_electrolyte_additive_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK","case_id":"R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK","symbol":"093370","company_name":"후성","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"C12_LIPF6_FLUOROCHEM_CUSTOMER_CALLOFF_MARGIN_RISK","deep_sub_archetype_id":"LIPF6_FLUOROCHEM_BATTERY_MATERIAL_THEME_WITHOUT_CUSTOMER_VOLUME_MARGIN_RECOVERY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":8750,"evidence_available_at_that_date":"source_proxy_LiPF6_fluorochemical_battery_material_theme_without_customer_volume_margin_recovery; evidence_url_pending","evidence_source":"source_proxy_LiPF6_fluorochemical_battery_material_theme_without_customer_volume_margin_recovery; evidence_url_pending","bridge_summary":"LiPF6/fluorochemical battery-material theme failed to show customer volume, margin, utilization, inventory or cashflow recovery; call-off/demand risk dominated the path","stage2_evidence_fields":["LiPF6_fluorochemical_theme","battery_material_beta","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_material_peak","customer_volume_bridge_absent","inventory_margin_pressure"],"stage4c_evidence_fields":["high_MAE_without_customer_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.6,"MFE_90D_pct":5.6,"MFE_180D_pct":5.6,"MFE_1Y_pct":5.6,"MFE_2Y_pct":5.6,"MAE_30D_pct":-7.66,"MAE_90D_pct":-14.17,"MAE_180D_pct":-40.57,"MAE_1Y_pct":-40.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":9240,"drawdown_after_peak_pct":-43.72,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"LiPF6_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"battery_material_theme_without_customer_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_fluorochemical_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE","trigger_id":"TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE","symbol":"348370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_contract_score":12,"capacity_orderbook_score":13,"utilization_margin_score":10,"calloff_risk_score":6,"relative_strength_score":12,"theme_risk_penalty":6},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_contract_score":15,"capacity_orderbook_score":16,"utilization_margin_score":12,"calloff_risk_score":11,"relative_strength_score":9,"theme_risk_penalty":9},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["customer_contract_score","capacity_orderbook_score","utilization_margin_score","calloff_risk_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C12 row is promoted only because electrolyte strength converts into customer contract/capacity/orderbook bridge; post-peak call-off/high-MAE risk blocks Green.","MFE_90D_pct":132.74,"MAE_90D_pct":-17.7,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START","trigger_id":"TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_contract_score":2,"capacity_orderbook_score":2,"utilization_margin_score":1,"calloff_risk_score":9,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_contract_score":0,"capacity_orderbook_score":0,"utilization_margin_score":0,"calloff_risk_score":16,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["customer_contract_score","capacity_orderbook_score","utilization_margin_score","calloff_risk_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C12 guard demotes battery-material/customer optionality rows when customer volume, utilization, margin and call-off protection bridge are absent.","MFE_90D_pct":13.8,"MAE_90D_pct":-18.93,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK","trigger_id":"TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK","symbol":"093370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"customer_contract_score":2,"capacity_orderbook_score":2,"utilization_margin_score":1,"calloff_risk_score":9,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"customer_contract_score":0,"capacity_orderbook_score":0,"utilization_margin_score":0,"calloff_risk_score":16,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["customer_contract_score","capacity_orderbook_score","utilization_margin_score","calloff_risk_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C12 guard demotes battery-material/customer optionality rows when customer volume, utilization, margin and call-off protection bridge are absent.","MFE_90D_pct":5.6,"MAE_90D_pct":-14.17,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c12_requires_customer_contract_volume_utilization_margin_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"C12 battery customer-contract/call-off rows should not promote toward Stage3-Yellow/Green unless battery-material signal converts into customer contract, orderbook, volume, utilization, localization, margin, inventory normalization, or cashflow bridge","348370 survives only as guarded positive after electrolyte customer-contract/capacity bridge; 278280 and 093370 are demoted because battery-material optionality lacked durable volume/margin and call-off protection","TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE|TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START|TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c12_battery_contract_4b_high_mae_calloff_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,1,1,0,"Battery-material winners and theme failures can peak before customer call-off, utilization and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 348370 guarded positive while preventing 278280/093370 battery-material false positives","TRG_R3L75_C12_348370_20240129_ELECTROLYTE_CUSTOMER_CONTRACT_CAPACITY_BRIDGE|TRG_R3L75_C12_278280_20240129_ELECTROLYTE_ADDITIVE_DEMAND_CALLOFF_FALSE_START|TRG_R3L75_C12_093370_20240129_LIPF6_FLUOROCHEM_DEMAND_CALLOFF_MARGIN_RISK",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE call-off watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"75","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["battery_material_optional_without_customer_volume_margin_bridge","electrolyte_contract_winner_needs_4B_calloff_watch","LiPF6_demand_calloff_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R3-specific handling

- R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`.
- This MD uses `C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.
- Validate `round_schedule_status=valid` and `round_sector_consistency=pass` before accepting rows.

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
- price-only/battery-material-theme-only rows cannot promote Stage2/Stage3.
- Prior MFE cannot block C12 call-off/high-MAE routing.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R3 direct L3 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C12 battery customer-contract/call-off rows cannot promote without customer contract, orderbook, volume pull-through, utilization, localization, inventory normalization, margin conversion, FCF/cash conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R3
completed_loop = 75
next_round = R4
next_loop = 75
round_schedule_status = valid
round_sector_consistency = pass
```

## 23. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

Stock-web:
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/348/348370.json
atlas/symbol_profiles/278/278280.json
atlas/symbol_profiles/093/093370.json
atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv
```

This loop continues loop 75 with R3 and adds 3 new independent C12 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R3/L3.
