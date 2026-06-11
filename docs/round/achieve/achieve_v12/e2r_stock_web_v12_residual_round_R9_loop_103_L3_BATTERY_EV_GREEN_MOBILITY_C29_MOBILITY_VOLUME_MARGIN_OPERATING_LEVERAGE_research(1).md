# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R9
selected_loop: 103
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OEM_PARTS_LOGISTICS_VOLUME_MIX_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_BLOWOFF
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
price_source: Songdaiki/stock-web
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

`C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE` remains a Priority 0 mobility archetype. The current local registry already has `R9/C29` through loop 102, so this run continues as `R9/C29 loop 103`.

This file is a sector-rule formalization pass. It consolidates current-session stock-web-derived C29 rows into one canonical guardrail:

```text
mobility / auto label
→ must become volume, mix, margin, operating leverage, logistics utilization, A/S margin, customer-volume or cash bridge
→ otherwise Stage2 should be capped or blocked
```

Direct uncached stock-web shard fetch has been unstable in recent turns, so this file reuses local rows already generated from `Songdaiki/stock-web` tradable 1D OHLC. Exact trigger rows should be deduped against C29 loops 100~102 during batch ingest. No production scoring is changed.

---

## 1. Research thesis

C29 is not `auto/mobility stock went up`.

It is the operating leverage bridge:

```text
vehicle volume / model mix / ASP / hybrid-EV mix / modules / logistics / A/S / customer order
→ margin, utilization, revision, cash conversion
→ price path validation
```

The loop splits six routes:

1. **OEM volume/mix/margin positive-control**
   - Stage2 remains valid when high-margin mix and shareholder-return/earnings bridge are visible.

2. **Core parts/module/A/S bridge**
   - Supplier Stage2 can open only when module, A/S, margin, and customer-volume bridge is company-specific.

3. **Finished-vehicle logistics bridge**
   - Logistics/shipping operating leverage can work, but should remain 4B if margin or corporate-action boundary risk appears.

4. **ADAS/subsystem supplier high-MFE watch**
   - Vertical MFE is valid only if customer-volume/order/margin bridge refreshes.

5. **Generic auto-parts label**
   - If MFE stays low and MAE deepens, Stage2 must be capped or blocked.

6. **Auto-parts theme blowoff**
   - High MFE followed by deep MAE is local 4B first, then hard block if no durable bridge refresh appears.

---

## 2. Source validation

```yaml
stock_web_manifest:
  source_name: FinanceData/marcap
  price_adjustment_status: raw_unadjusted_marcap
  max_date: 2026-02-20
  calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
  caveat: Raw/unadjusted OHLC; corporate-action contaminated windows blocked by default.
```

Local stock-web-derived row provenance:

```yaml
reused_price_rows_from_current_session:
  - e2r_stock_web_v12_residual_round_R9_loop_100_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R9_loop_101_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
  - e2r_stock_web_v12_residual_round_R9_loop_102_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
  - adjacent R13 high-MAE / 4B-4C guardrail files
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - this file formalizes C29 route-splitting after loops 100~102
  - exact duplicate trigger keys should not be counted again as new aggregate rows
```

Symbol caveats:

