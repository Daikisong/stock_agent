# E2R Stock-Web v12 Residual Research — R3 Loop 77 / L3 / C11

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 77,
  "computed_next_round": "R4",
  "computed_next_loop": 77,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_orderbook_margin_guardrail",
    "component_material_bridge_vs_theme_beta",
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

Previous completed state in this interactive run: R2 / loop 77.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 77
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
computed_next_round = R4
computed_next_loop = 77
```

R3 was routed to C11 because loop 76 used C13, and the visible no-repeat slice shows C11 concentration in a few cell/material names.  
This file tests battery material/component orderbook and margin bridge behavior rather than JV/utilization/AMPC policy beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C11 is concentrated in:

```text
247540, 003670, 348370, 066970, 373220
```

This run uses three different symbols:

```text
078600 / 대주전자재료 / silicon-anode customer orderbook and margin bridge
002710 / TCC스틸 / battery-can material orderbook lifecycle
006110 / 삼아알미늄 / aluminum-foil orderbook theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C11 is not “배터리 소재주가 올랐다.”

The mechanism must pass through:

```text
customer orderbook / contract visibility
→ call-off volume and capacity absorption
→ price pass-through / utilization
→ margin conversion
→ durable rerating
```

배터리 소재의 수주 스토리는 창고에 쌓인 원재료가 아니다.  
진짜 C11은 주문서가 출하량, 가동률, 단가, 마진으로 변할 때 살아난다.

---

## Case 1 — Positive with lifecycle 4B: 078600 / 대주전자재료

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is silicon-anode customer orderbook, call-off, capacity ramp, utilization and margin bridge evidence.

```text
evidence_family = SILICON_ANODE_BATTERY_CUSTOMER_ORDERBOOK_CAPA_RAMP_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-20
entry_date = 2024-02-21
entry_price = 70,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv`:

```text
2024-02-21,70300,77300,70100,76000
2024-03-25,97000,102000,95200,102000
2024-07-31,115000,119800,114800,117600
2024-08-16,128700,129400,121600,122200
2024-09-09,90300,93200,89400,93200
```

### Backtest

```text
MFE_30D  = +45.09%
MAE_30D  = -0.28%
MFE_90D  = +45.09%
MAE_90D  = -0.28%
MFE_180D = +84.07%
MAE_180D = -0.28%
peak_180 = 129,400 on 2024-08-16
trough_180 = 70,100 on 2024-02-21
peak_to_later_drawdown = -30.91%
```

### Interpretation

This is a clean C11 positive-shaped path.  
The entry-basis MAE was almost zero and the MFE expanded over months.

Correct treatment:

```text
verified customer orderbook / capacity ramp / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 002710 / TCC스틸

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is battery can / nickel-plated steel customer orderbook, capacity ramp, quality approval and margin evidence.

```text
evidence_family = BATTERY_CAN_NICKEL_PLATED_STEEL_CUSTOMER_ORDERBOOK_CAPA_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 49,450
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv`:

```text
2024-02-01,49450,50200,47500,49650
2024-02-21,79300,85900,76900,82200
2024-05-29,46500,47950,44400,46300
2024-06-11,56800,61700,55800,61000
2024-08-05,33500,34100,27000,29300
```

### Backtest

```text
MFE_30D  = +73.71%
MAE_30D  = -3.94%
MFE_90D  = +73.71%
MAE_90D  = -10.21%
MFE_180D = +73.71%
MAE_180D = -45.40%
peak_180 = 85,900 on 2024-02-21
trough_180 = 27,000 on 2024-08-05
peak_to_later_drawdown = -68.57%
```

### Interpretation

This is a C11 lifecycle winner, not permanent Green.  
The MFE was strong, but the later drawdown shows why orderbook and margin evidence must refresh.

Correct treatment:

```text
battery-can orderbook bridge verified → Stage2 possible
bridge stale + high MAE → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 006110 / 삼아알미늄

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests battery aluminum-foil orderbook/theme beta without enough call-off, utilization and margin evidence.

