# E2R Stock-Web v12 Residual Research — R2 Loop 76 / L2 / C10

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 76,
  "computed_next_round": "R3",
  "computed_next_loop": 76,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "memory_equipment_cycle_bridge_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
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

Previous completed state in this interactive run: R1 / loop 76.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 76
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
computed_next_round = R3
computed_next_loop = 76
```

R2 was routed to C10 because loop 75 used C06, and the visible no-repeat slice already shows C07/C08/C09 top-covered equipment/test-socket/blowoff names.  
This file tests memory/process/advanced-packaging equipment cycle bridge behavior rather than HBM memory-maker capacity or pure valuation blowoff.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Visible No-Repeat L2 concentration:

```text
C06 top-covered = UNKNOWN_SYMBOL, 000660, 005930
C07 top-covered = 042700, 089030, 039030, 058470, 095340
C08 top-covered = 058470, 131290, 리노공업, 티에스이, 095340
C09 top-covered = 039030, 042700, 095340, 이오테크닉스, 한미반도체
```

This run uses three different symbols:

```text
031980 / 피에스케이홀딩스 / advanced-packaging equipment order cycle
240810 / 원익IPS / memory process-equipment recovery bridge
036930 / 주성엔지니어링 / process-equipment cycle beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
036930 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C10 is not “semiconductor equipment stock went up.”

The mechanism must pass through:

```text
memory recovery / AI capex
→ equipment order or customer capex schedule
→ delivery, backlog, utilization
→ margin conversion
→ durable rerating
```

Equipment beta is a machine warming up.  
The real C10 bridge is the purchase order, delivery queue and gross margin running on the factory floor.

---

## Case 1 — Positive with lifecycle 4B: 031980 / 피에스케이홀딩스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is advanced-packaging / memory-equipment order, customer capacity, delivery and margin evidence.

```text
evidence_family = ADVANCED_PACKAGING_MEMORY_EQUIPMENT_ORDER_CUSTOMER_CAPACITY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-21
entry_date = 2024-02-22
entry_price = 35,650
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv`:

```text
2024-02-22,35650,43300,34800,41900
2024-03-20,41500,47200,40900,45500
2024-07-24,55900,61400,55800,58400
2024-08-05,44700,46400,38500,40850
2024-09-06,40150,40300,38000,38300
```

### Backtest

```text
MFE_30D  = +38.57%
MAE_30D  = -2.38%
MFE_90D  = +72.23%
MAE_90D  = -2.38%
MFE_180D = +72.23%
MAE_180D = -2.38%
peak_180 = 61,400 on 2024-07-24
trough_180 = 34,800 on 2024-02-22
peak_to_later_drawdown = -38.11%
```

### Interpretation

This is a C10 positive-shaped row.  
The entry-basis risk was controlled, and the MFE expanded over months.

But durable Stage2 needs non-price evidence:

```text
equipment order
advanced-package / memory customer capex
delivery backlog
margin bridge
```

After the July peak, local 4B should activate if order and margin evidence fades.

---

## Case 2 — Positive with lifecycle 4B: 240810 / 원익IPS

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is memory process-equipment order recovery, customer capex schedule, delivery and margin bridge evidence.

```text
evidence_family = MEMORY_PROCESS_EQUIPMENT_ORDER_RECOVERY_CAPEX_CUSTOMER_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-28
entry_date = 2024-02-29
entry_price = 28,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv`:

```text
2024-02-29,28700,33250,28600,32800
2024-03-20,34450,37950,33900,37400
2024-04-08,42950,44850,41400,41650
2024-08-05,31700,32500,29850,30600
2024-10-25,28850,28850,26950,27200
```

### Backtest

```text
MFE_30D  = +56.27%
MAE_30D  = -0.35%
MFE_90D  = +56.27%
MAE_90D  = -0.35%
MFE_180D = +56.27%
MAE_180D = -6.10%
peak_180 = 44,850 on 2024-04-08
trough_180 = 26,950 on 2024-10-25
peak_to_later_drawdown = -39.91%
```

### Interpretation

This is the cleaner process-equipment cycle row.  
It should not be overblocked if memory capex and order evidence is repaired.

Still, the post-peak drawdown says C10 needs lifecycle decay:

