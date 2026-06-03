# E2R Stock-Web v12 Residual Research — R4 Loop 79 / L4 / C17

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 79,
  "computed_next_round": "R5",
  "computed_next_loop": 79,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "chemical_commodity_margin_spread_guardrail",
    "price_cost_spread_inventory_utilization_margin_bridge",
    "defensive_spread_no_stage2_boundary",
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

Previous completed state in this interactive run: R3 / loop 79.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 79
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
computed_next_round = R5
computed_next_loop = 79
```

R4 was routed to C17 because loop 78 used C16.  
This file tests chemical commodity spread and margin bridge rows, not strategic-resource policy rows.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C17 concentration in:

```text
298020, 011780, 010060, 011170, 004000
```

This run uses three different symbols:

```text
014830 / 유니드 / KOH-caustic chemical spread-margin lifecycle
025000 / KPX케미칼 / defensive chemical spread no-Stage2 boundary
069260 / TKG휴켐스 / nitric-acid/TDI chemical spread fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C17 is not “화학 스프레드가 좋다.”

The mechanism must pass through:

```text
commodity price-cost spread
→ volume, inventory or utilization improvement
→ raw-material pass-through or contract pricing
→ margin conversion
→ durable rerating
```

화학 스프레드는 온도계다.  
C17이 보려는 것은 그 온도가 실제 가동률, 판매량, 가격 전가, 마진으로 올라가는지다.

---

## Case 1 — Spread-margin lifecycle candidate: 014830 / 유니드

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is KOH/caustic spread, export demand, inventory, utilization and margin bridge evidence.

```text
evidence_family = KOH_CAUSTIC_PRICE_COST_SPREAD_EXPORT_DEMAND_INVENTORY_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 74,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv`:

```text
2024-02-01,74500,77000,73500,76500
2024-02-21,80200,84000,79700,80200
2024-04-08,87100,88800,86000,86600
2024-07-24,100300,107000,90300,95000
2024-08-05,82400,82400,76400,78500
2024-10-25,65400,66400,65000,65200
```

### Backtest

```text
MFE_30D  = +12.75%
MAE_30D  = -4.03%
MFE_90D  = +19.19%
MAE_90D  = -5.91%
MFE_180D = +43.62%
MAE_180D = -12.75%
peak_180 = 107,000 on 2024-07-24
trough_180 = 65,000 on 2024-10-25
peak_to_later_drawdown = -39.25%
```

### Interpretation

This is a C17 spread-margin lifecycle candidate.  
The MFE was meaningful, but the post-peak drawdown means spread and margin evidence must refresh.

Correct treatment:

```text
verified KOH/caustic spread + volume/inventory/utilization + margin bridge → Stage2 possible
bridge stale after peak → local 4B-watch
```

---

## Case 2 — Defensive no-Stage2 boundary: 025000 / KPX케미칼

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests a bounded chemical-spread / cashflow name without a strong rerating bridge.

```text
evidence_family = POLYOL_CHEMICAL_SPREAD_DEFENSIVE_CASHFLOW_WITH_WEAK_RERATING_MARGIN_BRIDGE
case_role = overbearish_counterexample_defensive_no_stage2
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 43,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv`:

```text
2024-02-01,43200,44350,43200,44100
2024-02-23,45800,46100,45600,46050
2024-03-27,46400,46750,46250,46600
2024-08-05,47300,47300,45200,45900
2024-10-11,49000,49450,48900,49400
2024-11-01,47350,47350,46550,46700
```

### Backtest

```text
MFE_30D  = +6.71%
MAE_30D  = +0.00%
MFE_90D  = +8.22%
MAE_90D  = +0.00%
MFE_180D = +14.47%
MAE_180D = +0.00%
peak_180 = 49,450 on 2024-10-11
trough_180 = 43,200 on 2024-02-01
peak_to_later_drawdown = -5.56%
```

### Interpretation

This is not local 4B.  
But it is also not a durable Stage2 spread rerating unless price-cost spread, volume, utilization and margin evidence is visible.

Correct treatment:

```text
defensive spread / cashflow watch
bounded MAE
→ no forced 4B
→ no Stage2 without spread-margin bridge
```

