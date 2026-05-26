# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "round": "R3",
  "loop": "67",
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA",
  "fine_archetype_id": "AMPC_DIRECT_MARGIN_BRIDGE_WITH_US_UTILIZATION / AMPC_PROFIT_WITH_EV_DEMAND_CAPEX_GUARD / US_JV_ANNOUNCEMENT_WITH_DELAYED_RAMP_AND_CUSTOMER_EV_CUT",
  "selection_mode": "auto_coverage_gap_fill",
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_embedded": true,
  "handoff_prompt_executed_now": false
}
```

## 1. Current Calibrated Profile Assumption

`current_default_profile_proxy = e2r_2_1_stock_web_calibrated`.

Already-applied global axes are treated as active: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75.0`, `stage3_green_total_min=87.0`, `stage3_green_revision_min=55.0`, `stage3_cross_evidence_green_buffer=+1.5`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, and `hard_4c_thesis_break_routes_to_4c=true`.

This loop does not re-prove the global Stage2/Green/4B rules. It isolates C13-specific residual error: **AMPC and JV headlines behave very differently depending on whether they are direct operating-profit bridges or delayed utilization stories.**

## 2. Round / Large Sector / Canonical Archetype Scope

- round: R3
- loop: 67
- large_sector_id: `L3_BATTERY_EV_GREEN_MOBILITY`
- canonical_archetype_id: `C13_BATTERY_JV_UTILIZATION_AMPC_IRA`
- loop_objective: `coverage_gap_fill`, `counterexample_mining`, `sector_specific_rule_discovery`, `canonical_archetype_compression`, `4B_non_price_requirement_stress_test`

## 3. Previous Coverage / Duplicate Avoidance Check

Repository artifact search for `C13_BATTERY_JV_UTILIZATION_AMPC_IRA R3 calibration` returned no direct hit in `Songdaiki/stock_agent`. The immediate prior generated MD was C11, so this loop intentionally moves to a different canonical archetype. No `src/e2r` code was opened and no production patch was prepared.

Diversity outcome:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 2
same_archetype_new_symbol_count = 2
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
positive_case_count = 1
counterexample_count = 2
current_profile_error_count = 3
diversity_score_summary = avg=29.7; no duplicate same symbol+trigger+entry group
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest confirms `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, `symbol_count=5414`, and shard root `atlas/ohlcv_tradable_by_symbol_year`. The schema confirms `d,o,h,l,c,v,a,mc,s,m` for tradable rows and the MFE/MAE formula used in this file. fileciteturn1090file0 fileciteturn1091file0

Symbol profile validation:

- LG에너지솔루션 `373220`: active-like, available years 2022~2026, no corporate-action candidate dates in the profile. fileciteturn1093file0
- 삼성SDI `006400`: active-like, corporate-action candidates are old historical dates; 2024~2025 windows used here are clean. fileciteturn1094file0 fileciteturn1095file0
- SK이노베이션 `096770`: profile has `corporate_action_candidate_dates=["2024-11-20"]`, so the SK E&S / SK On financing-merger route is recorded as narrative-only. fileciteturn1096file0

## 5. Historical Eligibility Gate

All representative triggers satisfy the following:

- trigger_date is historical.
- entry_date exists in Stock-Web tradable shard.
- entry_date + 180 trading days is available within manifest `max_date=2026-02-20`.
- 30D / 90D / 180D MFE and MAE are computed.
- 180D corporate-action window is clean for LGES and Samsung SDI representative rows.

SK이노베이션 2024 merger/financing narrative is intentionally **not** used for quantitative calibration because its 180D window overlaps the profile corporate-action candidate date 2024-11-20.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| AMPC_DIRECT_MARGIN_BRIDGE_WITH_US_UTILIZATION | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | AMPC becomes score-positive only when it is an observable margin bridge and not just a policy headline. |
| AMPC_PROFIT_WITH_EV_DEMAND_CAPEX_GUARD | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | AMPC that merely offsets weak ex-credit economics should cap promotion. |
| US_JV_ANNOUNCEMENT_WITH_DELAYED_RAMP_AND_CUSTOMER_EV_CUT | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | JV is not equal to utilization; delayed ramp/customer demand cut is a C13 guard. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE | 373220 | LG에너지솔루션 | positive | AMPC/profit bridge later aligned with 180D MFE, but high early MAE shows it is not low-risk Green. |
| R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD | 373220 | LG에너지솔루션 | counterexample | Same policy axis, but weak demand/capex caution made early promotion poor. |
| R3L67_SDI_2024_GM_JV_DELAYED_RERATING | 006400 | 삼성SDI | counterexample + 4B | JV headline without near-term ramp became a false-positive route. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
```

