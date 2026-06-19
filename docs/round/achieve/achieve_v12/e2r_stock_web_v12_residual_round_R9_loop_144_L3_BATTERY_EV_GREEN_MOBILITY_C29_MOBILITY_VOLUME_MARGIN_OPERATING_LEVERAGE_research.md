# E2R Stock-Web v12 Residual Research — R9/L3/C29 Mobility Volume Margin Operating Leverage

```yaml
artifact_type: stock_web_v12_sector_archetype_residual_calibration_md
created_at_kst: 2026-06-15
selected_round: R9
selected_loop: 144
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0/1 quality repair — C29 mobility volume/mix/margin operating leverage, direct URL/proxy repair, high-MAE and 4B/4C balance
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF
loop_objective:
  - sector_specific_rule_discovery
  - canonical_archetype_rule_candidate
  - counterexample_mining
  - positive_case_balance
  - 4B_4C_transition_timing_test
  - source_proxy_quality_repair
  - complete_30_90_180_MFE_MAE
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
```

## 0. Execution guardrails

This file follows `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` as the execution prompt. It does not run live discovery, does not patch `stock_agent`, and does not propose production scoring changes. The No-Repeat Index is used only as a duplicate-avoidance and coverage-quality ledger.

Stock-Web basis used here:

```yaml
primary_price_source: Songdaiki/stock-web
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
required_forward_windows: [30D, 90D, 180D]
MFE_definition: max(high from entry_date through N tradable rows) / entry_close - 1
MAE_definition: min(low from entry_date through N tradable rows) / entry_close - 1
```

## 1. Coverage and duplicate-avoidance rationale

The latest No-Repeat Index shows all C01~C32 scopes above the minimum row floor. Therefore this run is not a row-count fill. It is a quality/balance repair run.

Selected scope:

```yaml
selected_scope: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
no_repeat_index_snapshot_for_C29:
  representative_rows: 404
  unique_symbols: 59
  positives: 66
  counterexamples: 93
  stage4B: 45
  stage4C: 14
  current_shadow_weights_EPS_Vis_Bott_Mis_Val_Cap_Info: [20, 18, 10, 15, 17, 15, 5]
reason_for_selection:
  - C29 was not covered in the current post-C26/C27/C28 run cluster.
  - C29 has many rows but still benefits from source-quality repair and clearer 4B/4C taxonomy.
  - Mobility winners can carry deep MAE; false positives can look like volume/mix stories but lack margin conversion.
```

Duplicate-avoidance rule applied:

```yaml
hard_duplicate_key: canonical_archetype_id + symbol + trigger_type + trigger_date + entry_date + evidence_family
new_independent_case_count: 7
reused_case_count: 0
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
calibration_usable_trigger_count: 7
```

## 2. Case summary table

