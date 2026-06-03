# E2R Stock-Web v12 Residual Research — R1 Loop 79 / L1 / C01

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 79,
  "computed_next_round": "R2",
  "computed_next_loop": 79,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "order_backlog_margin_bridge_guardrail",
    "ship_engine_backlog_margin_bridge_vs_construction_equipment_backlog_fade",
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

Previous completed state in this interactive run: R13 / loop 78.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 79
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
computed_next_round = R2
computed_next_loop = 79
```

R1 was routed to C01 because loop 78 used C02 and R11 used C04.  
This file tests order backlog / delivery / margin bridges in ship-engine and industrial equipment names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

This run uses three symbols outside recent L1 C02/C04 names:

```text
082740 / 한화엔진 / ship-engine backlog and margin bridge
077970 / STX엔진 / ship/defense-engine order backlog and delivery bridge
241560 / 두산밥캣 / construction-equipment backlog/channel fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
082740 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
```

## Research thesis

C01 is not “수주가 많다.”

The mechanism must pass through:

```text
order backlog
→ delivery slots / execution schedule
→ customer quality
→ revenue recognition
→ pricing and margin conversion
→ durable rerating
```

수주잔고는 창고에 쌓인 원재료다.  
C01이 보려는 것은 그 원재료가 납기, 매출 인식, 마진으로 제련되는지다.

---

## Case 1 — Positive with validation: 082740 / 한화엔진

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is ship-engine order backlog, LNG/dual-fuel delivery slots, pricing and margin bridge evidence.

```text
evidence_family = SHIP_ENGINE_LNG_DUALFUEL_ORDER_BACKLOG_DELIVERY_SLOT_MARGIN_BRIDGE
case_role = positive_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv`:

```text
2024-02-01,8600,8640,8210,8360
2024-02-20,8030,8150,7990,8060
2024-03-15,9670,9910,9320,9500
2024-04-24,12710,13890,12410,12450
2024-06-25,16030,16990,15500,15820
2024-08-05,13250,13300,11000,12000
2024-10-17,15820,16500,15450,16140
```

### Backtest

```text
MFE_30D  = +15.23%
MAE_30D  = -7.09%
MFE_90D  = +61.51%
MAE_90D  = -7.09%
MFE_180D = +97.56%
MAE_180D = -7.09%
peak_180 = 16,990 on 2024-06-25
trough_180 = 7,990 on 2024-02-20
peak_to_later_drawdown = -35.26%
```

### Interpretation

This is a C01 ship-engine backlog positive after validation.  
The price path supports a real order-backlog/margin candidate, but runtime promotion needs source repair and share-count continuity checks.

Correct treatment:

```text
verified order backlog / delivery slot / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 077970 / STX엔진

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is ship/defense engine order backlog, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = SHIP_ENGINE_DEFENSE_ENGINE_ORDER_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,480
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv`:

```text
2024-02-01,11480,11710,11480,11670
2024-02-23,12950,13100,12610,12800
2024-03-14,12960,13800,12960,13560
2024-03-20,13650,13840,13550,13800
2024-08-05,15000,15050,12880,13690
2024-08-19,22250,24400,21200,23000
2024-09-06,18010,18180,17140,17550
```

### Backtest

```text
MFE_30D  = +14.11%
MAE_30D  = +0.00%
MFE_90D  = +20.64%
MAE_90D  = +0.00%
MFE_180D = +112.54%
MAE_180D = +0.00%
peak_180 = 24,400 on 2024-08-19
trough_180 = 11,480 on 2024-02-01
peak_to_later_drawdown = -29.75%
```

### Interpretation

This is a clean C01 backlog-margin positive.  
The MFE expanded without entry-basis MAE.

Correct treatment:

```text
verified engine backlog / customer quality / delivery / revenue bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 241560 / 두산밥캣

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests construction-equipment backlog/channel beta without enough dealer inventory, order intake and margin bridge.

