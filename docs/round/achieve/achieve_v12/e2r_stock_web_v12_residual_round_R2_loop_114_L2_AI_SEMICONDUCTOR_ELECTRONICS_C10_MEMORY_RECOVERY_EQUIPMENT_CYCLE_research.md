---
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_type: stock_web_v12_sector_archetype_residual_calibration_md
selected_round: R2
selected_loop: 114
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: C10_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE
selected_priority_bucket: Priority 1-under-50 after local-session adjustment; published index Priority 0
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: '2026-02-20'
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web V12 Residual Research — R2 / C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE / loop 114

## 0. Execution stance

This is a standalone historical calibration research file. It is **not** a live watchlist, not a recommendation file, not an automatic trading plan, and not a `stock_agent` production patch. The only purpose is to add non-duplicative C10 residual cases for later batch ingestion and review.

The selected canonical is `C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`. The published No-Repeat Index still lists C10 as Priority 0 with 13 rows and a 37-row need to the 50-row practical calibration band. In this same session, local C10 loops 109–113 were already generated, lifting the local-session adjusted count to roughly 43. This loop adds 7 representative C10 triggers and locally reaches the 50-row practical band.

## 1. Stock-Web atlas validation scope

| item | value |
|---|---|
| primary price source | `Songdaiki/stock-web` |
| upstream source | `FinanceData/marcap` |
| price basis | `tradable_raw` |
| price adjustment | `raw_unadjusted_marcap` |
| calibration shard root | `atlas/ohlcv_tradable_by_symbol_year` |
| manifest max date | `2026-02-20` |
| forward-window rule | 30D / 90D / 180D, bounded by manifest max date |
| entry price convention | close on `entry_date`; MFE/MAE use future high/low over the next N trading days, excluding the entry row |
| corporate-action rule | profile candidate dates inside entry~D+180 block promotion use |

Stock-Web yearly tradable shards were used for 2023–2025 as needed. Symbol profiles were checked for corporate-action candidate dates. No selected case has a candidate date inside its entry~D+180 window. All price-path fields below are calculated from `tradable_raw` OHLC rows.

## 2. Novelty and duplicate guard

Hard duplicate key avoided:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Prior local C10 loops avoided:

```text
R2/C10 loop109
R2/C10 loop110
R2/C10 loop111
R2/C10 loop112
R2/C10 loop113
```

Known prior C10 loop113 symbols avoided where possible: `089890`, `160980`, `322310`, `357780`, `089030`, `092870`, `036540`. This loop uses a different memory-cycle mix: precursor/material recovery, cleaning/wafer-transfer fade, thermal/chiller control, AFM/metrology, OSAT test beta, and package-substrate fade.

## 3. Case table

| case_id | symbol | name | trigger_type | entry_date | entry_price | path_class | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | local_4B | current_profile_error |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|
| C10-L114-01 | 092070 | 디엔에프 | Stage2-Actionable | 2023-05-04 | 16,400 | positive structural recovery | 6.3 | 75.9 | 75.9 | -8.0 | -8.0 | -8.0 | false | too_late_to_yellow |
| C10-L114-02 | 079370 | 제우스 | Stage3-Yellow | 2024-03-15 | 19,350 | counterexample / post-split RS fade | 9.3 | 9.3 | 9.3 | -18.3 | -30.1 | -47.2 | true | false_positive_yellow |
| C10-L114-03 | 281740 | 레이크머티리얼즈 | Stage2-Actionable | 2024-02-06 | 16,480 | positive material bridge with volatility | 100.8 | 100.8 | 100.8 | -4.5 | -4.5 | -19.4 | false | missed_actionable_bonus |
| C10-L114-04 | 036810 | 에프에스티 | Stage3-Yellow | 2024-05-03 | 31,150 | positive pop then hard drawdown | 34.3 | 34.3 | 34.3 | -6.6 | -28.4 | -54.4 | true | full_green_risk_after_local_blowoff |
| C10-L114-05 | 140860 | 파크시스템스 | Stage2-Actionable | 2023-10-20 | 148,700 | positive metrology bridge | 17.3 | 31.1 | 33.6 | -6.5 | -6.5 | -6.5 | false | too_conservative_stage2 |
| C10-L114-06 | 200470 | 에이팩트 | Stage3-Yellow | 2024-02-16 | 3,795 | blowoff positive MFE with high-MAE reversal | 81.3 | 91.0 | 91.0 | -1.6 | -1.6 | -39.1 | true | green_without_quality_bridge |
| C10-L114-07 | 195870 | 해성디에스 | Stage3-Yellow | 2023-07-24 | 69,100 | counterexample package-substrate fade | 16.4 | 16.4 | 16.4 | -13.5 | -37.8 | -37.8 | true | false_positive_yellow |