This loop is intentionally counterexample-heavy because C13 policy/JV language is prone to over-scoring. The positive case is retained to avoid over-tightening the guard: direct AMPC margin bridge can matter, but only when connected to utilization and customer route.

## 9. Evidence Source Map

| case_id | trigger_date | evidence source | evidence family |
|---|---|---|---|
| R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE | 2025-04-07 | Reuters, LGES preliminary Q1 2025 earnings / IRA credit bridge | AMPC direct margin bridge |
| R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD | 2024-04-25 | Reuters, LGES Q1 2024 profit, IRA credit, slow EV demand | AMPC with demand/capex guard |
| R3L67_SDI_2024_GM_JV_DELAYED_RERATING | 2024-08-27 | Reuters, Samsung SDI-GM Indiana JV and GM EV forecast-cut context | JV delayed ramp / customer demand risk |

## 10. Price Data Source Map

| symbol | profile_path | shard paths used |
|---:|---|---|
| 373220 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv; atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv |
| 006400 | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv; atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv |
| 096770 | atlas/symbol_profiles/096/096770.json | narrative-only due corporate-action contaminated 180D route |

## 11. Case-by-Case Trigger Grid

|trigger_id|symbol|company|type|trigger_date|entry_date|entry_price|MFE30|MFE90|MFE180|MAE30|MAE90|MAE180|peak_date|peak_price|current_profile_verdict|aggregate_role|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A|373220|LG에너지솔루션|Stage2-Actionable|2025-04-07|2025-04-08|318000|11.01|26.73|65.72|-15.72|-16.35|-16.35|2025-10-29|527000|current_profile_too_late|representative|
|R3L67_T02_LGES_2024_Q1_AMPC_GUARD|373220|LG에너지솔루션|Stage2-Actionable|2024-04-25|2024-04-25|372500|6.58|6.58|19.19|-12.48|-15.97|-15.97|2024-10-08|444000|current_profile_too_early|representative|
|R3L67_T03_SDI_2024_GM_JV_STAGE2A|006400|삼성SDI|Stage2-Actionable|2024-08-27|2024-08-28|339500|15.91|15.91|15.91|-2.21|-30.04|-53.55|2024-09-30|393500|current_profile_false_positive|representative|
|R3L67_T04_SDI_2024_GM_JV_4B_OVERLAY|006400|삼성SDI|4B|2024-09-30|2024-09-30|378500|2.38|2.38|2.38|-15.19|-40.55|-58.34|2024-09-30|393500|current_profile_4B_too_late|4B_overlay_only|


## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| case_id | entry | 30D profile | 90D profile | 180D profile | interpretation |
|---|---:|---|---|---|---|
| LGES 2025 AMPC direct bridge | 318,000 | +11.01 / -15.72 | +26.73 / -16.35 | +65.72 / -16.35 | Positive, but only after a painful shakeout; not immediate Green. |
| LGES 2024 AMPC with demand guard | 372,500 | +6.58 / -12.48 | +6.58 / -15.97 | +19.19 / -15.97 | Policy credit alone overstates early reward. |
| Samsung SDI GM JV | 339,500 | +15.91 / -2.21 | +15.91 / -30.04 | +15.91 / -53.55 | Local bounce, then severe failed rerating. |

## 13. Current Calibrated Profile Stress Test

