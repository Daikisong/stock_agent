# E2R Stock-Web v12 Residual Research — R9 Loop 81 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 81,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 81,
  "computed_next_round": "R10",
  "computed_next_loop": 81,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_transport_volume_margin_guardrail",
    "airline_LCC_passenger_yield_fuel_cost_margin_bridge",
    "transport_theme_event_margin_fade_boundary",
    "share_count_validation_queue_creation",
    "extended_status_validation_queue_creation",
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

Previous completed state in this interactive run: R8 / loop 81.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 81
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 81
```

R9 was routed to C29 mobility/transport rather than construction/PF because the selected cases are airline / passenger transport volume-margin paths.  
This file deliberately avoids loop-80 auto-supplier names and uses an airline/transport sub-axis.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 concentration in:

```text
000270, 204320, 011210, 005380, 003490
```

This run uses three different transport symbols:

```text
091810 / 티웨이항공 / LCC route expansion, passenger yield and fuel-cost margin bridge
089590 / 제주항공 / LCC passenger recovery theme fade
020560 / 아시아나항공 / airline merger/transport margin theme fade with extended-status validation
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
091810 shows share-count changes inside the selected 2024 shard and requires validation.
020560 has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion must validate status/continuity.
```

## Research thesis

C29 is not “여객 수요가 회복됐다.”

The mechanism must pass through:

```text
mobility / airline / passenger-demand headline
→ passenger volume and load factor
→ yield, ancillary revenue or route quality
→ fuel-cost and labor / maintenance cost sensitivity
→ revenue conversion and operating margin bridge
→ durable rerating
```

항공주는 좌석이 아니라 빈 좌석이 줄어드는 속도와 그 좌석이 남기는 마진의 함수다.  
C29가 보려는 것은 여객 회복 headline이 실제 탑승률, 운임, 연료비, 정비비, 영업레버리지로 착륙하는지다.

---

## Case 1 — Volatile LCC lifecycle candidate: 091810 / 티웨이항공

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is LCC route expansion, passenger volume, load factor, yield, fuel-cost sensitivity, revenue conversion and margin bridge evidence.

```text
evidence_family = LCC_ROUTE_EXPANSION_PASSENGER_LOAD_FACTOR_YIELD_FUEL_COST_SHARECOUNT_MARGIN_BRIDGE
case_role = positive_airline_LCC_route_yield_lifecycle_with_sharecount_validation_and_high_MAE_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 3,155
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv`:

```text
2024-02-01,3155,3230,3015,3070
2024-02-14,3145,3180,2955,3020
2024-03-14,2755,2800,2675,2690
2024-03-19,2700,2700,2580,2605
2024-08-05,2580,2590,2305,2430
2024-09-20,2985,3300,2950,3295
2024-10-10,3680,3990,3320,3770
2024-10-22,2905,2965,2735,2910
2024-10-25,3105,3730,3045,3325
```

### Backtest

```text
MFE_30D  = +2.38%
MAE_30D  = -18.23%
MFE_90D  = +2.38%
MAE_90D  = -19.02%
MFE_180D = +26.47%
MAE_180D = -26.94%
peak_180 = 3,990 on 2024-10-10
trough_180 = 2,305 on 2024-08-05
peak_to_later_drawdown = -31.45%
```

### Interpretation

This is a volatile C29 lifecycle candidate, not a clean Green.  
The late MFE shows tradable transport beta, but the path first opened a deep MAE and share-count validation is required.

Correct treatment:

```text
verified route expansion / passenger volume / yield / fuel-cost / margin bridge → Stage2-Yellow possible
share-count validation first
bridge stale or absent → local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 089590 / 제주항공

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests LCC passenger recovery beta without enough yield, load factor, fuel-cost and operating-margin bridge.

```text
evidence_family = LCC_PASSENGER_RECOVERY_YIELD_FUEL_COST_MARGIN_THEME_WITH_WEAK_OPERATING_LEVERAGE_BRIDGE
case_role = counterexample_LCC_passenger_yield_margin_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 12,540
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv`:

```text
2024-02-01,12540,12760,12310,12510
2024-02-08,11740,11860,11520,11620
2024-03-04,11130,11140,10580,10690
2024-04-16,10700,10790,10430,10550
2024-06-27,10410,10470,10270,10300
2024-08-05,9460,9460,8300,8770
2024-09-04,8970,9000,8810,8850
2024-10-30,9190,9610,9150,9560
```

