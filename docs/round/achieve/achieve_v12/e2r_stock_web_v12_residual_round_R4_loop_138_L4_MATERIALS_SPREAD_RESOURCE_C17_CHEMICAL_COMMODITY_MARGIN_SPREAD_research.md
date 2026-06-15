# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 138
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: REFINING_PRODUCT_SPREAD_POSITIVE_VS_PETROCHEM_SOLAR_OVERSUPPLY_AND_BATTERY_EVENT_CONTAMINATION
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

`C17_CHEMICAL_COMMODITY_MARGIN_SPREAD` remains Priority 0 in the no-repeat index: 12 rows, still 18 rows short of the 30-row minimum. The visible top-covered set is concentrated in `011780`, `011170`, `004000`, `006650`, `014680`, and `014830`, so this run uses less-covered adjacent symbols and boundary cases.

Prior local C17 files reached `loop 137`, so this run continues as `R4/C17 loop 138`.

Direct stock-web file fetch for uncached shards was unstable in this turn, so this MD reuses already generated stock-web-derived v12 local rows from the current session. Those rows already carry 30D/90D/180D MFE and MAE from `Songdaiki/stock-web` tradable OHLC. No production scoring is changed.

---

## 1. Research thesis

C17 is not “chemical stock” and not “commodity price moved.” It is a company-specific spread bridge:

```text
feedstock / product price / refining or chemical spread
→ ASP, cost pass-through, inventory effect, utilization, margin and FCF
→ price path validation
```

This loop separates five routes.

1. **Refining product spread positive-control**  
   Spread economics can work when the company has a clear product-spread / inventory / margin channel.

2. **Petrochemical oversupply hard block**  
   A chemical label does not matter if oversupply and weak downstream demand prevent margin recovery.

3. **Solar/chemical hybrid oversupply block**  
   Material/solar/chemical labels can create hope, but not C17 Stage2 unless spread and margin bridge are visible.

4. **Materials margin bridge reclassification**  
   Some positive materials cases are real, but belong in C15 rather than C17.

5. **Battery/material event contamination**  
   High MFE can occur, but if the dominant bridge is battery-material event or capex narrative, C17 contribution should be capped.

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
  - C15_MATERIAL_SPREAD_SUPERCYCLE loop 104
  - C16_STRATEGIC_RESOURCE_POLICY_SUPPLY loop 114
  - prior local C17 boundary rows
reason:
  - uncached stock-web shard fetch intermittently failed in this turn
  - reused rows were already computed from stock-web tradable raw 1D OHLC
  - rows are reused only as C17 boundary and residual evidence
```

Symbol caveats:

```yaml
010950:
  name: S-Oil
  role: refining/product spread positive boundary
  calibration_usable: true

051910:
  name: LG화학
  role: petrochemical/materials oversupply counterexample
  calibration_usable: true

009830:
  name: 한화솔루션
  role: solar/chemical oversupply counterexample
  calibration_usable: true

002380:
  name: KCC
  role: materials margin bridge; valid positive but better C15 boundary
  calibration_usable: true

