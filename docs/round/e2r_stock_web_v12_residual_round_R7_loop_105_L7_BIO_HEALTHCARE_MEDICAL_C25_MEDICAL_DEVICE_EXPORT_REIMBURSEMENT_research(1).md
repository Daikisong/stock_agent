# E2R Stock-Web V12 Residual Research — R7 loop 105 — C25 Medical Device Export/Reimbursement

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R7_loop_105_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
selected_round: R7
selected_loop: 105
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5
deep_sub_archetype_id: C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 2 quality_repair_after_local_priority0_priority1_fill
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Execution boundary

This is not a live scan, recommendation list, brokerage/API task, or stock_agent code patch. The only output is this standalone historical calibration Markdown file. The selected scope is C25 because the published No-Repeat Index already puts C25 in Priority 2, but with an unusually weak positive/counterexample balance and explicit guidance that 50+ row scopes should be used for URL/proxy repair, failure-mode repair, 4B/4C balance, and quality repair rather than simple minimum coverage filling.

The current local session already generated C25 loop101, loop103, and loop104 summaries. This loop105 avoids the visible symbol groups from those outputs where possible and focuses on diagnostic/dental/X-ray/biomaterial device label spikes versus verified export/reimbursement/procedure-volume bridge.

## 2. Stock-Web manifest and price validation

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All trigger rows below use 2024~2025 tradable shards. Every row has a full 30D/90D/180D MFE/MAE path and an available 180 trading-row forward window ending before the manifest max date. Corporate-action candidate dates were checked from symbol profiles where available; no listed candidate date overlaps each row's entry_date~D+180 window. Because the non-price evidence is intentionally marked source_proxy_only, the rows are calibration price-path usable but promotion blocked until URL repair.

## 3. Residual thesis

C25 should not treat “medical device,” “diagnostic export,” “dental implant,” or “reimbursement” labels as enough for Stage2-Actionable or Stage3-Yellow. The residual pattern is surgical: when there is a visible bridge from device demand to procedure volume, reimbursement/export acceptance, revenue conversion, and margin durability, the price path can reward the entry with limited MAE. When that bridge is absent, the same label becomes a glass door: it looks like evidence until the first drawdown walks through it.

Proposed shadow rule:

```text
C25_verified_export_reimbursement_procedure_volume_revenue_margin_bridge_required_before_Yellow_or_Green_plus_device_label_to_local_4B_or_4C_watch_v5
```

## 4. Trigger summary table

| row_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | label | usable |
|---|---:|---|---|---|---|---:|---:|---:|---:|---:|---|---|
| C25_L105_T01 | 206640 | 바디텍메드 | Stage2-Actionable | 2024-03-15 | 2024-03-15 | 14510 | 34.87 | -7.65 | 45.07 | -7.99 | positive | true |
| C25_L105_T02 | 039840 | 디오 | Stage2-Actionable | 2024-08-16 | 2024-08-16 | 15920 | 12.12 | -3.45 | 33.17 | -4.96 | positive | true |
| C25_L105_T03 | 335810 | 프리시젼바이오 | Stage3-Yellow | 2024-09-20 | 2024-09-20 | 3120 | 82.69 | -16.67 | 82.69 | -22.12 | positive_high_volatility | true |
| C25_L105_T04 | 042520 | 한스바이오메드 | Stage2-Actionable | 2024-11-15 | 2024-11-15 | 6620 | 40.33 | -1.81 | 60.12 | -6.65 | positive | true |
| C25_L105_T05 | 043150 | 바텍 | Stage2 | 2024-04-15 | 2024-04-15 | 29750 | 3.03 | -22.52 | 3.03 | -37.04 | counterexample | true |
| C25_L105_T06 | 263690 | 디알젬 | Stage2 | 2024-06-17 | 2024-06-17 | 8990 | 0.00 | -25.47 | 0.00 | -42.83 | counterexample_4C | true |
| C25_L105_T07 | 049180 | 셀루메드 | Stage4B | 2024-10-21 | 2024-10-21 | 3625 | 1.79 | -58.79 | 1.79 | -76.55 | counterexample_4C | true |
| C25_L105_T08 | 950130 | 엑세스바이오 | Stage4B | 2024-08-16 | 2024-08-16 | 8970 | 23.75 | -45.15 | 23.75 | -51.17 | counterexample_high_MAE | true |

