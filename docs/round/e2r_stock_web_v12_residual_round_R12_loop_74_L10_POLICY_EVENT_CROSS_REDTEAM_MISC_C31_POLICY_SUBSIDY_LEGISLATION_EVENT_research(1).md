# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
scheduled_round: R12
scheduled_loop: 74
round_schedule_status: valid
round_sector_consistency: pass
computed_next_round: R13
computed_next_loop: 74
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: C31_SERVICE_TOURISM_DEMAND_MARGIN_CASHFLOW_BRIDGE_GUARD
loop_objective: coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
r12_branch: under_covered_service_tourism_branch
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

R12 allows `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches. The previous R12 loop used C31 policy-to-economics with utility, low-birth and education-policy names, and the previous R11 loop used C32 governance/control premium. This run keeps the C31 policy/event container but rotates to the under-covered service/tourism branch.

| layer | id | definition |
|---|---|---|
| round | R12 | policy/event or under-covered service/agri residual |
| large_sector | L10_POLICY_EVENT_CROSS_REDTEAM_MISC | policy/event, service reopening, tourism and cross-red-team |
| canonical | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | policy/event signal must become economics |
| fine | C31_SERVICE_TOURISM_DEMAND_MARGIN_CASHFLOW_BRIDGE_GUARD | service/tourism signal must become demand, margin and cashflow bridge |
| deep | OUTBOUND_TRAVEL_RECOVERY_PACKAGE_DEMAND_TO_MARGIN_OPERATING_LEVERAGE | travel package demand positive |
| deep | OUTBOUND_TRAVEL_REOPENING_THEME_WITHOUT_PACKAGE_MARGIN_OR_CASHFLOW_CONVERSION | travel-agent false positive |
| deep | CASINO_INBOUND_RECOVERY_OPTIONALITY_WITHOUT_VIP_DROP_HOLD_RATE_MARGIN_CONVERSION | casino/inbound false positive |

## 3. No-Repeat / Coverage Check

No-Repeat hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 top-covered symbols are `UNKNOWN_SYMBOL`, `004090`, `036460`, `112610`, `005860`, and `008970`. This run avoids that cluster and also avoids prior R12 service/tourism symbols `114090`, `032350`, `008770`, as well as the prior C31 policy-to-economics symbols `015760`, `013990`, `339950` and older agri-policy symbols `002900`, `000490`, `054050`.

| archetype | selected symbol | duplicate status | reason |
|---|---:|---|---|
| C31 | 039130 | new independent | not top-covered C31 symbol; outbound travel demand/package margin bridge |
| C31 | 080160 | new independent | not top-covered C31 symbol; travel-agent theme without durable margin/cashflow bridge |
| C31 | 034230 | new independent | not top-covered C31 symbol; casino/inbound tourism MFE without durable drop/margin bridge |

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
039130 has corporate-action candidate dates in 2003 and 2004, outside the selected 2024 representative window.
080160 has corporate-action candidates ending 2017, outside the selected 2024 representative window.
034230 has no corporate-action candidate contamination in the selected 2024 representative window.
All three representative 180D windows are treated as clean for this residual calibration.
```

## 6. Case Selection Summary

| role | symbol | company | trigger | entry | price | result |
|---|---:|---|---|---:|---:|---|
| service_demand_recovery_success_then_4B_drawdown_watch | 039130 | 하나투어 | Stage2-Actionable | 2024-01-29 | 60900 | outbound travel/package demand margin bridge worked, but later drawdown required 4B |
| travel_agent_low_MFE_high_MAE_counterexample | 080160 | 모두투어 | Stage2-Actionable | 2024-01-29 | 17070 | travel reopening theme lacked margin/cashflow bridge |
| casino_theme_MFE_then_high_MAE_counterexample | 034230 | 파라다이스 | Stage2-Actionable | 2024-01-29 | 12750 | casino/inbound tourism MFE lacked durable drop/hold-rate margin bridge |

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
| 039130 | 하나투어 | Stage2-Actionable | 2024-01-29 | 60900 | 12.97 | 15.93 | 15.93 | -3.28 | -8.87 | -27.5 | 2024-03-25 | 70600 | -37.46 |
| 080160 | 모두투어 | Stage2-Actionable | 2024-01-29 | 17070 | 4.04 | 4.04 | 4.04 | -10.84 | -10.84 | -40.25 | 2024-02-14 | 17760 | -42.57 |
| 034230 | 파라다이스 | Stage2-Actionable | 2024-01-29 | 12750 | 6.12 | 22.9 | 22.9 | -3.76 | -7.45 | -18.98 | 2024-04-09 | 15670 | -34.08 |

