# E2R v12 residual calibration research

## 0. Execution metadata

```yaml
schema_family: v12_sector_archetype_residual
selected_round: R4
selected_loop: 105
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: ALUMINIUM_BATTERY_FOIL_AND_CHEMICAL_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_VS_PRICE_SPIKE_DECAY
selection_basis:
  main_execution_prompt: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
  no_repeat_index: docs/core/V12_Research_No_Repeat_Index.md
web_raw_fetch_status_this_turn:
  main_execution_prompt: read_ok
  no_repeat_index: read_ok
  stock_web_manifest: read_ok
  uncached_symbol_shards: cache_miss_observed
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

`C15_MATERIAL_SPREAD_SUPERCYCLE` remains Priority 0 in the no-repeat index: 6 representative rows, still 24 rows short of the 30-row minimum. The v12 scheduler maps C15~C17 to `R4 / L4_MATERIALS_SPREAD_RESOURCE`. Prior local C15 sector files reached `R4/C15 loop 104`, so this continuation is `R4/C15 loop 105`.

This is not a live material-stock screen. It is a historical residual calibration file. Direct uncached `stock-web` symbol shards returned cache misses in this turn, so this MD uses stock-web-derived rows already calculated in the current v12 session from C16/C17/R13 material-boundary files. Exact source rows should be deduped against their original archetypes; this file changes the canonical scope to C15 and uses them to formalize a material-spread bridge rule. No production scoring is changed.

---

## 1. Research thesis

C15 is not `material stock + commodity rally = supercycle`.

It is the company-specific conversion bridge:

```text
raw material / metal / chemical / battery-foil spread
→ ASP, inventory gain, volume, utilization, margin, revision, FCF
→ price path validation
```

The recurring C15 failure mode is that high MFE appears first, then the company never proves the actual margin bridge. That price shape tempts the model to call a material label a supercycle, but the later MAE says the company never turned the commodity wind into torque.

This loop separates five routes:

1. **Company-specific material margin positive-control**
   - Stage2 can remain open when ASP/mix/margin/FCF bridge validates with controlled drawdown.

2. **Aluminum battery-foil high-MFE / high-MAE**
   - A vertical move may be tradable.
   - Without utilization, order, ASP/margin or cash refresh, route to local 4B and block Green.

3. **Aluminum rolling commodity beta low-MFE / high-MAE**
   - If MFE stays low and MAE expands, block Stage2-Actionable.

4. **Petrochemical/PP chemical label with balance-sheet/margin decay**
   - A chemical label does not equal product-spread recovery.
   - Low MFE and severe MAE should hard block C15.

5. **Strategic processing / dual-use material control**
   - Processing/offtake can preserve Stage2, but high MAE still requires margin/order refresh.

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
  - R4/C16 loop 112: aluminium foil and aluminium rolling material rows
  - R4/C17 loop 136: petrochemical/chemical margin counterexample row
  - R4/C15 loop 104: KCC material-margin positive-control row
  - R4/C16 loop 113/114 and R13 high-MAE files: Poongsan dual-use processing control
reason:
  - rows were already calculated from Songdaiki/stock-web tradable raw 1D OHLC
  - current file changes canonical scope to C15 and formalizes C15 material-spread conversion logic
  - exact source-archetype keys should be deduped separately from this C15 key
  - no production scoring changed
```

Symbol caveats:

```yaml
002380:
  name: KCC
  role: reused company-specific material/silicone/paint margin positive-control
  calibration_usable: true
  aggregate_credit_note: exact key likely appears in C15 loop 104; use as control if deduped

006110:
  name: 삼아알미늄
  role: aluminium battery-foil material label high-MFE/high-MAE local 4B
  calibration_usable: true

018470:
  name: 조일알미늄
  role: aluminium rolling commodity beta low-MFE/high-MAE false positive
  calibration_usable: true

298000:
  name: 효성화학
  role: chemical/PP material label with margin/balance-sheet decay
  calibration_usable: true

103140:
  name: 풍산
  role: reused dual-use copper/non-ferrous processing positive with high-MAE watch
  calibration_usable: true
  aggregate_credit_note: prior C15/C16/R13 control; use as control if deduped
```

---

## 3. Trigger rows

