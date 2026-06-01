# E2R Stock-Web v12 Residual Research — R4 Loop 73 / L4 / C17

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 73,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 73,
  "computed_next_round": "R5",
  "computed_next_loop": 73,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA",
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

Previous completed state in this interactive run: R3 / loop 73.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 73
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
computed_next_round = R5
computed_next_loop = 73
```

R4 was routed to C17 because loop 71 and loop 72 already covered C15/C16-style material spread and strategic resource policy.  
This run avoids the most repeated C17 symbols and tests product-specific spread versus price-only commodity beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C17 has existing coverage concentrated in `298020`, `011780`, `010060`, `011170`, and `004000`.  
This run uses:

```text
014830 / 유니드 / caustic potash spread bridge
010950 / S-Oil / refining spread beta local 4B
120110 / 코오롱인더 / industrial material spread fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C17 is not “commodity went up.”

The mechanism has to cross the bridge:

```text
chemical/refining/material price move
→ product-specific spread
→ utilization or export price
→ margin revision
→ durable rerating
```

A spread is like wind in a sail.  
It only moves the ship if the sail is actually connected to the mast.  
Generic commodity beta is just the flag flapping.

---

## Case 1 — Positive with later 4B-watch: 014830 / 유니드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is caustic potash / KOH spread, export price, utilization, and margin conversion evidence.

```text
evidence_family = CAUSTIC_POTASH_KOH_SPREAD_EXPORT_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-04-24
entry_date = 2024-04-25
entry_price = 91,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv`:

```text
2024-04-25,91700,101700,91100,92000
2024-05-22,112000,118200,111200,115400
2024-06-24,101900,103600,92100,95500
2024-12-09,60800,60800,58700,59000
```

### Backtest

```text
MFE_30D  = +28.90%
MAE_30D  = -0.65%
MFE_90D  = +28.90%
MAE_90D  = -0.65%
MFE_180D = +28.90%
MAE_180D = -35.99%
peak_180 = 118,200 on 2024-05-22
trough_180 = 58,700 on 2024-12-09
peak_to_later_drawdown = -50.34%
```

### Interpretation

This is the positive spread-bridge shape, but with a lifecycle warning.  
The early path had strong MFE and controlled MAE. After the peak, the drawdown says the model needs a later local 4B-watch if spread evidence stops refreshing.

---

## Case 2 — Counterexample: 010950 / S-Oil

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The row tests refinery/crack-spread beta without verified margin revision bridge.

```text
evidence_family = REFINING_CRACK_SPREAD_PRICE_BETA_WITH_WEAK_MARGIN_REVISION_BRIDGE
case_role = counterexample
trigger_date = 2024-04-10
entry_date = 2024-04-11
entry_price = 83,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv`:

```text
2024-04-11,83500,84500,82700,82700
2024-05-17,69300,69700,68800,68800
2024-06-27,66200,66700,66000,66300
2024-12-09,54900,54900,53400,53600
```

### Backtest

```text
MFE_30D  = +1.20%
MAE_30D  = -17.60%
MFE_90D  = +1.20%
MAE_90D  = -20.96%
MFE_180D = +1.20%
MAE_180D = -36.05%
peak_180 = 84,500 on 2024-04-11
trough_180 = 53,400 on 2024-12-09
peak_to_later_drawdown = -36.80%
```

### Interpretation

This is the C17 price-only commodity beta trap.  
The stock did not translate refining spread talk into a return path. Without inventory, utilization, crack spread and earnings revision evidence, this is local 4B-watch / false Stage2, not Green.

---

## Case 3 — Risk-positive: 120110 / 코오롱인더

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is aramid, tire cord, film or industrial-material spread-to-margin refresh evidence.

```text
evidence_family = ARAMID_TIRECORD_FILM_INDUSTRIAL_MATERIAL_SPREAD_WITH_WEAK_MARGIN_REFRESH
case_role = risk_positive
trigger_date = 2024-04-24
entry_date = 2024-04-25
entry_price = 36,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv`:

```text
2024-04-25,36500,38400,36250,38000
2024-05-22,42350,44150,41800,43350
2024-07-05,37300,37450,36200,36400
2024-12-09,26300,26300,25700,25800
```

### Backtest

```text
MFE_30D  = +20.96%
MAE_30D  = -0.68%
MFE_90D  = +20.96%
MAE_90D  = -0.82%
MFE_180D = +20.96%
MAE_180D = -29.59%
peak_180 = 44,150 on 2024-05-22
trough_180 = 25,700 on 2024-12-09
peak_to_later_drawdown = -41.79%
```

### Interpretation

This is the industrial-material spread fade.  
The first leg looked like margin recovery. The later path says the bridge did not refresh enough.

