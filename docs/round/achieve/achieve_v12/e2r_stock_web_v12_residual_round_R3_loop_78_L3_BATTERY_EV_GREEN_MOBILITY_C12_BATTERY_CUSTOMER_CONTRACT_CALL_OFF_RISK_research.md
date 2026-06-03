# E2R Stock-Web v12 Residual Research — R3 Loop 78 / L3 / C12

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 78,
  "computed_next_round": "R4",
  "computed_next_loop": 78,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_customer_contract_calloff_guardrail",
    "customer_calloff_capacity_absorption_margin_bridge",
    "separator_material_calloff_fade_boundary",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R2 / loop 78.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 78
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 78
```

R3 was routed to C12 because loop 77 used C11 and C13/C14 are already heavily represented in the visible no-repeat slice.  
This file tests customer contract / call-off / capacity-absorption risk rather than generic battery material orderbook rerating.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C12 concentration in:

```text
UNKNOWN_SYMBOL, 247540, 278280, 003670, 005070
```

This run uses three different symbols:

```text
121600 / 나노신소재 / CNT conductive-material customer call-off lifecycle
361610 / SK아이이테크놀로지 / separator call-off utilization fade
393890 / 더블유씨피 / separator customer call-off margin fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
121600 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
393890 changed market segment from KOSDAQ to KOSDAQ GLOBAL on 2024-06-14, but the profile does not flag this as a corporate-action candidate.
```

## Research thesis

C12 is not “배터리 고객사가 있다.”

The mechanism must pass through:

```text
customer contract / nomination
→ call-off volume and shipment cadence
→ capacity absorption / utilization
→ pricing and margin conversion
→ durable rerating
```

계약은 주문서가 아니라 문 앞의 예약표다.  
C12가 보려는 것은 그 예약이 실제 출하, 가동률, 단가, 마진으로 들어오는지다.

---

## Case 1 — Lifecycle positive: 121600 / 나노신소재

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is CNT conductive-material customer contract, call-off volume, capacity absorption, shipment cadence and margin bridge evidence.

```text
evidence_family = CNT_CONDUCTIVE_MATERIAL_BATTERY_CUSTOMER_CALLOFF_CAPACITY_ABSORPTION_MARGIN_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 95,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv`:

```text
2024-02-01,95600,99100,94200,98600
2024-02-21,105000,136300,104100,134000
2024-02-22,133100,157800,130600,138000
2024-06-11,122000,149800,121300,141500
2024-08-05,87900,89700,68500,74900
2024-09-10,80900,82600,78400,78900
```

### Backtest

```text
MFE_30D  = +65.06%
MAE_30D  = -1.46%
MFE_90D  = +65.06%
MAE_90D  = -1.46%
MFE_180D = +65.06%
MAE_180D = -28.35%
peak_180 = 157,800 on 2024-02-22
trough_180 = 68,500 on 2024-08-05
peak_to_later_drawdown = -56.59%
```

### Interpretation

This is a C12 lifecycle positive candidate.  
The initial move was strong and entry-basis MAE was controlled, but the later drawdown means call-off and margin evidence must refresh.

Correct treatment:

```text
verified customer call-off / capacity absorption / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 361610 / SK아이이테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests separator customer contract exposure without enough call-off, utilization and margin bridge.

```text
evidence_family = BATTERY_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE_WEAK_REFRESH
case_role = counterexample_separator_calloff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 73,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv`:

```text
2024-02-01,73400,74800,73400,74800
2024-02-02,75500,80800,74600,76000
2024-04-16,62000,62500,60600,60600
2024-05-30,45000,45350,43200,43300
2024-08-05,36000,36200,30950,32000
2024-09-10,31750,32100,30050,30050
```

### Backtest

```text
MFE_30D  = +10.08%
MAE_30D  = -11.31%
MFE_90D  = +10.08%
MAE_90D  = -41.83%
MFE_180D = +10.08%
MAE_180D = -59.06%
peak_180 = 80,800 on 2024-02-02
trough_180 = 30,050 on 2024-09-10
peak_to_later_drawdown = -62.81%
```

