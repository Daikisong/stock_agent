# E2R Stock-Web v12 Residual Research — R2 / L2 / C07 HBM Equipment Order Relative Strength

```text
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R2
selected_loop: 200
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality reinforcement: C07 has many rows but no hard 4C path and needs direct-order-vs-late-overheat cleanup.
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
production_scoring_changed: false
shadow_weight_only: true
```

## 1. Research objective

C07 has enough raw coverage, but the No-Repeat ledger shows `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` with `224 rows / 54 symbols / 4B-4C 42-0`. The residual problem is not row count. It is the boundary between:

- a **real supplier order bridge**: named customer, tool, supply contract, shipment, or repeat kit evidence; and
- a **relative-strength echo**: HBM-equipment language arriving after a large rerating, without fresh order/revenue/margin conversion.

The question is whether E2R should keep Stage2-Actionable for direct order rows while blocking Yellow/Green after high-MAE or post-peak evidence.

## 2. Price source validation

```text
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
tradable_columns: d,o,h,l,c,v,a,mc,s,m
```

Profile checks used:

```text
042700 Hanmi Semiconductor: corporate_action_candidate_dates = 2006-11-10, 2017-05-11, 2022-04-06; selected 2024 windows clean.
089030 Techwing: corporate_action_candidate_dates = 2011-12-13, 2011-12-29, 2022-08-01, 2022-08-23; selected 2024 window clean.
031980 PSK Holdings: corporate_action_candidate_dates = 1998-07-28, 2000-04-20, 2007-03-16, 2019-05-10, 2020-02-21; selected 2024 windows clean.
110990 DIT: corporate_action_candidate_dates = []; selected 2023/2025 windows clean.
```

No row uses a synthetic price. Every usable trigger row includes 30D/90D/180D MFE and MAE.

## 3. Novelty and duplicate check

```text
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + entry_date
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
usable_trigger_count: 7
source_reaudit_seed_count: 2
new_current_file_trigger_count: 5
unique_symbol_count: 4
source_proxy_only_count: 0
evidence_url_pending_count: 0
missing_required_mfe_mae_count: 0
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
```

Two Hanmi rows are retained as direct C07 representative anchors because they define the calibration boundary: the same customer-order evidence works early and becomes a 4B/Green brake after extreme extension. The other rows broaden the C07 rule into HBM test, reflow, and laser annealing equipment.

## 4. Trigger-level backtest table

| Symbol | Company | Trigger | Entry | Entry close | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | Peak | Role |
|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 042700 | Hanmi Semiconductor | Stage2-Actionable | 2024-03-25 | 97400 | 57.29/-2.05 | 101.44/-2.05 | 101.44/-28.75 | 2024-06-14 | direct_order_positive_high_mae_green_blocker |
| 042700 | Hanmi Semiconductor | Stage4B | 2024-06-10 | 160000 | 22.63/-7.13 | 22.63/-42.94 | 22.63/-56.62 | 2024-06-14 | late_direct_order_relative_strength_4b_guardrail |
| 089030 | Techwing | Stage2-Actionable | 2024-04-19 | 35400 | 27.68/-13.84 | 100.00/-13.84 | 100.00/-20.20 | 2024-07-11 | cube_prober_roadmap_positive_with_yellow_green_blocker |
| 031980 | PSK Holdings | Stage2-Actionable | 2024-06-03 | 55700 | 53.14/-5.03 | 53.14/-35.19 | 53.14/-50.27 | 2024-06-19 | micron_hbm_reflow_supplier_bridge_high_mae |
| 031980 | PSK Holdings | Stage4B | 2024-07-11 | 67400 | 3.41/-42.88 | 3.41/-50.52 | 3.41/-58.90 | 2024-07-11 | post_peak_no_fresh_order_relative_strength_reversal |
| 110990 | DIT | Stage3-Yellow | 2023-08-10 | 10740 | 28.96/-7.45 | 126.72/-7.45 | 201.21/-7.45 | 2024-04-26 | direct_laser_annealing_supply_positive_control |
| 110990 | DIT | Stage2-Actionable | 2025-01-15 | 14800 | 31.55/-4.73 | 31.55/-21.96 | 31.55/-25.20 | 2025-01-22 | additional_sk_hynix_kits_reorder_high_mae_cap |

