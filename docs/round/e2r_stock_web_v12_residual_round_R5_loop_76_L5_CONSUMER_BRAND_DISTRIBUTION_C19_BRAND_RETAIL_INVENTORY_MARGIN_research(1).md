# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R5
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R6
computed_next_loop: 76
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: C19_INVENTORY_SAME_STORE_MARGIN_CASHFLOW_BRIDGE_GUARD
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

R5 maps directly to `L5_CONSUMER_BRAND_DISTRIBUTION`. The previous R5 loop used C18 consumer export/channel reorder, and earlier R5 work touched C20 beauty/food and C19 retail/inventory. This run returns to C19, but avoids the top-covered C19 symbols and uses a fresh apparel / department-store / convenience-store split.

| layer | id | definition |
|---|---|---|
| round | R5 | consumer / brand / distribution |
| large_sector | L5_CONSUMER_BRAND_DISTRIBUTION | consumer, brand, retail, apparel, department store, distribution |
| canonical | C19_BRAND_RETAIL_INVENTORY_MARGIN | brand/retail inventory normalization, margin, cashflow |
| fine | C19_INVENTORY_SAME_STORE_MARGIN_CASHFLOW_BRIDGE_GUARD | retail signal must become inventory, same-store, margin and cashflow evidence |
| deep | APPAREL_BRAND_INVENTORY_NORMALIZATION_TO_GROSS_MARGIN_AND_CASHFLOW_BRIDGE | apparel brand positive |
| deep | DEPARTMENT_STORE_DUTYFREE_VALUEUP_THEME_WITHOUT_SSSG_MARGIN_INVENTORY_OR_CASHFLOW_CONVERSION | department-store false positive |
| deep | CONVENIENCE_RETAIL_DEFENSIVE_MARGIN_THEME_WITHOUT_SSSG_MIX_INVENTORY_OR_CASHFLOW_CONVERSION | convenience retail false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C19 top-covered symbols are `111770`, `081660`, `383220`, `UNKNOWN_SYMBOL`, `020000`, and `036620`. This run avoids that cluster and also avoids the previous R5/C18 representatives `003960`, `017810`, and `049770`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C19 | 093050 | new independent | not top-covered C19 symbol; apparel inventory/gross-margin/cashflow bridge |
| C19 | 004170 | new independent | not top-covered C19 symbol; department-store/duty-free MFE without durable inventory/margin bridge |
| C19 | 282330 | new independent | not top-covered C19 symbol; convenience retail margin theme low-MFE/high-MAE counterexample |
| reviewed | 069960 | not selected | usable but lower residual value than selected counterexample set |

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
093050 has no corporate-action candidate dates.
004170 has corporate-action candidates ending 2011-06-10, outside the selected 2024 representative window.
282330 has no corporate-action candidate dates.
069960 was inspected but not selected.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| apparel_brand_inventory_margin_success_then_4B_watch | 093050 | LF | Stage2-Actionable | 2024-01-29 | 12890 | apparel inventory/gross-margin bridge worked, but post-peak 4B required |
| department_store_MFE_then_high_MAE_counterexample | 004170 | 신세계 | Stage2-Actionable | 2024-01-29 | 170700 | department-store/duty-free value-up MFE lacked durable margin/cashflow bridge |
| convenience_retail_low_MFE_high_MAE_counterexample | 282330 | BGF리테일 | Stage2-Actionable | 2024-01-29 | 144600 | convenience retail defensive-margin theme produced shallow MFE and high MAE |

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
| 093050 | LF | Stage2-Actionable | 2024-01-29 | 12890 | 11.02 | 29.64 | 29.64 | -2.09 | -2.09 | -2.09 | 2024-05-17 | 16710 | -17.77 |
| 004170 | 신세계 | Stage2-Actionable | 2024-01-29 | 170700 | 11.48 | 11.48 | 11.48 | -6.27 | -8.03 | -18.69 | 2024-02-19 | 190300 | -27.06 |
| 282330 | BGF리테일 | Stage2-Actionable | 2024-01-29 | 144600 | 1.73 | 1.73 | 1.73 | -10.65 | -19.43 | -31.54 | 2024-01-29 | 147100 | -32.7 |

## 9. Case-by-Case Notes

### 9.1 093050 / LF — apparel inventory margin bridge

The entry row is 2024-01-29 at 12,890. The 30D path reached 14,310, the wider path reached 16,710, and the forward low stayed above the early entry low. This is a valid C19 positive only as guarded Yellow. The bridge is inventory normalization, channel mix, gross margin and cashflow conversion. The post-peak low keeps 4B watch alive.

