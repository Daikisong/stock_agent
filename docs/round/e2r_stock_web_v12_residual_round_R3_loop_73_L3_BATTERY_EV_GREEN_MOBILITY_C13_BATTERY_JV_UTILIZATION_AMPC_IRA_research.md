# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R3
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R4
computed_next_loop: 73
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: C13_UTILIZATION_CUSTOMER_MARGIN_FCF_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
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

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`. The prior R3 loop used C12 battery customer contract/call-off risk, so this run shifts to C13. The residual target is the difference between capacity rhetoric and real economics. A JV, IRA, AMPC, or capacity expansion is only the factory shell. The calibration question is whether utilization, customer pull-through, margin, AMPC realization, and FCF start moving inside the shell.

| layer | id | definition |
|---|---|---|
| round | R3 | battery / EV / green mobility |
| large_sector | L3_BATTERY_EV_GREEN_MOBILITY | battery, EV, green mobility, battery supply chain |
| canonical | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | JV, utilization, AMPC, IRA, local capacity, policy-to-economics bridge |
| fine | C13_UTILIZATION_CUSTOMER_MARGIN_FCF_BRIDGE_GUARD | capacity/JV/IRA needs utilization and margin bridge |
| deep | CYLINDRICAL_CAN_STEEL_CUSTOMER_CAPACITY_TO_MARGIN_AND_UTILIZATION | customer capacity bridge positive |
| deep | EU_COPPER_FOIL_CAPACITY_IRA_OPTIONALITY_WITHOUT_UTILIZATION_MARGIN_BRIDGE | copper foil utilization false start |
| deep | ELECTROLYTE_CAPACITY_JV_OPTIONALITY_WITHOUT_UTILIZATION_FCF_BRIDGE | electrolyte/JV false start |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C13 top-covered symbols are `373220`, `006400`, `096770`, `003670`, `020150`, and `051910`. This run avoids that cluster and also avoids the immediately prior R3/C12 symbols `137400`, `299030`, and `131390`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C13 | 002710 | new independent | not top-covered C13 symbol; battery can steel/customer capacity utilization bridge |
| C13 | 336370 | new independent | not top-covered C13 symbol; copper foil/IRA utilization false start |
| C13 | 025900 | new independent | not top-covered C13 symbol; electrolyte/JV utilization false start |

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
002710 has an old 2009 corporate-action candidate date, outside this 2023 representative window.
336370 has 2024 corporate-action candidate dates; this representative 2023 window is used before that contamination.
025900 has a 2024 corporate-action candidate date; this representative 2023 window is used before that contamination.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 002710 | TCC스틸 | Stage2-Actionable | 2023-03-23 | 22750 | capacity/customer utilization bridge worked |
| failed_rerating_high_MAE | 336370 | 솔루스첨단소재 | Stage2-Actionable | 2023-02-22 | 52200 | copper foil/IRA capacity optionality without utilization bridge failed |
| failed_rerating_high_MAE | 025900 | 동화기업 | Stage2-Actionable | 2023-03-03 | 62500 | electrolyte/JV capacity optionality without utilization/FCF bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 1
counterexample_count: 2
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 2
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 002710 | TCC스틸 | Stage2-Actionable | 2023-03-23 | 22750 | 115.38 | 230.99 | 230.99 | -13.14 | -13.14 | -13.14 | 2023-07-26 | 75300 | -36.85 |
| 336370 | 솔루스첨단소재 | Stage2-Actionable | 2023-02-22 | 52200 | 3.45 | 3.45 | 3.45 | -23.75 | -35.34 | -59.2 | 2023-02-22 | 54000 | -60.56 |
| 025900 | 동화기업 | Stage2-Actionable | 2023-03-03 | 62500 | 2.56 | 2.56 | 2.56 | -17.12 | -35.84 | -65.28 | 2023-03-06 | 64100 | -66.15 |

## 9. Case-by-Case Notes

### 9.1 002710 / TCC스틸 — capacity/customer utilization bridge positive

The entry row is 2023-03-23 at 22,750. The forward path reaches 49,000 in the short window and 75,300 in the wider window. This is the valid C13 path: capacity optionality and customer pull-through become utilization and margin leverage. The move still requires 4B watch after the peak because battery supply-chain reratings can crowd quickly.

### 9.2 336370 / 솔루스첨단소재 — copper foil utilization false start

The entry row is 2023-02-22 at 52,200. The local high reaches 54,000, but the path later falls deeply. This is a C13 false positive if the model gives too much credit to copper foil capacity, IRA/localization, or European expansion without utilization and margin confirmation.

### 9.3 025900 / 동화기업 — electrolyte/JV utilization false start

The entry row is 2023-03-03 at 62,500. The forward high reaches only 64,100 while the wider low falls to 21,700. This is the pure capacity/JV trap: a plant or partnership can be announced, but if utilization, margin, and FCF do not arrive, the market rents the factory and then leaves it empty.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C13 treats capacity/JV/IRA optionality as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C13 needs utilization/customer/margin/FCF bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for capacity-theme false starts. |
| Full 4B non-price requirement appropriate? | Yes. 002710 has a better non-price bridge; 336370/025900 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
002710:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after customer capacity / utilization / margin bridge
  Stage3-Green = wait for stronger FCF durability and post-MFE 4B review

336370:
  Stage2-Actionable = too generous if based only on copper foil capacity / IRA optionality
  Stage3-Yellow = reject without utilization, margin, or customer pull-through bridge
  Stage3-Green = reject

025900:
  Stage2-Actionable = too generous if based only on electrolyte/JV capacity optionality
  Stage3-Yellow = reject without utilization, margin, or FCF bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 002710 | 0.93 | 1.00 | good full-window 4B watch after capacity/utilization bridge |
| 336370 | 1.00 | 1.00 | capacity-theme local 4B watch, not positive stage |
| 025900 | 1.00 | 1.00 | weak local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c13_requires_utilization_customer_margin_fcf_bridge

rule:
  For C13 battery JV/capacity/IRA rows, do not promote capacity expansion,
  JV, AMPC, IRA, localization, or customer-capex optionality Stage2 signals into
  Stage3-Yellow/Green unless at least one non-price bridge is visible:
  utilization ramp, customer pull-through, contracted volume, AMPC realization,
  margin conversion, FCF/cash recovery, or verified operating leverage.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 79.0 | -28.11 | 66.7% | too generous to capacity/JV/IRA optionality rows |
| P0b e2r_2_0_baseline_reference | 3 | 79.0 | -28.11 | 33.3% | safer but may miss 002710 |
| P1 sector_specific_candidate_profile | 3 | 79.0 | -28.11 | 66.7% | no broad L3 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 230.99 | -13.14 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected | 3.0 | -35.59 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 002710 | current_profile_correct | customer/capacity utilization bridge aligned with strong MFE |
| 336370 | current_profile_false_positive | copper foil/IRA capacity optionality produced high MAE |
| 025900 | current_profile_false_positive | electrolyte/JV optionality produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | C13_UTILIZATION_CUSTOMER_MARGIN_FCF_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C13 non-top-covered utilization/JV/IRA residual reduced |

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
- capacity/IRA theme without utilization bridge
- battery JV false start high MAE
- capacity/customer bridge winner needs 4B watch
new_axis_proposed: null
existing_axis_strengthened:
- stage2_required_bridge
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
- round/sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean forward windows
```

