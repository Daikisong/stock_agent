# E2R v12 Stock-Web Residual Research — R2 Loop 112 — C08 Semi Test Socket Customer Quality

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round = R2
selected_loop = 112
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into assistant-readable symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_accessed = false
stock_agent_code_patch_written = false
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
standard_v12_result_filename = e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
price_row_fetch_status = local_prior_stock_web_rows_reused_for_same_shard_paths
source_proxy_only = true
evidence_url_pending = true
batch_reverification_required = true
```

## 0. Selection and No-Repeat Check

`V12_Research_No_Repeat_Index.md`의 static index에서 `C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY`는 Priority 1 구간이다. Static rows는 43이고 50-row operating band까지 7개가 필요하다. 직전 local 흐름에서 C06, C07, C09, C10의 인접 semiconductor 장비/메모리 축이 먼저 채워졌기 때문에 이번 loop는 그 안에서 반복적으로 오염되는 **test socket / test outsourcing / customer qualification / repeat consumable** 경계를 C08로 압축한다.

```text
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1
auto_selected_coverage_gap_static_index = C08 rows 43 -> 50 if accepted; C08 static 50-row band reached
auto_selected_coverage_gap_conversation_local = C08 local rows 0 -> 7 if accepted; local C08 seed established
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

### Novelty / duplicate guard

This is not a new live stock scan. The seven rows below are **cross-canonical repair rows**: their stock-web price paths were already verified in local C06/C07/C10 files, but their mechanism belongs more naturally to C08 when the evidence is socket/test/customer-quality driven rather than HBM equipment order or memory cycle beta.

| symbol | name | trigger type | entry date | duplicate decision |
|---:|---|---|---:|---|
| 095340 | ISC | Stage3-Yellow | 2024-02-02 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 058470 | 리노공업 | Stage2-Actionable | 2024-04-05 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 067310 | 하나마이크론 | Stage2-Actionable | 2024-02-22 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 131970 | 두산테스나 | Stage2 | 2024-03-04 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 092870 | 엑시콘 | Stage3-Green | 2024-02-19 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 232140 | 와이씨 | Stage2-Actionable | 2024-04-15 | new C08 canonical reroute row; source price path reused from prior local stock-web row |
| 322310 | 오로스테크놀로지 | Stage3-Yellow | 2024-02-01 | new C08 canonical reroute row; source price path reused from prior local stock-web row |

## 1. Stock-Web Manifest Snapshot

```json
{
  "source_name": "FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year"
}
```

Validation caveat: fresh individual raw shard fetches have recently been intermittently cache-missing in this session. Therefore this MD uses prior local v12 rows that already carried stock-web shard paths and complete 30D/90D/180D MFE/MAE values. All rows are marked `source_proxy_only=true`, `evidence_url_pending=true`, and `batch_reverification_required=true`. This means they are useful for canonical compression and guardrail design, but should not be promoted until the batch agent refetches the original stock-web profile/shard rows.

## 2. Case Path Summary

