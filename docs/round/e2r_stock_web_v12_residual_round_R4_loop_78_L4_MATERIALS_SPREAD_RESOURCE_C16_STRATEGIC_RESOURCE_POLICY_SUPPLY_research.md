# E2R Stock-Web v12 Residual Research — R4 Loop 78 / L4 / C16

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 78,
  "computed_next_round": "R5",
  "computed_next_loop": 78,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY",
  "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "strategic_resource_policy_supply_guardrail",
    "oil_supply_security_vs_rareearth_theme_beta",
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

Previous completed state in this interactive run: R3 / loop 78.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 78
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
computed_next_round = R5
computed_next_loop = 78
```

R4 was routed to C16 because loop 77 used C15 and C17 remains heavily covered.  
This file tests strategic-resource supply/security bridge behavior rather than generic commodity spread.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C16 is concentrated in:

```text
005290, 027580, 047400, 093370
```

This run uses three different symbols:

```text
004090 / 한국석유 / oil supply-security inventory/margin bridge
000910 / 유니온 / rare-earth resource theme fade
075970 / 동국알앤에스 / rare-earth refractory theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C16 is not “자원 테마가 올랐다.”

The mechanism must pass through:

```text
strategic resource / supply-security shock
→ direct beneficiary mapping
→ order, inventory, demand or volume bridge
→ pricing and margin conversion
→ durable rerating
```

자원 안보 headline은 지도 위의 붉은 표시다.  
C16이 보려는 것은 그 표시가 실제 재고, 가격, 물량, 마진으로 흘러드는 파이프라인이다.

---

## Case 1 — Resource-security lifecycle candidate: 004090 / 한국석유

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is oil supply shock, product pricing, inventory, demand and margin bridge evidence.

```text
evidence_family = OIL_SUPPLY_SECURITY_GEOPOLITICAL_PRICE_INVENTORY_REVENUE_MARGIN_BRIDGE
case_role = resource_security_positive_with_later_4b_watch
trigger_date = 2024-04-01
entry_date = 2024-04-02
entry_price = 12,810
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv`:

```text
2024-04-02,12810,15710,12650,15310
2024-04-16,20450,22400,19840,20200
2024-04-19,17220,22350,16890,21000
2024-06-04,21650,23300,21500,23300
2024-06-05,23650,28100,21600,23300
2024-08-05,23900,24950,20150,22600
2024-10-30,15820,15970,15700,15820
```

### Backtest

```text
MFE_30D  = +74.86%
MAE_30D  = -1.25%
MFE_90D  = +119.36%
MAE_90D  = -1.25%
MFE_180D = +119.36%
MAE_180D = -1.25%
peak_180 = 28,100 on 2024-06-05
trough_180 = 12,650 on 2024-04-02
peak_to_later_drawdown = -44.13%
```

### Interpretation

This is a C16 resource-security lifecycle candidate.  
The MFE was large and entry-basis MAE was controlled.

Correct treatment:

```text
verified supply-security / inventory / pricing / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 000910 / 유니온

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests rare-earth/resource-security theme beta without enough direct supply and margin bridge.

```text
evidence_family = RAREEARTH_RESOURCE_SECURITY_THEME_WITH_WEAK_DIRECT_SUPPLY_MARGIN_BRIDGE
case_role = counterexample_rareearth_policy_theme_local4b
trigger_date = 2024-01-09
entry_date = 2024-01-10
entry_price = 6,290
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv`:

```text
2024-01-10,6290,6580,5820,5840
2024-01-15,6190,6480,6030,6300
2024-02-01,5400,5490,5370,5420
2024-05-14,5700,5930,5600,5920
2024-08-05,4705,4750,3360,4100
2024-09-09,3820,4020,3795,4020
```

### Backtest

```text
MFE_30D  = +4.61%
MAE_30D  = -14.63%
MFE_90D  = +4.61%
MAE_90D  = -18.60%
MFE_180D = +4.61%
MAE_180D = -46.58%
peak_180 = 6,580 on 2024-01-10
trough_180 = 3,360 on 2024-08-05
peak_to_later_drawdown = -48.94%
```

### Interpretation

This is a C16 false-positive row.  
The resource-security headline did not become durable direct supply economics.

Correct treatment:

```text
rare-earth / resource-security theme beta
→ no verified supply/order/pricing/margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 075970 / 동국알앤에스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests rare-earth / refractory-material theme beta without enough order, volume and margin bridge.