```text
evidence_family = BATTERY_ALUMINUM_FOIL_ORDERBOOK_THEME_WITH_WEAK_CUSTOMER_CALLOFF_MARGIN_BRIDGE
case_role = counterexample_orderbook_material_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 86,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv`:

```text
2024-02-01,86500,88000,84800,86500
2024-02-21,110600,116400,110000,110700
2024-04-08,76400,79900,73800,78900
2024-07-18,42600,42900,41300,42000
2024-08-05,48100,49000,39600,42000
```

### Backtest

```text
MFE_30D  = +34.57%
MAE_30D  = -7.28%
MFE_90D  = +34.57%
MAE_90D  = -40.35%
MFE_180D = +34.57%
MAE_180D = -54.22%
peak_180 = 116,400 on 2024-02-21
trough_180 = 39,600 on 2024-08-05
peak_to_later_drawdown = -65.98%
```

### Interpretation

This is the C11 false-positive boundary.  
The first MFE was tradable, but it did not prove durable orderbook rerating.

Correct treatment:

```text
battery foil / material orderbook beta
→ no verified call-off / utilization / margin bridge
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
do_not_raise_generic_C11_battery_material_weight = true
do_not_treat_all_battery_orderbook_MFE_as_Green = true
do_not_convert_material_drawdown_to_hard_4C_without_non_price_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE
```

This fine archetype covers:

```text
1. silicon-anode customer/capacity/margin bridge → Stage2 possible after source repair
2. battery-can material orderbook/capacity bridge → Stage2 possible, lifecycle-managed
3. aluminum-foil material beta without call-off/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-SiliconAnodeCustomerOrderbookMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should allow battery-material orderbook Stage2 when a silicon-anode customer ramp, call-off/orderbook, capacity absorption and margin bridge are visible. Daejoo Electronic Materials produced high MFE with almost no entry-basis MAE; post-peak drawdown still requires lifecycle local 4B if orderbook/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, call-off, capacity ramp, utilization, price pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BatteryCanMaterialOrderbookBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 can include battery-can/component material names when customer orderbook, capacity ramp, quality approval and margin bridge are visible. TCC Steel produced very large early MFE, but the later high-MAE collapse says C11 must lifecycle-manage the signal and activate local 4B when orderbook/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, call-off, capacity ramp, utilization, price pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AluminumFoilOrderbookThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should not treat battery aluminum-foil or component-material beta as durable Stage2 unless customer call-off, contracted volume, utilization, price pass-through and margin evidence refreshes. Sama Aluminum had a strong MFE but later opened a very large MAE path, making it local 4B rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, call-off, capacity ramp, utilization, price pass-through and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "case_id": "R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "symbol": "078600", "company_name": "대주전자재료", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_margin_guardrail", "trigger_type": "Stage2-Actionable-SiliconAnodeCustomerOrderbookMarginBridge", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 70300.0, "evidence_available_at_that_date": "SILICON_ANODE_BATTERY_CUSTOMER_ORDERBOOK_CAPA_RAMP_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DAEJOO_2024_SILICON_ANODE_CUSTOMER_ORDERBOOK_CAPA_RAMP_MARGIN_BRIDGE", "stage2_evidence_fields": ["battery_customer_orderbook_candidate", "capacity_ramp_or_calloff_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_price_pass_through_candidate"], "stage4b_evidence_fields": ["material_orderbook_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/078/078600/2024.csv", "profile_path": "atlas/symbol_profiles/078/078600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.09, "MFE_90D_pct": 45.09, "MFE_180D_pct": 84.07, "MAE_30D_pct": -0.28, "MAE_90D_pct": -0.28, "MAE_180D_pct": -0.28, "peak_date": "2024-08-16", "peak_price": 129400.0, "drawdown_after_peak_pct": -30.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C11 should allow battery-material orderbook Stage2 when a silicon-anode customer ramp, call-off/orderbook, capacity absorption and margin bridge are visible. Daejoo Electronic Materials produced high MFE with almost no entry-basis MAE; post-peak drawdown still requires lifecycle local 4B if orderbook/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_078600_2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "case_id": "R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "symbol": "002710", "company_name": "TCC스틸", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_margin_guardrail", "trigger_type": "Stage2-Actionable-BatteryCanMaterialOrderbookBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 49450.0, "evidence_available_at_that_date": "BATTERY_CAN_NICKEL_PLATED_STEEL_CUSTOMER_ORDERBOOK_CAPA_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TCC_STEEL_2024_BATTERY_CAN_MATERIAL_CUSTOMER_ORDERBOOK_CAPA_MARGIN_BRIDGE", "stage2_evidence_fields": ["battery_customer_orderbook_candidate", "capacity_ramp_or_calloff_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_price_pass_through_candidate"], "stage4b_evidence_fields": ["material_orderbook_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002710/2024.csv", "profile_path": "atlas/symbol_profiles/002/002710.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 73.71, "MFE_90D_pct": 73.71, "MFE_180D_pct": 73.71, "MAE_30D_pct": -3.94, "MAE_90D_pct": -10.21, "MAE_180D_pct": -45.4, "peak_date": "2024-02-21", "peak_price": 85900.0, "drawdown_after_peak_pct": -68.57, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C11 can include battery-can/component material names when customer orderbook, capacity ramp, quality approval and margin bridge are visible. TCC Steel produced very large early MFE, but the later high-MAE collapse says C11 must lifecycle-manage the signal and activate local 4B when orderbook/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_002710_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "case_id": "R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "symbol": "006110", "company_name": "삼아알미늄", "round": "R3", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_margin_guardrail", "trigger_type": "Stage2-FalsePositive / AluminumFoilOrderbookThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 86500.0, "evidence_available_at_that_date": "BATTERY_ALUMINUM_FOIL_ORDERBOOK_THEME_WITH_WEAK_CUSTOMER_CALLOFF_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SAMA_ALUMINUM_2024_BATTERY_FOIL_CUSTOMER_CALLOFF_ORDERBOOK_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["battery_customer_orderbook_candidate", "capacity_ramp_or_calloff_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_price_pass_through_candidate"], "stage4b_evidence_fields": ["material_orderbook_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006110/2024.csv", "profile_path": "atlas/symbol_profiles/006/006110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.57, "MFE_90D_pct": 34.57, "MFE_180D_pct": 34.57, "MAE_30D_pct": -7.28, "MAE_90D_pct": -40.35, "MAE_180D_pct": -54.22, "peak_date": "2024-02-21", "peak_price": 116400.0, "drawdown_after_peak_pct": -65.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_calloff_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_order_cut_utilization_margin_or_financing_break", "trigger_outcome_label": "counterexample_orderbook_material_beta_local4b", "current_profile_verdict": "C11 should not treat battery aluminum-foil or component-material beta as durable Stage2 unless customer call-off, contracted volume, utilization, price pass-through and margin evidence refreshes. Sama Aluminum had a strong MFE but later opened a very large MAE path, making it local 4B rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_006110_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "trigger_id": "TRG_R3L77-C11-078600-DAEJOO-SILICON-ANODE-ORDERBOOK-MARGIN", "symbol": "078600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 14, "calloff_volume_score": 13, "capacity_absorption_score": 13, "price_pass_through_score": 11, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_orderbook_score": 16, "calloff_volume_score": 15, "capacity_absorption_score": 15, "price_pass_through_score": 13, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["customer_orderbook_score", "calloff_volume_score", "capacity_absorption_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified battery customer orderbook, call-off volume, capacity absorption, price pass-through and margin bridge; cap material/component theme beta when evidence fails to refresh.", "MFE_90D_pct": 45.09, "MAE_90D_pct": -0.28, "score_return_alignment_label": "battery_orderbook_positive_with_lifecycle_4b", "current_profile_verdict": "C11 should allow battery-material orderbook Stage2 when a silicon-anode customer ramp, call-off/orderbook, capacity absorption and margin bridge are visible. Daejoo Electronic Materials produced high MFE with almost no entry-basis MAE; post-peak drawdown still requires lifecycle local 4B if orderbook/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "trigger_id": "TRG_R3L77-C11-002710-TCCSTEEL-BATTERY-CAN-MATERIAL-ORDERBOOK-LIFECYCLE", "symbol": "002710", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 14, "calloff_volume_score": 13, "capacity_absorption_score": 13, "price_pass_through_score": 11, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_orderbook_score": 16, "calloff_volume_score": 15, "capacity_absorption_score": 15, "price_pass_through_score": 13, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["customer_orderbook_score", "calloff_volume_score", "capacity_absorption_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified battery customer orderbook, call-off volume, capacity absorption, price pass-through and margin bridge; cap material/component theme beta when evidence fails to refresh.", "MFE_90D_pct": 73.71, "MAE_90D_pct": -10.21, "score_return_alignment_label": "battery_orderbook_positive_with_lifecycle_4b", "current_profile_verdict": "C11 can include battery-can/component material names when customer orderbook, capacity ramp, quality approval and margin bridge are visible. TCC Steel produced very large early MFE, but the later high-MAE collapse says C11 must lifecycle-manage the signal and activate local 4B when orderbook/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "trigger_id": "TRG_R3L77-C11-006110-SAMA-ALUMINUM-FOIL-ORDERBOOK-THEME-FADE", "symbol": "006110", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 5, "calloff_volume_score": 3, "capacity_absorption_score": 3, "price_pass_through_score": 2, "margin_bridge_score": 2, "relative_strength_score": 8, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_orderbook_score": 3, "calloff_volume_score": 2, "capacity_absorption_score": 1, "price_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_orderbook_score", "calloff_volume_score", "capacity_absorption_score", "price_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified battery customer orderbook, call-off volume, capacity absorption, price pass-through and margin bridge; cap material/component theme beta when evidence fails to refresh.", "MFE_90D_pct": 34.57, "MAE_90D_pct": -40.35, "score_return_alignment_label": "false_positive_battery_material_bridge_gap", "current_profile_verdict": "C11 should not treat battery aluminum-foil or component-material beta as durable Stage2 unless customer call-off, contracted volume, utilization, price pass-through and margin evidence refreshes. Sama Aluminum had a strong MFE but later opened a very large MAE path, making it local 4B rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_MATERIAL_COMPONENT_ORDERBOOK_CAPA_MARGIN_BRIDGE_VS_MATERIAL_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C11 battery-material/component symbols outside top-covered 247540/003670/348370/066970/373220 set, +3 silicon-anode/battery-can/aluminum-foil trigger families, +2 orderbook positives, +1 material beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "axis": "battery_material_component_orderbook_CAPA_margin_bridge_vs_material_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C11 should split verified battery material/component orderbook rerating from battery-material theme beta. Stage2 requires customer orderbook, call-off volume, capacity absorption, price pass-through and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["078600", "002710", "006110"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C11 needs customer orderbook/call-off/margin proof. Daejoo Electronic Materials and TCC Steel show battery-material/component orderbook MFE after source repair; Sama Aluminum shows aluminum-foil orderbook theme fading into local 4B when call-off/utilization/margin bridge is absent."}
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
078600:
  corporate_action_candidate_dates = none
  selected window = 2024-02-21~D+180
  contamination = false

002710:
  corporate_action_candidate_dates = 2009-05-08
  selected window = 2024-02-01~D+180
  contamination = false

006110:
  corporate_action_candidate_dates = 2000-10-16, 2000-11-14, 2007-05-04, 2011-04-26, 2023-02-09
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C11 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C11 rule-shape discovery,
but coding-agent promotion requires non-proxy customer orderbook, call-off, capacity ramp, utilization, price pass-through and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C11 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
battery_material_component_orderbook_CAPA_margin_bridge_vs_material_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 078600, 002710 and 006110.
4. Keep generic C11 battery-orderbook weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer orderbook or contract visibility is explicit,
   - call-off volume or capacity absorption is visible,
   - price pass-through / utilization / margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is battery-material/component theme beta only,
   - orderbook/call-off/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, order cut, call-off collapse, utilization collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified battery orderbook/margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 77
next_round = R4
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