### 9.2 004170 / 신세계 — department-store value-up MFE without durable bridge

The entry row is 2024-01-29 at 170,700. The stock reached 190,300, but the broader path later fell to 138,800. The lesson is that department-store/duty-free value-up language can create MFE, but without same-store sales, inventory normalization, margin and cashflow bridge, it should not become Stage3-Green.

### 9.3 282330 / BGF리테일 — convenience retail low-quality MFE

The entry row is 2024-01-29 at 144,600. The best forward high was only 147,100, while the 180D low reached 99,000. This is the clean false-positive shape: convenience retail defensiveness and margin theme can look safe, but without same-store growth, product mix, inventory and cashflow evidence, the path becomes high-MAE protection evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C19 treats retail/value-up or defensive retail theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C19 needs inventory, same-store, margin and cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 004170 and 282330. |
| Full 4B non-price requirement appropriate? | Yes. 093050 has stronger non-price bridge; 004170/282330 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
093050:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after inventory normalization / gross-margin / cashflow bridge
  Stage3-Green = reject unless post-peak retail-cycle and inventory rebuild risk clear

004170:
  Stage2-Actionable = acceptable only as department-store/duty-free watch
  Stage3-Yellow = reject without same-store sales, inventory normalization, margin and cashflow bridge
  Stage3-Green = reject despite MFE

282330:
  Stage2-Actionable = too generous if based only on convenience-retail defensive margin theme
  Stage3-Yellow = reject without same-store growth, mix, inventory and cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 093050 | 0.86 | 1.00 | apparel inventory/margin bridge positive but full-window 4B/drawdown watch |
| 004170 | 1.00 | 1.00 | department-store MFE but no durable margin bridge; keep 4B/high-MAE watch |
| 282330 | 1.00 | 1.00 | convenience retail local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c19_requires_inventory_same_store_margin_cashflow_bridge

rule:
  For C19 brand/retail inventory-margin rows, do not promote apparel,
  department-store, duty-free, convenience retail, brand, offline retail,
  low-PBR retail, or defensive retail Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  inventory normalization, same-store sales, channel mix, product mix,
  gross-margin conversion, operating leverage, working-capital control,
  FCF/cash conversion, or earnings revision tied to retail economics.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.28 | -9.85 | 66.7% | too generous to retail theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 14.28 | -9.85 | 33.3% | safer but may miss 093050 |