```text
evidence_family = RAREEARTH_REFRACTORY_RESOURCE_SECURITY_THEME_WITH_WEAK_ORDER_VOLUME_MARGIN_BRIDGE
case_role = counterexample_rareearth_refractory_theme_local4b
trigger_date = 2024-01-15
entry_date = 2024-01-16
entry_price = 3,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/075/075970/2024.csv`:

```text
2024-01-16,3750,4060,3705,3780
2024-01-23,3600,4080,3600,3605
2024-02-27,3600,3620,3560,3565
2024-04-11,3205,3265,3135,3170
2024-08-05,2800,2885,2520,2555
2024-09-09,2285,2410,2285,2400
```

### Backtest

```text
MFE_30D  = +8.80%
MAE_30D  = -5.07%
MFE_90D  = +8.80%
MAE_90D  = -16.40%
MFE_180D = +8.80%
MAE_180D = -39.07%
peak_180 = 4,080 on 2024-01-23
trough_180 = 2,285 on 2024-09-09
peak_to_later_drawdown = -44.00%
```

### Interpretation

This is another resource-theme local 4B row.  
The first spike did not validate direct supply or order economics.

Correct treatment:

```text
rare-earth/refractory theme beta
→ no order / volume / margin bridge
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
do_not_raise_generic_C16_resource_theme_weight = true
do_not_treat_all_resource_security_MFE_as_Green = true
do_not_convert_resource_theme_drawdown_to_hard_4C_without_non_price_supply_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE
```

This fine archetype covers:

```text
1. oil supply-security / inventory / pricing bridge → Stage2 possible after source repair
2. rare-earth theme without direct supply economics → false Stage2 / local 4B
3. rare-earth refractory theme without order/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE", "symbol": "004090", "company_name": "한국석유", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "resource_security_positive", "best_trigger": "Stage2-ResourceSecurityLifecycle-OilSupplyInventoryMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 can allow oil/resource-security rows when geopolitical supply shock maps to product pricing, inventory, demand and margin bridge. Korea Petroleum produced a very large MFE with controlled entry-basis MAE, but later post-peak drawdown requires lifecycle local 4B if supply/inventory/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, direct beneficiary mapping, demand/order volume, pricing/inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RareEarthResourceThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat rare-earth/resource-security theme beta as durable Stage2 unless direct supply exposure, customer demand, pricing, inventory and margin bridge are visible. Union had a small early MFE and then opened a deep MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, direct beneficiary mapping, demand/order volume, pricing/inventory and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE", "symbol": "075970", "company_name": "동국알앤에스", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "case_type": "strategic_resource_policy_supply", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / RareEarthRefractoryThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C16 should not treat rare-earth/refractory theme spikes as durable Stage2 unless policy shock maps to direct order, volume, pricing and margin bridge. Dongkuk R&S produced only modest MFE and then a persistent drawdown, making it local 4B-watch rather than durable Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy resource supply, direct beneficiary mapping, demand/order volume, pricing/inventory and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE", "case_id": "R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE", "symbol": "004090", "company_name": "한국석유", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-ResourceSecurityLifecycle-OilSupplyInventoryMarginBridgeWithLifecycle4B", "trigger_date": "2024-04-01", "entry_date": "2024-04-02", "entry_price": 12810.0, "evidence_available_at_that_date": "OIL_SUPPLY_SECURITY_GEOPOLITICAL_PRICE_INVENTORY_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KOREA_PETROLEUM_2024_OIL_SUPPLY_SECURITY_INVENTORY_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["resource_security_or_supply_shock_candidate", "direct_supply_order_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_demand_or_volume_bridge_candidate"], "stage4b_evidence_fields": ["resource_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004090/2024.csv", "profile_path": "atlas/symbol_profiles/004/004090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 74.86, "MFE_90D_pct": 119.36, "MFE_180D_pct": 119.36, "MAE_30D_pct": -1.25, "MAE_90D_pct": -1.25, "MAE_180D_pct": -1.25, "peak_date": "2024-06-05", "peak_price": 28100.0, "drawdown_after_peak_pct": -44.13, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_security_peak_if_supply_order_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_supply_contract_loss_policy_reversal_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "resource_security_positive_with_later_4b_watch", "current_profile_verdict": "C16 can allow oil/resource-security rows when geopolitical supply shock maps to product pricing, inventory, demand and margin bridge. Korea Petroleum produced a very large MFE with controlled entry-basis MAE, but later post-peak drawdown requires lifecycle local 4B if supply/inventory/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_RESOURCE_POLICY_004090_2024-04-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE", "case_id": "R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE", "symbol": "000910", "company_name": "유니온", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / RareEarthResourceThemeFade", "trigger_date": "2024-01-09", "entry_date": "2024-01-10", "entry_price": 6290.0, "evidence_available_at_that_date": "RAREEARTH_RESOURCE_SECURITY_THEME_WITH_WEAK_DIRECT_SUPPLY_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:UNION_2024_RAREEARTH_RESOURCE_SECURITY_DIRECT_SUPPLY_DEMAND_MARGIN_BRIDGE", "stage2_evidence_fields": ["resource_security_or_supply_shock_candidate", "direct_supply_order_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_demand_or_volume_bridge_candidate"], "stage4b_evidence_fields": ["resource_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000910/2024.csv", "profile_path": "atlas/symbol_profiles/000/000910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.61, "MFE_90D_pct": 4.61, "MFE_180D_pct": 4.61, "MAE_30D_pct": -14.63, "MAE_90D_pct": -18.6, "MAE_180D_pct": -46.58, "peak_date": "2024-01-10", "peak_price": 6580.0, "drawdown_after_peak_pct": -48.94, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_security_peak_if_supply_order_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_supply_contract_loss_policy_reversal_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "counterexample_rareearth_policy_theme_local4b", "current_profile_verdict": "C16 should not treat rare-earth/resource-security theme beta as durable Stage2 unless direct supply exposure, customer demand, pricing, inventory and margin bridge are visible. Union had a small early MFE and then opened a deep MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_RESOURCE_POLICY_000910_2024-01-10", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE", "case_id": "R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE", "symbol": "075970", "company_name": "동국알앤에스", "round": "R4", "loop": "78", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|strategic_resource_policy_supply_guardrail", "trigger_type": "Stage2-FalsePositive / RareEarthRefractoryThemeFade", "trigger_date": "2024-01-15", "entry_date": "2024-01-16", "entry_price": 3750.0, "evidence_available_at_that_date": "RAREEARTH_REFRACTORY_RESOURCE_SECURITY_THEME_WITH_WEAK_ORDER_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:DONGKUK_RNS_2024_RAREEARTH_REFRACTORY_RESOURCE_POLICY_ORDER_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["resource_security_or_supply_shock_candidate", "direct_supply_order_or_inventory_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "pricing_demand_or_volume_bridge_candidate"], "stage4b_evidence_fields": ["resource_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/075/075970/2024.csv", "profile_path": "atlas/symbol_profiles/075/075970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.8, "MFE_90D_pct": 8.8, "MFE_180D_pct": 8.8, "MAE_30D_pct": -5.07, "MAE_90D_pct": -16.4, "MAE_180D_pct": -39.07, "peak_date": "2024-01-23", "peak_price": 4080.0, "drawdown_after_peak_pct": -44.0, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_resource_security_peak_if_supply_order_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_supply_contract_loss_policy_reversal_inventory_impairment_margin_or_financing_break", "trigger_outcome_label": "counterexample_rareearth_refractory_theme_local4b", "current_profile_verdict": "C16 should not treat rare-earth/refractory theme spikes as durable Stage2 unless policy shock maps to direct order, volume, pricing and margin bridge. Dongkuk R&S produced only modest MFE and then a persistent drawdown, making it local 4B-watch rather than durable Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C16_RESOURCE_POLICY_075970_2024-01-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE", "trigger_id": "TRG_R4L78-C16-004090-KOREA-PETROLEUM-OIL-SUPPLY-SECURITY-LIFECYCLE", "symbol": "004090", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"resource_security_score": 14, "direct_supply_mapping_score": 12, "order_or_inventory_score": 12, "pricing_volume_score": 13, "margin_bridge_score": 12, "relative_strength_score": 15, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_before": 80, "stage_label_before": "Resource-security lifecycle candidate after source repair", "raw_component_scores_after": {"resource_security_score": 12, "direct_supply_mapping_score": 15, "order_or_inventory_score": 15, "pricing_volume_score": 15, "margin_bridge_score": 14, "relative_strength_score": 14, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_after": 86, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["resource_security_score", "direct_supply_mapping_score", "order_or_inventory_score", "pricing_volume_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified resource-security direct beneficiary mapping, order/inventory, pricing/volume and margin bridge; cap strategic-resource theme beta when evidence fails to refresh.", "MFE_90D_pct": 119.36, "MAE_90D_pct": -1.25, "score_return_alignment_label": "resource_security_positive_with_lifecycle_4b", "current_profile_verdict": "C16 can allow oil/resource-security rows when geopolitical supply shock maps to product pricing, inventory, demand and margin bridge. Korea Petroleum produced a very large MFE with controlled entry-basis MAE, but later post-peak drawdown requires lifecycle local 4B if supply/inventory/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE", "trigger_id": "TRG_R4L78-C16-000910-UNION-RAREEARTH-RESOURCE-THEME-FADE", "symbol": "000910", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"resource_security_score": 7, "direct_supply_mapping_score": 3, "order_or_inventory_score": 2, "pricing_volume_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"resource_security_score": 4, "direct_supply_mapping_score": 2, "order_or_inventory_score": 1, "pricing_volume_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["resource_security_score", "direct_supply_mapping_score", "order_or_inventory_score", "pricing_volume_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified resource-security direct beneficiary mapping, order/inventory, pricing/volume and margin bridge; cap strategic-resource theme beta when evidence fails to refresh.", "MFE_90D_pct": 4.61, "MAE_90D_pct": -18.6, "score_return_alignment_label": "false_positive_resource_theme_bridge_gap", "current_profile_verdict": "C16 should not treat rare-earth/resource-security theme beta as durable Stage2 unless direct supply exposure, customer demand, pricing, inventory and margin bridge are visible. Union had a small early MFE and then opened a deep MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE", "trigger_id": "TRG_R4L78-C16-075970-DONGKUK-RNS-RAREEARTH-REFRACTORY-THEME-FADE", "symbol": "075970", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "raw_component_scores_before": {"resource_security_score": 7, "direct_supply_mapping_score": 3, "order_or_inventory_score": 2, "pricing_volume_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 46, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"resource_security_score": 4, "direct_supply_mapping_score": 2, "order_or_inventory_score": 1, "pricing_volume_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["resource_security_score", "direct_supply_mapping_score", "order_or_inventory_score", "pricing_volume_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified resource-security direct beneficiary mapping, order/inventory, pricing/volume and margin bridge; cap strategic-resource theme beta when evidence fails to refresh.", "MFE_90D_pct": 8.8, "MAE_90D_pct": -16.4, "score_return_alignment_label": "false_positive_resource_theme_bridge_gap", "current_profile_verdict": "C16 should not treat rare-earth/refractory theme spikes as durable Stage2 unless policy shock maps to direct order, volume, pricing and margin bridge. Dongkuk R&S produced only modest MFE and then a persistent drawdown, making it local 4B-watch rather than durable Green."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 78, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "fine_archetype_id": "OIL_RAREEARTH_RESOURCE_SECURITY_SUPPLY_BRIDGE_VS_RESOURCE_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 2, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C16 strategic-resource symbols outside top-covered 005290/027580/047400/093370 set, +2 oil/rare-earth resource-security trigger families, +1 oil supply lifecycle MFE candidate, +2 rare-earth theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 78, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "axis": "oil_rareearth_resource_security_supply_bridge_vs_resource_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C16 should split verified strategic-resource supply/security rerating from generic rare-earth/resource theme beta. Stage2 requires explicit resource-security event plus direct beneficiary mapping, order/inventory or demand bridge, pricing/volume bridge and margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["004090", "000910", "075970"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 78, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C16_STRATEGIC_RESOURCE_POLICY_SUPPLY", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C16 needs direct resource-supply economics proof. Korea Petroleum shows an oil supply-security lifecycle MFE candidate after source repair; Union and Dongkuk R&S show rare-earth/resource-policy theme beta fading into local 4B when direct order, pricing and margin bridge are absent."}
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
004090:
  name = 한국석유
  corporate_action_candidate_dates = 1997-08-07, 2021-04-15, 2021-05-07
  selected window = 2024-04-02~D+180
  contamination = false

000910:
  name = 유니온
  corporate_action_candidate_dates = 1997-01-03, 2008-05-07
  selected window = 2024-01-10~D+180
  contamination = false

075970:
  name = 동국알앤에스 from 2008-01-10
  corporate_action_candidate_dates = 2006-06-02, 2006-06-13, 2008-06-10
  selected window = 2024-01-16~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C16 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C16 rule-shape discovery,
but coding-agent promotion requires non-proxy resource-security event, direct beneficiary mapping, order/inventory/demand, pricing/volume and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R4/C16 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
oil_rareearth_resource_security_supply_bridge_vs_resource_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 004090, 000910 and 075970.
4. Keep generic C16 strategic-resource weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - strategic resource / supply-security event is explicit,
   - direct beneficiary mapping is visible,
   - order, inventory, demand or volume bridge exists,
   - pricing and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is resource-security or rare-earth theme beta only,
   - direct supply/order/pricing/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price supply contract loss, policy reversal, inventory impairment, pricing collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified resource-security direct-beneficiary positives are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 78
next_round = R5
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

