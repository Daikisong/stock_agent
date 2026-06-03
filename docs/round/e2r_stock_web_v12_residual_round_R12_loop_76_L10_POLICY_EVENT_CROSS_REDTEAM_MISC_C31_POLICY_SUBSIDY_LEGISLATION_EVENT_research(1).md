# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 76
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 76
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_CASINO_TOURISM_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r12_branch: under_covered_casino_tourism_policy_branch
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches. The previous R12 loop used C31 agri/smart-farm, and older R12 service/tourism work used tour agency / leisure representatives. This run keeps C31 but rotates to an under-covered casino/tourism policy branch.

| layer | id | definition |
|---|---|---|
| round | R12 | policy/event or under-covered service/agri/tourism residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy, subsidy, legislation, service/agri/tourism cross-red-team |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/subsidy/event must become economics |
| fine | C31_CASINO_TOURISM_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE_GUARD | casino/tourism signal must become visitor, revenue, margin and cashflow evidence |
| deep | DOMESTIC_CASINO_POLICY_CAPACITY_VISITOR_RECOVERY_TO_REVENUE_MARGIN_AND_CASHFLOW | domestic casino positive |
| deep | FOREIGNER_CASINO_VISITOR_RECOVERY_THEME_WITHOUT_DROP_AMOUNT_REVENUE_MARGIN_OR_CASHFLOW_CONVERSION | foreign casino false positive |
| deep | INTEGRATED_RESORT_AND_CASINO_TOURISM_OPTIONALITY_WITHOUT_OCCUPANCY_DROP_AMOUNT_MARGIN_OR_CASHFLOW_CONVERSION | integrated resort false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that cluster and also avoids prior C31 service/tourism representatives `039130`, `080160`, `034230`, policy-to-economics symbols `015760`, `013990`, `339950`, and agri-policy symbols `186230`, `097870`, `025860`, `002900`, `000490`, and `054050`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 035250 | new independent | not top-covered C31 symbol; domestic casino policy/visitor/margin bridge |
| C31 | 114090 | new independent | not top-covered C31 symbol; foreign casino visitor recovery without durable revenue/margin bridge |
| C31 | 032350 | new independent | not top-covered C31 symbol; integrated resort tourism MFE without cashflow/debt bridge |

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
MFE/MAE/peak/drawdown computed = true
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
corporate_action_window_status = clean_180D_window
```

Corporate-action caveat:

```text
035250 has a 2003-11-04 corporate-action candidate, outside the selected 2024 representative window.
114090 has no corporate-action candidate dates.
032350 has corporate-action candidates ending 2018-11-01, outside the selected 2024 representative window.
All three representative windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| casino_policy_visitor_margin_success_then_4B_watch | 035250 | 강원랜드 | Stage2-Actionable | 2024-01-29 | 15110 | domestic casino policy/visitor/margin bridge worked, but 4B drawdown watch required |
| foreign_casino_visitor_theme_low_MFE_high_MAE_counterexample | 114090 | GKL | Stage2-Actionable | 2024-01-29 | 12990 | foreign casino recovery theme lacked durable drop amount/margin/cashflow bridge |
| integrated_resort_tourism_MFE_then_high_MAE_counterexample | 032350 | 롯데관광개발 | Stage2-Actionable | 2024-01-29 | 9110 | integrated resort tourism MFE lacked occupancy/drop amount/cashflow bridge |

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
| 035250 | 강원랜드 | Stage2-Actionable | 2024-01-29 | 15110 | 21.38 | 21.38 | 23.16 | -1.06 | -3.31 | -11.78 | 2024-09-05 | 18610 | -11.61 |
| 114090 | GKL | Stage2-Actionable | 2024-01-29 | 12990 | 5.62 | 8.47 | 8.47 | -8.01 | -8.01 | -17.55 | 2024-04-05 | 14090 | -23.99 |
| 032350 | 롯데관광개발 | Stage2-Actionable | 2024-01-29 | 9110 | 5.93 | 17.67 | 17.67 | -3.29 | -3.29 | -11.2 | 2024-04-01 | 10720 | -24.53 |

