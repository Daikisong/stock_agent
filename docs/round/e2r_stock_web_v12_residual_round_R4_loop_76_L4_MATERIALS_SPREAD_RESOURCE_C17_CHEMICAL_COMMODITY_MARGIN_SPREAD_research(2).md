# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R4
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R5
computed_next_loop: 76
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: C17_SPREAD_MARGIN_CASHFLOW_CUSTOMER_VOLUME_BRIDGE_GUARD
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

R4 maps directly to `L4_MATERIALS_SPREAD_RESOURCE`. The previous R4 loop used C16 strategic-resource/policy-supply, and older R4 work covered C15 material-spread/supercycle. This run rotates to C17 chemical/commodity margin-spread and tests a fresh bridge: spread/margin/cashflow proof versus chemical recovery theme MFE.

| layer | id | definition |
|---|---|---|
| round | R4 | materials / spread / resource |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | materials, chemicals, commodity spread, resource and specialty materials |
| canonical | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | chemical commodity spread, price-cost margin, cashflow |
| fine | C17_SPREAD_MARGIN_CASHFLOW_CUSTOMER_VOLUME_BRIDGE_GUARD | chemical signal must become spread, margin, customer volume and cashflow evidence |
| deep | SILICONE_PAINT_MATERIAL_SPREAD_AND_NON_CORE_VALUE_TO_MARGIN_REPRICING | silicone/paint margin positive |
| deep | SOLAR_PVC_CAUSTIC_CHEMICAL_SPREAD_OPTIONALITY_WITHOUT_PRICE_COST_MARGIN_OR_CASHFLOW_CONVERSION | solar/chemical false positive |
| deep | SPECIALTY_CHEMICAL_AND_SEMI_MATERIAL_RECOVERY_OPTIONALITY_WITHOUT_SPREAD_CUSTOMER_VOLUME_MARGIN_CASHFLOW_CONVERSION | specialty chemical false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C17 top-covered symbols are `298020`, `011780`, `006650`, `011170`, `014830`, and `010950`. This run avoids that cluster and also avoids recent R4/C16 representatives `012320`, `047400`, and `037950`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C17 | 002380 | new independent | not top-covered C17 symbol; silicone/paint spread-margin repricing bridge |
| C17 | 009830 | new independent | not top-covered C17 symbol; solar/PVC/caustic chemical spread theme without durable margin bridge |
| C17 | 014680 | new independent | not top-covered C17 symbol; specialty chemical recovery without durable spread/customer-volume bridge |

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
002380 has a 2000-04-17 corporate-action candidate, outside the selected 2024 representative window.
009830 has corporate-action candidates ending 2008-07-04, outside the selected 2024 representative window.
014680 has corporate-action candidates ending 1999-10-04, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| silicone_paint_margin_success_then_4B_drawdown_watch | 002380 | KCC | Stage2-Actionable | 2024-01-29 | 233500 | silicone/paint spread-margin repricing worked, but 4B drawdown watch required |
| solar_chemical_spread_theme_low_MFE_high_MAE_counterexample | 009830 | 한화솔루션 | Stage2-Actionable | 2024-02-01 | 35000 | solar/PVC/caustic spread theme lacked durable margin/cashflow bridge |
| specialty_chemical_recovery_MFE_then_severe_MAE_counterexample | 014680 | 한솔케미칼 | Stage2-Actionable | 2024-03-21 | 210500 | specialty chemical recovery MFE lacked customer-volume/spread/cashflow bridge |

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
| 002380 | KCC | Stage2-Actionable | 2024-01-29 | 233500 | 25.48 | 40.26 | 47.75 | -7.92 | -7.92 | -7.92 | 2024-07-17 | 345000 | -21.59 |
| 009830 | 한화솔루션 | Stage2-Actionable | 2024-02-01 | 35000 | 2.43 | 2.43 | 2.43 | -24.29 | -24.29 | -36.71 | 2024-02-02 | 35850 | -38.21 |
| 014680 | 한솔케미칼 | Stage2-Actionable | 2024-03-21 | 210500 | 1.66 | 1.66 | 1.66 | -14.01 | -18.24 | -54.2 | 2024-03-21 | 214000 | -54.95 |

## 9. Case-by-Case Notes

### 9.1 002380 / KCC — silicone/paint spread and margin bridge

The entry row is 2024-01-29 at 233,500. The 30D path reached 293,000, the 90D path reached 327,500, and the 180D path reached 345,000. This is a valid C17 positive because the rerating needs spread, margin and non-core value repair evidence. It is not just a materials theme spike. The post-peak low of 270,500 keeps 4B drawdown watch alive.

### 9.2 009830 / 한화솔루션 — solar/chemical spread theme without durable bridge

