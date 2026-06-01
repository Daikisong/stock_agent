# E2R Stock-Web v12 Residual Research — R2 Loop 81 / L2 / C08

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 81,
  "computed_next_round": "R3",
  "computed_next_loop": 81,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "semi_test_socket_customer_quality_guardrail",
    "test_socket_interface_board_customer_quality_reorder_margin_bridge",
    "test_socket_theme_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## Execution compliance note

This file is a standalone historical calibration / sector-archetype residual research Markdown artifact.  
It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

The execution used `Songdaiki/stock-web` as the sole price atlas:

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

## Round / scope resolution

Previous completed state in this interactive run: R1 / loop 81.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 81
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
computed_next_round = R3
computed_next_loop = 81
```

R2 was routed to C08 because loop 80 R2 used C07 and loop 79 R2 used C09.  
This file tests test socket / interface board / socket-probe customer quality bridges.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C08 concentration in:

```text
058470, 131290, 095340, 리노공업, 티에스이
```

This run uses three different symbols:

```text
425420 / 티에프이 / test socket and interface board customer-quality lifecycle
098120 / 마이크로컨텍솔 / IC/test socket theme fade
080580 / 오킨스전자 / socket/probe theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C08 is not “소켓주가 올랐다.”

The mechanism must pass through:

```text
AI / HBM / advanced package demand
→ test socket or interface-board customer quality
→ reorder cadence and delivery schedule
→ utilization and revenue conversion
→ margin bridge
→ durable rerating
```

테스트소켓은 반도체 공정의 작은 접점이다.  
C08이 보려는 것은 접점이 실제 고객, 재주문, 납기, 매출, 마진으로 전류를 계속 흘리는지다.

---

## Case 1 — Test socket lifecycle candidate: 425420 / 티에프이

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is customer quality, reorder visibility, socket/interface-board demand, capacity utilization and margin bridge evidence.

```text
evidence_family = TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_CAPACITY_UTILIZATION_MARGIN_BRIDGE
case_role = positive_lifecycle_test_socket_customer_quality_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 29,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv`:

```text
2024-02-01,29500,30300,28350,28800
2024-02-08,30500,35950,30500,35200
2024-03-08,38300,41950,38000,38850
2024-03-21,43550,43950,40350,41800
2024-05-24,32500,32750,31100,31800
2024-08-05,20050,20350,16520,17490
2024-09-09,15140,15550,14720,15500
2024-10-25,15910,16500,15340,15340
```

### Backtest

```text
MFE_30D  = +42.20%
MAE_30D  = -3.90%
MFE_90D  = +48.98%
MAE_90D  = -3.90%
MFE_180D = +48.98%
MAE_180D = -50.10%
peak_180 = 43,950 on 2024-03-21
trough_180 = 14,720 on 2024-09-09
peak_to_later_drawdown = -66.51%
```

### Interpretation

This is a C08 lifecycle candidate.  
The early MFE was strong, but the later MAE path says customer/reorder/margin evidence must refresh.

Correct treatment:

```text
verified customer quality / reorder / delivery / margin bridge → Stage2-Yellow possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 098120 / 마이크로컨텍솔

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests IC/test-socket theme beta without enough customer reorder and margin bridge.

```text
evidence_family = IC_SOCKET_TEST_SOCKET_THEME_WITH_WEAK_CUSTOMER_REORDER_MARGIN_BRIDGE
case_role = counterexample_test_socket_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,080
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv`:

```text
2024-02-01,11080,11330,10700,10980
2024-02-14,11250,11860,11110,11540
2024-02-21,10180,10530,9980,10390
2024-03-14,10130,10180,9730,9820
2024-04-08,9790,9810,9010,9010
2024-08-05,6870,6910,5510,5680
2024-09-09,5060,5340,4965,5340
2024-10-25,5170,5250,5130,5180
```

### Backtest

```text
MFE_30D  = +7.04%
MAE_30D  = -12.18%
MFE_90D  = +7.04%
MAE_90D  = -29.33%
MFE_180D = +7.04%
MAE_180D = -55.19%
peak_180 = 11,860 on 2024-02-14
trough_180 = 4,965 on 2024-09-09
peak_to_later_drawdown = -58.14%
```

### Interpretation

This is a C08 false-positive boundary.  
The socket theme did not validate durable customer-quality rerating.

Correct treatment:

```text
IC/test-socket theme beta
→ no verified customer reorder / delivery / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 080580 / 오킨스전자

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests socket/probe/interface theme beta without enough customer-quality and reorder bridge.