### Backtest

```text
MFE_30D  = +1.75%
MAE_30D  = -15.63%
MFE_90D  = +1.75%
MAE_90D  = -18.10%
MFE_180D = +1.75%
MAE_180D = -33.81%
peak_180 = 12,760 on 2024-02-01
trough_180 = 8,300 on 2024-08-05
peak_to_later_drawdown = -34.95%
```

### Interpretation

This is a C29 LCC passenger recovery false-positive boundary.  
There was almost no forward MFE after entry and the drawdown widened into local-4B territory.

Correct treatment:

```text
LCC passenger recovery theme beta
→ no verified passenger volume / yield / fuel-cost / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 020560 / 아시아나항공

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
extended_status_validation_required = true
source_repair_required = true
```

This row tests airline merger/transport beta without enough volume, yield, integration and margin bridge.

```text
evidence_family = AIRLINE_MERGER_TRANSPORT_PASSENGER_VOLUME_YIELD_FUEL_COST_MARGIN_THEME_WITH_WEAK_OPERATING_LEVERAGE_BRIDGE
case_role = counterexample_airline_transport_margin_local4b_with_extended_status_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 13,280
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/020/020560/2024.csv`:

```text
2024-02-01,13280,13870,12130,12130
2024-02-08,13220,13510,13150,13510
2024-02-13,13590,14480,13320,14270
2024-02-14,14600,14610,12980,13020
2024-03-19,10970,10970,10650,10680
2024-07-24,10170,10240,10160,10160
2024-08-05,9710,9730,8780,8950
2024-09-11,9370,9480,9190,9210
2024-10-31,9970,10090,9820,10090
```

### Backtest

```text
MFE_30D  = +10.02%
MAE_30D  = -17.39%
MFE_90D  = +10.02%
MAE_90D  = -19.35%
MFE_180D = +10.02%
MAE_180D = -33.89%
peak_180 = 14,610 on 2024-02-14
trough_180 = 8,780 on 2024-08-05
peak_to_later_drawdown = -39.90%
```

### Interpretation

This is an airline transport / merger-beta local-4B boundary.  
The early MFE did not become durable passenger volume or margin operating leverage.

Correct treatment:

```text
airline merger / transport recovery beta
→ no verified passenger volume / integration / yield / margin bridge
→ local 4B-watch
→ extended-window ingestion must validate the 2024-12-30 profile corporate-action candidate
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
mobility_transport_volume_margin_bridge_required = strengthen
airline_yield_fuel_cost_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
share_count_validation_guard = strengthen
extended_status_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C29_airline_transport_weight = true
do_not_treat_all_airline_passenger_recovery_MFE_as_Green = true
do_not_ingest_sharecount_changed_or_status_sensitive_rows_without_validation = true
do_not_convert_airline_transport_drawdown_to_hard_4C_without_non_price_route_demand_margin_or_financing_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE
```

This fine archetype covers:

```text
1. LCC route expansion / yield bridge with validation → Stage2-Yellow possible after source repair
2. LCC passenger recovery beta without margin bridge → false Stage2 / local 4B
3. airline merger/transport recovery beta without integration/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE", "symbol": "091810", "company_name": "티웨이항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-LCCRouteExpansionYieldFuelCostMarginBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 can allow airline/LCC positives only when passenger volume, route expansion, load factor, yield, fuel-cost sensitivity and margin bridge are visible. T'way produced later MFE but had large interim MAE and stock-web share-count changes, so source repair and share-count validation are mandatory.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy passenger volume, load factor, yield, fuel-cost sensitivity, route/integration status, revenue conversion and operating margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE", "symbol": "089590", "company_name": "제주항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LCCPassengerYieldFuelCostMarginBridgeFadeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat LCC passenger recovery beta as durable Stage2 unless passenger volume, load factor, yield, fuel cost and operating margin bridge are visible. Jeju Air had almost no forward MFE after entry and then a persistent high-MAE path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy passenger volume, load factor, yield, fuel-cost sensitivity, route/integration status, revenue conversion and operating margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE", "symbol": "020560", "company_name": "아시아나항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AirlineMergerTransportVolumeMarginBridgeFadeWithExtendedStatusValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat airline merger/transport beta as durable volume-margin operating leverage unless passenger volume, yield, fuel-cost pass-through, integration path, revenue and margin bridge are visible. Asiana had early MFE, then a persistent high-MAE drawdown. The profile has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion needs validation.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy passenger volume, load factor, yield, fuel-cost sensitivity, route/integration status, revenue conversion and operating margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE", "case_id": "R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE", "symbol": "091810", "company_name": "티웨이항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_transport_volume_margin_guardrail", "trigger_type": "Stage2-Lifecycle-LCCRouteExpansionYieldFuelCostMarginBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 3155.0, "evidence_available_at_that_date": "LCC_ROUTE_EXPANSION_PASSENGER_LOAD_FACTOR_YIELD_FUEL_COST_SHARECOUNT_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:TWAY_AIR_2024_LCC_ROUTE_EXPANSION_PASSENGER_VOLUME_YIELD_FUEL_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["passenger_volume_or_route_candidate", "yield_load_factor_or_fuel_cost_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_integration_candidate"], "stage4b_evidence_fields": ["airline_transport_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/091/091810/2024.csv", "profile_path": "atlas/symbol_profiles/091/091810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.38, "MFE_90D_pct": 2.38, "MFE_180D_pct": 26.47, "MAE_30D_pct": -18.23, "MAE_90D_pct": -19.02, "MAE_180D_pct": -26.94, "peak_date": "2024-10-10", "peak_price": 3990.0, "drawdown_after_peak_pct": -31.45, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_airline_transport_peak_if_passenger_volume_yield_fuel_cost_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_route_loss_demand_break_fuel_cost_margin_financing_or_safety_regulatory_break", "trigger_outcome_label": "positive_airline_LCC_route_yield_lifecycle_with_sharecount_validation_and_high_MAE_watch", "current_profile_verdict": "C29 can allow airline/LCC positives only when passenger volume, route expansion, load factor, yield, fuel-cost sensitivity and margin bridge are visible. T'way produced later MFE but had large interim MAE and stock-web share-count changes, so source repair and share-count validation are mandatory.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C29_AIRLINE_TRANSPORT_MARGIN_091810_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE", "case_id": "R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE", "symbol": "089590", "company_name": "제주항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_transport_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / LCCPassengerYieldFuelCostMarginBridgeFadeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 12540.0, "evidence_available_at_that_date": "LCC_PASSENGER_RECOVERY_YIELD_FUEL_COST_MARGIN_THEME_WITH_WEAK_OPERATING_LEVERAGE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:JEJU_AIR_2024_LCC_PASSENGER_VOLUME_LOAD_FACTOR_YIELD_FUEL_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["passenger_volume_or_route_candidate", "yield_load_factor_or_fuel_cost_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_integration_candidate"], "stage4b_evidence_fields": ["airline_transport_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv", "profile_path": "atlas/symbol_profiles/089/089590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.75, "MFE_90D_pct": 1.75, "MFE_180D_pct": 1.75, "MAE_30D_pct": -15.63, "MAE_90D_pct": -18.1, "MAE_180D_pct": -33.81, "peak_date": "2024-02-01", "peak_price": 12760.0, "drawdown_after_peak_pct": -34.95, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_airline_transport_peak_if_passenger_volume_yield_fuel_cost_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_route_loss_demand_break_fuel_cost_margin_financing_or_safety_regulatory_break", "trigger_outcome_label": "counterexample_LCC_passenger_yield_margin_local4b", "current_profile_verdict": "C29 should not treat LCC passenger recovery beta as durable Stage2 unless passenger volume, load factor, yield, fuel cost and operating margin bridge are visible. Jeju Air had almost no forward MFE after entry and then a persistent high-MAE path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C29_AIRLINE_TRANSPORT_MARGIN_089590_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE", "case_id": "R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE", "symbol": "020560", "company_name": "아시아나항공", "round": "R9", "loop": "81", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_transport_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / AirlineMergerTransportVolumeMarginBridgeFadeWithExtendedStatusValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 13280.0, "evidence_available_at_that_date": "AIRLINE_MERGER_TRANSPORT_PASSENGER_VOLUME_YIELD_FUEL_COST_MARGIN_THEME_WITH_WEAK_OPERATING_LEVERAGE_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:ASIANA_AIRLINES_2024_PASSENGER_VOLUME_YIELD_FUEL_COST_INTEGRATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["passenger_volume_or_route_candidate", "yield_load_factor_or_fuel_cost_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "operating_leverage_or_integration_candidate"], "stage4b_evidence_fields": ["airline_transport_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020560/2024.csv", "profile_path": "atlas/symbol_profiles/020/020560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.02, "MFE_90D_pct": 10.02, "MFE_180D_pct": 10.02, "MAE_30D_pct": -17.39, "MAE_90D_pct": -19.35, "MAE_180D_pct": -33.89, "peak_date": "2024-02-14", "peak_price": 14610.0, "drawdown_after_peak_pct": -39.9, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_airline_transport_peak_if_passenger_volume_yield_fuel_cost_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_route_loss_demand_break_fuel_cost_margin_financing_or_safety_regulatory_break", "trigger_outcome_label": "counterexample_airline_transport_margin_local4b_with_extended_status_validation", "current_profile_verdict": "C29 should not treat airline merger/transport beta as durable volume-margin operating leverage unless passenger volume, yield, fuel-cost pass-through, integration path, revenue and margin bridge are visible. Asiana had early MFE, then a persistent high-MAE drawdown. The profile has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion needs validation.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_status_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C29_AIRLINE_TRANSPORT_MARGIN_020560_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE", "trigger_id": "TRG_R9L81-C29-091810-TWAY-LCC-ROUTE-YIELD-SHARECOUNT-LIFECYCLE", "symbol": "091810", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"passenger_volume_score": 13, "route_or_integration_visibility_score": 12, "load_factor_yield_score": 13, "fuel_cost_sensitivity_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 8, "sharecount_or_status_validation_risk": 10, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_before": 70, "stage_label_before": "Stage2/Yellow candidate after source repair and validation", "raw_component_scores_after": {"passenger_volume_score": 15, "route_or_integration_visibility_score": 14, "load_factor_yield_score": 15, "fuel_cost_sensitivity_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 7, "sharecount_or_status_validation_risk": 12, "execution_risk_score": 13, "source_confidence_score": 2}, "weighted_score_after": 76, "stage_label_after": "Stage2/Yellow after source repair + validation + lifecycle 4B", "changed_components": ["passenger_volume_score", "route_or_integration_visibility_score", "load_factor_yield_score", "fuel_cost_sensitivity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified passenger volume, route/load-factor/yield economics, fuel-cost sensitivity, revenue and operating margin bridge; cap airline transport theme beta when evidence fails to refresh.", "MFE_90D_pct": 2.38, "MAE_90D_pct": -19.02, "score_return_alignment_label": "airline_transport_volume_margin_positive_with_validation", "current_profile_verdict": "C29 can allow airline/LCC positives only when passenger volume, route expansion, load factor, yield, fuel-cost sensitivity and margin bridge are visible. T'way produced later MFE but had large interim MAE and stock-web share-count changes, so source repair and share-count validation are mandatory."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE", "trigger_id": "TRG_R9L81-C29-089590-JEJU-AIR-LCC-PASSENGER-YIELD-FADE", "symbol": "089590", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"passenger_volume_score": 4, "route_or_integration_visibility_score": 3, "load_factor_yield_score": 3, "fuel_cost_sensitivity_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_or_status_validation_risk": 0, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"passenger_volume_score": 3, "route_or_integration_visibility_score": 1, "load_factor_yield_score": 1, "fuel_cost_sensitivity_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_or_status_validation_risk": 0, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["passenger_volume_score", "route_or_integration_visibility_score", "load_factor_yield_score", "fuel_cost_sensitivity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified passenger volume, route/load-factor/yield economics, fuel-cost sensitivity, revenue and operating margin bridge; cap airline transport theme beta when evidence fails to refresh.", "MFE_90D_pct": 1.75, "MAE_90D_pct": -18.1, "score_return_alignment_label": "false_positive_airline_transport_bridge_gap", "current_profile_verdict": "C29 should not treat LCC passenger recovery beta as durable Stage2 unless passenger volume, load factor, yield, fuel cost and operating margin bridge are visible. Jeju Air had almost no forward MFE after entry and then a persistent high-MAE path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE", "trigger_id": "TRG_R9L81-C29-020560-ASIANA-AIRLINE-MERGER-TRANSPORT-MARGIN-FADE", "symbol": "020560", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"passenger_volume_score": 4, "route_or_integration_visibility_score": 3, "load_factor_yield_score": 3, "fuel_cost_sensitivity_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_or_status_validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"passenger_volume_score": 3, "route_or_integration_visibility_score": 1, "load_factor_yield_score": 1, "fuel_cost_sensitivity_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 3, "sharecount_or_status_validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["passenger_volume_score", "route_or_integration_visibility_score", "load_factor_yield_score", "fuel_cost_sensitivity_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified passenger volume, route/load-factor/yield economics, fuel-cost sensitivity, revenue and operating margin bridge; cap airline transport theme beta when evidence fails to refresh.", "MFE_90D_pct": 10.02, "MAE_90D_pct": -19.35, "score_return_alignment_label": "false_positive_airline_transport_bridge_gap", "current_profile_verdict": "C29 should not treat airline merger/transport beta as durable volume-margin operating leverage unless passenger volume, yield, fuel-cost pass-through, integration path, revenue and margin bridge are visible. Asiana had early MFE, then a persistent high-MAE drawdown. The profile has a 2024-12-30 corporate-action candidate outside the selected 180D window, so extended-window ingestion needs validation."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AIRLINE_LCC_PASSENGER_YIELD_FUEL_COST_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "extended_status_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 airline/transport symbols outside top-covered 000270/204320/011210/005380/003490 set and outside loop-80 auto-supplier names, +3 LCC/airline merger/transport margin trigger families, +1 LCC lifecycle candidate with validation, +2 airline transport local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_sharecount_and_status_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "airline_LCC_passenger_yield_fuel_cost_margin_bridge_vs_transport_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified airline/LCC volume-margin operating leverage from generic passenger recovery or airline event beta. Stage2 requires passenger volume, load factor, yield, route/integration visibility, fuel-cost sensitivity, revenue conversion and operating margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count and extended-status flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["091810", "089590", "020560"], "share_count_validation_required": ["091810"], "extended_status_validation_required": ["020560"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 81, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "mobility_transport_volume_margin_bridge_required", "airline_yield_fuel_cost_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "share_count_validation_guard", "extended_status_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 can expand from auto suppliers into airline/transport volume-margin operating leverage. T'way is a volatile LCC lifecycle candidate after source repair and share-count validation; Jeju Air and Asiana show airline transport theme beta fading into local 4B when passenger volume, yield, fuel-cost and margin bridge are absent or stale."}
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
091810:
  name = 티웨이항공
  corporate_action_candidate_dates = 2020-11-27, 2022-05-12, 2023-02-23, 2025-09-15, 2026-01-13
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

089590:
  name = 제주항공
  corporate_action_candidate_dates = 2020-09-03, 2021-11-12, 2022-11-24
  selected window = 2024-02-01~D+180
  contamination = false

020560:
  name = 아시아나항공
  corporate_action_candidate_dates = 2021-01-15, 2024-12-30
  selected 180D window = 2024-02-01~D+180
  contamination = false for 180D
  extended-window ingestion should validate 2024-12-30 corporate-action/status continuity
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
091810 requires share-count validation before runtime promotion.
020560 requires extended status/corporate-action validation for horizons beyond the selected 180D window.
This MD is useful for stock-web path calibration and C29 airline/transport margin rule-shape discovery,
but coding-agent promotion requires non-proxy passenger volume, load factor, yield, fuel-cost sensitivity, route/integration status, revenue conversion and operating margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 091810 needs share-count validation, and 020560 needs extended status validation.

Candidate axis:
airline_LCC_passenger_yield_fuel_cost_margin_bridge_vs_transport_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 091810, 089590 and 020560.
4. Validate 091810 share-count changes inside the selected window.
5. Validate 020560 extended-window status/corporate-action continuity before horizons beyond 180D.
6. Keep generic C29 mobility/transport weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - passenger volume or route expansion is explicit,
   - load factor and yield are visible,
   - fuel-cost sensitivity is modeled,
   - revenue conversion and operating margin bridge exist,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is airline/passenger recovery theme beta only,
   - passenger volume/yield/fuel-cost/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not convert local 4B-watch into full 4B/4C without non-price route loss, demand break, fuel-cost shock, safety/regulatory issue, financing or margin break.
10. Emit before/after diagnostics and reject if verified airline volume-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 81
next_round = R10
next_loop = 81
round_schedule_status = valid
round_sector_consistency = pass
```

