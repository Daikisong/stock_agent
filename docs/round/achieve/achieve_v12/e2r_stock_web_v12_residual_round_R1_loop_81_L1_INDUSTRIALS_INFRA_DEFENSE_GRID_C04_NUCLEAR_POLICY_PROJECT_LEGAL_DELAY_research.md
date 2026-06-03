# E2R Stock-Web v12 Residual Research — R1 Loop 81 / L1 / C04

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 81,
  "computed_next_round": "R2",
  "computed_next_loop": 81,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY",
  "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "nuclear_policy_project_legal_delay_guardrail",
    "nuclear_O&M_control_inspection_project_revenue_margin_bridge",
    "nuclear_theme_bridge_gap_boundary",
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

Previous completed state in this interactive run: R13 / loop 80.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 81
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
computed_next_round = R2
computed_next_loop = 81
```

R1 was routed to C04 because loop 80 R1 used C02 and loop 80 R11 used C32.  
This file tests nuclear O&M / control-system / inspection project bridges rather than grid capex or governance tender-cap events.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C04 concentration in:

```text
034020, 051600, 052690, 000720, 083650
```

This run uses three different symbols:

```text
126720 / 수산인더스트리 / nuclear O&M maintenance project revenue bridge
032820 / 우리기술 / nuclear control-system project relative-strength bridge
046120 / 오르비텍 / nuclear inspection / radiation-safety theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
032820 shows share-count changes inside the 2024 shard and requires coding-agent validation before runtime promotion.
```

## Research thesis

C04 is not “원전 정책이 좋다.”

The mechanism must pass through:

```text
nuclear policy / project event
→ named project, O&M scope, control-system or inspection order
→ customer quality and delivery schedule
→ revenue recognition
→ margin bridge
→ durable rerating
```

원전 정책은 원자로의 점화 스위치가 아니다.  
C04가 보려는 것은 그 스위치가 실제 정비 물량, 제어시스템 납품, 검사 계약, 매출과 마진으로 전류를 보내는지다.

---

## Case 1 — Nuclear O&M project candidate: 126720 / 수산인더스트리

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is nuclear power plant O&M / maintenance project orderbook, outage or regular-maintenance demand, revenue recognition and margin bridge evidence.

```text
evidence_family = NUCLEAR_POWER_PLANT_OM_MAINTENANCE_PROJECT_ORDER_REVENUE_MARGIN_BRIDGE
case_role = positive_nuclear_OM_project_revenue_bridge_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 19,260
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/126/126720/2024.csv`:

```text
2024-02-01,19260,19680,19010,19510
2024-02-21,21100,22250,20900,21550
2024-03-19,23400,24500,23350,23650
2024-04-05,22800,24450,22500,23800
2024-08-05,21400,21400,19640,19860
2024-08-14,22000,24000,21800,22600
2024-10-30,22600,23650,22000,23200
```

### Backtest

```text
MFE_30D  = +15.52%
MAE_30D  = -1.30%
MFE_90D  = +27.21%
MAE_90D  = -1.30%
MFE_180D = +27.21%
MAE_180D = -1.30%
peak_180 = 24,500 on 2024-03-19
trough_180 = 19,010 on 2024-02-01
peak_to_later_drawdown = -19.84%
```

### Interpretation

This is a C04 nuclear O&M candidate.  
The MFE was moderate and entry-basis MAE was very controlled.

Correct treatment:

```text
verified O&M / maintenance order / revenue / margin bridge → Stage2-Yellow possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Nuclear control-system positive: 032820 / 우리기술

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is nuclear control-system project order, customer quality, delivery schedule, revenue conversion and margin bridge evidence.

```text
evidence_family = NUCLEAR_CONTROL_SYSTEM_PROJECT_ORDER_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE
case_role = positive_nuclear_control_system_RS_with_sharecount_validation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 1,263
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv`:

```text
2024-02-01,1263,1279,1261,1271
2024-02-26,1330,1360,1311,1335
2024-03-12,1352,1559,1335,1477
2024-04-05,1528,1612,1490,1563
2024-07-24,2370,2520,2360,2485
2024-08-05,2170,2175,1800,1968
2024-09-13,2340,2570,2315,2440
2024-10-31,2150,2210,2145,2170
```

### Backtest

```text
MFE_30D  = +7.68%
MAE_30D  = -0.16%
MFE_90D  = +27.63%
MAE_90D  = -0.16%
MFE_180D = +103.48%
MAE_180D = -0.16%
peak_180 = 2,570 on 2024-09-13
trough_180 = 1,261 on 2024-02-01
peak_to_later_drawdown = -16.54%
```

