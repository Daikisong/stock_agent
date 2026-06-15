# e2r_stock_web_v12_residual_round_R1_loop_101_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research

## Metadata

```json
{
  "schema_family": "v12_sector_archetype_residual",
  "selected_round": "R1",
  "selected_loop": 101,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "EPC_CONSTRUCTION_SERVICE_ORDER_MARGIN_BRIDGE_VS_CIVIL_BACKLOG_PRICE_ONLY_FALSE_POSITIVE",
  "selection_basis": "docs/core/V12_Research_No_Repeat_Index.md",
  "selected_priority_bucket": "Priority 0",
  "round_schedule_status": "coverage_index_selected",
  "round_sector_consistency": "pass",
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## Selection / No-Repeat Basis

- selected_round: R1
- selected_loop: 101
- selected_priority_bucket: Priority 0
- canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
- V12_Research_No_Repeat_Index snapshot: C05 rows=13, symbols=10, positives/counter=2/4, 4B/4C=1/0, top covered symbols=000720, 028050, 047040, 006360, 011930, 023350.
- This loop avoids those top-covered symbols and adds 013580, 053690, 016250, and 375500 as new C05 symbols.

## Thesis

C05 is not a generic construction rally bucket. The local failure mode is narrower: an order, EPC, civil-construction, or project-management label can look like Stage2, but the rerating only persists when contract backlog is translated into gross margin, working-capital release, and cash-flow visibility. Without that bridge, price spikes behave like a scaffold without bolts: they stand for a few sessions, then the load moves back to cost risk and balance-sheet distrust.

This loop tests the residual error left after the global v12 rules. The global profile already blocks pure price-only blowoff and requires non-price evidence for full 4B. The C05-specific question is whether the non-price evidence must be stricter: not just "contract/order/backlog exists", but "order -> margin -> cash" is visible.

## Stock-Web Price Source Validation

| field | value |
|---|---|
| price_source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_max_date | 2026-02-20 |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| corporate_action_policy | windows with overlapping corporate-action candidates blocked by default |

Profile checks were performed on symbol_profiles for 013580, 053690, 016250, and 375500. None of the selected 2024 entry-to-180D windows overlaps a listed corporate-action candidate date.

## Case Table

| symbol | name | trigger_type | entry_date | entry_price | role | 180D MFE | 180D MAE | interpretation |
|---|---|---|---:|---:|---|---:|---:|---|
| 013580 | 계룡건설 | Stage2-Actionable | 2024-01-30 | 14200 | stage2_promote_candidate | 9.72% | -9.86% | underweights_low_mae_contract_margin_repair_when_price_MFE_is_modest_but_drawdown_is_contained |
| 053690 | 한미글로벌 | Stage2 | 2024-01-30 | 19010 | mixed_positive | 6.79% | -31.88% | stage2_actionable_bonus_can_overcredit_service_order_vocab_without_visible_margin_conversion |
| 016250 | SGC E&C | Stage2 | 2024-01-30 | 18470 | failed_rerating | 3.46% | -24.20% | source_proxy_epc_vocabulary_plus_stage2_bonus_is_too_generous_for_low_liquidity_margin_unproven_contractors |
| 375500 | DL이앤씨 | Stage4B | 2024-02-01 | 43100 | local_4b_watch | 1.62% | -33.64% | local_4b_watch_requires_stronger_non_price_margin_bridge_in_epc_civil_contractors |

## Calibration Readout

The C05 residual is asymmetric. A low-MAE contractor such as 013580 can deserve Stage2-Actionable watch even with only modest MFE because drawdown stayed contained. By contrast, 016250 and 375500 show that EPC/construction wording without visible margin conversion has poor forward asymmetry. 053690 sits in the middle: it offers a short service-order MFE burst but then behaves like a theme spike rather than a durable C05 rerating.

Therefore the proposed canonical compression is:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  -> positive gate: order/backlog/project-management evidence + explicit margin or cash bridge
  -> watch-only gate: order/backlog vocabulary + price MFE but weak margin bridge
  -> false-positive gate: civil/EPC label + no margin bridge + high 90D/180D MAE
```

