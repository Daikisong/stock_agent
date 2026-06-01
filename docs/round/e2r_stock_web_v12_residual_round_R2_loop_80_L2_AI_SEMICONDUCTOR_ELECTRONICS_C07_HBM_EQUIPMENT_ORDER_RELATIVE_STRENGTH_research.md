# E2R Stock-Web v12 Residual Research — R2 Loop 80 / L2 / C07

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 80,
  "computed_next_round": "R3",
  "computed_next_loop": 80,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH",
  "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "HBM_test_equipment_order_relative_strength_guardrail",
    "order_customer_capacity_delivery_margin_bridge",
    "inspection_metrology_theme_fade_boundary",
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

Previous completed state in this interactive run: R1 / loop 80.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 80
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
computed_next_round = R3
computed_next_loop = 80
```

R2 was routed to C07 because loop 79 R2 used C09.  
This file tests HBM/test-equipment order relative strength rather than advanced-equipment valuation blowoff.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C07 concentration in:

```text
042700, 089030, 039030, 058470, 095340
```

This run uses three different symbols:

```text
003160 / 디아이 / HBM test-equipment order relative-strength bridge
232140 / 와이씨 / HBM memory-test equipment customer-order bridge
348210 / 넥스틴 / inspection/metrology equipment theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
348210 shows later 2024 share-count change and requires coding-agent validation before runtime promotion.
```

## Research thesis

C07 is not “HBM 장비주가 올랐다.”

The mechanism must pass through:

```text
HBM / advanced memory capex
→ equipment order or backlog
→ customer quality and capacity expansion
→ delivery schedule and revenue recognition
→ margin bridge
→ durable relative strength
```

상대강도는 레이더에 잡힌 물체다.  
C07이 보려는 것은 그 물체가 실제 수주, 고객 투자, 납기, 매출, 마진으로 착륙하는지다.

---

## Case 1 — HBM test-equipment positive: 003160 / 디아이

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is HBM/memory test equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = HBM_MEMORY_TEST_EQUIPMENT_ORDER_CUSTOMER_CAPACITY_DELIVERY_MARGIN_BRIDGE
case_role = positive_HBM_test_equipment_RS_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,950
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv`:

```text
2024-02-01,5950,6040,5900,5980
2024-02-20,7190,8190,7140,7940
2024-03-05,9250,11750,9040,11740
2024-04-04,13550,17200,13350,16140
2024-07-24,17150,18580,17040,17740
2024-08-05,15300,15480,12640,13530
2024-10-28,20600,21000,18750,20500
```

### Backtest

```text
MFE_30D  = +97.48%
MAE_30D  = -2.52%
MFE_90D  = +210.42%
MAE_90D  = -2.52%
MFE_180D = +252.94%
MAE_180D = -2.52%
peak_180 = 21,000 on 2024-10-28
trough_180 = 5,800 on 2024-02-07
peak_to_later_drawdown = -22.76%
```

### Interpretation

This is a C07 HBM test-equipment positive.  
Relative strength was not just a flash; the entry-basis MAE stayed controlled while the MFE expanded.

Correct treatment:

```text
verified HBM test-equipment order / customer capacity / delivery / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — HBM memory-test customer-order positive: 232140 / 와이씨

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
name_change_inside_window = true
source_repair_required = true
```

The source-repair task is memory-test equipment customer order, HBM capacity expansion, delivery/revenue conversion and margin bridge evidence.

```text
evidence_family = HBM_MEMORY_TEST_EQUIPMENT_CUSTOMER_ORDER_CAPACITY_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_HBM_test_equipment_customer_order_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,490
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv`:

```text
2024-02-01,5490,5560,5250,5400
2024-02-28,6000,6790,5970,6690
2024-04-18,7160,9460,7050,9460
2024-04-26,12550,14980,12270,14090
2024-06-13,19110,22950,18660,21900
2024-08-05,16000,16020,12560,13730
2024-09-09,11280,12030,10830,11890
```

### Backtest

```text
MFE_30D  = +46.45%
MAE_30D  = -8.56%
MFE_90D  = +318.03%
MAE_90D  = -8.56%
MFE_180D = +318.03%
MAE_180D = -8.56%
peak_180 = 22,950 on 2024-06-13
trough_180 = 5,020 on 2024-02-06
peak_to_later_drawdown = -52.81%
```

### Interpretation

This is the strongest C07 MFE row in this run.  
But the large post-peak drawdown says customer order and margin evidence must refresh.

Correct treatment:

```text
verified customer order / HBM capacity / delivery / margin bridge → Stage2 possible
name-change continuity check
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 348210 / 넥스틴

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests inspection/metrology equipment theme beta without enough HBM customer order and margin bridge.

```text
evidence_family = INSPECTION_METROLOGY_EQUIPMENT_THEME_WITH_WEAK_HBM_CUSTOMER_ORDER_MARGIN_BRIDGE
case_role = counterexample_inspection_metrology_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 72,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv`:

```text
2024-02-01,72000,72100,67500,68800
2024-02-28,68900,76800,68700,74800
2024-03-04,77800,77900,75300,76200
2024-04-08,67300,67400,63500,64600
2024-08-05,53400,53700,44900,45000
2024-09-09,40950,42100,40350,42000
2024-10-25,67700,68000,67000,67500
```

### Backtest

```text
MFE_30D  = +6.81%
MAE_30D  = -8.19%
MFE_90D  = +8.19%
MAE_90D  = -11.81%
MFE_180D = +8.19%
MAE_180D = -43.96%
peak_180 = 77,900 on 2024-03-04
trough_180 = 40,350 on 2024-09-09
peak_to_later_drawdown = -48.20%
```

### Interpretation

This is a C07 false-positive boundary.  
Inspection/metrology exposure alone did not validate durable HBM equipment order relative strength.

Correct treatment:

```text
inspection/metrology equipment theme beta
→ no verified HBM customer order / delivery / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
relative_strength_requires_order_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C07_HBM_equipment_theme_weight = true
do_not_treat_all_HBM_equipment_MFE_as_Green = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_order_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE
```

This fine archetype covers:

```text
1. HBM test-equipment order and customer-capacity bridge → Stage2 possible after source repair
2. memory-test customer order / delivery bridge → Stage2 possible, lifecycle-managed
3. inspection/metrology equipment beta without HBM order bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-HBMTestEquipmentOrderRSBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should protect HBM/test-equipment positives when relative strength maps to equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge. DI produced a very large MFE with controlled entry-basis MAE, but the post-peak drawdown means source-repaired lifecycle 4B is still needed.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy HBM/test-equipment order, customer quality, capacity, delivery, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-HBMMemoryTestEquipmentCustomerOrderRSBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should preserve memory-test equipment positives when relative strength is backed by customer order quality, HBM capacity expansion, delivery cadence, revenue conversion and margin bridge. YC produced explosive MFE but later drawdown requires lifecycle treatment and source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy HBM/test-equipment order, customer quality, capacity, delivery, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE", "symbol": "348210", "company_name": "넥스틴", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "case_type": "HBM_equipment_order_relative_strength", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / InspectionMetrologyEquipmentThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C07 should not treat semiconductor inspection/metrology theme beta as durable Stage2 unless HBM/customer order, capacity expansion, delivery, recurring service and margin bridge are visible. Nextin had small early MFE and then a deep MAE path, making it a local 4B boundary rather than Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy HBM/test-equipment order, customer quality, capacity, delivery, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE", "case_id": "R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE", "symbol": "003160", "company_name": "디아이", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_test_equipment_order_RS_guardrail", "trigger_type": "Stage2-Actionable-HBMTestEquipmentOrderRSBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5950.0, "evidence_available_at_that_date": "HBM_MEMORY_TEST_EQUIPMENT_ORDER_CUSTOMER_CAPACITY_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DI_2024_HBM_TEST_EQUIPMENT_ORDER_CUSTOMER_CAPACITY_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_equipment_order_candidate", "customer_quality_or_capacity_candidate", "delivery_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_order_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003160/2024.csv", "profile_path": "atlas/symbol_profiles/003/003160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 97.48, "MFE_90D_pct": 210.42, "MFE_180D_pct": 252.94, "MAE_30D_pct": -2.52, "MAE_90D_pct": -2.52, "MAE_180D_pct": -2.52, "peak_date": "2024-10-28", "peak_price": 21000.0, "drawdown_after_peak_pct": -22.76, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_HBM_equipment_peak_if_order_customer_capacity_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_HBM_test_equipment_RS_with_later_4b_watch", "current_profile_verdict": "C07 should protect HBM/test-equipment positives when relative strength maps to equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge. DI produced a very large MFE with controlled entry-basis MAE, but the post-peak drawdown means source-repaired lifecycle 4B is still needed.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C07_HBM_EQUIPMENT_003160_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS", "case_id": "R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS", "symbol": "232140", "company_name": "와이씨", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_test_equipment_order_RS_guardrail", "trigger_type": "Stage2-Actionable-HBMMemoryTestEquipmentCustomerOrderRSBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5490.0, "evidence_available_at_that_date": "HBM_MEMORY_TEST_EQUIPMENT_CUSTOMER_ORDER_CAPACITY_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:YC_2024_HBM_MEMORY_TEST_EQUIPMENT_CUSTOMER_ORDER_CAPACITY_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_equipment_order_candidate", "customer_quality_or_capacity_candidate", "delivery_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_order_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/232/232140/2024.csv", "profile_path": "atlas/symbol_profiles/232/232140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 46.45, "MFE_90D_pct": 318.03, "MFE_180D_pct": 318.03, "MAE_30D_pct": -8.56, "MAE_90D_pct": -8.56, "MAE_180D_pct": -8.56, "peak_date": "2024-06-13", "peak_price": 22950.0, "drawdown_after_peak_pct": -52.81, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_HBM_equipment_peak_if_order_customer_capacity_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_HBM_test_equipment_customer_order_with_later_4b_watch", "current_profile_verdict": "C07 should preserve memory-test equipment positives when relative strength is backed by customer order quality, HBM capacity expansion, delivery cadence, revenue conversion and margin bridge. YC produced explosive MFE but later drawdown requires lifecycle treatment and source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C07_HBM_EQUIPMENT_232140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE", "case_id": "R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE", "symbol": "348210", "company_name": "넥스틴", "round": "R2", "loop": "80", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|HBM_test_equipment_order_RS_guardrail", "trigger_type": "Stage2-FalsePositive / InspectionMetrologyEquipmentThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 72000.0, "evidence_available_at_that_date": "INSPECTION_METROLOGY_EQUIPMENT_THEME_WITH_WEAK_HBM_CUSTOMER_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:NEXTIN_2024_INSPECTION_METROLOGY_HBM_CUSTOMER_ORDER_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["HBM_equipment_order_candidate", "customer_quality_or_capacity_candidate", "delivery_revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_order_or_backlog_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/348/348210/2024.csv", "profile_path": "atlas/symbol_profiles/348/348210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.81, "MFE_90D_pct": 8.19, "MFE_180D_pct": 8.19, "MAE_30D_pct": -8.19, "MAE_90D_pct": -11.81, "MAE_180D_pct": -43.96, "peak_date": "2024-03-04", "peak_price": 77900.0, "drawdown_after_peak_pct": -48.2, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_HBM_equipment_peak_if_order_customer_capacity_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_inspection_metrology_theme_local4b", "current_profile_verdict": "C07 should not treat semiconductor inspection/metrology theme beta as durable Stage2 unless HBM/customer order, capacity expansion, delivery, recurring service and margin bridge are visible. Nextin had small early MFE and then a deep MAE path, making it a local 4B boundary rather than Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C07_HBM_EQUIPMENT_348210_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE", "trigger_id": "TRG_R2L80-C07-003160-DI-HBM-TEST-EQUIPMENT-RS-ORDER-BRIDGE", "symbol": "003160", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_equipment_order_score": 15, "customer_quality_score": 14, "capacity_delivery_score": 14, "revenue_margin_bridge_score": 14, "relative_strength_score": 16, "execution_risk_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"HBM_equipment_order_score": 17, "customer_quality_score": 16, "capacity_delivery_score": 16, "revenue_margin_bridge_score": 16, "relative_strength_score": 15, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["HBM_equipment_order_score", "customer_quality_score", "capacity_delivery_score", "revenue_margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM equipment order/customer/capacity/delivery/margin bridge; cap inspection or equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 210.42, "MAE_90D_pct": -2.52, "score_return_alignment_label": "HBM_test_equipment_order_RS_positive_with_lifecycle_4b", "current_profile_verdict": "C07 should protect HBM/test-equipment positives when relative strength maps to equipment order, customer capacity, delivery schedule, revenue recognition and margin bridge. DI produced a very large MFE with controlled entry-basis MAE, but the post-peak drawdown means source-repaired lifecycle 4B is still needed."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS", "trigger_id": "TRG_R2L80-C07-232140-YC-HBM-TEST-EQUIPMENT-CUSTOMER-ORDER-RS", "symbol": "232140", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_equipment_order_score": 15, "customer_quality_score": 14, "capacity_delivery_score": 14, "revenue_margin_bridge_score": 14, "relative_strength_score": 16, "execution_risk_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"HBM_equipment_order_score": 17, "customer_quality_score": 16, "capacity_delivery_score": 16, "revenue_margin_bridge_score": 16, "relative_strength_score": 15, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["HBM_equipment_order_score", "customer_quality_score", "capacity_delivery_score", "revenue_margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM equipment order/customer/capacity/delivery/margin bridge; cap inspection or equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 318.03, "MAE_90D_pct": -8.56, "score_return_alignment_label": "HBM_test_equipment_order_RS_positive_with_lifecycle_4b", "current_profile_verdict": "C07 should preserve memory-test equipment positives when relative strength is backed by customer order quality, HBM capacity expansion, delivery cadence, revenue conversion and margin bridge. YC produced explosive MFE but later drawdown requires lifecycle treatment and source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE", "trigger_id": "TRG_R2L80-C07-348210-NEXTIN-INSPECTION-METROLOGY-THEME-FADE", "symbol": "348210", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "raw_component_scores_before": {"HBM_equipment_order_score": 5, "customer_quality_score": 3, "capacity_delivery_score": 3, "revenue_margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 22, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"HBM_equipment_order_score": 3, "customer_quality_score": 1, "capacity_delivery_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["HBM_equipment_order_score", "customer_quality_score", "capacity_delivery_score", "revenue_margin_bridge_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified HBM equipment order/customer/capacity/delivery/margin bridge; cap inspection or equipment theme beta when evidence fails to refresh.", "MFE_90D_pct": 8.19, "MAE_90D_pct": -11.81, "score_return_alignment_label": "false_positive_inspection_metrology_bridge_gap", "current_profile_verdict": "C07 should not treat semiconductor inspection/metrology theme beta as durable Stage2 unless HBM/customer order, capacity expansion, delivery, recurring service and margin bridge are visible. Nextin had small early MFE and then a deep MAE path, making it a local 4B boundary rather than Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 80, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "fine_archetype_id": "HBM_TEST_EQUIPMENT_ORDER_RELATIVE_STRENGTH_BRIDGE_VS_INSPECTION_METROLOGY_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C07 HBM/test/inspection-equipment symbols outside top-covered 042700/089030/039030/058470/095340 set, +3 DI/YC/Nextin trigger families, +2 HBM test-equipment RS positives, +1 inspection/metrology local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 80, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "axis": "HBM_test_equipment_order_relative_strength_bridge_vs_inspection_metrology_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C07 should split verified HBM/test-equipment order and customer-capacity rerating from generic inspection/equipment theme beta. Stage2 requires HBM equipment order, customer quality, capacity expansion, delivery/revenue and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003160", "232140", "348210"], "share_count_validation_required": ["348210"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 80, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH", "existing_axis_strengthened": ["stage2_required_bridge", "relative_strength_requires_order_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C07 needs HBM equipment order, customer quality, capacity/delivery and margin proof. DI and YC show HBM memory-test equipment relative-strength positives after source repair; Nextin shows inspection/metrology equipment theme beta fading into local 4B when HBM/customer order and margin bridge are absent or stale."}
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
003160:
  name = 디아이
  corporate_action_candidate_dates = 1997-01-03, 1998-07-03, 1999-10-18
  selected window = 2024-02-01~D+180
  contamination = false

232140:
  name = 와이씨 from 2024-04-25, 와이아이케이 before that
  corporate_action_candidate_dates = 2017-04-05
  selected window = 2024-02-01~D+180
  contamination = false
  name_change_inside_window = true → continuity validation recommended

348210:
  name = 넥스틴
  market = KOSDAQ GLOBAL during 2024
  corporate_action_candidate_dates = 2021-01-13, 2021-01-27
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C07 rows are source_proxy_only / evidence_url_pending.
348210 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C07 rule-shape discovery,
but coding-agent promotion requires non-proxy HBM/test-equipment order, customer quality, capacity expansion, delivery, revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C07 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 348210 needs share-count validation.

Candidate axis:
HBM_test_equipment_order_relative_strength_bridge_vs_inspection_metrology_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003160, 232140 and 348210.
4. Validate 232140 name-change continuity and 348210 share-count changes inside the selected window.
5. Keep generic C07 HBM-equipment weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - HBM equipment order or backlog is explicit,
   - customer quality or customer capacity is visible,
   - delivery schedule and revenue bridge exist,
   - margin bridge is credible,
   - relative strength is not price-only,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is HBM/inspection/metrology equipment theme beta only,
   - order/customer/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cut, customer loss, delivery delay, pricing collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified low-MAE HBM equipment positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 80
next_round = R3
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

