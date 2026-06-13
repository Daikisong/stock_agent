---
research_file: e2r_stock_web_v12_residual_round_R1_loop_144_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
prompt_version: e2r_v12_prompt_round_scheduler_corrected
selected_round: R1
selected_loop: 144
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: mixed_C02_transformer_order_margin_bridge_alternate_trigger_holdout_v144
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selection_role_of_no_repeat_index: duplicate_ledger_only
price_source_repo: Songdaiki/stock-web
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
---

# C02_POWER_GRID_DATACENTER_CAPEX residual calibration holdout — R1 loop 144

## 0. Research state

```yaml
selected_round: R1
selected_loop: 144
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: mixed_C02_transformer_order_margin_bridge_alternate_trigger_holdout_v144
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
no_repeat_index_used_as: duplicate_prevention_ledger_only
standard_filename_ok: true
filename_matches_metadata: true
source_repo_used_for_prices: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
entry_price_rule: entry_date_close
mfe_mae_rule: high_low_path_from_entry_date_over_30_90_180_tradable_rows
```

## 1. Selection basis

The static No-Repeat Index still lists `C02_POWER_GRID_DATACENTER_CAPEX` as the top Priority-0 under-covered canonical. This file is not another generic R13 replay; it is a C02-specific alternate-trigger holdout that tests earlier evidence dates for transformer/export/cable names. Prior local C02 rows used some of the same symbols at later entry dates, so this file marks them as **alternate-trigger holdouts** rather than pure new-symbol expansion. The hard duplicate key `canonical_archetype_id + symbol + trigger_type + entry_date` is still different for every row.

## 2. Thesis being tested

C02 should not treat “AI/data-center power demand” as a free Stage3 unlock. The correct mechanism is: named order or backlog visibility -> delivery/revenue recognition -> ASP or product-mix/margin bridge -> MAE discipline. Transformer pure plays can deserve Stage3 earlier than cable/theme read-throughs, but after a vertical MFE path the model must attach a local Stage4B watch unless the second bridge is already confirmed.

## 3. Evidence source table

| symbol | company | trigger_date | evidence URL | evidence summary |
|---:|---|---|---|---|
| 267260 | HD현대일렉트릭 | 2024-02-16 | https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467 | Mirae Asset report dated 2024-02-16 noted end-4Q23 order backlog jumped 59% YoY to KRW 5.5tn and linked demand to AI/datacenter/server power consumption and global customers. |
| 298040 | 효성중공업 | 2024-11-26 | https://www.ibks.com/company/common/download.jsp?filename=20241126095304680_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport | IBK report dated 2024-11-26 noted overseas orders expanding, heavy-industry backlog rising to KRW 7.3tn (+30.4% YoY), and North America/Europe/India growth continuing. |
| 103590 | 일진전기 | 2024-03-27 | https://ssl.pstatic.net/imgstock/upload/research/company/1711495027336.pdf | SK Securities report dated 2024-03-27 estimated 2024 order backlog at KRW 1.896tn (+10.7% YoY), assuming North American utility CAPEX growth and Hongseong Plant 2 capacity expansion from 2025. |
| 033100 | 제룡전기 | 2024-03-08 | https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf | Report dated 2024-03-08 cited 3Q23 backlog of KRW 323.1bn (+88% YoY), US export-led Q growth, and profitability from higher P/lower C in the transformer cycle. |
| 006340 | 대원전선 | 2024-06-27 | https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191 | Mirae Asset AI-generated report dated 2024-06-27 summarized AI/datacenter power-management theme and cable-stock rally narratives, but without named order or margin bridge confirmation. |

## 4. Representative trigger table