## Machine-readable case rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"REGIONAL_CIVIL_CONTRACT_MARGIN_REPAIR_LOW_MAE_STAGE2_ACTIONABLE","symbol":"013580","symbol_name":"계룡건설","case_role":"stage2_promote_candidate","entry_date":"2024-01-30","primary_trigger_type":"Stage2-Actionable","calibration_usable":true,"novelty_basis":"new_symbol_within_C05_not_in_top_covered_symbols","source_quality":"source_proxy_only","evidence_url_pending":true,"summary":"underweights_low_mae_contract_margin_repair_when_price_MFE_is_modest_but_drawdown_is_contained"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_MANAGEMENT_EPC_SERVICE_SPIKE_WITH_NO_DURABLE_MARGIN_BRIDGE","symbol":"053690","symbol_name":"한미글로벌","case_role":"mixed_positive","entry_date":"2024-01-30","primary_trigger_type":"Stage2","calibration_usable":true,"novelty_basis":"new_symbol_within_C05_not_in_top_covered_symbols","source_quality":"source_proxy_only","evidence_url_pending":true,"summary":"stage2_actionable_bonus_can_overcredit_service_order_vocab_without_visible_margin_conversion"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_EPC_CONTRACT_LABEL_LOW_LIQUIDITY_FALSE_POSITIVE","symbol":"016250","symbol_name":"SGC E&C","case_role":"failed_rerating","entry_date":"2024-01-30","primary_trigger_type":"Stage2","calibration_usable":true,"novelty_basis":"new_symbol_within_C05_not_in_top_covered_symbols","source_quality":"source_proxy_only","evidence_url_pending":true,"summary":"source_proxy_epc_vocabulary_plus_stage2_bonus_is_too_generous_for_low_liquidity_margin_unproven_contractors"}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGECAP_EPC_REPAIR_LOCAL_4B_PRICE_ONLY_WITHOUT_MARGIN_BRIDGE","symbol":"375500","symbol_name":"DL이앤씨","case_role":"local_4b_watch","entry_date":"2024-02-01","primary_trigger_type":"Stage4B","calibration_usable":true,"novelty_basis":"new_symbol_within_C05_not_in_top_covered_symbols","source_quality":"source_proxy_only","evidence_url_pending":true,"summary":"local_4b_watch_requires_stronger_non_price_margin_bridge_in_epc_civil_contractors"}
```

## Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"REGIONAL_CIVIL_CONTRACT_MARGIN_REPAIR_LOW_MAE_STAGE2_ACTIONABLE","symbol":"013580","symbol_name":"계룡건설","market":"KOSPI","trigger_type":"Stage2-Actionable","trigger_family":"civil_contract_margin_repair_low_mae_stage2_actionable","entry_date":"2024-01-30","entry_price":14200.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":8.66,"MAE_30D_pct":-2.11,"MFE_90D_pct":8.66,"MAE_90D_pct":-8.8,"MFE_180D_pct":9.72,"MAE_180D_pct":-9.86,"peak_price_180D":15580.0,"trough_price_180D":12800.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_profile_path":"atlas/symbol_profiles/013/013580.json","stock_web_tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv"],"corporate_action_window_status":"not_contaminated","corporate_action_candidate_dates_checked":["1999-07-16"],"calibration_usable":true,"calibration_block_reasons":[],"case_role":"stage2_promote_candidate","current_profile_error":"underweights_low_mae_contract_margin_repair_when_price_MFE_is_modest_but_drawdown_is_contained","source_quality":"source_proxy_only","evidence_url_pending":true,"same_entry_group_id":"C05_013580_2024-01-30_Stage2-Actionable","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"CONSTRUCTION_MANAGEMENT_EPC_SERVICE_SPIKE_WITH_NO_DURABLE_MARGIN_BRIDGE","symbol":"053690","symbol_name":"한미글로벌","market":"KOSPI","trigger_type":"Stage2","trigger_family":"construction_management_service_spike_no_durable_margin_bridge","entry_date":"2024-01-30","entry_price":19010.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":6.79,"MAE_30D_pct":-10.31,"MFE_90D_pct":6.79,"MAE_90D_pct":-31.88,"MFE_180D_pct":6.79,"MAE_180D_pct":-31.88,"peak_price_180D":20300.0,"trough_price_180D":12950.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_profile_path":"atlas/symbol_profiles/053/053690.json","stock_web_tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv"],"corporate_action_window_status":"not_contaminated","corporate_action_candidate_dates_checked":[],"calibration_usable":true,"calibration_block_reasons":[],"case_role":"mixed_positive","current_profile_error":"stage2_actionable_bonus_can_overcredit_service_order_vocab_without_visible_margin_conversion","source_quality":"source_proxy_only","evidence_url_pending":true,"same_entry_group_id":"C05_053690_2024-01-30_Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"SMALL_EPC_CONTRACT_LABEL_LOW_LIQUIDITY_FALSE_POSITIVE","symbol":"016250","symbol_name":"SGC E&C","market":"KOSDAQ","trigger_type":"Stage2","trigger_family":"small_epc_contract_label_low_liquidity_false_positive","entry_date":"2024-01-30","entry_price":18470.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":3.46,"MAE_30D_pct":-11.75,"MFE_90D_pct":3.46,"MAE_90D_pct":-18.9,"MFE_180D_pct":3.46,"MAE_180D_pct":-24.2,"peak_price_180D":19110.0,"trough_price_180D":14000.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_profile_path":"atlas/symbol_profiles/016/016250.json","stock_web_tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/016/016250/2024.csv"],"corporate_action_window_status":"not_contaminated","corporate_action_candidate_dates_checked":["2020-12-08","2021-04-09","2022-04-08","2023-04-07","2025-06-25"],"calibration_usable":true,"calibration_block_reasons":[],"case_role":"failed_rerating","current_profile_error":"source_proxy_epc_vocabulary_plus_stage2_bonus_is_too_generous_for_low_liquidity_margin_unproven_contractors","source_quality":"source_proxy_only","evidence_url_pending":true,"same_entry_group_id":"C05_016250_2024-01-30_Stage2","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LARGECAP_EPC_REPAIR_LOCAL_4B_PRICE_ONLY_WITHOUT_MARGIN_BRIDGE","symbol":"375500","symbol_name":"DL이앤씨","market":"KOSPI","trigger_type":"Stage4B","trigger_family":"largecap_epc_repair_local_4b_price_only_without_margin_bridge","entry_date":"2024-02-01","entry_price":43100.0,"entry_price_basis":"close","forward_window_trading_days":180,"MFE_30D_pct":1.62,"MAE_30D_pct":-21.69,"MFE_90D_pct":1.62,"MAE_90D_pct":-26.1,"MFE_180D_pct":1.62,"MAE_180D_pct":-33.64,"peak_price_180D":43800.0,"trough_price_180D":28600.0,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_profile_path":"atlas/symbol_profiles/375/375500.json","stock_web_tradable_shards":["atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv"],"corporate_action_window_status":"not_contaminated","corporate_action_candidate_dates_checked":["2022-04-08","2022-04-28"],"calibration_usable":true,"calibration_block_reasons":[],"case_role":"local_4b_watch","current_profile_error":"local_4b_watch_requires_stronger_non_price_margin_bridge_in_epc_civil_contractors","source_quality":"source_proxy_only","evidence_url_pending":true,"same_entry_group_id":"C05_375500_2024-02-01_Stage4B","dedupe_for_aggregate":true,"aggregate_group_role":"representative"}
```