```yaml
000270:
  name: 기아
  role: OEM product mix and margin positive-control

012330:
  name: 현대모비스
  role: module/core-parts/A/S margin bridge positive-control

086280:
  name: 현대글로비스
  role: vehicle logistics/shipping margin bridge with 4B watch

204320:
  name: HL만도
  role: subsystem/ADAS supplier bridge with refresh requirement

011210:
  name: 현대위아
  role: parts label low-MFE/high-MAE counterexample

010690:
  name: 화신
  role: auto-parts theme blowoff / 4B-to-block counterexample
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OEM_PRODUCT_MIX_MARGIN_OPERATING_LEVERAGE_POSITIVE_CONTROL","symbol":"000270","name":"기아","trigger_type":"Stage2-Actionable","entry_date":"2024-01-25","entry_close":93000,"price_basis":"tradable_raw","mfe_30d_pct":41.61,"mae_30d_pct":-7.42,"mfe_90d_pct":45.16,"mae_90d_pct":-7.42,"mfe_180d_pct":45.16,"mae_180d_pct":-7.42,"forward_high_30d":131700,"forward_low_30d":86100,"forward_high_90d":135000,"forward_low_90d":86100,"forward_high_180d":135000,"forward_low_180d":86100,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|000270|Stage2-Actionable|2024-01-25","non_price_bridge":"OEM profitability, product mix, ASP, shareholder-return and operating leverage bridge","score_alignment":"keep Stage2-Actionable; allow Stage3-Yellow while margin/mix/revision evidence remains refreshed","aggregate_credit_note":"exact key likely present in C29 loop 102; dedupe during ingest"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"CORE_PARTS_MODULE_AS_MARGIN_BRIDGE_POSITIVE_CONTROL","symbol":"012330","name":"현대모비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_close":241500,"price_basis":"tradable_raw","mfe_30d_pct":10.56,"mae_30d_pct":-2.69,"mfe_90d_pct":11.18,"mae_90d_pct":-2.69,"mfe_180d_pct":19.67,"mae_180d_pct":-3.52,"forward_high_30d":267000,"forward_low_30d":235000,"forward_high_90d":268500,"forward_low_90d":235000,"forward_high_180d":289000,"forward_low_180d":233000,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|012330|Stage2-Actionable|2024-10-16","non_price_bridge":"module/core-parts/A/S profitability and future mobility parts bridge, not pure completed-vehicle beta","score_alignment":"Stage2 can open, but requires company-specific module margin and A/S bridge before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"FINISHED_VEHICLE_LOGISTICS_VOLUME_MARGIN_BRIDGE_WITH_4B_WATCH","symbol":"086280","name":"현대글로비스","trigger_type":"Stage2-Actionable","entry_date":"2024-10-16","entry_close":123900,"price_basis":"tradable_raw","mfe_30d_pct":2.82,"mae_30d_pct":-9.52,"mfe_90d_pct":21.87,"mae_90d_pct":-9.93,"mfe_180d_pct":21.87,"mae_180d_pct":-15.25,"forward_high_30d":127400,"forward_low_30d":112100,"forward_high_90d":151000,"forward_low_90d":111600,"forward_high_180d":151000,"forward_low_180d":105000,"calibration_usable":true,"case_role":"positive_with_local_4B_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|086280|Stage2-Actionable|2024-10-16","non_price_bridge":"finished-vehicle logistics/PCC volume, shipping utilization and margin bridge; not pure OEM rerating","score_alignment":"Stage2 may open; local 4B if logistics margin or corporate-action boundary risk weakens"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"ADAS_SUBSYSTEM_SUPPLIER_HIGH_MFE_MARGIN_REFRESH_REQUIRED","symbol":"204320","name":"HL만도","trigger_type":"Stage2-Actionable","entry_date":"2024-04-29","entry_close":38350,"price_basis":"tradable_raw","mfe_30d_pct":30.38,"mae_30d_pct":-5.48,"mfe_90d_pct":30.38,"mae_90d_pct":-19.56,"mfe_180d_pct":30.38,"mae_180d_pct":-19.56,"forward_high_30d":50000,"forward_low_30d":36250,"forward_high_90d":50000,"forward_low_90d":30850,"forward_high_180d":50000,"forward_low_180d":30850,"calibration_usable":true,"case_role":"supplier_positive_with_watch","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|204320|Stage2-Actionable|2024-04-29","non_price_bridge":"ADAS/steering/brake subsystem supplier leverage, but customer-volume and margin refresh required","score_alignment":"Stage2 may open; block Stage3-Green if order/customer-volume/margin bridge is not refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"GENERIC_PARTS_LABEL_LOW_MFE_HIGH_MAE_STAGE2_BLOCK","symbol":"011210","name":"현대위아","trigger_type":"Stage2-FalsePositive","entry_date":"2024-09-13","entry_close":51600,"price_basis":"tradable_raw","mfe_30d_pct":4.26,"mae_30d_pct":-8.62,"mfe_90d_pct":4.26,"mae_90d_pct":-28.20,"mfe_180d_pct":4.26,"mae_180d_pct":-28.49,"forward_high_30d":53800,"forward_low_30d":47150,"forward_high_90d":53800,"forward_low_90d":37050,"forward_high_180d":53800,"forward_low_180d":36900,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|011210|Stage2-FalsePositive|2024-09-13","non_price_bridge":"engine/module/machine-tool parts label without durable margin, customer-volume, revision or cash bridge","score_alignment":"block Stage2-Actionable when generic parts label has low MFE and high MAE"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R9","loop":103,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_THEME_BLOWOFF_HIGH_MFE_DEEP_MAE_4B_TO_BLOCK","symbol":"010690","name":"화신","trigger_type":"Stage2-Watch","entry_date":"2024-06-12","entry_close":11690,"price_basis":"tradable_raw","mfe_30d_pct":35.93,"mae_30d_pct":-4.53,"mfe_90d_pct":35.93,"mae_90d_pct":-30.28,"mfe_180d_pct":35.93,"mae_180d_pct":-47.39,"forward_high_30d":15890,"forward_low_30d":11160,"forward_high_90d":15890,"forward_low_90d":8150,"forward_high_180d":15890,"forward_low_180d":6150,"calibration_usable":true,"case_role":"vertical_MFE_4B_to_block_counterexample","novelty_key":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE|010690|Stage2-Watch|2024-06-12","non_price_bridge":"auto-parts theme/volume label without durable customer-volume or margin bridge; vertical MFE followed by deep MAE","score_alignment":"route to local 4B first, then block if customer-volume/margin bridge does not refresh"}
```