| P1 sector_specific_candidate_profile | 3 | 14.28 | -9.85 | 66.7% | no broad L5 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 29.64 | -2.09 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 6.61 | -13.73 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 093050 | current_profile_correct_but_no_green | inventory/margin bridge aligned with MFE, but 4B drawdown watch remains |
| 004170 | current_profile_false_positive_if_green | department-store MFE lacked durable same-store/margin bridge |
| 282330 | current_profile_false_positive | convenience retail theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | C19_INVENTORY_SAME_STORE_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R5/C19 non-top-covered brand/retail inventory-margin residual reduced |

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
- retail theme without inventory/margin/cashflow bridge
- apparel brand inventory winner needs 4B watch
- convenience retail low-MFE high-MAE
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
- R5 direct L5 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact inventory/margin/cashflow disclosure URLs
- production scoring behavior
- live candidate status
- 069960 as representative row; reviewed but not selected
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_requires_inventory_same_store_margin_cashflow_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"C19 brand/retail inventory-margin rows should not promote toward Stage3-Yellow/Green unless retail or brand signal converts into inventory normalization, same-store sales, channel mix, gross margin, operating leverage, working-capital, or cashflow bridge","093050 survives as guarded positive after apparel inventory/margin bridge; 004170 and 282330 are demoted because department-store/convenience-retail theme MFE lacked durable inventory, same-store growth, margin and cashflow bridge","TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE|TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE|TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_retail_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,1,1,0,"Brand/retail winners and retail-theme false starts can peak before inventory and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 093050 guarded positive while preventing 004170/282330 retail-theme false positives","TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE|TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE|TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","symbol":"093050","company_name":"LF","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"APPAREL_BRAND_INVENTORY_NORMALIZATION_TO_GROSS_MARGIN_AND_CASHFLOW_BRIDGE","case_type":"apparel_brand_inventory_margin_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C19 brand/retail inventory-margin rows require inventory normalization, same-store sales, channel mix, gross margin, operating leverage, working-capital or cashflow bridge; retail/value-up theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE","symbol":"004170","company_name":"신세계","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_DEPARTMENT_STORE_VALUEUP_WITHOUT_DURABLE_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"DEPARTMENT_STORE_DUTYFREE_VALUEUP_THEME_WITHOUT_SSSG_MARGIN_INVENTORY_OR_CASHFLOW_CONVERSION","case_type":"department_store_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"C19 brand/retail inventory-margin rows require inventory normalization, same-store sales, channel mix, gross margin, operating leverage, working-capital or cashflow bridge; retail/value-up theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_CONVENIENCE_RETAIL_MARGIN_THEME_WITHOUT_SSSG_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONVENIENCE_RETAIL_DEFENSIVE_MARGIN_THEME_WITHOUT_SSSG_MIX_INVENTORY_OR_CASHFLOW_CONVERSION","case_type":"convenience_retail_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C19 brand/retail inventory-margin rows require inventory normalization, same-store sales, channel mix, gross margin, operating leverage, working-capital or cashflow bridge; retail/value-up theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","case_id":"R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","symbol":"093050","company_name":"LF","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"APPAREL_BRAND_INVENTORY_NORMALIZATION_TO_GROSS_MARGIN_AND_CASHFLOW_BRIDGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":12890,"evidence_available_at_that_date":"source_proxy_apparel_brand_inventory_normalization_gross_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_apparel_brand_inventory_normalization_gross_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"apparel brand inventory normalization and channel mix converted into gross-margin and cashflow bridge, but post-peak retail-cycle risk required 4B watch","stage2_evidence_fields":["apparel_brand_inventory_normalization","gross_margin_recovery_proxy","relative_strength","cashflow_bridge_proxy"],"stage3_evidence_fields":["inventory_to_margin_visibility","channel_mix_bridge","cashflow_conversion_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","retail_cycle_crowding","inventory_rebuild_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv","profile_path":"atlas/symbol_profiles/093/093050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.02,"MFE_90D_pct":29.64,"MFE_180D_pct":29.64,"MFE_1Y_pct":29.64,"MFE_2Y_pct":29.64,"MAE_30D_pct":-2.09,"MAE_90D_pct":-2.09,"MAE_180D_pct":-2.09,"MAE_1Y_pct":-2.09,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":16710,"drawdown_after_peak_pct":-17.77,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":0.86,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"apparel_brand_inventory_margin_positive_but_full_window_4B_drawdown_watch","four_b_evidence_type":"non_price_inventory_margin_cashflow_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"apparel_brand_inventory_margin_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE","case_id":"R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE","symbol":"004170","company_name":"신세계","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_DEPARTMENT_STORE_VALUEUP_WITHOUT_DURABLE_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"DEPARTMENT_STORE_DUTYFREE_VALUEUP_THEME_WITHOUT_SSSG_MARGIN_INVENTORY_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":170700,"evidence_available_at_that_date":"source_proxy_department_store_dutyfree_valueup_theme_without_SSSG_margin_inventory_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_department_store_dutyfree_valueup_theme_without_SSSG_margin_inventory_cashflow_bridge; evidence_url_pending","bridge_summary":"department-store/duty-free value-up theme produced MFE, but durable same-store sales, inventory normalization, margin and cashflow bridge did not hold through the forward path","stage2_evidence_fields":["department_store_valueup_theme","dutyfree_recovery_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","SSSG_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_inventory_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv","profile_path":"atlas/symbol_profiles/004/004170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.48,"MFE_90D_pct":11.48,"MFE_180D_pct":11.48,"MFE_1Y_pct":11.48,"MFE_2Y_pct":11.48,"MAE_30D_pct":-6.27,"MAE_90D_pct":-8.03,"MAE_180D_pct":-18.69,"MAE_1Y_pct":-18.69,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-19","peak_price":190300,"drawdown_after_peak_pct":-27.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"department_store_MFE_but_no_durable_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"retail_theme_without_durable_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"department_store_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE","case_id":"R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE","symbol":"282330","company_name":"BGF리테일","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"C19_CONVENIENCE_RETAIL_MARGIN_THEME_WITHOUT_SSSG_CASHFLOW_BRIDGE","deep_sub_archetype_id":"CONVENIENCE_RETAIL_DEFENSIVE_MARGIN_THEME_WITHOUT_SSSG_MIX_INVENTORY_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":144600,"evidence_available_at_that_date":"source_proxy_convenience_retail_defensive_margin_theme_without_SSSG_mix_inventory_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_convenience_retail_defensive_margin_theme_without_SSSG_mix_inventory_cashflow_bridge; evidence_url_pending","bridge_summary":"convenience retail defensive-margin theme generated only shallow MFE; same-store growth, product mix, inventory, margin and cashflow bridge were too weak, so high MAE dominated","stage2_evidence_fields":["convenience_retail_theme","defensive_margin_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","same_store_growth_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_retail_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv","profile_path":"atlas/symbol_profiles/282/282330.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.73,"MFE_90D_pct":1.73,"MFE_180D_pct":1.73,"MFE_1Y_pct":1.73,"MFE_2Y_pct":1.73,"MAE_30D_pct":-10.65,"MAE_90D_pct":-19.43,"MAE_180D_pct":-31.54,"MAE_1Y_pct":-31.54,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":147100,"drawdown_after_peak_pct":-32.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"convenience_retail_local_4B_watch_not_positive_stage","four_b_evidence_type":"retail_theme_without_durable_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"convenience_retail_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","trigger_id":"TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE","symbol":"093050","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"brand_strength_score":10,"inventory_normalization_score":12,"same_store_or_channel_score":10,"margin_cashflow_score":11,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"brand_strength_score":12,"inventory_normalization_score":15,"same_store_or_channel_score":12,"margin_cashflow_score":14,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["brand_strength_score","inventory_normalization_score","same_store_or_channel_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C19 row is promoted only because brand/retail signal converts into inventory normalization, margin and cashflow bridge; post-peak retail-cycle watch blocks Green.","MFE_90D_pct":29.64,"MAE_90D_pct":-2.09,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE","trigger_id":"TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE","symbol":"004170","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"brand_strength_score":8,"inventory_normalization_score":2,"same_store_or_channel_score":2,"margin_cashflow_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"brand_strength_score":3,"inventory_normalization_score":0,"same_store_or_channel_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["brand_strength_score","inventory_normalization_score","same_store_or_channel_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C19 guard demotes department-store/convenience retail theme rows when inventory, same-store growth, margin and cashflow bridge are absent.","MFE_90D_pct":11.48,"MAE_90D_pct":-8.03,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE","trigger_id":"TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE","symbol":"282330","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"brand_strength_score":8,"inventory_normalization_score":2,"same_store_or_channel_score":2,"margin_cashflow_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"brand_strength_score":3,"inventory_normalization_score":0,"same_store_or_channel_score":0,"margin_cashflow_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["brand_strength_score","inventory_normalization_score","same_store_or_channel_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C19 guard demotes department-store/convenience retail theme rows when inventory, same-store growth, margin and cashflow bridge are absent.","MFE_90D_pct":1.73,"MAE_90D_pct":-19.43,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c19_requires_inventory_same_store_margin_cashflow_bridge,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"C19 brand/retail inventory-margin rows should not promote toward Stage3-Yellow/Green unless retail or brand signal converts into inventory normalization, same-store sales, channel mix, gross margin, operating leverage, working-capital, or cashflow bridge","093050 survives as guarded positive after apparel inventory/margin bridge; 004170 and 282330 are demoted because department-store/convenience-retail theme MFE lacked durable inventory, same-store growth, margin and cashflow bridge","TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE|TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE|TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c19_retail_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,1,1,0,"Brand/retail winners and retail-theme false starts can peak before inventory and margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 093050 guarded positive while preventing 004170/282330 retail-theme false positives","TRG_R5L76_C19_093050_20240129_APPAREL_BRAND_INVENTORY_MARGIN_CASHFLOW_BRIDGE|TRG_R5L76_C19_004170_20240129_DEPARTMENT_STORE_VALUEUP_MFE_NO_DURABLE_MARGIN_BRIDGE|TRG_R5L76_C19_282330_20240129_CONVENIENCE_RETAIL_MARGIN_THEME_LOW_MFE_HIGH_MAE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"76","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["retail_theme_without_inventory_margin_cashflow_bridge","apparel_brand_inventory_winner_needs_4B_watch","convenience_retail_low_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R5-specific handling

- R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`.
- This MD uses `C19_BRAND_RETAIL_INVENTORY_MARGIN`.
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
- price-only/retail-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R5 direct L5 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C19 brand/retail inventory-margin rows cannot promote without inventory normalization, same-store sales, channel mix, product mix, gross-margin conversion, operating leverage, working-capital control, FCF/cash conversion, or earnings revision tied to retail economics.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R5
completed_loop = 76
next_round = R6
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
atlas/symbol_profiles/093/093050.json
atlas/symbol_profiles/004/004170.json
atlas/symbol_profiles/282/282330.json
atlas/symbol_profiles/069/069960.json
atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv
atlas/ohlcv_tradable_by_symbol_year/004/004170/2024.csv
atlas/ohlcv_tradable_by_symbol_year/282/282330/2024.csv
atlas/ohlcv_tradable_by_symbol_year/069/069960/2024.csv
```

This loop continues loop 76 with R5 and adds 3 new independent C19 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R5/L5.