The entry row is 2024-02-01 at 35,000. The high was only 35,850 before the forward path fell to 22,150. Solar/PVC/caustic spread optionality can sound like a margin turn, but without price-cost spread durability, module margin recovery and cashflow bridge, it should not survive as Stage3 evidence.

### 9.3 014680 / 한솔케미칼 — specialty chemical recovery false start

The entry row is 2024-03-21 at 210,500. The high was 214,000, then the path fell as low as 96,400 in the wider window. This row is useful because it shows that specialty chemical or semi-material recovery language cannot substitute for customer-volume, spread, margin and cashflow proof.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C17 treats chemical/spread recovery theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C17 needs spread, margin, customer-volume and cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 009830 and 014680. |
| Full 4B non-price requirement appropriate? | Yes. 002380 has bridge evidence; 009830/014680 do not. |
| 4C timing issue? | High-MAE/severe-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
002380:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after spread/margin/cashflow and valuation-repair bridge
  Stage3-Green = reject unless post-peak material-cycle and spread-reversal risk clear

009830:
  Stage2-Actionable = too generous if based only on solar/chemical spread theme
  Stage3-Yellow = reject without price-cost spread, margin and cashflow bridge
  Stage3-Green = reject

014680:
  Stage2-Actionable = acceptable only as specialty chemical recovery watch
  Stage3-Yellow = reject without customer volume, spread, margin and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 002380 | 0.85 | 1.00 | silicone/paint margin bridge positive but full-window 4B/drawdown watch |
| 009830 | 1.00 | 1.00 | solar/chemical spread theme local 4B watch, not positive stage |
| 014680 | 1.00 | 1.00 | specialty chemical recovery local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c17_requires_spread_margin_cashflow_customer_volume_bridge

rule:
  For C17 chemical/material spread rows, do not promote chemical,
  petrochemical, solar material, specialty chemical, paint, silicone,
  PVC/caustic, semi-material or commodity-spread Stage2 signals into
  Stage3-Yellow/Green unless at least one non-price bridge is visible:
  price-cost spread improvement, feedstock relief, customer volume,
  mix improvement, inventory normalization, margin conversion,
  FCF/cash conversion, or earnings revision tied to spread economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.78 | -16.82 | 66.7% | too generous to chemical recovery/spread theme |