| # | Symbol | Company | Trigger | Entry | Stage | Direction | MFE30/90/180 | MAE30/90/180 | Evidence family | Ingest note |
|---:|---|---|---|---|---|---|---:|---:|---|---|
| 1 | 005380 | Hyundai Motor | 2024-04-25 | 2024-04-26 @ 249500 | Stage3-Yellow | positive_high_MAE | 11.22/20.04/20.04 | -5.81/-13.23/-20.92 | current_quarter_volume_mix_margin_bridge | Stage3-Yellow_with_local_4B_watch |
| 2 | 000270 | Kia | 2025-01-24 | 2025-01-31 @ 102000 | Stage4B | counterexample | 0.78/0.98/17.45 | -10.39/-20.29/-20.29 | record_annual_result_already_discounted | Stage4B |
| 3 | 012330 | Hyundai Mobis | 2025-04-25 | 2025-04-28 @ 251000 | Stage3-Green | positive | 15.74/29.88/99.0 | -4.38/-4.38/-4.38 | high_value_component_orders_margin_bridge | Stage3-Green |
| 4 | 204320 | HL Mando | 2024-07-26 | 2024-07-29 @ 39850 | Stage4B | counterexample | 1.25/8.91/17.94 | -22.58/-22.58/-22.58 | new_wins_without_margin_net_profit_conversion | Stage4B_or_Stage1_watch |
| 5 | 161390 | Hankook Tire & Technology | 2025-02-04 | 2025-02-05 @ 37750 | Stage3-Yellow | positive | 12.05/15.36/28.48 | -2.91/-4.77/-4.77 | premium_mix_margin_operating_leverage | Stage3-Yellow_to_Green_if_reconfirmed |
| 6 | 086280 | Hyundai Glovis | 2024-10-31 | 2024-11-01 @ 121900 | Stage2-Actionable | positive | 4.18/23.87/24.28 | -8.78/-8.78/-14.27 | logistics_shipping_valueup_margin_guidance_bridge | Stage2-Actionable_or_Stage3-Yellow_after_execution |
| 7 | 003620 | KG Mobility | 2025-02-24 | 2025-02-25 @ 3975 | Stage4C | counterexample | 22.89/22.89/22.89 | -15.85/-19.87/-20.5 | thin_profit_one_day_blowoff_without_operating_leverage | Stage4C_or_Stage4B_until_margin_volume_confirmed |

## 3. Trigger JSONL