## 9. Case-by-Case Notes

### 9.1 039130 / 하나투어 — service demand to package margin bridge

The entry row is 2024-01-29 at 60,900. The 30D path reached 68,800 and the broader window reached 70,600. This is a guarded C31 positive because the signal was not just “travel reopening.” The bridge was package demand, demand-to-revenue visibility and margin/operating leverage. The later drawdown to 44,150 means the correct route is Yellow plus 4B watch, not Green loosening.

### 9.2 080160 / 모두투어 — travel-agent theme without margin bridge

The entry row is 2024-01-29 at 17,070. The forward high was only 17,760 and the broader low fell to 10,200. This is the travel-agent false-positive branch. Reopening language can sound similar across the group, but without package margin, cashflow, and operating leverage, the theme behaves like a postcard rather than an earnings bridge.

### 9.3 034230 / 파라다이스 — casino/inbound MFE without durable economics

The entry row is 2024-01-29 at 12,750. The stock reached 15,670, but later fell to 10,330. Casino/inbound tourism optionality produced MFE, yet a durable VIP drop, hold-rate, margin or cashflow bridge was not strong enough. That makes it useful 4B/high-MAE evidence, not Stage3-Green evidence.

## 10. Current Calibrated Profile Stress Test

| question | result |
|---|---|
| Stage2 actionable bonus too strong? | Yes when C31 treats service/tourism reopening theme as enough evidence. |
| Stage3 Yellow threshold too loose? | Not globally; C31 needs demand-to-revenue, margin, cashflow or operating-leverage bridge before Yellow. |
| Stage3 Green too strict? | Correct. No Green loosening. |
| Price-only blowoff guard appropriate? | Yes, especially for 080160 and 034230. |
| Full 4B non-price requirement appropriate? | Yes. 039130 has better bridge evidence; 080160/034230 do not. |
| 4C timing issue? | High-MAE watch is useful; no immediate hard 4C production delta proposed. |

## 11. Stage2 / Yellow / Green Comparison

```text
039130:
  Stage2-Actionable = correct
  Stage3-Yellow = allowed after package demand / revenue / margin bridge
  Stage3-Green = reject unless demand durability and post-peak drawdown clear

080160:
  Stage2-Actionable = too generous if based only on travel-agent reopening theme
  Stage3-Yellow = reject without package margin, cashflow and operating leverage bridge
  Stage3-Green = reject

034230:
  Stage2-Actionable = acceptable only as casino/inbound tourism watch
  Stage3-Yellow = reject without VIP drop, hold-rate, margin and cashflow bridge
  Stage3-Green = reject despite MFE
```

## 12. 4B Local vs Full-window Timing Audit

| symbol | local_peak_proximity | full_window_peak_proximity | verdict |
|---:|---:|---:|---|
| 039130 | 0.97 | 1.00 | service demand bridge positive but 4B/drawdown watch |
| 080160 | 1.00 | 1.00 | travel-agent theme local 4B watch, not positive stage |
| 034230 | 0.90 | 1.00 | casino tourism theme MFE but no durable economics bridge; keep 4B/high-MAE watch |

## 13. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate: true
rule_scope: canonical_archetype_specific
rule_id: c31_service_tourism_requires_demand_margin_cashflow_bridge