## 5. Case notes

### 5.1 Hanmi Semiconductor / 042700 / direct TC-bonder order

The March 2024 SK hynix order is a clean Stage2-Actionable row because it is named-customer, named-equipment, and contract-based. The 180D MFE reached 101.44%, but the same window later carried -28.75% MAE and a -64.63% post-peak drawdown. The correct rule is not to delete Stage2-Actionable; it is to block Stage3-Green until revenue, margin, or repeat-order conversion is visible.

The June 2024 direct order is the mirror image. The evidence is still real, but by the next trading day the stock was already in a late extension band. The forward path had only 22.63% MFE and -56.62% MAE. That is local Stage4B / Green blocker territory, not fresh Yellow/Green.

### 5.2 Techwing / 089030 / HBM cube prober

Techwing's cube-prober evidence is C07-relevant because it is HBM test equipment, but early 2024 evidence still mixed product roadmap, expected qualification, and future sales start. The forward path was strong, yet the second bridge was not yet a named order or recognized revenue. The calibration should allow Stage2-Actionable only when the product roadmap is backed by customer qualification or launch timing, and it should block Yellow/Green until order/revenue conversion appears.

### 5.3 PSK Holdings / 031980 / Micron HBM reflow versus post-peak echo

PSK's Micron HBM reflow row is one of the strongest supplier-bridge cases in this batch. TheElec reported Micron supply and described PSK's Samsung/SK hynix/Micron footprint. The forward path still had -50.27% 180D MAE, so C07 should preserve Actionable while applying a Green brake.

The July 2024 PSK row demonstrates the opposite edge: after the peak, the same HBM equipment narrative without fresh order/margin evidence should be local 4B, not a renewed positive trigger.

### 5.4 DIT / 110990 / laser annealing equipment

The 2023 DIT row is a positive control: direct SK hynix laser annealing supply, low MAE, and massive forward upside. Stage3-Yellow is defensible, but Green still waits for reported revenue, margin, and FCF conversion.

The 2025 DIT row is a repeat-order reopen. Additional SK hynix laser annealing kits justify Stage2-Actionable again, but immediate peak behavior and -25.20% 180D MAE keep Yellow/Green blocked.

## 6. Residual contribution summary

```text
rule_candidate: C07_HBM_EQUIPMENT_ORDER_BRIDGE_AND_OVERHEAT_GATE_V2
sector_rule_candidate: L2_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE

core_residual:
- Named customer + named tool + supply contract/repeat kit can preserve Stage2-Actionable.
- Product roadmap, HBM exposure, or customer qualification expectation alone stays capped until conversion evidence appears.
- Late direct-order evidence after a large rerating routes to Stage4B/watch or Green blocker before any Yellow/Green upgrade.
- High MAE on a real direct supplier row blocks Yellow/Green first; it does not erase Stage2-Actionable.
- Hard 4C requires confirmed non-price thesis break: order cancellation, failed customer qualification, revenue/margin collapse, or weak offset quality.
```

## 7. Current calibrated profile stress test

```text
current_default_profile_proxy: e2r_2_1_stock_web_calibrated / e2r_2_2 rolling-style active profile
stage2_actionable_evidence_bonus: +2.0
stage3_yellow_total_min: 75.0
stage3_green_total_min: 87.0
stage3_green_revision_min: 55.0
price_only_blowoff_blocks_positive_stage: true
full_4b_requires_non_price_evidence: true
hard_4c_thesis_break_routes_to_4c: true
```

Verdict:

```text
- The global Green strictness remains correct.
- C07 needs a canonical-specific second-bridge gate rather than a new global threshold.
- Direct order rows should not be punished as false positives merely because MAE is deep.
- Late relative-strength rows should not be promoted just because the customer/order headline is real.
```

