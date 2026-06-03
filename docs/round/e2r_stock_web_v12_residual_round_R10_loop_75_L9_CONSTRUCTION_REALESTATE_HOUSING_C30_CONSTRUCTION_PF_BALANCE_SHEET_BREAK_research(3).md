# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R10
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R11
computed_next_loop: 75
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_ORDERBOOK_BALANCE_PF_CASHFLOW_BRIDGE_GUARD
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

R10 maps directly to `L9_CONSTRUCTION_REALESTATE_HOUSING`. The previous completed R9 file used the allowed L3 mobility branch, so the scheduler now moves to the direct L9 construction/real-estate round. This file stays inside C30 but shifts to a fresh fine branch: regional housing orderbook/cashflow bridge versus building-material and developer rebound themes that do not convert into balance or cashflow repair.

| layer | id | definition |
|---|---|---|
| round | R10 | construction / real estate / housing |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, housing, real estate, PF, balance-sheet repair |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, trust and cashflow break/repair |
| fine | C30_ORDERBOOK_BALANCE_PF_CASHFLOW_BRIDGE_GUARD | promotion requires orderbook, balance, PF-risk, liquidity or cashflow bridge |
| deep | REGIONAL_HOUSING_ORDERBOOK_AND_PF_RISK_CONTAINMENT_TO_CASHFLOW_STABILITY_RERATING | regional housing positive |
| deep | BUILDING_MATERIALS_REMODELING_THEME_WITHOUT_HOUSING_ORDER_MARGIN_OR_CASHFLOW_CONVERSION | building-material false positive |
| deep | REAL_ESTATE_DEVELOPER_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_LIQUIDITY_OR_ORDER_CASHFLOW_CONVERSION | developer rebound false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols remain `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that cluster and also avoids recent C30 representatives: `003070`, `010960`, `002410`, `034300`, `013360`, `002780`, `012630`, `002460`, `001470`, `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 035890 | new independent | not top-covered C30 symbol; regional housing orderbook/cashflow bridge |
| C30 | 007210 | new independent | not top-covered C30 symbol; building-materials theme without order/margin bridge |
| C30 | 010780 | new independent | not top-covered C30 symbol; real-estate developer rebound without balance/cashflow bridge |

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
035890 has corporate-action candidates ending 2012-07-12, outside the selected 2024 representative window.
007210 has corporate-action candidates ending 2012-05-10, outside the selected 2024 representative window.
010780 has corporate-action candidates ending 2011-07-29, outside the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| regional_housing_orderbook_success_then_4B_watch | 035890 | 서희건설 | Stage2-Actionable | 2024-01-29 | 1259 | regional housing/orderbook cashflow bridge worked slowly |
| building_materials_theme_high_MAE_counterexample | 007210 | 벽산 | Stage2-Actionable | 2024-01-10 | 2770 | building-materials theme lacked order/margin/cashflow bridge |
| developer_rebound_MFE_then_high_MAE_counterexample | 010780 | 아이에스동서 | Stage2-Actionable | 2024-03-08 | 30100 | developer rebound MFE lacked balance/liquidity/cashflow bridge |

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
| 035890 | 서희건설 | Stage2-Actionable | 2024-01-29 | 1259 | 7.15 | 9.77 | 28.75 | -2.3 | -2.3 | -5.48 | 2024-10-10 | 1621 | -14.19 |
| 007210 | 벽산 | Stage2-Actionable | 2024-01-10 | 2770 | 5.05 | 5.05 | 5.05 | -13.18 | -24.91 | -32.85 | 2024-01-11 | 2910 | -36.08 |
| 010780 | 아이에스동서 | Stage2-Actionable | 2024-03-08 | 30100 | 3.65 | 3.65 | 3.65 | -18.44 | -18.94 | -32.39 | 2024-03-22 | 31200 | -34.78 |

## 9. Case-by-Case Notes

### 9.1 035890 / 서희건설 — regional housing orderbook bridge

The entry row is 2024-01-29 at 1,259. The path was slow, but the 180D window reached 1,621. This is a valid C30 positive only as guarded Yellow because the positive evidence is not a generic housing bounce. It needs regional orderbook, PF-risk containment and cashflow stability. The later peak still requires 4B/housing-cycle watch.