```text
evidence_family = SEMICONDUCTOR_SOCKET_PROBE_INTERFACE_THEME_WITH_WEAK_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE
case_role = counterexample_socket_probe_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,920
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv`:

```text
2024-02-01,11920,14090,11860,13350
2024-02-02,13650,14430,13120,13370
2024-02-14,11250,14120,11240,13450
2024-02-28,10180,10800,9890,10780
2024-04-08,8670,8670,7830,7980
2024-08-05,6000,6150,4865,5140
2024-09-12,5150,6550,5150,5750
2024-10-25,5600,5660,5500,5520
```

### Backtest

```text
MFE_30D  = +21.06%
MAE_30D  = -17.03%
MFE_90D  = +21.06%
MAE_90D  = -36.33%
MFE_180D = +21.06%
MAE_180D = -59.19%
peak_180 = 14,430 on 2024-02-02
trough_180 = 4,865 on 2024-08-05
peak_to_later_drawdown = -66.29%
```

### Interpretation

This is the socket/probe theme-fade row.  
The early MFE was tradable, but it did not become durable C08 customer-quality rerating.

Correct treatment:

```text
socket/probe/interface theme beta
→ no verified customer quality / reorder / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
customer_quality_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C08_socket_theme_weight = true
do_not_treat_all_socket_MFE_as_Green = true
do_not_convert_socket_theme_drawdown_to_hard_4C_without_non_price_customer_loss_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE
```

This fine archetype covers:

```text
1. test socket / interface-board customer-quality bridge → Stage2-Yellow possible after source repair
2. IC socket beta without reorder/margin bridge → false Stage2 / local 4B
3. socket/probe/interface beta without customer-quality bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-TestSocketCustomerQualityReorderMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should preserve test-socket/interface-board positives when customer quality, reorder visibility, capacity utilization, delivery cadence and margin bridge are visible. TFE produced a large MFE, but the later high-MAE drawdown forces lifecycle local 4B if reorder/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer quality, reorder cadence, socket/interface board demand, delivery/revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TestSocketCustomerQualityBridgeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should not treat IC/test-socket theme beta as durable Stage2 unless customer quality, reorder cadence, delivery/revenue and margin bridge are visible. Micro Contact Solution had only small early MFE and then severe MAE.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer quality, reorder cadence, socket/interface board demand, delivery/revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SocketProbeThemeMFEFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should not treat socket/probe/interface theme beta as durable Stage2 unless named customer quality, reorder, utilization, delivery and margin bridge are visible. Okins Electronics had a tradable early MFE, then a severe high-MAE fade.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer quality, reorder cadence, socket/interface board demand, delivery/revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "case_id": "R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-Lifecycle-TestSocketCustomerQualityReorderMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 29500.0, "evidence_available_at_that_date": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_CAPACITY_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TFE_2024_TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_candidate", "reorder_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "socket_interface_board_demand_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "profile_path": "atlas/symbol_profiles/425/425420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.2, "MFE_90D_pct": 48.98, "MFE_180D_pct": 48.98, "MAE_30D_pct": -3.9, "MAE_90D_pct": -3.9, "MAE_180D_pct": -50.1, "peak_date": "2024-03-21", "peak_price": 43950.0, "drawdown_after_peak_pct": -66.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_test_socket_peak_if_customer_quality_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_decline_margin_or_financing_break", "trigger_outcome_label": "positive_lifecycle_test_socket_customer_quality_with_later_high_MAE_4b_watch", "current_profile_verdict": "C08 should preserve test-socket/interface-board positives when customer quality, reorder visibility, capacity utilization, delivery cadence and margin bridge are visible. TFE produced a large MFE, but the later high-MAE drawdown forces lifecycle local 4B if reorder/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_425420_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE", "case_id": "R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-FalsePositive / TestSocketCustomerQualityBridgeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11080.0, "evidence_available_at_that_date": "IC_SOCKET_TEST_SOCKET_THEME_WITH_WEAK_CUSTOMER_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MICROCONTACTSOL_2024_TEST_SOCKET_CUSTOMER_REORDER_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_candidate", "reorder_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "socket_interface_board_demand_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "profile_path": "atlas/symbol_profiles/098/098120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.04, "MFE_90D_pct": 7.04, "MFE_180D_pct": 7.04, "MAE_30D_pct": -12.18, "MAE_90D_pct": -29.33, "MAE_180D_pct": -55.19, "peak_date": "2024-02-14", "peak_price": 11860.0, "drawdown_after_peak_pct": -58.14, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_test_socket_peak_if_customer_quality_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_decline_margin_or_financing_break", "trigger_outcome_label": "counterexample_test_socket_theme_local4b", "current_profile_verdict": "C08 should not treat IC/test-socket theme beta as durable Stage2 unless customer quality, reorder cadence, delivery/revenue and margin bridge are visible. Micro Contact Solution had only small early MFE and then severe MAE.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_098120_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE", "case_id": "R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "81", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-FalsePositive / SocketProbeThemeMFEFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11920.0, "evidence_available_at_that_date": "SEMICONDUCTOR_SOCKET_PROBE_INTERFACE_THEME_WITH_WEAK_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:OKINS_ELECTRONICS_2024_SOCKET_PROBE_INTERFACE_CUSTOMER_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_candidate", "reorder_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "socket_interface_board_demand_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "profile_path": "atlas/symbol_profiles/080/080580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.06, "MFE_90D_pct": 21.06, "MFE_180D_pct": 21.06, "MAE_30D_pct": -17.03, "MAE_90D_pct": -36.33, "MAE_180D_pct": -59.19, "peak_date": "2024-02-02", "peak_price": 14430.0, "drawdown_after_peak_pct": -66.29, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_test_socket_peak_if_customer_quality_reorder_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_decline_margin_or_financing_break", "trigger_outcome_label": "counterexample_socket_probe_theme_local4b", "current_profile_verdict": "C08 should not treat socket/probe/interface theme beta as durable Stage2 unless named customer quality, reorder, utilization, delivery and margin bridge are visible. Okins Electronics had a tradable early MFE, then a severe high-MAE fade.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_080580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "trigger_id": "TRG_R2L81-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 14, "reorder_visibility_score": 13, "socket_interface_demand_score": 13, "delivery_revenue_score": 12, "margin_bridge_score": 13, "relative_strength_score": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"customer_quality_score": 16, "reorder_visibility_score": 15, "socket_interface_demand_score": 15, "delivery_revenue_score": 14, "margin_bridge_score": 15, "relative_strength_score": 9, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_quality_score", "reorder_visibility_score", "socket_interface_demand_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer quality, reorder cadence, socket/interface demand, delivery/revenue and margin bridge; cap socket/probe theme beta when bridge fails to refresh.", "MFE_90D_pct": 48.98, "MAE_90D_pct": -3.9, "score_return_alignment_label": "test_socket_customer_quality_positive_with_lifecycle_4b", "current_profile_verdict": "C08 should preserve test-socket/interface-board positives when customer quality, reorder visibility, capacity utilization, delivery cadence and margin bridge are visible. TFE produced a large MFE, but the later high-MAE drawdown forces lifecycle local 4B if reorder/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE", "trigger_id": "TRG_R2L81-C08-098120-MICROCONTACTSOL-TEST-SOCKET-THEME-FADE", "symbol": "098120", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 4, "reorder_visibility_score": 3, "socket_interface_demand_score": 4, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_quality_score": 2, "reorder_visibility_score": 1, "socket_interface_demand_score": 2, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "reorder_visibility_score", "socket_interface_demand_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer quality, reorder cadence, socket/interface demand, delivery/revenue and margin bridge; cap socket/probe theme beta when bridge fails to refresh.", "MFE_90D_pct": 7.04, "MAE_90D_pct": -29.33, "score_return_alignment_label": "false_positive_socket_theme_bridge_gap", "current_profile_verdict": "C08 should not treat IC/test-socket theme beta as durable Stage2 unless customer quality, reorder cadence, delivery/revenue and margin bridge are visible. Micro Contact Solution had only small early MFE and then severe MAE."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE", "trigger_id": "TRG_R2L81-C08-080580-OKINS-ELECTRONICS-SOCKET-THEME-FADE", "symbol": "080580", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 4, "reorder_visibility_score": 3, "socket_interface_demand_score": 4, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_quality_score": 2, "reorder_visibility_score": 1, "socket_interface_demand_score": 2, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "reorder_visibility_score", "socket_interface_demand_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer quality, reorder cadence, socket/interface demand, delivery/revenue and margin bridge; cap socket/probe theme beta when bridge fails to refresh.", "MFE_90D_pct": 21.06, "MAE_90D_pct": -36.33, "score_return_alignment_label": "false_positive_socket_theme_bridge_gap", "current_profile_verdict": "C08 should not treat socket/probe/interface theme beta as durable Stage2 unless named customer quality, reorder, utilization, delivery and margin bridge are visible. Okins Electronics had a tradable early MFE, then a severe high-MAE fade."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 81, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_INTERFACE_BOARD_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE_VS_SOCKET_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C08 test-socket/interface symbols outside top-covered 058470/131290/095340 set, +3 TFE/MicroContactSol/Okins trigger families, +1 lifecycle test-socket customer-quality positive, +2 socket theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 81, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "axis": "test_socket_interface_board_customer_quality_reorder_margin_bridge_vs_socket_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C08 should split verified test-socket/interface-board customer-quality rerating from generic socket/probe theme beta. Stage2 requires customer quality, reorder visibility, socket/interface demand, delivery/revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["425420", "098120", "080580"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 81, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "existing_axis_strengthened": ["stage2_required_bridge", "customer_quality_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C08 needs customer quality, reorder cadence, socket/interface demand, delivery/revenue and margin proof. TFE shows a test-socket/interface-board lifecycle candidate after source repair; Micro Contact Solution and Okins Electronics show socket/probe theme beta fading into local 4B when customer-quality and margin bridge are absent or stale."}
```

