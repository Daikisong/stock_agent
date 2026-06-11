# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 104
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: MATERIALS_MARGIN_BRIDGE_VS_CHEMICAL_SOLAR_AND_BATTERY_MATERIAL_EVENT_CONTAMINATION
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

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains a Priority 0 archetype. The no-repeat index marks C15 as only `6 rows / need 24 to reach 30`, and prior local C15 files reached loop 103. This run therefore continues as `R4/C15 loop 104`.

This pass focuses on a boundary problem: C15 should not absorb every material-adjacent rally. Some rows belong to C17 chemical spread, C16 strategic resource supply, or battery/material event contamination. The task is to decide when a material price or spread move actually becomes a listed-company ASP/volume/margin bridge.

Direct stock-web file fetch for new raw shards intermittently failed in this turn, so this MD uses previously generated local v12 rows that were already computed from `Songdaiki/stock-web` tradable 1D OHLC. No production scoring is changed.

---

## 1. Research thesis

C15 is not a commodity ticker tape. It is the translation layer:

```text
raw material price / product spread / ASP uplift
→ company-specific inventory, volume, cost pass-through, margin or cash bridge
→ price path validation
```

This loop separates four situations:

1. **Company-specific materials margin bridge**  
   A material name can be a valid C15 positive if the spread improvement reaches margin and price path confirms with contained MAE.

2. **Chemical or solar oversupply masquerading as material spread**  
   If the underlying sector has oversupply, weak demand, or margin compression, a material/chemical label should not open C15 Stage2.

3. **Battery-material or event contamination**  
   A vertical move can be real, but the dominant driver may belong to battery material, policy, or another canonical archetype. C15 contribution should be capped.

4. **Small-cap metal beta without ASP-volume-margin proof**  
   High MFE can be a price flare. Without cash conversion, it must remain local 4B or false-positive block.

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
  - e2r_stock_web_v12_residual_round_R4_loop_137_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
  - e2r_stock_web_v12_residual_round_R4_loop_136_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
  - e2r_stock_web_v12_residual_round_R4_loop_102_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
  - e2r_stock_web_v12_residual_round_R4_loop_103_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
reason:
  - direct web fetch of uncached stock-web shards returned cache misses in this turn
  - local rows already include 30D/90D/180D MFE/MAE from stock-web tradable OHLC
  - rows are reused only as calibration evidence, with duplicate-key avoidance
```

Symbol caveats:

```yaml
002380:
  name: KCC
  role: company-specific materials/silicone/paint margin bridge positive-control
  calibration_usable: true

009830:
  name: 한화솔루션
  role: solar/chemical oversupply counterexample
  calibration_usable: true

011790:
  name: SKC
  role: battery/material event contamination watch
  calibration_usable: true

051910:
  name: LG화학
  role: petrochemical oversupply counterexample
  calibration_usable: true

