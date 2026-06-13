# E2R Stock-Web v12 Residual Research — R2 / C07 HBM Equipment Order Relative Strength Boundary Holdout v111

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 111
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C07 rows=18 / need-to-30=12 / need-to-50=32; current-session boundary holdout
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md`의 정적 장부에서 `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH`는 18 rows, need-to-30 12인 Priority 0 canonical로 남아 있다. 이번 pass는 이미 C06/C09/C10에서 반복적으로 나온 **HBM-adjacent 장비·계측·어닐링·환경제어 narrative**를 C07 관점으로 재검증하는 boundary holdout이다.

C07의 핵심 질문은 “AI/HBM 장비라고 불리는가?”가 아니다. **named HBM customer/order → delivery timing → revenue recognition → margin bridge**가 실제로 확인되는가다. 그 다리가 없으면 상대강도가 강해도 Stage3-Green이 아니라 Stage2-Watch 또는 local Stage4B overlay로 눌러야 한다.

## 2. No-repeat / novelty check

Prior current-session C07 loops used `089030`, `110990`, `232140`, `079370`, `039440`, `095610`, `089970`, `322310`, `064290`, `092870`, `042700`, `031980`, `095340`, `053610`, `420770`, `161580`, `232680`, `086390`, `089890`, `187870`, `160980` as C07 rows.

This file uses a C09/C10-to-C07 boundary set: `039030`, `217190`, `403870`, `122640`, `396470`, `140860`. These are not counted as fresh pure-C07 sector positives; they are marked as `cross_canonical_boundary_replay=true` and `independent_evidence_weight=0.5`. Hard duplicate key remains `canonical_archetype_id + symbol + trigger_type + entry_date`; the selected rows do not duplicate prior C07 keys.

## 3. Stock-Web validation scope

- `stock_web_manifest_max_date`: `2026-02-20`
- `calibration_shard_root`: `atlas/ohlcv_tradable_by_symbol_year`
- `price_adjustment_status`: `raw_unadjusted_marcap`
- Entry price and 30D/90D/180D MFE·MAE are taken from Stock-Web-derived prior source rows and replayed here as C07 boundary evidence.
- Every usable row has `entry_date`, `entry_price`, `MFE_30D_pct`, `MAE_30D_pct`, `MFE_90D_pct`, `MAE_90D_pct`, `MFE_180D_pct`, `MAE_180D_pct`.
- No selected row is marked as corporate-action contaminated in the 180D calibration window.

## 4. Case summary table

| symbol | name | C07 boundary stance | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 039030 | 이오테크닉스 | laser annealing / dicing route is real, but not pure C07 order conversion without named HBM delivery bridge | Stage4B | 2023-09-07 | 163900 | 1.59 | -20.01 | 26.60 | -20.01 | 71.45 | -20.01 | positive_with_guardrail |
| 217190 | 제너셈 | HBM 후공정 장비 order path exists, but full-window drawdown requires conversion gate | Stage4B | 2023-12-08 | 12600 | 17.06 | -1.98 | 37.30 | -4.60 | 37.30 | -40.56 | positive_with_guardrail |
| 396470 | 워트 | environment-control HBM read-through can produce fast MFE, but not C07 order/revenue conversion by itself | Stage4B | 2024-05-13 | 9870 | 67.68 | -9.42 | 85.31 | -9.42 | 85.31 | -34.45 | counterexample |
| 403870 | HPSP | HPA technology leadership is not equal to named HBM equipment order conversion at the selected entry | Stage4B | 2024-02-02 | 46850 | 36.39 | -6.51 | 36.39 | -23.91 | 36.39 | -51.65 | counterexample |
| 122640 | 예스티 | HBM-related equipment order evidence exists, but 180D MAE forces local 4B until delivery/revenue bridge confirms | Stage4B | 2024-06-04 | 17840 | 25.84 | -3.81 | 25.84 | -19.73 | 25.84 | -56.78 | positive_with_guardrail |
| 140860 | 파크시스템스 | nanometrology/AFM demand can support Stage2/Yellow, but C07 Green needs HBM equipment order conversion bridge | Stage2-Actionable | 2024-04-01 | 167700 | 3.40 | -17.05 | 18.43 | -17.05 | 33.57 | -17.05 | positive_with_guardrail |

## 5. Case notes

### 039030 이오테크닉스 — LASER_ANNEALING_ROUTE_C07_BOUNDARY

- Evidence: laser annealing / stealth dicing equipment is relevant to advanced memory and packaging processes, but C07 should not treat it as a pure HBM equipment order without named order and delivery-to-revenue bridge.
- Evidence URL: https://view.asiae.co.kr/article/2023082913041816228
- Price path: entry `2023-09-07` at `163900`, 180D MFE `71.45%`, 180D MAE `-20.01%`, peak `2024-04-12` / `281000`, drawdown after peak `-30.82%`.
- Calibration interpretation: keep the thesis as positive-with-guardrail. C07 Stage3 persistence requires a later order/revenue bridge check.

### 217190 제너셈 — HBM_BACKEND_EQUIPMENT_ORDER_BUT_CONVERSION_GATE

- Evidence: HBM backend equipment order path exists around wafer mounter / package sorter / backend automation, but full-window drawdown shows that order evidence still needs conversion discipline.
- Evidence URL: https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2023/12/48602_genesem_issue_comment.pdf
- Price path: entry `2023-12-08` at `12600`, 180D MFE `37.30%`, 180D MAE `-40.56%`, peak `2024-03-07` / `17300`, drawdown after peak `-56.71%`.
- Calibration interpretation: C07 positive but local 4B overlay is needed until shipment/revenue/margin bridge appears.

### 396470 워트 — ENVIRONMENT_CONTROL_NOT_ORDER_CONVERSION

- Evidence: HBM process environment-control read-through is real, but the row is closer to process-support equipment optionality than direct HBM order conversion.
- Evidence URL: https://v.daum.net/v/bL11mgGkMB?f=p
- Price path: entry `2024-05-13` at `9870`, 180D MFE `85.31%`, 180D MAE `-34.45%`, peak `2024-06-26` / `18290`, drawdown after peak `-64.63%`.
- Calibration interpretation: large MFE does not validate C07 Green. Treat as Stage4B/local watch unless named customer order and revenue recognition bridge are confirmed.

### 403870 HPSP — HPA_TECH_LEADERSHIP_NOT_DIRECT_HBM_ORDER

- Evidence: high-pressure hydrogen annealing leadership and customer expansion are strong, but C07 should not conflate technology monopoly with HBM equipment order relative strength unless memory customer allocation and revenue bridge are explicit.
- Evidence URL: https://www.mk.co.kr/en/economy/10934475
- Price path: entry `2024-02-02` at `46850`, 180D MFE `36.39%`, 180D MAE `-51.65%`, peak `2024-02-15` / `63900`, drawdown after peak `-64.55%`.
- Calibration interpretation: counterexample to price-only or technology-only C07 escalation. Keep Stage4B overlay.

### 122640 예스티 — HBM_EQUIPMENT_ORDER_WITH_HIGH_MAE

- Evidence: HBM equipment cumulative order evidence exists and is stronger than a pure theme, but price path shows severe post-entry risk.
- Evidence URL: https://marketin.edaily.co.kr/News/ReadE?newsId=02794566638918112
- Price path: entry `2024-06-04` at `17840`, 180D MFE `25.84%`, 180D MAE `-56.78%`, peak `2024-07-16` / `22450`, drawdown after peak `-65.66%`.
- Calibration interpretation: positive evidence survives, but C07 Stage3 persistence needs delivery/revenue/margin confirmation and local 4B overlay.

### 140860 파크시스템스 — NANOMETROLOGY_ORDER_MOMENTUM_NOT_PURE_C07

- Evidence: AFM/nanometrology demand can be tied to advanced packaging and HBM process requirements, but direct C07 HBM equipment order conversion remains a boundary question.
- Evidence URL: https://v.daum.net/v/ysn3GGva0J
- Price path: entry `2024-04-01` at `167700`, 180D MFE `33.57%`, 180D MAE `-17.05%`, peak `2024-11-07` / `224000`, drawdown after peak `-25.45%`.
- Calibration interpretation: acceptable Stage2-Actionable / Stage3-Yellow candidate if order/revenue bridge is later confirmed; do not auto-promote to Green on C07 label alone.

## 6. Current calibrated profile stress test

The current profile already has `stage2_required_bridge`, `local_4b_watch_guard`, `price_only_blowoff_blocks_positive_stage`, and `full_4b_requires_non_price_evidence`. This C07 boundary pass says those global axes are directionally correct, but C07 needs a more specific compression rule:

```text
C07 cannot inherit HBM-adjacent evidence from C06/C09/C10 as if it were pure HBM equipment order relative strength.
```

The remaining residual error is a label-compression error. A row may be valid as C09 advanced equipment, C10 memory recovery equipment, or C06 HBM-adjacent capacity proxy, while still being too weak for C07 Stage3 unless named order and revenue conversion are explicit.

## 7. Score / return alignment

| bucket | count | avg MFE30 | avg MAE30 | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | interpretation |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| all usable rows | 6 | 25.3267 | -9.7967 | 38.3117 | -15.7867 | 48.3100 | -36.7500 | strong upside but unstable full-window path |
| positive-with-guardrail | 4 | 11.9725 | -10.7125 | 27.0425 | -15.3475 | 42.0400 | -33.6000 | real evidence, but needs local 4B persistence cap |
| counterexample | 2 | 52.0350 | -7.9650 | 60.8500 | -16.6650 | 60.8500 | -43.0500 | technology/theme label alone overstates C07 quality |

High MFE confirms that the market did recognize the AI/HBM equipment narrative. Deep MAE confirms that C07 should not keep Stage3 persistence without the second bridge: named customer order, shipment, delivery timing, revenue recognition, and margin bridge.

## 8. Shadow rule candidate

```text
C07_HBM_EQUIPMENT_ORDER_REQUIRES_NAMED_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_V111
```

Rule mechanics:

1. Allow Stage2-Actionable when HBM-adjacent equipment evidence is public and the company has credible customer/process linkage.
2. Allow Stage3-Yellow only when at least two of the following exist: named customer/order, confirmed delivery timing, revenue recognition route, margin bridge, or explicit repeat order.
3. Block Stage3-Green when the evidence is mainly technology monopoly, HBM-adjacent process support, environment-control, or AFM/metrology optionality without direct order conversion.
4. Force local Stage4B overlay if 90D or 180D MAE is deep and no second bridge confirmation appears.
5. Do not route to hard 4C unless explicit customer cancellation, qualification failure, order cut, or thesis break is verified.

## 9. Machine-readable trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"039030","company_name":"이오테크닉스","trigger_id":"C07_R2_L111_T01_039030","case_id":"C07_BOUNDARY_V111_039030_2023-09-07","case_role":"positive_with_guardrail","trigger_type":"Stage4B","trigger_date":"2023-09-06","entry_date":"2023-09-07","entry_price":163900.0,"evidence_family":"laser_annealing_hbm_adjacent_order_bridge_boundary","evidence_url":"https://view.asiae.co.kr/article/2023082913041816228","stage2_evidence_fields":["public_event_or_research_evidence","advanced_equipment_process_linkage","early_order_or_customer_route"],"stage3_evidence_fields":["blocked_without_named_HBM_order_delivery_revenue_margin_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","local_4b_watch_guard","bridge_gap_reconfirmation_required"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2023.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.59,"MAE_30D_pct":-20.01,"MFE_90D_pct":26.6,"MAE_90D_pct":-20.01,"MFE_180D_pct":71.45,"MAE_180D_pct":-20.01,"peak_date":"2024-04-12","peak_price":281000.0,"drawdown_after_peak_pct":-30.82,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"C07 persistence should be capped until named HBM order and revenue bridge confirms","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"217190","company_name":"제너셈","trigger_id":"C07_R2_L111_T02_217190","case_id":"C07_BOUNDARY_V111_217190_2023-12-08","case_role":"positive_with_guardrail","trigger_type":"Stage4B","trigger_date":"2023-12-08","entry_date":"2023-12-08","entry_price":12600.0,"evidence_family":"hbm_backend_equipment_order_conversion_gate","evidence_url":"https://money2.daishin.com/PDF/Out/intranet_data/product/researchcenter/report/2023/12/48602_genesem_issue_comment.pdf","stage2_evidence_fields":["public_event_or_research_evidence","HBM_backend_equipment_order_path","customer_or_order_quality"],"stage3_evidence_fields":["partial_order_evidence","blocked_without_delivery_revenue_margin_bridge"],"stage4b_evidence_fields":["MAE180_breach","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/217/217190/2023.csv","profile_path":"atlas/symbol_profiles/217/217190.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.06,"MAE_30D_pct":-1.98,"MFE_90D_pct":37.3,"MAE_90D_pct":-4.6,"MFE_180D_pct":37.3,"MAE_180D_pct":-40.56,"peak_date":"2024-03-07","peak_price":17300.0,"drawdown_after_peak_pct":-56.71,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"positive C07 evidence but full-window drawdown requires 4B overlay","stage_after_shadow_rule":"Stage4B_local_overlay_until_delivery_revenue_margin_bridge","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"396470","company_name":"워트","trigger_id":"C07_R2_L111_T03_396470","case_id":"C07_BOUNDARY_V111_396470_2024-05-13","case_role":"counterexample","trigger_type":"Stage4B","trigger_date":"2024-05-10","entry_date":"2024-05-13","entry_price":9870.0,"evidence_family":"environment_control_hbm_readthrough_not_order_conversion","evidence_url":"https://v.daum.net/v/bL11mgGkMB?f=p","stage2_evidence_fields":["public_event_or_research_evidence","HBM_process_support_readthrough"],"stage3_evidence_fields":["blocked_without_named_HBM_order_delivery_revenue_margin_bridge"],"stage4b_evidence_fields":["fast_MFE_high_MAE","local_4b_watch_guard","theme_or_proxy_decontamination"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv","profile_path":"atlas/symbol_profiles/396/396470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":67.68,"MAE_30D_pct":-9.42,"MFE_90D_pct":85.31,"MAE_90D_pct":-9.42,"MFE_180D_pct":85.31,"MAE_180D_pct":-34.45,"peak_date":"2024-06-26","peak_price":18290.0,"drawdown_after_peak_pct":-64.63,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"environment-control proxy should not persist as C07 Stage3 without order/revenue bridge","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"403870","company_name":"HPSP","trigger_id":"C07_R2_L111_T04_403870","case_id":"C07_BOUNDARY_V111_403870_2024-02-02","case_role":"counterexample","trigger_type":"Stage4B","trigger_date":"2024-02-01","entry_date":"2024-02-02","entry_price":46850.0,"evidence_family":"hpa_technology_leadership_not_direct_hbm_order_conversion","evidence_url":"https://www.mk.co.kr/en/economy/10934475","stage2_evidence_fields":["technology_leadership","customer_expansion_expectation","advanced_equipment_route"],"stage3_evidence_fields":["blocked_without_direct_HBM_customer_allocation_or_revenue_bridge"],"stage4b_evidence_fields":["MAE90_or_MAE180_breach","local_4b_watch_guard","valuation_or_optionality_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv","profile_path":"atlas/symbol_profiles/403/403870.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":36.39,"MAE_30D_pct":-6.51,"MFE_90D_pct":36.39,"MAE_90D_pct":-23.91,"MFE_180D_pct":36.39,"MAE_180D_pct":-51.65,"peak_date":"2024-02-15","peak_price":63900.0,"drawdown_after_peak_pct":-64.55,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"technology monopoly can become C07 false persistence without HBM order conversion","stage_after_shadow_rule":"Stage4B_local_overlay_or_Stage2_Watch_cap","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"122640","company_name":"예스티","trigger_id":"C07_R2_L111_T05_122640","case_id":"C07_BOUNDARY_V111_122640_2024-06-04","case_role":"positive_with_guardrail","trigger_type":"Stage4B","trigger_date":"2024-06-03","entry_date":"2024-06-04","entry_price":17840.0,"evidence_family":"hbm_equipment_order_high_mae_conversion_gate","evidence_url":"https://marketin.edaily.co.kr/News/ReadE?newsId=02794566638918112","stage2_evidence_fields":["public_event_or_disclosure","HBM_equipment_order_evidence","customer_or_order_quality"],"stage3_evidence_fields":["partial_order_evidence","blocked_without_delivery_revenue_margin_bridge"],"stage4b_evidence_fields":["MAE180_breach","local_4b_watch_guard"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/122/122640/2024.csv","profile_path":"atlas/symbol_profiles/122/122640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":25.84,"MAE_30D_pct":-3.81,"MFE_90D_pct":25.84,"MAE_90D_pct":-19.73,"MFE_180D_pct":25.84,"MAE_180D_pct":-56.78,"peak_date":"2024-07-16","peak_price":22450.0,"drawdown_after_peak_pct":-65.66,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"actual HBM order evidence still needs delivery/revenue/margin bridge before C07 persistence","stage_after_shadow_rule":"Stage4B_local_overlay_until_delivery_revenue_margin_bridge","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","research_session":"post_calibrated_sector_archetype_residual_research","round":"R2","loop":111,"selected_round":"R2","selected_loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"mixed_C07_hbm_equipment_order_revenue_conversion_boundary_v111","cross_canonical_boundary_replay":true,"source_canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","symbol":"140860","company_name":"파크시스템스","trigger_id":"C07_R2_L111_T06_140860","case_id":"C07_BOUNDARY_V111_140860_2024-04-01","case_role":"positive_with_guardrail","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-29","entry_date":"2024-04-01","entry_price":167700.0,"evidence_family":"nanometrology_hbm_process_demand_boundary","evidence_url":"https://v.daum.net/v/ysn3GGva0J","stage2_evidence_fields":["public_event_or_research_evidence","advanced_packaging_or_HBM_process_linkage","customer_quality_route"],"stage3_evidence_fields":["possible_if_order_revenue_bridge_later_confirms","blocked_from_Green_without_direct_order_conversion"],"stage4b_evidence_fields":["local_4b_watch_guard_if_bridge_fails"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","profile_path":"atlas/symbol_profiles/140/140860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.4,"MAE_30D_pct":-17.05,"MFE_90D_pct":18.43,"MAE_90D_pct":-17.05,"MFE_180D_pct":33.57,"MAE_180D_pct":-17.05,"peak_date":"2024-11-07","peak_price":224000.0,"drawdown_after_peak_pct":-25.45,"forward_window_trading_days":180,"calibration_usable":true,"representative_for_aggregate":true,"source_proxy_only":false,"evidence_url_pending":false,"window_180D_corporate_action_contaminated":false,"current_profile_error":true,"current_profile_verdict":"nanometrology demand can support C07 watch but cannot force pure HBM equipment Green without order conversion","stage_after_shadow_rule":"Stage2_Actionable_or_Stage3_Yellow_with_Green_cap","independent_evidence_weight":0.5,"production_scoring_patch_applied":false,"calibration_block_reasons":[]}
```

