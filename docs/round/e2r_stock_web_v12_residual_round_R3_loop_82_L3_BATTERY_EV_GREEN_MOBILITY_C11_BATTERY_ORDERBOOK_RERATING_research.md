# E2R Stock-Web v12 Residual Research — R3 Loop 82 / L3 / C11

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 82,
  "computed_next_round": "R4",
  "computed_next_loop": 82,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING",
  "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "battery_orderbook_rerating_guardrail",
    "battery_equipment_customer_order_delivery_revenue_margin_bridge",
    "battery_equipment_theme_fade_boundary",
    "share_count_validation_queue_creation",
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

Previous completed state in this interactive run: R2 / loop 82.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 82
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
computed_next_round = R4
computed_next_loop = 82
```

R3 was routed to C11 because loop 82 R2 used C09, loop 81 R3 used C13, and loop 80 R3 used C12.  
This file tests battery equipment/material orderbook rerating rather than C12 call-off risk or C13 AMPC/IRA utilization.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C11 concentration in:

```text
247540, 003670, 393890, 348370, 066970, 222080
```

This run uses three different symbols:

```text
137400 / 피엔티 / battery equipment orderbook lifecycle
299030 / 하나기술 / battery equipment orderbook theme fade
114190 / 강원에너지 / battery material/equipment theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
137400 and 299030 show share-count changes inside the selected 2024 shard and require coding-agent validation before runtime promotion.
```

## Research thesis

C11 is not “2차전지 장비주가 올랐다.”

The mechanism must pass through:

```text
battery capex / equipment / material headline
→ customer orderbook
→ delivery schedule and backlog conversion
→ revenue recognition
→ margin bridge
→ durable rerating
```

배터리 장비주는 공장 사진이 아니라 납품표다.  
C11이 보려는 것은 headline이 실제 고객 발주, 납기, 매출, 마진으로 컨베이어벨트를 타고 들어오는지다.

---

## Case 1 — Battery equipment orderbook lifecycle candidate: 137400 / 피엔티

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is customer orderbook, delivery schedule, capacity/backlog conversion, revenue recognition and margin bridge evidence.

```text
evidence_family = BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_CAPACITY_REVENUE_MARGIN_BRIDGE
case_role = positive_battery_equipment_orderbook_lifecycle_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 35,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv`:

```text
2024-02-01,35800,36400,35000,36250
2024-02-21,41600,46700,41150,43500
2024-03-06,47500,48200,45200,45900
2024-05-29,53600,62500,53000,60300
2024-06-13,83000,85000,79900,83500
2024-06-19,85100,89500,84000,84500
2024-08-05,51100,53400,45950,49200
2024-10-10,63500,64100,60700,61500
```

### Backtest

```text
MFE_30D  = +34.64%
MAE_30D  = -2.23%
MFE_90D  = +137.43%
MAE_90D  = -2.23%
MFE_180D = +150.00%
MAE_180D = -2.23%
peak_180 = 89,500 on 2024-06-19
trough_180 = 35,000 on 2024-02-01
peak_to_later_drawdown = -48.66%
```

### Interpretation

This is a strong C11 orderbook lifecycle candidate.  
The MFE was very large and entry-basis MAE was shallow, but share-count validation and non-price orderbook evidence are needed.

Correct treatment:

```text
verified customer orderbook / delivery / revenue / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 299030 / 하나기술

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests battery equipment orderbook theme beta without enough delivery/revenue/margin bridge.

```text
evidence_family = BATTERY_EQUIPMENT_ORDERBOOK_THEME_WITH_WEAK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = counterexample_battery_equipment_orderbook_theme_local4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 52,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv`:

```text
2024-02-01,52700,53100,51200,52800
2024-02-21,59100,65000,58100,62300
2024-03-08,64000,73100,61400,67200
2024-05-03,60800,67700,60700,64700
2024-06-12,62800,64900,60700,61500
2024-06-24,49050,49600,40550,41150
2024-08-05,30150,30550,24350,25450
2024-10-25,27800,28150,26900,27250
```

### Backtest

```text
MFE_30D  = +38.71%
MAE_30D  = -2.85%
MFE_90D  = +38.71%
MAE_90D  = -5.79%
MFE_180D = +38.71%
MAE_180D = -53.80%
peak_180 = 73,100 on 2024-03-08
trough_180 = 24,350 on 2024-08-05
peak_to_later_drawdown = -66.69%
```