```jsonl
{"MAE_180D_pct": -20.92, "MAE_30D_pct": -5.81, "MAE_90D_pct": -13.23, "MFE_180D_pct": 20.04, "MFE_30D_pct": 11.22, "MFE_90D_pct": 20.04, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "positive_high_MAE", "company": "Hyundai Motor", "component_scores_current": {"Bottleneck": 8, "Capital": 14, "EPS_FCF": 22, "Info": 7, "Mispricing": 14, "Valuation": 15, "Visibility": 19}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": true, "entry_date": "2024-04-26", "entry_price": 249500.0, "evidence_family": "current_quarter_volume_mix_margin_bridge", "evidence_summary": "2024 Q1 revenue record and 8.7% OPM; volume slightly down but North America/India, SUV/luxury and hybrid sales mix supported profitability; high-MAE path argues for Green delay rather than hard 4C.", "evidence_url": "https://www.hyundai.com/worldwide/en/newsroom/detail/hyundai-motor-announces-2024-q1-business-results-0000000755", "expected_stage_after_shadow": "Stage3-Yellow_with_local_4B_watch", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::005380::2024-04-25::current_quarter_volume_mix_margin_bridge", "peak_180D_date": "2024-06-28", "peak_180D_high": 299500.0, "peak_30D_date": "2024-05-22", "peak_30D_high": 277500.0, "peak_90D_date": "2024-06-28", "peak_90D_high": 299500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "green_too_early_high_MAE_without_drawdown_confirmation", "row_type": "trigger", "same_entry_group_key": "C29::005380::Stage3-Yellow::2024-04-25::2024-04-26", "score_total_after_shadow": 76, "score_total_current": 78, "source_proxy_only": false, "source_quality": "direct_company_press_release", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv"], "symbol": "005380", "trigger_date": "2024-04-25", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-11-14", "trough_180D_low": 197300.0, "trough_30D_date": "2024-05-09", "trough_30D_low": 235000.0, "trough_90D_date": "2024-08-05", "trough_90D_low": 216500.0}
{"MAE_180D_pct": -20.29, "MAE_30D_pct": -10.39, "MAE_90D_pct": -20.29, "MFE_180D_pct": 17.45, "MFE_30D_pct": 0.78, "MFE_90D_pct": 0.98, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "counterexample", "company": "Kia", "component_scores_current": {"Bottleneck": 7, "Capital": 13, "EPS_FCF": 24, "Info": 6, "Mispricing": 16, "Valuation": 17, "Visibility": 18}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": true, "entry_date": "2025-01-31", "entry_price": 102000.0, "evidence_family": "record_annual_result_already_discounted", "evidence_summary": "2024 record revenue and operating profit headline was real, but post-entry 30D/90D MFE was nearly absent while MAE exceeded -20%; record result alone did not convert into fresh mobility rerating.", "evidence_url": "https://worldwide.kia.com/en/newsroom/view/?id=161160", "expected_stage_after_shadow": "Stage4B", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::000270::2025-01-24::record_annual_result_already_discounted", "peak_180D_date": "2025-10-21", "peak_180D_high": 119800.0, "peak_30D_date": "2025-01-31", "peak_30D_high": 102800.0, "peak_90D_date": "2025-03-26", "peak_90D_high": 103000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "result_headline_overcredit_without_forward_volume_margin_surprise", "row_type": "trigger", "same_entry_group_key": "C29::000270::Stage4B::2025-01-24::2025-01-31", "score_total_after_shadow": 70, "score_total_current": 79, "source_proxy_only": false, "source_quality": "direct_company_press_release_unparsed_open_search_verified", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/000/000270/2025.csv"], "symbol": "000270", "trigger_date": "2025-01-24", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-11", "trough_180D_low": 81300.0, "trough_30D_date": "2025-02-12", "trough_30D_low": 91400.0, "trough_90D_date": "2025-04-11", "trough_90D_low": 81300.0}
{"MAE_180D_pct": -4.38, "MAE_30D_pct": -4.38, "MAE_90D_pct": -4.38, "MFE_180D_pct": 99.0, "MFE_30D_pct": 15.74, "MFE_90D_pct": 29.88, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "positive", "company": "Hyundai Mobis", "component_scores_current": {"Bottleneck": 11, "Capital": 14, "EPS_FCF": 25, "Info": 7, "Mispricing": 15, "Valuation": 17, "Visibility": 24}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": false, "entry_date": "2025-04-28", "entry_price": 251000.0, "evidence_family": "high_value_component_orders_margin_bridge", "evidence_summary": "Record Q1 operating profit, high-value electrification/chassis component demand, A/S profit base and overseas orders produced strong low-MAE rerating path.", "evidence_url": "https://en.yna.co.kr/view/AEN20250425003451320", "expected_stage_after_shadow": "Stage3-Green", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::012330::2025-04-25::high_value_component_orders_margin_bridge", "peak_180D_date": "2026-01-22", "peak_180D_high": 499500.0, "peak_30D_date": "2025-06-12", "peak_30D_high": 290500.0, "peak_90D_date": "2025-09-01", "peak_90D_high": 326000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "none_clean_positive", "row_type": "trigger", "same_entry_group_key": "C29::012330::Stage3-Green::2025-04-25::2025-04-28", "score_total_after_shadow": 88, "score_total_current": 86, "source_proxy_only": false, "source_quality": "newswire_with_company_result_detail_plus_official_IR_location", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/012/012330/2025.csv"], "symbol": "012330", "trigger_date": "2025-04-25", "trigger_type": "Stage3-Green", "trough_180D_date": "2025-05-26", "trough_180D_low": 240000.0, "trough_30D_date": "2025-05-26", "trough_30D_low": 240000.0, "trough_90D_date": "2025-05-26", "trough_90D_low": 240000.0}
{"MAE_180D_pct": -22.58, "MAE_30D_pct": -22.58, "MAE_90D_pct": -22.58, "MFE_180D_pct": 17.94, "MFE_30D_pct": 1.25, "MFE_90D_pct": 8.91, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "counterexample", "company": "HL Mando", "component_scores_current": {"Bottleneck": 10, "Capital": 12, "EPS_FCF": 15, "Info": 4, "Mispricing": 15, "Valuation": 16, "Visibility": 19}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": true, "entry_date": "2024-07-29", "entry_price": 39850.0, "evidence_family": "new_wins_without_margin_net_profit_conversion", "evidence_summary": "Q2 sales and new wins were visible, but OPM was modest and price path showed immediate deep MAE; new order/win language did not deserve Actionable upgrade without clearer margin/net-profit conversion.", "evidence_url": "https://quartr.com/events/hl-mando-corporation-a204320-q2-2024_FRayHXQc", "expected_stage_after_shadow": "Stage4B_or_Stage1_watch", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::204320::2024-07-26::new_wins_without_margin_net_profit_conversion", "peak_180D_date": "2025-02-13", "peak_180D_high": 47000.0, "peak_30D_date": "2024-07-29", "peak_30D_high": 40350.0, "peak_90D_date": "2024-11-21", "peak_90D_high": 43400.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "order_win_overcredit_margin_bridge_missing", "row_type": "trigger", "same_entry_group_key": "C29::204320::Stage4B::2024-07-26::2024-07-29", "score_total_after_shadow": 62, "score_total_current": 72, "source_proxy_only": true, "source_quality": "conference_call_transcript_summary_proxy", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv"], "symbol": "204320", "trigger_date": "2024-07-26", "trigger_type": "Stage4B", "trough_180D_date": "2024-09-09", "trough_180D_low": 30850.0, "trough_30D_date": "2024-09-09", "trough_30D_low": 30850.0, "trough_90D_date": "2024-09-09", "trough_90D_low": 30850.0}
{"MAE_180D_pct": -4.77, "MAE_30D_pct": -2.91, "MAE_90D_pct": -4.77, "MFE_180D_pct": 28.48, "MFE_30D_pct": 12.05, "MFE_90D_pct": 15.36, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "positive", "company": "Hankook Tire & Technology", "component_scores_current": {"Bottleneck": 9, "Capital": 15, "EPS_FCF": 24, "Info": 7, "Mispricing": 13, "Valuation": 15, "Visibility": 22}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": false, "entry_date": "2025-02-05", "entry_price": 37750.0, "evidence_family": "premium_mix_margin_operating_leverage", "evidence_summary": "2024 record sales/profit, 18-inch+ tire mix expansion and premium OE supply supported durable margin leverage; forward window showed moderate MFE with contained MAE.", "evidence_url": "https://www.hankooktire.com/mea/en/company/media-list/media-detail.630985.html", "expected_stage_after_shadow": "Stage3-Yellow_to_Green_if_reconfirmed", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::161390::2025-02-04::premium_mix_margin_operating_leverage", "peak_180D_date": "2025-07-24", "peak_180D_high": 48500.0, "peak_30D_date": "2025-03-19", "peak_30D_high": 42300.0, "peak_90D_date": "2025-03-25", "peak_90D_high": 43550.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "none_positive_mix_margin_bridge", "row_type": "trigger", "same_entry_group_key": "C29::161390::Stage3-Yellow::2025-02-04::2025-02-05", "score_total_after_shadow": 84, "score_total_current": 82, "source_proxy_only": false, "source_quality": "direct_company_press_release", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/161/161390/2025.csv"], "symbol": "161390", "trigger_date": "2025-02-04", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-08", "trough_180D_low": 35950.0, "trough_30D_date": "2025-02-05", "trough_30D_low": 36650.0, "trough_90D_date": "2025-04-08", "trough_90D_low": 35950.0}
{"MAE_180D_pct": -14.27, "MAE_30D_pct": -8.78, "MAE_90D_pct": -8.78, "MFE_180D_pct": 24.28, "MFE_30D_pct": 4.18, "MFE_90D_pct": 23.87, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "positive", "company": "Hyundai Glovis", "component_scores_current": {"Bottleneck": 8, "Capital": 18, "EPS_FCF": 19, "Info": 7, "Mispricing": 13, "Valuation": 14, "Visibility": 22}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": true, "entry_date": "2024-11-01", "entry_price": 121900.0, "evidence_family": "logistics_shipping_valueup_margin_guidance_bridge", "evidence_summary": "Value-up plan set diversification, asset-focused growth, 2030 sales/OPM targets and shareholder-return floor; price path validates Actionable/Yellow but mid-term guidance and 14% MAE argue against immediate Green.", "evidence_url": "https://www.glovis.net/upload/asisupload/2024/10/202410311003108830.pdf", "expected_stage_after_shadow": "Stage2-Actionable_or_Stage3-Yellow_after_execution", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::086280::2024-10-31::logistics_shipping_valueup_margin_guidance_bridge", "peak_180D_date": "2025-07-28", "peak_180D_high": 151500.0, "peak_30D_date": "2024-11-27", "peak_30D_high": 127000.0, "peak_90D_date": "2025-01-31", "peak_90D_high": 151000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "long_dated_valueup_should_be_Actionable_not_Green", "row_type": "trigger", "same_entry_group_key": "C29::086280::Stage2-Actionable::2024-10-31::2024-11-01", "score_total_after_shadow": 78, "score_total_current": 77, "source_proxy_only": false, "source_quality": "direct_company_IR_PDF_screenshot_verified", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv"], "symbol": "086280", "trigger_date": "2024-10-31", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-05-08", "trough_180D_low": 104500.0, "trough_30D_date": "2024-11-15", "trough_30D_low": 111200.0, "trough_90D_date": "2024-11-15", "trough_90D_low": 111200.0}
{"MAE_180D_pct": -20.5, "MAE_30D_pct": -15.85, "MAE_90D_pct": -19.87, "MFE_180D_pct": 22.89, "MFE_30D_pct": 22.89, "MFE_90D_pct": 22.89, "calibration_usable": true, "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "case_direction": "counterexample", "company": "KG Mobility", "component_scores_current": {"Bottleneck": 6, "Capital": 9, "EPS_FCF": 13, "Info": 4, "Mispricing": 20, "Valuation": 18, "Visibility": 14}, "corporate_action_overlap_D_to_D180": "not_observed_in_selected_tradable_window_profile_spot_check", "current_profile_error": true, "entry_date": "2025-02-25", "entry_price": 3975.0, "evidence_family": "thin_profit_one_day_blowoff_without_operating_leverage", "evidence_summary": "2024 turned profitable, but operating profit was thin relative to revenue and price reaction was a one-day blowoff followed by sustained drawdown; without durable volume/margin bridge, this is 4B/4C protection, not Stage2 evidence.", "evidence_url": "https://biz.chosun.com/en/en-industry/2025/02/25/TGGR5V7LVVH2LOO5CQTSH6NTTU/", "expected_stage_after_shadow": "Stage4C_or_Stage4B_until_margin_volume_confirmed", "fine_archetype_id": "AUTO_VOLUME_MIX_MARGIN_LEVERAGE_VS_THIN_PROFIT_BLOWOFF", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C29::003620::2025-02-24::thin_profit_one_day_blowoff_without_operating_leverage", "peak_180D_date": "2025-02-26", "peak_180D_high": 4885.0, "peak_30D_date": "2025-02-26", "peak_30D_high": 4885.0, "peak_90D_date": "2025-02-26", "peak_90D_high": 4885.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_source": "Songdaiki/stock-web", "residual_error_type": "thin_profit_price_blowoff_overcredit", "row_type": "trigger", "same_entry_group_key": "C29::003620::Stage4C::2025-02-24::2025-02-25", "score_total_after_shadow": 55, "score_total_current": 68, "source_proxy_only": true, "source_quality": "news_proxy_company_result_detail", "stock_web_paths": ["atlas/ohlcv_tradable_by_symbol_year/003/003620/2025.csv"], "symbol": "003620", "trigger_date": "2025-02-24", "trigger_type": "Stage4C", "trough_180D_date": "2025-10-13", "trough_180D_low": 3160.0, "trough_30D_date": "2025-04-07", "trough_30D_low": 3345.0, "trough_90D_date": "2025-05-26", "trough_90D_low": 3185.0}
```

