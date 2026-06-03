# E2R Stock-Web v12 Residual Research — R3 Loop 73 / L3 / C14

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 73,
  "computed_next_round": "R4",
  "computed_next_loop": 73,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R2 / loop 73.

Therefore:

```text
scheduled_round = R3
scheduled_loop = 73
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
computed_next_round = R4
computed_next_loop = 73
```

R3 was routed to C14 because loop 72 already filled C12.  
This file avoids the most repeated C14 symbols and tests separator/material demand-slowdown transfer.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
361610 / SK아이이테크놀로지 / Stage4B-Local-SeparatorDemandSlowdown / 2024-04-25
393890 / 더블유씨피 / Stage4B-Local-SeparatorCustomerDemand / 2024-04-25
051910 / LG화학 / Stage2-RiskWatch / NoHard4C / 2024-04-25
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C14 is not simply “EV demand slowed.”

The chain is layered:

```text
EV demand slowdown
→ cell-maker capex/order pacing
→ separator and material utilization pressure
→ MAE and post-peak drawdown
```

But the severity differs by business model.  
A pure separator supplier is a tight spring: lower utilization quickly releases downside.  
An integrated chemical/material company has more buffers, so the same slowdown should not become hard 4C without explicit non-price thesis break.

---

## Case 1 — Risk-positive: 361610 / SK아이이테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is separator utilization, customer volume, and EV demand slowdown evidence.

```text
evidence_family = SEPARATOR_UTILIZATION_EV_DEMAND_SLOWDOWN_WITH_WEAK_CUSTOMER_VOLUME_BRIDGE
case_role = risk_positive
trigger_date = 2024-04-25
entry_date = 2024-04-25
entry_price = 63,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv`:

```text
2024-04-25,63800,64000,61400,61700
2024-04-29,63000,64200,62200,63600
2024-05-23,48900,49000,47400,47550
2024-08-05,36000,36200,30950,32000
```

### Backtest

```text
MFE_30D  = +0.63%
MAE_30D  = -25.47%
MFE_90D  = +0.63%
MAE_90D  = -51.49%
MFE_180D = +0.63%
MAE_180D = -51.49%
peak_180 = 64,200 on 2024-04-29
trough_180 = 30,950 on 2024-08-05
peak_to_later_drawdown = -51.79%
```

### Interpretation

This is a clean C14 local 4B row.  
The stock did not generate enough MFE to compensate for utilization/demand risk. The correct label is local 4B-watch, not hard 4C unless non-price evidence confirms structural break.

---

## Case 2 — Risk-positive: 393890 / 더블유씨피

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is separator customer demand, capex/utilization, and margin pressure evidence.

```text
evidence_family = SEPARATOR_CUSTOMER_DEMAND_SLOWDOWN_CAPEX_UTILIZATION_MARGIN_RISK
case_role = risk_positive
trigger_date = 2024-04-25
entry_date = 2024-04-25
entry_price = 31,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv`:

```text
2024-04-25,31750,33150,31750,32500
2024-05-03,36650,38050,36650,37100
2024-08-05,23450,23450,20200,20450
2024-10-24,16260,16340,15630,15730
```

### Backtest

```text
MFE_30D  = +19.84%
MAE_30D  = +0.00%
MFE_90D  = +19.84%
MAE_90D  = -50.46%
MFE_180D = +19.84%
MAE_180D = -50.46%
peak_180 = 38,050 on 2024-05-03
trough_180 = 15,730 on 2024-10-24
peak_to_later_drawdown = -58.66%
```

### Interpretation

This is the “MFE exists but bridge fails” version of C14.  
The early rally would seduce a price-only model, but the later 180D path says customer utilization/margin risk dominated.

---

## Case 3 — Overbearish counterexample: 051910 / LG화학

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests whether diversified chemical/cathode exposure should be classified as hard 4C after EV-material demand slowdown.

```text
evidence_family = INTEGRATED_CHEMICAL_CATHODE_EV_DEMAND_SLOWDOWN_WITH_DIVERSIFIED_BUFFER
case_role = overbearish_counterexample
trigger_date = 2024-04-25
entry_date = 2024-04-25
entry_price = 377,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv`:

```text
2024-04-25,377000,380000,371500,373000
2024-04-30,397500,412000,390500,402500
2024-08-05,302500,304500,263500,272500
2024-09-27,360000,368500,353500,357500
```

### Backtest

```text
MFE_30D  = +9.28%
MAE_30D  = -1.46%
MFE_90D  = +9.28%
MAE_90D  = -30.11%
MFE_180D = +9.28%
MAE_180D = -30.11%
peak_180 = 412,000 on 2024-04-30
trough_180 = 263,500 on 2024-08-05
peak_to_later_drawdown = -36.04%
```

### Interpretation

This is not bullish.  
But it is also not hard 4C.

The drawdown justifies RiskWatch or local 4B boundary. The later rebound and diversified business buffer mean hard 4C should wait for explicit non-price evidence such as impairment, plant restructuring, contract cancellation, or customer thesis break.

---

## Cross-case residual finding

### What this strengthens