## 5. Machine-readable trigger rows JSONL

```jsonl
{"row_id":"C25_L105_T01","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"206640","company_name":"바디텍메드","trigger_date":"2024-03-15","trigger_type":"Stage2-Actionable","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-03-15","entry_price":14510.0,"entry_close":14130.0,"MFE_30D_pct":11.99,"MAE_30D_pct":-7.65,"MFE_90D_pct":34.87,"MAE_90D_pct":-7.65,"MFE_180D_pct":45.07,"MAE_180D_pct":-7.99,"peak_180D_price":21050.0,"peak_180D_date":"2024-08-19","trough_180D_price":13350.0,"trough_180D_date":"2024-10-22","forward_window_end_180D":"2024-12-09","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/206/206640/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/206/206640/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/206/206640.json","profile_corporate_action_candidate_dates":["2015-09-11","2016-02-12"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"positive","evidence_family":"POCT export revenue/margin bridge proxy","trigger_family":"poct_export_margin_bridge","fine_case":"diagnostic export revenue/margin bridge held despite sector label fatigue","diagnosis":"verified bridge candidate: price path rewarded low-MAE entry once diagnostic export/revenue proxy was present","raw_component_score_breakdown":{"rerating_evidence":18,"revision_visibility":13,"margin_fcf_bridge":15,"customer_reimbursement_quality":14,"valuation_risk_control":9,"price_path_alignment":16,"red_team_penalty":-4},"simulated_total_score":81,"current_profile_expected_error":false}
{"row_id":"C25_L105_T02","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"039840","company_name":"디오","trigger_date":"2024-08-16","trigger_type":"Stage2-Actionable","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-08-16","entry_price":15920.0,"entry_close":16000.0,"MFE_30D_pct":12.12,"MAE_30D_pct":-2.32,"MFE_90D_pct":12.12,"MAE_90D_pct":-3.45,"MFE_180D_pct":33.17,"MAE_180D_pct":-4.96,"peak_180D_price":21200.0,"peak_180D_date":"2025-05-14","trough_180D_price":15130.0,"trough_180D_date":"2025-03-11","forward_window_end_180D":"2025-05-19","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/039/039840/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/039/039840/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/039/039840.json","profile_corporate_action_candidate_dates":["2015-09-04"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"positive","evidence_family":"dental implant sell-through margin recovery proxy","trigger_family":"dental_implant_export_recovery_bridge","fine_case":"dental implant recovery entry after de-rating; low MAE and delayed 180D follow-through","diagnosis":"positive but slow: 30/90D did not prove the thesis, 180D did; avoid premature 4B if drawdown remains shallow","raw_component_score_breakdown":{"rerating_evidence":16,"revision_visibility":11,"margin_fcf_bridge":13,"customer_reimbursement_quality":12,"valuation_risk_control":12,"price_path_alignment":14,"red_team_penalty":-3},"simulated_total_score":75,"current_profile_expected_error":false}
{"row_id":"C25_L105_T03","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"335810","company_name":"프리시젼바이오","trigger_date":"2024-09-20","trigger_type":"Stage3-Yellow","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-09-20","entry_price":3120.0,"entry_close":3200.0,"MFE_30D_pct":82.69,"MAE_30D_pct":0.0,"MFE_90D_pct":82.69,"MAE_90D_pct":-16.67,"MFE_180D_pct":82.69,"MAE_180D_pct":-22.12,"peak_180D_price":5700.0,"peak_180D_date":"2024-10-07","trough_180D_price":2430.0,"trough_180D_date":"2025-05-08","forward_window_end_180D":"2025-06-20","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/335/335810/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/335/335810/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/335/335810.json","profile_corporate_action_candidate_dates":["2025-11-20"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"positive_high_volatility","evidence_family":"POCT diagnostic event spike with short bridge proxy","trigger_family":"diagnostic_event_spike_high_MAE_filter","fine_case":"large MFE but subsequent 90/180D MAE shows event spike must not become clean Green without revenue bridge","diagnosis":"positive-MFE / bad-entry hybrid: Stage3-Yellow may be allowed only with high-MAE guard, not clean Green","raw_component_score_breakdown":{"rerating_evidence":18,"revision_visibility":8,"margin_fcf_bridge":8,"customer_reimbursement_quality":9,"valuation_risk_control":4,"price_path_alignment":12,"red_team_penalty":-12},"simulated_total_score":47,"current_profile_expected_error":true}
{"row_id":"C25_L105_T04","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"042520","company_name":"한스바이오메드","trigger_date":"2024-11-15","trigger_type":"Stage2-Actionable","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-11-15","entry_price":6620.0,"entry_close":7140.0,"MFE_30D_pct":40.33,"MAE_30D_pct":-1.81,"MFE_90D_pct":40.33,"MAE_90D_pct":-1.81,"MFE_180D_pct":60.12,"MAE_180D_pct":-6.65,"peak_180D_price":10600.0,"peak_180D_date":"2025-06-11","trough_180D_price":6180.0,"trough_180D_date":"2025-04-09","forward_window_end_180D":"2025-08-12","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/042/042520/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/042/042520/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/042/042520.json","profile_corporate_action_candidate_dates":[],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"positive","evidence_family":"biomaterial/aesthetic implant export recovery proxy","trigger_family":"biomaterial_recovery_low_MAE_bridge","fine_case":"late-2024 washed-out biomaterial device entry with low MAE and strong 180D recovery","diagnosis":"positive recovery exception: label spike risk was low because entry followed collapse and MAE stayed shallow","raw_component_score_breakdown":{"rerating_evidence":15,"revision_visibility":10,"margin_fcf_bridge":12,"customer_reimbursement_quality":11,"valuation_risk_control":14,"price_path_alignment":17,"red_team_penalty":-3},"simulated_total_score":76,"current_profile_expected_error":false}
{"row_id":"C25_L105_T05","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"043150","company_name":"바텍","trigger_date":"2024-04-15","trigger_type":"Stage2","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-04-15","entry_price":29750.0,"entry_close":29500.0,"MFE_30D_pct":3.03,"MAE_30D_pct":-4.2,"MFE_90D_pct":3.03,"MAE_90D_pct":-22.52,"MFE_180D_pct":3.03,"MAE_180D_pct":-37.04,"peak_180D_price":30650.0,"peak_180D_date":"2024-05-08","trough_180D_price":18730.0,"trough_180D_date":"2024-12-27","forward_window_end_180D":"2025-01-09","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/043/043150/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/043/043150.json","profile_corporate_action_candidate_dates":["2010-09-02"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"counterexample","evidence_family":"dental imaging export label without margin bridge","trigger_family":"dental_imaging_label_no_bridge_false_positive","fine_case":"device/export label looked stable but price path showed persistent 90/180D drawdown without MFE","diagnosis":"false positive: Stage2 should require export/reimbursement/procedure-volume bridge before Actionable","raw_component_score_breakdown":{"rerating_evidence":12,"revision_visibility":5,"margin_fcf_bridge":4,"customer_reimbursement_quality":7,"valuation_risk_control":5,"price_path_alignment":2,"red_team_penalty":-16},"simulated_total_score":19,"current_profile_expected_error":true}
{"row_id":"C25_L105_T06","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"263690","company_name":"디알젬","trigger_date":"2024-06-17","trigger_type":"Stage2","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-06-17","entry_price":8990.0,"entry_close":8800.0,"MFE_30D_pct":0.0,"MAE_30D_pct":-10.68,"MFE_90D_pct":0.0,"MAE_90D_pct":-25.47,"MFE_180D_pct":0.0,"MAE_180D_pct":-42.83,"peak_180D_price":8990.0,"peak_180D_date":"2024-06-17","trough_180D_price":5140.0,"trough_180D_date":"2024-11-15","forward_window_end_180D":"2025-03-14","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/263/263690/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/263/263690/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/263/263690.json","profile_corporate_action_candidate_dates":[],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"counterexample_4C","evidence_family":"X-ray device export label without demand pull","trigger_family":"xray_export_label_hard_4c","fine_case":"entry never produced positive MFE and fell into sustained 180D drawdown","diagnosis":"hard 4C candidate: no non-price bridge plus zero MFE over 180D means device label should fail fast","raw_component_score_breakdown":{"rerating_evidence":10,"revision_visibility":4,"margin_fcf_bridge":3,"customer_reimbursement_quality":6,"valuation_risk_control":6,"price_path_alignment":0,"red_team_penalty":-20},"simulated_total_score":9,"current_profile_expected_error":true}
{"row_id":"C25_L105_T07","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"049180","company_name":"셀루메드","trigger_date":"2024-10-21","trigger_type":"Stage4B","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-10-21","entry_price":3625.0,"entry_close":3590.0,"MFE_30D_pct":1.79,"MAE_30D_pct":-41.79,"MFE_90D_pct":1.79,"MAE_90D_pct":-58.79,"MFE_180D_pct":1.79,"MAE_180D_pct":-76.55,"peak_180D_price":3690.0,"peak_180D_date":"2024-10-21","trough_180D_price":850.0,"trough_180D_date":"2025-05-20","forward_window_end_180D":"2025-07-16","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/049/049180/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/049/049180/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/049/049180.json","profile_corporate_action_candidate_dates":["2005-03-04","2005-08-02","2006-07-05","2007-05-21","2007-06-18","2008-09-03","2009-08-27","2009-11-19","2010-02-22","2010-10-21","2013-05-27","2016-03-04","2017-05-25","2021-03-26","2026-02-10"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"counterexample_4C","evidence_family":"biomaterial/medical device label after price spike","trigger_family":"biomaterial_label_spike_to_4c","fine_case":"prior spike left no support; local 4B should route to hard 4C once bridge remains absent","diagnosis":"strong hard-4C route: near-zero MFE and -76.55% 180D MAE after label spike","raw_component_score_breakdown":{"rerating_evidence":9,"revision_visibility":2,"margin_fcf_bridge":2,"customer_reimbursement_quality":4,"valuation_risk_control":1,"price_path_alignment":0,"red_team_penalty":-24},"simulated_total_score":-6,"current_profile_expected_error":true}
{"row_id":"C25_L105_T08","round":"R7","loop":105,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"C25_DIAGNOSTIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_V5","deep_sub_archetype_id":"C25_DEEP_DIAGNOSTIC_DENTAL_XRAY_BIOMATERIAL_DEVICE_PROCEDURE_VOLUME_VS_LABEL_SPIKE","symbol":"950130","company_name":"엑세스바이오","trigger_date":"2024-08-16","trigger_type":"Stage4B","entry_rule":"trigger-day open from tradable shard; if trigger date is non-trading, next tradable open","entry_date":"2024-08-16","entry_price":8970.0,"entry_close":9410.0,"MFE_30D_pct":23.75,"MAE_30D_pct":-31.66,"MFE_90D_pct":23.75,"MAE_90D_pct":-45.15,"MFE_180D_pct":23.75,"MAE_180D_pct":-51.17,"peak_180D_price":11100.0,"peak_180D_date":"2024-08-19","trough_180D_price":4380.0,"trough_180D_date":"2025-04-07","forward_window_end_180D":"2025-05-19","forward_trading_rows_180D":180,"price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","price_shard_urls":["https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/950/950130/2024.csv","https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/ohlcv_tradable_by_symbol_year/950/950130/2025.csv"],"profile_url":"https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/symbol_profiles/950/950130.json","profile_corporate_action_candidate_dates":["2019-09-09"],"corporate_action_overlap_180D":false,"calibration_usable":true,"promotion_usable":false,"promotion_blocked_reason":"source_proxy_only/evidence_url_pending; price path usable but non-price evidence URL repair required","source_proxy_only":true,"evidence_url_pending":true,"case_label":"counterexample_high_MAE","evidence_family":"diagnostic export/COVID legacy label spike","trigger_family":"diagnostic_label_spike_high_MAE_watch","fine_case":"front-loaded MFE existed but was swamped by -45%/-51% MAE; not a clean positive case","diagnosis":"local 4B/high-MAE guard: MFE alone would mislead, MAE path demands source/procedure-volume bridge","raw_component_score_breakdown":{"rerating_evidence":13,"revision_visibility":4,"margin_fcf_bridge":4,"customer_reimbursement_quality":6,"valuation_risk_control":3,"price_path_alignment":5,"red_team_penalty":-18},"simulated_total_score":17,"current_profile_expected_error":true}
```

