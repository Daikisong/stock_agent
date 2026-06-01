# E2R Stock-Web v12 Residual Research — R2 Loop 79 / L2 / C09

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 79,
  "computed_next_round": "R3",
  "computed_next_loop": 79,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF",
  "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "advanced_equipment_valuation_blowoff_guardrail",
    "order_quality_customer_capacity_bridge_vs_valuation_blowoff",
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

Previous completed state in this interactive run: R1 / loop 79.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 79
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
computed_next_round = R3
computed_next_loop = 79
```

R2 was routed to C09 because loop 78 used C08.  
This file tests advanced-equipment order quality vs valuation blowoff rather than test-socket customer quality.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C09 is concentrated in:

```text
039030, 042700, 095340, 이오테크닉스, 한미반도체
```

This run uses three different symbols:

```text
240810 / 원익IPS / advanced equipment order-quality positive
403870 / HPSP / advanced equipment valuation blowoff
036930 / 주성엔지니어링 / advanced equipment theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
403870 and 036930 show share-count changes inside the selected window and require coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C09 is not “반도체 장비주가 올랐다.”

The mechanism must pass through:

```text
advanced process / HBM / customer capex demand
→ tool order or backlog
→ delivery schedule and customer quality
→ capacity or utilization bridge
→ pricing and margin conversion
→ valuation discipline
```

장비주 MFE는 불꽃이다.  
C09가 보려는 것은 그 불꽃이 수주잔고, 납기, 고객 투자, 마진으로 계속 공급되는지, 아니면 산소가 끊긴 valuation blowoff인지다.

---

## Case 1 — Protected equipment-order candidate: 240810 / 원익IPS

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is advanced-equipment order backlog, customer quality, delivery schedule and margin bridge evidence.

```text
evidence_family = ADVANCED_SEMI_EQUIPMENT_ORDER_BACKLOG_CUSTOMER_QUALITY_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
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
2024-10-25,28850,28850,26950,27200
```

### Backtest

```text
MFE_30D  = +17.66%
MAE_30D  = -5.94%
MFE_90D  = +48.02%
MAE_90D  = -5.94%
MFE_180D = +48.02%
MAE_180D = -11.06%
peak_180 = 44,850 on 2024-04-08
trough_180 = 26,950 on 2024-10-25
peak_to_later_drawdown = -39.91%
```

### Interpretation

This is a protected C09 candidate, not a pure blowoff.  
The drawdown after the peak still requires lifecycle management, but the entry-basis MAE was bounded.

Correct treatment:

```text
verified tool order / customer quality / delivery / margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Valuation blowoff / local 4B: 403870 / HPSP

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is advanced process equipment order, customer capacity, HBM/logic capex bridge, pricing and margin evidence.

```text
evidence_family = ADVANCED_PROCESS_EQUIPMENT_HBM_THEME_VALUATION_BLOWOFF_WITH_WEAK_REFRESHED_ORDER_MARGIN_BRIDGE
case_role = valuation_blowoff_local4b_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 44,950
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv`:

```text
2024-02-01,44950,46250,44300,44900
2024-02-07,45650,46150,43800,44000
2024-02-13,49400,62400,49250,59300
2024-02-15,62400,63900,59200,63100
2024-04-05,46750,47350,45850,46700
2024-08-05,28350,28750,22650,23450
2024-09-09,24050,24650,23700,24450
```

### Backtest

```text
MFE_30D  = +42.16%
MAE_30D  = -2.56%
MFE_90D  = +42.16%
MAE_90D  = -2.56%
MFE_180D = +42.16%
MAE_180D = -49.61%
peak_180 = 63,900 on 2024-02-15
trough_180 = 22,650 on 2024-08-05
peak_to_later_drawdown = -64.55%
```

### Interpretation

This is the clean C09 valuation blowoff row.  
The MFE was real, but the later collapse says price outran refreshed order/margin proof.

Correct treatment:

```text
advanced-equipment theme MFE
→ missing/stale order-capacity-margin refresh
→ local 4B-watch
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

This row tests advanced deposition/equipment theme beta without enough customer order and margin refresh.

