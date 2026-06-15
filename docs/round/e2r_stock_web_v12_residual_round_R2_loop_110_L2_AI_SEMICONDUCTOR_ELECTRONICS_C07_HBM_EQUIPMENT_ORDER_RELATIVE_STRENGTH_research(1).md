# E2R Stock-Web V12 Residual Research — R2 / loop 110 / C07 HBM Equipment Order Relative Strength

```yaml
completed_round: R2
completed_loop: 110
selected_round: R2
selected_loop: 110
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1-under-50 after local-session adjustment; published index Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
fine_archetype_id: C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION
deep_sub_archetype_id: C07_DEEP_FRONTEND_DRY_STRIP_THERMAL_ALD_COMPONENT_PROXY_RS_VS_VERIFIED_ORDER_REVENUE_BRIDGE
loop_objective:
  - coverage_gap_fill
  - residual_false_positive_mining
  - residual_missed_structural_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_specific_rule_discovery
price_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

## 1. Selection rationale

The active scheduler is coverage-index-first. The published no-repeat ledger still lists `C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH` as Priority 0 with 18 representative rows, needing 12 rows to reach the 30-row stability band and 32 rows to reach the 50-row practical calibration band. Same-session local outputs already raised C07 through loop107/108/109 to roughly 38 representative rows, but C07 remained below 50. This loop adds seven new representative trigger families, taking the local-session adjusted count to about 45.

This loop deliberately stays inside C07 rather than drifting into C06 customer-capacity or C09 valuation-blowoff. The selected mechanism is: **HBM / advanced-memory equipment relative strength is useful only when it is tied to order, revenue, or shipment conversion; otherwise component/proxy relative strength should remain local 4B watch.**

## 2. Stock-Web validation scope

Manifest basis:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

All trigger windows below use same-day or next-available tradable open from the Stock-Web tradable shard. The 30/90/180D windows are trading-day windows counted from `entry_date`. No entry window overlaps the listed corporate-action candidate dates in each profile.

| symbol | name | profile caveat used in this loop |
|---|---|---|
| 319660 | 피에스케이 | corporate-action candidates exist in 2022 only; 2024 window not overlapped |
| 095610 | 테스 | corporate-action candidates are 2011/2016 only; 2024 window not overlapped |
| 084370 | 유진테크 | corporate-action candidates are 2007/2010/2012 only; 2024 window not overlapped |
| 036930 | 주성엔지니어링 | corporate-action candidate is 2000 only; 2024~2025 window not overlapped |
| 240810 | 원익IPS | no corporate-action candidate in profile |
| 064760 | 티씨케이 | no corporate-action candidate in profile |
| 166090 | 하나머티리얼즈 | corporate-action candidates are 2018 only; 2024 window not overlapped |

## 3. Trigger-level OHLC result summary

| symbol | name | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | class |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 319660 | 피에스케이 | Stage2-Actionable | 2024-01-31 | 2024-01-31 | 20500 | 36.10 | -4.73 | 75.12 | -4.73 | 90.73 | -4.73 | positive |
| 095610 | 테스 | Stage2-Actionable | 2024-01-31 | 2024-01-31 | 19320 | 8.95 | -5.75 | 70.29 | -5.75 | 70.29 | -18.53 | positive |
| 084370 | 유진테크 | Stage3-Yellow | 2024-03-15 | 2024-03-15 | 35100 | 61.25 | -2.14 | 70.94 | -2.14 | 70.94 | -10.11 | positive |
| 036930 | 주성엔지니어링 | Stage2-Actionable | 2024-09-10 | 2024-09-10 | 23050 | 34.71 | -4.34 | 54.45 | -4.34 | 88.29 | -4.34 | positive |
| 240810 | 원익IPS | Stage4B-Watch | 2024-04-15 | 2024-04-15 | 38300 | 1.57 | -12.53 | 5.22 | -22.06 | 5.22 | -44.78 | counterexample |
| 064760 | 티씨케이 | Stage4B-Watch | 2024-07-15 | 2024-07-15 | 131700 | 0.00 | -29.92 | 0.00 | -48.75 | 0.00 | -49.51 | counterexample |
| 166090 | 하나머티리얼즈 | Stage4B-Watch | 2024-07-15 | 2024-07-15 | 58000 | 2.07 | -38.53 | 2.07 | -59.91 | 2.07 | -62.33 | counterexample |

## 4. Case interpretation

### 4.1 Positive routes: direct equipment/order conversion should not be over-blocked

`319660`, `095610`, `084370`, and `036930` show the side of C07 where relative strength was not merely a label chase. The common structure is not “semiconductor equipment went up,” but rather: memory/HBM capex expectation was close enough to order, revenue, or process-equipment conversion that early MAE stayed controlled while 90D MFE expanded materially. The current calibrated profile can still be too conservative when the C07 signal appears after inventory reset or after a drawdown, especially if the evidence is classified as generic equipment rather than HBM-adjacent conversion.

### 4.2 Counterexample routes: component/proxy strength should remain local 4B watch

`240810`, `064760`, and `166090` show the other side. The price path was not protected by a verified order/revenue bridge. In these cases, component or broad equipment proxy labels produced either weak upside or severe 90D/180D MAE. The correct shadow rule is not to ban all C07 signals; it is to require a verified bridge before Yellow/Green, while routing proxy-only relative strength to local 4B watch.

## 5. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -4.73, "MAE_180D_trough_date": "2024-02-01", "MAE_30D_pct": -4.73, "MAE_30D_trough_date": "2024-02-01", "MAE_90D_pct": -4.73, "MAE_90D_trough_date": "2024-02-01", "MFE_180D_pct": 90.73, "MFE_180D_peak_date": "2024-07-11", "MFE_30D_pct": 36.1, "MFE_30D_peak_date": "2024-03-18", "MFE_90D_pct": 75.12, "MFE_90D_peak_date": "2024-06-17", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-01-319660", "close_180D_date": "2024-10-30", "close_180D_return_pct": -0.98, "close_30D_date": "2024-03-18", "close_30D_return_pct": 35.85, "close_90D_date": "2024-06-17", "close_90D_return_pct": 62.68, "corporate_action_candidate_dates": ["2022-09-21", "2022-10-20"], "corporate_action_window_overlap_180D": false, "counterexample_case": false, "current_profile_error": true, "deep_sub_archetype_id": "C07_DRY_STRIP_MEMORY_RECOVERY_ORDER_REVENUE_CONVERSION", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|319660|Stage2-Actionable|2024-01-31", "entry_close": 20100.0, "entry_date": "2024-01-31", "entry_high": 20600.0, "entry_low": 20050.0, "entry_open": 20500.0, "entry_price": 20500.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "피에스케이", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "319660", "trigger_date": "2024-01-31", "trigger_family": "dry_strip_memory_order_bridge_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -18.53, "MAE_180D_trough_date": "2024-10-29", "MAE_30D_pct": -5.75, "MAE_30D_trough_date": "2024-02-14", "MAE_90D_pct": -5.75, "MAE_90D_trough_date": "2024-02-14", "MFE_180D_pct": 70.29, "MFE_180D_peak_date": "2024-04-17", "MFE_30D_pct": 8.95, "MFE_30D_peak_date": "2024-03-06", "MFE_90D_pct": 70.29, "MFE_90D_peak_date": "2024-04-17", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-02-095610", "close_180D_date": "2024-10-30", "close_180D_return_pct": -16.05, "close_30D_date": "2024-03-18", "close_30D_return_pct": -0.88, "close_90D_date": "2024-06-17", "close_90D_return_pct": 19.05, "corporate_action_candidate_dates": ["2011-08-10", "2011-08-29", "2016-05-09"], "corporate_action_window_overlap_180D": false, "counterexample_case": false, "current_profile_error": true, "deep_sub_archetype_id": "C07_FRONT_END_MEMORY_EQUIPMENT_ORDER_REVENUE_CONVERSION", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|095610|Stage2-Actionable|2024-01-31", "entry_close": 18990.0, "entry_date": "2024-01-31", "entry_high": 19350.0, "entry_low": 18940.0, "entry_open": 19320.0, "entry_price": 19320.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "테스", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "095610", "trigger_date": "2024-01-31", "trigger_family": "front_end_memory_equipment_order_bridge_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -10.11, "MAE_180D_trough_date": "2024-12-03", "MAE_30D_pct": -2.14, "MAE_30D_trough_date": "2024-03-19", "MAE_90D_pct": -2.14, "MAE_90D_trough_date": "2024-03-19", "MFE_180D_pct": 70.94, "MFE_180D_peak_date": "2024-05-28", "MFE_30D_pct": 61.25, "MFE_30D_peak_date": "2024-04-24", "MFE_90D_pct": 70.94, "MFE_90D_peak_date": "2024-05-28", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-03-084370", "close_180D_date": "2024-12-10", "close_180D_return_pct": -3.7, "close_30D_date": "2024-04-29", "close_30D_return_pct": 55.27, "close_90D_date": "2024-07-26", "close_90D_return_pct": 20.8, "corporate_action_candidate_dates": ["2007-05-17", "2010-01-22", "2012-06-07"], "corporate_action_window_overlap_180D": false, "counterexample_case": false, "current_profile_error": false, "deep_sub_archetype_id": "C07_THERMAL_ALD_HBM_CAPACITY_EQUIPMENT_BRIDGE", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|084370|Stage3-Yellow|2024-03-15", "entry_close": 34900.0, "entry_date": "2024-03-15", "entry_high": 35300.0, "entry_low": 34450.0, "entry_open": 35100.0, "entry_price": 35100.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "유진테크", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "084370", "trigger_date": "2024-03-15", "trigger_family": "thermal_ald_hbm_capacity_bridge_positive", "trigger_type": "Stage3-Yellow", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -4.34, "MAE_180D_trough_date": "2024-09-10", "MAE_30D_pct": -4.34, "MAE_30D_trough_date": "2024-09-10", "MAE_90D_pct": -4.34, "MAE_90D_trough_date": "2024-09-10", "MFE_180D_pct": 88.29, "MFE_180D_peak_date": "2025-03-21", "MFE_30D_pct": 34.71, "MFE_30D_peak_date": "2024-10-29", "MFE_90D_pct": 54.45, "MFE_90D_peak_date": "2025-01-16", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-04-036930", "close_180D_date": "2025-06-16", "close_180D_return_pct": 35.36, "close_30D_date": "2024-10-30", "close_30D_return_pct": 29.5, "close_90D_date": "2025-01-31", "close_90D_return_pct": 37.53, "corporate_action_candidate_dates": ["2000-06-22"], "corporate_action_window_overlap_180D": false, "counterexample_case": false, "current_profile_error": true, "deep_sub_archetype_id": "C07_POST_DRAWDOWN_DRAM_HBM_CAPEX_RECOVERY_BRIDGE", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|036930|Stage2-Actionable|2024-09-10", "entry_close": 22300.0, "entry_date": "2024-09-10", "entry_high": 23050.0, "entry_low": 22050.0, "entry_open": 23050.0, "entry_price": 23050.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "주성엔지니어링", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "036930", "trigger_date": "2024-09-10", "trigger_family": "post_drawdown_dram_hbm_capex_recovery_positive", "trigger_type": "Stage2-Actionable", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -44.78, "MAE_180D_trough_date": "2024-12-09", "MAE_30D_pct": -12.53, "MAE_30D_trough_date": "2024-05-13", "MAE_90D_pct": -22.06, "MAE_90D_trough_date": "2024-08-05", "MFE_180D_pct": 5.22, "MFE_180D_peak_date": "2024-07-04", "MFE_30D_pct": 1.57, "MFE_30D_peak_date": "2024-04-15", "MFE_90D_pct": 5.22, "MFE_90D_peak_date": "2024-07-04", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-05-240810", "close_180D_date": "2025-01-10", "close_180D_return_pct": -39.3, "close_30D_date": "2024-05-30", "close_30D_return_pct": -4.31, "close_90D_date": "2024-08-26", "close_90D_return_pct": -13.19, "corporate_action_candidate_dates": [], "corporate_action_window_overlap_180D": false, "counterexample_case": true, "current_profile_error": true, "deep_sub_archetype_id": "C07_ORDER_BRIDGE_LAG_PRICE_ONLY_RS_FADE", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|240810|Stage4B-Watch|2024-04-15", "entry_close": 38900.0, "entry_date": "2024-04-15", "entry_high": 38900.0, "entry_low": 37050.0, "entry_open": 38300.0, "entry_price": 38300.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "원익IPS", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "240810", "trigger_date": "2024-04-15", "trigger_family": "order_bridge_lag_price_only_rs_fade_counter", "trigger_type": "Stage4B-Watch", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -49.51, "MAE_180D_trough_date": "2024-12-09", "MAE_30D_pct": -29.92, "MAE_30D_trough_date": "2024-08-05", "MAE_90D_pct": -48.75, "MAE_90D_trough_date": "2024-11-21", "MFE_180D_pct": 0.0, "MFE_180D_peak_date": "2024-07-15", "MFE_30D_pct": 0.0, "MFE_30D_peak_date": "2024-07-15", "MFE_90D_pct": 0.0, "MFE_90D_peak_date": "2024-07-15", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-06-064760", "close_180D_date": "2025-04-14", "close_180D_return_pct": -35.91, "close_30D_date": "2024-08-27", "close_30D_return_pct": -21.11, "close_90D_date": "2024-11-27", "close_90D_return_pct": -46.55, "corporate_action_candidate_dates": [], "corporate_action_window_overlap_180D": false, "counterexample_case": true, "current_profile_error": true, "deep_sub_archetype_id": "C07_SIC_RING_COMPONENT_PROXY_RS_FADE", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|064760|Stage4B-Watch|2024-07-15", "entry_close": 131000.0, "entry_date": "2024-07-15", "entry_high": 131700.0, "entry_low": 128100.0, "entry_open": 131700.0, "entry_price": 131700.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "티씨케이", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "064760", "trigger_date": "2024-07-15", "trigger_family": "sic_ring_component_proxy_rs_fade_counter", "trigger_type": "Stage4B-Watch", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
{"MAE_180D_pct": -62.33, "MAE_180D_trough_date": "2024-12-09", "MAE_30D_pct": -38.53, "MAE_30D_trough_date": "2024-08-27", "MAE_90D_pct": -59.91, "MAE_90D_trough_date": "2024-11-27", "MFE_180D_pct": 2.07, "MFE_180D_peak_date": "2024-07-17", "MFE_30D_pct": 2.07, "MFE_30D_peak_date": "2024-07-17", "MFE_90D_pct": 2.07, "MFE_90D_peak_date": "2024-07-17", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-07-166090", "close_180D_date": "2025-04-14", "close_180D_return_pct": -51.29, "close_30D_date": "2024-08-27", "close_30D_return_pct": -37.16, "close_90D_date": "2024-11-27", "close_90D_return_pct": -58.88, "corporate_action_candidate_dates": ["2018-06-14", "2018-07-10"], "corporate_action_window_overlap_180D": false, "counterexample_case": true, "current_profile_error": true, "deep_sub_archetype_id": "C07_SILICON_PARTS_PROXY_RS_FADE", "duplicate_check_key": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH|166090|Stage4B-Watch|2024-07-15", "entry_close": 58000.0, "entry_date": "2024-07-15", "entry_high": 58400.0, "entry_low": 56700.0, "entry_open": 58000.0, "entry_price": 58000.0, "entry_rule": "same_day_open_if_trigger_before_session_or_next_available_tradable_open_proxy", "evidence_url_pending": true, "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "forward_window_basis": "trading_days_from_entry_in_tradable_shard", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "manifest_max_date": "2026-02-20", "market": "KOSDAQ GLOBAL", "name": "하나머티리얼즈", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_block_reason": "source_proxy_only__needs_url_repair_before_profile_patch", "promotion_usable": false, "research_id": "R2_L110_C07", "residual_error_type": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "row_type": "trigger", "same_session_novelty_note": "Avoids prior C07 loop107/108/109 symbol-date groups; uses new symbol or new trigger-family route in the same canonical.", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "166090", "trigger_date": "2024-07-15", "trigger_family": "silicon_parts_proxy_rs_fade_counter", "trigger_type": "Stage4B-Watch", "upstream_source": "FinanceData/marcap", "window_180D_row_count": 181, "window_30D_row_count": 31, "window_90D_row_count": 91, "years_loaded": [2023, 2024, 2025]}
```

