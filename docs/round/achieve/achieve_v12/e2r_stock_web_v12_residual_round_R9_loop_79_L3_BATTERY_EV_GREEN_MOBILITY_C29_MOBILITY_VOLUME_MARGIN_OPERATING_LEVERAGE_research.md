# E2R Stock-Web v12 Residual Research — R9 Loop 79 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 79,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 79,
  "computed_next_round": "R10",
  "computed_next_loop": 79,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_supplier_volume_margin_guardrail",
    "tire_lamp_body_supplier_volume_mix_margin_bridge",
    "EV_body_parts_theme_fade_boundary",
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

Previous completed state in this interactive run: R8 / loop 79.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 79
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 79
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests tire, auto lamp/module and EV body-parts supplier volume-margin bridges.

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

This run uses three different symbols and avoids loop-78 R9 names:

```text
005850 / 에스엘 / auto lamp/electronics volume-mix-margin bridge
161390 / 한국타이어앤테크놀로지 / tire OE-replacement mix-margin lifecycle
009900 / 명신산업 / EV body-parts theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C29 is not “자동차 부품주가 올랐다.”

The mechanism must pass through:

```text
customer program / mobility demand
→ OE, replacement, module or body-parts volume
→ product mix, utilization or raw-material cost spread
→ pricing and margin conversion
→ durable operating leverage
```

모빌리티 부품주는 조립 라인의 볼트다.  
C29가 보려는 것은 그 볼트가 실제 고객 프로그램, 물량, 믹스, 가동률, 마진으로 조여지는지다.

---

## Case 1 — Positive with lifecycle 4B: 005850 / 에스엘

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is auto lamp/electronics customer volume, product mix, pricing and margin bridge evidence.

```text
evidence_family = AUTO_LAMP_ELECTRONICS_CUSTOMER_VOLUME_PRODUCT_MIX_PRICING_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 32,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv`:

```text
2024-02-01,32200,34550,31900,33750
2024-02-05,37400,37450,34450,36000
2024-04-19,30150,30200,29450,29800
2024-06-17,43350,47650,42800,44200
2024-06-18,44700,46350,43750,45000
2024-08-05,35600,35600,30950,32750
2024-10-25,33000,33250,32500,33150
```

### Backtest

```text
MFE_30D  = +16.30%
MAE_30D  = -3.11%
MFE_90D  = +47.98%
MAE_90D  = -8.54%
MFE_180D = +47.98%
MAE_180D = -8.54%
peak_180 = 47,650 on 2024-06-17
trough_180 = 29,450 on 2024-04-19
peak_to_later_drawdown = -35.05%
```

### Interpretation

This is a C29 auto lamp/module positive.  
The move was not just theme beta; entry-basis drawdown stayed bounded until the operating-leverage MFE arrived.

Correct treatment:

```text
verified customer program / volume / product mix / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Tire lifecycle candidate: 161390 / 한국타이어앤테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is tire OE/replacement volume, product mix, raw-material cost spread, pricing and margin bridge evidence.

```text
evidence_family = TIRE_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_RAW_MATERIAL_COST_SPREAD_MARGIN_BRIDGE
case_role = positive_lifecycle_with_later_high_MAE_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 51,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv`:

```text
2024-02-01,51200,52700,50600,52000
2024-02-05,52600,52600,47950,50000
2024-02-23,59100,59600,57700,58700
2024-04-16,60500,63300,60100,63100
2024-05-07,47200,48400,42150,43750
2024-08-05,42250,42350,37850,38650
2024-10-25,36200,36800,35400,35550
```

### Backtest

```text
MFE_30D  = +16.41%
MAE_30D  = -6.35%
MFE_90D  = +23.63%
MAE_90D  = -17.68%
MFE_180D = +23.63%
MAE_180D = -30.86%
peak_180 = 63,300 on 2024-04-16
trough_180 = 35,400 on 2024-10-25
peak_to_later_drawdown = -44.08%
```

### Interpretation

This is a tire volume/mix lifecycle row.  
It can be a C29 candidate only when OE/replacement volume, mix and cost-spread margin evidence is visible; the later MAE path forces lifecycle 4B discipline.

