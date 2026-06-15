# E2R Stock-Web V12 Residual Research — R1 loop 113 — C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY

## 0. Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selected_round = R1
selected_loop = 113
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3
deep_sub_archetype_id = C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE
output_filename = e2r_stock_web_v12_residual_round_R1_loop_113_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

## 1. Selection basis

The execution prompt requires `coverage_index_first`, not a mechanical R1→R13 rotation. After the local session filled most Priority 0/1 gaps to the 50-row practical calibration band, this loop selects `C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY` as a Priority 2 quality-repair target. The published No-Repeat Index shows C04 with 71 representative rows, 16 symbols, 0 positive / 32 counterexample rows, and 12/0 4B/4C rows; that means the archetype is not under-covered, but it is skewed toward counterexamples and lacks hard 4C confirmation.

Visible `docs/round` listing shows prior standard C04 loops at `R1_loop_100`, `105`, `106`, `109`, and `112`; therefore this file uses `R1_loop_113`.

## 2. Price atlas validation scope

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
manifest_max_date = 2026-02-20
MFE/MAE windows = 30 / 90 / 180 tradable rows from entry_date, using entry_date open as entry_price
```

All rows below use downloaded `stock-web` tradable CSV shards for 2024, 2025, and where needed 2026. The computed MFE/MAE values are based on raw, unadjusted OHLC from those shards. Company-specific bridge URLs are intentionally marked pending; this loop is usable as residual calibration evidence but should remain blocked for promotion until URL repair confirms each issuer-specific project/order/revenue bridge.

## 3. Event frame

This loop compresses several C04 fine paths into one canonical rule candidate:

- Czech preferred-bidder win created a large nuclear-export project rerating path.
- Westinghouse/EDF appeals and Czech antitrust/court procedures created real contract-signing delay risk.
- January 2025 IP settlement with Westinghouse removed one legal overhang, but not every listed nuclear proxy had the same revenue bridge.
- May 2025 court-block style headlines show why generic project-delay news should not automatically become hard 4C unless order qualification, contract signing, or issuer-level revenue bridge actually breaks.

## 4. Trigger summary table

|symbol|company_name|trigger_type|trigger_date|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|observed_path_label|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|034020|두산에너빌리티|Stage3-Yellow|2025-01-17|2025-01-17|21500.00|43.72|-1.63|102.09|-7.16|293.95|-7.16|positive_structural_repricing|
|052690|한전기술|Stage3-Yellow|2025-01-17|2025-01-17|64800.00|17.13|-5.71|17.13|-23.15|87.81|-23.15|positive_high_MAE_bridge|
|051600|한전KPS|Stage2-Actionable|2025-01-17|2025-01-17|44250.00|8.70|-6.78|8.70|-14.12|47.80|-14.12|slow_counterexample|
|105840|우진|Stage4B|2024-10-30|2024-10-30|8400.00|0.83|-32.98|1.19|-32.98|58.33|-32.98|counterexample_high_MAE_recovery|
|083650|비에이치아이|Stage2-Actionable|2024-07-18|2024-07-18|10210.00|3.13|-30.46|95.10|-31.44|142.90|-31.44|positive_after_high_MAE|
|094820|일진파워|Stage4B|2024-08-27|2024-08-27|9500.00|7.68|-10.32|24.95|-27.37|45.16|-27.37|counterexample_local_4B|
|032820|우리기술|Stage4B|2025-05-07|2025-05-07|1709.00|173.84|-0.06|206.61|-0.06|483.97|-0.06|false_4B_positive_exception|
|011700|한신기계|Stage4B|2024-07-18|2024-07-18|5220.00|0.96|-41.00|0.96|-41.95|0.96|-54.79|hard_counterexample_label_fade|

## 5. Path interpretation

### 5.1 Positives

`034020`, `052690`, `083650`, and `032820` show that C04 legal-delay logic can be too conservative when a later legal/IP hurdle resolution or renewed project momentum remains alive. The positive path is not simply “nuclear theme went up”; it is “project/legal risk did not destroy the bridge, and the market later paid for the contract-option value.”

### 5.2 Counterexamples

`051600`, `105840`, `094820`, and `011700` show the other side of C04. O&M/service, small equipment, and label-only proxy names can suffer deep drawdowns when the contract is not signed or when appeals create uncertainty. `011700` is the cleanest hard-fade route: 180D MFE stayed below +1% while MAE reached -54.79%.

### 5.3 Residual current-profile error

The current calibrated profile already blocks price-only blowoff and requires non-price bridge for full 4B, but C04 still needs a narrower rule: legal/project delay headlines should not route to hard 4C unless the delay attacks the issuer-level bridge. Otherwise, as in `032820`, a court-block event can be a false 4B/4C signal inside a still-active theme squeeze.

## 6. Machine-readable trigger rows JSONL

```jsonl
{"MAE_180D_pct": -7.16, "MAE_30D_pct": -1.63, "MAE_90D_pct": -7.16, "MFE_180D_pct": 293.95, "MFE_30D_pct": 43.72, "MFE_90D_pct": 102.09, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_01_034020", "close_180D_pct": 273.02, "close_30D_pct": 23.26, "close_90D_pct": 98.37, "company_name": "두산에너빌리티", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": false, "current_profile_error": false, "current_profile_error_type": "none", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|034020|Stage3-Yellow|2025-01-17", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2025-01-17", "entry_price": 21500.0, "evidence_family": "Westinghouse_IP_settlement_Czech_contract_hurdle_removed", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "positive_structural_repricing", "peak_180D_date": "2025-10-16", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 70, "capital": 62, "eps": 78, "info": 76, "revision": 74, "valuation": 50, "visibility": 82}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "034020", "thesis": "IP settlement made Czech contract signing more investable; heavy nuclear equipment bridge was broad but visible.", "trigger_date": "2025-01-17", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 70.64}
{"MAE_180D_pct": -23.15, "MAE_30D_pct": -5.71, "MAE_90D_pct": -23.15, "MFE_180D_pct": 87.81, "MFE_30D_pct": 17.13, "MFE_90D_pct": 17.13, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_02_052690", "close_180D_pct": 50.77, "close_30D_pct": 1.85, "close_90D_pct": -5.71, "company_name": "한전기술", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": false, "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|052690|Stage3-Yellow|2025-01-17", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2025-01-17", "entry_price": 64800.0, "evidence_family": "Westinghouse_IP_settlement_engineering_design_bridge", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "positive_high_MAE_bridge", "peak_180D_date": "2025-06-25", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 55, "capital": 58, "eps": 58, "info": 75, "revision": 60, "valuation": 42, "visibility": 75}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "052690", "thesis": "Engineering/design exposure had strong long-window upside but 90D path carried high MAE; Yellow should require project-scope confirmation.", "trigger_date": "2025-01-17", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2025-04-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 60.56}
{"MAE_180D_pct": -14.12, "MAE_30D_pct": -6.78, "MAE_90D_pct": -14.12, "MFE_180D_pct": 47.8, "MFE_30D_pct": 8.7, "MFE_90D_pct": 8.7, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_03_051600", "close_180D_pct": 12.66, "close_30D_pct": -2.15, "close_90D_pct": -4.63, "company_name": "한전KPS", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": true, "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|051600|Stage2-Actionable|2025-01-17", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2025-01-17", "entry_price": 44250.0, "evidence_family": "O&M_service_bridge_after_IP_settlement", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "slow_counterexample", "peak_180D_date": "2025-06-25", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 38, "capital": 62, "eps": 52, "info": 68, "revision": 45, "valuation": 55, "visibility": 60}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "051600", "thesis": "O&M/service exposure is less levered to Czech EPC than construction/equipment; Stage2 requires maintenance backlog/revision bridge, not nuclear label alone.", "trigger_date": "2025-01-17", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 54.45}
{"MAE_180D_pct": -32.98, "MAE_30D_pct": -32.98, "MAE_90D_pct": -32.98, "MFE_180D_pct": 58.33, "MFE_30D_pct": 0.83, "MFE_90D_pct": 1.19, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_04_105840", "close_180D_pct": 26.19, "close_30D_pct": -27.38, "close_90D_pct": -7.38, "company_name": "우진", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": true, "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|105840|Stage4B|2024-10-30", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2024-10-30", "entry_price": 8400.0, "evidence_family": "UOHS_temporary_block_appeal_delay", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "counterexample_high_MAE_recovery", "peak_180D_date": "2025-06-19", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 45, "capital": 52, "eps": 35, "info": 60, "revision": 30, "valuation": 35, "visibility": 42}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "105840", "thesis": "Policy/project label could not absorb legal delay and no immediate order/revision bridge; local 4B watch was justified before later rebound.", "trigger_date": "2024-10-30", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 40.99}
{"MAE_180D_pct": -31.44, "MAE_30D_pct": -30.46, "MAE_90D_pct": -31.44, "MFE_180D_pct": 142.9, "MFE_30D_pct": 3.13, "MFE_90D_pct": 95.1, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_05_083650", "close_180D_pct": 94.61, "close_30D_pct": -22.43, "close_90D_pct": 66.11, "company_name": "비에이치아이", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": false, "current_profile_error": true, "current_profile_error_type": "false_4B_or_hard4C_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|083650|Stage2-Actionable|2024-07-18", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2024-07-18", "entry_price": 10210.0, "evidence_family": "Czech_preferred_bidder_supplier_order_bridge", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "positive_after_high_MAE", "peak_180D_date": "2025-02-14", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 62, "capital": 48, "eps": 60, "info": 65, "revision": 50, "valuation": 45, "visibility": 57}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": false, "stage4c_case": false, "symbol": "083650", "thesis": "Supplier/equipment proxy sold off first, then later rerated; C04 should avoid hard 4C without project/order cancellation.", "trigger_date": "2024-07-18", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-09-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 54.64}
{"MAE_180D_pct": -27.37, "MAE_30D_pct": -10.32, "MAE_90D_pct": -27.37, "MFE_180D_pct": 45.16, "MFE_30D_pct": 7.68, "MFE_90D_pct": 24.95, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_06_094820", "close_180D_pct": 23.47, "close_30D_pct": -4.21, "close_90D_pct": -10.42, "company_name": "일진파워", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": true, "current_profile_error": false, "current_profile_error_type": "none", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|094820|Stage4B|2024-08-27", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2024-08-27", "entry_price": 9500.0, "evidence_family": "Westinghouse_EDF_appeal_overhang", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "counterexample_local_4B", "peak_180D_date": "2025-05-26", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 45, "capital": 50, "eps": 42, "info": 58, "revision": 38, "valuation": 38, "visibility": 43}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "094820", "thesis": "Appeal overhang created drawdown; 4B should remain watch unless order pipeline or regulatory qualification breaks.", "trigger_date": "2024-08-27", "trigger_type": "Stage4B", "trough_180D_date": "2024-12-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 43.6}
{"MAE_180D_pct": -0.06, "MAE_30D_pct": -0.06, "MAE_90D_pct": -0.06, "MFE_180D_pct": 483.97, "MFE_30D_pct": 173.84, "MFE_90D_pct": 206.61, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_07_032820", "close_180D_pct": 411.41, "close_30D_pct": 157.17, "close_90D_pct": 127.62, "company_name": "우리기술", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": false, "current_profile_error": true, "current_profile_error_type": "false_4B_or_hard4C_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|032820|Stage4B|2025-05-07", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2025-05-07", "entry_price": 1709.0, "evidence_family": "Czech_court_signing_block_theme_spike_exception", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "false_4B_positive_exception", "peak_180D_date": "2026-01-21", "positive_case": true, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 55, "capital": 45, "eps": 50, "info": 55, "revision": 35, "valuation": 25, "visibility": 40}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": false, "symbol": "032820", "thesis": "Court block would look like 4B/4C, but retail/proxy route exploded; hard 4C must require direct revenue or legal qualification break.", "trigger_date": "2025-05-07", "trigger_type": "Stage4B", "trough_180D_date": "2025-05-07", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 41.55}
{"MAE_180D_pct": -54.79, "MAE_30D_pct": -41.0, "MAE_90D_pct": -41.95, "MFE_180D_pct": 0.96, "MFE_30D_pct": 0.96, "MFE_90D_pct": 0.96, "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "case_id": "C04_L113_08_011700", "close_180D_pct": -47.8, "close_30D_pct": -34.1, "close_90D_pct": -34.67, "company_name": "한신기계", "corporate_action_check": "tradable_shard_used; profile/corporate_action URL pending for batch repair except spot-checks", "counterexample_case": true, "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "dedupe_key": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY|011700|Stage4B|2024-07-18", "deep_sub_archetype_id": "C04_DEEP_CZECH_DUKOVANY_WESTINGHOUSE_EDF_APPEAL_IP_SETTLEMENT_COURT_BLOCK_VS_NUCLEAR_POLICY_LABEL_SPIKE", "entry_date": "2024-07-18", "entry_price": 5220.0, "evidence_family": "Czech_preferred_bidder_compressor_label_spike", "evidence_url_pending": true, "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3", "forward_window_status": "180_trading_days_available_before_manifest_max_date", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "observed_path_label": "hard_counterexample_label_fade", "peak_180D_date": "2024-07-18", "positive_case": false, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "promotion_blocked_reason": "company_specific_bridge_url_pending; use as residual calibration/proxy row until URL repair", "promotion_usable": false, "raw_component_scores": {"bottleneck": 35, "capital": 45, "eps": 28, "info": 52, "revision": 22, "valuation": 30, "visibility": 32}, "row_type": "trigger", "selected_loop": 113, "selected_round": "R1", "source_proxy_only": true, "stage4b_case": true, "stage4c_case": true, "symbol": "011700", "thesis": "Nuclear compressor label lacked order/revenue bridge and collapsed; local 4B/4C route should be explicit for pure label names.", "trigger_date": "2024-07-18", "trigger_type": "Stage4B", "trough_180D_date": "2025-04-09", "upstream_source": "FinanceData/marcap", "weighted_score_current_profile_proxy": 33.14}
```

## 7. Score simulation JSONL

```jsonl
{"case_id": "C04_L113_01_034020", "current_profile_error": false, "current_profile_error_type": "none", "observed_path_label": "positive_structural_repricing", "raw_component_scores": {"bottleneck": 70, "capital": 62, "eps": 78, "info": 76, "revision": 74, "valuation": 50, "visibility": 82}, "symbol": "034020", "trigger_type": "Stage3-Yellow", "weighted_score_current_profile_proxy": 70.64}
{"case_id": "C04_L113_02_052690", "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "observed_path_label": "positive_high_MAE_bridge", "raw_component_scores": {"bottleneck": 55, "capital": 58, "eps": 58, "info": 75, "revision": 60, "valuation": 42, "visibility": 75}, "symbol": "052690", "trigger_type": "Stage3-Yellow", "weighted_score_current_profile_proxy": 60.56}
{"case_id": "C04_L113_03_051600", "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "observed_path_label": "slow_counterexample", "raw_component_scores": {"bottleneck": 38, "capital": 62, "eps": 52, "info": 68, "revision": 45, "valuation": 55, "visibility": 60}, "symbol": "051600", "trigger_type": "Stage2-Actionable", "weighted_score_current_profile_proxy": 54.45}
{"case_id": "C04_L113_04_105840", "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "observed_path_label": "counterexample_high_MAE_recovery", "raw_component_scores": {"bottleneck": 45, "capital": 52, "eps": 35, "info": 60, "revision": 30, "valuation": 35, "visibility": 42}, "symbol": "105840", "trigger_type": "Stage4B", "weighted_score_current_profile_proxy": 40.99}
{"case_id": "C04_L113_05_083650", "current_profile_error": true, "current_profile_error_type": "false_4B_or_hard4C_risk", "observed_path_label": "positive_after_high_MAE", "raw_component_scores": {"bottleneck": 62, "capital": 48, "eps": 60, "info": 65, "revision": 50, "valuation": 45, "visibility": 57}, "symbol": "083650", "trigger_type": "Stage2-Actionable", "weighted_score_current_profile_proxy": 54.64}
{"case_id": "C04_L113_06_094820", "current_profile_error": false, "current_profile_error_type": "none", "observed_path_label": "counterexample_local_4B", "raw_component_scores": {"bottleneck": 45, "capital": 50, "eps": 42, "info": 58, "revision": 38, "valuation": 38, "visibility": 43}, "symbol": "094820", "trigger_type": "Stage4B", "weighted_score_current_profile_proxy": 43.6}
{"case_id": "C04_L113_07_032820", "current_profile_error": true, "current_profile_error_type": "false_4B_or_hard4C_risk", "observed_path_label": "false_4B_positive_exception", "raw_component_scores": {"bottleneck": 55, "capital": 45, "eps": 50, "info": 55, "revision": 35, "valuation": 25, "visibility": 40}, "symbol": "032820", "trigger_type": "Stage4B", "weighted_score_current_profile_proxy": 41.55}
{"case_id": "C04_L113_08_011700", "current_profile_error": true, "current_profile_error_type": "too_early_or_price_label_risk", "observed_path_label": "hard_counterexample_label_fade", "raw_component_scores": {"bottleneck": 35, "capital": 45, "eps": 28, "info": 52, "revision": 22, "valuation": 30, "visibility": 32}, "symbol": "011700", "trigger_type": "Stage4B", "weighted_score_current_profile_proxy": 33.14}
```

## 8. Aggregate row

```json
{
  "row_type": "aggregate",
  "selected_round": "R1",
  "selected_loop": 113,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "C04_CZECH_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_IP_APPEAL_CONTRACT_SIGNING_BRIDGE_V3",
  "trigger_row_count": 8,
  "calibration_usable_trigger_count": 8,
  "new_independent_case_count": 8,
  "reused_case_count": 0,
  "same_archetype_new_symbol_count": 8,
  "same_archetype_new_trigger_family_count": 8,
  "positive_case_count": 4,
  "counterexample_count": 4,
  "stage4b_case_count": 4,
  "stage4c_case_count": 1,
  "current_profile_error_count": 6,
  "source_proxy_only_count": 8,
  "evidence_url_pending_count": 8,
  "promotion_blocked_until_url_repair": true,
  "avg_MFE_90D_pct": 57.09,
  "avg_MAE_90D_pct": -22.28,
  "avg_MFE_180D_pct": 145.11,
  "avg_MAE_180D_pct": -23.88,
  "do_not_propose_new_weight_delta": false,
  "sector_specific_rule_candidate": true,
  "canonical_archetype_rule_candidate": true,
  "loop_contribution_label": "canonical_archetype_rule_candidate"
}
```

## 9. Shadow rule candidate

```yaml
shadow_rule_candidate:
  scope: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  rule_id: C04_project_legal_delay_requires_issuer_bridge_break_before_hard_4C_v4
  action: candidate_only_no_runtime_patch_now
  positive_condition:
    - legal/IP/regulatory hurdle is resolved or contract signing remains live
    - issuer has direct project, engineering, heavy-equipment, O&M, or supplier revenue bridge
    - MFE90 or MFE180 path confirms survival of project-option value
  guardrail_condition:
    - appeal, court block, or IP dispute exists without issuer-level order/revenue/revision bridge
    - valuation or price spike is caused by generic nuclear label only
    - MAE90 <= -20% before any verified non-price bridge appears
  hard_4C_condition:
    - confirmed contract cancellation, legal disqualification, export-control block, or issuer-level order bridge failure
    - no recovery-band exception within 90/180D path
  local_4B_condition:
    - project signing delayed or legal overhang appears, but bridge is not yet broken
    - keep as local watch rather than full 4B unless non-price evidence confirms thesis damage
```

## 10. Residual contribution summary

```text
new_axis_proposed = C04_legal_project_delay_requires_direct_issuer_bridge_break_before_hard_4C_plus_recovery_band_exception
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, hard_4c_confirmation
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_appeal_or_court_delay_headline_is_present
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
do_not_propose_new_weight_delta = false
promotion_blocked_until_url_repair = true
```

## 11. Deferred Coding Agent Handoff Prompt

```text
Do not execute this handoff in the research session.

When batching V12 research outputs into stock_agent, ingest this file as a C04 quality-repair residual study. Keep production scoring unchanged unless multiple C04 loops confirm the same pattern. Candidate patch axis:

- Add/strengthen C04-specific hard_4c confirmation guard: project/legal delay headlines alone should route to local_4B_watch, not hard_4C, unless issuer-level order/revenue/revision bridge is broken.
- Add C04 recovery-band exception: if legal/IP delay is followed by high MFE90/MFE180 and no confirmed contract cancellation, avoid full 4C.
- Require issuer bridge before Stage3-Yellow/Green for nuclear proxy names: direct EPC, engineering, heavy equipment, O&M, component order, or documented supplier linkage.
- Keep source_proxy_only rows blocked from promotion until company-specific evidence URLs are repaired.

Required parser fields are already present: trigger_type, entry_date, entry_price, MFE/MAE 30/90/180D, large_sector_id, canonical_archetype_id, fine_archetype_id, price_basis, price_adjustment_status, and dedupe_key.
```

## 12. Next research state

```text
completed_round = R1
completed_loop = 113
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG, C16_STRATEGIC_RESOURCE_POLICY_SUPPLY, C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY, C31_POLICY_SUBSIDY_LEGISLATION_EVENT, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
