# E2R Stock-Web v12 Residual Research — R2 Loop 82 / L2 / C09

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 82,
  "computed_next_round": "R3",
  "computed_next_loop": 82,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "advanced_equipment_valuation_blowoff_guardrail",
    "semicap_ALD_metrology_memory_capex_order_revenue_margin_bridge",
    "valuation_blowoff_theme_fade_boundary",
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

Previous completed state in this interactive run: R1 / loop 82.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 82
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
computed_next_round = R3
computed_next_loop = 82
```

R2 was routed to C09 because loop 81 R2 used C08 and loop 80 R2 used C07.  
This file tests semicap / ALD / metrology advanced-equipment valuation blowoff and order/revenue bridge separation.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C09 concentration in:

```text
039030, 042700, 095340, 이오테크닉스, 한미반도체
```

This run uses three different symbols:

```text
240810 / 원익IPS / semicap memory-capex order bridge lifecycle
036930 / 주성엔지니어링 / ALD equipment valuation blowoff with share-count validation
322310 / 오로스테크놀로지 / overlay metrology valuation blowoff
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
036930 shows share-count changes inside the 2024 shard and requires coding-agent validation before runtime promotion.
```

## Research thesis

C09 is not “반도체 장비주가 올랐다.”

The mechanism must pass through:

```text
AI / HBM / memory capex headline
→ customer order or capex allocation
→ backlog and delivery schedule
→ revenue recognition
→ margin bridge
→ durable rerating
```

첨단 장비주는 장비 사진이 아니라 납품표다.  
C09가 보려는 것은 headline의 빛이 실제 발주, 납기, 매출, 마진으로 웨이퍼 위에 찍히는지다.

---

## Case 1 — Semicap lifecycle candidate: 240810 / 원익IPS

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is memory capex allocation, equipment order, delivery/backlog conversion, revenue recognition and margin bridge evidence.

```text
evidence_family = SEMICAP_MEMORY_CAPEX_ALD_DEPOSITION_ORDER_CUSTOMER_REVENUE_MARGIN_BRIDGE
case_role = positive_semicap_order_bridge_lifecycle_with_later_valuation_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 30,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv`:

```text
2024-02-01,30300,30800,30150,30700
2024-02-27,28950,29100,28500,28500
2024-03-20,34450,37950,33900,37400
2024-03-29,36750,43400,36750,41500
2024-04-08,42950,44850,41400,41650
2024-08-05,31700,32500,29850,30600
2024-09-11,29500,29600,27800,28000
2024-10-31,27050,28050,26800,27850
```

### Backtest

```text
MFE_30D  = +25.25%
MAE_30D  = -6.93%
MFE_90D  = +48.02%
MAE_90D  = -6.93%
MFE_180D = +48.02%
MAE_180D = -11.55%
peak_180 = 44,850 on 2024-04-08
trough_180 = 26,800 on 2024-10-31
peak_to_later_drawdown = -40.25%
```

### Interpretation

This is a C09 lifecycle candidate, not automatic blowoff rejection.  
The early MFE was tradable and entry-basis MAE was not catastrophic, but the later drawdown requires order/revenue/margin bridge refresh.

Correct treatment:

```text
verified memory capex / customer order / delivery / revenue / margin bridge → Stage2-Yellow possible
bridge stale after peak → valuation local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 036930 / 주성엔지니어링

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests ALD/deposition equipment theme beta without enough order/revenue/margin bridge.

```text
evidence_family = ALD_DEPOSITION_HBM_MEMORY_CAPEX_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_ALD_equipment_valuation_blowoff_local4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 33,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv`:

```text
2024-02-01,33000,33300,30700,31150
2024-02-06,30350,30350,26900,29300
2024-02-28,34700,40750,34150,40000
2024-04-08,38450,41450,36200,approx_from_stock_web_row
2024-08-05,25700,26000,22150,23200
2024-09-09,22200,22950,22050,22700
2024-09-10,23050,23050,22050,22300
2024-10-31,29450,31800,29450,31000
```

### Backtest

```text
MFE_30D  = +23.48%
MAE_30D  = -18.48%
MFE_90D  = +25.61%
MAE_90D  = -18.48%
MFE_180D = +25.61%
MAE_180D = -33.18%
peak_180 = 41,450 on 2024-04-08
trough_180 = 22,050 on 2024-09-09~2024-09-10
peak_to_later_drawdown = -46.80%
```

### Interpretation

This is a C09 valuation-blowoff / local-4B boundary.  
The MFE was not enough because customer order, backlog conversion and margin bridge are unresolved, and the MAE later widened.