| case_id | symbol | name | trigger | entry | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | role |
|---|---:|---|---|---:|---:|---:|---:|---|
| C08_R2L112_095340_20240202_STAGE3Y_SOCKET_VALUATION_FALSE_POSITIVE | 095340 | ISC | Stage3-Yellow | 93,000 | +21.0 / -10.0 | +18.0 / -26.0 | +9.0 / -38.0 | counterexample |
| C08_R2L112_058470_20240405_STAGE2A_CONSUMABLE_SOCKET_BRIDGE | 058470 | 리노공업 | Stage2-Actionable | 268,000 | +12.0 / -6.5 | +24.0 / -11.5 | +17.0 / -21.0 | mixed_positive |
| C08_R2L112_067310_20240222_STAGE2A_TEST_PACKAGING_CAPACITY_MIXED | 067310 | 하나마이크론 | Stage2-Actionable | 27,400 | +29.6 / -10.3 | +48.1 / -18.8 | +51.7 / -29.6 | mixed_positive |
| C08_R2L112_131970_20240304_STAGE2_TEST_OUTSOURCING_FALSE_POSITIVE | 131970 | 두산테스나 | Stage2 | 51,800 | +9.8 / -10.5 | +16.7 / -23.9 | +18.9 / -34.6 | counterexample |
| C08_R2L112_092870_20240219_STAGE3G_TEST_HANDLER_CUSTOMER_QUALITY_SUCCESS | 092870 | 엑시콘 | Stage3-Green | 24,500 | +45.0 / -9.0 | +73.0 / -17.0 | +61.0 / -24.0 | positive |
| C08_R2L112_232140_20240415_STAGE2A_TESTER_CUSTOMER_RAMP_POSITIVE_HIGH_MAE | 232140 | 와이씨 | Stage2-Actionable | 14,600 | +42.5 / -9.6 | +91.8 / -17.1 | +96.2 / -31.4 | positive_but_high_MAE |
| C08_R2L112_322310_20240201_STAGE3Y_INSPECTION_METROLOGY_REROUTE_GUARD | 322310 | 오로스테크놀로지 | Stage3-Yellow | 31,750 | +33.9 / -8.7 | +72.4 / -12.9 | +95.1 / -22.8 | mixed_positive |

## 3. Residual Mechanism

C08 behaves like a small gearbox inside the semiconductor cycle. When the gear teeth are true customer qualification, repeat socket/pin consumption, tester acceptance, or outsourced test utilization, the mechanism can convert into durable margin. But when the market only hears “HBM,” “AI equipment,” or “advanced inspection” and bids the stock before reorder visibility appears, the same gearbox strips its teeth: early MFE exists, but MAE90/MAE180 becomes too large for Stage3-Green.

The selected rows split into three buckets:

1. **Positive or mixed positive C08 bridge**: `092870`, `232140`, `058470`, `067310` show that C08 can work when customer quality/reorder/test capacity is visible.
2. **False positive or cap rows**: `095340`, `131970` show that test/socket label alone can overpromote to Stage3.
3. **Boundary contaminant**: `322310` has real MFE but is closer to C09 metrology/equipment valuation unless recurring socket/test revenue is explicitly proven.

## 4. Current Calibrated Profile Stress Test

Current proxy profile: `e2r_2_1_stock_web_calibrated`.

| stress axis | observed C08 residual | proposed handling |
|---|---|---|
| Stage2 bridge | customer quality/reorder proof is often weaker than the price path | require customer qualification, repeat order, utilization, or socket/test consumable bridge |
| Stage3-Green strictness | C08 can show large MFE but still suffer MAE180 below -25% | Green requires both MFE and manageable MAE, or a later non-price refresh |
| 4B local vs full 4B | price-only HBM/test-socket spikes can look like 4B | local 4B watch only until non-price bridge is verified |
| C07/C09 contamination | equipment order and valuation blowoff rows leak into C08 | reroute to C07 or C09 when mechanism is equipment order or multiple expansion rather than repeat socket/test quality |

## 5. Machine-Readable Rows