```jsonl
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COMPANY_SPECIFIC_SILICONE_PAINT_MATERIAL_MARGIN_POSITIVE_CONTROL","source_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","symbol":"002380","name":"KCC","trigger_type":"Stage2-Actionable","entry_date":"2024-01-30","entry_close":244000,"price_basis":"tradable_raw","mfe_30d_pct":17.62,"mae_30d_pct":-2.46,"mfe_90d_pct":20.49,"mae_90d_pct":-7.79,"mfe_180d_pct":41.39,"mae_180d_pct":-7.79,"forward_high_30d":287000,"forward_low_30d":238000,"forward_high_90d":294000,"forward_low_90d":225000,"forward_high_180d":345000,"forward_low_180d":225000,"calibration_usable":true,"case_role":"reused_positive_control","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|002380|Stage2-Actionable|2024-01-30","non_price_bridge":"company-specific materials/silicone/paint margin recovery bridge rather than generic commodity beta","score_alignment":"keep Stage2; allow Yellow path when margin/revision/FCF bridge remains refreshed","aggregate_credit_note":"exact key likely present in C15 loop 104; use as positive-control if deduped"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_BATTERY_FOIL_LABEL_HIGH_MFE_HIGH_MAE_LOCAL_4B","source_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"006110","name":"삼아알미늄","trigger_type":"Stage2-Watch","entry_date":"2024-05-20","entry_close":75500,"price_basis":"tradable_raw","mfe_30d_pct":28.34,"mae_30d_pct":-7.28,"mfe_90d_pct":28.34,"mae_90d_pct":-47.55,"mfe_180d_pct":28.34,"mae_180d_pct":-53.58,"forward_high_30d":96900,"forward_low_30d":70000,"forward_high_90d":96900,"forward_low_90d":39600,"forward_high_180d":96900,"forward_low_180d":35050,"calibration_usable":true,"case_role":"high_MFE_high_MAE_local_4B","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|006110|Stage2-Watch|2024-05-20","non_price_bridge":"aluminium battery-foil material label without refreshed customer order, utilization, ASP/margin or cash bridge","score_alignment":"local 4B only; block Stage3-Green until order/utilization/margin bridge refresh"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"ALUMINIUM_ROLLING_COMMODITY_BETA_LOW_MFE_HIGH_MAE_FALSE_POSITIVE","source_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"018470","name":"조일알미늄","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":2470,"price_basis":"tradable_raw","mfe_30d_pct":7.29,"mae_30d_pct":-17.41,"mfe_90d_pct":7.29,"mae_90d_pct":-41.30,"mfe_180d_pct":7.29,"mae_180d_pct":-44.70,"forward_high_30d":2650,"forward_low_30d":2040,"forward_high_90d":2650,"forward_low_90d":1450,"forward_high_180d":2650,"forward_low_180d":1366,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|018470|Stage2-FalsePositive|2024-05-20","non_price_bridge":"aluminium rolling commodity beta label without company-specific ASP, volume, margin or FCF bridge","score_alignment":"block Stage2-Actionable; low MFE and high MAE reject C15 material-spread bridge"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"PETROCHEM_PP_MATERIAL_LABEL_WITH_MARGIN_BALANCE_SHEET_DECAY_HARD_BLOCK","source_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","symbol":"298000","name":"효성화학","trigger_type":"Stage2-FalsePositive","entry_date":"2024-05-20","entry_close":71000,"price_basis":"tradable_raw","mfe_30d_pct":1.41,"mae_30d_pct":-16.20,"mfe_90d_pct":9.01,"mae_90d_pct":-22.39,"mfe_180d_pct":9.01,"mae_180d_pct":-60.35,"forward_high_30d":72000,"forward_low_30d":59500,"forward_high_90d":77400,"forward_low_90d":55100,"forward_high_180d":77400,"forward_low_180d":28150,"calibration_usable":true,"case_role":"hard_counterexample","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|298000|Stage2-FalsePositive|2024-05-20","non_price_bridge":"petrochemical/PP material label without visible product-spread, margin repair, FCF or balance-sheet bridge","score_alignment":"hard block C15 Stage2; severe 180D MAE shows material label failed"}
{"row_type":"trigger","schema_family":"v12_sector_archetype_residual","round":"R4","loop":105,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"DUAL_USE_COPPER_PROCESSING_MATERIAL_BRIDGE_HIGH_MAE_WATCH","source_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","symbol":"103140","name":"풍산","trigger_type":"Stage2-Actionable","entry_date":"2024-04-26","entry_close":62900,"price_basis":"tradable_raw","mfe_30d_pct":25.44,"mae_30d_pct":-10.17,"mfe_90d_pct":25.44,"mae_90d_pct":-25.28,"mfe_180d_pct":25.44,"mae_180d_pct":-26.63,"forward_high_30d":78900,"forward_low_30d":56500,"forward_high_90d":78900,"forward_low_90d":47000,"forward_high_180d":78900,"forward_low_180d":46150,"calibration_usable":true,"case_role":"reused_positive_with_local_4B_watch","novelty_key":"C15_MATERIAL_SPREAD_SUPERCYCLE|103140|Stage2-Actionable|2024-04-26","non_price_bridge":"actual copper/non-ferrous processing plus defense dual-use material demand; high MAE requires order/margin refresh","score_alignment":"Stage2 may open; block Green until processing margin, order and cash bridge refresh","aggregate_credit_note":"may already appear in prior C15/C16 controls; dedupe if represented"}
```

