# E2R Stock-Web V12 Residual Research — R2 loop 117 / C09 Advanced Equipment Valuation Blowoff

```yaml
completed_round: R2
completed_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger: C09 rows=10 / need_to_30=20 / need_to_50=40
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
  - holdout_validation
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_code_patch_included: false
production_scoring_patch_applied: false
handoff_prompt_executed_now: false
```

## 1. Selection rationale

`V12_Research_No_Repeat_Index.md` still shows C09 as a Priority 0 under-covered canonical with 10 rows, 20 rows short of the 30-row minimum stability band and 40 rows short of the 50-row practical calibration band. This loop therefore selects `C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF` and derives `R2 / L2_AI_SEMICONDUCTOR_ELECTRONICS` from the canonical mapping.

This pass intentionally avoids the C09 symbols already used in this session such as `322310`, `348210`, `240810`, `319660`, `101490`, `036930`, `140860`, `064290`, `036810`, `098460`, `039030`, `217190`, `396470`, `403870`, and `122640`. The new set focuses on glass-substrate/TGV equipment, wafer-transfer robotics, HBM burn-in tester qualification risk, semiconductor back-end laser packaging, FOUP cleaning, and tool-automation boundary cases.

## 2. Stock-Web atlas verification

```yaml
manifest_checked: true
schema_checked: true
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
profile_checked_for_each_symbol: true
corporate_action_contaminated_rows: 0
insufficient_forward_window_rows: 0
```

Stock-Web is used only as the price atlas. Entry rows and forward windows are derived from actual tradable OHLC rows. No current/live scan or production scoring patch is included.

## 3. Trigger-level result table

|symbol|name|trigger_type|entry_date|entry_price|MFE_30D_pct|MAE_30D_pct|MFE_90D_pct|MAE_90D_pct|MFE_180D_pct|MAE_180D_pct|classification|
|---|---|---|---|---|---|---|---|---|---|---|---|
|161580|필옵틱스|Stage3-Yellow|2025-05-27|35900.0|24.9304|-5.7103|24.9304|-20.3343|67.9666|-20.3343|positive_with_local_4B_watch|
|232680|라온테크|Stage3-Yellow|2024-12-19|6460.0|55.418|-5.2632|82.0433|-5.2632|82.0433|-5.2632|positive_with_local_4B_watch|
|086390|유니테스트|Stage4B-LocalWatch|2025-04-03|10480.0|13.4542|-18.2252|33.7786|-18.2252|112.7863|-18.2252|positive_after_bridge_but_entry_requires_4B|
|089890|코세스|Stage4B-LocalWatch|2024-03-13|15740.0|20.3939|-13.4689|26.5565|-18.4244|26.5565|-61.9441|counterexample_high_MAE|
|187870|디바이스이엔지|Stage2-Actionable|2024-02-19|15120.0|5.8201|-4.1667|16.2037|-4.1667|16.2037|-25.5952|counterexample_low_MFE_delayed_margin_bridge|
|160980|싸이맥스|Stage4B-LocalWatch|2024-06-17|20950.0|6.4439|-27.1122|6.4439|-51.2172|6.4439|-64.6301|counterexample_hype_without_timing_bridge|

## 4. Interpretation

The C09 residual error is not that advanced equipment optionality is useless. It is that the market often prices an entire future equipment lane before the named order, delivery timing, revenue recognition, and margin bridge are visible. 필옵틱스 and 라온테크 show that real equipment capability can produce strong MFE. But both still need a local 4B watch after vertical rerating because peak-to-trough drawdown remains large. 유니테스트 shows a delayed-positive structure: once qualification/supply bridge becomes real, MFE opens, but the entry date still carried supply-failure and inventory/cash-flow warnings. 코세스, 디바이스이엔지, and 싸이맥스 show the opposite side of the same mechanism: business exposure is real, but without a fresh named-order or revenue/margin bridge, C09 becomes a high-MAE Stage2/4B trap.

## 5. Aggregate metrics

```yaml
{
  "jsonl_trigger_row_count": 6,
  "calibration_usable_rows": 6,
  "representative_rows": 6,
  "positive_case_count": 3,
  "counterexample_count": 3,
  "local_4B_watch_count": 5,
  "current_profile_error_count": 6,
  "avg_MFE_30D_pct": 21.0768,
  "avg_MAE_30D_pct": -12.3244,
  "avg_MFE_90D_pct": 31.6594,
  "avg_MAE_90D_pct": -19.6052,
  "avg_MFE_180D_pct": 52.0,
  "avg_MAE_180D_pct": -32.6653,
  "source_proxy_only_rows": 0,
  "evidence_url_pending_rows": 0
}
```

## 6. Current calibrated profile stress test