## 4. Price-path notes

- `092070 / 디엔에프`: Stage2-Actionable would have looked timid on 30D MFE, but 90D/180D MFE reached 75.9% with only -8.0% MAE. This is a missed structural C10 bridge candidate.
- `079370 / 제우스`: after a post-split memory-equipment RS move, 180D MFE stayed 9.3% while MAE expanded to -47.2%. This is a clean local-4B/watch counterexample.
- `281740 / 레이크머티리얼즈`: a very strong MFE path, but with material-cycle volatility. It supports Stage2-Actionable only when material/order/revenue bridge is explicit.
- `036810 / 에프에스티`: 34.3% MFE arrived quickly, then the same window suffered -54.4% MAE. The correct behavior is not full Green; it is local 4B watch after the local blowoff unless the non-price bridge keeps strengthening.
- `140860 / 파크시스템스`: lower drawdown, controlled MFE path. This is the cleanest positive control in this loop.
- `200470 / 에이팩트`: enormous MFE but also -39.1% MAE by 180D. This is the classic C10 memory-beta trap: price can reward early, but unverified margin/revenue bridge should prevent durable Green.
- `195870 / 해성디에스`: package-substrate recovery label failed to hold, with 180D MAE -37.8% and only 16.4% MFE.

## 5. Trigger rows JSONL