---

## 4. Case analysis

### 4.1 KCC / 002380 — company-specific margin bridge positive-control

KCC remains the control for what C15 should keep. The bridge is not generic commodity beta; it is material/silicone/paint margin conversion.

```yaml
entry_close: 244000
30D_MFE_MAE: +17.62 / -2.46
90D_MFE_MAE: +20.49 / -7.79
180D_MFE_MAE: +41.39 / -7.79
route: KeepStage2
```

### 4.2 Sam-A Aluminium / 006110 — high-MFE aluminium foil trap

This row is dangerous because the early MFE is strong enough to look like a materials supercycle. But the later path failed.

```yaml
entry_close: 75500
30D_MFE_MAE: +28.34 / -7.28
90D_MFE_MAE: +28.34 / -47.55
180D_MFE_MAE: +28.34 / -53.58
route: Local4B_BlockGreen
```

C15 should treat this as local 4B only unless order, utilization, ASP/margin and cash bridge refresh.

### 4.3 Choil Aluminium / 018470 — commodity label false positive

Choil shows the cleaner false-positive shape: low MFE and deep MAE.

```yaml
entry_close: 2470
30D_MFE_MAE: +7.29 / -17.41
90D_MFE_MAE: +7.29 / -41.30
180D_MFE_MAE: +7.29 / -44.70
route: Stage2FalsePositiveBlock
```

The commodity label did not convert into a company-level margin bridge.

### 4.4 Hyosung Chemical / 298000 — material/chemical label with balance-sheet decay

Hyosung Chemical blocks the broader mistake of treating petrochemical vocabulary as spread repair.

```yaml
entry_close: 71000
30D_MFE_MAE: +1.41 / -16.20
90D_MFE_MAE: +9.01 / -22.39
180D_MFE_MAE: +9.01 / -60.35
route: Stage2FalsePositiveBlock
```

Severe 180D MAE makes this a hard C15 counterexample unless new margin/FCF/balance-sheet repair evidence appears.

### 4.5 Poongsan / 103140 — processing bridge survives, but needs 4B watch

Poongsan keeps the model from blocking all metals cases. It has real copper/non-ferrous processing and dual-use demand relevance.

```yaml
entry_close: 62900
30D_MFE_MAE: +25.44 / -10.17
90D_MFE_MAE: +25.44 / -25.28
180D_MFE_MAE: +25.44 / -26.63
route: Stage2_with_local_4B
```

The bridge is real, but the drawdown means Green waits for order/margin/cash refresh.

---

## 5. Score-return alignment

```yaml
new_independent_case_count: 3
reused_control_case_count: 2
calibration_usable_case_count: 5
calibration_usable_trigger_count: 5
positive_case_count: 2
counterexample_or_cap_count: 3
local_4B_watch_count: 2
current_profile_error_count: 4
duplicate_note: exact source rows may already exist under C16/C17/R13, but C15 canonical keys for 006110, 018470 and 298000 are new in this local sequence
```

| symbol | role | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | lesson |
|---|---:|---:|---:|---:|---|
| 002380 | positive-control | +17.62 / -2.46 | +20.49 / -7.79 | +41.39 / -7.79 | company margin bridge validates |
| 006110 | high-MFE local 4B | +28.34 / -7.28 | +28.34 / -47.55 | +28.34 / -53.58 | battery-foil label needs utilization/margin refresh |
| 018470 | hard false positive | +7.29 / -17.41 | +7.29 / -41.30 | +7.29 / -44.70 | aluminium beta without margin bridge fails |
| 298000 | hard false positive | +1.41 / -16.20 | +9.01 / -22.39 | +9.01 / -60.35 | chemical material label without repair fails |
| 103140 | positive + 4B | +25.44 / -10.17 | +25.44 / -25.28 | +25.44 / -26.63 | real processing bridge still needs refresh |

---

## 6. Raw component score breakdown