| P0b e2r_2_0_baseline_reference | 3 | 14.78 | -16.82 | 33.3% | safer but may miss 002380 |
| P1 sector_specific_candidate_profile | 3 | 14.78 | -16.82 | 66.7% | no broad L4 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 40.26 | -7.92 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 2.04 | -21.27 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 002380 | current_profile_correct_but_no_green | spread/margin bridge aligned with MFE, but 4B drawdown blocks Green |
| 009830 | current_profile_false_positive | solar/chemical spread theme produced shallow MFE and high MAE |
| 014680 | current_profile_false_positive | specialty chemical recovery MFE lacked durable volume/spread bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | C17_SPREAD_MARGIN_CASHFLOW_CUSTOMER_VOLUME_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R4/C17 non-top-covered chemical spread residual reduced |

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
- chemical recovery theme without spread/margin bridge
- silicone/paint spread winner needs 4B watch
- specialty chemical recovery severe high-MAE
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
- R4 direct L4 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact spread/margin/cashflow disclosure URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_requires_spread_margin_cashflow_customer_volume_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 chemical/material spread rows should not promote toward Stage3-Yellow/Green unless spread or material signal converts into price-cost spread, feedstock relief, customer volume, mix, margin, inventory normalization, FCF or cashflow bridge","002380 survives as guarded positive after silicone/paint spread-margin bridge; 009830 and 014680 are demoted because chemical/solar/specialty-material recovery themes lacked durable spread, volume, margin and cashflow bridge","TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE|TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE|TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_chemical_spread_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,1,1,0,"Chemical spread winners and recovery-theme false starts can peak before spread/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 002380 guarded positive while preventing 009830/014680 chemical-theme false positives","TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE|TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE|TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","symbol":"002380","company_name":"KCC","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","deep_sub_archetype_id":"SILICONE_PAINT_MATERIAL_SPREAD_AND_NON_CORE_VALUE_TO_MARGIN_REPRICING","case_type":"silicone_paint_margin_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C17 chemical/material spread rows require price-cost spread, feedstock relief, customer volume, mix, margin, inventory normalization or cashflow bridge; chemical/solar/specialty-material theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SOLAR_CHEMICAL_SPREAD_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"SOLAR_PVC_CAUSTIC_CHEMICAL_SPREAD_OPTIONALITY_WITHOUT_PRICE_COST_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"solar_chemical_spread_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C17 chemical/material spread rows require price-cost spread, feedstock relief, customer volume, mix, margin, inventory normalization or cashflow bridge; chemical/solar/specialty-material theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SPECIALTY_CHEMICAL_RECOVERY_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"SPECIALTY_CHEMICAL_AND_SEMI_MATERIAL_RECOVERY_OPTIONALITY_WITHOUT_SPREAD_CUSTOMER_VOLUME_MARGIN_CASHFLOW_CONVERSION","case_type":"specialty_chemical_recovery_MFE_then_severe_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C17 chemical/material spread rows require price-cost spread, feedstock relief, customer volume, mix, margin, inventory normalization or cashflow bridge; chemical/solar/specialty-material theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","case_id":"R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","symbol":"002380","company_name":"KCC","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","deep_sub_archetype_id":"SILICONE_PAINT_MATERIAL_SPREAD_AND_NON_CORE_VALUE_TO_MARGIN_REPRICING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":233500,"evidence_available_at_that_date":"source_proxy_silicone_paint_material_spread_margin_repricing_non_core_value_bridge; evidence_url_pending","evidence_source":"source_proxy_silicone_paint_material_spread_margin_repricing_non_core_value_bridge; evidence_url_pending","bridge_summary":"silicone/paint material spread recovery, margin repricing and non-core value recognition converted into durable rerating bridge; post-peak material-cycle risk required 4B watch","stage2_evidence_fields":["silicone_paint_spread_recovery","material_margin_repricing","non_core_value_proxy","relative_strength"],"stage3_evidence_fields":["spread_to_margin_visibility","earnings_revision_proxy","valuation_discount_repair"],"stage4b_evidence_fields":["post_MFE_peak_watch","material_cycle_crowding","spread_reversal_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv","profile_path":"atlas/symbol_profiles/002/002380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.48,"MFE_90D_pct":40.26,"MFE_180D_pct":47.75,"MFE_1Y_pct":47.75,"MFE_2Y_pct":47.75,"MAE_30D_pct":-7.92,"MAE_90D_pct":-7.92,"MAE_180D_pct":-7.92,"MAE_1Y_pct":-7.92,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-17","peak_price":345000,"drawdown_after_peak_pct":-21.59,"green_lateness_ratio":"0.41","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"silicone_paint_margin_bridge_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_spread_margin_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"silicone_paint_margin_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE","case_id":"R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE","symbol":"009830","company_name":"한화솔루션","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SOLAR_CHEMICAL_SPREAD_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"SOLAR_PVC_CAUSTIC_CHEMICAL_SPREAD_OPTIONALITY_WITHOUT_PRICE_COST_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35000,"evidence_available_at_that_date":"source_proxy_solar_PVC_caustic_chemical_spread_theme_without_price_cost_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_solar_PVC_caustic_chemical_spread_theme_without_price_cost_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"solar/chemical spread optionality produced only shallow MFE; price-cost spread, module margin, PVC/caustic recovery and cashflow bridge failed to become durable","stage2_evidence_fields":["solar_chemical_spread_theme","commodity_price_cost_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","price_cost_spread_bridge_absent","cashflow_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_spread_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv","profile_path":"atlas/symbol_profiles/009/009830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.43,"MFE_90D_pct":2.43,"MFE_180D_pct":2.43,"MFE_1Y_pct":2.43,"MFE_2Y_pct":2.43,"MAE_30D_pct":-24.29,"MAE_90D_pct":-24.29,"MAE_180D_pct":-36.71,"MAE_1Y_pct":-36.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-02","peak_price":35850,"drawdown_after_peak_pct":-38.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"solar_chemical_spread_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"chemical_spread_theme_without_durable_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"solar_chemical_theme_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE","case_id":"R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE","symbol":"014680","company_name":"한솔케미칼","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"C17_SPECIALTY_CHEMICAL_RECOVERY_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"SPECIALTY_CHEMICAL_AND_SEMI_MATERIAL_RECOVERY_OPTIONALITY_WITHOUT_SPREAD_CUSTOMER_VOLUME_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":210500,"evidence_available_at_that_date":"source_proxy_specialty_chemical_semi_material_recovery_without_customer_volume_spread_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_specialty_chemical_semi_material_recovery_without_customer_volume_spread_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"specialty chemical and semi-material recovery optionality did not convert into durable spread, customer volume, margin or cashflow bridge; the path degraded into severe MAE","stage2_evidence_fields":["specialty_chemical_recovery_theme","semi_material_demand_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_recovery_peak","customer_volume_bridge_absent","spread_margin_bridge_absent"],"stage4c_evidence_fields":["severe_high_MAE_without_customer_volume_or_spread_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv","profile_path":"atlas/symbol_profiles/014/014680.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.66,"MFE_90D_pct":1.66,"MFE_180D_pct":1.66,"MFE_1Y_pct":1.66,"MFE_2Y_pct":1.66,"MAE_30D_pct":-14.01,"MAE_90D_pct":-18.24,"MAE_180D_pct":-54.2,"MAE_1Y_pct":-54.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-21","peak_price":214000,"drawdown_after_peak_pct":-54.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"specialty_chemical_recovery_local_4B_watch_not_positive_stage","four_b_evidence_type":"chemical_spread_theme_without_durable_margin_cashflow_bridge","four_c_protection_label":"severe_high_MAE_watch","trigger_outcome_label":"specialty_chemical_recovery_MFE_then_severe_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","trigger_id":"TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE","symbol":"002380","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"spread_recovery_score":12,"customer_volume_score":9,"margin_bridge_score":12,"cashflow_bridge_score":10,"relative_strength_score":11,"theme_risk_penalty":6},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":15,"customer_volume_score":10,"margin_bridge_score":15,"cashflow_bridge_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":81,"stage_label_after":"Stage3-Yellow","changed_components":["spread_recovery_score","customer_volume_score","margin_bridge_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C17 row is promoted only because material spread recovery converts into margin/cashflow and valuation repair bridge; 4B post-peak spread-cycle watch blocks Green.","MFE_90D_pct":40.26,"MAE_90D_pct":-7.92,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE","trigger_id":"TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE","symbol":"009830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"spread_recovery_score":8,"customer_volume_score":2,"margin_bridge_score":1,"cashflow_bridge_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":3,"customer_volume_score":0,"margin_bridge_score":0,"cashflow_bridge_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["spread_recovery_score","customer_volume_score","margin_bridge_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C17 guard demotes chemical/solar/specialty-material recovery theme rows when price-cost spread, customer volume, margin and cashflow bridge are absent.","MFE_90D_pct":2.43,"MAE_90D_pct":-24.29,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE","trigger_id":"TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE","symbol":"014680","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"spread_recovery_score":8,"customer_volume_score":2,"margin_bridge_score":1,"cashflow_bridge_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":3,"customer_volume_score":0,"margin_bridge_score":0,"cashflow_bridge_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":38,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["spread_recovery_score","customer_volume_score","margin_bridge_score","cashflow_bridge_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C17 guard demotes chemical/solar/specialty-material recovery theme rows when price-cost spread, customer volume, margin and cashflow bridge are absent.","MFE_90D_pct":1.66,"MAE_90D_pct":-18.24,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_requires_spread_margin_cashflow_customer_volume_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"C17 chemical/material spread rows should not promote toward Stage3-Yellow/Green unless spread or material signal converts into price-cost spread, feedstock relief, customer volume, mix, margin, inventory normalization, FCF or cashflow bridge","002380 survives as guarded positive after silicone/paint spread-margin bridge; 009830 and 014680 are demoted because chemical/solar/specialty-material recovery themes lacked durable spread, volume, margin and cashflow bridge","TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE|TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE|TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c17_chemical_spread_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,1,1,0,"Chemical spread winners and recovery-theme false starts can peak before spread/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 002380 guarded positive while preventing 009830/014680 chemical-theme false positives","TRG_R4L76_C17_002380_20240129_SILICONE_PAINT_MARGIN_REPRICING_BRIDGE|TRG_R4L76_C17_009830_20240201_SOLAR_CHEMICAL_SPREAD_THEME_NO_MARGIN_BRIDGE|TRG_R4L76_C17_014680_20240321_SPECIALTY_CHEMICAL_RECOVERY_NO_DURABLE_SPREAD_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"76","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["chemical_recovery_theme_without_spread_margin_bridge","silicone_paint_spread_winner_needs_4B_watch","specialty_chemical_recovery_severe_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R4-specific handling

- R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`.
- This MD uses `C17_CHEMICAL_COMMODITY_MARGIN_SPREAD`.
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
- price-only/chemical-spread-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R4 direct L4 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C17 chemical/material spread rows cannot promote without price-cost spread improvement, feedstock relief, customer volume, mix improvement, inventory normalization, margin conversion, FCF/cash conversion, or earnings revision tied to spread economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R4
completed_loop = 76
next_round = R5
next_loop = 76
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
atlas/symbol_profiles/002/002380.json
atlas/symbol_profiles/009/009830.json
atlas/symbol_profiles/014/014680.json
atlas/ohlcv_tradable_by_symbol_year/002/002380/2024.csv
atlas/ohlcv_tradable_by_symbol_year/009/009830/2024.csv
atlas/ohlcv_tradable_by_symbol_year/014/014680/2024.csv
```

This loop continues loop 76 with R4 and adds 3 new independent C17 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R4/L4.