## 6. Score simulation rows JSONL

```jsonl
{"row_id":"C25_L105_T01","symbol":"206640","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"rerating_evidence":18,"revision_visibility":13,"margin_fcf_bridge":15,"customer_reimbursement_quality":14,"valuation_risk_control":9,"price_path_alignment":16,"red_team_penalty":-4},"simulated_total_score":81,"calibrated_profile_stress_result":"acceptable_if_bridge_URL_repaired","recommended_stage_route":"Stage2-Actionable_or_Yellow_after_URL_repair"}
{"row_id":"C25_L105_T02","symbol":"039840","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"rerating_evidence":16,"revision_visibility":11,"margin_fcf_bridge":13,"customer_reimbursement_quality":12,"valuation_risk_control":12,"price_path_alignment":14,"red_team_penalty":-3},"simulated_total_score":75,"calibrated_profile_stress_result":"acceptable_if_bridge_URL_repaired","recommended_stage_route":"Stage2-Actionable_or_Yellow_after_URL_repair"}
{"row_id":"C25_L105_T03","symbol":"335810","trigger_type":"Stage3-Yellow","raw_component_score_breakdown":{"rerating_evidence":18,"revision_visibility":8,"margin_fcf_bridge":8,"customer_reimbursement_quality":9,"valuation_risk_control":4,"price_path_alignment":12,"red_team_penalty":-12},"simulated_total_score":47,"calibrated_profile_stress_result":"false_positive_or_high_MAE_guard_needed","recommended_stage_route":"Stage3-Yellow_with_high_MAE_guard"}
{"row_id":"C25_L105_T04","symbol":"042520","trigger_type":"Stage2-Actionable","raw_component_score_breakdown":{"rerating_evidence":15,"revision_visibility":10,"margin_fcf_bridge":12,"customer_reimbursement_quality":11,"valuation_risk_control":14,"price_path_alignment":17,"red_team_penalty":-3},"simulated_total_score":76,"calibrated_profile_stress_result":"acceptable_if_bridge_URL_repaired","recommended_stage_route":"Stage2-Actionable_or_Yellow_after_URL_repair"}
{"row_id":"C25_L105_T05","symbol":"043150","trigger_type":"Stage2","raw_component_score_breakdown":{"rerating_evidence":12,"revision_visibility":5,"margin_fcf_bridge":4,"customer_reimbursement_quality":7,"valuation_risk_control":5,"price_path_alignment":2,"red_team_penalty":-16},"simulated_total_score":19,"calibrated_profile_stress_result":"false_positive_or_high_MAE_guard_needed","recommended_stage_route":"local_4B_or_4C_watch"}
{"row_id":"C25_L105_T06","symbol":"263690","trigger_type":"Stage2","raw_component_score_breakdown":{"rerating_evidence":10,"revision_visibility":4,"margin_fcf_bridge":3,"customer_reimbursement_quality":6,"valuation_risk_control":6,"price_path_alignment":0,"red_team_penalty":-20},"simulated_total_score":9,"calibrated_profile_stress_result":"false_positive_or_high_MAE_guard_needed","recommended_stage_route":"local_4B_or_4C_watch"}
{"row_id":"C25_L105_T07","symbol":"049180","trigger_type":"Stage4B","raw_component_score_breakdown":{"rerating_evidence":9,"revision_visibility":2,"margin_fcf_bridge":2,"customer_reimbursement_quality":4,"valuation_risk_control":1,"price_path_alignment":0,"red_team_penalty":-24},"simulated_total_score":-6,"calibrated_profile_stress_result":"false_positive_or_high_MAE_guard_needed","recommended_stage_route":"local_4B_or_4C_watch"}
{"row_id":"C25_L105_T08","symbol":"950130","trigger_type":"Stage4B","raw_component_score_breakdown":{"rerating_evidence":13,"revision_visibility":4,"margin_fcf_bridge":4,"customer_reimbursement_quality":6,"valuation_risk_control":3,"price_path_alignment":5,"red_team_penalty":-18},"simulated_total_score":17,"calibrated_profile_stress_result":"false_positive_or_high_MAE_guard_needed","recommended_stage_route":"local_4B_or_4C_watch"}
```

