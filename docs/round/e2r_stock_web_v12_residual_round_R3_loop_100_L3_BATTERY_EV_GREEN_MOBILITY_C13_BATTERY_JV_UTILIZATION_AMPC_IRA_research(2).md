# E2R Stock-Web V12 Residual Research — R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / loop 100

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
```

## 0. File / Scheduler Metadata

```text
output_file = e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round = R3
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL
deep_sub_archetype_id = C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Selection Rationale

Published No-Repeat Index 기준 C13은 58 rows의 Priority 2 구역이다. 이 세션에서는 C02/C09/C14/C10/C06/C07/C11/C01/C28/C12/C05/C23/C27/C08/C19 등 under-covered 또는 exact-50 축을 이미 로컬 보강했다. 따라서 이번 loop는 새 coverage를 억지로 늘리는 작업이 아니라, C13의 `AMPC/JV/utilization` 라벨이 실제로 Stage2/Yellow로 올라갈 수 있는 경우와 local 4B/4C로 꺾여야 하는 경우를 분리하는 quality repair다.

C13은 정책·보조금·JV 이름표가 너무 선명해서, 가격은 먼저 움직이고 실적 bridge는 늦게 따라오는 구간이 많다. 배터리 공장은 굴러가는 컨베이어처럼 보이지만, 실제 병목은 `고객 pull → utilization → AMPC 인식 → margin/FCF` 순서로 걸린다. 이 중 하나가 빠지면 라벨은 엔진이 아니라 네온사인에 가깝다.

## 2. Price Atlas Validation Scope

```text
primary_price_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_usage = not_used_for_calibration
```

Downloaded / checked tradable shards:

```text
atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
atlas/ohlcv_tradable_by_symbol_year/373/373220/2025.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2025.csv
atlas/ohlcv_tradable_by_symbol_year/096/096770/2024.csv
atlas/ohlcv_tradable_by_symbol_year/096/096770/2025.csv
atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv
atlas/ohlcv_tradable_by_symbol_year/003/003670/2025.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2025.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv
atlas/ohlcv_tradable_by_symbol_year/066/066970/2025.csv
atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv
atlas/ohlcv_tradable_by_symbol_year/361/361610/2025.csv
```

Corporate action/profile notes were checked from symbol profiles where accessible. The selected SK이노베이션 trigger uses 2024-01-02, whose 180-trading-day window ends before the 2024-11-20 corporate-action candidate noted in the profile, so it is retained as calibration usable for this specific window. All rows below have complete 30D/90D/180D MFE/MAE fields.

## 3. Trigger Summary Table

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C13_R3_L100_001 | 373220 | LG에너지솔루션 | Stage2-Actionable | 2024-06-17 | 336500 | 11.44 | -6.98 | 31.95 | -7.58 | 31.95 | -7.58 | positive |
| C13_R3_L100_002 | 006400 | 삼성SDI | Stage3-Yellow | 2024-02-15 | 386000 | 28.11 | -5.96 | 28.11 | -9.07 | 28.11 | -31.74 | positive_then_late_4B |
| C13_R3_L100_003 | 096770 | SK이노베이션 | Stage4B | 2024-01-02 | 140200 | 0.07 | -23.32 | 0.07 | -26.82 | 0.07 | -34.59 | counterexample |
| C13_R3_L100_004 | 003670 | 포스코퓨처엠 | Stage4B | 2024-08-16 | 210500 | 25.42 | -4.99 | 25.42 | -35.25 | 25.42 | -49.12 | counterexample |
| C13_R3_L100_005 | 247540 | 에코프로비엠 | Stage4B | 2024-02-15 | 253000 | 17.98 | -7.11 | 17.98 | -30.75 | 17.98 | -41.23 | counterexample |
| C13_R3_L100_006 | 066970 | 엘앤에프 | Stage3-Yellow | 2024-02-15 | 147600 | 34.82 | -2.03 | 34.82 | -9.15 | 34.82 | -43.83 | positive_then_4B |
| C13_R3_L100_007 | 361610 | SK아이이테크놀로지 | Stage4C | 2024-02-15 | 68700 | 13.10 | -1.46 | 13.10 | -37.85 | 13.10 | -59.10 | counterexample |