### Interpretation

This is a C11 false-positive / local-4B boundary.  
The early MFE was tradable, but it did not become durable orderbook/revenue/margin rerating.

Correct treatment:

```text
battery equipment orderbook theme beta
→ no verified customer order / delivery / revenue / margin bridge
→ local 4B-watch
→ share-count validation before runtime ingestion
```

---

## Case 3 — Counterexample / local 4B: 114190 / 강원에너지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests battery material/equipment theme beta without enough direct order/revenue/margin bridge.

```text
evidence_family = BATTERY_MATERIAL_EQUIPMENT_THEME_WITH_WEAK_DIRECT_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_battery_material_equipment_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 12,910
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/114/114190/2024.csv`:

```text
2024-02-01,12910,13140,12750,13140
2024-02-14,13150,14980,13130,14050
2024-02-21,16000,18490,15700,17000
2024-02-28,19900,21850,19600,20700
2024-03-19,21300,21950,20250,20700
2024-08-05,12170,12300,10320,10610
2024-09-09,10280,10980,10280,10840
2024-10-07,12800,15120,12750,14700
```

### Backtest

```text
MFE_30D  = +69.25%
MAE_30D  = -3.95%
MFE_90D  = +70.02%
MAE_90D  = -3.95%
MFE_180D = +70.02%
MAE_180D = -20.37%
peak_180 = 21,950 on 2024-03-19
trough_180 = 10,280 on 2024-09-09~2024-09-11
peak_to_later_drawdown = -53.17%
```

### Interpretation

This is a C11 battery material/equipment theme-fade row.  
The early MFE was strong, but the bridge to durable direct order and margin economics is unresolved.

Correct treatment:

```text
battery material/equipment theme beta
→ no verified customer order / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
battery_orderbook_delivery_revenue_margin_bridge_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C11_battery_equipment_weight = true
do_not_treat_all_battery_equipment_MFE_as_Green = true
do_not_ingest_sharecount_changed_orderbook_rows_without_validation = true
do_not_convert_battery_equipment_drawdown_to_hard_4C_without_non_price_order_delivery_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE
```

This fine archetype covers:

```text
1. battery equipment orderbook / delivery bridge → Stage2 possible after source repair
2. battery equipment theme beta without delivery/revenue bridge → false Stage2 / local 4B
3. battery material/equipment theme beta without direct order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-BatteryEquipmentOrderbookDeliveryRevenueBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should protect battery equipment orderbook positives only when customer orderbook, delivery schedule, capacity utilization, revenue recognition and margin bridge are visible. PNT produced very large MFE with shallow entry-basis MAE, but stock-web shard shows share-count movement and post-peak drawdown requires lifecycle 4B discipline.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE", "symbol": "299030", "company_name": "하나기술", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BatteryEquipmentOrderbookThemeFadeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should not treat battery equipment orderbook theme beta as durable Stage2 unless customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Hana Technology had a sharp early MFE, then severe high-MAE fade and share-count changes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE", "symbol": "114190", "company_name": "강원에너지", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "case_type": "battery_orderbook_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / BatteryMaterialEquipmentThemeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C11 should not treat battery material/equipment theme beta as durable orderbook rerating unless direct customer order, material supply volume, delivery, revenue and margin bridge are visible. Kangwon Energy had strong early MFE but then high MAE and post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE", "case_id": "R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE", "symbol": "137400", "company_name": "피엔티", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail", "trigger_type": "Stage2-Lifecycle-BatteryEquipmentOrderbookDeliveryRevenueBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 35800.0, "evidence_available_at_that_date": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_CAPACITY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PNT_2024_BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_orderbook_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capacity_or_backlog_conversion_candidate"], "stage4b_evidence_fields": ["battery_equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/137/137400/2024.csv", "profile_path": "atlas/symbol_profiles/137/137400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 34.64, "MFE_90D_pct": 137.43, "MFE_180D_pct": 150.0, "MAE_30D_pct": -2.23, "MAE_90D_pct": -2.23, "MAE_180D_pct": -2.23, "peak_date": "2024-06-19", "peak_price": 89500.0, "drawdown_after_peak_pct": -48.66, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_customer_order_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_battery_equipment_orderbook_lifecycle_with_sharecount_validation", "current_profile_verdict": "C11 should protect battery equipment orderbook positives only when customer orderbook, delivery schedule, capacity utilization, revenue recognition and margin bridge are visible. PNT produced very large MFE with shallow entry-basis MAE, but stock-web shard shows share-count movement and post-peak drawdown requires lifecycle 4B discipline.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_137400_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE", "case_id": "R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE", "symbol": "299030", "company_name": "하나기술", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail", "trigger_type": "Stage2-FalsePositive / BatteryEquipmentOrderbookThemeFadeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 52700.0, "evidence_available_at_that_date": "BATTERY_EQUIPMENT_ORDERBOOK_THEME_WITH_WEAK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANA_TECHNOLOGY_2024_BATTERY_EQUIPMENT_ORDERBOOK_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_orderbook_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capacity_or_backlog_conversion_candidate"], "stage4b_evidence_fields": ["battery_equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/299/299030/2024.csv", "profile_path": "atlas/symbol_profiles/299/299030.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 38.71, "MFE_90D_pct": 38.71, "MFE_180D_pct": 38.71, "MAE_30D_pct": -2.85, "MAE_90D_pct": -5.79, "MAE_180D_pct": -53.8, "peak_date": "2024-03-08", "peak_price": 73100.0, "drawdown_after_peak_pct": -66.69, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_customer_order_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_battery_equipment_orderbook_theme_local4b_with_sharecount_validation", "current_profile_verdict": "C11 should not treat battery equipment orderbook theme beta as durable Stage2 unless customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Hana Technology had a sharp early MFE, then severe high-MAE fade and share-count changes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_299030_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE", "case_id": "R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE", "symbol": "114190", "company_name": "강원에너지", "round": "R3", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|battery_orderbook_rerating_guardrail", "trigger_type": "Stage2-FalsePositive / BatteryMaterialEquipmentThemeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 12910.0, "evidence_available_at_that_date": "BATTERY_MATERIAL_EQUIPMENT_THEME_WITH_WEAK_DIRECT_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KANGWON_ENERGY_2024_BATTERY_MATERIAL_EQUIPMENT_CUSTOMER_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_orderbook_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "capacity_or_backlog_conversion_candidate"], "stage4b_evidence_fields": ["battery_equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/114/114190/2024.csv", "profile_path": "atlas/symbol_profiles/114/114190.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 69.25, "MFE_90D_pct": 70.02, "MFE_180D_pct": 70.02, "MAE_30D_pct": -3.95, "MAE_90D_pct": -3.95, "MAE_180D_pct": -20.37, "peak_date": "2024-03-19", "peak_price": 21950.0, "drawdown_after_peak_pct": -53.17, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_battery_orderbook_peak_if_customer_order_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_battery_material_equipment_theme_local4b", "current_profile_verdict": "C11 should not treat battery material/equipment theme beta as durable orderbook rerating unless direct customer order, material supply volume, delivery, revenue and margin bridge are visible. Kangwon Energy had strong early MFE but then high MAE and post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C11_BATTERY_ORDERBOOK_114190_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE", "trigger_id": "TRG_R3L82-C11-137400-PNT-BATTERY-EQUIPMENT-ORDERBOOK-LIFECYCLE", "symbol": "137400", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 14, "delivery_schedule_score": 13, "capacity_backlog_conversion_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 14, "sharecount_validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair and validation", "raw_component_scores_after": {"customer_orderbook_score": 16, "delivery_schedule_score": 15, "capacity_backlog_conversion_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 13, "sharecount_validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_orderbook_score", "delivery_schedule_score", "capacity_backlog_conversion_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge; cap battery-equipment or battery-material theme beta when bridge fails to refresh.", "MFE_90D_pct": 137.43, "MAE_90D_pct": -2.23, "score_return_alignment_label": "battery_orderbook_positive_with_lifecycle_4b", "current_profile_verdict": "C11 should protect battery equipment orderbook positives only when customer orderbook, delivery schedule, capacity utilization, revenue recognition and margin bridge are visible. PNT produced very large MFE with shallow entry-basis MAE, but stock-web shard shows share-count movement and post-peak drawdown requires lifecycle 4B discipline."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE", "trigger_id": "TRG_R3L82-C11-299030-HANA-TECH-BATTERY-EQUIPMENT-ORDERBOOK-FADE", "symbol": "299030", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 4, "delivery_schedule_score": 3, "capacity_backlog_conversion_score": 3, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 7, "sharecount_validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_orderbook_score": 2, "delivery_schedule_score": 1, "capacity_backlog_conversion_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 5, "sharecount_validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_orderbook_score", "delivery_schedule_score", "capacity_backlog_conversion_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge; cap battery-equipment or battery-material theme beta when bridge fails to refresh.", "MFE_90D_pct": 38.71, "MAE_90D_pct": -5.79, "score_return_alignment_label": "false_positive_battery_orderbook_theme_bridge_gap", "current_profile_verdict": "C11 should not treat battery equipment orderbook theme beta as durable Stage2 unless customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Hana Technology had a sharp early MFE, then severe high-MAE fade and share-count changes."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE", "trigger_id": "TRG_R3L82-C11-114190-KANGWON-ENERGY-BATTERY-MATERIAL-EQUIPMENT-THEME-FADE", "symbol": "114190", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "raw_component_scores_before": {"customer_orderbook_score": 4, "delivery_schedule_score": 3, "capacity_backlog_conversion_score": 3, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 14, "sharecount_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_orderbook_score": 2, "delivery_schedule_score": 1, "capacity_backlog_conversion_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 5, "sharecount_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_orderbook_score", "delivery_schedule_score", "capacity_backlog_conversion_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge; cap battery-equipment or battery-material theme beta when bridge fails to refresh.", "MFE_90D_pct": 70.02, "MAE_90D_pct": -3.95, "score_return_alignment_label": "false_positive_battery_orderbook_theme_bridge_gap", "current_profile_verdict": "C11 should not treat battery material/equipment theme beta as durable orderbook rerating unless direct customer order, material supply volume, delivery, revenue and margin bridge are visible. Kangwon Energy had strong early MFE but then high MAE and post-peak drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "fine_archetype_id": "BATTERY_EQUIPMENT_ORDERBOOK_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_VS_EQUIPMENT_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 1, "diversity_score_summary": "+3 C11 battery-orderbook symbols outside top-covered 247540/003670/393890/348370/066970 set, +3 PNT/Hana/Kangwon equipment-material trigger families, +1 orderbook lifecycle positive, +2 equipment/material theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "axis": "battery_equipment_orderbook_customer_delivery_revenue_margin_bridge_vs_equipment_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C11 should split verified battery equipment/material orderbook rerating from generic battery equipment theme beta. Stage2 requires customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["137400", "299030", "114190"], "share_count_validation_required": ["137400", "299030"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C11_BATTERY_ORDERBOOK_RERATING", "existing_axis_strengthened": ["stage2_required_bridge", "battery_orderbook_delivery_revenue_margin_bridge_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C11 needs battery equipment/material MFE to map into customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin proof. PNT is a strong orderbook lifecycle candidate after source repair and share-count validation; Hana Technology and Kangwon Energy show battery equipment/material theme beta fading into local 4B when order/revenue bridge is absent or stale."}
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
  name = 피엔티
  corporate_action_candidate_dates = 2012-11-30, 2012-12-26, 2019-05-07, 2019-05-30
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

299030:
  name = 하나기술
  corporate_action_candidate_dates = 2021-03-22, 2021-04-13
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

114190:
  name = 강원에너지 from 2021-11-17, 강원 / 강원비앤이 / 웰크론강원 before that
  corporate_action_candidate_dates = 2012-12-05, 2012-12-26, 2022-05-25
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C11 rows are source_proxy_only / evidence_url_pending.
137400 and 299030 require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C11 battery orderbook rule-shape discovery,
but coding-agent promotion requires non-proxy customer orderbook, delivery schedule, backlog conversion, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C11 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 137400/299030 need share-count validation.

Candidate axis:
battery_equipment_orderbook_customer_delivery_revenue_margin_bridge_vs_equipment_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 137400, 299030 and 114190.
4. Validate 137400 and 299030 share-count changes inside the selected window.
5. Keep generic C11 battery-orderbook weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer orderbook is explicit,
   - delivery schedule and backlog conversion are visible,
   - revenue recognition exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is battery equipment/material theme beta only,
   - customer order / delivery / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, delivery delay, customer loss, financing or margin break.
9. Emit before/after diagnostics and reject if verified battery equipment orderbook positives are overblocked.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 82
next_round = R4
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