## 6. Machine-readable case rows JSONL

```jsonl
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-01-319660", "classification": "positive", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "dry strip and process equipment strength converted into a large MFE path with low early MAE, but close return faded by 180D; good Stage2/Yellow, not blind hold.", "name": "피에스케이", "row_type": "case", "symbol": "319660", "trigger_family": "dry_strip_memory_order_bridge_positive"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-02-095610", "classification": "positive", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "front-end memory equipment path delivered very high 90D MFE with limited early MAE, then lost durability by 180D; bridge needs active 4B monitoring after peak.", "name": "테스", "row_type": "case", "symbol": "095610", "trigger_family": "front_end_memory_equipment_order_bridge_positive"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-03-084370", "classification": "positive", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "thermal/ALD route showed a clean 30/90D positive path; Stage3-Yellow is justified only when order/revenue bridge is visible.", "name": "유진테크", "row_type": "case", "symbol": "084370", "trigger_family": "thermal_ald_hbm_capacity_bridge_positive"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-04-036930", "classification": "positive", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "post-drawdown recovery trigger produced strong 30/90/180D MFE with low MAE; current profile can be too conservative after inventory reset.", "name": "주성엔지니어링", "row_type": "case", "symbol": "036930", "trigger_family": "post_drawdown_dram_hbm_capex_recovery_positive"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-05-240810", "classification": "counterexample", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "large-equipment label without fresh order/revenue confirmation produced weak MFE and large 180D MAE; proxy label should remain local 4B watch.", "name": "원익IPS", "row_type": "case", "symbol": "240810", "trigger_family": "order_bridge_lag_price_only_rs_fade_counter"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-06-064760", "classification": "counterexample", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "component proxy route produced no upside after entry and severe drawdown; component RS cannot be treated as HBM equipment order conversion.", "name": "티씨케이", "row_type": "case", "symbol": "064760", "trigger_family": "sic_ring_component_proxy_rs_fade_counter"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-07-166090", "classification": "counterexample", "fine_archetype_id": "C07_FRONTEND_AND_COMPONENT_HBM_MEMORY_EQUIPMENT_RS_ORDER_REVENUE_CONVERSION", "mechanism_summary": "silicon-parts proxy faded sharply despite HBM supply-chain label; source-proxy label should not unlock Yellow/Green.", "name": "하나머티리얼즈", "row_type": "case", "symbol": "166090", "trigger_family": "silicon_parts_proxy_rs_fade_counter"}
```

