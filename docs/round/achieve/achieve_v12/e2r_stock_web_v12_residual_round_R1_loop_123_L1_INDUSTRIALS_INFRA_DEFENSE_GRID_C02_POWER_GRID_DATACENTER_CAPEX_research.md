# E2R Stock-Web v12 Residual Research — R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02_POWER_GRID_DATACENTER_CAPEX

```text
selected_round: R1
selected_loop: 123
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_static_ledger / C02 rows 10 need_to_30 20 before local continuation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE
loop_objective: coverage_gap_fill | followup_new_symbol_date_family | source_proxy_replacement | 4B_non_price_requirement_stress_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Coverage decision

The remote No-Repeat Index still lists `C02_POWER_GRID_DATACENTER_CAPEX` as the lowest Priority 0 bucket: 10 representative rows, `need_to_30=20`, `need_to_50=40`. This loop keeps the same canonical because C02 still needs boundary cases, but it avoids the previous transformer/cable/high-voltage equipment set and instead tests the **AMI / smart-meter / capacitor / ESS-cooling proxy boundary**.

This is not a live stock recommendation and not a production scoring patch. It is a standalone historical calibration MD using stock-web `tradable_raw` OHLCV rows.

## 2. Price-source and validation scope

Stock-Web manifest facts used in this loop:

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
tradable_row_count: 14354401
raw_row_count: 15214118
symbol_count: 5414
manifest_max_date: 2026-02-20
```

Downloaded shard years:

```text
040160: 2024, 2025
057540: 2024, 2025
009470: 2024, 2025
001820: 2024, 2025
125210: 2024, 2025
107640: 2024, 2025
```

MFE/MAE is computed from entry close `c` against max `h` and min `l` over 30/90/180 trading-day windows. Share-count stability in the downloaded tradable rows is used as a raw-unadjusted contamination screen. `107640` is kept as narrative-only because `s` changes inside the 180D window.

## 3. Evidence split and case table

| symbol | company | trigger_type | entry_date | entry_price | MFE30 / MAE30 | MFE90 / MAE90 | MFE180 / MAE180 | role | verdict |
|---|---|---|---:|---:|---:|---:|---:|---|---|
| 040160 | NuriFlex | Stage2 | 2024-05-16 | 3500 | 4.14 / -9.57 | 4.14 / -27.71 | 4.14 / -35.14 | usable representative | false_positive_if_AMI_policy_language_promoted_to_C02_Actionable |
| 057540 | OmniSystem | Stage2 | 2024-05-17 | 1060 | 12.08 / -9.25 | 12.08 / -27.64 | 12.08 / -38.4 | usable representative | false_positive_if_meter_product_identity_gets_C02_Yellow |
| 009470 | Samhwa Electric | Stage4B | 2024-06-05 | 73100 | 22.98 / -26.13 | 22.98 / -52.39 | 22.98 / -65.12 | usable representative | missed_local_4B_if_component_route_treated_as_fresh_Yellow_after_reprice |
| 001820 | Samhwa Capacitor | Stage2 | 2024-10-10 | 35750 | 3.5 / -26.29 | 3.5 / -35.24 | 3.5 / -39.86 | usable representative | false_positive_if_capacitor_optional_route_promoted_before_named_customer_or_margin_bridge |
| 125210 | Amogreentech | Stage2 | 2024-01-09 | 12900 | 2.79 / -20.23 | 2.79 / -24.03 | 2.79 / -48.06 | usable representative | false_positive_if_ESS_power_material_identity_treated_as_C02_direct_CAPEX |
| 107640 | Hanjung NCS | Stage4B | 2024-06-24 | 34000 | 81.76 / -11.03 | 81.76 / -11.03 | 81.76 / -45.59 | narrative-only blocked | narrative_useful_but_not_representative_due_share_count_change |


## 4. Interpretation

C02 is not just “anything related to electricity.” It is closer to a toll gate where physical grid/datacenter capex has to pass with a named customer, direct power-system order, backlog, capacity or lead-time lock, and margin conversion. AMI vendors and metering companies are useful for smart-grid vocabulary, but the price paths here show why they should usually remain Stage2-watch without direct backlog and earnings bridge.

