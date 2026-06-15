# E2R Stock-Web v12 Residual Research — R3 / C13 Battery JV Utilization AMPC IRA

```yaml
schema_family: v12_sector_archetype_residual
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R3
selected_loop: 100
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: BATTERY_JV_IRA_AMPC_UTILIZATION_TO_CASH_BRIDGE_VS_SUPPLY_CHAIN_LABEL_HIGH_MAE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - stage2_actionable_bonus_stress_test
  - local_4b_guard
  - canonical_archetype_compression
price_source: Songdaiki/stock-web
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection / No-Repeat Rationale

`V12_Research_No_Repeat_Index.md` marks `C13_BATTERY_JV_UTILIZATION_AMPC_IRA` as a Priority 0 archetype with only 15 representative rows, 12 symbols, 1/2 positive/counter balance, and 1/2 4B/4C coverage. Existing C13 concentration is around `051910`, `066970`, `373220`, `003670`, `005070`, and `006400`.

This loop therefore avoids those C13-top-covered symbols and adds four surrounding battery-supply-chain cases where the market priced JV / IRA / AMPC / localization vocabulary differently:

- `348370` 엔켐 — electrolyte localization / IRA supply-chain label, extreme MFE then 4B guard.
- `247540` 에코프로비엠 — cathode JV / AMPC vocabulary but demand-utilization drag.
- `020150` 롯데에너지머티리얼즈 — copper-foil local supply bridge, strong but volatile follow-through.
- `278280` 천보 — electrolyte additive recovery label without durable utilization/cash bridge.

The goal is not to prove “AMPC/IRA is bullish.” The goal is to force C13 to distinguish **company-level utilization-to-cash conversion** from **battery supply-chain vocabulary with high-MAE path risk**.

## 2. Price Source Validation

```jsonl
{"row_type":"price_source_validation","symbol":"348370","name":"엔켐","profile_path":"atlas/symbol_profiles/348/348370.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv","profile_first_date":"2021-11-01","profile_last_date":"2026-02-20","row_status_counts.tradable_ohlcv":1053,"corporate_action_candidate_count":0,"corporate_action_window_status":"clean_for_2024_entry_180D","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"247540","name":"에코프로비엠","profile_path":"atlas/symbol_profiles/247/247540.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_first_date":"2019-03-05","profile_last_date":"2026-02-20","row_status_counts.tradable_ohlcv":1712,"corporate_action_candidate_dates":["2022-06-27","2022-07-15"],"corporate_action_window_status":"clean_for_2024_entry_180D","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"020150","name":"롯데에너지머티리얼즈","profile_path":"atlas/symbol_profiles/020/020150.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv","profile_first_date":"2011-03-04","profile_last_date":"2026-02-20","row_status_counts.tradable_ohlcv":3681,"corporate_action_candidate_count":0,"corporate_action_window_status":"clean_for_2024_entry_180D","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
{"row_type":"price_source_validation","symbol":"278280","name":"천보","profile_path":"atlas/symbol_profiles/278/278280.json","tradable_shard":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv","profile_first_date":"2019-02-11","profile_last_date":"2026-02-20","row_status_counts.tradable_ohlcv":1727,"corporate_action_candidate_count":0,"corporate_action_window_status":"clean_for_2024_entry_180D","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_usable":true}
```

## 3. Case Summary

| case_id | symbol | role | entry_date | entry_price | 180D path | residual lesson |
|---|---:|---|---:|---:|---|---|
| C13-R3-L100-01 | 348370 | structural_success + local_4B_watch | 2024-01-15 | 107000 | extreme MFE with shallow early MAE | C13 can work when localization/JV vocabulary is immediately repriced, but 4B watch must turn on after vertical move. |
| C13-R3-L100-02 | 247540 | counterexample / high_MAE | 2024-01-22 | 248000 | modest MFE then heavy drawdown | Cathode JV/AMPC label alone cannot override demand-utilization break. |
| C13-R3-L100-03 | 020150 | mixed_positive + local_4B_watch | 2024-02-07 | 34650 | strong early MFE, later drawdown | Copper-foil localization can create Stage2-Actionable, but only if utilization/customer call-off bridge follows. |
| C13-R3-L100-04 | 278280 | counterexample | 2024-02-08 | 95000 | weak MFE, persistent MAE | Electrolyte additive recovery label without shipment/cash bridge should not receive a positive C13 bump. |

## 4. Machine-readable Trigger Rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C13-R3-L100-01","same_entry_group_id":"C13-R3-L100-01-A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_LOCALIZATION_IRA_SUPPLY_CHAIN_EXTREME_MFE_4B_WATCH","symbol":"348370","name":"엔켐","trigger_type":"Stage2-Actionable","entry_date":"2024-01-15","entry_price":107000.0,"entry_price_basis":"close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":235.05,"MAE_30D_pct":-6.36,"MFE_90D_pct":268.69,"MAE_90D_pct":-6.36,"MFE_180D_pct":268.69,"MAE_180D_pct":-6.36,"peak_date_proxy":"2024-04-08","peak_price_proxy":394500.0,"trough_date_proxy":"2024-01-22","trough_price_proxy":100200.0,"corporate_action_window_status":"clean","evidence_quality":"source_proxy_only","evidence_url_pending":true,"case_role":"structural_success","current_profile_error":"C13 local 4B guard too slow after vertical repricing; Stage2-Actionable OK but positive weight must not extrapolate beyond utilization-to-cash bridge","calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C13-R3-L100-02","same_entry_group_id":"C13-R3-L100-02-A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"CATHODE_JV_AMPC_LABEL_WITH_UTILIZATION_DEMAND_DRAG_HIGH_MAE","symbol":"247540","name":"에코프로비엠","trigger_type":"Stage2","entry_date":"2024-01-22","entry_price":248000.0,"entry_price_basis":"close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":10.08,"MAE_30D_pct":-14.92,"MFE_90D_pct":20.36,"MAE_90D_pct":-14.92,"MFE_180D_pct":20.36,"MAE_180D_pct":-47.58,"peak_date_proxy":"2024-03-27","peak_price_proxy":298500.0,"trough_date_proxy":"2024-H2","trough_price_proxy":130000.0,"corporate_action_window_status":"clean","evidence_quality":"source_proxy_only","evidence_url_pending":true,"case_role":"failed_rerating","current_profile_error":"C13 can over-credit cathode JV/AMPC vocabulary when utilization/call-off and EV demand drag are already pressuring the path","calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C13-R3-L100-03","same_entry_group_id":"C13-R3-L100-03-A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"COPPER_FOIL_LOCAL_SUPPLY_CUSTOMER_UTILIZATION_BRIDGE_LOCAL_4B","symbol":"020150","name":"롯데에너지머티리얼즈","trigger_type":"Stage2-Actionable","entry_date":"2024-02-07","entry_price":34650.0,"entry_price_basis":"close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":41.99,"MAE_30D_pct":-0.29,"MFE_90D_pct":51.23,"MAE_90D_pct":-13.00,"MFE_180D_pct":51.23,"MAE_180D_pct":-30.74,"peak_date_proxy":"2024-03-27","peak_price_proxy":52400.0,"trough_date_proxy":"2024-H2","trough_price_proxy":24000.0,"corporate_action_window_status":"clean","evidence_quality":"source_proxy_only","evidence_url_pending":true,"case_role":"mixed_positive","current_profile_error":"Stage2-Actionable captures early copper-foil rerating, but C13 needs a local 4B watch if customer utilization evidence does not follow the price MFE","calibration_usable":true,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C13-R3-L100-04","same_entry_group_id":"C13-R3-L100-04-A","dedupe_for_aggregate":true,"aggregate_group_role":"representative","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"ELECTROLYTE_ADDITIVE_RECOVERY_LABEL_NO_UTILIZATION_CASH_BRIDGE","symbol":"278280","name":"천보","trigger_type":"Stage2","entry_date":"2024-02-08","entry_price":95000.0,"entry_price_basis":"close","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","forward_window_trading_days":180,"MFE_30D_pct":5.05,"MAE_30D_pct":-9.26,"MFE_90D_pct":5.05,"MAE_90D_pct":-17.26,"MFE_180D_pct":5.05,"MAE_180D_pct":-35.00,"peak_date_proxy":"2024-02-21","peak_price_proxy":99800.0,"trough_date_proxy":"2024-H2","trough_price_proxy":61750.0,"corporate_action_window_status":"clean","evidence_quality":"source_proxy_only","evidence_url_pending":true,"case_role":"failed_rerating","current_profile_error":"Electrolyte additive recovery language without utilization/cash conversion is a C13 false positive, not a Stage2-Actionable boost","calibration_usable":true,"calibration_block_reasons":[]}
```

## 5. Score / Return Alignment

```jsonl
{"row_type":"score_simulation","case_id":"C13-R3-L100-01","symbol":"348370","raw_component_score_breakdown":{"EPS_FCF_Explosion":16,"Earnings_Visibility_Quality":17,"Bottleneck_Pricing_Power":15,"Market_Mispricing":14,"Valuation_Rerating_Runway":14,"Capital_Allocation":5,"Information_Confidence":7},"simulated_total":88,"simulated_stage":"Stage2-Actionable_to_Stage4B_watch","actual_180D_path":"very_high_MFE_low_initial_MAE","alignment":"positive_but_4B_guard_required"}
{"row_type":"score_simulation","case_id":"C13-R3-L100-02","symbol":"247540","raw_component_score_breakdown":{"EPS_FCF_Explosion":13,"Earnings_Visibility_Quality":13,"Bottleneck_Pricing_Power":13,"Market_Mispricing":11,"Valuation_Rerating_Runway":9,"Capital_Allocation":7,"Information_Confidence":6},"simulated_total":72,"simulated_stage":"Stage2","actual_180D_path":"modest_MFE_high_MAE","alignment":"false_positive_if_C13_weight_overcredits_JV_AMPC_label"}
{"row_type":"score_simulation","case_id":"C13-R3-L100-03","symbol":"020150","raw_component_score_breakdown":{"EPS_FCF_Explosion":15,"Earnings_Visibility_Quality":16,"Bottleneck_Pricing_Power":14,"Market_Mispricing":13,"Valuation_Rerating_Runway":12,"Capital_Allocation":6,"Information_Confidence":7},"simulated_total":83,"simulated_stage":"Stage2-Actionable","actual_180D_path":"good_MFE_with_later_drawdown","alignment":"early_positive_but_requires_utilization_followthrough"}
{"row_type":"score_simulation","case_id":"C13-R3-L100-04","symbol":"278280","raw_component_score_breakdown":{"EPS_FCF_Explosion":9,"Earnings_Visibility_Quality":12,"Bottleneck_Pricing_Power":10,"Market_Mispricing":11,"Valuation_Rerating_Runway":9,"Capital_Allocation":5,"Information_Confidence":6},"simulated_total":62,"simulated_stage":"Stage1_or_weak_Stage2","actual_180D_path":"weak_MFE_high_MAE","alignment":"counterexample"}
```

## 6. Aggregate Metrics

```jsonl
{"row_type":"aggregate_metric","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","representative_trigger_count":4,"calibration_usable_trigger_count":4,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":2,"current_profile_error_count":4,"avg_MFE_30D_pct":73.04,"avg_MAE_30D_pct":-7.71,"avg_MFE_90D_pct":86.33,"avg_MAE_90D_pct":-12.89,"avg_MFE_180D_pct":86.33,"avg_MAE_180D_pct":-29.92,"new_independent_case_count":4,"reused_case_count":0,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4}
```

## 7. Shadow Rule Candidate

```jsonl
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_JV_AMPC_UTILIZATION_TO_CASH_BRIDGE_REQUIRED","change_type":"new_axis_proposed","direction":"positive_stage_gate_tightening","proposal":"For C13, JV/IRA/AMPC vocabulary should only receive Stage2-Actionable quality when at least one company-level bridge is visible: utilization ramp, customer call-off durability, subsidy-to-OP/FCF conversion, shipment/revenue recognition, or margin revision. Without that bridge, cap at weak Stage2 or narrative watch."}
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_PRICE_MFE_LOCAL_4B_GUARD","change_type":"existing_axis_strengthened","direction":"guardrail","proposal":"If a C13 name delivers >40% MFE inside 30D without fresh utilization/cash evidence, mark local_4B_watch even if the full 180D path remains positive."}
{"row_type":"shadow_weight","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","axis":"C13_LABEL_FALSE_POSITIVE_HIGH_MAE_GUARD","change_type":"new_axis_proposed","direction":"negative_guardrail","proposal":"Battery materials names with AMPC/IRA/JV label but worsening utilization or customer call-off should receive high-MAE guard; do not add positive C13 weight solely from supply-chain label."}
```

## 8. Residual Contribution

```jsonl
{"row_type":"residual_contribution","selected_round":"R3","selected_loop":100,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":"C13_JV_AMPC_UTILIZATION_TO_CASH_BRIDGE_REQUIRED | C13_LABEL_FALSE_POSITIVE_HIGH_MAE_GUARD","existing_axis_strengthened":"stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail","existing_axis_weakened":null,"do_not_propose_new_weight_delta":false}
```

## 9. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 3
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 10. Deferred Coding Agent Handoff Prompt

Do not execute in this research loop.

```text
You are the later coding agent for Songdaiki/stock_agent. Ingest this MD as one v12 sector-archetype residual research artifact. Do not blindly apply global score changes. Parse trigger rows, aggregate metrics, and shadow_weight rows. For C13_BATTERY_JV_UTILIZATION_AMPC_IRA, evaluate whether to add an archetype-specific bridge requirement: JV/IRA/AMPC/subsidy labels should only upgrade to Stage2-Actionable if utilization, customer call-off, shipment revenue, subsidy-to-OP/FCF, margin revision, or cash conversion evidence is present. Also evaluate a local 4B guard when early price MFE exceeds 40% without fresh non-price follow-through. Keep production scoring unchanged until batch validation across multiple v12 files passes.
```

## 11. Final Research State

```text
completed_round = R3
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
current_profile_error_count = 4
calibration_usable_case_count = 4
calibration_usable_trigger_count = 4
diversity_score_summary = Priority 0 C13 shortage fill; existing C13 top-covered 051910/066970/373220/003670/005070/006400 avoided; 348370/247540/020150/278280 added as new C13 symbols
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false

auto_selected_coverage_gap = C13 rows 15 -> 19 if accepted; still Priority 0, need 11 to 30
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
new_axis_proposed = C13_JV_AMPC_UTILIZATION_TO_CASH_BRIDGE_REQUIRED | C13_LABEL_FALSE_POSITIVE_HIGH_MAE_GUARD
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
next_recommended_archetypes = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C02_POWER_GRID_DATACENTER_CAPEX
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C13_BATTERY_JV_UTILIZATION_AMPC_IRA.
