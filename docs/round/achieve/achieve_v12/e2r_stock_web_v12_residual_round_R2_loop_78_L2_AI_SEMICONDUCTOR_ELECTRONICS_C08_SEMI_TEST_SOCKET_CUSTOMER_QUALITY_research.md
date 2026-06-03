# E2R Stock-Web v12 Residual Research — R2 Loop 78 / L2 / C08

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 78,
  "computed_next_round": "R3",
  "computed_next_loop": 78,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "semi_test_socket_customer_quality_guardrail",
    "customer_quality_socket_reorder_margin_bridge_vs_theme_beta",
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

Previous completed state in this interactive run: R1 / loop 78.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 78
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
computed_next_round = R3
computed_next_loop = 78
```

R2 was routed to C08 because loop 77 used C07 equipment-order relative strength.  
This file tests test-socket / probe-pin / connector customer-quality bridges rather than generic HBM equipment beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C08 is concentrated in:

```text
058470, 131290, 리노공업, 티에스이, 095340
```

This run uses three different symbols:

```text
425420 / 티에프이 / test socket customer-quality lifecycle candidate
080580 / 오킨스전자 / test socket connector theme fade
098120 / 마이크로컨텍솔 / IC socket customer-quality fade
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
advanced package / HBM / test demand
→ customer qualification and socket/probe order
→ reorder cadence and shipment visibility
→ ASP and margin bridge
→ durable rerating
```

테스트 소켓 테마는 핀 하나가 튀는 소리일 수 있다.  
C08은 그 핀이 실제 고객 인증, 반복 발주, 출하, 마진으로 꽂히는지를 본다.

---

## Case 1 — Lifecycle positive: 425420 / 티에프이

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is customer qualification, test-socket/probe-card order, HBM/advanced package demand, reorder cadence and margin bridge evidence.

```text
evidence_family = TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_HBM_REORDER_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 29,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv`:

```text
2024-02-01,29500,30300,28350,28800
2024-03-08,38300,41950,38000,38850
2024-03-20,40300,43850,38800,43100
2024-03-21,43550,43950,40350,41800
2024-08-05,20050,20350,16520,17490
2024-09-09,15140,15550,14720,15500
```

### Backtest

```text
MFE_30D  = +42.20%
MAE_30D  = -3.90%
MFE_90D  = +48.98%
MAE_90D  = -6.78%
MFE_180D = +48.98%
MAE_180D = -50.10%
peak_180 = 43,950 on 2024-03-21
trough_180 = 14,720 on 2024-09-09
peak_to_later_drawdown = -66.51%
```

### Interpretation

This is a C08 lifecycle positive candidate, not permanent Green.  
The early MFE and controlled early MAE are useful, but the later collapse says customer/reorder/margin evidence must refresh.

Correct treatment:

```text
verified customer qualification / socket order / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 080580 / 오킨스전자

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests socket/connector/HBM theme beta without enough customer-quality, reorder and margin bridge.

```text
evidence_family = TEST_SOCKET_CONNECTOR_HBM_THEME_WITH_WEAK_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE
case_role = counterexample_socket_connector_theme_local4b
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
2024-03-27,9300,9300,8600,8730
2024-04-09,8080,8390,7750,7780
2024-08-05,6000,6150,4865,5140
```

### Backtest

```text
MFE_30D  = +21.06%
MAE_30D  = -17.37%
MFE_90D  = +21.06%
MAE_90D  = -34.98%
MFE_180D = +21.06%
MAE_180D = -59.19%
peak_180 = 14,430 on 2024-02-02
trough_180 = 4,865 on 2024-08-05
peak_to_later_drawdown = -66.29%
```

### Interpretation

This is a socket theme false positive.  
The first move was tradable, but it did not validate durable customer-quality rerating.

Correct treatment:

```text
socket / connector theme beta
→ no verified qualification / reorder / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 098120 / 마이크로컨텍솔

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests IC-socket/test-parts exposure without enough customer order and margin bridge.

```text
evidence_family = IC_SOCKET_TEST_PARTS_THEME_WITH_WEAK_CUSTOMER_QUALITY_ORDER_MARGIN_BRIDGE
case_role = counterexample_IC_socket_quality_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,080
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv`:

```text
2024-02-01,11080,11330,10700,10980
2024-02-14,11250,11860,11110,11540
2024-03-14,10130,10180,9730,9820
2024-04-08,9790,9810,9010,9010
2024-08-05,6870,6910,5510,5680
2024-09-09,5060,5340,4965,5340
```

### Backtest

```text
MFE_30D  = +7.04%
MAE_30D  = -12.18%
MFE_90D  = +7.04%
MAE_90D  = -29.96%
MFE_180D = +7.04%
MAE_180D = -55.19%
peak_180 = 11,860 on 2024-02-14
trough_180 = 4,965 on 2024-09-09
peak_to_later_drawdown = -58.14%
```

### Interpretation

This is the weak-MFE C08 boundary.  
The price path did not validate a customer-quality cycle.

Correct treatment:

```text
IC socket / test-parts beta
→ no customer qualification / order / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C08_socket_theme_weight = true
do_not_treat_all_test_socket_MFE_as_Green = true
do_not_convert_socket_drawdown_to_hard_4C_without_non_price_customer_qualification_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE
```

This fine archetype covers:

```text
1. test-socket customer-quality MFE → Stage2 possible after source repair, lifecycle-managed
2. socket/connector theme without reorder/margin bridge → false Stage2 / local 4B
3. IC-socket test-parts beta without customer order bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TestSocketCustomerQualityBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should allow test-socket / probe-pin positives only when customer quality, HBM or advanced package qualification, reorder cadence and margin bridge are visible. TFE had strong early MFE, but the later drawdown means the signal must be lifecycle-managed if quality/reorder/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer qualification, socket/probe demand, reorder, ASP and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TestSocketConnectorThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should not treat socket/connector/HBM theme beta as durable Stage2 unless customer qualification, socket reorder, shipment, ASP and margin bridge are visible. Okins Electronics had an early MFE but then opened a severe MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer qualification, socket/probe demand, reorder, ASP and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "case_type": "semi_test_socket_customer_quality", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ICSocketCustomerQualityFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C08 should not treat IC-socket/test-parts exposure as durable Stage2 unless customer quality, socket demand, order visibility and margin bridge refreshes. Micro Contact Solution had limited MFE and then a large MAE drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer qualification, socket/probe demand, reorder, ASP and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "case_id": "R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "company_name": "티에프이", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-Actionable-TestSocketCustomerQualityBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 29500.0, "evidence_available_at_that_date": "TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_HBM_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TFE_2024_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_HBM_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_or_qualification_candidate", "test_socket_or_probe_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "HBM_advanced_package_or_reorder_bridge_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/425/425420/2024.csv", "profile_path": "atlas/symbol_profiles/425/425420.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.2, "MFE_90D_pct": 48.98, "MFE_180D_pct": 48.98, "MAE_30D_pct": -3.9, "MAE_90D_pct": -6.78, "MAE_180D_pct": -50.1, "peak_date": "2024-03-21", "peak_price": 43950.0, "drawdown_after_peak_pct": -66.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_socket_peak_if_customer_quality_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_qualification_failure_order_cut_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C08 should allow test-socket / probe-pin positives only when customer quality, HBM or advanced package qualification, reorder cadence and margin bridge are visible. TFE had strong early MFE, but the later drawdown means the signal must be lifecycle-managed if quality/reorder/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_425420_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE", "case_id": "R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE", "symbol": "080580", "company_name": "오킨스전자", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-FalsePositive / TestSocketConnectorThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11920.0, "evidence_available_at_that_date": "TEST_SOCKET_CONNECTOR_HBM_THEME_WITH_WEAK_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:OKINS_ELECTRONICS_2024_TEST_SOCKET_CONNECTOR_CUSTOMER_QUALITY_REORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_or_qualification_candidate", "test_socket_or_probe_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "HBM_advanced_package_or_reorder_bridge_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/080/080580/2024.csv", "profile_path": "atlas/symbol_profiles/080/080580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.06, "MFE_90D_pct": 21.06, "MFE_180D_pct": 21.06, "MAE_30D_pct": -17.37, "MAE_90D_pct": -34.98, "MAE_180D_pct": -59.19, "peak_date": "2024-02-02", "peak_price": 14430.0, "drawdown_after_peak_pct": -66.29, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_socket_peak_if_customer_quality_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_qualification_failure_order_cut_margin_or_financing_break", "trigger_outcome_label": "counterexample_socket_connector_theme_local4b", "current_profile_verdict": "C08 should not treat socket/connector/HBM theme beta as durable Stage2 unless customer qualification, socket reorder, shipment, ASP and margin bridge are visible. Okins Electronics had an early MFE but then opened a severe MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_080580_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE", "case_id": "R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE", "symbol": "098120", "company_name": "마이크로컨텍솔", "round": "R2", "loop": "78", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|semi_test_socket_customer_quality_guardrail", "trigger_type": "Stage2-FalsePositive / ICSocketCustomerQualityFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11080.0, "evidence_available_at_that_date": "IC_SOCKET_TEST_PARTS_THEME_WITH_WEAK_CUSTOMER_QUALITY_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MICROCONTACTSOL_2024_IC_SOCKET_TEST_PARTS_CUSTOMER_QUALITY_ORDER_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_quality_or_qualification_candidate", "test_socket_or_probe_order_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "HBM_advanced_package_or_reorder_bridge_candidate"], "stage4b_evidence_fields": ["socket_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/098/098120/2024.csv", "profile_path": "atlas/symbol_profiles/098/098120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.04, "MFE_90D_pct": 7.04, "MFE_180D_pct": 7.04, "MAE_30D_pct": -12.18, "MAE_90D_pct": -29.96, "MAE_180D_pct": -55.19, "peak_date": "2024-02-14", "peak_price": 11860.0, "drawdown_after_peak_pct": -58.14, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_socket_peak_if_customer_quality_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_qualification_failure_order_cut_margin_or_financing_break", "trigger_outcome_label": "counterexample_IC_socket_quality_local4b", "current_profile_verdict": "C08 should not treat IC-socket/test-parts exposure as durable Stage2 unless customer quality, socket demand, order visibility and margin bridge refreshes. Micro Contact Solution had limited MFE and then a large MAE drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C08_TEST_SOCKET_098120_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "trigger_id": "TRG_R2L78-C08-425420-TFE-TEST-SOCKET-CUSTOMER-QUALITY-LIFECYCLE", "symbol": "425420", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 14, "socket_probe_order_score": 14, "qualification_visibility_score": 13, "reorder_visibility_score": 12, "margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_quality_score": 16, "socket_probe_order_score": 16, "qualification_visibility_score": 15, "reorder_visibility_score": 14, "margin_bridge_score": 14, "relative_strength_score": 11, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_quality_score", "socket_probe_order_score", "qualification_visibility_score", "reorder_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer qualification, socket/probe order, reorder and margin bridge; cap socket/test-parts theme beta when evidence fails to refresh.", "MFE_90D_pct": 48.98, "MAE_90D_pct": -6.78, "score_return_alignment_label": "test_socket_quality_positive_with_lifecycle_4b", "current_profile_verdict": "C08 should allow test-socket / probe-pin positives only when customer quality, HBM or advanced package qualification, reorder cadence and margin bridge are visible. TFE had strong early MFE, but the later drawdown means the signal must be lifecycle-managed if quality/reorder/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE", "trigger_id": "TRG_R2L78-C08-080580-OKINS-TEST-SOCKET-THEME-FADE", "symbol": "080580", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 4, "socket_probe_order_score": 3, "qualification_visibility_score": 3, "reorder_visibility_score": 2, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_quality_score": 2, "socket_probe_order_score": 1, "qualification_visibility_score": 1, "reorder_visibility_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "socket_probe_order_score", "qualification_visibility_score", "reorder_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer qualification, socket/probe order, reorder and margin bridge; cap socket/test-parts theme beta when evidence fails to refresh.", "MFE_90D_pct": 21.06, "MAE_90D_pct": -34.98, "score_return_alignment_label": "false_positive_socket_theme_bridge_gap", "current_profile_verdict": "C08 should not treat socket/connector/HBM theme beta as durable Stage2 unless customer qualification, socket reorder, shipment, ASP and margin bridge are visible. Okins Electronics had an early MFE but then opened a severe MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE", "trigger_id": "TRG_R2L78-C08-098120-MICROCONTACTSOL-IC-SOCKET-CUSTOMER-QUALITY-FADE", "symbol": "098120", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "raw_component_scores_before": {"customer_quality_score": 4, "socket_probe_order_score": 3, "qualification_visibility_score": 3, "reorder_visibility_score": 2, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_quality_score": 2, "socket_probe_order_score": 1, "qualification_visibility_score": 1, "reorder_visibility_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_quality_score", "socket_probe_order_score", "qualification_visibility_score", "reorder_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer qualification, socket/probe order, reorder and margin bridge; cap socket/test-parts theme beta when evidence fails to refresh.", "MFE_90D_pct": 7.04, "MAE_90D_pct": -29.96, "score_return_alignment_label": "false_positive_socket_theme_bridge_gap", "current_profile_verdict": "C08 should not treat IC-socket/test-parts exposure as durable Stage2 unless customer quality, socket demand, order visibility and margin bridge refreshes. Micro Contact Solution had limited MFE and then a large MAE drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 78, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "fine_archetype_id": "TEST_SOCKET_PROBE_PIN_CUSTOMER_QUALITY_BRIDGE_VS_SOCKET_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C08 test/socket symbols outside top-covered 058470/131290/리노공업/티에스이/095340 set, +3 TFE/Okins/Microcontact trigger families, +1 test-socket quality lifecycle candidate, +2 socket theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 78, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "axis": "test_socket_probe_pin_customer_quality_bridge_vs_socket_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C08 should split verified semi test-socket/probe-pin customer-quality rerating from generic socket/theme beta. Stage2 requires named customer qualification, socket/probe order, advanced-package/HBM demand, reorder cadence and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["425420", "080580", "098120"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 78, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C08 needs customer qualification and socket/probe reorder proof. TFE shows a test-socket lifecycle MFE candidate after source repair; Okins Electronics and Micro Contact Solution show socket/test-parts theme beta fading into local 4B when customer quality, order and margin bridge are absent."}
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

080580:
  name = 오킨스전자
  corporate_action_candidate_dates = 2021-01-07, 2021-01-29
  selected window = 2024-02-01~D+180
  contamination = false

098120:
  name = 마이크로컨텍솔
  corporate_action_candidate_dates = 2011-04-19, 2011-05-17
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C08 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C08 rule-shape discovery,
but coding-agent promotion requires non-proxy customer qualification, socket/probe order, reorder, ASP and margin evidence.
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
test_socket_probe_pin_customer_quality_bridge_vs_socket_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 425420, 080580 and 098120.
4. Keep generic C08 test-socket/customer-quality weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer qualification or quality win is explicit,
   - test socket / probe / connector order visibility is visible,
   - HBM or advanced package demand bridge exists,
   - reorder cadence and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is socket/test-parts theme beta only,
   - customer qualification/order/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, qualification failure, order cut, utilization collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified low-MAE customer-quality socket positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 78
next_round = R3
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