```text
local_4b_watch_guard = strengthen
hard_4c_confirmation = strengthen
stage2_required_bridge = strengthen
```

### What this does not justify

```text
do_not_turn_all_EV_slowdown_into_hard_4C = true
do_not_ignore_pure_separator_supplier_utilization_beta = true
do_not_treat_material_rebound_as_Stage2_without_demand_bridge = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C
```

This fine archetype covers:

```text
1. pure separator utilization/customer slowdown → local 4B-watch
2. separator supplier with early MFE then severe drawdown → local 4B-watch after bridge failure
3. integrated chemical/cathode exposure → RiskWatch/no hard 4C unless non-price break appears
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "case_type": "ev_demand_slowdown_4b_4c_boundary", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SeparatorDemandSlowdown", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy EV demand, customer utilization, capex, material margin or buffer evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "case_type": "ev_demand_slowdown_4b_4c_boundary", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage4B-Local-SeparatorCustomerDemand", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy EV demand, customer utilization, capex, material margin or buffer evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "case_type": "ev_demand_slowdown_4b_4c_boundary", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-RiskWatch / NoHard4C", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy EV demand, customer utilization, capex, material margin or buffer evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "case_id": "R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "loop_objective": "counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-Local-SeparatorDemandSlowdown", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 63800.0, "evidence_available_at_that_date": "SEPARATOR_UTILIZATION_EV_DEMAND_SLOWDOWN_WITH_WEAK_CUSTOMER_VOLUME_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SKIET_2024_SEPARATOR_UTILIZATION_EV_DEMAND_SLOWDOWN_CUSTOMER_VOLUME_BRIDGE", "stage2_evidence_fields": ["slow_ev_demand", "demand_risk_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "post_peak_drawdown", "utilization_or_customer_demand_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.63, "MFE_90D_pct": 0.63, "MFE_180D_pct": 0.63, "MAE_30D_pct": -25.47, "MAE_90D_pct": -51.49, "MAE_180D_pct": -51.49, "peak_date": "2024-04-29", "peak_price": 64200.0, "drawdown_after_peak_pct": -51.79, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_slowdown_confirmation", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_contract_or_impairment_break", "trigger_outcome_label": "risk_positive", "current_profile_verdict": "C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_361610_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "case_id": "R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "symbol": "393890", "company_name": "더블유씨피", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "loop_objective": "counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B-Local-SeparatorCustomerDemand", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 31750.0, "evidence_available_at_that_date": "SEPARATOR_CUSTOMER_DEMAND_SLOWDOWN_CAPEX_UTILIZATION_MARGIN_RISK", "evidence_source": "source_proxy_manual_verification_required:WCP_2024_SEPARATOR_CUSTOMER_DEMAND_CAPEX_UTILIZATION_MARGIN_RISK", "stage2_evidence_fields": ["slow_ev_demand", "demand_risk_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "post_peak_drawdown", "utilization_or_customer_demand_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/393/393890/2024.csv", "profile_path": "atlas/symbol_profiles/393/393890.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.84, "MFE_90D_pct": 19.84, "MFE_180D_pct": 19.84, "MAE_30D_pct": -0.0, "MAE_90D_pct": -50.46, "MAE_180D_pct": -50.46, "peak_date": "2024-05-03", "peak_price": 38050.0, "drawdown_after_peak_pct": -58.66, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_slowdown_confirmation", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_contract_or_impairment_break", "trigger_outcome_label": "risk_positive", "current_profile_verdict": "Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_393890_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "case_id": "R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "loop_objective": "counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-RiskWatch / NoHard4C", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 377000.0, "evidence_available_at_that_date": "INTEGRATED_CHEMICAL_CATHODE_EV_DEMAND_SLOWDOWN_WITH_DIVERSIFIED_BUFFER", "evidence_source": "source_proxy_manual_verification_required:LGCHEM_2024_EV_MATERIAL_DEMAND_SLOWDOWN_INTEGRATED_BUSINESS_BUFFER", "stage2_evidence_fields": ["slow_ev_demand", "demand_risk_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["MAE_widening", "post_peak_drawdown", "utilization_or_customer_demand_risk"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2024.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.28, "MFE_90D_pct": 9.28, "MFE_180D_pct": 9.28, "MAE_30D_pct": -1.46, "MAE_90D_pct": -30.11, "MAE_180D_pct": -30.11, "peak_date": "2024-04-30", "peak_price": 412000.0, "drawdown_after_peak_pct": -36.04, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_slowdown_confirmation", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_contract_or_impairment_break", "trigger_outcome_label": "overbearish_counterexample", "current_profile_verdict": "C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C14_EV_DEMAND_SLOWDOWN_051910_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "trigger_id": "TRG_R3L73-C14-361610-SKIET-SEPARATOR-DEMAND-SLOWDOWN-LOCAL4B", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 16, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 41, "stage_label_before": "Stage4B-local-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no Stage2", "changed_components": ["relative_strength_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "EV demand slowdown should route separator suppliers to local 4B when utilization/customer volume risk opens MAE; integrated chemical buffer should prevent hard 4C without explicit non-price break.", "MFE_90D_pct": 0.63, "MAE_90D_pct": -51.49, "score_return_alignment_label": "risk_positive_alignment", "current_profile_verdict": "C14 should fire local 4B-watch when EV demand slowdown translates into separator utilization pressure and the stock path opens severe MAE. Hard 4C still requires non-price evidence such as plant impairment, contract cancellation, insolvency, or structural customer loss."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "trigger_id": "TRG_R3L73-C14-393890-WCP-SEPARATOR-CUSTOMER-DEMAND-LOCAL4B", "symbol": "393890", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 5, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 16, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 41, "stage_label_before": "Stage4B-local-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 1, "revision_score": 1, "relative_strength_score": 2, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 18, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 35, "stage_label_after": "Stage4B-local-watch / no Stage2", "changed_components": ["relative_strength_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "EV demand slowdown should route separator suppliers to local 4B when utilization/customer volume risk opens MAE; integrated chemical buffer should prevent hard 4C without explicit non-price break.", "MFE_90D_pct": 19.84, "MAE_90D_pct": -50.46, "score_return_alignment_label": "risk_positive_alignment", "current_profile_verdict": "Separator suppliers need stricter C14 treatment than diversified cell or chemical names. WCP produced initial MFE, but the later 180D MAE and post-peak drawdown show customer demand/utilization risk converting into local 4B-watch."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "trigger_id": "TRG_R3L73-C14-051910-LGCHEM-INTEGRATED-MATERIALS-DEMAND-RISK-NO-HARD4C", "symbol": "051910", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 5, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 10, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 48, "stage_label_before": "RiskWatch / no hard 4C", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 4, "revision_score": 1, "relative_strength_score": 6, "customer_quality_score": 1, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 11, "legal_or_contract_risk_score": 5, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 50, "stage_label_after": "RiskWatch / no hard 4C without non-price break", "changed_components": ["relative_strength_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "EV demand slowdown should route separator suppliers to local 4B when utilization/customer volume risk opens MAE; integrated chemical buffer should prevent hard 4C without explicit non-price break.", "MFE_90D_pct": 9.28, "MAE_90D_pct": -30.11, "score_return_alignment_label": "overbearish_no_hard4c_boundary", "current_profile_verdict": "C14 should flag EV/material demand slowdown risk, but not convert diversified integrated chemical/cathode exposure into hard 4C when later rebound and business-buffer evidence can exist. The correct label is RiskWatch/local 4B boundary, not hard thesis break without non-price evidence."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R3", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_MATERIAL_UTILIZATION_DEMAND_SLOWDOWN_LOCAL4B_VS_INTEGRATED_BUFFER_NO_HARD4C", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "risk_positive_case_count": 2, "overbearish_counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C14 symbols, +2 separator/material slowdown trigger families, +2 local-4B risk positives, +1 integrated-buffer no-hard-4C counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R3", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "axis": "separator_material_utilization_demand_slowdown_local4b_vs_integrated_buffer_no_hard4c", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C14 should split pure separator suppliers from diversified integrated materials names. Separator/customer-utilization slowdown with severe MAE should become local 4B-watch. Integrated chemical/cathode exposure should remain RiskWatch/no-hard-4C unless explicit contract, impairment, plant, or customer thesis break appears.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["361610", "393890", "051910"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "existing_axis_strengthened": ["local_4b_watch_guard", "hard_4c_confirmation", "stage2_required_bridge"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C14 should not flatten all EV slowdown cases. Separator suppliers behave like high-beta utilization risk and deserve local 4B when MAE opens. Integrated chemical/cathode exposure can be risky but should not be hard 4C without non-price thesis break."}
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
361610:
  corporate_action_candidate_dates = none
  selected window = 2024-04-25~D+180
  contamination = false

393890:
  corporate_action_candidate_dates = none
  selected window = 2024-04-25~D+180
  contamination = false

051910:
  corporate_action_candidate_dates = none
  selected window = 2024-04-25~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C14 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C14 rule-shape discovery,
but coding-agent promotion requires non-proxy EV demand, utilization, capex/order, margin, impairment or buffer evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R3/C14 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
separator_material_utilization_demand_slowdown_local4b_vs_integrated_buffer_no_hard4c

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 361610, 393890 and 051910.
4. Keep hard 4C evidence-based:
   - impairment,
   - plant closure or restructuring,
   - contract cancellation,
   - customer thesis break,
   - insolvency/refinancing break.
5. Use local 4B-watch when:
   - EV demand slowdown or capex/order delay exists,
   - pure separator/material supplier exposure is present,
   - MAE_90D <= -25% or MAE_180D <= -30%,
   - post-peak drawdown <= -35%.
6. Keep RiskWatch/no-hard-4C when:
   - integrated chemical/cathode exposure has diversified buffer,
   - price drawdown occurs but non-price thesis break is not confirmed.
7. Emit before/after diagnostics and reject if C14 overclassifies integrated buffered names as hard 4C.
```

---

## Final round state

```text
completed_round = R3
completed_loop = 73
next_round = R4
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

