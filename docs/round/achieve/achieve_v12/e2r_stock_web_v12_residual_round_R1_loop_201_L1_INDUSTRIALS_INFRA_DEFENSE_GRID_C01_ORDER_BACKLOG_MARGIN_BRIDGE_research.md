# E2R Stock-Web v12 Residual Research — R1 / C01 backlog-margin bridge quality repair

```text
research_file = e2r_stock_web_v12_residual_round_R1_loop_201_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md
selected_round = R1
selected_loop = 201
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 1 balance reinforcement / C01 backlog-to-FCF counterexample repair
round_schedule_status = coverage_index_selected
round_sector_consistency = pass

large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = C01_BACKLOG_MARGIN_SECOND_BRIDGE_AND_HIGH_MAE_CAP_REPAIR
loop_objective = stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_green_cap | holdout_validation

production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Coverage-index selection

`V12_Research_No_Repeat_Index.md` is used only as the no-repeat ledger. The current corpus is no longer a raw row-count fill problem, so this loop uses Priority 1 balance reinforcement for `C01_ORDER_BACKLOG_MARGIN_BRIDGE`: order/backlog language must be separated from actual margin, FCF, and working-capital conversion.

This batch avoids the previous visible C01 duplicate keys by using different `symbol + trigger_type + entry_date` combinations and promotes only rows whose 180-tradable-day share-count window is clean.

## 2. Price source validation

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
stock_web_manifest_max_date = 2026-02-20
tradable_schema = d,o,h,l,c,v,a,mc,s,m
mfe_formula = (max high from entry_date through N tradable rows / entry close - 1) * 100
mae_formula = (min low from entry_date through N tradable rows / entry close - 1) * 100
corporate_action_check = shares_unique_180D == 1 for promoted trigger rows
```

All promoted trigger rows below have at least 180 tradable forward rows, complete 30D/90D/180D MFE/MAE fields, and `corporate_action_contaminated_180D = false`.

## 3. Promoted case matrix

| symbol | company | trigger | entry | entry close | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | corporate-action status | current profile verdict |
|---|---|---|---:|---:|---|---:|---:|---:|---|---|
| 097230 | HJ Shipbuilding & Construction | Stage2 | 2025-01-08 | 7,270 | positive_control_but_stage2_cap | 6.60/-20.36 | 36.18/-22.56 | 372.49/-22.56 | clean_180D_window | green_block_needed |
| 010620 | HD Hyundai Mipo | Stage2-Actionable | 2025-02-06 | 115,600 | positive_actionable_margin_bridge | 9.43/-12.54 | 78.20/-13.93 | 119.29/-13.93 | clean_180D_window | green_block_needed |
| 010140 | Samsung Heavy Industries | Stage2-Actionable | 2024-07-26 | 11,870 | high_mae_success | 3.45/-19.71 | 3.54/-21.40 | 33.45/-21.40 | clean_180D_window | green_block_needed |
| 010140 | Samsung Heavy Industries | Stage2-Actionable | 2025-03-21 | 14,580 | positive_actionable_backlog_to_profit_bridge | 7.82/-13.24 | 35.67/-13.24 | 122.91/-13.24 | clean_180D_window | green_block_needed |
| 329180 | HD Hyundai Heavy Industries | Stage2-Actionable | 2024-07-31 | 211,000 | positive_actionable_before_full_acceleration | 5.45/-19.48 | 15.88/-19.95 | 92.89/-19.95 | clean_180D_window | green_block_needed |
| 042660 | Hanwha Ocean | Stage3-Yellow | 2025-04-28 | 89,300 | positive_yellow_backlog_to_sales_bridge | 6.72/-18.03 | 38.63/-19.93 | 70.66/-19.93 | clean_180D_window | green_block_needed |
| 010620 | HD Hyundai Mipo | Stage4B | 2024-04-26 | 73,500 | counterexample_to_overhard_4c | 8.03/-6.67 | 67.07/-6.67 | 96.33/-6.67 | clean_180D_window | hard_4c_too_early_if_used |

## 4. Case notes