## Machine-readable score_simulation / aggregate / shadow / residual rows

```jsonl
{"row_type":"score_simulation","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","profile_proxy":"e2r_2_1_stock_web_calibrated","scenario":"C05_epc_contract_margin_bridge_required","raw_component_score_breakdown":{"EPS_FCF_Explosion":18,"Earnings_Visibility_and_Quality":22,"Bottleneck_and_Pricing_Power":10,"Market_Mispricing":12,"Valuation_Rerating_Runway":10,"Capital_Allocation":8,"Information_Confidence":20},"residual_error":"contract/order vocabulary alone still admits false Stage2/4B rows when margin bridge is weak","shadow_rule_candidate":"C05 requires explicit order-to-margin-to-cash bridge before Stage2-Actionable or local 4B promotion"}
{"row_type":"aggregate_metric","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","calibration_usable_case_count":4,"calibration_usable_trigger_count":4,"new_independent_case_count":4,"reused_case_count":0,"positive_case_count":1,"mixed_positive_count":1,"counterexample_count":2,"local_4b_watch_count":1,"current_profile_error_count":4,"median_MFE_180D_pct":5.73,"median_MAE_180D_pct":-27.94,"conclusion":"C05 remains under-covered and needs a stronger company-level margin/working-capital bridge gate."}
{"row_type":"shadow_weight","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_axis_proposed":"C05_epc_order_to_margin_to_cash_bridge_required","existing_axis_strengthened":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard","high_MAE_guardrail"],"suggested_shadow_delta":{"Earnings_Visibility_and_Quality":1,"Information_Confidence":1,"Market_Mispricing":-1},"do_not_apply_now":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","selected_round":"R1","selected_loop":101,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","loop_contribution_label":"canonical_archetype_rule_candidate","residual_error_found":true,"summary":"C05 false positives are not simply price-only; the residual failure is contract/backlog wording without evidence of gross margin, cost pass-through, working-capital release, or execution timing."}
{"row_type":"price_source_validation","price_source":"Songdaiki/stock-web","manifest":"atlas/manifest.json","source_name":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","manifest_max_date":"2026-02-20","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_unadjusted_caveat_acknowledged":true}
```