---

## Validation scope

```text
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
forward_window_basis = stock_web_manifest_max_date
all_selected_entry_dates_present_in_tradable_shards = true
all_selected_180D_windows_available = true
production_scoring_changed = false
shadow_weight_only = true
```

Profile checks:

```text
425420:
  name = 티에프이
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

098120:
  name = 마이크로컨텍솔
  corporate_action_candidate_dates = 2011-04-19, 2011-05-17
  selected window = 2024-02-01~D+180
  contamination = false

080580:
  name = 오킨스전자
  corporate_action_candidate_dates = 2021-01-07, 2021-01-29
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C08 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C08 rule-shape discovery,
but coding-agent promotion requires non-proxy customer quality, reorder cadence, socket/interface board demand, delivery/revenue conversion and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C08 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
test_socket_interface_board_customer_quality_reorder_margin_bridge_vs_socket_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 425420, 098120 and 080580.
4. Keep generic C08 test-socket/customer-quality weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer quality is explicit,
   - reorder cadence or socket/interface-board demand is visible,
   - delivery schedule and revenue conversion exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is socket/probe/interface theme beta only,
   - customer/reorder/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, utilization decline, financing or margin break.
8. Emit before/after diagnostics and reject if verified customer-quality socket positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 81
next_round = R3
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