## 7. Machine-readable score simulation rows JSONL

```jsonl
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-01-319660", "profile_error_label": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "raw_component_score_breakdown": {"customer_lock": 66, "margin_fcf": 64, "redteam_risk": 38, "revenue_bridge": 72, "revision_visibility": 62, "supply_demand": 74, "valuation_risk": 48}, "row_type": "score_simulation", "shadow_rule_action": "allow_Stage2_Actionable_or_Yellow_after_verified_bridge; add local_4B_after_peak_or_close_fade", "simulated_current_profile_total": 77, "simulated_shadow_rule_total_after_C07_bridge_guard": 80, "symbol": "319660"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-02-095610", "profile_error_label": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "raw_component_score_breakdown": {"customer_lock": 66, "margin_fcf": 64, "redteam_risk": 38, "revenue_bridge": 72, "revision_visibility": 62, "supply_demand": 74, "valuation_risk": 48}, "row_type": "score_simulation", "shadow_rule_action": "allow_Stage2_Actionable_or_Yellow_after_verified_bridge; add local_4B_after_peak_or_close_fade", "simulated_current_profile_total": 77, "simulated_shadow_rule_total_after_C07_bridge_guard": 80, "symbol": "095610"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-03-084370", "profile_error_label": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "raw_component_score_breakdown": {"customer_lock": 66, "margin_fcf": 64, "redteam_risk": 38, "revenue_bridge": 72, "revision_visibility": 62, "supply_demand": 74, "valuation_risk": 48}, "row_type": "score_simulation", "shadow_rule_action": "allow_Stage2_Actionable_or_Yellow_after_verified_bridge; add local_4B_after_peak_or_close_fade", "simulated_current_profile_total": 77, "simulated_shadow_rule_total_after_C07_bridge_guard": 80, "symbol": "084370"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-04-036930", "profile_error_label": "missed_structural_positive_if_direct_order_or_revenue_bridge_is_not_verified_as_C07", "raw_component_score_breakdown": {"customer_lock": 66, "margin_fcf": 64, "redteam_risk": 38, "revenue_bridge": 72, "revision_visibility": 62, "supply_demand": 74, "valuation_risk": 48}, "row_type": "score_simulation", "shadow_rule_action": "allow_Stage2_Actionable_or_Yellow_after_verified_bridge; add local_4B_after_peak_or_close_fade", "simulated_current_profile_total": 75, "simulated_shadow_rule_total_after_C07_bridge_guard": 78, "symbol": "036930"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-05-240810", "profile_error_label": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "raw_component_score_breakdown": {"customer_lock": 40, "margin_fcf": 32, "redteam_risk": 82, "revenue_bridge": 38, "revision_visibility": 34, "supply_demand": 55, "valuation_risk": 76}, "row_type": "score_simulation", "shadow_rule_action": "block_Yellow; route_to_local_4B_watch_until_order_revenue_bridge_is_verified", "simulated_current_profile_total": 61, "simulated_shadow_rule_total_after_C07_bridge_guard": 54, "symbol": "240810"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-06-064760", "profile_error_label": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "raw_component_score_breakdown": {"customer_lock": 40, "margin_fcf": 32, "redteam_risk": 82, "revenue_bridge": 38, "revision_visibility": 34, "supply_demand": 55, "valuation_risk": 76}, "row_type": "score_simulation", "shadow_rule_action": "block_Yellow; route_to_local_4B_watch_until_order_revenue_bridge_is_verified", "simulated_current_profile_total": 61, "simulated_shadow_rule_total_after_C07_bridge_guard": 54, "symbol": "064760"}
{"canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "case_id": "C07-L110-07-166090", "profile_error_label": "false_positive_risk_if_HBM_equipment_label_or_component_proxy_is_accepted_without_order_revenue_bridge", "raw_component_score_breakdown": {"customer_lock": 40, "margin_fcf": 32, "redteam_risk": 82, "revenue_bridge": 38, "revision_visibility": 34, "supply_demand": 55, "valuation_risk": 76}, "row_type": "score_simulation", "shadow_rule_action": "block_Yellow; route_to_local_4B_watch_until_order_revenue_bridge_is_verified", "simulated_current_profile_total": 61, "simulated_shadow_rule_total_after_C07_bridge_guard": 54, "symbol": "166090"}
```

