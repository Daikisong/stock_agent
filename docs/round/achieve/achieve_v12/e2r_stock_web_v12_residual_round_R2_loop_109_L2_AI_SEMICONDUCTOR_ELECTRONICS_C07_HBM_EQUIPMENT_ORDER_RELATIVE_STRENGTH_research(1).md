---
title: "E2R Stock-Web V12 Residual Research — R2 Loop 109 — C07 HBM Equipment Order Relative Strength"
created_at_kst: "2026-06-13"
mode: "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12"
selected_round: "R2"
selected_loop: 109
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
large_sector_id: "L2_AI_SEMICONDUCTOR_ELECTRONICS"
canonical_archetype_id: "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH"
fine_archetype_id: "C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE"
deep_sub_archetype_id: "C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE"
stock_web_manifest_max_date: "2026-02-20"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_executed_now: false
---

# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id = C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE
deep_sub_archetype_id = C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE
```

This is a standalone historical calibration artifact. It is not a live scan, not a watchlist, not investment advice, not a code patch, and not a production scoring change. It follows the coverage-index-first scheduler. `V12_Research_No_Repeat_Index.md` is used only as the duplicate-avoidance and coverage ledger.

## 1. Current Calibrated Profile Assumption

Assumed current profile proxy: `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as constraints, not rediscoveries:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop asks a narrower C07 question: **when does HBM / advanced-packaging equipment relative strength carry verified order or revenue conversion, and when is it only a theme label sitting on top of price momentum?**

## 2. Coverage / Scheduler Decision

The published No-Repeat Index reports `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` as Priority 0 with 18 representative rows and 12 rows needed to reach the 30-row minimum stability zone. In this local session, previous C07 artifacts were loop107 and loop108. Those used the following C07 symbols and were excluded from this loop:

```text
loop107 = 281820, 253590, 092870, 064290, 322310, 083450, 348210
loop108 = 232140, 319660, 240810, 089890, 382800, 217190
```

This loop adds seven new C07 symbols and seven new trigger families.

```text
C07 published index rows = 18
local C07 loop107 representative triggers = 7
local C07 loop108 representative triggers = 6
this loop representative triggers = 7
local-session adjusted C07 rows after loop109 = 38
remaining to 30 = 0
remaining to 50 = 12
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

## 3. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_name = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

The stock-web manifest basis used for this loop is `raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `raw_row_count=15214118`, and `symbol_count=5414`. Every representative trigger row below includes the canonical 30D/90D/180D MFE/MAE fields.

## 4. Historical Eligibility Gate

All representative rows use historical trigger dates before the stock-web manifest max date and have 180 trading-day forward windows in the downloaded stock-web CSV shards. Corporate action screening was handled by symbol profile review. 2024/2025 windows were clean for the seven representative rows; one extra Zeus row is included only as narrative-only because its stock-web profile flags 2024 corporate-action candidate dates inside the D+180 window.

## 5. Canonical Archetype Compression Map

| level | id | meaning |
|---|---|---|
| large sector | `L2_AI_SEMICONDUCTOR_ELECTRONICS` | AI / semiconductor / electronics historical calibration |
| canonical | `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` | HBM equipment relative strength that must convert into order/revenue/margin evidence |
| fine | `C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE` | advanced-packaging, process, metrology, chiller, environment-control, transfer equipment split by conversion quality |
| deep | `C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE` | direct order/revenue conversion versus source-proxy-only label and local price blowoff |

## 6. Case Selection Summary

