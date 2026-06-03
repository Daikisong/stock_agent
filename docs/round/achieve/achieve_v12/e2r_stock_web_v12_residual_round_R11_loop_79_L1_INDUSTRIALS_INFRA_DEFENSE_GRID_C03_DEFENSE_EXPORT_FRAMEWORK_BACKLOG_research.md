# E2R Stock-Web v12 Residual Research — R11 Loop 79 / L1 / C03

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 79,
  "computed_next_round": "R12",
  "computed_next_loop": 79,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "defense_export_framework_backlog_guardrail",
    "export_framework_backlog_delivery_margin_bridge",
    "defense_theme_backlog_gap_boundary",
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

Previous completed state in this interactive run: R10 / loop 79.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 79
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
computed_next_round = R12
computed_next_loop = 79
```

R11 was routed to L1 because this run focuses on policy-defense/export framework linkage rather than a generic R13 cross-archetype checkpoint.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C03 concentration in:

```text
012450, 079550, 047810, 065450
```

This run uses three different symbols:

```text
064350 / 현대로템 / ground-system export framework and backlog bridge
103140 / 풍산 / ammunition export demand and margin bridge
010820 / 퍼스텍 / defense/drone component theme backlog gap
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C03 is not “방산주가 올랐다.”

The mechanism must pass through:

```text
defense policy / export framework
→ named customer or project
→ order backlog
→ delivery schedule and revenue recognition
→ margin bridge
→ durable rerating
```

방산 export framework는 계약서의 표지다.  
C03이 보려는 것은 그 표지 안에 실제 고객, 납기표, 잔고, 매출 인식, 마진이 있는지다.

---

## Case 1 — Ground-system positive: 064350 / 현대로템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is K2/ground-system export framework, named customer, backlog, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = GROUND_SYSTEM_K2_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_export_framework_backlog_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 28,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv`:

```text
2024-02-01,28100,28650,27400,27500
2024-02-02,27600,27600,26950,27150
2024-02-22,30900,34500,30350,34500
2024-04-12,41850,43450,40750,41600
2024-07-29,49500,50900,48900,49950
2024-10-18,67400,68000,64600,65000
2024-11-01,61800,62900,60200,61500
```

### Backtest

```text
MFE_30D  = +22.78%
MAE_30D  = -4.09%
MFE_90D  = +54.63%
MAE_90D  = -4.09%
MFE_180D = +141.99%
MAE_180D = -4.09%
peak_180 = 68,000 on 2024-10-18
trough_180 = 26,950 on 2024-02-02
peak_to_later_drawdown = -11.47%
```

### Interpretation

This is a C03 ground-system export/backlog positive.  
The MFE was very large while entry-basis MAE stayed controlled.

Correct treatment:

```text
verified export framework / named customer / backlog / delivery / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Ammo/export positive: 103140 / 풍산

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is ammunition export demand, backlog, shipment cadence, copper/raw-material spread, revenue and margin bridge evidence.

```text
evidence_family = AMMUNITION_DEFENSE_EXPORT_DEMAND_BACKLOG_COPPER_SPREAD_REVENUE_MARGIN_BRIDGE
case_role = positive_ammo_export_backlog_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 38,650
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv`:

```text
2024-02-01,38650,39800,38050,39400
2024-02-08,39200,39200,37550,37950
2024-03-07,45000,51300,44900,46100
2024-04-12,60200,67500,59600,61600
2024-05-14,78100,78900,75600,76300
2024-08-05,53300,54100,47000,49400
2024-10-22,71000,74000,70400,72100
```

### Backtest

```text
MFE_30D  = +32.73%
MAE_30D  = -2.85%
MFE_90D  = +104.14%
MAE_90D  = -2.85%
MFE_180D = +104.14%
MAE_180D = -2.85%
peak_180 = 78,900 on 2024-05-14
trough_180 = 37,550 on 2024-02-08
peak_to_later_drawdown = -40.43%
```

### Interpretation

This is a C03 ammunition/export-demand positive with lifecycle risk.  
The initial signal was strong, but the later drawdown means export demand, backlog and margin evidence must refresh.

Correct treatment:

```text
verified ammo export demand / backlog / shipment / copper-spread / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 010820 / 퍼스텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests defense/drone component theme beta without enough named export framework, backlog, delivery and margin bridge.

```text
evidence_family = DEFENSE_DRONE_COMPONENT_THEME_WITH_WEAK_NAMED_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = counterexample_defense_theme_backlog_gap_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv`:

```text
2024-02-01,3200,3270,3195,3255
2024-02-07,3290,3470,3265,3275
2024-04-09,3410,3550,3350,3460
2024-08-05,3220,3345,2685,2835
2024-09-09,2560,2710,2555,2685
2024-10-24,3655,3920,3500,3540
2024-10-31,3515,3605,3185,3190
```

### Backtest