| case_id | current proxy likely label | verdict | residual error |
|---|---|---|---|
| LGES 2025 AMPC direct bridge | Stage3-Yellow, slow to promote | current_profile_too_late | Direct AMPC bridge can be under-rewarded if treated as generic policy. |
| LGES 2024 AMPC guard | Stage3-Yellow risk | current_profile_too_early | AMPC without ex-credit profit and utilization confirmation creates high-MAE false comfort. |
| Samsung SDI GM JV | Stage3-Yellow risk | current_profile_false_positive | JV headline plus good customer name over-scores when ramp is delayed. |

Existing axes:
- `stage2_actionable_evidence_bonus`: existing_axis_tested; kept.
- `stage3_yellow_total_min`: existing_axis_tested; kept.
- `full_4b_requires_non_price_evidence`: existing_axis_strengthened by Samsung SDI 4B overlay.
- `price_only_blowoff_blocks_positive_stage`: existing_axis_kept.

## 14. Stage2 / Yellow / Green Comparison

No clean confirmed Stage3-Green trigger was assigned in this loop. That is the point: C13 tends to create attractive Stage2/Yellow stories before the utilization math becomes visible. The proper comparison is not "Stage2 vs Green lateness"; it is **Stage2 headline vs utilization-confirmed Stage2/Yellow**.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
late_green_count = 1
```

## 15. 4B Local vs Full-window Timing Audit

Samsung SDI provides the 4B overlay:

```text
Stage2_Actionable entry = 339,500 on 2024-08-28
Stage4B overlay entry = 378,500 on 2024-09-30
full_window_peak_price = 393,500
four_b_local_peak_proximity = 0.722
four_b_full_window_peak_proximity = 0.722
four_b_timing_verdict = good_full_window_4B_timing
four_b_evidence_type = contract_delay | margin_or_backlog_slowdown | explicit_event_cap
```

This is not a price-only 4B. The non-price evidence was that the JV's mass production timing did not close the current-cycle utilization gap, while customer EV demand risk was already visible.

## 16. 4C Protection Audit

No hard 4C row is proposed. Samsung SDI was a 4B overlay / failed rerating row, not a thesis-break 4C row. The JV was not cancelled; the error was timing and utilization quality.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c13_ampc_without_ex_credit_profit_guard
proposal = If AMPC prevents headline loss but ex-credit profit remains weak and capex/utilization commentary is defensive, cap positive stage at Stage2-Actionable or low Yellow.
reason = LGES 2024 showed policy credit can protect reported profit without clean 90D reward.
confidence = low_to_medium
production_scoring_changed = false
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c13_direct_ampc_margin_bridge_bonus
delta = +1 shadow-only
reason = Direct AMPC bridge tied to utilization should not be treated as generic policy optionality.

axis_2 = c13_generic_jv_delayed_ramp_guard
delta = -2 shadow-only
reason = JV headline with delayed mass production / customer EV cut should be capped and can support 4B overlay.
```

## 19. Before / After Backtest Comparison

|profile_id|scope|hypothesis|eligible|selected|avg_MFE90|avg_MAE90|avg_MFE180|avg_MAE180|false_positive_rate|missed_structural|late_green|verdict|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|P0_e2r_2_1_stock_web_calibrated_proxy|current_proxy|no C13-specific split|3|T01|T02|T03|16.41|-20.79|33.61|-28.62|0.67|1|1|mixed|
|P0b_e2r_2_0_baseline_reference|rollback_reference|generic subsidy/JV over-score risk|3|T01|T02|T03|16.41|-20.79|33.61|-28.62|0.67|1|0|weaker|
|P1_sector_specific_candidate_profile|sector_specific|L3 subsidy/JV needs ex-credit economics and utilization|3|T01|T02|T03|16.41|-20.79|33.61|-28.62|0.33|0|1|better|
|P2_canonical_archetype_candidate_profile|canonical_archetype_specific|split direct AMPC bridge from generic delayed JV|3|T01|T02|T03|16.41|-20.79|33.61|-28.62|0.33|0|1|best_candidate|
|P3_counterexample_guard_profile|guard_profile|max protect against generic subsidy/JV false positives|3|T01|T02|T03|16.41|-20.79|33.61|-28.62|0.0|1|1|too_conservative|