```jsonl
{"row_type":"score_simulation","symbol":"002380","raw_material_label":3,"raw_company_specific_ASP_margin_bridge":5,"raw_inventory_volume_bridge":3,"raw_FCF_revision_bridge":4,"raw_validation":4,"raw_label_only_risk":0,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"KeepStage2_MaterialMarginBridge"}
{"row_type":"score_simulation","symbol":"006110","raw_material_label":4,"raw_company_specific_ASP_margin_bridge":1,"raw_inventory_volume_bridge":1,"raw_FCF_revision_bridge":0,"raw_validation":1,"raw_label_only_risk":4,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":1.0,"simulated_route":"Local4B_BlockGreen"}
{"row_type":"score_simulation","symbol":"018470","raw_material_label":4,"raw_company_specific_ASP_margin_bridge":0,"raw_inventory_volume_bridge":0,"raw_FCF_revision_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"298000","raw_material_label":3,"raw_company_specific_ASP_margin_bridge":0,"raw_inventory_volume_bridge":0,"raw_FCF_revision_bridge":0,"raw_validation":0,"raw_label_only_risk":5,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":0.0,"simulated_route":"Stage2FalsePositiveBlock"}
{"row_type":"score_simulation","symbol":"103140","raw_material_label":3,"raw_company_specific_ASP_margin_bridge":3,"raw_inventory_volume_bridge":3,"raw_FCF_revision_bridge":2,"raw_validation":3,"raw_label_only_risk":1,"stage2_actionable_bonus_before":2.0,"stage2_actionable_bonus_after":2.0,"simulated_route":"Stage2WithLocal4B"}
```

---

## 7. Current calibrated profile stress test

### Existing error risk

C15 can over-credit:

```text
aluminium / copper / chemical / battery-foil label
+ early MFE
```

But a material label is only ore in the ground. The model should ask whether the company has the furnace, customer order, pricing power and cash register.

Correct C15 scoring:

```text
material label -> ASP / volume / utilization / margin / FCF bridge -> price validation
```

### Rule candidate

```text
C15_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_REQUIREMENT_V105

if C15
and material_metal_chemical_or_battery_foil_label == true
and company_specific_ASP_volume_utilization_margin_or_FCF_bridge == false:
    stage2_actionable_bonus = 0
    max_stage = Stage2-Watch
```

```text
if C15
and company_specific_material_margin_bridge == true
and MFE_90D_pct >= +20
and MAE_90D_pct > -10:
    keep_stage2_actionable_bonus = true
    allow_stage3_yellow_path = true
```

```text
if C15
and material_label == true
and MFE_30D_pct >= +20
and MAE_90D_pct <= -25
and refreshed_margin_cash_bridge == false:
    local_4B_watch = true
    block_stage3_green = true
```

```text
if C15
and material_label == true
and MFE_90D_pct < +10
and MAE_90D_pct <= -20:
    route = Stage2_FalsePositive_Block
```

```text
if C15
and dominant_driver_belongs_to_C16_C17_battery_policy_or_governance_axis == true:
    cap_C15_contribution = true
    require_reclassification = true
```

---

## 8. Residual contribution summary

```yaml
do_not_propose_new_weight_delta: false
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
new_axis_proposed: C15_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_REQUIREMENT_V105
existing_axis_strengthened:
  - C15_material_label_not_enough_without_ASP_margin_FCF_bridge
  - C15_high_MFE_material_label_local_4B_until_margin_refresh
  - C15_low_MFE_high_MAE_material_label_false_positive_block
  - C15_company_specific_margin_bridge_positive_escape_hatch
  - C15_reclassification_guard_for_C16_C17_or_battery_policy_drivers
existing_axis_weakened: null
```

---

## 9. Deferred Coding Agent Handoff Prompt

```text
Do not patch production scoring from this MD alone. Batch this C15 loop with C15 loops 101~104, C16 loops 112~114, C17 loops 136~138 and R13 high-MAE/accounting-trust guardrails. Extract `C15_MATERIAL_LABEL_TO_ASP_MARGIN_FCF_BRIDGE_REQUIREMENT_V105` as a shadow-rule candidate. Preserve company-specific material margin positives, route high-MFE/high-MAE material labels to local 4B, block low-MFE/high-MAE material labels, and reclassify rows whose dominant bridge belongs to C16, C17, battery-policy or governance mechanics.
```

---

## 10. Next research state

```yaml
completed_round: R4
completed_loop: 105
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
next_recommended_archetypes:
  - C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
  - C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  - C22_INSURANCE_RATE_CYCLE_RESERVE
  - R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
  - C18_CONSUMER_EXPORT_CHANNEL_REORDER
```