## 4. Case Notes

### 4.1 C13_R3_L100_001 — 373220 / LG에너지솔루션 / Stage2-Actionable

This is the cleanest positive in this loop. Entry at 2024-06-17 produced MFE90 and MFE180 of 31.95% while MAE90/180 stayed at -7.58%. For C13, this is the pattern where AMPC/JV utilization should be allowed to become Stage2-Actionable if margin and utilization bridge are visible. It is still not a Green unlock without verified non-price URL repair.

### 4.2 C13_R3_L100_002 — 006400 / 삼성SDI / Stage3-Yellow

This row is useful because the 30D/90D route looked good: MFE90 was 28.11% with MAE90 at -9.07%. But by 180D, MAE expanded to -31.74% and close_180D_return was -31.48%. The rule implication is not “block all C13 Yellow,” but “C13 Yellow requires a post-peak utilization/margin fade watch.”

### 4.3 C13_R3_L100_003 — 096770 / SK이노베이션 / Stage4B

The entry produced almost no upside: MFE180 was only 0.07%, while MAE180 was -34.59%. This is the policy/JV label trap. If the JV/battery story arrives with balance-sheet drag and no utilization-margin bridge, current profile should keep it at local 4B watch, not Stage2.

### 4.4 C13_R3_L100_004 — 003670 / 포스코퓨처엠 / Stage4B

The stock gave a strong 30D rebound, MFE30 25.42%, but MAE180 reached -49.12%. This is a classic short-MFE rebound versus demand-reset case. C13 should distinguish “material localization bounce” from true order/utilization/margin conversion.

### 4.5 C13_R3_L100_005 — 247540 / 에코프로비엠 / Stage4B

MFE30/90/180 was capped at 17.98%, while MAE90/180 deteriorated to -30.75% and -41.23%. This supports a guard that policy or IRA premium must not unlock Yellow without delivery, spread, and margin bridge.

### 4.6 C13_R3_L100_006 — 066970 / 엘앤에프 / Stage3-Yellow then 4B

This is a fast positive that later faded. MFE30/90/180 reached 34.82%, but MAE180 later reached -43.83%. The row argues for a two-step rule: C13 can allow Yellow for early localization/contract strength, but full Green should require margin and FCF proof, and local 4B must activate after post-peak deterioration.

### 4.7 C13_R3_L100_007 — 361610 / SK아이이테크놀로지 / Stage4C

This is the hard 4C anchor. MFE180 was only 13.10%, while MAE180 reached -59.10%. For separator/JV capacity routes, confirmed utilization and customer-pull break should route to hard 4C, not just local 4B.

## 5. Machine-Readable Trigger Rows JSONL