011790:
  name: SKC
  role: battery/material event contamination
  calibration_usable: true
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":138,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"REFINING_PRODUCT_SPREAD_MARGIN_POSITIVE_WITH_180D_4B_WATCH","symbol":"010950","name":"S-Oil","trigger_type":"Stage2-Actionable","entry_date":"2024-02-13","entry_close":71500,"price_basis":"tradable_raw","mfe_30d_pct":11.47,"mae_30d_pct":-1.40,"mfe_90d_pct":18.18,"mae_90d_pct":-7.13,"mfe_180d_pct":18.18,"mae_180d_pct":-20.14,"forward_high_30d":79700,"forward_low_30d":70500,"forward_high_90d":84500,"forward_low_90d":66400,"forward_high_180d":84500,"forward_low_180d":57100,"calibration_usable":true,"case_role":"positive_boundary_control","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|010950|Stage2-Actionable|2024-02-13","non_price_bridge":"refining/product spread rebound with clear margin transmission, but 180D drawdown requires local 4B watch","score_alignment":"keep Stage2; block Green unless spread/margin/FCF bridge refreshes"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":138,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"PETROCHEM_OVERSUPPLY_LOW_MFE_DEEP_MAE_STAGE2_BLOCK","symbol":"051910","name":"LG화학","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":391500,"price_basis":"tradable_raw","mfe_30d_pct":2.04,"mae_30d_pct":-10.60,"mfe_90d_pct":2.04,"mae_90d_pct":-32.69,"mfe_180d_pct":2.04,"mae_180d_pct":-46.87,"forward_high_30d":399500,"forward_low_30d":350000,"forward_high_90d":399500,"forward_low_90d":263500,"forward_high_180d":399500,"forward_low_180d":208000,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|051910|Stage2-FalsePositive|2024-05-20","non_price_bridge":"petrochemical and battery-material label without actual spread/margin recovery; oversupply and cycle pressure dominated","score_alignment":"hard block C17 Stage2 bonus when MFE is absent and MAE expands"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":138,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SOLAR_CHEMICAL_OVERSUPPLY_MARGIN_BRIDGE_MISSING_STAGE2_CAP","symbol":"009830","name":"한화솔루션","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":31800,"price_basis":"tradable_raw","mfe_30d_pct":7.86,"mae_30d_pct":-11.79,"mfe_90d_pct":7.86,"mae_90d_pct":-30.35,"mfe_180d_pct":7.86,"mae_180d_pct":-37.11,"forward_high_30d":34300,"forward_low_30d":28050,"forward_high_90d":34300,"forward_low_90d":22150,"forward_high_180d":34300,"forward_low_180d":20000,"calibration_usable":true,"case_role":"oversupply_counterexample","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|009830|Stage2-Watch|2024-05-20","non_price_bridge":"solar/chemical oversupply prevented product spread and OPM bridge from forming","score_alignment":"cap Stage2; require ASP/utilization/spread margin recovery before Actionable"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":138,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"MATERIALS_MARGIN_BRIDGE_REAL_BUT_RECLASSIFY_TO_C15","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"positive_reclassification_control","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"materials/silicone/paint margin bridge is valid but belongs more cleanly to C15 than C17","score_alignment":"do not over-credit C17; reclassify to C15 if chemical commodity spread is not dominant"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":138,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BATTERY_MATERIAL_EVENT_CONTAMINATION_HIGH_MFE_C17_CONTRIBUTION_CAP","symbol":"011790","name":"SKC","trigger_type":"Stage2-Watch","entry_date":"2024-05-23","entry_close":117000,"price_basis":"tradable_raw","mfe_30d_pct":70.94,"mae_30d_pct":0.00,"mfe_90d_pct":70.94,"mae_90d_pct":-8.03,"mfe_180d_pct":70.94,"mae_180d_pct":-20.17,"forward_high_30d":200000,"forward_low_30d":117000,"forward_high_90d":200000,"forward_low_90d":107600,"forward_high_180d":200000,"forward_low_180d":93400,"calibration_usable":true,"case_role":"event_contamination_local_4B","novelty_key":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD|011790|Stage2-Watch|2024-05-23","non_price_bridge":"vertical MFE likely dominated by battery/material event rather than chemical commodity spread margin conversion","score_alignment":"cap C17 contribution; require reclassification or product-spread margin proof before Green"}
```

---

## 4. Case analysis

### 4.1 S-Oil / 010950 — refining spread positive, but 180D 4B watch

S-Oil is the cleanest positive-control in this loop. It has an actual product-spread and refining-margin mechanism, not just a chemical label.

```yaml
entry_close: 71500
30d_MFE_MAE: +11.47 / -1.40
90d_MFE_MAE: +18.18 / -7.13
180d_MFE_MAE: +18.18 / -20.14
route: Stage2-Actionable with 180D local 4B watch
```

The bridge worked initially. But 180D MAE crossed -20%, so Green requires a refreshed spread/margin/FCF bridge.

---

### 4.2 LG Chem / 051910 — hard block for petrochemical oversupply

LG Chem is the hard C17 counterexample.

```yaml
entry_close: 391500
30d_MFE_MAE: +2.04 / -10.60
90d_MFE_MAE: +2.04 / -32.69
180d_MFE_MAE: +2.04 / -46.87
route: Stage2-FalsePositive
```

The name has chemical/material exposure, but the spread did not translate into margin recovery. Oversupply and cycle pressure dominated.

---

### 4.3 Hanwha Solutions / 009830 — solar/chemical oversupply cap

Hanwha Solutions is another oversupply case. It did slightly better than LG Chem on MFE, but still failed the margin bridge test.

```yaml
entry_close: 31800
30d_MFE_MAE: +7.86 / -11.79
90d_MFE_MAE: +7.86 / -30.35
180d_MFE_MAE: +7.86 / -37.11
route: Stage2-Watch / cap Actionable
```

A product label is not enough if utilization, ASP and OPM remain under pressure.

---

### 4.4 KCC / 002380 — real positive, but not the dominant C17 bridge

KCC is not a false positive. It is a reclassification control. The margin bridge was real, but the cleaner archetype is C15 materials margin rather than C17 chemical commodity spread.

```yaml
entry_close: 244000
90d_MFE_MAE: +20.49 / -7.79
180d_MFE_MAE: +41.39 / -7.79
route: positive but reclassify to C15
```

---

### 4.5 SKC / 011790 — high-MFE event contamination

SKC is the high-MFE trap. It produced a huge move, but C17 must not automatically absorb it as chemical spread improvement.

```yaml
entry_close: 117000
30d_MFE_MAE: +70.94 / 0.00
90d_MFE_MAE: +70.94 / -8.03
180d_MFE_MAE: +70.94 / -20.17
route: local 4B / event-contamination cap
```

The bridge may belong to battery-material event logic, not broad chemical commodity margin spread.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 5
new_visible_C17_symbol_count: 5
same_archetype_new_trigger_family_count: 5
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_or_cap_count: 3
local_4B_or_reclassification_count: 3
current_profile_error_count: 3
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 010950 | refining positive + 4B | +11.47 / -1.40 | +18.18 / -7.13 | +18.18 / -20.14 | real refining spread, but Green needs refresh |
| 051910 | hard counterexample | +2.04 / -10.60 | +2.04 / -32.69 | +2.04 / -46.87 | chemical label without spread recovery fails |
| 009830 | oversupply cap | +7.86 / -11.79 | +7.86 / -30.35 | +7.86 / -37.11 | solar/chemical oversupply blocks C17 Stage2 |
| 002380 | reclassify positive | +17.62 / -2.46 | +20.49 / -7.79 | +41.39 / -7.79 | real margin bridge, cleaner C15 |
| 011790 | event contamination | +70.94 / 0.00 | +70.94 / -8.03 | +70.94 / -20.17 | high MFE may belong to battery/material event |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"010950","raw_feedstock_product_spread_bridge":4,"raw_margin_FCF_bridge":3,"raw_utilization_ASP_bridge":3,"raw_validation":3,"raw_oversupply_risk":1,"raw_reclassification_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2Actionable_RefiningSpread_4BWatch"}
{"row_type":"score_simulation","symbol":"051910","raw_feedstock_product_spread_bridge":1,"raw_margin_FCF_bridge":0,"raw_utilization_ASP_bridge":1,"raw_validation":0,"raw_oversupply_risk":5,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositive_PetrochemOversupply"}
{"row_type":"score_simulation","symbol":"009830","raw_feedstock_product_spread_bridge":1,"raw_margin_FCF_bridge":0,"raw_utilization_ASP_bridge":1,"raw_validation":0,"raw_oversupply_risk":5,"raw_reclassification_risk":2,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2Watch_SolarChemicalOversupplyCap"}
{"row_type":"score_simulation","symbol":"002380","raw_feedstock_product_spread_bridge":2,"raw_margin_FCF_bridge":4,"raw_utilization_ASP_bridge":3,"raw_validation":4,"raw_oversupply_risk":1,"raw_reclassification_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Positive_ReclassifyC15"}
{"row_type":"score_simulation","symbol":"011790","raw_feedstock_product_spread_bridge":2,"raw_margin_FCF_bridge":2,"raw_utilization_ASP_bridge":2,"raw_validation":3,"raw_oversupply_risk":1,"raw_reclassification_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_EventContamination"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C17 can over-credit:

```text
chemical stock
+ material/commodity rally
+ high short-window MFE
```

This is too broad. A chemical spread is not the same thing as a commodity price. It is the distance between feedstock cost and product ASP, multiplied through utilization and margin.

The score should ask:

```text
Did the spread enter ASP, utilization, OPM, inventory gain, revision or FCF?
```

If not, the label is only a weather report. The company needs a working refinery or chemical plant gearbox for the wind to become torque.

### Rule candidate

```text
C17_PRODUCT_SPREAD_MARGIN_FCF_BRIDGE_REQUIREMENT_V138

