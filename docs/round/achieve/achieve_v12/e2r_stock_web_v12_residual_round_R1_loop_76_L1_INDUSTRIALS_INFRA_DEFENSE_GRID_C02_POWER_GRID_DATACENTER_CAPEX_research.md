# E2R Stock-Web v12 Residual Research — R1 Loop 76 / L1 / C02

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 76,
  "computed_next_round": "R2",
  "computed_next_loop": 76,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX",
  "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "power_grid_datacenter_capex_guardrail",
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

Previous completed state in this interactive run: R13 / loop 75.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 76
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
computed_next_round = R2
computed_next_loop = 76
```

R1 was routed away from C03/C04 because loop 75 used C04 and loop 74 used C03.  
This file tests C02 power-grid / datacenter-capex transformer and cable bridge behavior.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat lists C03 and C04 in the R1 table, while C02 is not present in the visible coverage slice. The duplicate rule still applies: new symbol and new trigger-family expansion is preferred.

Selected symbols:

```text
033100 / 제룡전기 / transformer export grid-capex backlog bridge
000500 / 가온전선 / power-cable grid-capex lifecycle bridge
006340 / 대원전선 / copper-cable grid theme spike fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
000500 has a 2024-11-11 corporate-action candidate, but the selected measurement window is kept before that action; extended validation must not cross it without adjustment.
```

## Research thesis

C02 is not “power-grid stock went up.”

The mechanism must pass through:

```text
grid / datacenter capex
→ transformer or cable order backlog
→ customer / delivery slot / ASP or copper pass-through
→ margin conversion
→ durable rerating
```

A grid headline is the thunder.  
The investable bridge is the transformer or cable order actually humming in the substation.

---

## Case 1 — Positive with lifecycle 4B: 033100 / 제룡전기

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is transformer export orders, grid/datacenter customer demand, backlog, delivery slots, ASP and margin evidence.

```text
evidence_family = TRANSFORMER_EXPORT_GRID_CAPEX_BACKLOG_ORDER_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-03-01
entry_date = 2024-03-04
entry_price = 21,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv`:

```text
2024-03-04,21750,27200,21750,27200
2024-04-24,53000,62000,51100,61500
2024-05-13,75800,80700,68300,71500
2024-07-11,98000,100700,94300,95900
2024-09-06,46700,47000,43850,44750
```

### Backtest

```text
MFE_30D  = +159.77%
MAE_30D  = +0.00%
MFE_90D  = +363.00%
MAE_90D  = +0.00%
MFE_180D = +363.00%
MAE_180D = +0.00%
peak_180 = 100,700 on 2024-07-11
trough_180 = 21,750 on 2024-03-04
peak_to_later_drawdown = -56.45%
```

### Interpretation

This is a very strong C02 positive-shaped path.  
The price path says transformer/grid-capex order backlog was powerful. But the later drawdown also says this should be lifecycle-managed.

Correct treatment:

```text
verified backlog / delivery / margin bridge → Stage2/Green possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Positive with lifecycle caveat: 000500 / 가온전선

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is power-cable export order, grid capex, copper pass-through, delivery and margin evidence.

```text
evidence_family = POWER_CABLE_GRID_CAPEX_EXPORT_ORDER_COPPER_COST_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch_and_corporate_action_caveat
trigger_date = 2024-01-24
entry_date = 2024-01-25
entry_price = 21,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv`:

```text
2024-01-25,21700,26900,20750,26250
2024-04-12,39450,48150,38500,44650
2024-05-13,66800,74500,64000,66300
2024-08-05,39500,39750,30900,32400
2024-09-06,30850,31200,29800,29800
```

### Backtest

```text
MFE_30D  = +35.71%
MAE_30D  = -4.38%
MFE_90D  = +243.32%
MAE_90D  = -4.38%
MFE_180D = +243.32%
MAE_180D = -4.38%
peak_180 = 74,500 on 2024-05-13
trough_180 = 20,750 on 2024-01-25
peak_to_later_drawdown = -60.00%
```

### Interpretation

This is the cable version of C02.  
It had controlled early MAE and very large MFE. But the later drawdown requires a lifecycle 4B guard if order/copper-pass-through/margin bridge fades.

---

## Case 3 — Counterexample / local 4B: 006340 / 대원전선

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests copper/cable/grid theme MFE without enough durable order-backlog or margin bridge.

```text
evidence_family = COPPER_CABLE_GRID_THEME_SPIKE_WITH_WEAK_ORDER_BACKLOG_MARGIN_BRIDGE
case_role = counterexample_theme_spike_local4b
trigger_date = 2024-04-04
entry_date = 2024-04-05
entry_price = 1,884
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv`:

```text
2024-04-05,1884,2095,1747,2095
2024-04-29,2970,3435,2870,3195
2024-05-13,4705,5450,4540,4885
2024-07-24,3575,3665,3515,3515
2024-09-09,2565,2760,2550,2735
```

### Backtest

```text
MFE_30D  = +189.28%
MAE_30D  = -7.27%
MFE_90D  = +189.28%
MAE_90D  = -7.27%
MFE_180D = +189.28%
MAE_180D = -7.27%
peak_180 = 5,450 on 2024-05-13
trough_180 = 1,747 on 2024-04-05
peak_to_later_drawdown = -53.21%
```

### Interpretation

This is not a bad-entry case. It is more dangerous: large MFE can fool the model into calling a theme spike Green.

Correct treatment:

```text
theme-spike MFE
→ source repair required
→ local 4B-watch after bridge fade
```

unless order backlog and margin bridge are verified.

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
do_not_raise_generic_C02_power_grid_weight = true
do_not_treat_all_cable_or_transformer_MFE_as_Green = true
do_not_convert_grid_equipment_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE
```

This fine archetype covers:

```text
1. transformer export / grid-capex backlog bridge → Stage2/Green possible after source repair
2. power cable / grid capex / copper pass-through bridge → Stage2 possible, with lifecycle decay
3. copper-cable grid theme spike without order/margin bridge → false Stage2 / local 4B after peak
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TransformerGridCapexBacklogBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should allow transformer suppliers when grid/datacenter capex converts into export order backlog, delivery slot, ASP and margin bridge. Jeryong Electric had extreme MFE and no entry-basis MAE, but later drawdown requires lifecycle local 4B if backlog/order evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy transformer/cable order, backlog, customer, delivery slot, ASP/copper pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CableGridCapexLifecycleBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should include cable suppliers only when grid capex, export order, copper pass-through and margin bridge are visible. Gaon Cable produced high MFE with controlled early MAE, but post-peak drawdown and a later 2024 corporate-action candidate require lifecycle and validation controls.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy transformer/cable order, backlog, customer, delivery slot, ASP/copper pass-through and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "case_type": "power_grid_datacenter_capex", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / CopperCableGridThemeSpikeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C02 should not treat copper/cable/grid theme spikes as durable Stage2 unless customer order, backlog, delivery and margin bridge are explicit. Daewon Cable had huge tradable MFE but then a deep post-peak drawdown, making it a theme-spike lifecycle local 4B row rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy transformer/cable order, backlog, customer, delivery slot, ASP/copper pass-through and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "case_id": "R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "symbol": "033100", "company_name": "제룡전기", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-Actionable-TransformerGridCapexBacklogBridge", "trigger_date": "2024-03-01", "entry_date": "2024-03-04", "entry_price": 21750.0, "evidence_available_at_that_date": "TRANSFORMER_EXPORT_GRID_CAPEX_BACKLOG_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JERYONG_ELECTRIC_2024_TRANSFORMER_EXPORT_GRID_DATACENTER_BACKLOG_ORDER_ASP_MARGIN_BRIDGE", "stage2_evidence_fields": ["power_grid_datacenter_capex", "order_backlog_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/033/033100/2024.csv", "profile_path": "atlas/symbol_profiles/033/033100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 159.77, "MFE_90D_pct": 363.0, "MFE_180D_pct": 363.0, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-07-11", "peak_price": 100700.0, "drawdown_after_peak_pct": -56.45, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_or_cable_peak_if_backlog_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_backlog_customer_ASP_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C02 should allow transformer suppliers when grid/datacenter capex converts into export order backlog, delivery slot, ASP and margin bridge. Jeryong Electric had extreme MFE and no entry-basis MAE, but later drawdown requires lifecycle local 4B if backlog/order evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_033100_2024-03-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "case_id": "R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "symbol": "000500", "company_name": "가온전선", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-Actionable-CableGridCapexLifecycleBridge", "trigger_date": "2024-01-24", "entry_date": "2024-01-25", "entry_price": 21700.0, "evidence_available_at_that_date": "POWER_CABLE_GRID_CAPEX_EXPORT_ORDER_COPPER_COST_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:GAON_CABLE_2024_POWER_CABLE_GRID_CAPEX_EXPORT_ORDER_COPPER_PASS_THROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["power_grid_datacenter_capex", "order_backlog_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000500/2024.csv", "profile_path": "atlas/symbol_profiles/000/000500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.71, "MFE_90D_pct": 243.32, "MFE_180D_pct": 243.32, "MAE_30D_pct": -4.38, "MAE_90D_pct": -4.38, "MAE_180D_pct": -4.38, "peak_date": "2024-05-13", "peak_price": 74500.0, "drawdown_after_peak_pct": -60.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_or_cable_peak_if_backlog_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_backlog_customer_ASP_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch_and_corporate_action_caveat", "current_profile_verdict": "C02 should include cable suppliers only when grid capex, export order, copper pass-through and margin bridge are visible. Gaon Cable produced high MFE with controlled early MAE, but post-peak drawdown and a later 2024 corporate-action candidate require lifecycle and validation controls.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_000500_2024-01-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "case_id": "R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "symbol": "006340", "company_name": "대원전선", "round": "R1", "loop": "76", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|power_grid_datacenter_capex_guardrail", "trigger_type": "Stage2-FalsePositive / CopperCableGridThemeSpikeFade", "trigger_date": "2024-04-04", "entry_date": "2024-04-05", "entry_price": 1884.0, "evidence_available_at_that_date": "COPPER_CABLE_GRID_THEME_SPIKE_WITH_WEAK_ORDER_BACKLOG_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DAEWON_CABLE_2024_COPPER_CABLE_GRID_THEME_ORDER_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["power_grid_datacenter_capex", "order_backlog_or_delivery_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_ASP_bridge_candidate"], "stage4b_evidence_fields": ["theme_spike", "bridge_stale_or_absent", "post_peak_drawdown", "MAE_widening"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006340/2024.csv", "profile_path": "atlas/symbol_profiles/006/006340.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 189.28, "MFE_90D_pct": 189.28, "MFE_180D_pct": 189.28, "MAE_30D_pct": -7.27, "MAE_90D_pct": -7.27, "MAE_180D_pct": -7.27, "peak_date": "2024-05-13", "peak_price": 5450.0, "drawdown_after_peak_pct": -53.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_grid_capex_or_cable_peak_if_backlog_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_backlog_customer_ASP_or_margin_break", "trigger_outcome_label": "counterexample_theme_spike_local4b", "current_profile_verdict": "C02 should not treat copper/cable/grid theme spikes as durable Stage2 unless customer order, backlog, delivery and margin bridge are explicit. Daewon Cable had huge tradable MFE but then a deep post-peak drawdown, making it a theme-spike lifecycle local 4B row rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_before_future_CA", "share_count_change_inside_window": false, "same_entry_group_id": "C02_GRID_CAPEX_006340_2024-04-05", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "trigger_id": "TRG_R1L76-C02-033100-JERYONG-TRANSFORMER-GRID-CAPEX-BACKLOG", "symbol": "033100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 14, "order_backlog_score": 15, "customer_quality_score": 13, "delivery_ASP_score": 13, "margin_bridge_score": 14, "relative_strength_score": 16, "execution_risk_score": 6, "theme_spike_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 88, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"grid_capex_score": 10, "order_backlog_score": 17, "customer_quality_score": 15, "delivery_ASP_score": 15, "margin_bridge_score": 16, "relative_strength_score": 15, "execution_risk_score": 7, "theme_spike_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 92, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_ASP_score", "margin_bridge_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified transformer/cable order backlog, customer quality, delivery/ASP and margin bridge; cap copper/cable theme MFE when bridge evidence is absent or stale.", "MFE_90D_pct": 363.0, "MAE_90D_pct": 0.0, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C02 should allow transformer suppliers when grid/datacenter capex converts into export order backlog, delivery slot, ASP and margin bridge. Jeryong Electric had extreme MFE and no entry-basis MAE, but later drawdown requires lifecycle local 4B if backlog/order evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "trigger_id": "TRG_R1L76-C02-000500-GAON-CABLE-GRID-CAPEX-LIFECYCLE", "symbol": "000500", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 14, "order_backlog_score": 15, "customer_quality_score": 13, "delivery_ASP_score": 13, "margin_bridge_score": 14, "relative_strength_score": 16, "execution_risk_score": 6, "theme_spike_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 88, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"grid_capex_score": 10, "order_backlog_score": 17, "customer_quality_score": 15, "delivery_ASP_score": 15, "margin_bridge_score": 16, "relative_strength_score": 15, "execution_risk_score": 7, "theme_spike_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 92, "stage_label_after": "Stage2/Green candidate after source repair + lifecycle 4B", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_ASP_score", "margin_bridge_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified transformer/cable order backlog, customer quality, delivery/ASP and margin bridge; cap copper/cable theme MFE when bridge evidence is absent or stale.", "MFE_90D_pct": 243.32, "MAE_90D_pct": -4.38, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C02 should include cable suppliers only when grid capex, export order, copper pass-through and margin bridge are visible. Gaon Cable produced high MFE with controlled early MAE, but post-peak drawdown and a later 2024 corporate-action candidate require lifecycle and validation controls."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "trigger_id": "TRG_R1L76-C02-006340-DAEWON-CABLE-COPPER-GRID-THEME-FADE", "symbol": "006340", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"grid_capex_score": 14, "order_backlog_score": 4, "customer_quality_score": 3, "delivery_ASP_score": 2, "margin_bridge_score": 2, "relative_strength_score": 16, "execution_risk_score": 18, "theme_spike_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 55, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"grid_capex_score": 10, "order_backlog_score": 2, "customer_quality_score": 2, "delivery_ASP_score": 1, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 21, "theme_spike_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 40, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["order_backlog_score", "customer_quality_score", "delivery_ASP_score", "margin_bridge_score", "theme_spike_risk_score"], "component_delta_explanation": "Reward only verified transformer/cable order backlog, customer quality, delivery/ASP and margin bridge; cap copper/cable theme MFE when bridge evidence is absent or stale.", "MFE_90D_pct": 189.28, "MAE_90D_pct": -7.27, "score_return_alignment_label": "false_positive_grid_cable_theme_bridge_gap", "current_profile_verdict": "C02 should not treat copper/cable/grid theme spikes as durable Stage2 unless customer order, backlog, delivery and margin bridge are explicit. Daewon Cable had huge tradable MFE but then a deep post-peak drawdown, making it a theme-spike lifecycle local 4B row rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 76, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "TRANSFORMER_CABLE_GRID_CAPEX_ORDER_MARGIN_BRIDGE_VS_COPPER_CABLE_THEME_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C02 grid/datacenter capex symbols outside C03/C04 loop-75 focus, +3 transformer/cable/copper-cable trigger families, +2 order/backlog positives, +1 copper-cable theme-spike local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 76, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "axis": "transformer_cable_grid_capex_order_margin_bridge_vs_copper_cable_theme_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C02 should split verified transformer/cable grid-capex order-backlog rerating from copper/cable theme beta. Stage2 requires customer/order backlog, delivery slot, ASP/copper pass-through and margin bridge. If MFE fades and post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["033100", "000500", "006340"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 76, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C02 needs order/backlog/margin proof. Jeryong Electric and Gaon Cable show transformer/cable grid-capex positives after source repair; Daewon Cable shows copper/cable theme MFE fading into local 4B when order/backlog/margin bridge is absent."}
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
033100:
  corporate_action_candidate_dates = 1999-11-30, 1999-12-27, 2000-02-21, 2000-08-30, 2006-01-06, 2007-08-31, 2011-11-28, 2014-11-06
  selected window = 2024-03-04~D+180
  contamination = false