```jsonl
{"MAE_180D_pct": -7.58, "MAE_30D_pct": -6.98, "MAE_90D_pct": -7.58, "MFE_180D_pct": 31.95, "MFE_30D_pct": 11.44, "MFE_90D_pct": 31.95, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_001", "case_role": "positive", "close_180D_date": "2025-03-17", "close_180D_return_pct": -3.42, "company_name": "LG에너지솔루션", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 92696426500, "entry_date": "2024-06-17", "entry_high": 346000.0, "entry_low": 336500.0, "entry_open": 345000.0, "entry_price": 336500.0, "entry_request_date": "2024-06-17", "entry_volume": 273382, "evidence_family": "AMPC_JV_utilization_margin_bridge_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|373220|Stage2-Actionable|2024-06-17", "peak_180D_date": "2024-10-08", "peak_180D_price": 444000.0, "peak_30D_date": "2024-07-11", "peak_30D_price": 375000.0, "peak_90D_date": "2024-10-08", "peak_90D_price": 444000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "current_profile_too_conservative_if_AMPC_utilization_and_margin_bridge_are_visible", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 72, "margin_visibility": 61, "red_team_risk": 36, "revision_bridge": 58, "utilization_visibility": 67, "valuation_risk": 41}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "373220", "thesis": "AMPC와 북미 JV utilization이 단순 정책 headline이 아니라 마진 방어와 생산량 회복 bridge로 읽힐 때 Stage2-Actionable은 유효했다.", "trigger_family": "direct_cellmaker_AMPC_utilization_recovery_bridge", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-08-05", "trough_180D_price": 311000.0, "trough_30D_date": "2024-07-25", "trough_30D_price": 313000.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 311000.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -31.74, "MAE_30D_pct": -5.96, "MAE_90D_pct": -9.07, "MFE_180D_pct": 28.11, "MFE_30D_pct": 28.11, "MFE_90D_pct": 28.11, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_002", "case_role": "positive_then_late_4B", "close_180D_date": "2024-11-12", "close_180D_return_pct": -31.48, "company_name": "삼성SDI", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 100364086500, "entry_date": "2024-02-15", "entry_high": 393000.0, "entry_low": 385500.0, "entry_open": 393000.0, "entry_price": 386000.0, "entry_request_date": "2024-02-15", "entry_volume": 258465, "evidence_family": "JV_capacity_AMPC_operating_leverage_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|006400|Stage3-Yellow|2024-02-15", "peak_180D_date": "2024-03-25", "peak_180D_price": 494500.0, "peak_30D_date": "2024-03-25", "peak_30D_price": 494500.0, "peak_90D_date": "2024-03-25", "peak_90D_price": 494500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["1996-01-03", "1998-11-03", "2014-07-15"], "corporate_action_candidate_count": 3, "overlap_180D": false}, "profile_residual_label": "Yellow_can_be_right_for_90D_but_needs_180D_fade_guard", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 69, "margin_visibility": 56, "red_team_risk": 49, "revision_bridge": 54, "utilization_visibility": 60, "valuation_risk": 55}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "006400", "thesis": "JV/AMPC 기대가 30~90D에는 강한 MFE를 만들었지만 180D에서는 EV 수요와 mix 둔화가 다시 덮었다. C13은 Yellow 이후 4B fade-watch가 필요하다.", "trigger_family": "premium_cell_JV_AMPC_operating_leverage_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-11-12", "trough_180D_price": 263500.0, "trough_30D_date": "2024-03-06", "trough_30D_price": 363000.0, "trough_90D_date": "2024-06-28", "trough_90D_price": 351000.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -34.59, "MAE_30D_pct": -23.32, "MAE_90D_pct": -26.82, "MFE_180D_pct": 0.07, "MFE_30D_pct": 0.07, "MFE_90D_pct": 0.07, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_003", "case_role": "counterexample", "close_180D_date": "2024-09-26", "close_180D_return_pct": -13.98, "company_name": "SK이노베이션", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 39948512500, "entry_date": "2024-01-02", "entry_high": 140300.0, "entry_low": 138100.0, "entry_open": 139800.0, "entry_price": 140200.0, "entry_request_date": "2024-01-02", "entry_volume": 286766, "evidence_family": "JV_loss_cash_burn_utilization_drag_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|096770|Stage4B|2024-01-02", "peak_180D_date": "2024-01-02", "peak_180D_price": 140300.0, "peak_30D_date": "2024-01-02", "peak_30D_price": 140300.0, "peak_90D_date": "2024-01-02", "peak_90D_price": 140300.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2024-11-20"], "corporate_action_candidate_count": 1, "note": "chosen 2024-01-02 window ends before 2024-11-20 candidate", "overlap_180D": false}, "profile_residual_label": "policy_or_JV_label_without_utilization_margin_bridge_should_not_unlock_Yellow", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 58, "margin_visibility": 31, "red_team_risk": 72, "revision_bridge": 35, "utilization_visibility": 42, "valuation_risk": 65}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "096770", "thesis": "JV/IRA/AMPC 이름표가 있어도 배터리 손실, utilization, 재무 부담이 bridge를 압도하면 Stage2가 아니라 local 4B watch가 먼저다.", "trigger_family": "battery_JV_balance_sheet_utilization_drag", "trigger_type": "Stage4B", "trough_180D_date": "2024-08-05", "trough_180D_price": 91700.0, "trough_30D_date": "2024-01-23", "trough_30D_price": 107500.0, "trough_90D_date": "2024-04-16", "trough_90D_price": 102600.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -49.12, "MAE_30D_pct": -4.99, "MAE_90D_pct": -35.25, "MFE_180D_pct": 25.42, "MFE_30D_pct": 25.42, "MFE_90D_pct": 25.42, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_004", "case_role": "counterexample", "close_180D_date": "2025-05-20", "close_180D_return_pct": -48.84, "company_name": "포스코퓨처엠", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 44988515000, "entry_date": "2024-08-16", "entry_high": 217500.0, "entry_low": 210000.0, "entry_open": 216000.0, "entry_price": 210500.0, "entry_request_date": "2024-08-16", "entry_volume": 211271, "evidence_family": "cathode_material_localization_demand_reset_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|003670|Stage4B|2024-08-16", "peak_180D_date": "2024-09-30", "peak_180D_price": 264000.0, "peak_30D_date": "2024-09-30", "peak_30D_price": 264000.0, "peak_90D_date": "2024-09-30", "peak_90D_price": 264000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"corporate_action_candidate_count": "profile_view_truncated", "overlap_180D": false}, "profile_residual_label": "short_MFE_rebound_must_not_override_180D_demand_reset_MAE", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 62, "margin_visibility": 33, "red_team_risk": 76, "revision_bridge": 38, "utilization_visibility": 39, "valuation_risk": 70}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "003670", "thesis": "IRA/localization narrative가 30D rebound를 만들 수 있지만, 고객 pull과 utilization이 회복되지 않으면 90~180D MAE가 thesis를 다시 훼손한다.", "trigger_family": "IRA_material_localization_bounce_vs_demand_reset", "trigger_type": "Stage4B", "trough_180D_date": "2025-05-20", "trough_180D_price": 107100.0, "trough_30D_date": "2024-08-19", "trough_30D_price": 200000.0, "trough_90D_date": "2025-01-02", "trough_90D_price": 136300.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -41.23, "MAE_30D_pct": -7.11, "MAE_90D_pct": -30.75, "MFE_180D_pct": 17.98, "MFE_30D_pct": 17.98, "MFE_90D_pct": 17.98, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_005", "case_role": "counterexample", "close_180D_date": "2024-11-12", "close_180D_return_pct": -39.57, "company_name": "에코프로비엠", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 236907889000, "entry_date": "2024-02-15", "entry_high": 256500.0, "entry_low": 241500.0, "entry_open": 249500.0, "entry_price": 253000.0, "entry_request_date": "2024-02-15", "entry_volume": 951210, "evidence_family": "cathode_policy_premium_margin_gap_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|247540|Stage4B|2024-02-15", "peak_180D_date": "2024-03-27", "peak_180D_price": 298500.0, "peak_30D_date": "2024-03-27", "peak_30D_price": 298500.0, "peak_90D_date": "2024-03-27", "peak_90D_price": 298500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2022-06-27", "2022-07-15"], "corporate_action_candidate_count": 2, "overlap_180D": false}, "profile_residual_label": "policy_premium_needs_delivery_margin_bridge_before_Yellow", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 61, "margin_visibility": 32, "red_team_risk": 78, "revision_bridge": 37, "utilization_visibility": 41, "valuation_risk": 74}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "247540", "thesis": "IRA 수혜 기대가 있어도 고객 물량과 양극재 spread/마진 bridge가 확인되지 않으면 초기 MFE보다 90~180D MAE가 더 중요한 반례다.", "trigger_family": "IRA_cathode_policy_premium_without_order_margin_bridge", "trigger_type": "Stage4B", "trough_180D_date": "2024-09-10", "trough_180D_price": 148700.0, "trough_30D_date": "2024-02-20", "trough_30D_price": 235000.0, "trough_90D_date": "2024-06-28", "trough_90D_price": 175200.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -43.83, "MAE_30D_pct": -2.03, "MAE_90D_pct": -9.15, "MFE_180D_pct": 34.82, "MFE_30D_pct": 34.82, "MFE_90D_pct": 34.82, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_006", "case_role": "positive_then_4B", "close_180D_date": "2024-11-12", "close_180D_return_pct": -19.92, "company_name": "엘앤에프", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 41060625500, "entry_date": "2024-02-15", "entry_high": 149300.0, "entry_low": 144600.0, "entry_open": 147500.0, "entry_price": 147600.0, "entry_request_date": "2024-02-15", "entry_volume": 279133, "evidence_family": "localization_contract_margin_fade_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|066970|Stage3-Yellow|2024-02-15", "peak_180D_date": "2024-03-25", "peak_180D_price": 199000.0, "peak_30D_date": "2024-03-25", "peak_30D_price": 199000.0, "peak_90D_date": "2024-03-25", "peak_90D_price": 199000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2016-02-19", "2021-08-11"], "corporate_action_candidate_count": 2, "overlap_180D": false}, "profile_residual_label": "C13_can_have_fast_MFE_but_needs_post_peak_margin_fade_watch", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 66, "margin_visibility": 44, "red_team_risk": 64, "revision_bridge": 49, "utilization_visibility": 51, "valuation_risk": 67}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "066970", "thesis": "localization/JV supply-chain 기대는 30~90D에는 강하게 먹혔지만 180D MAE가 크게 열렸다. Stage3-Yellow는 가능하지만 full Green은 margin bridge 없이는 막아야 한다.", "trigger_family": "US_supply_chain_localization_rebound_then_margin_fade", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-09-10", "trough_180D_price": 82900.0, "trough_30D_date": "2024-02-15", "trough_30D_price": 144600.0, "trough_90D_date": "2024-06-28", "trough_90D_price": 134100.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -59.1, "MAE_30D_pct": -1.46, "MAE_90D_pct": -37.85, "MFE_180D_pct": 13.1, "MFE_30D_pct": 13.1, "MFE_90D_pct": 13.1, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L100_007", "case_role": "counterexample", "close_180D_date": "2024-11-12", "close_180D_return_pct": -58.88, "company_name": "SK아이이테크놀로지", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_in_C13_session", "deep_sub_archetype_id": "C13_DEEP_NORTH_AMERICA_AMPC_JV_UTILIZATION_AND_MATERIAL_LOCALIZATION_VS_DEMAND_RESET", "entry_amount": 11902419600, "entry_date": "2024-02-15", "entry_high": 68900.0, "entry_low": 67700.0, "entry_open": 68400.0, "entry_price": 68700.0, "entry_request_date": "2024-02-15", "entry_volume": 173985, "evidence_family": "separator_utilization_customer_pull_break_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_MARGIN_BRIDGE_VS_POLICY_LABEL", "forward_window_status": "available_180_trading_days", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|361610|Stage4C|2024-02-15", "peak_180D_date": "2024-03-26", "peak_180D_price": 77700.0, "peak_30D_date": "2024-03-26", "peak_30D_price": 77700.0, "peak_90D_date": "2024-03-26", "peak_90D_price": 77700.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "confirmed_utilization_break_should_route_to_hard_4C_not_Stage2", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 57, "margin_visibility": 24, "red_team_risk": 84, "revision_bridge": 28, "utilization_visibility": 30, "valuation_risk": 78}, "selected_loop": 100, "selected_round": "R3", "source_proxy_only": true, "symbol": "361610", "thesis": "분리막 capacity/JV supply-chain label이 있어도 utilization과 고객 pull이 무너지면 C13은 Stage4C로 내려야 한다. 이 케이스는 C13 hard-4C timing 보강용이다.", "trigger_family": "separator_capacity_utilization_break_hard_4C", "trigger_type": "Stage4C", "trough_180D_date": "2024-11-12", "trough_180D_price": 28100.0, "trough_30D_date": "2024-02-15", "trough_30D_price": 67700.0, "trough_90D_date": "2024-06-04", "trough_90D_price": 42700.0, "upstream_source": "FinanceData/marcap"}
```

