# E2R Stock-Web v12 Residual Research — R9 Loop 72 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 72,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 72,
  "computed_next_round": "R10",
  "computed_next_loop": 72,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA",
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

Previous completed state in this interactive run: R8 / loop 72.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 72
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on C29/C30 bridge
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 72
```

R9 was routed to C29 because R10 is reserved for construction/PF balance-sheet break.  
This run avoids the top-covered C29 OEM symbols and tests non-OEM mobility routes: parts/AS margin, rental fleet utilization, and airline passenger-volume beta.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C29 has top concentration in `000270`, `204320`, `011210`, and `005380`.  
This run avoids those high-repeat rows and adds:

```text
012330 / 현대모비스 / auto parts AS-module margin leverage
089860 / 롯데렌탈 / rental fleet utilization / used-car economics
089590 / 제주항공 / LCC passenger recovery beta local-4B counterexample
```

Data-quality note:

```text
All three rows are stock-web calibration usable.
All three rows are marked source_proxy_only=true / evidence_url_pending=true.
This file is a source-repair queue plus stock-web path calibration, not immediate runtime weight evidence.
```

## Research thesis

C29 is not merely “cars sold more.”

The proper mechanism is:

```text
mobility volume or utilization
→ margin bridge
→ operating leverage
→ durable rerating
```

For a parts company, the bridge can be AS/module margin.  
For a rental company, it can be fleet utilization, used-car disposal economics, or capital return.  
For an airline, raw passenger recovery is not enough; fuel, FX, yield and capacity discipline decide whether the volume becomes profit.

Mobility is a road, not a destination.  
The car moving is not the signal; the toll booth collecting margin is.

---

## Case 1 — Positive after source repair: 012330 / 현대모비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is to verify AS/module margin recovery, parts mix, shareholder-return/value-up bridge, or operating leverage evidence.

```text
evidence_family = AUTO_PARTS_AS_MODULE_MARGIN_OPERATING_LEVERAGE_VALUEUP_BRIDGE
case_role = positive
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 208,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv`:

```text
2024-02-01,208000,222500,208000,219500
2024-03-15,265000,269000,263500,269000
2024-03-18,269500,270000,265500,268000
2024-08-05,215000,215500,200500,204000
```

### Backtest

```text
MFE_30D  = +29.33%
MAE_30D  = +0.00%
MFE_90D  = +29.81%
MAE_90D  = +0.00%
MFE_180D = +29.81%
MAE_180D = -3.61%
peak_180 = 270,000 on 2024-03-18
trough_180 = 200,500 on 2024-08-05
peak_to_later_drawdown = -25.74%
```

### Interpretation

This is a clean C29 positive path.  
The key is not OEM volume alone. Hyundai Mobis needs the bridge:

```text
parts / AS / module margin
or operating leverage
or capital-return/value-up path
```

The price path justifies a Stage2 candidate after source repair, but not a generic auto-beta weight.

---

## Case 2 — Positive slow anchor: 089860 / 롯데렌탈

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The evidence family to repair is rental fleet utilization, used-car margin, fleet turnover, and capital-return bridge.

```text
evidence_family = RENTAL_FLEET_UTILIZATION_USED_CAR_MARGIN_CAPITAL_RETURN_BRIDGE
case_role = positive_slow
trigger_date = 2024-02-22
entry_date = 2024-02-23
entry_price = 26,800
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/089/089860/2024.csv`:

```text
2024-02-23,26800,27750,26700,27650
2024-03-26,28150,28300,27800,27900
2024-06-28,31250,31500,30750,31250
2024-08-28,32100,32350,31400,32050
2024-09-09,29950,30600,29800,30400
```

### Backtest

```text
MFE_30D  = +5.60%
MAE_30D  = -0.75%
MFE_90D  = +17.54%
MAE_90D  = -0.75%
MFE_180D = +20.71%
MAE_180D = -0.93%
peak_180 = 32,350 on 2024-08-28
trough_180 = 26,550 on 2024-08-05
peak_to_later_drawdown = -7.88%
```

### Interpretation

This is the slow operating-leverage version of C29.  
It is not an explosive winner, but the low MAE matters. Rental fleet utilization is a grindstone, not a rocket.

A valid Stage2 requires evidence that utilization and used-car economics actually convert into margin/cash flow.

---

## Case 3 — Counterexample / local 4B: 089590 / 제주항공

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests LCC passenger-volume recovery without fuel/FX/unit-margin bridge.

```text
evidence_family = LCC_PASSENGER_VOLUME_RECOVERY_WITH_WEAK_FUEL_FX_MARGIN_BRIDGE
case_role = counterexample
trigger_date = 2024-01-04
entry_date = 2024-01-05
entry_price = 11,790
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/089/089590/2024.csv`:

```text
2024-01-05,11790,12500,11790,12430
2024-01-18,12920,13590,12850,13490
2024-03-04,11130,11140,10580,10690
2024-08-05,9460,9460,8300,8770
```

### Backtest

```text
MFE_30D  = +15.27%
MAE_30D  = -4.07%
MFE_90D  = +15.27%
MAE_90D  = -10.26%
MFE_180D = +15.27%
MAE_180D = -29.60%
peak_180 = 13,590 on 2024-01-18
trough_180 = 8,300 on 2024-08-05
peak_to_later_drawdown = -38.93%
```

### Interpretation

This is the C29 passenger-volume trap.  
The recovery story produced short-term MFE, but the 180D path became a drawdown.

For airlines, the model needs more than passenger volume:

```text
yield
fuel
FX
capacity discipline
unit margin
balance-sheet risk
```

Without that bridge, C29 should label the row as local 4B-watch / false Stage2, not durable Green.

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
do_not_raise_generic_C29_weight = true
do_not_treat_mobility_volume_beta_as_Green = true
do_not_convert_airline_drawdown_to_hard_4C_without_non_price_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA
```