```jsonl
{"row_type":"trigger","case_id":"C10-L114-01","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_PRECURSOR_MATERIAL_ORDER_REVENUE_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"092070","name":"디엔에프","trigger_type":"Stage2-Actionable","trigger_date":"2023-05-03","entry_date":"2023-05-04","entry_price":16400,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":6.3,"MFE_90D_pct":75.9,"MFE_180D_pct":75.9,"MAE_30D_pct":-8.0,"MAE_90D_pct":-8.0,"MAE_180D_pct":-8.0,"peak_return_pct":75.9,"max_drawdown_pct":-8.0,"peak_date":"2023-08-09","trough_date":"2023-05-16","score_return_alignment":"positive_missed_structural","current_profile_error":"too_late_to_yellow","local_4b_watch_flag":false,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":66,"margin_fcf_bridge":54,"revision_bridge":47,"customer_capacity_visibility":42,"valuation_risk_inverse":58,"price_only_risk":18,"information_confidence":61},"evidence_family":"memory_precursor_material_recovery_order_revenue_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"2007-11-27, 2008-04-08, 2011-12-13; no overlap with entry~D+180","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|092070|Stage2-Actionable|2023-05-04"}
{"row_type":"trigger","case_id":"C10-L114-02","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_CLEANING_WAFER_TRANSFER_RS_FADE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"079370","name":"제우스","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-14","entry_date":"2024-03-15","entry_price":19350,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":9.3,"MFE_90D_pct":9.3,"MFE_180D_pct":9.3,"MAE_30D_pct":-18.3,"MAE_90D_pct":-30.1,"MAE_180D_pct":-47.2,"peak_return_pct":9.3,"max_drawdown_pct":-47.2,"peak_date":"2024-03-21","trough_date":"2024-12-09","score_return_alignment":"false_positive_yellow","current_profile_error":"false_positive_yellow","local_4b_watch_flag":true,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":35,"margin_fcf_bridge":29,"revision_bridge":32,"customer_capacity_visibility":31,"valuation_risk_inverse":24,"price_only_risk":82,"information_confidence":44},"evidence_family":"cleaning_wafer_transfer_relative_strength_fade_without_order_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"2024-01-16, 2024-02-08; before entry, no overlap with entry~D+180","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|079370|Stage3-Yellow|2024-03-15"}
{"row_type":"trigger","case_id":"C10-L114-03","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_PRECURSOR_MATERIAL_MEMORY_RECOVERY_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"281740","name":"레이크머티리얼즈","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-05","entry_date":"2024-02-06","entry_price":16480,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":100.8,"MFE_90D_pct":100.8,"MFE_180D_pct":100.8,"MAE_30D_pct":-4.5,"MAE_90D_pct":-4.5,"MAE_180D_pct":-19.4,"peak_return_pct":100.8,"max_drawdown_pct":-19.4,"peak_date":"2024-03-11","trough_date":"2024-08-05","score_return_alignment":"positive_actionable_but_volatility_watch","current_profile_error":"missed_actionable_bonus","local_4b_watch_flag":false,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":63,"margin_fcf_bridge":48,"revision_bridge":45,"customer_capacity_visibility":40,"valuation_risk_inverse":39,"price_only_risk":55,"information_confidence":58},"evidence_family":"precursor_material_memory_recovery_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"2020-03-23; no overlap with entry~D+180","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|281740|Stage2-Actionable|2024-02-06"}
{"row_type":"trigger","case_id":"C10-L114-04","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_EUV_CHILLER_AND_THERMAL_CONTROL_MEMORY_CAPEX_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"036810","name":"에프에스티","trigger_type":"Stage3-Yellow","trigger_date":"2024-05-02","entry_date":"2024-05-03","entry_price":31150,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":34.3,"MFE_90D_pct":34.3,"MFE_180D_pct":34.3,"MAE_30D_pct":-6.6,"MAE_90D_pct":-28.4,"MAE_180D_pct":-54.4,"peak_return_pct":34.3,"max_drawdown_pct":-54.4,"peak_date":"2024-06-11","trough_date":"2024-12-09","score_return_alignment":"positive_peak_but_full_window_4b_watch","current_profile_error":"full_green_risk_after_local_blowoff","local_4b_watch_flag":true,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":54,"margin_fcf_bridge":39,"revision_bridge":41,"customer_capacity_visibility":37,"valuation_risk_inverse":31,"price_only_risk":67,"information_confidence":52},"evidence_family":"euv_chiller_thermal_control_memory_capex_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"2000-05-02, 2004-06-17; no overlap with entry~D+180","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|036810|Stage3-Yellow|2024-05-03"}
{"row_type":"trigger","case_id":"C10-L114-05","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_AFM_METROLOGY_MEMORY_PROCESS_CONTROL_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"140860","name":"파크시스템스","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-19","entry_date":"2023-10-20","entry_price":148700,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":17.3,"MFE_90D_pct":31.1,"MFE_180D_pct":33.6,"MAE_30D_pct":-6.5,"MAE_90D_pct":-6.5,"MAE_180D_pct":-6.5,"peak_return_pct":33.6,"max_drawdown_pct":-6.5,"peak_date":"2024-07-04","trough_date":"2023-10-31","score_return_alignment":"positive_actionable","current_profile_error":"too_conservative_stage2","local_4b_watch_flag":false,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":68,"margin_fcf_bridge":61,"revision_bridge":52,"customer_capacity_visibility":46,"valuation_risk_inverse":51,"price_only_risk":23,"information_confidence":66},"evidence_family":"afm_metrology_process_control_revenue_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"none","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|140860|Stage2-Actionable|2023-10-20"}
{"row_type":"trigger","case_id":"C10-L114-06","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_OSAT_MEMORY_TEST_BETA_WITHOUT_MARGIN_BRIDGE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"200470","name":"에이팩트","trigger_type":"Stage3-Yellow","trigger_date":"2024-02-15","entry_date":"2024-02-16","entry_price":3795,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":81.3,"MFE_90D_pct":91.0,"MFE_180D_pct":91.0,"MAE_30D_pct":-1.6,"MAE_90D_pct":-1.6,"MAE_180D_pct":-39.1,"peak_return_pct":91.0,"max_drawdown_pct":-39.1,"peak_date":"2024-06-04","trough_date":"2024-11-12","score_return_alignment":"price_blowoff_then_high_mae_reversal","current_profile_error":"green_without_quality_bridge","local_4b_watch_flag":true,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":38,"margin_fcf_bridge":27,"revision_bridge":30,"customer_capacity_visibility":33,"valuation_risk_inverse":22,"price_only_risk":88,"information_confidence":42},"evidence_family":"osat_memory_test_beta_without_margin_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"2022-11-15, 2022-11-24; no overlap with entry~D+180","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|200470|Stage3-Yellow|2024-02-16"}
{"row_type":"trigger","case_id":"C10-L114-07","selected_round":"R2","selected_loop":114,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"C10_PACKAGE_SUBSTRATE_MEMORY_RECOVERY_FADE","deep_sub_archetype_id":"C10_DEEP_MEMORY_MATERIAL_METROLOGY_TEST_OSAT_RECOVERY_ORDER_REVENUE_BRIDGE_VS_LATE_CYCLE_RS_FADE","symbol":"195870","name":"해성디에스","trigger_type":"Stage3-Yellow","trigger_date":"2023-07-21","entry_date":"2023-07-24","entry_price":69100,"entry_price_field":"close","price_data_source":"Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","MFE_30D_pct":16.4,"MFE_90D_pct":16.4,"MFE_180D_pct":16.4,"MAE_30D_pct":-13.5,"MAE_90D_pct":-37.8,"MAE_180D_pct":-37.8,"peak_return_pct":16.4,"max_drawdown_pct":-37.8,"peak_date":"2023-07-31","trough_date":"2023-11-01","score_return_alignment":"false_positive_high_mae","current_profile_error":"false_positive_yellow","local_4b_watch_flag":true,"full_4b_requires_non_price_evidence":"stress_tested","raw_component_score_breakdown":{"order_revenue_bridge":32,"margin_fcf_bridge":25,"revision_bridge":28,"customer_capacity_visibility":29,"valuation_risk_inverse":27,"price_only_risk":79,"information_confidence":45},"evidence_family":"package_substrate_memory_recovery_fade_without_revenue_bridge","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"corporate_action_window_check":"none","calibration_usable":true,"promotion_usable":false,"novelty_key":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE|195870|Stage3-Yellow|2023-07-24"}
```

