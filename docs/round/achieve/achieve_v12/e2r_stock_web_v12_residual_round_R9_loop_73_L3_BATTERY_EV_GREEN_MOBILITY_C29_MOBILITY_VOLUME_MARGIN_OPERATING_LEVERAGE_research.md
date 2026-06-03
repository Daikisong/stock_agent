# E2R Stock-Web v12 Residual Research — R9 Loop 73 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 73,
  "computed_next_round": "R10",
  "computed_next_loop": 73,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA",
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

Previous completed state in this interactive run: R8 / loop 73.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 73
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on C29/C30 bridge
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 73
```

R9 was routed to C29 because R10 remains the construction/PF balance-sheet round.  
This file avoids the most repeated C29 OEM rows and tests non-OEM mobility routes: tires, auto logistics, and thermal-management parts.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 coverage is concentrated in `000270`, `204320`, `011210`, `005380`, and `003490`.  
This run uses:

```text
161390 / 한국타이어앤테크놀로지 / tire price-mix and replacement-margin bridge
086280 / 현대글로비스 / post-CA logistics/PCC operating leverage
018880 / 한온시스템 / EV thermal-management beta false positive
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
086280 had corporate-action candidates on 2024-07-12 and 2024-08-02, so the selected entry is deliberately after those dates.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C29 is not “mobility stock went up.”

The proper mechanism is:

```text
volume / utilization / fleet / product mix
→ pricing, capacity or cost bridge
→ operating leverage
→ durable rerating
```

For tires, the bridge is price/mix and replacement demand.  
For logistics, it is PCC/CKD capacity, freight economics and capital return.  
For thermal parts, EV exposure is not enough unless customer volume and margin conversion are visible.

A moving car is just motion.  
C29 cares whether the drivetrain turns motion into torque.

---

## Case 1 — Positive with later 4B-watch: 161390 / 한국타이어앤테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tire price/mix, replacement demand, raw-material spread, and margin leverage evidence.

```text
evidence_family = TIRE_PRICE_MIX_REPLACEMENT_DEMAND_RAW_MATERIAL_SPREAD_MARGIN_LEVERAGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-17
entry_date = 2024-01-18
entry_price = 45,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv`:

```text
2024-01-18,45100,47600,44200,47100
2024-02-23,59100,59600,57700,58700
2024-07-31,43300,44850,43100,44650
2024-08-05,42250,42350,37850,38650
```

### Backtest

```text
MFE_30D  = +32.15%
MAE_30D  = -2.00%
MFE_90D  = +32.15%
MAE_90D  = -2.00%
MFE_180D = +32.15%
MAE_180D = -16.08%
peak_180 = 59,600 on 2024-02-23
trough_180 = 37,850 on 2024-08-05
peak_to_later_drawdown = -36.49%
```

### Interpretation

This is a C29 non-OEM positive path.  
The early price path supports tire price/mix margin leverage, but the later drawdown says the model needs a later local 4B-watch if mix/spread evidence stops refreshing.

---