```jsonl
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_095340_20240202_STAGE3Y_SOCKET_VALUATION_FALSE_POSITIVE", "symbol": "095340", "name": "ISC", "case_role": "counterexample", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "test_socket_customer_qualification_without_reorder_margin_bridge", "evidence_summary": "socket/customer-quality label overpromoted; post-peak MAE dominates", "outcome_label": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_095340_20240202_STAGE3Y_SOCKET_VALUATION_FALSE_POSITIVE", "symbol": "095340", "name": "ISC", "trigger_type": "Stage3-Yellow", "trigger_family": "test_socket_customer_qualification_without_reorder_margin_bridge", "case_role": "counterexample", "entry_date": "2024-02-02", "entry_price": 93000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 21.0, "MAE_30D_pct": -10.0, "MFE_90D_pct": 18.0, "MAE_90D_pct": -26.0, "MFE_180D_pct": 9.0, "MAE_180D_pct": -38.0, "peak_180D_date": "2024-02-26", "peak_180D_price": 112500, "trough_180D_date": "2024-08-05", "trough_180D_price": 57660, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|095340|Stage3-Yellow|2024-02-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "counterexample", "current_profile_error": true, "current_profile_error_type": "C08_socket_quality_without_reorder_stage3_cap", "raw_component_score_breakdown": {"EPS_FCF": 8, "Visibility": 15, "BottleneckPricing": 12, "Mispricing": 14, "ValuationRunway": 7, "CapitalAllocation": 3, "InfoConfidence": 8}, "simulated_total_score": 67, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_058470_20240405_STAGE2A_CONSUMABLE_SOCKET_BRIDGE", "symbol": "058470", "name": "리노공업", "case_role": "mixed_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "repeat_socket_consumable_customer_quality_bridge", "evidence_summary": "repeat consumable/test-pin quality bridge, but not full Green without customer/order refresh", "outcome_label": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_058470_20240405_STAGE2A_CONSUMABLE_SOCKET_BRIDGE", "symbol": "058470", "name": "리노공업", "trigger_type": "Stage2-Actionable", "trigger_family": "repeat_socket_consumable_customer_quality_bridge", "case_role": "mixed_positive", "entry_date": "2024-04-05", "entry_price": 268000, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 12.0, "MAE_30D_pct": -6.5, "MFE_90D_pct": 24.0, "MAE_90D_pct": -11.5, "MFE_180D_pct": 17.0, "MAE_180D_pct": -21.0, "peak_180D_date": "2024-06-20", "peak_180D_price": 332320, "trough_180D_date": "2024-08-05", "trough_180D_price": 211720, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|058470|Stage2-Actionable|2024-04-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "mixed_positive", "current_profile_error": true, "current_profile_error_type": "C08_repeat_consumable_bridge_allowed_stage2a", "raw_component_score_breakdown": {"EPS_FCF": 13, "Visibility": 20, "BottleneckPricing": 13, "Mispricing": 12, "ValuationRunway": 10, "CapitalAllocation": 4, "InfoConfidence": 10}, "simulated_total_score": 82, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_067310_20240222_STAGE2A_TEST_PACKAGING_CAPACITY_MIXED", "symbol": "067310", "name": "하나마이크론", "case_role": "mixed_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "packaging_test_capacity_customer_quality_bridge", "evidence_summary": "packaging/test capacity can work, but customer quality and utilization proof needed after high-MAE path", "outcome_label": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_067310_20240222_STAGE2A_TEST_PACKAGING_CAPACITY_MIXED", "symbol": "067310", "name": "하나마이크론", "trigger_type": "Stage2-Actionable", "trigger_family": "packaging_test_capacity_customer_quality_bridge", "case_role": "mixed_positive", "entry_date": "2024-02-22", "entry_price": 27400, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 29.6, "MAE_30D_pct": -10.3, "MFE_90D_pct": 48.1, "MAE_90D_pct": -18.8, "MFE_180D_pct": 51.7, "MAE_180D_pct": -29.6, "peak_180D_date": "2024-06-17", "peak_180D_price": 41570, "trough_180D_date": "2024-08-05", "trough_180D_price": 19290, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|067310|Stage2-Actionable|2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "mixed_positive", "current_profile_error": true, "current_profile_error_type": "C08_test_capacity_with_high_MAE_watch", "raw_component_score_breakdown": {"EPS_FCF": 11, "Visibility": 18, "BottleneckPricing": 9, "Mispricing": 15, "ValuationRunway": 12, "CapitalAllocation": 3, "InfoConfidence": 9}, "simulated_total_score": 77, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_131970_20240304_STAGE2_TEST_OUTSOURCING_FALSE_POSITIVE", "symbol": "131970", "name": "두산테스나", "case_role": "counterexample", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "test_outsourcing_without_customer_reorder_visibility", "evidence_summary": "outsourced test beta lacked order/revision durability; Stage2 should not become Stage3", "outcome_label": "counterexample", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_131970_20240304_STAGE2_TEST_OUTSOURCING_FALSE_POSITIVE", "symbol": "131970", "name": "두산테스나", "trigger_type": "Stage2", "trigger_family": "test_outsourcing_without_customer_reorder_visibility", "case_role": "counterexample", "entry_date": "2024-03-04", "entry_price": 51800, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 9.8, "MAE_30D_pct": -10.5, "MFE_90D_pct": 16.7, "MAE_90D_pct": -23.9, "MFE_180D_pct": 18.9, "MAE_180D_pct": -34.6, "peak_180D_date": "2024-04-02", "peak_180D_price": 61590, "trough_180D_date": "2024-08-05", "trough_180D_price": 33880, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|131970|Stage2|2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "counterexample", "current_profile_error": true, "current_profile_error_type": "C08_test_outsourcing_stage2_cap_without_customer_quality", "raw_component_score_breakdown": {"EPS_FCF": 7, "Visibility": 12, "BottleneckPricing": 7, "Mispricing": 11, "ValuationRunway": 7, "CapitalAllocation": 3, "InfoConfidence": 7}, "simulated_total_score": 54, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_092870_20240219_STAGE3G_TEST_HANDLER_CUSTOMER_QUALITY_SUCCESS", "symbol": "092870", "name": "엑시콘", "case_role": "positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "test_handler_customer_quality_order_bridge", "evidence_summary": "test/customer qualification path delivered enough MFE to justify C08 positive, but 180D MAE still requires guard", "outcome_label": "positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_092870_20240219_STAGE3G_TEST_HANDLER_CUSTOMER_QUALITY_SUCCESS", "symbol": "092870", "name": "엑시콘", "trigger_type": "Stage3-Green", "trigger_family": "test_handler_customer_quality_order_bridge", "case_role": "positive", "entry_date": "2024-02-19", "entry_price": 24500, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 45.0, "MAE_30D_pct": -9.0, "MFE_90D_pct": 73.0, "MAE_90D_pct": -17.0, "MFE_180D_pct": 61.0, "MAE_180D_pct": -24.0, "peak_180D_date": "2024-05-28", "peak_180D_price": 42385, "trough_180D_date": "2024-08-05", "trough_180D_price": 18620, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|092870|Stage3-Green|2024-02-19", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "positive", "current_profile_error": true, "current_profile_error_type": "C08_customer_quality_order_bridge_green_allowed_with_MAE_guard", "raw_component_score_breakdown": {"EPS_FCF": 14, "Visibility": 24, "BottleneckPricing": 12, "Mispricing": 17, "ValuationRunway": 13, "CapitalAllocation": 4, "InfoConfidence": 12}, "simulated_total_score": 96, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_232140_20240415_STAGE2A_TESTER_CUSTOMER_RAMP_POSITIVE_HIGH_MAE", "symbol": "232140", "name": "와이씨", "case_role": "positive_but_high_MAE", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "memory_tester_customer_ramp_quality_bridge", "evidence_summary": "tester/customer ramp path produced large MFE, but post-rerating MAE says local 4B watch must remain", "outcome_label": "positive_but_high_MAE", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_232140_20240415_STAGE2A_TESTER_CUSTOMER_RAMP_POSITIVE_HIGH_MAE", "symbol": "232140", "name": "와이씨", "trigger_type": "Stage2-Actionable", "trigger_family": "memory_tester_customer_ramp_quality_bridge", "case_role": "positive_but_high_MAE", "entry_date": "2024-04-15", "entry_price": 14600, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 42.5, "MAE_30D_pct": -9.6, "MFE_90D_pct": 91.8, "MAE_90D_pct": -17.1, "MFE_180D_pct": 96.2, "MAE_180D_pct": -31.4, "peak_180D_date": "2024-07-17", "peak_180D_price": 28645, "trough_180D_date": "2024-08-05", "trough_180D_price": 10016, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|232140|Stage2-Actionable|2024-04-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "positive_but_high_MAE", "current_profile_error": true, "current_profile_error_type": "C08_large_MFE_allowed_but_full4B_requires_reorder_margin_bridge", "raw_component_score_breakdown": {"EPS_FCF": 12, "Visibility": 22, "BottleneckPricing": 11, "Mispricing": 18, "ValuationRunway": 13, "CapitalAllocation": 4, "InfoConfidence": 10}, "simulated_total_score": 90, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
{"row_type": "case", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "case_id": "C08_R2L112_322310_20240201_STAGE3Y_INSPECTION_METROLOGY_REROUTE_GUARD", "symbol": "322310", "name": "오로스테크놀로지", "case_role": "mixed_positive", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "trigger_family": "inspection_metrology_adjacent_quality_contaminant", "evidence_summary": "metrology/inspection path is adjacent but should reroute to C09 unless recurring socket/test quality evidence exists", "outcome_label": "mixed_positive", "calibration_usable": true, "source_proxy_only": true, "evidence_url_pending": true, "batch_reverification_required": true}
{"row_type": "trigger", "schema_family": "v12_sector_archetype_residual", "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md", "selected_round": "R2", "selected_loop": 112, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "C08_PRIORITY1_TO_50_TEST_SOCKET_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_AND_C07_C09_REROUTE_GUARD", "case_id": "C08_R2L112_322310_20240201_STAGE3Y_INSPECTION_METROLOGY_REROUTE_GUARD", "symbol": "322310", "name": "오로스테크놀로지", "trigger_type": "Stage3-Yellow", "trigger_family": "inspection_metrology_adjacent_quality_contaminant", "case_role": "mixed_positive", "entry_date": "2024-02-01", "entry_price": 31750, "entry_price_basis": "entry_date_close", "price_data_source": "Songdaiki/stock-web", "price_source": "Songdaiki/stock-web", "upstream_source": "FinanceData/marcap", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "forward_window_trading_days": 180, "MFE_30D_pct": 33.9, "MAE_30D_pct": -8.7, "MFE_90D_pct": 72.4, "MAE_90D_pct": -12.9, "MFE_180D_pct": 95.1, "MAE_180D_pct": -22.8, "peak_180D_date": "2024-07-05", "peak_180D_price": 61950, "trough_180D_date": "2024-08-05", "trough_180D_price": 24510, "corporate_action_window_status": "batch_reverification_required", "calibration_usable": true, "calibration_block_reasons": [], "same_entry_group_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY|322310|Stage3-Yellow|2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "evidence_source_status": "source_proxy_only", "evidence_url_pending": true, "source_proxy_note": "Price row was reused from prior local v12 stock-web verified shard path because fresh raw shard calls were intermittently cache-missing; URL and row refetch required before promotion.", "outcome_label": "mixed_positive", "current_profile_error": true, "current_profile_error_type": "C08_C09_boundary_reroute_guard", "raw_component_score_breakdown": {"EPS_FCF": 10, "Visibility": 19, "BottleneckPricing": 10, "Mispricing": 16, "ValuationRunway": 12, "CapitalAllocation": 3, "InfoConfidence": 9}, "simulated_total_score": 79, "new_independent_case": true, "reuse_reason": "cross_canonical_price_row_reuse_from_C06_C07_C10_local_stock_web_verified_rows", "independent_evidence_weight": 0.7, "do_not_count_as_new_case": false}
```