## 4. Component-level residual diagnosis

### 4.1 What current profile can overcredit

C29 is especially vulnerable to three false-positive families.

1. **Record-result overcredit** — OEM or supplier reports record sales/profit, but the surprise is already priced and forward MFE is weak. Kia 2025 and parts of Hyundai 2024 fit this pattern.
2. **Order/new-win overcredit** — supplier announces large new wins or broad EV/SDV exposure, but margin/net-profit conversion is not yet visible. HL Mando 2024 Q2 is the calibration example.
3. **Thin-profit blowoff** — turnaround headline is technically true, but operating profit is too thin and one-day MFE is followed by persistent drawdown. KG Mobility is the hard protection example.

### 4.2 What current profile can undercredit

C29 also has true structural winners where MAE alone should not kill the case.

1. **High-value component order + A/S profit base** — Hyundai Mobis showed the cleanest low-MAE positive path.
2. **Premium mix margin leverage** — Hankook Tire showed record profit and high-inch tire mix converting to controlled drawdown.
3. **Asset/logistics operating leverage** — Hyundai Glovis value-up plan is long-dated, but diversification, shipping/logistics asset growth and capital-return policy make it an Actionable/Yellow bridge rather than a pure theme.

## 5. Proposed shadow rule candidate

```yaml
new_axis_proposed: C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_CONFIRMATION_GATE
production_scoring_changed: false
shadow_weight_only: true
before_shadow_weights_EPS_Vis_Bott_Mis_Val_Cap_Info: [20, 18, 10, 15, 17, 15, 5]
after_shadow_weights_EPS_Vis_Bott_Mis_Val_Cap_Info:  [19, 21, 9, 13, 16, 17, 5]
suggested_shadow_delta_EPS_Vis_Bott_Mis_Val_Cap_Info: [-1, +3, -1, -2, -1, +2, 0]
```

