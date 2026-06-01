# E2R Stock-Web v12 Residual Research — R4 Loop 76 / L4 / C17

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 76,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 76,
  "computed_next_round": "R5",
  "computed_next_loop": 76,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "chemical_spread_margin_bridge_guardrail",
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

Previous completed state in this interactive run: R3 / loop 76.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 76
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
computed_next_round = R5
computed_next_loop = 76
```

R4 was routed to C17 because loop 75 used C16 and loop 74 had already used a materials spread/resource axis.  
This file tests chemical price-cost spread / margin bridge behavior, not strategic-resource policy beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C17 is concentrated in:

```text
298020, 011780, 010060, 011170, 004000
```

This run uses three different symbols:

```text
014830 / 유니드 / KOH·가성칼륨 price-cost spread bridge
004430 / 송원산업 / specialty additive spread beta fade
120110 / 코오롱인더 / industrial chemical/material spread beta fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C17 is not “chemical stock went up.”

The mechanism must pass through:

```text
commodity / chemical price move
→ price-cost spread
→ inventory / order / utilization
→ product mix and margin bridge
→ durable rerating
```

A commodity quote is the weather report.  
The investable bridge is whether the company turns that weather into spread, volume and margin.

---

## Case 1 — Positive with lifecycle 4B: 014830 / 유니드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is KOH/caustic potash price spread, export demand, inventory, utilization and margin bridge evidence.

```text
evidence_family = KOH_CAUSTIC_POTASH_EXPORT_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-24
entry_date = 2024-01-25
entry_price = 68,300
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv`:

```text
2024-01-25,68300,76000,68200,74900
2024-02-21,80200,84000,79700,80200
2024-05-22,112000,118200,111200,115400
2024-06-11,117000,118700,112800,113200
2024-10-25,65400,66400,65000,65200
```

### Backtest

```text
MFE_30D  = +22.99%
MAE_30D  = -0.15%
MFE_90D  = +73.79%
MAE_90D  = -0.15%
MFE_180D = +73.79%
MAE_180D = -4.83%
peak_180 = 118,700 on 2024-06-11
trough_180 = 65,000 on 2024-10-25
peak_to_later_drawdown = -45.24%
```

### Interpretation

This is the useful C17 positive row.  
The move was not just a one-day beta spike; it had controlled entry-basis MAE and a large MFE path.

But durable Stage2 requires source repair:

```text
price-cost spread
export / inventory demand
utilization
margin conversion
```

Once the spread/margin bridge fades, local 4B should activate.

---

## Case 2 — Counterexample / local 4B: 004430 / 송원산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests specialty additive / polymer stabilizer spread beta without order, inventory and margin refresh.

```text
evidence_family = POLYMER_STABILIZER_SPECIALTY_ADDITIVE_SPREAD_BETA_WITH_WEAK_ORDER_MARGIN_BRIDGE
case_role = counterexample_commodity_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 15,280
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004430/2024.csv`:

```text
2024-02-01,15280,15610,15210,15590
2024-02-16,15980,16180,15900,16100
2024-03-07,14390,14420,14150,14240
2024-08-05,11240,11240,9980,10100
2024-09-20,10300,10430,10000,10000
```

### Backtest

```text
MFE_30D  = +5.89%
MAE_30D  = -6.81%
MFE_90D  = +5.89%
MAE_90D  = -20.55%
MFE_180D = +5.89%
MAE_180D = -34.69%
peak_180 = 16,180 on 2024-02-16
trough_180 = 9,980 on 2024-08-05
peak_to_later_drawdown = -38.32%
```

### Interpretation

This is a C17 false-positive / local 4B row.  
The first rebound was small and could not confirm durable spread recovery.

Correct treatment:

```text
commodity / additive beta
→ no order/inventory/margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 120110 / 코오롱인더

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests industrial chemical / film / aramid material beta without enough volume, mix and margin bridge.

```text
evidence_family = INDUSTRIAL_CHEMICAL_FILM_ARAMID_SPREAD_BETA_WITH_WEAK_VOLUME_MARGIN_BRIDGE
case_role = counterexample_industrial_material_beta_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 40,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv`:

```text
2024-02-01,40600,41900,40550,41850
2024-02-08,42150,42400,41500,41650
2024-03-07,36900,37300,36300,36350
2024-08-05,35600,35600,31400,32150
2024-10-25,32050,32150,30950,31100
```

### Backtest

```text
MFE_30D  = +4.43%
MAE_30D  = -10.59%
MFE_90D  = +4.43%
MAE_90D  = -10.71%
MFE_180D = +4.43%
MAE_180D = -23.77%
peak_180 = 42,400 on 2024-02-08
trough_180 = 30,950 on 2024-10-25
peak_to_later_drawdown = -27.00%
```

### Interpretation

This is not a hard 4C case.  
But it is also not a C17 spread-cycle positive. The price path lacks MFE and kept leaking lower.

Correct treatment:

```text
industrial material beta
→ no confirmed volume/mix/margin bridge
→ local 4B-watch / no durable Green
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
do_not_raise_generic_C17_chemical_beta_weight = true
do_not_treat_all_chemical_spread_MFE_as_Green = true
do_not_convert_chemical_material_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE
```

This fine archetype covers:

```text
1. KOH / caustic potash price-cost spread bridge → Stage2 possible after source repair
2. specialty additive beta without order/inventory bridge → false Stage2 / local 4B
3. industrial chemical/material beta without volume/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KOHCausticPotashSpreadMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should allow chemical commodity Stage2 when the commodity price/spread move connects to inventory, export demand, utilization and margin bridge. Unid produced large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if KOH/spread/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy commodity price-cost spread, inventory, order, utilization, product mix and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "symbol": "004430", "company_name": "송원산업", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SpecialtyAdditiveSpreadFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not treat specialty additive or commodity-spread beta as durable Stage2 unless order, inventory restocking, price-cost spread and margin evidence refreshes. Songwon Industrial had weak MFE and then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy commodity price-cost spread, inventory, order, utilization, product mix and margin evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / IndustrialChemicalMaterialSpreadFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not treat industrial chemical/material spread beta as durable Stage2 unless volume, product mix, price-cost spread and margin bridge are visible. Kolon Industries had very limited MFE and then a persistent drawdown, so it is a local 4B-watch row rather than a spread-cycle Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy commodity price-cost spread, inventory, order, utilization, product mix and margin evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "case_id": "R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_spread_margin_bridge_guardrail", "trigger_type": "Stage2-Actionable-KOHCausticPotashSpreadMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-24", "entry_date": "2024-01-25", "entry_price": 68300.0, "evidence_available_at_that_date": "KOH_CAUSTIC_POTASH_EXPORT_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:UNID_2024_KOH_CAUSTIC_POTASH_EXPORT_PRICE_SPREAD_INVENTORY_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_spread_or_price_cycle", "inventory_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "volume_mix_or_cost_pass_through_candidate"], "stage4b_evidence_fields": ["commodity_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv", "profile_path": "atlas/symbol_profiles/014/014830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.99, "MFE_90D_pct": 73.79, "MFE_180D_pct": 73.79, "MAE_30D_pct": -0.15, "MAE_90D_pct": -0.15, "MAE_180D_pct": -4.83, "peak_date": "2024-06-11", "peak_price": 118700.0, "drawdown_after_peak_pct": -45.24, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_order_volume_or_margin_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C17 should allow chemical commodity Stage2 when the commodity price/spread move connects to inventory, export demand, utilization and margin bridge. Unid produced large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if KOH/spread/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_014830_2024-01-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "case_id": "R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "symbol": "004430", "company_name": "송원산업", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_spread_margin_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / SpecialtyAdditiveSpreadFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15280.0, "evidence_available_at_that_date": "POLYMER_STABILIZER_SPECIALTY_ADDITIVE_SPREAD_BETA_WITH_WEAK_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SONGWON_2024_POLYMER_STABILIZER_SPECIALTY_ADDITIVE_ORDER_INVENTORY_SPREAD_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_spread_or_price_cycle", "inventory_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "volume_mix_or_cost_pass_through_candidate"], "stage4b_evidence_fields": ["commodity_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004430/2024.csv", "profile_path": "atlas/symbol_profiles/004/004430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.89, "MFE_90D_pct": 5.89, "MFE_180D_pct": 5.89, "MAE_30D_pct": -6.81, "MAE_90D_pct": -20.55, "MAE_180D_pct": -34.69, "peak_date": "2024-02-16", "peak_price": 16180.0, "drawdown_after_peak_pct": -38.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_order_volume_or_margin_break", "trigger_outcome_label": "counterexample_commodity_beta_local4b", "current_profile_verdict": "C17 should not treat specialty additive or commodity-spread beta as durable Stage2 unless order, inventory restocking, price-cost spread and margin evidence refreshes. Songwon Industrial had weak MFE and then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_004430_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "case_id": "R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "76", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_spread_margin_bridge_guardrail", "trigger_type": "Stage2-FalsePositive / IndustrialChemicalMaterialSpreadFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 40600.0, "evidence_available_at_that_date": "INDUSTRIAL_CHEMICAL_FILM_ARAMID_SPREAD_BETA_WITH_WEAK_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOLON_INDUSTRIES_2024_INDUSTRIAL_CHEMICAL_FILM_ARAMID_VOLUME_PRICE_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_spread_or_price_cycle", "inventory_or_order_bridge_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "volume_mix_or_cost_pass_through_candidate"], "stage4b_evidence_fields": ["commodity_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv", "profile_path": "atlas/symbol_profiles/120/120110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.43, "MFE_90D_pct": 4.43, "MFE_180D_pct": 4.43, "MAE_30D_pct": -10.59, "MAE_90D_pct": -10.71, "MAE_180D_pct": -23.77, "peak_date": "2024-02-08", "peak_price": 42400.0, "drawdown_after_peak_pct": -27.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_order_volume_or_margin_break", "trigger_outcome_label": "counterexample_industrial_material_beta_local4b", "current_profile_verdict": "C17 should not treat industrial chemical/material spread beta as durable Stage2 unless volume, product mix, price-cost spread and margin bridge are visible. Kolon Industries had very limited MFE and then a persistent drawdown, so it is a local 4B-watch row rather than a spread-cycle Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_120110_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "trigger_id": "TRG_R4L76-C17-014830-UNID-KOH-CAUSTIC-POTASH-SPREAD-BRIDGE", "symbol": "014830", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_spread_score": 14, "inventory_order_score": 13, "utilization_volume_score": 12, "margin_bridge_score": 14, "relative_strength_score": 13, "execution_risk_score": 7, "commodity_beta_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable after source repair", "raw_component_scores_after": {"commodity_spread_score": 16, "inventory_order_score": 15, "utilization_volume_score": 13, "margin_bridge_score": 16, "relative_strength_score": 12, "execution_risk_score": 8, "commodity_beta_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 88, "stage_label_after": "Stage2/Yellow-Green candidate after source repair + lifecycle 4B", "changed_components": ["commodity_spread_score", "inventory_order_score", "margin_bridge_score", "execution_risk_score", "commodity_beta_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, inventory/order, utilization/volume and margin bridge; cap commodity/material beta when evidence fails to refresh.", "MFE_90D_pct": 73.79, "MAE_90D_pct": -0.15, "score_return_alignment_label": "aligned_positive_with_lifecycle_4b", "current_profile_verdict": "C17 should allow chemical commodity Stage2 when the commodity price/spread move connects to inventory, export demand, utilization and margin bridge. Unid produced large MFE with controlled entry-basis MAE, but the later post-peak drawdown requires lifecycle local 4B if KOH/spread/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "trigger_id": "TRG_R4L76-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-SPREAD-FADE", "symbol": "004430", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_spread_score": 6, "inventory_order_score": 3, "utilization_volume_score": 3, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 18, "commodity_beta_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 3, "inventory_order_score": 2, "utilization_volume_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 21, "commodity_beta_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_order_score", "margin_bridge_score", "execution_risk_score", "commodity_beta_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, inventory/order, utilization/volume and margin bridge; cap commodity/material beta when evidence fails to refresh.", "MFE_90D_pct": 5.89, "MAE_90D_pct": -20.55, "score_return_alignment_label": "false_positive_chemical_spread_bridge_gap", "current_profile_verdict": "C17 should not treat specialty additive or commodity-spread beta as durable Stage2 unless order, inventory restocking, price-cost spread and margin evidence refreshes. Songwon Industrial had weak MFE and then opened a high-MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "trigger_id": "TRG_R4L76-C17-120110-KOLON-INDUSTRIES-CHEMICAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"commodity_spread_score": 6, "inventory_order_score": 3, "utilization_volume_score": 3, "margin_bridge_score": 2, "relative_strength_score": 4, "execution_risk_score": 18, "commodity_beta_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 48, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 3, "inventory_order_score": 2, "utilization_volume_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 21, "commodity_beta_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 37, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_order_score", "margin_bridge_score", "execution_risk_score", "commodity_beta_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, inventory/order, utilization/volume and margin bridge; cap commodity/material beta when evidence fails to refresh.", "MFE_90D_pct": 4.43, "MAE_90D_pct": -10.71, "score_return_alignment_label": "false_positive_chemical_spread_bridge_gap", "current_profile_verdict": "C17 should not treat industrial chemical/material spread beta as durable Stage2 unless volume, product mix, price-cost spread and margin bridge are visible. Kolon Industries had very limited MFE and then a persistent drawdown, so it is a local 4B-watch row rather than a spread-cycle Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 76, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_SPECIALTY_ADDITIVE_INDUSTRIAL_CHEMICAL_SPREAD_BRIDGE_VS_COMMODITY_BETA_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C17 chemical/material symbols outside top-covered set, +3 KOH/specialty-additive/industrial-material spread trigger families, +1 chemical-spread positive, +2 commodity beta local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 76, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "axis": "koh_specialty_additive_industrial_chemical_spread_bridge_vs_commodity_beta_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C17 should split verified chemical price-cost spread and margin recovery from generic commodity/material beta. Stage2 requires price-cost spread, inventory/order, utilization/volume, product mix and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["014830", "004430", "120110"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 76, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C17 needs price-cost spread and margin proof. Unid shows a KOH/caustic potash spread positive after source repair; Songwon Industrial and Kolon Industries show specialty additive/industrial material beta fading into local 4B when order, volume and margin bridge is absent."}
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
014830:
  corporate_action_candidate_dates = 2015-08-18, 2022-11-28
  selected window = 2024-01-25~D+180
  contamination = false

004430:
  corporate_action_candidate_dates = 1997-01-03, 2004-02-10, 2004-04-20
  selected window = 2024-02-01~D+180
  contamination = false

120110:
  corporate_action_candidate_dates = 2010-12-27
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C17 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C17 rule-shape discovery,
but coding-agent promotion requires non-proxy commodity price-cost spread, inventory, order, utilization, product mix and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C17 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
koh_specialty_additive_industrial_chemical_spread_bridge_vs_commodity_beta_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 014830, 004430 and 120110.
4. Keep generic C17 commodity/chemical beta weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - commodity or chemical price-cost spread is explicit,
   - inventory, order, volume or utilization bridge is visible,
   - product mix / cost pass-through / margin conversion exists,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is chemical/material commodity beta only,
   - spread/order/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price spread collapse, inventory impairment, order loss, volume cut, financing or margin break.
8. Emit before/after diagnostics and reject if verified chemical spread positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 76
next_round = R5
next_loop = 76
round_schedule_status = valid
round_sector_consistency = pass
```

