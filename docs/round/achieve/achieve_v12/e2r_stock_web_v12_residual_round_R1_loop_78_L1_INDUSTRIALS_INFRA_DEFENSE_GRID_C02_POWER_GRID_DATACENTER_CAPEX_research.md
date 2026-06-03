# E2R Stock-Web v12 Residual Research — R1 Loop 78 / L1 / C02

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 78,
  "computed_next_round": "R2",
  "computed_next_loop": 78,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "power_grid_datacenter_capex_guardrail",
    "cable_transformer_backlog_margin_bridge_vs_electrical_theme_beta",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "post_corporate_action_validation_queue_creation"
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

Previous completed state in this interactive run: R13 / loop 77.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 78
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
computed_next_round = R2
computed_next_loop = 78
```

R1 was routed to C02 because loop 77 used C01 on R1 and C03 on R11.  
This file tests power cable / transformer / switchgear paths tied to grid and data-center capex.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Visible No-Repeat R1 concentration:

```text
C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

This run uses three symbols outside the recent loop-77 R1/R11 names:

```text
103590 / 일진전기 / post-CA power cable-transformer capex backlog bridge
000500 / 가온전선 / power cable / datacenter grid capex bridge
017040 / 광명전기 / switchgear electrical-equipment theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
103590 has a 2024-02-13 corporate-action candidate, so the selected trigger starts 2024-02-14 after that candidate date.
000500 has a future 2024-11-11 corporate-action candidate, after the selected 180D calibration window.
```

## Research thesis

C02 is not “전력기기주가 올랐다.”

The mechanism must pass through:

```text
grid / datacenter capex demand
→ customer orderbook and delivery slot
→ ASP, copper pass-through or product mix
→ margin conversion
→ durable rerating
```

전력망 테마는 전압이다.  
C02가 보려는 것은 그 전압이 실제 발주서, 납기표, 단가, 마진으로 흐르는 회로다.

---

## Case 1 — Positive after CA validation: 103590 / 일진전기

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
post_corporate_action_validation_required = true
source_repair_required = true
```

The source-repair task is power cable / transformer orderbook, delivery schedule, ASP/copper pass-through and margin bridge evidence.

```text
evidence_family = POWER_CABLE_TRANSFORMER_DATACENTER_GRID_CAPEX_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_POST_CA
case_role = positive_with_post_CA_validation_and_lifecycle_4b_watch
trigger_date = 2024-02-13
entry_date = 2024-02-14
entry_price = 11,790
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv`:

```text
2024-02-13,11600,11980,11530,11920
2024-02-14,11790,12100,11630,11780
2024-02-19,10800,10940,10310,10380
2024-03-28,20600,22400,20200,20450
2024-05-29,29050,30250,27100,28600
2024-09-09,16740,18570,16600,18360
```

### Backtest

```text
MFE_30D  = +89.99%
MAE_30D  = -12.55%
MFE_90D  = +156.57%
MAE_90D  = -12.55%
MFE_180D = +156.57%
MAE_180D = -12.55%
peak_180 = 30,250 on 2024-05-29
trough_180 = 10,310 on 2024-02-19
peak_to_later_drawdown = -45.12%
```

### Interpretation

This is a C02 positive after post-CA validation.  
The MFE path validates a tradable grid/cable/transformer rerating candidate, but runtime promotion needs source repair and continuity validation.

Correct treatment:

```text
verified orderbook / delivery / ASP / margin bridge → Stage2 possible
post-CA validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 000500 / 가온전선

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is power cable orderbook, data-center/grid customer demand, ASP/copper pass-through and margin evidence.

```text
evidence_family = POWER_CABLE_DATACENTER_GRID_CAPEX_CUSTOMER_ORDERBOOK_ASP_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_future_CA_caveat
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 22,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv`:

```text
2024-02-01,22400,23950,22250,22800
2024-02-14,24150,24400,23600,24100
2024-03-13,27950,32000,27600,29100
2024-04-12,39450,48150,38500,44650
2024-05-13,66800,74500,64000,66300
2024-07-22,45500,45800,41750,42550
```

### Backtest

```text
MFE_30D  = +42.86%
MAE_30D  = -2.01%
MFE_90D  = +232.59%
MAE_90D  = -2.01%
MFE_180D = +232.59%
MAE_180D = -2.01%
peak_180 = 74,500 on 2024-05-13
trough_180 = 21,950 around 2024-01-31~2024-02-01
peak_to_later_drawdown = -43.96%
```

### Interpretation