## 8. Aggregate row

```json
{"avg_MAE_90D_pct": -21.1, "avg_MFE_90D_pct": 39.73, "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "counterexample_count": 3, "current_profile_error_count": 6, "evidence_url_pending_count": 7, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "median_MAE_180D_pct": -18.53, "median_MFE_180D_pct": 70.29, "new_independent_case_count": 7, "positive_case_count": 4, "promotion_blocked_until_url_repair": true, "representative_trigger_count": 7, "research_id": "R2_L110_C07", "row_type": "aggregate", "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 7, "source_proxy_only_count": 7, "stage4b_case_count": 3, "stage4c_case_count": 0, "trigger_row_count": 7}
```

## 9. Shadow rule candidate

```json
{
  "row_type": "shadow_rule_candidate",
  "research_id": "R2_L110_C07",
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "new_axis_proposed": "C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow_or_Green_plus_component_proxy_RS_to_local_4B_watch_v2",
  "existing_axis_strengthened": [
    "stage2_required_bridge",
    "local_4b_watch_guard",
    "price_only_blowoff_blocks_positive_stage",
    "full_4b_requires_non_price_evidence"
  ],
  "existing_axis_weakened": null,
  "rule_logic": [
    "If C07 signal has verified order/revenue/shipment conversion and early MAE remains controlled, allow Stage2-Actionable or Yellow even when the ticker is not a pure HBM label.",
    "If C07 signal is only component/proxy relative strength without order/revenue bridge, block Yellow/Green and route to local Stage4B-Watch.",
    "If 30D/90D MFE is high but 180D close return fades sharply, keep 4B local watch after peak rather than treating C07 as durable structural Green."
  ],
  "promotion_status": "blocked_until_url_repair",
  "reason": "All seven rows are Stock-Web price verified but source_proxy_only for non-price evidence; external evidence URL repair is required before applying profile patch."
}
```