---

## 4. Case analysis

### 4.1 Kia / 000270 — OEM product-mix positive-control

Kia is the clean C29 positive route. The bridge is not merely mobility vocabulary. The stock path reflects profitability, product mix, ASP, shareholder return and operating leverage.

```yaml
entry_close: 93000
30d_MFE_MAE: +41.61 / -7.42
90d_MFE_MAE: +45.16 / -7.42
180d_MFE_MAE: +45.16 / -7.42
route: Stage2-Actionable positive-control
```

### 4.2 Hyundai Mobis / 012330 — core parts and A/S margin bridge

Mobis is a slower positive-control. It lacks the explosive OEM profile, but MAE stayed controlled and the bridge is company-specific: module, core parts, A/S profitability, and future mobility parts.

```yaml
entry_close: 241500
30d_MFE_MAE: +10.56 / -2.69
90d_MFE_MAE: +11.18 / -2.69
180d_MFE_MAE: +19.67 / -3.52
route: Stage2-Actionable with margin bridge requirement
```

### 4.3 Hyundai Glovis / 086280 — logistics operating leverage with 4B watch

Glovis is not an auto OEM. Its bridge is finished-vehicle logistics, PCC shipping, utilization and margin. The 90D move validates, but the 180D MAE makes it 4B watch.

```yaml
entry_close: 123900
30d_MFE_MAE: +2.82 / -9.52
90d_MFE_MAE: +21.87 / -9.93
180d_MFE_MAE: +21.87 / -15.25
route: Stage2-Actionable with local 4B watch
```

### 4.4 HL Mando / 204320 — subsystem supplier positive, but margin refresh required

HL Mando demonstrates a supplier bridge that can work, but requires customer-volume and order/margin refresh.

```yaml
entry_close: 38350
30d_MFE_MAE: +30.38 / -5.48
90d_MFE_MAE: +30.38 / -19.56
180d_MFE_MAE: +30.38 / -19.56
route: Stage2-Actionable with local watch
```

### 4.5 Hyundai Wia / 011210 — generic parts label false-positive

Wia is the generic-parts counterexample. MFE stayed low while MAE deepened.

```yaml
entry_close: 51600
30d_MFE_MAE: +4.26 / -8.62
90d_MFE_MAE: +4.26 / -28.20
180d_MFE_MAE: +4.26 / -28.49
route: Stage2-FalsePositive
```

### 4.6 Hwashin / 010690 — vertical theme blowoff

Hwashin is the high-MFE trap. The first move is large, but the full route failed without durable customer-volume and margin bridge.