```text
evidence_family = ADVANCED_DEPOSITION_EQUIPMENT_HBM_THEME_WITH_WEAK_CUSTOMER_ORDER_MARGIN_REFRESH
case_role = counterexample_advanced_equipment_theme_local4b
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
2024-04-08,38450,41450,36200,41650
2024-06-28,35350,39050,34600,37350
2024-08-05,25700,26000,22150,23200
2024-09-10,23050,23050,22050,22300
```

### Backtest

```text
MFE_30D  = +23.48%
MAE_30D  = -18.48%
MFE_90D  = +25.61%
MAE_90D  = -18.48%
MFE_180D = +25.61%
MAE_180D = -32.88%
peak_180 = 41,450 on 2024-04-08
trough_180 = 22,150 on 2024-08-05
peak_to_later_drawdown = -46.56%
```

### Interpretation

This is a C09 false-positive boundary.  
The first equipment-theme move was tradable, but it did not validate durable order/customer-capacity rerating.

Correct treatment:

```text
advanced deposition/equipment theme beta
→ no refreshed customer order / capacity / margin bridge
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
do_not_raise_generic_C09_equipment_theme_weight = true
do_not_treat_all_advanced_equipment_MFE_as_Green = true
do_not_convert_equipment_drawdown_to_hard_4C_without_non_price_order_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE
```

This fine archetype covers:

```text
1. advanced-equipment order/customer bridge with bounded MAE → Stage2 possible after source repair
2. advanced-process equipment MFE without refreshed order/margin bridge → valuation blowoff / local 4B
3. deposition/equipment theme beta without customer bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AdvancedEquipmentOrderQualityBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should not block advanced-equipment positives when customer quality, tool order/backlog, delivery schedule, utilization/customer capacity and margin bridge are visible. Wonik IPS produced a meaningful MFE with bounded MAE, so it is a protected candidate after source repair rather than a pure blowoff.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy equipment order, customer quality, delivery, capacity, valuation and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "valuation_blowoff_local4b", "best_trigger": "Stage4B-Local-AdvancedEquipmentValuationBlowoffWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should detect advanced-equipment valuation blowoff when a large MFE arrives before refreshed tool order, customer capacity and margin evidence. HPSP produced a huge early MFE and then a deep MAE/post-peak drawdown; runtime ingestion also needs share-count validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy equipment order, customer quality, delivery, capacity, valuation and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "case_type": "advanced_equipment_valuation_blowoff", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AdvancedEquipmentThemeValuationFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C09 should not treat advanced deposition/equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery, customer capacity and margin bridge refreshes. Jusung Engineering had a tradable MFE, then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy equipment order, customer quality, delivery, capacity, valuation and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE", "case_id": "R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE", "symbol": "240810", "company_name": "원익IPS", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage2-Actionable-AdvancedEquipmentOrderQualityBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 30300.0, "evidence_available_at_that_date": "ADVANCED_SEMI_EQUIPMENT_ORDER_BACKLOG_CUSTOMER_QUALITY_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WONIK_IPS_2024_ADVANCED_SEMI_EQUIPMENT_ORDER_BACKLOG_CUSTOMER_QUALITY_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["equipment_order_or_backlog_candidate", "customer_quality_or_capacity_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv", "profile_path": "atlas/symbol_profiles/240/240810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.66, "MFE_90D_pct": 48.02, "MFE_180D_pct": 48.02, "MAE_30D_pct": -5.94, "MAE_90D_pct": -5.94, "MAE_180D_pct": -11.06, "peak_date": "2024-04-08", "peak_price": 44850.0, "drawdown_after_peak_pct": -39.91, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_peak_if_order_customer_capacity_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C09 should not block advanced-equipment positives when customer quality, tool order/backlog, delivery schedule, utilization/customer capacity and margin bridge are visible. Wonik IPS produced a meaningful MFE with bounded MAE, so it is a protected candidate after source repair rather than a pure blowoff.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_240810_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF", "case_id": "R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF", "symbol": "403870", "company_name": "HPSP", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage4B-Local-AdvancedEquipmentValuationBlowoffWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 44950.0, "evidence_available_at_that_date": "ADVANCED_PROCESS_EQUIPMENT_HBM_THEME_VALUATION_BLOWOFF_WITH_WEAK_REFRESHED_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HPSP_2024_ADVANCED_PROCESS_EQUIPMENT_HBM_ORDER_CUSTOMER_CAPACITY_MARGIN_BRIDGE_BLOWOFF", "stage2_evidence_fields": ["equipment_order_or_backlog_candidate", "customer_quality_or_capacity_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403870/2024.csv", "profile_path": "atlas/symbol_profiles/403/403870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.16, "MFE_90D_pct": 42.16, "MFE_180D_pct": 42.16, "MAE_30D_pct": -2.56, "MAE_90D_pct": -2.56, "MAE_180D_pct": -49.61, "peak_date": "2024-02-15", "peak_price": 63900.0, "drawdown_after_peak_pct": -64.55, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_peak_if_order_customer_capacity_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "valuation_blowoff_local4b_with_sharecount_validation", "current_profile_verdict": "C09 should detect advanced-equipment valuation blowoff when a large MFE arrives before refreshed tool order, customer capacity and margin evidence. HPSP produced a huge early MFE and then a deep MAE/post-peak drawdown; runtime ingestion also needs share-count validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_403870_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE", "case_id": "R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE", "symbol": "036930", "company_name": "주성엔지니어링", "round": "R2", "loop": "79", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|advanced_equipment_valuation_blowoff_guardrail", "trigger_type": "Stage2-FalsePositive / AdvancedEquipmentThemeValuationFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 33000.0, "evidence_available_at_that_date": "ADVANCED_DEPOSITION_EQUIPMENT_HBM_THEME_WITH_WEAK_CUSTOMER_ORDER_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:JUSUNG_ENGINEERING_2024_ADVANCED_DEPOSITION_EQUIPMENT_CUSTOMER_ORDER_CAPACITY_MARGIN_BRIDGE", "stage2_evidence_fields": ["equipment_order_or_backlog_candidate", "customer_quality_or_capacity_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "delivery_schedule_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["equipment_theme_beta", "valuation_blowoff", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv", "profile_path": "atlas/symbol_profiles/036/036930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.48, "MFE_90D_pct": 25.61, "MFE_180D_pct": 25.61, "MAE_30D_pct": -18.48, "MAE_90D_pct": -18.48, "MAE_180D_pct": -32.88, "peak_date": "2024-04-08", "peak_price": 41450.0, "drawdown_after_peak_pct": -46.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_equipment_peak_if_order_customer_capacity_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cut_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_advanced_equipment_theme_local4b", "current_profile_verdict": "C09 should not treat advanced deposition/equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery, customer capacity and margin bridge refreshes. Jusung Engineering had a tradable MFE, then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C09_ADVANCED_EQUIPMENT_036930_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE", "trigger_id": "TRG_R2L79-C09-240810-WONIKIPS-ADVANCED-EQUIPMENT-ORDER-QUALITY-POSITIVE", "symbol": "240810", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"equipment_order_score": 14, "customer_quality_score": 13, "delivery_capacity_score": 13, "valuation_risk_score": 6, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"equipment_order_score": 16, "customer_quality_score": 15, "delivery_capacity_score": 15, "valuation_risk_score": 8, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_capacity_score", "valuation_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advanced-equipment order/customer/capacity/margin bridge; cap or route to local 4B when valuation blowoff appears without refreshed order or margin proof.", "MFE_90D_pct": 48.02, "MAE_90D_pct": -5.94, "score_return_alignment_label": "equipment_order_quality_positive_with_lifecycle_4b", "current_profile_verdict": "C09 should not block advanced-equipment positives when customer quality, tool order/backlog, delivery schedule, utilization/customer capacity and margin bridge are visible. Wonik IPS produced a meaningful MFE with bounded MAE, so it is a protected candidate after source repair rather than a pure blowoff."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF", "trigger_id": "TRG_R2L79-C09-403870-HPSP-ADVANCED-EQUIPMENT-VALUATION-BLOWOFF", "symbol": "403870", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"equipment_order_score": 5, "customer_quality_score": 3, "delivery_capacity_score": 3, "valuation_risk_score": 22, "margin_bridge_score": 2, "relative_strength_score": 12, "execution_risk_score": 22, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage4B-local-watch / valuation blowoff", "raw_component_scores_after": {"equipment_order_score": 3, "customer_quality_score": 1, "delivery_capacity_score": 1, "valuation_risk_score": 25, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_capacity_score", "valuation_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advanced-equipment order/customer/capacity/margin bridge; cap or route to local 4B when valuation blowoff appears without refreshed order or margin proof.", "MFE_90D_pct": 42.16, "MAE_90D_pct": -2.56, "score_return_alignment_label": "valuation_blowoff_or_false_positive_equipment_theme", "current_profile_verdict": "C09 should detect advanced-equipment valuation blowoff when a large MFE arrives before refreshed tool order, customer capacity and margin evidence. HPSP produced a huge early MFE and then a deep MAE/post-peak drawdown; runtime ingestion also needs share-count validation."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE", "trigger_id": "TRG_R2L79-C09-036930-JUSUNG-ADVANCED-EQUIPMENT-THEME-BLOWOFF-FADE", "symbol": "036930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "raw_component_scores_before": {"equipment_order_score": 5, "customer_quality_score": 3, "delivery_capacity_score": 3, "valuation_risk_score": 22, "margin_bridge_score": 2, "relative_strength_score": 5, "execution_risk_score": 22, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage4B-local-watch / valuation blowoff", "raw_component_scores_after": {"equipment_order_score": 3, "customer_quality_score": 1, "delivery_capacity_score": 1, "valuation_risk_score": 25, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["equipment_order_score", "customer_quality_score", "delivery_capacity_score", "valuation_risk_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified advanced-equipment order/customer/capacity/margin bridge; cap or route to local 4B when valuation blowoff appears without refreshed order or margin proof.", "MFE_90D_pct": 25.61, "MAE_90D_pct": -18.48, "score_return_alignment_label": "valuation_blowoff_or_false_positive_equipment_theme", "current_profile_verdict": "C09 should not treat advanced deposition/equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery, customer capacity and margin bridge refreshes. Jusung Engineering had a tradable MFE, then opened a high-MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 79, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "fine_archetype_id": "ADVANCED_SEMI_EQUIPMENT_ORDER_QUALITY_VALUATION_BLOWOFF_VS_EQUIPMENT_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "valuation_blowoff_local4b_count": 1, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "current_profile_error_count": 2, "diversity_score_summary": "+3 C09 advanced-equipment symbols outside top-covered 039030/042700/095340/이오테크닉스/한미반도체 set, +3 Wonik/HPSP/Jusung trigger families, +1 protected low-MAE equipment-order positive, +2 valuation blowoff/local-4B boundaries, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 79, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "axis": "advanced_semi_equipment_order_quality_valuation_blowoff_vs_equipment_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C09 should split verified advanced-equipment order/customer-quality rerating from valuation blowoff and generic equipment theme beta. Stage2 requires order/backlog, delivery schedule, customer quality/capacity, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["240810", "403870", "036930"], "share_count_validation_required": ["403870", "036930"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 79, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C09 needs equipment order, customer quality, delivery/capacity and margin proof. Wonik IPS shows a bounded-MAE equipment-order candidate after source repair; HPSP and Jusung Engineering show advanced-equipment valuation/theme MFE fading into local 4B when refreshed order and margin bridge are absent or stale."}
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

403870:
  name = HPSP
  corporate_action_candidate_dates = 2023-03-16, 2023-04-11
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
  market_segment = KOSDAQ until 2024-06-13, KOSDAQ GLOBAL from 2024-06-14

036930:
  name = 주성엔지니어링 from 2008-01-11
  corporate_action_candidate_dates = 2000-06-22
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
```

Data-quality caveat:

```text
All selected C09 rows are source_proxy_only / evidence_url_pending.
403870 and 036930 also require share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C09 rule-shape discovery,
but coding-agent promotion requires non-proxy equipment order, customer quality, delivery/capacity, pricing and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C09 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 403870/036930 need share-count validation.

Candidate axis:
advanced_semi_equipment_order_quality_valuation_blowoff_vs_equipment_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 240810, 403870 and 036930.
4. Validate 403870 and 036930 share-count changes inside the selected window.
5. Keep generic C09 advanced-equipment/valuation-blowoff weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - equipment order/backlog is explicit,
   - customer quality or customer capacity is visible,
   - delivery schedule or pricing bridge exists,
   - margin bridge is credible,
   - valuation risk is not already blowoff-like,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is advanced-equipment theme beta only,
   - order/customer/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cut, customer loss, delivery delay, pricing collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified low-MAE equipment-order positives are overblocked.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 79
next_round = R3
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