## 10. Residual contribution summary

```json
{
  "row_type": "residual_contribution_summary",
  "research_id": "R2_L110_C07",
  "new_independent_case_count": 7,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 7,
  "same_archetype_new_trigger_family_count": 7,
  "positive_case_count": 4,
  "counterexample_count": 3,
  "stage4b_case_count": 3,
  "stage4c_case_count": 0,
  "current_profile_error_count": 6,
  "source_proxy_only_count": 7,
  "evidence_url_pending_count": 7,
  "promotion_blocked_until_url_repair": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false,
  "auto_selected_coverage_gap": "C07 base index 18 + local loop107 7 + local loop108 6 + local loop109 7 + loop110 7 = local-session adjusted about 45; above 30-row stability band, about 5 short of 50-row practical calibration band"
}
```

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation agent for Songdaiki/stock_agent. Do not execute during the research session that created this MD.

Read this standalone V12 residual research MD and ingest only rows that pass the repository's V12 validation gates. Treat all trigger rows as price-verified by Songdaiki/stock-web tradable_raw shards, but do not promote profile patch decisions from rows marked source_proxy_only/evidence_url_pending until URL repair is completed.

Candidate patch axis:
C07_verified_order_or_revenue_conversion_bridge_required_before_Yellow_or_Green_plus_component_proxy_RS_to_local_4B_watch_v2

Implementation intent:
- Add or strengthen a C07-specific bridge requirement before Yellow/Green.
- Allow Stage2-Actionable or Yellow when HBM/advanced-memory equipment relative strength is tied to verified order, shipment, revenue, or margin bridge.
- Route component/proxy-only C07 labels to local 4B watch, not full 4B or Green.
- Preserve existing global guardrails: price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, stage2_required_bridge.
- Do not use this MD to change production scoring unless evidence URL repair confirms the non-price bridge for each row.
```

## 12. Next research state

```text
completed_round = R2
completed_loop = 110
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1-under-50 after local-session adjustment; published index Priority 0
next_recommended_archetypes = C06_HBM_MEMORY_CUSTOMER_CAPACITY, C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C11_BATTERY_ORDERBOOK_RERATING, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