### Interpretation

This is a C04 nuclear control-system relative-strength positive, but share-count validation is required before runtime ingestion.

Correct treatment:

```text
verified control-system order / customer / delivery / margin bridge → Stage2 possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 046120 / 오르비텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests nuclear inspection / radiation-safety theme beta without enough project order, revenue and margin bridge.

```text
evidence_family = NUCLEAR_INSPECTION_RADIATION_SAFETY_POLICY_THEME_WITH_WEAK_PROJECT_REVENUE_MARGIN_BRIDGE
case_role = counterexample_nuclear_inspection_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,290
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv`:

```text
2024-02-01,3290,3340,3245,3335
2024-02-19,3520,3530,3450,3490
2024-03-14,3405,3555,3375,3495
2024-04-11,3105,3180,2970,3175
2024-08-05,2495,2585,2040,2175
2024-09-09,2115,2200,2090,2200
2024-10-31,2300,2300,2165,2180
```

### Backtest

```text
MFE_30D  = +7.29%
MAE_30D  = -1.37%
MFE_90D  = +9.12%
MAE_90D  = -9.73%
MFE_180D = +9.12%
MAE_180D = -37.99%
peak_180 = 3,590 on 2024-03-14
trough_180 = 2,040 on 2024-08-05
peak_to_later_drawdown = -43.18%
```

### Interpretation

This is a C04 false-positive / local-4B boundary.  
The nuclear inspection theme did not validate durable project-revenue rerating.

Correct treatment:

```text
nuclear inspection / radiation-safety theme beta
→ no verified project order / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
project_order_revenue_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C04_nuclear_policy_theme_weight = true
do_not_treat_all_nuclear_policy_MFE_as_Green = true
do_not_ingest_sharecount_changed_control-system_rows_without_validation = true
do_not_convert_nuclear_theme_drawdown_to_hard_4C_without_non_price_project_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE
```

This fine archetype covers:

```text
1. nuclear O&M maintenance project revenue bridge → Stage2-Yellow possible after source repair
2. nuclear control-system project / delivery bridge → Stage2 possible after source repair and share-count validation
3. nuclear inspection/radiation-safety theme without project bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE", "symbol": "126720", "company_name": "수산인더스트리", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-NuclearOMMaintenanceProjectRevenueBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should allow nuclear O&M/maintenance positives when policy attention maps to maintenance project orderbook, outage/regular-maintenance demand, revenue recognition and margin bridge. Susan Industries had controlled entry-basis MAE and moderate MFE, so it should not be overblocked after source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy, project order, O&M/inspection/control-system backlog, customer quality, delivery, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT", "symbol": "032820", "company_name": "우리기술", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-NuclearControlSystemProjectRSBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should protect nuclear control-system positives when project/order evidence, customer quality, delivery schedule, revenue conversion and margin bridge are visible. Woori Technology produced very large MFE with nearly no early MAE, but share-count validation is required before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy, project order, O&M/inspection/control-system backlog, customer quality, delivery, revenue and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "case_type": "nuclear_policy_project_legal_delay", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / NuclearInspectionThemeBridgeFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C04 should not treat nuclear inspection/radiation-safety theme beta as durable Stage2 unless inspection backlog, project order, customer quality, revenue and margin bridge are visible. Orbitech had only small MFE and then a deep MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy nuclear policy, project order, O&M/inspection/control-system backlog, customer quality, delivery, revenue and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE", "case_id": "R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE", "symbol": "126720", "company_name": "수산인더스트리", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_guardrail", "trigger_type": "Stage2-Yellow-NuclearOMMaintenanceProjectRevenueBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 19260.0, "evidence_available_at_that_date": "NUCLEAR_POWER_PLANT_OM_MAINTENANCE_PROJECT_ORDER_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SUSAN_INDUSTRIES_2024_NUCLEAR_OM_MAINTENANCE_PROJECT_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_project_candidate", "order_backlog_or_maintenance_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_delivery_schedule_candidate"], "stage4b_evidence_fields": ["nuclear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/126/126720/2024.csv", "profile_path": "atlas/symbol_profiles/126/126720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.52, "MFE_90D_pct": 27.21, "MFE_180D_pct": 27.21, "MAE_30D_pct": -1.3, "MAE_90D_pct": -1.3, "MAE_180D_pct": -1.3, "peak_date": "2024-03-19", "peak_price": 24500.0, "drawdown_after_peak_pct": -19.84, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_regulatory_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_nuclear_OM_project_revenue_bridge_with_later_4b_watch", "current_profile_verdict": "C04 should allow nuclear O&M/maintenance positives when policy attention maps to maintenance project orderbook, outage/regular-maintenance demand, revenue recognition and margin bridge. Susan Industries had controlled entry-basis MAE and moderate MFE, so it should not be overblocked after source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_POLICY_PROJECT_126720_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT", "case_id": "R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT", "symbol": "032820", "company_name": "우리기술", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_guardrail", "trigger_type": "Stage2-Actionable-NuclearControlSystemProjectRSBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 1263.0, "evidence_available_at_that_date": "NUCLEAR_CONTROL_SYSTEM_PROJECT_ORDER_CUSTOMER_DELIVERY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:WOORI_TECHNOLOGY_2024_NUCLEAR_CONTROL_SYSTEM_PROJECT_ORDER_CUSTOMER_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_project_candidate", "order_backlog_or_maintenance_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_delivery_schedule_candidate"], "stage4b_evidence_fields": ["nuclear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032820/2024.csv", "profile_path": "atlas/symbol_profiles/032/032820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.68, "MFE_90D_pct": 27.63, "MFE_180D_pct": 103.48, "MAE_30D_pct": -0.16, "MAE_90D_pct": -0.16, "MAE_180D_pct": -0.16, "peak_date": "2024-09-13", "peak_price": 2570.0, "drawdown_after_peak_pct": -16.54, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_regulatory_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "positive_nuclear_control_system_RS_with_sharecount_validation_and_later_4b_watch", "current_profile_verdict": "C04 should protect nuclear control-system positives when project/order evidence, customer quality, delivery schedule, revenue conversion and margin bridge are visible. Woori Technology produced very large MFE with nearly no early MAE, but share-count validation is required before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C04_NUCLEAR_POLICY_PROJECT_032820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE", "case_id": "R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE", "symbol": "046120", "company_name": "오르비텍", "round": "R1", "loop": "81", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|nuclear_policy_project_guardrail", "trigger_type": "Stage2-FalsePositive / NuclearInspectionThemeBridgeFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3290.0, "evidence_available_at_that_date": "NUCLEAR_INSPECTION_RADIATION_SAFETY_POLICY_THEME_WITH_WEAK_PROJECT_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ORBITECH_2024_NUCLEAR_INSPECTION_RADIATION_SAFETY_PROJECT_ORDER_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["nuclear_policy_project_candidate", "order_backlog_or_maintenance_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_or_delivery_schedule_candidate"], "stage4b_evidence_fields": ["nuclear_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.29, "MFE_90D_pct": 9.12, "MFE_180D_pct": 9.12, "MAE_30D_pct": -1.37, "MAE_90D_pct": -9.73, "MAE_180D_pct": -37.99, "peak_date": "2024-03-14", "peak_price": 3590.0, "drawdown_after_peak_pct": -43.18, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_nuclear_policy_peak_if_project_order_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_project_cancellation_regulatory_delay_customer_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_nuclear_inspection_theme_local4b", "current_profile_verdict": "C04 should not treat nuclear inspection/radiation-safety theme beta as durable Stage2 unless inspection backlog, project order, customer quality, revenue and margin bridge are visible. Orbitech had only small MFE and then a deep MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C04_NUCLEAR_POLICY_PROJECT_046120_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE", "trigger_id": "TRG_R1L81-C04-126720-SUSAN-INDUSTRIES-NUCLEAR-OM-PROJECT-BRIDGE", "symbol": "126720", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"nuclear_policy_score": 13, "project_order_score": 13, "customer_quality_score": 12, "delivery_revenue_score": 12, "margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 74, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"nuclear_policy_score": 15, "project_order_score": 15, "customer_quality_score": 14, "delivery_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 80, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["nuclear_policy_score", "project_order_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project/O&M/control-system order, customer quality, delivery/revenue and margin bridge; cap nuclear inspection/theme beta when evidence fails to refresh.", "MFE_90D_pct": 27.21, "MAE_90D_pct": -1.3, "score_return_alignment_label": "nuclear_project_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should allow nuclear O&M/maintenance positives when policy attention maps to maintenance project orderbook, outage/regular-maintenance demand, revenue recognition and margin bridge. Susan Industries had controlled entry-basis MAE and moderate MFE, so it should not be overblocked after source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT", "trigger_id": "TRG_R1L81-C04-032820-WOORITECH-NUCLEAR-CONTROL-SYSTEM-RS-SHARECOUNT", "symbol": "032820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"nuclear_policy_score": 13, "project_order_score": 13, "customer_quality_score": 12, "delivery_revenue_score": 12, "margin_bridge_score": 12, "relative_strength_score": 12, "execution_risk_score": 10, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 74, "stage_label_before": "Stage2/Yellow candidate after source repair", "raw_component_scores_after": {"nuclear_policy_score": 15, "project_order_score": 15, "customer_quality_score": 14, "delivery_revenue_score": 14, "margin_bridge_score": 14, "relative_strength_score": 11, "execution_risk_score": 11, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 80, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["nuclear_policy_score", "project_order_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project/O&M/control-system order, customer quality, delivery/revenue and margin bridge; cap nuclear inspection/theme beta when evidence fails to refresh.", "MFE_90D_pct": 27.63, "MAE_90D_pct": -0.16, "score_return_alignment_label": "nuclear_project_positive_with_lifecycle_4b", "current_profile_verdict": "C04 should protect nuclear control-system positives when project/order evidence, customer quality, delivery schedule, revenue conversion and margin bridge are visible. Woori Technology produced very large MFE with nearly no early MAE, but share-count validation is required before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE", "trigger_id": "TRG_R1L81-C04-046120-ORBITECH-NUCLEAR-INSPECTION-THEME-FADE", "symbol": "046120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"nuclear_policy_score": 6, "project_order_score": 3, "customer_quality_score": 3, "delivery_revenue_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 22, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"nuclear_policy_score": 4, "project_order_score": 1, "customer_quality_score": 1, "delivery_revenue_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 24, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["nuclear_policy_score", "project_order_score", "customer_quality_score", "delivery_revenue_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified nuclear project/O&M/control-system order, customer quality, delivery/revenue and margin bridge; cap nuclear inspection/theme beta when evidence fails to refresh.", "MFE_90D_pct": 9.12, "MAE_90D_pct": -9.73, "score_return_alignment_label": "false_positive_nuclear_inspection_theme_bridge_gap", "current_profile_verdict": "C04 should not treat nuclear inspection/radiation-safety theme beta as durable Stage2 unless inspection backlog, project order, customer quality, revenue and margin bridge are visible. Orbitech had only small MFE and then a deep MAE path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 81, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_CONTROL_INSPECTION_POLICY_PROJECT_REVENUE_BRIDGE_VS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C04 nuclear policy/project symbols outside top-covered 034020/051600/052690/000720/083650 set, +3 O&M/control-system/inspection trigger families, +2 nuclear project positives, +1 nuclear inspection local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 81, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "axis": "nuclear_OM_control_inspection_policy_project_revenue_bridge_vs_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C04 should split verified nuclear O&M/control-system project revenue-margin rerating from generic nuclear inspection/policy theme beta. Stage2 requires policy/project event plus order backlog, O&M or control-system delivery, customer quality, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["126720", "032820", "046120"], "share_count_validation_required": ["032820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 81, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "existing_axis_strengthened": ["stage2_required_bridge", "project_order_revenue_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C04 needs nuclear policy/project events to map into O&M/control-system/inspection order backlog, delivery, revenue and margin proof. Susan Industries and Woori Technology show nuclear project/O&M/control-system candidates after source repair; Orbitech shows inspection/radiation-safety theme beta fading into local 4B."}
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
126720:
  name = 수산인더스트리
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

032820:
  name = 우리기술
  corporate_action_candidate_dates = 2003-10-28, 2005-06-07, 2007-07-03, 2007-07-31, 2009-07-29
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

046120:
  name = 오르비텍 from 2013-04-12, 케이엔디티 before that
  corporate_action_candidate_dates = 2017-06-30
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C04 rows are source_proxy_only / evidence_url_pending.
032820 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C04 rule-shape discovery,
but coding-agent promotion requires non-proxy nuclear policy/project, O&M/control-system/inspection order, delivery, revenue and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R1/C04 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 032820 needs share-count validation.

Candidate axis:
nuclear_OM_control_inspection_policy_project_revenue_bridge_vs_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 126720, 032820 and 046120.
4. Validate 032820 share-count changes inside the selected window.
5. Keep generic C04 nuclear-policy weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - nuclear policy/project event is explicit,
   - named project, O&M scope, control-system or inspection order is visible,
   - customer quality and delivery schedule exist,
   - revenue recognition and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is nuclear policy/inspection theme beta only,
   - project/order/revenue/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price project cancellation, regulatory delay, customer loss, financing or margin break.
9. Emit before/after diagnostics and reject if verified O&M/control-system positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 81
next_round = R2
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