### 9.2 007210 / 벽산 — building-materials theme without source bridge

The entry row is 2024-01-10 at 2,770. The local high reached 2,910, but the 180D low reached 1,860. A remodeling or building-material narrative is not enough. Without housing order pull-through, margin, inventory normalization and cashflow, the row becomes high-MAE protection evidence.

### 9.3 010780 / 아이에스동서 — developer rebound without balance/cashflow bridge

The entry row is 2024-03-08 at 30,100. The best forward high was 31,200, while the 180D low reached 20,350. This is the real-estate developer false-positive branch: a value rebound without balance repair, liquidity/refinancing, inventory normalization or order-to-cashflow bridge should not receive Stage3 credit.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats building-material/developer price recovery as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs orderbook/balance/PF/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 007210 and 010780. |
| Full 4B non-price requirement appropriate? | Yes. 035890 has bridge evidence; 007210/010780 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
035890:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after regional orderbook / PF-risk / cashflow bridge
  Stage3-Green = reject unless housing-cycle and post-peak durability clear

007210:
  Stage2-Actionable = too generous if based only on building-material/remodeling theme
  Stage3-Yellow = reject without order, margin, inventory and cashflow bridge
  Stage3-Green = reject

010780:
  Stage2-Actionable = too generous if based only on developer/property rebound
  Stage3-Yellow = reject without balance repair, liquidity, inventory normalization and order-to-cashflow bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 035890 | 0.83 | 1.00 | slow regional housing bridge positive but 4B/housing-cycle watch |
| 007210 | 1.00 | 1.00 | building-materials theme local 4B watch, not positive stage |
| 010780 | 1.00 | 1.00 | developer rebound local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_orderbook_balance_pf_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote construction, housing,
  building-materials, remodeling, developer, property-cycle or value-rebound
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  orderbook/backlog, NAV or balance repair, PF-risk containment, liquidity/refinancing,
  trust-quality repair, order-to-cashflow visibility, inventory normalization,
  asset support, or credible capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 6.16 | -15.38 | 66.7% | too generous to building-material/developer theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 6.16 | -15.38 | 33.3% | safer but may miss 035890 |