```yaml
current_profile_proxy: e2r_2_2_rolling_calibrated
stage2_required_bridge: strengthened
local_4b_watch_guard: strengthened
price_only_blowoff_blocks_positive_stage: strengthened
full_4b_requires_non_price_evidence: strengthened
hard_4c_thesis_break_routes_to_4c: unchanged
residual_error_found: true
```

C09 should not be weakened into a pure momentum or theme detector. The better shadow axis is a bridge gate: advanced equipment exposure can support Stage2, but Stage3-Yellow requires named customer/order evidence plus at least one conversion bridge: delivery schedule, revenue-recognition path, capacity allocation, margin visibility, or repeat purchase order. A high MFE row may remain positive, but if MAE90/MAE180 expands before the bridge appears, the row should be tagged as `Stage4B-LocalWatch` rather than promoted to Green.

## 7. Proposed shadow rule candidate

```text
C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_OPTIONALITY_4B_CAP_V117
```

### Rule sketch

```yaml
if canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:
  stage2_allowed_when:
    - advanced_equipment_exposure_confirmed
    - customer_or_application_quality_visible
  stage3_yellow_allowed_when:
    - named_customer_or_named_order_confirmed
    - delivery_timing_or_revenue_recognition_bridge_confirmed
    - margin_or_repeat_order_bridge_visible
  stage3_green_blocked_when:
    - only_theme_or_optionality
    - only_price_relative_strength
    - no_non_price_order_revenue_bridge
  local_4b_watch_when:
    - MFE_30D_or_90D_opens_but_MAE_90D_or_180D_deepens
    - peak_drawdown_after_optional_blowoff_exceeds_35pct
```

## 8. Machine-readable trigger rows JSONL