## Shadow Rule Candidate

```text
new_axis_proposed = C05_epc_order_to_margin_to_cash_bridge_required
rule:
  For C05, do not promote EPC/civil-construction/project-management vocabulary to Stage2-Actionable or full local 4B unless at least one bridge is present:
    1. fresh backlog/order converts into margin revision,
    2. working-capital/cost overrun risk is visibly easing,
    3. project mix has credible cost pass-through,
    4. quarterly OPM/FCF confirms the contract story.
If only price MFE + contract label is present, keep as Stage2 watch or local 4B watch, not Green/Actionable.
```

## Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 4
calibration_usable_trigger_count: 4
representative_trigger_count: 4
new_weight_evidence_candidate_count: 4
guardrail_candidate_count: 3
narrative_only_or_rejected_count: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## Deferred Coding Agent Handoff Prompt

```text
Do not execute in this research session.
When batch-applying v12 research outputs, parse this file as a C05 sector-archetype residual candidate. Add no production rule directly. Use the trigger rows to evaluate whether C05 needs a stricter order-to-margin-to-cash bridge before Stage2-Actionable and local 4B promotion. Preserve source_quality=source_proxy_only and evidence_url_pending=true; do not over-weight until primary evidence URLs are repaired.
```

## Final State

```text
completed_round = R1
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
new_independent_case_count = 4
reused_case_count = 0
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
positive_case_count = 1
mixed_positive_count = 1
counterexample_count = 2
local_4b_watch_count = 1
current_profile_error_count = 4
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
new_axis_proposed = C05_epc_order_to_margin_to_cash_bridge_required
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
auto_selected_coverage_gap = C05 rows 13 -> 17 if accepted; still Priority 0, need 13 to 30
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION
```

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.