```text
order recovery verified → Stage2 possible
order/margin bridge stale → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 036930 / 주성엔지니어링

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

This row tests generic memory/process-equipment beta without sufficient order and margin refresh.

```text
evidence_family = MEMORY_PROCESS_EQUIPMENT_CYCLE_BETA_WITH_WEAK_ORDER_MARGIN_REFRESH
case_role = counterexample_equipment_beta_local4b_with_sharecount_validation
trigger_date = 2024-02-27
entry_date = 2024-02-28
entry_price = 34,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv`:

```text
2024-02-28,34700,40750,34150,40000
2024-04-08,38450,41450,36200,41650_proxy_close_note
2024-08-05,25700,26000,22150,23200
2024-09-09,22200,22950,22050,22700
2024-10-29,26950,31050,26300,31050
```

### Backtest

```text
MFE_30D  = +19.45%
MAE_30D  = -7.93%
MFE_90D  = +19.45%
MAE_90D  = -7.93%
MFE_180D = +19.45%
MAE_180D = -36.46%
peak_180 = 41,450 on 2024-04-08
trough_180 = 22,050 on 2024-09-09
peak_to_later_drawdown = -46.80%
```

### Interpretation

This is the C10 false-positive boundary.  
The first move was tradable, but not durable enough to be Green without customer order and margin bridge.

Correct treatment:

```text
equipment-cycle beta
→ no order/margin refresh
→ local 4B-watch
```

Also, the share-count change inside the selected window must block runtime promotion until validated.

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
do_not_raise_generic_C10_equipment_cycle_weight = true
do_not_treat_all_equipment_cycle_MFE_as_Green = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE
```

This fine archetype covers:

```text
1. advanced-packaging equipment order/capacity bridge → Stage2 possible after source repair
2. memory process-equipment capex recovery bridge → Stage2 possible, with lifecycle decay
3. generic equipment-cycle beta without order/margin refresh → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "symbol": "031980", "company_name": "피에스케이홀딩스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "case_type": "memory_recovery_equipment_cycle", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AdvancedPackagingEquipmentOrderCycleBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C10 should allow equipment-cycle Stage2 when memory/advanced-package equipment demand connects to actual order, customer capacity, delivery and margin bridge. PSK Holdings produced high MFE with controlled entry-basis MAE; post-peak drawdown requires lifecycle local 4B if order/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy memory/process/advanced-package equipment order, customer capex, delivery and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "case_type": "memory_recovery_equipment_cycle", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-MemoryProcessEquipmentRecoveryBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C10 should preserve process-equipment recovery winners when memory capex/order recovery, customer schedule and margin bridge are visible. Wonik IPS produced a strong early MFE with moderate MAE, then faded, so C10 needs lifecycle local 4B after bridge decay.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy memory/process/advanced-package equipment order, customer capex, delivery and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "case_type": "memory_recovery_equipment_cycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ProcessEquipmentCycleBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C10 should not treat generic equipment-cycle or memory recovery beta as durable Stage2 unless customer order, delivery, capex conversion and margin evidence refreshes. Jusung Engineering produced only limited MFE and then high MAE; share-count movement inside the window requires validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy memory/process/advanced-package equipment order, customer capex, delivery and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "case_id": "R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "symbol": "031980", "company_name": "피에스케이홀딩스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|memory_equipment_cycle_bridge_guardrail", "trigger_type": "Stage2-Actionable-AdvancedPackagingEquipmentOrderCycleBridge", "trigger_date": "2024-02-21", "entry_date": "2024-02-22", "entry_price": 35650.0, "evidence_available_at_that_date": "ADVANCED_PACKAGING_MEMORY_EQUIPMENT_ORDER_CUSTOMER_CAPACITY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:PSK_HOLDINGS_2024_ADVANCED_PACKAGING_MEMORY_EQUIPMENT_CUSTOMER_ORDER_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_recovery_or_AI_capex", "equipment_order_or_customer_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_cycle_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/031/031980/2024.csv", "profile_path": "atlas/symbol_profiles/031/031980.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 38.57, "MFE_90D_pct": 72.23, "MFE_180D_pct": 72.23, "MAE_30D_pct": -2.38, "MAE_90D_pct": -2.38, "MAE_180D_pct": -2.38, "peak_date": "2024-07-24", "peak_price": 61400.0, "drawdown_after_peak_pct": -38.11, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_equipment_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C10 should allow equipment-cycle Stage2 when memory/advanced-package equipment demand connects to actual order, customer capacity, delivery and margin bridge. PSK Holdings produced high MFE with controlled entry-basis MAE; post-peak drawdown requires lifecycle local 4B if order/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C10_MEMORY_EQUIP_031980_2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "case_id": "R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|memory_equipment_cycle_bridge_guardrail", "trigger_type": "Stage2-Actionable-MemoryProcessEquipmentRecoveryBridge", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 28700.0, "evidence_available_at_that_date": "MEMORY_PROCESS_EQUIPMENT_ORDER_RECOVERY_CAPEX_CUSTOMER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WONIK_IPS_2024_MEMORY_PROCESS_EQUIPMENT_ORDER_RECOVERY_CUSTOMER_CAPEX_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_recovery_or_AI_capex", "equipment_order_or_customer_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_cycle_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 56.27, "MFE_90D_pct": 56.27, "MFE_180D_pct": 56.27, "MAE_30D_pct": -0.35, "MAE_90D_pct": -0.35, "MAE_180D_pct": -6.1, "peak_date": "2024-04-08", "peak_price": 44850.0, "drawdown_after_peak_pct": -39.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_equipment_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C10 should preserve process-equipment recovery winners when memory capex/order recovery, customer schedule and margin bridge are visible. Wonik IPS produced a strong early MFE with moderate MAE, then faded, so C10 needs lifecycle local 4B after bridge decay.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C10_MEMORY_EQUIP_240810_2024-02-29", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "case_id": "R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|memory_equipment_cycle_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / ProcessEquipmentCycleBetaFade", "trigger_date": "2024-02-27", "entry_date": "2024-02-28", "entry_price": 34700.0, "evidence_available_at_that_date": "MEMORY_PROCESS_EQUIPMENT_CYCLE_BETA_WITH_WEAK_ORDER_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:JUSUNG_ENGINEERING_2024_MEMORY_PROCESS_EQUIPMENT_ORDER_CAPEX_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_recovery_or_AI_capex", "equipment_order_or_customer_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_cycle_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.45, "MFE_90D_pct": 19.45, "MFE_180D_pct": 19.45, "MAE_30D_pct": -7.93, "MAE_90D_pct": -7.93, "MAE_180D_pct": -36.46, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_memory_equipment_peak_if_order_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_capex_delivery_or_margin_break", "trigger_outcome_label": "counterexample_equipment_beta_local4b_with_sharecount_validation", "current_profile_verdict": "C10 should not treat generic equipment-cycle or memory recovery beta as durable Stage2 unless customer order, delivery, capex conversion and margin evidence refreshes. Jusung Engineering produced only limited MFE and then high MAE; share-count movement inside the window requires validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C10_MEMORY_EQUIP_036930_2024-02-28", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "trigger_id": "TRG_R2L76-C10-031980-PSK-HOLDINGS-ADVANCED-PACKAGING-EQUIPMENT-CYCLE", "symbol": "031980", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"memory_recovery_score": 12, "equipment_order_score": 14, "customer_capex_score": 13, "delivery_backlog_score": 12, "margin_bridge_score": 13, "relative_strength_score": 14, "execution_risk_score": 6, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"memory_recovery_score": 11, "equipment_order_score": 16, "customer_capex_score": 15, "delivery_backlog_score": 14, "margin_bridge_score": 15, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["equipment_order_score", "customer_capex_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified memory equipment orders, customer capex, delivery/backlog and margin bridge; cap equipment-cycle beta when order/margin evidence fails to refresh.", "MFE_90D_pct": 72.23, "MAE_90D_pct": -2.38, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C10 should allow equipment-cycle Stage2 when memory/advanced-package equipment demand connects to actual order, customer capacity, delivery and margin bridge. PSK Holdings produced high MFE with controlled entry-basis MAE; post-peak drawdown requires lifecycle local 4B if order/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "trigger_id": "TRG_R2L76-C10-240810-WONIK-IPS-MEMORY-PROCESS-EQUIPMENT-CYCLE", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"memory_recovery_score": 12, "equipment_order_score": 14, "customer_capex_score": 13, "delivery_backlog_score": 12, "margin_bridge_score": 13, "relative_strength_score": 14, "execution_risk_score": 6, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"memory_recovery_score": 11, "equipment_order_score": 16, "customer_capex_score": 15, "delivery_backlog_score": 14, "margin_bridge_score": 15, "relative_strength_score": 13, "execution_risk_score": 7, "dilution_or_sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["equipment_order_score", "customer_capex_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified memory equipment orders, customer capex, delivery/backlog and margin bridge; cap equipment-cycle beta when order/margin evidence fails to refresh.", "MFE_90D_pct": 56.27, "MAE_90D_pct": -0.35, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C10 should preserve process-equipment recovery winners when memory capex/order recovery, customer schedule and margin bridge are visible. Wonik IPS produced a strong early MFE with moderate MAE, then faded, so C10 needs lifecycle local 4B after bridge decay."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "trigger_id": "TRG_R2L76-C10-036930-JUSUNG-EQUIPMENT-CYCLE-BETA-FADE", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "raw_component_scores_before": {"memory_recovery_score": 6, "equipment_order_score": 4, "customer_capex_score": 4, "delivery_backlog_score": 3, "margin_bridge_score": 2, "relative_strength_score": 7, "execution_risk_score": 18, "dilution_or_sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"memory_recovery_score": 4, "equipment_order_score": 2, "customer_capex_score": 2, "delivery_backlog_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 21, "dilution_or_sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 39, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["equipment_order_score", "customer_capex_score", "delivery_backlog_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified memory equipment orders, customer capex, delivery/backlog and margin bridge; cap equipment-cycle beta when order/margin evidence fails to refresh.", "MFE_90D_pct": 19.45, "MAE_90D_pct": -7.93, "score_return_alignment_label": "false_positive_equipment_cycle_bridge_gap", "current_profile_verdict": "C10 should not treat generic equipment-cycle or memory recovery beta as durable Stage2 unless customer order, delivery, capex conversion and margin evidence refreshes. Jusung Engineering produced only limited MFE and then high MAE; share-count movement inside the window requires validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 76, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_PROCESS_ADVANCED_PACKAGING_EQUIPMENT_ORDER_CYCLE_BRIDGE_VS_EQUIPMENT_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C10 memory/process/advanced-packaging equipment symbols outside C06 loop-75 and C07/C08/C09 top-covered sets, +3 order/recovery/equipment-beta trigger families, +2 equipment-order positives, +1 equipment-cycle local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 76, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "axis": "memory_process_advanced_packaging_equipment_order_cycle_bridge_vs_equipment_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C10 should split verified memory/process/advanced-packaging equipment order-cycle rerating from generic equipment beta. Stage2 requires equipment order, customer capex schedule, delivery/backlog, utilization or margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["031980", "240810", "036930"], "share_count_validation_required": ["036930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 76, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C10 needs memory/process/advanced-package equipment order proof. PSK Holdings and Wonik IPS show equipment-order cycle positives after source repair; Jusung Engineering shows equipment-cycle beta fading into local 4B when order/margin bridge is absent."}
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
031980:
  corporate_action_candidate_dates = 1998-07-28, 2000-04-20, 2007-03-16, 2019-05-10, 2020-02-21
  selected window = 2024-02-22~D+180
  contamination = false

240810:
  corporate_action_candidate_dates = none
  selected window = 2024-02-29~D+180
  contamination = false

036930:
  corporate_action_candidate_dates = 2000-06-22
  selected window = 2024-02-28~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C10 rows are source_proxy_only / evidence_url_pending.
036930 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C10 rule-shape discovery,
but coding-agent promotion requires non-proxy memory/process/advanced-package equipment order, customer capex, delivery and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C10 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 036930 needs share-count validation.

Candidate axis:
memory_process_advanced_packaging_equipment_order_cycle_bridge_vs_equipment_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 031980, 240810 and 036930.
4. Validate 036930 share-count changes inside the selected window.
5. Keep generic C10 memory-equipment cycle weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - memory recovery or AI capex demand is explicit,
   - equipment order / customer capex / delivery backlog is visible,
   - margin or utilization bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is equipment-cycle beta only,
   - order/capex/margin bridge is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer order cut, capex cancellation, delivery delay, utilization collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified memory/advanced-packaging equipment positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 76
next_round = R3
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

