# E2R Stock-Web v12 Residual Research — R9 Loop 77 / L3 / C29

## Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R9",
  "scheduled_loop": 77,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R9",
  "completed_loop": 77,
  "computed_next_round": "R10",
  "computed_next_loop": 77,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE",
  "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "mobility_supplier_volume_margin_guardrail",
    "rail_tire_auto_part_bridge_vs_theme_beta",
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

Previous completed state in this interactive run: R8 / loop 77.

Therefore:

```text
scheduled_round = R9
scheduled_loop = 77
allowed_large_sector = L3_BATTERY_EV_GREEN_MOBILITY or L9_CONSTRUCTION_REALESTATE_HOUSING depending on mobility/transport nature
selected_large_sector = L3_BATTERY_EV_GREEN_MOBILITY
selected_canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
computed_next_round = R10
computed_next_loop = 77
```

R9 was routed to mobility/transport rather than construction because R10 is the dedicated construction/PF round.  
This file tests rail mobility, tire mix-margin and auto-parts operating-leverage bridges.

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

This run uses three different symbols and avoids loop-76 R9 names:

```text
064350 / 현대로템 / rail mobility orderbook and margin bridge
161390 / 한국타이어앤테크놀로지 / tire OE/replacement mix-margin fade
010100 / 한국무브넥스 / auto-parts volume/margin theme fade
```

Data-quality note:

```text
All three rows are stock-web calibration usable by profile-level corporate-action candidates.
All three rows are source_proxy_only=true / evidence_url_pending=true.
No selected row has a profile-level 2024 corporate-action candidate inside the selected window.
```

## Research thesis

C29 is not “모빌리티 주가가 올랐다.”

The mechanism must pass through:

```text
customer volume / rail or auto program
→ orderbook, delivery or platform visibility
→ product mix, utilization and pricing
→ margin conversion
→ durable operating leverage
```

모빌리티 주가의 첫 급등은 엔진 시동음이다.  
C29가 보려는 것은 실제 생산 물량, 납기, 믹스, 가동률, 마진이 도로 위로 굴러가는지다.

---

## Case 1 — Positive with lifecycle 4B: 064350 / 현대로템

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

The source-repair task is rail/mobility orderbook, export/customer cadence, delivery slot, utilization and margin bridge evidence.

```text
evidence_family = RAIL_MOBILITY_ORDERBOOK_EXPORT_DELIVERY_SLOT_UTILIZATION_MARGIN_BRIDGE
case_role = positive_with_later_4b_watch
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 28,100
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv`:

```text
2024-02-01,28100,28650,27400,27500
2024-02-22,30900,34500,30350,34500
2024-04-12,41850,43450,40750,41600
2024-06-17,40350,43000,38850,42600
2024-10-18,67400,68000,64600,65000
2024-11-01,61800,62900,60200,61500
```

### Backtest

```text
MFE_30D  = +22.78%
MAE_30D  = -4.09%
MFE_90D  = +54.63%
MAE_90D  = -4.09%
MFE_180D = +141.99%
MAE_180D = -4.09%
peak_180 = 68,000 on 2024-10-18
trough_180 = 26,950 on 2024-02-02
peak_to_later_drawdown = -11.47%
```

### Interpretation

This is the C29 positive-shaped path.  
The price path had large MFE and controlled entry-basis MAE.

Correct treatment:

```text
verified orderbook / delivery slot / utilization / margin bridge → Stage2 possible
bridge stale after peak → lifecycle local 4B-watch
```

---

## Case 2 — Counterexample / local 4B: 161390 / 한국타이어앤테크놀로지

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests tire OE/replacement-cycle beta without enough volume, cost-spread and margin refresh.

```text
evidence_family = TIRE_OE_REPLACEMENT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE_WEAK_REFRESH
case_role = counterexample_tire_mix_margin_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 51,200
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv`:

```text
2024-02-01,51200,52700,50600,52000
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

This is a C29 false-positive boundary.  
The MFE was real, but the later drawdown says the tire mix-margin bridge did not remain durable.

Correct treatment:

```text
tire OE/replacement beta
→ no refreshed volume / mix / cost-spread / margin bridge
→ local 4B-watch
```

---

## Case 3 — Counterexample / local 4B: 010100 / 한국무브넥스

### Evidence status

```text
source_proxy_only = true
evidence_url_pending = true
source_repair_required = true
```

This row tests auto-parts / drivetrain component beta without enough named program, volume and margin evidence.

```text
evidence_family = AUTO_PARTS_DRIVETRAIN_COMPONENT_VOLUME_PROGRAM_MIX_MARGIN_BRIDGE_WEAK
case_role = counterexample_auto_parts_theme_local4b
trigger_date = 2024-01-31
entry_date = 2024-02-01
entry_price = 6,330
```

### Stock-Web price path

Observed rows from `atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv`:

```text
2024-02-01,6330,6700,6310,6430
2024-02-02,6460,7890,6460,7250
2024-04-08,4960,5120,4900,5020
2024-08-05,3985,3990,3200,3445
2024-09-04,3750,3750,3525,3550
2024-10-24,3625,3625,3360,3415
```

### Backtest

```text
MFE_30D  = +24.64%
MAE_30D  = -11.53%
MFE_90D  = +24.64%
MAE_90D  = -24.17%
MFE_180D = +24.64%
MAE_180D = -49.45%
peak_180 = 7,890 on 2024-02-02
trough_180 = 3,200 on 2024-08-05
peak_to_later_drawdown = -59.44%
```

### Interpretation

This is the sharp auto-parts theme-fade row.  
The first spike did not prove operating leverage.

Correct treatment:

```text
auto-parts/drivetrain theme beta
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
```

### What this does not justify

```text
do_not_raise_generic_C29_mobility_theme_weight = true
do_not_treat_all_mobility_MFE_as_Green = true
do_not_convert_mobility_or_auto_parts_drawdown_to_hard_4C_without_non_price_customer_program_or_margin_break = true
```

### Candidate canonical compression

Fine labels can compress into:

```text
RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE
```

This fine archetype covers:

```text
1. rail/mobility orderbook and export delivery bridge → Stage2 possible after source repair
2. tire OE/replacement mix-margin beta without refreshed proof → false Stage2 / local 4B
3. auto-parts/drivetrain beta without customer program bridge → false Stage2 / local 4B
```

---

## Machine-readable rows

### price source validation row

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type": "case", "case_id": "R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "symbol": "064350", "company_name": "현대로템", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable-RailMobilityOrderbookMarginBridgeWithLifecycle4B", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should allow rail/mobility equipment positives when orderbook, delivery slots, export/customer cadence, utilization and margin bridge are visible. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but the move must be lifecycle-managed if orderbook/margin evidence fades.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rail/auto/tire customer volume, orderbook/program visibility, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / TireOEMReplacementMixMarginFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat tire/OE/replacement-cycle beta as durable Stage2 unless OE/replacement volume, product mix, raw-material cost spread and margin bridge refreshes. Hankook Tire had a tradable MFE, then opened a high-MAE drawdown path.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rail/auto/tire customer volume, orderbook/program visibility, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
{"row_type": "case", "case_id": "R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "symbol": "010100", "company_name": "한국무브넥스", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "case_type": "mobility_volume_margin_operating_leverage", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive / AutoPartsVolumeMarginThemeFade", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "score_price_alignment": "C29 should not treat auto-parts or drivetrain component beta as durable Stage2 unless named customer program, volume, mix, pricing and margin bridge are visible. Korea Movenex produced an early spike, then leaked into a high-MAE drawdown.", "current_profile_verdict": "source_repair_required_before_runtime_weight", "price_source": "Songdaiki/stock-web", "notes": "Stock-web path usable; non-proxy rail/auto/tire customer volume, orderbook/program visibility, product mix, utilization, pricing and margin bridge evidence required before runtime promotion."}
```

### trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "case_id": "R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "symbol": "064350", "company_name": "현대로템", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-Actionable-RailMobilityOrderbookMarginBridgeWithLifecycle4B", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 28100.0, "evidence_available_at_that_date": "RAIL_MOBILITY_ORDERBOOK_EXPORT_DELIVERY_SLOT_UTILIZATION_MARGIN_BRIDGE", "evidence_source": "source_proxy_manual_verification_required:HYUNDAI_ROTEM_2024_RAIL_MOBILITY_ORDERBOOK_EXPORT_DELIVERY_UTILIZATION_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_orderbook_candidate", "program_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_export_or_cost_spread_candidate"], "stage4b_evidence_fields": ["mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/064/064350/2024.csv", "profile_path": "atlas/symbol_profiles/064/064350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.78, "MFE_90D_pct": 54.63, "MFE_180D_pct": 141.99, "MAE_30D_pct": -4.09, "MAE_90D_pct": -4.09, "MAE_180D_pct": -4.09, "peak_date": "2024-10-18", "peak_price": 68000.0, "drawdown_after_peak_pct": -11.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "positive_with_later_4b_watch", "current_profile_verdict": "C29 should allow rail/mobility equipment positives when orderbook, delivery slots, export/customer cadence, utilization and margin bridge are visible. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but the move must be lifecycle-managed if orderbook/margin evidence fades.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_064350_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "case_id": "R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / TireOEMReplacementMixMarginFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 51200.0, "evidence_available_at_that_date": "TIRE_OE_REPLACEMENT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE_WEAK_REFRESH", "evidence_source": "source_proxy_manual_verification_required:HANKOOK_TIRE_2024_OE_REPLACEMENT_MIX_RAW_MATERIAL_COST_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_orderbook_candidate", "program_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_export_or_cost_spread_candidate"], "stage4b_evidence_fields": ["mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.41, "MFE_90D_pct": 23.63, "MFE_180D_pct": 23.63, "MAE_30D_pct": -6.35, "MAE_90D_pct": -17.68, "MAE_180D_pct": -30.86, "peak_date": "2024-04-16", "peak_price": 63300.0, "drawdown_after_peak_pct": -44.08, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_tire_mix_margin_local4b", "current_profile_verdict": "C29 should not treat tire/OE/replacement-cycle beta as durable Stage2 unless OE/replacement volume, product mix, raw-material cost spread and margin bridge refreshes. Hankook Tire had a tradable MFE, then opened a high-MAE drawdown path.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_161390_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
{"row_type": "trigger", "trigger_id": "TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "case_id": "R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "symbol": "010100", "company_name": "한국무브넥스", "round": "R9", "loop": "77", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|mobility_supplier_volume_margin_guardrail", "trigger_type": "Stage2-FalsePositive / AutoPartsVolumeMarginThemeFade", "trigger_date": "2024-01-31", "entry_date": "2024-02-01", "entry_price": 6330.0, "evidence_available_at_that_date": "AUTO_PARTS_DRIVETRAIN_COMPONENT_VOLUME_PROGRAM_MIX_MARGIN_BRIDGE_WEAK", "evidence_source": "source_proxy_manual_verification_required:KOREA_MOVENEX_2024_AUTO_PARTS_VOLUME_PROGRAM_MIX_PRICING_MARGIN_BRIDGE", "stage2_evidence_fields": ["customer_volume_or_orderbook_candidate", "program_mix_or_pricing_candidate", "margin_bridge_candidate"], "stage3_evidence_fields": ["relative_strength", "utilization_export_or_cost_spread_candidate"], "stage4b_evidence_fields": ["mobility_theme_beta", "bridge_stale_or_absent", "MAE_widening", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010100/2024.csv", "profile_path": "atlas/symbol_profiles/010/010100.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 24.64, "MFE_90D_pct": 24.64, "MFE_180D_pct": 24.64, "MAE_30D_pct": -11.53, "MAE_90D_pct": -24.17, "MAE_180D_pct": -49.45, "peak_date": "2024-02-02", "peak_price": 7890.0, "drawdown_after_peak_pct": -59.44, "green_lateness_ratio": null, "four_b_local_peak_proximity": "local_4b_watch_after_mobility_peak_if_volume_mix_or_margin_bridge_fades", "four_b_full_window_peak_proximity": "full_4b_requires_non_price_customer_loss_program_delay_volume_pricing_margin_or_financing_break", "trigger_outcome_label": "counterexample_auto_parts_theme_local4b", "current_profile_verdict": "C29 should not treat auto-parts or drivetrain component beta as durable Stage2 unless named customer program, volume, mix, pricing and margin bridge are visible. Korea Movenex produced an early spike, then leaked into a high-MAE drawdown.", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile", "share_count_change_inside_window": false, "same_entry_group_id": "C29_MOBILITY_VOLUME_010100_2024-02-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "source_proxy_only": true, "evidence_url_pending": true}
```

### score simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "trigger_id": "TRG_R9L77-C29-064350-HYUNDAI-ROTEM-RAIL-MOBILITY-ORDERBOOK-MARGIN", "symbol": "064350", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 15, "program_orderbook_score": 15, "mix_pricing_score": 14, "utilization_score": 13, "margin_bridge_score": 14, "relative_strength_score": 15, "execution_risk_score": 8, "source_confidence_score": 2}, "weighted_score_before": 84, "stage_label_before": "Stage2 candidate after source repair", "raw_component_scores_after": {"customer_volume_score": 17, "program_orderbook_score": 17, "mix_pricing_score": 16, "utilization_score": 15, "margin_bridge_score": 16, "relative_strength_score": 14, "execution_risk_score": 9, "source_confidence_score": 2}, "weighted_score_after": 90, "stage_label_after": "Stage2/Yellow-Green after source repair + lifecycle 4B", "changed_components": ["customer_volume_score", "program_orderbook_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rail/auto/tire customer volume, program/orderbook, product mix, utilization, pricing and margin bridge; cap mobility theme beta when evidence fails to refresh.", "MFE_90D_pct": 54.63, "MAE_90D_pct": -4.09, "score_return_alignment_label": "mobility_volume_margin_positive_with_lifecycle_4b", "current_profile_verdict": "C29 should allow rail/mobility equipment positives when orderbook, delivery slots, export/customer cadence, utilization and margin bridge are visible. Hyundai Rotem produced very large MFE with controlled entry-basis MAE, but the move must be lifecycle-managed if orderbook/margin evidence fades."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "trigger_id": "TRG_R9L77-C29-161390-HANKOOK-TIRE-OE-REPLACEMENT-MIX-MARGIN-FADE", "symbol": "161390", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "program_orderbook_score": 4, "mix_pricing_score": 3, "utilization_score": 3, "margin_bridge_score": 2, "relative_strength_score": 6, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "program_orderbook_score": 2, "mix_pricing_score": 1, "utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "program_orderbook_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rail/auto/tire customer volume, program/orderbook, product mix, utilization, pricing and margin bridge; cap mobility theme beta when evidence fails to refresh.", "MFE_90D_pct": 23.63, "MAE_90D_pct": -17.68, "score_return_alignment_label": "false_positive_mobility_theme_bridge_gap", "current_profile_verdict": "C29 should not treat tire/OE/replacement-cycle beta as durable Stage2 unless OE/replacement volume, product mix, raw-material cost spread and margin bridge refreshes. Hankook Tire had a tradable MFE, then opened a high-MAE drawdown path."}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "trigger_id": "TRG_R9L77-C29-010100-KOREA-MOVENEX-AUTO-PARTS-VOLUME-MARGIN-FADE", "symbol": "010100", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"customer_volume_score": 5, "program_orderbook_score": 4, "mix_pricing_score": 3, "utilization_score": 3, "margin_bridge_score": 2, "relative_strength_score": 6, "execution_risk_score": 20, "source_confidence_score": 2}, "weighted_score_before": 50, "stage_label_before": "Stage2-FalsePositive / local 4B-watch", "raw_component_scores_after": {"customer_volume_score": 3, "program_orderbook_score": 2, "mix_pricing_score": 1, "utilization_score": 1, "margin_bridge_score": 1, "relative_strength_score": 3, "execution_risk_score": 23, "source_confidence_score": 2}, "weighted_score_after": 36, "stage_label_after": "Stage4B-local-watch / no durable Green", "changed_components": ["customer_volume_score", "program_orderbook_score", "mix_pricing_score", "utilization_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Reward only verified rail/auto/tire customer volume, program/orderbook, product mix, utilization, pricing and margin bridge; cap mobility theme beta when evidence fails to refresh.", "MFE_90D_pct": 24.64, "MAE_90D_pct": -24.17, "score_return_alignment_label": "false_positive_mobility_theme_bridge_gap", "current_profile_verdict": "C29 should not treat auto-parts or drivetrain component beta as durable Stage2 unless named customer program, volume, mix, pricing and margin bridge are visible. Korea Movenex produced an early spike, then leaked into a high-MAE drawdown."}
```

### aggregate row

```jsonl
{"row_type": "aggregate", "round": "R9", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "RAIL_TIRE_AUTO_PART_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_FADE", "calibration_usable_case_count": 3, "calibration_usable_trigger_count": 3, "new_independent_case_count": 3, "reused_case_count": 0, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "four_b_case_count": 3, "four_c_case_count": 0, "source_proxy_only_count": 3, "evidence_url_pending_count": 3, "share_count_change_inside_window_count": 0, "current_profile_error_count": 2, "diversity_score_summary": "+3 C29 rail/tire/auto-parts symbols outside top-covered 000270/204320/011210/005380/003490 set and outside loop-76 R9 names, +3 rail/tire/auto-parts trigger families, +1 mobility orderbook positive, +2 mobility theme local-4B counterexamples, no hard duplicate", "residual_contribution_label": "coverage_gap_fill_with_source_repair_needed"}
```

### shadow weight row

```jsonl
{"row_type": "shadow_weight", "round": "R9", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "axis": "rail_tire_auto_part_volume_mix_margin_bridge_vs_auto_parts_theme_fade", "decision": "hold_for_source_repair_and_more_evidence", "proposed_runtime_effect": "C29 should split verified rail/mobility/auto supplier operating leverage from generic auto-parts or mobility theme beta. Stage2 requires customer volume, program/orderbook visibility, product mix, utilization, pricing and margin conversion. If MFE fades and MAE/post-peak drawdown opens without bridge refresh, route to local 4B-watch.", "do_not_propose_new_weight_delta": true, "needs_more_evidence": true, "source_repair_required": ["064350", "161390", "010100"]}
```

### residual contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": 77, "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "existing_axis_strengthened": ["stage2_required_bridge", "price_only_blowoff_blocks_positive_stage", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "new_axis_proposed": null, "sector_specific_rule_candidate": true, "canonical_archetype_rule_candidate": true, "narrative_summary": "C29 needs customer volume/program/mix/margin proof. Hyundai Rotem shows a rail/mobility orderbook positive after source repair; Hankook Tire and Korea Movenex show tire/auto-parts theme MFE fading into local 4B when volume, mix and margin bridge are absent or stale."}
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
064350:
  corporate_action_candidate_dates = 2020-08-14
  selected window = 2024-02-01~D+180
  contamination = false

161390:
  corporate_action_candidate_dates = none
  selected window = 2024-02-01~D+180
  contamination = false

010100:
  name = 한국무브넥스 from 2023-04-26, 한국프랜지 before that
  corporate_action_candidate_dates = 1996-12-06, 2002-11-12, 2004-12-02, 2018-05-04
  selected window = 2024-02-01~D+180
  contamination = false
```

Data-quality caveat:

```text
All selected C29 rows are source_proxy_only / evidence_url_pending.
This MD is useful for stock-web path calibration and C29 rule-shape discovery,
but coding-agent promotion requires non-proxy rail/auto/tire customer volume, orderbook/program visibility, product mix, utilization, pricing and margin evidence.
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
rail_tire_auto_part_volume_mix_margin_bridge_vs_auto_parts_theme_fade

Required checks before implementation:
1. Validate all trigger rows against stock-web tradable_raw OHLC shards.
2. Confirm no hard duplicate key:
   canonical_archetype_id + symbol + trigger_type + entry_date.
3. Verify non-proxy source URLs for 064350, 161390 and 010100.
4. Keep generic C29 mobility/auto-parts weight unchanged until source repair is complete.
5. Consider Stage2 only when:
   - customer volume or orderbook/program visibility is explicit,
   - delivery slot, utilization, product mix or pricing bridge exists,
   - margin conversion is visible,
   - MAE remains controlled or the signal is lifecycle-managed.
6. Consider local 4B-watch when:
   - the trigger is mobility, tire or auto-parts theme beta only,
   - customer program/volume/margin evidence is weak or stale,
   - MAE_90D <= -20% or MAE_180D <= -25%,
   - post-peak drawdown <= -35%.
7. Do not convert local 4B-watch into full 4B/4C without non-price customer loss, program delay, order cut, volume decline, pricing/mix collapse, financing or margin break.
8. Emit before/after diagnostics and reject if verified rail/mobility operating-leverage positives are overblocked.
```

---

## Final round state

```text
completed_round = R9
completed_loop = 77
next_round = R10
next_loop = 77
round_schedule_status = valid
round_sector_consistency = pass
```