## 7. Aggregate JSON

```json
{
  "row_type": "v12_aggregate",
  "round": "R7",
  "loop": 105,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "trigger_row_count": 8,
  "calibration_usable_trigger_count": 8,
  "representative_trigger_count": 8,
  "new_independent_case_count": 8,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 8,
  "same_archetype_new_trigger_family_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_case_count": 5,
  "stage4c_case_count": 3,
  "current_profile_error_count": 5,
  "source_proxy_only_count": 8,
  "evidence_url_pending_count": 8,
  "promotion_blocked_until_url_repair": true,
  "residual_contribution_label": "canonical_archetype_rule_candidate",
  "new_axis_proposed": "C25_verified_export_reimbursement_procedure_volume_revenue_margin_bridge_required_before_Yellow_or_Green_plus_device_label_to_local_4B_or_4C_watch_v5",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "hard_4c_confirmation",
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": []
}
```

## 8. Positive vs counterexample readout

Positive rows are not simply rows with large MFE. They are rows where MFE arrived without intolerable MAE and where a plausible bridge exists from the device label to revenue/procedure-volume/reimbursement behavior. Counterexamples are rows where label-only evidence produced either no MFE or an unacceptable drawdown sequence.

- Positive bridge candidates: 바디텍메드, 디오, 프리시젼바이오, 한스바이오메드.
- Counterexample / 4B·4C watch candidates: 바텍, 디알젬, 셀루메드, 엑세스바이오.
- Important hybrid: 프리시젼바이오 delivered +82.69% MFE but also moved into -22.12% 180D MAE after the event. That should count as a positive-MFE/high-MAE warning, not a clean Green unlock.

