# E2R Stock-Web v12 Residual Research — R2 loop 131 — L2 / C09 Advanced Equipment Valuation Blowoff

```text
MD filename: e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
selected_round: R2
selected_loop: 131
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 / under_30_representative_rows / remote C09 rows=10 need_to_30=20 need_to_50=40
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD
loop_objective: coverage_gap_fill | followup_new_symbol_date_family | source_proxy_replacement | counterexample_mining | 4B_non_price_requirement_stress_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection and novelty check

`V12_Research_No_Repeat_Index.md` still places `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` in Priority 0 with 10 representative rows and `need_to_30=20`. The prior local C09 files already covered the obvious HBM-equipment and high-profile process-tool names, so this loop deliberately moves to lower-overlap boundary cases: wafer-transfer automation, dry-strip process equipment, display-heavy semiconductor equipment, vacuum robot component exposure, EHD printing/coating, and FOUP humidity-control / HBM-adjacent process-control routes.

Strict no-repeat guard applied:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 6
reused_case_count = 0
same_archetype_new_symbol_count = 6
same_archetype_new_trigger_family_count = 6
calibration_usable_trigger_count = 6
representative_trigger_count = 6
positive_case_count = 3
counterexample_count = 3
stage4b_overlay_count = 5
stage4c_case_count = 0
current_profile_error_count = 6
```

## 2. Price source validation

The price basis is `Songdaiki/stock-web` `tradable_raw`, transformed from FinanceData/marcap, with `raw_unadjusted_marcap` adjustment status. The manifest max date is `2026-02-20`; no price after that date is assumed. The schema definition used here is:

```text
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
entry_price = close c column on entry_date
forward_window = 30/90/180 tradable rows from entry row
corporate_action_window_status = clean if share-count ratio in local 180D window < 1.20
```

All six representative rows have full 30/90/180D MFE/MAE and clean local 180D share-count windows.

## 3. Trigger-level result table

| symbol | company | trigger / entry | trigger_type | MFE30/90/180 | MAE30/90/180 | peak / post-peak DD | role |
|---|---|---|---|---:|---:|---:|---|
| 071280 | 로체시스템즈 | 2024-01-02 / 2024-01-02 @ 6,380 | Stage2 | 29.78/95.92/190.44 | -3.13/-3.13/-3.13 | 2024-06-21 / -44.68% | positive |
| 319660 | 피에스케이 | 2024-02-01 / 2024-02-01 @ 19,760 | Stage2-Actionable | 41.19/81.68/97.87 | -1.16/-1.16/-1.16 | 2024-07-11 / -48.87% | positive |
| 265520 | AP시스템 | 2024-01-31 / 2024-01-31 @ 21,350 | Stage2 | 4.68/70.02/70.02 | -5.15/-5.15/-25.01 | 2024-05-03 / -55.90% | counterexample |
| 232680 | 라온로보틱스 | 2024-12-09 / 2024-12-09 @ 5,900 | Stage2 | 30.51/99.32/99.32 | -3.73/-3.73/-3.73 | 2025-02-19 / -43.79% | positive |
| 419080 | 엔젯 | 2024-08-01 / 2024-08-01 @ 11,800 | Stage2 | 1.02/1.02/1.02 | -24.24/-40.25/-40.25 | 2024-08-29 / -40.86% | counterexample |
| 417840 | 저스템 | 2024-11-26 / 2024-11-26 @ 6,270 | Stage2 | 80.22/80.22/103.83 | -21.45/-21.45/-21.45 | 2025-08-13 / -16.98% | counterexample |

## 4. Case interpretation

### 4.1 로체시스템즈 / 071280

Rorze/Rorze Systems style wafer-transfer automation is real process infrastructure. The path showed an unusually clean 180D MFE of 190.44% with only -3.13% MAE inside the window. However, this row is still not clean Stage3-Yellow because the trigger evidence is product-route identity rather than a named customer order, qualification pass, or revenue/margin conversion. It supports C09 credit for process automation only at Stage2-watch or small Stage2-Actionable weight, followed by local 4B once the MFE is expressed.

### 4.2 피에스케이 / 319660

PSK is the cleanest process-tool row in this loop. Dry strip / dry clean / NHM strip / edge clean is a true process-equipment niche, and the early 2024 row produced 97.87% 180D MFE with only -1.16% MAE. Still, the peak came within the 180D window and the post-peak drawdown reached -48.87%, so the correction is not “upgrade Green”; it is “credit Stage2-Actionable early, then force local 4B/profit-lock after a fast reprice.”

