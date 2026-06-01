# E2R Stock-Web v12 Residual Research — R9 Loop 78 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 78,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 78,
  "computed_next_round": "R10",
  "computed_next_loop": 78,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_supplier_volume_margin_guardrail",
    "tire_auto_module_thermal_bridge_vs_EV_parts_theme_beta",
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

Previous completed state in this interactive run: R8 / loop 78.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 78
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 78
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests tire, auto module/AS-parts, and thermal-management supplier volume-margin bridges.

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

This run uses three different symbols and avoids loop-77 R9 names:

```text
073240 / 금호타이어 / tire OE-replacement mix-margin bridge
012330 / 현대모비스 / auto module / AS-parts mix-margin bridge
018880 / 한온시스템 / thermal EV-parts theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
012330 shows share-count changes inside the selected window and requires coding-agent validation before runtime promotion.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C29 is not “자동차 부품주가 올랐다.”

The mechanism must pass through:

```text
customer program / mobility demand
→ OE, replacement, AS or module volume
→ product mix, utilization or cost spread
→ pricing and margin conversion
→ durable operating leverage
```

모빌리티 부품주는 엔진룸의 작은 톱니다.  
C29가 보려는 것은 그 톱니가 실제 물량, 믹스, 가동률, 마진이라는 기어와 맞물려 돌아가는지다.

---

## Case 1 — Positive with lifecycle 4B: 073240 / 금호타이어

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tire OE/replacement volume, product mix, raw-material cost spread and margin bridge evidence.

```text
evidence_family = TIRE_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 5,750
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv`:

```text
2024-02-01,5750,6060,5750,5930
2024-02-16,6550,6780,6510,6780
2024-04-30,6940,7250,6840,7040
2024-05-02,7040,7900,6980,7830
2024-05-07,8290,8360,8010,8120
2024-08-05,4930,4930,4280,4465
2024-09-09,4205,4370,4130,4350
```

### Backtest

```text
MFE_30D  = +17.91%
MAE_30D  = +0.00%
MFE_90D  = +45.39%
MAE_90D  = -5.57%
MFE_180D = +45.39%
MAE_180D = -25.57%
peak_180 = 8,360 on 2024-05-07
trough_180 = 4,280 on 2024-08-05
peak_to_later_drawdown = -48.80%
```

### Interpretation

This is a C29 tire mix-margin MFE candidate.  
The move was real, but the later high-MAE path says the tire mix/cost/margin bridge cannot be left stale.

Correct treatment:

```text
verified OE/replacement volume / mix / cost-spread / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Slow positive with lifecycle 4B: 012330 / 현대모비스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
share_count_change_inside_window = true
source_repair_required = true
```

The source-repair task is auto module/AS-parts customer volume, product mix, electrification exposure, pricing and margin bridge evidence.

```text
evidence_family = AUTO_MODULE_AS_PARTS_VOLUME_MIX_CUSTOMER_PROGRAM_MARGIN_BRIDGE
case_role = positive_slow_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 208,000
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv`:

```text
2024-02-01,208000,222500,208000,219500
2024-02-23,243000,250000,242500,247000
2024-03-15,265000,269000,263500,269000
2024-04-03,246500,249500,238500,240500
2024-08-05,215000,215500,200500,204000
2024-10-25,249500,267000,248000,256500
```

### Backtest

```text
MFE_30D  = +20.19%
MAE_30D  = +0.00%
MFE_90D  = +29.33%
MAE_90D  = +0.00%
MFE_180D = +29.33%
MAE_180D = -3.61%
peak_180 = 269,000 on 2024-03-15
trough_180 = 200,500 on 2024-08-05
peak_to_later_drawdown = -25.47%
```

### Interpretation

This is a slow C29 positive, not a blow-off row.  
It should not be overblocked if AS-parts, module mix, customer volume and margin bridge are verified.

Correct treatment:

```text
verified module/AS-parts volume / product mix / margin bridge → Stage2-Yellow possible
share-count validation first
bridge stale after peak → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 018880 / 한온시스템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests EV thermal-management / auto-parts beta without enough program volume and margin bridge.

