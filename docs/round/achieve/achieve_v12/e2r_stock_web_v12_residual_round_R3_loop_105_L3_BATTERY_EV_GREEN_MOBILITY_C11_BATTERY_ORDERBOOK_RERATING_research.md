---
title: "E2R Stock-Web v12 Residual Research — R3/L3 C11 Battery Orderbook Rerating loop105"
output_file: "e2r_stock_web_v12_residual_round_R3_loop_105_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md"
selected_round: "R3"
selected_loop: 105
selection_basis: "docs/core/V12_Research_No_Repeat_Index.md"
selected_priority_bucket: "Priority 1-under-50 after local-session adjustment; published index Priority 0"
round_schedule_status: "coverage_index_selected"
round_sector_consistency: "pass"
large_sector_id: "L3_BATTERY_EV_GREEN_MOBILITY"
canonical_archetype_id: "C11_BATTERY_ORDERBOOK_RERATING"
fine_archetype_id: "C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE"
deep_sub_archetype_id: "C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE"
price_source: "Songdaiki/stock-web"
price_basis: "tradable_raw"
price_adjustment_status: "raw_unadjusted_marcap"
stock_web_manifest_max_date: "2026-02-20"
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
---

# 0. Execution Scope

This file is a standalone historical calibration / sector-archetype residual research MD for `Songdaiki/stock_agent` v12 batch ingestion. It is not a live stock screen, not a recommendation list, not an auto-trading output, and not a production scoring patch. The only production-facing output is a deferred handoff prompt for a later coding-agent batch.