## 8. Machine-readable JSONL

```jsonl
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_01_042700_2024-03-25_Stage2Actionable","trigger_id":"C07_200_042700_2024-03-25_Stage2Actionable","symbol":"042700","company_name":"Hanmi Semiconductor","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-22","entry_date":"2024-03-25","entry_price":97400.0,"actual_1d_ohlc_row":{"d":"2024-03-25","o":95700.0,"h":101900.0,"l":95400.0,"c":97400.0,"v":3839354},"MFE_30D_pct":57.29,"MAE_30D_pct":-2.05,"MFE_90D_pct":101.44,"MAE_90D_pct":-2.05,"MFE_180D_pct":101.44,"MAE_180D_pct":-28.75,"peak_180D_date":"2024-06-14","peak_180D_price":196200.0,"drawdown_after_peak_pct":-64.63,"evidence_summary":"SK hynix direct TC bonder order; supplier-level customer/order evidence, not just HBM beta.","evidence_family":["direct_customer_order","HBM_TC_bonder","SK_Hynix","supplier_level_order_conversion"],"source_url":"https://www.kedglobal.com/korean-chipmakers/newsView/ked202403220008","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage2-Actionable|2024-03-25","dedupe_for_aggregate":true,"case_role":"direct_order_positive_high_mae_green_blocker","source_sector_reaudit_seed":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage2-Actionable|2024-03-25","symbol":"042700","company_name":"Hanmi Semiconductor","trigger_type":"Stage2-Actionable","entry_date":"2024-03-25","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":17,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":3,"information_confidence":16},"stage_after_current_profile":"Stage2-Actionable","stage_after_shadow_rule":"Stage2-Actionable","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_02_042700_2024-06-10_Stage4B","trigger_id":"C07_200_042700_2024-06-10_Stage4B","symbol":"042700","company_name":"Hanmi Semiconductor","trigger_type":"Stage4B","trigger_date":"2024-06-07","entry_date":"2024-06-10","entry_price":160000.0,"actual_1d_ohlc_row":{"d":"2024-06-10","o":159700.0,"h":161100.0,"l":156800.0,"c":160000.0,"v":1233444},"MFE_30D_pct":22.63,"MAE_30D_pct":-7.13,"MFE_90D_pct":22.63,"MAE_90D_pct":-42.94,"MFE_180D_pct":22.63,"MAE_180D_pct":-56.62,"peak_180D_date":"2024-06-14","peak_180D_price":196200.0,"drawdown_after_peak_pct":-64.63,"evidence_summary":"Large disclosed TC bonder order arrived after a steep rerating; direct evidence remains valid but should act as 4B/Green brake after extension.","evidence_family":["direct_customer_order","late_cycle_order","relative_strength_overheat","green_blocker"],"source_url":"https://www.kedglobal.com/korean-chipmakers/newsView/ked202406070008","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/042/042700/2024.csv","profile_path":"atlas/symbol_profiles/042/042700.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage4B|2024-06-10","dedupe_for_aggregate":true,"case_role":"late_direct_order_relative_strength_4b_guardrail","source_sector_reaudit_seed":true,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|042700|Stage4B|2024-06-10","symbol":"042700","company_name":"Hanmi Semiconductor","trigger_type":"Stage4B","entry_date":"2024-06-10","raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":17,"bottleneck_pricing":15,"market_mispricing":7,"valuation_rerating":4,"capital_allocation":3,"information_confidence":16},"stage_after_current_profile":"Stage4B","stage_after_shadow_rule":"Stage4B","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_03_089030_2024-04-19_Stage2Actionable","trigger_id":"C07_200_089030_2024-04-19_Stage2Actionable","symbol":"089030","company_name":"Techwing","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-19","entry_date":"2024-04-19","entry_price":35400.0,"actual_1d_ohlc_row":{"d":"2024-04-19","o":37100.0,"h":37650.0,"l":32400.0,"c":35400.0,"v":1944619},"MFE_30D_pct":27.68,"MAE_30D_pct":-13.84,"MFE_90D_pct":100.0,"MAE_90D_pct":-13.84,"MFE_180D_pct":100.0,"MAE_180D_pct":-20.2,"peak_180D_date":"2024-07-11","peak_180D_price":70800.0,"drawdown_after_peak_pct":-60.03,"evidence_summary":"Cube prober / HBM test equipment roadmap and expected customer qualification create Actionable, but not Yellow/Green until actual customer order or revenue conversion.","evidence_family":["HBM_test_equipment","cube_prober","customer_qualification_pending","product_roadmap"],"source_url":"https://www.asiae.co.kr/en/article/2024031315391648405","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/089/089030/2024.csv","profile_path":"atlas/symbol_profiles/089/089030.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage2-Actionable|2024-04-19","dedupe_for_aggregate":true,"case_role":"cube_prober_roadmap_positive_with_yellow_green_blocker","source_sector_reaudit_seed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|089030|Stage2-Actionable|2024-04-19","symbol":"089030","company_name":"Techwing","trigger_type":"Stage2-Actionable","entry_date":"2024-04-19","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":12,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":3,"information_confidence":18},"stage_after_current_profile":"Stage2-Actionable","stage_after_shadow_rule":"Stage2-Actionable","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_04_031980_2024-06-03_Stage2Actionable","trigger_id":"C07_200_031980_2024-06-03_Stage2Actionable","symbol":"031980","company_name":"PSK Holdings","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-31","entry_date":"2024-06-03","entry_price":55700.0,"actual_1d_ohlc_row":{"d":"2024-06-03","o":56400.0,"h":56500.0,"l":52900.0,"c":55700.0,"v":223818},"MFE_30D_pct":53.14,"MAE_30D_pct":-5.03,"MFE_90D_pct":53.14,"MAE_90D_pct":-35.19,"MFE_180D_pct":53.14,"MAE_180D_pct":-50.27,"peak_180D_date":"2024-06-19","peak_180D_price":85300.0,"drawdown_after_peak_pct":-67.53,"evidence_summary":"TheElec reported HBM reflow equipment supplied to Micron; that is direct customer/supplier bridge, but the forward path had very deep MAE.","evidence_family":["direct_customer_supply","Micron","HBM_reflow","all_three_DRAM_makers"],"source_url":"https://www.thelec.net/news/articleView.html?idxno=4859","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-06-03","dedupe_for_aggregate":true,"case_role":"micron_hbm_reflow_supplier_bridge_high_mae","source_sector_reaudit_seed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-06-03","symbol":"031980","company_name":"PSK Holdings","trigger_type":"Stage2-Actionable","entry_date":"2024-06-03","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":12,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":3,"information_confidence":18},"stage_after_current_profile":"Stage2-Actionable","stage_after_shadow_rule":"Stage2-Actionable","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_05_031980_2024-07-11_Stage4B","trigger_id":"C07_200_031980_2024-07-11_Stage4B","symbol":"031980","company_name":"PSK Holdings","trigger_type":"Stage4B","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":67400.0,"actual_1d_ohlc_row":{"d":"2024-07-11","o":68900.0,"h":69700.0,"l":66600.0,"c":67400.0,"v":361527},"MFE_30D_pct":3.41,"MAE_30D_pct":-42.88,"MFE_90D_pct":3.41,"MAE_90D_pct":-50.52,"MFE_180D_pct":3.41,"MAE_180D_pct":-58.9,"peak_180D_date":"2024-07-11","peak_180D_price":69700.0,"drawdown_after_peak_pct":-60.26,"evidence_summary":"Same HBM supplier thesis after the price peak lacked fresh order/revenue follow-through; route to local 4B rather than sticky hard 4C absent issuer thesis break.","evidence_family":["post_peak_entry","stale_supplier_thesis","relative_strength_reversal","no_fresh_order"],"source_url":"https://www.thelec.net/news/articleView.html?idxno=4859","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage4B|2024-07-11","dedupe_for_aggregate":true,"case_role":"post_peak_no_fresh_order_relative_strength_reversal","source_sector_reaudit_seed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage4B|2024-07-11","symbol":"031980","company_name":"PSK Holdings","trigger_type":"Stage4B","entry_date":"2024-07-11","raw_component_score_breakdown":{"eps_fcf_explosion":8,"earnings_visibility":12,"bottleneck_pricing":15,"market_mispricing":7,"valuation_rerating":4,"capital_allocation":3,"information_confidence":18},"stage_after_current_profile":"Stage4B","stage_after_shadow_rule":"Stage4B","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_06_110990_2023-08-10_Stage3Yellow","trigger_id":"C07_200_110990_2023-08-10_Stage3Yellow","symbol":"110990","company_name":"DIT","trigger_type":"Stage3-Yellow","trigger_date":"2023-08-10","entry_date":"2023-08-10","entry_price":10740.0,"actual_1d_ohlc_row":{"d":"2023-08-10","o":11120.0,"h":11220.0,"l":10420.0,"c":10740.0,"v":332064},"MFE_30D_pct":28.96,"MAE_30D_pct":-7.45,"MFE_90D_pct":126.72,"MAE_90D_pct":-7.45,"MFE_180D_pct":201.21,"MAE_180D_pct":-7.45,"peak_180D_date":"2024-04-26","peak_180D_price":32350.0,"drawdown_after_peak_pct":-21.23,"evidence_summary":"TheElec reported DIT had begun supplying laser annealing equipment to SK hynix; direct customer/process evidence with low MAE supports Yellow, but Green still waits for reported revenue/margin.","evidence_family":["direct_customer_supply","SK_Hynix","laser_annealing","HBM3E_process"],"source_url":"https://www.thelec.net/news/articleView.html?idxno=4615","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2023.csv","profile_path":"atlas/symbol_profiles/110/110990.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage3-Yellow|2023-08-10","dedupe_for_aggregate":true,"case_role":"direct_laser_annealing_supply_positive_control","source_sector_reaudit_seed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage3-Yellow|2023-08-10","symbol":"110990","company_name":"DIT","trigger_type":"Stage3-Yellow","entry_date":"2023-08-10","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":17,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":3,"information_confidence":18},"stage_after_current_profile":"Stage3-Yellow","stage_after_shadow_rule":"Stage3-Yellow","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"trigger","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","case_id":"C07_200_07_110990_2025-01-15_Stage2Actionable","trigger_id":"C07_200_110990_2025-01-15_Stage2Actionable","symbol":"110990","company_name":"DIT","trigger_type":"Stage2-Actionable","trigger_date":"2025-01-15","entry_date":"2025-01-15","entry_price":14800.0,"actual_1d_ohlc_row":{"d":"2025-01-15","o":14500.0,"h":14960.0,"l":14500.0,"c":14800.0,"v":116664},"MFE_30D_pct":31.55,"MAE_30D_pct":-4.73,"MFE_90D_pct":31.55,"MAE_90D_pct":-21.96,"MFE_180D_pct":31.55,"MAE_180D_pct":-25.2,"peak_180D_date":"2025-01-22","peak_180D_price":19470.0,"drawdown_after_peak_pct":-43.04,"evidence_summary":"Additional laser annealing kit supply to SK hynix reopens Actionable; immediate peak and 180D MAE keep Yellow/Green blocked.","evidence_family":["repeat_order","additional_kits","SK_Hynix","laser_annealing"],"source_url":"https://www.thelec.net/news/articleView.html?idxno=5112","source_proxy_only":false,"evidence_url_pending":false,"price_data_source":"Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/110/110990/2025.csv","profile_path":"atlas/symbol_profiles/110/110990.json","stock_web_manifest_max_date":"2026-02-20","corporate_action_window_status":"clean_180D_window","calibration_usable":true,"calibration_block_reasons":[],"same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage2-Actionable|2025-01-15","dedupe_for_aggregate":true,"case_role":"additional_sk_hynix_kits_reorder_high_mae_cap","source_sector_reaudit_seed":false,"production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"score_simulation","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_ref":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|110990|Stage2-Actionable|2025-01-15","symbol":"110990","company_name":"DIT","trigger_type":"Stage2-Actionable","entry_date":"2025-01-15","raw_component_score_breakdown":{"eps_fcf_explosion":17,"earnings_visibility":17,"bottleneck_pricing":15,"market_mispricing":10,"valuation_rerating":8,"capital_allocation":3,"information_confidence":18},"stage_after_current_profile":"Stage2-Actionable","stage_after_shadow_rule":"Stage2-Actionable","stage3_green_allowed":false,"residual_reason":"direct_order_or_supplier_bridge_preserves_actionable_but_high_MAE_or_late_entry_blocks_green","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"aggregate","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_EQUIPMENT_DIRECT_ORDER_VS_RELATIVE_STRENGTH_OVERHEAT_GATE_V2","trigger_count":7,"unique_symbol_count":4,"stage2_actionable_count":4,"stage3_yellow_count":1,"stage4b_count":2,"hard_4c_count":0,"source_reaudit_seed_count":2,"source_proxy_only_count":0,"evidence_url_pending_count":0,"missing_required_mfe_mae_count":0,"production_scoring_changed":false,"shadow_weight_only":true,"residual_conclusion":"C07 needs a supplier-order bridge to preserve Stage2-Actionable, while late relative-strength evidence should be capped to 4B/Green blocker unless revenue/margin conversion repeats."}
{"row_type":"shadow_weight","schema_version":"e2r_stock_web_v12_residual.v1","research_file":"e2r_stock_web_v12_residual_round_R2_loop_200_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md","selected_round":"R2","selected_loop":200,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","candidate_rule_id":"C07_HBM_EQUIPMENT_ORDER_BRIDGE_AND_OVERHEAT_GATE_V2","production_scoring_changed":false,"shadow_weight_only":true,"axis_strengthened":["stage2_required_bridge","stage3_green_not_loosened","late_relative_strength_4b_watch"],"proposed_delta":"no_global_delta; canonical_shadow_only; increase information_confidence only for named customer order, reduce valuation_rerating credit after post-peak relative strength","confidence":"medium"}
```