000500:
  corporate_action_candidate_dates = 1997-01-03, 2022-11-08, 2024-11-11, 2025-02-20
  selected window = 2024-01-25~approximately D+180
  contamination = false for measured window before 2024-11-11
  caveat = extended validation must not cross 2024-11-11 without adjustment

006340:
  corporate_action_candidate_dates = 1996-11-29, 1997-06-19, 1999-09-10, 2000-03-21, 2007-01-25, 2010-05-07
  selected window = 2024-04-05~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C02 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C02 rule-shape discovery,
but coding-agent promotion requires non-proxy transformer/cable order, backlog, customer, delivery slot, ASP/copper pass-through and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C02 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
transformer_cable_grid_capex_order_margin_bridge_vs_copper_cable_theme_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 033100, 000500 and 006340.
4. Validate that 000500 measurement does not cross the 2024-11-11 corporate-action candidate without adjustment.
5. Keep generic C02 power-grid weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - grid/datacenter capex demand is explicit,
   - transformer/cable order backlog or delivery-slot bridge is visible,
   - customer, ASP/copper pass-through or margin bridge exists,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is cable/copper/grid theme beta only,
   - order/backlog/margin evidence is weak or stale,
   - post-peak drawdown <= -35%, even if entry-basis MAE is controlled.
8. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, customer loss, backlog cut, ASP/margin collapse, financing or capacity-execution break.
9. Emit before/after diagnostics and reject if verified transformer/cable backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 76
next_round = R2
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

