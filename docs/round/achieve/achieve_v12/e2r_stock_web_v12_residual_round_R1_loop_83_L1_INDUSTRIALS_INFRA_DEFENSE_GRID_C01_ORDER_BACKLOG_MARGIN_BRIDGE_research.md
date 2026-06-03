# E2R Stock-Web v12 Residual Research — R1 Loop 83 / L1 / C01

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 83,
  "computed_next_round": "R2",
  "computed_next_loop": 83,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "industrial_order_backlog_margin_bridge_guardrail",
    "marine_engine_customer_order_delivery_revenue_margin_bridge",
    "construction_equipment_orderbook_cycle_fade_boundary",
    "share_count_name_change_validation_queue_creation",
    "bounded_positive_lifecycle_guard",
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

Previous completed state in this interactive run: R13 / loop 82.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 83
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
computed_next_round = R2
computed_next_loop = 83
```

R1 was routed to C01 because loop 82 R1 used C03, loop 81 R1 used C04, and loop 80 R1 used C02.  
This file tests industrial / marine-engine / equipment orderbacklog margin bridges rather than defense-export framework or power-grid capex.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C01 concentration in:

```text
009540, 010620, 001440, 010120, 010140, 267260
```

This run uses three different symbols:

```text
077970 / STX엔진 / marine-engine orderbacklog delivery margin bridge
082740 / 한화엔진 / large marine-engine backlog with name/share-count validation
241560 / 두산밥캣 / construction-equipment orderbacklog cycle fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
082740 has name change and share-count movement inside the selected 2024 window, so coding-agent validation is required before runtime promotion.
```

## Research thesis

C01 is not “산업재가 올랐다.”

The mechanism must pass through:

```text
industrial / shipbuilding / equipment headline
→ customer or program order backlog
→ delivery schedule
→ revenue recognition
→ margin bridge
→ durable rerating
```

산업재 수주는 뉴스의 굉음이 아니라 납기표와 원가표가 맞물리는 톱니바퀴다.  
C01이 보려는 것은 headline이 실제 수주잔고, 납품, 매출, 마진으로 돌아가는지다.

---

## Case 1 — Marine-engine orderbacklog positive: 077970 / STX엔진

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is marine/naval/commercial engine orderbacklog, customer/program quality, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = MARINE_ENGINE_NAVAL_COMMERCIAL_ENGINE_ORDERBACKLOG_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_marine_engine_orderbacklog_margin_bridge_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 11,480
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv`:

```text
2024-02-01,11480,11710,11480,11670
2024-02-19,12400,12690,12300,12670
2024-03-14,12960,13800,12960,13560
2024-07-24,17300,17300,16720,17080
2024-08-05,15000,15050,12880,13690
2024-08-16,16650,21550,16420,21550
2024-08-19,22250,24400,21200,23000
2024-09-06,18010,18180,17140,17550
2024-10-22,21500,22000,21000,21500
```

### Backtest

```text
MFE_30D  = +20.64%
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

This is a strong C01 marine-engine backlog candidate after source repair.  
The price path had very large MFE and effectively no entry-basis MAE, but the post-peak drawdown means the bridge must refresh.

Correct treatment:

```text
verified marine-engine backlog / customer-program / delivery / revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Marine-engine lifecycle candidate with validation: 082740 / 한화엔진

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
name_change_validation_required = true
source_repair_required = true
```

The source-repair task is shipbuilding customer orderbook, large-engine delivery schedule, revenue conversion and margin bridge evidence.

```text
evidence_family = LARGE_MARINE_ENGINE_ORDERBACKLOG_SHIPBUILDING_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_WITH_NAME_SHARECOUNT_VALIDATION
case_role = positive_marine_engine_backlog_lifecycle_with_name_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 8,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv`:

```text
2024-02-01,8600,8640,8210,8360
2024-02-20,8030,8150,7990,8060
2024-02-28,8520,9170,8370,9090
2024-03-14,8770,9750,8770,9570
2024-03-20,9700,9950,9620,9950
2024-07-24,16900,17160,15880,15880
2024-08-05,13250,13300,11000,12000
2024-10-17,15820,16500,15450,16140
```

### Backtest

```text
MFE_30D  = +15.70%
MAE_30D  = -7.09%
MFE_90D  = +18.84%
MAE_90D  = -7.09%
MFE_180D = +99.53%
MAE_180D = -7.09%
peak_180 = 17,160 on 2024-07-24
trough_180 = 7,990 on 2024-02-20
peak_to_later_drawdown = -35.90%
```

### Interpretation

This is a C01 marine-engine backlog lifecycle candidate with data validation blockers.  
The price path is strong enough to protect after source repair, but the name/share-count transition means runtime promotion must wait.

Correct treatment:

```text
verified shipbuilding orderbook / engine delivery / revenue / margin bridge → Stage2-Yellow possible
name/share-count validation first
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