| row_id | symbol | name | trigger_date | entry_date | entry_price | trigger_type | outcome_label | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | drawdown_after_peak_pct | calibration_usable | current_profile_error |
|---|---:|---|---|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| C02_R1_L144_01 | 267260 | HD현대일렉트릭 | 2024-02-16 | 2024-02-16 | 115900 | Stage3-Green | positive_order_backlog_margin_bridge | 59.6204 | -0.5177 | 179.1199 | -0.5177 | 256.7731 | -0.5177 | 2024-11-12 | -8.4643 | true | current_profile_too_late_if_waiting_for_more_evidence |
| C02_R1_L144_02 | 298040 | 효성중공업 | 2024-11-26 | 2024-11-26 | 399000 | Stage3-Yellow | positive_backlog_but_local_4b_after_vertical_rerating | 16.2907 | -8.2707 | 37.5940 | -8.2707 | 239.8496 | -8.2707 | 2025-07-28 | -20.8702 | true | current_profile_understates_upside_but_needs_4b_watch |
| C02_R1_L144_03 | 103590 | 일진전기 | 2024-03-27 | 2024-03-27 | 20700 | Stage2-Actionable | transformer_backlog_stage2_positive_with_4b_watch | 26.8116 | -14.3478 | 46.1353 | -14.3478 | 46.1353 | -19.8068 | 2024-05-29 | -45.1240 | true | stage3_if_overpromoted_before_capacity_delivery_bridge |
| C02_R1_L144_04 | 033100 | 제룡전기 | 2024-03-08 | 2024-03-08 | 32550 | Stage3-Yellow | distribution_transformer_export_positive_but_vertical_rerating | 73.5791 | -7.6805 | 209.3702 | -7.6805 | 209.3702 | -7.6805 | 2024-07-11 | -61.0725 | true | local_4b_needed_after_vertical_rerating |
| C02_R1_L144_05 | 006340 | 대원전선 | 2024-06-27 | 2024-06-27 | 4350 | Stage4B-LocalWatch | cable_ai_power_grid_theme_blowoff_counterexample | 9.7701 | -39.3103 | 9.7701 | -41.3793 | 9.7701 | -49.3103 | 2024-06-28 | -53.8220 | true | price_theme_false_positive_if_not_capped |

## 5. Case notes

### 267260 HD현대일렉트릭 — positive_order_backlog_margin_bridge

- Evidence: Mirae Asset report dated 2024-02-16 noted end-4Q23 order backlog jumped 59% YoY to KRW 5.5tn and linked demand to AI/datacenter/server power consumption and global customers.
- Price path: entry `2024-02-16` at `115900`, MFE/MAE 90D `179.1199% / -0.5177%`, MFE/MAE 180D `256.7731% / -0.5177%`.
- Interpretation: clean positive; C02 Stage3-Green can be allowed when backlog and margin bridge are explicit.

### 298040 효성중공업 — positive_backlog_but_local_4b_after_vertical_rerating

- Evidence: IBK report dated 2024-11-26 noted overseas orders expanding, heavy-industry backlog rising to KRW 7.3tn (+30.4% YoY), and North America/Europe/India growth continuing.
- Price path: entry `2024-11-26` at `399000`, MFE/MAE 90D `37.5940% / -8.2707%`, MFE/MAE 180D `239.8496% / -8.2707%`.
- Interpretation: structural positive, but late-cycle entry needs local 4B after fast rerating.

### 103590 일진전기 — transformer_backlog_stage2_positive_with_4b_watch

- Evidence: SK Securities report dated 2024-03-27 estimated 2024 order backlog at KRW 1.896tn (+10.7% YoY), assuming North American utility CAPEX growth and Hongseong Plant 2 capacity expansion from 2025.
- Price path: entry `2024-03-27` at `20700`, MFE/MAE 90D `46.1353% / -14.3478%`, MFE/MAE 180D `46.1353% / -19.8068%`.
- Interpretation: Stage2 positive; Stage3 requires capacity/delivery conversion and peak drawdown watch.

### 033100 제룡전기 — distribution_transformer_export_positive_but_vertical_rerating

- Evidence: Report dated 2024-03-08 cited 3Q23 backlog of KRW 323.1bn (+88% YoY), US export-led Q growth, and profitability from higher P/lower C in the transformer cycle.
- Price path: entry `2024-03-08` at `32550`, MFE/MAE 90D `209.3702% / -7.6805%`, MFE/MAE 180D `209.3702% / -7.6805%`.
- Interpretation: very strong positive, but vertical MFE requires local 4B after peak.

### 006340 대원전선 — cable_ai_power_grid_theme_blowoff_counterexample

