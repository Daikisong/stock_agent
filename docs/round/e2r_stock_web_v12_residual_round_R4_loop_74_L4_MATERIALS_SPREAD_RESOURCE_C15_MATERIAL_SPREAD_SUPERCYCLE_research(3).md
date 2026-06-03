# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R4
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R5
computed_next_loop: 74
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: C15_SPREAD_MARGIN_PASS_THROUGH_DEMAND_FCF_BRIDGE_GUARD
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

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`. The previous R4 loop used C16 strategic resource/policy supply, so this run shifts to C15. The selected branch is spread-to-margin rather than resource-discovery: copper, stainless/nickel, and aluminum themes can all produce price heat, but only the ones tied to pass-through, product mix, demand, margin, and FCF deserve Stage3 promotion.

| layer | id | definition |
|---|---|---|
| round | R4 | materials / spread / resource |
| large_sector | L4_MATERIALS_SPREAD_RESOURCE | commodity/material spread, resource, metal, chemical and product-mix bridge |
| canonical | C15_MATERIAL_SPREAD_SUPERCYCLE | material spread/supercycle, price-to-margin bridge |
| fine | C15_SPREAD_MARGIN_PASS_THROUGH_DEMAND_FCF_BRIDGE_GUARD | spread signal must become margin/pass-through/demand/FCF bridge |
| deep | COPPER_PRICE_SPREAD_AND_DEFENSE_PRODUCT_MIX_TO_MARGIN_FCF_BRIDGE | copper spread positive |
| deep | STAINLESS_NICKEL_OPTIONALITY_WITHOUT_SPREAD_MARGIN_OR_DEMAND_CONVERSION | stainless/nickel theme watch |
| deep | ALUMINUM_EXTRUSION_MATERIAL_THEME_WITHOUT_VOLUME_MARGIN_CASHFLOW_CONVERSION | aluminum theme high-MAE watch |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C15 top-covered symbols are `005490`, `004020`, `012800`, `025820`, `001430`, and `018470`. This run avoids that top-covered cluster and also avoids the immediately prior R4/C16 resource-policy symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C15 | 103140 | new independent | not top-covered C15 symbol; copper spread / defense product-mix margin bridge |
| C15 | 004560 | new independent | not top-covered C15 symbol; stainless/nickel theme without durable margin bridge |
| C15 | 001780 | new independent | not top-covered C15 symbol; aluminum material theme without volume/margin/cashflow bridge |

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
103140 has no corporate-action candidate dates.
004560 has only historical corporate-action/name-transition candidate windows before the selected 2024 window.
001780 has historical name-transition/corporate-action candidates before the selected 2024 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 103140 | 풍산 | Stage2-Actionable | 2024-03-05 | 43200 | copper spread / defense product-mix margin bridge worked |
| theme_MFE_then_high_MAE_counterexample | 004560 | 현대비앤지스틸 | Stage2-Actionable | 2024-01-10 | 19110 | stainless/nickel theme lacked durable spread/margin bridge |
| aluminum_theme_false_start_high_MAE | 001780 | 알루코 | Stage2-Actionable | 2024-01-19 | 3400 | aluminum material theme lacked volume/margin/cashflow bridge |

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
| 103140 | 풍산 | Stage2-Actionable | 2024-03-05 | 43200 | 56.25 | 82.64 | 82.64 | -1.62 | -1.62 | -1.62 | 2024-05-14 | 78900 | -40.43 |
| 004560 | 현대비앤지스틸 | Stage2-Actionable | 2024-01-10 | 19110 | 9.11 | 21.14 | 21.14 | -10.31 | -10.78 | -16.8 | 2024-05-29 | 23150 | -31.32 |
| 001780 | 알루코 | Stage2-Actionable | 2024-01-19 | 3400 | 8.24 | 32.94 | 32.94 | -5.59 | -12.06 | -20.44 | 2024-03-26 | 4520 | -40.15 |

## 9. Case-by-Case Notes

### 9.1 103140 / 풍산 — copper spread and product-mix bridge

The entry row is 2024-03-05 at 43,200. The 30D path reaches 67,500 and the 90D/180D path reaches 78,900. This is a valid C15 positive because the price move is tied to copper spread, pass-through, defense product mix, and margin/FCF bridge. It still needs 4B watch after the peak because material spread cycles can compress quickly when the commodity price or multiple reverses.

### 9.2 004560 / 현대비앤지스틸 — stainless/nickel theme with weak margin bridge

The entry row is 2024-01-10 at 19,110. MFE exists, but the broader low reaches 15,900 and the post-peak path is not supported by a clear demand/spread/margin conversion bridge. This is not a clean Stage3 case. It is a 4B/high-MAE watch row.

### 9.3 001780 / 알루코 — aluminum material theme false start

The entry row is 2024-01-19 at 3,400. The price reaches 4,520, but later declines to 2,705. This is the C15 false-positive shape: a metal/material label can create a move, but without volume, margin, pass-through, inventory, or cashflow evidence, the move is more heat than furnace.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C15 treats metal/material theme MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C15 needs spread-to-margin/pass-through/FCF bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 004560 and 001780. |
| Full 4B non-price requirement appropriate? | Yes. 103140 has non-price bridge; 004560/001780 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
103140:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after spread-to-margin / product-mix / FCF bridge
  Stage3-Green = wait for stronger post-peak spread durability and 4B review

004560:
  Stage2-Actionable = acceptable only as materials watch
  Stage3-Yellow = reject without demand, spread, margin, or pass-through bridge
  Stage3-Green = reject despite MFE

001780:
  Stage2-Actionable = acceptable only as material theme watch
  Stage3-Yellow = reject without volume, margin, inventory, or cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 103140 | 0.96 | 1.00 | good full-window 4B watch after copper spread/margin bridge |
| 004560 | 0.90 | 1.00 | metal theme MFE but no margin bridge; keep 4B/high-MAE watch |
| 001780 | 1.00 | 1.00 | aluminum theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c15_requires_spread_to_margin_pass_through_demand_fcf_bridge

rule:
  For C15 material-spread rows, do not promote copper, aluminum, nickel,
  stainless, steel, chemical, or commodity spread Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  spread-to-margin conversion, raw-material pass-through, demand/volume recovery,
  product-mix upgrade, inventory normalization, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 45.57 | -8.15 | 66.7% | too generous to metal/material theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 45.57 | -8.15 | 33.3% | safer but may miss 103140 |
| P1 sector_specific_candidate_profile | 3 | 45.57 | -8.15 | 66.7% | no broad L4 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 82.64 | -1.62 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 27.04 | -11.42 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 103140 | current_profile_correct | copper spread/product-mix bridge aligned with strong MFE |
| 004560 | current_profile_false_positive_if_green | metal theme MFE existed but no durable spread/margin bridge |
| 001780 | current_profile_false_positive_if_green | aluminum theme produced MFE then high-MAE path |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | C15_SPREAD_MARGIN_PASS_THROUGH_DEMAND_FCF_BRIDGE_GUARD | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | false | true | C15 non-top-covered materials spread residual reduced |

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
- metal theme MFE without spread-margin bridge
- material spread winner needs 4B watch
- aluminum theme high-MAE without demand-margin bridge
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
shadow_weight,c15_requires_spread_to_margin_pass_through_demand_fcf_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"C15 materials spread rows should not promote toward Stage3-Yellow/Green unless commodity/material signal converts into spread-to-margin, pass-through, product mix, demand, inventory normalization, FCF, or cash conversion bridge","103140 survives with strong MFE after copper spread/product-mix margin bridge; 004560 and 001780 remain 4B/high-MAE watch because metal/material theme lacks durable spread-margin bridge","TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE|TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE|TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c15_material_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,1,1,0,"Material spread winners and metal-theme false starts can peak before margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 103140 positive while preventing 004560/001780 material-theme false positives","TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE|TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE|TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","symbol":"103140","company_name":"풍산","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","deep_sub_archetype_id":"COPPER_PRICE_SPREAD_AND_DEFENSE_PRODUCT_MIX_TO_MARGIN_FCF_BRIDGE","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C15 materials spread rows require spread-to-margin, pass-through, demand, volume, inventory, FCF or product-mix bridge; metal-price/material theme alone is insufficient."}
{"row_type":"case","case_id":"R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE","symbol":"004560","company_name":"현대비앤지스틸","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STAINLESS_NICKEL_THEME_WITHOUT_SPREAD_MARGIN_BRIDGE","deep_sub_archetype_id":"STAINLESS_NICKEL_OPTIONALITY_WITHOUT_SPREAD_MARGIN_OR_DEMAND_CONVERSION","case_type":"theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C15 materials spread rows require spread-to-margin, pass-through, demand, volume, inventory, FCF or product-mix bridge; metal-price/material theme alone is insufficient."}
{"row_type":"case","case_id":"R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"001780","company_name":"알루코","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_ALUMINUM_THEME_WITHOUT_DEMAND_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"ALUMINUM_EXTRUSION_MATERIAL_THEME_WITHOUT_VOLUME_MARGIN_CASHFLOW_CONVERSION","case_type":"aluminum_theme_false_start_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C15 materials spread rows require spread-to-margin, pass-through, demand, volume, inventory, FCF or product-mix bridge; metal-price/material theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","case_id":"R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","symbol":"103140","company_name":"풍산","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","deep_sub_archetype_id":"COPPER_PRICE_SPREAD_AND_DEFENSE_PRODUCT_MIX_TO_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":43200,"evidence_available_at_that_date":"source_proxy_copper_price_spread_defense_mix_margin_FCF_bridge; evidence_url_pending","evidence_source":"source_proxy_copper_price_spread_defense_mix_margin_FCF_bridge; evidence_url_pending","bridge_summary":"copper price/spread and defense product-mix route converted into margin and FCF visibility rather than simple metal-price theme","stage2_evidence_fields":["copper_spread_recovery","defense_product_mix","relative_strength","margin_bridge_proxy"],"stage3_evidence_fields":["spread_to_margin_visibility","inventory_or_lme_pass_through","FCF_bridge_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","copper_spread_crowding_after_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":56.25,"MFE_90D_pct":82.64,"MFE_180D_pct":82.64,"MFE_1Y_pct":82.64,"MFE_2Y_pct":82.64,"MAE_30D_pct":-1.62,"MAE_90D_pct":-1.62,"MAE_180D_pct":-1.62,"MAE_1Y_pct":-1.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":78900,"drawdown_after_peak_pct":-40.43,"green_lateness_ratio":"0.35","four_b_local_peak_proximity":0.96,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_copper_spread_margin_bridge","four_b_evidence_type":"non_price_spread_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE","case_id":"R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE","symbol":"004560","company_name":"현대비앤지스틸","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_STAINLESS_NICKEL_THEME_WITHOUT_SPREAD_MARGIN_BRIDGE","deep_sub_archetype_id":"STAINLESS_NICKEL_OPTIONALITY_WITHOUT_SPREAD_MARGIN_OR_DEMAND_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":19110,"evidence_available_at_that_date":"source_proxy_stainless_nickel_price_theme_without_spread_margin_demand_bridge; evidence_url_pending","evidence_source":"source_proxy_stainless_nickel_price_theme_without_spread_margin_demand_bridge; evidence_url_pending","bridge_summary":"stainless/nickel theme produced some MFE, but demand, spread, and margin conversion bridge stayed weak and later path degraded into high MAE","stage2_evidence_fields":["stainless_nickel_theme","metal_spread_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_local_peak","spread_margin_bridge_absent","demand_conversion_absent"],"stage4c_evidence_fields":["high_MAE_without_spread_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004560/2024.csv","profile_path":"atlas/symbol_profiles/004/004560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.11,"MFE_90D_pct":21.14,"MFE_180D_pct":21.14,"MFE_1Y_pct":21.14,"MFE_2Y_pct":21.14,"MAE_30D_pct":-10.31,"MAE_90D_pct":-10.78,"MAE_180D_pct":-16.8,"MAE_1Y_pct":-16.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-29","peak_price":23150,"drawdown_after_peak_pct":-31.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"metal_theme_MFE_but_no_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"metal_theme_without_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE","case_id":"R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"001780","company_name":"알루코","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"C15_ALUMINUM_THEME_WITHOUT_DEMAND_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"ALUMINUM_EXTRUSION_MATERIAL_THEME_WITHOUT_VOLUME_MARGIN_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-19","entry_date":"2024-01-19","entry_price":3400,"evidence_available_at_that_date":"source_proxy_aluminum_extrusion_material_theme_without_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_aluminum_extrusion_material_theme_without_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"aluminum/material theme created MFE, but volume, margin, and cashflow bridge did not follow; later high-MAE path blocks positive Stage3 routing","stage2_evidence_fields":["aluminum_material_theme","extrusion_or_lightweighting_optionality","price_spike","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_theme_peak","volume_margin_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_demand_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv","profile_path":"atlas/symbol_profiles/001/001780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.24,"MFE_90D_pct":32.94,"MFE_180D_pct":32.94,"MFE_1Y_pct":32.94,"MFE_2Y_pct":32.94,"MAE_30D_pct":-5.59,"MAE_90D_pct":-12.06,"MAE_180D_pct":-20.44,"MAE_1Y_pct":-20.44,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-26","peak_price":4520,"drawdown_after_peak_pct":-40.15,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"aluminum_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"metal_theme_without_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","trigger_id":"TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"spread_recovery_score":12,"margin_bridge_score":12,"pass_through_score":10,"product_mix_score":10,"relative_strength_score":10,"risk_penalty":5},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":15,"margin_bridge_score":15,"pass_through_score":13,"product_mix_score":13,"relative_strength_score":8,"risk_penalty":6},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["spread_recovery_score","margin_bridge_score","pass_through_score","product_mix_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C15 row is promoted only because material spread recovery converts into product-mix, margin, pass-through and FCF bridge.","MFE_90D_pct":82.64,"MAE_90D_pct":-1.62,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE","trigger_id":"TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE","symbol":"004560","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"spread_recovery_score":8,"margin_bridge_score":1,"pass_through_score":1,"product_mix_score":2,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":4,"margin_bridge_score":0,"pass_through_score":0,"product_mix_score":1,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["spread_recovery_score","margin_bridge_score","pass_through_score","product_mix_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C15 guard demotes material/metal theme rows when spread-to-margin, demand, pass-through, inventory or FCF bridge is absent.","MFE_90D_pct":21.14,"MAE_90D_pct":-10.78,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE","trigger_id":"TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE","symbol":"001780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"spread_recovery_score":8,"margin_bridge_score":1,"pass_through_score":1,"product_mix_score":2,"relative_strength_score":11,"risk_penalty":8},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"spread_recovery_score":4,"margin_bridge_score":0,"pass_through_score":0,"product_mix_score":1,"relative_strength_score":5,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["spread_recovery_score","margin_bridge_score","pass_through_score","product_mix_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C15 guard demotes material/metal theme rows when spread-to-margin, demand, pass-through, inventory or FCF bridge is absent.","MFE_90D_pct":32.94,"MAE_90D_pct":-12.06,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_requires_spread_to_margin_pass_through_demand_fcf_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"C15 materials spread rows should not promote toward Stage3-Yellow/Green unless commodity/material signal converts into spread-to-margin, pass-through, product mix, demand, inventory normalization, FCF, or cash conversion bridge","103140 survives with strong MFE after copper spread/product-mix margin bridge; 004560 and 001780 remain 4B/high-MAE watch because metal/material theme lacks durable spread-margin bridge","TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE|TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE|TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c15_material_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,1,1,0,"Material spread winners and metal-theme false starts can peak before margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 103140 positive while preventing 004560/001780 material-theme false positives","TRG_R4L74_C15_103140_20240305_COPPER_SPREAD_DEFENSE_MARGIN_BRIDGE|TRG_R4L74_C15_004560_20240110_STAINLESS_NICKEL_THEME_WEAK_MARGIN_BRIDGE|TRG_R4L74_C15_001780_20240119_ALUMINUM_THEME_NO_DEMAND_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["metal_theme_MFE_without_spread_margin_bridge","material_spread_winner_needs_4B_watch","aluminum_theme_high_MAE_without_demand_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/material-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C15 material-spread rows cannot promote without spread-to-margin, pass-through, product mix, demand/volume, inventory normalization, FCF/cash conversion, or earnings-revision bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R4
completed_loop = 74
next_round = R5
next_loop = 74
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
atlas/symbol_profiles/103/103140.json
atlas/symbol_profiles/004/004560.json
atlas/symbol_profiles/001/001780.json
atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv
atlas/ohlcv_tradable_by_symbol_year/004/004560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001780/2024.csv
```

This loop continues loop 74 with R4 and adds 3 new independent C15 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R4/L4.