| case | symbol | company | trigger | entry_date | entry_price | role | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | current verdict |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C07-R2-L109-031980 | 031980 | 피에스케이홀딩스 | Stage2-Actionable | 2024-05-30 | 54,900 | positive | 55.37% | -5.10% | 55.37% | -34.24% | 55.37% | -49.54% | current_profile_correct_if_Yellow_requires_direct_customer_order_and_Green_blocked_by_post_peak_drawdown |
| C07-R2-L109-396470 | 396470 | 워트 | Stage2-Actionable | 2024-04-01 | 10,300 | positive | 40.29% | -5.05% | 77.57% | -13.20% | 77.57% | -37.18% | current_profile_too_conservative_if_auxiliary_equipment_proxy_zeroed_out_but_Green_should_remain_blocked |
| C07-R2-L109-140860 | 140860 | 파크시스템스 | Stage3-Yellow | 2024-12-13 | 213,000 | positive | 17.37% | -7.00% | 17.37% | -14.88% | 45.54% | -14.88% | current_profile_too_conservative_if_hybrid_bonding_metrology_not_recognized_as_C07_Yellow |
| C07-R2-L109-036810 | 036810 | 에프에스티 | Stage2-Actionable | 2024-10-25 | 17,250 | positive | 12.23% | -10.72% | 39.42% | -17.74% | 39.42% | -17.74% | current_profile_missed_actionable_if_high_ASP_chiller_bridge_not_counted |
| C07-R2-L109-084370 | 084370 | 유진테크 | Stage2-Actionable | 2024-01-05 | 40,650 | positive | 15.62% | -20.79% | 44.40% | -20.79% | 47.60% | -20.79% | current_profile_correct_as_actionable_but_Green_should_be_blocked_by_high_MAE_and_proxy_order |
| C07-R2-L109-039030 | 039030 | 이오테크닉스 | Stage4B | 2024-04-26 | 239,500 | counterexample | 6.89% | -19.92% | 6.89% | -45.97% | 6.89% | -52.61% | current_profile_false_positive_if_laser_HBM_label_promoted_without_order_revenue_bridge |
| C07-R2-L109-160980 | 160980 | 싸이맥스 | Stage4B | 2024-03-21 | 20,000 | counterexample | 14.25% | -16.85% | 18.75% | -24.85% | 18.75% | -62.95% | current_profile_false_positive_if_hidden_beneficiary_relative_strength_promoted_without_order_revenue_bridge |


## 7. Case Notes

### C07-R2-L109-031980 — 피에스케이홀딩스

This is the cleanest direct C07 bridge in the loop. The evidence points to HBM reflow equipment supply to Micron and Big-3 customer coverage. Stock-web confirms strong 30D/90D/180D MFE, but the large post-peak drawdown means C07 should reward order conversion while still capping Green until margin/revision durability is visible.

### C07-R2-L109-396470 — 워트

Wort is an auxiliary-equipment proxy: HBM/debonding raises the need for tight environment control, but the source is not a direct order row. The price path worked, so the current profile should not zero it out; however, this remains Stage2-Actionable with a bridge requirement rather than free Yellow/Green.

### C07-R2-L109-140860 — 파크시스템스

Park Systems is a delayed positive. Hybrid bonding metrology was described as a future revenue bridge, and the 180D path confirms that C07 can be too conservative when metrology bottleneck evidence is present. Because the near-term 90D MFE is modest, the row supports Yellow only when a revenue reflection timetable is visible.

### C07-R2-L109-036810 — 에프에스티

FST is an ASP-bridge case rather than a direct HBM order case. Cryogenic chiller pricing and advanced process relevance justify Actionable credit, but not Green. The path supports a Stage2 bridge rule for auxiliary process equipment whose ASP bridge is explicit.

### C07-R2-L109-084370 — 유진테크

Eugene Tech shows why C07 and C10 overlap must be compressed carefully. HBM/advanced-DRAM capex supported a good 90D/180D MFE, but the MAE was high. The right treatment is Stage2-Actionable with High-MAE guard, not unguarded Stage3-Green.

### C07-R2-L109-039030 — 이오테크닉스

This is the first clean counterexample. The HBM laser-packaging narrative arrived after substantial repricing. Stock-web shows only +6.89% MFE and deep 90D/180D MAE. C07 should not let a laser/HBM label unlock Yellow without verified order or revenue conversion.

### C07-R2-L109-160980 — 싸이맥스

This is the second clean counterexample. The hidden-beneficiary narrative was plausible, but the price path shows a small MFE and very large 180D MAE. The rule implication is direct: hidden-beneficiary relative strength should be Stage4B-watch until order/revenue bridge appears.

### Narrative-only validation: 079370 제우스

Zeus has highly relevant HBM cleaning-equipment evidence, but it is excluded from representative calibration because the stock-web profile flags corporate-action candidate dates on 2024-01-16 and 2024-02-08, inside the D+180 window for the January 2024 evidence date. This row is useful for future URL/evidence repair but not usable for promotion in raw-unadjusted OHLC.

## 8. 4B Local vs Full Window Split

Two representative rows are explicit Stage4B-watch paths.

