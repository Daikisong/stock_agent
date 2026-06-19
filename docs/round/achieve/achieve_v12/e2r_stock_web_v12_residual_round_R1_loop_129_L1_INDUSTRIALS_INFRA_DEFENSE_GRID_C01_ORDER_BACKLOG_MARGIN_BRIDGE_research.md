# E2R v12 Residual Research — R1 loop 129 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C01_ORDER_BACKLOG_MARGIN_BRIDGE

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
production_scoring_changed = false
shadow_weight_only = true
output_format = one_standalone_markdown_file
selected_round = R1
selected_loop = 129
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance/quality repair — C01 backlog→margin/FCF conversion failure, URL/proxy repair, high-MAE residual and 4C red-team check
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
filename = e2r_stock_web_v12_residual_round_R1_loop_129_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
```

## 0. Source/eligibility preflight

- Main execution prompt: `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`.
- No-repeat ledger: `docs/core/V12_Research_No_Repeat_Index.md`.
- Price atlas: `Songdaiki/stock-web`.
- Price basis: `tradable_raw`.
- Price adjustment status: `raw_unadjusted_marcap`.
- Stock-Web manifest max date: `2026-02-20`.
- Schema calculation basis: `MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100`; `MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100`.

No stock_agent code was opened or patched. This file is a research handoff only.

## 1. Why C01 this time

The updated no-repeat ledger shows that simple 30/50/80 row shortages are no longer the main gap. The current residual gap is quality repair: verified evidence URLs, source_proxy replacement, complete MFE/MAE rows, and balance of positive/counterexample cases. The latest local prior output in this chat was C05 loop 128. To avoid rematerializing C05, this run moves to C01 under the same R1/L1 family.

C01 is not “large backlog equals buy.” It is a conversion test. Backlog is a warehouse full of future revenue, but until it moves through the factory door into margin, cash flow, and revisions, it can still become dead weight. The cases below therefore separate backlog visibility from margin bridge, working-capital strain, and 4B/4C protection.

## 2. Case summary table

| symbol | company | trigger | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | current_profile_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|
| 108380 | 대양전기공업 | Stage2-Actionable | 2025-03-19 | 18170 | 9.41 | -20.64 | 51.07 | -20.64 | 86.30 | -20.64 | 2025-11-03 | 33850 | current_profile_too_early |
| 017960 | 한국카본 | Stage2-Actionable | 2024-05-17 | 10990 | 5.10 | -6.19 | 21.47 | -6.92 | 35.94 | -14.47 | 2025-01-22 | 14940 | current_profile_too_early |
| 014620 | 성광벤드 | Stage2-Actionable | 2025-03-21 | 26300 | 12.17 | -14.26 | 40.30 | -14.26 | 47.53 | -14.26 | 2025-09-11 | 38800 | current_profile_correct |
| 100090 | SK오션플랜트 | Stage2-Actionable | 2025-03-19 | 14620 | 7.73 | -17.44 | 51.50 | -17.44 | 115.46 | -17.44 | 2025-09-15 | 31500 | current_profile_4B_too_late |
| 008830 | 대동기어 | Stage4C | 2025-03-17 | 23000 | 8.04 | -30.96 | 8.04 | -30.96 | 8.04 | -39.13 | 2025-04-23 | 24850 | current_profile_correct |

## 3. Evidence source table

| symbol | company | source_url | source_proxy_only | evidence_url_pending | as-of evidence note |
|---|---|---|---:|---:|---|
| 108380 | 대양전기공업 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250318001593&docno=&method=search&viewerhost= | false | false | 2024 year-end order backlog disclosure and ship/defense delivery visibility. |
| 017960 | 한국카본 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000945&docno=&method=search&viewerhost= | false | false | LNG-carrier insulation-panel order/backlog route; margin conversion delayed. |
| 014620 | 성광벤드 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001932&method=search | false | false | Industrial fittings order cycle with raw material/nickel cost spread watch. |
| 100090 | SK오션플랜트 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250318000286&method=search | false | false | Ship/offshore backlog note and project/PO timing caveat. |
| 008830 | 대동기어 | https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250314000146&docno=&method=search&viewerhost= | false | false | Financial quality veto: weak liquidity/debt profile and no clean backlog-to-margin bridge at trigger date. |

## 4. Verified Stock-Web price rows

Rows are copied from the downloaded Stock-Web tradable shards in this execution. Format: `d,o,h,l,c,v,m`.

| symbol | row_kind | row |
|---|---|---|
| 108380 | entry | `2025-03-19,19060,19060,18060,18170,138678,KOSDAQ` |
| 108380 | 180D peak | `2025-11-03,30050,33850,30050,31850,234451,KOSDAQ` |
| 108380 | 180D MAE/trough | `2025-04-09,15300,15300,14420,14700,26905,KOSDAQ` |
| 017960 | entry | `2024-05-17,11500,11550,10990,10990,652908,KOSPI` |
| 017960 | 180D peak | `2025-01-22,14330,14940,14180,14630,1480715,KOSPI` |
| 017960 | 180D MAE/trough | `2024-12-09,9900,9970,9400,9410,710049,KOSPI` |
| 014620 | entry | `2025-03-21,25400,26600,25350,26300,377001,KOSDAQ` |
| 014620 | 180D peak | `2025-09-11,37200,38800,35400,35750,968114,KOSDAQ` |
| 014620 | 180D MAE/trough | `2025-04-07,23050,23850,22550,22600,363674,KOSDAQ` |
| 100090 | entry | `2025-03-19,14450,14950,14450,14620,68391,KOSPI` |
| 100090 | 180D peak | `2025-09-15,29600,31500,28300,28550,8391943,KOSPI` |
| 100090 | 180D MAE/trough | `2025-04-09,12140,12700,12070,12160,128274,KOSPI` |
| 008830 | entry | `2025-03-17,21600,23600,21050,23000,2070870,KOSDAQ` |
| 008830 | 180D peak | `2025-04-23,21600,24850,21150,22700,8175569,KOSDAQ` |
| 008830 | 180D MAE/trough | `2025-11-10,14000,14740,14000,14740,39004,KOSDAQ` |

## 5. Case notes and profile stress test

### 5.1 108380 대양전기공업 — structural success, but early MAE is not trivial

The order/backlog evidence is real enough for Stage2-Actionable, but the price path shows that even a correct C01 idea can first cut against the entry. Entry was `2025-03-19` at `18,170`; 30D MAE reached `-20.64%` before the 180D peak at `33,850`. This is not a failure; it is a reminder that C01 needs a “backlog-to-margin delay” pain budget. The current calibrated profile is directionally right but too early if it does not distinguish backlog visibility from realized margin bridge.

### 5.2 017960 한국카본 — large LNG backlog, delayed monetization

This case is a counterexample to instant Green. Backlog visibility was present, but 30D MFE was only `5.10%` and MAE later reached `-14.47%` before 180D MFE expanded to `35.94%`. The signal is not false; the timing is. C01 should not let large backlog alone unlock Stage3-Green before margin/revision confirmation.

### 5.3 014620 성광벤드 — successful order cycle, but spread/cost gate matters

The fittings order cycle did work over 90D/180D, with 90D MFE `40.30%` and 180D MFE `47.53%`. However, the same entry path suffered `-14.26%` MAE and a `-34.02%` post-peak drawdown. This supports a C01 subtype where order recovery must be paired with raw-material/cost-spread checks before full Green.

### 5.4 100090 SK오션플랜트 — backlog/project success with late 4B watch

The representative Stage2-Actionable row is strong on MFE (`115.46%` at 180D), but the after-peak drawdown was `-44.76%`. The usable trigger row is still the March 2025 Stage2 row because a September 2025 4B trigger does not have a full 180D forward window by the manifest max date. It is therefore retained as narrative-only 4B timing evidence, not a machine trigger row.

### 5.5 008830 대동기어 — 4C/financial-quality veto prevents false C01 promotion

The annual report evidence points to weak financial quality rather than a clean backlog-to-margin bridge. Entry `2025-03-17` at `23,000` produced only `8.04%` MFE over 30/90/180D, while MAE reached `-39.13%`. This is the negative-control case: industrial component narrative without cash/margin conversion and with weak liquidity should be blocked or routed to 4C/watch.

## 6. Residual contribution

```text
new_independent_case_count = 5
reused_case_count = 0
same_archetype_new_symbol_count = 5
same_archetype_new_trigger_family_count = 5
calibration_usable_case_count = 5
calibration_usable_trigger_count = 5
positive_case_count = 3
counterexample_count = 2
4B_or_4C_case_count = 2
current_profile_error_count = 4
source_proxy_only_count = 0
evidence_url_pending_count = 0
rows_missing_required_mfe_mae = 0
```

### New axis proposed

```text
axis = C01_backlog_to_margin_fcf_bridge_cap
shadow_weight_only = true
production_scoring_changed = false
```

Rule candidate:

```text
For C01_ORDER_BACKLOG_MARGIN_BRIDGE, do not allow backlog/order visibility alone to unlock Stage2-Actionable or Stage3-Green.
Require at least two of:
1. explicit delivery/revenue conversion window,
2. margin bridge or product-mix bridge,
3. confirmed revision or repeat conversion,
4. customer/project quality with low cancellation/call-off risk,
5. clean working-capital/liquidity profile.

