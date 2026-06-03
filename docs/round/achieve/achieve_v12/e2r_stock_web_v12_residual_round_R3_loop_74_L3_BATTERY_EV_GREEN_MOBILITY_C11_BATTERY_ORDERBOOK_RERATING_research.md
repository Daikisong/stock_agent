# E2R Stock-Web v12 Residual Research — R3 Loop 74 / L3 / C11

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 74,
  "computed_next_round": "R4",
  "computed_next_loop": 74,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "residual_missed_structural_mining",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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

Previous completed state in this interactive run: R2 / loop 74.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 74
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
computed_next_round = R4
computed_next_loop = 74
```

R3 was routed to C11 because loop 73 already stressed C14 and this loop needs a battery orderbook rerating coverage fill.  
No-Repeat shows C11 is concentrated in a small group of existing battery-cell/material names, so this file tests equipment and CNT material orderbook paths.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C11 coverage is concentrated in:

```text
247540, 003670, 348370, 066970, 373220
```

This run uses three different symbols:

```text
137400 / 피엔티 / battery equipment orderbook bridge
121600 / 나노신소재 / CNT conductive additive orderbook bridge
222080 / 씨아이에스 / battery equipment capex beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
All three selected windows show share-count changes in the price shard and therefore require coding-agent share-count validation before runtime promotion.
```

## Research thesis

C11 is not “battery stock went up.”

The true path is:

```text
battery customer/capex cycle
→ named orderbook or customer qualification
→ delivery or capacity visibility
→ margin/revision bridge
→ durable rerating
```

An orderbook is the warehouse ledger.  
A theme candle is just the forklift horn.

The residual split is:

```text
C11 positive:
  customer/orderbook/delivery bridge
  + controlled early MAE
  + relative strength

C11 false positive:
  equipment/material capex beta
  + no verified orderbook refresh
  + later MAE or post-peak drawdown

C11 local 4B:
  price peak forms before orderbook/margin evidence refreshes
```

---

## Case 1 — Positive with later 4B-watch: 137400 / 피엔티

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is roll-to-roll battery equipment orderbook, customer delivery timing, backlog and margin bridge evidence.

```text
evidence_family = BATTERY_COATER_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-02-20
entry_date = 2024-02-21
entry_price = 41,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv`:

```text
2024-02-21,41600,46700,41150,43500
2024-05-29,53600,62500,53000,60300
2024-06-19,85100,89500,84000,84500
2024-12-27,38300,38450,36750,37350
```

### Backtest

```text
MFE_30D  = +15.87%
MAE_30D  = -4.57%
MFE_90D  = +115.14%
MAE_90D  = -12.74%
MFE_180D = +115.14%
MAE_180D = -12.74%
peak_180 = 89,500 on 2024-06-19
trough_180 = 36,300 on 2024-04-08
peak_to_later_drawdown = -58.94%
```

### Interpretation

This is a strong C11 positive-shaped path.  
The price path says the orderbook bridge may have mattered. But runtime promotion should wait for source repair and share-count validation.

The later drawdown also means C11 needs lifecycle decay:

```text
orderbook bridge verified → Stage2/Green possible
post-peak bridge stale → local 4B-watch
```

---

## Case 2 — Positive with later 4B-watch: 121600 / 나노신소재

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is CNT conductive additive capacity, customer qualification, orderbook and margin bridge evidence.

```text
evidence_family = CNT_CONDUCTIVE_ADDITIVE_BATTERY_CUSTOMER_ORDERBOOK_CAPACITY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_sharecount_validation
trigger_date = 2024-02-20
entry_date = 2024-02-21
entry_price = 105,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv`:

```text
2024-02-21,105000,136300,104100,134000
2024-02-22,133100,157800,130600,138000
2024-06-11,122000,149800,121300,141500
2024-12-09,61800,62500,58800,59100
```

### Backtest

```text
MFE_30D  = +50.29%
MAE_30D  = +0.00%
MFE_90D  = +50.29%
MAE_90D  = -4.57%
MFE_180D = +50.29%
MAE_180D = -44.00%
peak_180 = 157,800 on 2024-02-22
trough_180 = 58,800 on 2024-12-09
peak_to_later_drawdown = -62.74%
```

### Interpretation

This row is the C11 material-orderbook version of a lifecycle winner.  
The entry produced immediate MFE, but the later collapse says the system must not hold a stale Green after the order/customer bridge fades.

---

## Case 3 — Counterexample / local 4B: 222080 / 씨아이에스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests battery equipment / solid-state capex beta without verified orderbook or margin refresh.

```text
evidence_family = BATTERY_ELECTRODE_EQUIPMENT_SOLID_STATE_CAPEX_BETA_WITH_WEAK_ORDERBOOK_MARGIN_REFRESH
case_role = counterexample_with_sharecount_validation
trigger_date = 2024-02-14
entry_date = 2024-02-15
entry_price = 10,140
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv`:

```text
2024-02-15,10140,11590,10000,11000
2024-03-11,13750,15110,13750,14300
2024-07-22,9650,9670,9270,9270
2024-12-09,7600,7700,7050,7050
```

### Backtest

```text
MFE_30D  = +49.01%
MAE_30D  = -1.38%
MFE_90D  = +49.01%
MAE_90D  = -9.66%
MFE_180D = +49.01%
MAE_180D = -30.47%
peak_180 = 15,110 on 2024-03-11
trough_180 = 7,050 on 2024-12-09
peak_to_later_drawdown = -53.34%
```

### Interpretation

This is the C11 false-positive shape.  
The first leg was tradable, but the bridge did not hold. Without non-proxy orderbook/delivery/margin refresh, the correct label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C11_battery_beta_weight = true
do_not_treat_all_battery_equipment_or_material_MFE_as_Green = true
do_not_convert_battery_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE
```

