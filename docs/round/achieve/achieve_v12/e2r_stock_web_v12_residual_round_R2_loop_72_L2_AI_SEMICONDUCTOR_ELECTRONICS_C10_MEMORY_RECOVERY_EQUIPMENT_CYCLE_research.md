# E2R Stock-Web v12 Residual Research — R2 Loop 72 / L2 / C10

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 72,
  "computed_next_round": "R3",
  "computed_next_loop": 72,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA",
  "loop_objective": [
    "coverage_gap_fill",
    "residual_missed_structural_mining",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression"
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

Previous completed state in this interactive run: R1 / loop 72.

Therefore:

```text
scheduled_round = R2
scheduled_loop = 72
allowed_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_large_sector = L2_AI_SEMICONDUCTOR_ELECTRONICS
selected_canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
computed_next_round = R3
computed_next_loop = 72
```

R2 was routed to C10 because the no-repeat coverage table lists C06, C07, C08, C09, then moves to C11. C10 therefore behaves like a missing R2 canonical coverage gap rather than a crowded HBM equipment rerun.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected rows:

```text
240810 / 원익IPS / Stage2-Actionable / 2024-02-29
036930 / 주성엔지니어링 / Stage2-FalsePositive / 2024-02-28
084370 / 유진테크 / Stage2-Actionable / 2024-02-20
```

Data-quality note:

```text
All three rows are calibration-usable on stock-web OHLC,
but non-price evidence is source_proxy_only=true / evidence_url_pending=true.
They should be treated as source-repair candidates before any runtime weight change.
```

## Research thesis

C10 is not HBM equipment relative strength.  
C10 is the older, broader mechanism: memory cycle trough → capex restart → process equipment orders → revenue/margin conversion.

The price path can brighten before the furnace is actually loaded.  
The rule should ask whether the equipment maker has real order visibility, not merely whether DRAM/NAND sentiment warmed up.

```text
C10 positive:
  memory recovery + capex restart + customer/order visibility + process equipment conversion

C10 local 4B watch:
  memory recovery beta + high MFE + weak/stale order bridge + post-peak drawdown
```

---

## Case 1 — Positive with later local 4B watch: 240810 / 원익IPS

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included as a C10 price-path anchor, not as a production-ready weight row.  
The non-price bridge to repair is memory recovery → process-equipment capex restart → order/revenue conversion.

```text
evidence_family = MEMORY_RECOVERY_CAPEX_RESTART_PROCESS_EQUIPMENT_ORDER_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-02-28
entry_date = 2024-02-29
entry_price = 28,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/240/240810/2024.csv`:

```text
2024-02-29,28700,33250,28600,32800
2024-04-08,42950,44850,41400,41650
2024-09-19,29000,29000,27650,28450
```

### Backtest

```text
MFE_30D  = +56.27%
MAE_30D  = -0.35%
MFE_90D  = +56.27%
MAE_90D  = -0.70%
MFE_180D = +56.27%
MAE_180D = -3.66%
peak_180 = 44,850 on 2024-04-08
trough_180 = 27,650 on 2024-09-19
peak_to_later_drawdown = -38.35%
```

### Interpretation

The entry was attractive on return/MAE alignment, but the post-peak drawdown shows why C10 needs two labels:

```text
early Stage2-Actionable if order/capex evidence is verified
later local 4B-watch once peak-to-later drawdown opens and fresh order evidence is absent
```

---

## Case 2 — Counterexample: 036930 / 주성엔지니어링

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included as a C10 counterexample.  
The non-price bridge to repair is whether the 2024 price spike had fresh memory-equipment order visibility, or whether it was simply memory recovery beta.

```text
evidence_family = MEMORY_RECOVERY_EQUIPMENT_BETA_WITH_WEAK_ORDER_VISIBILITY
case_role = counterexample
trigger_date = 2024-02-27
entry_date = 2024-02-28
entry_price = 34,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/036/036930/2024.csv`:

```text
2024-02-28,34700,40750,34150,40000
2024-04-08,38450,41450,36250,36500
2024-09-09,22200,22950,22050,22700
```

### Backtest

```text
MFE_30D  = +19.45%
MAE_30D  = -4.18%
MFE_90D  = +19.45%
MAE_90D  = -8.79%
MFE_180D = +19.45%
MAE_180D = -36.46%
peak_180 = 41,450 on 2024-04-08
trough_180 = 22,050 on 2024-09-09
peak_to_later_drawdown = -46.80%
```

### Interpretation

This is the C10 false-positive pattern.  
The chart initially moved with the memory-equipment basket, but MFE was not large enough to compensate for later MAE and drawdown.

The rule candidate is:

```text
if memory recovery evidence is generic
and no fresh customer/order/capex bridge is confirmed
and MAE_180D <= -25%
then classify as local 4B-watch / false Stage2 rather than Green.
```

---

## Case 3 — Positive anchor: 084370 / 유진테크

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row is included as a positive OHLC anchor.  
The bridge to repair is customer capex restart / process equipment order visibility.

```text
evidence_family = MEMORY_RECOVERY_PROCESS_EQUIPMENT_CUSTOMER_CAPEX_RESTART
case_role = positive
trigger_date = 2024-02-19
entry_date = 2024-02-20
entry_price = 34,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/084/084370/2024.csv`:

```text
2024-02-20,34500,38150,34500,36700
2024-05-28,53800,60000,53600,56500
2024-11-19,33700,33800,32450,33250
```

### Backtest

```text
MFE_30D  = +29.57%
MAE_30D  = -0.43%
MFE_90D  = +73.91%
MAE_90D  = -0.43%
MFE_180D = +73.91%
MAE_180D = -5.94%
peak_180 = 60,000 on 2024-05-28
trough_180 = 32,450 on 2024-11-19
peak_to_later_drawdown = -45.92%
```

### Interpretation

This is a strong positive C10 anchor, but even here the later post-peak drawdown is large.  
Therefore C10 should not be implemented as a simple positive weight. It needs a lifecycle:

```text
Stage2 early when capex/order bridge is verified
local 4B-watch after peak if fresh order bridge stops updating
full 4B only when non-price deterioration appears
```

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
do_not_raise_generic_C10_weight_yet = true
do_not_treat_all_memory_recovery_equipment_names_as_Green = true
do_not_relax_full_4B_non_price_evidence = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA
```

This fine archetype covers:

```text
1. memory recovery + process-equipment order/capex bridge → Stage2-Actionable possible
2. memory recovery beta without fresh order visibility → false Stage2 / local 4B-watch
3. positive equipment-cycle winner after peak → local 4B-watch if bridge evidence stops refreshing
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "case_id": "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE", "symbol": "240810", "company": "원익IPS", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-28", "entry_date": "2024-02-29", "entry_price": 28700.0, "mfe_30_pct": 56.27, "mae_30_pct": -0.35, "mfe_90_pct": 56.27, "mae_90_pct": -0.7, "mfe_180_pct": 56.27, "mae_180_pct": -3.66, "peak_price_180": 44850.0, "peak_date_180": "2024-04-08", "trough_price_180": 27650.0, "trough_date_180": "2024-09-19", "peak_to_later_drawdown_pct": -38.35, "case_role": "positive_with_later_4b_watch", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "MEMORY_RECOVERY_CAPEX_RESTART_PROCESS_EQUIPMENT_ORDER_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:WONIKIPS_MEMORY_RECOVERY_CAPEX_RESTART_PROCESS_EQUIPMENT_2024", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "case_id": "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA", "symbol": "036930", "company": "주성엔지니어링", "trigger_type": "Stage2-FalsePositive / Stage4B-Local-PriceOnly", "trigger_date": "2024-02-27", "entry_date": "2024-02-28", "entry_price": 34700.0, "mfe_30_pct": 19.45, "mae_30_pct": -4.18, "mfe_90_pct": 19.45, "mae_90_pct": -8.79, "mfe_180_pct": 19.45, "mae_180_pct": -36.46, "peak_price_180": 41450.0, "peak_date_180": "2024-04-08", "trough_price_180": 22050.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -46.8, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "MEMORY_RECOVERY_EQUIPMENT_BETA_WITH_WEAK_ORDER_VISIBILITY", "evidence_url": "source_proxy_manual_verification_required:JUSUNG_ENGINEERING_MEMORY_RECOVERY_EQUIPMENT_BETA_WEAK_ORDER_VISIBILITY_2024", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "case_id": "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE", "symbol": "084370", "company": "유진테크", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-20", "entry_price": 34500.0, "mfe_30_pct": 29.57, "mae_30_pct": -0.43, "mfe_90_pct": 73.91, "mae_90_pct": -0.43, "mfe_180_pct": 73.91, "mae_180_pct": -5.94, "peak_price_180": 60000.0, "peak_date_180": "2024-05-28", "trough_price_180": 32450.0, "trough_date_180": "2024-11-19", "peak_to_later_drawdown_pct": -45.92, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "MEMORY_RECOVERY_PROCESS_EQUIPMENT_CUSTOMER_CAPEX_RESTART", "evidence_url": "source_proxy_manual_verification_required:EUGENETECH_MEMORY_RECOVERY_PROCESS_EQUIPMENT_CUSTOMER_CAPEX_RESTART_2024", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R2L72-C10-240810-WONIKIPS-MEMORY-RECOVERY-EQUIPMENT-BRIDGE", "symbol": "240810", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 13, "bottleneck_pricing_power": 11, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["memory_recovery_equipment_cycle", "capex_restart_bridge_present", "local_4b_watch_after_peak_drawdown", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable with later local 4B watch", "profile_stress_result": "C10 should permit early Stage2 when memory recovery is tied to wafer-fab equipment order/capex restart evidence, but later post-peak drawdown shows the same case also needs local 4B-watch once capex timing cools."}
{"row_type": "score_simulation", "case_id": "R2L72-C10-036930-JUSUNG-MEMORY-EQUIPMENT-PRICE-ONLY-BETA", "symbol": "036930", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 7, "earnings_visibility": 7, "bottleneck_pricing_power": 6, "market_mispricing": 13, "valuation_rerating": 13, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["memory_recovery_equipment_cycle", "capex_bridge_weak_or_stale", "local_4b_watch_after_peak_drawdown", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "Generic memory equipment recovery beta is not enough for Green. Without fresh order/backlog/customer evidence, modest MFE followed by high 180D MAE should be routed to local 4B-watch rather than durable Stage2."}
{"row_type": "score_simulation", "case_id": "R2L72-C10-084370-EUGENETECH-MEMORY-RECOVERY-LP-CVD-ORDER-BRIDGE", "symbol": "084370", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 12, "earnings_visibility": 13, "bottleneck_pricing_power": 11, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["memory_recovery_equipment_cycle", "capex_restart_bridge_present", "local_4b_watch_after_peak_drawdown", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable with later local 4B watch", "profile_stress_result": "C10 should reward equipment-cycle recovery only when the signal has memory capex restart and process-equipment customer linkage, not merely AI/HBM theme price beta."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "fine_archetype_id": "MEMORY_RECOVERY_CAPEX_RESTART_EQUIPMENT_ORDER_VISIBILITY_VS_PRICE_ONLY_RECOVERY_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 new C10 symbols, +3 memory equipment trigger families, +2 positive cycle anchors, +1 weak-order-visibility counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "axis": "memory_recovery_capex_restart_equipment_order_visibility_vs_price_only_recovery_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C10 should split memory-recovery equipment signals into capex/order/customer bridge positives and price-only recovery-beta local-4B watches. Do not raise generic C10 weight until non-proxy evidence repair is complete.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["240810", "036930", "084370"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R2", "loop": 72, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C10 memory recovery equipment cycle should be driven by capex restart, customer/order visibility and process-equipment conversion, not by generic memory price recovery beta. Even positive anchors need local 4B-watch after peak if post-peak drawdown exceeds roughly 35%."}
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
240810:
  corporate_action_candidate_dates = none
  selected window = 2024-02-29~D+180
  contamination = false

036930:
  corporate_action_candidate_dates = 2000-06-22
  selected window = 2024-02-28~D+180
  contamination = false

084370:
  corporate_action_candidate_dates = 2007-05-17, 2010-01-22, 2012-06-07
  selected window = 2024-02-20~D+180
  contamination = false
```

External sector context to verify in source repair:

```text
- SK Hynix 2024 DRAM/HBM capacity investment and M15X capex restart.
- South Korea 2024 semiconductor support package including equipment makers.
- Company-level non-proxy evidence for 240810, 036930 and 084370 should be attached before promotion.
```

Data-quality caveat:

```text
All three rows are source_proxy_only / evidence_url_pending.
They are useful as C10 stock-web price-path calibration rows,
but coding-agent promotion requires non-proxy company-level evidence repair.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R2/C10 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
memory_recovery_capex_restart_equipment_order_visibility_vs_price_only_recovery_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 240810, 036930 and 084370.
4. Keep generic C10 positive weight unchanged until source repair is complete.
5. Consider scoped Stage2 bridge logic only when:
   - memory recovery evidence exists,
   - customer/order/capex restart evidence is present,
   - equipment maker has process-equipment revenue or margin conversion path,
   - evidence is not merely HBM/AI/memory price beta.
6. Consider local-4B-watch if:
   - peak_to_later_drawdown <= -35%,
   - MAE_180D <= -25% or evidence bridge stops refreshing,
   - order/capex bridge is stale/weak,
   - valuation rerating has outrun actual equipment-cycle confirmation.
7. Do not convert local 4B-watch into full 4B without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C10 missed structural positives increase.
```

---

## Final round state

```text
completed_round = R2
completed_loop = 72
next_round = R3
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