This fine archetype covers:

```text
1. auto parts AS/module margin operating leverage → Stage2 possible after source repair
2. rental fleet utilization / used-car economics → slow Stage2 possible after source repair
3. LCC passenger recovery beta without fuel/FX/unit-margin bridge → local 4B-watch
```

---

## Machine-readable rows

### trigger rows

```jsonl
{"row_type": "trigger", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_id": "R9L72-C29-012330-MOBIS-AS-MODULE-MARGIN-LEVERAGE", "symbol": "012330", "company": "현대모비스", "trigger_type": "Stage2-Actionable-AutoPartsMarginBridge", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 208000.0, "mfe_30_pct": 29.33, "mae_30_pct": 0.0, "mfe_90_pct": 29.81, "mae_90_pct": 0.0, "mfe_180_pct": 29.81, "mae_180_pct": -3.61, "peak_price_180": 270000.0, "peak_date_180": "2024-03-18", "trough_price_180": 200500.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -25.74, "case_role": "positive", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "AUTO_PARTS_AS_MODULE_MARGIN_OPERATING_LEVERAGE_VALUEUP_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:HYUNDAI_MOBIS_2024_AS_MODULE_MARGIN_OPERATING_LEVERAGE_VALUEUP_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_id": "R9L72-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-SLOW-POSITIVE", "symbol": "089860", "company": "롯데렌탈", "trigger_type": "Stage2-Actionable-FleetUtilizationMarginBridge", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 26800.0, "mfe_30_pct": 5.6, "mae_30_pct": -0.75, "mfe_90_pct": 17.54, "mae_90_pct": -0.75, "mfe_180_pct": 20.71, "mae_180_pct": -0.93, "peak_price_180": 32350.0, "peak_date_180": "2024-08-28", "trough_price_180": 26550.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -7.88, "case_role": "positive_slow", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "RENTAL_FLEET_UTILIZATION_USED_CAR_MARGIN_CAPITAL_RETURN_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:LOTTE_RENTAL_2024_FLEET_UTILIZATION_USED_CAR_MARGIN_CAPITAL_RETURN_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "case_id": "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B", "symbol": "089590", "company": "제주항공", "trigger_type": "Stage4B-Local-AirlinePassengerBeta", "trigger_date": "2024-01-04", "entry_date": "2024-01-05", "entry_price": 11790.0, "mfe_30_pct": 15.27, "mae_30_pct": -4.07, "mfe_90_pct": 15.27, "mae_90_pct": -10.26, "mfe_180_pct": 15.27, "mae_180_pct": -29.6, "peak_price_180": 13590.0, "peak_date_180": "2024-01-18", "trough_price_180": 8300.0, "trough_date_180": "2024-08-05", "peak_to_later_drawdown_pct": -38.93, "case_role": "counterexample", "calibration_usable": true, "corporate_action_contaminated_180d": false, "evidence_family": "LCC_PASSENGER_VOLUME_RECOVERY_WITH_WEAK_FUEL_FX_MARGIN_BRIDGE", "evidence_url": "source_proxy_manual_verification_required:JEJU_AIR_2024_LCC_PASSENGER_RECOVERY_FUEL_FX_UNIT_MARGIN_BRIDGE", "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "case_id": "R9L72-C29-012330-MOBIS-AS-MODULE-MARGIN-LEVERAGE", "symbol": "012330", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 12, "bottleneck_pricing_power": 5, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["mobility_volume_margin_operating_leverage", "non_oem_mobility_route", "bridge_present_after_source_repair", "stage2_candidate", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C29 should allow Stage2 when mobility volume is tied to parts/AS/module margin recovery and operating leverage, not simply OEM vehicle beta. The stock-web path shows high MFE with controlled MAE, but non-proxy evidence needs repair before runtime promotion."}
{"row_type": "score_simulation", "case_id": "R9L72-C29-089860-LOTTE-RENTAL-FLEET-UTILIZATION-SLOW-POSITIVE", "symbol": "089860", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 10, "earnings_visibility": 12, "bottleneck_pricing_power": 5, "market_mispricing": 12, "valuation_rerating": 11, "capital_allocation": 3, "information_confidence": 2}, "diagnostic_flags": ["mobility_volume_margin_operating_leverage", "non_oem_mobility_route", "bridge_present_after_source_repair", "stage2_candidate", "source_proxy_only"], "expected_current_profile_stage": "Stage2-Actionable after source repair", "profile_stress_result": "C29 should include non-OEM mobility operating leverage such as fleet utilization, rental margin, used-car disposal economics, and capital return. The path is slow but controlled, which fits mobility operating leverage better than price-only beta."}
{"row_type": "score_simulation", "case_id": "R9L72-C29-089590-JEJU-AIR-PASSENGER-RECOVERY-BETA-LOCAL4B", "symbol": "089590", "baseline_current_proxy": "e2r_2_1_stock_web_calibrated", "raw_component_score_breakdown": {"eps_fcf_explosion": 4, "earnings_visibility": 5, "bottleneck_pricing_power": 3, "market_mispricing": 12, "valuation_rerating": 6, "capital_allocation": 2, "information_confidence": 2}, "diagnostic_flags": ["mobility_volume_margin_operating_leverage", "non_oem_mobility_route", "passenger_recovery_beta_weak_margin_bridge", "local_4b_watch", "source_proxy_only"], "expected_current_profile_stage": "Stage4B-local-watch / no durable Green", "profile_stress_result": "Airline passenger recovery beta can produce short-run MFE, but without fuel/FX/unit-margin and capacity discipline evidence it should not become durable Stage2/Green. The 180D MAE and post-peak drawdown argue for local 4B-watch."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "AUTO_PARTS_RENTAL_AIRLINE_VOLUME_MARGIN_LEVERAGE_VS_PRICE_ONLY_MOBILITY_BETA", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "current_profile_error_count": 1, "diversity_score_summary": "+3 underused C29 symbols, +3 mobility operating-leverage trigger families, +2 parts/rental positives, +1 LCC passenger-beta local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "auto_parts_rental_airline_volume_margin_leverage_vs_price_only_mobility_beta", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split true volume-to-margin operating leverage from generic mobility beta. Stage2 requires evidence of parts/AS/module margin, fleet utilization/used-car economics, or unit-margin improvement. Passenger-volume recovery without fuel/FX/unit-margin bridge should be capped or routed to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["012330", "089860", "089590"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 72, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 should not be limited to OEM volume beta. Hyundai Mobis and Lotte Rental show parts/rental operating-leverage paths with controlled MAE, while Jeju Air shows passenger-volume recovery beta failing without unit-margin/fuel/FX bridge and should route to local 4B-watch."}
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
012330:
  corporate_action_candidate_dates = 1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
  selected window = 2024-02-01~D+180
  contamination = false

089860:
  corporate_action_candidate_dates = none
  selected window = 2024-02-23~D+180
  contamination = false

089590:
  corporate_action_candidate_dates = 2020-09-03, 2021-11-12, 2022-11-24
  selected window = 2024-01-05~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
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
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair.

Candidate axis:
auto_parts_rental_airline_volume_margin_leverage_vs_price_only_mobility_beta

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 012330, 089860 and 089590.
4. Keep generic C29 weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - mobility volume/utilization is explicitly evidenced,
   - margin or operating leverage bridge is present,
   - parts/AS/module margin, fleet utilization, used-car economics, or unit-margin conversion is visible,
   - MAE remains controlled.
6. Consider local 4B-watch when:
   - the trigger is passenger-volume or mobility beta only,
   - fuel/FX/yield/unit-margin evidence is weak,
   - MAE_180D <= -25% or peak-to-later drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price deterioration evidence.
8. Emit before/after diagnostics and reject if C29 overblocks verified operating-leverage positives.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 72
next_round = R10
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