| symbol | company | trigger_date | local peak proximity | full-window peak proximity | verdict |
|---:|---|---:|---:|---:|---|
| 039030 | 이오테크닉스 | 2024-04-26 | 0.94 | 0.94 | HBM laser label arrived near local/full-window peak; direct order bridge missing |
| 160980 | 싸이맥스 | 2024-03-21 | 0.88 | 0.84 | hidden-beneficiary RS faded; order/revenue bridge missing |

C07 4B split rule candidate:

```text
if C07 evidence is source_proxy_only or label-driven
and no verified equipment supply/order/revenue conversion is present
and price is within 0.85~1.00 of 30D or 180D peak,
then cap at Stage2 or route to Stage4B-Watch, not Stage3-Yellow/Green.
```

## 9. Machine-Readable Rows JSONL

```jsonl
{"row_type":"case","case_id":"C07-R2-L109-031980","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"direct_customer_order_conversion_high_mfe_high_drawdown","positive_or_counterexample":"positive","best_trigger":"C07-R2-L109-031980-Stage2Actionable-2024-05-30","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_post_peak_guard_needed","current_profile_verdict":"current_profile_correct_if_Yellow_requires_direct_customer_order_and_Green_blocked_by_post_peak_drawdown","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-396470","symbol":"396470","company_name":"워트","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"auxiliary_environment_control_hbm_proxy_success","positive_or_counterexample":"positive","best_trigger":"C07-R2-L109-396470-Stage2Actionable-2024-04-01","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_proxy_but_no_green_unlock","current_profile_verdict":"current_profile_too_conservative_if_auxiliary_equipment_proxy_zeroed_out_but_Green_should_remain_blocked","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-140860","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"hybrid_bonding_metrology_delayed_positive","positive_or_counterexample":"positive","best_trigger":"C07-R2-L109-140860-Stage3Yellow-2024-12-13","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_delayed_180D_mfe","current_profile_verdict":"current_profile_too_conservative_if_hybrid_bonding_metrology_not_recognized_as_C07_Yellow","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-036810","symbol":"036810","company_name":"에프에스티","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"cryo_chiller_asp_bridge_positive","positive_or_counterexample":"positive","best_trigger":"C07-R2-L109-036810-Stage2Actionable-2024-10-25","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_ASP_bridge_not_green","current_profile_verdict":"current_profile_missed_actionable_if_high_ASP_chiller_bridge_not_counted","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-084370","symbol":"084370","company_name":"유진테크","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"advanced_dram_hbm_capex_equipment_positive_high_mae","positive_or_counterexample":"positive","best_trigger":"C07-R2-L109-084370-Stage2Actionable-2024-01-05","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_but_high_MAE_guard","current_profile_verdict":"current_profile_correct_as_actionable_but_Green_should_be_blocked_by_high_MAE_and_proxy_order","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-039030","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"laser_hbm_label_after_price_run_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C07-R2-L109-039030-Stage4B-2024-04-26","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_filtered_to_4B_watch","current_profile_verdict":"current_profile_false_positive_if_laser_HBM_label_promoted_without_order_revenue_bridge","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"case","case_id":"C07-R2-L109-160980","symbol":"160980","company_name":"싸이맥스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","case_type":"hidden_hbm_beneficiary_relative_strength_counterexample","positive_or_counterexample":"counterexample","best_trigger":"C07-R2-L109-160980-Stage4B-2024-03-21","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_filtered_or_4B_guarded","current_profile_verdict":"current_profile_false_positive_if_hidden_beneficiary_relative_strength_promoted_without_order_revenue_bridge","price_source":"Songdaiki/stock-web","notes":"new C07 symbol for loop109; previous C07 loop107/108 symbols excluded"}
{"row_type":"trigger","trigger_id":"C07-R2-L109-031980-Stage2Actionable-2024-05-30","case_id":"C07-R2-L109-031980","symbol":"031980","company_name":"피에스케이홀딩스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-05-30","entry_date":"2024-05-30","entry_price":54900.0,"evidence_available_at_that_date":"TheElec reported that PSK Holdings supplied reflow equipment to Micron in 1Q24 and that the equipment is used for HBM mass production; this gives C07 a verified customer/order bridge, not only an HBM label.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=28196","stage2_evidence_fields":["verified_HBM_reflow_equipment_supply","Micron_customer_route","advanced_packaging_order_bridge"],"stage3_evidence_fields":["direct_big3_customer_presence","revenue_conversion_expected_but_margin_bridge_partial"],"stage4b_evidence_fields":["post_peak_drawdown_risk_after_fast_repricing"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv","profile_path":"atlas/symbol_profiles/031/031980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":55.37,"MFE_90D_pct":55.37,"MFE_180D_pct":55.37,"MAE_30D_pct":-5.1,"MAE_90D_pct":-34.24,"MAE_180D_pct":-49.54,"peak_date":"2024-06-19","peak_price":85300.0,"drawdown_after_peak_pct":-67.53,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger_but_post_peak_guard_checked","trigger_outcome_label":"positive_direct_hbm_reflow_order_but_needs_post_peak_4B_watch","current_profile_verdict":"current_profile_correct_if_Yellow_requires_direct_customer_order_and_Green_blocked_by_post_peak_drawdown","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|031980|Stage2-Actionable|2024-05-30","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-396470-Stage2Actionable-2024-04-01","case_id":"C07-R2-L109-396470","symbol":"396470","company_name":"워트","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":10300.0,"evidence_available_at_that_date":"KIPOST described Wort THC/TCU/FFU environment-control equipment and management comments that HBM/debonding back-end use was expanding. This is a C07 auxiliary-equipment proxy, not a direct HBM order row.","evidence_source":"https://www.kipost.net/news/articleView.html?idxno=313257","stage2_evidence_fields":["HBM_backend_environment_control_proxy","THC_TCU_FFU_equipment_route","capacity_supporting_auxiliary_equipment"],"stage3_evidence_fields":["relative_strength_with_forward_MFE","customer_route_proxy_only"],"stage4b_evidence_fields":["proxy_label_requires_order_bridge_before_Green"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/396/396470/2024.csv","profile_path":"atlas/symbol_profiles/396/396470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":40.29,"MFE_90D_pct":77.57,"MFE_180D_pct":77.57,"MAE_30D_pct":-5.05,"MAE_90D_pct":-13.2,"MAE_180D_pct":-37.18,"peak_date":"2024-06-26","peak_price":18290.0,"drawdown_after_peak_pct":-64.63,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger_but_post_peak_guard_checked","trigger_outcome_label":"positive_auxiliary_equipment_proxy_with_90D_MFE_but_requires_bridge_cap","current_profile_verdict":"current_profile_too_conservative_if_auxiliary_equipment_proxy_zeroed_out_but_Green_should_remain_blocked","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|396470|Stage2-Actionable|2024-04-01","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-140860-Stage3Yellow-2024-12-13","case_id":"C07-R2-L109-140860","symbol":"140860","company_name":"파크시스템스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Yellow","trigger_date":"2024-12-13","entry_date":"2024-12-13","entry_price":213000.0,"evidence_available_at_that_date":"TheElec described AFM metrology relevance for hybrid bonding and Park Systems comments that hybrid-bonding related sales would begin to be reflected from the following year, making it a verified metrology bridge rather than pure label strength.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=31680","stage2_evidence_fields":["hybrid_bonding_metrology_need","wafer_AFMs_process_control","customer_specific_solution_route"],"stage3_evidence_fields":["revenue_bridge_next_year_guidance","metrology_bottleneck_linkage"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/140/140860/2024.csv","profile_path":"atlas/symbol_profiles/140/140860.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":17.37,"MFE_90D_pct":17.37,"MFE_180D_pct":45.54,"MAE_30D_pct":-7.0,"MAE_90D_pct":-14.88,"MAE_180D_pct":-14.88,"peak_date":"2025-07-14","peak_price":310000.0,"drawdown_after_peak_pct":-23.87,"green_lateness_ratio":0.61,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger_but_post_peak_guard_checked","trigger_outcome_label":"positive_delayed_hybrid_bonding_metrology_bridge","current_profile_verdict":"current_profile_too_conservative_if_hybrid_bonding_metrology_not_recognized_as_C07_Yellow","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|140860|Stage3-Yellow|2024-12-13","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-036810-Stage2Actionable-2024-10-25","case_id":"C07-R2-L109-036810","symbol":"036810","company_name":"에프에스티","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-10-25","entry_date":"2024-10-25","entry_price":17250.0,"evidence_available_at_that_date":"TheBell reported that cryogenic etch chillers are a core equipment piece and that FST indicated the cryogenic chiller price is more than 2.5x conventional chillers; this is a price/ASP bridge but still not a direct HBM order bridge.","evidence_source":"https://www.thebell.co.kr/front/newsview.asp?key=202410251619163280105220","stage2_evidence_fields":["cryo_chiller_equipment_ASP_bridge","advanced_memory_process_support","equipment_price_uplift"],"stage3_evidence_fields":["margin_bridge_partial","direct_order_url_not_confirmed"],"stage4b_evidence_fields":["Green_block_until_order_revenue_revision_bridge"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036810/2024.csv","profile_path":"atlas/symbol_profiles/036/036810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.23,"MFE_90D_pct":39.42,"MFE_180D_pct":39.42,"MAE_30D_pct":-10.72,"MAE_90D_pct":-17.74,"MAE_180D_pct":-17.74,"peak_date":"2025-02-25","peak_price":24050.0,"drawdown_after_peak_pct":-34.05,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger_but_post_peak_guard_checked","trigger_outcome_label":"positive_chiller_ASP_bridge_with_order_bridge_still_missing","current_profile_verdict":"current_profile_missed_actionable_if_high_ASP_chiller_bridge_not_counted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|036810|Stage2-Actionable|2024-10-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-084370-Stage2Actionable-2024-01-05","case_id":"C07-R2-L109-084370","symbol":"084370","company_name":"유진테크","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-05","entry_date":"2024-01-05","entry_price":40650.0,"evidence_available_at_that_date":"TheElec reported that Samsung Electronics and SK Hynix investment recovery was concentrated on HBM and advanced DRAM, and named Eugene Tech among 1b-related equipment suppliers; it is a memory-equipment bridge but not a direct HBM order row.","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=25122","stage2_evidence_fields":["advanced_DRAM_HBM_capex_route","memory_customer_equipment_supplier","order_cycle_recovery_proxy"],"stage3_evidence_fields":["MFE90_supports_actionable","high_MAE_blocks_green"],"stage4b_evidence_fields":["drawdown_guard_needed_after_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv","profile_path":"atlas/symbol_profiles/084/084370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":15.62,"MFE_90D_pct":44.4,"MFE_180D_pct":47.6,"MAE_30D_pct":-20.79,"MAE_90D_pct":-20.79,"MAE_180D_pct":-20.79,"peak_date":"2024-05-28","peak_price":60000.0,"drawdown_after_peak_pct":-41.08,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_a_4B_trigger_but_post_peak_guard_checked","trigger_outcome_label":"positive_memory_capex_equipment_with_high_MAE_guardrail","current_profile_verdict":"current_profile_correct_as_actionable_but_Green_should_be_blocked_by_high_MAE_and_proxy_order","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|084370|Stage2-Actionable|2024-01-05","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-039030-Stage4B-2024-04-26","case_id":"C07-R2-L109-039030","symbol":"039030","company_name":"이오테크닉스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":239500.0,"evidence_available_at_that_date":"The April 2024 laser-dicing/HBM packaging narrative arrived near a local price peak; the stock-web path shows very small MFE and large 90D/180D MAE, so C07 should route this to 4B-watch unless a direct order/revenue bridge appears.","evidence_source":"https://news.nate.com/view/20240426n04398","stage2_evidence_fields":["HBM_laser_packaging_label","customer_eval_or_domestic_route_proxy"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_led_local_peak","order_revenue_bridge_missing","large_90D_180D_MAE"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/039/039030/2024.csv","profile_path":"atlas/symbol_profiles/039/039030.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.89,"MFE_90D_pct":6.89,"MFE_180D_pct":6.89,"MAE_30D_pct":-19.92,"MAE_90D_pct":-45.97,"MAE_180D_pct":-52.61,"peak_date":"2024-04-29","peak_price":256000.0,"drawdown_after_peak_pct":-55.66,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.94,"four_b_full_window_peak_proximity":0.94,"four_b_timing_verdict":"price_only_or_label_driven_peak_requires_4B_watch","trigger_outcome_label":"counterexample_laser_hbm_label_near_peak_without_order_bridge","current_profile_verdict":"current_profile_false_positive_if_laser_HBM_label_promoted_without_order_revenue_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|039030|Stage4B|2024-04-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"trigger","trigger_id":"C07-R2-L109-160980-Stage4B-2024-03-21","case_id":"C07-R2-L109-160980","symbol":"160980","company_name":"싸이맥스","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","deep_sub_archetype_id":"C07_DEEP_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_ORDER_REVENUE_CONVERSION_VS_PRICE_ONLY_RS_FADE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","trigger_type":"Stage4B","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":20000.0,"evidence_available_at_that_date":"SisaJournal-e summarized brokerage attention on hidden HBM beneficiaries and described Cymechs as a wafer-transfer equipment supplier in Samsung/SK value chains. The price path gave only modest MFE and then a deep 180D MAE, so hidden-beneficiary RS should be 4B-watch until order/revenue conversion appears.","evidence_source":"https://www.sisajournal-e.com/news/curationView.html?idxno=401442","stage2_evidence_fields":["hidden_HBM_beneficiary_label","wafer_transfer_equipment_proxy","semicap_relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["beneficiary_label_without_direct_order","large_180D_MAE","relative_strength_fade"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/160/160980/2024.csv","profile_path":"atlas/symbol_profiles/160/160980.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.25,"MFE_90D_pct":18.75,"MFE_180D_pct":18.75,"MAE_30D_pct":-16.85,"MAE_90D_pct":-24.85,"MAE_180D_pct":-62.95,"peak_date":"2024-05-29","peak_price":23750.0,"drawdown_after_peak_pct":-68.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.84,"four_b_timing_verdict":"price_only_or_label_driven_peak_requires_4B_watch","trigger_outcome_label":"counterexample_hidden_beneficiary_RS_without_order_conversion","current_profile_verdict":"current_profile_false_positive_if_hidden_beneficiary_relative_strength_promoted_without_order_revenue_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_by_stock_web_profile_or_old_CA_outside_window","same_entry_group_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|160980|Stage4B|2024-03-21","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-031980-Stage2Actionable-2024-05-30","case_id":"C07-R2-L109-031980","symbol":"031980","company_name":"피에스케이홀딩스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":77.5,"weighted_score_after":76.0,"stage_label_before":"Stage3-Yellow","stage_label_after":"Stage3-Yellow-Guarded","raw_component_scores_before":{"contract_score":72,"backlog_visibility_score":58,"customer_quality_score":72,"margin_bridge_score":42,"revision_score":38,"relative_strength_score":88,"valuation_repricing_score":78,"execution_risk_score":62,"accounting_trust_risk_score":10},"raw_component_scores_after":{"contract_score":82,"backlog_visibility_score":66,"customer_quality_score":82,"margin_bridge_score":46,"revision_score":42,"relative_strength_score":76,"valuation_repricing_score":65,"execution_risk_score":68,"accounting_trust_risk_score":10},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"positive_but_post_peak_guard_needed"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-396470-Stage2Actionable-2024-04-01","case_id":"C07-R2-L109-396470","symbol":"396470","company_name":"워트","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":71.5,"weighted_score_after":68.5,"stage_label_before":"Stage2-Actionable","stage_label_after":"Stage2-Actionable-BridgeRequired","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":24,"customer_quality_score":35,"margin_bridge_score":18,"revision_score":18,"relative_strength_score":80,"valuation_repricing_score":70,"execution_risk_score":70,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":34,"customer_quality_score":44,"margin_bridge_score":24,"revision_score":22,"relative_strength_score":68,"valuation_repricing_score":55,"execution_risk_score":72,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"positive_proxy_but_no_green_unlock"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-140860-Stage3Yellow-2024-12-13","case_id":"C07-R2-L109-140860","symbol":"140860","company_name":"파크시스템스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":73.0,"weighted_score_after":76.5,"stage_label_before":"Stage2-Actionable","stage_label_after":"Stage3-Yellow","raw_component_scores_before":{"contract_score":50,"backlog_visibility_score":50,"customer_quality_score":64,"margin_bridge_score":40,"revision_score":42,"relative_strength_score":62,"valuation_repricing_score":58,"execution_risk_score":50,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":58,"backlog_visibility_score":56,"customer_quality_score":70,"margin_bridge_score":45,"revision_score":47,"relative_strength_score":60,"valuation_repricing_score":54,"execution_risk_score":52,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"positive_delayed_180D_mfe"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-036810-Stage2Actionable-2024-10-25","case_id":"C07-R2-L109-036810","symbol":"036810","company_name":"에프에스티","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":65.0,"weighted_score_after":71.0,"stage_label_before":"Watchlist-only","stage_label_after":"Stage2-Actionable","raw_component_scores_before":{"contract_score":22,"backlog_visibility_score":28,"customer_quality_score":40,"margin_bridge_score":38,"revision_score":25,"relative_strength_score":55,"valuation_repricing_score":48,"execution_risk_score":55,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":36,"customer_quality_score":44,"margin_bridge_score":48,"revision_score":30,"relative_strength_score":54,"valuation_repricing_score":42,"execution_risk_score":58,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"positive_ASP_bridge_not_green"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-084370-Stage2Actionable-2024-01-05","case_id":"C07-R2-L109-084370","symbol":"084370","company_name":"유진테크","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":73.5,"weighted_score_after":72.0,"stage_label_before":"Stage2-Actionable","stage_label_after":"Stage2-Actionable-HighMAEGuard","raw_component_scores_before":{"contract_score":38,"backlog_visibility_score":40,"customer_quality_score":55,"margin_bridge_score":35,"revision_score":32,"relative_strength_score":74,"valuation_repricing_score":62,"execution_risk_score":58,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":44,"backlog_visibility_score":45,"customer_quality_score":60,"margin_bridge_score":38,"revision_score":35,"relative_strength_score":68,"valuation_repricing_score":55,"execution_risk_score":62,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"positive_but_high_MAE_guard"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-039030-Stage4B-2024-04-26","case_id":"C07-R2-L109-039030","symbol":"039030","company_name":"이오테크닉스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":76.0,"weighted_score_after":43.5,"stage_label_before":"Stage3-Yellow","stage_label_after":"Stage4B-Watch","raw_component_scores_before":{"contract_score":28,"backlog_visibility_score":24,"customer_quality_score":38,"margin_bridge_score":18,"revision_score":16,"relative_strength_score":86,"valuation_repricing_score":82,"execution_risk_score":75,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":16,"backlog_visibility_score":16,"customer_quality_score":30,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":48,"valuation_repricing_score":40,"execution_risk_score":88,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"false_positive_filtered_to_4B_watch"}
{"row_type":"score_simulation","trigger_id":"C07-R2-L109-160980-Stage4B-2024-03-21","case_id":"C07-R2-L109-160980","symbol":"160980","company_name":"싸이맥스","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C07_shadow","weighted_score_before":72.5,"weighted_score_after":40.0,"stage_label_before":"Stage2-Actionable","stage_label_after":"Stage4B-Watch","raw_component_scores_before":{"contract_score":25,"backlog_visibility_score":22,"customer_quality_score":36,"margin_bridge_score":14,"revision_score":12,"relative_strength_score":78,"valuation_repricing_score":70,"execution_risk_score":78,"accounting_trust_risk_score":8},"raw_component_scores_after":{"contract_score":14,"backlog_visibility_score":14,"customer_quality_score":28,"margin_bridge_score":8,"revision_score":6,"relative_strength_score":42,"valuation_repricing_score":35,"execution_risk_score":88,"accounting_trust_risk_score":8},"changed_components":["contract_score","backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C07 shadow profile rewards verified HBM/advanced-packaging equipment order or revenue conversion and discounts relative-strength-only or source-proxy labels after local price blowoff.","score_return_alignment_label":"false_positive_filtered_or_4B_guarded"}
{"row_type":"aggregate","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","fine_archetype_id":"C07_HBM_ADVANCED_PACKAGING_PROCESS_AUX_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION_BRIDGE","calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":0,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"positive_case_count":5,"counterexample_count":2,"stage4b_case_count":2,"stage4c_case_count":0,"current_profile_error_count":5,"source_proxy_only_count":2,"evidence_url_pending_count":0,"narrative_only_or_rejected_count":1,"auto_selected_coverage_gap":"C07 base index 18 + local loop107 7 + local loop108 6 + loop109 7 = local-session adjusted 38; above 30-row stability band, 12 short of 50-row practical calibration band","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"new_axis_proposed":"C07_verified_HBM_or_advanced_packaging_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_source_proxy_label_to_4B_watch","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null}
{"row_type":"shadow_weight","round":"R2","loop":"109","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","shadow_rule_candidate_id":"C07_verified_equipment_order_revenue_bridge_before_Yellow_v2","target_scope":"canonical_archetype_specific","production_scoring_changed_now":false,"shadow_weight_only":true,"proposed_component_directions":{"contract_score":"increase only for verified HBM/advanced-packaging equipment supply/order","backlog_visibility_score":"increase only when delivery/revenue conversion is visible","relative_strength_score":"cap when the evidence is only source-proxy or label-driven","valuation_repricing_score":"cap after local blowoff without margin/revision bridge","execution_risk_score":"increase for post-peak high-MAE cases"},"implementation_status":"deferred_coding_agent_only"}
{"row_type":"residual_contribution","round":"R2","loop":"109","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","residual_error_theme":"C07 still confuses verified HBM equipment order/revenue conversion with broad equipment-label relative strength.","profile_stress_result":"Direct customer/order rows such as PSK Holdings should survive Stage2/Yellow, but laser/hidden-beneficiary labels such as EO Technics and Cymechs should route to Stage4B-watch until order/revenue bridge appears.","coding_handoff_needed":true,"batch_patch_candidate":"Add C07 canonical shadow bridge: verified_order_or_revenue_conversion required for Yellow/Green; source-proxy-only label gets Stage2 cap or local 4B watch."}
{"row_type":"narrative_only","symbol":"079370","company_name":"제우스","canonical_archetype_id":"C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH","trigger_date":"2024-01-10","evidence_source":"https://www.thelec.kr/news/articleView.html?idxno=25238","why_excluded":"stock-web profile flags corporate_action_candidate_dates 2024-01-16 and 2024-02-08, inside the D+180 window; raw/unadjusted path therefore cannot be used for promotion.","calibration_usable":false,"calibration_block_reasons":["corporate_action_contaminated_180D_window"]}
```