## 9. Case-by-Case Notes

### 9.1 035250 / 강원랜드 — casino policy-to-visitor margin bridge

The entry row is 2024-01-29 at 15,110. The path reached 18,340 in the early window and later reached 18,610. This is a valid C31 positive only as guarded Yellow. The bridge is not generic tourism heat; it is domestic casino policy/capacity normalization, visitor recovery, revenue quality, margin and cashflow. The later low around 13,330 and post-peak drawdown keep 4B active.

### 9.2 114090 / GKL — foreign casino visitor theme without durable margin bridge

The entry row is 2024-01-29 at 12,990. The path reached 14,090, but later fell to 10,710. This is a clean C31 counterexample: foreign-casino visitor recovery can create shallow MFE, but without drop amount, visitor mix, revenue quality, margin and cashflow bridge, it should not receive Stage3 credit.

### 9.3 032350 / 롯데관광개발 — integrated resort MFE without cashflow bridge

The entry row is 2024-01-29 at 9,110. The stock reached 10,720, but the wider path fell to 8,090. Integrated resort and casino tourism optionality may produce MFE, but without occupancy, casino drop amount, margin, debt burden and cashflow evidence, it should remain Watch/4B/high-MAE rather than Stage3-Green.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats casino/tourism recovery MFE as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 needs visitor/revenue/margin/cashflow bridge before Yellow. |
| Stage3 Green too strict? | Correct. This round reinforces strict Green. |
| Price-only blowoff guard appropriate? | Yes, especially for 114090 and 032350. |
| Full 4B non-price requirement appropriate? | Yes. 035250 has a better bridge; 114090/032350 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
035250:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after casino policy / visitor / revenue / margin / cashflow bridge
  Stage3-Green = reject unless regulatory reversal and post-peak tourism-cycle risk clear

114090:
  Stage2-Actionable = too generous if based only on foreign casino visitor-recovery theme
  Stage3-Yellow = reject without drop amount, visitor mix, revenue quality, margin and cashflow bridge
  Stage3-Green = reject despite MFE

032350:
  Stage2-Actionable = acceptable only as integrated-resort tourism watch
  Stage3-Yellow = reject without occupancy, casino drop amount, margin and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 035250 | 0.99 | 1.00 | casino visitor/margin bridge positive but full-window 4B watch |
| 114090 | 1.00 | 1.00 | foreign casino visitor theme local 4B watch, not positive stage |
| 032350 | 1.00 | 1.00 | integrated resort tourism MFE but no cashflow bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_casino_tourism_requires_policy_visitor_revenue_margin_cashflow_bridge

rule:
  For C31 casino/tourism policy-event rows, do not promote casino,
  foreigner casino, domestic casino, integrated resort, tourism recovery,
  visa/flight recovery, policy-capacity, or leisure-service Stage2 signals into
  Stage3-Yellow/Green unless at least one non-price bridge is visible:
  policy-to-demand conversion, visitor demand, drop amount, occupancy,
  revenue quality, channel/visitor mix, margin conversion, working-capital control,
  debt burden improvement, FCF/cash conversion, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 15.84 | -4.87 | 66.7% | too generous to casino/tourism theme MFE |
