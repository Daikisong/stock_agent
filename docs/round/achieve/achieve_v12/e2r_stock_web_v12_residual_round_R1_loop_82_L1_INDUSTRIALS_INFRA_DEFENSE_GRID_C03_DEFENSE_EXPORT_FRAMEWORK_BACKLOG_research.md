# E2R Stock-Web v12 Residual Research — R1 Loop 82 / L1 / C03

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 82,
  "computed_next_round": "R2",
  "computed_next_loop": 82,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "defense_export_framework_backlog_guardrail",
    "ammo_defense_electronics_component_order_margin_bridge",
    "defense_theme_whipsaw_boundary",
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

Previous completed state in this interactive run: R13 / loop 81.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 82
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
computed_next_round = R2
computed_next_loop = 82
```

R1 was routed to C03 because loop 81 R1 used C04 and loop 80 R1 used C02.  
This file tests defense export / ammunition / defense-electronics backlog bridges rather than grid capex or nuclear project delay.

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
103140 / 풍산 / ammunition export backlog and margin bridge
272210 / 한화시스템 / defense electronics program backlog bridge
010820 / 퍼스텍 / defense component / drone theme whipsaw
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
defense export / framework / geopolitical headline
→ named customer, country or program
→ backlog and delivery schedule
→ revenue recognition
→ margin bridge
→ durable rerating
```

방산 수출은 대포 소리가 아니라 계약서의 납기표다.  
C03이 보려는 것은 headline의 굉음이 실제 수주잔고, 납품, 매출, 마진으로 금속처럼 굳는지다.

---

## Case 1 — Ammunition export backlog positive: 103140 / 풍산

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is ammunition export backlog, customer/country program, metal spread, delivery schedule, revenue recognition and margin bridge evidence.

```text
evidence_family = AMMUNITION_DEFENSE_EXPORT_BACKLOG_METAL_SPREAD_REVENUE_MARGIN_BRIDGE
case_role = positive_ammo_export_backlog_margin_bridge_with_later_4b_watch
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
2024-05-02,67500,75000,67000,72700
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

This is a clean C03 ammunition/export backlog candidate after source repair.  
The price path had large MFE and shallow entry-basis MAE, but post-peak drawdown requires lifecycle management.

Correct treatment:

```text
verified export backlog / customer-country program / delivery / revenue / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Defense electronics backlog positive: 272210 / 한화시스템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is defense electronics, radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge evidence.

```text
evidence_family = DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_PROGRAM_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_defense_electronics_program_backlog_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 15,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv`:

```text
2024-02-01,15350,15500,14960,15110
2024-02-14,15630,16870,15500,16500
2024-03-07,18710,19180,17950,18160
2024-04-26,18730,20000,18290,19940
2024-06-18,19500,22450,19350,21700
2024-07-24,20300,22750,19950,22250
2024-07-30,22100,23400,19920,20500
2024-09-09,16710,16970,16530,16890
```

### Backtest

```text
MFE_30D  = +24.95%
MAE_30D  = -2.61%
MFE_90D  = +46.25%
MAE_90D  = -2.61%
MFE_180D = +52.44%
MAE_180D = -2.61%
peak_180 = 23,400 on 2024-07-30
trough_180 = 14,950 on 2024-02-06
peak_to_later_drawdown = -29.36%
```

### Interpretation

This is a C03 defense electronics / program backlog candidate.  
The MFE was strong and MAE was controlled; it should not be blocked once non-price backlog evidence is repaired.

Correct treatment:

```text
verified radar/C4I/sensor program / export backlog / delivery / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / theme whipsaw: 010820 / 퍼스텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests defense component / drone / robot theme beta without enough contract backlog, customer program, delivery and margin bridge.

```text
evidence_family = DEFENSE_COMPONENT_DRONE_ROBOT_THEME_WITH_WEAK_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = counterexample_defense_component_theme_whipsaw_local4b
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
2024-09-10,2700,3175,2700,2895
2024-10-23,3120,3880,3090,3485
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

This is not clean Stage2.  
It had a late theme spike, but it first opened a deep interim MAE and the order/backlog/margin bridge is missing.

Correct treatment:

```text
defense component / drone / robot theme beta
→ no verified contract backlog / delivery / margin bridge
→ local 4B-watch / theme-whipsaw boundary
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
defense_export_backlog_bridge_required = strengthen
customer_program_delivery_revenue_bridge_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C03_defense_theme_weight = true
do_not_treat_all_defense_MFE_as_Green = true
do_not_convert_defense_theme_whipsaw_to_hard_4C_without_non_price_contract_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW
```

This fine archetype covers:

```text
1. ammunition export backlog and margin bridge → Stage2 possible after source repair
2. defense electronics / radar / C4I program bridge → Stage2-Yellow possible after source repair
3. defense component / drone theme without backlog bridge → false Stage2 / local 4B whipsaw
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AmmoExportBacklogMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should protect defense/ammunition positives only when export backlog, customer country/program, delivery schedule, metal spread, revenue recognition and margin bridge are visible. Poongsan produced a very large MFE with shallow entry-basis MAE, but post-peak drawdown requires lifecycle 4B if backlog/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export backlog, customer/program, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "company_name": "한화시스템", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DefenseElectronicsBacklogProgramRevenueBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should allow defense electronics positives when radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge are visible. Hanwha Systems produced strong MFE with controlled entry-basis MAE, but bridge refresh is required after post-peak drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export backlog, customer/program, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW", "symbol": "010820", "company_name": "퍼스텍", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DefenseComponentDroneThemeWhipsawWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should not treat defense component/drone/robot theme beta as durable Stage2 unless contract backlog, customer program, delivery schedule, revenue conversion and margin bridge are visible. Firstec had a late theme spike but also a deep interim MAE, so it is a whipsaw/local-4B boundary rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export backlog, customer/program, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN", "case_id": "R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN", "symbol": "103140", "company_name": "풍산", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_backlog_guardrail", "trigger_type": "Stage2-Actionable-AmmoExportBacklogMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 38650.0, "evidence_available_at_that_date": "AMMUNITION_DEFENSE_EXPORT_BACKLOG_METAL_SPREAD_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:POONGSAN_2024_AMMUNITION_EXPORT_BACKLOG_METAL_SPREAD_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_program_candidate", "backlog_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_contract_duration_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv", "profile_path": "atlas/symbol_profiles/103/103140.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.73, "MFE_90D_pct": 104.14, "MFE_180D_pct": 104.14, "MAE_30D_pct": -2.85, "MAE_90D_pct": -2.85, "MAE_180D_pct": -2.85, "peak_date": "2024-05-14", "peak_price": 78900.0, "drawdown_after_peak_pct": -40.43, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_contract_cancellation_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_ammo_export_backlog_margin_bridge_with_later_4b_watch", "current_profile_verdict": "C03 should protect defense/ammunition positives only when export backlog, customer country/program, delivery schedule, metal spread, revenue recognition and margin bridge are visible. Poongsan produced a very large MFE with shallow entry-basis MAE, but post-peak drawdown requires lifecycle 4B if backlog/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_EXPORT_103140_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "case_id": "R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "company_name": "한화시스템", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_backlog_guardrail", "trigger_type": "Stage2-Actionable-DefenseElectronicsBacklogProgramRevenueBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15350.0, "evidence_available_at_that_date": "DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_PROGRAM_BACKLOG_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_SYSTEMS_2024_DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_BACKLOG_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_program_candidate", "backlog_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_contract_duration_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv", "profile_path": "atlas/symbol_profiles/272/272210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.95, "MFE_90D_pct": 46.25, "MFE_180D_pct": 52.44, "MAE_30D_pct": -2.61, "MAE_90D_pct": -2.61, "MAE_180D_pct": -2.61, "peak_date": "2024-07-30", "peak_price": 23400.0, "drawdown_after_peak_pct": -29.36, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_contract_cancellation_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_defense_electronics_program_backlog_with_later_4b_watch", "current_profile_verdict": "C03 should allow defense electronics positives when radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge are visible. Hanwha Systems produced strong MFE with controlled entry-basis MAE, but bridge refresh is required after post-peak drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_EXPORT_272210_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW", "case_id": "R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW", "symbol": "010820", "company_name": "퍼스텍", "round": "R1", "loop": "82", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "loop_objective": "coverage_gap_fill|counterexample_mining|defense_export_backlog_guardrail", "trigger_type": "Stage2-FalsePositive / DefenseComponentDroneThemeWhipsawWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3200.0, "evidence_available_at_that_date": "DEFENSE_COMPONENT_DRONE_ROBOT_THEME_WITH_WEAK_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FIRSTEC_2024_DEFENSE_COMPONENT_DRONE_ROBOT_CONTRACT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_program_candidate", "backlog_delivery_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_contract_duration_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.44, "MFE_90D_pct": 10.94, "MFE_180D_pct": 22.5, "MAE_30D_pct": -0.63, "MAE_90D_pct": -0.63, "MAE_180D_pct": -20.16, "peak_date": "2024-10-24", "peak_price": 3920.0, "drawdown_after_peak_pct": -18.75, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_export_contract_cancellation_customer_loss_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_defense_component_theme_whipsaw_local4b", "current_profile_verdict": "C03 should not treat defense component/drone/robot theme beta as durable Stage2 unless contract backlog, customer program, delivery schedule, revenue conversion and margin bridge are visible. Firstec had a late theme spike but also a deep interim MAE, so it is a whipsaw/local-4B boundary rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_EXPORT_010820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN", "trigger_id": "TRG_R1L82-C03-103140-POONGSAN-AMMO-EXPORT-BACKLOG-MARGIN", "symbol": "103140", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 14, "backlog_quality_score": 14, "customer_program_score": 13, "delivery_revenue_score": 13, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"export_framework_score": 16, "backlog_quality_score": 16, "customer_program_score": 15, "delivery_revenue_score": 15, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_framework_score", "backlog_quality_score", "customer_program_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, program backlog, customer quality, delivery/revenue and margin bridge; cap defense theme beta when backlog and margin evidence fails to refresh.", "MFE_90D_pct": 104.14, "MAE_90D_pct": -2.85, "score_return_alignment_label": "defense_export_backlog_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should protect defense/ammunition positives only when export backlog, customer country/program, delivery schedule, metal spread, revenue recognition and margin bridge are visible. Poongsan produced a very large MFE with shallow entry-basis MAE, but post-peak drawdown requires lifecycle 4B if backlog/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "trigger_id": "TRG_R1L82-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 14, "backlog_quality_score": 14, "customer_program_score": 13, "delivery_revenue_score": 13, "margin_bridge_score": 13, "relative_strength_score": 13, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"export_framework_score": 16, "backlog_quality_score": 16, "customer_program_score": 15, "delivery_revenue_score": 15, "margin_bridge_score": 15, "relative_strength_score": 12, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["export_framework_score", "backlog_quality_score", "customer_program_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, program backlog, customer quality, delivery/revenue and margin bridge; cap defense theme beta when backlog and margin evidence fails to refresh.", "MFE_90D_pct": 46.25, "MAE_90D_pct": -2.61, "score_return_alignment_label": "defense_export_backlog_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should allow defense electronics positives when radar/C4I/sensor program backlog, export customer, delivery milestones, revenue conversion and margin bridge are visible. Hanwha Systems produced strong MFE with controlled entry-basis MAE, but bridge refresh is required after post-peak drawdown."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW", "trigger_id": "TRG_R1L82-C03-010820-FIRSTEC-DEFENSE-COMPONENT-THEME-WHIPSAW", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"export_framework_score": 5, "backlog_quality_score": 3, "customer_program_score": 3, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_before": 43, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"export_framework_score": 3, "backlog_quality_score": 1, "customer_program_score": 1, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 25, "source_confidence_score": 2}, "weighted_score_after": 32, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_framework_score", "backlog_quality_score", "customer_program_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, program backlog, customer quality, delivery/revenue and margin bridge; cap defense theme beta when backlog and margin evidence fails to refresh.", "MFE_90D_pct": 10.94, "MAE_90D_pct": -0.63, "score_return_alignment_label": "false_positive_defense_component_theme_whipsaw", "current_profile_verdict": "C03 should not treat defense component/drone/robot theme beta as durable Stage2 unless contract backlog, customer program, delivery schedule, revenue conversion and margin bridge are visible. Firstec had a late theme spike but also a deep interim MAE, so it is a whipsaw/local-4B boundary rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 82, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "AMMO_DEFENSE_ELECTRONICS_COMPONENT_EXPORT_BACKLOG_MARGIN_BRIDGE_VS_DEFENSE_THEME_WHIPSAW", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C03 defense/export symbols outside top-covered 012450/079550/047810/065450 set, +3 ammunition/defense-electronics/component-theme trigger families, +2 defense backlog positives, +1 defense component whipsaw local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 82, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "axis": "ammo_defense_electronics_component_export_backlog_margin_bridge_vs_defense_theme_whipsaw", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C03 should split verified ammunition/export and defense-electronics backlog margin rerating from generic defense component/drone theme beta. Stage2 requires named export/customer/program, backlog, delivery schedule, revenue recognition and margin bridge. If MFE fades or MAE opens without backlog/margin refresh, route to local 4B-watch. Theme whipsaws should not be Green without non-price backlog evidence.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["103140", "272210", "010820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 82, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "existing_axis_strengthened": ["stage2_required_bridge", "defense_export_backlog_bridge_required", "customer_program_delivery_revenue_bridge_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C03 needs defense headlines to map into export framework, customer/program backlog, delivery, revenue recognition and margin proof. Poongsan and Hanwha Systems show defense backlog positives after source repair; Firstec shows defense component/drone theme whipsaw where late MFE without backlog bridge should not be durable Green."}
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
103140:
  name = 풍산
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

272210:
  name = 한화시스템
  corporate_action_candidate_dates = 2021-06-23
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
This MD is useful for stock-web path calibration and C03 defense-export/backlog rule-shape discovery,
but coding-agent promotion requires non-proxy export framework, named customer/program, backlog, delivery schedule, revenue recognition and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C03 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
ammo_defense_electronics_component_export_backlog_margin_bridge_vs_defense_theme_whipsaw

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 103140, 272210 and 010820.
4. Keep generic C03 defense theme weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - export framework or named defense program is explicit,
   - customer/country/program quality is visible,
   - backlog and delivery schedule exist,
   - revenue recognition and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is defense component/drone/theme beta only,
   - backlog/delivery/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%,
   - or a deep interim MAE is followed by a price-only theme spike without bridge repair.
7. Do not convert local 4B-watch into full 4B/4C without non-price export contract cancellation, customer loss, delivery delay, financing or margin break.
8. Emit before/after diagnostics and reject if verified ammunition or defense-electronics backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 82
next_round = R2
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