rule:
  For C31 service/tourism policy-event rows, do not promote tourism,
  travel-agent, casino, inbound recovery, reopening, visa, route, or service-demand
  Stage2 signals into Stage3-Yellow/Green unless at least one non-price bridge is visible:
  demand-to-revenue conversion, package margin, VIP drop/hold-rate durability,
  cashflow conversion, cost normalization, operating leverage, or earnings revision.
```

## 14. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive rate | verdict |
|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 14.29 | -9.05 | 66.7% | too generous to tourism/service theme rows |
| P0b e2r_2_0_baseline_reference | 3 | 14.29 | -9.05 | 33.3% | safer but may miss 039130 |
| P1 sector_specific_candidate_profile | 3 | 14.29 | -9.05 | 66.7% | no broad L10 loosen |
| P2 canonical_archetype_candidate_profile | 1 selected positive | 15.93 | -8.87 | 0% after bridge gate | preferred shadow |
| P3 counterexample_guard_profile | 2 rejected/watch | 13.47 | -9.14 | 0% after no-Green routing | useful guard |

## 15. Score-Return Alignment Matrix

| case | current profile verdict | alignment |
|---|---|---|
| 039130 | current_profile_correct_but_no_green | demand/package margin bridge aligned with MFE, but drawdown needs 4B |
| 080160 | current_profile_false_positive | travel-agent theme produced low MFE and high MAE |
| 034230 | current_profile_false_positive_if_green | casino/inbound MFE lacked durable drop/margin bridge |

## 16. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C/watch | new_independent | reused | usable_triggers | representative | profile_errors | sector_rule | canonical_rule | coverage_gap_after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | C31_SERVICE_TOURISM_DEMAND_MARGIN_CASHFLOW_BRIDGE_GUARD | 1 | 2 | 3 | 3 | 3 | 0 | 3 | 3 | 2 | false | true | R12 service/tourism C31 residual reduced |

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
- tourism theme without margin/cashflow bridge
- service demand recovery winner needs 4B watch
- casino inbound theme MFE without drop/margin bridge
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
- R12 allowed service/tourism branch
- large_sector/canonical consistency
- duplicate avoidance at symbol level
- representative rows use clean 180D windows
```

Not validated:

```text
- exact disclosure/news URLs
- exact tourism policy or earnings report URLs
- production scoring behavior
- live candidate status
```

## 19. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_service_tourism_requires_demand_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 service/tourism policy-event rows should not promote toward Stage3-Yellow/Green unless reopening or tourism signal converts into package demand, VIP drop/hold-rate, revenue, margin, cashflow, or operating-leverage bridge","039130 survives as guarded positive after demand/margin bridge; 080160 and 034230 are demoted because travel-agent/casino themes lacked durable margin and cashflow bridge","TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE|TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE|TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered service/tourism branch"
shadow_weight,c31_tourism_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Tourism/service reopening winners and theme failures can peak before margin/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 039130 guarded positive while preventing 080160/034230 tourism-theme false positives","TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE|TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE|TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

## 20. Machine-Readable Rows

### 20.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 20.2 case rows

```jsonl
{"row_type":"case","case_id":"R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE","symbol":"039130","company_name":"하나투어","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SERVICE_TOURISM_POLICY_DEMAND_MARGIN_BRIDGE","deep_sub_archetype_id":"OUTBOUND_TRAVEL_RECOVERY_PACKAGE_DEMAND_TO_MARGIN_OPERATING_LEVERAGE","case_type":"service_demand_recovery_success_then_4B_drawdown_watch","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green","price_source":"Songdaiki/stock-web","notes":"R12 under-covered service/tourism branch: C31 service policy/event rows require demand-to-revenue, package margin, VIP drop/hold-rate, cashflow, or operating-leverage bridge; reopening/tourism theme alone is insufficient."}
{"row_type":"case","case_id":"R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE","symbol":"080160","company_name":"모두투어","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_TRAVEL_AGENT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"OUTBOUND_TRAVEL_REOPENING_THEME_WITHOUT_PACKAGE_MARGIN_OR_CASHFLOW_CONVERSION","case_type":"travel_agent_low_MFE_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"R12 under-covered service/tourism branch: C31 service policy/event rows require demand-to-revenue, package margin, VIP drop/hold-rate, cashflow, or operating-leverage bridge; reopening/tourism theme alone is insufficient."}
{"row_type":"case","case_id":"R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_CASINO_INBOUND_TOURISM_THEME_WITHOUT_DROP_MARGIN_BRIDGE","deep_sub_archetype_id":"CASINO_INBOUND_RECOVERY_OPTIONALITY_WITHOUT_VIP_DROP_HOLD_RATE_MARGIN_CONVERSION","case_type":"casino_theme_MFE_then_high_MAE_counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green","price_source":"Songdaiki/stock-web","notes":"R12 under-covered service/tourism branch: C31 service policy/event rows require demand-to-revenue, package margin, VIP drop/hold-rate, cashflow, or operating-leverage bridge; reopening/tourism theme alone is insufficient."}
```