If backlog is visible but margin bridge is missing and execution/working-capital risk is high:
- cap at Stage2 Watch, or
- if financial-quality evidence is explicitly adverse, route to Stage4C/watch.
```

## 7. Score simulation rows

| symbol | before_label | before_score | after_label | after_score | component_delta |
|---|---|---:|---|---:|---|
| 108380 | Stage2-Actionable | 76.0 | Stage2-Actionable_high_MAE_watch | 74.5 | margin bridge recognized, but early-MAE risk remains visible |
| 017960 | Stage2-Actionable | 73.0 | Stage2_Watch_until_margin_conversion | 68.0 | backlog large, margin/revision conversion delayed |
| 014620 | Stage2-Actionable | 75.5 | Stage2-Actionable_cost_spread_watch | 74.0 | cost-spread watch prevents overclean Green |
| 100090 | Stage2-Actionable | 77.5 | Stage2-Actionable_with_4B_watch_required | 72.0 | project success but 4B watch becomes necessary after overheat |
| 008830 | Stage1_or_no_actionable | 54.0 | Stage4C_or_blocked_watch | 42.0 | financial-quality veto blocks backlog-narrative false positive |

## 8. Machine-readable trigger JSONL

```jsonl
{"row_type":"trigger","trigger_id":"C01_L129_T01_108380_Stage2_Actionable_2025-03-19","case_id":"C01_L129_108380_20250318_structural_success_high_mae","symbol":"108380","company_name":"대양전기공업","round":"R1","loop":129,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE","sector":"shipbuilding electrical equipment / defense battery","primary_archetype":"order_backlog_to_margin_fcf_conversion","loop_objective":"C01 backlog-to-margin/FCF conversion repair; URL/proxy-quality repair; high-MAE and 4C residual mining","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-18","evidence_available_at_that_date":"KIND business report acptno=20250318001593; 2024-12-31 order backlog disclosure and ship/defense delivery visibility","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250318001593&docno=&method=search&viewerhost=","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["public_disclosure","order_or_backlog_visibility","customer_or_project_route","relative_strength_observed"],"stage3_evidence_fields":["margin_bridge_partial","financial_visibility_partial","conversion_timing_needed"],"stage4b_evidence_fields":["not_present_at_trigger_date"],"stage4c_evidence_fields":["not_present_at_trigger_date"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/108/108380/2025.csv","profile_path":"atlas/symbol_profiles/108/108380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-19","entry_price":18170.0,"MFE_30D_pct":9.41,"MFE_90D_pct":51.07,"MFE_180D_pct":86.3,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.64,"MAE_90D_pct":-20.64,"MAE_180D_pct":-20.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-11-03","peak_price":33850.0,"drawdown_after_peak_pct":-18.46,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_full_window_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_timing_verdict":"stage2_row_no_full_4b","four_b_evidence_type":"none_at_trigger_date","four_c_protection_label":"not_applicable","trigger_outcome_label":"backlog_margin_bridge_positive_with_initial_mae","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":193,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_candidate_in_window","same_entry_group_id":"C01_L129_108380_2025-03-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":78,"margin_bridge_score":58,"revision_score":52,"relative_strength_score":60,"customer_quality_score":70,"policy_or_regulatory_score":38,"valuation_repricing_score":56,"execution_risk_score":46,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"raw_component_scores_after":{"contract_score":72,"backlog_visibility_score":76,"margin_bridge_score":64,"revision_score":54,"relative_strength_score":60,"customer_quality_score":70,"policy_or_regulatory_score":38,"valuation_repricing_score":54,"execution_risk_score":52,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":10,"accounting_trust_risk_score":18},"weighted_score_before":76.0,"weighted_score_after":74.5,"label_before":"Stage2-Actionable","label_after":"Stage2-Actionable_high_MAE_watch","component_delta_explanation":"C01 shadow gate raises required margin/FCF conversion proof and penalizes weak liquidity/working-capital risk; production scoring unchanged."}
{"row_type":"trigger","trigger_id":"C01_L129_T02_017960_Stage2_Actionable_2024-05-17","case_id":"C01_L129_017960_20240516_delayed_success_counterexample_to_green","symbol":"017960","company_name":"한국카본","round":"R1","loop":129,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE","sector":"LNG carrier insulation panels / composite material supplier","primary_archetype":"order_backlog_to_margin_fcf_conversion","loop_objective":"C01 backlog-to-margin/FCF conversion repair; URL/proxy-quality repair; high-MAE and 4C residual mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-16","evidence_available_at_that_date":"KIND quarterly report acptno=20240516000945; LNG-carrier insulation-panel order/backlog visibility but revenue/margin conversion lag","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516000945&docno=&method=search&viewerhost=","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["public_disclosure","order_or_backlog_visibility","customer_or_project_route","relative_strength_observed"],"stage3_evidence_fields":["margin_bridge_delayed","financial_visibility_partial","conversion_timing_needed"],"stage4b_evidence_fields":["not_present_at_trigger_date"],"stage4c_evidence_fields":["not_present_at_trigger_date"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/017/017960/2024.csv;atlas/ohlcv_tradable_by_symbol_year/017/017960/2025.csv","profile_path":"atlas/symbol_profiles/017/017960.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":10990.0,"MFE_30D_pct":5.1,"MFE_90D_pct":21.47,"MFE_180D_pct":35.94,"MFE_1Y_pct":105.19,"MFE_2Y_pct":null,"MAE_30D_pct":-6.19,"MAE_90D_pct":-6.92,"MAE_180D_pct":-14.47,"MAE_1Y_pct":-14.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-01-22","peak_price":14940.0,"drawdown_after_peak_pct":-12.58,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_full_window_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_timing_verdict":"stage2_row_no_full_4b","four_b_evidence_type":"none_at_trigger_date","four_c_protection_label":"not_applicable","trigger_outcome_label":"large_backlog_but_margin_conversion_delayed","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":395,"calibration_block_reasons":[],"corporate_action_window_status":"clean_2024_2025_window; historical candidates 1996/1999/2012 outside window","same_entry_group_id":"C01_L129_017960_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":68,"backlog_visibility_score":84,"margin_bridge_score":44,"revision_score":36,"relative_strength_score":42,"customer_quality_score":72,"policy_or_regulatory_score":25,"valuation_repricing_score":45,"execution_risk_score":58,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":8,"accounting_trust_risk_score":24},"raw_component_scores_after":{"contract_score":68,"backlog_visibility_score":80,"margin_bridge_score":42,"revision_score":36,"relative_strength_score":42,"customer_quality_score":72,"policy_or_regulatory_score":25,"valuation_repricing_score":42,"execution_risk_score":64,"legal_or_contract_risk_score":18,"dilution_cb_risk_score":8,"accounting_trust_risk_score":24},"weighted_score_before":73.0,"weighted_score_after":68.0,"label_before":"Stage2-Actionable","label_after":"Stage2_Watch_until_margin_conversion","component_delta_explanation":"C01 shadow gate raises required margin/FCF conversion proof and penalizes weak liquidity/working-capital risk; production scoring unchanged."}
{"row_type":"trigger","trigger_id":"C01_L129_T03_014620_Stage2_Actionable_2025-03-21","case_id":"C01_L129_014620_20250320_structural_success_high_mae","symbol":"014620","company_name":"성광벤드","round":"R1","loop":129,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE","sector":"industrial fittings / LNG and plant pipe fittings","primary_archetype":"order_backlog_to_margin_fcf_conversion","loop_objective":"C01 backlog-to-margin/FCF conversion repair; URL/proxy-quality repair; high-MAE and 4C residual mining","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-20","evidence_available_at_that_date":"KIND business report acptno=20250320001932; 2024 industry/order cycle disclosure, raw-material and nickel cost pressure, order-to-sales timing","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250320001932&method=search","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["public_disclosure","order_or_backlog_visibility","customer_or_project_route","relative_strength_observed"],"stage3_evidence_fields":["margin_bridge_partial","financial_visibility_partial","conversion_timing_needed"],"stage4b_evidence_fields":["not_present_at_trigger_date"],"stage4c_evidence_fields":["not_present_at_trigger_date"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014620/2025.csv","profile_path":"atlas/symbol_profiles/014/014620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-21","entry_price":26300.0,"MFE_30D_pct":12.17,"MFE_90D_pct":40.3,"MFE_180D_pct":47.53,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-14.26,"MAE_90D_pct":-14.26,"MAE_180D_pct":-14.26,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-11","peak_price":38800.0,"drawdown_after_peak_pct":-34.02,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_full_window_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_timing_verdict":"stage2_row_no_full_4b","four_b_evidence_type":"none_at_trigger_date","four_c_protection_label":"not_applicable","trigger_outcome_label":"fittings_order_cycle_success_but_requires_cost_spread_gate","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":191,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_no_candidate_in_window","same_entry_group_id":"C01_L129_014620_2025-03-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":64,"backlog_visibility_score":66,"margin_bridge_score":56,"revision_score":46,"relative_strength_score":58,"customer_quality_score":62,"policy_or_regulatory_score":18,"valuation_repricing_score":52,"execution_risk_score":50,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":20},"raw_component_scores_after":{"contract_score":64,"backlog_visibility_score":66,"margin_bridge_score":61,"revision_score":48,"relative_strength_score":58,"customer_quality_score":62,"policy_or_regulatory_score":18,"valuation_repricing_score":50,"execution_risk_score":54,"legal_or_contract_risk_score":12,"dilution_cb_risk_score":8,"accounting_trust_risk_score":20},"weighted_score_before":75.5,"weighted_score_after":74.0,"label_before":"Stage2-Actionable","label_after":"Stage2-Actionable_cost_spread_watch","component_delta_explanation":"C01 shadow gate raises required margin/FCF conversion proof and penalizes weak liquidity/working-capital risk; production scoring unchanged."}
{"row_type":"trigger","trigger_id":"C01_L129_T04_100090_Stage2_Actionable_2025-03-19","case_id":"C01_L129_100090_20250318_structural_success_with_4b_watch","symbol":"100090","company_name":"SK오션플랜트","round":"R1","loop":129,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE","sector":"ship/offshore block and offshore plant fabrication","primary_archetype":"order_backlog_to_margin_fcf_conversion","loop_objective":"C01 backlog-to-margin/FCF conversion repair; URL/proxy-quality repair; high-MAE and 4C residual mining","trigger_type":"Stage2-Actionable","trigger_date":"2025-03-18","evidence_available_at_that_date":"KIND corrected business report acptno=20250318000286; year-end 2024 backlog note for ship/offshore business, project timing and block PO caveat","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250318000286&method=search","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["public_disclosure","order_or_backlog_visibility","customer_or_project_route","relative_strength_observed"],"stage3_evidence_fields":["margin_bridge_partial","financial_visibility_partial","conversion_timing_needed"],"stage4b_evidence_fields":["observed_ex_post_overheat_watch"],"stage4c_evidence_fields":["not_present_at_trigger_date"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/100/100090/2025.csv","profile_path":"atlas/symbol_profiles/100/100090.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-19","entry_price":14620.0,"MFE_30D_pct":7.73,"MFE_90D_pct":51.5,"MFE_180D_pct":115.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.44,"MAE_90D_pct":-17.44,"MAE_180D_pct":-17.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-09-15","peak_price":31500.0,"drawdown_after_peak_pct":-44.76,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"narrative_only_insufficient_forward_window_at_2025-09-15","four_b_full_window_peak_proximity":"narrative_only_insufficient_forward_window_at_2025-09-15","four_b_timing_verdict":"4B_watch_needed_but_not_machine_usable_due_forward_window","four_b_evidence_type":"valuation_positioning_overheat_ex_post_observed","four_c_protection_label":"not_applicable","trigger_outcome_label":"backlog_project_success_then_overheat_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":193,"calibration_block_reasons":[],"corporate_action_window_status":"clean_2025_window; historical candidates 2012/2018/2022 outside window","same_entry_group_id":"C01_L129_100090_2025-03-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":74,"margin_bridge_score":48,"revision_score":42,"relative_strength_score":65,"customer_quality_score":66,"policy_or_regulatory_score":30,"valuation_repricing_score":60,"execution_risk_score":62,"legal_or_contract_risk_score":24,"dilution_cb_risk_score":10,"accounting_trust_risk_score":24},"raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":72,"margin_bridge_score":50,"revision_score":42,"relative_strength_score":65,"customer_quality_score":66,"policy_or_regulatory_score":30,"valuation_repricing_score":56,"execution_risk_score":70,"legal_or_contract_risk_score":26,"dilution_cb_risk_score":10,"accounting_trust_risk_score":24},"weighted_score_before":77.5,"weighted_score_after":72.0,"label_before":"Stage2-Actionable","label_after":"Stage2-Actionable_with_4B_watch_required","component_delta_explanation":"C01 shadow gate raises required margin/FCF conversion proof and penalizes weak liquidity/working-capital risk; production scoring unchanged."}
{"row_type":"trigger","trigger_id":"C01_L129_T05_008830_Stage4C_2025-03-17","case_id":"C01_L129_008830_20250314_failed_rerating_4c_redteam","symbol":"008830","company_name":"대동기어","round":"R1","loop":129,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE","sector":"powertrain gear / industrial machinery component","primary_archetype":"order_backlog_to_margin_fcf_conversion","loop_objective":"C01 backlog-to-margin/FCF conversion repair; URL/proxy-quality repair; high-MAE and 4C residual mining","trigger_type":"Stage4C","trigger_date":"2025-03-14","evidence_available_at_that_date":"KIND business report acptno=20250314000146; earnings decline, current ratio 79.6%, debt ratio 191.5%; no clean backlog-to-margin bridge at trigger date","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20250314000146&docno=&method=search&viewerhost=","source_proxy_only":false,"evidence_url_pending":false,"stage2_evidence_fields":["public_financial_report","no_clean_backlog_bridge","relative_strength_only_rejected"],"stage3_evidence_fields":["no_confirmed_revision","margin_bridge_missing","working_capital_risk"],"stage4b_evidence_fields":["liquidity_overhang","balance_sheet_pressure"],"stage4c_evidence_fields":["accounting_or_trust_break","financial_quality_veto","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/008/008830/2025.csv","profile_path":"atlas/symbol_profiles/008/008830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2025-03-17","entry_price":23000.0,"MFE_30D_pct":8.04,"MFE_90D_pct":8.04,"MFE_180D_pct":8.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-30.96,"MAE_90D_pct":-30.96,"MAE_180D_pct":-39.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-04-23","peak_price":24850.0,"drawdown_after_peak_pct":-43.66,"green_lateness_ratio":"not_applicable_no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_full_window_peak_proximity":"not_applicable_no_usable_stage4b_trigger","four_b_timing_verdict":"stage2_row_no_full_4b","four_b_evidence_type":"none_at_trigger_date","four_c_protection_label":"4C_success_financial_quality_veto","trigger_outcome_label":"financial_quality_veto_prevents_backlog_narrative_false_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":195,"calibration_block_reasons":[],"corporate_action_window_status":"clean_2025_window; historical candidates 1998/1999/2011/2019 outside window","same_entry_group_id":"C01_L129_008830_2025-03-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"raw_component_scores_before":{"contract_score":32,"backlog_visibility_score":25,"margin_bridge_score":18,"revision_score":15,"relative_strength_score":40,"customer_quality_score":45,"policy_or_regulatory_score":10,"valuation_repricing_score":38,"execution_risk_score":88,"legal_or_contract_risk_score":22,"dilution_cb_risk_score":30,"accounting_trust_risk_score":76},"raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":20,"margin_bridge_score":15,"revision_score":12,"relative_strength_score":38,"customer_quality_score":45,"policy_or_regulatory_score":10,"valuation_repricing_score":30,"execution_risk_score":92,"legal_or_contract_risk_score":24,"dilution_cb_risk_score":34,"accounting_trust_risk_score":82},"weighted_score_before":54.0,"weighted_score_after":42.0,"label_before":"Stage1_or_no_actionable","label_after":"Stage4C_or_blocked_watch","component_delta_explanation":"C01 shadow gate raises required margin/FCF conversion proof and penalizes weak liquidity/working-capital risk; production scoring unchanged."}
```

## 9. Narrative-only / rejected rows

```json
{
  "row_type": "narrative_only",
  "case_id": "C01_L129_100090_20250915_4B_overlay",
  "symbol": "100090",
  "company_name": "SK오션플랜트",
  "round": "R1",
  "loop": 129,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIPBUILDING_EQUIPMENT_BACKLOG_TO_MARGIN_FCF_BRIDGE",
  "narrative_label": "Stage4B overlay candidate after observed full 180D peak",
  "trigger_date": "2025-09-15",
  "reason_not_trigger": "insufficient_forward_window_in_stock_web for 180D from 2025-09-15; retained only for 4B timing narrative",
  "observed_entry_price_if_used": 31500.0,
  "observed_drawdown_after_peak_pct": -44.76,
  "do_not_count_as_new_case": true
}
```

## 10. Batch Ingest Self-Audit

```text
expected_v12_result_file: true
filename_pattern_pass: true
metadata_filename_consistency: pass
jsonl_trigger_row_count: 5
calibration_usable_trigger_count: 5
representative_trigger_count: 5
new_weight_evidence_candidate_count: 1
guardrail_candidate_count: 2
narrative_only_or_rejected_count: 1
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
rows_with_compact_mfe_mae_alias_only: 0
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

You are a coding agent for Songdaiki/stock_agent. Read this MD together with the cumulative v12 corpus. Do not accept this single MD as sufficient to patch production by itself. If the cumulative batch confirms the pattern, implement only a shadow/profile candidate for canonical_archetype_id=C01_ORDER_BACKLOG_MARGIN_BRIDGE:

- Add/adjust a C01-specific bridge gate requiring backlog/order evidence to be paired with margin bridge, delivery/revenue conversion visibility, revision confirmation, or clean working-capital quality before Stage2-Actionable/Stage3-Green.
- Add a financial-quality veto for industrial component narratives where liquidity/debt/working-capital evidence is adverse and backlog-to-margin bridge is missing.
- Keep global thresholds unchanged unless broader batch evidence supports it.
- Do not loosen Stage3-Green.
- Preserve current price-only blowoff and full-4B non-price-evidence requirements.
- Re-run v12 calibration with --include-archive and verify no unknown canonical/sector IDs.
```

## 12. Final research state

```text
completed_round = R1
completed_loop = 129
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance/quality repair — C01 backlog→FCF conversion failure / high-MAE residual / URL-proxy repair
next_recommended_archetypes = C13_BATTERY_JV_UTILIZATION_AMPC_IRA; C15_MATERIAL_SPREAD_SUPERCYCLE; C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE; C01_ORDER_BACKLOG_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
