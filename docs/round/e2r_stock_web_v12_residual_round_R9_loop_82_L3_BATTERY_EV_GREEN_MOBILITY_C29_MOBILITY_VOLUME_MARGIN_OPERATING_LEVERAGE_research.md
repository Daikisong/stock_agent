# E2R Stock-Web v12 Residual Research — R9 Loop 82 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 82,
  "computed_next_round": "R10",
  "computed_next_loop": 82,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_volume_margin_operating_leverage_guardrail",
    "logistics_rental_carsharing_utilization_margin_bridge",
    "transport_theme_fade_boundary",
    "share_count_validation_queue_creation",
    "extended_status_name_change_validation_queue_creation",
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

Previous completed state in this interactive run: R8 / loop 82.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 82
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 82
```

R9 was routed to C29 mobility/transport rather than construction/PF because the selected cases are logistics / rental / carsharing volume-margin paths.  
This file deliberately avoids loop-81 airline names and the top-covered C29 auto names.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 concentration in:

```text
UNKNOWN_SYMBOL, 000270, 005380, 204320, 018880, 161390
```

This run uses three different transport/mobility symbols:

```text
089860 / 롯데렌탈 / rental fleet utilization and residual-value margin bridge
403550 / 쏘카 / carsharing fleet utilization and platform unit-economics bridge
000120 / CJ대한통운 / logistics parcel volume and margin bridge fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
403550 shows share-count changes inside the selected 2024 shard and requires validation.
000120 is a valid 2024 CJ대한통운 row but stock-web profile has later name/status continuity complexity, so extended-horizon ingestion must validate name/status continuity.
```

## Research thesis

C29 is not “운송주가 올랐다.”

The mechanism must pass through:

```text
mobility / logistics / rental headline
→ volume or fleet utilization
→ pricing or cost pass-through
→ customer / contract mix
→ revenue conversion and margin bridge
→ durable operating leverage
```

운송주는 차와 트럭의 수가 아니라 그 차들이 빈 시간 없이 얼마나 굴러가고, 가격과 원가를 얼마나 마진으로 바꾸는지의 함수다.

---

## Case 1 — Bounded rental utilization candidate: 089860 / 롯데렌탈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is rental fleet utilization, residual-value cycle, pricing, rental demand, revenue conversion and margin bridge evidence.

```text
evidence_family = RENTAL_CAR_FLEET_UTILIZATION_RESIDUAL_VALUE_PRICING_REVENUE_MARGIN_BRIDGE
case_role = positive_bounded_rental_fleet_utilization_margin_candidate_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 26,500
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/089/089860/2024.csv`:

```text
2024-02-01,26500,26950,26500,26900
2024-02-23,26800,27750,26700,27650
2024-02-26,27800,28150,27450,27800
2024-04-02,27600,28400,27500,28100
2024-08-05,28650,28900,26550,27050
2024-08-28,32100,32350,31400,32050
2024-09-24,31550,32050,31350,31900
2024-10-25,28800,28800,28000,28550
```

### Backtest

```text
MFE_30D  = +6.23%
MAE_30D  = +0.00%
MFE_90D  = +7.17%
MAE_90D  = +0.00%
MFE_180D = +22.08%
MAE_180D = +0.00%
peak_180 = 32,350 on 2024-08-28
trough_180 = 26,500 on 2024-02-01
peak_to_later_drawdown = -13.45%
```

### Interpretation

This is a bounded C29 rental/fleet utilization candidate.  
The MAE stayed controlled, so it should not be forced into 4B without non-price deterioration.

Correct treatment:

```text
verified fleet utilization / residual value / pricing / margin bridge → Stage2-Yellow possible
bounded MAE + weak bridge → RiskWatch
no forced 4B without non-price utilization or margin break
```

---

## Case 2 — Carsharing platform candidate: 403550 / 쏘카

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_validation_required = true
source_repair_required = true
```

The source-repair task is carsharing active-user demand, fleet utilization, pricing, unit economics, revenue conversion and margin bridge evidence.

```text
evidence_family = CARSHARING_MOBILITY_PLATFORM_FLEET_UTILIZATION_ACTIVE_USER_PRICING_REVENUE_MARGIN_BRIDGE
case_role = positive_carsharing_platform_utilization_candidate_with_sharecount_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 16,430
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/403/403550/2024.csv`:

```text
2024-02-01,16430,16980,16260,16910
2024-02-20,18550,19320,18320,18550
2024-03-11,20500,21400,19900,21150
2024-03-25,21250,22550,21100,22200
2024-04-12,19410,21400,16850,19780
2024-08-05,19150,19150,17700,18320
2024-09-25,18810,18850,17810,17880
2024-10-31,18400,18500,18180,18320
```

### Backtest

```text
MFE_30D  = +17.59%
MAE_30D  = -1.03%
MFE_90D  = +37.25%
MAE_90D  = -1.03%
MFE_180D = +37.25%
MAE_180D = -1.03%
peak_180 = 22,550 on 2024-03-25
trough_180 = 16,260 on 2024-02-01
peak_to_later_drawdown = -21.51%
```

### Interpretation

This is a C29 carsharing/platform utilization candidate.  
The path is good enough to protect after source repair, but share-count validation blocks runtime promotion.

Correct treatment:

```text
verified fleet utilization / active-user demand / pricing / unit-economics bridge → Stage2-Yellow possible
share-count validation first
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 000120 / CJ대한통운

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
extended_name_status_validation_required = true
source_repair_required = true
```

This row tests logistics / parcel volume theme beta without enough margin operating-leverage bridge.

```text
evidence_family = LOGISTICS_PARCEL_DELIVERY_VOLUME_ECOMMERCE_FREIGHT_RATE_THEME_WITH_WEAK_MARGIN_BRIDGE
case_role = counterexample_logistics_volume_margin_theme_local4b_with_extended_name_validation
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 135,700
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/000/000120/2024.csv`:

```text
2024-02-01,135700,138500,134500,137400
2024-02-02,136000,148600,134500,148500
2024-02-27,128300,129000,123600,125400
2024-03-25,117300,118200,113700,116700
2024-07-24,92300,97000,91600,96000
2024-08-05,99700,100000,91000,93300
2024-09-11,99900,105400,99700,104000
2024-10-22,88300,88300,84200,87100
```

### Backtest

```text
MFE_30D  = +9.51%
MAE_30D  = -9.06%
MFE_90D  = +9.51%
MAE_90D  = -16.21%
MFE_180D = +9.51%
MAE_180D = -37.95%
peak_180 = 148,600 on 2024-02-02
trough_180 = 84,200 on 2024-10-22
peak_to_later_drawdown = -43.34%
```

### Interpretation

This is a C29 logistics volume/margin false-positive boundary.  
The early MFE did not become durable parcel-volume or logistics-margin operating leverage.

Correct treatment:

```text
logistics / parcel-volume theme beta
→ no verified volume / freight-rate / contract-mix / automation-productivity / margin bridge
→ local 4B-watch
→ extended name/status validation before long-horizon ingestion
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
mobility_volume_margin_bridge_required = strengthen
fleet_utilization_pricing_margin_guard = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
share_count_validation_guard = strengthen
extended_status_name_validation_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C29_mobility_transport_weight = true
do_not_treat_all_mobility_or_logistics_MFE_as_Green = true
do_not_ingest_sharecount_changed_or_name_sensitive_rows_without_validation = true
do_not_convert_transport_drawdown_to_hard_4C_without_non_price_volume_contract_cost_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE
```

This fine archetype covers:

```text
1. rental fleet utilization and residual-value margin bridge → Stage2-Yellow possible after source repair
2. carsharing platform utilization and unit-economics bridge → Stage2-Yellow possible after source repair and share-count validation
3. logistics / parcel-volume beta without margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN", "symbol": "089860", "company_name": "롯데렌탈", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositiveRentalFleetUtilizationResidualValueMarginBridgeNoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow rental/mobility positives only when fleet utilization, used-car residual value, pricing, rental demand, revenue conversion and margin bridge are visible. Lotte Rental produced bounded MAE and later MFE, so it is a protected RiskWatch/Stage2-Yellow candidate after source repair rather than forced 4B.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy logistics/rental/carsharing volume, utilization, pricing, cost pass-through, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN", "symbol": "403550", "company_name": "쏘카", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Yellow-CarsharingFleetUtilizationRevenueMarginBridgeWithSharecountValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 can protect car-sharing/platform mobility positives only when fleet utilization, active user demand, pricing, unit economics, revenue conversion and margin bridge are visible. Socar had controlled entry-basis MAE and strong MFE, but stock-web share count changes require validation before runtime promotion.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy logistics/rental/carsharing volume, utilization, pricing, cost pass-through, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE", "symbol": "000120", "company_name": "CJ대한통운", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / LogisticsParcelVolumeMarginFadeWithLocal4BAndNameChangeValidation", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat logistics/parcel volume beta as durable Stage2 unless parcel volume, freight-rate/pass-through, contract mix, automation productivity, revenue conversion and margin bridge are visible. CJ Logistics had early MFE and then persistent high-MAE fade, so it is a local-4B boundary until operating-leverage proof is repaired.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy logistics/rental/carsharing volume, utilization, pricing, cost pass-through, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN", "case_id": "R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN", "symbol": "089860", "company_name": "롯데렌탈", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail", "trigger_type": "RiskWatch-PositiveRentalFleetUtilizationResidualValueMarginBridgeNoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 26500.0, "evidence_available_at_that_date": "RENTAL_CAR_FLEET_UTILIZATION_RESIDUAL_VALUE_PRICING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_RENTAL_2024_RENTAL_FLEET_UTILIZATION_RESIDUAL_VALUE_PRICING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["volume_or_utilization_candidate", "pricing_or_cost_pass_through_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_contract_mix_candidate"], "stage4b_evidence_fields": ["transport_mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/089/089860/2024.csv", "profile_path": "atlas/symbol_profiles/089/089860.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.23, "MFE_90D_pct": 7.17, "MFE_180D_pct": 22.08, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-08-28", "peak_price": 32350.0, "drawdown_after_peak_pct": -13.45, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_transport_mobility_peak_if_volume_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_volume_collapse_contract_loss_cost_shock_financing_or_margin_break", "trigger_outcome_label": "positive_bounded_rental_fleet_utilization_margin_candidate_no_forced4b", "current_profile_verdict": "C29 should allow rental/mobility positives only when fleet utilization, used-car residual value, pricing, rental demand, revenue conversion and margin bridge are visible. Lotte Rental produced bounded MAE and later MFE, so it is a protected RiskWatch/Stage2-Yellow candidate after source repair rather than forced 4B.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_name_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_089860_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN", "case_id": "R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN", "symbol": "403550", "company_name": "쏘카", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail", "trigger_type": "Stage2-Yellow-CarsharingFleetUtilizationRevenueMarginBridgeWithSharecountValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 16430.0, "evidence_available_at_that_date": "CARSHARING_MOBILITY_PLATFORM_FLEET_UTILIZATION_ACTIVE_USER_PRICING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SOCAR_2024_CARSHARING_FLEET_UTILIZATION_ACTIVE_USER_PRICING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["volume_or_utilization_candidate", "pricing_or_cost_pass_through_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_contract_mix_candidate"], "stage4b_evidence_fields": ["transport_mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/403/403550/2024.csv", "profile_path": "atlas/symbol_profiles/403/403550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.59, "MFE_90D_pct": 37.25, "MFE_180D_pct": 37.25, "MAE_30D_pct": -1.03, "MAE_90D_pct": -1.03, "MAE_180D_pct": -1.03, "peak_date": "2024-03-25", "peak_price": 22550.0, "drawdown_after_peak_pct": -21.51, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_transport_mobility_peak_if_volume_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_volume_collapse_contract_loss_cost_shock_financing_or_margin_break", "trigger_outcome_label": "positive_carsharing_platform_utilization_candidate_with_sharecount_validation", "current_profile_verdict": "C29 can protect car-sharing/platform mobility positives only when fleet utilization, active user demand, pricing, unit economics, revenue conversion and margin bridge are visible. Socar had controlled entry-basis MAE and strong MFE, but stock-web share count changes require validation before runtime promotion.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_name_validation_required", "share_count_change_inside_window": true, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_403550_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE", "case_id": "R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE", "symbol": "000120", "company_name": "CJ대한통운", "round": "R9", "loop": "82", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_volume_margin_operating_leverage_guardrail", "trigger_type": "Stage2-FalsePositive / LogisticsParcelVolumeMarginFadeWithLocal4BAndNameChangeValidation", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 135700.0, "evidence_available_at_that_date": "LOGISTICS_PARCEL_DELIVERY_VOLUME_ECOMMERCE_FREIGHT_RATE_THEME_WITH_WEAK_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:CJ_LOGISTICS_2024_PARCEL_VOLUME_FREIGHT_RATE_CONTRACT_MIX_AUTOMATION_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["volume_or_utilization_candidate", "pricing_or_cost_pass_through_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "customer_or_contract_mix_candidate"], "stage4b_evidence_fields": ["transport_mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000120/2024.csv", "profile_path": "atlas/symbol_profiles/000/000120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.51, "MFE_90D_pct": 9.51, "MFE_180D_pct": 9.51, "MAE_30D_pct": -9.06, "MAE_90D_pct": -16.21, "MAE_180D_pct": -37.95, "peak_date": "2024-02-02", "peak_price": 148600.0, "drawdown_after_peak_pct": -43.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_transport_mobility_peak_if_volume_utilization_revenue_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_volume_collapse_contract_loss_cost_shock_financing_or_margin_break", "trigger_outcome_label": "counterexample_logistics_volume_margin_theme_local4b_with_extended_name_validation", "current_profile_verdict": "C29 should not treat logistics/parcel volume beta as durable Stage2 unless parcel volume, freight-rate/pass-through, contract mix, automation productivity, revenue conversion and margin bridge are visible. CJ Logistics had early MFE and then persistent high-MAE fade, so it is a local-4B boundary until operating-leverage proof is repaired.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_or_sharecount_name_validation_required", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_000120_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN", "trigger_id": "TRG_R9L82-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-MARGIN", "symbol": "089860", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_utilization_score": 14, "pricing_cost_pass_through_score": 13, "customer_contract_mix_score": 12, "revenue_conversion_score": 12, "margin_bridge_score": 12, "relative_strength_score": 8, "validation_risk": 0, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "RiskWatch / Stage2-Yellow candidate after source repair and validation", "raw_component_scores_after": {"volume_utilization_score": 16, "pricing_cost_pass_through_score": 15, "customer_contract_mix_score": 14, "revenue_conversion_score": 14, "margin_bridge_score": 14, "relative_strength_score": 7, "validation_risk": 0, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Yellow after source repair + lifecycle guard", "changed_components": ["volume_utilization_score", "pricing_cost_pass_through_score", "customer_contract_mix_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified transport/mobility volume, fleet utilization, pricing/cost pass-through, contract mix, revenue conversion and margin bridge; cap theme beta when operating-leverage evidence fails to refresh.", "MFE_90D_pct": 7.17, "MAE_90D_pct": 0.0, "score_return_alignment_label": "mobility_volume_margin_positive_or_bounded_candidate", "current_profile_verdict": "C29 should allow rental/mobility positives only when fleet utilization, used-car residual value, pricing, rental demand, revenue conversion and margin bridge are visible. Lotte Rental produced bounded MAE and later MFE, so it is a protected RiskWatch/Stage2-Yellow candidate after source repair rather than forced 4B."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN", "trigger_id": "TRG_R9L82-C29-403550-SOCAR-CARSHARING-UTILIZATION-MARGIN", "symbol": "403550", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_utilization_score": 14, "pricing_cost_pass_through_score": 13, "customer_contract_mix_score": 12, "revenue_conversion_score": 12, "margin_bridge_score": 12, "relative_strength_score": 8, "validation_risk": 10, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 72, "stage_label_before": "RiskWatch / Stage2-Yellow candidate after source repair and validation", "raw_component_scores_after": {"volume_utilization_score": 16, "pricing_cost_pass_through_score": 15, "customer_contract_mix_score": 14, "revenue_conversion_score": 14, "margin_bridge_score": 14, "relative_strength_score": 7, "validation_risk": 12, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 78, "stage_label_after": "Stage2-Yellow after source repair + lifecycle guard", "changed_components": ["volume_utilization_score", "pricing_cost_pass_through_score", "customer_contract_mix_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified transport/mobility volume, fleet utilization, pricing/cost pass-through, contract mix, revenue conversion and margin bridge; cap theme beta when operating-leverage evidence fails to refresh.", "MFE_90D_pct": 37.25, "MAE_90D_pct": -1.03, "score_return_alignment_label": "mobility_volume_margin_positive_or_bounded_candidate", "current_profile_verdict": "C29 can protect car-sharing/platform mobility positives only when fleet utilization, active user demand, pricing, unit economics, revenue conversion and margin bridge are visible. Socar had controlled entry-basis MAE and strong MFE, but stock-web share count changes require validation before runtime promotion."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE", "trigger_id": "TRG_R9L82-C29-000120-CJ-LOGISTICS-PARCEL-VOLUME-MARGIN-FADE", "symbol": "000120", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"volume_utilization_score": 4, "pricing_cost_pass_through_score": 3, "customer_contract_mix_score": 2, "revenue_conversion_score": 2, "margin_bridge_score": 1, "relative_strength_score": 4, "validation_risk": 10, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"volume_utilization_score": 2, "pricing_cost_pass_through_score": 1, "customer_contract_mix_score": 1, "revenue_conversion_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "validation_risk": 12, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["volume_utilization_score", "pricing_cost_pass_through_score", "customer_contract_mix_score", "revenue_conversion_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified transport/mobility volume, fleet utilization, pricing/cost pass-through, contract mix, revenue conversion and margin bridge; cap theme beta when operating-leverage evidence fails to refresh.", "MFE_90D_pct": 9.51, "MAE_90D_pct": -16.21, "score_return_alignment_label": "false_positive_transport_mobility_bridge_gap", "current_profile_verdict": "C29 should not treat logistics/parcel volume beta as durable Stage2 unless parcel volume, freight-rate/pass-through, contract mix, automation productivity, revenue conversion and margin bridge are visible. CJ Logistics had early MFE and then persistent high-MAE fade, so it is a local-4B boundary until operating-leverage proof is repaired."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "LOGISTICS_RENTAL_CARSHARING_VOLUME_UTILIZATION_MARGIN_BRIDGE_VS_TRANSPORT_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "extended_name_status_validation_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 mobility/logistics symbols outside top-covered UNKNOWN/000270/005380/204320/018880/161390 set and outside loop-81 airline names, +3 rental/carsharing/logistics trigger families, +2 bounded mobility positives, +1 logistics volume-margin local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_sharecount_and_name_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "logistics_rental_carsharing_volume_utilization_margin_bridge_vs_transport_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified logistics/rental/carsharing volume-utilization margin rerating from generic mobility/transport theme beta. Stage2 requires volume/utilization, pricing or cost pass-through, customer/contract mix, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count and extended name/status flags require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["089860", "403550", "000120"], "share_count_validation_required": ["403550"], "extended_name_status_validation_required": ["000120"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 82, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "mobility_volume_margin_bridge_required", "fleet_utilization_pricing_margin_guard", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "share_count_validation_guard", "extended_status_name_validation_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs mobility/logistics MFE to map into volume, fleet utilization, pricing/cost pass-through, contract mix, revenue conversion and margin proof. Lotte Rental and Socar are bounded mobility utilization candidates after source repair and validation; CJ Logistics shows logistics volume-margin theme fading into local 4B when operating leverage evidence is absent or stale."}
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
089860:
  name = 롯데렌탈
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

403550:
  name = 쏘카
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

000120:
  name = CJ대한통운 during selected 2024 window
  profile has later name/status complexity after selected window
  corporate_action_candidate_dates = 1996-01-03, 1997-02-28, 1999-08-25, 2000-05-19, 2001-08-03, 2001-10-19, 2006-06-15, 2008-03-21, 2009-05-15
  selected window = 2024-02-01~D+180
  contamination = false
  extended_name_status_validation_required = true for long-horizon ingestion
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
403550 requires share-count validation before runtime promotion.
000120 requires extended name/status validation before longer-horizon ingestion.
This MD is useful for stock-web path calibration and C29 mobility/logistics rule-shape discovery,
but coding-agent promotion requires non-proxy volume, fleet utilization, pricing/cost pass-through, contract mix, revenue conversion and margin evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair, 403550 needs share-count validation, and 000120 needs extended name/status validation.

Candidate axis:
logistics_rental_carsharing_volume_utilization_margin_bridge_vs_transport_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 089860, 403550 and 000120.
4. Validate 403550 share-count changes inside the selected window.
5. Validate 000120 name/status continuity for any horizon beyond the selected 180D window.
6. Keep generic C29 mobility/transport weight unchanged until source repair is complete.
7. Consider Stage2 only when:
   - volume or fleet utilization is explicit,
   - pricing or cost pass-through is visible,
   - customer / contract mix is visible,
   - revenue conversion and margin bridge are credible,
   - MAE remains controlled or the signal is lifecycle-managed.
8. Consider local 4B-watch when:
   - the trigger is mobility/logistics theme beta only,
   - volume / utilization / pricing / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
9. Do not force local 4B when bounded rental/carsharing rows have controlled MAE and no confirmed non-price bridge break.
10. Do not convert local 4B-watch into full 4B/4C without non-price volume collapse, contract loss, cost shock, financing or margin break.
11. Emit before/after diagnostics and reject if verified mobility utilization positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 82
next_round = R10
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