### 20.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE","case_id":"R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE","symbol":"039130","company_name":"하나투어","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_SERVICE_TOURISM_POLICY_DEMAND_MARGIN_BRIDGE","deep_sub_archetype_id":"OUTBOUND_TRAVEL_RECOVERY_PACKAGE_DEMAND_TO_MARGIN_OPERATING_LEVERAGE","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":60900,"evidence_available_at_that_date":"source_proxy_outbound_travel_recovery_package_demand_margin_operating_leverage_bridge; evidence_url_pending","evidence_source":"source_proxy_outbound_travel_recovery_package_demand_margin_operating_leverage_bridge; evidence_url_pending","bridge_summary":"outbound travel demand recovery and package mix converted into revenue/margin operating-leverage visibility, but later demand fatigue and drawdown require 4B watch","stage2_evidence_fields":["outbound_travel_recovery","package_demand_proxy","relative_strength","service_margin_bridge_proxy"],"stage3_evidence_fields":["demand_to_revenue_visibility","package_mix_margin_bridge","operating_leverage_proxy"],"stage4b_evidence_fields":["post_demand_recovery_peak_watch","travel_service_crowding_after_reopening_rerating"],"stage4c_evidence_fields":["drawdown_watch_after_recovery_peak"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv","profile_path":"atlas/symbol_profiles/039/039130.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.97,"MFE_90D_pct":15.93,"MFE_180D_pct":15.93,"MFE_1Y_pct":15.93,"MFE_2Y_pct":15.93,"MAE_30D_pct":-3.28,"MAE_90D_pct":-8.87,"MAE_180D_pct":-27.5,"MAE_1Y_pct":-27.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-25","peak_price":70600,"drawdown_after_peak_pct":-37.46,"green_lateness_ratio":"0.48","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"service_demand_bridge_positive_but_4B_drawdown_watch","four_b_evidence_type":"non_price_service_demand_margin_bridge","four_c_protection_label":"drawdown_watch_after_peak","trigger_outcome_label":"service_demand_recovery_success_then_4B_watch","current_profile_verdict":"current_profile_correct_but_no_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE","case_id":"R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE","symbol":"080160","company_name":"모두투어","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_TRAVEL_AGENT_THEME_WITHOUT_MARGIN_CASHFLOW_BRIDGE","deep_sub_archetype_id":"OUTBOUND_TRAVEL_REOPENING_THEME_WITHOUT_PACKAGE_MARGIN_OR_CASHFLOW_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":17070,"evidence_available_at_that_date":"source_proxy_outbound_travel_agent_theme_without_package_margin_cashflow_bridge; evidence_url_pending","evidence_source":"source_proxy_outbound_travel_agent_theme_without_package_margin_cashflow_bridge; evidence_url_pending","bridge_summary":"travel-agent reopening theme failed to convert into durable package demand, margin, cashflow, or operating-leverage bridge","stage2_evidence_fields":["travel_reopening_theme","outbound_tourism_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["weak_local_peak","package_margin_bridge_absent","cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_margin_cashflow_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv","profile_path":"atlas/symbol_profiles/080/080160.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.04,"MFE_90D_pct":4.04,"MFE_180D_pct":4.04,"MFE_1Y_pct":4.04,"MFE_2Y_pct":4.04,"MAE_30D_pct":-10.84,"MAE_90D_pct":-10.84,"MAE_180D_pct":-40.25,"MAE_1Y_pct":-40.25,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-14","peak_price":17760,"drawdown_after_peak_pct":-42.57,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"travel_agent_theme_local_4B_watch_not_positive_stage","four_b_evidence_type":"tourism_theme_without_service_economics_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"failed_travel_agent_reopening_counterexample","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE","case_id":"R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE","symbol":"034230","company_name":"파라다이스","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"C31_CASINO_INBOUND_TOURISM_THEME_WITHOUT_DROP_MARGIN_BRIDGE","deep_sub_archetype_id":"CASINO_INBOUND_RECOVERY_OPTIONALITY_WITHOUT_VIP_DROP_HOLD_RATE_MARGIN_CONVERSION","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":12750,"evidence_available_at_that_date":"source_proxy_casino_inbound_tourism_theme_without_VIP_drop_hold_rate_margin_bridge; evidence_url_pending","evidence_source":"source_proxy_casino_inbound_tourism_theme_without_VIP_drop_hold_rate_margin_bridge; evidence_url_pending","bridge_summary":"casino/inbound tourism theme produced MFE, but VIP drop, hold-rate, margin and cashflow bridge were not durable enough; later high-MAE path blocks Green routing","stage2_evidence_fields":["casino_inbound_tourism_theme","China_or_VIP_recovery_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_MFE_peak","drop_hold_rate_bridge_absent","margin_cashflow_bridge_absent"],"stage4c_evidence_fields":["high_MAE_without_drop_or_margin_bridge"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv","profile_path":"atlas/symbol_profiles/034/034230.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.12,"MFE_90D_pct":22.9,"MFE_180D_pct":22.9,"MFE_1Y_pct":22.9,"MFE_2Y_pct":22.9,"MAE_30D_pct":-3.76,"MAE_90D_pct":-7.45,"MAE_180D_pct":-18.98,"MAE_1Y_pct":-18.98,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-09","peak_price":15670,"drawdown_after_peak_pct":-34.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"casino_tourism_theme_MFE_but_no_drop_margin_bridge_keep_4B_high_MAE_watch","four_b_evidence_type":"tourism_theme_without_service_economics_bridge","four_c_protection_label":"high_MAE_watch","trigger_outcome_label":"casino_theme_MFE_then_high_MAE_counterexample","current_profile_verdict":"current_profile_false_positive_if_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE_entry","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 20.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE","trigger_id":"TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE","symbol":"039130","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":8,"service_demand_score":12,"margin_cashflow_score":11,"operating_leverage_score":10,"relative_strength_score":10,"theme_risk_penalty":6},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":7,"service_demand_score":15,"margin_cashflow_score":14,"operating_leverage_score":13,"relative_strength_score":8,"theme_risk_penalty":8},"weighted_score_after":80,"stage_label_after":"Stage3-Yellow","changed_components":["policy_event_score","service_demand_score","margin_cashflow_score","operating_leverage_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 service/tourism row is promoted only because demand recovery converts into revenue, margin and operating-leverage bridge; drawdown keeps 4B watch active.","MFE_90D_pct":15.93,"MAE_90D_pct":-8.87,"score_return_alignment_label":"score_return_aligned","current_profile_verdict":"current_profile_correct_but_no_green"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE","trigger_id":"TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE","symbol":"080160","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":10,"service_demand_score":4,"margin_cashflow_score":1,"operating_leverage_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"service_demand_score":2,"margin_cashflow_score":0,"operating_leverage_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","service_demand_score","margin_cashflow_score","operating_leverage_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes tourism/casino reopening theme rows when service demand, package/VIP economics, margin, cashflow or operating-leverage bridge is absent.","MFE_90D_pct":4.04,"MAE_90D_pct":-10.84,"score_return_alignment_label":"score_return_misaligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE","trigger_id":"TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE","symbol":"034230","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"policy_event_score":10,"service_demand_score":4,"margin_cashflow_score":1,"operating_leverage_score":1,"relative_strength_score":10,"theme_risk_penalty":8},"weighted_score_before":61,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"policy_event_score":4,"service_demand_score":2,"margin_cashflow_score":0,"operating_leverage_score":0,"relative_strength_score":4,"theme_risk_penalty":16},"weighted_score_after":39,"stage_label_after":"Stage1-Watch_or_4B-HighMAE","changed_components":["policy_event_score","service_demand_score","margin_cashflow_score","operating_leverage_score","relative_strength_score","theme_risk_penalty"],"component_delta_explanation":"C31 guard demotes tourism/casino reopening theme rows when service demand, package/VIP economics, margin, cashflow or operating-leverage bridge is absent.","MFE_90D_pct":22.9,"MAE_90D_pct":-7.45,"score_return_alignment_label":"score_return_mixed","current_profile_verdict":"current_profile_false_positive_if_green"}
```

### 20.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_service_tourism_requires_demand_margin_cashflow_bridge,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"C31 service/tourism policy-event rows should not promote toward Stage3-Yellow/Green unless reopening or tourism signal converts into package demand, VIP drop/hold-rate, revenue, margin, cashflow, or operating-leverage bridge","039130 survives as guarded positive after demand/margin bridge; 080160 and 034230 are demoted because travel-agent/casino themes lacked durable margin and cashflow bridge","TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE|TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE|TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE",3,3,2,medium,canonical_shadow_only,"not production; R12 under-covered service/tourism branch"
shadow_weight,c31_tourism_theme_4b_high_mae_watch_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,1,1,0,"Tourism/service reopening winners and theme failures can peak before margin/cashflow durability is confirmed; local/full-window 4B and high-MAE watch should remain active","preserves 039130 guarded positive while preventing 080160/034230 tourism-theme false positives","TRG_R12L74_C31_039130_20240129_OUTBOUND_TRAVEL_DEMAND_PACKAGE_MARGIN_BRIDGE|TRG_R12L74_C31_080160_20240129_TRAVEL_AGENT_THEME_NO_MARGIN_RECOVERY_BRIDGE|TRG_R12L74_C31_034230_20240129_CASINO_INBOUND_TOURISM_THEME_NO_DROP_MARGIN_BRIDGE",3,3,2,medium,existing_axis_kept,"strengthens local/full-window 4B and high-MAE watch without global delta"
```