### 4.3 AP시스템 / 265520

AP Systems has real semiconductor/display laser and plasma equipment capability, but the route is mixed-scope. The price path had 70.02% 90D/180D MFE, then a -55.90% post-peak drawdown. This is the archetypal C09 boundary: equipment identity alone produced tradable convexity, but display-heavy mix and missing named semiconductor order mean Stage2-watch plus 4B cap is safer than Yellow.

### 4.4 라온로보틱스 / 232680

Raon Robotics has vacuum wafer-transfer robot relevance. The price path after 2024-12-09 was strong, with 99.32% 90D/180D MFE and -3.73% MAE. But the evidence is component-level route identity, not a named customer PO. C09 should avoid discarding this route entirely, yet still block full Yellow until order/acceptance/revenue conversion appears.

### 4.5 엔젯 / 419080

Enjet is the negative control. EHD printing/coating/plasma language touches semiconductor and display processes, but the trigger produced only 1.02% MFE and -40.25% MAE over 90D/180D. The row shows why C09 cannot treat “advanced manufacturing technology” as equivalent to equipment bottleneck. Without semiconductor order/revenue conversion, this should be Stage2-watch or rejected as source/proxy only.

### 4.6 저스템 / 417840

Justem is an HBM-adjacent process-control boundary case. The route through FOUP humidity control and hybrid-bonding development is plausible, and the 180D MFE reached 103.83%. But 30D/90D MAE already touched -21.45%, and the trigger did not yet prove a large named customer order. This supports a staged rule: keep as Stage2-watch until named order or acceptance appears; do not promote clean Yellow merely from HBM-adjacent equipment R&D.

## 5. Score-return alignment

The loop does not argue that C09 should be broadened blindly. It argues for a split:

```text
credit:
  - real process-tool identity
  - process-critical component route
  - named customer/order/qualification
  - revenue and OP-margin conversion
  - early entry before reprice

penalize:
  - display-heavy or mixed scope without semicon order
  - EHD/printing/coating or component identity without customer conversion
  - HBM-adjacent R&D without order/acceptance
  - fast MFE already expressed before new evidence
  - post-peak confirmation headlines
```

## 6. Proposed shadow rule candidate

```text
canonical_archetype_rule_candidate:
C09_PROCESS_TOOL_COMPONENT_SCOPE_AND_REPRICE_GUARD

rule:
For C09, award Stage2 credit for real process equipment or process-critical component routes, but Stage2-Actionable requires at least one of: named customer/order, formal qualification, shipment/delivery, or revenue/margin conversion. Product identity, display-heavy mix, EHD printing/coating, humidity-control development, and wafer-transfer component narratives are capped at Stage2-watch unless order conversion appears. If 30D/90D MFE has already expressed the theme without new non-price evidence, add local 4B/profit-lock rather than fresh Yellow/Green.
```

No production scoring change is made here.

## 7. Machine-readable rows