## Case 2 — Positive after post-CA validation: 086280 / 현대글로비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
post_corporate_action_entry = true
```

The source-repair task is PCC/CKD capacity, freight rate, auto-logistics operating leverage, capital-return bridge, and post-corporate-action validation.

```text
evidence_family = AUTO_LOGISTICS_PCC_CKD_FREIGHT_RATE_CAPACITY_CAPITAL_RETURN_POST_CORPORATE_ACTION
case_role = positive_after_ca_validation
trigger_date = 2024-08-22
entry_date = 2024-08-23
entry_price = 108,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv` and `2025.csv`:

```text
2024-08-23,108600,115400,108000,114100
2024-09-27,123300,125200,122200,123900
2025-01-31,145500,151000,145500,149400
2025-04-08,111700,111900,106100,107000
```

### Backtest

```text
MFE_30D  = +15.29%
MAE_30D  = -2.30%
MFE_90D  = +39.04%
MAE_90D  = -2.30%
MFE_180D = +39.04%
MAE_180D = -2.30%
peak_180 = 151,000 on 2025-01-31
trough_180 = 106,100 on 2025-04-08
peak_to_later_drawdown = -29.74%
```

### Interpretation

This is the logistics/capacity version of C29.  
The post-CA entry matters: using a pre-split July window would distort the path. After the corporate-action candidates, the price path is a clean operating-leverage candidate.

Runtime promotion still needs non-proxy freight/capacity/capital-return evidence.

---

## Case 3 — Counterexample / local 4B: 018880 / 한온시스템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests EV thermal-management and auto-parts beta without customer-volume/pricing/margin conversion.

```text
evidence_family = EV_THERMAL_MANAGEMENT_VOLUME_BETA_WITH_WEAK_MARGIN_AND_CUSTOMER_VOLUME_BRIDGE
case_role = counterexample
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,160
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv`:

```text
2024-02-01,6160,6420,6120,6360
2024-02-02,6360,6550,6260,6480
2024-03-19,5910,5930,5590,5590
2024-08-05,4290,4300,3800,3870
```

### Backtest

```text
MFE_30D  = +6.33%
MAE_30D  = -9.25%
MFE_90D  = +6.33%
MAE_90D  = -23.21%
MFE_180D = +6.33%
MAE_180D = -38.31%
peak_180 = 6,550 on 2024-02-02
trough_180 = 3,800 on 2024-08-05
peak_to_later_drawdown = -41.98%
```

### Interpretation

This is the C29 false-positive path.  
The EV thermal-management label is not enough. If customer-volume and pricing/margin conversion are weak, the model should route to local 4B-watch rather than durable Stage2.

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
do_not_raise_generic_C29_mobility_weight = true
do_not_treat_all_auto_parts_or_EV_parts_beta_as_Green = true
do_not_convert_mobility_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA
```

This fine archetype covers:

```text
1. tire price/mix + replacement demand + margin leverage → Stage2 possible after source repair
2. logistics/PCC/CKD capacity + post-CA validation → Stage2 possible after source repair
3. thermal-management EV parts beta without margin/customer-volume bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TirePriceMixMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy volume, pricing, mix, logistics capacity, capital-return or margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "symbol": "086280", "company_name": "현대글로비스", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-LogisticsPCCMarginBridgePostCA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy volume, pricing, mix, logistics capacity, capital-return or margin evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ThermalEVPartsBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy volume, pricing, mix, logistics capacity, capital-return or margin evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "case_id": "R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-TirePriceMixMarginBridge", "trigger_date": "2024-01-17", "entry_date": "2024-01-18", "entry_price": 45100.0, "evidence_available_at_that_date": "TIRE_PRICE_MIX_REPLACEMENT_DEMAND_RAW_MATERIAL_SPREAD_MARGIN_LEVERAGE", "evidence_source": "source_proxy_manual_verification_required:HANKOOK_TIRE_2024_PRICE_MIX_REPLACEMENT_RAW_MATERIAL_SPREAD_MARGIN_LEVERAGE", "stage2_evidence_fields": ["mobility_volume_or_utilization", "margin_bridge_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_capacity_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_mobility_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 32.15, "MFE_90D_pct": 32.15, "MFE_180D_pct": 32.15, "MAE_30D_pct": -2.0, "MAE_90D_pct": -2.0, "MAE_180D_pct": -16.08, "peak_date": "2024-02-23", "peak_price": 59600.0, "drawdown_after_peak_pct": -36.49, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_operating_leverage_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_customer_volume_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C29_MOBILITY_161390_2024-01-18", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "case_id": "R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "symbol": "086280", "company_name": "현대글로비스", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable-LogisticsPCCMarginBridgePostCA", "trigger_date": "2024-08-22", "entry_date": "2024-08-23", "entry_price": 108600.0, "evidence_available_at_that_date": "AUTO_LOGISTICS_PCC_CKD_FREIGHT_RATE_CAPACITY_CAPITAL_RETURN_POST_CORPORATE_ACTION", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_GLOVIS_2024_AUTO_LOGISTICS_PCC_CKD_MARGIN_CAPITAL_RETURN_BRIDGE_POST_CA", "stage2_evidence_fields": ["mobility_volume_or_utilization", "margin_bridge_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_capacity_bridge_candidate"], "stage4b_evidence_fields": ["later_local_4b_after_mobility_peak_if_bridge_stale"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086280/2024.csv", "profile_path": "atlas/symbol_profiles/086/086280.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.29, "MFE_90D_pct": 39.04, "MFE_180D_pct": 39.04, "MAE_30D_pct": -2.3, "MAE_90D_pct": -2.3, "MAE_180D_pct": -2.3, "peak_date": "2025-01-31", "peak_price": 151000.0, "drawdown_after_peak_pct": -29.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_operating_leverage_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_customer_volume_break", "trigger_outcome_label": "positive_after_ca_validation", "current_profile_verdict": "C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C29_MOBILITY_086280_2024-08-23", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "case_id": "R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "73", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-FalsePositive / ThermalEVPartsBetaLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6160.0, "evidence_available_at_that_date": "EV_THERMAL_MANAGEMENT_VOLUME_BETA_WITH_WEAK_MARGIN_AND_CUSTOMER_VOLUME_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANON_SYSTEMS_2024_EV_THERMAL_MANAGEMENT_CUSTOMER_VOLUME_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["mobility_volume_or_utilization", "margin_bridge_candidate", "operating_leverage_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_mix_or_capacity_bridge_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "profile_path": "atlas/symbol_profiles/018/018880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.33, "MFE_90D_pct": 6.33, "MFE_180D_pct": 6.33, "MAE_30D_pct": -9.25, "MAE_90D_pct": -23.21, "MAE_180D_pct": -38.31, "peak_date": "2024-02-02", "peak_price": 6550.0, "drawdown_after_peak_pct": -41.98, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_operating_leverage_peak_if_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_customer_volume_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C29_MOBILITY_018880_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "trigger_id": "TRG_R9L73-C29-161390-HANKOOKTIRE-PRICE-MIX-MARGIN-LEVERAGE", "symbol": "161390", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 12, "pricing_mix_score": 14, "margin_bridge_score": 14, "capital_return_or_capacity_score": 3, "relative_strength_score": 13, "customer_quality_score": 9, "valuation_repricing_score": 11, "execution_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"volume_or_utilization_score": 13, "pricing_mix_score": 16, "margin_bridge_score": 16, "capital_return_or_capacity_score": 2, "relative_strength_score": 12, "customer_quality_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 5, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified pricing/mix/capacity-to-margin bridge; cap price-only mobility or EV thermal beta when customer volume and margin evidence are weak.", "MFE_90D_pct": 32.15, "MAE_90D_pct": -2.0, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C29 should include tire price/mix and replacement-demand margin leverage, not only OEM vehicle volume. 한국타이어 produced a strong MFE with controlled early MAE, but later post-peak drawdown means local 4B-watch is needed if margin/mix evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "trigger_id": "TRG_R9L73-C29-086280-GLOVIS-PCC-LOGISTICS-MARGIN-POST-CA", "symbol": "086280", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 12, "pricing_mix_score": 8, "margin_bridge_score": 14, "capital_return_or_capacity_score": 10, "relative_strength_score": 13, "customer_quality_score": 9, "valuation_repricing_score": 11, "execution_risk_score": 5, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"volume_or_utilization_score": 13, "pricing_mix_score": 10, "margin_bridge_score": 16, "capital_return_or_capacity_score": 12, "relative_strength_score": 12, "customer_quality_score": 9, "valuation_repricing_score": 10, "execution_risk_score": 5, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage3-Yellow/Green candidate after source repair", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified pricing/mix/capacity-to-margin bridge; cap price-only mobility or EV thermal beta when customer volume and margin evidence are weak.", "MFE_90D_pct": 39.04, "MAE_90D_pct": -2.3, "score_return_alignment_label": "aligned_positive_or_lifecycle_positive", "current_profile_verdict": "C29 should include logistics/PCC/CKD operating leverage when freight rate, capacity and capital-return bridge are visible. Because Hyundai Glovis had 2024 corporate-action candidates, the entry is placed after the 2024-08-02 candidate; the post-CA path is strong but needs source repair."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "trigger_id": "TRG_R9L73-C29-018880-HANON-THERMAL-EV-BETA-LOCAL4B", "symbol": "018880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_or_utilization_score": 5, "pricing_mix_score": 3, "margin_bridge_score": 3, "capital_return_or_capacity_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "valuation_repricing_score": 5, "execution_risk_score": 16, "source_confidence_score": 2}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"volume_or_utilization_score": 3, "pricing_mix_score": 2, "margin_bridge_score": 2, "capital_return_or_capacity_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "valuation_repricing_score": 4, "execution_risk_score": 18, "source_confidence_score": 2}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["pricing_mix_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified pricing/mix/capacity-to-margin bridge; cap price-only mobility or EV thermal beta when customer volume and margin evidence are weak.", "MFE_90D_pct": 6.33, "MAE_90D_pct": -23.21, "score_return_alignment_label": "false_positive_margin_bridge_gap", "current_profile_verdict": "C29 should not treat EV thermal-management or auto-parts theme beta as durable Stage2 when customer volume, pricing and margin conversion are weak. Hanon generated only small MFE and later severe MAE, making it a local 4B-watch / false Stage2 row."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_LOGISTICS_THERMAL_PARTS_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C29 symbols, +3 tire/logistics/thermal trigger families, +2 margin-leverage positives, +1 EV thermal beta false-positive/local-4B path, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "tire_logistics_thermal_parts_margin_leverage_vs_price_only_mobility_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified pricing/mix/capacity/logistics-to-margin operating leverage from price-only mobility or EV parts beta. Stage2 requires tire price/mix, replacement demand, PCC/CKD capacity, freight-rate, customer volume, capital return or margin conversion evidence. If MFE fades and MAE/drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["161390", "086280", "018880"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 73, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 should not be limited to OEM volume. 한국타이어 and 현대글로비스 show price/mix and logistics-capacity operating leverage after source repair; 한온시스템 shows EV thermal-management beta failing without customer-volume/margin bridge."}
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
161390:
  corporate_action_candidate_dates = none
  selected window = 2024-01-18~D+180
  contamination = false

086280:
  corporate_action_candidate_dates = 2024-07-12, 2024-08-02
  selected window = 2024-08-23~D+180
  contamination = false because entry is after the latest 2024 corporate-action candidate

018880:
  corporate_action_candidate_dates = 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12
  selected window = 2024-02-01~2024-08-05 within 180D evidence window
  contamination = false for the measured 2024 path, but full coding-agent validation should avoid extending through 2025-01-09 without adjustment
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy volume, pricing, mix, capacity, freight-rate, customer-volume and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
tire_logistics_thermal_parts_margin_leverage_vs_price_only_mobility_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 161390, 086280 and 018880.
4. Validate 086280 post-corporate-action basis before using it as runtime evidence.
5. Keep generic C29 mobility weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - volume/utilization or mix evidence is explicit,
   - pricing, freight-rate, capacity, replacement demand or customer-volume bridge exists,
   - margin or operating leverage conversion is visible,
   - MAE remains controlled.
7. Consider local 4B-watch when:
   - the trigger is price-only mobility or EV-parts beta,
   - customer-volume or margin evidence is weak/stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
9. Emit before/after diagnostics and reject if verified tire/logistics operating-leverage positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 73
next_round = R10
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