The correct C17 rule is:

```text
spread-to-margin evidence verified → Stage2 possible
spread optimism without refresh + MAE/drawdown → local 4B-watch
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
do_not_raise_generic_C17_weight = true
do_not_treat_all_chemical_or_refining_spread_beta_as_Green = true
do_not_convert_spread_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA
```

This fine archetype covers:

```text
1. product-specific caustic/potash spread + margin bridge → Stage2 possible after source repair
2. refinery/crack-spread price beta without revision bridge → false Stage2 / local 4B
3. aramid/tire-cord/film spread optimism without margin refresh → local 4B-watch
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-CausticPotashSpreadBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, utilization, export price, product mix or margin revision evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "symbol": "010950", "company_name": "S-Oil", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RefiningSpreadBetaLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, utilization, export price, product mix or margin revision evidence must be attached before runtime promotion."}
{"row_type": "case", "case_id": "R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "risk_positive", "best_trigger": "Stage2-FalsePositive / IndustrialMaterialSpreadFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, utilization, export price, product mix or margin revision evidence must be attached before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "case_id": "R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable-CausticPotashSpreadBridge", "trigger_date": "2024-04-24", "entry_date": "2024-04-25", "entry_price": 91700.0, "evidence_available_at_that_date": "CAUSTIC_POTASH_KOH_SPREAD_EXPORT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:UNID_2024_CAUSTIC_POTASH_KOH_SPREAD_EXPORT_MARGIN_BRIDGE", "stage2_evidence_fields": ["commodity_spread", "margin_bridge_candidate", "product_specific_spread"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv", "profile_path": "atlas/symbol_profiles/014/014830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 28.9, "MFE_90D_pct": 28.9, "MFE_180D_pct": 28.9, "MAE_30D_pct": -0.65, "MAE_90D_pct": -0.65, "MAE_180D_pct": -35.99, "peak_date": "2024-05-22", "peak_price": 118200.0, "drawdown_after_peak_pct": -50.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_contract_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C17_CHEMICAL_SPREAD_014830_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "case_id": "R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "symbol": "010950", "company_name": "S-Oil", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / RefiningSpreadBetaLocal4B", "trigger_date": "2024-04-10", "entry_date": "2024-04-11", "entry_price": 83500.0, "evidence_available_at_that_date": "REFINING_CRACK_SPREAD_PRICE_BETA_WITH_WEAK_MARGIN_REVISION_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SOIL_2024_REFINING_CRACK_SPREAD_INVENTORY_UTILIZATION_MARGIN_REVISION_BRIDGE", "stage2_evidence_fields": ["commodity_spread", "margin_bridge_candidate", "product_specific_spread"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010950/2024.csv", "profile_path": "atlas/symbol_profiles/010/010950.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.2, "MFE_90D_pct": 1.2, "MFE_180D_pct": 1.2, "MAE_30D_pct": -17.6, "MAE_90D_pct": -20.96, "MAE_180D_pct": -36.05, "peak_date": "2024-04-11", "peak_price": 84500.0, "drawdown_after_peak_pct": -36.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_contract_break", "trigger_outcome_label": "counterexample", "current_profile_verdict": "C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C17_CHEMICAL_SPREAD_010950_2024-04-11", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "case_id": "R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "company_name": "코오롱인더", "round": "R4", "loop": "73", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-FalsePositive / IndustrialMaterialSpreadFade", "trigger_date": "2024-04-24", "entry_date": "2024-04-25", "entry_price": 36500.0, "evidence_available_at_that_date": "ARAMID_TIRECORD_FILM_INDUSTRIAL_MATERIAL_SPREAD_WITH_WEAK_MARGIN_REFRESH", "evidence_source": "source_proxy_manual_verification_required:KOLON_INDUSTRIES_2024_ARAMID_TIRECORD_FILM_SPREAD_MARGIN_REFRESH", "stage2_evidence_fields": ["commodity_spread", "margin_bridge_candidate", "product_specific_spread"], "stage3_evidence_fields": ["relative_strength", "spread_to_margin_conversion_candidate"], "stage4b_evidence_fields": ["bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/120/120110/2024.csv", "profile_path": "atlas/symbol_profiles/120/120110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.96, "MFE_90D_pct": 20.96, "MFE_180D_pct": 20.96, "MAE_30D_pct": -0.68, "MAE_90D_pct": -0.82, "MAE_180D_pct": -29.59, "peak_date": "2024-05-22", "peak_price": 44150.0, "drawdown_after_peak_pct": -41.79, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_spread_peak_if_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_margin_or_contract_break", "trigger_outcome_label": "risk_positive", "current_profile_verdict": "C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "C17_CHEMICAL_SPREAD_120110_2024-04-25", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "trigger_id": "TRG_R4L73-C17-014830-UNID-CAUSTIC-POTASH-SPREAD-MARGIN-BRIDGE", "symbol": "014830", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 13, "revision_score": 10, "relative_strength_score": 12, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 15, "revision_score": 11, "relative_strength_score": 12, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 82, "stage_label_after": "Stage2-Actionable after source repair / later local 4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Reward only product-specific spread-to-margin bridge; cap generic commodity/refining/material beta when evidence fails to refresh and MAE opens.", "MFE_90D_pct": 28.9, "MAE_90D_pct": -0.65, "score_return_alignment_label": "positive_with_later_4b", "current_profile_verdict": "C17 should allow Stage2 only when a commodity/spread move connects to product-specific spread, export price, cost pass-through, and margin conversion. 유니드 produced a real MFE path, but later collapse means local 4B-watch should activate if spread evidence stops refreshing."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "trigger_id": "TRG_R4L73-C17-010950-SOIL-REFINING-SPREAD-BETA-LOCAL4B", "symbol": "010950", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Reward only product-specific spread-to-margin bridge; cap generic commodity/refining/material beta when evidence fails to refresh and MAE opens.", "MFE_90D_pct": 1.2, "MAE_90D_pct": -20.96, "score_return_alignment_label": "false_positive_or_risk_positive_bridge_gap", "current_profile_verdict": "C17 should not treat refinery spread beta as Green unless crack spread, inventory, utilization, and earnings revision bridge are visible. S-Oil produced almost no MFE and later severe 180D MAE, so local 4B-watch is more appropriate."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "trigger_id": "TRG_R4L73-C17-120110-KOLONIND-INDUSTRIAL-MATERIAL-SPREAD-FADE", "symbol": "120110", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 1, "backlog_visibility_score": 2, "margin_bridge_score": 4, "revision_score": 3, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 49, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"contract_score": 1, "backlog_visibility_score": 1, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 4, "customer_quality_score": 3, "policy_or_regulatory_score": 0, "valuation_repricing_score": 4, "execution_risk_score": 16, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 42, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Reward only product-specific spread-to-margin bridge; cap generic commodity/refining/material beta when evidence fails to refresh and MAE opens.", "MFE_90D_pct": 20.96, "MAE_90D_pct": -0.82, "score_return_alignment_label": "false_positive_or_risk_positive_bridge_gap", "current_profile_verdict": "C17 industrial materials should require spread-to-margin refresh. 코오롱인더 produced an initial MFE on industrial-material optimism, but later MAE and drawdown widened; this supports local 4B-watch unless aramid/tire-cord/film margin evidence refreshes."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 73, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CAUSTIC_POTASH_REFINING_INDUSTRIAL_MATERIAL_SPREAD_BRIDGE_VS_PRICE_ONLY_COMMODITY_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "risk_positive_case_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 2, "diversity_score_summary": "+3 underused C17 symbols, +3 chemical/refining/industrial-material spread families, +1 positive spread bridge, +2 local-4B/fade paths, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 73, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "axis": "caustic_potash_refining_industrial_material_spread_bridge_vs_price_only_commodity_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C17 should split product-specific spread-to-margin conversion from generic commodity/refining/material beta. Stage2 requires spread, utilization, export price, product mix, and margin revision evidence. If spread evidence fades and MAE/post-peak drawdown opens, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["014830", "010950", "120110"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 73, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C17 needs product-specific spread-to-margin proof. 유니드 shows a valid spread bridge with later 4B lifecycle; S-Oil shows refining beta failing without margin revision; 코오롱인더 shows industrial material spread optimism fading into local 4B."}
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
  selected window = 2024-04-25~D+180
  contamination = false

010950:
  corporate_action_candidate_dates = 2001-12-03
  selected window = 2024-04-11~D+180
  contamination = false

120110:
  corporate_action_candidate_dates = 2010-12-27
  selected window = 2024-04-25~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C17 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C17 rule-shape discovery,
but coding-agent promotion requires non-proxy spread, utilization, export-price, product-mix and margin-revision evidence.
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
caustic_potash_refining_industrial_material_spread_bridge_vs_price_only_commodity_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 014830, 010950 and 120110.
4. Keep generic C17 commodity/spread weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - product-specific spread evidence is explicit,
   - utilization/export price/product mix is improving,
   - margin revision or earnings bridge is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is generic commodity/refining/material beta,
   - spread evidence fails to refresh,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if verified product-spread positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 73
next_round = R5
next_loop = 73
round_schedule_status = valid
round_sector_consistency = pass
```

