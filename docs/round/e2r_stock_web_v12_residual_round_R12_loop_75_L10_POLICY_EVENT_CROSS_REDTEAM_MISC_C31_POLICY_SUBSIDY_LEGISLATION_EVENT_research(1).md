# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 75
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 75
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_AGRI_SMARTFARM_POLICY_ORDER_VOLUME_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r12_branch: under_covered_agri_smartfarm_branch
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches. The previous R12 loop used C31 service/tourism. This run keeps the C31 policy/event container but rotates to an under-covered agri/smart-farm branch: smart-farm order economics versus fertilizer/food-security theme spikes that fail to become volume, spread, margin or cashflow evidence.

| layer | id | definition |
|---|---|---|
| round | R12 | policy/event or under-covered service/agri residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, subsidy, service/agri cross-red-team |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/event must become economics |
| fine | C31_AGRI_SMARTFARM_POLICY_ORDER_VOLUME_MARGIN_BRIDGE_GUARD | agri signal must become order, volume, spread, margin or cashflow bridge |
| deep | SMART_FARM_FACILITY_POLICY_ORDER_EXPORT_TO_REVENUE_MARGIN_AND_CASHFLOW_OPTION | smart-farm positive |
| deep | ORGANIC_FERTILIZER_FOOD_SECURITY_POLICY_THEME_WITHOUT_VOLUME_PRICE_COST_MARGIN_CONVERSION | organic fertilizer false positive |
| deep | FERTILIZER_AND_FOOD_SECURITY_POLICY_OPTIONALITY_WITHOUT_PRICE_COST_SPREAD_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION | fertilizer false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that cluster and avoids prior C31 service/tourism symbols `039130`, `080160`, `034230`, prior policy-to-economics symbols `015760`, `013990`, `339950`, and earlier agri-policy symbols `002900`, `000490`, `054050`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 186230 | new independent | not top-covered C31 symbol; smart-farm policy/order/export margin bridge |
| C31 | 097870 | new independent | not top-covered C31 symbol; organic fertilizer/food-security theme without volume/margin bridge |
| C31 | 025860 | new independent | not top-covered C31 symbol; fertilizer/food-security theme without price-cost spread bridge |
| reviewed | 001550 | not used | usable but lower residual value than selected false-positive set |

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
186230 has corporate-action candidates ending 2020-11-13, outside the selected 2024 representative window.
097870 has a 2018-05-18 corporate-action candidate, outside the selected 2024 representative window.
025860 has corporate-action candidates ending 2002-10-07, outside the selected 2024 representative window.
001550/조비 was inspected but not selected; its 2024 path had lower residual value for this loop.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| smart_farm_policy_order_success_then_4B_watch | 186230 | 그린플러스 | Stage2-Actionable | 2024-02-21 | 9200 | smart-farm policy/order/export bridge worked, but 4B cashflow watch required |
| organic_fertilizer_theme_MFE_then_high_MAE_counterexample | 097870 | 효성오앤비 | Stage2-Actionable | 2024-06-26 | 7390 | organic fertilizer/food-security theme lacked volume/margin bridge |
| fertilizer_policy_theme_low_MFE_high_MAE_counterexample | 025860 | 남해화학 | Stage2-Actionable | 2024-07-17 | 7140 | fertilizer policy MFE lacked price-cost spread and margin bridge |

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
| 186230 | 그린플러스 | Stage2-Actionable | 2024-02-21 | 9200 | 24.89 | 24.89 | 32.61 | -12.83 | -22.07 | -22.07 | 2024-08-20 | 12200 | -31.48 |
| 097870 | 효성오앤비 | Stage2-Actionable | 2024-06-26 | 7390 | 16.91 | 16.91 | 16.91 | -8.93 | -24.22 | -24.22 | 2024-06-27 | 8640 | -35.19 |
| 025860 | 남해화학 | Stage2-Actionable | 2024-07-17 | 7140 | 6.44 | 6.44 | 6.44 | -12.04 | -13.17 | -13.17 | 2024-07-23 | 7600 | -18.42 |

