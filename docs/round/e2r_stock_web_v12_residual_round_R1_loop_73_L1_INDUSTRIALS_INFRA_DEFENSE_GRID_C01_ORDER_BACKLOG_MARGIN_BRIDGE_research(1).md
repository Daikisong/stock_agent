# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R1
scheduled_loop: 73
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R2
computed_next_loop: 73
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: C01_SHIPYARD_ENGINE_BACKLOG_MARGIN_FCF_BRIDGE_GUARD
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

R13 / loop 72 has closed, so the scheduler rolls to `R1 / loop 73`. R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`. This run avoids the immediately prior R1/C05 EPC-margin gap and moves to C01. The selected residual is the bridge between order backlog and actual economics: backlog headlines can look like a cargo manifest, but the ship only sails if margin, working capital, delivery, customer quality, and FCF turn with it.

| layer | id | definition |
|---|---|---|
| round | R1 | industrials / infrastructure / defense / grid |
| large_sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID | infrastructure, shipbuilding, plant, defense, grid industrials |
| canonical | C01_ORDER_BACKLOG_MARGIN_BRIDGE | order backlog must convert into margin, cash, and delivery evidence |
| fine | C01_SHIPYARD_ENGINE_BACKLOG_MARGIN_FCF_BRIDGE_GUARD | shipyard/engine backlog must become margin and FCF |
| deep | LNG_NAVAL_OFFSHORE_BACKLOG_TO_MARGIN_AND_FCF_RECOVERY | shipyard backlog turnaround |
| deep | MARINE_ENGINE_ORDER_BACKLOG_TO_MARGIN_LEVERAGE_WITH_4B_GUARD | marine-engine backlog margin bridge |
| deep | OFFSHORE_WIND_FABRICATION_BACKLOG_THEME_WITH_WORKING_CAPITAL_MARGIN_RISK | backlog theme false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C01 top-covered symbols are `010620`, `329180`, `009540`, `010140`, `077970`, and `082740`. This run avoids that cluster and also avoids the prior R1/C05 representative symbols.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C01 | 042660 | new independent | not top-covered C01 symbol; shipyard backlog/margin turnaround |
| C01 | 071970 | new independent | not top-covered C01 symbol; marine-engine backlog/margin bridge |
| C01 | 100090 | new independent | not top-covered C01 symbol; offshore-wind/order theme counterexample |

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
042660 has corporate-action candidate dates before this representative 2024 entry window.
071970 has old corporate-action candidate dates and no flagged 2024 180D contamination.
100090 has a 2022 candidate date before this 2023 entry window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| structural_success_then_4B_watch | 042660 | 한화오션 | Stage2-Actionable | 2024-02-27 | 24150 | shipyard backlog/margin turnaround worked |
| structural_success_with_drawdown_watch | 071970 | HD현대마린엔진 | Stage2-Actionable | 2024-04-18 | 13990 | marine-engine backlog/margin bridge worked, but 4B/high-MAE guard needed |
| failed_rerating_high_MAE | 100090 | SK오션플랜트 | Stage2-Actionable | 2023-07-25 | 22900 | offshore-wind/order backlog theme without margin/working-capital bridge failed |

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
| 042660 | 한화오션 | Stage2-Actionable | 2024-02-27 | 24150 | 27.95 | 42.65 | 69.98 | -7.87 | -7.87 | -7.87 | 2024-11-15 | 41050 | -27.28 |
| 071970 | HD현대마린엔진 | Stage2-Actionable | 2024-04-18 | 13990 | 27.23 | 77.63 | 77.63 | -8.15 | -8.15 | -8.15 | 2024-07-31 | 24850 | -36.98 |
| 100090 | SK오션플랜트 | Stage2-Actionable | 2023-07-25 | 22900 | 2.62 | 2.62 | 2.62 | -10.92 | -35.55 | -44.02 | 2023-08-01 | 23500 | -45.45 |

## 9. Case-by-Case Notes

### 9.1 042660 / 한화오션 — shipyard backlog to margin-turnaround bridge

The entry row is 2024-02-27 at 24,150. The forward window reaches 30,900 in the 30D window, 34,450 by the 90D window, and 41,050 later. This is a valid C01 route because the thesis is not merely “shipbuilding is strong.” It requires backlog quality, vessel/project mix, delivery visibility, and margin/FCF recovery.

### 9.2 071970 / HD현대마린엔진 — marine-engine backlog bridge with 4B guard

The entry row is 2024-04-18 at 13,990. The price path reaches 24,850, but later drawdown from the peak is large. This validates the backlog-to-margin bridge for the marine-engine sub-chain, while also arguing that C01 winners still need 4B/high-MAE watch after fast MFE.

### 9.3 100090 / SK오션플랜트 — order/backlog theme without margin bridge

The entry row is 2023-07-25 at 22,900. Upside stalls near 23,500 while the later path falls to 12,820. This is the C01 failure mode: offshore-wind or fabrication backlog language can be real, but if working capital, margin conversion, and FCF visibility do not arrive, the “backlog” becomes inventory in the market’s warehouse.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C01 treats order/backlog or offshore-wind theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C01 needs backlog-to-margin/FCF bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for order-theme false starts and fast 4B winners. |
| Full 4B non-price requirement appropriate? | Yes. 042660/071970 have better non-price backlog bridge; 100090 does not. |
| 4C timing issue? | High-MAE watch is useful for 100090; no immediate hard 4C promotion proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
042660:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after backlog-to-margin and FCF recovery bridge
  Stage3-Green = wait for stronger cash conversion and post-MFE 4B review

071970:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after engine backlog/margin bridge
  Stage3-Green = reject unless drawdown guard, delivery durability, and margin cycle risk clear

100090:
  Stage2-Actionable = too generous if based only on order/offshore-wind fabrication theme
  Stage3-Yellow = reject without margin, working-capital, delivery, or FCF bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 042660 | 0.92 | 1.00 | good full-window 4B watch after backlog/margin bridge |
| 071970 | 0.95 | 1.00 | good 4B watch but requires margin-cycle drawdown guard |
| 100090 | 1.00 | 1.00 | weak local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c01_requires_backlog_to_margin_working_capital_fcf_bridge

rule:
  For C01 order/backlog rows, do not promote order, backlog, shipbuilding,
  offshore fabrication, or industrial capex Stage2 signals into Stage3-Yellow/Green
  unless at least one non-price bridge is visible:
  backlog-to-margin conversion, working-capital containment, delivery schedule,
  customer/project quality, FCF/cash collection, or earnings revision tied to backlog conversion.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 40.97 | -17.19 | 33.3% | useful but can over-credit order-theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 40.97 | -17.19 | 0% | safer but may miss 042660/071970 |
| P1 sector_specific_candidate_profile | 3 | 40.97 | -17.19 | 33.3% | no broad L1 loosen |
| P2 canonical_archetype_candidate_profile | 2 selected positives | 60.14 | -8.01 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 1 rejected | 2.62 | -35.55 | 0% after demotion | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 042660 | current_profile_correct | backlog/margin bridge aligned with strong MFE and contained MAE |
| 071970 | current_profile_partially_correct | engine backlog bridge worked, but peak drawdown requires 4B/high-MAE watch |
| 100090 | current_profile_false_positive | order/offshore-wind theme produced shallow MFE and high MAE |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | C01_SHIPYARD_ENGINE_BACKLOG_MARGIN_FCF_BRIDGE_GUARD | 2 | 1 | 3 | 2 | 3 | 0 | 3 | 3 | 1 | false | true | C01 non-top-covered shipyard/engine/offshore backlog residual reduced |

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
- order backlog theme without margin bridge
- shipyard backlog winner needs 4B watch
- offshore wind fabrication high-MAE after backlog theme
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
shadow_weight,c01_requires_backlog_to_margin_working_capital_fcf_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 order/backlog rows should not promote toward Stage3-Yellow/Green unless backlog converts into margin, working-capital containment, FCF visibility, delivery schedule, or customer-quality bridge","042660 and 071970 survive with strong MFE after backlog/margin bridge; 100090 fails when order/offshore-wind theme lacks margin/working-capital/FCF bridge","TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND|TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE|TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_order_backlog_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,"Shipyard/engine backlog winners and offshore-fabrication failures can peak before margin durability is confirmed; local 4B/high-MAE watch should remain active","preserves 042660/071970 positives while preventing 100090 order-theme false positive","TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND|TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE|TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND","symbol":"042660","company_name":"한화오션","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPYARD_BACKLOG_MARGIN_TURNAROUND_BRIDGE","deep_sub_archetype_id":"LNG_NAVAL_OFFSHORE_BACKLOG_TO_MARGIN_AND_FCF_RECOVERY","case_type":"structural_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"C01 order backlog rows require backlog-to-margin, working-capital, FCF, customer-quality, or delivery conversion bridge; order/backlog theme alone is insufficient."}
{"row_type":"case","case_id":"R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIP_ENGINE_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"MARINE_ENGINE_ORDER_BACKLOG_TO_MARGIN_LEVERAGE_WITH_4B_GUARD","case_type":"structural_success_with_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct","price_source":"Songdaiki/stock-web","notes":"C01 order backlog rows require backlog-to-margin, working-capital, FCF, customer-quality, or delivery conversion bridge; order/backlog theme alone is insufficient."}
{"row_type":"case","case_id":"R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE","symbol":"100090","company_name":"SK오션플랜트","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_OFFSHORE_WIND_ORDER_THEME_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"OFFSHORE_WIND_FABRICATION_BACKLOG_THEME_WITH_WORKING_CAPITAL_MARGIN_RISK","case_type":"failed_rerating_high_MAE","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"C01 order backlog rows require backlog-to-margin, working-capital, FCF, customer-quality, or delivery conversion bridge; order/backlog theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND","case_id":"R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND","symbol":"042660","company_name":"한화오션","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIPYARD_BACKLOG_MARGIN_TURNAROUND_BRIDGE","deep_sub_archetype_id":"LNG_NAVAL_OFFSHORE_BACKLOG_TO_MARGIN_AND_FCF_RECOVERY","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-27","entry_date":"2024-02-27","entry_price":24150,"evidence_available_at_that_date":"source_proxy_shipyard_order_backlog_margin_turnaround_FCF_bridge; evidence_url_pending","evidence_source":"source_proxy_shipyard_order_backlog_margin_turnaround_FCF_bridge; evidence_url_pending","bridge_summary":"shipyard backlog and mix/order-quality route converted into margin-turnaround and FCF-recovery optionality rather than simple shipbuilding theme strength","stage2_evidence_fields":["shipyard_order_backlog","margin_turnaround_proxy","relative_strength","customer_or_vessel_mix_quality"],"stage3_evidence_fields":["backlog_to_margin_conversion","FCF_recovery_proxy","non_price_order_quality_bridge"],"stage4b_evidence_fields":["post_MFE_peak_watch","shipyard_crowding_after_backlog_rerating"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv","profile_path":"atlas/symbol_profiles/042/042660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.95,"MFE_90D_pct":42.65,"MFE_180D_pct":69.98,"MFE_1Y_pct":69.98,"MFE_2Y_pct":69.98,"MAE_30D_pct":-7.87,"MAE_90D_pct":-7.87,"MAE_180D_pct":-7.87,"MAE_1Y_pct":-7.87,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-15","peak_price":41050,"drawdown_after_peak_pct":-27.28,"green_lateness_ratio":"0.39","four_b_local_peak_proximity":0.92,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_watch_after_backlog_margin_bridge","four_b_evidence_type":"non_price_backlog_margin_bridge","four_c_protection_label":"none","trigger_outcome_label":"structural_success_then_4B_watch","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE","case_id":"R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE","symbol":"071970","company_name":"HD현대마린엔진","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_SHIP_ENGINE_BACKLOG_MARGIN_BRIDGE","deep_sub_archetype_id":"MARINE_ENGINE_ORDER_BACKLOG_TO_MARGIN_LEVERAGE_WITH_4B_GUARD","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-18","entry_date":"2024-04-18","entry_price":13990,"evidence_available_at_that_date":"source_proxy_marine_engine_order_backlog_margin_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_marine_engine_order_backlog_margin_leverage_bridge; evidence_url_pending","bridge_summary":"ship-engine order backlog and propulsion-cycle visibility produced strong MFE, but post-peak drawdown required 4B/high-MAE watch rather than Green loosening","stage2_evidence_fields":["marine_engine_backlog","shipbuilding_cycle_order_pullthrough","relative_strength","margin_leverage_proxy"],"stage3_evidence_fields":["backlog_to_revenue_visibility","engine_margin_conversion","customer_shipyard_pullthrough"],"stage4b_evidence_fields":["post_MFE_peak_watch","engine_cycle_crowding","valuation_repricing_after_MFE"],"stage4c_evidence_fields":["high_MAE_watch_after_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv","profile_path":"atlas/symbol_profiles/071/071970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":27.23,"MFE_90D_pct":77.63,"MFE_180D_pct":77.63,"MFE_1Y_pct":77.63,"MFE_2Y_pct":77.63,"MAE_30D_pct":-8.15,"MAE_90D_pct":-8.15,"MAE_180D_pct":-8.15,"MAE_1Y_pct":-8.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":24850,"drawdown_after_peak_pct":-36.98,"green_lateness_ratio":"0.34","four_b_local_peak_proximity":0.95,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_watch_but_requires_margin_cycle_drawdown_guard","four_b_evidence_type":"non_price_backlog_margin_bridge","four_c_protection_label":"high_MAE_watch_after_peak","trigger_outcome_label":"structural_success_but_needs_4B_high_MAE_guard","current_profile_verdict":"current_profile_partially_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE","case_id":"R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE","symbol":"100090","company_name":"SK오션플랜트","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"C01_OFFSHORE_WIND_ORDER_THEME_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"OFFSHORE_WIND_FABRICATION_BACKLOG_THEME_WITH_WORKING_CAPITAL_MARGIN_RISK","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2023-07-25","entry_date":"2023-07-25","entry_price":22900,"evidence_available_at_that_date":"source_proxy_offshore_wind_fabrication_order_theme_without_margin_working_capital_bridge; evidence_url_pending","evidence_source":"source_proxy_offshore_wind_fabrication_order_theme_without_margin_working_capital_bridge; evidence_url_pending","bridge_summary":"offshore-wind/order backlog theme failed to convert into margin, working-capital, or FCF bridge and reversed into high MAE","stage2_evidence_fields":["offshore_wind_order_theme","fabrication_backlog_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","working_capital_margin_risk","order_theme_reversal_watch"],"stage4c_evidence_fields":["high_MAE_without_margin_or_FCF_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/100/100090/2023.csv|atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv","profile_path":"atlas/symbol_profiles/100/100090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.62,"MFE_90D_pct":2.62,"MFE_180D_pct":2.62,"MFE_1Y_pct":2.62,"MFE_2Y_pct":2.62,"MAE_30D_pct":-10.92,"MAE_90D_pct":-35.55,"MAE_180D_pct":-44.02,"MAE_1Y_pct":-44.02,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-01","peak_price":23500,"drawdown_after_peak_pct":-45.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"weak_local_4B_watch_not_positive_stage","four_b_evidence_type":"order_theme_without_margin_working_capital_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_rerating_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND","trigger_id":"TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND","symbol":"042660","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":12,"margin_bridge_score":11,"working_capital_score":7,"FCF_visibility_score":8,"customer_quality_score":9,"relative_strength_score":10,"risk_penalty":4},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":14,"margin_bridge_score":15,"working_capital_score":10,"FCF_visibility_score":11,"customer_quality_score":11,"relative_strength_score":8,"risk_penalty":4},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["order_backlog_score","margin_bridge_score","working_capital_score","FCF_visibility_score","customer_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C01 row is promoted only because order backlog converts into margin, FCF, customer quality, and delivery visibility.","MFE_90D_pct":42.65,"MAE_90D_pct":-7.87,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE","trigger_id":"TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE","symbol":"071970","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":11,"margin_bridge_score":10,"working_capital_score":6,"FCF_visibility_score":6,"customer_quality_score":8,"relative_strength_score":11,"risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":13,"margin_bridge_score":13,"working_capital_score":7,"FCF_visibility_score":8,"customer_quality_score":10,"relative_strength_score":8,"risk_penalty":9},"weighted_score_after":77,"stage_label_after":"Stage3-Yellow","changed_components":["order_backlog_score","margin_bridge_score","working_capital_score","FCF_visibility_score","customer_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C01 backlog bridge works, but post-MFE drawdown requires 4B/high-MAE watch and prevents Green loosening.","MFE_90D_pct":77.63,"MAE_90D_pct":-8.15,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_partially_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE","trigger_id":"TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE","symbol":"100090","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","raw_component_scores_before":{"order_backlog_score":8,"margin_bridge_score":1,"working_capital_score":0,"FCF_visibility_score":0,"customer_quality_score":3,"relative_strength_score":10,"risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"order_backlog_score":4,"margin_bridge_score":0,"working_capital_score":0,"FCF_visibility_score":0,"customer_quality_score":1,"relative_strength_score":4,"risk_penalty":15},"weighted_score_after":41,"stage_label_after":"Stage1-Watch","changed_components":["order_backlog_score","margin_bridge_score","working_capital_score","FCF_visibility_score","customer_quality_score","relative_strength_score","risk_penalty"],"component_delta_explanation":"C01 guard demotes order/backlog theme rows when margin, working-capital, FCF, or delivery bridge is absent.","MFE_90D_pct":2.62,"MAE_90D_pct":-35.55,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c01_requires_backlog_to_margin_working_capital_fcf_bridge,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"C01 order/backlog rows should not promote toward Stage3-Yellow/Green unless backlog converts into margin, working-capital containment, FCF visibility, delivery schedule, or customer-quality bridge","042660 and 071970 survive with strong MFE after backlog/margin bridge; 100090 fails when order/offshore-wind theme lacks margin/working-capital/FCF bridge","TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND|TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE|TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c01_order_backlog_4b_high_mae_watch_guard,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,1,1,0,"Shipyard/engine backlog winners and offshore-fabrication failures can peak before margin durability is confirmed; local 4B/high-MAE watch should remain active","preserves 042660/071970 positives while preventing 100090 order-theme false positive","TRG_R1L73_C01_042660_20240227_SHIPYARD_BACKLOG_MARGIN_TURNAROUND|TRG_R1L73_C01_071970_20240418_ENGINE_BACKLOG_MARGIN_BRIDGE|TRG_R1L73_C01_100090_20230725_OFFSHORE_WIND_ORDER_THEME_NO_MARGIN_BRIDGE",3,3,1,medium,existing_axis_kept,"strengthens local 4B/high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R1","loop":"73","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["order_backlog_theme_without_margin_bridge","shipyard_backlog_winner_needs_4B_watch","offshore_wind_fabrication_high_MAE_after_backlog_theme"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
- price-only/order-theme-only rows cannot promote Stage2/Stage3.
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
11. Add validation that C01 order/backlog rows cannot promote without margin, working-capital, FCF, or delivery bridge.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R1
completed_loop = 73
next_round = R2
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
atlas/symbol_profiles/042/042660.json
atlas/symbol_profiles/071/071970.json
atlas/symbol_profiles/100/100090.json
atlas/ohlcv_tradable_by_symbol_year/042/042660/2024.csv
atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/100/100090/2023.csv
atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv
```

This loop starts loop 73 with R1 and adds 3 new independent C01 representative cases, 2 positives, 1 counterexample, and 1 canonical-archetype residual guard candidate for R1/L1.