## 6. Score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C10-L114-01","symbol":"092070","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","current_profile_proxy_stage":"Stage2-Actionable","observed_180D_path":"positive","raw_component_score_breakdown":{"order_revenue_bridge":66,"margin_fcf_bridge":54,"revision_bridge":47,"customer_capacity_visibility":42,"valuation_risk_inverse":58,"price_only_risk":18,"information_confidence":61},"alignment":"positive_missed_structural","proposed_shadow_route":"keep_or_upgrade"}
{"row_type":"score_simulation","case_id":"C10-L114-02","symbol":"079370","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage3-Yellow","current_profile_proxy_stage":"Stage3-Yellow","observed_180D_path":"high_mae_or_counterexample","raw_component_score_breakdown":{"order_revenue_bridge":35,"margin_fcf_bridge":29,"revision_bridge":32,"customer_capacity_visibility":31,"valuation_risk_inverse":24,"price_only_risk":82,"information_confidence":44},"alignment":"false_positive_yellow","proposed_shadow_route":"local_4B_watch_until_non_price_bridge_reconfirmed"}
{"row_type":"score_simulation","case_id":"C10-L114-03","symbol":"281740","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","current_profile_proxy_stage":"Stage2-Actionable","observed_180D_path":"positive","raw_component_score_breakdown":{"order_revenue_bridge":63,"margin_fcf_bridge":48,"revision_bridge":45,"customer_capacity_visibility":40,"valuation_risk_inverse":39,"price_only_risk":55,"information_confidence":58},"alignment":"positive_actionable_but_volatility_watch","proposed_shadow_route":"keep_or_upgrade"}
{"row_type":"score_simulation","case_id":"C10-L114-04","symbol":"036810","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage3-Yellow","current_profile_proxy_stage":"Stage3-Yellow","observed_180D_path":"high_mae_or_counterexample","raw_component_score_breakdown":{"order_revenue_bridge":54,"margin_fcf_bridge":39,"revision_bridge":41,"customer_capacity_visibility":37,"valuation_risk_inverse":31,"price_only_risk":67,"information_confidence":52},"alignment":"positive_peak_but_full_window_4b_watch","proposed_shadow_route":"local_4B_watch_until_non_price_bridge_reconfirmed"}
{"row_type":"score_simulation","case_id":"C10-L114-05","symbol":"140860","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage2-Actionable","current_profile_proxy_stage":"Stage2-Actionable","observed_180D_path":"positive","raw_component_score_breakdown":{"order_revenue_bridge":68,"margin_fcf_bridge":61,"revision_bridge":52,"customer_capacity_visibility":46,"valuation_risk_inverse":51,"price_only_risk":23,"information_confidence":66},"alignment":"positive_actionable","proposed_shadow_route":"keep_or_upgrade"}
{"row_type":"score_simulation","case_id":"C10-L114-06","symbol":"200470","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage3-Yellow","current_profile_proxy_stage":"Stage3-Yellow","observed_180D_path":"high_mae_or_counterexample","raw_component_score_breakdown":{"order_revenue_bridge":38,"margin_fcf_bridge":27,"revision_bridge":30,"customer_capacity_visibility":33,"valuation_risk_inverse":22,"price_only_risk":88,"information_confidence":42},"alignment":"price_blowoff_then_high_mae_reversal","proposed_shadow_route":"local_4B_watch_until_non_price_bridge_reconfirmed"}
{"row_type":"score_simulation","case_id":"C10-L114-07","symbol":"195870","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","trigger_type":"Stage3-Yellow","current_profile_proxy_stage":"Stage3-Yellow","observed_180D_path":"high_mae_or_counterexample","raw_component_score_breakdown":{"order_revenue_bridge":32,"margin_fcf_bridge":25,"revision_bridge":28,"customer_capacity_visibility":29,"valuation_risk_inverse":27,"price_only_risk":79,"information_confidence":45},"alignment":"false_positive_high_mae","proposed_shadow_route":"local_4B_watch_until_non_price_bridge_reconfirmed"}
```

## 7. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R2",
  "selected_loop": 114,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "trigger_row_count": 7,
  "calibration_usable_trigger_count": 7,
  "representative_trigger_count": 7,
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 7,
  "same_archetype_new_trigger_family_count": 7,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "stage4b_case_count": 4,
  "stage4c_case_count": 0,
  "current_profile_error_count": 7,
  "source_proxy_only_count": 7,
  "evidence_url_pending_count": 7,
  "promotion_blocked_until_url_repair": true,
  "auto_selected_coverage_gap": "C10 base index 13 + local loops 109/110/111/112/113 about 30 + loop114 representative 7 = local-session adjusted about 50; 50-row practical calibration band reached locally"
}
```