| P1 sector_specific_candidate_profile | 3 | 6.16 | -15.38 | 66.7% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 9.77 | -2.3 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 4.35 | -21.93 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 035890 | current_profile_correct_but_no_green | orderbook/cashflow bridge aligned with MFE but Green blocked by cycle risk |
| 007210 | current_profile_false_positive | building-material theme produced local MFE and high MAE |
| 010780 | current_profile_false_positive | developer rebound produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_ORDERBOOK_BALANCE_PF_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R10/C30 building-material/developer residual reduced |

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
- building-material theme without order/margin bridge
- regional housing orderbook winner needs 4B watch
- real-estate developer rebound high-MAE without balance/cashflow bridge
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
- R10 direct L9 sector consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/report URLs
- exact orderbook/PF/cashflow disclosure URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_orderbook_balance_pf_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction, housing, building-material or developer signal converts into orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, inventory normalization, asset support, or capital-structure bridge","035890 survives as guarded positive after regional housing orderbook/cashflow bridge; 007210 and 010780 are demoted because building-material/developer MFE lacked balance and cashflow bridge","TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE|TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R10 direct L9 branch"
shadow_weight,c30_building_material_developer_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional housing winners and building-material/developer false starts can peak before cashflow and balance durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 035890 guarded positive while preventing 007210/010780 construction-theme false positives","TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE|TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","symbol":"035890","company_name":"서희건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_HOUSING_ORDERBOOK_AND_PF_RISK_CONTAINMENT_TO_CASHFLOW_STABILITY_RERATING","case_type":"regional_housing_orderbook_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF/balance-sheet rows require orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, inventory normalization, asset support, or capital-structure bridge; construction/materials/developer price theme alone is insufficient."}
{"row_type":"case","case_id":"R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"007210","company_name":"벽산","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_BUILDING_MATERIALS_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"BUILDING_MATERIALS_REMODELING_THEME_WITHOUT_HOUSING_ORDER_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"building_materials_theme_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF/balance-sheet rows require orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, inventory normalization, asset support, or capital-structure bridge; construction/materials/developer price theme alone is insufficient."}
{"row_type":"case","case_id":"R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REAL_ESTATE_DEVELOPER_REBOUND_WITHOUT_BALANCE_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REAL_ESTATE_DEVELOPER_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_LIQUIDITY_OR_ORDER_CASHFLOW_CONVERSION","case_type":"developer_rebound_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C30 construction/PF/balance-sheet rows require orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, inventory normalization, asset support, or capital-structure bridge; construction/materials/developer price theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","case_id":"R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","symbol":"035890","company_name":"서희건설","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REGIONAL_HOUSING_ORDERBOOK_AND_PF_RISK_CONTAINMENT_TO_CASHFLOW_STABILITY_RERATING","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1259,"evidence_available_at_that_date":"source_proxy_regional_housing_orderbook_PF_risk_containment_cashflow_stability_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_housing_orderbook_PF_risk_containment_cashflow_stability_bridge; evidence_url_pending","bridge_summary":"regional housing orderbook and PF-risk containment converted into slow cashflow-stability rerating, but local peaks and housing-cycle risk required 4B watch","stage2_evidence_fields":["regional_housing_orderbook","PF_risk_containment_proxy","cashflow_stability_proxy","relative_strength"],"stage3_evidence_fields":["orderbook_to_cashflow_visibility","balance_sheet_stability","PF_liquidity_risk_containment"],"stage4b_evidence_fields":["slow_MFE_peak_watch","regional_housing_cycle_crowding"],"stage4c_evidence_fields":["housing_cycle_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv","profile_path":"atlas/symbol_profiles/035/035890.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.15,"MFE_90D_pct":9.77,"MFE_180D_pct":28.75,"MFE_1Y_pct":28.75,"MFE_2Y_pct":28.75,"MAE_30D_pct":-2.3,"MAE_90D_pct":-2.3,"MAE_180D_pct":-5.48,"MAE_1Y_pct":-5.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-10","peak_price":1621,"drawdown_after_peak_pct":-14.19,"green_lateness_ratio":"0.62","four_b_local_peak_proximity":0.83,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"slow_regional_housing_orderbook_positive_but_4B_housing_cycle_watch","four_b_evidence_type":"non_price_order_cashflow_PF_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"regional_housing_orderbook_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE","case_id":"R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"007210","company_name":"벽산","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_BUILDING_MATERIALS_THEME_WITHOUT_ORDER_MARGIN_BRIDGE","deep_sub_archetype_id":"BUILDING_MATERIALS_REMODELING_THEME_WITHOUT_HOUSING_ORDER_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","entry_date":"2024-01-10","entry_price":2770,"evidence_available_at_that_date":"source_proxy_building_materials_remodeling_theme_without_housing_order_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_building_materials_remodeling_theme_without_housing_order_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"building-materials/remodeling theme created a local price spike, but housing order, margin, inventory and cashflow bridge were absent; high MAE dominated the forward path","stage2_evidence_fields":["building_materials_theme","housing_repair_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_theme_peak","housing_order_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_order_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/007/007210/2024.csv","profile_path":"atlas/symbol_profiles/007/007210.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.05,"MFE_90D_pct":5.05,"MFE_180D_pct":5.05,"MFE_1Y_pct":5.05,"MFE_2Y_pct":5.05,"MAE_30D_pct":-13.18,"MAE_90D_pct":-24.91,"MAE_180D_pct":-32.85,"MAE_1Y_pct":-32.85,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-11","peak_price":2910,"drawdown_after_peak_pct":-36.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"building_materials_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_theme_without_balance_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"building_materials_theme_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE","case_id":"R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE","symbol":"010780","company_name":"아이에스동서","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REAL_ESTATE_DEVELOPER_REBOUND_WITHOUT_BALANCE_CASHFLOW_BRIDGE","deep_sub_archetype_id":"REAL_ESTATE_DEVELOPER_VALUE_REBOUND_WITHOUT_BALANCE_REPAIR_LIQUIDITY_OR_ORDER_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":30100,"evidence_available_at_that_date":"source_proxy_real_estate_developer_value_rebound_without_balance_repair_liquidity_order_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_real_estate_developer_value_rebound_without_balance_repair_liquidity_order_cashflow_bridge; evidence_url_pending","bridge_summary":"developer/property rebound theme failed to convert into durable balance repair, liquidity, order-to-cashflow, inventory normalization or capital-structure bridge","stage2_evidence_fields":["developer_value_rebound","property_cycle_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","balance_repair_bridge_absent","liquidity_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_balance_or_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv","profile_path":"atlas/symbol_profiles/010/010780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.65,"MFE_90D_pct":3.65,"MFE_180D_pct":3.65,"MFE_1Y_pct":3.65,"MFE_2Y_pct":3.65,"MAE_30D_pct":-18.44,"MAE_90D_pct":-18.94,"MAE_180D_pct":-32.39,"MAE_1Y_pct":-32.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-22","peak_price":31200,"drawdown_after_peak_pct":-34.78,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"developer_rebound_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_theme_without_balance_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"developer_rebound_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","trigger_id":"TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE","symbol":"035890","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":12,"balance_repair_score":10,"PF_risk_bridge_score":11,"liquidity_cashflow_score":11,"relative_strength_score":8,"risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":15,"balance_repair_score":12,"PF_risk_bridge_score":14,"liquidity_cashflow_score":14,"relative_strength_score":7,"risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 row is promoted only because regional housing orderbook and cashflow/PF-risk containment bridge exists; slow MFE and cycle risk keep 4B guard active.","MFE_90D_pct":9.77,"MAE_90D_pct":-2.3,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE","trigger_id":"TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE","symbol":"007210","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"balance_repair_score":1,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":9,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"balance_repair_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":3,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes building-materials/developer rebound theme rows when orderbook, balance repair, liquidity and cashflow bridge are absent.","MFE_90D_pct":5.05,"MAE_90D_pct":-24.91,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE","trigger_id":"TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE","symbol":"010780","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"balance_repair_score":1,"PF_risk_bridge_score":1,"liquidity_cashflow_score":0,"relative_strength_score":9,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"balance_repair_score":0,"PF_risk_bridge_score":0,"liquidity_cashflow_score":0,"relative_strength_score":3,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","liquidity_cashflow_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes building-materials/developer rebound theme rows when orderbook, balance repair, liquidity and cashflow bridge are absent.","MFE_90D_pct":3.65,"MAE_90D_pct":-18.94,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_orderbook_balance_pf_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction, housing, building-material or developer signal converts into orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality, order-to-cashflow, inventory normalization, asset support, or capital-structure bridge","035890 survives as guarded positive after regional housing orderbook/cashflow bridge; 007210 and 010780 are demoted because building-material/developer MFE lacked balance and cashflow bridge","TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE|TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R10 direct L9 branch"
shadow_weight,c30_building_material_developer_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional housing winners and building-material/developer false starts can peak before cashflow and balance durability is proven; local/full-window 4B and high-MAE watch should remain active","preserves 035890 guarded positive while preventing 007210/010780 construction-theme false positives","TRG_R10L75_C30_035890_20240129_REGIONAL_HOUSING_ORDERBOOK_CASHFLOW_BRIDGE|TRG_R10L75_C30_007210_20240110_BUILDING_MATERIALS_THEME_NO_ORDER_MARGIN_BRIDGE|TRG_R10L75_C30_010780_20240308_REAL_ESTATE_DEVELOPER_REBOUND_NO_BALANCE_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R10","loop":"75","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["building_material_theme_without_order_margin_bridge","regional_housing_orderbook_winner_needs_4B_watch","real_estate_developer_rebound_high_MAE_without_balance_cashflow_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R10-specific handling

- R10 maps to `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses `C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK`.
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
- price-only/construction-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R10 direct L9 sector.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C30 construction/PF rows cannot promote without orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality repair, order-to-cashflow visibility, inventory normalization, asset support, or capital-structure improvement.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R10
completed_loop = 75
next_round = R11
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
atlas/symbol_profiles/035/035890.json
atlas/symbol_profiles/007/007210.json
atlas/symbol_profiles/010/010780.json
atlas/ohlcv_tradable_by_symbol_year/035/035890/2024.csv
atlas/ohlcv_tradable_by_symbol_year/007/007210/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv
```

This loop continues loop 75 with R10 and adds 3 new independent C30 representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R10/L9.
