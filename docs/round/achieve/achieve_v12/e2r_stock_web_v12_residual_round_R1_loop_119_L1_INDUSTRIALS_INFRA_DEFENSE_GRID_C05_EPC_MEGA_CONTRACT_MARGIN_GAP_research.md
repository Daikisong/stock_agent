# E2R Stock-Web V12 Residual Research — C05 EPC / Engineering Contract Margin-Cash Bridge Holdout v119

## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R1_loop_119_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
selected_round: R1
selected_loop: 119
selection_basis: docs/core/V12_Research_No_Repeat_Index.md used as no-repeat ledger only
selected_priority_bucket: Priority 1 static ledger C05 rows=47 / need-to-50=3; current-session C05 already above 50, so this is a new-symbol quality holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119
loop_objective:
  - holdout_validation
  - counterexample_mining
  - EPC_contract_to_revenue_margin_cash_bridge
  - 4B_non_price_requirement_stress_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
production_code_patch_included: false
production_scoring_patch_applied: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check
The MAIN prompt requires coverage-index-first selection, standard V12 filename, actual Stock-Web OHLC rows, and complete 30D/90D/180D MFE/MAE for every usable trigger. C05 is still a Priority 1 static-ledger target in the No-Repeat Index, but this session has already added several C05 files. Therefore this file uses six new C05 symbols and treats the loop as a quality holdout rather than a raw count-filling pass.

```yaml
hard_duplicate_key_checked: canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_symbol_count: 6
reused_case_count: 0
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
```

