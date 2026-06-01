# E2R Stock-Web v12 Residual Research — R11 Loop 77 / L1 / C03

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R11",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R11",
  "completed_loop": 77,
  "computed_next_round": "R12",
  "computed_next_loop": 77,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "policy_defense_linkage",
    "defense_export_backlog_guardrail",
    "4B_non_price_requirement_stress_test",
    "framework_contract_delivery_margin_bridge",
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

Previous completed state in this interactive run: R10 / loop 77.

Therefore:

```text
scheduled_round = R11
scheduled_loop = 77
allowed_large_sector = L10_POLICY_EVENT_CROSS_REDTEAM_MISC or L1_INDUSTRIALS_INFRA_DEFENSE_GRID depending on policy-defense linkage
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
computed_next_round = R12
computed_next_loop = 77
```

R11 was routed to L1 because this is policy-defense linkage, not a generic L10 red-team row.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C03 is concentrated in:

```text
012450, 079550, 047810, 065450
```

This run uses three different symbols:

```text
003570 / SNT다이내믹스 / defense drivetrain export-backlog bridge
272210 / 한화시스템 / defense electronics / radar / C4I backlog bridge
010820 / 퍼스텍 / defense/unmanned theme beta fade
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
policy / defense export framework
→ named customer program or order
→ backlog and delivery schedule
→ revenue recognition and margin conversion
→ durable rerating
```

방산 headline은 포성이 아니라 신호탄이다.  
C03은 그 신호탄이 실제 계약, 납기, 매출 인식, 마진으로 착지하는지를 본다.

---

## Case 1 — Positive with lifecycle 4B: 003570 / SNT다이내믹스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is defense drivetrain/transmission export program, backlog, delivery schedule and margin bridge evidence.

```text
evidence_family = DEFENSE_DRIVETRAIN_TRANSMISSION_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 14,610
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv`:

```text
2024-02-01,14610,15640,14520,15540
2024-02-29,18350,19240,18320,18670
2024-06-21,20450,21100,19720,21100
2024-07-26,20800,26750,20650,21150
2024-10-23,27750,28200,25950,26700
2024-11-01,24750,25350,23950,24550
```

### Backtest

```text
MFE_30D  = +31.69%
MAE_30D  = -0.62%
MFE_90D  = +44.42%
MAE_90D  = -0.62%
MFE_180D = +93.02%
MAE_180D = -0.62%
peak_180 = 28,200 on 2024-10-23
trough_180 = 14,520 on 2024-02-01
peak_to_later_drawdown = -15.07%
```

### Interpretation

This is a clean C03 positive-shaped path.  
The MFE expanded while entry-basis MAE stayed tiny.

Correct treatment:

```text
verified defense drivetrain backlog / delivery / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Positive with lifecycle 4B: 272210 / 한화시스템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is defense electronics/radar/C4I order, export/customer program, delivery and margin bridge evidence.

```text
evidence_family = DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 15,350
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv`:

```text
2024-02-01,15350,15500,14960,15110
2024-02-27,16580,18500,16580,17160
2024-03-07,18710,19180,17950,18160
2024-07-24,20300,22750,19950,22250
2024-07-30,22100,23400,19920,20500
2024-09-09,16710,16970,16530,16890
```

### Backtest

```text
MFE_30D  = +24.95%
MAE_30D  = -2.54%
MFE_90D  = +37.46%
MAE_90D  = -2.54%
MFE_180D = +52.44%
MAE_180D = -2.54%
peak_180 = 23,400 on 2024-07-30
trough_180 = 14,960 on 2024-02-01~2024-02-05
peak_to_later_drawdown = -29.36%
```

### Interpretation

This is a C03 defense-electronics positive with lifecycle decay risk.  
The positive path should be protected after source repair, but the later drawdown still needs lifecycle management.

Correct treatment:

```text
verified radar/C4I backlog and delivery bridge → Stage2 possible
post-peak drawdown without bridge refresh → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B-watch: 010820 / 퍼스텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests defense/unmanned-system theme beta without enough named program, backlog, delivery and margin bridge.