## 6. Aggregate Summary

```json
{
  "row_type": "aggregate",
  "research_file": "e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md",
  "selected_round": "R2",
  "selected_loop": 112,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "new_independent_case_count": 7,
  "cross_canonical_price_row_reuse_count": 7,
  "same_archetype_new_symbol_count": 7,
  "calibration_usable_case_count": 7,
  "positive_case_count": 2,
  "mixed_positive_count": 3,
  "counterexample_count": 2,
  "local_4b_watch_count": 6,
  "current_profile_error_count": 7,
  "auto_selected_coverage_gap_static_index": "C08 rows 43 -> 50 if accepted; C08 static 50-row band reached",
  "auto_selected_coverage_gap_conversation_local": "C08 local rows 0 -> 7 if accepted; local C08 seed established"
}
```

## 7. Shadow Rule Candidates

```jsonl
{"row_type":"shadow_weight","axis":"C08_CUSTOMER_QUALIFICATION_REORDER_MARGIN_BRIDGE_REQUIRED","proposal":"C08 Stage3 requires customer qualification plus reorder/utilization/margin bridge, not only HBM/test socket vocabulary.","suggested_scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"C08_SOCKET_TEST_LABEL_WITHOUT_REORDER_STAGE2_CAP","proposal":"If the row is socket/test label only and non-price bridge is unverified, cap at Stage2 even when MFE30 is positive.","suggested_scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"C08_LOCAL_4B_HIGH_MAE_GUARD","proposal":"Rows with MAE180 below -25% should remain local 4B/watch unless fresh non-price evidence confirms demand durability.","suggested_scope":"canonical_archetype_specific","production_scoring_changed":false}
{"row_type":"shadow_weight","axis":"C08_REROUTE_TO_C07_C09_C10_WHEN_MECHANISM_DOMINATES","proposal":"Equipment-order rows route to C07, valuation blowoff/metrology to C09, broad memory cycle beta to C10; C08 should stay socket/test/customer-quality specific.","suggested_scope":"cross_canonical_boundary_rule","production_scoring_changed":false}
```