### 4.1 HJ Shipbuilding & Construction / 097230 / Stage2 / 2025-01-08
HJ Shipbuilding reported KRW4.69tn 2024 order intake, including KRW1.75tn shipbuilding orders; this is strong backlog/order evidence but not yet a verified FCF or working-capital conversion bridge.

Stock-Web path: `30D 6.60/-20.36`, `90D 36.18/-22.56`, `180D 372.49/-22.56`. Order-intake record should allow C01 Stage2, but Actionable/Yellow should wait for margin or cash conversion. The forward path was a huge 180D winner after a deep early valley, so Green must remain MAE-capped.

### 4.2 HD Hyundai Mipo / 010620 / Stage2-Actionable / 2025-02-06
HD Hyundai Mipo swung to 2024 operating profit after a prior-year loss and revenue rose; this gives actual margin conversion after the backlog cycle rather than only order intake.

Stock-Web path: `30D 9.43/-12.54`, `90D 78.20/-13.93`, `180D 119.29/-13.93`. This is proper C01 Stage2-Actionable: backlog/order cycle plus actual margin conversion. Green remains blocked until FCF/working-capital evidence appears.

### 4.3 Samsung Heavy Industries / 010140 / Stage2-Actionable / 2024-07-26
Q2 net income and operating profit rose sharply while sales rose 30.1%; this is an earnings conversion bridge, but the stock still entered a deep drawdown before the 180D recovery.

Stock-Web path: `30D 3.45/-19.71`, `90D 3.54/-21.40`, `180D 33.45/-21.40`. Direct earnings evidence supports Stage2-Actionable, but the -21.40% 90D/180D MAE blocks Green and keeps this as a high-MAE positive control.

### 4.4 Samsung Heavy Industries / 010140 / Stage2-Actionable / 2025-03-21
2024 operating profit improved with high-value LNG and container-vessel order mix and 2025 order-target language, adding a backlog-to-profit bridge.

Stock-Web path: `30D 7.82/-13.24`, `90D 35.67/-13.24`, `180D 122.91/-13.24`. C01 should recognize high-value-vessel mix and operating-profit conversion as Actionable, but Green still needs multi-quarter cash/working-capital proof.

### 4.5 HD Hyundai Heavy Industries / 329180 / Stage2-Actionable / 2024-07-31
HD Hyundai group Q2 reporting showed shipbuilding profit growth, high-value dual-fuel ship revenue reflection, order-screening, cost reduction and annual order target already exceeded.

Stock-Web path: `30D 5.45/-19.48`, `90D 15.88/-19.95`, `180D 92.89/-19.95`. This is a clean C01 Stage2-Actionable bridge from order quality to margin. The early -19.95% MAE still argues for Yellow/Green gating until persistence is seen.

### 4.6 Hanwha Ocean / 042660 / Stage3-Yellow / 2025-04-28
Q1 2025 operating income spiked 388.8% YoY and management tied the bottom line to high-value premium ships, including LNG vessels, while new orders continued.

Stock-Web path: `30D 6.72/-18.03`, `90D 38.63/-19.93`, `180D 70.66/-19.93`. Actual earnings conversion plus high-value ship mix supports Stage3-Yellow. Green remains withheld because 180D MAE still approached -20% and FCF evidence is not explicit.

### 4.7 HD Hyundai Mipo / 010620 / Stage4B / 2024-04-26
HD Hyundai Mipo was still expected to post a Q1 loss due to low-priced orders and production-stabilization costs, but the same report noted order-book expansion and expected full-year turnaround.

Stock-Web path: `30D 8.03/-6.67`, `90D 67.07/-6.67`, `180D 96.33/-6.67`. This should be local 4B/watch, not hard 4C: bad margin evidence existed, but backlog/order-cycle offset survived and the 180D price path recovered strongly.

## 5. Residual contribution summary

```text
loop_contribution_label = canonical_archetype_rule_candidate | high_MAE_green_cap | second_bridge_required | 4B_not_hard_4C_when_offset_survives
canonical_rule_candidate = C01_SECOND_BRIDGE_REQUIRED_FOR_ACTIONABLE_AND_YELLOW
sector_rule_candidate = L1_BACKLOG_MARGIN_FCF_AND_HIGH_MAE_CAP_GATE
do_not_propose_new_weight_delta = false
production_scoring_changed = false
shadow_weight_only = true
```