- Evidence: Mirae Asset AI-generated report dated 2024-06-27 summarized AI/datacenter power-management theme and cable-stock rally narratives, but without named order or margin bridge confirmation.
- Price path: entry `2024-06-27` at `4350`, MFE/MAE 90D `9.7701% / -41.3793%`, MFE/MAE 180D `9.7701% / -49.3103%`.
- Interpretation: counterexample; theme-only cable rerating needs 4B cap unless named order/margin bridge appears.

## 6. Machine-readable rows

```jsonl
{"row_type":"case","case_id":"C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_transformer_backlog_margin_bridge_clean_positive","case_type":"early_structural_positive","positive_or_counterexample":"positive","best_trigger":"Stage3-Green","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol may appear in prior C02 session rows, but trigger_type+entry_date differs; treat as alternate-trigger holdout not exact duplicate","independent_evidence_weight":0.75,"score_price_alignment":"clean positive; C02 Stage3-Green can be allowed when backlog and margin bridge are explicit.","current_profile_verdict":"current_profile_too_late_if_waiting_for_more_evidence","price_source":"Songdaiki/stock-web","notes":"positive_order_backlog_margin_bridge"}
{"row_type":"trigger","trigger_id":"C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216_T1","case_id":"C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216","symbol":"267260","company_name":"HD현대일렉트릭","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_transformer_backlog_margin_bridge_clean_positive","loop_objective":"coverage_gap_fill | alternate-trigger holdout | order-margin bridge validation | 4B theme cap test","trigger_type":"Stage3-Green","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":115900.0,"evidence_available_at_that_date":"Mirae Asset report dated 2024-02-16 noted end-4Q23 order backlog jumped 59% YoY to KRW 5.5tn and linked demand to AI/datacenter/server power consumption and global customers.","evidence_source_url":"https://securities.miraeasset.com/bbs/download/2122467.pdf?attachmentId=2122467","stage2_evidence_fields":["power-grid/datacenter demand","order/backlog or theme evidence","customer/capex route"],"stage3_evidence_fields":["named backlog/order evidence","delivery/revenue/margin bridge strength varies by case"],"stage4b_evidence_fields":["post_peak_watch_only"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/267/267260/2024.csv|atlas/ohlcv_tradable_by_symbol_year/267/267260/2025.csv","profile_path":"atlas/symbol_profiles/267/267260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":59.6204,"MAE_30D_pct":-0.5177,"MFE_90D_pct":179.1199,"MAE_90D_pct":-0.5177,"MFE_180D_pct":256.7731,"MAE_180D_pct":-0.5177,"peak_date":"2024-11-12","peak_price":413500.0,"drawdown_after_peak_pct":-8.4643,"four_b_local_peak_proximity":0.35,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":[],"trigger_outcome_label":"positive_order_backlog_margin_bridge","current_profile_verdict":"current_profile_too_late_if_waiting_for_more_evidence","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|267260|Stage3-Green|2024-02-16","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"alternate-trigger holdout; not same trigger_type+entry_date as prior C02 rows in local session","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216","trigger_id":"C02_R1L144_267260_C02_transformer_backlog_margin_bridge_clean_positive_20240216_T1","symbol":"267260","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":78,"revision_score":80,"relative_strength_score":90,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_before":74.75,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":85,"revision_score":80,"relative_strength_score":90,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_after":75.62,"stage_label_after":"Stage3-Green","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C02 v144 shadow gate separates named order/backlog/margin bridge from cable/theme or late-entry high-MAE rows.","MFE_90D_pct":179.1199,"MAE_90D_pct":-0.5177,"score_return_alignment_label":"clean positive; C02 Stage3-Green can be allowed when backlog and margin bridge are explicit.","current_profile_verdict":"current_profile_too_late_if_waiting_for_more_evidence"}
{"row_type":"case","case_id":"C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_heavy_transformer_us_eu_backlog_margin_bridge","case_type":"structural_positive_with_4b_watch","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol may appear in prior C02 session rows, but trigger_type+entry_date differs; treat as alternate-trigger holdout not exact duplicate","independent_evidence_weight":0.75,"score_price_alignment":"structural positive, but late-cycle entry needs local 4B after fast rerating.","current_profile_verdict":"current_profile_understates_upside_but_needs_4b_watch","price_source":"Songdaiki/stock-web","notes":"positive_backlog_but_local_4b_after_vertical_rerating"}
{"row_type":"trigger","trigger_id":"C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126_T1","case_id":"C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126","symbol":"298040","company_name":"효성중공업","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_heavy_transformer_us_eu_backlog_margin_bridge","loop_objective":"coverage_gap_fill | alternate-trigger holdout | order-margin bridge validation | 4B theme cap test","trigger_type":"Stage3-Yellow","trigger_date":"2024-11-26","entry_date":"2024-11-26","entry_price":399000.0,"evidence_available_at_that_date":"IBK report dated 2024-11-26 noted overseas orders expanding, heavy-industry backlog rising to KRW 7.3tn (+30.4% YoY), and North America/Europe/India growth continuing.","evidence_source_url":"https://www.ibks.com/company/common/download.jsp?filename=20241126095304680_ko.pdf&filepath=%2Ffiles%2Ftradeinfo%2Fbusreport","stage2_evidence_fields":["power-grid/datacenter demand","order/backlog or theme evidence","customer/capex route"],"stage3_evidence_fields":["named backlog/order evidence","delivery/revenue/margin bridge strength varies by case"],"stage4b_evidence_fields":["vertical_rerating","MAE90_or_MAE180_guard","theme_or_late_entry_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298040/2024.csv|atlas/ohlcv_tradable_by_symbol_year/298/298040/2025.csv|atlas/ohlcv_tradable_by_symbol_year/298/298040/2026.csv","profile_path":"atlas/symbol_profiles/298/298040.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":16.2907,"MAE_30D_pct":-8.2707,"MFE_90D_pct":37.594,"MAE_90D_pct":-8.2707,"MFE_180D_pct":239.8496,"MAE_180D_pct":-8.2707,"peak_date":"2025-07-28","peak_price":1356000.0,"drawdown_after_peak_pct":-20.8702,"four_b_local_peak_proximity":0.35,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":[],"trigger_outcome_label":"positive_backlog_but_local_4b_after_vertical_rerating","current_profile_verdict":"current_profile_understates_upside_but_needs_4b_watch","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|298040|Stage3-Yellow|2024-11-26","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"alternate-trigger holdout; not same trigger_type+entry_date as prior C02 rows in local session","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126","trigger_id":"C02_R1L144_298040_C02_heavy_transformer_us_eu_backlog_margin_bridge_20241126_T1","symbol":"298040","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":65,"revision_score":65,"relative_strength_score":65,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_before":68.12,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":65,"revision_score":65,"relative_strength_score":65,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_after":68.12,"stage_label_after":"Stage3-Yellow","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C02 v144 shadow gate separates named order/backlog/margin bridge from cable/theme or late-entry high-MAE rows.","MFE_90D_pct":37.594,"MAE_90D_pct":-8.2707,"score_return_alignment_label":"structural positive, but late-cycle entry needs local 4B after fast rerating.","current_profile_verdict":"current_profile_understates_upside_but_needs_4b_watch"}
{"row_type":"case","case_id":"C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327","symbol":"103590","company_name":"일진전기","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_transformer_cable_backlog_factory_expansion_bridge","case_type":"positive_with_peak_drawdown","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol may appear in prior C02 session rows, but trigger_type+entry_date differs; treat as alternate-trigger holdout not exact duplicate","independent_evidence_weight":0.75,"score_price_alignment":"Stage2 positive; Stage3 requires capacity/delivery conversion and peak drawdown watch.","current_profile_verdict":"stage3_if_overpromoted_before_capacity_delivery_bridge","price_source":"Songdaiki/stock-web","notes":"transformer_backlog_stage2_positive_with_4b_watch"}
{"row_type":"trigger","trigger_id":"C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327_T1","case_id":"C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327","symbol":"103590","company_name":"일진전기","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_transformer_cable_backlog_factory_expansion_bridge","loop_objective":"coverage_gap_fill | alternate-trigger holdout | order-margin bridge validation | 4B theme cap test","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":20700.0,"evidence_available_at_that_date":"SK Securities report dated 2024-03-27 estimated 2024 order backlog at KRW 1.896tn (+10.7% YoY), assuming North American utility CAPEX growth and Hongseong Plant 2 capacity expansion from 2025.","evidence_source_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1711495027336.pdf","stage2_evidence_fields":["power-grid/datacenter demand","order/backlog or theme evidence","customer/capex route"],"stage3_evidence_fields":["named backlog/order evidence","delivery/revenue/margin bridge strength varies by case"],"stage4b_evidence_fields":["vertical_rerating","MAE90_or_MAE180_guard","theme_or_late_entry_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv|atlas/ohlcv_tradable_by_symbol_year/103/103590/2025.csv","profile_path":"atlas/symbol_profiles/103/103590.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":26.8116,"MAE_30D_pct":-14.3478,"MFE_90D_pct":46.1353,"MAE_90D_pct":-14.3478,"MFE_180D_pct":46.1353,"MAE_180D_pct":-19.8068,"peak_date":"2024-05-29","peak_price":30250.0,"drawdown_after_peak_pct":-45.124,"four_b_local_peak_proximity":0.35,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":[],"trigger_outcome_label":"transformer_backlog_stage2_positive_with_4b_watch","current_profile_verdict":"stage3_if_overpromoted_before_capacity_delivery_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|103590|Stage2-Actionable|2024-03-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"alternate-trigger holdout; not same trigger_type+entry_date as prior C02 rows in local session","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327","trigger_id":"C02_R1L144_103590_C02_transformer_cable_backlog_factory_expansion_bridge_20240327_T1","symbol":"103590","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":65,"revision_score":65,"relative_strength_score":65,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_before":65.62,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":60,"margin_bridge_score":65,"revision_score":65,"relative_strength_score":65,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_after":65.62,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C02 v144 shadow gate separates named order/backlog/margin bridge from cable/theme or late-entry high-MAE rows.","MFE_90D_pct":46.1353,"MAE_90D_pct":-14.3478,"score_return_alignment_label":"Stage2 positive; Stage3 requires capacity/delivery conversion and peak drawdown watch.","current_profile_verdict":"stage3_if_overpromoted_before_capacity_delivery_bridge"}
{"row_type":"case","case_id":"C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_distribution_transformer_us_export_opm_positive","case_type":"high_mfe_positive_with_4b_watch","positive_or_counterexample":"positive","best_trigger":"Stage3-Yellow","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol may appear in prior C02 session rows, but trigger_type+entry_date differs; treat as alternate-trigger holdout not exact duplicate","independent_evidence_weight":0.75,"score_price_alignment":"very strong positive, but vertical MFE requires local 4B after peak.","current_profile_verdict":"local_4b_needed_after_vertical_rerating","price_source":"Songdaiki/stock-web","notes":"distribution_transformer_export_positive_but_vertical_rerating"}
{"row_type":"trigger","trigger_id":"C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308_T1","case_id":"C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308","symbol":"033100","company_name":"제룡전기","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_distribution_transformer_us_export_opm_positive","loop_objective":"coverage_gap_fill | alternate-trigger holdout | order-margin bridge validation | 4B theme cap test","trigger_type":"Stage3-Yellow","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":32550.0,"evidence_available_at_that_date":"Report dated 2024-03-08 cited 3Q23 backlog of KRW 323.1bn (+88% YoY), US export-led Q growth, and profitability from higher P/lower C in the transformer cycle.","evidence_source_url":"https://ssl.pstatic.net/imgstock/upload/research/company/1709852777300.pdf","stage2_evidence_fields":["power-grid/datacenter demand","order/backlog or theme evidence","customer/capex route"],"stage3_evidence_fields":["named backlog/order evidence","delivery/revenue/margin bridge strength varies by case"],"stage4b_evidence_fields":["vertical_rerating","MAE90_or_MAE180_guard","theme_or_late_entry_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv|atlas/ohlcv_tradable_by_symbol_year/033/033100/2025.csv","profile_path":"atlas/symbol_profiles/033/033100.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":73.5791,"MAE_30D_pct":-7.6805,"MFE_90D_pct":209.3702,"MAE_90D_pct":-7.6805,"MFE_180D_pct":209.3702,"MAE_180D_pct":-7.6805,"peak_date":"2024-07-11","peak_price":100700.0,"drawdown_after_peak_pct":-61.0725,"four_b_local_peak_proximity":0.35,"four_b_full_window_peak_proximity":0.2,"four_b_evidence_type":[],"trigger_outcome_label":"distribution_transformer_export_positive_but_vertical_rerating","current_profile_verdict":"local_4b_needed_after_vertical_rerating","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|033100|Stage3-Yellow|2024-03-08","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"alternate-trigger holdout; not same trigger_type+entry_date as prior C02 rows in local session","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308","trigger_id":"C02_R1L144_033100_C02_distribution_transformer_us_export_opm_positive_20240308_T1","symbol":"033100","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":78,"revision_score":80,"relative_strength_score":90,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_before":74.75,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":70,"backlog_visibility_score":80,"margin_bridge_score":78,"revision_score":80,"relative_strength_score":90,"customer_quality_score":80,"valuation_repricing_score":80,"execution_risk_score":40},"weighted_score_after":74.75,"stage_label_after":"Stage3-Yellow","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C02 v144 shadow gate separates named order/backlog/margin bridge from cable/theme or late-entry high-MAE rows.","MFE_90D_pct":209.3702,"MAE_90D_pct":-7.6805,"score_return_alignment_label":"very strong positive, but vertical MFE requires local 4B after peak.","current_profile_verdict":"local_4b_needed_after_vertical_rerating"}
{"row_type":"case","case_id":"C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627","symbol":"006340","company_name":"대원전선","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_cable_grid_theme_event_premium_4b_counterexample","case_type":"counterexample","positive_or_counterexample":"counterexample","best_trigger":"Stage4B-LocalWatch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"same symbol may appear in prior C02 session rows, but trigger_type+entry_date differs; treat as alternate-trigger holdout not exact duplicate","independent_evidence_weight":0.75,"score_price_alignment":"counterexample; theme-only cable rerating needs 4B cap unless named order/margin bridge appears.","current_profile_verdict":"price_theme_false_positive_if_not_capped","price_source":"Songdaiki/stock-web","notes":"cable_ai_power_grid_theme_blowoff_counterexample"}
{"row_type":"trigger","trigger_id":"C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627_T1","case_id":"C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627","symbol":"006340","company_name":"대원전선","round":"R1","loop":"144","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"C02_cable_grid_theme_event_premium_4b_counterexample","loop_objective":"coverage_gap_fill | alternate-trigger holdout | order-margin bridge validation | 4B theme cap test","trigger_type":"Stage4B-LocalWatch","trigger_date":"2024-06-27","entry_date":"2024-06-27","entry_price":4350.0,"evidence_available_at_that_date":"Mirae Asset AI-generated report dated 2024-06-27 summarized AI/datacenter power-management theme and cable-stock rally narratives, but without named order or margin bridge confirmation.","evidence_source_url":"https://securities.miraeasset.com/bbs/download/2129191.pdf?attachmentId=2129191","stage2_evidence_fields":["power-grid/datacenter demand","order/backlog or theme evidence","customer/capex route"],"stage3_evidence_fields":["not enough for Stage3","delivery/revenue/margin bridge strength varies by case"],"stage4b_evidence_fields":["vertical_rerating","MAE90_or_MAE180_guard","theme_or_late_entry_cap"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv|atlas/ohlcv_tradable_by_symbol_year/006/006340/2025.csv","profile_path":"atlas/symbol_profiles/006/006340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.7701,"MAE_30D_pct":-39.3103,"MFE_90D_pct":9.7701,"MAE_90D_pct":-41.3793,"MFE_180D_pct":9.7701,"MAE_180D_pct":-49.3103,"peak_date":"2024-06-28","peak_price":4775.0,"drawdown_after_peak_pct":-53.822,"four_b_local_peak_proximity":0.75,"four_b_full_window_peak_proximity":0.55,"four_b_evidence_type":["local_4b_watch_guard"],"trigger_outcome_label":"cable_ai_power_grid_theme_blowoff_counterexample","current_profile_verdict":"price_theme_false_positive_if_not_capped","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","corporate_action_candidate_dates_profile":[],"same_entry_group_id":"C02_POWER_GRID_DATACENTER_CAPEX|006340|Stage4B-LocalWatch|2024-06-27","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"alternate-trigger holdout; not same trigger_type+entry_date as prior C02 rows in local session","independent_evidence_weight":0.75,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627","trigger_id":"C02_R1L144_006340_C02_cable_grid_theme_event_premium_4b_counterexample_20240627_T1","symbol":"006340","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":60,"margin_bridge_score":30,"revision_score":65,"relative_strength_score":65,"customer_quality_score":35,"valuation_repricing_score":60,"execution_risk_score":75},"weighted_score_before":53.12,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":35,"backlog_visibility_score":60,"margin_bridge_score":30,"revision_score":65,"relative_strength_score":65,"customer_quality_score":35,"valuation_repricing_score":45,"execution_risk_score":90},"weighted_score_after":53.12,"stage_label_after":"Stage4B-LocalWatch","changed_components":["valuation_repricing_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C02 v144 shadow gate separates named order/backlog/margin bridge from cable/theme or late-entry high-MAE rows.","MFE_90D_pct":9.7701,"MAE_90D_pct":-41.3793,"score_return_alignment_label":"counterexample; theme-only cable rerating needs 4B cap unless named order/margin bridge appears.","current_profile_verdict":"price_theme_false_positive_if_not_capped"}
```