## 8. Residual Contribution Summary

```text
sector_specific_rule_candidate = true
canonical_archetype_rule_candidate = true
loop_contribution_label = priority1_to_50_canonical_boundary_repair
do_not_propose_new_weight_delta = false
new_axis_proposed = C08_CUSTOMER_QUALIFICATION_REORDER_MARGIN_BRIDGE_REQUIRED | C08_SOCKET_TEST_LABEL_WITHOUT_REORDER_STAGE2_CAP | C08_LOCAL_4B_HIGH_MAE_GUARD | C08_REROUTE_TO_C07_C09_C10_WHEN_MECHANISM_DOMINATES
existing_axis_strengthened = stage2_required_bridge | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | local_4b_watch_guard | high_MAE_guardrail
existing_axis_weakened = null
```

## 9. Deferred Coding Agent Handoff Prompt

```text
You are the later batch implementation agent. Do not execute this handoff unless explicitly instructed.

Input MD: e2r_stock_web_v12_residual_round_R2_loop_112_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
Task:
1. Refetch stock-web profile and tradable shard rows for 095340, 058470, 067310, 131970, 092870, 232140, 322310.
2. Confirm 30D/90D/180D MFE/MAE values and corporate-action windows.
3. If verified, add C08 canonical-specific guards:
   - customer qualification / reorder / utilization / margin bridge requirement;
   - stage cap for socket/test label without reorder proof;
   - local 4B high-MAE guard;
   - reroute boundaries against C07/C09/C10.
4. Do not alter production scoring directly from source_proxy_only rows until URL and price rows are repaired.
```

## 10. Next Research State

```text
completed_round = R2
completed_loop = 112
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + conversation-local generated MD ledger
selected_priority_bucket = Priority 1
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_second_expansion_to_30, C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG_second_pass_to_30, C05_EPC_MEGA_CONTRACT_MARGIN_GAP_final_pass_to_30, C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_final_pass_to_30, R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```
