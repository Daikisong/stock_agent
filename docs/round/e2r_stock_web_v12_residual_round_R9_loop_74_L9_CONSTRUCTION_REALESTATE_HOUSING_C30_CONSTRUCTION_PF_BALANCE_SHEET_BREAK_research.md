# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R9
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R10
computed_next_loop: 74
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: C30_ORDER_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r9_branch: L9_CONSTRUCTION_REALESTATE_HOUSING_allowed
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

R9 allows either the L3 mobility branch or the L9 construction/real-estate branch. The previous R9 loop used the L3/C29 auto-parts branch, so this run rotates to the allowed L9 branch. The target is not the top-covered major builder cluster. It is the smaller construction/PF repair boundary: orderbook and cashflow bridge can create a guarded repair path, but regional-builder price heat without PF/liquidity repair should be demoted.

| layer | id | definition |
|---|---|---|
| round | R9 | mobility or construction bridge round |
| large_sector | L9_CONSTRUCTION_REALESTATE_HOUSING | construction, real estate, housing, PF and balance-sheet repair |
| canonical | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF, liquidity, balance sheet, trust and cashflow break/repair |
| fine | C30_ORDER_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | promotion requires order/balance/PF/liquidity/cashflow bridge |
| deep | DIVERSIFIED_CONSTRUCTION_INFRA_ORDERBOOK_TO_BALANCE_REPAIR_AND_PF_RISK_CONTAINMENT | diversified builder repair positive |
| deep | CIVIL_ENGINEERING_SUBCONTRACT_ORDERBOOK_TO_CASHFLOW_AND_BALANCE_STABILITY | civil engineering low-beta positive |
| deep | REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_BALANCE_OR_PF_REPAIR | regional builder false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols are `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that cluster and also avoids prior C30 representatives including `012630`, `002460`, `001470`, `375500`, `021320`, `014790`, `013580`, `004960`, and `002990`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C30 | 003070 | new independent | not top-covered C30 symbol; diversified builder/infrastructure PF repair bridge |
| C30 | 010960 | new independent | not top-covered C30 symbol; civil engineering order/cashflow low-beta bridge |
| C30 | 002410 | new independent | not top-covered C30 symbol; regional builder/PF cashflow break counterexample |

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
003070 has a 2023-01-31 corporate-action candidate, before the selected 2024 representative window; 2025-12-11 is after the window.
010960 has corporate-action candidates ending 2010, outside the selected 2024 window.
002410 has corporate-action candidates ending 2017, outside the selected 2024 window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_drawdown_watch | 003070 | 코오롱글로벌 | Stage2-Actionable | 2024-01-29 | 9470 | diversified builder infra/PF repair bridge worked late |
| modest_success_low_beta_cashflow_bridge | 010960 | 삼호개발 | Stage2-Actionable | 2024-02-01 | 3410 | civil engineering order/cashflow bridge worked modestly |
| failed_regional_builder_high_MAE_counterexample | 002410 | 범양건영 | Stage2-Actionable | 2024-01-29 | 1827 | regional builder/PF theme lacked cashflow and balance bridge |

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
| 003070 | 코오롱글로벌 | Stage2-Actionable | 2024-01-29 | 9470 | 12.99 | 12.99 | 60.51 | -7.07 | -10.45 | -10.45 | 2024-06-27 | 15200 | -44.08 |
| 010960 | 삼호개발 | Stage2-Actionable | 2024-02-01 | 3410 | 3.52 | 4.11 | 7.04 | -6.3 | -6.3 | -7.62 | 2024-07-30 | 3650 | -13.7 |
| 002410 | 범양건영 | Stage2-Actionable | 2024-01-29 | 1827 | 2.85 | 2.85 | 2.85 | -8.59 | -25.18 | -39.03 | 2024-01-29 | 1879 | -40.71 |

## 9. Case-by-Case Notes

### 9.1 003070 / 코오롱글로벌 — diversified builder repair bridge

The entry row is 2024-01-29 at 9,470. The early 30D/90D path was modest, but the wider 180D path eventually reached 15,200. This is a delayed C30 positive. The bridge is not construction-theme heat alone; it is infrastructure/orderbook visibility, PF-risk containment and balance repair. Because the move arrives late and then draws down, it should route to Yellow plus 4B watch, not Green.

### 9.2 010960 / 삼호개발 — civil engineering low-beta cashflow bridge

The entry row is 2024-02-01 at 3,410. The best 180D high reaches 3,650, and downside remains relatively contained. This is a low-beta C30 repair row. The signal is useful for balance/cashflow stability calibration, but the magnitude is too modest for Green. It is the kind of case that keeps the model from ignoring quiet cashflow repair while still preventing over-promotion.

### 9.3 002410 / 범양건영 — regional builder/PF cashflow break

The entry row is 2024-01-29 at 1,827. The local upside barely extends beyond entry while the forward low reaches 1,114. This is the C30 false-positive branch: a regional-builder rebound or PF relief story cannot substitute for order visibility, liquidity, cashflow, balance repair or trust quality.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C30 treats regional-builder/PF theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C30 needs order/balance/PF/liquidity/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 002410. |
| Full 4B non-price requirement appropriate? | Yes. 003070/010960 have better bridge evidence; 002410 does not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
003070:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed only after infra/orderbook and balance/PF-risk repair bridge
  Stage3-Green = reject unless delayed MFE and post-peak drawdown risk clear

010960:
  Stage2-Actionable = correct as low-beta repair
  Stage3-Yellow = allowed as guarded low-beta balance/cashflow bridge
  Stage3-Green = reject because MFE is modest

002410:
  Stage2-Actionable = too generous if based only on regional-builder/PF relief theme
  Stage3-Yellow = reject without order, cashflow, balance, liquidity or PF repair bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 003070 | 0.70 | 1.00 | delayed full-window 4B watch after infra/balance/PF repair bridge |
| 010960 | 0.94 | 1.00 | low-beta 4B watch after order/cashflow bridge |
| 002410 | 1.00 | 1.00 | regional-builder local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c30_requires_order_balance_pf_liquidity_cashflow_bridge

rule:
  For C30 construction/PF rows, do not promote regional builder, construction,
  housing, PF relief, value-rebound, or infrastructure-repair Stage2 signals into
  Stage3-Yellow/Green unless at least one non-price bridge is visible:
  orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing,
  trust-quality repair, order-to-cashflow visibility, asset sale, or credible
  capital-structure improvement.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 6.65 | -13.98 | 33.3% | useful but can over-credit regional-builder theme |
| P0b e2r_2_0_baseline_reference | 3 | 6.65 | -13.98 | 0% | safer but may miss 003070/010960 |
| P1 sector_specific_candidate_profile | 3 | 6.65 | -13.98 | 33.3% | no broad L9 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 8.55 | -8.38 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 2.85 | -25.18 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 003070 | current_profile_correct_with_drawdown_guard | delayed MFE aligns with order/balance/PF repair bridge but needs 4B |
| 010960 | current_profile_correct_but_no_green | low-beta cashflow bridge aligns with modest positive path |
| 002410 | current_profile_false_positive | regional-builder theme produced high MAE without source bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | C30_ORDER_BALANCE_PF_LIQUIDITY_CASHFLOW_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | R9 allowed L9/C30 non-top-covered construction/PF residual reduced |

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
- regional builder / PF theme without cashflow bridge
- construction low-beta positive needs no-Green guard
- delayed construction repair MFE requires 4B watch
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
- R9 allowed L9 branch consistency
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
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
shadow_weight,c30_requires_order_balance_pf_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction or housing rebound converts into orderbook, balance repair, PF-risk containment, liquidity/refinancing, cashflow, or trust-quality bridge","003070 and 010960 survive only as guarded positives with order/cashflow/PF bridge; 002410 fails when regional-builder theme lacks order, balance and cashflow bridge","TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE|TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE|TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK",3,3,1,medium,canonical_shadow_only,"not production; R9 allowed L9 branch"
shadow_weight,c30_regional_builder_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional-builder/PF rows can peak before cashflow and balance repair is proven; local/full-window 4B and high-MAE watch should remain active","preserves guarded 003070/010960 positives while preventing 002410 regional-builder false positive","TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE|TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE|TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE","symbol":"003070","company_name":"코오롱글로벌","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_DIVERSIFIED_BUILDER_INFRA_BALANCE_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"DIVERSIFIED_CONSTRUCTION_INFRA_ORDERBOOK_TO_BALANCE_REPAIR_AND_PF_RISK_CONTAINMENT","case_type":"structural_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_with_drawdown_guard","price_source":"Songdaiki/stock-web","notes":"R9 uses the allowed L9 construction branch. C30 rows require NAV/balance/PF/liquidity/order/cashflow bridge; regional-builder or construction/PF theme alone is insufficient."}
{"row_type":"case","case_id":"R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","symbol":"010960","company_name":"삼호개발","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","deep_sub_archetype_id":"CIVIL_ENGINEERING_SUBCONTRACT_ORDERBOOK_TO_CASHFLOW_AND_BALANCE_STABILITY","case_type":"modest_success_low_beta_cashflow_bridge","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_low_beta","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R9 uses the allowed L9 construction branch. C30 rows require NAV/balance/PF/liquidity/order/cashflow bridge; regional-builder or construction/PF theme alone is insufficient."}
{"row_type":"case","case_id":"R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK","symbol":"002410","company_name":"범양건영","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_PF_CASHFLOW_BREAK_WITHOUT_REPAIR_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_BALANCE_OR_PF_REPAIR","case_type":"failed_regional_builder_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R9 uses the allowed L9 construction branch. C30 rows require NAV/balance/PF/liquidity/order/cashflow bridge; regional-builder or construction/PF theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE","case_id":"R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE","symbol":"003070","company_name":"코오롱글로벌","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_DIVERSIFIED_BUILDER_INFRA_BALANCE_PF_REPAIR_BRIDGE","deep_sub_archetype_id":"DIVERSIFIED_CONSTRUCTION_INFRA_ORDERBOOK_TO_BALANCE_REPAIR_AND_PF_RISK_CONTAINMENT","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":9470,"evidence_available_at_that_date":"source_proxy_diversified_builder_infra_orderbook_PF_risk_containment_balance_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_diversified_builder_infra_orderbook_PF_risk_containment_balance_repair_bridge; evidence_url_pending","bridge_summary":"diversified construction/infrastructure orderbook and PF-risk containment created a delayed rerating path, but the path still required 4B drawdown guard","stage2_evidence_fields":["construction_value_repair","infra_orderbook_proxy","PF_risk_containment_proxy","relative_strength"],"stage3_evidence_fields":["orderbook_to_cashflow_visibility","balance_sheet_repair_proxy","PF_liquidity_risk_containment"],"stage4b_evidence_fields":["delayed_MFE_peak_watch","construction_PF_rerating_crowding"],"stage4c_evidence_fields":["drawdown_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv","profile_path":"atlas/symbol_profiles/003/003070.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.99,"MFE_90D_pct":12.99,"MFE_180D_pct":60.51,"MFE_1Y_pct":60.51,"MFE_2Y_pct":60.51,"MAE_30D_pct":-7.07,"MAE_90D_pct":-10.45,"MAE_180D_pct":-10.45,"MAE_1Y_pct":-10.45,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":15200,"drawdown_after_peak_pct":-44.08,"green_lateness_ratio":"0.55","four_b_local_peak_proximity":0.7,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"delayed_full_window_4B_watch_after_infra_balance_PF_repair_bridge","four_b_evidence_type":"non_price_order_balance_PF_cashflow_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"structural_success_then_4B_drawdown_watch","current_profile_verdict":"current_profile_correct_with_drawdown_guard","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","case_id":"R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","symbol":"010960","company_name":"삼호개발","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","deep_sub_archetype_id":"CIVIL_ENGINEERING_SUBCONTRACT_ORDERBOOK_TO_CASHFLOW_AND_BALANCE_STABILITY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3410,"evidence_available_at_that_date":"source_proxy_civil_engineering_orderbook_cashflow_balance_stability_bridge; evidence_url_pending","evidence_source":"source_proxy_civil_engineering_orderbook_cashflow_balance_stability_bridge; evidence_url_pending","bridge_summary":"civil-engineering orderbook and cashflow stability produced a low-beta repair path; the signal is useful but not explosive enough for Green","stage2_evidence_fields":["civil_engineering_orderbook","cashflow_stability_proxy","balance_sheet_stability","relative_strength"],"stage3_evidence_fields":["order_to_cashflow_visibility","low_MAE_balance_stability","construction_cycle_risk_containment"],"stage4b_evidence_fields":["low_beta_peak_watch","limited_upside_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv","profile_path":"atlas/symbol_profiles/010/010960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.52,"MFE_90D_pct":4.11,"MFE_180D_pct":7.04,"MFE_1Y_pct":7.04,"MFE_2Y_pct":7.04,"MAE_30D_pct":-6.3,"MAE_90D_pct":-6.3,"MAE_180D_pct":-7.62,"MAE_1Y_pct":-7.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-30","peak_price":3650,"drawdown_after_peak_pct":-13.7,"green_lateness_ratio":"0.64","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"low_beta_4B_watch_after_order_cashflow_bridge","four_b_evidence_type":"non_price_order_balance_PF_cashflow_bridge","four_c_protection_label":"none","trigger_outcome_label":"modest_structural_success_low_beta","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK","case_id":"R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK","symbol":"002410","company_name":"범양건영","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"C30_REGIONAL_BUILDER_PF_CASHFLOW_BREAK_WITHOUT_REPAIR_BRIDGE","deep_sub_archetype_id":"REGIONAL_BUILDER_VALUE_REBOUND_WITHOUT_ORDER_CASHFLOW_BALANCE_OR_PF_REPAIR","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":1827,"evidence_available_at_that_date":"source_proxy_regional_builder_value_rebound_without_order_cashflow_balance_PF_repair_bridge; evidence_url_pending","evidence_source":"source_proxy_regional_builder_value_rebound_without_order_cashflow_balance_PF_repair_bridge; evidence_url_pending","bridge_summary":"regional builder value-rebound and PF relief theme did not convert into order visibility, balance repair, liquidity or cashflow bridge; the path became high-MAE protection evidence","stage2_evidence_fields":["regional_builder_theme","PF_relief_expectation","price_rebound","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","cashflow_bridge_absent","PF_balance_repair_absent"],"stage4c_evidence_fields":["high_MAE_without_order_cashflow_or_PF_repair"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv","profile_path":"atlas/symbol_profiles/002/002410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.85,"MFE_90D_pct":2.85,"MFE_180D_pct":2.85,"MFE_1Y_pct":2.85,"MFE_2Y_pct":2.85,"MAE_30D_pct":-8.59,"MAE_90D_pct":-25.18,"MAE_180D_pct":-39.03,"MAE_1Y_pct":-39.03,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-29","peak_price":1879,"drawdown_after_peak_pct":-40.71,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"regional_builder_local_4B_watch_not_positive_stage","four_b_evidence_type":"construction_theme_without_balance_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_regional_builder_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE","trigger_id":"TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE","symbol":"003070","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":11,"balance_repair_score":10,"PF_risk_bridge_score":10,"cashflow_liquidity_score":9,"relative_strength_score":10,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":14,"balance_repair_score":13,"PF_risk_bridge_score":13,"cashflow_liquidity_score":11,"relative_strength_score":7,"risk_penalty":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","cashflow_liquidity_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 construction/infrastructure row is promoted only because orderbook and balance/PF-risk bridge exists; delayed MFE and drawdown keep 4B guard active.","MFE_90D_pct":12.99,"MAE_90D_pct":-10.45,"score_return_alignment_label":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_with_drawdown_guard"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","trigger_id":"TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE","symbol":"010960","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":10,"balance_repair_score":9,"PF_risk_bridge_score":9,"cashflow_liquidity_score":11,"relative_strength_score":6,"risk_penalty":5},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":12,"balance_repair_score":11,"PF_risk_bridge_score":10,"cashflow_liquidity_score":13,"relative_strength_score":5,"risk_penalty":6},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","cashflow_liquidity_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 low-beta civil-engineering row is a guarded Yellow only; cashflow stability helps but limited MFE blocks Green.","MFE_90D_pct":4.11,"MAE_90D_pct":-6.3,"score_return_alignment_label":"score_return_aligned_low_beta","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK","trigger_id":"TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK","symbol":"002410","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","raw_component_scores_before":{"orderbook_score":3,"balance_repair_score":1,"PF_risk_bridge_score":1,"cashflow_liquidity_score":0,"relative_strength_score":9,"risk_penalty":9},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"orderbook_score":0,"balance_repair_score":0,"PF_risk_bridge_score":0,"cashflow_liquidity_score":0,"relative_strength_score":3,"risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["orderbook_score","balance_repair_score","PF_risk_bridge_score","cashflow_liquidity_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C30 guard demotes regional-builder/PF theme rows when order, balance repair, liquidity and cashflow bridge are absent.","MFE_90D_pct":2.85,"MAE_90D_pct":-25.18,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c30_requires_order_balance_pf_liquidity_cashflow_bridge,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"C30 construction/PF rows should not promote toward Stage3-Yellow/Green unless construction or housing rebound converts into orderbook, balance repair, PF-risk containment, liquidity/refinancing, cashflow, or trust-quality bridge","003070 and 010960 survive only as guarded positives with order/cashflow/PF bridge; 002410 fails when regional-builder theme lacks order, balance and cashflow bridge","TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE|TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE|TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK",3,3,1,medium,canonical_shadow_only,"not production; R9 allowed L9 branch"
shadow_weight,c30_regional_builder_4b_high_mae_watch_guard,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,1,1,0,"Regional-builder/PF rows can peak before cashflow and balance repair is proven; local/full-window 4B and high-MAE watch should remain active","preserves guarded 003070/010960 positives while preventing 002410 regional-builder false positive","TRG_R9L74_C30_003070_20240129_DIVERSIFIED_BUILDER_INFRA_PF_REPAIR_BRIDGE|TRG_R9L74_C30_010960_20240201_CIVIL_ENGINEERING_ORDER_CASHFLOW_LOW_BETA_BRIDGE|TRG_R9L74_C30_002410_20240129_REGIONAL_BUILDER_PF_CASHFLOW_BREAK",3,3,1,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R9","loop":"74","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["regional_builder_PF_theme_without_cashflow_bridge","construction_low_beta_positive_needs_no_green","delayed_construction_repair_MFE_requires_4B_watch"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R9-specific handling

- R9 may use `L3_BATTERY_EV_GREEN_MOBILITY` or `L9_CONSTRUCTION_REALESTATE_HOUSING`.
- This MD uses the allowed L9 construction branch.
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
3. Validate R9 allowed branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C30 construction/PF rows cannot promote without orderbook/backlog, NAV/balance repair, PF-risk containment, liquidity/refinancing, trust-quality repair, order-to-cashflow visibility, asset sale, or capital-structure improvement.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R9
completed_loop = 74
next_round = R10
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
atlas/symbol_profiles/003/003070.json
atlas/symbol_profiles/010/010960.json
atlas/symbol_profiles/002/002410.json
atlas/ohlcv_tradable_by_symbol_year/003/003070/2024.csv
atlas/ohlcv_tradable_by_symbol_year/010/010960/2024.csv
atlas/ohlcv_tradable_by_symbol_year/002/002410/2024.csv
```

This loop continues loop 74 with R9 and adds 3 new independent C30 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R9/L9.