This row tests construction-equipment backlog/cycle beta without enough dealer-channel, inventory, production and margin bridge.

```text
evidence_family = CONSTRUCTION_EQUIPMENT_ORDERBOOK_INVENTORY_DEALER_CHANNEL_RENTAL_DEMAND_MARGIN_THEME_WITH_WEAK_REVENUE_BRIDGE
case_role = counterexample_construction_equipment_orderbacklog_cycle_fade_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 50,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv`:

```text
2024-02-01,50500,50700,47850,49300
2024-02-08,50200,50200,46150,46300
2024-02-21,47750,47800,44400,44500
2024-03-14,49050,52300,48800,51600
2024-03-27,50200,57300,50200,56100
2024-08-05,38400,38700,33350,34250
2024-08-29,43250,45950,40050,42050
2024-10-25,39150,39150,37700,37800
```

### Backtest

```text
MFE_30D  = +3.96%
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

This is a C01 equipment-cycle false-positive boundary.  
The initial MFE was modest and the later high-MAE path indicates that orderbacklog/revenue/margin bridge did not refresh.

Correct treatment:

```text
construction-equipment cycle beta
→ no verified dealer inventory / rental demand / production / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
industrial_order_backlog_bridge_required = strengthen
customer_program_delivery_revenue_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
name_share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C01_industrial_theme_weight = true
do_not_treat_all_industrial_MFE_as_Green = true
do_not_ingest_name_or_sharecount_changed_rows_without_validation = true
do_not_convert_equipment_cycle_drawdown_to_hard_4C_without_non_price_order_cancellation_customer_loss_delivery_delay_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE
```

This fine archetype covers:

```text
1. marine-engine customer/program backlog and delivery bridge → Stage2 possible after source repair
2. marine-engine lifecycle candidate with name/share-count validation → Stage2-Yellow possible after validation
3. construction-equipment cycle beta without revenue/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-MarineEngineOrderBacklogDeliveryRevenueMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should protect industrial orderbacklog positives only when customer/program backlog, delivery schedule, revenue recognition and margin bridge are visible. STX Engine produced very large MFE with effectively no entry-basis MAE, but post-peak drawdown still requires lifecycle 4B if order/delivery/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer/program backlog, delivery schedule, revenue recognition, dealer/channel inventory or production scheduling and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-MarineEngineOrderBacklogDeliveryRevenueBridgeWithNameSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 can protect marine-engine positives when shipbuilding customer orderbook, delivery schedule, revenue conversion and margin bridge are visible. Hanwha Engine had large MFE and controlled early MAE, but 2024 name/share-count continuity must be validated before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer/program backlog, delivery schedule, revenue recognition, dealer/channel inventory or production scheduling and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE", "symbol": "241560", "company_name": "두산밥캣", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "case_type": "order_backlog_margin_bridge", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ConstructionEquipmentBacklogMarginCycleFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C01 should not treat construction-equipment backlog/cycle beta as durable Stage2 unless dealer channel inventory, rental demand, production scheduling, revenue conversion and margin bridge are visible. Doosan Bobcat had modest MFE and then high MAE, so it is local 4B-watch unless the bridge is repaired.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer/program backlog, delivery schedule, revenue recognition, dealer/channel inventory or production scheduling and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN", "case_id": "R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN", "symbol": "077970", "company_name": "STX엔진", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|industrial_order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-MarineEngineOrderBacklogDeliveryRevenueMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 11480.0, "evidence_available_at_that_date": "MARINE_ENGINE_NAVAL_COMMERCIAL_ENGINE_ORDERBACKLOG_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:STX_ENGINE_2024_MARINE_ENGINE_ORDERBACKLOG_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_channel_candidate"], "stage4b_evidence_fields": ["industrial_cycle_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/077/077970/2024.csv", "profile_path": "atlas/symbol_profiles/077/077970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.64, "MFE_90D_pct": 20.64, "MFE_180D_pct": 112.54, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-08-19", "peak_price": 24400.0, "drawdown_after_peak_pct": -29.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_delivery_delay_financing_or_margin_break", "trigger_outcome_label": "positive_marine_engine_orderbacklog_margin_bridge_with_later_4b_watch", "current_profile_verdict": "C01 should protect industrial orderbacklog positives only when customer/program backlog, delivery schedule, revenue recognition and margin bridge are visible. STX Engine produced very large MFE with effectively no entry-basis MAE, but post-peak drawdown still requires lifecycle 4B if order/delivery/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_name_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDER_BACKLOG_077970_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT", "case_id": "R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT", "symbol": "082740", "company_name": "한화엔진", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|industrial_order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-Lifecycle-MarineEngineOrderBacklogDeliveryRevenueBridgeWithNameSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 8600.0, "evidence_available_at_that_date": "LARGE_MARINE_ENGINE_ORDERBACKLOG_SHIPBUILDING_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE_WITH_NAME_SHARECOUNT_VALIDATION", "evidence_source": "source_proxy_manual_verification_required:HANWHA_ENGINE_2024_MARINE_ENGINE_ORDERBACKLOG_SHIPBUILDING_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_channel_candidate"], "stage4b_evidence_fields": ["industrial_cycle_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/082/082740/2024.csv", "profile_path": "atlas/symbol_profiles/082/082740.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.7, "MFE_90D_pct": 18.84, "MFE_180D_pct": 99.53, "MAE_30D_pct": -7.09, "MAE_90D_pct": -7.09, "MAE_180D_pct": -7.09, "peak_date": "2024-07-24", "peak_price": 17160.0, "drawdown_after_peak_pct": -35.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_delivery_delay_financing_or_margin_break", "trigger_outcome_label": "positive_marine_engine_backlog_lifecycle_with_name_sharecount_validation", "current_profile_verdict": "C01 can protect marine-engine positives when shipbuilding customer orderbook, delivery schedule, revenue conversion and margin bridge are visible. Hanwha Engine had large MFE and controlled early MAE, but 2024 name/share-count continuity must be validated before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_name_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C01_ORDER_BACKLOG_082740_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE", "case_id": "R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE", "symbol": "241560", "company_name": "두산밥캣", "round": "R1", "loop": "83", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|industrial_order_backlog_margin_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / ConstructionEquipmentBacklogMarginCycleFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 50500.0, "evidence_available_at_that_date": "CONSTRUCTION_EQUIPMENT_ORDERBOOK_INVENTORY_DEALER_CHANNEL_RENTAL_DEMAND_MARGIN_THEME_WITH_WEAK_REVENUE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DOOSAN_BOBCAT_2024_CONSTRUCTION_EQUIPMENT_ORDERBOOK_DEALER_INVENTORY_RENTAL_DEMAND_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["order_backlog_candidate", "delivery_schedule_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_channel_candidate"], "stage4b_evidence_fields": ["industrial_cycle_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/241/241560/2024.csv", "profile_path": "atlas/symbol_profiles/241/241560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.96, "MFE_90D_pct": 13.47, "MFE_180D_pct": 13.47, "MAE_30D_pct": -12.08, "MAE_90D_pct": -12.08, "MAE_180D_pct": -33.96, "peak_date": "2024-03-27", "peak_price": 57300.0, "drawdown_after_peak_pct": -41.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_industrial_backlog_peak_if_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_customer_loss_delivery_delay_financing_or_margin_break", "trigger_outcome_label": "counterexample_construction_equipment_orderbacklog_cycle_fade_local4b", "current_profile_verdict": "C01 should not treat construction-equipment backlog/cycle beta as durable Stage2 unless dealer channel inventory, rental demand, production scheduling, revenue conversion and margin bridge are visible. Doosan Bobcat had modest MFE and then high MAE, so it is local 4B-watch unless the bridge is repaired.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_name_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C01_ORDER_BACKLOG_241560_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN", "trigger_id": "TRG_R1L83-C01-077970-STX-ENGINE-MARINE-ENGINE-BACKLOG-MARGIN", "symbol": "077970", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 14, "customer_program_score": 13, "delivery_schedule_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 14, "sharecount_or_name_validation_risk": 0, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair and validation", "raw_component_scores_after": {"order_backlog_score": 16, "customer_program_score": 15, "delivery_schedule_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 13, "sharecount_or_name_validation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_program_score", "delivery_schedule_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, customer/program quality, delivery schedule, revenue conversion and margin bridge; cap industrial-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 20.64, "MAE_90D_pct": 0.0, "score_return_alignment_label": "industrial_orderbacklog_positive_with_lifecycle_4b", "current_profile_verdict": "C01 should protect industrial orderbacklog positives only when customer/program backlog, delivery schedule, revenue recognition and margin bridge are visible. STX Engine produced very large MFE with effectively no entry-basis MAE, but post-peak drawdown still requires lifecycle 4B if order/delivery/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT", "trigger_id": "TRG_R1L83-C01-082740-HANWHA-ENGINE-MARINE-ENGINE-BACKLOG-NAME-SHARECOUNT", "symbol": "082740", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 14, "customer_program_score": 13, "delivery_schedule_score": 13, "revenue_conversion_score": 13, "margin_bridge_score": 13, "relative_strength_score": 14, "sharecount_or_name_validation_risk": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair and validation", "raw_component_scores_after": {"order_backlog_score": 16, "customer_program_score": 15, "delivery_schedule_score": 15, "revenue_conversion_score": 15, "margin_bridge_score": 15, "relative_strength_score": 13, "sharecount_or_name_validation_risk": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_program_score", "delivery_schedule_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, customer/program quality, delivery schedule, revenue conversion and margin bridge; cap industrial-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 18.84, "MAE_90D_pct": -7.09, "score_return_alignment_label": "industrial_orderbacklog_positive_with_lifecycle_4b", "current_profile_verdict": "C01 can protect marine-engine positives when shipbuilding customer orderbook, delivery schedule, revenue conversion and margin bridge are visible. Hanwha Engine had large MFE and controlled early MAE, but 2024 name/share-count continuity must be validated before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE", "trigger_id": "TRG_R1L83-C01-241560-DOOSAN-BOBCAT-EQUIPMENT-CYCLE-FADE", "symbol": "241560", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 4, "customer_program_score": 3, "delivery_schedule_score": 2, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "sharecount_or_name_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"order_backlog_score": 2, "customer_program_score": 1, "delivery_schedule_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "sharecount_or_name_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["order_backlog_score", "customer_program_score", "delivery_schedule_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified order backlog, customer/program quality, delivery schedule, revenue conversion and margin bridge; cap industrial-cycle theme beta when bridge fails to refresh.", "MFE_90D_pct": 13.47, "MAE_90D_pct": -12.08, "score_return_alignment_label": "false_positive_industrial_cycle_bridge_gap", "current_profile_verdict": "C01 should not treat construction-equipment backlog/cycle beta as durable Stage2 unless dealer channel inventory, rental demand, production scheduling, revenue conversion and margin bridge are visible. Doosan Bobcat had modest MFE and then high MAE, so it is local 4B-watch unless the bridge is repaired."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 83, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MARINE_ENGINE_INDUSTRIAL_EQUIPMENT_ORDERBACKLOG_DELIVERY_MARGIN_BRIDGE_VS_CYCLE_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "name_change_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C01 symbols outside top-covered 009540/010620/001440/010120/010140/267260 set, +3 marine-engine/large-engine/construction-equipment trigger families, +2 backlog positives, +1 equipment-cycle local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_name_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 83, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "axis": "marine_engine_industrial_equipment_orderbacklog_delivery_margin_bridge_vs_cycle_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C01 should split verified marine-engine / industrial-equipment orderbacklog margin rerating from generic industrial cycle beta. Stage2 requires customer/program backlog, delivery schedule, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Name/share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["077970", "082740", "241560"], "share_count_validation_required": ["082740"], "name_change_validation_required": ["082740"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 83, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "existing_axis_strengthened": ["stage2_required_bridge", "industrial_order_backlog_bridge_required", "customer_program_delivery_revenue_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "name_share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C01 needs industrial backlog MFE to map into customer/program backlog, delivery schedule, revenue recognition and margin proof. STX Engine and Hanwha Engine are marine-engine backlog positives after source repair and validation; Doosan Bobcat shows construction-equipment cycle beta fading into local 4B when order/revenue/margin bridge is absent or stale."}
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
077970:
  name = STX엔진
  corporate_action_candidate_dates = 2005-11-29, 2013-10-16, 2015-05-07, 2025-04-21
  selected window = 2024-02-01~D+180
  contamination = false

082740:
  current name = 한화엔진
  name history = HSD엔진 until 2024-03-14, 한화엔진 from 2024-03-15
  corporate_action_candidate_dates = 2018-06-19, 2021-03-17, 2022-08-25
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
  name_change_inside_window = true → coding-agent validation required

241560:
  name = 두산밥캣
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C01 rows are source_proxy_only / evidence_url_pending.
082740 requires name/share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C01 orderbacklog bridge rule-shape discovery,
but coding-agent promotion requires non-proxy customer/program backlog, delivery schedule, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C01 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 082740 needs name/share-count validation.

Candidate axis:
marine_engine_industrial_equipment_orderbacklog_delivery_margin_bridge_vs_cycle_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 077970, 082740 and 241560.
4. Validate 082740 name-change and share-count movement inside the selected window.
5. Keep generic C01 industrial/orderbacklog weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer/program backlog is explicit,
   - delivery schedule is visible,
   - revenue recognition exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is industrial equipment/cycle beta only,
   - customer order / delivery / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, customer loss, delivery delay, financing or margin break.
9. Emit before/after diagnostics and reject if verified marine-engine backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 83
next_round = R2
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

