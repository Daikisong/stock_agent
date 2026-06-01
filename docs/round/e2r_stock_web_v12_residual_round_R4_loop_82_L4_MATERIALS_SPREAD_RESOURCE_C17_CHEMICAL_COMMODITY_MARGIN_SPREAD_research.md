# E2R Stock-Web v12 Residual Research — R4 Loop 82 / L4 / C17

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R4",
  "scheduled_loop": 82,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 82,
  "computed_next_round": "R5",
  "computed_next_loop": 82,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "chemical_commodity_margin_spread_guardrail",
    "polyol_chlor_alkali_additive_spread_margin_bridge",
    "bounded_no_forced4B_guard",
    "chemical_theme_margin_fade_boundary",
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

Previous completed state in this interactive run: R3 / loop 82.

Therefore:

```text
scheduled_round = R4
scheduled_loop = 82
allowed_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_large_sector = L4_MATERIALS_SPREAD_RESOURCE
selected_canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
computed_next_round = R5
computed_next_loop = 82
```

R4 was routed to C17 because loop 81 R4 used C16 and loop 80 R4 used C15.  
This file tests chemical commodity spread/margin bridge boundaries rather than strategic resource policy or broad material spread supercycle.

## No-Repeat / novelty check

No hard duplicate is intentionally reused.

Hard duplicate key checked conceptually:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat shows C17 concentration in:

```text
298020, 011780, 006650, 011170, 010950, 014830
```

This run uses three different symbols:

```text
025000 / KPX케미칼 / polyol spread margin bounded recovery
004000 / 롯데정밀화학 / chlor-alkali / ammonia spread bounded RiskWatch
004430 / 송원산업 / polymer additive margin spread fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected 180D window.
```

## Research thesis

C17 is not “화학주가 반등했다.”

The mechanism must pass through:

```text
commodity spread / product price headline
→ input-cost pass-through
→ customer volume and utilization
→ pricing power
→ revenue conversion and margin bridge
→ durable rerating
```

화학 스프레드는 불꽃이 아니라 압력계다.  
C17이 보려는 것은 가격 headline이 실제 원가 전가, 판매량, 가동률, 매출, 마진의 압력으로 유지되는지다.

---

## Case 1 — Bounded spread recovery candidate: 025000 / KPX케미칼

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is polyol/PU spread, input-cost pass-through, customer volume, utilization, pricing and margin bridge evidence.

```text
evidence_family = POLYOL_PU_CHEMICAL_SPREAD_CUSTOMER_VOLUME_INPUT_COST_PASS_THROUGH_MARGIN_BRIDGE
case_role = positive_bounded_polyol_margin_recovery_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 43,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv`:

```text
2024-02-01,43200,44350,43200,44100
2024-02-13,45500,46050,45500,45850
2024-03-27,46400,46750,46250,46600
2024-07-29,46550,48200,46550,48150
2024-08-05,47300,47300,45200,45900
2024-09-23,46700,47400,46700,46800
2024-10-11,49000,49450,48900,49400
2024-10-25,47000,47100,46500,46900
```

### Backtest

```text
MFE_30D  = +6.83%
MAE_30D  = +0.00%
MFE_90D  = +8.22%
MAE_90D  = +0.00%
MFE_180D = +14.58%
MAE_180D = +0.00%
peak_180 = 49,500 on 2024-10-11~2024-10-15
trough_180 = 43,200 on 2024-02-01
peak_to_later_drawdown = -6.06%
```

### Interpretation

This is a bounded C17 spread-recovery candidate, not an explosive rerating row.  
The MAE stayed controlled, so it should not be forced into 4B without non-price margin break evidence.

Correct treatment:

```text
verified polyol spread / input-cost pass-through / customer volume / margin bridge → Stage2-Yellow possible
bounded MAE + weak bridge → RiskWatch
no forced 4B without non-price spread or margin deterioration
```

---

## Case 2 — Bounded no-forced-4B boundary: 004000 / 롯데정밀화학

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests chlor-alkali / ammonia / specialty chemical spread recovery with bounded MAE but incomplete durable bridge.

```text
evidence_family = CHLOR_ALKALI_AMMONIA_ECH_CELLULOSE_SPREAD_WITH_BOUNDED_MAE_AND_WEAK_REVENUE_MARGIN_BRIDGE
case_role = overbearish_counterexample_bounded_chemical_spread_no_forced4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 49,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/004/004000/2024.csv`:

```text
2024-02-01,49200,51500,48600,51000
2024-02-02,51100,51800,50200,51100
2024-02-27,47450,47850,46750,46900
2024-04-08,45600,45750,45000,45200
2024-08-05,45950,45950,42000,42900
2024-08-26,48450,49450,48150,49300
2024-09-05,49900,51200,49400,50600
2024-10-25,45700,45800,44400,45100
```

### Backtest

```text
MFE_30D  = +5.28%
MAE_30D  = -4.98%
MFE_90D  = +5.28%
MAE_90D  = -8.54%
MFE_180D = +5.28%
MAE_180D = -14.63%
peak_180 = 51,800 on 2024-02-02
trough_180 = 42,000 on 2024-08-05
peak_to_later_drawdown = -18.92%
```

### Interpretation

This is not durable Stage2, but it is also not forced local 4B.  
The price path is bounded enough that C17 should wait for margin proof, not create a price-only bearish escalation.

Correct treatment:

```text
chlor-alkali / ammonia / specialty spread watch
bounded MAE
→ no durable Stage2 without spread, volume, revenue and margin bridge
→ no forced 4B without non-price margin deterioration
```

---

## Case 3 — Counterexample / local 4B: 004430 / 송원산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests polymer additive / chemical spread theme beta without enough volume, pricing and margin bridge.

```text
evidence_family = POLYMER_ADDITIVE_CHEMICAL_SPREAD_THEME_WITH_WEAK_CUSTOMER_VOLUME_PRICING_REVENUE_MARGIN_BRIDGE
case_role = counterexample_polymer_additive_margin_fade_local4b
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
2024-04-08,13610,13750,13500,13500
2024-07-26,11250,12130,11220,12090
2024-08-05,11240,11240,9980,10100
2024-09-25,11550,12520,11330,12360
2024-10-28,13440,13800,13270,13600
```

### Backtest

```text
MFE_30D  = +5.89%
MAE_30D  = -0.52%
MFE_90D  = +5.89%
MAE_90D  = -11.72%
MFE_180D = +5.89%
MAE_180D = -34.69%
peak_180 = 16,180 on 2024-02-16
trough_180 = 9,980 on 2024-08-05
peak_to_later_drawdown = -38.32%
```

### Interpretation

This is a C17 chemical-additive margin fade row.  
The early MFE was tiny, and the later drawdown widened into local-4B territory.

Correct treatment:

```text
polymer additive / chemical spread theme beta
→ no verified customer volume / pricing / revenue / margin bridge
→ local 4B-watch
```

---

## Cross-case residual finding

### What this strengthens

```text
stage2_required_bridge = strengthen
chemical_spread_margin_bridge_required = strengthen
price_only_blowoff_blocks_positive_stage = strengthen
local_4b_watch_guard = strengthen
bounded_MAE_no_forced_4B_guard = strengthen
full_4b_requires_non_price_evidence = keep
```

### What this does not justify

```text
do_not_raise_generic_C17_chemical_spread_weight = true
do_not_treat_all_chemical_rebounds_as_Green = true
do_not_force_4B_on_bounded_chemical_rows_without_non_price_margin_break = true
do_not_convert_chemical_spread_drawdown_to_hard_4C_without_non_price_spread_customer_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE
```

This fine archetype covers:

```text
1. polyol/PU spread recovery with bounded MAE → Stage2-Yellow possible after source repair
2. chlor-alkali/ammonia spread watch with bounded MAE → RiskWatch / no durable Stage2 / no forced 4B
3. polymer additive margin/theme fade → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED", "symbol": "025000", "company_name": "KPX케미칼", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "positive", "best_trigger": "RiskWatch-PositivePolyolSpreadMarginRecoveryNoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should allow chemical spread recovery candidates only when input-cost pass-through, customer volume, utilization, pricing and margin bridge are visible. KPX Chemical had bounded MAE and mild MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair, not a forced 4B row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, input-cost pass-through, customer volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH", "symbol": "004000", "company_name": "롯데정밀화학", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "overbearish_counterexample", "best_trigger": "RiskWatch-ChlorAlkaliAmmoniaSpreadRecoveryNoDurableStage2NoForced4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not force bounded chemical spread rows into 4B when no non-price margin break is confirmed, but it also should not call durable Stage2 without spread recovery, volume, pricing and margin bridge. Lotte Fine Chemical is a bounded RiskWatch row.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, input-cost pass-through, customer volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE", "symbol": "004430", "company_name": "송원산업", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "case_type": "chemical_commodity_margin_spread", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / PolymerAdditiveMarginSpreadFadeWithLocal4BWatch", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C17 should not treat chemical additive or commodity spread theme beta as durable Stage2 unless customer volume, pricing power, input-cost pass-through, revenue and margin bridge are visible. Songwon Industrial had tiny early MFE and then high MAE before a late theme bounce.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy spread, input-cost pass-through, customer volume, pricing, revenue conversion and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED", "case_id": "R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED", "symbol": "025000", "company_name": "KPX케미칼", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "RiskWatch-PositivePolyolSpreadMarginRecoveryNoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 43200.0, "evidence_available_at_that_date": "POLYOL_PU_CHEMICAL_SPREAD_CUSTOMER_VOLUME_INPUT_COST_PASS_THROUGH_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KPX_CHEMICAL_2024_POLYOL_PU_SPREAD_INPUT_COST_PASS_THROUGH_CUSTOMER_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["spread_or_input_cost_candidate", "customer_volume_or_pricing_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/025/025000/2024.csv", "profile_path": "atlas/symbol_profiles/025/025000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.83, "MFE_90D_pct": 8.22, "MFE_180D_pct": 14.58, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": 0.0, "peak_date": "2024-10-11~2024-10-15", "peak_price": 49500.0, "drawdown_after_peak_pct": -6.06, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_spread_volume_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_customer_volume_loss_input_cost_shock_or_margin_break", "trigger_outcome_label": "positive_bounded_polyol_margin_recovery_no_forced4b", "current_profile_verdict": "C17 should allow chemical spread recovery candidates only when input-cost pass-through, customer volume, utilization, pricing and margin bridge are visible. KPX Chemical had bounded MAE and mild MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair, not a forced 4B row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEMICAL_SPREAD_025000_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH", "case_id": "R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH", "symbol": "004000", "company_name": "롯데정밀화학", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "RiskWatch-ChlorAlkaliAmmoniaSpreadRecoveryNoDurableStage2NoForced4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 49200.0, "evidence_available_at_that_date": "CHLOR_ALKALI_AMMONIA_ECH_CELLULOSE_SPREAD_WITH_BOUNDED_MAE_AND_WEAK_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:LOTTE_FINE_CHEMICAL_2024_CHLOR_ALKALI_AMMONIA_SPREAD_VOLUME_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["spread_or_input_cost_candidate", "customer_volume_or_pricing_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004000/2024.csv", "profile_path": "atlas/symbol_profiles/004/004000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.28, "MFE_90D_pct": 5.28, "MFE_180D_pct": 5.28, "MAE_30D_pct": -4.98, "MAE_90D_pct": -8.54, "MAE_180D_pct": -14.63, "peak_date": "2024-02-02", "peak_price": 51800.0, "drawdown_after_peak_pct": -18.92, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_spread_volume_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_customer_volume_loss_input_cost_shock_or_margin_break", "trigger_outcome_label": "overbearish_counterexample_bounded_chemical_spread_no_forced4b", "current_profile_verdict": "C17 should not force bounded chemical spread rows into 4B when no non-price margin break is confirmed, but it also should not call durable Stage2 without spread recovery, volume, pricing and margin bridge. Lotte Fine Chemical is a bounded RiskWatch row.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEMICAL_SPREAD_004000_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE", "case_id": "R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE", "symbol": "004430", "company_name": "송원산업", "round": "R4", "loop": "82", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|chemical_commodity_margin_spread_guardrail", "trigger_type": "Stage2-FalsePositive / PolymerAdditiveMarginSpreadFadeWithLocal4BWatch", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 15280.0, "evidence_available_at_that_date": "POLYMER_ADDITIVE_CHEMICAL_SPREAD_THEME_WITH_WEAK_CUSTOMER_VOLUME_PRICING_REVENUE_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SONGWON_INDUSTRIAL_2024_POLYMER_ADDITIVE_SPREAD_CUSTOMER_VOLUME_PRICING_REVENUE_MARGIN_BRIDGE", "stage2_evidence_fields": ["spread_or_input_cost_candidate", "customer_volume_or_pricing_candidate", "revenue_margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_or_pass_through_candidate"], "stage4b_evidence_fields": ["chemical_spread_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004430/2024.csv", "profile_path": "atlas/symbol_profiles/004/004430.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.89, "MFE_90D_pct": 5.89, "MFE_180D_pct": 5.89, "MAE_30D_pct": -0.52, "MAE_90D_pct": -11.71, "MAE_180D_pct": -34.69, "peak_date": "2024-02-16", "peak_price": 16180.0, "drawdown_after_peak_pct": -38.32, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_chemical_spread_peak_if_spread_volume_pricing_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_spread_collapse_customer_volume_loss_input_cost_shock_or_margin_break", "trigger_outcome_label": "counterexample_polymer_additive_margin_fade_local4b", "current_profile_verdict": "C17 should not treat chemical additive or commodity spread theme beta as durable Stage2 unless customer volume, pricing power, input-cost pass-through, revenue and margin bridge are visible. Songwon Industrial had tiny early MFE and then high MAE before a late theme bounce.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C17_CHEMICAL_SPREAD_004430_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED", "trigger_id": "TRG_R4L82-C17-025000-KPX-CHEMICAL-POLYOL-SPREAD-BOUNDED", "symbol": "025000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"spread_recovery_score": 13, "input_cost_pass_through_score": 12, "customer_volume_score": 12, "pricing_power_score": 11, "revenue_margin_bridge_score": 12, "relative_strength_score": 5, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_before": 68, "stage_label_before": "RiskWatch / Stage2-Yellow after source repair", "raw_component_scores_after": {"spread_recovery_score": 15, "input_cost_pass_through_score": 14, "customer_volume_score": 14, "pricing_power_score": 13, "revenue_margin_bridge_score": 14, "relative_strength_score": 4, "execution_risk_score": 12, "source_confidence_score": 2}, "weighted_score_after": 74, "stage_label_after": "RiskWatch / Stage2-Yellow only after source repair", "changed_components": ["spread_recovery_score", "input_cost_pass_through_score", "customer_volume_score", "pricing_power_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified spread recovery, input-cost pass-through, customer volume, pricing and margin bridge; cap chemical theme beta when bridge fails to refresh while protecting bounded rows from forced 4B.", "MFE_90D_pct": 8.22, "MAE_90D_pct": 0.0, "score_return_alignment_label": "chemical_spread_bounded_positive_or_riskwatch", "current_profile_verdict": "C17 should allow chemical spread recovery candidates only when input-cost pass-through, customer volume, utilization, pricing and margin bridge are visible. KPX Chemical had bounded MAE and mild MFE, so it is a RiskWatch/Stage2-Yellow candidate after source repair, not a forced 4B row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH", "trigger_id": "TRG_R4L82-C17-004000-LOTTE-FINE-CHEM-CHLOR-ALKALI-BOUNDED-RISKWATCH", "symbol": "004000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"spread_recovery_score": 6, "input_cost_pass_through_score": 6, "customer_volume_score": 5, "pricing_power_score": 5, "revenue_margin_bridge_score": 4, "relative_strength_score": 5, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 58, "stage_label_before": "RiskWatch / no durable Stage2 and no forced 4B", "raw_component_scores_after": {"spread_recovery_score": 5, "input_cost_pass_through_score": 5, "customer_volume_score": 4, "pricing_power_score": 4, "revenue_margin_bridge_score": 3, "relative_strength_score": 4, "execution_risk_score": 7, "source_confidence_score": 2}, "weighted_score_after": 60, "stage_label_after": "RiskWatch / no durable Stage2 and no forced 4B", "changed_components": ["spread_recovery_score", "input_cost_pass_through_score", "customer_volume_score", "pricing_power_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified spread recovery, input-cost pass-through, customer volume, pricing and margin bridge; cap chemical theme beta when bridge fails to refresh while protecting bounded rows from forced 4B.", "MFE_90D_pct": 5.28, "MAE_90D_pct": -8.54, "score_return_alignment_label": "chemical_spread_bounded_positive_or_riskwatch", "current_profile_verdict": "C17 should not force bounded chemical spread rows into 4B when no non-price margin break is confirmed, but it also should not call durable Stage2 without spread recovery, volume, pricing and margin bridge. Lotte Fine Chemical is a bounded RiskWatch row."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE", "trigger_id": "TRG_R4L82-C17-004430-SONGWON-INDUSTRIAL-ADDITIVE-MARGIN-FADE", "symbol": "004430", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"spread_recovery_score": 4, "input_cost_pass_through_score": 3, "customer_volume_score": 2, "pricing_power_score": 2, "revenue_margin_bridge_score": 1, "relative_strength_score": 5, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_before": 42, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"spread_recovery_score": 2, "input_cost_pass_through_score": 1, "customer_volume_score": 1, "pricing_power_score": 1, "revenue_margin_bridge_score": 1, "relative_strength_score": 4, "execution_risk_score": 26, "source_confidence_score": 2}, "weighted_score_after": 31, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["spread_recovery_score", "input_cost_pass_through_score", "customer_volume_score", "pricing_power_score", "revenue_margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified spread recovery, input-cost pass-through, customer volume, pricing and margin bridge; cap chemical theme beta when bridge fails to refresh while protecting bounded rows from forced 4B.", "MFE_90D_pct": 5.89, "MAE_90D_pct": -11.71, "score_return_alignment_label": "false_positive_chemical_theme_bridge_gap", "current_profile_verdict": "C17 should not treat chemical additive or commodity spread theme beta as durable Stage2 unless customer volume, pricing power, input-cost pass-through, revenue and margin bridge are visible. Songwon Industrial had tiny early MFE and then high MAE before a late theme bounce."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R4", "loop": 82, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "POLYOL_CHLOR_ALKALI_ADDITIVE_SPREAD_MARGIN_BRIDGE_VS_CHEMICAL_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "overbearish_counterexample_count": 1, "four_b_case_count": 1, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C17 chemical-spread symbols outside top-covered 298020/011780/006650/011170/010950/014830 set, +3 polyol/chlor-alkali/additive trigger families, +1 bounded spread recovery candidate, +1 bounded no-forced-4B row, +1 additive margin local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R4", "loop": 82, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "axis": "polyol_chlor_alkali_additive_spread_margin_bridge_vs_chemical_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C17 should split verified chemical spread/margin recovery from generic chemical theme beta. Stage2 requires spread recovery, input-cost pass-through, customer volume, utilization, pricing power, revenue conversion and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Bounded rows should remain RiskWatch/no-forced-4B unless non-price margin break is confirmed.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["025000", "004000", "004430"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": 82, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "existing_axis_strengthened": ["stage2_required_bridge", "chemical_spread_margin_bridge_required", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "bounded_MAE_no_forced_4B_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C17 needs chemical spread headlines to map into spread recovery, input-cost pass-through, customer volume, pricing and margin proof. KPX Chemical is a bounded spread recovery candidate after source repair; Lotte Fine Chemical is a bounded no-forced-4B RiskWatch row; Songwon Industrial shows polymer-additive margin/theme fade into local 4B."}
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
025000:
  name = KPX케미칼 from 2008-09-11, 포리올 / 한국포리올 before that
  corporate_action_candidate_dates = 2006-09-29
  selected window = 2024-02-01~D+180
  contamination = false

004000:
  name = 롯데정밀화학 from 2016-03-18, 삼성정밀화학 before that
  corporate_action_candidate_dates = profile continuation outside selected 2024 window by retrieved profile state
  selected window = 2024-02-01~D+180
  contamination = false

004430:
  name = 송원산업
  corporate_action_candidate_dates = 1997-01-03, 2004-02-10, 2004-04-20
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C17 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C17 chemical spread rule-shape discovery,
but coding-agent promotion requires non-proxy chemical spread, input-cost pass-through, customer volume, pricing, revenue conversion and margin evidence.
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
polyol_chlor_alkali_additive_spread_margin_bridge_vs_chemical_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 025000, 004000 and 004430.
4. Keep generic C17 chemical-spread weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - product spread or input-cost premise is explicit,
   - input-cost pass-through is visible,
   - customer volume and utilization are visible,
   - pricing power and revenue conversion exist,
   - margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is chemical spread/theme beta only,
   - customer volume / pricing / revenue / margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not force local 4B when bounded chemical rows have controlled MAE and no confirmed non-price margin break.
8. Do not convert local 4B-watch into full 4B/4C without non-price spread collapse, customer volume loss, input-cost shock, financing or margin break.
9. Emit before/after diagnostics and reject if verified chemical spread positives or bounded no-forced-4B rows are overblocked.
```

---

## Final round state

```text
completed_round = R4
completed_loop = 82
next_round = R5
next_loop = 82
round_schedule_status = valid
round_sector_consistency = pass
```

