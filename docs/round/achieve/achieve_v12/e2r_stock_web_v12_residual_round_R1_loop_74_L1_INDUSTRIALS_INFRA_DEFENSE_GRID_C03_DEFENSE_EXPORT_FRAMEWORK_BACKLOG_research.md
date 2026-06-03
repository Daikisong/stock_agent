# E2R Stock-Web v12 Residual Research — R1 Loop 74 / L1 / C03

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 74,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 74,
  "computed_next_round": "R2",
  "computed_next_loop": 74,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG",
  "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "residual_missed_structural_mining",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
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

Previous completed state in this interactive run: R13 / loop 73.

Therefore:

```text
scheduled_round = R1
scheduled_loop = 74
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
computed_next_round = R2
computed_next_loop = 74
```

R1 was routed to C03 because loop 73 used C01 and prior loop 72 used C02.  
C03 remains thin in the No-Repeat table and is concentrated in a small set of existing defense names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C03 is concentrated in `012450`, `079550`, `047810`, and `065450`.  
This run uses three different symbols:

```text
064350 / 현대로템 / ground-systems export framework backlog
003570 / SNT다이내믹스 / defense powertrain export backlog
010820 / 퍼스텍 / defense electronics / drone price beta local 4B
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C03 is not “defense stock went up.”

The real mechanism is:

```text
named export framework
→ customer/program visibility
→ backlog and production cadence
→ margin conversion
→ durable rerating
```

A defense headline is a flare.  
A signed export framework is the convoy route.  
Backlog is the fuel truck.

The residual split is:

```text
C03 positive:
  named defense program / export framework / customer visibility
  + backlog conversion
  + production cadence and margin bridge

C03 false positive:
  electronics, drone, or defense theme beta
  + no named order/backlog bridge
  + later MAE or post-peak drawdown

C03 local 4B:
  price spike fades before program evidence refreshes
```

---

## Case 1 — Positive with later 4B-watch: 064350 / 현대로템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is K2/ground-systems export framework, customer program, production cadence, backlog and margin bridge evidence.

```text
evidence_family = K2_TANK_POLAND_GROUND_SYSTEMS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-21
entry_date = 2024-02-22
entry_price = 30,900
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv`:

```text
2024-02-22,30900,34500,30350,34500
2024-03-12,31200,31250,29900,30000
2024-07-24,46500,48300,45850,47950
2024-11-20,66700,69500,65900,67100
2024-12-09,45500,46500,44300,44450
```

### Backtest

```text
MFE_30D  = +28.16%
MAE_30D  = -3.24%
MFE_90D  = +56.31%
MAE_90D  = -3.24%
MFE_180D = +124.92%
MAE_180D = -3.24%
peak_180 = 69,500 on 2024-11-20
trough_180 = 29,900 on 2024-03-12
peak_to_later_drawdown = -36.26%
```

### Interpretation

This is a strong C03 positive-shaped path.  
The key is not defense heat; it is named ground-systems export framework and production/backlog bridge. The later post-peak drawdown means a lifecycle local 4B-watch is still needed if the evidence stops refreshing.

---

## Case 2 — Positive with later 4B-watch: 003570 / SNT다이내믹스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is defense powertrain / transmission export program, backlog, customer quality and margin bridge evidence.

```text
evidence_family = DEFENSE_POWERTRAIN_TRANSMISSION_EXPORT_BACKLOG_MARGIN_BRIDGE
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
2024-06-25,22000,22500,21000,21300
2024-10-23,27750,28200,25950,26700
2024-12-09,17580,17580,16260,16370
```

### Backtest

```text
MFE_30D  = +31.69%
MAE_30D  = -0.62%
MFE_90D  = +54.00%
MAE_90D  = -0.62%
MFE_180D = +93.02%
MAE_180D = -0.62%
peak_180 = 28,200 on 2024-10-23
trough_180 = 14,520 on 2024-02-01
peak_to_later_drawdown = -42.34%
```

### Interpretation

This is the supplier version of C03.  
Powertrain and transmission names should not be ignored if the export program creates backlog and margin conversion. But the post-peak drawdown says the positive label should decay into local 4B-watch if the backlog evidence becomes stale.

---

## Case 3 — Counterexample / local 4B: 010820 / 퍼스텍

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests defense electronics / drone-theme price beta without named export order or backlog bridge.

```text
evidence_family = DEFENSE_ELECTRONICS_DRONE_THEME_PRICE_BETA_WITH_WEAK_BACKLOG_AND_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-16
entry_date = 2024-01-17
entry_price = 3,470
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv`:

```text
2024-01-17,3470,3990,3465,3765
2024-01-25,3250,3290,3165,3195
2024-08-05,3220,3345,2685,2835
2024-09-09,2560,2710,2555,2685
```

### Backtest

```text
MFE_30D  = +14.99%
MAE_30D  = -8.79%
MFE_90D  = +14.99%
MAE_90D  = -8.79%
MFE_180D = +14.99%
MAE_180D = -26.37%
peak_180 = 3,990 on 2024-01-17
trough_180 = 2,555 on 2024-09-09
peak_to_later_drawdown = -35.96%
```

### Interpretation

This is the C03 defense-beta trap.  
The first candle looked exciting, but the path did not prove backlog or margin conversion.

The correct label is:

```text
false Stage2 / local 4B-watch
```

not durable Green.

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C03_defense_weight = true
do_not_treat_all_defense_theme_spikes_as_Green = true
do_not_convert_defense_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA
```