## 7. Aggregate findings

```yaml
new_independent_case_count: 5
reused_symbol_count_vs_current_session: 5
same_archetype_new_trigger_family_count: 5
positive_case_count: 4
counterexample_count: 1
stage4b_overlay_count: 4
stage4c_count: 0
calibration_usable_rows: 5
representative_rows: 5
avg_MFE_30D_pct: 37.2144
avg_MAE_30D_pct: -14.0254
avg_MFE_90D_pct: 96.3979
avg_MAE_90D_pct: -14.4392
avg_MFE_180D_pct: 152.3797
avg_MAE_180D_pct: -17.1172
source_proxy_only_rows: 0
evidence_url_pending_rows: 0
rows_missing_required_mfe_mae: 0
```

## 8. Residual contribution summary

This loop strengthens the C02 split between (a) transformer/backlog rows where named order, backlog duration, and margin bridge justify Stage3, and (b) cable/theme rows where AI-grid or copper demand creates fast MFE but not durable Stage3 evidence. The residual error is not that C02 is broadly underweighted; it is that the same headline family can mean different stages depending on revenue/margin bridge and MAE discipline.

## 9. Proposed shadow rule candidate

```text
C02_TRANSFORMER_BACKLOG_STAGE3_REQUIRES_DELIVERY_REVENUE_MARGIN_BRIDGE_AND_CABLE_THEME_4B_CAP_V144
```

## 10. Deferred Coding Agent Handoff Prompt

```text
Read this standalone C02 v12 residual calibration file and ingest only machine-readable trigger rows where calibration_usable=true. Do not patch production scoring directly. Validate filename/metadata consistency, required MFE/MAE completeness, corporate-action contamination, and duplicate key canonical_archetype_id + symbol + trigger_type + entry_date. Treat rows as alternate-trigger holdouts because the same symbols may appear in local C02 session files with different entry dates. Aggregate with existing V12 rows and evaluate the shadow rule candidate C02_TRANSFORMER_BACKLOG_STAGE3_REQUIRES_DELIVERY_REVENUE_MARGIN_BRIDGE_AND_CABLE_THEME_4B_CAP_V144.
```

## 11. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
jsonl_trigger_row_count: 5
calibration_usable_rows: 5
representative_rows: 5
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

## 12. Next research state

```yaml
completed_round: R1
completed_loop: 144
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C02 rows=10 / need-to-30=20; current-session C02 alternate-trigger holdout
next_recommended_archetypes:
  - C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_holdout_if_new_order_revenue_bridge
  - C14_EV_DEMAND_SLOWDOWN_4B_4C_holdout_if_new_utilization_or_order_cut_path
  - R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_holdout_quality_only
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