Rule candidate:

```yaml
C29_stage2_actionable_gate:
  require_at_least_two_of:
    - current_or_near_term_unit_volume_growth
    - premium_mix_or_ASP_improvement
    - operating_margin_or_OP_revision_bridge
    - supplier_order_or_backlog_with_margin_conversion
    - high_value_component_content_per_vehicle
    - cost_raw_material_logistics_tailwind_with_reported_margin_effect
    - capital_return_or_shareholder_policy_supporting_per_share_value
  cap_to_watch_or_stage4B_if:
    - record_result_without_forward_surprise
    - long_dated_2030_target_without_current_year_execution
    - new_win_without_margin_or_net_profit_conversion
    - one_day_price_blowoff_without_durable_volume_margin_bridge
  route_to_stage4C_if:
    - thin_profit_or_loss_dominated_turnaround is paired with sustained post-event drawdown
    - volume/mix thesis is broken by repeated weak shipment/utilization/margin evidence
    - supplier evidence remains order headline only while profitability keeps deteriorating
```

Interpretation:

C29 should reward operating leverage only when volume/mix is not just a showroom story but a factory line that passes through price, margin and cash. In mobility, the headline is often a car on the display floor; E2R should score the engine only after it turns the wheels.

## 6. Case-by-case notes

### 6.1 Hyundai Motor — positive but Green delay