Correct treatment:

```text
ALD/deposition equipment theme beta
→ no verified customer order / revenue / margin bridge
→ local 4B-watch
→ share-count validation before runtime ingestion
```

---

## Case 3 — Counterexample / local 4B: 322310 / 오로스테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests overlay metrology / inspection-equipment theme beta without enough customer-order and margin bridge.

```text
evidence_family = OVERLAY_METROLOGY_ADVANCED_EQUIPMENT_THEME_WITH_WEAK_CUSTOMER_ORDER_REVENUE_MARGIN_BRIDGE
case_role = counterexample_metrology_equipment_valuation_blowoff_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 28,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv`:

```text
2024-02-01,28300,28900,26700,27200
2024-02-20,30300,34550,29600,33750
2024-02-27,36100,40750,34050,37200
2024-03-13,36000,36700,33100,33750
2024-08-05,19950,19980,16300,16860
2024-09-09,15300,15950,15130,15730
2024-09-25,18000,18850,17810,17950
2024-10-25,15900,16000,15600,15750
```

### Backtest

```text
MFE_30D  = +43.99%
MAE_30D  = -5.65%
MFE_90D  = +43.99%
MAE_90D  = -5.65%
MFE_180D = +43.99%
MAE_180D = -46.54%
peak_180 = 40,750 on 2024-02-27
trough_180 = 15,130 on 2024-09-09
peak_to_later_drawdown = -62.87%
```

### Interpretation

This is a C09 advanced-equipment valuation-blowoff counterexample.  
The early spike did not become durable customer-order/revenue economics.

Correct treatment:

```text
overlay metrology / inspection equipment theme beta
→ no verified customer order / delivery / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
customer_order_revenue_margin_bridge_required = strengthen
valuation_blowoff_local_4b_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C09_equipment_theme_weight = true
do_not_treat_all_advanced_equipment_MFE_as_Green = true
do_not_ingest_sharecount_changed_equipment_rows_without_validation = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_customer_order_delivery_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE
```

This fine archetype covers:

```text
1. broad semicap memory-capex order bridge → Stage2-Yellow possible after source repair
2. ALD/deposition theme beta without order/revenue bridge → false Stage2 / local 4B
3. overlay metrology equipment valuation blowoff without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-SemicapMemoryCapexOrderRevenueBridgeWithValuation4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should not mechanically reject all advanced-equipment MFE. Wonik IPS had a credible semicap/order-cycle price path, but promotion requires memory capex, customer order, delivery/revenue and margin evidence; later drawdown requires lifecycle 4B if bridge fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer order, delivery/backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ALDEquipmentValuationBlowoffFadeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should not treat ALD/deposition equipment theme beta as durable Stage2 unless named customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Jusung produced a fast spike and then deep MAE; the 2024 shard also shows share-count change, so validation is required.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer order, delivery/backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / MetrologyInspectionEquipmentValuationBlowoffFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should cap overlay metrology/inspection equipment MFE when it is mostly valuation/theme beta. Without customer order, delivery, revenue conversion and margin bridge, Oros' early spike should be treated as local 4B/fade rather than durable Stage2.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer order, delivery/backlog conversion, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE", "case_id": "R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage2-Lifecycle-SemicapMemoryCapexOrderRevenueBridgeWithValuation4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 30300.0, "evidence_available_at_that_date": "SEMICAP_MEMORY_CAPEX_ALD_DEPOSITION_ORDER_CUSTOMER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WONIK_IPS_2024_SEMICAP_MEMORY_CAPEX_CUSTOMER_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_capex_or_equipment_candidate", "customer_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "backlog_conversion_or_customer_quality_candidate"], "stage4b_evidence_fields": ["valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.25, "MFE_90D_pct": 48.02, "MFE_180D_pct": 48.02, "MAE_30D_pct": -6.93, "MAE_90D_pct": -6.93, "MAE_180D_pct": -11.55, "peak_date": "2024-04-08", "peak_price": 44850.0, "drawdown_after_peak_pct": -40.25, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_advanced_equipment_peak_if_customer_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_cut_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_semicap_order_bridge_lifecycle_with_later_valuation_4b_watch", "current_profile_verdict": "C09 should not mechanically reject all advanced-equipment MFE. Wonik IPS had a credible semicap/order-cycle price path, but promotion requires memory capex, customer order, delivery/revenue and margin evidence; later drawdown requires lifecycle 4B if bridge fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_240810_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT", "case_id": "R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage2-FalsePositive / ALDEquipmentValuationBlowoffFadeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 33000.0, "evidence_available_at_that_date": "ALD_DEPOSITION_HBM_MEMORY_CAPEX_THEME_WITH_WEAK_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JUSUNG_ENGINEERING_2024_ALD_DEPOSITION_MEMORY_CAPEX_CUSTOMER_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_capex_or_equipment_candidate", "customer_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "backlog_conversion_or_customer_quality_candidate"], "stage4b_evidence_fields": ["valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.48, "MFE_90D_pct": 25.61, "MFE_180D_pct": 25.61, "MAE_30D_pct": -18.48, "MAE_90D_pct": -18.48, "MAE_180D_pct": -33.18, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_advanced_equipment_peak_if_customer_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_cut_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_ALD_equipment_valuation_blowoff_local4b_with_sharecount_validation", "current_profile_verdict": "C09 should not treat ALD/deposition equipment theme beta as durable Stage2 unless named customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Jusung produced a fast spike and then deep MAE; the 2024 shard also shows share-count change, so validation is required.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_036930_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF", "case_id": "R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF", "symbol": "322310", "company_name": "오로스테크놀로지", "round": "R2", "loop": "82", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage2-FalsePositive / MetrologyInspectionEquipmentValuationBlowoffFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 28300.0, "evidence_available_at_that_date": "OVERLAY_METROLOGY_ADVANCED_EQUIPMENT_THEME_WITH_WEAK_CUSTOMER_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:OROS_TECHNOLOGY_2024_OVERLAY_METROLOGY_CUSTOMER_ORDER_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["memory_capex_or_equipment_candidate", "customer_order_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "backlog_conversion_or_customer_quality_candidate"], "stage4b_evidence_fields": ["valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/322/322310/2024.csv", "profile_path": "atlas/symbol_profiles/322/322310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 43.99, "MFE_90D_pct": 43.99, "MFE_180D_pct": 43.99, "MAE_30D_pct": -5.65, "MAE_90D_pct": -5.65, "MAE_180D_pct": -46.54, "peak_date": "2024-02-27", "peak_price": 40750.0, "drawdown_after_peak_pct": -62.87, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_advanced_equipment_peak_if_customer_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_order_cut_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_metrology_equipment_valuation_blowoff_local4b", "current_profile_verdict": "C09 should cap overlay metrology/inspection equipment MFE when it is mostly valuation/theme beta. Without customer order, delivery, revenue conversion and margin bridge, Oros' early spike should be treated as local 4B/fade rather than durable Stage2.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_322310_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE", "trigger_id": "TRG_R2L82-C09-240810-WONIK-IPS-SEMICAP-ORDER-BRIDGE-LIFECYCLE", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_order_score": 13, "equipment_capex_visibility_score": 13, "backlog_delivery_score": 12, "revenue_conversion_score": 12, "margin_bridge_score": 12, "valuation_risk_score": 10, "relative_strength_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"customer_order_score": 15, "equipment_capex_visibility_score": 15, "backlog_delivery_score": 14, "revenue_conversion_score": 14, "margin_bridge_score": 14, "valuation_risk_score": 12, "relative_strength_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_order_score", "equipment_capex_visibility_score", "backlog_delivery_score", "revenue_conversion_score", "margin_bridge_score", "valuation_risk_score"], "component_delta_explanation": "Reward only verified equipment customer order, delivery/backlog conversion, revenue and margin bridge; cap valuation/theme blowoff when the bridge fails to refresh.", "MFE_90D_pct": 48.02, "MAE_90D_pct": -6.93, "score_return_alignment_label": "advanced_equipment_lifecycle_candidate", "current_profile_verdict": "C09 should not mechanically reject all advanced-equipment MFE. Wonik IPS had a credible semicap/order-cycle price path, but promotion requires memory capex, customer order, delivery/revenue and margin evidence; later drawdown requires lifecycle 4B if bridge fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT", "trigger_id": "TRG_R2L82-C09-036930-JUSUNG-ALD-EQUIPMENT-VALUATION-BLOWOFF-SHARECOUNT", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_order_score": 4, "equipment_capex_visibility_score": 5, "backlog_delivery_score": 3, "revenue_conversion_score": 2, "margin_bridge_score": 1, "valuation_risk_score": 24, "relative_strength_score": 6, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / valuation local 4B-watch", "raw_component_scores_after": {"customer_order_score": 2, "equipment_capex_visibility_score": 3, "backlog_delivery_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "valuation_risk_score": 26, "relative_strength_score": 4, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_order_score", "equipment_capex_visibility_score", "backlog_delivery_score", "revenue_conversion_score", "margin_bridge_score", "valuation_risk_score"], "component_delta_explanation": "Reward only verified equipment customer order, delivery/backlog conversion, revenue and margin bridge; cap valuation/theme blowoff when the bridge fails to refresh.", "MFE_90D_pct": 25.61, "MAE_90D_pct": -18.48, "score_return_alignment_label": "valuation_blowoff_false_positive_bridge_gap", "current_profile_verdict": "C09 should not treat ALD/deposition equipment theme beta as durable Stage2 unless named customer order, delivery schedule, backlog conversion, revenue and margin bridge are visible. Jusung produced a fast spike and then deep MAE; the 2024 shard also shows share-count change, so validation is required."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF", "trigger_id": "TRG_R2L82-C09-322310-AUROS-METROLOGY-VALUATION-BLOWOFF", "symbol": "322310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"customer_order_score": 4, "equipment_capex_visibility_score": 5, "backlog_delivery_score": 3, "revenue_conversion_score": 2, "margin_bridge_score": 1, "valuation_risk_score": 24, "relative_strength_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / valuation local 4B-watch", "raw_component_scores_after": {"customer_order_score": 2, "equipment_capex_visibility_score": 3, "backlog_delivery_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "valuation_risk_score": 26, "relative_strength_score": 4, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_order_score", "equipment_capex_visibility_score", "backlog_delivery_score", "revenue_conversion_score", "margin_bridge_score", "valuation_risk_score"], "component_delta_explanation": "Reward only verified equipment customer order, delivery/backlog conversion, revenue and margin bridge; cap valuation/theme blowoff when the bridge fails to refresh.", "MFE_90D_pct": 43.99, "MAE_90D_pct": -5.65, "score_return_alignment_label": "valuation_blowoff_false_positive_bridge_gap", "current_profile_verdict": "C09 should cap overlay metrology/inspection equipment MFE when it is mostly valuation/theme beta. Without customer order, delivery, revenue conversion and margin bridge, Oros' early spike should be treated as local 4B/fade rather than durable Stage2."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 82, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "SEMICAP_ALD_METROLOGY_MEMORY_CAPEX_ORDER_BRIDGE_VS_VALUATION_BLOWOFF_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C09 advanced-equipment symbols outside top-covered 039030/042700/095340/Hanmi/Eo Technics set, +3 semicap/ALD/metrology trigger families, +1 semicap lifecycle candidate, +2 valuation blowoff local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 82, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "axis": "semicap_ALD_metrology_memory_capex_order_bridge_vs_valuation_blowoff_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C09 should split verified advanced-equipment order/revenue/margin rerating from generic semicap valuation blowoff. Stage2 requires memory capex or equipment premise, customer order/backlog, delivery schedule, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["240810", "036930", "322310"], "share_count_validation_required": ["036930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 82, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "existing_axis_strengthened": ["stage2_required_bridge", "customer_order_revenue_margin_bridge_required", "valuation_blowoff_local_4b_guard", "price_only_blowoff_blocks_positive_stage", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C09 needs advanced-equipment MFE to map into customer order, backlog/delivery, revenue and margin proof. Wonik IPS is a lifecycle candidate after source repair; Jusung and Oros show ALD/metrology valuation blowoff fading into local 4B when order/revenue bridge is absent or stale."}
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
240810:
  name = 원익IPS
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

036930:
  name = 주성엔지니어링 from 2008-01-11, 주성엔지니어 before that
  corporate_action_candidate_dates = 2000-06-22
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

322310:
  name = 오로스테크놀로지
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C09 rows are source_proxy_only / evidence_url_pending.
036930 requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C09 advanced-equipment valuation-blowoff rule-shape discovery,
but coding-agent promotion requires non-proxy customer order, backlog/delivery conversion, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C09 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 036930 needs share-count validation.

Candidate axis:
semicap_ALD_metrology_memory_capex_order_bridge_vs_valuation_blowoff_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 240810, 036930 and 322310.
4. Validate 036930 share-count changes inside the selected window.
5. Keep generic C09 advanced-equipment valuation weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - memory capex / equipment premise is explicit,
   - customer order or backlog is visible,
   - delivery schedule and revenue recognition exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is advanced-equipment theme beta only,
   - customer order / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer order cut, delivery delay, financing or margin break.
9. Emit before/after diagnostics and reject if verified semicap order positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 82
next_round = R3
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