```text
evidence_family = THERMAL_MANAGEMENT_EV_PARTS_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE
case_role = counterexample_thermal_EV_parts_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,160
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv`:

```text
2024-02-01,6160,6420,6120,6360
2024-02-13,6470,6590,6400,6520
2024-03-19,5910,5930,5590,5590
2024-07-18,5650,5650,5410,5500
2024-08-05,4290,4300,3800,3870
2024-10-02,4250,4250,3860,3865
```

### Backtest

```text
MFE_30D  = +6.98%
MAE_30D  = -2.44%
MFE_90D  = +6.98%
MAE_90D  = -9.74%
MFE_180D = +6.98%
MAE_180D = -38.31%
peak_180 = 6,590 on 2024-02-13
trough_180 = 3,800 on 2024-08-05~2024-08-09
peak_to_later_drawdown = -42.34%
```

### Interpretation

This is a C29 false-positive boundary.  
Thermal-management exposure did not validate durable volume-margin operating leverage.

Correct treatment:

```text
thermal / EV-parts theme beta
→ no verified customer program / volume / pricing / margin bridge
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
share_count_validation_guard = strengthen
```

### What this does not justify

```text
do_not_raise_generic_C29_mobility_parts_theme_weight = true
do_not_treat_all_auto_parts_or_tire_MFE_as_Green = true
do_not_convert_mobility_supplier_drawdown_to_hard_4C_without_non_price_customer_program_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE
```

This fine archetype covers:

```text
1. tire OE/replacement mix-margin bridge → Stage2 possible after source repair
2. auto module/AS-parts mix-margin bridge → Stage2-Yellow possible, lifecycle-managed
3. thermal/EV-parts beta without volume-margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-TireOEMReplacementMixMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow tire names when OE/replacement volume, product mix, utilization, raw-material spread and margin bridge are visible. Kumho Tire produced large MFE, but later high MAE and post-peak drawdown require lifecycle local 4B if mix/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/AS volume, product mix, utilization, pricing, cost spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-SlowPositive-AutoModuleASVolumeMixMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should preserve large auto-module and AS-parts suppliers when customer volume, module mix, AS parts profitability, electrification exposure and margin bridge are visible. Hyundai Mobis produced a slow MFE with controlled MAE; it should not be overblocked, but lifecycle local 4B is needed if mix/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/AS volume, product mix, utilization, pricing, cost spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / ThermalEVPartsVolumeMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat thermal-management or EV-parts beta as durable Stage2 unless customer program, volume, pricing, utilization and margin bridge are visible. Hanon Systems had only small MFE and then a severe MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/AS volume, product mix, utilization, pricing, cost spread and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN", "case_id": "R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN", "symbol": "073240", "company_name": "금호타이어", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Actionable-TireOEMReplacementMixMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 5750.0, "evidence_available_at_that_date": "TIRE_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:KUMHO_TIRE_2024_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_AS_or_cost_spread_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/073/073240/2024.csv", "profile_path": "atlas/symbol_profiles/073/073240.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.91, "MFE_90D_pct": 45.39, "MFE_180D_pct": 45.39, "MAE_30D_pct": 0.0, "MAE_90D_pct": -5.57, "MAE_180D_pct": -25.57, "peak_date": "2024-05-07", "peak_price": 8360.0, "drawdown_after_peak_pct": -48.8, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should allow tire names when OE/replacement volume, product mix, utilization, raw-material spread and margin bridge are visible. Kumho Tire produced large MFE, but later high MAE and post-peak drawdown require lifecycle local 4B if mix/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_PARTS_073240_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE", "case_id": "R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE", "symbol": "012330", "company_name": "현대모비스", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-SlowPositive-AutoModuleASVolumeMixMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 208000.0, "evidence_available_at_that_date": "AUTO_MODULE_AS_PARTS_VOLUME_MIX_CUSTOMER_PROGRAM_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_MOBIS_2024_AUTO_MODULE_AS_PARTS_VOLUME_MIX_ELECTRIFICATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_AS_or_cost_spread_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/012/012330/2024.csv", "profile_path": "atlas/symbol_profiles/012/012330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 20.19, "MFE_90D_pct": 29.33, "MFE_180D_pct": 29.33, "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -3.61, "peak_date": "2024-03-15", "peak_price": 269000.0, "drawdown_after_peak_pct": -25.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_slow_with_later_4b_watch", "current_profile_verdict": "C29 should preserve large auto-module and AS-parts suppliers when customer volume, module mix, AS parts profitability, electrification exposure and margin bridge are visible. Hyundai Mobis produced a slow MFE with controlled MAE; it should not be overblocked, but lifecycle local 4B is needed if mix/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": true, "same_entry_group_id": "C29_MOBILITY_PARTS_012330_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE", "case_id": "R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE", "symbol": "018880", "company_name": "한온시스템", "round": "R9", "loop": "78", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / ThermalEVPartsVolumeMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6160.0, "evidence_available_at_that_date": "THERMAL_MANAGEMENT_EV_PARTS_THEME_WITH_WEAK_VOLUME_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANON_SYSTEMS_2024_THERMAL_MANAGEMENT_EV_PARTS_CUSTOMER_PROGRAM_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_or_utilization_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_AS_or_cost_spread_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/018/018880/2024.csv", "profile_path": "atlas/symbol_profiles/018/018880.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.98, "MFE_90D_pct": 6.98, "MFE_180D_pct": 6.98, "MAE_30D_pct": -2.44, "MAE_90D_pct": -9.74, "MAE_180D_pct": -38.31, "peak_date": "2024-02-13", "peak_price": 6590.0, "drawdown_after_peak_pct": -42.34, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_parts_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_thermal_EV_parts_local4b", "current_profile_verdict": "C29 should not treat thermal-management or EV-parts beta as durable Stage2 unless customer program, volume, pricing, utilization and margin bridge are visible. Hanon Systems had only small MFE and then a severe MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_PARTS_018880_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN", "trigger_id": "TRG_R9L78-C29-073240-KUMHO-TIRE-OE-REPLACEMENT-MIX-MARGIN", "symbol": "073240", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 14, "program_visibility_score": 13, "mix_pricing_score": 13, "utilization_or_cost_spread_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 9, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 16, "program_visibility_score": 15, "mix_pricing_score": 15, "utilization_or_cost_spread_score": 14, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 10, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer volume/program, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 45.39, "MAE_90D_pct": -5.57, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 should allow tire names when OE/replacement volume, product mix, utilization, raw-material spread and margin bridge are visible. Kumho Tire produced large MFE, but later high MAE and post-peak drawdown require lifecycle local 4B if mix/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE", "trigger_id": "TRG_R9L78-C29-012330-HYUNDAI-MOBIS-MODULE-AS-MARGIN-BRIDGE", "symbol": "012330", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 14, "program_visibility_score": 13, "mix_pricing_score": 13, "utilization_or_cost_spread_score": 12, "margin_bridge_score": 13, "relative_strength_score": 12, "execution_risk_score": 9, "sharecount_validation_risk": 8, "source_confidence_score": 2}, "weighted_score_before": 78, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 16, "program_visibility_score": 15, "mix_pricing_score": 15, "utilization_or_cost_spread_score": 14, "margin_bridge_score": 15, "relative_strength_score": 11, "execution_risk_score": 10, "sharecount_validation_risk": 10, "source_confidence_score": 2}, "weighted_score_after": 84, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer volume/program, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 29.33, "MAE_90D_pct": 0.0, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 should preserve large auto-module and AS-parts suppliers when customer volume, module mix, AS parts profitability, electrification exposure and margin bridge are visible. Hyundai Mobis produced a slow MFE with controlled MAE; it should not be overblocked, but lifecycle local 4B is needed if mix/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE", "trigger_id": "TRG_R9L78-C29-018880-HANON-THERMAL-EV-PARTS-THEME-FADE", "symbol": "018880", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "program_visibility_score": 3, "mix_pricing_score": 3, "utilization_or_cost_spread_score": 2, "margin_bridge_score": 2, "relative_strength_score": 3, "execution_risk_score": 22, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_before": 47, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "program_visibility_score": 1, "mix_pricing_score": 1, "utilization_or_cost_spread_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 24, "sharecount_validation_risk": 0, "source_confidence_score": 2}, "weighted_score_after": 34, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer volume/program, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 6.98, "MAE_90D_pct": -9.74, "score_return_alignment_label": "false_positive_mobility_parts_bridge_gap", "current_profile_verdict": "C29 should not treat thermal-management or EV-parts beta as durable Stage2 unless customer program, volume, pricing, utilization and margin bridge are visible. Hanon Systems had only small MFE and then a severe MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_MODULE_THERMAL_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 1, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 mobility/tire/module/thermal symbols outside top-covered 000270/204320/011210/005380/003490 set and outside loop-77 R9 names, +3 tire/module/thermal trigger families, +2 mobility volume-margin positives, +1 EV thermal parts local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_and_sharecount_validation_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "tire_auto_module_thermal_volume_mix_margin_bridge_vs_EV_parts_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified tire/module/thermal supplier volume-margin rerating from generic EV/auto-parts theme beta. Stage2 requires customer program or volume, OE/replacement/AS demand, product mix, utilization or cost spread, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch. Share-count changes require validation before runtime promotion.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["073240", "012330", "018880"], "share_count_validation_required": ["012330"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 78, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "share_count_validation_guard"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs customer volume, mix, utilization and margin proof. Kumho Tire and Hyundai Mobis show tire/module volume-margin MFE candidates after source repair; Hanon Systems shows thermal/EV parts beta fading into local 4B when volume and margin bridge are absent or stale."}
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
073240:
  name = 금호타이어
  corporate_action_candidate_dates = 2010-11-02, 2010-12-14, 2018-07-20
  selected window = 2024-02-01~D+180
  contamination = false

012330:
  name = 현대모비스 from 2000-11-02, 현대정공 before that
  corporate_action_candidate_dates = 1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
  selected window = 2024-02-01~D+180
  contamination = false by profile
  share_count_change_inside_window = true → coding-agent validation required

018880:
  name = 한온시스템 from 2015-08-07, 한라비스테온공조 / 한라공조 before that
  corporate_action_candidate_dates = 2004-05-12, 2016-02-16, 2025-01-09, 2026-01-12
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
012330 also requires share-count validation before runtime promotion.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy customer program, OE/replacement/AS volume, product mix, utilization, pricing, cost spread and margin bridge evidence.
```

---

## Deferred Coding Agent Handoff Prompt

Do not execute this now.

```text
You are the coding agent for Songdaiki/stock_agent.

Read this standalone v12 residual research MD and ingest machine-readable rows only after validation.

Do not patch production scoring blindly.
This R9/C29 artifact is marked do_not_propose_new_weight_delta=true because all rows need source repair and 012330 needs share-count validation.

Candidate axis:
tire_auto_module_thermal_volume_mix_margin_bridge_vs_EV_parts_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 073240, 012330 and 018880.
4. Validate 012330 share-count changes inside the selected window.
5. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
6. Consider Stage2 only when:
   - customer program or mobility demand is explicit,
   - OE/replacement/AS/module volume is visible,
   - product mix, utilization or cost-spread bridge exists,
   - pricing and margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
7. Consider local 4B-watch when:
   - the trigger is tire/auto-parts/thermal EV theme beta only,
   - customer program/volume/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
8. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, program delay, order cut, volume decline, pricing/mix collapse, financing or margin break.
9. Emit before/after diagnostics and reject if verified mobility volume-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 78
next_round = R10
next_loop = 78
round_schedule_status = valid
round_sector_consistency = pass
```