### 20.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R12","loop":"74","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"residual_error_types_found":["tourism_theme_without_margin_cashflow_bridge","service_demand_recovery_winner_needs_4B_watch","casino_inbound_theme_MFE_without_drop_margin_bridge"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 21. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### R12-specific handling

- R12 may use `L10_POLICY_EVENT_CROSS_REDTEAM_MISC` or under-covered service/agri branches.
- This MD uses a C31 under-covered service/tourism branch.
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
- price-only/tourism-theme-only rows cannot promote Stage2/Stage3.
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
12. Add validation that C31 service/tourism rows cannot promote without demand-to-revenue conversion, package margin, VIP drop/hold-rate durability, cashflow conversion, cost normalization, operating leverage, or earnings revision.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 22. Next Round State

```text
completed_round = R12
completed_loop = 74
next_round = R13
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
atlas/symbol_profiles/039/039130.json
atlas/symbol_profiles/080/080160.json
atlas/symbol_profiles/034/034230.json
atlas/ohlcv_tradable_by_symbol_year/039/039130/2024.csv
atlas/ohlcv_tradable_by_symbol_year/080/080160/2024.csv
atlas/ohlcv_tradable_by_symbol_year/034/034230/2024.csv
```

This loop continues loop 74 with R12 and adds 3 new independent C31 service/tourism representative cases, 1 positive, 2 counterexamples/watch cases, and 1 canonical-archetype residual guard candidate for R12/L10.
