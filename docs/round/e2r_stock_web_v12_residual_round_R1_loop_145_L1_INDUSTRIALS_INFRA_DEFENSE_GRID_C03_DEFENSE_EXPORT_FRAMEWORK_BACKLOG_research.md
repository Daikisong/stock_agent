# E2R Stock-Web v12 Residual Research — R1 / L1 / C03 Defense Export Framework Backlog

```text
filename = e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md
selected_round = R1
selected_loop = 145
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C03 rows 62
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
fine_archetype_family = DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTABLE_BACKLOG_MARGIN_BRIDGE
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection / No-Repeat audit

`V12_Research_No_Repeat_Index.md` marks C03 as a Priority 2 bucket with 62 representative rows, so this loop is not a quantity fill. It is a quality-repair loop: URL/proxy replacement, counterexample mining, 4B balance, and a sharper canonical compression for defense export backlog.

This loop avoids reusing the recent session's C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27/C08/C19/C31/C18/C26/C32/C29/C30/C21/C20/C16/C15/C04/C22/C17 axes. C03 maps to R1 / L1, so the round-sector pair is valid.

```text
minimum_new_independent_case_ratio = 0.60
actual_new_independent_case_count = 9
calibration_usable_trigger_count = 9
new_independent_case_ratio = 1.00
minimum_new_symbol_count = 2
actual_new_symbol_count = 6
minimum_positive_case_count = 1
actual_positive_case_count = 6
minimum_counterexample_count = 1
actual_counterexample_count = 3
```

## 2. Price atlas validation

```text
price_source = Songdaiki/stock-web
price_source_repo = https://github.com/Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
entry_price_basis = close_c_column
forward_window_required = 180 trading days
corporate_action_window_rule = block if shares change or profile corporate-action window overlaps entry~D+180
```

Price shards used:

- `atlas/ohlcv_tradable_by_symbol_year/012/012450/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/012/012450/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/047/047810/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/064/064350/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/064/064350/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/079/079550/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/079/079550/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/103/103140/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/272/272210/2025.csv`

All representative trigger rows below have 180 forward trading rows and constant shares in the entry-to-D180 window, so `calibration_usable=true`.

## 3. Evidence split

C03 should not treat every defense headline the same. This loop splits five evidence families:

1. **Named prime framework / named customer**: Poland July 2022 framework created a genuine backlog bridge for Hyundai Rotem and Hanwha Aerospace before the later executive contracts.
2. **Late executive confirmation after reprice**: August 2022 executive contracts were real but arrived after a fast reprice, producing high early MAE. These need local 4B/profit-lock handling, not a fresh Green unlock.
3. **New country aircraft export**: KAI Malaysia FA-50 had named customer/platform/value, but long delivery timing means Stage2-Actionable rather than automatic Yellow/Green.
4. **Air-defense system prime / subsystem contract**: LIG Nex1 Saudi and Hanwha Systems Saudi MFR show direct system/subsystem export bridges that should not be dismissed as generic defense proxy.
5. **Ammunition policy proxy**: Poongsan ammunition exposure is real, but policy or transfer headlines without company-level named order/margin bridge should remain Stage2/watch or counterexample.

## 4. Backtest result summary

| symbol | company | trigger_date | trigger_type | positive_or_counterexample | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | stage4_overlay |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 064350 | Hyundai Rotem | 2022-07-28 | Stage2-Actionable | positive | 2022-07-28 | 24950.0 | 31.66 | 31.66 | 31.66 | -3.61 | -7.62 | -7.62 | none |
| 012450 | Hanwha Aerospace | 2022-07-28 | Stage3-Yellow | positive | 2022-07-28 | 53700.0 | 61.64 | 61.64 | 123.65 | 0.19 | -2.05 | -2.05 | none |
| 064350 | Hyundai Rotem | 2022-08-29 | Stage4B | counterexample | 2022-08-29 | 30100.0 | 2.99 | 7.31 | 25.58 | -21.93 | -23.42 | -23.42 | local_4B_after_fast_reprice |
| 012450 | Hanwha Aerospace | 2022-08-29 | Stage4B | counterexample | 2022-08-29 | 79600.0 | 9.05 | 9.05 | 50.88 | -33.92 | -33.92 | -33.92 | local_4B_after_fast_reprice |
| 047810 | Korea Aerospace Industries | 2023-02-24 | Stage2-Actionable | positive | 2023-02-24 | 46500.0 | 10.11 | 31.18 | 31.18 | -10.75 | -10.75 | -10.75 | none |
| 079550 | LIG Nex1 | 2024-02-07 | Stage3-Yellow | positive | 2024-02-07 | 113400.0 | 68.69 | 91.36 | 137.65 | -0.09 | -0.09 | -0.09 | none |
| 272210 | Hanwha Systems | 2024-07-09 | Stage2-Actionable | positive | 2024-07-09 | 19120.0 | 22.38 | 57.95 | 126.99 | -10.62 | -13.55 | -13.55 | none |
| 103140 | Poongsan | 2023-05-25 | Stage2 | counterexample | 2023-05-25 | 39300.0 | 15.14 | 15.14 | 15.14 | -1.53 | -19.21 | -19.21 | none |
| 079550 | LIG Nex1 | 2024-09-20 | Stage2-Actionable | positive | 2024-09-20 | 211000.0 | 27.73 | 28.67 | 208.06 | -1.42 | -20.0 | -20.0 | local_4B_after_fast_reprice_and_high_MAE90 |


## 5. Interpretation

The cleanest positives are the early July 2022 framework entries for Hanwha Aerospace and Hyundai Rotem, LIG Nex1's February 2024 Saudi M-SAM contract, and Hanwha Systems' July 2024 named MFR contract. They share a direct customer / platform / role bridge. The price path behaved like a rerating tape: Hanwha Aerospace's July 2022 framework row produced +61.64% MFE90 with only -2.05% MAE90, LIG Nex1's Saudi row produced +91.36% MFE90 with nearly no drawdown, and Hanwha Systems' named radar row produced +57.95% MFE90.

The failures are equally important. Hyundai Rotem and Hanwha Aerospace August 2022 executive-contract rows were not bad business events; they were bad incremental entry points because the July framework had already pulled the spring. The price path shows the mechanism: Hyundai Rotem had only +2.99% MFE30 but -21.93% MAE30 after the executive contract, and Hanwha Aerospace had +9.05% MFE30 but -33.92% MAE30. This is exactly where C03 needs a reprice-aware 4B guard rather than another positive-stage promotion.

Poongsan is the proxy trap. The company makes ammunition, but the 2023 ammunition transfer news was not a named Poongsan export order. The row produced only +15.14% MFE90 and -19.21% MAE90, so it should not be promoted like a prime/system contract.

## 6. Canonical shadow rule candidate

```text
canonical_archetype_rule_candidate = C03_DIRECT_EXPORT_CONTRACT_REQUIRES_EXECUTABLE_BACKLOG_AND_ROLE_SPECIFIC_MARGIN_BRIDGE_WITH_REPRICE_GUARD
```

Proposed C03-specific gate:

```text
if evidence has named customer + named platform/system + named prime/subsystem role + value/delivery schedule:
    allow Stage2-Actionable; allow Stage3-Yellow only when backlog-to-revenue and margin bridge are visible.