Proposed shadow logic:

1. **Order/backlog headline alone** may enter Stage2, but should not become Stage2-Actionable or Yellow without a second bridge.
2. The second bridge can be actual operating-profit turn, high-value vessel mix reflected in revenue, order-screening strategy, production stabilization, supplier order-to-sales conversion, or explicit cost-rate normalization.
3. **Stage3-Yellow** is allowed when actual earnings conversion and backlog/order bridge coexist.
4. **Stage3-Green remains blocked** until FCF / working-capital / cash conversion is visible across more than one evidence family.
5. A quarterly loss, cost shock, or cost-rate headline becomes **local 4B/watch** first if backlog/mix offset is alive.
6. **Hard 4C** requires backlog collapse, liquidity stress, accounting-trust break, customer cancellation, or execution failure with weak offset quality.

## 6. Machine-readable JSONL trigger rows

```jsonl
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_001_097230_Stage2_20250108", "case_role": "positive_control_but_stage2_cap", "company": "HJ Shipbuilding & Construction", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "green_too_loose_if_high_mae_ignored", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|097230|Stage2|2025-01-08", "entry_date": "2025-01-08", "entry_market": "KOSPI", "entry_ohlc": {"c": 7270.0, "h": 7750.0, "l": 6860.0, "o": 7140.0, "v": 3696076}, "entry_price": 7270.0, "evidence_date": "2025-01-08", "evidence_family": "shipbuilding_record_order_intake_stage2_cap", "evidence_summary": "HJ Shipbuilding reported KRW4.69tn 2024 order intake, including KRW1.75tn shipbuilding orders; this is strong backlog/order evidence but not yet a verified FCF or working-capital conversion bridge.", "evidence_url_pending": false, "fine_archetype_id": "SHIPBUILDING_RECORD_ORDER_INTAKE_STAGE2_CAP", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|097230|Stage2|2025-01-08", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -22.56, "mae_30d_pct": -20.36, "mae_90d_pct": -22.56, "max_high_180d": 34350.0, "mfe_180d_pct": 372.49, "mfe_30d_pct": 6.6, "mfe_90d_pct": 36.18, "min_low_180d": 5630.0, "peak_date_180d": "2025-09-10", "positive_or_counterexample": "guardrail_positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/097/097230/2025.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 72, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://pulse.mk.co.kr/news/english/11212735", "stock_web_manifest_max_date": "2026-02-20", "ticker": "097230", "trigger_type": "Stage2", "trough_date_180d": "2025-04-07"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_002_010620_Stage2Actionable_20250206", "case_role": "positive_actionable_margin_bridge", "company": "HD Hyundai Mipo", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "stage2_actionable_or_yellow_supported_but_green_still_blocked", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage2-Actionable|2025-02-06", "entry_date": "2025-02-06", "entry_market": "KOSPI", "entry_ohlc": {"c": 115600.0, "h": 126500.0, "l": 115000.0, "o": 125800.0, "v": 1262929}, "entry_price": 115600.0, "evidence_date": "2025-02-06", "evidence_family": "mipo_full_year_swing_to_black_margin_bridge", "evidence_summary": "HD Hyundai Mipo swung to 2024 operating profit after a prior-year loss and revenue rose; this gives actual margin conversion after the backlog cycle rather than only order intake.", "evidence_url_pending": false, "fine_archetype_id": "MIPO_FULL_YEAR_SWING_TO_BLACK_MARGIN_BRIDGE", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage2-Actionable|2025-02-06", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -13.93, "mae_30d_pct": -12.54, "mae_90d_pct": -13.93, "max_high_180d": 253500.0, "mfe_180d_pct": 119.29, "mfe_30d_pct": 9.43, "mfe_90d_pct": 78.2, "min_low_180d": 99500.0, "peak_date_180d": "2025-10-27", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2025.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 92, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://en.yna.co.kr/view/AEN20250206006600320", "stock_web_manifest_max_date": "2026-02-20", "ticker": "010620", "trigger_type": "Stage2-Actionable", "trough_date_180d": "2025-03-28"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_003_010140_Stage2Actionable_20240726", "case_role": "high_mae_success", "company": "Samsung Heavy Industries", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "green_too_loose_if_high_mae_ignored", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2024-07-26", "entry_date": "2024-07-26", "entry_market": "KOSPI", "entry_ohlc": {"c": 11870.0, "h": 12280.0, "l": 11100.0, "o": 11190.0, "v": 42712575}, "entry_price": 11870.0, "evidence_date": "2024-07-25", "evidence_family": "samsung_heavy_q2_profit_high_mae_cap", "evidence_summary": "Q2 net income and operating profit rose sharply while sales rose 30.1%; this is an earnings conversion bridge, but the stock still entered a deep drawdown before the 180D recovery.", "evidence_url_pending": false, "fine_archetype_id": "SAMSUNG_HEAVY_Q2_PROFIT_HIGH_MAE_CAP", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2024-07-26", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -21.4, "mae_30d_pct": -19.71, "mae_90d_pct": -21.4, "max_high_180d": 15840.0, "mfe_180d_pct": 33.45, "mfe_30d_pct": 3.45, "mfe_90d_pct": 3.54, "min_low_180d": 9330.0, "peak_date_180d": "2025-03-19", "positive_or_counterexample": "guardrail_positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010140/2024.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 92, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://en.yna.co.kr/view/AEN20240725009200320", "stock_web_manifest_max_date": "2026-02-20", "ticker": "010140", "trigger_type": "Stage2-Actionable", "trough_date_180d": "2024-09-09"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_004_010140_Stage2Actionable_20250321", "case_role": "positive_actionable_backlog_to_profit_bridge", "company": "Samsung Heavy Industries", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "stage2_actionable_or_yellow_supported_but_green_still_blocked", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2025-03-21", "entry_date": "2025-03-21", "entry_market": "KOSPI", "entry_ohlc": {"c": 14580.0, "h": 14690.0, "l": 14140.0, "o": 14450.0, "v": 10733577}, "entry_price": 14580.0, "evidence_date": "2025-03-21", "evidence_family": "samsung_heavy_2024_op_high_value_vessel_mix", "evidence_summary": "2024 operating profit improved with high-value LNG and container-vessel order mix and 2025 order-target language, adding a backlog-to-profit bridge.", "evidence_url_pending": false, "fine_archetype_id": "SAMSUNG_HEAVY_2024_OP_HIGH_VALUE_VESSEL_MIX", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010140|Stage2-Actionable|2025-03-21", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -13.24, "mae_30d_pct": -13.24, "mae_90d_pct": -13.24, "max_high_180d": 32500.0, "mfe_180d_pct": 122.91, "mfe_30d_pct": 7.82, "mfe_90d_pct": 35.67, "min_low_180d": 12650.0, "peak_date_180d": "2025-10-30", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010140/2025.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 92, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://www.imarinenews.com/20846.html", "stock_web_manifest_max_date": "2026-02-20", "ticker": "010140", "trigger_type": "Stage2-Actionable", "trough_date_180d": "2025-04-07"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_005_329180_Stage2Actionable_20240731", "case_role": "positive_actionable_before_full_acceleration", "company": "HD Hyundai Heavy Industries", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "stage2_actionable_or_yellow_supported_but_green_still_blocked", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage2-Actionable|2024-07-31", "entry_date": "2024-07-31", "entry_market": "KOSPI", "entry_ohlc": {"c": 211000.0, "h": 221000.0, "l": 203000.0, "o": 203500.0, "v": 502707}, "entry_price": 211000.0, "evidence_date": "2024-07-31", "evidence_family": "hd_hhi_q2_order_screening_profit_bridge", "evidence_summary": "HD Hyundai group Q2 reporting showed shipbuilding profit growth, high-value dual-fuel ship revenue reflection, order-screening, cost reduction and annual order target already exceeded.", "evidence_url_pending": false, "fine_archetype_id": "HD_HHI_Q2_ORDER_SCREENING_PROFIT_BRIDGE", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|329180|Stage2-Actionable|2024-07-31", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -19.95, "mae_30d_pct": -19.48, "mae_90d_pct": -19.95, "max_high_180d": 407000.0, "mfe_180d_pct": 92.89, "mfe_30d_pct": 5.45, "mfe_90d_pct": 15.88, "min_low_180d": 168900.0, "peak_date_180d": "2025-04-28", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 92, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://www.imarinenews.com/12422.html", "stock_web_manifest_max_date": "2026-02-20", "ticker": "329180", "trigger_type": "Stage2-Actionable", "trough_date_180d": "2024-11-06"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_006_042660_Stage3Yellow_20250428", "case_role": "positive_yellow_backlog_to_sales_bridge", "company": "Hanwha Ocean", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "stage2_actionable_or_yellow_supported_but_green_still_blocked", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage3-Yellow|2025-04-28", "entry_date": "2025-04-28", "entry_market": "KOSPI", "entry_ohlc": {"c": 89300.0, "h": 95300.0, "l": 88300.0, "o": 95000.0, "v": 6344048}, "entry_price": 89300.0, "evidence_date": "2025-04-28", "evidence_family": "hanwha_ocean_q1_high_value_premium_ship_yellow", "evidence_summary": "Q1 2025 operating income spiked 388.8% YoY and management tied the bottom line to high-value premium ships, including LNG vessels, while new orders continued.", "evidence_url_pending": false, "fine_archetype_id": "HANWHA_OCEAN_Q1_HIGH_VALUE_PREMIUM_SHIP_YELLOW", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|042660|Stage3-Yellow|2025-04-28", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -19.93, "mae_30d_pct": -18.03, "mae_90d_pct": -19.93, "max_high_180d": 152400.0, "mfe_180d_pct": 70.66, "mfe_30d_pct": 6.72, "mfe_90d_pct": 38.63, "min_low_180d": 71500.0, "peak_date_180d": "2026-01-15", "positive_or_counterexample": "positive", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042660/2025.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "yes_capped", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 22, "eps_fcf_explosion": 18, "information_confidence": 7, "market_mispricing": 12, "total": 92, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://en.yna.co.kr/view/AEN20250428006651320", "stock_web_manifest_max_date": "2026-02-20", "ticker": "042660", "trigger_type": "Stage3-Yellow", "trough_date_180d": "2025-07-07"}
{"calibration_usable": true, "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "case_id": "C01_R1L201_007_010620_Stage4B_20240426", "case_role": "counterexample_to_overhard_4c", "company": "HD Hyundai Mipo", "corporate_action_contaminated_180d": false, "corporate_action_window_status": "clean_180D_window", "current_profile_error": "hard_4c_overfire_if_offset_ignored", "duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage4B|2024-04-26", "entry_date": "2024-04-26", "entry_market": "KOSPI", "entry_ohlc": {"c": 73500.0, "h": 74500.0, "l": 70000.0, "o": 70200.0, "v": 410961}, "entry_price": 73500.0, "evidence_date": "2024-04-26", "evidence_family": "mipo_low_priced_orders_loss_but_cycle_offset_4b", "evidence_summary": "HD Hyundai Mipo was still expected to post a Q1 loss due to low-priced orders and production-stabilization costs, but the same report noted order-book expansion and expected full-year turnaround.", "evidence_url_pending": false, "fine_archetype_id": "MIPO_LOW_PRICED_ORDERS_LOSS_BUT_CYCLE_OFFSET_4B", "forward_window_available_180d": true, "forward_window_trading_days": 180, "hard_duplicate_key": "C01_ORDER_BACKLOG_MARGIN_BRIDGE|010620|Stage4B|2024-04-26", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "mae_180d_pct": -6.67, "mae_30d_pct": -6.67, "mae_90d_pct": -6.67, "max_high_180d": 144300.0, "mfe_180d_pct": 96.33, "mfe_30d_pct": 8.03, "mfe_90d_pct": 67.07, "min_low_180d": 68600.0, "peak_date_180d": "2025-01-21", "positive_or_counterexample": "counterexample", "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "price_source": "Songdaiki/stock-web", "production_scoring_changed": false, "round": "R1", "row_type": "trigger", "score_simulation": {"current_profile_proxy": "e2r_2_2_rolling_calibrated", "green_allowed": "no", "positive_stage_allowed": "no_watch_only", "raw_component_score_breakdown": {"bottleneck_pricing": 17, "capital_allocation": 5, "earnings_visibility": 13, "eps_fcf_explosion": 8, "information_confidence": 7, "market_mispricing": 12, "total": 63, "valuation_rerating": 11}, "reason": "C01 positive cases need margin/FCF conversion; Green remains blocked until cash conversion / multi-quarter evidence."}, "shadow_weight_only": true, "shares_unique_180d": 1, "source_proxy_only": false, "source_url": "https://www.imarinenews.com/8776.html", "stock_web_manifest_max_date": "2026-02-20", "ticker": "010620", "trigger_type": "Stage4B", "trough_date_180d": "2024-06-10"}
```