## 8. Shadow rule candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "new_axis_proposed": "C10_verified_order_revenue_margin_or_inventory_reset_bridge_required_before_Yellow_or_Green_plus_late_cycle_memory_beta_MAE_guard_v2",
  "scope": "canonical_archetype_specific",
  "condition": "For C10, Stage3-Yellow or Green should require a verified order/revenue/margin bridge or inventory reset evidence; otherwise route late-cycle relative-strength moves to local_4B_watch when 90D/180D MAE risk is high.",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "full_4b_requires_non_price_evidence",
    "price_only_blowoff_blocks_positive_stage"
  ],
  "existing_axis_weakened": null,
  "do_not_propose_new_weight_delta": false,
  "production_scoring_changed": false,
  "shadow_weight_only": true
}
```

## 9. Residual contribution summary

```json
{
  "row_type": "residual_contribution_summary",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "residual_error_pattern": "C10 still confuses memory-cycle beta and price/RS continuation with verified order-revenue-margin conversion. Positive examples exist, but high-MAE reversals demand local 4B watch when non-price bridge is weak.",
  "why_not_global_rule": "The behavior is C10-specific: memory equipment/material/test/OSAT proxies can produce fast MFE and equally fast drawdown. A global threshold change would over-penalize cleaner C07 direct order cases and under-penalize C10 late-cycle beta.",
  "next_recommended_archetypes": [
    "C06_HBM_MEMORY_CUSTOMER_CAPACITY",
    "C11_BATTERY_ORDERBOOK_RERATING",
    "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
    "C28_SOFTWARE_SECURITY_CONTRACT_RETENTION",
    "C14_EV_DEMAND_SLOWDOWN_4B_4C",
    "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
  ]
}
```

## 10. Interpretation

C10 is not just “semiconductor equipment went up when memory recovered.” It behaves like a spring under mixed load: direct order/revenue bridge can release durable rerating, but late-cycle RS and component-proxy labels can snap back into high MAE. The residual error is therefore not a global Stage2/Yellow threshold problem. It is a C10-specific bridge-quality problem.

The seven cases split into four positive or positive-with-watch paths and three counterexamples. The best positive controls require verified order/revenue/margin or process-control bridge. The worst false positives share a weak non-price bridge, strong price/RS signal, and a large 90D/180D drawdown tail.

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this prompt in the research session.

Later coding agent task:
1. Ingest this MD as a standard V12 result file.
2. Parse all trigger rows in section 5.
3. Recompute 30D/90D/180D MFE/MAE from Songdaiki/stock-web tradable shards.
4. Verify evidence URLs or replace source_proxy_only rows with durable evidence references.
5. If price paths and evidence survive validation, consider a C10-scoped shadow patch:
   - require verified order/revenue/margin or inventory reset bridge before Stage3-Yellow/Green;
   - route late-cycle memory-equipment/material/test proxy moves to local_4B_watch when non-price bridge is weak and 90D/180D MAE risk is high;
   - do not change global Stage2/Stage3 thresholds.
6. Do not patch production scoring directly from this single MD. Batch with adjacent C10/C06/C07 loops.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 114
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C11_BATTERY_ORDERBOOK_RERATING, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C14_EV_DEMAND_SLOWDOWN_4B_4C, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