if C17
and chemical_commodity_or_refining_label == true
and company_specific_product_spread_margin_FCF_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C17
and oversupply_or_utilization_downcycle == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C17
and refining_or_product_spread_bridge == true
and MFE_90D_pct >= +15
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C17
and MFE_30D_pct >= +30
and dominant_driver_belongs_to_C15_C16_battery_or_policy_event == true:
    local_4B_watch = true
    cap_C17_contribution = true
    require_reclassification = true
```

```text
if C17
and MFE_90D_pct >= +15
and MAE_180D_pct <= -20
and refreshed_spread_margin_FCF_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C17_PRODUCT_SPREAD_MARGIN_FCF_BRIDGE_REQUIREMENT_V138
existing_axis_strengthened:
  - C17_chemical_label_not_enough_without_product_spread_bridge
  - C17_oversupply_utilization_downcycle_stage2_block
  - C17_refining_product_spread_positive_escape_hatch
  - C17_high_MFE_event_contamination_reclassification_guard
  - C17_180D_drawdown_local_4B_until_margin_refresh
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C17 loop with C15 loop 104, C16 loop 114, prior C17 loops 136~137, and R13 accounting-trust/high-MAE files. Extract `C17_PRODUCT_SPREAD_MARGIN_FCF_BRIDGE_REQUIREMENT_V138` as a shadow-rule candidate. Preserve refining/product-spread positive controls, block oversupply/utilization-downcycle cases, and reclassify high-MFE rows whose dominant driver belongs to C15, C16, battery-material event, or policy axes.
```

---

## 10. Next research state

```yaml
completed_round: R4
completed_loop: 138
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
  - C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
  - R13_CROSS_ARCHETYPE_ACCOUNTING_TRUST_PRICE_VALIDATION
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C24_BIO_TRIAL_DATA_EVENT_RISK
```