```text
evidence_family = CONSTRUCTION_EQUIPMENT_ORDER_BACKLOG_CHANNEL_INVENTORY_MARGIN_BRIDGE_WEAK_REFRESH
case_role = counterexample_construction_equipment_backlog_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 50,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv`:

```text
2024-02-01,50500,50700,47850,49300
2024-02-21,47750,47800,44400,44500
2024-03-14,49050,52300,48800,51600
2024-03-27,50200,57300,50200,56100
2024-07-25,47000,47950,41150,44150
2024-08-05,38400,38700,33350,34250
2024-10-25,39150,39150,37700,37800
```

### Backtest

```text
MFE_30D  = +4.55%
MAE_30D  = -12.08%
MFE_90D  = +13.47%
MAE_90D  = -12.08%
MFE_180D = +13.47%
MAE_180D = -33.96%
peak_180 = 57,300 on 2024-03-27
trough_180 = 33,350 on 2024-08-05
peak_to_later_drawdown = -41.80%
```

### Interpretation

This is a C01 false-positive boundary.  
A modest backlog beta did not validate durable margin conversion.

Correct treatment:

```text
construction-equipment backlog/channel beta
→ no verified order intake / dealer inventory / margin bridge
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
do_not_raise_generic_C01_order_backlog_weight = true
do_not_treat_all_order_backlog_MFE_as_Green = true
do_not_convert_order_backlog_drawdown_to_hard_4C_without_non_price_order_delivery_margin_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE
```

This fine archetype covers:

```text
1. ship-engine backlog / delivery slot / margin bridge → Stage2 possible after source repair
2. ship-defense engine backlog / delivery bridge → Stage2 possible, lifecycle-managed
3. construction-equipment backlog/channel beta without refreshed margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ShipEngineBacklogMarginBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should allow industrial ship-engine positives when shipbuilding orderbook maps to engine order backlog, delivery slots, pricing, revenue recognition and margin conversion. Hanwha Engine produced a large MFE, but raw share-count movement inside the window requires validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy order backlog, delivery slots, customer quality, revenue recognition, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-ShipEngineDefenseEngineBacklogMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should preserve ship/defense engine suppliers when order backlog, delivery schedule, customer quality, revenue recognition and margin bridge are visible. STX Engine produced high MFE with essentially no entry-basis MAE, but lifecycle local 4B is needed if backlog or margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy order backlog, delivery slots, customer quality, revenue recognition, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE", "symbol": "241560", "company_name": "두산밥캣", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ConstructionEquipmentBacklogMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should not treat construction-equipment backlog/channel beta as durable Stage2 unless dealer inventory, order intake, utilization, pricing and margin bridge refreshes. Doosan Bobcat had a modest MFE and then a high-MAE drawdown, making it a local 4B-watch row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy order backlog, delivery slots, customer quality, revenue recognition, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN", "case_id": "R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-ShipEngineBacklogMarginBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8600.0, "evidence_available_at_that_date": "SHIP_ENGINE_LNG_DUALFUEL_ORDER_BACKLOG_DELIVERY_SLOT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_ENGINE_2024_SHIP_ENGINE_ORDER_BACKLOG_DELIVERY_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_or_revenue_recognition_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["order_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv", "profile_path": "atlas/symbol_profiles/082/082740.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.23, "MFE_90D_pct": 61.51, "MFE_180D_pct": 97.56, "MAE_30D_pct": -7.09, "MAE_90D_pct": -7.09, "MAE_180D_pct": -7.09, "peak_date": "2024-06-25", "peak_price": 16990.0, "drawdown_after_peak_pct": -35.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_order_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C01 should allow industrial ship-engine positives when shipbuilding orderbook maps to engine order backlog, delivery slots, pricing, revenue recognition and margin conversion. Hanwha Engine produced a large MFE, but raw share-count movement inside the window requires validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C01_ORDER_BACKLOG_082740_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN", "case_id": "R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-ShipEngineDefenseEngineBacklogMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11480.0, "evidence_available_at_that_date": "SHIP_ENGINE_DEFENSE_ENGINE_ORDER_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:STX_ENGINE_2024_SHIP_DEFENSE_ENGINE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_or_revenue_recognition_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["order_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv", "profile_path": "atlas/symbol_profiles/077/077970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.11, "MFE_90D_pct": 20.64, "MFE_180D_pct": 112.54, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-08-19", "peak_price": 24400.0, "drawdown_after_peak_pct": -29.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_order_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C01 should preserve ship/defense engine suppliers when order backlog, delivery schedule, customer quality, revenue recognition and margin bridge are visible. STX Engine produced high MFE with essentially no entry-basis MAE, but lifecycle local 4B is needed if backlog or margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDER_BACKLOG_077970_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE", "case_id": "R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE", "symbol": "241560", "company_name": "두산밥캣", "round": "R1", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / ConstructionEquipmentBacklogMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 50500.0, "evidence_available_at_that_date": "CONSTRUCTION_EQUIPMENT_ORDER_BACKLOG_CHANNEL_INVENTORY_MARGIN_BRIDGE_WEAK_REFRESH", "evidence_source": "source_proxy_manual_verification_required:DOOSAN_BOBCAT_2024_CONSTRUCTION_EQUIPMENT_ORDER_BACKLOG_DEALER_INVENTORY_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_or_revenue_recognition_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_pricing_bridge_candidate"], "stage4b_evidence_fields": ["order_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv", "profile_path": "atlas/symbol_profiles/241/241560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.55, "MFE_90D_pct": 13.47, "MFE_180D_pct": 13.47, "MAE_30D_pct": -12.08, "MAE_90D_pct": -12.08, "MAE_180D_pct": -33.96, "peak_date": "2024-03-27", "peak_price": 57300.0, "drawdown_after_peak_pct": -41.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_order_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_construction_equipment_backlog_local4b", "current_profile_verdict": "C01 should not treat construction-equipment backlog/channel beta as durable Stage2 unless dealer inventory, order intake, utilization, pricing and margin bridge refreshes. Doosan Bobcat had a modest MFE and then a high-MAE drawdown, making it a local 4B-watch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDER_BACKLOG_241560_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN", "trigger_id": "TRG_R1L79-C01-082740-HANWHA-ENGINE-SHIP-ENGINE-BACKLOG-MARGIN", "symbol": "082740", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 15, "delivery_schedule_score": 14, "customer_quality_score": 13, "pricing_revenue_score": 13, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"order_backlog_score": 17, "delivery_schedule_score": 16, "customer_quality_score": 15, "pricing_revenue_score": 15, "margin_bridge_score": 16, "relative_strength_score": 14, "execution_risk_score": 9, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "delivery_schedule_score", "customer_quality_score", "pricing_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, delivery schedule, customer quality, pricing/revenue recognition and margin bridge; cap order/backlog theme beta when evidence fails to refresh.", "MFE_90D_pct": 61.51, "MAE_90D_pct": -7.09, "score_return_alignment_label": "order_backlog_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C01 should allow industrial ship-engine positives when shipbuilding orderbook maps to engine order backlog, delivery slots, pricing, revenue recognition and margin conversion. Hanwha Engine produced a large MFE, but raw share-count movement inside the window requires validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN", "trigger_id": "TRG_R1L79-C01-077970-STX-ENGINE-ORDER-BACKLOG-DELIVERY-MARGIN", "symbol": "077970", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 15, "delivery_schedule_score": 14, "customer_quality_score": 13, "pricing_revenue_score": 13, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"order_backlog_score": 17, "delivery_schedule_score": 16, "customer_quality_score": 15, "pricing_revenue_score": 15, "margin_bridge_score": 16, "relative_strength_score": 14, "execution_risk_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "delivery_schedule_score", "customer_quality_score", "pricing_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, delivery schedule, customer quality, pricing/revenue recognition and margin bridge; cap order/backlog theme beta when evidence fails to refresh.", "MFE_90D_pct": 20.64, "MAE_90D_pct": 0.0, "score_return_alignment_label": "order_backlog_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C01 should preserve ship/defense engine suppliers when order backlog, delivery schedule, customer quality, revenue recognition and margin bridge are visible. STX Engine produced high MFE with essentially no entry-basis MAE, but lifecycle local 4B is needed if backlog or margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE", "trigger_id": "TRG_R1L79-C01-241560-DOOSAN-BOBCAT-CONSTRUCTION-EQUIPMENT-BACKLOG-FADE", "symbol": "241560", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 5, "delivery_schedule_score": 3, "customer_quality_score": 3, "pricing_revenue_score": 2, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 22, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"order_backlog_score": 3, "delivery_schedule_score": 1, "customer_quality_score": 1, "pricing_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["order_backlog_score", "delivery_schedule_score", "customer_quality_score", "pricing_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, delivery schedule, customer quality, pricing/revenue recognition and margin bridge; cap order/backlog theme beta when evidence fails to refresh.", "MFE_90D_pct": 13.47, "MAE_90D_pct": -12.08, "score_return_alignment_label": "false_positive_order_backlog_bridge_gap", "current_profile_verdict": "C01 should not treat construction-equipment backlog/channel beta as durable Stage2 unless dealer inventory, order intake, utilization, pricing and margin bridge refreshes. Doosan Bobcat had a modest MFE and then a high-MAE drawdown, making it a local 4B-watch row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_AND_EQUIPMENT_ORDER_BACKLOG_MARGIN_BRIDGE_VS_CONSTRUCTION_EQUIPMENT_BACKLOG_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C01 ship-engine / construction-equipment order-backlog symbols outside recent C02/C04 L1 names, +3 ship-engine/defense-engine/construction-equipment trigger families, +2 backlog-margin positives, +1 construction-equipment backlog local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "axis": "ship_engine_and_equipment_order_backlog_margin_bridge_vs_construction_equipment_backlog_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C01 should split verified order-backlog / delivery / margin rerating from generic industrial backlog beta. Stage2 requires order backlog, delivery slots, customer quality, revenue recognition, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["082740", "077970", "241560"], "share_count_validation_required": ["082740"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C01 needs order backlog, delivery, revenue recognition and margin proof. Hanwha Engine and STX Engine show ship-engine backlog-margin positives after source repair; Doosan Bobcat shows construction-equipment backlog/channel beta fading into local 4B when dealer inventory, order intake and margin bridge are absent or stale."}
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
082740:
  name = 한화엔진 from 2024-03-15, HSD엔진 before that
  corporate_action_candidate_dates = 2018-06-19, 2021-03-17, 2022-08-25
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

077970:
  name = STX엔진
  corporate_action_candidate_dates = 2005-11-29, 2013-10-16, 2015-05-07, 2025-04-21
  selected window = 2024-02-01~D+180
  contamination = false

241560:
  name = 두산밥캣
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C01 rows are source_proxy_only / evidence_url_pending.
082740 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C01 rule-shape discovery,
but coding-agent promotion requires non-proxy order backlog, delivery slot, customer quality, revenue recognition, pricing and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C01 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 082740 needs share-count validation.

Candidate axis:
ship_engine_and_equipment_order_backlog_margin_bridge_vs_construction_equipment_backlog_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 082740, 077970 and 241560.
4. Validate 082740 share-count changes inside the selected window.
5. Keep generic C01 order-backlog weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - order backlog is explicit,
   - delivery slot or execution schedule is visible,
   - customer quality is visible,
   - revenue recognition and pricing bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is order/backlog theme beta only,
   - delivery/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, delivery delay, customer loss, pricing failure, financing or margin break.
9. Emit before/after diagnostics and reject if verified low-MAE backlog-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 79
next_round = R2
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

