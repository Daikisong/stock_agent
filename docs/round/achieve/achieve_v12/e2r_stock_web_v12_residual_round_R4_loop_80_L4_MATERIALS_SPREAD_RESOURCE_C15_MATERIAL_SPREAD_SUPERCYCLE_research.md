# E2R Stock-Web v12 Residual Research — R4 Loop 80 / L4 / C15

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 80,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 80,
  "computed_next_round": "R5",
  "computed_next_loop": 80,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "material_spread_supercycle_guardrail",
    "nonferrous_smelter_spread_event_separation",
    "steel_lithium_resource_theme_margin_fade_boundary",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation",
    "share_count_validation_queue_creation"
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

Previous completed state in this interactive run: R3 / loop 80.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 80
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
computed_next_round = R5
computed_next_loop = 80
```

R4 was routed to C15 because loop 79 R4 used C17 and C15 still has metal/steel/resource spread residual space.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C15 concentration in:

```text
006260, 011170, 103140, 006650, 011780
```

This run uses three different symbols:

```text
010130 / 고려아연 / nonferrous smelter spread + event separation
005490 / POSCO홀딩스 / steel-lithium resource spread fade
004020 / 현대제철 / steel spread and margin fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
010130 and 005490 show share-count changes inside the selected window and require coding-agent validation.
010130 also needs governance/event separation before runtime promotion.
```

## Research thesis

C15 is not “원자재가 올랐다.”

The mechanism must pass through:

```text
commodity price or resource cycle
→ price-cost spread / TC-RC / raw-material pass-through
→ inventory and utilization
→ volume or shipment cadence
→ margin conversion
→ durable rerating
```

소재 스프레드는 파도다.  
C15가 보려는 것은 파도 높이가 아니라 그 파도가 실제 재고 회전, 가동률, 가격 전가, 마진을 해안으로 밀어 올리는지다.

---

## Case 1 — Nonferrous positive with event separation: 010130 / 고려아연

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
event_separation_required = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is zinc/copper/precious-metal smelter spread, TC/RC, inventory, utilization, margin bridge and governance/event separation evidence.

```text
evidence_family = NONFERROUS_ZINC_COPPER_PRECIOUS_METAL_SMELTER_SPREAD_INVENTORY_MARGIN_BRIDGE_WITH_GOVERNANCE_EVENT_SEPARATION
case_role = positive_lifecycle_with_event_separation_and_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 467,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv`:

```text
2024-02-01,467500,477500,466000,475000
2024-03-06,443500,443500,435000,436000
2024-05-21,535000,546000,530000,537000
2024-07-12,542000,543000,534000,541000
2024-08-05,478000,478000,445000,454500
2024-10-29,1335000,1543000,1319000,1543000
2024-10-31,864000,1084000,830000,998000
```

### Backtest

```text
MFE_30D  = +2.35%
MAE_30D  = -6.95%
MFE_90D  = +16.79%
MAE_90D  = -6.95%
MFE_180D = +230.05%
MAE_180D = -6.95%
peak_180 = 1,543,000 on 2024-10-29
trough_180 = 435,000 on 2024-03-06~2024-03-07
peak_to_later_drawdown = -46.21%
```

### Interpretation

This is a large C15 MFE row, but not a clean pure-spread row.  
The late 2024 move must be split between nonferrous spread economics and governance/tender-event mechanics.

Correct treatment:

```text
verified smelter spread / TC-RC / inventory / utilization / margin bridge → Stage2 possible
governance/event separation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 005490 / POSCO홀딩스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

This row tests steel/lithium/resource beta without enough steel spread, lithium economics, inventory and margin bridge.

```text
evidence_family = STEEL_LITHIUM_RESOURCE_THEME_WITH_WEAK_VOLUME_PRICE_COST_SPREAD_AND_MARGIN_BRIDGE
case_role = counterexample_steel_lithium_resource_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 422,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv`:

```text
2024-02-01,422500,440000,417000,437000
2024-03-05,453000,471000,447000,447000
2024-04-08,390500,404500,380500,403000
2024-08-05,351000,351000,309000,314500
2024-09-30,391000,395500,384500,385000
2024-10-25,341000,345500,332500,335500
```

### Backtest

```text
MFE_30D  = +11.48%
MAE_30D  = -1.30%
MFE_90D  = +11.48%
MAE_90D  = -9.94%
MFE_180D = +11.48%
MAE_180D = -26.86%
peak_180 = 471,000 on 2024-03-05
trough_180 = 309,000 on 2024-08-05
peak_to_later_drawdown = -34.39%
```

### Interpretation

This is a C15 false-positive / local-4B boundary.  
A tradable bounce happened, but it did not validate durable steel/lithium spread rerating.

Correct treatment:

```text
steel/lithium/resource theme beta
→ no verified volume / inventory / price-cost spread / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 004020 / 현대제철

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests HRC/rebar/auto steel spread beta without enough volume, utilization and price pass-through.

```text
evidence_family = STEEL_HRC_REBAR_AUTO_STEEL_SPREAD_VOLUME_UTILIZATION_MARGIN_BRIDGE_WEAK
case_role = counterexample_steel_spread_margin_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 33,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv`:

```text
2024-02-01,33200,35500,33150,34900
2024-02-13,36700,37500,36200,36350
2024-04-08,32000,32150,31600,31850
2024-08-05,26800,26900,24350,24800
2024-09-09,24100,24550,23750,24350
2024-10-25,26500,26750,25050,25550
```

### Backtest

```text
MFE_30D  = +12.95%
MAE_30D  = -0.15%
MFE_90D  = +12.95%
MAE_90D  = -4.82%
MFE_180D = +12.95%
MAE_180D = -28.46%
peak_180 = 37,500 on 2024-02-13
trough_180 = 23,750 on 2024-09-09~2024-09-12
peak_to_later_drawdown = -36.67%
```

### Interpretation

This is the steel-spread fade row.  
The early move did not become durable margin spread rerating.

Correct treatment:

```text
steel spread beta
→ no verified utilization / price pass-through / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
event_separation_guard = strengthen
share_count_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C15_material_spread_weight = true
do_not_treat_all_resource_or_steel_MFE_as_Green = true
do_not_ingest_event_driven_nonferrous_MFE_without_event_separation = true
do_not_convert_material_spread_drawdown_to_hard_4C_without_non_price_spread_margin_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE
```

This fine archetype covers:

```text
1. nonferrous smelter spread with governance/event separation → Stage2 possible after source repair
2. steel/lithium/resource beta without spread-margin bridge → false Stage2 / local 4B
3. steel spread beta without utilization and pass-through bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-NonferrousSmelterSpreadWithGovernanceEventSeparation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should allow nonferrous smelter positives only when zinc/copper/precious-metal spread, TC/RC, inventory, utilization and margin bridge are visible. Korea Zinc produced enormous MFE, but a late governance/tender-event component must be separated from commodity-spread economics before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy metal/steel spread, inventory, utilization, price pass-through, TC/RC or raw-material spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SteelLithiumResourceSpreadThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat steel/lithium/resource beta as durable Stage2 unless steel spread, lithium resource economics, inventory, volume, pricing and margin bridge refreshes. POSCO Holdings had a tradable bounce but then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy metal/steel spread, inventory, utilization, price pass-through, TC/RC or raw-material spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE", "symbol": "004020", "company_name": "현대제철", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "case_type": "material_spread_supercycle", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / SteelSpreadMarginFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C15 should not treat steel spread beta as durable Stage2 unless HRC/rebar/auto steel volume, utilization, raw-material spread, price pass-through and margin bridge are visible. Hyundai Steel produced modest MFE and then a high-MAE downtrend.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy metal/steel spread, inventory, utilization, price pass-through, TC/RC or raw-material spread and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE", "case_id": "R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE", "symbol": "010130", "company_name": "고려아연", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail", "trigger_type": "Stage2-Lifecycle-NonferrousSmelterSpreadWithGovernanceEventSeparation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 467500.0, "evidence_available_at_that_date": "NONFERROUS_ZINC_COPPER_PRECIOUS_METAL_SMELTER_SPREAD_INVENTORY_MARGIN_BRIDGE_WITH_GOVERNANCE_EVENT_SEPARATION", "evidence_source": "source_proxy_manual_verification_required:KOREA_ZINC_2024_NONFERROUS_SMELTER_SPREAD_TC_RC_INVENTORY_MARGIN_AND_GOVERNANCE_EVENT_SEPARATION", "stage2_evidence_fields": ["commodity_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_pass_through_or_TC_RC_candidate"], "stage4b_evidence_fields": ["material_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010130/2024.csv", "profile_path": "atlas/symbol_profiles/010/010130.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.35, "MFE_90D_pct": 16.79, "MFE_180D_pct": 230.05, "MAE_30D_pct": -6.95, "MAE_90D_pct": -6.95, "MAE_180D_pct": -6.95, "peak_date": "2024-10-29", "peak_price": 1543000.0, "drawdown_after_peak_pct": -46.21, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_material_spread_peak_if_spread_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_contract_loss_margin_or_financing_break", "trigger_outcome_label": "positive_lifecycle_with_event_separation_and_later_4b_watch", "current_profile_verdict": "C15 should allow nonferrous smelter positives only when zinc/copper/precious-metal spread, TC/RC, inventory, utilization and margin bridge are visible. Korea Zinc produced enormous MFE, but a late governance/tender-event component must be separated from commodity-spread economics before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C15_MATERIAL_SPREAD_010130_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE", "case_id": "R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE", "symbol": "005490", "company_name": "POSCO홀딩스", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail", "trigger_type": "Stage2-FalsePositive / SteelLithiumResourceSpreadThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 422500.0, "evidence_available_at_that_date": "STEEL_LITHIUM_RESOURCE_THEME_WITH_WEAK_VOLUME_PRICE_COST_SPREAD_AND_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:POSCO_HOLDINGS_2024_STEEL_LITHIUM_RESOURCE_SPREAD_VOLUME_INVENTORY_MARGIN_BRIDGE", "stage2_evidence_fields": ["commodity_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_pass_through_or_TC_RC_candidate"], "stage4b_evidence_fields": ["material_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005490/2024.csv", "profile_path": "atlas/symbol_profiles/005/005490.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.48, "MFE_90D_pct": 11.48, "MFE_180D_pct": 11.48, "MAE_30D_pct": -1.3, "MAE_90D_pct": -9.94, "MAE_180D_pct": -26.86, "peak_date": "2024-03-05", "peak_price": 471000.0, "drawdown_after_peak_pct": -34.39, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_material_spread_peak_if_spread_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_contract_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_steel_lithium_resource_theme_local4b", "current_profile_verdict": "C15 should not treat steel/lithium/resource beta as durable Stage2 unless steel spread, lithium resource economics, inventory, volume, pricing and margin bridge refreshes. POSCO Holdings had a tradable bounce but then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C15_MATERIAL_SPREAD_005490_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE", "case_id": "R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE", "symbol": "004020", "company_name": "현대제철", "round": "R4", "loop": "80", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|material_spread_supercycle_guardrail", "trigger_type": "Stage2-FalsePositive / SteelSpreadMarginFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 33200.0, "evidence_available_at_that_date": "STEEL_HRC_REBAR_AUTO_STEEL_SPREAD_VOLUME_UTILIZATION_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_STEEL_2024_STEEL_SPREAD_VOLUME_UTILIZATION_PRICE_PASS_THROUGH_MARGIN_BRIDGE", "stage2_evidence_fields": ["commodity_spread_candidate", "volume_inventory_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "price_pass_through_or_TC_RC_candidate"], "stage4b_evidence_fields": ["material_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004020/2024.csv", "profile_path": "atlas/symbol_profiles/004/004020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 12.95, "MFE_90D_pct": 12.95, "MFE_180D_pct": 12.95, "MAE_30D_pct": -0.15, "MAE_90D_pct": -4.82, "MAE_180D_pct": -28.46, "peak_date": "2024-02-13", "peak_price": 37500.0, "drawdown_after_peak_pct": -36.67, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_material_spread_peak_if_spread_inventory_utilization_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_inventory_impairment_contract_loss_margin_or_financing_break", "trigger_outcome_label": "counterexample_steel_spread_margin_local4b", "current_profile_verdict": "C15 should not treat steel spread beta as durable Stage2 unless HRC/rebar/auto steel volume, utilization, raw-material spread, price pass-through and margin bridge are visible. Hyundai Steel produced modest MFE and then a high-MAE downtrend.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_event_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C15_MATERIAL_SPREAD_004020_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE", "trigger_id": "TRG_R4L80-C15-010130-KOREA-ZINC-NONFERROUS-SPREAD-EVENT-LIFECYCLE", "symbol": "010130", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 14, "inventory_utilization_score": 13, "price_pass_through_score": 12, "margin_bridge_score": 13, "relative_strength_score": 15, "event_separation_risk": 10, "sharecount_validation_risk": 8, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair and event separation", "raw_component_scores_after": {"commodity_spread_score": 16, "inventory_utilization_score": 15, "price_pass_through_score": 14, "margin_bridge_score": 15, "relative_strength_score": 14, "event_separation_risk": 12, "sharecount_validation_risk": 10, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["commodity_spread_score", "inventory_utilization_score", "price_pass_through_score", "margin_bridge_score", "event_separation_risk", "execution_risk_score"], "component_delta_explanation": "Reward only verified material spread, inventory/utilization, price pass-through and margin bridge; cap resource/steel theme beta or event-driven MFE when bridge proof is missing or event separation is unvalidated.", "MFE_90D_pct": 16.79, "MAE_90D_pct": -6.95, "score_return_alignment_label": "material_spread_positive_with_event_separation", "current_profile_verdict": "C15 should allow nonferrous smelter positives only when zinc/copper/precious-metal spread, TC/RC, inventory, utilization and margin bridge are visible. Korea Zinc produced enormous MFE, but a late governance/tender-event component must be separated from commodity-spread economics before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE", "trigger_id": "TRG_R4L80-C15-005490-POSCO-HOLDINGS-STEEL-LITHIUM-SPREAD-FADE", "symbol": "005490", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 5, "inventory_utilization_score": 3, "price_pass_through_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "event_separation_risk": 0, "sharecount_validation_risk": 8, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 3, "inventory_utilization_score": 1, "price_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "event_separation_risk": 0, "sharecount_validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_utilization_score", "price_pass_through_score", "margin_bridge_score", "event_separation_risk", "execution_risk_score"], "component_delta_explanation": "Reward only verified material spread, inventory/utilization, price pass-through and margin bridge; cap resource/steel theme beta or event-driven MFE when bridge proof is missing or event separation is unvalidated.", "MFE_90D_pct": 11.48, "MAE_90D_pct": -9.94, "score_return_alignment_label": "false_positive_material_spread_bridge_gap", "current_profile_verdict": "C15 should not treat steel/lithium/resource beta as durable Stage2 unless steel spread, lithium resource economics, inventory, volume, pricing and margin bridge refreshes. POSCO Holdings had a tradable bounce but then opened a high-MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE", "trigger_id": "TRG_R4L80-C15-004020-HYUNDAI-STEEL-SPREAD-MARGIN-FADE", "symbol": "004020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"commodity_spread_score": 5, "inventory_utilization_score": 3, "price_pass_through_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "event_separation_risk": 0, "sharecount_validation_risk": 0, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 45, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"commodity_spread_score": 3, "inventory_utilization_score": 1, "price_pass_through_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "event_separation_risk": 0, "sharecount_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["commodity_spread_score", "inventory_utilization_score", "price_pass_through_score", "margin_bridge_score", "event_separation_risk", "execution_risk_score"], "component_delta_explanation": "Reward only verified material spread, inventory/utilization, price pass-through and margin bridge; cap resource/steel theme beta or event-driven MFE when bridge proof is missing or event separation is unvalidated.", "MFE_90D_pct": 12.95, "MAE_90D_pct": -4.82, "score_return_alignment_label": "false_positive_material_spread_bridge_gap", "current_profile_verdict": "C15 should not treat steel spread beta as durable Stage2 unless HRC/rebar/auto steel volume, utilization, raw-material spread, price pass-through and margin bridge are visible. Hyundai Steel produced modest MFE and then a high-MAE downtrend."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 80, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NONFERROUS_STEEL_RESOURCE_SPREAD_SUPERCYCLE_BRIDGE_VS_STEEL_LITHIUM_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 2, "event_separation_required_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C15 nonferrous/steel/material-spread symbols outside top-covered 006260/011170/103140/006650/011780 set, +3 nonferrous-smelter/steel-lithium/steel-spread trigger families, +1 event-separated nonferrous MFE candidate, +2 steel/resource spread local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_event_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 80, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "axis": "nonferrous_steel_resource_spread_supercycle_bridge_vs_steel_lithium_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C15 should split verified nonferrous/steel spread margin rerating from generic resource/steel/lithium theme beta and event-driven MFE. Stage2 requires commodity spread, inventory, utilization, price pass-through and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Event-driven nonferrous rows require separation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["010130", "005490", "004020"], "event_separation_required": ["010130"], "share_count_validation_required": ["010130", "005490"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 80, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "event_separation_guard", "share_count_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C15 needs commodity spread, inventory, utilization, price pass-through and margin proof. Korea Zinc shows a large nonferrous MFE candidate that needs governance/event separation; POSCO Holdings and Hyundai Steel show resource/steel spread beta fading into local 4B when spread and margin bridge are absent or stale."}
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
010130:
  name = 고려아연
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required
  event_separation_required = true

005490:
  name = POSCO홀딩스 from 2022-03-17, POSCO before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

004020:
  name = 현대제철 from 2006-03-17, INI스틸 / 인천제철 before that
  corporate_action_candidate_dates = 1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C15 rows are source_proxy_only / evidence_url_pending.
010130 needs governance/event separation and share-count validation.
005490 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C15 rule-shape discovery,
but coding-agent promotion requires non-proxy metal/steel spread, inventory, utilization, price pass-through, TC/RC or raw-material spread and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C15 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 010130 needs event separation, and 010130/005490 need share-count validation.

Candidate axis:
nonferrous_steel_resource_spread_supercycle_bridge_vs_steel_lithium_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 010130, 005490 and 004020.
4. Validate 010130 event/governance separation from commodity-spread evidence.
5. Validate 010130 and 005490 share-count changes inside the selected window.
6. Keep generic C15 material-spread weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - commodity spread or price-cost spread is explicit,
   - inventory, utilization or volume improvement is visible,
   - price pass-through, TC/RC or raw-material spread bridge exists,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is resource/steel/material theme beta only,
   - spread/inventory/utilization/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price spread collapse, inventory impairment, contract loss, financing or margin break.
10. Emit before/after diagnostics and reject if verified material-spread positives or event-separated rows are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 80
next_round = R5
next_loop = 80
round_schedule_status = valid
round_sector_consistency = pass
```

