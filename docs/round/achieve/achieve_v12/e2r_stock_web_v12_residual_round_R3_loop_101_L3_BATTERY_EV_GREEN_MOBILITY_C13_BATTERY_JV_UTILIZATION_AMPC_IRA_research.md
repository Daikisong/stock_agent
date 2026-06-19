# E2R Stock-Web V12 Residual Research — R3 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA / loop 101

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
output_file = e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
selected_round = R3
selected_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2
deep_sub_archetype_id = C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 1. Selection Rationale

Published No-Repeat Index 기준 C13은 58 rows의 Priority 2 구역이다. 같은 세션에서 Priority 0/1 under-50 canonical들을 50-row practical band까지 로컬 보강한 뒤, C13은 `AMPC / IRA / JV / localization` 라벨이 실제 utilization·margin bridge로 바뀌는 경우와 단순 정책 네온사인으로 끝나는 경우를 분리하기 위한 quality repair 대상으로 남았다.

직전 C13 loop100은 direct cellmaker와 대형 소재주 중심이었다. 이번 loop101은 copper foil, silicon anode, CNT/conductive material, electrolyte, equipment, separator 쪽으로 fine route를 넓혀, C13이 정책 단어 하나로 움직이는 종목군이 아니라 `고객 pull → utilization → revenue recognition → margin/FCF`로 이어지는 컨베이어인지 검증한다.

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
atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv
atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv
atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv
atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/078/078600/2025.csv
atlas/ohlcv_tradable_by_symbol_year/348/348370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/348/348370/2025.csv
atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv
atlas/ohlcv_tradable_by_symbol_year/137/137400/2025.csv
atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv
atlas/ohlcv_tradable_by_symbol_year/222/222080/2025.csv
atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv
atlas/ohlcv_tradable_by_symbol_year/393/393890/2025.csv
```

Profile check summary:

```text
020150 corporate_action_candidate_count = 0
121600 candidate_dates = 2015-12-17; selected 2024 window overlap = false
078600 corporate_action_candidate_count = 0
348370 corporate_action_candidate_count = 0
137400 candidate_dates = 2012-11-30, 2012-12-26, 2019-05-07, 2019-05-30; selected 2024 window overlap = false
222080 candidate_dates = 2017-01-20; selected 2024 window overlap = false
393890 corporate_action_candidate_count = 0
```

All rows below have complete 30D/90D/180D MFE/MAE fields and 180-trading-day forward windows available inside the Stock-Web manifest max date.

## 3. Trigger Summary Table

| case_id | symbol | name | trigger_type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | role |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C13_R3_L101_001 | 020150 | 롯데에너지머티리얼즈 | Stage2-Actionable | 2024-02-15 | 35350 | 48.23 | -3.25 | 67.47 | -3.25 | 67.47 | -13.72 | positive |
| C13_R3_L101_002 | 078600 | 대주전자재료 | Stage3-Yellow | 2024-02-15 | 71700 | 43.93 | -3.49 | 127.89 | -3.49 | 127.89 | -3.49 | positive |
| C13_R3_L101_003 | 137400 | 피엔티 | Stage3-Yellow | 2024-05-02 | 40500 | 117.78 | -1.60 | 120.99 | -1.60 | 120.99 | -9.63 | positive |
| C13_R3_L101_004 | 222080 | 씨아이에스 | Stage2-Actionable | 2024-08-05 | 8000 | 52.88 | -2.50 | 52.88 | -11.88 | 52.88 | -18.75 | positive |
| C13_R3_L101_005 | 121600 | 나노신소재 | Stage4B | 2024-06-17 | 125400 | 4.39 | -27.51 | 4.39 | -45.37 | 4.39 | -54.47 | counterexample |
| C13_R3_L101_006 | 348370 | 엔켐 | Stage4C | 2024-06-17 | 276000 | 4.35 | -39.82 | 4.35 | -46.01 | 4.35 | -71.27 | counterexample |
| C13_R3_L101_007 | 393890 | 더블유씨피 | Stage4C | 2024-02-15 | 40700 | 21.62 | -3.44 | 21.62 | -28.01 | 21.62 | -65.16 | counterexample |

## 4. Case Notes

### C13_R3_L101_001 — 020150 / 롯데에너지머티리얼즈 / Stage2-Actionable

copper foil/localization route에서 AMPC·JV 라벨만이 아니라 고객 pull과 utilization rebound가 같이 보이면 Stage2-Actionable이 유효했다. 다만 180D close return은 약해 full Green에는 margin bridge 확인이 필요하다. Stock-Web window result: MFE90 67.47%, MAE90 -3.25%, MFE180 67.47%, MAE180 -13.72%, close_180D_return -9.05%.

### C13_R3_L101_002 — 078600 / 대주전자재료 / Stage3-Yellow

silicon-anode 소재는 직접 AMPC 수혜보다 고객 qualification과 증설/납품 bridge가 핵심이다. 90D MFE가 크게 열리고 180D MAE가 낮아 C13의 positive exception으로 남긴다. Stock-Web window result: MFE90 127.89%, MAE90 -3.49%, MFE180 127.89%, MAE180 -3.49%, close_180D_return 24.97%.

### C13_R3_L101_003 — 137400 / 피엔티 / Stage3-Yellow

JV/cell ramp에서 equipment order가 실제 매출 인식으로 이어질 때 C13은 단순 정책주가 아니라 order-revenue bridge가 있는 Yellow가 된다. Stock-Web window result: MFE90 120.99%, MAE90 -1.60%, MFE180 120.99%, MAE180 -9.63%, close_180D_return -6.54%.

### C13_R3_L101_004 — 222080 / 씨아이에스 / Stage2-Actionable

전극공정 장비는 배터리 capex가 꺾인 뒤에도 고객 acceptance와 수주잔고가 살아 있으면 강한 recovery band가 생긴다. Stage2는 허용하되 Green은 utilization/margin 확인 전까지 보류한다. Stock-Web window result: MFE90 52.88%, MAE90 -11.88%, MFE180 52.88%, MAE180 -18.75%, close_180D_return -6.75%.

### C13_R3_L101_005 — 121600 / 나노신소재 / Stage4B

CNT/소재 localization 라벨은 있어도 고객 pull·margin bridge가 없으면 180D MAE가 크게 열린다. C13에서는 policy/localization label-only를 local 4B watch로 둬야 한다. Stock-Web window result: MFE90 4.39%, MAE90 -45.37%, MFE180 4.39%, MAE180 -54.47%, close_180D_return -44.50%.

### C13_R3_L101_006 — 348370 / 엔켐 / Stage4C

electrolyte 증설/AMPC 라벨이 있어도 실제 demand reset과 valuation blowoff가 겹치면 hard 4C에 가깝다. 이 케이스는 generic policy label이 thesis를 방어하지 못한 반례다. Stock-Web window result: MFE90 4.35%, MAE90 -46.01%, MFE180 4.35%, MAE180 -71.27%, close_180D_return -71.01%.

### C13_R3_L101_007 — 393890 / 더블유씨피 / Stage4C

separator capacity/JV localization narrative가 남아 있어도 utilization과 고객 pull이 무너지면 C13은 Stage2가 아니라 4C 쪽으로 라우팅해야 한다. Stock-Web window result: MFE90 21.62%, MAE90 -28.01%, MFE180 21.62%, MAE180 -65.16%, close_180D_return -65.11%.

## 5. Machine-Readable Trigger Rows JSONL

```jsonl
{"MAE_180D_pct": -13.72, "MAE_30D_pct": -3.25, "MAE_90D_pct": -3.25, "MFE_180D_pct": 67.47, "MFE_30D_pct": 48.23, "MFE_90D_pct": 67.47, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_001", "case_role": "positive", "close_180D_date": "2024-11-12", "close_180D_return_pct": -9.05, "company_name": "롯데에너지머티리얼즈", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 5604364000, "entry_date": "2024-02-15", "entry_high": 36700.0, "entry_low": 35100.0, "entry_open": 35400.0, "entry_price": 35350.0, "entry_request_date": "2024-02-15", "entry_volume": 156915, "evidence_family": "copper_foil_AMPC_localization_utilization_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": false, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|020150|Stage2-Actionable|2024-02-15", "peak_180D_date": "2024-06-18", "peak_180D_price": 59200.0, "peak_30D_date": "2024-03-27", "peak_30D_price": 52400.0, "peak_90D_date": "2024-06-18", "peak_90D_price": 59200.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": [], "corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "policy_or_AMPC_label_needs_verified_utilization_margin_bridge", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 58, "margin_visibility": 54, "red_team_risk": 49, "revision_bridge": 48, "utilization_visibility": 61, "valuation_risk": 55}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "020150", "thesis": "copper foil/localization route에서 AMPC·JV 라벨만이 아니라 고객 pull과 utilization rebound가 같이 보이면 Stage2-Actionable이 유효했다. 다만 180D close return은 약해 full Green에는 margin bridge 확인이 필요하다.", "trigger_family": "copper_foil_AMPC_localization_rebound_margin_bridge", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2024-08-05", "trough_180D_price": 30500.0, "trough_30D_date": "2024-02-20", "trough_30D_price": 34200.0, "trough_90D_date": "2024-02-20", "trough_90D_price": 34200.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -3.49, "MAE_30D_pct": -3.49, "MAE_90D_pct": -3.49, "MFE_180D_pct": 127.89, "MFE_30D_pct": 43.93, "MFE_90D_pct": 127.89, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_002", "case_role": "positive", "close_180D_date": "2024-11-12", "close_180D_return_pct": 24.97, "company_name": "대주전자재료", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 7187828900, "entry_date": "2024-02-15", "entry_high": 71900.0, "entry_low": 70100.0, "entry_open": 71300.0, "entry_price": 71700.0, "entry_request_date": "2024-02-15", "entry_volume": 101050, "evidence_family": "anode_material_customer_qualification_capacity_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": false, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|078600|Stage3-Yellow|2024-02-15", "peak_180D_date": "2024-06-12", "peak_180D_price": 163400.0, "peak_30D_date": "2024-03-26", "peak_30D_price": 103200.0, "peak_90D_date": "2024-06-12", "peak_90D_price": 163400.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": [], "corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "policy_or_AMPC_label_needs_verified_utilization_margin_bridge", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 63, "margin_visibility": 58, "red_team_risk": 32, "revision_bridge": 61, "utilization_visibility": 66, "valuation_risk": 47}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "078600", "thesis": "silicon-anode 소재는 직접 AMPC 수혜보다 고객 qualification과 증설/납품 bridge가 핵심이다. 90D MFE가 크게 열리고 180D MAE가 낮아 C13의 positive exception으로 남긴다.", "trigger_family": "silicon_anode_material_customer_qualification_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-02-20", "trough_180D_price": 69200.0, "trough_30D_date": "2024-02-20", "trough_30D_price": 69200.0, "trough_90D_date": "2024-02-20", "trough_90D_price": 69200.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -9.63, "MAE_30D_pct": -1.6, "MAE_90D_pct": -1.6, "MFE_180D_pct": 120.99, "MFE_30D_pct": 117.78, "MFE_90D_pct": 120.99, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_003", "case_role": "positive", "close_180D_date": "2025-02-03", "close_180D_return_pct": -6.54, "company_name": "피엔티", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 3180147900, "entry_date": "2024-05-02", "entry_high": 40500.0, "entry_low": 39850.0, "entry_open": 39900.0, "entry_price": 40500.0, "entry_request_date": "2024-05-02", "entry_volume": 78979, "evidence_family": "battery_equipment_order_backlog_utilization_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": false, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|137400|Stage3-Yellow|2024-05-02", "peak_180D_date": "2024-06-19", "peak_180D_price": 89500.0, "peak_30D_date": "2024-06-18", "peak_30D_price": 88200.0, "peak_90D_date": "2024-06-19", "peak_90D_price": 89500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2012-11-30", "2012-12-26", "2019-05-07", "2019-05-30"], "corporate_action_candidate_count": 4, "overlap_180D": false}, "profile_residual_label": "policy_or_AMPC_label_needs_verified_utilization_margin_bridge", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 60, "margin_visibility": 56, "red_team_risk": 38, "revision_bridge": 59, "utilization_visibility": 70, "valuation_risk": 52}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "137400", "thesis": "JV/cell ramp에서 equipment order가 실제 매출 인식으로 이어질 때 C13은 단순 정책주가 아니라 order-revenue bridge가 있는 Yellow가 된다.", "trigger_family": "battery_equipment_JV_ramp_order_bridge", "trigger_type": "Stage3-Yellow", "trough_180D_date": "2024-12-30", "trough_180D_price": 36600.0, "trough_30D_date": "2024-05-02", "trough_30D_price": 39850.0, "trough_90D_date": "2024-05-02", "trough_90D_price": 39850.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -18.75, "MAE_30D_pct": -2.5, "MAE_90D_pct": -11.88, "MFE_180D_pct": 52.88, "MFE_30D_pct": 52.88, "MFE_90D_pct": 52.88, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_004", "case_role": "positive", "close_180D_date": "2025-05-08", "close_180D_return_pct": -6.75, "company_name": "씨아이에스", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 8113943820, "entry_date": "2024-08-05", "entry_high": 9190.0, "entry_low": 7800.0, "entry_open": 9100.0, "entry_price": 8000.0, "entry_request_date": "2024-08-05", "entry_volume": 956215, "evidence_family": "electrode_equipment_customer_acceptance_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": false, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|222080|Stage2-Actionable|2024-08-05", "peak_180D_date": "2024-08-20", "peak_180D_price": 12230.0, "peak_30D_date": "2024-08-20", "peak_30D_price": 12230.0, "peak_90D_date": "2024-08-20", "peak_90D_price": 12230.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2017-01-20"], "corporate_action_candidate_count": 1, "overlap_180D": false}, "profile_residual_label": "policy_or_AMPC_label_needs_verified_utilization_margin_bridge", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 55, "margin_visibility": 47, "red_team_risk": 44, "revision_bridge": 46, "utilization_visibility": 58, "valuation_risk": 50}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "222080", "thesis": "전극공정 장비는 배터리 capex가 꺾인 뒤에도 고객 acceptance와 수주잔고가 살아 있으면 강한 recovery band가 생긴다. Stage2는 허용하되 Green은 utilization/margin 확인 전까지 보류한다.", "trigger_family": "electrode_equipment_acceptance_recovery_bridge", "trigger_type": "Stage2-Actionable", "trough_180D_date": "2025-04-09", "trough_180D_price": 6500.0, "trough_30D_date": "2024-08-05", "trough_30D_price": 7800.0, "trough_90D_date": "2024-12-09", "trough_90D_price": 7050.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -54.47, "MAE_30D_pct": -27.51, "MAE_90D_pct": -45.37, "MFE_180D_pct": 4.39, "MFE_30D_pct": 4.39, "MFE_90D_pct": 4.39, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_005", "case_role": "counterexample", "close_180D_date": "2025-03-17", "close_180D_return_pct": -44.5, "company_name": "나노신소재", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 43412430200, "entry_date": "2024-06-17", "entry_high": 130800.0, "entry_low": 123900.0, "entry_open": 126000.0, "entry_price": 125400.0, "entry_request_date": "2024-06-17", "entry_volume": 341070, "evidence_family": "CNT_material_policy_label_no_margin_bridge_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": true, "hard_4c_candidate": false, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": true, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|121600|Stage4B|2024-06-17", "peak_180D_date": "2024-06-18", "peak_180D_price": 130900.0, "peak_30D_date": "2024-06-18", "peak_30D_price": 130900.0, "peak_90D_date": "2024-06-18", "peak_90D_price": 130900.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": ["2015-12-17"], "corporate_action_candidate_count": 1, "overlap_180D": false}, "profile_residual_label": "policy_label_without_utilization_margin_bridge_should_route_to_4B_or_4C", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 43, "margin_visibility": 25, "red_team_risk": 82, "revision_bridge": 28, "utilization_visibility": 30, "valuation_risk": 78}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "121600", "thesis": "CNT/소재 localization 라벨은 있어도 고객 pull·margin bridge가 없으면 180D MAE가 크게 열린다. C13에서는 policy/localization label-only를 local 4B watch로 둬야 한다.", "trigger_family": "CNT_conductive_material_policy_label_fade", "trigger_type": "Stage4B", "trough_180D_date": "2025-01-02", "trough_180D_price": 57100.0, "trough_30D_date": "2024-07-29", "trough_30D_price": 90900.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 68500.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -71.27, "MAE_30D_pct": -39.82, "MAE_90D_pct": -46.01, "MFE_180D_pct": 4.35, "MFE_30D_pct": 4.35, "MFE_90D_pct": 4.35, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_006", "case_role": "counterexample", "close_180D_date": "2025-03-18", "close_180D_return_pct": -71.01, "company_name": "엔켐", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 200994386000, "entry_date": "2024-06-17", "entry_high": 288000.0, "entry_low": 270500.0, "entry_open": 277000.0, "entry_price": 276000.0, "entry_request_date": "2024-06-17", "entry_volume": 725105, "evidence_family": "electrolyte_policy_label_demand_reset_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": true, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|348370|Stage4C|2024-06-17", "peak_180D_date": "2024-06-17", "peak_180D_price": 288000.0, "peak_30D_date": "2024-06-17", "peak_30D_price": 288000.0, "peak_90D_date": "2024-06-17", "peak_90D_price": 288000.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": [], "corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "policy_label_without_utilization_margin_bridge_should_route_to_4B_or_4C", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 42, "margin_visibility": 19, "red_team_risk": 89, "revision_bridge": 22, "utilization_visibility": 24, "valuation_risk": 86}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "348370", "thesis": "electrolyte 증설/AMPC 라벨이 있어도 실제 demand reset과 valuation blowoff가 겹치면 hard 4C에 가깝다. 이 케이스는 generic policy label이 thesis를 방어하지 못한 반례다.", "trigger_family": "electrolyte_AMPC_theme_hard_demand_reset", "trigger_type": "Stage4C", "trough_180D_date": "2025-03-18", "trough_180D_price": 79300.0, "trough_30D_date": "2024-07-29", "trough_30D_price": 166100.0, "trough_90D_date": "2024-08-05", "trough_90D_price": 149000.0, "upstream_source": "FinanceData/marcap"}
{"MAE_180D_pct": -65.16, "MAE_30D_pct": -3.44, "MAE_90D_pct": -28.01, "MFE_180D_pct": 21.62, "MFE_30D_pct": 21.62, "MFE_90D_pct": 21.62, "blocked_reason": "source_proxy_only_until_verified_URL_repair", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "calibration_usable": true, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "case_id": "C13_R3_L101_007", "case_role": "counterexample", "close_180D_date": "2024-11-12", "close_180D_return_pct": -65.11, "company_name": "더블유씨피", "corporate_action_contaminated_180D_window": false, "dedupe_status": "new_symbol_or_new_trigger_family_after_C13_loop100", "deep_sub_archetype_id": "C13_DEEP_BATTERY_MATERIAL_EQUIPMENT_JV_UTILIZATION_AMPC_POLICY_LABEL_VS_ORDER_MARGIN_BRIDGE", "entry_amount": 12049189950, "entry_date": "2024-02-15", "entry_high": 41050.0, "entry_low": 39600.0, "entry_open": 40900.0, "entry_price": 40700.0, "entry_request_date": "2024-02-15", "entry_volume": 298756, "evidence_family": "separator_customer_pull_utilization_break_source_proxy", "evidence_url_pending": true, "fine_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA_UTILIZATION_MARGIN_BRIDGE_VS_POLICY_LABEL_V2", "forward_window_status": "available_180_trading_days", "full_4b_candidate": false, "hard_4c_candidate": true, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "local_4b_candidate": true, "novelty_key": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA|393890|Stage4C|2024-02-15", "peak_180D_date": "2024-03-07", "peak_180D_price": 49500.0, "peak_30D_date": "2024-03-07", "peak_30D_price": 49500.0, "peak_90D_date": "2024-03-07", "peak_90D_price": 49500.0, "price_adjustment_status": "raw_unadjusted_marcap", "price_basis": "tradable_raw", "price_data_source": "Songdaiki/stock-web", "profile_check": {"candidate_dates": [], "corporate_action_candidate_count": 0, "overlap_180D": false}, "profile_residual_label": "policy_label_without_utilization_margin_bridge_should_route_to_4B_or_4C", "promotion_usable": false, "representative_for_aggregate": true, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "row_type": "trigger", "score": {"evidence_quality": 41, "margin_visibility": 21, "red_team_risk": 87, "revision_bridge": 24, "utilization_visibility": 26, "valuation_risk": 80}, "selected_loop": 101, "selected_round": "R3", "source_proxy_only": true, "symbol": "393890", "thesis": "separator capacity/JV localization narrative가 남아 있어도 utilization과 고객 pull이 무너지면 C13은 Stage2가 아니라 4C 쪽으로 라우팅해야 한다.", "trigger_family": "separator_capacity_utilization_break_hard_4C_v2", "trigger_type": "Stage4C", "trough_180D_date": "2024-11-12", "trough_180D_price": 14180.0, "trough_30D_date": "2024-03-29", "trough_30D_price": 39300.0, "trough_90D_date": "2024-06-28", "trough_90D_price": 29300.0, "upstream_source": "FinanceData/marcap"}
```

## 6. Aggregate / Shadow / Residual Rows JSONL

```jsonl
{"avg_MAE_180D_pct": -33.78, "avg_MAE_90D_pct": -19.94, "avg_MFE_180D_pct": 57.08, "avg_MFE_90D_pct": 57.08, "calibration_usable_trigger_count": 7, "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "counterexample_count": 3, "current_profile_error_count": 6, "evidence_url_pending_count": 7, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "new_independent_case_count": 7, "positive_case_count": 4, "promotion_blocked_until_url_repair": true, "representative_trigger_count": 7, "research_file": "e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md", "reused_case_count": 0, "row_type": "aggregate_summary", "same_archetype_new_symbol_count": 7, "same_archetype_new_trigger_family_count": 7, "selected_loop": 101, "selected_round": "R3", "source_proxy_only_count": 7, "stage4b_case_count": 3, "stage4c_case_count": 2, "trigger_row_count": 7}
{"candidate_axis": "C13_verified_utilization_margin_or_customer_pull_bridge_required_before_Yellow_or_Green_v2", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "do_not_propose_new_weight_delta": false, "global_threshold_change": false, "row_type": "shadow_weight_candidate", "scope": "canonical_archetype_specific_only", "stage3_green_threshold_change": false, "suggested_rule": "Require utilization/customer pull/order-to-revenue/margin bridge before Stage3-Yellow or Green in C13; keep policy/AMPC/JV label-only moves at local 4B watch; route confirmed demand/utilization collapse with MAE > 50% to hard 4C only when non-price evidence supports it."}
{"existing_axis_strengthened": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_confirmation", "full_4b_requires_non_price_evidence"], "existing_axis_weakened": "hard_4c_thesis_break_routes_to_4c_when_only_generic_AMPC_IRA_or_JV_label_is_present", "new_axis_proposed": "C13_verified_utilization_margin_or_customer_pull_bridge_required_before_Yellow_or_Green_plus_policy_label_to_local_4B_or_4C_watch_v2", "row_type": "residual_contribution", "why_not_global_patch": "C13 has both strong positive MFE when order/utilization bridge exists and severe MAE when the same policy/JV/AMPC label lacks margin conversion; the patch must stay canonical-specific."}
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
positive_case_count = 4
counterexample_count = 3
stage4b_case_count = 3
stage4c_case_count = 2
current_profile_error_count = 6
source_proxy_only_count = 7
evidence_url_pending_count = 7
promotion_blocked_until_url_repair = true
```

Residual conclusion:

```text
new_axis_proposed = C13_verified_utilization_margin_or_customer_pull_bridge_required_before_Yellow_or_Green_plus_policy_label_to_local_4B_or_4C_watch_v2
existing_axis_strengthened = stage2_required_bridge, local_4b_watch_guard, hard_4c_confirmation, full_4b_requires_non_price_evidence
existing_axis_weakened = hard_4c_thesis_break_routes_to_4c_when_only_generic_AMPC_IRA_or_JV_label_is_present
```

Score-return alignment:

```text
positive rows = 4; avg MFE180 = 92.31; avg MAE180 = -11.4
counterexample rows = 3; avg MFE180 = 10.12; avg MAE180 = -63.63
```

C13 should not be globally loosened. It needs a bridge test. The row set says: `AMPC/JV/localization label + actual utilization/order/margin bridge = Stage2/Yellow allowed`; `AMPC/JV/localization label only = local 4B watch`; `confirmed utilization/customer-pull/demand break with severe MAE = hard 4C only after non-price confirmation`.

## 8. Deferred Coding Agent Handoff Prompt

```text
You are a later batch implementation coding agent. Do not use this MD as live trading advice. Ingest this file only as one V12 historical calibration artifact.

Target file:
e2r_stock_web_v12_residual_round_R3_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Apply nothing directly to production. Parse machine-readable trigger rows and aggregate/shadow/residual rows. If URL repair later verifies non-price evidence, consider a canonical-scope patch candidate for C13_BATTERY_JV_UTILIZATION_AMPC_IRA:

- require verified utilization/customer-pull/order-to-revenue/margin or AMPC-recognition bridge before Stage3-Yellow/Green;
- route generic AMPC/IRA/JV/localization label-only rows to local 4B watch;
- route confirmed utilization/customer-pull/demand collapse to hard 4C only when non-price evidence confirms the thesis break;
- do not change global Stage3-Green threshold;
- do not change production scoring unless batch validation across other C13 rows supports it.
```

## 9. Next Research State

```text
completed_round = R3
completed_loop = 101
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 2 quality_repair_after_local_priority0_priority1_fill
next_recommended_archetypes = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY, C19_BRAND_RETAIL_INVENTORY_MARGIN, C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT, C22_INSURANCE_RATE_CYCLE_RESERVE, C24_BIO_TRIAL_DATA_EVENT_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```