## 9. Case-by-Case Notes

### 9.1 186230 / 그린플러스 — smart-farm policy-to-order bridge

The entry row is 2024-02-21 at 9,200. The path reached 11,490 in the early window and later reached 12,200. This is a valid C31 positive only as guarded Yellow because the bridge is policy-to-facility order, export/revenue optionality, margin and cashflow, not just smart-farm theme language. The forward low and post-peak drawdown keep 4B watch active.

### 9.2 097870 / 효성오앤비 — organic fertilizer policy theme without margin bridge

The entry row is 2024-06-26 at 7,390. The next local high reached 8,640, but the later low reached 5,600. This is the agri-policy false-positive branch: fertilizer and food-security language can move price, but without volume, subsidy-to-demand, price-cost spread, margin and cashflow bridge, it should not become Stage3 evidence.

### 9.3 025860 / 남해화학 — fertilizer/food-security theme without spread bridge

The entry row is 2024-07-17 at 7,140. The high reached 7,600, while the later low reached 6,200. This row is less dramatic but cleaner as a low-quality MFE case: fertilizer optionality without price-cost spread, volume and margin conversion should stay Watch/4B.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats fertilizer/food-security theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 needs policy-to-order, volume, spread, margin or cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 097870 local spike. |
| Full 4B non-price requirement appropriate? | Yes. 186230 has a better non-price bridge; 097870/025860 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
186230:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after smart-farm policy/order/revenue bridge
  Stage3-Green = reject unless project timing, cashflow and working-capital durability clear

097870:
  Stage2-Actionable = too generous if based only on organic fertilizer / food-security theme
  Stage3-Yellow = reject without volume, subsidy-to-demand, margin and cashflow bridge
  Stage3-Green = reject despite MFE

025860:
  Stage2-Actionable = too generous if based only on fertilizer/food-security policy option
  Stage3-Yellow = reject without price-cost spread, volume and margin bridge
  Stage3-Green = reject
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 186230 | 0.75 | 1.00 | smart-farm policy/order bridge positive but full-window 4B cashflow watch |
| 097870 | 1.00 | 1.00 | fertilizer policy theme local 4B watch, not positive stage |
| 025860 | 1.00 | 1.00 | fertilizer food-security theme local 4B watch, not positive stage |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_agri_requires_policy_to_order_volume_spread_margin_cashflow_bridge

rule:
  For C31 agri/smart-farm policy-event rows, do not promote smart-farm,
  fertilizer, organic fertilizer, food security, crop-input, subsidy, or agri-policy
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  policy-to-order conversion, facility order backlog, subsidy-to-demand, export/revenue visibility,
  volume pull-through, price-cost spread, inventory normalization, margin conversion,
  working-capital control, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 16.08 | -19.82 | 66.7% | too generous to fertilizer/food-security theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 16.08 | -19.82 | 33.3% | safer but may miss 186230 |