010950:
  name: S-Oil
  role: refining/product-spread positive-but-not-C15 boundary control
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SILICONE_PAINT_MATERIALS_MARGIN_BRIDGE_POSITIVE_CONTROL","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"calibration_usable":true,"case_role":"positive_control","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"company-specific materials/silicone/paint margin recovery bridge rather than pure commodity beta","score_alignment":"keep Stage2; allow Yellow path when margin/revision/cash bridge refreshes"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SOLAR_CHEMICAL_OVERSUPPLY_MATERIAL_LABEL_STAGE2_BLOCK","symbol":"009830","name":"한화솔루션","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":31800,"price_basis":"tradable_raw","mfe_30d_pct":7.86,"mae_30d_pct":-11.79,"mfe_90d_pct":7.86,"mae_90d_pct":-30.35,"mfe_180d_pct":7.86,"mae_180d_pct":-37.11,"calibration_usable":true,"case_role":"counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|009830|Stage2-Watch|2024-05-20","non_price_bridge":"solar/chemical materials label without ASP-volume-margin recovery; oversupply dominated","score_alignment":"block C15 Stage2-Actionable unless margin/revision bridge is refreshed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"BATTERY_MATERIAL_EVENT_CONTAMINATION_VERTICAL_MFE_LOCAL_4B","symbol":"011790","name":"SKC","trigger_type":"Stage2-Watch","entry_date":"2024-05-23","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":70.94,"mae_30d_pct":0.0,"mfe_90d_pct":70.94,"mae_90d_pct":-8.03,"mfe_180d_pct":70.94,"mae_180d_pct":-20.17,"calibration_usable":true,"case_role":"event_contamination_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|011790|Stage2-Watch|2024-05-23","non_price_bridge":"vertical move likely dominated by battery/material event rather than broad material spread conversion","score_alignment":"cap C15 contribution; reclassify or require product spread/margin proof before Green"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETROCHEM_OVERSUPPLY_MATERIAL_LABEL_FALSE_POSITIVE","symbol":"051910","name":"LG화학","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":391500,"price_basis":"tradable_raw","mfe_30d_pct":2.04,"mae_30d_pct":-10.60,"mfe_90d_pct":2.04,"mae_90d_pct":-32.69,"mfe_180d_pct":2.04,"mae_180d_pct":-46.87,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|051910|Stage2-FalsePositive|2024-05-20","non_price_bridge":"petrochemical/materials label without company-specific spread or margin bridge; oversupply dominated","score_alignment":"hard block for C15 Stage2 bonus when MFE is absent and MAE expands"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":104,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REFINING_PRODUCT_SPREAD_POSITIVE_BOUNDARY_RECLASSIFY_TO_C17","symbol":"010950","name":"S-Oil","trigger_type":"Stage2-Actionable","entry_date":"2024-02-13","entry_close":71500,"price_basis":"tradable_raw","mfe_30d_pct":11.47,"mae_30d_pct":-1.40,"mfe_90d_pct":18.18,"mae_90d_pct":-7.13,"mfe_180d_pct":18.18,"mae_180d_pct":-20.14,"calibration_usable":true,"case_role":"positive_boundary_control","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|010950|Stage2-Actionable|2024-02-13","non_price_bridge":"refining product spread rebound; valid spread economics but better classified as C17 not generic C15","score_alignment":"do not over-credit C15; use as boundary control and reclassify to chemical/refining spread axis"}
```

---

## 4. Case analysis

### 4.1 KCC / 002380 — company-specific materials bridge

KCC is the positive-control. The stock had moderate 90D MFE, stronger 180D MFE, and contained MAE. That is the shape C15 wants.

```yaml
entry_close: 244000
30d_MFE_MAE: +17.62 / -2.46
90d_MFE_MAE: +20.49 / -7.79
180d_MFE_MAE: +41.39 / -7.79
route: Stage2-Actionable
```

The lesson: C15 should preserve Stage2 when material price/spread improvement reaches company-specific margin and price validates without deep drawdown.

---

### 4.2 Hanwha Solutions / 009830 — oversupply defeats the material label

Hanwha Solutions is a counterexample. The label is materials/solar/chemical, but price path rejects a C15 spread bridge.

```yaml
entry_close: 31800
90d_MFE_MAE: +7.86 / -30.35
180d_MFE_MAE: +7.86 / -37.11
route: Stage2-Watch / block Actionable
```

The material signboard was visible, but the warehouse leaked margin through oversupply.

---

### 4.3 SKC / 011790 — vertical MFE, but wrong canonical bridge risk

SKC is the dangerous one. MFE was very high, but the driver may not be broad C15 material-spread conversion. It looks more like a battery/material event axis or non-C15 contamination.

```yaml
entry_close: 117000
90d_MFE_MAE: +70.94 / -8.03
180d_MFE_MAE: +70.94 / -20.17
route: local 4B / reclassification watch
```

C15 should not swallow every high-MFE materials event. It should ask which bridge created the money: product spread, battery capex, policy, or one-off event.

---

### 4.4 LG Chem / 051910 — low MFE, deep MAE hard block

LG Chem is a hard counterexample for generic materials labels.

```yaml
entry_close: 391500
90d_MFE_MAE: +2.04 / -32.69
180d_MFE_MAE: +2.04 / -46.87
route: Stage2-FalsePositive
```

This row says C15 must require visible margin/revision/FCF recovery. A material label alone is not a spread supercycle.

---

### 4.5 S-Oil / 010950 — valid spread economics, but boundary belongs to C17

S-Oil is not a failure. It is a boundary control. Refining spread economics can be real, but the correct canonical home is closer to C17 chemical/refining margin spread, not broad C15 materials supercycle.

```yaml
entry_close: 71500
90d_MFE_MAE: +18.18 / -7.13
180d_MFE_MAE: +18.18 / -20.14
route: positive boundary / reclassify to C17
```

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 5
new_visible_C15_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_or_cap_count: 3
local_4B_or_reclassify_count: 2
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 002380 | positive-control | +17.62 / -2.46 | +20.49 / -7.79 | +41.39 / -7.79 | material margin bridge validates |
| 009830 | counterexample | +7.86 / -11.79 | +7.86 / -30.35 | +7.86 / -37.11 | oversupply defeats material label |
| 011790 | event contamination 4B | +70.94 / 0.00 | +70.94 / -8.03 | +70.94 / -20.17 | high MFE needs canonical reclassification |
| 051910 | hard counterexample | +2.04 / -10.60 | +2.04 / -32.69 | +2.04 / -46.87 | material/petchem label without margin bridge fails |
| 010950 | positive boundary | +11.47 / -1.40 | +18.18 / -7.13 | +18.18 / -20.14 | valid spread but better classified as C17 |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"002380","raw_material_spread_bridge":4,"raw_margin_bridge":4,"raw_volume_or_cash_bridge":3,"raw_validation":4,"raw_oversupply_risk":1,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2-Actionable-positive-control"}
{"row_type":"score_simulation","symbol":"009830","raw_material_spread_bridge":1,"raw_margin_bridge":0,"raw_volume_or_cash_bridge":1,"raw_validation":0,"raw_oversupply_risk":5,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2-Watch-oversupply-block"}
{"row_type":"score_simulation","symbol":"011790","raw_material_spread_bridge":2,"raw_margin_bridge":2,"raw_volume_or_cash_bridge":2,"raw_validation":3,"raw_oversupply_risk":1,"raw_reclassification_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B-reclassification-watch"}
{"row_type":"score_simulation","symbol":"051910","raw_material_spread_bridge":1,"raw_margin_bridge":0,"raw_volume_or_cash_bridge":1,"raw_validation":0,"raw_oversupply_risk":5,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"010950","raw_material_spread_bridge":3,"raw_margin_bridge":3,"raw_volume_or_cash_bridge":3,"raw_validation":3,"raw_oversupply_risk":2,"raw_reclassification_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"BoundaryPositive-ReclassifyC17"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C15 can over-credit:

```text
materials label
+ commodity price rally
+ high short-window MFE
```

The correct test is narrower:

```text
Did the material spread reach the company’s ASP, inventory gain, volume, margin, revision, or FCF?
```

A commodity rally is wind. A spread bridge is a gearbox. The score should not reward wind unless it turns the company’s shaft.

### Rule candidate

```text
C15_COMPANY_SPECIFIC_SPREAD_MARGIN_BRIDGE_REQUIREMENT_V104