```text
MFE_30D  = +8.44%
MAE_30D  = -0.63%
MFE_90D  = +10.94%
MAE_90D  = -0.63%
MFE_180D = +22.50%
MAE_180D = -20.16%
peak_180 = 3,920 on 2024-10-24
trough_180 = 2,555 on 2024-09-09
peak_to_later_drawdown = -18.75%
```

### Interpretation

This is a defense-theme backlog-gap boundary.  
A late spike occurred, but durable C03 requires backlog, delivery and margin evidence.

Correct treatment:

```text
defense/drone theme beta
→ no verified named export / backlog / delivery / margin bridge
→ local 4B-watch rather than durable Green
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
defense_theme_backlog_gap_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C03_defense_theme_weight = true
do_not_treat_all_defense_MFE_as_Green = true
do_not_convert_defense_drawdown_to_hard_4C_without_non_price_export_backlog_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE
```

This fine archetype covers:

```text
1. ground-system export framework and backlog bridge → Stage2 possible after source repair
2. ammunition export demand / backlog / raw-material spread bridge → Stage2 possible, lifecycle-managed
3. defense/drone component theme without backlog bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GroundSystemExportFrameworkBacklogBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should allow ground-system positives when export framework or follow-on contract maps to named customer/project, backlog, delivery schedule, revenue recognition and margin bridge. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but lifecycle 4B is needed if delivery/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer/project, order backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG", "symbol": "103140", "company_name": "풍산", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AmmoExportDemandBacklogMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should preserve ammo/munitions positives when defense export demand, backlog visibility, order/shipment cadence, raw-material spread and margin bridge are visible. Poongsan produced a very large MFE with bounded entry-basis MAE, but post-peak drawdown requires lifecycle management.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer/project, order backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DefenseDroneThemeBacklogGapWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should not treat drone/defense component theme beta as durable Stage2 unless named export framework, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had limited early MFE, then high MAE, and a late theme spike; without backlog/margin proof it should be local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer/project, order backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG", "case_id": "R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_framework_backlog_guardrail", "trigger_type": "Stage2-Actionable-GroundSystemExportFrameworkBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 28100.0, "evidence_available_at_that_date": "GROUND_SYSTEM_K2_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_ROTEM_2024_K2_GROUND_SYSTEM_EXPORT_FRAMEWORK_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_program_visibility_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.78, "MFE_90D_pct": 54.63, "MFE_180D_pct": 141.99, "MAE_30D_pct": -4.09, "MAE_90D_pct": -4.09, "MAE_180D_pct": -4.09, "peak_date": "2024-10-18", "peak_price": 68000.0, "drawdown_after_peak_pct": -11.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_peak_if_export_framework_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_cancellation_order_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_export_framework_backlog_with_later_4b_watch", "current_profile_verdict": "C03 should allow ground-system positives when export framework or follow-on contract maps to named customer/project, backlog, delivery schedule, revenue recognition and margin bridge. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but lifecycle 4B is needed if delivery/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_064350_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG", "case_id": "R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG", "symbol": "103140", "company_name": "풍산", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_framework_backlog_guardrail", "trigger_type": "Stage2-Actionable-AmmoExportDemandBacklogMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 38650.0, "evidence_available_at_that_date": "AMMUNITION_DEFENSE_EXPORT_DEMAND_BACKLOG_COPPER_SPREAD_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:POONGSAN_2024_AMMUNITION_DEFENSE_EXPORT_DEMAND_BACKLOG_COPPER_SPREAD_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_program_visibility_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.73, "MFE_90D_pct": 104.14, "MFE_180D_pct": 104.14, "MAE_30D_pct": -2.85, "MAE_90D_pct": -2.85, "MAE_180D_pct": -2.85, "peak_date": "2024-05-14", "peak_price": 78900.0, "drawdown_after_peak_pct": -40.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_peak_if_export_framework_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_cancellation_order_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_ammo_export_backlog_with_later_4b_watch", "current_profile_verdict": "C03 should preserve ammo/munitions positives when defense export demand, backlog visibility, order/shipment cadence, raw-material spread and margin bridge are visible. Poongsan produced a very large MFE with bounded entry-basis MAE, but post-peak drawdown requires lifecycle management.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_103140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP", "case_id": "R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "79", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_framework_backlog_guardrail", "trigger_type": "Stage2-FalsePositive / DefenseDroneThemeBacklogGapWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3200.0, "evidence_available_at_that_date": "DEFENSE_DRONE_COMPONENT_THEME_WITH_WEAK_NAMED_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FIRSTEC_2024_DEFENSE_DRONE_COMPONENT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework_candidate", "order_backlog_or_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_program_visibility_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.44, "MFE_90D_pct": 10.94, "MFE_180D_pct": 22.5, "MAE_30D_pct": -0.63, "MAE_90D_pct": -0.63, "MAE_180D_pct": -20.16, "peak_date": "2024-10-24", "peak_price": 3920.0, "drawdown_after_peak_pct": -18.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_peak_if_export_framework_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_cancellation_order_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_defense_theme_backlog_gap_local4b", "current_profile_verdict": "C03 should not treat drone/defense component theme beta as durable Stage2 unless named export framework, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had limited early MFE, then high MAE, and a late theme spike; without backlog/margin proof it should be local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_010820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG", "trigger_id": "TRG_R11L79-C03-064350-HYUNDAI-ROTEM-GROUND-SYSTEM-EXPORT-BACKLOG", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 15, "named_customer_project_score": 14, "order_backlog_score": 15, "delivery_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"export_framework_score": 17, "named_customer_project_score": 16, "order_backlog_score": 17, "delivery_revenue_score": 16, "margin_bridge_score": 16, "relative_strength_score": 14, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["export_framework_score", "named_customer_project_score", "order_backlog_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer/project, order backlog, delivery/revenue and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 54.63, "MAE_90D_pct": -4.09, "score_return_alignment_label": "defense_export_framework_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should allow ground-system positives when export framework or follow-on contract maps to named customer/project, backlog, delivery schedule, revenue recognition and margin bridge. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but lifecycle 4B is needed if delivery/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG", "trigger_id": "TRG_R11L79-C03-103140-POONGSAN-AMMO-EXPORT-DEMAND-BACKLOG", "symbol": "103140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 15, "named_customer_project_score": 14, "order_backlog_score": 15, "delivery_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"export_framework_score": 17, "named_customer_project_score": 16, "order_backlog_score": 17, "delivery_revenue_score": 16, "margin_bridge_score": 16, "relative_strength_score": 14, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["export_framework_score", "named_customer_project_score", "order_backlog_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer/project, order backlog, delivery/revenue and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 104.14, "MAE_90D_pct": -2.85, "score_return_alignment_label": "defense_export_framework_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should preserve ammo/munitions positives when defense export demand, backlog visibility, order/shipment cadence, raw-material spread and margin bridge are visible. Poongsan produced a very large MFE with bounded entry-basis MAE, but post-peak drawdown requires lifecycle management."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP", "trigger_id": "TRG_R11L79-C03-010820-FIRSTEC-DEFENSE-DRONE-THEME-BACKLOG-GAP", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 5, "named_customer_project_score": 3, "order_backlog_score": 3, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_framework_score": 3, "named_customer_project_score": 1, "order_backlog_score": 1, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_framework_score", "named_customer_project_score", "order_backlog_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer/project, order backlog, delivery/revenue and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 10.94, "MAE_90D_pct": -0.63, "score_return_alignment_label": "false_positive_defense_theme_backlog_gap", "current_profile_verdict": "C03 should not treat drone/defense component theme beta as durable Stage2 unless named export framework, order backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had limited early MFE, then high MAE, and a late theme spike; without backlog/margin proof it should be local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEM_AMMO_DEFENSE_ELECTRONICS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C03 defense/export symbols outside top-covered 012450/079550/047810/065450 set, +3 ground-system/ammo/drone-component trigger families, +2 defense export-backlog positives, +1 defense theme backlog-gap local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "axis": "ground_system_ammo_defense_electronics_export_framework_backlog_margin_bridge_vs_defense_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C03 should split verified defense export framework / order backlog / delivery-margin rerating from generic defense theme beta. Stage2 requires named export framework, customer/project visibility, order backlog, delivery schedule, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["064350", "103140", "010820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 79, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "defense_theme_backlog_gap_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C03 needs defense export framework, named project/customer, backlog, delivery and margin proof. Hyundai Rotem and Poongsan show defense export/backlog positives after source repair; Firstec shows defense/drone theme beta fading into local 4B when backlog, delivery and margin bridge are absent or stale."}
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
064350:
  name = 현대로템
  corporate_action_candidate_dates = 2020-08-14
  selected window = 2024-02-01~D+180
  contamination = false

103140:
  name = 풍산
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

010820:
  name = 퍼스텍 from 2002-02-19, 제일정밀 before that
  corporate_action_candidate_dates = 1999-11-05, 2002-02-19, 2003-07-16, 2006-12-22
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C03 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C03 rule-shape discovery,
but coding-agent promotion requires non-proxy defense export framework, named customer/project, order backlog, delivery schedule, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R11/C03 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
ground_system_ammo_defense_electronics_export_framework_backlog_margin_bridge_vs_defense_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 064350, 103140 and 010820.
4. Keep generic C03 defense-export-framework weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - export framework or policy event is explicit,
   - named customer/project is visible,
   - order backlog or shipment/delivery schedule exists,
   - revenue recognition and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is defense theme beta only,
   - export/backlog/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price export cancellation, order delay, customer loss, financing or margin break.
8. Emit before/after diagnostics and reject if verified defense export/backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 79
next_round = R12
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