| P1 sector_specific_candidate_profile | 3 | 16.08 | -19.82 | 66.7% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 24.89 | -22.07 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 11.68 | -18.7 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 186230 | current_profile_correct_but_no_green | policy/order bridge aligned with MFE, but cashflow/drawdown watch blocks Green |
| 097870 | current_profile_false_positive | organic fertilizer theme produced high MAE without volume/margin bridge |
| 025860 | current_profile_false_positive | fertilizer/food-security row produced low-quality MFE without spread bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_AGRI_SMARTFARM_POLICY_ORDER_VOLUME_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R12 agri/smart-farm C31 residual reduced |

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
- agri policy theme without volume/margin bridge
- smart-farm order winner needs 4B watch
- fertilizer food-security local MFE high-MAE
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
- R12 allowed agri/smart-farm branch
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/news URLs
- exact policy/subsidy/order announcement URLs
- production scoring behavior
- live candidate status
- 001550 as representative row; reviewed but not selected
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_agri_requires_policy_to_order_volume_spread_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 agri/smart-farm policy rows should not promote toward Stage3-Yellow/Green unless policy/subsidy/food-security signal converts into facility order, subsidy-to-demand, export/revenue, volume, price-cost spread, margin, working-capital, or cashflow bridge","186230 survives as guarded positive after smart-farm order/revenue bridge; 097870 and 025860 are demoted because fertilizer/food-security themes lacked durable volume/spread/margin bridge","TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE|TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE|TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered agri/smart-farm branch"
shadow_weight,c31_agri_policy_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Agri/smart-farm winners and fertilizer-theme false starts can peak before order/spread/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 186230 guarded positive while preventing 097870/025860 agri-policy theme false positives","TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE|TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE|TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE","symbol":"186230","company_name":"그린플러스","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SMART_FARM_POLICY_ORDER_EXPORT_MARGIN_BRIDGE","deep_sub_archetype_id":"SMART_FARM_FACILITY_POLICY_ORDER_EXPORT_TO_REVENUE_MARGIN_AND_CASHFLOW_OPTION","case_type":"smart_farm_policy_order_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/smart-farm branch: C31 policy/subsidy rows require policy-to-order, subsidy-to-demand, volume, price-cost spread, margin, working capital, or cashflow bridge; food-security/fertilizer theme alone is insufficient."}
{"row_type":"case","case_id":"R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE","symbol":"097870","company_name":"효성오앤비","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_ORGANIC_FERTILIZER_POLICY_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"ORGANIC_FERTILIZER_FOOD_SECURITY_POLICY_THEME_WITHOUT_VOLUME_PRICE_COST_MARGIN_CONVERSION","case_type":"organic_fertilizer_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/smart-farm branch: C31 policy/subsidy rows require policy-to-order, subsidy-to-demand, volume, price-cost spread, margin, working capital, or cashflow bridge; food-security/fertilizer theme alone is insufficient."}
{"row_type":"case","case_id":"R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE","symbol":"025860","company_name":"남해화학","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_FERTILIZER_FOOD_SECURITY_THEME_WITHOUT_PRICE_COST_SPREAD_BRIDGE","deep_sub_archetype_id":"FERTILIZER_AND_FOOD_SECURITY_POLICY_OPTIONALITY_WITHOUT_PRICE_COST_SPREAD_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"fertilizer_policy_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 under-covered agri/smart-farm branch: C31 policy/subsidy rows require policy-to-order, subsidy-to-demand, volume, price-cost spread, margin, working capital, or cashflow bridge; food-security/fertilizer theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE","case_id":"R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE","symbol":"186230","company_name":"그린플러스","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SMART_FARM_POLICY_ORDER_EXPORT_MARGIN_BRIDGE","deep_sub_archetype_id":"SMART_FARM_FACILITY_POLICY_ORDER_EXPORT_TO_REVENUE_MARGIN_AND_CASHFLOW_OPTION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":9200,"evidence_available_at_that_date":"source_proxy_smart_farm_policy_order_export_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_smart_farm_policy_order_export_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"smart-farm facility policy and order/export optionality converted into revenue and margin bridge, but project timing, cashflow and working-capital risk required 4B watch","stage2_evidence_fields":["smart_farm_policy","facility_order_proxy","export_optionality","relative_strength"],"stage3_evidence_fields":["policy_to_order_visibility","order_to_revenue_bridge","margin_cashflow_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","project_timing_risk","working_capital_cashflow_watch"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/186/186230/2024.csv","profile_path":"atlas/symbol_profiles/186/186230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":24.89,"MFE_90D_pct":24.89,"MFE_180D_pct":32.61,"MFE_1Y_pct":32.61,"MFE_2Y_pct":32.61,"MAE_30D_pct":-12.83,"MAE_90D_pct":-22.07,"MAE_180D_pct":-22.07,"MAE_1Y_pct":-22.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-20","peak_price":12200,"drawdown_after_peak_pct":-31.48,"green_lateness_ratio":"0.55","four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"smart_farm_policy_order_bridge_positive_but_full_window_4B_cashflow_watch","four_b_evidence_type":"non_price_policy_order_margin_cashflow_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"smart_farm_policy_order_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE","case_id":"R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE","symbol":"097870","company_name":"효성오앤비","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_ORGANIC_FERTILIZER_POLICY_THEME_WITHOUT_VOLUME_MARGIN_BRIDGE","deep_sub_archetype_id":"ORGANIC_FERTILIZER_FOOD_SECURITY_POLICY_THEME_WITHOUT_VOLUME_PRICE_COST_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-06-26","entry_date":"2024-06-26","entry_price":7390,"evidence_available_at_that_date":"source_proxy_organic_fertilizer_food_security_policy_theme_without_volume_price_cost_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_organic_fertilizer_food_security_policy_theme_without_volume_price_cost_margin_bridge; evidence_url_pending","bridge_summary":"organic fertilizer and food-security policy theme produced MFE, but volume, price-cost spread, subsidy pass-through, margin, and cashflow bridge did not persist","stage2_evidence_fields":["organic_fertilizer_theme","food_security_policy","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["local_policy_theme_peak","volume_margin_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_volume_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/097/097870/2024.csv","profile_path":"atlas/symbol_profiles/097/097870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.91,"MFE_90D_pct":16.91,"MFE_180D_pct":16.91,"MFE_1Y_pct":16.91,"MFE_2Y_pct":16.91,"MAE_30D_pct":-8.93,"MAE_90D_pct":-24.22,"MAE_180D_pct":-24.22,"MAE_1Y_pct":-24.22,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-27","peak_price":8640,"drawdown_after_peak_pct":-35.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fertilizer_policy_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"agri_policy_theme_without_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"organic_fertilizer_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE","case_id":"R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE","symbol":"025860","company_name":"남해화학","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_FERTILIZER_FOOD_SECURITY_THEME_WITHOUT_PRICE_COST_SPREAD_BRIDGE","deep_sub_archetype_id":"FERTILIZER_AND_FOOD_SECURITY_POLICY_OPTIONALITY_WITHOUT_PRICE_COST_SPREAD_VOLUME_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","entry_date":"2024-07-17","entry_price":7140,"evidence_available_at_that_date":"source_proxy_fertilizer_food_security_policy_optionality_without_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_fertilizer_food_security_policy_optionality_without_price_cost_spread_volume_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"fertilizer/food-security policy optionality produced a short local MFE, but price-cost spread, volume, margin and cashflow bridge remained weak","stage2_evidence_fields":["fertilizer_policy_theme","food_security_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","price_cost_spread_bridge_absent","volume_margin_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_spread_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025860/2024.csv","profile_path":"atlas/symbol_profiles/025/025860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.44,"MFE_90D_pct":6.44,"MFE_180D_pct":6.44,"MFE_1Y_pct":6.44,"MFE_2Y_pct":6.44,"MAE_30D_pct":-12.04,"MAE_90D_pct":-13.17,"MAE_180D_pct":-13.17,"MAE_1Y_pct":-13.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-23","peak_price":7600,"drawdown_after_peak_pct":-18.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"fertilizer_food_security_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"agri_policy_theme_without_volume_margin_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"fertilizer_policy_theme_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE","trigger_id":"TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE","symbol":"186230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":11,"order_or_subsidy_score":11,"volume_spread_score":8,"margin_cashflow_score":9,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":13,"order_or_subsidy_score":14,"volume_spread_score":10,"margin_cashflow_score":12,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":78,"stage_label_after":"Stage3-Yellow","changed_components":["policy_event_score","order_or_subsidy_score","volume_spread_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 agri/smart-farm row is promoted only because policy signal converts into order/revenue and margin/cashflow bridge; delayed MFE and drawdown keep 4B active.","MFE_90D_pct":24.89,"MAE_90D_pct":-22.07,"score_return_alignment_label":"score_return_aligned_late","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE","trigger_id":"TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE","symbol":"097870","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":11,"order_or_subsidy_score":2,"volume_spread_score":1,"margin_cashflow_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"order_or_subsidy_score":0,"volume_spread_score":0,"margin_cashflow_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","order_or_subsidy_score","volume_spread_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes agri/fertilizer/food-security theme rows when volume, spread, subsidy-to-demand, margin and cashflow bridge are absent.","MFE_90D_pct":16.91,"MAE_90D_pct":-24.22,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE","trigger_id":"TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE","symbol":"025860","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":11,"order_or_subsidy_score":2,"volume_spread_score":1,"margin_cashflow_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"order_or_subsidy_score":0,"volume_spread_score":0,"margin_cashflow_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","order_or_subsidy_score","volume_spread_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes agri/fertilizer/food-security theme rows when volume, spread, subsidy-to-demand, margin and cashflow bridge are absent.","MFE_90D_pct":6.44,"MAE_90D_pct":-13.17,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_agri_requires_policy_to_order_volume_spread_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 agri/smart-farm policy rows should not promote toward Stage3-Yellow/Green unless policy/subsidy/food-security signal converts into facility order, subsidy-to-demand, export/revenue, volume, price-cost spread, margin, working-capital, or cashflow bridge","186230 survives as guarded positive after smart-farm order/revenue bridge; 097870 and 025860 are demoted because fertilizer/food-security themes lacked durable volume/spread/margin bridge","TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE|TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE|TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered agri/smart-farm branch"
shadow_weight,c31_agri_policy_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Agri/smart-farm winners and fertilizer-theme false starts can peak before order/spread/margin durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 186230 guarded positive while preventing 097870/025860 agri-policy theme false positives","TRG_R12L75_C31_186230_20240221_SMART_FARM_POLICY_ORDER_EXPORT_BRIDGE|TRG_R12L75_C31_097870_20240626_ORGANIC_FERTILIZER_POLICY_THEME_NO_MARGIN_BRIDGE|TRG_R12L75_C31_025860_20240717_FERTILIZER_FOOD_SECURITY_THEME_NO_SPREAD_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"75","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["agri_policy_theme_without_volume_margin_bridge","smart_farm_order_winner_needs_4B_watch","fertilizer_food_security_local_MFE_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R12-specific handling

- R12 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches.
- This MD uses a C31 under-covered agri/smart-farm branch.
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
- price-only/agri-policy-theme-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate R12 allowed branch and large_sector_id.
4. Validate canonical_archetype_id.
5. Validate novelty and reuse fields.
6. Deduplicate same_entry_group_id and reused cases.
7. Aggregate by large_sector_id and canonical_archetype_id.
8. Update sector_shadow_profile and archetype_shadow_profile only.
9. Preserve global calibrated profile unless explicitly promoted.
10. Report new independent cases, counterexamples, and residual error types.
11. Add tests that duplicate low-value loops cannot change weights.
12. Add validation that C31 agri/smart-farm policy rows cannot promote without policy-to-order conversion, facility order backlog, subsidy-to-demand, export/revenue visibility, volume pull-through, price-cost spread, inventory normalization, margin conversion, working-capital control, FCF/cash conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R12
completed_loop = 75
next_round = R13
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
atlas/symbol_profiles/186/186230.json
atlas/symbol_profiles/097/097870.json
atlas/symbol_profiles/025/025860.json
atlas/symbol_profiles/001/001550.json
atlas/ohlcv_tradable_by_symbol_year/186/186230/2024.csv
atlas/ohlcv_tradable_by_symbol_year/097/097870/2024.csv
atlas/ohlcv_tradable_by_symbol_year/025/025860/2024.csv
atlas/ohlcv_tradable_by_symbol_year/001/001550/2024.csv
```

This loop continues loop 75 with R12 and adds 3 new independent C31 agri/smart-farm representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R12/L10.