| P0b e2r_2_0_baseline_reference | 3 | 15.84 | -4.87 | 33.3% | safer but may miss 035250 |
| P1 sector_specific_candidate_profile | 3 | 15.84 | -4.87 | 66.7% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 21.38 | -3.31 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 13.07 | -5.65 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 035250 | current_profile_correct_but_no_green | visitor/revenue/margin bridge aligned with MFE, but 4B watch remains |
| 114090 | current_profile_false_positive | foreign casino MFE lacked durable revenue/margin bridge |
| 032350 | current_profile_false_positive_if_green | integrated resort MFE lacked cashflow/debt bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_CASINO_TOURISM_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R12/C31 casino-tourism residual reduced |

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
- casino tourism theme without revenue/margin/cashflow bridge
- domestic casino policy winner needs 4B watch
- integrated resort tourism MFE then high MAE
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
- R12 allowed under-covered casino/tourism branch
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean windows outside listed corporate-action candidate dates
```

Not validated:

```text
- exact disclosure/news URLs
- exact casino policy / visitor / revenue / margin disclosure URLs
- production scoring behavior
- live candidate status
- previous tour agency/leisure symbols intentionally skipped
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_casino_tourism_requires_policy_visitor_revenue_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 casino/tourism policy rows should not promote toward Stage3-Yellow/Green unless policy/event signal converts into visitor demand, drop amount, occupancy, revenue quality, margin, working-capital, debt burden improvement, FCF or cashflow bridge","035250 survives as guarded positive after domestic casino policy/visitor/margin bridge; 114090 and 032350 are demoted because foreign-casino or integrated-resort tourism theme MFE lacked durable revenue quality, margin and cashflow bridge","TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE|TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered casino/tourism branch"
shadow_weight,c31_casino_tourism_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Casino/tourism winners and tourism-theme false starts can peak before visitor quality, margin and cashflow durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 035250 guarded positive while preventing 114090/032350 tourism theme false positives","TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE|TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","symbol":"035250","company_name":"강원랜드","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","deep_sub_archetype_id":"DOMESTIC_CASINO_POLICY_CAPACITY_VISITOR_RECOVERY_TO_REVENUE_MARGIN_AND_CASHFLOW","case_type":"casino_policy_visitor_margin_success_then_4B_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R12 under-covered casino/tourism policy branch: C31 policy/event rows require policy-to-demand, visitor/drop amount, occupancy, revenue quality, margin, debt/cashflow or working-capital bridge; tourism/casino theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"114090","company_name":"GKL","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_FOREIGN_CASINO_VISITOR_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"FOREIGNER_CASINO_VISITOR_RECOVERY_THEME_WITHOUT_DROP_AMOUNT_REVENUE_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"foreign_casino_visitor_theme_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 under-covered casino/tourism policy branch: C31 policy/event rows require policy-to-demand, visitor/drop amount, occupancy, revenue quality, margin, debt/cashflow or working-capital bridge; tourism/casino theme MFE alone is insufficient."}
{"row_type":"case","case_id":"R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_INTEGRATED_RESORT_TOURISM_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"INTEGRATED_RESORT_AND_CASINO_TOURISM_OPTIONALITY_WITHOUT_OCCUPANCY_DROP_AMOUNT_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"integrated_resort_tourism_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R12 under-covered casino/tourism policy branch: C31 policy/event rows require policy-to-demand, visitor/drop amount, occupancy, revenue quality, margin, debt/cashflow or working-capital bridge; tourism/casino theme MFE alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","case_id":"R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","symbol":"035250","company_name":"강원랜드","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","deep_sub_archetype_id":"DOMESTIC_CASINO_POLICY_CAPACITY_VISITOR_RECOVERY_TO_REVENUE_MARGIN_AND_CASHFLOW","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":15110,"evidence_available_at_that_date":"source_proxy_domestic_casino_policy_capacity_visitor_recovery_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_domestic_casino_policy_capacity_visitor_recovery_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"domestic casino policy/capacity and visitor recovery converted into revenue, margin and cashflow bridge, but post-peak tourism-policy and regulatory crowding risk required 4B watch","stage2_evidence_fields":["casino_policy_capacity","visitor_recovery_proxy","relative_strength","margin_cashflow_proxy"],"stage3_evidence_fields":["visitor_to_revenue_visibility","margin_cashflow_bridge","policy_capacity_normalization_proxy"],"stage4b_evidence_fields":["post_MFE_peak_watch","casino_policy_crowding","regulatory_reversal_risk"],"stage4c_evidence_fields":["post_peak_drawdown_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv","profile_path":"atlas/symbol_profiles/035/035250.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":21.38,"MFE_90D_pct":21.38,"MFE_180D_pct":23.16,"MFE_1Y_pct":23.16,"MFE_2Y_pct":23.16,"MAE_30D_pct":-1.06,"MAE_90D_pct":-3.31,"MAE_180D_pct":-11.78,"MAE_1Y_pct":-11.78,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-05","peak_price":18610,"drawdown_after_peak_pct":-11.61,"green_lateness_ratio":"0.44","four_b_local_peak_proximity":0.99,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casino_policy_visitor_margin_bridge_positive_but_full_window_4B_watch","four_b_evidence_type":"non_price_policy_visitor_margin_cashflow_bridge","four_c_protection_label":"post_peak_drawdown_watch","trigger_outcome_label":"casino_policy_visitor_margin_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE","case_id":"R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"114090","company_name":"GKL","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_FOREIGN_CASINO_VISITOR_THEME_WITHOUT_DURABLE_MARGIN_BRIDGE","deep_sub_archetype_id":"FOREIGNER_CASINO_VISITOR_RECOVERY_THEME_WITHOUT_DROP_AMOUNT_REVENUE_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":12990,"evidence_available_at_that_date":"source_proxy_foreigner_casino_visitor_recovery_theme_without_drop_amount_revenue_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_foreigner_casino_visitor_recovery_theme_without_drop_amount_revenue_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"foreign-casino visitor recovery theme produced only low-quality MFE; drop amount, visitor mix, revenue quality, margin and cashflow bridge did not become durable","stage2_evidence_fields":["foreign_casino_recovery_theme","visitor_rebound_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","drop_amount_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_visitor_revenue_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv","profile_path":"atlas/symbol_profiles/114/114090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.62,"MFE_90D_pct":8.47,"MFE_180D_pct":8.47,"MFE_1Y_pct":8.47,"MFE_2Y_pct":8.47,"MAE_30D_pct":-8.01,"MAE_90D_pct":-8.01,"MAE_180D_pct":-17.55,"MAE_1Y_pct":-17.55,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-05","peak_price":14090,"drawdown_after_peak_pct":-23.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"foreign_casino_visitor_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"casino_tourism_theme_without_revenue_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"foreign_casino_visitor_theme_low_MFE_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE","case_id":"R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE","symbol":"032350","company_name":"롯데관광개발","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_INTEGRATED_RESORT_TOURISM_THEME_WITHOUT_CASHFLOW_BRIDGE","deep_sub_archetype_id":"INTEGRATED_RESORT_AND_CASINO_TOURISM_OPTIONALITY_WITHOUT_OCCUPANCY_DROP_AMOUNT_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":9110,"evidence_available_at_that_date":"source_proxy_integrated_resort_casino_tourism_optionality_without_occupancy_drop_amount_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_integrated_resort_casino_tourism_optionality_without_occupancy_drop_amount_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"integrated-resort/casino tourism optionality produced MFE, but occupancy, casino drop amount, revenue quality, margin, debt burden and cashflow bridge did not remain durable","stage2_evidence_fields":["integrated_resort_tourism_theme","casino_visitor_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["tourism_theme_MFE_peak","occupancy_drop_amount_bridge_absent","cashflow_debt_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_resort_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv","profile_path":"atlas/symbol_profiles/032/032350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.93,"MFE_90D_pct":17.67,"MFE_180D_pct":17.67,"MFE_1Y_pct":17.67,"MFE_2Y_pct":17.67,"MAE_30D_pct":-3.29,"MAE_90D_pct":-3.29,"MAE_180D_pct":-11.2,"MAE_1Y_pct":-11.2,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":10720,"drawdown_after_peak_pct":-24.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"integrated_resort_tourism_MFE_but_no_cashflow_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"casino_tourism_theme_without_revenue_margin_cashflow_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"integrated_resort_tourism_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","trigger_id":"TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE","symbol":"035250","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":11,"visitor_demand_score":12,"revenue_quality_score":10,"margin_cashflow_score":11,"relative_strength_score":9,"theme_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":13,"visitor_demand_score":15,"revenue_quality_score":12,"margin_cashflow_score":14,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["policy_event_score","visitor_demand_score","revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 casino/tourism row is promoted only because policy/visitor signal converts into revenue quality, margin and cashflow bridge; regulatory and post-peak 4B risk block Green.","MFE_90D_pct":21.38,"MAE_90D_pct":-3.31,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE","trigger_id":"TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE","symbol":"114090","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":10,"visitor_demand_score":6,"revenue_quality_score":2,"margin_cashflow_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"visitor_demand_score":2,"revenue_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","visitor_demand_score","revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes casino/tourism theme rows when visitor quality, drop amount, occupancy, margin, debt and cashflow bridge are absent.","MFE_90D_pct":8.47,"MAE_90D_pct":-8.01,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE","trigger_id":"TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE","symbol":"032350","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":10,"visitor_demand_score":6,"revenue_quality_score":2,"margin_cashflow_score":0,"relative_strength_score":9,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"visitor_demand_score":2,"revenue_quality_score":0,"margin_cashflow_score":0,"relative_strength_score":3,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","visitor_demand_score","revenue_quality_score","margin_cashflow_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes casino/tourism theme rows when visitor quality, drop amount, occupancy, margin, debt and cashflow bridge are absent.","MFE_90D_pct":17.67,"MAE_90D_pct":-3.29,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_casino_tourism_requires_policy_visitor_revenue_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 casino/tourism policy rows should not promote toward Stage3-Yellow/Green unless policy/event signal converts into visitor demand, drop amount, occupancy, revenue quality, margin, working-capital, debt burden improvement, FCF or cashflow bridge","035250 survives as guarded positive after domestic casino policy/visitor/margin bridge; 114090 and 032350 are demoted because foreign-casino or integrated-resort tourism theme MFE lacked durable revenue quality, margin and cashflow bridge","TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE|TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered casino/tourism branch"
shadow_weight,c31_casino_tourism_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Casino/tourism winners and tourism-theme false starts can peak before visitor quality, margin and cashflow durability are confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 035250 guarded positive while preventing 114090/032350 tourism theme false positives","TRG_R12L76_C31_035250_20240129_CASINO_POLICY_VISITOR_REVENUE_MARGIN_BRIDGE|TRG_R12L76_C31_114090_20240129_FOREIGN_CASINO_VISITOR_THEME_NO_DURABLE_MARGIN_BRIDGE|TRG_R12L76_C31_032350_20240129_INTEGRATED_RESORT_TOURISM_THEME_NO_CASHFLOW_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"76","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["casino_tourism_theme_without_revenue_margin_cashflow_bridge","domestic_casino_policy_winner_needs_4B_watch","integrated_resort_tourism_MFE_then_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R12-specific handling

- R12 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri/tourism branches.
- This MD uses a C31 casino/tourism policy branch.
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
- Positive score promotion requires non-price evidence and clean MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only/casino-tourism-theme-only rows cannot promote Stage2/Stage3.
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
12. Add validation that C31 casino/tourism rows cannot promote without policy-to-demand conversion, visitor demand, drop amount, occupancy, revenue quality, visitor/channel mix, margin conversion, working-capital control, debt burden improvement, FCF/cash conversion, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R12
completed_loop = 76
next_round = R13
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
atlas/symbol_profiles/035/035250.json
atlas/symbol_profiles/114/114090.json
atlas/symbol_profiles/032/032350.json
atlas/ohlcv_tradable_by_symbol_year/035/035250/2024.csv
atlas/ohlcv_tradable_by_symbol_year/114/114090/2024.csv
atlas/ohlcv_tradable_by_symbol_year/032/032350/2024.csv
```

This loop continues loop 76 with R12 and adds 3 new independent C31 casino/tourism representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R12/L10.