Correct treatment:

```text
verified tire volume / mix / cost-spread / margin bridge → Stage2-Yellow possible
bridge stale + high MAE after peak → local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 009900 / 명신산업

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests EV body-parts theme beta without enough customer program, volume and margin bridge.

```text
evidence_family = EV_BODY_PARTS_CUSTOMER_VOLUME_THEME_WITH_WEAK_ORDER_MARGIN_BRIDGE
case_role = counterexample_EV_body_parts_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 16,420
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv`:

```text
2024-02-01,16420,16840,16420,16670
2024-02-02,16750,17720,16700,17440
2024-03-07,15500,15540,15120,15160
2024-04-08,14600,14700,14190,14200
2024-08-05,12600,12640,10500,10770
2024-09-04,11000,11190,10730,10730
2024-10-25,12520,13380,12240,12940
```

### Backtest

```text
MFE_30D  = +7.92%
MAE_30D  = -7.92%
MFE_90D  = +7.92%
MAE_90D  = -13.58%
MFE_180D = +7.92%
MAE_180D = -36.05%
peak_180 = 17,720 on 2024-02-02
trough_180 = 10,500 on 2024-08-05
peak_to_later_drawdown = -40.74%
```

### Interpretation

This is a C29 false-positive boundary.  
EV body-parts exposure did not validate durable volume-margin operating leverage.

Correct treatment:

```text
EV/body-parts theme beta
→ no verified customer program / volume / margin bridge
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
do_not_raise_generic_C29_mobility_parts_theme_weight = true
do_not_treat_all_tire_or_auto_parts_MFE_as_Green = true
do_not_convert_mobility_supplier_drawdown_to_hard_4C_without_non_price_customer_program_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE
```

This fine archetype covers:

```text
1. auto lamp/electronics volume-mix-margin bridge → Stage2 possible after source repair
2. tire OE/replacement mix and cost-spread bridge → Stage2-Yellow possible, lifecycle-managed
3. EV body-parts beta without customer volume/margin bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-AutoLampModuleVolumeMixMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow auto lamp/electronics suppliers when customer program volume, product mix, pricing, utilization and margin bridge are visible. SL produced a large MFE with bounded MAE, but the post-peak drawdown requires lifecycle local 4B if volume/mix/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/module volume, product mix, utilization, pricing, raw-material cost spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Lifecycle-TireVolumeMixCostSpreadMarginBridgeWithLocal4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 can preserve tire volume/mix positives when OE/replacement demand, product mix, raw-material cost spread, pricing and margin bridge are visible. Hankook Tire produced meaningful MFE, but later high MAE after the peak means the signal must be lifecycle-managed instead of permanent Green.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/module volume, product mix, utilization, pricing, raw-material cost spread and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE", "symbol": "009900", "company_name": "명신산업", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / EVBodyPartsVolumeMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat EV body/parts beta as durable Stage2 unless customer program, volume, utilization, pricing and margin bridge are visible. Myoung Shin Industrial had a small early MFE and then a severe MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy customer program, OE/replacement/module volume, product mix, utilization, pricing, raw-material cost spread and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE", "case_id": "R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE", "symbol": "005850", "company_name": "에스엘", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Actionable-AutoLampModuleVolumeMixMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 32200.0, "evidence_available_at_that_date": "AUTO_LAMP_ELECTRONICS_CUSTOMER_VOLUME_PRODUCT_MIX_PRICING_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:SL_2024_AUTO_LAMP_ELECTRONICS_CUSTOMER_VOLUME_PRODUCT_MIX_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_pricing_or_cost_spread_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_or_module_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005850/2024.csv", "profile_path": "atlas/symbol_profiles/005/005850.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.3, "MFE_90D_pct": 47.98, "MFE_180D_pct": 47.98, "MAE_30D_pct": -3.11, "MAE_90D_pct": -8.54, "MAE_180D_pct": -8.54, "peak_date": "2024-06-17", "peak_price": 47650.0, "drawdown_after_peak_pct": -35.05, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should allow auto lamp/electronics suppliers when customer program volume, product mix, pricing, utilization and margin bridge are visible. SL produced a large MFE with bounded MAE, but the post-peak drawdown requires lifecycle local 4B if volume/mix/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_005850_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE", "case_id": "R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Lifecycle-TireVolumeMixCostSpreadMarginBridgeWithLocal4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 51200.0, "evidence_available_at_that_date": "TIRE_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_RAW_MATERIAL_COST_SPREAD_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HANKOOK_TIRE_2024_OE_REPLACEMENT_VOLUME_PRODUCT_MIX_COST_SPREAD_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_pricing_or_cost_spread_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_or_module_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.41, "MFE_90D_pct": 23.63, "MFE_180D_pct": 23.63, "MAE_30D_pct": -6.35, "MAE_90D_pct": -17.68, "MAE_180D_pct": -30.86, "peak_date": "2024-04-16", "peak_price": 63300.0, "drawdown_after_peak_pct": -44.08, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_lifecycle_with_later_high_MAE_4b_watch", "current_profile_verdict": "C29 can preserve tire volume/mix positives when OE/replacement demand, product mix, raw-material cost spread, pricing and margin bridge are visible. Hankook Tire produced meaningful MFE, but later high MAE after the peak means the signal must be lifecycle-managed instead of permanent Green.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_161390_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE", "case_id": "R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE", "symbol": "009900", "company_name": "명신산업", "round": "R9", "loop": "79", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / EVBodyPartsVolumeMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 16420.0, "evidence_available_at_that_date": "EV_BODY_PARTS_CUSTOMER_VOLUME_THEME_WITH_WEAK_ORDER_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:MYOUNGSHIN_INDUSTRIAL_2024_EV_BODY_PARTS_CUSTOMER_PROGRAM_VOLUME_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_program_or_volume_candidate", "product_mix_pricing_or_cost_spread_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "OE_replacement_or_module_volume_bridge_candidate"], "stage4b_evidence_fields": ["mobility_parts_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009900/2024.csv", "profile_path": "atlas/symbol_profiles/009/009900.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.92, "MFE_90D_pct": 7.92, "MFE_180D_pct": 7.92, "MAE_30D_pct": -7.92, "MAE_90D_pct": -13.58, "MAE_180D_pct": -36.05, "peak_date": "2024-02-02", "peak_price": 17720.0, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_volume_margin_peak_if_customer_program_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_EV_body_parts_theme_local4b", "current_profile_verdict": "C29 should not treat EV body/parts beta as durable Stage2 unless customer program, volume, utilization, pricing and margin bridge are visible. Myoung Shin Industrial had a small early MFE and then a severe MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_MARGIN_009900_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE", "trigger_id": "TRG_R9L79-C29-005850-SL-AUTO-LAMP-MIX-MARGIN-BRIDGE", "symbol": "005850", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 14, "program_visibility_score": 13, "mix_pricing_score": 13, "utilization_or_cost_spread_score": 12, "margin_bridge_score": 13, "relative_strength_score": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 16, "program_visibility_score": 15, "mix_pricing_score": 15, "utilization_or_cost_spread_score": 14, "margin_bridge_score": 15, "relative_strength_score": 9, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, volume, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 47.98, "MAE_90D_pct": -8.54, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 should allow auto lamp/electronics suppliers when customer program volume, product mix, pricing, utilization and margin bridge are visible. SL produced a large MFE with bounded MAE, but the post-peak drawdown requires lifecycle local 4B if volume/mix/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE", "trigger_id": "TRG_R9L79-C29-161390-HANKOOK-TIRE-MIX-MARGIN-LIFECYCLE", "symbol": "161390", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 14, "program_visibility_score": 13, "mix_pricing_score": 13, "utilization_or_cost_spread_score": 12, "margin_bridge_score": 13, "relative_strength_score": 10, "execution_risk_score": 10, "source_confidence_score": 2}, "weighted_score_before": 76, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 16, "program_visibility_score": 15, "mix_pricing_score": 15, "utilization_or_cost_spread_score": 14, "margin_bridge_score": 15, "relative_strength_score": 9, "execution_risk_score": 11, "source_confidence_score": 2}, "weighted_score_after": 82, "stage_label_after": "Stage2/Yellow after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, volume, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 23.63, "MAE_90D_pct": -17.68, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 can preserve tire volume/mix positives when OE/replacement demand, product mix, raw-material cost spread, pricing and margin bridge are visible. Hankook Tire produced meaningful MFE, but later high MAE after the peak means the signal must be lifecycle-managed instead of permanent Green."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE", "trigger_id": "TRG_R9L79-C29-009900-MYOUNGSHIN-EV-BODY-PARTS-THEME-FADE", "symbol": "009900", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "program_visibility_score": 3, "mix_pricing_score": 2, "utilization_or_cost_spread_score": 2, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 22, "source_confidence_score": 2}, "weighted_score_before": 44, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "program_visibility_score": 1, "mix_pricing_score": 1, "utilization_or_cost_spread_score": 1, "margin_bridge_score": 1, "relative_strength_score": 2, "execution_risk_score": 24, "source_confidence_score": 2}, "weighted_score_after": 33, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "program_visibility_score", "mix_pricing_score", "utilization_or_cost_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified customer program, volume, product mix, utilization/cost spread and margin bridge; cap mobility supplier theme beta when evidence fails to refresh.", "MFE_90D_pct": 7.92, "MAE_90D_pct": -13.58, "score_return_alignment_label": "false_positive_EV_body_parts_bridge_gap", "current_profile_verdict": "C29 should not treat EV body/parts beta as durable Stage2 unless customer program, volume, utilization, pricing and margin bridge are visible. Myoung Shin Industrial had a small early MFE and then a severe MAE drawdown path."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 79, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_AUTO_LAMP_EV_BODY_VOLUME_MIX_MARGIN_BRIDGE_VS_EV_PARTS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 2, "counterexample_count": 1, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 1, "diversity_score_summary": "+3 C29 mobility/tire/lamp/body symbols outside top-covered 000270/204320/011210/005380/003490 set and outside loop-78 R9 names, +3 tire/lamp/body trigger families, +2 volume-mix-margin positives, +1 EV body-parts local-4B counterexample, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 79, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "tire_auto_lamp_EV_body_volume_mix_margin_bridge_vs_EV_parts_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified tire/lamp/mobility supplier volume-margin rerating from generic EV/auto-parts theme beta. Stage2 requires customer program or volume, OE/replacement/module demand, product mix, utilization or cost spread, pricing and margin bridge. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["005850", "161390", "009900"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 79, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs customer program, volume, mix, utilization/cost-spread and margin proof. SL and Hankook Tire show tire/lamp volume-margin candidates after source repair; Myoung Shin Industrial shows EV body-parts beta fading into local 4B when customer volume and margin bridge are absent or stale."}
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
005850:
  name = 에스엘 from 2004-11-15, 삼립산업 before that
  corporate_action_candidate_dates = 2002-07-30, 2003-12-16, 2007-10-22, 2019-04-16
  selected window = 2024-02-01~D+180
  contamination = false

161390:
  name = 한국타이어앤테크놀로지 from 2019-05-22, 한국타이어 before that
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

009900:
  name = 명신산업
  corporate_action_candidate_dates = 2021-06-18
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy customer program, OE/replacement/module volume, product mix, utilization, pricing, raw-material cost spread and margin bridge evidence.
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
tire_auto_lamp_EV_body_volume_mix_margin_bridge_vs_EV_parts_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 005850, 161390 and 009900.
4. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer program or mobility demand is explicit,
   - OE/replacement/module/body-parts volume is visible,
   - product mix, utilization or cost-spread bridge exists,
   - pricing and margin bridge is credible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is tire/auto-parts/EV body-parts theme beta only,
   - customer program/volume/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, program delay, order cut, volume decline, pricing/mix collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified mobility volume-margin positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 79
next_round = R10
next_loop = 79
round_schedule_status = valid
round_sector_consistency = pass
```