Hyundai's 2024 Q1 release showed record quarterly revenue, 8.7% operating margin, hybrid sales growth and resilient SUV/luxury mix. The price path produced 20.04% 90D/180D MFE but also -20.92% 180D MAE. This is not a hard 4C because the operating bridge remained real; it is a high-MAE winner that should delay Green until drawdown-aware confirmation.

### 6.2 Kia — record result overcredit

Kia's 2024 annual result headline was strong, but the entry after the result produced only 0.98% 90D MFE with -20.29% 90D MAE. This is a C29 example where record earnings alone are not sufficient. The new rule should require fresh forward volume/mix/margin surprise or per-share capital-return bridge before Actionable/Green.

### 6.3 Hyundai Mobis — clean high-value component positive

Hyundai Mobis delivered a clean positive profile: record Q1 operating profit, high-value component demand, A/S profit base and overseas orders. The 180D MFE reached 99.00% with only -4.38% MAE. This is the strongest confirmation that C29 should increase visibility and bridge weight when the order/component story is already crossing into earnings.

### 6.4 HL Mando — new wins without enough margin conversion

HL Mando had visible new wins and SDV/EV exposure, but the price path gave only 1.25% 30D MFE and -22.58% MAE. New-win language should not unlock Stage2-Actionable unless operating margin, net profit and conversion timing are visible.