## 10. Aggregate / Residual Contribution Summary

```text
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 7
positive_case_count = 5
counterexample_count = 2
stage4b_case_count = 2
stage4c_case_count = 0
current_profile_error_count = 5
source_proxy_only_count = 2
evidence_url_pending_count = 0
narrative_only_or_rejected_count = 1
```

Residual contribution:

```text
C07 still needs a canonical-specific distinction between verified equipment order/revenue conversion and source-proxy-only HBM label relative strength. Direct customer/order evidence should survive Stage2/Yellow. Source-proxy labels after price blowoff should be capped or sent to local 4B-watch.
```

## 11. Shadow Rule Candidate

```text
shadow_rule_candidate_id = C07_verified_equipment_order_revenue_bridge_before_Yellow_v2
scope = canonical_archetype_specific
production_scoring_changed_now = false
shadow_weight_only = true
```

Candidate logic:

```text
For C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH:
1. Stage2-Actionable is allowed when at least one of the following is present:
   - verified HBM / advanced-packaging equipment supply
   - named customer route with delivery or evaluation-to-revenue bridge
   - explicit ASP bridge for process/auxiliary equipment with memory/HBM process linkage
2. Stage3-Yellow requires at least two of:
   - direct equipment order / shipment / supply report
   - revenue reflection timing
   - margin or ASP bridge
   - customer quality bridge
3. Stage3-Green remains blocked unless revision/margin bridge is visible.
4. source_proxy_only + local peak proximity >= 0.85 routes to Stage4B-Watch.
```

## 12. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation coding agent. Do not use this handoff unless the user explicitly starts a coding-agent implementation session.

Input artifact:
e2r_stock_web_v12_residual_round_R2_loop_109_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md

Task:
Batch-ingest this MD together with other V12 residual research files. Validate every trigger row against stock-web tradable_raw OHLC shards and symbol profiles. Do not trust narrative-only rows for promotion. If rows pass strict validation, consider a canonical-archetype-specific C07 shadow patch:

C07_verified_HBM_or_advanced_packaging_equipment_order_revenue_bridge_required_before_Yellow_or_Green_plus_source_proxy_label_to_4B_watch

Implementation constraints:
- Do not loosen global Stage3-Green threshold.
- Do not change production scoring from this single MD.
- Apply only if aggregate validation across multiple C07 files supports the same direction.
- Keep C07 distinct from C06 customer-capacity and C10 memory-equipment-cycle routes.
- Preserve price_only_blowoff_blocks_positive_stage and full_4b_requires_non_price_evidence.
```

## 13. Next Research State

```text
completed_round = R2
completed_loop = 109
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C11_BATTERY_ORDERBOOK_RERATING, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C02_POWER_GRID_DATACENTER_CAPEX, C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