if C15
and material_commodity_or_spread_label == true
and company_specific_ASP_volume_margin_inventory_or_FCF_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C15
and oversupply_or_negative_margin_cycle == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C15
and MFE_30D_pct >= +30
and dominant_driver_belongs_to_C16_C17_or_battery_event == true:
    local_4B_watch = true
    cap_C15_contribution = true
    require_reclassification = true
```

```text
if C15
and company_specific_material_margin_bridge == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C15_COMPANY_SPECIFIC_SPREAD_MARGIN_BRIDGE_REQUIREMENT_V104
existing_axis_strengthened:
  - C15_material_label_not_enough_without_margin_bridge
  - C15_oversupply_negative_margin_cycle_stage2_block
  - C15_vertical_MFE_event_contamination_reclassification_guard
  - C15_company_specific_margin_bridge_positive_escape_hatch
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this file with C15 loop 101~103, C16 loop 111~113, C17 loop 136~137, and relevant R13 accounting-trust/high-MAE files. Extract `C15_COMPANY_SPECIFIC_SPREAD_MARGIN_BRIDGE_REQUIREMENT_V104` as a shadow-rule candidate. Preserve company-specific ASP/volume/margin/FCF positive-control cases, block oversupply/negative-margin label cases, and reclassify high-MFE events whose dominant bridge belongs to C16, C17 or battery/event axes.
```

---

## 10. Next research state

```yaml
completed_round: R4
completed_loop: 104
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
  - C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
```