## 20. Score-Return Alignment Matrix

| case_id | before_score | after_score | before_label | after_label | MFE90 | MAE90 | alignment |
|---|---:|---:|---|---|---:|---:|---|
| LGES 2025 AMPC | 79 | 84 | Stage3-Yellow | Stage3-Yellow | 26.73 | -16.35 | aligned but high-MAE |
| LGES 2024 AMPC guard | 76 | 68 | Stage3-Yellow | Stage2-Actionable | 6.58 | -15.97 | overpromotion reduced |
| Samsung SDI GM JV | 78 | 64 | Stage3-Yellow | Stage2-Watch | 15.91 | -30.04 | false-positive guarded |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C13_BATTERY_JV_UTILIZATION_AMPC_IRA | mixed C13 fine routes | 1 | 2 | 1 | 0 | 3 | 0 | 4 | 3 | 3 | true | true | Needs more non-LGES positives and one hard 4C cancellation/call-off row. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, full_4b_requires_non_price_evidence
residual_error_types_found: direct_AMPC_bridge_too_late, generic_policy_or_JV_false_positive, AMPC_without_ex_credit_profit_high_MAE
new_axis_proposed: c13_direct_ampc_margin_bridge_bonus; c13_generic_jv_delayed_ramp_guard; c13_ampc_without_ex_credit_profit_guard
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-Web manifest and schema.
- LGES and Samsung SDI profile windows.
- Actual Stock-Web `tradable_raw` entry prices and 30D/90D/180D MFE/MAE.
- 4B local vs full-window split for Samsung SDI.