### 6.5 Hankook Tire — premium mix margin leverage

Hankook Tire's 2024 result showed record sales/profit and high-inch tire mix expansion. The price path had 28.48% 180D MFE with only -4.77% MAE, making it a positive example for premium-mix and margin-leverage confirmation.

### 6.6 Hyundai Glovis — Actionable but not immediate Green

Hyundai Glovis' value-up plan gave diversification, logistics/shipping growth, 2030 sales and OPM targets, and shareholder-return policy. The 180D MFE was 24.28%, but the 180D MAE was -14.27%. It qualifies as Actionable/Yellow, not immediate Green, because a large part of the bridge is mid-term execution.

### 6.7 KG Mobility — thin-profit one-day blowoff

KG Mobility turned profitable in 2024, but the operating profit base was thin and the post-event path had one-day 22.89% MFE followed by -20.50% 180D MAE. This is a Stage4C-style protection row: the headline should not be treated as durable operating leverage without stronger volume/margin proof.

## 7. Batch ingest self-audit

```yaml
standard_filename: pass
metadata_filename_consistency: pass
round_sector_consistency: pass
canonical_stage_labels_only: pass
required_mfe_mae_fields_complete: pass
rows_missing_required_mfe_mae: 0
trigger_rows_total: 7
calibration_usable_trigger_count: 7
narrative_only_rows: 0
same_entry_group_dedupe: pass
source_proxy_only_count: 2
evidence_url_pending_count: 0
corporate_action_overlap_D_to_D180: no_selected_window_overlap_observed_from_tradable_shard_profile_spot_check
new_independent_case_count: 7
same_archetype_new_symbol_count: 7
same_archetype_new_trigger_family_count: 7
positive_case_count: 4
counterexample_count: 3
stage4B_case_count: 2
stage4C_case_count: 1
current_profile_error_count: 5
```

## 8. Deferred Coding Agent Handoff Prompt

```text
Read this MD as one v12 residual calibration artifact.

Ingest only rows with row_type="trigger" and calibration_usable=true.
Validate that every trigger row has canonical stage labels and the six required MFE/MAE fields:
MFE_30D_pct, MFE_90D_pct, MFE_180D_pct, MAE_30D_pct, MAE_90D_pct, MAE_180D_pct.

Do not patch production scoring directly.
Use the proposed C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_CONFIRMATION_GATE as shadow-only evidence for the next v12 promotion planner run.
Deduplicate by canonical_archetype_id + symbol + trigger_type + trigger_date + entry_date + evidence_family.
```

## 9. Final status

```yaml
completed_state: completed
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
loop_contribution_label: C29_volume_mix_margin_leverage_quality_repair
new_axis_proposed: C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_CONFIRMATION_GATE
existing_axis_strengthened:
  - stage2_required_bridge
  - local_4b_watch_guard
  - hard_4c_confirmation
  - full_4b_requires_non_price_evidence
  - drawdown_aware_confirmation
existing_axis_weakened: null
next_recommended_archetypes:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - R13_CROSS_ARCHETYPE_STAGE2_FALSE_POSITIVE_REVIEW
```