```yaml
entry_close: 11690
30d_MFE_MAE: +35.93 / -4.53
90d_MFE_MAE: +35.93 / -30.28
180d_MFE_MAE: +35.93 / -47.39
route: local 4B -> block if bridge does not refresh
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 0
reused_control_case_count: 6
calibration_usable_case_count: 6
calibration_usable_trigger_count: 6
positive_case_count: 4
counterexample_or_cap_count: 2
local_4B_or_watch_count: 3
current_profile_error_count: 3
duplicate_note: exact C29 novelty keys are likely already represented in loops 100~102; this file should be treated as rule-formalization evidence unless batch ingest finds new keys
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 000270 | OEM positive | +41.61 / -7.42 | +45.16 / -7.42 | +45.16 / -7.42 | product mix and margin bridge validates |
| 012330 | core parts positive | +10.56 / -2.69 | +11.18 / -2.69 | +19.67 / -3.52 | module/A/S margin bridge, not pure OEM beta |
| 086280 | logistics 4B | +2.82 / -9.52 | +21.87 / -9.93 | +21.87 / -15.25 | logistics utilization/margin bridge needs refresh |
| 204320 | supplier watch | +30.38 / -5.48 | +30.38 / -19.56 | +30.38 / -19.56 | subsystem bridge works but needs customer-volume refresh |
| 011210 | hard counterexample | +4.26 / -8.62 | +4.26 / -28.20 | +4.26 / -28.49 | generic parts label fails |
| 010690 | blowoff 4B->block | +35.93 / -4.53 | +35.93 / -30.28 | +35.93 / -47.39 | vertical theme MFE without bridge should not become Green |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"000270","raw_volume_bridge":4,"raw_mix_ASP_bridge":5,"raw_margin_operating_leverage":5,"raw_customer_or_order_bridge":3,"raw_cash_revision_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"012330","raw_volume_bridge":3,"raw_mix_ASP_bridge":2,"raw_margin_operating_leverage":3,"raw_customer_or_order_bridge":3,"raw_cash_revision_bridge":3,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-core-parts-positive"}
{"row_type":"score_simulation","symbol":"086280","raw_volume_bridge":4,"raw_mix_ASP_bridge":1,"raw_margin_operating_leverage":3,"raw_customer_or_order_bridge":4,"raw_cash_revision_bridge":2,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-logistics-4B"}
{"row_type":"score_simulation","symbol":"204320","raw_volume_bridge":3,"raw_mix_ASP_bridge":1,"raw_margin_operating_leverage":3,"raw_customer_or_order_bridge":3,"raw_cash_revision_bridge":2,"raw_validation":3,"raw_label_only_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-supplier-watch"}
{"row_type":"score_simulation","symbol":"011210","raw_volume_bridge":1,"raw_mix_ASP_bridge":0,"raw_margin_operating_leverage":0,"raw_customer_or_order_bridge":1,"raw_cash_revision_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositive-generic-parts-label"}
{"row_type":"score_simulation","symbol":"010690","raw_volume_bridge":1,"raw_mix_ASP_bridge":0,"raw_margin_operating_leverage":1,"raw_customer_or_order_bridge":1,"raw_cash_revision_bridge":0,"raw_validation":1,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Local4B-to-block-theme-blowoff"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C29 can over-credit:

```text
mobility label
auto parts vocabulary
ADAS / EV / future-car theme
short-window vertical MFE
```

The correct bridge is narrower:

```text
volume -> mix/ASP -> margin -> customer-volume/order -> revision/cash
```

A steering part is not automatically operating leverage. A future-car label is not automatically margin. C29 should reward the drivetrain only when torque reaches the wheels.

### Rule candidate

```text
C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIREMENT_V103

if C29
and auto_mobility_or_parts_label == true
and company_specific_volume_mix_margin_customer_order_or_cash_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C29
and OEM_volume_mix_margin_bridge == true
and MFE_90D_pct >= +25
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C29
and parts_supplier_or_logistics_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct <= -10:
    local_4B_watch = true
    block_stage3_green_until_customer_volume_margin_refresh = true
```

```text
if C29
and auto_parts_theme_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C29
and MFE_30D_pct >= +30
and MAE_90D_pct <= -25
and durable_volume_margin_bridge == false:
    route = local_4B_then_block_if_no_refresh
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_formalization_from_existing_controls
new_axis_proposed: C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIREMENT_V103
existing_axis_strengthened:
  - C29_OEM_mix_margin_positive_escape_hatch
  - C29_core_parts_module_AS_margin_bridge
  - C29_logistics_volume_margin_local_4B
  - C29_generic_auto_parts_label_stage2_block
  - C29_vertical_parts_theme_blowoff_4B_to_block
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C29 loop with loops 100~102 and adjacent R13 high-MAE / 4B-4C / Stage2 false-positive guardrails. Extract `C29_VOLUME_MIX_MARGIN_OPERATING_LEVERAGE_REQUIREMENT_V103` as a shadow-rule candidate. Preserve OEM product-mix/margin positives and company-specific parts/logistics bridges, but block generic auto-parts and mobility-theme labels without customer-volume, margin, revision or cash bridge.
```

---

## 10. Next research state

```yaml
completed_round: R9
completed_loop: 103
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
  - C15_MATERIAL_SPREAD_SUPERCYCLE
```