if evidence is framework agreement before full reprice and named role is direct:
    allow early Stage2-Actionable / Yellow depending on role quality and valuation context.

if evidence is executive contract after a fast prior framework reprice:
    keep business thesis positive but add local_4B_after_fast_reprice overlay; do not force new Green.

if evidence is policy/war/ammunition proxy without firm-level named order:
    cap at Stage2-watch; require company-level order or margin bridge before Actionable.

if repeat export contract follows major rerating and contract details are confidential:
    require staged entry; avoid immediate Green unless order details and margin/production bridge are disclosed.
```

## 7. Machine-readable trigger rows JSONL

```jsonl
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_001_HYUNDAI_ROTEM_POLAND_FRAMEWORK_20220728","trigger_row_id":"TRG_01_064350_20220728","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTABLE_BACKLOG_MARGIN_BRIDGE","symbol":"064350","company":"Hyundai Rotem","trigger_date":"2022-07-28","entry_date":"2022-07-28","entry_price":24950.0,"entry_price_basis":"close_c_column","trigger_type":"Stage2-Actionable","positive_or_counterexample":"positive","evidence_family":"POLAND_K2_FRAMEWORK_CONTRACT_DIRECT_PLATFORM_PRIME","evidence_summary":"Poland framework covered K2 tanks, with Hyundai Rotem as the named manufacturer; early framework was not merely a generic defense-theme headline.","evidence_url":"https://www.reuters.com/world/with-massive-polish-arms-deal-skorea-steps-closer-ukraine-war-2022-07-28/","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":31.66,"MFE_90D_pct":31.66,"MFE_180D_pct":31.66,"MAE_30D_pct":-3.61,"MAE_90D_pct":-7.62,"MAE_180D_pct":-7.62,"peak_30D_date":"2022-08-26","peak_90D_date":"2022-08-26","peak_180D_date":"2022-08-26","trough_30D_date":"2022-08-05","trough_90D_date":"2022-10-27","trough_180D_date":"2022-10-27","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|064350|Stage2-Actionable|2022-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_trigger_family_for_C03_in_this_session","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"mostly_correct_but_needs_role_specific_bridge_gate","current_profile_error_type":"residual_under_specificity_if_framework_treated_as_generic_theme","stage4_overlay":"none","thesis_label":"prime_direct_framework_positive","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_002_HANWHA_AERO_POLAND_FRAMEWORK_20220728","trigger_row_id":"TRG_02_012450_20220728","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_FRAMEWORK_TO_EXECUTABLE_BACKLOG_MARGIN_BRIDGE","symbol":"012450","company":"Hanwha Aerospace","trigger_date":"2022-07-28","entry_date":"2022-07-28","entry_price":53700.0,"entry_price_basis":"close_c_column","trigger_type":"Stage3-Yellow","positive_or_counterexample":"positive","evidence_family":"POLAND_K9_CHUNMOO_FRAMEWORK_DIRECT_PLATFORM_PRIME","evidence_summary":"Poland framework included K9 howitzers and later Chunmoo route; Hanwha had a named prime role and platform-level export backlog path.","evidence_url":"https://www.reuters.com/world/with-massive-polish-arms-deal-skorea-steps-closer-ukraine-war-2022-07-28/","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":61.64,"MFE_90D_pct":61.64,"MFE_180D_pct":123.65,"MAE_30D_pct":0.19,"MAE_90D_pct":-2.05,"MAE_180D_pct":-2.05,"peak_30D_date":"2022-09-07","peak_90D_date":"2022-09-07","peak_180D_date":"2023-04-11","trough_30D_date":"2022-07-29","trough_90D_date":"2022-10-13","trough_180D_date":"2022-10-13","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|012450|Stage3-Yellow|2022-07-28","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_trigger_family_for_C03_in_this_session","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"too_conservative_if_framework_quality_not_recognized","current_profile_error_type":"current_profile_too_late_for_prime_framework_with_named_customer","stage4_overlay":"none","thesis_label":"prime_direct_framework_high_quality_positive","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_003_HYUNDAI_ROTEM_POLAND_EXECUTIVE_AFTER_RUNUP_20220829","trigger_row_id":"TRG_03_064350_20220829","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_EXECUTIVE_CONTRACT_LATE_REPRICE_4B_GUARD","symbol":"064350","company":"Hyundai Rotem","trigger_date":"2022-08-29","entry_date":"2022-08-29","entry_price":30100.0,"entry_price_basis":"close_c_column","trigger_type":"Stage4B","positive_or_counterexample":"counterexample","evidence_family":"POLAND_K2_EXECUTIVE_CONTRACT_AFTER_FRAMEWORK_REPRICE","evidence_summary":"The formal 4.499tn won K2 contract confirmed 180 tanks, but it arrived after the July framework reprice and caused high 30/90D MAE.","evidence_url":"https://en.yna.co.kr/view/AEN20220829002100320","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":2.99,"MFE_90D_pct":7.31,"MFE_180D_pct":25.58,"MAE_30D_pct":-21.93,"MAE_90D_pct":-23.42,"MAE_180D_pct":-23.42,"peak_30D_date":"2022-08-30","peak_90D_date":"2022-12-01","peak_180D_date":"2023-04-25","trough_30D_date":"2022-10-12","trough_90D_date":"2022-10-27","trough_180D_date":"2022-10-27","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|064350|Stage4B|2022-08-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"same_symbol_as_case_001_but_new_trigger_family_executive_contract_vs_framework","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"current_profile_verdict":"false_positive_if_executive_contract_forced_to_yellow_without_reprice_context","current_profile_error_type":"local_4b_after_framework_runup_needed","stage4_overlay":"local_4B_after_fast_reprice","thesis_label":"late_confirmation_counterexample","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_004_HANWHA_AERO_POLAND_K9_EXECUTIVE_AFTER_RUNUP_20220829","trigger_row_id":"TRG_04_012450_20220829","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_EXECUTIVE_CONTRACT_LATE_REPRICE_4B_GUARD","symbol":"012450","company":"Hanwha Aerospace","trigger_date":"2022-08-29","entry_date":"2022-08-29","entry_price":79600.0,"entry_price_basis":"close_c_column","trigger_type":"Stage4B","positive_or_counterexample":"counterexample","evidence_family":"POLAND_K9_EXECUTIVE_CONTRACT_AFTER_FRAMEWORK_REPRICE","evidence_summary":"Hanwha Defense signed the first executive K9 contract after the initial framework; immediate 30/90D drawdown showed late-confirmation risk despite long-run upside.","evidence_url":"https://www.edrmagazine.eu/hanwha-defense-signs-2-4-billion-contract-to-supply-k9-self-propelled-howitzers-to-poland","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":9.05,"MFE_90D_pct":9.05,"MFE_180D_pct":50.88,"MAE_30D_pct":-33.92,"MAE_90D_pct":-33.92,"MAE_180D_pct":-33.92,"peak_30D_date":"2022-09-07","peak_90D_date":"2022-09-07","peak_180D_date":"2023-04-11","trough_30D_date":"2022-10-13","trough_90D_date":"2022-10-13","trough_180D_date":"2022-10-13","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|012450|Stage4B|2022-08-29","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"same_symbol_as_case_002_but_new_trigger_family_executive_contract_vs_framework","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"current_profile_verdict":"over_promotes_if_contract_confirmation_ignores_prior_reprice","current_profile_error_type":"current_profile_false_positive_without_local_4b_reprice_gate","stage4_overlay":"local_4B_after_fast_reprice","thesis_label":"late_confirmation_counterexample","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_005_KAI_MALAYSIA_FA50_20230224","trigger_row_id":"TRG_05_047810_20230224","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_AIRCRAFT_NEW_CUSTOMER_DELIVERY_VISIBILITY_GATE","symbol":"047810","company":"Korea Aerospace Industries","trigger_date":"2023-02-24","entry_date":"2023-02-24","entry_price":46500.0,"entry_price_basis":"close_c_column","trigger_type":"Stage2-Actionable","positive_or_counterexample":"positive","evidence_family":"MALAYSIA_FA50_NAMED_EXPORT_CONTRACT_NEW_CUSTOMER","evidence_summary":"KAI won a 1.2tn won Malaysia FA-50 deal for 18 aircraft with delivery beginning in 2026; named customer and platform were clear, but revenue timing was long-dated.","evidence_url":"https://en.yna.co.kr/view/AEN20230224005100320","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":10.11,"MFE_90D_pct":31.18,"MFE_180D_pct":31.18,"MAE_30D_pct":-10.75,"MAE_90D_pct":-10.75,"MAE_180D_pct":-10.75,"peak_30D_date":"2023-04-06","peak_90D_date":"2023-04-25","peak_180D_date":"2023-04-25","trough_30D_date":"2023-03-16","trough_90D_date":"2023-03-16","trough_180D_date":"2023-03-16","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|047810|Stage2-Actionable|2023-02-24","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_and_new_country_export_trigger_for_C03","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"correct_to_keep_actionable_not_green_until_delivery_margin_bridge","current_profile_error_type":"none_or_minor_green_block_works","stage4_overlay":"none","thesis_label":"aircraft_export_positive_with_long_delivery_gate","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_006_LIG_NEX1_SAUDI_MSAM_20240207","trigger_row_id":"TRG_06_079550_20240207","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_AIR_DEFENSE_SYSTEM_PRIME_CONTRACT_GATE","symbol":"079550","company":"LIG Nex1","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":113400.0,"entry_price_basis":"close_c_column","trigger_type":"Stage3-Yellow","positive_or_counterexample":"positive","evidence_family":"SAUDI_MSAM_II_DIRECT_SYSTEM_EXPORT_NAMED_CONTRACT","evidence_summary":"Saudi Arabia agreed to buy 10 Cheongung M-SAM II batteries; LIG Nex1 was the named prime for a $3.2bn export system.","evidence_url":"https://www.reuters.com/business/aerospace-defense/saudis-agree-32-bln-deal-buy-south-korean-missile-defence-system-ministry-2024-02-06/","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":68.69,"MFE_90D_pct":91.36,"MFE_180D_pct":137.65,"MAE_30D_pct":-0.09,"MAE_90D_pct":-0.09,"MAE_180D_pct":-0.09,"peak_30D_date":"2024-03-11","peak_90D_date":"2024-06-21","peak_180D_date":"2024-11-06","trough_30D_date":"2024-02-08","trough_90D_date":"2024-02-08","trough_180D_date":"2024-02-08","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|079550|Stage3-Yellow|2024-02-07","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_and_new_air_defense_export_trigger_for_C03","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"too_late_if_system_prime_contract_not_given_yellow_credit","current_profile_error_type":"current_profile_too_late_for_named_system_prime","stage4_overlay":"none","thesis_label":"direct_system_prime_positive","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_007_HANWHA_SYSTEMS_SAUDI_MFR_20240709","trigger_row_id":"TRG_07_272210_20240709","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_SUBSYSTEM_NAMED_CONTRACT_SIZE_GATE","symbol":"272210","company":"Hanwha Systems","trigger_date":"2024-07-09","entry_date":"2024-07-09","entry_price":19120.0,"entry_price_basis":"close_c_column","trigger_type":"Stage2-Actionable","positive_or_counterexample":"positive","evidence_family":"SAUDI_CHEONGUNG_MFR_SUBSYSTEM_DIRECT_EXPORT_CONTRACT","evidence_summary":"Hanwha Systems clinched the Cheongung-II MFR radar supply contract for Saudi Arabia; this converts a subsystem proxy into a direct named-contract bridge.","evidence_url":"https://en.yna.co.kr/view/AEN20240709007700320","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":22.38,"MFE_90D_pct":57.95,"MFE_180D_pct":126.99,"MAE_30D_pct":-10.62,"MAE_90D_pct":-13.55,"MAE_180D_pct":-13.55,"peak_30D_date":"2024-07-30","peak_90D_date":"2024-11-14","peak_180D_date":"2025-03-19","trough_30D_date":"2024-08-05","trough_90D_date":"2024-09-09","trough_180D_date":"2024-09-09","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|272210|Stage2-Actionable|2024-07-09","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_and_subsystem_direct_contract_trigger_for_C03","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"could_underweight_subsystem_if_proxy_only_filter_too_strict","current_profile_error_type":"residual_missed_structural_for_named_subsystem_contract","stage4_overlay":"none","thesis_label":"named_subsystem_contract_positive","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_008_POONGSAN_AMMO_PROXY_20230525","trigger_row_id":"TRG_08_103140_20230525","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_AMMUNITION_PROXY_NEEDS_FIRM_LEVEL_ORDER_GATE","symbol":"103140","company":"Poongsan","trigger_date":"2023-05-25","entry_date":"2023-05-25","entry_price":39300.0,"entry_price_basis":"close_c_column","trigger_type":"Stage2","positive_or_counterexample":"counterexample","evidence_family":"AMMUNITION_POLICY_AND_ARTILLERY_SUPPLY_PROXY_WITHOUT_FIRM_LEVEL_EXPORT_CONTRACT","evidence_summary":"News that South Korean ammunition was headed to Ukraine via the U.S. created a defense-ammunition proxy path; Poongsan makes ammunition, but this row lacked a company-level named export order or margin bridge.","evidence_url":"https://www.reuters.com/business/aerospace-defense/south-korean-ammunition-headed-ukraine-via-us-wsj-2023-05-25/","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":15.14,"MFE_90D_pct":15.14,"MFE_180D_pct":15.14,"MAE_30D_pct":-1.53,"MAE_90D_pct":-19.21,"MAE_180D_pct":-19.21,"peak_30D_date":"2023-06-26","peak_90D_date":"2023-06-26","peak_180D_date":"2023-06-26","trough_30D_date":"2023-05-30","trough_90D_date":"2023-10-04","trough_180D_date":"2023-10-04","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|103140|Stage2|2023-05-25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"new_symbol_and_proxy_failure_mode_for_C03","independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"current_profile_verdict":"false_positive_if_policy_ammunition_proxy_gets_actionable_without_named_order","current_profile_error_type":"source_proxy_only_current_profile_false_positive","stage4_overlay":"none","thesis_label":"ammo_policy_proxy_counterexample","validation_status":"pass","source_proxy_only":true,"evidence_url_pending":false}
{"row_type":"trigger","schema_version":"v12_stock_web_residual","source_md":"e2r_stock_web_v12_residual_round_R1_loop_145_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_research.md","case_id":"C03_R1_L145_009_LIG_NEX1_IRAQ_MSAM_20240920","trigger_row_id":"TRG_09_079550_20240920","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","fine_archetype_id":"DEFENSE_EXPORT_REPEAT_SYSTEM_CONTRACT_STAGED_ENTRY_GATE","symbol":"079550","company":"LIG Nex1","trigger_date":"2024-09-20","entry_date":"2024-09-20","entry_price":211000.0,"entry_price_basis":"close_c_column","trigger_type":"Stage2-Actionable","positive_or_counterexample":"positive","evidence_family":"IRAQ_MSAM_II_REPEAT_EXPORT_CONTRACT_CONFIDENTIAL_DETAILS_HIGH_MAE","evidence_summary":"LIG announced a 3.71tn won Iraq M-SAM export order after the Saudi deal; repeat-country expansion was real, but confidentiality and post-runup volatility require staged entry rather than forced Green.","evidence_url":"https://www.reuters.com/business/aerospace-defense/south-koreas-lig-nex1-wins-28-bln-deal-with-iraq-export-missile-systems-2024-09-19/","price_source":"Songdaiki/stock-web","price_data_source":"Songdaiki/stock-web","price_source_repo":"https://github.com/Songdaiki/stock-web","upstream_source":"FinanceData/marcap","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","stock_web_manifest_max_date":"2026-02-20","forward_window_trading_days":180,"MFE_30D_pct":27.73,"MFE_90D_pct":28.67,"MFE_180D_pct":208.06,"MAE_30D_pct":-1.42,"MAE_90D_pct":-20.0,"MAE_180D_pct":-20.0,"peak_30D_date":"2024-11-06","peak_90D_date":"2024-11-08","peak_180D_date":"2025-06-23","trough_30D_date":"2024-09-27","trough_90D_date":"2024-12-10","trough_180D_date":"2024-12-10","corporate_action_window_status":"clean_by_constant_shares_in_entry_to_D180","calibration_usable":true,"same_entry_group_id":"C03|079550|Stage2-Actionable|2024-09-20","dedupe_for_aggregate":true,"aggregate_group_role":"representative","reuse_reason":"same_symbol_as_case_006_but_new_trigger_family_repeat_export_contract_vs_initial_saudii_contract","independent_evidence_weight":0.5,"do_not_count_as_new_case":false,"current_profile_verdict":"over_green_if_repeat_contract_ignores_high_mae_and_confidential_details","current_profile_error_type":"staged_entry_needed_for_repeat_contract_after_large_rerating","stage4_overlay":"local_4B_after_fast_reprice_and_high_MAE90","thesis_label":"repeat_export_positive_but_staged_entry_needed","validation_status":"pass","source_proxy_only":false,"evidence_url_pending":false}
```

## 8. Machine-readable score simulation rows JSONL

```jsonl
{"row_type":"score_simulation","case_id":"C03_R1_L145_001_HYUNDAI_ROTEM_POLAND_FRAMEWORK_20220728","symbol":"064350","entry_date":"2022-07-28","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":12,"earnings_visibility_score":14,"bottleneck_pricing_score":11,"market_mispricing_score":10,"valuation_rerating_score":9,"capital_allocation_score":3,"information_confidence_score":17,"total_score_simulated":76,"revision_score_simulated":51,"simulated_stage":"Stage2-Actionable","score_return_alignment":"positive","stage_decision_note":"prime_direct_framework_positive"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_002_HANWHA_AERO_POLAND_FRAMEWORK_20220728","symbol":"012450","entry_date":"2022-07-28","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":13,"earnings_visibility_score":16,"bottleneck_pricing_score":12,"market_mispricing_score":10,"valuation_rerating_score":10,"capital_allocation_score":3,"information_confidence_score":18,"total_score_simulated":82,"revision_score_simulated":54,"simulated_stage":"Stage3-Yellow","score_return_alignment":"positive","stage_decision_note":"prime_direct_framework_high_quality_positive"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_003_HYUNDAI_ROTEM_POLAND_EXECUTIVE_AFTER_RUNUP_20220829","symbol":"064350","entry_date":"2022-08-29","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":13,"earnings_visibility_score":17,"bottleneck_pricing_score":11,"market_mispricing_score":4,"valuation_rerating_score":3,"capital_allocation_score":3,"information_confidence_score":18,"total_score_simulated":69,"revision_score_simulated":53,"simulated_stage":"Stage4B","score_return_alignment":"counterexample_or_high_MAE","stage_decision_note":"late_confirmation_counterexample"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_004_HANWHA_AERO_POLAND_K9_EXECUTIVE_AFTER_RUNUP_20220829","symbol":"012450","entry_date":"2022-08-29","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":13,"earnings_visibility_score":17,"bottleneck_pricing_score":12,"market_mispricing_score":4,"valuation_rerating_score":2,"capital_allocation_score":3,"information_confidence_score":18,"total_score_simulated":69,"revision_score_simulated":54,"simulated_stage":"Stage4B","score_return_alignment":"counterexample_or_high_MAE","stage_decision_note":"late_confirmation_counterexample"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_005_KAI_MALAYSIA_FA50_20230224","symbol":"047810","entry_date":"2023-02-24","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":9,"earnings_visibility_score":13,"bottleneck_pricing_score":9,"market_mispricing_score":10,"valuation_rerating_score":8,"capital_allocation_score":3,"information_confidence_score":17,"total_score_simulated":69,"revision_score_simulated":48,"simulated_stage":"Stage2-Actionable","score_return_alignment":"positive","stage_decision_note":"aircraft_export_positive_with_long_delivery_gate"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_006_LIG_NEX1_SAUDI_MSAM_20240207","symbol":"079550","entry_date":"2024-02-07","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":14,"earnings_visibility_score":17,"bottleneck_pricing_score":13,"market_mispricing_score":11,"valuation_rerating_score":10,"capital_allocation_score":3,"information_confidence_score":19,"total_score_simulated":87,"revision_score_simulated":58,"simulated_stage":"Stage3-Yellow","score_return_alignment":"positive","stage_decision_note":"direct_system_prime_positive"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_007_HANWHA_SYSTEMS_SAUDI_MFR_20240709","symbol":"272210","entry_date":"2024-07-09","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":11,"earnings_visibility_score":15,"bottleneck_pricing_score":12,"market_mispricing_score":9,"valuation_rerating_score":8,"capital_allocation_score":2,"information_confidence_score":18,"total_score_simulated":75,"revision_score_simulated":53,"simulated_stage":"Stage2-Actionable","score_return_alignment":"positive","stage_decision_note":"named_subsystem_contract_positive"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_008_POONGSAN_AMMO_PROXY_20230525","symbol":"103140","entry_date":"2023-05-25","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":5,"earnings_visibility_score":7,"bottleneck_pricing_score":9,"market_mispricing_score":5,"valuation_rerating_score":4,"capital_allocation_score":2,"information_confidence_score":9,"total_score_simulated":41,"revision_score_simulated":32,"simulated_stage":"Stage2","score_return_alignment":"counterexample_or_high_MAE","stage_decision_note":"ammo_policy_proxy_counterexample"}
{"row_type":"score_simulation","case_id":"C03_R1_L145_009_LIG_NEX1_IRAQ_MSAM_20240920","symbol":"079550","entry_date":"2024-09-20","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","eps_fcf_bridge_score":13,"earnings_visibility_score":15,"bottleneck_pricing_score":13,"market_mispricing_score":5,"valuation_rerating_score":5,"capital_allocation_score":3,"information_confidence_score":16,"total_score_simulated":70,"revision_score_simulated":55,"simulated_stage":"Stage2-Actionable","score_return_alignment":"positive","stage_decision_note":"repeat_export_positive_but_staged_entry_needed"}
```

## 9. Aggregate / shadow weight / residual rows JSONL

```jsonl
{"row_type":"aggregate","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","trigger_jsonl_rows":9,"calibration_usable_trigger_count":9,"representative_trigger_count":9,"new_independent_case_count":9,"same_archetype_new_symbol_count":6,"same_archetype_new_trigger_family_count":9,"positive_case_count":6,"counterexample_count":3,"stage4b_overlay_count":3,"stage4c_case_count":0,"current_profile_error_count":8,"avg_MFE_90D_positive":50.41,"avg_MAE_90D_counterexample":-25.52,"new_axis_proposed":"C03_DIRECT_EXPORT_CONTRACT_REQUIRES_EXECUTABLE_BACKLOG_AND_ROLE_SPECIFIC_MARGIN_BRIDGE_WITH_REPRICE_GUARD","loop_contribution_label":"canonical_archetype_rule_candidate"}
{"row_type":"shadow_weight","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","production_scoring_changed":false,"shadow_weight_only":true,"axis":"C03_DIRECT_EXPORT_CONTRACT_REQUIRES_EXECUTABLE_BACKLOG_AND_ROLE_SPECIFIC_MARGIN_BRIDGE_WITH_REPRICE_GUARD","suggested_delta_direction":"conditional_plus_for_named_prime_or_named_subsystem_contract; conditional_minus_for_policy_proxy_or_late_confirmation_after_fast_reprice","max_shadow_delta":1,"do_not_propose_global_delta":true,"reason":"C03 already has >50 rows; this is quality repair, not a global threshold rewrite."}
{"row_type":"residual_contribution","selected_round":"R1","selected_loop":145,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG","residual_error_found":true,"residual_summary":"The calibrated profile still needs a C03-specific split between early named framework/prime contracts, later executive-contract confirmations after price reprice, named subsystem export contracts, and ammunition/policy proxies without company-level order evidence.","existing_axis_tested":["stage2_required_bridge","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"existing_axis_strengthened":["stage2_required_bridge","local_4b_watch_guard"],"existing_axis_weakened":[],"do_not_propose_new_weight_delta":false,"loop_contribution_label":"canonical_archetype_rule_candidate"}
```

## 10. Batch ingest self-audit

```text
filename_matches_standard_v12_pattern = true
metadata_round_loop_matches_filename = true
row_type_trigger_has_required_stage_label = true
entry_date_present = true
entry_price_present = true
price_source_present = true
price_basis_tradable_raw = true
price_adjustment_status_raw_unadjusted_marcap = true
forward_window_trading_days_gte_180 = true
MFE_30D_pct_present = true
MFE_90D_pct_present = true
MFE_180D_pct_present = true
MAE_30D_pct_present = true
MAE_90D_pct_present = true
MAE_180D_pct_present = true
large_sector_id_present = true
canonical_archetype_id_present = true
corporate_action_window_status_not_contaminated = true
same_entry_group_id_present = true
dedupe_for_aggregate_present = true
aggregate_group_role_present = true
calibration_usable_present = true
```

## 11. Residual contribution summary

This loop adds 9 new independent cases, 3 counterexamples, and 8 residual errors for R1/L1/C03.

```text
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
new_axis_proposed = C03_DIRECT_EXPORT_CONTRACT_REQUIRES_EXECUTABLE_BACKLOG_AND_ROLE_SPECIFIC_MARGIN_BRIDGE_WITH_REPRICE_GUARD
existing_axis_tested = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_strengthened = stage2_required_bridge | local_4b_watch_guard
existing_axis_weakened = null
```

## 12. Deferred Coding Agent Handoff Prompt — do not execute now

```text
You are a coding agent working later inside stock_agent. Do not change production scoring blindly. Ingest this MD as one v12 residual research artifact. Validate every row_type="trigger" row against the v12 strict schema. Confirm that all rows use price_source=Songdaiki/stock-web, price_basis=tradable_raw, price_adjustment_status=raw_unadjusted_marcap, and complete 30/90/180D MFE/MAE fields. If valid, add the canonical shadow-rule candidate C03_DIRECT_EXPORT_CONTRACT_REQUIRES_EXECUTABLE_BACKLOG_AND_ROLE_SPECIFIC_MARGIN_BRIDGE_WITH_REPRICE_GUARD to the candidate ledger only. Do not overwrite global Stage thresholds. Treat this as C03-specific quality repair: plus credit for named prime/system/subsystem export contracts with executable backlog and role-specific margin bridge; negative/guard credit for policy/ammunition proxy without firm-level order; local 4B overlay for executive-contract confirmations after fast framework reprice. Keep production_scoring_changed=false unless a separate batch promotion planner accepts the patch.
```

## 13. Next research state

```text
completed_round = R1
completed_loop = 145
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 / over_50_rows_quality_repair / C03 rows 62
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C24_BIO_TRIAL_DATA_EVENT_RISK_quality_repair, C13_BATTERY_JV_UTILIZATION_AMPC_IRA_AMPC_UTILIZATION_REPAIR, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_quality_repair, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_if_guardrail_needed, C02_POWER_GRID_DATACENTER_CAPEX_followup_only_if_new_symbols_available
```