The capacitor/ESS-cooling cases are more ambiguous. `009470` has a genuine datacenter power-efficiency route through SSD backup power and cooling efficiency, but the price path says the market paid first and asked for conversion later: 90D MFE stayed at 22.98% while 180D MAE fell to -65.12%. That is not a clean fresh Yellow; it is a local 4B/profit-lock route. `107640` has a strong ESS liquid-cooling narrative and huge early MFE, but stock-web raw-unadjusted share count changes block representative calibration use.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_040160_20240516_NURIFLEX_AMI_ROADMAP_PROXY","trigger_id":"TRG_R1L123_C02_040160_20240516_01","symbol":"040160","company_name":"NuriFlex","market":"KOSDAQ","evidence_date":"2024-05-14","trigger_date":"2024-05-14","entry_date":"2024-05-16","entry_price":3500.0,"trigger_type":"Stage2","evidence_family":"AMI_national_roadmap_and_overseas_metering_optional_order","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":4.14,"MFE_90D_pct":4.14,"MFE_180D_pct":4.14,"MAE_30D_pct":-9.57,"MAE_90D_pct":-27.71,"MAE_180D_pct":-35.14,"peak_30D_date":"2024-06-11","peak_90D_date":"2024-06-11","peak_180D_date":"2024-06-11","low_30D_date":"2024-06-25","low_90D_date":"2024-09-05","low_180D_date":"2024-11-14","share_count_unique_180D":1,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|040160|Stage2|2024-05-16","positive_or_counterexample":"counterexample","stage4b_overlay":false,"current_profile_verdict":"false_positive_if_AMI_policy_language_promoted_to_C02_Actionable","residual_error_type":"AMI_policy_rollout_without_backlog_capa_margin_bridge","source_url":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240514000588&docno=&method=search&viewerhost="}
{"row_type":"trigger","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_057540_20240517_OMNISYSTEM_DIGITAL_METER_PROXY","trigger_id":"TRG_R1L123_C02_057540_20240517_02","symbol":"057540","company_name":"OmniSystem","market":"KOSDAQ","evidence_date":"2024-05-16","trigger_date":"2024-05-16","entry_date":"2024-05-17","entry_price":1060.0,"trigger_type":"Stage2","evidence_family":"digital_meter_and_remote_metering_production","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":12.08,"MFE_90D_pct":12.08,"MFE_180D_pct":12.08,"MAE_30D_pct":-9.25,"MAE_90D_pct":-27.64,"MAE_180D_pct":-38.4,"peak_30D_date":"2024-06-11","peak_90D_date":"2024-06-11","peak_180D_date":"2024-06-11","low_30D_date":"2024-05-30","low_90D_date":"2024-09-09","low_180D_date":"2024-11-15","share_count_unique_180D":1,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|057540|Stage2|2024-05-17","positive_or_counterexample":"counterexample","stage4b_overlay":false,"current_profile_verdict":"false_positive_if_meter_product_identity_gets_C02_Yellow","residual_error_type":"product_identity_without_customer_order_or_margin_bridge","source_url":"https://kind.krx.co.kr/common/disclsviewer.do?acptno=20240516001023&docno=&method=search&viewerhost="}
{"row_type":"trigger","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_009470_20240605_SAMHWA_ELECTRIC_DATACENTER_CAPACITOR_LOCAL4B","trigger_id":"TRG_R1L123_C02_009470_20240605_03","symbol":"009470","company_name":"Samhwa Electric","market":"KOSPI","evidence_date":"2024-06-05","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":73100.0,"trigger_type":"Stage4B","evidence_family":"enterprise_SSD_S_CAP_and_immersion_cooling_datacenter_power_efficiency","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":22.98,"MFE_90D_pct":22.98,"MFE_180D_pct":22.98,"MAE_30D_pct":-26.13,"MAE_90D_pct":-52.39,"MAE_180D_pct":-65.12,"peak_30D_date":"2024-06-11","peak_90D_date":"2024-06-11","peak_180D_date":"2024-06-11","low_30D_date":"2024-07-18","low_90D_date":"2024-08-05","low_180D_date":"2024-12-09","share_count_unique_180D":1,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|009470|Stage4B|2024-06-05","positive_or_counterexample":"positive_control_with_4B","stage4b_overlay":true,"current_profile_verdict":"missed_local_4B_if_component_route_treated_as_fresh_Yellow_after_reprice","residual_error_type":"valid_power_component_route_but_post_reprice_drawdown_guard_needed","source_url":"https://file.alphasquare.co.kr/media/pdfs/company-ir/20240605%EC%82%BC%ED%99%94%EC%A0%84%EA%B8%B0_%EA%B5%AD%EB%82%B4NDR.pdf"}
{"row_type":"trigger","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_001820_20241010_SAMHWA_CAPACITOR_MLCC_PROXY","trigger_id":"TRG_R1L123_C02_001820_20241010_04","symbol":"001820","company_name":"Samhwa Capacitor","market":"KOSPI","evidence_date":"2024-10-10","trigger_date":"2024-10-10","entry_date":"2024-10-10","entry_price":35750.0,"trigger_type":"Stage2","evidence_family":"MLCC_DC_link_capacitor_power_infrastructure_optional_route","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":3.5,"MFE_90D_pct":3.5,"MFE_180D_pct":3.5,"MAE_30D_pct":-26.29,"MAE_90D_pct":-35.24,"MAE_180D_pct":-39.86,"peak_30D_date":"2024-10-14","peak_90D_date":"2024-10-14","peak_180D_date":"2024-10-14","low_30D_date":"2024-11-21","low_90D_date":"2024-12-09","low_180D_date":"2025-04-09","share_count_unique_180D":1,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|001820|Stage2|2024-10-10","positive_or_counterexample":"counterexample","stage4b_overlay":false,"current_profile_verdict":"false_positive_if_capacitor_optional_route_promoted_before_named_customer_or_margin_bridge","residual_error_type":"component_optional_route_without_direct_grid_or_IDC_order","source_url":"https://stock.pstatic.net/stock-research/company/74/20241010_company_980241000.pdf"}
{"row_type":"trigger","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_125210_20240109_AMOGREENTECH_ESS_MAGNETIC_PROXY","trigger_id":"TRG_R1L123_C02_125210_20240109_05","symbol":"125210","company_name":"Amogreentech","market":"KOSDAQ","evidence_date":"2024-01-09","trigger_date":"2024-01-09","entry_date":"2024-01-09","entry_price":12900.0,"trigger_type":"Stage2","evidence_family":"ESS_and_high_efficiency_magnetic_material_power_conversion_proxy","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":2.79,"MFE_90D_pct":2.79,"MFE_180D_pct":2.79,"MAE_30D_pct":-20.23,"MAE_90D_pct":-24.03,"MAE_180D_pct":-48.06,"peak_30D_date":"2024-01-11","peak_90D_date":"2024-01-11","peak_180D_date":"2024-01-11","low_30D_date":"2024-02-01","low_90D_date":"2024-04-16","low_180D_date":"2024-08-05","share_count_unique_180D":1,"corporate_action_window_status":"not_contaminated","calibration_usable":true,"dedupe_for_aggregate":true,"aggregate_group_role":"representative","same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|125210|Stage2|2024-01-09","positive_or_counterexample":"counterexample","stage4b_overlay":false,"current_profile_verdict":"false_positive_if_ESS_power_material_identity_treated_as_C02_direct_CAPEX","residual_error_type":"ESS_power_component_proxy_without_grid_customer_delivery_margin","source_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1705368850173.pdf"}
```

## 6. Narrative-only / blocked rows JSONL

```jsonl
{"row_type":"narrative_only","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","case_id":"R1L123_C02_107640_20240624_HANJUNG_NCS_ESS_COOLING_NARRATIVE_ONLY","trigger_id":"TRG_R1L123_C02_107640_20240624_06_BLOCKED","symbol":"107640","company_name":"Hanjung NCS","evidence_date":"2024-05-31","entry_date":"2024-06-24","entry_price":34000.0,"trigger_type":"Stage4B","price_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":81.76,"MFE_90D_pct":81.76,"MFE_180D_pct":81.76,"MAE_30D_pct":-11.03,"MAE_90D_pct":-11.03,"MAE_180D_pct":-45.59,"share_count_unique_180D":4,"share_count_min_180D":8751446,"share_count_max_180D":9057946,"calibration_usable":false,"dedupe_for_aggregate":false,"aggregate_group_role":"blocked_narrative_only","blocked_reason":"corporate_action_or_share_count_changed_inside_180D_raw_unadjusted_window","source_url":"https://www.sks.co.kr/data1/research/qna_file/20240531071340936_0_ko.pdf","evidence_summary":"Pre-IPO research described ESS liquid-cooling components, Samsung SDI SBB reference, and the AI/power-demand tailwind. Price path had large early MFE, but share-count changes inside the 180D raw-unadjusted window block representative calibration use."}
```

## 7. Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_shadow_test","case_id":"R1L123_C02_040160_20240516_NURIFLEX_AMI_ROADMAP_PROXY","trigger_id":"TRG_R1L123_C02_040160_20240516_01","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","symbol":"040160","company_name":"NuriFlex","raw_component_scores_before":{"evidence_bridge":10,"direct_customer_order":6,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":4,"price_context_4b":8,"information_confidence":10},"raw_component_scores_after":{"evidence_bridge":5,"direct_customer_order":3,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":16,"price_context_4b":10,"information_confidence":12},"stage_label_before":"Stage2","stage_label_after":"Stage2-watch","changed_components":["direct_customer_order","backlog_capa_delivery","margin_conversion","proxy_penalty","price_context_4b"],"MFE_90D_pct":4.14,"MAE_90D_pct":-27.71,"score_return_alignment_label":"AMI_policy_rollout_without_backlog_capa_margin_bridge","current_profile_verdict":"false_positive_if_AMI_policy_language_promoted_to_C02_Actionable"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_shadow_test","case_id":"R1L123_C02_057540_20240517_OMNISYSTEM_DIGITAL_METER_PROXY","trigger_id":"TRG_R1L123_C02_057540_20240517_02","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","symbol":"057540","company_name":"OmniSystem","raw_component_scores_before":{"evidence_bridge":10,"direct_customer_order":6,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":4,"price_context_4b":8,"information_confidence":10},"raw_component_scores_after":{"evidence_bridge":5,"direct_customer_order":3,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":16,"price_context_4b":10,"information_confidence":12},"stage_label_before":"Stage2","stage_label_after":"Stage2-watch","changed_components":["direct_customer_order","backlog_capa_delivery","margin_conversion","proxy_penalty","price_context_4b"],"MFE_90D_pct":12.08,"MAE_90D_pct":-27.64,"score_return_alignment_label":"product_identity_without_customer_order_or_margin_bridge","current_profile_verdict":"false_positive_if_meter_product_identity_gets_C02_Yellow"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_shadow_test","case_id":"R1L123_C02_009470_20240605_SAMHWA_ELECTRIC_DATACENTER_CAPACITOR_LOCAL4B","trigger_id":"TRG_R1L123_C02_009470_20240605_03","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","symbol":"009470","company_name":"Samhwa Electric","raw_component_scores_before":{"evidence_bridge":10,"direct_customer_order":6,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":4,"price_context_4b":8,"information_confidence":10},"raw_component_scores_after":{"evidence_bridge":8,"direct_customer_order":8,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":8,"price_context_4b":18,"information_confidence":12},"stage_label_before":"Stage2-Actionable","stage_label_after":"Stage4B_local_profit_lock","changed_components":["direct_customer_order","backlog_capa_delivery","margin_conversion","proxy_penalty","price_context_4b"],"MFE_90D_pct":22.98,"MAE_90D_pct":-52.39,"score_return_alignment_label":"valid_power_component_route_but_post_reprice_drawdown_guard_needed","current_profile_verdict":"missed_local_4B_if_component_route_treated_as_fresh_Yellow_after_reprice"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_shadow_test","case_id":"R1L123_C02_001820_20241010_SAMHWA_CAPACITOR_MLCC_PROXY","trigger_id":"TRG_R1L123_C02_001820_20241010_04","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","symbol":"001820","company_name":"Samhwa Capacitor","raw_component_scores_before":{"evidence_bridge":10,"direct_customer_order":6,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":4,"price_context_4b":8,"information_confidence":10},"raw_component_scores_after":{"evidence_bridge":5,"direct_customer_order":3,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":16,"price_context_4b":10,"information_confidence":12},"stage_label_before":"Stage2","stage_label_after":"Stage2-watch","changed_components":["direct_customer_order","backlog_capa_delivery","margin_conversion","proxy_penalty","price_context_4b"],"MFE_90D_pct":3.5,"MAE_90D_pct":-35.24,"score_return_alignment_label":"component_optional_route_without_direct_grid_or_IDC_order","current_profile_verdict":"false_positive_if_capacitor_optional_route_promoted_before_named_customer_or_margin_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy_shadow_test","case_id":"R1L123_C02_125210_20240109_AMOGREENTECH_ESS_MAGNETIC_PROXY","trigger_id":"TRG_R1L123_C02_125210_20240109_05","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","symbol":"125210","company_name":"Amogreentech","raw_component_scores_before":{"evidence_bridge":10,"direct_customer_order":6,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":4,"price_context_4b":8,"information_confidence":10},"raw_component_scores_after":{"evidence_bridge":5,"direct_customer_order":3,"backlog_capa_delivery":5,"margin_conversion":4,"proxy_penalty":16,"price_context_4b":10,"information_confidence":12},"stage_label_before":"Stage2","stage_label_after":"Stage2-watch","changed_components":["direct_customer_order","backlog_capa_delivery","margin_conversion","proxy_penalty","price_context_4b"],"MFE_90D_pct":2.79,"MAE_90D_pct":-24.03,"score_return_alignment_label":"ESS_power_component_proxy_without_grid_customer_delivery_margin","current_profile_verdict":"false_positive_if_ESS_power_material_identity_treated_as_C02_direct_CAPEX"}
```

## 8. Aggregate / shadow rule / residual contribution JSONL

```jsonl
{"row_type":"aggregate","schema_family":"v12_stock_web_sector_archetype_residual","research_file":"e2r_stock_web_v12_residual_round_R1_loop_123_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md","selected_round":"R1","selected_loop":123,"selection_basis":"docs/core/V12_Research_No_Repeat_Index.md","selected_priority_bucket":"Priority 0 / under_30_static_ledger / C02 rows 10 need_to_30 20 before local continuation","round_schedule_status":"coverage_index_selected","round_sector_consistency":"pass","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","trigger_rows_total":5,"calibration_usable_trigger_count":5,"representative_trigger_count":5,"narrative_only_blocked_count":1,"new_independent_case_count":5,"reused_case_count":0,"same_archetype_new_symbol_count":6,"new_symbol_count":6,"same_archetype_new_trigger_family_count":6,"new_trigger_family_count":6,"positive_case_count":1,"counterexample_count":4,"stage4b_overlay_count":2,"stage4c_case_count":0,"current_profile_error_count":5,"avg_MFE_90D_pct":9.1,"avg_MAE_90D_pct":-33.4,"diversity_score_summary":"6 new symbols, 6 new trigger families, 5 representative usable rows, 1 narrative-only share-count block; hard_duplicate=0; new_independent_ratio=1.00 for usable triggers","production_scoring_changed":false,"shadow_weight_only":true,"canonical_archetype_rule_candidate":"C02_DIRECT_GRID_IDC_ORDER_BACKLOG_REQUIRED_WITH_AMI_CAPACITOR_ESS_PROXY_GUARD"}
{"row_type":"shadow_rule_candidate","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"AMI_SMART_METER_CAPACITOR_AND_ESS_COOLING_PROXY_BOUNDARY_GATE","rule_id":"C02_DIRECT_GRID_IDC_ORDER_BACKLOG_REQUIRED_WITH_AMI_CAPACITOR_ESS_PROXY_GUARD","rule_scope":"canonical_archetype_specific","rule_text":"For C02, do not promote AMI, smart-meter, capacitor, ESS cooling, power-supply, or generic power-component vocabulary above Stage2-watch unless the evidence shows named grid/datacenter customer, power-system order, backlog or shipment schedule, CAPA/lead-time lock, ASP/pricing power, and OP-margin or FCF conversion. Valid component routes can receive Stage2-Actionable only with direct customer/order and must receive local 4B/profit-lock if the price path repriced before conversion evidence.","support_trigger_ids":["TRG_R1L123_C02_040160_20240516_01","TRG_R1L123_C02_057540_20240517_02","TRG_R1L123_C02_009470_20240605_03","TRG_R1L123_C02_001820_20241010_04","TRG_R1L123_C02_125210_20240109_05"],"blocked_narrative_ids":["TRG_R1L123_C02_107640_20240624_06_BLOCKED"],"candidate_delta":"tighten C02 Stage2-Actionable/Yellow gate for AMI/capacitor/ESS-cooling proxies; add local 4B cap for valid but already repriced component route; block raw-unadjusted share-count windows","apply_now":false,"shadow_only":true,"production_scoring_changed":false}
{"row_type":"residual_contribution","round":"R1","loop":123,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","new_independent_case_count":5,"reused_case_count":0,"new_symbol_count":6,"new_trigger_family_count":6,"positive_case_count":1,"counterexample_count":4,"current_profile_error_count":5,"tested_existing_calibrated_axes":["stage2_required_bridge","stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"residual_error_types_found":["AMI_policy_rollout_without_margin_bridge","digital_meter_product_identity_overcredit","capacitor_datacenter_optional_route_overcredit","ESS_power_component_proxy_scope_leakage","valid_power_component_but_post_reprice_4B_needed","raw_unadjusted_share_count_block"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C02_DIRECT_GRID_IDC_ORDER_BACKLOG_REQUIRED_WITH_AMI_CAPACITOR_ESS_PROXY_GUARD","existing_axis_strengthened":["stage2_required_bridge","full_4b_requires_non_price_evidence","local_4b_watch_guard"],"existing_axis_weakened":null}
```

## 9. Batch-ingest self audit

```text
filename_matches_standard_v12_pattern: true
metadata_round_loop_matches_filename: true
trigger_rows_have_canonical_stage_label: true
entry_date_present: true
entry_price_positive: true
price_source_is_stock_web: true
price_basis_is_tradable_raw: true
price_adjustment_status_is_raw_unadjusted_marcap: true
all_usable_trigger_rows_have_30_90_180_MFE_MAE: true
forward_window_trading_days_gte_180_for_usable_rows: true
corporate_action_window_status_not_contaminated_for_usable_rows: true
narrative_only_rows_excluded_from_aggregate: true
large_sector_id_present: true
canonical_archetype_id_present: true
same_entry_group_id_present: true
dedupe_for_aggregate_present: true
aggregate_group_role_present: true
calibration_usable_present: true
```

## 10. Research contribution summary

This loop adds **5 usable new independent C02 cases**, **4 counterexamples**, **1 positive/4B component-route control**, and **5 residual errors** for `R1 / L1_INDUSTRIALS_INFRA_DEFENSE_GRID / C02_POWER_GRID_DATACENTER_CAPEX`.

```text
new_independent_case_count: 5
reused_case_count: 0
new_symbol_count: 6
same_archetype_new_symbol_count: 6
same_archetype_new_trigger_family_count: 6
new_trigger_family_count: 6
positive_case_count: 1
counterexample_count: 4
current_profile_error_count: 5
diversity_score_summary: 6 symbols, 6 trigger families, 5 usable representative rows, 1 narrative-only share-count block; hard_duplicate=0; new_independent_ratio=1.00 for usable triggers
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying v12 research MDs later:
1. Ingest this file only if filename and metadata match the v12 regex.
2. Use only row_type="trigger" rows with calibration_usable=true for aggregate/weight calculations.
3. Keep row_type="narrative_only" rows out of representative aggregate metrics.
4. Preserve the canonical rule candidate:
   C02_DIRECT_GRID_IDC_ORDER_BACKLOG_REQUIRED_WITH_AMI_CAPACITOR_ESS_PROXY_GUARD
5. For C02, tighten Stage2-Actionable/Yellow promotion when evidence is only AMI/smart-meter/capacitor/ESS-cooling/power-component vocabulary.
6. Require named grid/datacenter customer, power-system order, backlog or delivery schedule, CAPA/lead-time lock, ASP/pricing power, and OP margin/FCF conversion before full C02 rerating credit.
7. Add local 4B/profit-lock overlay when a valid component route has already repriced before margin conversion evidence.
8. Block representative calibration when stock-web raw-unadjusted share-count changes inside the 180D window.
```

## 12. Next research state

```text
completed_round: R1
completed_loop: 123
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_static_ledger / C02 rows 10 need_to_30 20 before local continuation
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_followup_after_shard_recheck
  - C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_utilization_regime
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_new_symbols_only
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION_if_more_share_count_or_proxy_blocks_accumulate
```