## 6. Aggregate / Shadow / Residual Rows JSONL

```jsonl
{"avg_MAE_180D_pct": -38.17, "avg_MAE_90D_pct": -22.35, "avg_MFE_180D_pct": 21.64, "avg_MFE_90D_pct": 21.64, "calibration_usable_trigger_count": 7, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "counterexample_count": 4, "current_profile_error_count": 6, "evidence_url_pending_count": 7, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "new_independent_case_count": 7, "positive_case_count": 3, "promotion_blocked_until_url_repair": true, "representative_trigger_count": 7, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "reused_case_count": 0, "row_type": "aggregate_summary", "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 7, "selected_loop": 100, "selected_round": "R3", "source_proxy_only_count": 7, "stage4b_case_count": 5, "stage4c_case_count": 1, "trigger_row_count": 7}
{"candidate_axis": "C13_AMPC_JV_utilization_margin_bridge_required_before_Yellow_or_Green", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "do_not_propose_new_weight_delta": false, "global_threshold_change": false, "row_type": "shadow_weight_candidate", "scope": "canonical_archetype_specific_only", "stage3_green_threshold_change": false, "suggested_rule": "Require verified utilization/customer pull/margin or AMPC-recognition bridge before Stage3-Yellow/Green; route policy-only or JV-label-only rebound to local 4B watch; route confirmed separator/cell utilization break to hard 4C only when demand-reset evidence is non-price confirmed."}
{"existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_when_only_generic_IRA_or_AMPC_label_is_present", "new_axis_proposed": "C13_AMPC_JV_utilization_margin_bridge_required_before_Yellow_or_Green_plus_policy_label_to_local_4B_watch", "row_type": "residual_contribution", "why_not_global_patch": "C13 cases show the policy/JV/AMPC label is neither always bullish nor always bearish; it needs utilization and margin bridge by battery sub-route."}
```