This fine archetype covers:

```text
1. ground-systems export framework + backlog visibility → Stage2 possible after source repair
2. defense powertrain / transmission export backlog → Stage2 possible after source repair
3. defense electronics / drone-theme beta without named order bridge → false Stage2 / local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-GroundSystemsExportBacklog", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer, backlog, production cadence and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "symbol": "003570", "company_name": "SNT다이내믹스", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-DefensePowertrainExportBacklog", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer, backlog, production cadence and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "symbol": "010820", "company_name": "퍼스텍", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "case_type": "defense_export_framework_backlog", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / DefenseElectronicsPriceBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy export framework, named customer, backlog, production cadence and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "case_id": "R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "symbol": "064350", "company_name": "현대로템", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-GroundSystemsExportBacklog", "trigger_date": "2024-02-21", "entry_date": "2024-02-22", "entry_price": 30900.0, "evidence_available_at_that_date": "K2_TANK_POLAND_GROUND_SYSTEMS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_ROTEM_2024_K2_POLAND_GROUND_SYSTEMS_EXPORT_FRAMEWORK_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework", "backlog_candidate", "customer_or_program_candidate"], "stage3_evidence_fields": ["relative_strength", "program_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_export_backlog_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.16, "MFE_90D_pct": 56.31, "MFE_180D_pct": 124.92, "MAE_30D_pct": -3.24, "MAE_90D_pct": -3.24, "MAE_180D_pct": -3.24, "peak_date": "2024-11-20", "peak_price": 69500.0, "drawdown_after_peak_pct": -36.26, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_backlog_or_price_beta_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_or_program_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C03_DEFENSE_064350_2024-02-22", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "case_id": "R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "symbol": "003570", "company_name": "SNT다이내믹스", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-DefensePowertrainExportBacklog", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 14610.0, "evidence_available_at_that_date": "DEFENSE_POWERTRAIN_TRANSMISSION_EXPORT_BACKLOG_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SNT_DYNAMICS_2024_DEFENSE_POWERTRAIN_TRANSMISSION_EXPORT_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework", "backlog_candidate", "customer_or_program_candidate"], "stage3_evidence_fields": ["relative_strength", "program_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_export_backlog_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003570/2024.csv", "profile_path": "atlas/symbol_profiles/003/003570.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.69, "MFE_90D_pct": 54.0, "MFE_180D_pct": 93.02, "MAE_30D_pct": -0.62, "MAE_90D_pct": -0.62, "MAE_180D_pct": -0.62, "peak_date": "2024-10-23", "peak_price": 28200.0, "drawdown_after_peak_pct": -42.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_backlog_or_price_beta_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_or_program_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C03_DEFENSE_003570_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "case_id": "R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "symbol": "010820", "company_name": "퍼스텍", "round": "R1", "loop": "74", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / DefenseElectronicsPriceBetaLocal4B", "trigger_date": "2024-01-16", "entry_date": "2024-01-17", "entry_price": 3470.0, "evidence_available_at_that_date": "DEFENSE_ELECTRONICS_DRONE_THEME_PRICE_BETA_WITH_WEAK_BACKLOG_AND_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:FIRSTEC_2024_DEFENSE_ELECTRONICS_DRONE_THEME_BACKLOG_MARGIN_BRIDGE", "stage2_evidence_fields": ["defense_export_framework", "backlog_candidate", "customer_or_program_candidate"], "stage3_evidence_fields": ["relative_strength", "program_backlog_margin_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010820/2024.csv", "profile_path": "atlas/symbol_profiles/010/010820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 14.99, "MFE_90D_pct": 14.99, "MFE_180D_pct": 14.99, "MAE_30D_pct": -8.79, "MAE_90D_pct": -8.79, "MAE_180D_pct": -26.37, "peak_date": "2024-01-17", "peak_price": 3990.0, "drawdown_after_peak_pct": -35.96, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_defense_backlog_or_price_beta_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_order_cancellation_or_program_margin_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C03_DEFENSE_010820_2024-01-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "trigger_id": "TRG_R1L74-C03-064350-HYUNDAI-ROTEM-K2-GROUND-SYSTEMS-BACKLOG", "symbol": "064350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 16, "margin_bridge_score": 13, "revision_score": 11, "relative_strength_score": 15, "customer_quality_score": 13, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified named export framework/backlog/customer-program bridge; cap defense electronics or drone price beta when no backlog or margin bridge is verified.", "MFE_90D_pct": 56.31, "MAE_90D_pct": -3.24, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C03 should allow Stage2 when defense-export attention is tied to a named ground-systems framework, backlog visibility, production cadence and margin bridge. Hyundai Rotem's stock-web path had large MFE and limited entry-basis MAE; after the late-2024 peak, a local 4B lifecycle guard is still needed if export/backlog evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "trigger_id": "TRG_R1L74-C03-003570-SNT-DYNAMICS-POWERTRAIN-EXPORT-BACKLOG", "symbol": "003570", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 14, "backlog_visibility_score": 15, "margin_bridge_score": 11, "revision_score": 10, "relative_strength_score": 15, "customer_quality_score": 12, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"contract_score": 16, "backlog_visibility_score": 16, "margin_bridge_score": 13, "revision_score": 11, "relative_strength_score": 15, "customer_quality_score": 13, "policy_or_regulatory_score": 4, "valuation_repricing_score": 12, "execution_risk_score": 5, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified named export framework/backlog/customer-program bridge; cap defense electronics or drone price beta when no backlog or margin bridge is verified.", "MFE_90D_pct": 54.0, "MAE_90D_pct": -0.62, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C03 should include defense powertrain and transmission suppliers when export programs convert into backlog and margin. SNT Dynamics produced a strong 180D MFE with very controlled entry MAE, but later drawdown after the October peak requires lifecycle local 4B if backlog/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "trigger_id": "TRG_R1L74-C03-010820-FIRSTEC-DEFENSE-ELECTRONICS-PRICE-BETA", "symbol": "010820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "raw_component_scores_before": {"contract_score": 3, "backlog_visibility_score": 3, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 3, "policy_or_regulatory_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 15, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 52, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 4, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 43, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified named export framework/backlog/customer-program bridge; cap defense electronics or drone price beta when no backlog or margin bridge is verified.", "MFE_90D_pct": 14.99, "MAE_90D_pct": -8.79, "score_return_alignment_label": "false_positive_defense_price_beta_bridge_gap", "current_profile_verdict": "C03 should not treat defense electronics or drone-theme price beta as durable Stage2 unless named export order, customer framework, backlog conversion or margin bridge is visible. Firstec had a same-day spike but later MAE and drawdown opened, so it is a local 4B-watch / false Stage2 row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R1", "loop": 74, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "fine_archetype_id": "GROUND_SYSTEMS_POWERTRAIN_EXPORT_BACKLOG_VS_DEFENSE_ELECTRONICS_PRICE_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused/new C03 symbols, +3 defense export/backlog/electronics trigger families, +2 structural defense positives, +1 price-beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R1", "loop": 74, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "axis": "ground_systems_powertrain_export_backlog_vs_defense_electronics_price_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C03 should split verified defense export framework/backlog from price-only defense electronics or drone beta. Stage2 requires named customer, program framework, order/backlog visibility, production cadence and margin bridge. If price beta fades and MAE/drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["064350", "003570", "010820"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": 74, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C03 needs a named defense program bridge. Hyundai Rotem and SNT Dynamics show ground-system and powertrain backlog positives after source repair; Firstec shows defense electronics/drone price beta fading into local 4B without backlog/margin proof."}
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
  corporate_action_candidate_dates = 2020-08-14
  selected window = 2024-02-22~D+180
  contamination = false

003570:
  corporate_action_candidate_dates = 1998-12-22, 2000-04-28, 2000-07-03, 2003-03-31, 2006-04-05
  selected window = 2024-02-01~D+180
  contamination = false

010820:
  corporate_action_candidate_dates = 1999-11-05, 2002-02-19, 2003-07-16, 2006-12-22
  selected window = 2024-01-17~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C03 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C03 rule-shape discovery,
but coding-agent promotion requires non-proxy export framework, program, order, backlog, production cadence and margin evidence.
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
ground_systems_powertrain_export_backlog_vs_defense_electronics_price_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 064350, 003570 and 010820.
4. Keep generic C03 defense theme weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - named export framework or customer program is explicit,
   - order/backlog visibility is present,
   - production cadence or delivery schedule is visible,
   - margin or revision bridge is credible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is defense electronics/drone/theme beta only,
   - named backlog or margin bridge is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price order cancellation, program delay, margin break, or thesis deterioration evidence.
8. Emit before/after diagnostics and reject if verified defense export backlog positives are overblocked.
```

---

## Final round state

```text
completed_round = R1
completed_loop = 74
next_round = R2
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

