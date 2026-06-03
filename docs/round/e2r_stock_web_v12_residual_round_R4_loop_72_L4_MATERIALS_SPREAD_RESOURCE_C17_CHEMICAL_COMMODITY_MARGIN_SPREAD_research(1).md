# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R4
scheduled_loop: 72
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R5
computed_next_loop: 72
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: C17_SPREAD_TO_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`. Inside R4, C17 is already well covered, but it still contains a live residual: chemical/commodity spread winners and chemical-theme false positives can look similar in the first few candles. The separating bridge is whether spread actually converts into margin, cashflow, product mix, or earnings visibility.

| layer | id | definition |
|---|---|---|
| round | R4 | materials / spread / resource |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | materials, chemical spread, commodity and resource cycles |
| canonical | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | chemical/commodity spread, refining/chemical margin, reversal risk |
| fine | C17_SPREAD_TO_MARGIN_CASHFLOW_BRIDGE_GUARD | spread must become margin and cashflow |
| deep | ECH_CAUSTIC_SPREAD_TO_OP_MARGIN_AND_FCF_CONVERSION | specialty chemical spread success |
| deep | TIRE_CORD_AROMID_CHEMICAL_MIX_MARGIN_LEVERAGE | industrial material mix/margin success with drawdown watch |
| deep | BATTERY_MATERIAL_CHEMICAL_THEME_WITHOUT_SPREAD_TO_MARGIN_CONVERSION | chemical theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C17 top-covered symbols are `298020`, `011780`, `006650`, `011170`, `014830`, and `010950`. This run avoids that cluster and uses new-symbol C17 rows to stress the margin bridge.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C17 | 004000 | new independent | not top-covered C17 symbol; specialty chemical spread-to-margin positive |
| C17 | 120110 | new independent | not top-covered C17 symbol; chemical mix/margin positive with 4B watch |
| C17 | 161000 | new independent | not top-covered C17 symbol; chemical/battery-material theme counterexample |

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

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 004000 | 롯데정밀화학 | Stage2-Actionable | 2021-07-14 | 73300 | specialty chemical spread-to-margin bridge worked |
| structural_success_with_drawdown_watch | 120110 | 코오롱인더 | Stage2-Actionable | 2021-06-16 | 67900 | chemical mix/spread bridge worked, but reversal watch needed |
| failed_rerating_high_MAE | 161000 | 애경케미칼 | Stage2-Actionable | 2023-06-19 | 26650 | chemical/battery-material theme without spread bridge failed |

## 7. Positive vs Counterexample Balance

```text
positive_case_count: 2
counterexample_count: 1
4B_case_count: 3
4C_or_high_MAE_watch_count: 2
calibration_usable_case_count: 3
current_profile_error_count: 1
```

## 8. Trigger-Level OHLC Backtest Table

| symbol | company | trigger | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | peak_date | peak_price | DD after peak |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 004000 | 롯데정밀화학 | Stage2-Actionable | 2021-07-14 | 73300 | 6.55 | 38.47 | 38.47 | -13.1 | -13.1 | -13.1 | 2021-09-29 | 101500 | -38.82 |
| 120110 | 코오롱인더 | Stage2-Actionable | 2021-06-16 | 67900 | 26.22 | 40.94 | 40.94 | -6.33 | -13.4 | -13.4 | 2021-09-10 | 95700 | -37.51 |
| 161000 | 애경케미칼 | Stage2-Actionable | 2023-06-19 | 26650 | 4.32 | 4.32 | 4.32 | -26.27 | -44.09 | -50.28 | 2023-06-22 | 27800 | -52.34 |

## 9. Case-by-Case Notes

### 9.1 004000 / 롯데정밀화학 — spread-to-margin positive

The entry row is 2021-07-14 at 73,300. The first month was not clean, but the 90D path reached 101,500. This is the difference between commodity noise and margin conversion: spread evidence can tolerate some early MAE if the earnings bridge keeps walking.

### 9.2 120110 / 코오롱인더 — chemical mix/margin success with reversal watch

The entry row is 2021-06-16 at 67,900. The 30D/90D path validated the chemical mix and industrial-material margin bridge, but the later drawdown means this should not loosen Green. The right output is Yellow plus 4B/high-MAE watch.

### 9.3 161000 / 애경케미칼 — chemical/battery-material theme false positive

The entry row is 2023-06-19 at 26,650. The path quickly loses asymmetry: MFE is shallow while MAE expands. This is the C17 trap. Chemical-theme relative strength is the smell of smoke; spread-to-margin conversion is the fire.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C17 treats chemical/battery-material theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C17 needs spread-to-margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 161000 near the local theme peak. |
| Full 4B non-price requirement appropriate? | Yes. 004000/120110 have non-price spread bridge; 161000 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
004000:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after spread-to-margin bridge
  Stage3-Green = wait for stronger FCF durability and post-MFE 4B check

120110:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed with 4B/high-MAE watch active
  Stage3-Green = reject unless margin durability clears reversal risk

161000:
  Stage2-Actionable = too generous if based only on chemical/battery-material theme
  Stage3-Yellow = reject without spread-to-margin conversion
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 004000 | 0.96 | 1.00 | good full-window 4B watch after spread/margin bridge |
| 120110 | 0.94 | 1.00 | good 4B watch but requires spread reversal guard |
| 161000 | 1.00 | 1.00 | price/theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c17_requires_spread_to_margin_cashflow_bridge

rule:
  For C17 chemical/commodity rows, do not promote chemical spread/theme Stage2 signals
  into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  spread-to-margin conversion, product mix improvement, cashflow visibility,
  earnings revision, inventory normalization, or customer-demand-through-margin evidence.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 27.91 | -23.53 | 33.3% | useful but can over-credit chemical theme |
| P0b e2r_2_0_baseline_reference | 3 | 27.91 | -23.53 | 0% | safer but may miss spread/margin bridge winners |
| P1 sector_specific_candidate_profile | 3 | 27.91 | -23.53 | 33.3% | no broad L4 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 39.7 | -13.25 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 4.32 | -44.09 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 004000 | current_profile_correct | spread-to-margin bridge aligned with strong MFE |
| 120110 | current_profile_partially_correct | bridge worked, but drawdown requires 4B/high-MAE watch |
| 161000 | current_profile_false_positive | chemical theme produced low MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17_SPREAD_TO_MARGIN_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C17 non-top-covered spread/margin residual reduced |

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
- chemical theme without spread/margin bridge
- spread winner needs 4B reversal watch
- commodity cycle high-MAE after price spike
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
shadow_weight,c17_requires_spread_to_margin_cashflow_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 chemical/commodity rows should not promote toward Stage3-Yellow/Green unless commodity or chemical spread converts into margin/cashflow/mix visibility","004000 and 120110 survive with strong MFE after spread/margin bridge; 161000 fails when chemical/battery-material theme lacks durable spread-to-margin conversion","TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE|TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE|TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_chemical_spread_4b_reversal_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,1,1,0,"Chemical spread winners and theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 004000/120110 positives while preventing 161000 theme false positive","TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE|TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE|TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SPECIALTY_CHEMICAL_SPREAD_TO_MARGIN_BRIDGE","deep_sub_archetype_id":"ECH_CAUSTIC_SPREAD_TO_OP_MARGIN_AND_FCF_CONVERSION","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C17 chemical/commodity rows require spread-to-margin conversion and cashflow/mix bridge; chemical or battery-material theme alone is insufficient."}
{"row_type":"case","case_id":"R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_MIX_SPREAD_TO_MARGIN_BRIDGE","deep_sub_archetype_id":"TIRE_CORD_AROMID_CHEMICAL_MIX_MARGIN_LEVERAGE","case_type":"structural_success_with_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C17 chemical/commodity rows require spread-to-margin conversion and cashflow/mix bridge; chemical or battery-material theme alone is insufficient."}
{"row_type":"case","case_id":"R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_THEME_PRICE_SPIKE_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_MATERIAL_CHEMICAL_THEME_WITHOUT_SPREAD_TO_MARGIN_CONVERSION","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C17 chemical/commodity rows require spread-to-margin conversion and cashflow/mix bridge; chemical or battery-material theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE","case_id":"R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE","symbol":"004000","company_name":"롯데정밀화학","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SPECIALTY_CHEMICAL_SPREAD_TO_MARGIN_BRIDGE","deep_sub_archetype_id":"ECH_CAUSTIC_SPREAD_TO_OP_MARGIN_AND_FCF_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-07-14","entry_date":"2021-07-14","entry_price":73300,"evidence_available_at_that_date":"source_proxy_ECH_caustic_spread_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_ECH_caustic_spread_margin_bridge; evidence_url_pending","bridge_summary":"commodity/specialty chemical spread moved into margin/earnings visibility rather than price-only commodity beta","stage2_evidence_fields":["chemical_spread_expansion","specialty_chemical_margin_bridge","relative_strength","earnings_revision_proxy"],"stage3_evidence_fields":["spread_to_margin_conversion","cashflow_visibility_proxy","non_price_margin_bridge"],"stage4b_evidence_fields":["post_spread_rerating_peak_watch","valuation_repricing_after_MFE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv","profile_path":"atlas/symbol_profiles/004/004000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.55,"MFE_90D_pct":38.47,"MFE_180D_pct":38.47,"MFE_1Y_pct":38.47,"MFE_2Y_pct":38.47,"MAE_30D_pct":-13.1,"MAE_90D_pct":-13.1,"MAE_180D_pct":-13.1,"MAE_1Y_pct":-13.1,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-29","peak_price":101500,"drawdown_after_peak_pct":-38.82,"green_lateness_ratio":"0.37","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_spread_margin_bridge","four_b_evidence_type":"non_price_spread_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE","case_id":"R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE","symbol":"120110","company_name":"코오롱인더","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_MIX_SPREAD_TO_MARGIN_BRIDGE","deep_sub_archetype_id":"TIRE_CORD_AROMID_CHEMICAL_MIX_MARGIN_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-06-16","entry_date":"2021-06-16","entry_price":67900,"evidence_available_at_that_date":"source_proxy_tirecord_aromid_chemical_mix_spread_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_tirecord_aromid_chemical_mix_spread_margin_bridge; evidence_url_pending","bridge_summary":"chemical mix and industrial materials spread translated into margin leverage, but post-peak drawdown required 4B watch","stage2_evidence_fields":["chemical_mix_spread_expansion","margin_leverage_proxy","relative_strength","industrial_material_demand_bridge"],"stage3_evidence_fields":["mix_margin_conversion","earnings_visibility_proxy","non_price_spread_bridge"],"stage4b_evidence_fields":["post_MFE_reversal_watch","chemical_cycle_peak_risk"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/120/120110/2021.csv","profile_path":"atlas/symbol_profiles/120/120110.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.22,"MFE_90D_pct":40.94,"MFE_180D_pct":40.94,"MFE_1Y_pct":40.94,"MFE_2Y_pct":40.94,"MAE_30D_pct":-6.33,"MAE_90D_pct":-13.4,"MAE_180D_pct":-13.4,"MAE_1Y_pct":-13.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-09-10","peak_price":95700,"drawdown_after_peak_pct":-37.51,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_spread_reversal_guard","four_b_evidence_type":"non_price_spread_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE","case_id":"R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE","symbol":"161000","company_name":"애경케미칼","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_CHEMICAL_THEME_PRICE_SPIKE_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"BATTERY_MATERIAL_CHEMICAL_THEME_WITHOUT_SPREAD_TO_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-06-19","entry_date":"2023-06-19","entry_price":26650,"evidence_available_at_that_date":"source_proxy_battery_material_chemical_theme_without_spread_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_battery_material_chemical_theme_without_spread_margin_bridge; evidence_url_pending","bridge_summary":"chemical/battery-material theme and price strength lacked durable spread-to-margin conversion and reversed into high MAE","stage2_evidence_fields":["battery_material_chemical_theme","price_strength","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","weak_follow_through","commodity_theme_reversal_watch"],"stage4c_evidence_fields":["high_MAE_without_spread_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv","profile_path":"atlas/symbol_profiles/161/161000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.32,"MFE_90D_pct":4.32,"MFE_180D_pct":4.32,"MFE_1Y_pct":4.32,"MFE_2Y_pct":4.32,"MAE_30D_pct":-26.27,"MAE_90D_pct":-44.09,"MAE_180D_pct":-50.28,"MAE_1Y_pct":-50.28,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-06-22","peak_price":27800,"drawdown_after_peak_pct":-52.34,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"price_theme_without_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE","trigger_id":"TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE","symbol":"004000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"chemical_spread_score":12,"margin_bridge_score":12,"cashflow_visibility_score":8,"relative_strength_score":10,"commodity_reversal_risk_score":3,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"chemical_spread_score":13,"margin_bridge_score":16,"cashflow_visibility_score":11,"relative_strength_score":8,"commodity_reversal_risk_score":4,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["chemical_spread_score","margin_bridge_score","cashflow_visibility_score","relative_strength_score","commodity_reversal_risk_score","risk_penalty"],"component_delta_explanation":"C17 row is promoted only because spread expansion converts into margin and cashflow visibility.","MFE_90D_pct":38.47,"MAE_90D_pct":-13.1,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE","trigger_id":"TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE","symbol":"120110","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"chemical_spread_score":11,"margin_bridge_score":10,"cashflow_visibility_score":7,"relative_strength_score":10,"commodity_reversal_risk_score":5,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"chemical_spread_score":12,"margin_bridge_score":13,"cashflow_visibility_score":8,"relative_strength_score":7,"commodity_reversal_risk_score":7,"risk_penalty":8},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["chemical_spread_score","margin_bridge_score","cashflow_visibility_score","relative_strength_score","commodity_reversal_risk_score","risk_penalty"],"component_delta_explanation":"C17 spread/mix bridge works, but post-MFE chemical cycle drawdown prevents Green loosening.","MFE_90D_pct":40.94,"MAE_90D_pct":-13.4,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE","trigger_id":"TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE","symbol":"161000","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"chemical_spread_score":8,"margin_bridge_score":1,"cashflow_visibility_score":1,"relative_strength_score":12,"commodity_reversal_risk_score":10,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"chemical_spread_score":4,"margin_bridge_score":0,"cashflow_visibility_score":0,"relative_strength_score":5,"commodity_reversal_risk_score":14,"risk_penalty":14},"weighted_score_after":42,"stage_label_after":"Stage1-Watch","changed_components":["chemical_spread_score","margin_bridge_score","cashflow_visibility_score","relative_strength_score","commodity_reversal_risk_score","risk_penalty"],"component_delta_explanation":"C17 guard demotes chemical/battery-material theme when spread-to-margin bridge is absent.","MFE_90D_pct":4.32,"MAE_90D_pct":-44.09,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_requires_spread_to_margin_cashflow_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 chemical/commodity rows should not promote toward Stage3-Yellow/Green unless commodity or chemical spread converts into margin/cashflow/mix visibility","004000 and 120110 survive with strong MFE after spread/margin bridge; 161000 fails when chemical/battery-material theme lacks durable spread-to-margin conversion","TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE|TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE|TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_chemical_spread_4b_reversal_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,1,1,0,"Chemical spread winners and theme failures can peak quickly; local 4B/high-MAE watch should remain active after MFE","preserves 004000/120110 positives while preventing 161000 theme false positive","TRG_R4L72_C17_004000_20210714_ECH_CAUSTIC_SPREAD_MARGIN_BRIDGE|TRG_R4L72_C17_120110_20210616_TIRE_CORD_AROMID_CHEMICAL_MARGIN_BRIDGE|TRG_R4L72_C17_161000_20230619_CHEMICAL_BATTERY_MATERIAL_THEME_WITHOUT_SPREAD_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["chemical_theme_without_spread_margin_bridge","spread_winner_needs_4B_reversal_watch","commodity_cycle_high_MAE_after_price_spike"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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

## 22. Next Round State

```text
completed_round = R4
completed_loop = 72
next_round = R5
next_loop = 72
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
atlas/symbol_profiles/004/004000.json
atlas/symbol_profiles/120/120110.json
atlas/symbol_profiles/161/161000.json
atlas/ohlcv_tradable_by_symbol_year/004/004000/2021.csv
atlas/ohlcv_tradable_by_symbol_year/120/120110/2021.csv
atlas/ohlcv_tradable_by_symbol_year/161/161000/2023.csv
```

This loop adds 3 new independent C17 cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R4/L4.