Not validated:
- No live/current stock scan.
- No `stock_agent/src/e2r` code inspection.
- No production patch.
- No broker/API/auto-trading action.
- No hard 4C cancellation/call-off row.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c13_direct_ampc_margin_bridge_bonus,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,+1,+1,"Reward AMPC only when it directly changes operating-profit bridge and links to US utilization/customer route.","Improves LGES 2025 capture without global threshold changes.","R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c13_generic_jv_delayed_ramp_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,-2,-2,"Punish JV headlines when mass production is delayed beyond current cycle or customer EV forecast is cut.","Blocks Samsung SDI false Yellow/Green route.","R3L67_T03_SDI_2024_GM_JV_STAGE2A|R3L67_T04_SDI_2024_GM_JV_4B_OVERLAY",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c13_ampc_without_ex_credit_profit_guard,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,0,-1,-1,"If AMPC prevents headline loss but ex-credit profit remains weak and capex is reduced, cap Stage3 promotion.","Reduces LGES 2024 high-MAE promotion.","R3L67_T02_LGES_2024_Q1_AMPC_GUARD",3,3,2,low,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_DIRECT_MARGIN_BRIDGE_WITH_US_UTILIZATION","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"AMPC was a real operating-profit bridge only when connected to US utilization/customer route; 180D MFE confirmed but early MAE stayed large.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Direct AMPC bridge should receive narrow C13 support, not broad subsidy promotion."}
{"row_type":"case","case_id":"R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_PROFIT_WITH_EV_DEMAND_CAPEX_GUARD","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R3L67_T02_LGES_2024_Q1_AMPC_GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"AMPC preserved reported profit, but EV-demand/capex caution made the 90D profile weak and high-MAE.","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Subsidy without ex-credit profit and utilization confirmation should not promote to Green."}
{"row_type":"case","case_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_JV_ANNOUNCEMENT_WITH_DELAYED_RAMP_AND_CUSTOMER_EV_CUT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L67_T03_SDI_2024_GM_JV_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"JV headline created a local bounce, but 2027 ramp timing plus customer EV-forecast risk made it a false-positive rerating path.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Clean C13 guard case: JV/contract without near-term utilization should be capped."}
{"row_type":"trigger","trigger_id":"R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A","case_id":"R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_DIRECT_MARGIN_BRIDGE_WITH_US_UTILIZATION","sector":"battery_ev","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2025-04-07","evidence_available_at_that_date":"Q1 2025 preliminary profit was materially supported by IRA/AMPC credit bridge, while ex-credit profitability still required utilization confirmation.","evidence_source":"Reuters, 2025-04-07, LG Energy Solution preliminary Q1 2025 earnings / IRA tax credit bridge.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-04-08","entry_price":318000,"MFE_30D_pct":11.01,"MFE_90D_pct":26.73,"MFE_180D_pct":65.72,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-15.72,"MAE_90D_pct":-16.35,"MAE_180D_pct":-16.35,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-10-29","peak_price":527000,"drawdown_after_peak_pct":-30.65,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_high_MAE_then_180D_rerating","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE:2025-04-08:318000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L67_T02_LGES_2024_Q1_AMPC_GUARD","case_id":"R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"AMPC_PROFIT_WITH_EV_DEMAND_CAPEX_GUARD","sector":"battery_ev","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-25","evidence_available_at_that_date":"Q1 2024 profit was supported by IRA tax credit, but the same disclosure context carried slow EV-demand and capex-minimization risk.","evidence_source":"Reuters, 2024-04-25, LG Energy Solution Q1 2024 profit / IRA tax credit / slow EV demand.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":372500,"MFE_30D_pct":6.58,"MFE_90D_pct":6.58,"MFE_180D_pct":19.19,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-12.48,"MAE_90D_pct":-15.97,"MAE_180D_pct":-15.97,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-08","peak_price":444000,"drawdown_after_peak_pct":-22.86,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_AMPC_without_utilization_confirmation","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD:2024-04-25:372500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L67_T03_SDI_2024_GM_JV_STAGE2A","case_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_JV_ANNOUNCEMENT_WITH_DELAYED_RAMP_AND_CUSTOMER_EV_CUT","sector":"battery_ev","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-08-27","evidence_available_at_that_date":"Samsung SDI and GM finalized a US JV; production timing was 2027 and customer EV-forecast risk was visible.","evidence_source":"Reuters, 2024-08-27/28, Samsung SDI-GM Indiana JV final agreement and GM EV forecast-cut context.","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","policy_or_regulatory_optionality","capacity_or_volume_route"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_delay","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-28","entry_price":339500,"MFE_30D_pct":15.91,"MFE_90D_pct":15.91,"MFE_180D_pct":15.91,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-2.21,"MAE_90D_pct":-30.04,"MAE_180D_pct":-53.55,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-59.92,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating_after_generic_JV_headline","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING:2024-08-28:339500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L67_T04_SDI_2024_GM_JV_4B_OVERLAY","case_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"US_JV_ANNOUNCEMENT_WITH_DELAYED_RAMP_AND_CUSTOMER_EV_CUT","sector":"battery_ev","primary_archetype":"battery_jv_utilization_ampc_ira","loop_objective":"coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-09-30","evidence_available_at_that_date":"Post-JV local peak was near the full observed window peak while delayed ramp/customer-demand risk remained non-price evidence.","evidence_source":"Stock-Web OHLC row plus Reuters JV timing and GM demand-risk context.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","contract_delay","margin_or_backlog_slowdown","explicit_event_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-09-30","entry_price":378500,"MFE_30D_pct":2.38,"MFE_90D_pct":2.38,"MFE_180D_pct":2.38,"MFE_1Y_pct":"not_used","MFE_2Y_pct":"not_used","MAE_30D_pct":-15.19,"MAE_90D_pct":-40.55,"MAE_180D_pct":-58.34,"MAE_1Y_pct":"not_used","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-30","peak_price":393500,"drawdown_after_peak_pct":-59.92,"green_lateness_ratio":0.722,"four_b_local_peak_proximity":0.722,"four_b_full_window_peak_proximity":0.722,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["contract_delay","margin_or_backlog_slowdown","explicit_event_cap"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING:2024-09-30:378500","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L67_LGES_2025_Q1_AMPC_MARGIN_BRIDGE","trigger_id":"R3L67_T01_LGES_2025_Q1_AMPC_STAGE2A","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":3,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":9,"revision_score":5,"relative_strength_score":3,"customer_quality_score":7,"policy_or_regulatory_score":9,"valuation_repricing_score":0,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","+C13_AMPC_direct_bridge_bonus","execution_risk_score"],"component_delta_explanation":"Direct AMPC bridge receives a narrow C13 bonus only when linked to utilization/customer route; still below Green without revision confirmation.","MFE_90D_pct":26.73,"MAE_90D_pct":-16.35,"score_return_alignment_label":"aligned_but_high_MAE","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L67_LGES_2024_Q1_AMPC_CAPEX_GUARD","trigger_id":"R3L67_T02_LGES_2024_Q1_AMPC_GUARD","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":7,"revision_score":2,"relative_strength_score":0,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":2,"relative_strength_score":0,"customer_quality_score":5,"policy_or_regulatory_score":8,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-Actionable","changed_components":["execution_risk_score","C13_demand_capex_guard","margin_bridge_score"],"component_delta_explanation":"AMPC headline is capped because the same disclosure carried EV-demand/capex caution and weak ex-credit economics.","MFE_90D_pct":6.58,"MAE_90D_pct":-15.97,"score_return_alignment_label":"overpromotion_reduced","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L67_SDI_2024_GM_JV_DELAYED_RERATING","trigger_id":"R3L67_T03_SDI_2024_GM_JV_STAGE2A","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","raw_component_scores_before":{"contract_score":7,"backlog_visibility_score":5,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":0,"customer_quality_score":8,"policy_or_regulatory_score":7,"valuation_repricing_score":0,"execution_risk_score":6,"legal_or_contract_risk_score":4,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":6,"backlog_visibility_score":3,"margin_bridge_score":1,"revision_score":2,"relative_strength_score":0,"customer_quality_score":7,"policy_or_regulatory_score":6,"valuation_repricing_score":0,"execution_risk_score":8,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-Watch","changed_components":["backlog_visibility_score","execution_risk_score","legal_or_contract_risk_score","C13_delayed_ramp_guard"],"component_delta_explanation":"JV headline is not immediate utilization; 2027 ramp and customer EV-forecast cut convert it into watch/4B overlay rather than positive Stage3.","MFE_90D_pct":15.91,"MAE_90D_pct":-30.04,"score_return_alignment_label":"false_positive_guarded","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R3","loop":"67","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","full_4b_requires_non_price_evidence"],"residual_error_types_found":["generic_policy_or_JV_false_positive","direct_AMPC_bridge_too_late","AMPC_without_ex_credit_profit_high_MAE"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R3L67_SKI_2024_SKENS_MERGER_CORP_ACTION_BLOCKED","symbol":"096770","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reason":"SK Innovation battery-financing / SK E&S merger narrative overlaps a Stock-Web corporate-action candidate date 2024-11-20; not used for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration","profile_path":"atlas/symbol_profiles/096/096770.json","calibration_block_reasons":["corporate_action_contaminated_180D_window"]}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

## 27. Next Round State

```text
next_round = R3_loop_68_C14_EV_DEMAND_SLOWDOWN_4B_4C
reason = This C13 loop found JV/utilization false positives; C14 should test whether EV demand slowdown routes to 4B/4C earlier than the current proxy.
```

## 28. Source Notes

- Stock-Web manifest/schema/profile/CSV rows were read from `Songdaiki/stock-web` only.
- `stock_agent` source code was not opened.
- `SK이노베이션` is preserved only as narrative-only because `096770` has a 2024-11-20 corporate-action candidate in the Stock-Web profile.
- Evidence sources are used as historical event labels. Quantitative calibration relies only on Stock-Web OHLC rows.