```jsonl
{"symbol": "161580", "name": "필옵틱스", "trigger_date": "2025-05-27", "evidence_family": "glass_substrate_TGV_equipment_shipments_customer_diversification", "trigger_type": "Stage3-Yellow", "classification": "positive_with_local_4B_watch", "source_url": "https://marketin.edaily.co.kr/News/ReadE?newsId=01804006642173184", "thesis": "유리기판/TGV 장비 출하와 고객사 다변화가 확인됐지만 자회사·디스플레이 mix와 peak 이후 drawdown 때문에 Green 직행은 cap", "entry_date": "2025-05-27", "entry_price": 35900.0, "MFE_30D_pct": 24.9304, "MAE_30D_pct": -5.7103, "MFE_90D_pct": 24.9304, "MAE_90D_pct": -20.3343, "MFE_180D_pct": 67.9666, "MAE_180D_pct": -20.3343, "peak_date": "2026-01-30", "peak_price": 60300.0, "drawdown_after_peak_pct": -22.2222, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
{"symbol": "232680", "name": "라온테크", "trigger_date": "2024-12-19", "evidence_family": "wafer_transfer_robot_market_growth_customer_quality", "trigger_type": "Stage3-Yellow", "classification": "positive_with_local_4B_watch", "source_url": "https://file.alphasquare.co.kr/media/pdfs/company-ir/20241106%EB%9D%BC%EC%98%A8%ED%85%8C%ED%81%AC_%ED%9A%8C%EC%82%AC_%EC%9D%BC%EB%B0%98_%ED%98%84%ED%99%A9.pdf", "thesis": "반도체 웨이퍼 이송로봇 수요 회복과 장비 market growth가 강한 MFE로 연결됐으나 peak 이후 drawdown이 커서 4B watch 필요", "entry_date": "2024-12-19", "entry_price": 6460.0, "MFE_30D_pct": 55.418, "MAE_30D_pct": -5.2632, "MFE_90D_pct": 82.0433, "MAE_90D_pct": -5.2632, "MFE_180D_pct": 82.0433, "MAE_180D_pct": -5.2632, "peak_date": "2025-02-19", "peak_price": 11760.0, "drawdown_after_peak_pct": -43.7925, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
{"symbol": "086390", "name": "유니테스트", "trigger_date": "2025-04-03", "evidence_family": "HBM_burnin_tester_qualification_risk_supply_failure", "trigger_type": "Stage4B-LocalWatch", "classification": "positive_after_bridge_but_entry_requires_4B", "source_url": "https://dealsite.co.kr/articles/139224", "thesis": "HBM4 번인테스터 optionality는 있으나 수주 실패·재고/현금흐름 부담이 먼저 확인되어 Stage2/3 persistence 전 4B cap 필요", "entry_date": "2025-04-03", "entry_price": 10480.0, "MFE_30D_pct": 13.4542, "MAE_30D_pct": -18.2252, "MFE_90D_pct": 33.7786, "MAE_90D_pct": -18.2252, "MFE_180D_pct": 112.7863, "MAE_180D_pct": -18.2252, "peak_date": "2025-10-01", "peak_price": 22300.0, "drawdown_after_peak_pct": -40.8072, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
{"symbol": "089890", "name": "코세스", "trigger_date": "2024-03-13", "evidence_family": "advanced_packaging_laser_bonder_optionality_without_fresh_order_bridge", "trigger_type": "Stage4B-LocalWatch", "classification": "counterexample_high_MAE", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1642645695610.pdf", "thesis": "반도체 후공정/레이저 패키징 장비 노출은 있으나 fresh named order·revenue bridge가 약한 상태에서 MAE180이 깊게 열림", "entry_date": "2024-03-13", "entry_price": 15740.0, "MFE_30D_pct": 20.3939, "MAE_30D_pct": -13.4689, "MFE_90D_pct": 26.5565, "MAE_90D_pct": -18.4244, "MFE_180D_pct": 26.5565, "MAE_180D_pct": -61.9441, "peak_date": "2024-06-27", "peak_price": 19920.0, "drawdown_after_peak_pct": -69.9297, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
{"symbol": "187870", "name": "디바이스이엔지", "trigger_date": "2024-02-19", "evidence_family": "FOUP_cleaning_semiconductor_equipment_mix_shift", "trigger_type": "Stage2-Actionable", "classification": "counterexample_low_MFE_delayed_margin_bridge", "source_url": "https://ssl.pstatic.net/imgstock/upload/research/company/1708297940818.pdf", "thesis": "반도체 FOUP 오염제어 장비 비중 확대 thesis는 Stage2 신호지만 MFE가 제한적이고 180D drawdown이 커 Stage3 승격 전 order/revenue bridge 필요", "entry_date": "2024-02-19", "entry_price": 15120.0, "MFE_30D_pct": 5.8201, "MAE_30D_pct": -4.1667, "MFE_90D_pct": 16.2037, "MAE_90D_pct": -4.1667, "MFE_180D_pct": 16.2037, "MAE_180D_pct": -25.5952, "peak_date": "2024-06-18", "peak_price": 17570.0, "drawdown_after_peak_pct": -35.9704, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
{"symbol": "160980", "name": "싸이맥스", "trigger_date": "2024-06-17", "evidence_family": "wafer_transfer_robot_HBM_tool_automation_boundary", "trigger_type": "Stage4B-LocalWatch", "classification": "counterexample_hype_without_timing_bridge", "source_url": "https://cymechs.com/", "thesis": "웨이퍼 이송장치/로봇 국산화와 tool automation 품질은 있으나 HBM/후공정 timing bridge 없이 90D/180D MAE가 급격히 훼손", "entry_date": "2024-06-17", "entry_price": 20950.0, "MFE_30D_pct": 6.4439, "MAE_30D_pct": -27.1122, "MFE_90D_pct": 6.4439, "MAE_90D_pct": -51.2172, "MFE_180D_pct": 6.4439, "MAE_180D_pct": -64.6301, "peak_date": "2024-06-20", "peak_price": 22300.0, "drawdown_after_peak_pct": -66.7713, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "mixed_C09_advanced_equipment_order_revenue_bridge_fifth_pass", "price_source": "Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_usable": true, "representative": true, "source_proxy_only": false, "evidence_url_pending": false, "corporate_action_contaminated_180D": false, "insufficient_forward_window": false, "current_profile_error": true, "independent_evidence_weight": 1.0}
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not treat this MD as an immediate production patch request. Ingest this file only together with other V12 residual research files. Parse machine-readable trigger rows, validate the Stock-Web entry_date/entry_price/MFE/MAE fields, and deduplicate by canonical_archetype_id + symbol + trigger_type + entry_date. If accepted, consider a C09 shadow rule candidate named C09_ADVANCED_EQUIPMENT_REQUIRES_NAMED_ORDER_REVENUE_MARGIN_BRIDGE_WITH_OPTIONALITY_4B_CAP_V117. Do not change production scoring unless aggregate evidence across files supports it.
```

## 10. Batch Ingest Self-Audit

```yaml
standard_filename_ok: true
filename_matches_metadata: true
uses_no_repeat_index_as_ledger_only: true
uses_stock_web_actual_ohlcv: true
all_rows_have_entry_date: true
all_rows_have_entry_price: true
all_rows_have_MFE_30D_pct: true
all_rows_have_MAE_30D_pct: true
all_rows_have_MFE_90D_pct: true
all_rows_have_MAE_90D_pct: true
all_rows_have_MFE_180D_pct: true
all_rows_have_MAE_180D_pct: true
jsonl_trigger_row_count: 6
calibration_usable_rows: 6
representative_rows: 6
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

## 11. Next research state

```yaml
completed_round: R2
completed_loop: 117
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0 static ledger C09 rows=10 need_to_30=20
next_recommended_archetypes:
  - C14_EV_DEMAND_SLOWDOWN_4B_4C
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C06_HBM_MEMORY_CUSTOMER_CAPACITY
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```