## 7. Aggregate shadow row

```json
{
  "avg_mae_180d_pct": -16.81,
  "avg_mae_90d_pct": -16.81,
  "avg_mfe_180d_pct": 129.72,
  "avg_mfe_90d_pct": 39.31,
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "case_count": 7,
  "counterexample_or_guardrail_case_count": 3,
  "do_not_propose_new_weight_delta": false,
  "fine_archetype_id": "C01_BACKLOG_MARGIN_SECOND_BRIDGE_AND_HIGH_MAE_CAP_REPAIR",
  "guardrail_positive_count": 2,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "positive_case_count": 4,
  "production_scoring_changed": false,
  "round": "R1",
  "row_type": "aggregate_shadow_weight",
  "shadow_rule_candidate": "C01_BACKLOG_MARGIN_FCF_TWO_STEP_GATE",
  "shadow_weight_only": true,
  "stage4b_case_count": 1,
  "stage4c_case_count": 0,
  "usable_trigger_count": 7
}
```

## 8. Validation self-audit

```text
new_independent_case_count = 7
new_independent_trigger_count = 7
unique_symbol_count = 5
positive_case_count = 4
guardrail_positive_count = 2
counterexample_case_count = 1
source_proxy_only_count = 0
evidence_url_pending_count = 0
missing_required_mfe_mae_count = 0
corporate_action_contaminated_180D_count = 0
insufficient_forward_window_180D_count = 0
production_scoring_changed = false
shadow_weight_only = true
ready_for_batch_ingest = true
```