## 7. Current Calibrated Profile Stress Test

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

Stress result:

```text
trigger_row_count = 7
calibration_usable_trigger_count = 7
representative_trigger_count = 7
new_independent_case_count = 7
reused_case_count = 0
same_archetype_new_symbol_count = 7
same_archetype_new_trigger_family_count = 7
positive_case_count = 3
counterexample_count = 4
stage4b_case_count = 5
stage4c_case_count = 1
current_profile_error_count = 6
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
```

Residual conclusion:

```text
new_axis_proposed = C13_AMPC_JV_utilization_margin_bridge_required_before_Yellow_or_Green_plus_policy_label_to_local_4B_watch
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation, full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_IRA_or_AMPC_label_is_present
```

C13 should not be globally loosened. It needs a bridge test. The row set says: `AMPC/JV label + actual utilization/margin bridge = Stage2/Yellow allowed`; `AMPC/JV label only = local 4B watch`; `confirmed utilization/customer-pull break = hard 4C`.

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation coding agent. Do not use this MD as live trading advice. Ingest this file only as one V12 historical calibration artifact.

Target file:
e2r_stock_web_v12_residual_round_R3_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Apply nothing directly to production. Parse machine-readable trigger rows and aggregate/shadow/residual rows. If URL repair later verifies non-price evidence, consider a canonical-scope patch candidate for C13_BATTERY_JV_UTILIZATION_AMPC_IRA:

- require verified utilization/customer-pull/margin or AMPC-recognition bridge before Stage3-Yellow/Green;
- route generic AMPC/IRA/JV label-only rows to local 4B watch;
- route separator/cell utilization/customer-pull break to hard 4C only when non-price evidence confirms the thesis break;
- do not change global Stage3-Green threshold;
- do not change production scoring unless batch validation across other C13 rows supports it.
```

## 9. Next Research State

```text
completed_round = R3
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