## 2. Price source validation
Stock-Web manifest basis: `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `max_date=2026-02-20`, and `calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year`. MFE/MAE follows the Stock-Web schema: max high / min low from entry date through the 30/90/180 tradable-row window. All six trigger rows have an available 180-trading-day forward window and no known 180D corporate-action overlap from profile-level dates used in this run.

## 3. Core finding
C05 should not treat **contract amount / EPC pipeline / engineering order competitiveness** as a clean Stage3 rerating by itself. A contract can open Stage2-Actionable, but Stage3-Yellow/Green should wait for the second bridge: revenue recognition, realized margin, working-capital absorption, and cash collection. If the price path shows deep MAE before that bridge appears, the correct route is `Stage2-Watch` or `Stage4B-LocalWatch`, not Stage3 persistence.

```text
contract/order headline -> revenue recognition + margin + cash bridge? -> Stage3 possible
contract/order headline -> bridge missing + MAE breach -> Stage2-Watch / local 4B overlay
```

## 4. Selected trigger rows
| # | symbol | company | trigger | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---:|---|---|---|---|---:|---:|---:|---:|---:|---|
| 1 | 091590 | 남화토건 | Stage2-Actionable | 2024-03-27 | 5270 | 1.14% | -30.93% | 1.14% | -30.93% | contract_headline_high_mae |
| 2 | 028100 | 동아지질 | Stage2-Actionable | 2024-11-29 | 13560 | 13.57% | -11.06% | 30.53% | -11.06% | large_contract_positive_with_long_delivery_gate |
| 3 | 023350 | 한국종합기술 | Stage2 | 2024-05-17 | 5470 | 11.52% | -21.21% | 44.42% | -23.13% | engineering_order_growth_low_mae_holdout |
| 4 | 054930 | 유신 | Stage2 | 2024-08-13 | 25550 | 10.76% | -20.35% | 10.76% | -23.68% | quality_holdout_with_high_mae |
| 5 | 126880 | 제이엔케이글로벌 | Stage4B | 2024-06-27 | 3855 | 15.82% | -24.77% | 15.82% | -26.33% | contract_revision_margin_gap_counterexample |
| 6 | 389260 | 대명에너지 | Stage2-Actionable | 2024-04-19 | 14780 | 44.79% | -32.34% | 44.79% | -34.30% | renewable_epc_pipeline_positive_with_cash_gate |


## 5. Aggregate stress result
```yaml
selected_round: "R1"
selected_loop: 119
large_sector_id: "L1_INDUSTRIALS_INFRA_DEFENSE_GRID"
canonical_archetype_id: "C05_EPC_MEGA_CONTRACT_MARGIN_GAP"
calibration_usable_rows: 6
representative_rows: 6
unique_symbol_count: 6
positive_case_count: 3
counterexample_count: 3
stage4b_overlay_count: 5
stage4c_count: 0
current_profile_error_count: 5
avg_MFE_90D_pct: 16.2671
avg_MAE_90D_pct: -23.4441
avg_MFE_180D_pct: 24.5785
avg_MAE_180D_pct: -24.9049
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rule_candidate: "C05_EPC_ENGINEERING_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V119"
```

## 6. Case notes

### 6.1 남화토건 / 091590
Public contract amount and counterparty were visible, but this was still a construction-project cash/margin bridge problem. C05 should not promote it above Stage2 until progress-rate revenue and cost absorption are visible.

### 6.2 동아지질 / 028100
The Singapore tunnel contract was material to revenue and deserves C05 positive treatment, but the long duration and civil-work cost risk mean Stage3 should be gated by revenue recognition and margin conversion.

### 6.3 한국종합기술 / 023350
The engineering order-growth report supports Stage2 stability and low-MAE holdout, but it is not a signed mega EPC contract. This row helps separate engineering service backlog from EPC margin rerating.

### 6.4 유신 / 054930
Engineering competitiveness and SOC exposure are real, yet small-cap price path volatility and the absence of a named cash-collection bridge require a Stage2-Watch cap.

### 6.5 제이엔케이글로벌 / 126880
A fired-heater supply contract is C05-relevant, but a contract amount reduction and delivery-period extension are direct local-4B evidence.

### 6.6 대명에너지 / 389260
Renewable EPC pipeline visibility is positive, but long-dated project development and PF/cash timing mean Stage3-Green should wait for actual revenue and margin bridge.

## 7. Machine-readable rows
```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_091590_NAMHWA_357BN_MILITARY_FACILITY_CONTRACT","trigger_id":"C05_R1_L119_091590_20240327_TRG","symbol":"091590","company_name":"남화토건","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":5270.0,"evidence_available_at_that_date":"국군중앙계약관과 357억9847만원 규모 23-U-세탁소 신축 시설공사 계약이 확인됐다. 단일 계약 headline은 Stage2 근거지만, 군 시설공사/건축공사 성격상 매출인식·원가율·cash collection bridge가 확인되기 전 Stage3로 올리면 안 된다.","evidence_source":"https://www.datatooza.com/article/2024032716245590123f2b92199f_80","stage2_evidence_fields":["single_sales_supply_contract","public_contract_amount_visible","project_delivery_window_visible"],"stage3_evidence_fields":["not_supported_without_realized_margin_or_cash_collection"],"stage4b_evidence_fields":["construction_margin_gap_risk","working_capital_timing_risk","contract_headline_without_FCF_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/091/091590/2024.csv","profile_path":"atlas/symbol_profiles/091/091590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.1385,"MAE_30D_pct":-13.2827,"MFE_90D_pct":1.1385,"MAE_90D_pct":-30.9298,"MFE_180D_pct":1.1385,"MAE_180D_pct":-30.9298,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-27","peak_price":5330.0,"drawdown_after_peak_pct":-31.7073,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2024-12-19","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_091590_Stage2-Actionable_2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_091590_NAMHWA_357BN_MILITARY_FACILITY_CONTRACT","trigger_id":"C05_R1_L119_091590_20240327_TRG","symbol":"091590","company_name":"남화토건","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":55,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":31.9,"local_4b_pressure_score":75},"weighted_score_before":62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_size_visibility":45,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":31.9,"local_4b_pressure_score":90},"weighted_score_after":50,"stage_label_after":"Stage4B-LocalWatch","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":1.1385,"MAE_90D_pct":-30.9298,"score_return_alignment_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_028100_DONGA_1539BN_SINGAPORE_TUNNEL_CONTRACT","trigger_id":"C05_R1_L119_028100_20241129_TRG","symbol":"028100","company_name":"동아지질","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-11-29","entry_date":"2024-11-29","entry_price":13560.0,"evidence_available_at_that_date":"싱가포르 Pasir Ris Interchange Station and Tunnels 관련 공사에서 1,538.9억원 규모 계약이 공시됐다. 최근 매출액 대비 44.6% 수준이라 C05 positive evidence지만, 계약기간이 장기이므로 revenue recognition과 margin bridge gate를 남긴다.","evidence_source":"https://www.hankyung.com/article/202411293621L","stage2_evidence_fields":["large_overseas_civil_contract","named_project_and_counterparty","contract_amount_material_to_sales"],"stage3_evidence_fields":["backlog_visibility_partial","revenue_recognition_timing_needs_confirmation"],"stage4b_evidence_fields":["long_duration_contract","cost_overrun_and_working_capital_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028100/2024.csv","profile_path":"atlas/symbol_profiles/028/028100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.5693,"MAE_30D_pct":-11.0619,"MFE_90D_pct":13.5693,"MAE_90D_pct":-11.0619,"MFE_180D_pct":30.531,"MAE_180D_pct":-11.0619,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-07-04","peak_price":17700.0,"drawdown_after_peak_pct":-16.1582,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2025-08-27","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_028100_Stage2-Actionable_2024-11-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_028100_DONGA_1539BN_SINGAPORE_TUNNEL_CONTRACT","trigger_id":"C05_R1_L119_028100_20241129_TRG","symbol":"028100","company_name":"동아지질","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":65,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":55.58,"local_4b_pressure_score":55},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_size_visibility":60,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":55.58,"local_4b_pressure_score":65},"weighted_score_after":65,"stage_label_after":"Stage2-Actionable_or_Stage3-Yellow_after_bridge","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":13.5693,"MAE_90D_pct":-11.0619,"score_return_alignment_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_023350_KET_ENGINEERING_ORDER_GROWTH_STABLE_BUSINESS","trigger_id":"C05_R1_L119_023350_20240517_TRG","symbol":"023350","company_name":"한국종합기술","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":5470.0,"evidence_available_at_that_date":"한국기업평가 리포트는 종합엔지니어링 사업기반, 주요 사업 수주 증대, 시공부문 확대를 통한 외형 성장을 언급했다. C05에서는 안정적 order backlog evidence로 인정하되, 단일 mega EPC contract가 아니라 Stage2/Stage3-Yellow 후보로 제한한다.","evidence_source":"https://m.kisrating.com/fileDown.do?fileName=rs20240517-12.pdf&gubun=2&menuCd=R8","stage2_evidence_fields":["engineering_order_growth","stable_domestic_engineering_position","construction_segment_expansion"],"stage3_evidence_fields":["margin_bridge_partial","not_a_single_mega_contract"],"stage4b_evidence_fields":["low_liquidity_smallcap_watch","project_mix_margin_uncertainty"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/023/023350/2024.csv","profile_path":"atlas/symbol_profiles/023/023350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":11.5174,"MAE_30D_pct":-3.1079,"MFE_90D_pct":11.5174,"MAE_90D_pct":-21.2066,"MFE_180D_pct":44.4241,"MAE_180D_pct":-23.1261,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-13","peak_price":7900.0,"drawdown_after_peak_pct":-35.1899,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2025-02-13","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_023350_Stage2_2024-05-17","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_023350_KET_ENGINEERING_ORDER_GROWTH_STABLE_BUSINESS","trigger_id":"C05_R1_L119_023350_20240517_TRG","symbol":"023350","company_name":"한국종합기술","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":65,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":53.89,"local_4b_pressure_score":75},"weighted_score_before":70,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_size_visibility":60,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":53.89,"local_4b_pressure_score":90},"weighted_score_after":65,"stage_label_after":"Stage2-Actionable_or_Stage3-Yellow_after_bridge","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":11.5174,"MAE_90D_pct":-21.2066,"score_return_alignment_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_054930_YOOSHIN_ENGINEERING_ORDER_COMPETITIVENESS","trigger_id":"C05_R1_L119_054930_20240813_TRG","symbol":"054930","company_name":"유신","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage2","trigger_date":"2024-08-13","entry_date":"2024-08-13","entry_price":25550.0,"evidence_available_at_that_date":"신용평가 자료는 유신이 토목엔지니어링 분야에서 수주실적·기술인력·수주경쟁력을 보유한다고 평가했다. 하지만 이는 반복 용역/공공 SOC exposure이지 mega EPC margin bridge가 아니므로 C05 Stage3 과승격을 막아야 한다.","evidence_source":"https://m.kisrating.com/fileDown.do?fileName=rs20240813-15.pdf&gubun=2&menuCd=R8","stage2_evidence_fields":["engineering_order_competitiveness","SOC_policy_exposure","stable_design_supervision_business"],"stage3_evidence_fields":["not_supported_without_major_contract_revenue_margin_bridge"],"stage4b_evidence_fields":["smallcap_liquidity_watch","policy_order_to_margin_gap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/054/054930/2024.csv","profile_path":"atlas/symbol_profiles/054/054930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.9354,"MAE_30D_pct":-20.3523,"MFE_90D_pct":10.7632,"MAE_90D_pct":-20.3523,"MFE_180D_pct":10.7632,"MAE_180D_pct":-23.6791,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-11-13","peak_price":28300.0,"drawdown_after_peak_pct":-31.0954,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2025-05-15","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_054930_Stage2_2024-08-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_054930_YOOSHIN_ENGINEERING_ORDER_COMPETITIVENESS","trigger_id":"C05_R1_L119_054930_20240813_TRG","symbol":"054930","company_name":"유신","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":55,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":40.1,"local_4b_pressure_score":75},"weighted_score_before":62,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_size_visibility":45,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":40.1,"local_4b_pressure_score":90},"weighted_score_after":50,"stage_label_after":"Stage2-Watch","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":10.7632,"MAE_90D_pct":-20.3523,"score_return_alignment_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_126880_JNK_FIRED_HEATER_CONTRACT_REDUCTION_REVISION","trigger_id":"C05_R1_L119_126880_20240627_TRG","symbol":"126880","company_name":"제이엔케이글로벌","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-06-27","entry_date":"2024-06-27","entry_price":3855.0,"evidence_available_at_that_date":"Fired Heaters 공급계약 정정공시에서 계약금액이 121억원에서 79.49억원으로 줄고 계약기간도 연장됐다. EPC/plant equipment contract evidence가 있더라도 계약금액 축소·납기 연장은 C05의 local 4B guardrail이다.","evidence_source":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240627000567&docno=&method=search&viewerhost=","stage2_evidence_fields":["plant_equipment_supply_contract","fired_heater_EPC_linkage"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["contract_amount_reduction","delivery_period_extension","customer_negotiation_revision","revenue_margin_bridge_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/126/126880/2024.csv","profile_path":"atlas/symbol_profiles/126/126880.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.8236,"MAE_30D_pct":-24.773,"MFE_90D_pct":15.8236,"MAE_90D_pct":-24.773,"MFE_180D_pct":15.8236,"MAE_180D_pct":-26.3294,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-05","peak_price":4465.0,"drawdown_after_peak_pct":-36.3942,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2025-03-26","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_126880_Stage4B_2024-06-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_126880_JNK_FIRED_HEATER_CONTRACT_REDUCTION_REVISION","trigger_id":"C05_R1_L119_126880_20240627_TRG","symbol":"126880","company_name":"제이엔케이글로벌","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":55,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":40.53,"local_4b_pressure_score":75},"weighted_score_before":67,"stage_label_before":"Stage2-Actionable_without_C05_specific_guard","raw_component_scores_after":{"contract_size_visibility":45,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":40.53,"local_4b_pressure_score":90},"weighted_score_after":55,"stage_label_after":"Stage4B-LocalWatch","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":15.8236,"MAE_90D_pct":-24.773,"score_return_alignment_label":"counterexample_or_local_4b","current_profile_verdict":"current_profile_false_positive_if_contract_headline_is_promoted_without_margin_cash_bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","case_id":"C05_R1_L119_389260_DAEMYUNG_WIND_EPC_PIPELINE_IR","trigger_id":"C05_R1_L119_389260_20240419_TRG","symbol":"389260","company_name":"대명에너지","round":"R1","loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","sector":"industrials_infra_defense_grid","primary_archetype":"epc_mega_contract_margin_gap","loop_objective":"holdout_validation|counterexample_mining|working_capital_cash_collection_gate|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":14780.0,"evidence_available_at_that_date":"2024년 4월 IR 자료/KIRS 자료에서 김천풍력발전 EPC, 곡성풍력 등 EPC·운영계약 현황과 2024~2025년 매출 반영 기대가 제시됐다. 자체 개발 EPC pipeline은 C05 positive지만 장기 프로젝트라 cash collection과 margin bridge 확인 전 Green은 제한한다.","evidence_source":"https://w4.kirs.or.kr/download/research/240524_%EB%8C%80%EB%AA%85%EC%97%90%EB%84%88%EC%A7%80.pdf","stage2_evidence_fields":["renewable_EPC_pipeline","project_development_to_EPC_route","revenue_recognition_expected"],"stage3_evidence_fields":["project_pipeline_visible_but_cash_margin_bridge_needed"],"stage4b_evidence_fields":["long_duration_project_cash_collection_watch","renewable_policy_or_PF_timing_risk"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/389/389260/2024.csv","profile_path":"atlas/symbol_profiles/389/389260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":44.7903,"MAE_30D_pct":-3.3829,"MFE_90D_pct":44.7903,"MAE_90D_pct":-32.341,"MFE_180D_pct":44.7903,"MAE_180D_pct":-34.3031,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_1Y_pct":null,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-27","peak_price":21400.0,"drawdown_after_peak_pct":-54.6262,"four_b_timing_verdict":"local_4b_watch_until_revenue_margin_working_capital_cash_bridge_confirmed","four_b_evidence_type":"EPC_contract_revenue_margin_or_working_capital_gap","four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge","calibration_usable":true,"forward_window_trading_days":180,"forward_window_end_date":"2025-01-15","calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_profile_dates_or_no_overlap","window_180D_corporate_action_contaminated":false,"same_entry_group_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP_389260_Stage2-Actionable_2024-04-19","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false,"production_scoring_patch_applied":false}
{"row_type":"score_simulation","profile_id":"C05_working_capital_margin_cash_gate_v119_shadow","case_id":"C05_R1_L119_389260_DAEMYUNG_WIND_EPC_PIPELINE_IR","trigger_id":"C05_R1_L119_389260_20240419_TRG","symbol":"389260","company_name":"대명에너지","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","raw_component_scores_before":{"contract_size_visibility":65,"backlog_or_project_visibility":62,"revenue_recognition_visibility":40,"margin_bridge_score":35,"working_capital_cash_collection_score":32,"execution_risk_score":65,"price_path_quality_score":47.33,"local_4b_pressure_score":75},"weighted_score_before":70,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_size_visibility":60,"backlog_or_project_visibility":58,"revenue_recognition_visibility":35,"margin_bridge_score":28,"working_capital_cash_collection_score":25,"execution_risk_score":75,"price_path_quality_score":47.33,"local_4b_pressure_score":90},"weighted_score_after":65,"stage_label_after":"Stage4B-LocalWatch","changed_components":["revenue_recognition_visibility","margin_bridge_score","working_capital_cash_collection_score","local_4b_pressure_score"],"component_delta_explanation":"C05-specific gate discounts contract/order headlines until revenue recognition, realized margin, working-capital and cash-collection bridge are confirmed; deep MAE forces local 4B overlay.","MFE_90D_pct":44.7903,"MAE_90D_pct":-32.341,"score_return_alignment_label":"positive_with_guardrail","current_profile_verdict":"current_profile_correct_only_if_stage3_waits_for_revenue_margin_cash_bridge"}
{"row_type":"aggregate","selected_round":"R1","selected_loop":119,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"mixed_C05_engineering_civil_heater_renewable_epc_cash_margin_holdout_v119","calibration_usable_rows":6,"representative_rows":6,"unique_symbol_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_overlay_count":5,"stage4c_count":0,"current_profile_error_count":5,"avg_MFE_30D_pct":14.9624,"avg_MAE_30D_pct":-12.6601,"avg_MFE_90D_pct":16.2671,"avg_MAE_90D_pct":-23.4441,"avg_MFE_180D_pct":24.5785,"avg_MAE_180D_pct":-24.9049,"rows_MAE180_le_minus_20pct":5,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"rule_candidate":"C05_EPC_ENGINEERING_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V119"}
{"row_type":"shadow_weight","rule_scope":"canonical_archetype","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","new_axis_proposed":"C05_EPC_ENGINEERING_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V119","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":[],"do_not_propose_new_weight_delta":false}
{"row_type":"residual_contribution","new_independent_case_count":6,"reused_case_count":0,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"positive_case_count":3,"counterexample_count":3,"current_profile_error_count":5,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 8. Proposed shadow rule candidate
```text
C05_EPC_ENGINEERING_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V119
```

Rule mechanics:

```yaml
Stage2_Actionable_allowed_when:
  - signed contract, material order, engineering backlog, or EPC pipeline is publicly visible
Stage3_Yellow_allowed_when_all:
  - revenue recognition timing is visible
  - realized margin or OPM bridge is visible
  - working-capital / cash-collection burden is not worsening
  - price path does not show a deep MAE breach before the bridge appears
Stage4B_LocalWatch_when_any:
  - contract amount is reduced or delivery is delayed
  - long-duration project has cash-collection uncertainty
  - MAE90 <= -20 or MAE180 <= -25 before the revenue/margin bridge
Stage4C_reserved_for:
  - cancellation, credit collapse, accounting/trust break, or confirmed project loss thesis break
```

## 9. Residual Contribution Summary
```yaml
new_independent_case_count: 6
reused_case_count: 0
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
positive_case_count: 3
counterexample_count: 3
current_profile_error_count: 5
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
new_axis_proposed: C05_EPC_ENGINEERING_CONTRACT_REQUIRES_REVENUE_MARGIN_WORKING_CAPITAL_AND_CASH_COLLECTION_GATE_V119
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 10. Batch Ingest Self-Audit
```yaml
expected_v12_result_file: true
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
rows_missing_entry_price_or_date: 0
rows_with_noncanonical_trigger_type: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 11. Deferred Coding Agent Handoff Prompt
```text
Read this standalone V12 residual research file and ingest only machine-readable rows that pass validation. Do not apply production scoring blindly. Treat the proposed C05 axis as a shadow rule candidate: require revenue recognition, realized margin, working-capital and cash-collection confirmation before Stage3 persistence for EPC/engineering contract headlines. Keep the evidence as C05-specific unless repeated across other contract-heavy archetypes.
```

## 12. Next research state
```yaml
completed_round: R1
completed_loop: 119
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 static C05 holdout; session-adjusted quality pass
next_recommended_archetypes:
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
  - C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_holdout_only_if_new_delivery_or_calloff_path
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP_holdout_only_if_new_working_capital_or_cash_collection_path
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