```text
evidence_family = DEFENSE_UNMANNED_COMPONENT_THEME_WITH_WEAK_BACKLOG_DELIVERY_MARGIN_BRIDGE
case_role = counterexample_defense_theme_local4b_watch
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
2024-10-23,3120,3880,3090,3485
2024-10-24,3655,3920,3500,3540
```

### Backtest

```text
MFE_30D  = +8.44%
MAE_30D  = -0.63%
MFE_90D  = +10.94%
MAE_90D  = -13.75%
MFE_180D = +22.50%
MAE_180D = -20.16%
peak_180 = 3,920 on 2024-10-24
trough_180 = 2,555 on 2024-09-09
peak_to_later_drawdown = -21.17%
```

### Interpretation

This is not a confirmed durable C03 Green.  
The late theme spike is tradable, but the path spent a long time in drawdown and still needs named program/backlog proof.

Correct treatment:

```text
defense/unmanned theme beta
→ no verified program / backlog / delivery / margin bridge
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
```

### What this does not justify

```text
do_not_raise_generic_C03_defense_theme_weight = true
do_not_treat_all_defense_MFE_as_Green = true
do_not_convert_defense_drawdown_to_hard_4C_without_non_price_contract_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE
```

This fine archetype covers:

```text
1. drivetrain/transmission export backlog bridge → Stage2 possible after source repair
2. defense electronics / radar / C4I backlog bridge → Stage2 possible, lifecycle-managed
3. unmanned/defense component theme beta without backlog bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "symbol": "003570", "company_name": "SNT다이내믹스", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DefenseDrivetrainExportBacklogBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should allow defense component suppliers when export framework demand maps to drivetrain/transmission backlog, delivery schedule and margin bridge. SNT Dynamics produced large MFE with almost no entry-basis MAE, but lifecycle local 4B is still required if export/backlog/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy defense/export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "company_name": "한화시스템", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DefenseElectronicsExportBacklogBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should include defense electronics / radar / C4I names only when policy-defense demand maps to backlog, customer program, delivery schedule and margin bridge. Hanwha Systems produced solid MFE with controlled MAE, but later drawdown says C03 must lifecycle-manage the signal.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy defense/export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DefenseUnmannedThemeBetaFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should not treat defense/unmanned-system theme beta as durable Stage2 unless named defense program, contract backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had tradable MFE but spent much of the window in drawdown and only later spiked, making it a local 4B-watch boundary rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy defense/export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "case_id": "R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "symbol": "003570", "company_name": "SNT다이내믹스", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|policy_defense_linkage|defense_export_backlog_guardrail", "trigger_type": "Stage2-Actionable-DefenseDrivetrainExportBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14610.0, "evidence_available_at_that_date": "DEFENSE_DRIVETRAIN_TRANSMISSION_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SNT_DYNAMICS_2024_DEFENSE_DRIVETRAIN_TRANSMISSION_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_policy_framework_candidate", "program_backlog_or_order_candidate", "delivery_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_revenue_recognition_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv", "profile_path": "atlas/symbol_profiles/003/003570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.69, "MFE_90D_pct": 44.42, "MFE_180D_pct": 93.02, "MAE_30D_pct": -0.62, "MAE_90D_pct": -0.62, "MAE_180D_pct": -0.62, "peak_date": "2024-10-23", "peak_price": 28200.0, "drawdown_after_peak_pct": -15.07, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_cancellation_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C03 should allow defense component suppliers when export framework demand maps to drivetrain/transmission backlog, delivery schedule and margin bridge. SNT Dynamics produced large MFE with almost no entry-basis MAE, but lifecycle local 4B is still required if export/backlog/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_003570_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "case_id": "R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "company_name": "한화시스템", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|policy_defense_linkage|defense_export_backlog_guardrail", "trigger_type": "Stage2-Actionable-DefenseElectronicsExportBacklogBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15350.0, "evidence_available_at_that_date": "DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANWHA_SYSTEMS_2024_DEFENSE_ELECTRONICS_RADAR_C4I_EXPORT_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_policy_framework_candidate", "program_backlog_or_order_candidate", "delivery_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_revenue_recognition_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/272/272210/2024.csv", "profile_path": "atlas/symbol_profiles/272/272210.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.95, "MFE_90D_pct": 37.46, "MFE_180D_pct": 52.44, "MAE_30D_pct": -2.54, "MAE_90D_pct": -2.54, "MAE_180D_pct": -2.54, "peak_date": "2024-07-30", "peak_price": 23400.0, "drawdown_after_peak_pct": -29.36, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_cancellation_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C03 should include defense electronics / radar / C4I names only when policy-defense demand maps to backlog, customer program, delivery schedule and margin bridge. Hanwha Systems produced solid MFE with controlled MAE, but later drawdown says C03 must lifecycle-manage the signal.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_272210_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "case_id": "R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "symbol": "010820", "company_name": "퍼스텍", "round": "R11", "loop": "77", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "loop_objective": "coverage_gap_fill|policy_defense_linkage|defense_export_backlog_guardrail", "trigger_type": "Stage2-FalsePositive / DefenseUnmannedThemeBetaFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3200.0, "evidence_available_at_that_date": "DEFENSE_UNMANNED_COMPONENT_THEME_WITH_WEAK_BACKLOG_DELIVERY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FIRSTEC_2024_DEFENSE_UNMANNED_COMPONENT_PROGRAM_BACKLOG_DELIVERY_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_or_policy_framework_candidate", "program_backlog_or_order_candidate", "delivery_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_quality_revenue_recognition_or_margin_bridge_candidate"], "stage4b_evidence_fields": ["defense_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.44, "MFE_90D_pct": 10.94, "MFE_180D_pct": 22.5, "MAE_30D_pct": -0.63, "MAE_90D_pct": -13.75, "MAE_180D_pct": -20.16, "peak_date": "2024-10-24", "peak_price": 3920.0, "drawdown_after_peak_pct": -21.17, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_export_peak_if_backlog_delivery_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_contract_cancellation_delivery_delay_margin_or_financing_break", "trigger_outcome_label": "counterexample_defense_theme_local4b_watch", "current_profile_verdict": "C03 should not treat defense/unmanned-system theme beta as durable Stage2 unless named defense program, contract backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had tradable MFE but spent much of the window in drawdown and only later spiked, making it a local 4B-watch boundary rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C03_DEFENSE_BACKLOG_010820_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "trigger_id": "TRG_R11L77-C03-003570-SNT-DYNAMICS-DEFENSE-DRIVETRAIN-EXPORT-BACKLOG", "symbol": "003570", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"defense_policy_framework_score": 13, "export_backlog_score": 15, "customer_program_score": 14, "delivery_schedule_score": 13, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"defense_policy_framework_score": 12, "export_backlog_score": 17, "customer_program_score": 16, "delivery_schedule_score": 15, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["export_backlog_score", "customer_program_score", "delivery_schedule_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 44.42, "MAE_90D_pct": -0.62, "score_return_alignment_label": "defense_export_backlog_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should allow defense component suppliers when export framework demand maps to drivetrain/transmission backlog, delivery schedule and margin bridge. SNT Dynamics produced large MFE with almost no entry-basis MAE, but lifecycle local 4B is still required if export/backlog/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "trigger_id": "TRG_R11L77-C03-272210-HANWHA-SYSTEMS-DEFENSE-ELECTRONICS-BACKLOG", "symbol": "272210", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"defense_policy_framework_score": 13, "export_backlog_score": 15, "customer_program_score": 14, "delivery_schedule_score": 13, "margin_bridge_score": 13, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"defense_policy_framework_score": 12, "export_backlog_score": 17, "customer_program_score": 16, "delivery_schedule_score": 15, "margin_bridge_score": 15, "relative_strength_score": 14, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["export_backlog_score", "customer_program_score", "delivery_schedule_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 37.46, "MAE_90D_pct": -2.54, "score_return_alignment_label": "defense_export_backlog_positive_with_lifecycle_4b", "current_profile_verdict": "C03 should include defense electronics / radar / C4I names only when policy-defense demand maps to backlog, customer program, delivery schedule and margin bridge. Hanwha Systems produced solid MFE with controlled MAE, but later drawdown says C03 must lifecycle-manage the signal."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "trigger_id": "TRG_R11L77-C03-010820-FIRSTEC-DEFENSE-UNMANNED-THEME-BETA-FADE", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"defense_policy_framework_score": 6, "export_backlog_score": 4, "customer_program_score": 3, "delivery_schedule_score": 2, "margin_bridge_score": 2, "relative_strength_score": 6, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"defense_policy_framework_score": 4, "export_backlog_score": 2, "customer_program_score": 2, "delivery_schedule_score": 1, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 21, "source_confidence_score": 2}, "weighted_score_after": 38, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["export_backlog_score", "customer_program_score", "delivery_schedule_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified defense export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge; cap defense theme beta when evidence fails to refresh.", "MFE_90D_pct": 10.94, "MAE_90D_pct": -13.75, "score_return_alignment_label": "false_positive_defense_theme_bridge_gap", "current_profile_verdict": "C03 should not treat defense/unmanned-system theme beta as durable Stage2 unless named defense program, contract backlog, delivery schedule, revenue recognition and margin bridge are visible. Firstec had tradable MFE but spent much of the window in drawdown and only later spiked, making it a local 4B-watch boundary rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R11", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "DEFENSE_SYSTEM_ELECTRONICS_DRIVETRAIN_EXPORT_BACKLOG_BRIDGE_VS_DEFENSE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C03 policy-defense symbols outside visible top-covered 012450/079550/047810/065450 set, +3 drivetrain/electronics/unmanned trigger families, +2 export-backlog positives, +1 defense theme local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R11", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "axis": "defense_system_electronics_drivetrain_export_backlog_bridge_vs_defense_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C03 should split verified defense export framework/backlog rerating from generic defense theme beta. Stage2 requires policy/defense demand plus named customer program, export backlog, delivery schedule, revenue recognition and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["003570", "272210", "010820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": 77, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C03 needs named program/backlog/delivery/margin proof. SNT Dynamics and Hanwha Systems show defense export/backlog positives after source repair; Firstec shows defense/unmanned theme beta that should be capped unless backlog and delivery bridge are verified."}
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
003570:
  name = SNT다이내믹스 from 2023-03-15
  corporate_action_candidate_dates = profile old-window only, none in selected 2024 window
  selected window = 2024-02-01~D+180
  contamination = false

272210:
  corporate_action_candidate_dates = 2021-06-23
  selected window = 2024-02-01~D+180
  contamination = false

010820:
  name = 퍼스텍 from 2002-02-19
  corporate_action_candidate_dates = 1999-11-05, 2002-02-19, 2003-07-16, 2006-12-22
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C03 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C03 rule-shape discovery,
but coding-agent promotion requires non-proxy defense export framework, named customer program, backlog, delivery schedule, revenue recognition and margin bridge evidence.
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
defense_system_electronics_drivetrain_export_backlog_bridge_vs_defense_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 003570, 272210 and 010820.
4. Keep generic C03 defense-theme weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - defense export or policy framework demand is explicit,
   - named customer program or order is visible,
   - backlog and delivery schedule are visible,
   - revenue recognition and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is defense/unmanned/component theme beta only,
   - program/backlog/delivery/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -25~35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price contract cancellation, program delay, export-policy reversal, delivery failure, financing or margin break.
8. Emit before/after diagnostics and reject if verified low-MAE defense backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R11
completed_loop = 77
next_round = R12
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