| gate | status |
|---|---|
| standard v12 filename | pass |
| selected_round / filename_round match | pass |
| selected_loop / filename_loop match | pass |
| large_sector_id valid for round | pass |
| canonical_archetype_id valid | pass |
| actual stock-web manifest/profile checked | pass |
| every usable trigger has entry_price | pass |
| every usable trigger has 30/90/180D MFE/MAE | pass |
| hard duplicate key avoided | pass |
| positive/counterexample/guardrail balance included | pass |
| R13 naming misuse | not applicable |
| production scoring changed | false |

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not apply this MD alone as a production patch. In the next batch calibration/coding session, ingest this file with the rest of docs/round using the v12 parser. Treat the proposed candidate C01_BACKLOG_MARGIN_FCF_TWO_STEP_GATE as a shadow rule only. Validate duplicate keys, confirm the Stock-Web price rows, and compare against the cumulative representative trigger rows before promotion.

Expected implementation target if the batch supports it:
- Add or strengthen C01-specific bridge checks.
- Preserve Stage2 for order/backlog-only evidence.
- Require a second bridge for Stage2-Actionable and Yellow.
- Keep Green gated by FCF/working-capital/multi-quarter conversion.
- Keep single-quarter loss headlines in local 4B/watch if backlog/mix offset survives.
```

## 10. Next Research State

```text
completed_round: R1
completed_loop: 201
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance / quality reinforcement
round_schedule_status: coverage_index_selected
round_sector_consistency: pass

next_recommended_archetypes:
- C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_DIRECT_ROW_REPAIR
- C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_HARD_4C_DIRECT_BREAK_PAIR
- C05_EPC_MEGA_CONTRACT_MARGIN_GAP_HARD_4C_DIRECT_BREAK_ONLY
- R13_CROSS_ARCHETYPE_HIGH_MAE_GUARDRAIL_HOLDOUT_REFRESH
- C01_ORDER_BACKLOG_MARGIN_BRIDGE_WORKING_CAPITAL_CASHFLOW_ONLY_REPAIR
```