```jsonl
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_01_071280_Stage2_2024-01-02","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"071280","company_name":"로체시스템즈","case_polarity":"positive","outcome_label":"positive_high_convexity_with_post_peak_4b_guard","evidence_quality":"official_product_route_but_no_trigger_specific_order","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+071280+Stage2+2024-01-02","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_01_071280_Stage2_2024-01-02","case_id":"CASE_C09_L131_01_071280_Stage2_2024-01-02","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"071280","company_name":"로체시스템즈","trigger_type":"Stage2","trigger_date":"2024-01-02","entry_date":"2024-01-02","entry_price":6380.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/071/071280/2024.csv","symbol_profile_path":"atlas/symbol_profiles/071/071280.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":29.78,"MFE_90D_pct":95.92,"MFE_180D_pct":190.44,"MAE_30D_pct":-3.13,"MAE_90D_pct":-3.13,"MAE_180D_pct":-3.13,"peak_date":"2024-06-21","peak_price":18530.0,"peak_180D_pct":190.44,"drawdown_after_peak_pct":-44.68,"positive_or_counterexample":"positive","trigger_outcome_label":"positive_high_convexity_with_post_peak_4b_guard","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2_watch_or_Actionable_small_weight; Yellow only after order/revenue conversion.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"Wafer transfer / clean automation product route gives real C09 process-equipment identity, but no named customer/order was attached at trigger.","evidence_sources":["https://www.rorze.com/en/products_category/wafer-transfer-system/"],"evidence_quality":"official_product_route_but_no_trigger_specific_order","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_071280_2024-01-02_Stage2","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+071280+Stage2+2024-01-02","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_01_071280_Stage2_2024-01-02","trigger_id":"TRIG_C09_L131_01_071280_Stage2_2024-01-02","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"071280","company_name":"로체시스템즈","trigger_type":"Stage2","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2_watch_or_Actionable_small_weight; Yellow only after order/revenue conversion.","raw_component_score_breakdown":{"equipment_identity":8,"named_customer_or_order":2,"process_role_specificity":7,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-2},"weighted_score_before":70,"weighted_score_after_shadow":72,"score_return_alignment_label":"positive_high_convexity_with_post_peak_4b_guard","MFE_90D_pct":95.92,"MAE_90D_pct":-3.13,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_02_319660_Stage2Actionable_2024-02-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"319660","company_name":"피에스케이","case_polarity":"positive","outcome_label":"positive_process_tool_niche_with_profit_lock_4b","evidence_quality":"official_process_equipment_identity","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+319660+Stage2-Actionable+2024-02-01","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_02_319660_Stage2Actionable_2024-02-01","case_id":"CASE_C09_L131_02_319660_Stage2Actionable_2024-02-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"319660","company_name":"피에스케이","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":19760.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","symbol_profile_path":"atlas/symbol_profiles/319/319660.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":41.19,"MFE_90D_pct":81.68,"MFE_180D_pct":97.87,"MAE_30D_pct":-1.16,"MAE_90D_pct":-1.16,"MAE_180D_pct":-1.16,"peak_date":"2024-07-11","peak_price":39100.0,"peak_180D_pct":97.87,"drawdown_after_peak_pct":-48.87,"positive_or_counterexample":"positive","trigger_outcome_label":"positive_process_tool_niche_with_profit_lock_4b","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2-Actionable with local 4B/profit-lock after fast MFE; no automatic Green.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"Dry strip / dry clean / NHM strip / edge clean process-equipment niche is real bottleneck exposure; price path rewards early recognition but later drawdown needs 4B cap.","evidence_sources":["https://www.pskinc.com/aboutpsk/overview.php"],"evidence_quality":"official_process_equipment_identity","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_319660_2024-02-01_Stage2-Actionable","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+319660+Stage2-Actionable+2024-02-01","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_02_319660_Stage2Actionable_2024-02-01","trigger_id":"TRIG_C09_L131_02_319660_Stage2Actionable_2024-02-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"319660","company_name":"피에스케이","trigger_type":"Stage2-Actionable","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2-Actionable with local 4B/profit-lock after fast MFE; no automatic Green.","raw_component_score_breakdown":{"equipment_identity":8,"named_customer_or_order":2,"process_role_specificity":7,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-2},"weighted_score_before":76,"weighted_score_after_shadow":72,"score_return_alignment_label":"positive_process_tool_niche_with_profit_lock_4b","MFE_90D_pct":81.68,"MAE_90D_pct":-1.16,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_03_265520_Stage2_2024-01-31","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"265520","company_name":"AP시스템","case_polarity":"counterexample","outcome_label":"display_heavy_semiconductor_equipment_proxy_needs_scope_discount","evidence_quality":"official_company_route_but_scope_mixed","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+265520+Stage2+2024-01-31","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_03_265520_Stage2_2024-01-31","case_id":"CASE_C09_L131_03_265520_Stage2_2024-01-31","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"265520","company_name":"AP시스템","trigger_type":"Stage2","trigger_date":"2024-01-31","entry_date":"2024-01-31","entry_price":21350.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/265/265520/2024.csv","symbol_profile_path":"atlas/symbol_profiles/265/265520.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":4.68,"MFE_90D_pct":70.02,"MFE_180D_pct":70.02,"MAE_30D_pct":-5.15,"MAE_90D_pct":-5.15,"MAE_180D_pct":-25.01,"peak_date":"2024-05-03","peak_price":36300.0,"peak_180D_pct":70.02,"drawdown_after_peak_pct":-55.9,"positive_or_counterexample":"counterexample","trigger_outcome_label":"display_heavy_semiconductor_equipment_proxy_needs_scope_discount","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2-watch with scope discount and local 4B after fast reprice.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"The company has semiconductor/display laser/plasma equipment capability, but display-heavy mix and absent named semiconductor order make it a C09 boundary/proxy case.","evidence_sources":["https://www.apsystems.co.kr/eng/company/introduce.asp"],"evidence_quality":"official_company_route_but_scope_mixed","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_265520_2024-01-31_Stage2","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+265520+Stage2+2024-01-31","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_03_265520_Stage2_2024-01-31","trigger_id":"TRIG_C09_L131_03_265520_Stage2_2024-01-31","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"265520","company_name":"AP시스템","trigger_type":"Stage2","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2-watch with scope discount and local 4B after fast reprice.","raw_component_score_breakdown":{"equipment_identity":6,"named_customer_or_order":2,"process_role_specificity":5,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-6},"weighted_score_before":70,"weighted_score_after_shadow":64,"score_return_alignment_label":"display_heavy_semiconductor_equipment_proxy_needs_scope_discount","MFE_90D_pct":70.02,"MAE_90D_pct":-5.15,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_04_232680_Stage2_2024-12-09","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"232680","company_name":"라온로보틱스","case_polarity":"positive","outcome_label":"positive_component_route_but_requires_named_order_before_yellow","evidence_quality":"official_product_route_but_no_named_order","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+232680+Stage2+2024-12-09","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_04_232680_Stage2_2024-12-09","case_id":"CASE_C09_L131_04_232680_Stage2_2024-12-09","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"232680","company_name":"라온로보틱스","trigger_type":"Stage2","trigger_date":"2024-12-09","entry_date":"2024-12-09","entry_price":5900.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/232/232680/2024.csv","symbol_profile_path":"atlas/symbol_profiles/232/232680.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.51,"MFE_90D_pct":99.32,"MFE_180D_pct":99.32,"MAE_30D_pct":-3.73,"MAE_90D_pct":-3.73,"MAE_180D_pct":-3.73,"peak_date":"2025-02-19","peak_price":11760.0,"peak_180D_pct":99.32,"drawdown_after_peak_pct":-43.79,"positive_or_counterexample":"positive","trigger_outcome_label":"positive_component_route_but_requires_named_order_before_yellow","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2-watch/Actionable-small-weight; 4B overlay after MFE.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"Vacuum wafer transfer robot route is genuine component-level bottleneck exposure, but named customer/tool order and margin conversion were not visible at trigger.","evidence_sources":["https://raonrobot.com/en/m11.php"],"evidence_quality":"official_product_route_but_no_named_order","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_232680_2024-12-09_Stage2","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+232680+Stage2+2024-12-09","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_04_232680_Stage2_2024-12-09","trigger_id":"TRIG_C09_L131_04_232680_Stage2_2024-12-09","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"232680","company_name":"라온로보틱스","trigger_type":"Stage2","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2-watch/Actionable-small-weight; 4B overlay after MFE.","raw_component_score_breakdown":{"equipment_identity":8,"named_customer_or_order":2,"process_role_specificity":7,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-2},"weighted_score_before":70,"weighted_score_after_shadow":72,"score_return_alignment_label":"positive_component_route_but_requires_named_order_before_yellow","MFE_90D_pct":99.32,"MAE_90D_pct":-3.73,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_05_419080_Stage2_2024-08-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"419080","company_name":"엔젯","case_polarity":"counterexample","outcome_label":"eHD_printing_and_coating_product_identity_without_semiconductor_order_conversion","evidence_quality":"official_product_identity_only","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+419080+Stage2+2024-08-01","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_05_419080_Stage2_2024-08-01","case_id":"CASE_C09_L131_05_419080_Stage2_2024-08-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"419080","company_name":"엔젯","trigger_type":"Stage2","trigger_date":"2024-08-01","entry_date":"2024-08-01","entry_price":11800.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/419/419080/2024.csv","symbol_profile_path":"atlas/symbol_profiles/419/419080.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.02,"MFE_90D_pct":1.02,"MFE_180D_pct":1.02,"MAE_30D_pct":-24.24,"MAE_90D_pct":-40.25,"MAE_180D_pct":-40.25,"peak_date":"2024-08-29","peak_price":11920.0,"peak_180D_pct":1.02,"drawdown_after_peak_pct":-40.86,"positive_or_counterexample":"counterexample","trigger_outcome_label":"eHD_printing_and_coating_product_identity_without_semiconductor_order_conversion","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2-watch or reject-as-proxy; block Actionable/Yellow without order/revenue bridge.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"EHD printing/coating/plasma technology touches semiconductor/display processes, but no hard semiconductor order, utilization, or margin bridge appeared at trigger.","evidence_sources":["https://enjet.co.kr/"],"evidence_quality":"official_product_identity_only","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_419080_2024-08-01_Stage2","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+419080+Stage2+2024-08-01","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_05_419080_Stage2_2024-08-01","trigger_id":"TRIG_C09_L131_05_419080_Stage2_2024-08-01","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"419080","company_name":"엔젯","trigger_type":"Stage2","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2-watch or reject-as-proxy; block Actionable/Yellow without order/revenue bridge.","raw_component_score_breakdown":{"equipment_identity":6,"named_customer_or_order":2,"process_role_specificity":5,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-6},"weighted_score_before":70,"weighted_score_after_shadow":64,"score_return_alignment_label":"eHD_printing_and_coating_product_identity_without_semiconductor_order_conversion","MFE_90D_pct":1.02,"MAE_90D_pct":-40.25,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"case","schema_family":"v12_sector_archetype_residual","case_id":"CASE_C09_L131_06_417840_Stage2_2024-11-26","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"417840","company_name":"저스템","case_polarity":"counterexample","outcome_label":"HBM_adjacent_humidity_control_research_route_high_MAE_requires_order_confirmation","evidence_quality":"company_investor_update_but_pre_order_conversion","calibration_usable":true,"representative_for_aggregate":true,"strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+417840+Stage2+2024-11-26","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","trigger_id":"TRIG_C09_L131_06_417840_Stage2_2024-11-26","case_id":"CASE_C09_L131_06_417840_Stage2_2024-11-26","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"417840","company_name":"저스템","trigger_type":"Stage2","trigger_date":"2024-11-26","entry_date":"2024-11-26","entry_price":6270.0,"entry_price_basis":"close_c_column","price_source":"Songdaiki/stock-web","price_source_repo":"Songdaiki/stock-web","price_source_url":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/417/417840/2024.csv","symbol_profile_path":"atlas/symbol_profiles/417/417840.json","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":80.22,"MFE_90D_pct":80.22,"MFE_180D_pct":103.83,"MAE_30D_pct":-21.45,"MAE_90D_pct":-21.45,"MAE_180D_pct":-21.45,"peak_date":"2025-08-13","peak_price":12780.0,"peak_180D_pct":103.83,"drawdown_after_peak_pct":-16.98,"positive_or_counterexample":"counterexample","trigger_outcome_label":"HBM_adjacent_humidity_control_research_route_high_MAE_requires_order_confirmation","current_profile_verdict":"would over-credit if advanced-equipment/product identity overrides missing order/revenue conversion or bad reprice context","shadow_profile_verdict":"Stage2-watch only until named order/acceptance; MAE guard prevents clean Yellow.","current_profile_error":"scope_or_blowoff_residual_error","residual_contribution":"C09 should credit real process-equipment identity, but cap Stage2-Actionable/Yellow when there is no named order, delivery, revenue/margin conversion, or when evidence arrives after a fast reprice.","evidence_summary":"FOUP humidity-control and HBM-adjacent hybrid bonding development route is C09-relevant, but direct large customer order was not yet confirmed at trigger and MAE crossed -20%.","evidence_sources":["https://www.justem.co.kr/main/sub02_05_view.php?bo_uid=370&ps_page=1"],"evidence_quality":"company_investor_update_but_pre_order_conversion","calibration_usable":true,"price_path_valid":true,"forward_window_trading_days":180,"corporate_action_window_status":"clean_180D_window; share_count_ratio_max<1.20 in local stock-web shard check","same_entry_group_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_417840_2024-11-26_Stage2","strict_no_repeat_key":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF+417840+Stage2+2024-11-26","is_new_independent_case":true,"dedupe_for_aggregate":true,"aggregate_role":"representative","source_file":"docs/round/e2r_stock_web_v12_residual_round_R2_loop_131_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md"}
{"row_type":"score_simulation","schema_family":"v12_sector_archetype_residual","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"CASE_C09_L131_06_417840_Stage2_2024-11-26","trigger_id":"TRIG_C09_L131_06_417840_Stage2_2024-11-26","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_EQUIPMENT_PROCESS_TOOL_COMPONENT_AND_SCOPE_PROXY_REPRICE_GUARD","symbol":"417840","company_name":"저스템","trigger_type":"Stage2","current_profile_stage":"Stage2_or_Yellow_risk_if_product_identity_is_overweighted","proposed_shadow_stage":"Stage2-watch only until named order/acceptance; MAE guard prevents clean Yellow.","raw_component_score_breakdown":{"equipment_identity":6,"named_customer_or_order":2,"process_role_specificity":5,"revenue_margin_conversion":3,"valuation_blowoff_or_post_peak_risk":8,"source_quality":7,"proxy_penalty":-6},"weighted_score_before":70,"weighted_score_after_shadow":64,"score_return_alignment_label":"HBM_adjacent_humidity_control_research_route_high_MAE_requires_order_confirmation","MFE_90D_pct":80.22,"MAE_90D_pct":-21.45,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","schema_family":"v12_sector_archetype_residual","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","usable_trigger_count":6,"representative_trigger_count":6,"new_symbol_count":6,"positive_case_count":3,"counterexample_count":3,"stage4b_overlay_count":5,"stage4c_case_count":0,"avg_MFE_90D_pct":71.36,"avg_MAE_90D_pct":-12.48,"current_profile_error_count":6,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"shadow_weight","schema_family":"v12_sector_archetype_residual","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","axis":"C09_PROCESS_TOOL_COMPONENT_SCOPE_AND_REPRICE_GUARD","proposed_delta":0.0,"proposed_rule":"For C09, credit real process-equipment or process-critical component routes only when process role is clear. Stage2-Actionable requires named order/customer/qualification or revenue-margin conversion. Product identity, display-heavy mix, EHD printing, humidity-control R&D, and wafer-transfer component narratives are capped at Stage2-watch until order conversion is visible. After fast MFE, apply local 4B/profit-lock rather than fresh Yellow/Green.","supported_symbols":["071280","319660","265520","232680","419080","417840"],"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","schema_family":"v12_sector_archetype_residual","round":"R2","loop":131,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_axis":"advanced_equipment_identity_vs_order_conversion_and_post_reprice_context","residual_summary":"The residual C09 error is not failure to detect equipment names; it is over-crediting scope proxies and under-applying 4B after price has already expressed the theme. Real process equipment can be early and high-convexity, but every row still needs order/revenue/margin conversion before Yellow/Green.","production_scoring_changed":false,"shadow_weight_only":true}
```