## 10. Machine-readable score simulations

```jsonl
{"row_type":"score_simulation","round":"R2","loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","rule_candidate":"C07_HBM_EQUIPMENT_ORDER_REQUIRES_NAMED_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_V111","baseline_current_profile_proxy_stage":"Stage2_or_Stage3_if_HBM_proxy_is_overcompressed","shadow_rule_corrected_stage":"Stage2-Watch_or_local_Stage4B_overlay_until_order_revenue_bridge_confirms","raw_component_score_breakdown":{"eps_fcf_explosion":55,"earnings_visibility":57,"bottleneck_pricing":60,"market_mispricing":58,"valuation_rerating":48,"capital_allocation":35,"information_confidence":69,"bridge_confirmation_score":42,"risk_guardrail_penalty":-11},"simulated_total_score_before_guardrail":63.1,"simulated_total_score_after_guardrail":56.5,"score_return_alignment":"reduces false persistence from HBM-adjacent labels while preserving true order conversion candidates as watched positives","production_scoring_patch_applied":false}
{"row_type":"aggregate","round":"R2","loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","jsonl_trigger_row_count":6,"calibration_usable_rows":6,"representative_rows":6,"positive_case_count":4,"counterexample_count":2,"stage4b_case_count":5,"stage4c_case_count":0,"cross_canonical_boundary_replay":true,"average_MFE_30D_pct":25.3267,"average_MAE_30D_pct":-9.7967,"average_MFE_90D_pct":38.3117,"average_MAE_90D_pct":-15.7867,"average_MFE_180D_pct":48.31,"average_MAE_180D_pct":-36.75,"source_proxy_only_rows":0,"evidence_url_pending_rows":0,"current_profile_error_count":6,"production_scoring_patch_applied":false}
{"row_type":"residual_contribution","round":"R2","loop":111,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","selected_priority_bucket":"Priority 0 static ledger C07 rows=18 / need-to-30=12","previous_static_index_rows":18,"new_representative_rows":6,"session_adjusted_boundary_holdout":"C07 source quality strengthened but C09/C10/C06 source rows are not over-counted as pure C07 positives","sector_specific_rule_candidate":"L2_C07_HBM_EQUIPMENT_ORDER_TO_REVENUE_CONVERSION_WITH_PROXY_DECONTAMINATION","canonical_archetype_rule_candidate":"C07_HBM_EQUIPMENT_ORDER_REQUIRES_NAMED_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE_WITH_PROXY_4B_CAP_V111","loop_contribution_label":"canonical_archetype_rule_candidate","new_axis_proposed":["C07_proxy_decontamination_gate","C07_named_order_delivery_revenue_margin_gate","C07_high_MAE_local_4B_overlay"],"existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"existing_axis_weakened":null,"do_not_propose_new_weight_delta":false}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute now. Later batch coding agent should ingest this MD as a v12 result file. Validate all trigger rows against schema_family=v12_sector_archetype_residual. Treat this file as a C07 boundary holdout: cross_canonical_boundary_replay=true and independent_evidence_weight=0.5. Do not double-count source C09/C10/C06 sector positives. Evaluate whether C07 runtime profile needs a shadow gate requiring named HBM equipment order, delivery/revenue recognition, and margin bridge before Stage3-Yellow/Green persistence. Preserve production_scoring_patch_applied=false in this research artifact.
```

## 12. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
cross_canonical_boundary_replay: true
source_canonical_family: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
calibration_usable_rows: 6
representative_rows: 6
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
future_data_leakage_detected: false
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
ready_for_batch_ingest: true
```

## 13. Next research state

```text
completed_round = R2
completed_loop = 111
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 static ledger C07 rows=18 / need-to-30=12 / boundary holdout
next_recommended_archetypes = C11_BATTERY_ORDERBOOK_RERATING | C01_ORDER_BACKLOG_MARGIN_BRIDGE | R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