## 9. Batch Ingest Self-Audit

```text
ready_for_batch_ingest: true
standard_v12_filename: true
filename_round_matches_metadata: true
filename_loop_matches_metadata: true
selected_round: R2
selected_loop: 200
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
invalid_round_sector_pair: false
all_usable_triggers_have_30_90_180_mfe_mae: true
actual_1d_ohlc_row_present_for_each_trigger: true
entry_price_present_for_each_trigger: true
corporate_action_contaminated_180D_count: 0
insufficient_forward_window_180D_count: 0
source_proxy_only_count: 0
evidence_url_pending_count: 0
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batch-applying v12 residual MDs later, parse this file as a C07 canonical shadow-rule candidate.
Candidate rule id:
C07_HBM_EQUIPMENT_ORDER_BRIDGE_AND_OVERHEAT_GATE_V2

Required implementation review:
1. Do not loosen global Stage3-Green.
2. For C07 only, preserve Stage2-Actionable when evidence includes named customer + named HBM equipment + contract/supply/repeat kit.
3. Cap product-roadmap / HBM-equipment-profile evidence at Stage2 unless customer qualification, order, shipment, or recognized revenue appears.
4. Route post-peak direct-order evidence to Stage4B/watch or Green blocker when 90D/180D MAE is deep and no fresh conversion bridge appears.
5. Hard 4C requires order cancellation, failed qualification, supplier revenue/margin collapse, or weak offset quality.
6. Do not alter production scoring unless multiple MDs confirm the same C07 rule.
```

## 11. Next Research State

```text
completed_round: R2
completed_loop: 200
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority quality reinforcement / C07 4B-4C boundary and direct URL repair
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_EX_SUBSIDY_MARGIN_DIRECT_REPAIR
- C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_DIRECT_OFFTAKE_POSITIVE_CONTROL_REPAIR
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
- R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_OFFSET_QUALITY_REFRESH
```
