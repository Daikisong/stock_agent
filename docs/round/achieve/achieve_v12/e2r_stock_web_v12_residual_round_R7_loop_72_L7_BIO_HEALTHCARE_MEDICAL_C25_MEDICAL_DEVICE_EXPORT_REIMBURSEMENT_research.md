# E2R Stock-Web v12 Residual Research — R7 Loop 72 / L7 / C25

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R7",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R7",
  "completed_loop": 72,
  "computed_next_round": "R8",
  "computed_next_loop": 72,
  "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL",
  "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT",
  "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA",
  "loop_objective": [
    "coverage_gap_fill",
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
```

## Round / scope resolution

Previous completed state in this interactive run: R6 / loop 72.

Therefore:

```text
scheduled_round = R7
scheduled_loop = 72
allowed_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_large_sector = L7_BIO_HEALTHCARE_MEDICAL
selected_canonical_archetype_id = C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
computed_next_round = R8
computed_next_loop = 72
```

R7 was routed to C25 because loop 71 already produced a C24 trial-data risk file.  
The goal here is to test the medical-device route: export, reimbursement, adoption, distributor sell-through, regulatory bridge, and recurring device revenue.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat already shows C25 has substantial coverage with top-symbol concentration in names such as 338220, 214150, 145720, 228670 and 328130.  
This run avoids those top-covered symbols and adds:

```text
099190 / 아이센스 / CGM launch-reimbursement adoption risk
043150 / 바텍 / dental imaging export/channel weakness
226400 / 오스테오닉 / orthopedic implant export bridge
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C25 is not simply “medical device product launched.”

The correct mechanism is:

```text
regulatory approval / reimbursement / export distributor access
→ real adoption or reorder
→ recurring device revenue / consumable pull-through / margin conversion
→ durable rerating
```

A launch headline without adoption is like a hospital room with the monitor turned on but no patient connected.  
The signal exists, but it is not yet measuring the business.

The split is:

```text
C25 positive:
  export or reimbursement bridge + adoption/reorder/distribution evidence + controlled MAE

C25 false positive:
  launch/reimbursement optimism + no adoption or export reorder bridge + high MAE

C25 local 4B:
  weak export/channel or dental/diagnostic device demand + absent bridge + MFE too small to offset drawdown
```

---

## Case 1 — Counterexample: 099190 / 아이센스 / CGM launch-reimbursement beta

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests whether CGM launch/reimbursement optimism is enough.  
The source-repair task is to verify non-proxy evidence for reimbursement uptake, adoption, export reorder, and margin conversion.

```text
evidence_family = CGM_LAUNCH_REIMBURSEMENT_ADOPTION_WITH_WEAK_EXPORT_REORDER_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 24,400
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/099/099190/2024.csv`:

```text
2024-02-01,24400,24500,23200,23750
2024-02-02,24000,25550,24000,25200
2024-04-11,19300,19650,18880,19320
2024-09-09,14820,15290,14520,15050
```

### Backtest

```text
MFE_30D  = +4.71%
MAE_30D  = -15.78%
MFE_90D  = +4.71%
MAE_90D  = -22.62%
MFE_180D = +4.71%
MAE_180D = -40.49%
peak_180 = 25,550 on 2024-02-02
trough_180 = 14,520 on 2024-09-09
peak_to_later_drawdown = -43.17%
```

### Interpretation

This is the C25 false-positive shape.  
A launch or reimbursement story can create attention, but the price path says the bridge was not enough.

For C25, the system should ask:

```text
Did reimbursement produce actual uptake?
Did export/distributor reorder appear?
Did device revenue or margin conversion improve?
```

If those are absent, this should be local 4B-watch / false Stage2, not Green.

---

## Case 2 — Risk-positive: 043150 / 바텍 / dental imaging export weakness

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests dental imaging export/channel weakness without a fresh order or reimbursement bridge.

```text
evidence_family = DENTAL_IMAGING_EXPORT_CHANNEL_WEAKNESS_WITH_NO_REIMBURSEMENT_BRIDGE
case_role = risk_positive
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/043/043150/2024.csv`:

```text
2024-02-01,32500,32500,31550,31900
2024-06-26,26400,27200,26400,26800
2024-09-04,23350,23350,22700,22700
2024-10-08,24100,25000,24050,24550
```

### Backtest

```text
MFE_30D  = +0.00%
MAE_30D  = -8.31%
MFE_90D  = +0.00%
MAE_90D  = -18.77%
MFE_180D = +0.00%
MAE_180D = -30.15%
peak_180 = 32,500 on 2024-02-01
trough_180 = 22,700 on 2024-09-04
peak_to_later_drawdown = -30.15%
```

### Interpretation

This is not a hard 4C.  
It is a local 4B watch: no MFE, widening MAE, and no verified export/reimbursement/order bridge.

C25 needs a channel-order bridge. Without that, a device manufacturer can drift lower even if the category sounds structurally healthy.

---

## Case 3 — Positive after source repair: 226400 / 오스테오닉

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is orthopedic implant export, regulatory/distribution access, and revenue conversion.

```text
evidence_family = ORTHOPEDIC_IMPLANT_EXPORT_REGULATORY_DISTRIBUTION_BRIDGE
case_role = positive
trigger_date = 2024-06-28
entry_date = 2024-07-01
entry_price = 4,580
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/226/226400/2024.csv` and `2025.csv`:

```text
2024-07-01,4580,5200,4580,5110
2024-08-05,4750,4765,4150,4265
2024-10-02,5880,6390,5810,6280
2025-02-10,8310,8880,8100,8220
2025-03-21,6980,7100,6610,6700
```

### Backtest

```text
MFE_30D  = +23.14%
MAE_30D  = -9.39%
MFE_90D  = +39.52%
MAE_90D  = -9.39%
MFE_180D = +93.89%
MAE_180D = -9.39%
peak_180 = 8,880 on 2025-02-10
trough_180 = 4,150 on 2024-08-05
peak_to_later_drawdown = -25.56%
```

### Interpretation

This is the C25 positive shape after source repair.  
The stock-web path shows strong MFE with controlled MAE. The model should not need to wait for a late price breakout if the regulatory/export/distribution bridge is verified.

But because this row is still `source_proxy_only`, it should remain a shadow candidate until source repair is complete.

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
do_not_raise_generic_C25_weight = true
do_not_treat_launch_or_reimbursement_headline_as_Green = true
do_not_convert_local_4B_device_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA
```

This fine archetype covers:

```text
1. CGM launch/reimbursement optimism without adoption → false Stage2 / local 4B
2. dental imaging export/channel weakness → local 4B-watch
3. orthopedic implant export/regulatory/distribution bridge → Stage2 possible after source repair
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "case_id": "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL", "symbol": "099190", "company": "아이센스", "trigger_type": "Stage2-FalsePositive / CGMReimbursementLaunchBeta", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 24400.0, "mfe_30_pct": 4.71, "mae_30_pct": -15.78, "mfe_90_pct": 4.71, "mae_90_pct": -22.62, "mfe_180_pct": 4.71, "mae_180_pct": -40.49, "peak_price_180": 25550.0, "peak_date_180": "2024-02-02", "trough_price_180": 14520.0, "trough_date_180": "2024-09-09", "peak_to_later_drawdown_pct": -43.17, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "CGM_LAUNCH_REIMBURSEMENT_ADOPTION_WITH_WEAK_EXPORT_REORDER_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:ISENS_CGM_LAUNCH_REIMBURSEMENT_ADOPTION_EXPORT_REORDER_BRIDGE_2024", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "case_id": "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN", "symbol": "043150", "company": "바텍", "trigger_type": "Stage4B-Local-DentalImagingExportWeakness", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32500.0, "mfe_30_pct": 0.0, "mae_30_pct": -8.31, "mfe_90_pct": 0.0, "mae_90_pct": -18.77, "mfe_180_pct": 0.0, "mae_180_pct": -30.15, "peak_price_180": 32500.0, "peak_date_180": "2024-02-01", "trough_price_180": 22700.0, "trough_date_180": "2024-09-04", "peak_to_later_drawdown_pct": -30.15, "case_role": "risk_positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "DENTAL_IMAGING_EXPORT_CHANNEL_WEAKNESS_WITH_NO_REIMBURSEMENT_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:VATECH_DENTAL_IMAGING_EXPORT_CHANNEL_WEAKNESS_ORDER_REIMBURSEMENT_BRIDGE_2024", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "case_id": "R7L72-C25-226400-OSTEONIC-ORTHOPEDIC-EXPORT-IMPLANT-BRIDGE", "symbol": "226400", "company": "오스테오닉", "trigger_type": "Stage2-Actionable-OrthopedicExportBridge", "trigger_date": "2024-06-28", "entry_date": "2024-07-01", "entry_price": 4580.0, "mfe_30_pct": 23.14, "mae_30_pct": -9.39, "mfe_90_pct": 39.52, "mae_90_pct": -9.39, "mfe_180_pct": 93.89, "mae_180_pct": -9.39, "peak_price_180": 8880.0, "peak_date_180": "2025-02-10", "trough_price_180": 4150.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -25.56, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "ORTHOPEDIC_IMPLANT_EXPORT_REGULATORY_DISTRIBUTION_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:OSTEONIC_ORTHOPEDIC_IMPLANT_EXPORT_REGULATORY_DISTRIBUTION_BRIDGE_2024", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R7L72-C25-099190-ISENS-CGM-REIMBURSEMENT-LAUNCH-BETA-FAIL", "symbol": "099190", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 2, "market_mispricing": 13, "valuation_rerating": 5, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["medical_device_export_reimbursement", "export_or_reimbursement_bridge", "bridge_weak_or_absent", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "C25 should not turn CGM launch/reimbursement optimism into durable Stage2 unless adoption, reimbursement uptake, export reorder, or margin evidence is visible. The stock-web path had small MFE and large 180D MAE."}
{"row_type": "score_simulation", "case_id": "R7L72-C25-043150-VATECH-DENTAL-IMAGING-EXPORT-SLOWDOWN", "symbol": "043150", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 3, "earnings_visibility": 4, "bottleneck_pricing_power": 2, "market_mispricing": 13, "valuation_rerating": 5, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["medical_device_export_reimbursement", "export_or_reimbursement_bridge", "bridge_weak_or_absent", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "Dental imaging export/channel narratives should require fresh order or reimbursement bridge. When MFE is absent and 180D MAE opens, C25 should route to local 4B-watch rather than Stage2/Green."}
{"row_type": "score_simulation", "case_id": "R7L72-C25-226400-OSTEONIC-ORTHOPEDIC-EXPORT-IMPLANT-BRIDGE", "symbol": "226400", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 11, "earnings_visibility": 12, "bottleneck_pricing_power": 4, "market_mispricing": 13, "valuation_rerating": 10, "capital_allocation": 1, "information_confidence": 2}, "diagnostic_flags": ["medical_device_export_reimbursement", "export_or_reimbursement_bridge", "bridge_present_after_source_repair", "stage2_candidate", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C25 should allow Stage2 when a small medtech exporter has orthopedic implant regulatory/distribution evidence that converts to export revenue. The stock-web path shows strong MFE with controlled MAE, but source repair is required before runtime promotion."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "fine_archetype_id": "MEDTECH_EXPORT_REIMBURSEMENT_ADOPTION_BRIDGE_VS_PRICE_ONLY_LAUNCH_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "risk_positive_case_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C25 symbols, +3 medtech export/reimbursement trigger families, +1 orthopedic export positive, +2 weak-adoption/export local-4B paths, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "axis": "medtech_export_reimbursement_adoption_bridge_vs_price_only_launch_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C25 should split real medtech export/reimbursement adoption bridge from price-only launch beta. Stage2 requires verified export orders, reimbursement uptake, regulatory clearance, distributor sell-through, or recurring device revenue. Weak adoption and no reorder should route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["099190", "043150", "226400"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R7", "loop": 72, "large_sector_id": "L7_BIO_HEALTHCARE_MEDICAL", "canonical_archetype_id": "C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C25 should not reward launch/reimbursement headlines without adoption or export reorder evidence. 아이센스 and 바텍 show weak/absent bridge local-4B paths, while 오스테오닉 shows a small-cap orthopedic export path that can become Stage2 if non-proxy regulatory/distribution evidence is repaired."}
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
099190:
  corporate_action_candidate_dates = 2015-10-02, 2023-03-14, 2023-04-10
  selected window = 2024-02-01~D+180
  contamination = false

043150:
  corporate_action_candidate_dates = 2010-09-02
  selected window = 2024-02-01~D+180
  contamination = false

226400:
  corporate_action_candidate_dates = 2018-02-22, 2020-07-15
  selected window = 2024-07-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C25 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and source-repair queue creation,
but coding-agent promotion requires non-proxy company-level evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R7/C25 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
medtech_export_reimbursement_adoption_bridge_vs_price_only_launch_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 099190, 043150 and 226400.
4. Keep generic C25 weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - regulatory approval, reimbursement, export, or distributor bridge is explicitly evidenced,
   - adoption/reorder or recurring device revenue is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is launch/reimbursement optimism only,
   - MFE is small or temporary,
   - MAE_180D <= -25% or peak-to-later drawdown <= -35%,
   - adoption/export bridge is weak or stale.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C25 overblocks verified medtech export positives.
```

---

## Final round state

```text
completed_round = R7
completed_loop = 72
next_round = R8
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