## 9. Local 4B vs full 4B split

```text
local_4B_watch = device/export/reimbursement label spike without verified procedure-volume, revenue, or margin bridge
full_4B = confirmed non-price bridge deterioration plus failed price path
hard_4C = zero or near-zero MFE with deep MAE after the bridge is absent or broken
```

C25 loop105 strengthens the rule that local 4B can be raised by price path + weak evidence, but full 4B/4C needs non-price bridge failure. 셀루메드 and 디알젬 are the cleanest hard-4C candidates in this loop because the price path does not merely retrace; it never confirms the medical device label as a rerating bridge.

## 10. Validation scope

```text
calibration_usable_trigger_count = 8
representative_trigger_count = 8
trigger_rows_missing_required_price_fields = 0
corporate_action_overlap_180D_count = 0
source_proxy_only_count = 8
evidence_url_pending_count = 8
promotion_usable_count = 0
promotion_blocked_until_url_repair = true
```

## 11. Residual contribution summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

This loop adds quality-repair evidence rather than minimum-coverage evidence. Its purpose is to distinguish three C25 routes:

1. true bridge: procedure/reimbursement/export demand appears in price path with shallow MAE;
2. event bridge: high MFE appears, but high MAE demands a guardrail;
3. label-only failure: medical-device wording produces no durable path and should route to local 4B or hard 4C.

## 12. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not run this handoff during research collection. When batch applying V12 research artifacts, ingest this MD as a standalone C25 residual calibration candidate. Parse all JSONL trigger rows, confirm required MFE/MAE fields, validate that source_proxy_only rows remain promotion-blocked until URL repair, and only then consider the shadow rule:
C25_verified_export_reimbursement_procedure_volume_revenue_margin_bridge_required_before_Yellow_or_Green_plus_device_label_to_local_4B_or_4C_watch_v5.
Do not loosen global Stage3-Green thresholds. Do not change production scoring directly from this single file. Treat this as one C25-specific evidence packet for batch aggregation.
```

## 13. Next research state

```text
completed_round = R7
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C22_INSURANCE_RATE_CYCLE_RESERVE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN, C24_BIO_TRIAL_DATA_EVENT_RISK, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