Primary price atlas assumptions:

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
```

# 1. Coverage-index Selection

`V12_Research_No_Repeat_Index.md` still marks `C11_BATTERY_ORDERBOOK_RERATING` as published-index Priority 0 with 18 rows. In this running session, local C11 loops 101/102/103/104 were treated as already produced; loop104 left C11 at roughly 46 local-session rows. This loop adds 7 new representative C11 rows and locally moves C11 to roughly 53, above the 50-row practical calibration band.

```text
selected_round = R3
selected_loop = 105
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id = C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE
deep_sub_archetype_id = C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE
```

# 2. Novelty / Deduplication Gate

Prior visible/local C11 symbol groups avoided include `003670`, `006400`, `066970`, `096770`, `247540`, `373220`, `078600`, `079810`, `089980`, `220260`, `282880`, `290670`, `299030`, `011790`, `020150`, `086520`, `121600`, `137400`, `222080`, `348370`, `361610`, `382840`, `005420`, `006110`, `093370`, `278280`, `336370`, `393890`, and `417200`.

New representative symbol set for this loop: `217820`, `382480`, `095500`, `107600`, `360070`, `340930`, `011500`.

```text
same_entry_group_id = canonical_archetype_id + symbol + trigger_type + entry_date + entry_price
hard duplicate check = no reused same symbol + same trigger_type + same entry_date group from visible local C11 loops 101/102/103/104
new_independent_case_ratio = 1.00
```

# 3. Stock-Web OHLC Input / Price Source Validation

- primary_price_source: `Songdaiki/stock-web`
- upstream_source: `FinanceData/marcap`
- price_basis: `tradable_raw`
- price_adjustment_status: `raw_unadjusted_marcap`
- calibration_shard_root: `atlas/ohlcv_tradable_by_symbol_year`
- manifest_max_date: `2026-02-20`
- local OHLC files used: `217820_2023.csv`, `217820_2024.csv`, `382480_2023.csv`, `382480_2024.csv`, `095500_2023.csv`, `095500_2024.csv`, `107600_2023.csv`, `107600_2024.csv`, `360070_2023.csv`, `360070_2024.csv`, `340930_2023.csv`, `340930_2024.csv`, `011500_2023.csv`, `011500_2024.csv`

Every trigger row has a complete 180-trading-day forward window inside the stock-web atlas. MFE is calculated from the forward-window `h` column against entry-date close, and MAE is calculated from the forward-window `l` column against entry-date close.

# 4. Historical Eligibility Gate

Every trigger row below has:

- past trigger date and entry date;
- entry price from the `c` column of the selected entry date;
- 30D / 90D / 180D MFE and MAE calculated from `h` and `l` columns;
- `price_basis=tradable_raw`;
- `price_adjustment_status=raw_unadjusted_marcap`;
- no corporate-action candidate date overlapping the selected entry-to-180D window.

Corporate-action profile check summary:

```text
217820: candidate dates 2019-09-23, 2019-10-14, 2022-11-29; selected 2023-01-02~2023-09-21 window clean.
382480: candidate date 2022-04-05; selected 2023-04-03~2023-12-26 window clean.
095500: candidate dates 2007-10-24, 2008-12-02, 2009-01-05; selected 2023 window clean.
107600: no corporate action candidate dates in profile.
360070: no corporate action candidate dates in profile.
340930: candidate dates 2024-04-16, 2024-05-07, 2026-01-12, 2026-01-29; selected 2023-06-01~2024-02-26 window clean.
011500: candidate date 2008-04-30; selected 2023 window clean.
```

# 5. Canonical Archetype Compression Map

`C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE` compresses the following deep routes back into `C11_BATTERY_ORDERBOOK_RERATING`:

1. formation / activation equipment orderbook route;
2. slot-die / coating component route;
3. lithium-material and recycling/precursor proxy route;
4. battery system engineering order-revenue route;
5. assembly equipment route;
6. solid-electrolyte material route.

The compression rule is strict: a C11 row is not Yellow/Green merely because it has a battery orderbook, capacity, or material label. It needs customer acceptance, delivery, revenue conversion, margin stability, or FCF conversion. If the label moves price first and the bridge does not arrive, the case belongs in local 4B watch rather than positive rerating.

# 6. Case Selection Summary

| case_id | symbol | name | trigger | entry | entry_price | role | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current profile verdict |
|---|---:|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|
| C11_R3L105_001 | 217820 | 원익피앤이 | Stage2-Actionable | 2023-01-02 | 7470 | positive_structural_success | 7.9 | 59.17 | 115.26 | -3.61 | -3.61 | -4.02 | current_profile_missed_structural |
| C11_R3L105_002 | 382480 | 지아이텍 | Stage3-Yellow | 2023-04-03 | 4815 | counterexample_high_MAE | 24.2 | 24.2 | 24.2 | -15.78 | -16.1 | -41.85 | current_profile_false_positive |
| C11_R3L105_003 | 095500 | 미래나노텍 | Stage3-Yellow | 2023-04-03 | 35850 | counterexample_failed_rerating | 2.93 | 2.93 | 2.93 | -43.65 | -43.65 | -58.16 | current_profile_false_positive |
| C11_R3L105_004 | 107600 | 새빗켐 | Stage2-Actionable | 2023-01-02 | 73900 | positive_structural_success | 40.05 | 96.62 | 96.62 | -1.22 | -1.22 | -1.22 | current_profile_missed_structural |
| C11_R3L105_005 | 360070 | 탑머티리얼 | Stage2 | 2023-06-01 | 57000 | positive_structural_success | 32.98 | 67.72 | 72.98 | -5.09 | -12.81 | -17.81 | current_profile_too_late |
| C11_R3L105_006 | 340930 | 유일에너테크 | Stage3-Yellow | 2023-06-01 | 18460 | counterexample_local_4B | 12.41 | 12.41 | 12.41 | -11.65 | -33.69 | -53.58 | current_profile_false_positive |
| C11_R3L105_007 | 011500 | 한농화성 | Stage3-Yellow | 2023-04-03 | 23100 | counterexample_local_4B | 37.88 | 37.88 | 37.88 | -29.48 | -34.63 | -56.06 | current_profile_false_positive |


# 7. Positive vs Counterexample Balance

```text
positive_case_count = 3
counterexample_count = 4
stage4b_case_count = 4
stage4c_case_count = 0
current_profile_error_count = 7
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
```

# 8. Mechanism Notes

C11 has a split personality. When an orderbook is already tied to delivery acceptance or revenue conversion, the rerating can be structurally early. When the same language is merely a proxy label, the price often behaves like a match head: bright for a moment, then starved of oxygen once margin/FCF conversion fails to appear. This loop therefore separates early positive bridge cases from high-MAE proxy failures.

# 9. Current Calibrated Profile Stress Test

The current calibrated profile already blocks many price-only upgrades, but C11 still has a residual error: battery equipment/material orderbook language can still over-promote proxy names before delivery/revenue/margin/FCF evidence is visible. The proposed shadow rule is C11-specific, not a global threshold change.

```text
new_axis_proposed = C11_verified_orderbook_to_delivery_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_proxy_high_MAE_local_4B_watch_v3
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence
existing_axis_weakened = null
```

# 10. Machine-readable Trigger Rows JSONL

```jsonl
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_001","case_id":"C11_R3L105_001","symbol":"217820","company_name":"원익피앤이","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-02","entry_date":"2023-01-02","entry_price":7470.0,"evidence_family":"formation_equipment_orderbook_to_revenue_bridge","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["delivery_acceptance","revenue_conversion","margin_or_fcf_bridge"],"stage4b_evidence_fields":["valuation_risk_after_large_MFE"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/217/217820/2023.csv","atlas/ohlcv_tradable_by_symbol_year/217/217820/2024.csv"],"profile_path":"atlas/symbol_profiles/217/217820.json","MFE_30D_pct":7.9,"MFE_90D_pct":59.17,"MFE_180D_pct":115.26,"MAE_30D_pct":-3.61,"MAE_90D_pct":-3.61,"MAE_180D_pct":-4.02,"peak_30D_date":"2023-02-02","peak_90D_date":"2023-04-19","peak_180D_date":"2023-08-16","peak_30D_price":8060.0,"peak_90D_price":11890.0,"peak_180D_price":16080.0,"trough_30D_date":"2023-01-03","trough_90D_date":"2023-01-03","trough_180D_date":"2023-09-21","trough_30D_price":7200.0,"trough_90D_price":7200.0,"trough_180D_price":7170.0,"window_30D_end_date":"2023-02-15","window_90D_end_date":"2023-05-15","window_180D_end_date":"2023-09-21","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":0.07,"four_b_full_window_peak_proximity":0.51,"four_b_timing_verdict":"positive_but_requires_valuation_watch_after_large_MFE","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_missed_structural","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|217820|Stage2-Actionable|2023-01-02|7470","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"positive_structural_success","residual_contribution":"formation/activation equipment orderbook route where early Stage2-Actionable recognition worked when delivery visibility was not merely a label"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_002","case_id":"C11_R3L105_002","symbol":"382480","company_name":"지아이텍","trigger_type":"Stage3-Yellow","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":4815.0,"evidence_family":"slot_die_coating_component_price_spike_without_delivery_margin_bridge","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["insufficient_delivery_acceptance","insufficient_margin_or_fcf_bridge"],"stage4b_evidence_fields":["high_MAE","post_spike_price_decay","bridge_absent"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/382/382480/2023.csv","atlas/ohlcv_tradable_by_symbol_year/382/382480/2024.csv"],"profile_path":"atlas/symbol_profiles/382/382480.json","MFE_30D_pct":24.2,"MFE_90D_pct":24.2,"MFE_180D_pct":24.2,"MAE_30D_pct":-15.78,"MAE_90D_pct":-16.1,"MAE_180D_pct":-41.85,"peak_30D_date":"2023-04-20","peak_90D_date":"2023-04-20","peak_180D_date":"2023-04-20","peak_30D_price":5980.0,"peak_90D_price":5980.0,"peak_180D_price":5980.0,"trough_30D_date":"2023-05-16","trough_90D_date":"2023-08-10","trough_180D_date":"2023-10-26","trough_30D_price":4055.0,"trough_90D_price":4040.0,"trough_180D_price":2800.0,"window_30D_end_date":"2023-05-17","window_90D_end_date":"2023-08-11","window_180D_end_date":"2023-12-26","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_needed_for_high_MAE_or_bridge_absence","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"counterexample_high_MAE","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|382480|Stage3-Yellow|2023-04-03|4815","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"counterexample_high_MAE","residual_contribution":"slot-die/coating component proxy that needed local 4B watch after the spring price spike rather than Yellow continuation"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_003","case_id":"C11_R3L105_003","symbol":"095500","company_name":"미래나노텍","trigger_type":"Stage3-Yellow","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":35850.0,"evidence_family":"battery_material_price_blowoff_without_order_margin_bridge","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["insufficient_delivery_acceptance","insufficient_margin_or_fcf_bridge"],"stage4b_evidence_fields":["high_MAE","post_spike_price_decay","bridge_absent"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/095/095500/2023.csv","atlas/ohlcv_tradable_by_symbol_year/095/095500/2024.csv"],"profile_path":"atlas/symbol_profiles/095/095500.json","MFE_30D_pct":2.93,"MFE_90D_pct":2.93,"MFE_180D_pct":2.93,"MAE_30D_pct":-43.65,"MAE_90D_pct":-43.65,"MAE_180D_pct":-58.16,"peak_30D_date":"2023-04-03","peak_90D_date":"2023-04-03","peak_180D_date":"2023-04-03","peak_30D_price":36900.0,"peak_90D_price":36900.0,"peak_180D_price":36900.0,"trough_30D_date":"2023-05-15","trough_90D_date":"2023-05-15","trough_180D_date":"2023-10-26","trough_30D_price":20200.0,"trough_90D_price":20200.0,"trough_180D_price":15000.0,"window_30D_end_date":"2023-05-17","window_90D_end_date":"2023-08-11","window_180D_end_date":"2023-12-26","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_needed_for_high_MAE_or_bridge_absence","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"counterexample_failed_rerating","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|095500|Stage3-Yellow|2023-04-03|35850","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"counterexample_failed_rerating","residual_contribution":"battery material label failed when orderbook-to-margin conversion did not follow the April blowoff"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_004","case_id":"C11_R3L105_004","symbol":"107600","company_name":"새빗켐","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-02","entry_date":"2023-01-02","entry_price":73900.0,"evidence_family":"recycling_precursor_orderbook_proxy_success","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["delivery_acceptance","revenue_conversion","margin_or_fcf_bridge"],"stage4b_evidence_fields":["valuation_risk_after_large_MFE"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/107/107600/2023.csv","atlas/ohlcv_tradable_by_symbol_year/107/107600/2024.csv"],"profile_path":"atlas/symbol_profiles/107/107600.json","MFE_30D_pct":40.05,"MFE_90D_pct":96.62,"MFE_180D_pct":96.62,"MAE_30D_pct":-1.22,"MAE_90D_pct":-1.22,"MAE_180D_pct":-1.22,"peak_30D_date":"2023-02-09","peak_90D_date":"2023-03-02","peak_180D_date":"2023-03-02","peak_30D_price":103500.0,"peak_90D_price":145300.0,"peak_180D_price":145300.0,"trough_30D_date":"2023-01-03","trough_90D_date":"2023-01-03","trough_180D_date":"2023-01-03","trough_30D_price":73000.0,"trough_90D_price":73000.0,"trough_180D_price":73000.0,"window_30D_end_date":"2023-02-15","window_90D_end_date":"2023-05-15","window_180D_end_date":"2023-09-21","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":0.41,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"positive_but_requires_valuation_watch_after_large_MFE","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_missed_structural","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|107600|Stage2-Actionable|2023-01-02|73900","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"positive_structural_success","residual_contribution":"recycling/precursor proxy that worked early when the orderbook/capacity narrative had immediate price-path confirmation"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_005","case_id":"C11_R3L105_005","symbol":"360070","company_name":"탑머티리얼","trigger_type":"Stage2","trigger_date":"2023-06-01","entry_date":"2023-06-01","entry_price":57000.0,"evidence_family":"battery_system_engineering_order_revenue_bridge","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["delivery_acceptance","revenue_conversion","margin_or_fcf_bridge"],"stage4b_evidence_fields":["valuation_risk_after_large_MFE"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/360/360070/2023.csv","atlas/ohlcv_tradable_by_symbol_year/360/360070/2024.csv"],"profile_path":"atlas/symbol_profiles/360/360070.json","MFE_30D_pct":32.98,"MFE_90D_pct":67.72,"MFE_180D_pct":72.98,"MAE_30D_pct":-5.09,"MAE_90D_pct":-12.81,"MAE_180D_pct":-17.81,"peak_30D_date":"2023-06-09","peak_90D_date":"2023-07-20","peak_180D_date":"2024-02-23","peak_30D_price":75800.0,"peak_90D_price":95600.0,"peak_180D_price":98600.0,"trough_30D_date":"2023-06-01","trough_90D_date":"2023-10-10","trough_180D_date":"2024-01-31","trough_30D_price":54100.0,"trough_90D_price":49700.0,"trough_180D_price":46850.0,"window_30D_end_date":"2023-07-14","window_90D_end_date":"2023-10-16","window_180D_end_date":"2024-02-26","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":0.45,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"positive_but_requires_valuation_watch_after_large_MFE","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"positive_structural_success","current_profile_verdict":"current_profile_too_late","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|360070|Stage2|2023-06-01|57000","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"positive_structural_success","residual_contribution":"system engineering/electrode route where a real order-revenue bridge survived the 180D window despite normal drawdown"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_006","case_id":"C11_R3L105_006","symbol":"340930","company_name":"유일에너테크","trigger_type":"Stage3-Yellow","trigger_date":"2023-06-01","entry_date":"2023-06-01","entry_price":18460.0,"evidence_family":"battery_assembly_equipment_label_without_conversion","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["insufficient_delivery_acceptance","insufficient_margin_or_fcf_bridge"],"stage4b_evidence_fields":["high_MAE","post_spike_price_decay","bridge_absent"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/340/340930/2023.csv","atlas/ohlcv_tradable_by_symbol_year/340/340930/2024.csv"],"profile_path":"atlas/symbol_profiles/340/340930.json","MFE_30D_pct":12.41,"MFE_90D_pct":12.41,"MFE_180D_pct":12.41,"MAE_30D_pct":-11.65,"MAE_90D_pct":-33.69,"MAE_180D_pct":-53.58,"peak_30D_date":"2023-06-14","peak_90D_date":"2023-06-14","peak_180D_date":"2023-06-14","peak_30D_price":20750.0,"peak_90D_price":20750.0,"peak_180D_price":20750.0,"trough_30D_date":"2023-07-10","trough_90D_date":"2023-10-06","trough_180D_date":"2024-02-01","trough_30D_price":16310.0,"trough_90D_price":12240.0,"trough_180D_price":8570.0,"window_30D_end_date":"2023-07-14","window_90D_end_date":"2023-10-16","window_180D_end_date":"2024-02-26","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_needed_for_high_MAE_or_bridge_absence","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"counterexample_local_4B","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|340930|Stage3-Yellow|2023-06-01|18460","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"counterexample_local_4B","residual_contribution":"assembly equipment label where missing delivery/margin conversion led to a large 180D drawdown"}
{"row_type":"trigger","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","deep_sub_archetype_id":"C11_DEEP_FORMATION_SLOTDIE_RECYCLING_SYSTEM_ENGINEERING_ASSEMBLY_SOLID_ELECTROLYTE_ORDERBOOK_VS_MARGIN_FCF_BRIDGE","loop_objective":"coverage_gap_fill + residual_false_positive_mining + residual_missed_structural_mining + 4B_non_price_requirement_stress_test + canonical_archetype_specific_rule_discovery","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"calibration_usable":true,"calibration_block_reasons":[],"dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"not_reused_new_symbol_for_C11_loop105","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"trigger_id":"TRG_C11_R3L105_007","case_id":"C11_R3L105_007","symbol":"011500","company_name":"한농화성","trigger_type":"Stage3-Yellow","trigger_date":"2023-04-03","entry_date":"2023-04-03","entry_price":23100.0,"evidence_family":"solid_electrolyte_material_label_without_margin_fcf_bridge","evidence_available_at_that_date":"source_proxy_only operating context; direct price path from stock-web; operating URL repair pending","evidence_source":"source_proxy_only_stock_web_profile_plus_historical_public_event_proxy","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","orderbook_or_delivery_visibility"],"stage3_evidence_fields":["insufficient_delivery_acceptance","insufficient_margin_or_fcf_bridge"],"stage4b_evidence_fields":["high_MAE","post_spike_price_decay","bridge_absent"],"stage4c_evidence_fields":[],"price_shard_path":["atlas/ohlcv_tradable_by_symbol_year/011/011500/2023.csv","atlas/ohlcv_tradable_by_symbol_year/011/011500/2024.csv"],"profile_path":"atlas/symbol_profiles/011/011500.json","MFE_30D_pct":37.88,"MFE_90D_pct":37.88,"MFE_180D_pct":37.88,"MAE_30D_pct":-29.48,"MAE_90D_pct":-34.63,"MAE_180D_pct":-56.06,"peak_30D_date":"2023-04-24","peak_90D_date":"2023-04-24","peak_180D_date":"2023-04-24","peak_30D_price":31850.0,"peak_90D_price":31850.0,"peak_180D_price":31850.0,"trough_30D_date":"2023-05-16","trough_90D_date":"2023-08-08","trough_180D_date":"2023-11-01","trough_30D_price":16290.0,"trough_90D_price":15100.0,"trough_180D_price":10150.0,"window_30D_end_date":"2023-05-17","window_90D_end_date":"2023-08-11","window_180D_end_date":"2023-12-26","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"below_entry_price_flag_180D":true,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4B_watch_needed_for_high_MAE_or_bridge_absence","four_c_protection_label":"not_applicable_no_hard_4c_route","trigger_outcome_label":"counterexample_local_4B","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window_checked_against_profile_candidate_dates","same_entry_group_id":"C11_BATTERY_ORDERBOOK_RERATING|011500|Stage3-Yellow|2023-04-03|23100","source_proxy_only":true,"evidence_url_pending":true,"promotion_blocked_until_url_repair":true,"case_role":"counterexample_local_4B","residual_contribution":"solid-electrolyte material label needed high-MAE local 4B guard because bridge evidence lagged price"}
```

# 11. Score Simulation Rows JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C11_R3L105_001","symbol":"217820","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":17.0,"orderbook_visibility":15.0,"delivery_acceptance_bridge":13.5,"revenue_margin_fcf_bridge":13.0,"valuation_risk_control":7.0,"red_team_risk_penalty":-4.0},"research_proxy_total_before_shadow":79.0,"research_proxy_total_after_shadow":81.0,"shadow_rule_effect":"positive_bridge_recognition","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","case_id":"C11_R3L105_002","symbol":"382480","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":15.5,"orderbook_visibility":13.0,"delivery_acceptance_bridge":6.5,"revenue_margin_fcf_bridge":6.0,"valuation_risk_control":5.0,"red_team_risk_penalty":-8.0},"research_proxy_total_before_shadow":75.5,"research_proxy_total_after_shadow":70.5,"shadow_rule_effect":"requires_delivery_revenue_margin_FCF_bridge_before_Yellow_or_Green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","case_id":"C11_R3L105_003","symbol":"095500","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":15.5,"orderbook_visibility":13.0,"delivery_acceptance_bridge":6.5,"revenue_margin_fcf_bridge":6.0,"valuation_risk_control":5.0,"red_team_risk_penalty":-8.0},"research_proxy_total_before_shadow":75.5,"research_proxy_total_after_shadow":70.5,"shadow_rule_effect":"requires_delivery_revenue_margin_FCF_bridge_before_Yellow_or_Green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","case_id":"C11_R3L105_004","symbol":"107600","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":17.0,"orderbook_visibility":15.0,"delivery_acceptance_bridge":13.5,"revenue_margin_fcf_bridge":13.0,"valuation_risk_control":7.0,"red_team_risk_penalty":-4.0},"research_proxy_total_before_shadow":79.0,"research_proxy_total_after_shadow":81.0,"shadow_rule_effect":"positive_bridge_recognition","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","case_id":"C11_R3L105_005","symbol":"360070","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":17.0,"orderbook_visibility":15.0,"delivery_acceptance_bridge":13.5,"revenue_margin_fcf_bridge":13.0,"valuation_risk_control":7.0,"red_team_risk_penalty":-4.0},"research_proxy_total_before_shadow":79.0,"research_proxy_total_after_shadow":81.0,"shadow_rule_effect":"positive_bridge_recognition","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","case_id":"C11_R3L105_006","symbol":"340930","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":15.5,"orderbook_visibility":13.0,"delivery_acceptance_bridge":6.5,"revenue_margin_fcf_bridge":6.0,"valuation_risk_control":5.0,"red_team_risk_penalty":-8.0},"research_proxy_total_before_shadow":75.5,"research_proxy_total_after_shadow":70.5,"shadow_rule_effect":"requires_delivery_revenue_margin_FCF_bridge_before_Yellow_or_Green","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","case_id":"C11_R3L105_007","symbol":"011500","before_profile_id":"e2r_2_1_stock_web_calibrated_proxy","after_profile_id":"proposed_C11_shadow_profile_only","raw_component_score_breakdown":{"rerating_evidence":15.5,"orderbook_visibility":13.0,"delivery_acceptance_bridge":6.5,"revenue_margin_fcf_bridge":6.0,"valuation_risk_control":5.0,"red_team_risk_penalty":-8.0},"research_proxy_total_before_shadow":75.5,"research_proxy_total_after_shadow":70.5,"shadow_rule_effect":"requires_delivery_revenue_margin_FCF_bridge_before_Yellow_or_Green","current_profile_verdict":"current_profile_false_positive"}
```

# 12. Aggregate / Shadow / Residual Rows JSONL

```jsonl
{"row_type":"aggregate_summary","round":"R3","loop":105,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"C11_BATTERY_EQUIPMENT_MATERIAL_ACCEPTANCE_ORDERBOOK_MARGIN_FCF_CONVERSION_BRIDGE","calibration_usable_trigger_count":7,"representative_trigger_count":7,"new_independent_case_count":7,"reused_case_count":0,"same_archetype_new_symbol_count":7,"same_archetype_new_trigger_family_count":7,"new_trigger_family_count":7,"positive_case_count":3,"counterexample_count":4,"stage4b_case_count":4,"stage4c_case_count":0,"current_profile_error_count":7,"source_proxy_only_count":7,"evidence_url_pending_count":7,"promotion_blocked_until_url_repair":true,"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"shadow_weight_candidate","scope":"canonical_archetype_specific","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","new_axis_proposed":"C11_verified_orderbook_to_delivery_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_proxy_high_MAE_local_4B_watch_v3","existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard","full_4b_requires_non_price_evidence"],"existing_axis_weakened":null,"recommended_delta_type":"shadow_rule_only_no_production_patch_now","promotion_blocked_until_url_repair":true}
{"row_type":"residual_contribution","this_loop_adds":"7 new independent C11 cases, 4 counterexamples, 3 positive structural successes, and 7 URL-repair tasks.","main_residual":"C11 orderbook labels need a stricter acceptance/delivery/revenue/margin/FCF bridge. Equipment or material proxy labels alone create high-MAE false positives.","current_profile_error_distribution":{"current_profile_false_positive":4,"current_profile_missed_structural":2,"current_profile_too_late":1}}
```

# 13. Batch Ingest Self-audit

```text
filename_matches_required_regex = true
metadata_round_matches_filename = true
metadata_loop_matches_filename = true
round_sector_consistency = pass
canonical_archetype_id_present = true
large_sector_id_present = true
all_trigger_rows_have_30_90_180_MFE_MAE = true
all_trigger_type_values_are_canonical_stage_labels = true
all_rows_have_price_source_fields = true
minimum_positive_case_count_met = true
minimum_counterexample_count_met = true
minimum_calibration_usable_case_count_met = true
new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

# 14. Residual Contribution Summary

This loop adds 7 new independent C11 cases: 3 structural successes and 4 high-MAE / failed-rerating counterexamples. C11's sector-specific residual is not that orderbook evidence is useless. It is that orderbook evidence must be distinguished from battery-label enthusiasm. The shadow candidate requires a verified bridge from orderbook to delivery, revenue, margin, or FCF before Yellow/Green, and routes proxy-only price spikes to local 4B watch.

# 15. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When a later coding-agent batch is explicitly invoked, ingest this MD as a standard V12 result file. Parse trigger rows, score_simulation rows, aggregate_summary, shadow_weight_candidate, and residual_contribution rows. Do not change production scoring from this single MD. Treat the proposed rule as a C11 canonical-archetype-specific shadow candidate only:

C11_verified_orderbook_to_delivery_revenue_margin_FCF_bridge_required_before_Yellow_or_Green_plus_proxy_high_MAE_local_4B_watch_v3

Before any patch decision, repair evidence_url_pending rows by attaching source URLs for each public event proxy, then compare this loop with earlier C11 loops 101/102/103/104 and the published V12 representative trigger ledger. Block promotion if the evidence remains source_proxy_only. If promoted, apply only a small-scope C11 rule that requires delivery/revenue/margin/FCF bridge before Yellow/Green for equipment/material proxies and strengthens local 4B watch for high-MAE orderbook reratings.
```

# 16. Next Research State

```text
completed_round = R3
completed_loop = 105
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C11_BATTERY_ORDERBOOK_RERATING, C14_EV_DEMAND_SLOWDOWN_4B_4C, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