## 8. Validation scope

```text
validated_price_source: Songdaiki/stock-web
price_basis: tradable_raw
entry_price_basis: close_c_column
required_mfe_mae_fields_present: true
MFE_30D_pct / MFE_90D_pct / MFE_180D_pct: present for every usable trigger
MAE_30D_pct / MAE_90D_pct / MAE_180D_pct: present for every usable trigger
trigger_type_canonical_stage_label: true
corporate_action_contaminated_180D_window: false for all representative rows in local share-count check
insufficient_forward_window: false
hard_duplicate_key_checked_against_local_C09_files: true
production_scoring_changed: false
shadow_weight_only: true
```

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not execute during this research session.

Later coding agent task:
1. Copy this MD into docs/round/ with the exact filename.
2. Run the v12 calibration ingest pipeline only after a batch of MDs is collected.
3. Parse every JSONL row in section 7.
4. Enforce strict duplicate key = canonical_archetype_id + symbol + trigger_type + entry_date.
5. Treat C09_PROCESS_TOOL_COMPONENT_SCOPE_AND_REPRICE_GUARD as a shadow rule candidate only.
6. Do not change production scoring unless multiple independent C09 loops support the same axis.
```

## 10. References

- MAIN EXECUTION PROMPT: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
- NO-REPEAT INDEX: https://raw.githubusercontent.com/Songdaiki/stock_agent/main/docs/core/V12_Research_No_Repeat_Index.md
- stock-web manifest: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/manifest.json
- stock-web schema: https://raw.githubusercontent.com/Songdaiki/stock-web/main/atlas/schema.json
- 071280 로체시스템즈: https://www.rorze.com/en/products_category/wafer-transfer-system/
- 319660 피에스케이: https://www.pskinc.com/aboutpsk/overview.php
- 265520 AP시스템: https://www.apsystems.co.kr/eng/company/introduce.asp
- 232680 라온로보틱스: https://raonrobot.com/en/m11.php
- 419080 엔젯: https://enjet.co.kr/
- 417840 저스템: https://www.justem.co.kr/main/sub02_05_view.php?bo_uid=370&ps_page=1

## 11. Next research state

```text
completed_round = R2
completed_loop = 131
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0 / C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF / remote rows 10 / need_to_30 20
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes =
  - C14_EV_DEMAND_SLOWDOWN_4B_4C_followup_utilization_regime
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_followup_new_symbol_boundary
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY_followup_new_customer_route
  - C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_followup_new_order_route
  - C11_BATTERY_ORDERBOOK_RERATING_followup_margin_FCF_bridge
```