This is a powerful cable/grid capex positive, but not permanent Green.  
The later drawdown after a huge MFE says the model must ask whether orderbook, ASP and margin evidence refreshed.

Correct treatment:

```text
Stage2 possible after source repair
future CA caveat for extended validation
lifecycle local 4B if orderbook/margin bridge fades
```

---

## Case 3 — Counterexample / local 4B: 017040 / 광명전기

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests switchgear / electrical-equipment theme beta without enough customer order, backlog and margin bridge.

```text
evidence_family = SWITCHGEAR_ELECTRICAL_EQUIPMENT_GRID_THEME_WITH_WEAK_ORDER_BACKLOG_MARGIN_BRIDGE
case_role = counterexample_switchgear_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 2,140
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv`:

```text
2024-02-01,2140,2185,2140,2180
2024-03-05,2555,2640,2355,2385
2024-04-08,2525,2885,2510,2715
2024-05-07,2685,3270,2670,3185
2024-05-08,3090,3320,3020,3060
2024-08-05,1935,1999,1614,1744
2024-10-25,1452,1464,1390,1391
```

### Backtest

```text
MFE_30D  = +23.36%
MAE_30D  = +0.00%
MFE_90D  = +55.14%
MAE_90D  = +0.00%
MFE_180D = +55.14%
MAE_180D = -35.05%
peak_180 = 3,320 on 2024-05-08
trough_180 = 1,390 on 2024-10-25
peak_to_later_drawdown = -58.13%
```

### Interpretation

This is the C02 false-positive boundary.  
The theme MFE was real, but it did not prove durable grid/datacenter capex rerating.

Correct treatment:

```text
switchgear/electrical theme beta
→ no verified order / backlog / delivery / margin bridge
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
corporate_action_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C02_grid_theme_weight = true
do_not_treat_all_power_equipment_MFE_as_Green = true
do_not_convert_grid_equipment_drawdown_to_hard_4C_without_non_price_order_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE
```

This fine archetype covers:

```text
1. power cable / transformer post-CA orderbacklog bridge → Stage2 possible after source repair and validation
2. power cable / datacenter grid capex bridge → Stage2 possible, lifecycle-managed
3. switchgear electrical-equipment theme beta without backlog/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-PostCAPowerCableTransformerBacklogBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should allow power cable/transformer names when datacenter/grid capex maps to order backlog, delivery slots, ASP/copper pass-through and margin bridge. Iljin Electric produced very large MFE after the 2024-02-13 corporate-action candidate; runtime promotion requires post-CA continuity validation and source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, delivery slot, ASP/copper pass-through, customer quality and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-PowerCableDatacenterGridCapexBacklogBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should include cable names only when grid/datacenter capex maps to customer orderbook, cable shipment, ASP/copper pass-through and margin bridge. Gaon Cable produced high MFE with controlled entry-basis MAE, but the later drawdown requires lifecycle local 4B if orderbook/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, delivery slot, ASP/copper pass-through, customer quality and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SwitchgearElectricalThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should not treat switchgear/electrical-equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery schedule, ASP and margin bridge are visible. Kwangmyung Electric produced a strong theme MFE, then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy grid/datacenter capex, order backlog, delivery slot, ASP/copper pass-through, customer quality and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA", "case_id": "R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-Actionable-PostCAPowerCableTransformerBacklogBridgeWithLifecycle4B", "trigger_date": "2024-02-13", "entry_date": "2024-02-14", "entry_price": 11790.0, "evidence_available_at_that_date": "POWER_CABLE_TRANSFORMER_DATACENTER_GRID_CAPEX_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_POST_CA", "evidence_source": "source_proxy_manual_verification_required:ILJIN_ELECTRIC_2024_POWER_CABLE_TRANSFORMER_DATACENTER_GRID_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_POST_CA", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_delivery_slot_candidate", "ASP_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_copper_pass_through_candidate"], "stage4b_evidence_fields": ["grid_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "profile_path": "atlas/symbol_profiles/103/103590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 89.99, "MFE_90D_pct": 156.57, "MFE_180D_pct": 156.57, "MAE_30D_pct": -12.55, "MAE_90D_pct": -12.55, "MAE_180D_pct": -12.55, "peak_date": "2024-05-29", "peak_price": 30250.0, "drawdown_after_peak_pct": -45.12, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_with_post_CA_validation_and_lifecycle_4b_watch", "current_profile_verdict": "C02 should allow power cable/transformer names when datacenter/grid capex maps to order backlog, delivery slots, ASP/copper pass-through and margin bridge. Iljin Electric produced very large MFE after the 2024-02-13 corporate-action candidate; runtime promotion requires post-CA continuity validation and source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": true, "same_entry_group_id": "C02_GRID_CAPEX_103590_2024-02-14", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG", "case_id": "R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-Actionable-PowerCableDatacenterGridCapexBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 22400.0, "evidence_available_at_that_date": "POWER_CABLE_DATACENTER_GRID_CAPEX_CUSTOMER_ORDERBOOK_ASP_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:GAON_CABLE_2024_DATACENTER_GRID_POWER_CABLE_ORDERBOOK_ASP_MARGIN_BRIDGE", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_delivery_slot_candidate", "ASP_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_copper_pass_through_candidate"], "stage4b_evidence_fields": ["grid_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv", "profile_path": "atlas/symbol_profiles/000/000500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 42.86, "MFE_90D_pct": 232.59, "MFE_180D_pct": 232.59, "MAE_30D_pct": -2.01, "MAE_90D_pct": -2.01, "MAE_180D_pct": -2.01, "peak_date": "2024-05-13", "peak_price": 74500.0, "drawdown_after_peak_pct": -43.96, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_future_CA_caveat", "current_profile_verdict": "C02 should include cable names only when grid/datacenter capex maps to customer orderbook, cable shipment, ASP/copper pass-through and margin bridge. Gaon Cable produced high MFE with controlled entry-basis MAE, but the later drawdown requires lifecycle local 4B if orderbook/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_000500_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE", "case_id": "R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE", "symbol": "017040", "company_name": "광명전기", "round": "R1", "loop": "78", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-FalsePositive / SwitchgearElectricalThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 2140.0, "evidence_available_at_that_date": "SWITCHGEAR_ELECTRICAL_EQUIPMENT_GRID_THEME_WITH_WEAK_ORDER_BACKLOG_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KWANGMYUNG_ELECTRIC_2024_SWITCHGEAR_ELECTRICAL_EQUIPMENT_GRID_ORDER_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["grid_datacenter_capex_candidate", "order_backlog_delivery_slot_candidate", "ASP_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_copper_pass_through_candidate"], "stage4b_evidence_fields": ["grid_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017040/2024.csv", "profile_path": "atlas/symbol_profiles/017/017040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.36, "MFE_90D_pct": 55.14, "MFE_180D_pct": 55.14, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -35.05, "peak_date": "2024-05-08", "peak_price": 3320.0, "drawdown_after_peak_pct": -58.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_peak_if_order_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_delivery_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_switchgear_theme_local4b", "current_profile_verdict": "C02 should not treat switchgear/electrical-equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery schedule, ASP and margin bridge are visible. Kwangmyung Electric produced a strong theme MFE, then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_or_post_CA_validated_window_required", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_017040_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA", "trigger_id": "TRG_R1L78-C02-103590-ILJIN-ELECTRIC-POWER-CABLE-TRANSFORMER-POST-CA", "symbol": "103590", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_datacenter_capex_score": 14, "order_backlog_score": 14, "delivery_slot_score": 13, "ASP_copper_pass_through_score": 12, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "post_CA_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"grid_datacenter_capex_score": 16, "order_backlog_score": 16, "delivery_slot_score": 15, "ASP_copper_pass_through_score": 14, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "post_CA_validation_risk": 12, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "delivery_slot_score", "ASP_copper_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, delivery slots, ASP/copper pass-through and margin bridge; cap electrical theme beta when evidence fails to refresh.", "MFE_90D_pct": 156.57, "MAE_90D_pct": -12.55, "score_return_alignment_label": "grid_datacenter_capex_positive_with_lifecycle_4b", "current_profile_verdict": "C02 should allow power cable/transformer names when datacenter/grid capex maps to order backlog, delivery slots, ASP/copper pass-through and margin bridge. Iljin Electric produced very large MFE after the 2024-02-13 corporate-action candidate; runtime promotion requires post-CA continuity validation and source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG", "trigger_id": "TRG_R1L78-C02-000500-GAON-CABLE-DATACENTER-GRID-CABLE-BACKLOG", "symbol": "000500", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_datacenter_capex_score": 14, "order_backlog_score": 14, "delivery_slot_score": 13, "ASP_copper_pass_through_score": 12, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"grid_datacenter_capex_score": 16, "order_backlog_score": 16, "delivery_slot_score": 15, "ASP_copper_pass_through_score": 14, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "delivery_slot_score", "ASP_copper_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, delivery slots, ASP/copper pass-through and margin bridge; cap electrical theme beta when evidence fails to refresh.", "MFE_90D_pct": 232.59, "MAE_90D_pct": -2.01, "score_return_alignment_label": "grid_datacenter_capex_positive_with_lifecycle_4b", "current_profile_verdict": "C02 should include cable names only when grid/datacenter capex maps to customer orderbook, cable shipment, ASP/copper pass-through and margin bridge. Gaon Cable produced high MFE with controlled entry-basis MAE, but the later drawdown requires lifecycle local 4B if orderbook/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE", "trigger_id": "TRG_R1L78-C02-017040-KWANGMYUNG-ELECTRIC-SWITCHGEAR-THEME-FADE", "symbol": "017040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_datacenter_capex_score": 6, "order_backlog_score": 4, "delivery_slot_score": 3, "ASP_copper_pass_through_score": 3, "margin_bridge_score": 2, "relative_strength_score": 8, "execution_risk_score": 20, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"grid_datacenter_capex_score": 4, "order_backlog_score": 2, "delivery_slot_score": 2, "ASP_copper_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 23, "post_CA_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["order_backlog_score", "delivery_slot_score", "ASP_copper_pass_through_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified grid/datacenter capex, order backlog, delivery slots, ASP/copper pass-through and margin bridge; cap electrical theme beta when evidence fails to refresh.", "MFE_90D_pct": 55.14, "MAE_90D_pct": 0.0, "score_return_alignment_label": "false_positive_grid_theme_bridge_gap", "current_profile_verdict": "C02 should not treat switchgear/electrical-equipment theme beta as durable Stage2 unless customer order, backlog conversion, delivery schedule, ASP and margin bridge are visible. Kwangmyung Electric produced a strong theme MFE, then opened a high-MAE drawdown path, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "POWER_CABLE_TRANSFORMER_DATACENTER_CAPEX_BACKLOG_BRIDGE_VS_SWITCHGEAR_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "post_corporate_action_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C02 grid/cable/switchgear symbols outside recent loop-77 R1/R11 C01/C03 names, +3 cable/transformer/switchgear trigger families, +2 grid capex positives, +1 electrical theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_post_CA_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "axis": "power_cable_transformer_datacenter_capex_backlog_bridge_vs_switchgear_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C02 should split verified power-grid/datacenter capex order-backlog rerating from generic electrical-equipment theme beta. Stage2 requires grid/datacenter capex demand, customer orderbook, delivery slot, ASP/copper pass-through and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Post-CA entries require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["103590", "000500", "017040"], "post_corporate_action_validation_required": ["103590"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 78, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "corporate_action_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C02 needs grid/datacenter orderbacklog and margin proof. Iljin Electric and Gaon Cable show power cable/datacenter capex MFE candidates after source repair; Kwangmyung Electric shows switchgear/electrical theme beta fading into local 4B when order, delivery and margin bridge are absent."}
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
103590:
  name = 일진전기
  corporate_action_candidate_dates = 2024-02-13
  selected window starts 2024-02-14 after the 2024-02-13 candidate
  contamination = false after post-CA entry, but coding-agent validation required

000500:
  name = 가온전선
  corporate_action_candidate_dates = 1997-01-03, 2022-11-08, 2024-11-11, 2025-02-20
  selected window = 2024-02-01~D+180, before 2024-11-11
  contamination = false for selected 180D window
  caveat = extended validation must not cross 2024-11-11 without adjustment

017040:
  name = 광명전기
  corporate_action_candidate_dates = 2000-01-24, 2000-04-25, 2001-12-10
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C02 rows are source_proxy_only / evidence_url_pending.
103590 requires post-corporate-action validation.
This MD is useful for stock-web path calibration and C02 rule-shape discovery,
but coding-agent promotion requires non-proxy grid/datacenter capex, order backlog, delivery slot, ASP/copper pass-through, customer quality and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C02 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 103590 needs post-CA validation.

Candidate axis:
power_cable_transformer_datacenter_capex_backlog_bridge_vs_switchgear_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 103590, 000500 and 017040.
4. Validate 103590 post-CA continuity after the 2024-02-13 corporate-action candidate.
5. Keep generic C02 grid/datacenter capex weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - grid/datacenter capex demand is explicit,
   - customer orderbook and delivery slot are visible,
   - ASP/copper pass-through or product mix bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is electrical-equipment or grid theme beta only,
   - order/backlog/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, customer loss, delivery delay, pricing/copper pass-through failure, financing or margin break.
9. Emit before/after diagnostics and reject if verified low-MAE power cable/backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 78
next_round = R2
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