---

## Case 3 — Counterexample / local 4B: 069260 / TKG휴켐스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests nitric-acid/TDI/MNB spread exposure without enough volume and margin refresh.

```text
evidence_family = NITRIC_ACID_TDI_MNB_CHEMICAL_SPREAD_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE
case_role = counterexample_chemical_spread_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 20,600
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv`:

```text
2024-02-01,20600,21000,20600,20950
2024-02-02,20850,21200,20700,21000
2024-04-05,19600,19680,19230,19370
2024-08-05,19020,19020,17400,17680
2024-09-09,17960,18060,17860,18040
2024-10-25,19760,19850,19680,19760
```

### Backtest

```text
MFE_30D  = +2.91%
MAE_30D  = -3.59%
MFE_90D  = +2.91%
MAE_90D  = -7.77%
MFE_180D = +2.91%
MAE_180D = -15.53%
peak_180 = 21,200 on 2024-02-02
trough_180 = 17,400 on 2024-08-05
peak_to_later_drawdown = -17.92%
```

### Interpretation

This is a weak-MFE chemical spread fade.  
The price path did not validate durable spread-margin rerating.

Correct treatment:

```text
chemical spread theme beta
→ no verified volume / utilization / raw-material pass-through / margin bridge
→ local 4B-watch only after evidence or MAE threshold confirms deterioration
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
defensive_bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C17_chemical_spread_weight = true
do_not_treat_all_spread_MFE_as_Green = true
do_not_force_4B_on_bounded_defensive_spread_rows = true
do_not_convert_chemical_spread_drawdown_to_hard_4C_without_non_price_spread_margin_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE
```

This fine archetype covers:

```text
1. KOH/caustic spread + margin bridge → Stage2 possible after source repair
2. defensive polyol/spread cashflow with bounded MAE → RiskWatch / no forced 4B
3. nitric-acid/TDI/MNB spread beta without volume/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-KOHChemicalSpreadMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should allow chemical spread positives only when commodity price/cost spread, export demand, inventory, utilization and margin bridge refreshes. Unid produced meaningful MFE and then a drawdown; it is Stage2 only after source repair and lifecycle-managed if spread/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy price/cost spread, raw-material pass-through, volume, inventory, utilization and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2", "symbol": "025000", "company_name": "KPX케미칼", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-DefensiveChemicalSpreadBoundedNoStage2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not force local 4B when a chemical name has bounded MAE and defensive cashflow, but it also should not mark Stage2 unless spread expansion, volume, utilization and margin bridge are visible. KPX Chemical is a low-volatility boundary row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy price/cost spread, raw-material pass-through, volume, inventory, utilization and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / NitricAcidChemicalSpreadFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not treat nitric-acid/TDI/MNB spread exposure as durable Stage2 unless volume, contract price, utilization, raw-material spread and margin bridge refreshes. TKG Huchems produced tiny MFE and then a persistent drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy price/cost spread, raw-material pass-through, volume, inventory, utilization and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE", "case_id": "R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE", "symbol": "014830", "company_name": "유니드", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "Stage2-Actionable-KOHChemicalSpreadMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 74500.0, "evidence_available_at_that_date": "KOH_CAUSTIC_PRICE_COST_SPREAD_EXPORT_DEMAND_INVENTORY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:UNID_2024_KOH_CAUSTIC_SPREAD_EXPORT_INVENTORY_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_price_cost_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_price_or_raw_material_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv", "profile_path": "atlas/symbol_profiles/014/014830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.75, "MFE_90D_pct": 19.19, "MFE_180D_pct": 43.62, "MAE_30D_pct": -4.03, "MAE_90D_pct": -5.91, "MAE_180D_pct": -12.75, "peak_date": "2024-07-24", "peak_price": 107000.0, "drawdown_after_peak_pct": -39.25, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_volume_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_contract_loss_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C17 should allow chemical spread positives only when commodity price/cost spread, export demand, inventory, utilization and margin bridge refreshes. Unid produced meaningful MFE and then a drawdown; it is Stage2 only after source repair and lifecycle-managed if spread/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_014830_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2", "case_id": "R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2", "symbol": "025000", "company_name": "KPX케미칼", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "RiskWatch-DefensiveChemicalSpreadBoundedNoStage2", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 43200.0, "evidence_available_at_that_date": "POLYOL_CHEMICAL_SPREAD_DEFENSIVE_CASHFLOW_WITH_WEAK_RERATING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KPX_CHEMICAL_2024_POLYOL_SPREAD_VOLUME_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_price_cost_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_price_or_raw_material_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv", "profile_path": "atlas/symbol_profiles/025/025000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.71, "MFE_90D_pct": 8.22, "MFE_180D_pct": 14.47, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-10-11", "peak_price": 49450.0, "drawdown_after_peak_pct": -5.56, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_volume_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_contract_loss_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "overbearish_counterexample_defensive_no_stage2", "current_profile_verdict": "C17 should not force local 4B when a chemical name has bounded MAE and defensive cashflow, but it also should not mark Stage2 unless spread expansion, volume, utilization and margin bridge are visible. KPX Chemical is a low-volatility boundary row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_025000_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE", "case_id": "R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE", "symbol": "069260", "company_name": "TKG휴켐스", "round": "R4", "loop": "79", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "Stage2-FalsePositive / NitricAcidChemicalSpreadFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 20600.0, "evidence_available_at_that_date": "NITRIC_ACID_TDI_MNB_CHEMICAL_SPREAD_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TKG_HUCHEMS_2024_NITRIC_ACID_TDI_MNB_SPREAD_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["chemical_price_cost_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "contract_price_or_raw_material_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/069/069260/2024.csv", "profile_path": "atlas/symbol_profiles/069/069260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.91, "MFE_90D_pct": 2.91, "MFE_180D_pct": 2.91, "MAE_30D_pct": -3.59, "MAE_90D_pct": -7.77, "MAE_180D_pct": -15.53, "peak_date": "2024-02-02", "peak_price": 21200.0, "drawdown_after_peak_pct": -17.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_volume_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_contract_loss_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "counterexample_chemical_spread_local4b", "current_profile_verdict": "C17 should not treat nitric-acid/TDI/MNB spread exposure as durable Stage2 unless volume, contract price, utilization, raw-material spread and margin bridge refreshes. TKG Huchems produced tiny MFE and then a persistent drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEM_SPREAD_069260_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE", "trigger_id": "TRG_R4L79-C17-014830-UNID-KOH-SPREAD-MARGIN-LIFECYCLE", "symbol": "014830", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"price_cost_spread_score": 14, "volume_inventory_score": 13, "utilization_score": 13, "margin_bridge_score": 14, "relative_strength_score": 12, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"price_cost_spread_score": 16, "volume_inventory_score": 15, "utilization_score": 15, "margin_bridge_score": 16, "relative_strength_score": 11, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["price_cost_spread_score", "volume_inventory_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, volume, inventory, utilization and margin bridge; cap chemical spread/theme beta when evidence fails to refresh, but do not force 4B for bounded defensive spread rows.", "MFE_90D_pct": 19.19, "MAE_90D_pct": -5.91, "score_return_alignment_label": "chemical_spread_positive_with_lifecycle_4b", "current_profile_verdict": "C17 should allow chemical spread positives only when commodity price/cost spread, export demand, inventory, utilization and margin bridge refreshes. Unid produced meaningful MFE and then a drawdown; it is Stage2 only after source repair and lifecycle-managed if spread/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2", "trigger_id": "TRG_R4L79-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-DEFENSIVE-NO-STAGE2", "symbol": "025000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"price_cost_spread_score": 8, "volume_inventory_score": 6, "utilization_score": 6, "margin_bridge_score": 5, "relative_strength_score": 4, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / defensive no-Stage2", "raw_component_scores_after": {"price_cost_spread_score": 7, "volume_inventory_score": 5, "utilization_score": 5, "margin_bridge_score": 4, "relative_strength_score": 3, "execution_risk_score": 6, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no forced local 4B", "changed_components": ["price_cost_spread_score", "volume_inventory_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, volume, inventory, utilization and margin bridge; cap chemical spread/theme beta when evidence fails to refresh, but do not force 4B for bounded defensive spread rows.", "MFE_90D_pct": 8.22, "MAE_90D_pct": 0.0, "score_return_alignment_label": "defensive_spread_no_stage2_no_4b_boundary", "current_profile_verdict": "C17 should not force local 4B when a chemical name has bounded MAE and defensive cashflow, but it also should not mark Stage2 unless spread expansion, volume, utilization and margin bridge are visible. KPX Chemical is a low-volatility boundary row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE", "trigger_id": "TRG_R4L79-C17-069260-TKG-HUCHEMS-NITRIC-ACID-SPREAD-FADE", "symbol": "069260", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"price_cost_spread_score": 4, "volume_inventory_score": 2, "utilization_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"price_cost_spread_score": 3, "volume_inventory_score": 1, "utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["price_cost_spread_score", "volume_inventory_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified price-cost spread, volume, inventory, utilization and margin bridge; cap chemical spread/theme beta when evidence fails to refresh, but do not force 4B for bounded defensive spread rows.", "MFE_90D_pct": 2.91, "MAE_90D_pct": -7.77, "score_return_alignment_label": "false_positive_chemical_spread_bridge_gap", "current_profile_verdict": "C17 should not treat nitric-acid/TDI/MNB spread exposure as durable Stage2 unless volume, contract price, utilization, raw-material spread and margin bridge refreshes. TKG Huchems produced tiny MFE and then a persistent drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 79, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "KOH_POLYOL_NITRIC_ACID_CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_SPREAD_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "overbearish_counterexample_count": 1, "counterexample_count": 1, "four_b_case_count": 2, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C17 chemical-spread symbols outside top-covered 298020/011780/010060/011170/004000 set, +3 KOH/polyol/nitric-acid trigger families, +1 spread-margin positive, +1 defensive no-Stage2/no-4B boundary, +1 chemical-spread local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 79, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "axis": "KOH_polyol_nitric_acid_chemical_spread_margin_bridge_vs_spread_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C17 should split verified chemical price-cost spread / utilization / margin rerating from generic commodity-spread theme beta. Stage2 requires spread expansion, volume or inventory improvement, utilization, raw-material pass-through and margin bridge. Local 4B requires stale/failed spread-margin bridge plus MAE or post-peak drawdown. Defensive bounded-MAE rows should stay RiskWatch/no-Stage2, not forced 4B.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["014830", "025000", "069260"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 79, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "defensive_bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C17 needs price-cost spread, volume, inventory, utilization and margin proof. Unid shows a KOH/spread-margin lifecycle candidate after source repair; KPX Chemical is a defensive bounded-MAE no-Stage2/no-forced-4B boundary; TKG Huchems shows chemical spread exposure fading when volume and margin bridge are absent or stale."}
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
  name = 유니드
  corporate_action_candidate_dates = 2015-08-18, 2022-11-28
  selected window = 2024-02-01~D+180
  contamination = false

025000:
  name = KPX케미칼 from 2008-09-11, 포리올 / 한국포리올 before that
  corporate_action_candidate_dates = 2006-09-29
  selected window = 2024-02-01~D+180
  contamination = false

069260:
  name = TKG휴켐스 from 2022-04-11, 휴켐스 before that
  corporate_action_candidate_dates = 2010-09-27
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C17 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C17 rule-shape discovery,
but coding-agent promotion requires non-proxy price-cost spread, raw-material pass-through, volume, inventory, utilization and margin evidence.
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
KOH_polyol_nitric_acid_chemical_spread_margin_bridge_vs_spread_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 014830, 025000 and 069260.
4. Keep generic C17 chemical spread weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - commodity price-cost spread is explicit,
   - volume, inventory or utilization improvement is visible,
   - raw-material pass-through or contract-pricing bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is chemical spread/theme beta only,
   - spread/volume/utilization/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when defensive spread/cashflow rows have bounded MAE and no confirmed bridge break.
8. Do not convert local 4B-watch into full 4B/4C without non-price spread collapse, contract loss, inventory impairment, financing or margin break.
9. Emit before/after diagnostics and reject if verified chemical-spread positives or bounded defensive rows are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 79
next_round = R5
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