Not validated:

```text
- exact disclosure URLs
- exact report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_requires_utilization_customer_margin_fcf_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"C13 battery JV/capacity/IRA rows should not promote toward Stage3-Yellow/Green unless capacity or IRA optionality converts into utilization, customer pull-through, margin, AMPC, or FCF bridge","002710 survives with strong MFE after customer/capacity utilization bridge; 336370 and 025900 fail when utilization/margin/FCF bridge is absent","TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE|TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START|TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c13_capacity_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,1,1,0,"Battery capacity/JV winners and false starts can peak before utilization is confirmed; local 4B/high-MAE watch should remain active after MFE","preserves 002710 positive while preventing 336370/025900 capacity-theme false positives","TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE|TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START|TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE","symbol":"002710","company_name":"TCC스틸","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_CAN_STEEL_CAPACITY_UTILIZATION_CUSTOMER_BRIDGE","deep_sub_archetype_id":"CYLINDRICAL_CAN_STEEL_CUSTOMER_CAPACITY_TO_MARGIN_AND_UTILIZATION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C13 battery JV/capacity/IRA rows require utilization, margin, FCF, AMPC, customer pull-through, or JV ramp bridge; capacity/IRA/JV theme alone is insufficient."}
{"row_type":"case","case_id":"R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_COPPER_FOIL_CAPACITY_UTILIZATION_MARGIN_FALSE_START","deep_sub_archetype_id":"EU_COPPER_FOIL_CAPACITY_IRA_OPTIONALITY_WITHOUT_UTILIZATION_MARGIN_BRIDGE","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C13 battery JV/capacity/IRA rows require utilization, margin, FCF, AMPC, customer pull-through, or JV ramp bridge; capacity/IRA/JV theme alone is insufficient."}
{"row_type":"case","case_id":"R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START","symbol":"025900","company_name":"동화기업","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_ELECTROLYTE_JV_CAPACITY_UTILIZATION_FALSE_START","deep_sub_archetype_id":"ELECTROLYTE_CAPACITY_JV_OPTIONALITY_WITHOUT_UTILIZATION_FCF_BRIDGE","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C13 battery JV/capacity/IRA rows require utilization, margin, FCF, AMPC, customer pull-through, or JV ramp bridge; capacity/IRA/JV theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE","case_id":"R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE","symbol":"002710","company_name":"TCC스틸","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_BATTERY_CAN_STEEL_CAPACITY_UTILIZATION_CUSTOMER_BRIDGE","deep_sub_archetype_id":"CYLINDRICAL_CAN_STEEL_CUSTOMER_CAPACITY_TO_MARGIN_AND_UTILIZATION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-23","entry_date":"2023-03-23","entry_price":22750,"evidence_available_at_that_date":"source_proxy_battery_can_steel_customer_capacity_utilization_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_can_steel_customer_capacity_utilization_bridge; evidence_url_pending","bridge_summary":"battery can steel/customer capacity signal converted into utilization and margin optionality rather than remaining only a battery materials theme","stage2_evidence_fields":["battery_can_steel_capacity","customer_capacity_pullthrough","relative_strength","utilization_proxy"],"stage3_evidence_fields":["capacity_to_utilization_visibility","margin_leverage_proxy","customer_quality_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","battery_can_capacity_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv","profile_path":"atlas/symbol_profiles/002/002710.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":115.38,"MFE_90D_pct":230.99,"MFE_180D_pct":230.99,"MFE_1Y_pct":230.99,"MFE_2Y_pct":230.99,"MAE_30D_pct":-13.14,"MAE_90D_pct":-13.14,"MAE_180D_pct":-13.14,"MAE_1Y_pct":-13.14,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":75300,"drawdown_after_peak_pct":-36.85,"green_lateness_ratio":"0.30","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_capacity_utilization_customer_bridge","four_b_evidence_type":"non_price_utilization_customer_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START","case_id":"R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START","symbol":"336370","company_name":"솔루스첨단소재","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_COPPER_FOIL_CAPACITY_UTILIZATION_MARGIN_FALSE_START","deep_sub_archetype_id":"EU_COPPER_FOIL_CAPACITY_IRA_OPTIONALITY_WITHOUT_UTILIZATION_MARGIN_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-02-22","entry_date":"2023-02-22","entry_price":52200,"evidence_available_at_that_date":"source_proxy_copper_foil_IRA_capacity_optionality_without_utilization_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_copper_foil_IRA_capacity_optionality_without_utilization_margin_bridge; evidence_url_pending","bridge_summary":"copper foil / IRA / capacity optionality lacked utilization, margin, and customer pull-through bridge and rolled into high MAE","stage2_evidence_fields":["copper_foil_capacity_optionality","IRA_or_localization_theme","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_local_peak","utilization_bridge_absent","margin_pressure_watch"],"stage4c_evidence_fields":["high_MAE_without_utilization_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv","profile_path":"atlas/symbol_profiles/336/336370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.45,"MFE_90D_pct":3.45,"MFE_180D_pct":3.45,"MFE_1Y_pct":3.45,"MFE_2Y_pct":3.45,"MAE_30D_pct":-23.75,"MAE_90D_pct":-35.34,"MAE_180D_pct":-59.2,"MAE_1Y_pct":-59.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-22","peak_price":54000,"drawdown_after_peak_pct":-60.56,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"capacity_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"capacity_IRA_theme_without_utilization_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START","case_id":"R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START","symbol":"025900","company_name":"동화기업","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"C13_ELECTROLYTE_JV_CAPACITY_UTILIZATION_FALSE_START","deep_sub_archetype_id":"ELECTROLYTE_CAPACITY_JV_OPTIONALITY_WITHOUT_UTILIZATION_FCF_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-03-03","entry_date":"2023-03-03","entry_price":62500,"evidence_available_at_that_date":"source_proxy_electrolyte_JV_capacity_optional_without_utilization_FCF_bridge; evidence_url_pending","evidence_source":"source_proxy_electrolyte_JV_capacity_optional_without_utilization_FCF_bridge; evidence_url_pending","bridge_summary":"electrolyte/JV/capacity optionality lacked utilization, FCF, and margin bridge; Stage2 theme collapsed into persistent high MAE","stage2_evidence_fields":["electrolyte_capacity_JV_optionality","battery_material_relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","utilization_bridge_absent","FCF_margin_pressure_watch"],"stage4c_evidence_fields":["high_MAE_without_utilization_or_FCF_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025900/2023.csv","profile_path":"atlas/symbol_profiles/025/025900.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.56,"MFE_90D_pct":2.56,"MFE_180D_pct":2.56,"MFE_1Y_pct":2.56,"MFE_2Y_pct":2.56,"MAE_30D_pct":-17.12,"MAE_90D_pct":-35.84,"MAE_180D_pct":-65.28,"MAE_1Y_pct":-65.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-03-06","peak_price":64100,"drawdown_after_peak_pct":-66.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_local_4B_watch_not_positive_stage","four_b_evidence_type":"capacity_IRA_theme_without_utilization_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE","trigger_id":"TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE","symbol":"002710","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"capacity_JV_AMPC_score":12,"utilization_bridge_score":12,"customer_pullthrough_score":11,"margin_FCF_score":9,"relative_strength_score":12,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capacity_JV_AMPC_score":13,"utilization_bridge_score":16,"customer_pullthrough_score":14,"margin_FCF_score":12,"relative_strength_score":9,"risk_penalty":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["capacity_JV_AMPC_score","utilization_bridge_score","customer_pullthrough_score","margin_FCF_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C13 row is promoted only because capacity/JV/IRA theme converts into customer utilization and margin bridge; 4B watch remains active after MFE.","MFE_90D_pct":230.99,"MAE_90D_pct":-13.14,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START","trigger_id":"TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START","symbol":"336370","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"capacity_JV_AMPC_score":10,"utilization_bridge_score":1,"customer_pullthrough_score":2,"margin_FCF_score":1,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capacity_JV_AMPC_score":4,"utilization_bridge_score":0,"customer_pullthrough_score":0,"margin_FCF_score":0,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["capacity_JV_AMPC_score","utilization_bridge_score","customer_pullthrough_score","margin_FCF_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C13 guard demotes capacity/JV/IRA optionality when utilization, customer pull-through, margin, AMPC, or FCF bridge is absent.","MFE_90D_pct":3.45,"MAE_90D_pct":-35.34,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START","trigger_id":"TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START","symbol":"025900","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"capacity_JV_AMPC_score":10,"utilization_bridge_score":1,"customer_pullthrough_score":2,"margin_FCF_score":1,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"capacity_JV_AMPC_score":4,"utilization_bridge_score":0,"customer_pullthrough_score":0,"margin_FCF_score":0,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["capacity_JV_AMPC_score","utilization_bridge_score","customer_pullthrough_score","margin_FCF_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C13 guard demotes capacity/JV/IRA optionality when utilization, customer pull-through, margin, AMPC, or FCF bridge is absent.","MFE_90D_pct":2.56,"MAE_90D_pct":-35.84,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_requires_utilization_customer_margin_fcf_bridge,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,1,+1,"C13 battery JV/capacity/IRA rows should not promote toward Stage3-Yellow/Green unless capacity or IRA optionality converts into utilization, customer pull-through, margin, AMPC, or FCF bridge","002710 survives with strong MFE after customer/capacity utilization bridge; 336370 and 025900 fail when utilization/margin/FCF bridge is absent","TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE|TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START|TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c13_capacity_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,1,1,0,"Battery capacity/JV winners and false starts can peak before utilization is confirmed; local 4B/high-MAE watch should remain active after MFE","preserves 002710 positive while preventing 336370/025900 capacity-theme false positives","TRG_R3L73_C13_002710_20230323_BATTERY_STEEL_CAPACITY_CUSTOMER_UTILIZATION_BRIDGE|TRG_R3L73_C13_336370_20230222_COPPER_FOIL_UTILIZATION_FALSE_START|TRG_R3L73_C13_025900_20230303_ELECTROLYTE_JV_UTILIZATION_FALSE_START",3,3,2,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R3","loop":"73","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["capacity_IRA_theme_without_utilization_bridge","battery_JV_false_start_high_MAE","capacity_customer_bridge_winner_needs_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

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
- price-only/capacity-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C13 capacity/JV/IRA rows cannot promote without utilization, customer, margin, AMPC, or FCF bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R3
completed_loop = 73
next_round = R4
next_loop = 73
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
atlas/symbol_profiles/002/002710.json
atlas/symbol_profiles/336/336370.json
atlas/symbol_profiles/025/025900.json
atlas/ohlcv_tradable_by_symbol_year/002/002710/2023.csv
atlas/ohlcv_tradable_by_symbol_year/336/336370/2023.csv
atlas/ohlcv_tradable_by_symbol_year/025/025900/2023.csv
```

This loop continues loop 73 with R3 and adds 3 new independent C13 representative cases, 1 positive, 2 counterexamples, and 1 canonical-archetype residual guard candidate for R3/L3.