### Interpretation

This is a C12 call-off risk failure.  
The first bounce was not enough to validate durable separator utilization or margin conversion.

Correct treatment:

```text
separator / customer contract beta
→ no refreshed call-off / utilization / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 393890 / 더블유씨피

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests separator customer call-off exposure without enough utilization and shipment-margin evidence.

```text
evidence_family = BATTERY_SEPARATOR_CUSTOMER_CALLOFF_CAPACITY_UTILIZATION_MARGIN_BRIDGE_WEAK
case_role = counterexample_separator_customer_calloff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 39,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv`:

```text
2024-02-01,39750,40400,39300,40250
2024-02-22,44950,49400,44250,47100
2024-03-07,46200,49500,45400,49500
2024-04-08,36850,36850,34350,35550
2024-08-05,23450,23450,20200,20450
2024-10-25,15950,16100,15390,15510
```

### Backtest

```text
MFE_30D  = +24.53%
MAE_30D  = -2.26%
MFE_90D  = +24.53%
MAE_90D  = -13.58%
MFE_180D = +24.53%
MAE_180D = -61.28%
peak_180 = 49,500 on 2024-03-07
trough_180 = 15,390 on 2024-10-25
peak_to_later_drawdown = -68.91%
```

### Interpretation

This is a classic C12 false-positive shape.  
The early MFE was tradable, but the later drawdown says customer call-off and utilization bridge failed to refresh.

Correct treatment:

```text
separator customer-calloff beta
→ no utilization / shipment / margin bridge
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
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C12_battery_customer_contract_weight = true
do_not_treat_all_customer_contract_MFE_as_Green = true
do_not_convert_calloff_drawdown_to_hard_4C_without_non_price_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE
```

This fine archetype covers:

```text
1. CNT conductive-material customer call-off MFE → Stage2 possible after source repair, lifecycle-managed
2. separator contract exposure without utilization bridge → false Stage2 / local 4B
3. separator call-off exposure without shipment/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CNTConductiveMaterialCustomerCalloffBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should allow battery-material positives when customer contract visibility maps to call-off volume, capacity absorption, shipment cadence and margin bridge. Nano New Material produced large MFE with controlled early MAE, but the later post-peak drawdown requires lifecycle local 4B if customer call-off or margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off volume, capacity absorption, utilization, shipment cadence, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SeparatorCustomerCalloffUtilizationFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not treat separator customer-contract exposure as durable Stage2 unless call-off volume, utilization, pricing and margin bridge refreshes. SK IE Technology had only a small early MFE and then a severe high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off volume, capacity absorption, utilization, shipment cadence, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "case_type": "battery_customer_contract_calloff_risk", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SeparatorCustomerCalloffMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C12 should not treat separator customer-calloff exposure as durable Stage2 unless customer order, utilization, shipment and margin bridge are visible. WCP had tradable MFE but then a deep post-peak drawdown, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer contract, call-off volume, capacity absorption, utilization, shipment cadence, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE", "case_id": "R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage2-Actionable-CNTConductiveMaterialCustomerCalloffBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 95600.0, "evidence_available_at_that_date": "CNT_CONDUCTIVE_MATERIAL_BATTERY_CUSTOMER_CALLOFF_CAPACITY_ABSORPTION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NANO_NEW_MATERIAL_2024_CNT_CONDUCTIVE_BATTERY_CUSTOMER_CALLOFF_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "capacity_absorption_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "shipment_cadence_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["battery_calloff_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 65.06, "MFE_90D_pct": 65.06, "MFE_180D_pct": 65.06, "MAE_30D_pct": -1.46, "MAE_90D_pct": -1.46, "MAE_180D_pct": -28.35, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -56.59, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_calloff_peak_if_customer_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_calloff_collapse_capacity_underutilization_margin_or_financing_break", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C12 should allow battery-material positives when customer contract visibility maps to call-off volume, capacity absorption, shipment cadence and margin bridge. Nano New Material produced large MFE with controlled early MAE, but the later post-peak drawdown requires lifecycle local 4B if customer call-off or margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C12_BATTERY_CALLOFF_121600_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B", "case_id": "R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage2-FalsePositive / SeparatorCustomerCalloffUtilizationFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 73400.0, "evidence_available_at_that_date": "BATTERY_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE_WEAK_REFRESH", "evidence_source": "source_proxy_manual_verification_required:SK_IET_2024_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "capacity_absorption_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "shipment_cadence_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["battery_calloff_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.08, "MFE_90D_pct": 10.08, "MFE_180D_pct": 10.08, "MAE_30D_pct": -11.31, "MAE_90D_pct": -41.83, "MAE_180D_pct": -59.06, "peak_date": "2024-02-02", "peak_price": 80800.0, "drawdown_after_peak_pct": -62.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_calloff_peak_if_customer_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_calloff_collapse_capacity_underutilization_margin_or_financing_break", "trigger_outcome_label": "counterexample_separator_calloff_local4b", "current_profile_verdict": "C12 should not treat separator customer-contract exposure as durable Stage2 unless call-off volume, utilization, pricing and margin bridge refreshes. SK IE Technology had only a small early MFE and then a severe high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_361610_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE", "case_id": "R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_customer_contract_calloff_guardrail", "trigger_type": "Stage2-FalsePositive / SeparatorCustomerCalloffMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 39750.0, "evidence_available_at_that_date": "BATTERY_SEPARATOR_CUSTOMER_CALLOFF_CAPACITY_UTILIZATION_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:WCP_2024_SEPARATOR_CUSTOMER_CALLOFF_UTILIZATION_SHIPMENT_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_contract_or_calloff_candidate", "capacity_absorption_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "shipment_cadence_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["battery_calloff_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.53, "MFE_90D_pct": 24.53, "MFE_180D_pct": 24.53, "MAE_30D_pct": -2.26, "MAE_90D_pct": -13.58, "MAE_180D_pct": -61.28, "peak_date": "2024-03-07", "peak_price": 49500.0, "drawdown_after_peak_pct": -68.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_calloff_peak_if_customer_volume_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_calloff_collapse_capacity_underutilization_margin_or_financing_break", "trigger_outcome_label": "counterexample_separator_customer_calloff_local4b", "current_profile_verdict": "C12 should not treat separator customer-calloff exposure as durable Stage2 unless customer order, utilization, shipment and margin bridge are visible. WCP had tradable MFE but then a deep post-peak drawdown, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C12_BATTERY_CALLOFF_393890_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE", "trigger_id": "TRG_R3L78-C12-121600-NANO-CNT-CUSTOMER-CALLOFF-LIFECYCLE", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 14, "calloff_volume_score": 14, "capacity_absorption_score": 13, "shipment_cadence_score": 12, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 8, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_contract_score": 16, "calloff_volume_score": 16, "capacity_absorption_score": 15, "shipment_cadence_score": 14, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 9, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["customer_contract_score", "calloff_volume_score", "capacity_absorption_score", "shipment_cadence_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract, call-off volume, capacity absorption, shipment cadence and margin bridge; cap battery call-off theme beta when evidence fails to refresh.", "MFE_90D_pct": 65.06, "MAE_90D_pct": -1.46, "score_return_alignment_label": "battery_calloff_positive_with_lifecycle_4b", "current_profile_verdict": "C12 should allow battery-material positives when customer contract visibility maps to call-off volume, capacity absorption, shipment cadence and margin bridge. Nano New Material produced large MFE with controlled early MAE, but the later post-peak drawdown requires lifecycle local 4B if customer call-off or margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B", "trigger_id": "TRG_R3L78-C12-361610-SKIET-SEPARATOR-CALLOFF-LOCAL4B", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_volume_score": 3, "capacity_absorption_score": 2, "shipment_cadence_score": 2, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_volume_score": 1, "capacity_absorption_score": 1, "shipment_cadence_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_volume_score", "capacity_absorption_score", "shipment_cadence_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract, call-off volume, capacity absorption, shipment cadence and margin bridge; cap battery call-off theme beta when evidence fails to refresh.", "MFE_90D_pct": 10.08, "MAE_90D_pct": -41.83, "score_return_alignment_label": "false_positive_battery_calloff_bridge_gap", "current_profile_verdict": "C12 should not treat separator customer-contract exposure as durable Stage2 unless call-off volume, utilization, pricing and margin bridge refreshes. SK IE Technology had only a small early MFE and then a severe high-MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE", "trigger_id": "TRG_R3L78-C12-393890-WCP-SEPARATOR-CUSTOMER-CALLOFF-FADE", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "raw_component_scores_before": {"customer_contract_score": 5, "calloff_volume_score": 3, "capacity_absorption_score": 2, "shipment_cadence_score": 2, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 22, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_contract_score": 3, "calloff_volume_score": 1, "capacity_absorption_score": 1, "shipment_cadence_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_contract_score", "calloff_volume_score", "capacity_absorption_score", "shipment_cadence_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer contract, call-off volume, capacity absorption, shipment cadence and margin bridge; cap battery call-off theme beta when evidence fails to refresh.", "MFE_90D_pct": 24.53, "MAE_90D_pct": -13.58, "score_return_alignment_label": "false_positive_battery_calloff_bridge_gap", "current_profile_verdict": "C12 should not treat separator customer-calloff exposure as durable Stage2 unless customer order, utilization, shipment and margin bridge are visible. WCP had tradable MFE but then a deep post-peak drawdown, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "fine_archetype_id": "BATTERY_MATERIAL_SEPARATOR_CUSTOMER_CALLOFF_MARGIN_BRIDGE_VS_CALLOFF_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "+3 C12 battery material/separator symbols outside top-covered 247540/278280/003670/005070 set, +3 CNT/separator call-off trigger families, +1 call-off lifecycle MFE candidate, +2 separator call-off local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "axis": "battery_material_separator_customer_calloff_margin_bridge_vs_calloff_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C12 should split verified battery customer contract / call-off rerating from generic battery-material or separator beta. Stage2 requires customer contract visibility, call-off volume, capacity absorption, shipment cadence, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["121600", "361610", "393890"], "share_count_validation_required": ["121600"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C12 needs customer call-off and capacity-absorption proof. Nano New Material shows a CNT conductive-material call-off MFE candidate after source repair; SK IE Technology and WCP show separator call-off exposure fading into local 4B when utilization, shipment and margin bridge are absent or stale."}
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
121600:
  name = 나노신소재
  corporate_action_candidate_dates = 2015-12-17
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

361610:
  name = SK아이이테크놀로지
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

393890:
  name = 더블유씨피
  corporate_action_candidate_dates = none
  market_segment = KOSDAQ until 2024-06-13, KOSDAQ GLOBAL from 2024-06-14
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C12 rows are source_proxy_only / evidence_url_pending.
121600 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C12 rule-shape discovery,
but coding-agent promotion requires non-proxy customer contract, call-off volume, capacity absorption, utilization, shipment cadence, pricing and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C12 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 121600 needs share-count validation.

Candidate axis:
battery_material_separator_customer_calloff_margin_bridge_vs_calloff_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 121600, 361610 and 393890.
4. Validate 121600 share-count changes inside the selected window.
5. Keep generic C12 customer-contract/call-off weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer contract / nomination / call-off visibility is explicit,
   - shipment cadence and capacity absorption are visible,
   - utilization and pricing bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is battery customer-contract or separator call-off beta only,
   - call-off/utilization/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, call-off collapse, capacity underutilization, financing or margin break.
9. Emit before/after diagnostics and reject if verified low-MAE customer-calloff positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 78
next_round = R4
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