This fine archetype covers:

```text
1. roll-to-roll / coater equipment orderbook bridge → Stage2 possible after source repair
2. CNT conductive additive customer/orderbook bridge → Stage2 possible after source repair
3. battery equipment capex beta without order/margin refresh → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-BatteryEquipmentOrderbookBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy orderbook/customer/delivery/margin evidence and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CNTMaterialOrderbookBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy orderbook/customer/delivery/margin evidence and share-count validation required before runtime promotion."}
{"row_type": "case", "case_id": "R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "symbol": "222080", "company_name": "씨아이에스", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BatteryEquipmentCapexBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row.", "current_profile_verdict": "source_repair_and_sharecount_validation_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy orderbook/customer/delivery/margin evidence and share-count validation required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "case_id": "R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-BatteryEquipmentOrderbookBridge", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 41600.0, "evidence_available_at_that_date": "BATTERY_COATER_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PNT_2024_BATTERY_ROLL_TO_ROLL_EQUIPMENT_ORDERBOOK_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["battery_orderbook_candidate", "customer_capacity_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "orderbook_to_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv", "profile_path": "atlas/symbol_profiles/137/137400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.87, "MFE_90D_pct": 115.14, "MFE_180D_pct": 115.14, "MAE_30D_pct": -4.57, "MAE_90D_pct": -12.74, "MAE_180D_pct": -12.74, "peak_date": "2024-06-19", "peak_price": 89500.0, "drawdown_after_peak_pct": -58.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_137400_2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "case_id": "R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "symbol": "121600", "company_name": "나노신소재", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-CNTMaterialOrderbookBridge", "trigger_date": "2024-02-20", "entry_date": "2024-02-21", "entry_price": 105000.0, "evidence_available_at_that_date": "CNT_CONDUCTIVE_ADDITIVE_BATTERY_CUSTOMER_ORDERBOOK_CAPACITY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NANO_NEW_MATERIALS_2024_CNT_CONDUCTIVE_ADDITIVE_CUSTOMER_ORDERBOOK_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["battery_orderbook_candidate", "customer_capacity_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "orderbook_to_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv", "profile_path": "atlas/symbol_profiles/121/121600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 50.29, "MFE_90D_pct": 50.29, "MFE_180D_pct": 50.29, "MAE_30D_pct": 0.0, "MAE_90D_pct": -4.57, "MAE_180D_pct": -44.0, "peak_date": "2024-02-22", "peak_price": 157800.0, "drawdown_after_peak_pct": -62.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_sharecount_validation", "current_profile_verdict": "C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_121600_2024-02-21", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "case_id": "R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "symbol": "222080", "company_name": "씨아이에스", "round": "R3", "loop": "74", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / BatteryEquipmentCapexBetaFade", "trigger_date": "2024-02-14", "entry_date": "2024-02-15", "entry_price": 10140.0, "evidence_available_at_that_date": "BATTERY_ELECTRODE_EQUIPMENT_SOLID_STATE_CAPEX_BETA_WITH_WEAK_ORDERBOOK_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:CIS_2024_BATTERY_ELECTRODE_EQUIPMENT_SOLID_STATE_CAPEX_ORDERBOOK_MARGIN_REFRESH", "stage2_evidence_fields": ["battery_orderbook_candidate", "customer_capacity_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "orderbook_to_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/222/222080/2024.csv", "profile_path": "atlas/symbol_profiles/222/222080.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 49.01, "MFE_90D_pct": 49.01, "MFE_180D_pct": 49.01, "MAE_30D_pct": -1.38, "MAE_90D_pct": -9.66, "MAE_180D_pct": -30.47, "peak_date": "2024-03-11", "peak_price": 15110.0, "drawdown_after_peak_pct": -53.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_or_margin_break", "trigger_outcome_label": "counterexample_with_sharecount_validation", "current_profile_verdict": "C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_222080_2024-02-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "trigger_id": "TRG_R3L74-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-BRIDGE", "symbol": "137400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 14, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 11, "valuation_repricing_score": 12, "execution_risk_score": 5, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 16, "margin_bridge_score": 13, "revision_score": 11, "relative_strength_score": 15, "customer_quality_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_cb_risk_score": 6, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Yellow/Green candidate after source repair + lifecycle 4B", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified battery orderbook/customer/delivery bridge; cap equipment/material capex beta when order/margin evidence fails to refresh and share-count validation is unresolved.", "MFE_90D_pct": 115.14, "MAE_90D_pct": -12.74, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C11 should allow Stage2 when equipment orderbook and delivery-slot visibility convert into margin/revision bridge. PNT produced very high MFE after the trigger, but later post-peak drawdown and an in-window share-count change require lifecycle local 4B and coding-agent validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "trigger_id": "TRG_R3L74-C11-121600-NANO-CNT-MATERIAL-ORDERBOOK-BRIDGE", "symbol": "121600", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 12, "backlog_visibility_score": 14, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 16, "customer_quality_score": 11, "valuation_repricing_score": 12, "execution_risk_score": 5, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 14, "backlog_visibility_score": 16, "margin_bridge_score": 13, "revision_score": 11, "relative_strength_score": 15, "customer_quality_score": 12, "valuation_repricing_score": 11, "execution_risk_score": 5, "dilution_cb_risk_score": 6, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Yellow/Green candidate after source repair + lifecycle 4B", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified battery orderbook/customer/delivery bridge; cap equipment/material capex beta when order/margin evidence fails to refresh and share-count validation is unresolved.", "MFE_90D_pct": 50.29, "MAE_90D_pct": -4.57, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C11 should include battery material orderbook rerating when CNT additive capacity, customer qualification, order visibility and margin bridge are visible. Nano New Materials had a strong event-window MFE, but the later 2024 collapse shows lifecycle local 4B is necessary if customer/order evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "trigger_id": "TRG_R3L74-C11-222080-CIS-EQUIPMENT-CAPEX-BETA-FADE", "symbol": "222080", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"contract_score": 4, "backlog_visibility_score": 5, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 9, "customer_quality_score": 4, "valuation_repricing_score": 6, "execution_risk_score": 15, "dilution_cb_risk_score": 3, "accounting_trust_risk_score": 0}, "weighted_score_before": 55, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 3, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 3, "valuation_repricing_score": 5, "execution_risk_score": 18, "dilution_cb_risk_score": 6, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score", "dilution_cb_risk_score"], "component_delta_explanation": "Reward only verified battery orderbook/customer/delivery bridge; cap equipment/material capex beta when order/margin evidence fails to refresh and share-count validation is unresolved.", "MFE_90D_pct": 49.01, "MAE_90D_pct": -9.66, "score_return_alignment_label": "false_positive_orderbook_bridge_gap", "current_profile_verdict": "C11 should not treat battery equipment or solid-state capex beta as durable Stage2 unless orderbook, delivery, customer or margin evidence refreshes. CIS generated a sharp MFE but later gave it back and opened large MAE, making it a false Stage2 / local 4B-watch row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_CNT_ORDERBOOK_BRIDGE_VS_CAPEX_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C11 battery equipment/material symbols, +3 orderbook/CNT/equipment-capex trigger families, +2 orderbook positives, +1 capex-beta fade counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "axis": "battery_equipment_cnt_orderbook_bridge_vs_capex_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C11 should split verified battery equipment/material orderbook rerating from capex beta. Stage2 requires named customer, orderbook, delivery visibility, capacity qualification, or margin bridge. If price MFE is followed by stale bridge evidence and large post-peak drawdown, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["137400", "121600", "222080"], "share_count_validation_required": ["137400", "121600", "222080"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 74, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C11 needs orderbook bridge proof. PNT and Nano New Materials show battery equipment/CNT orderbook positives with later lifecycle drawdown; CIS shows battery equipment capex beta fading into local 4B when order/margin refresh fails."}
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
137400:
  corporate_action_candidate_dates = 2012-11-30, 2012-12-26, 2019-05-07, 2019-05-30
  selected window = 2024-02-21~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

121600:
  corporate_action_candidate_dates = 2015-12-17
  selected window = 2024-02-21~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

222080:
  corporate_action_candidate_dates = 2017-01-20
  selected window = 2024-02-15~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C11 rows are source_proxy_only / evidence_url_pending.
All three also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C11 rule-shape discovery,
but coding-agent promotion requires non-proxy orderbook, customer, delivery, capacity and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C11 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and share-count validation.

Candidate axis:
battery_equipment_cnt_orderbook_bridge_vs_capex_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 137400, 121600 and 222080.
4. Validate share-count changes inside each selected window.
5. Keep generic C11 battery beta weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer/orderbook/delivery evidence is explicit,
   - capacity or qualification bridge is visible,
   - margin/revision bridge exists,
   - MAE remains controlled.
7. Consider local 4B-watch when:
   - the trigger is equipment/material capex beta only,
   - orderbook or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, customer loss, utilization collapse, or margin-break evidence.
9. Emit before/after diagnostics and reject if verified orderbook positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 74
next_round = R4
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

