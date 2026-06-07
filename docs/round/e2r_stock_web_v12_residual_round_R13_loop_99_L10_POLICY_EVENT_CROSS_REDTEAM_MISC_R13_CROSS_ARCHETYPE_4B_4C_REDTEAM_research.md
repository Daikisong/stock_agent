# E2R Stock-Web v12 Residual Research — R13 / Loop 99

```yaml
scheduled_round: R13
scheduled_loop: 99
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: MOBILITY_BUILDING_MATERIAL_TELEMEDICINE_HOLDING_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_TRUST_REDTEAM

research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_data_source: Songdaiki/stock-web
upstream_source: FinanceData/marcap
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
manifest_max_date: 2026-02-20

production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false

review_trigger_count: 12
reviewed_original_canonical_count: 4
reviewed_original_canonical_ids:
  - C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reviewed_fine_branch_count: 4
reviewed_fine_branches:
  - VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE
  - CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE
  - TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE
  - HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE

new_independent_case_count: 0
do_not_count_as_new_case_count: 12
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
watch_yellow_cap_count: 4
local_burst_or_4b_watch_count: 5
hard_4c_candidate_count: 4
stage2_false_positive_or_high_mae_count: 8

mobility_supplier_execution_case_count: 3
building_material_cashflow_case_count: 3
telemedicine_policy_adoption_case_count: 3
holding_nav_governance_execution_case_count: 3
label_to_execution_bridge_case_count: 12

oem_volume_model_mix_bridge_missing_count: 2
building_material_receivables_margin_bridge_missing_count: 2
policy_to_adoption_order_revenue_bridge_missing_count: 2
capital_allocation_minority_value_bridge_missing_count: 2
liquidity_row_tradeability_trust_caveat_count: 7
old_corporate_action_or_name_history_caveat_count: 9
event_window_separation_required_count: 3
rejected_or_checked_not_used_candidate_count: 3
calibration_usable_review_count: 12

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 99
next_round: R1
next_loop: 100
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 99
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a normal sector-expansion round. It is a cross-archetype checkpoint for:

```text
false positive
high MAE
4B too early / too late
4C late
accounting / listing / tradeability trust
price validation
event-label vs company-specific execution bridge
```

After this file:

```text
next_round = R1
next_loop = 100
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the twelve cases produced in loop99 R9~R12:

```text
R9 / C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
  - 011070 LG이노텍
  - 013570 디와이
  - 122690 서진오토모티브

R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 183190 아세아시멘트
  - 344820 KCC글라스
  - 007210 벽산

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 032620 유비케어
  - 032850 비트컴퓨터
  - 099750 이지케어텍

R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 000070 삼양홀딩스
  - 004990 롯데지주
  - 006840 AK홀딩스
```

No-repeat handling:

```text
row_type = review_case
new_independent_case_count = 0
do_not_count_as_new_case_count = 12
independent_evidence_weight_total = 0.0
```

The original R9/R10/R11/R12 rows remain the usable calibration cases. This R13 file only validates cross-archetype guardrails and links the original cases into a shared failure grammar.

---

## 3. Cross-archetype question

The same structural error appears across four loop99 event families:

```text
C29 vehicle electronics / hydraulic / drivetrain mobility suppliers:
  auto/mobility label exists,
  but equity value depends on named OEM/model/program, production schedule,
  volume, model mix, utilization, pass-through, warranty/quality,
  working capital, customer concentration, and OP margin.

C30 cement / glass / insulation / building materials:
  construction-material label exists,
  but equity value depends on construction volume, selling price,
  fuel/electricity/freight/raw-material cost, inventory, receivables,
  cash collection, housing/remodeling/PF exposure, working capital,
  and margin/FCF conversion.

C31 telemedicine / digital health / healthcare IT policy:
  public policy and medical-access salience exists,
  but equity value depends on adoption by hospitals, clinics, pharmacies, and patients,
  platform traffic, paid conversion, order visibility, renewal, usage,
  workflow integration, compliance/support/cloud cost, revenue recognition,
  cash collection, and OP margin.

C32 holding-company NAV discount / governance:
  Value-up, NAV discount, and holding-company salience exists,
  but equity value depends on capital allocation execution,
  buyback cancellation, dividend, asset sale, restructuring mechanics,
  control math, minority protection, approval path, liquidity, and price survival.
```

Shared false-positive mechanism:

```text
recognizable macro / policy / theme / value label
  -> first price spike or attention burst
  -> model over-promotes label to Stage2-Actionable or Stage3-Green
  -> company-specific execution / cashflow / order / margin / capital-allocation bridge is absent or stale
  -> high MAE, Watch cap, local 4B, hard 4C, or event-window separation follows
```

Shared guardrail:

```text
A label opens the door.
C29 asks whether OEM program volume becomes OP margin.
C30 asks whether materials shipment becomes cash and FCF.
C31 asks whether policy becomes adoption, usage, order, renewal, and OP.
C32 asks whether the holding-company vault opens for minority shareholders.
```

---

## 4. Reviewed case matrix

| Original canonical | Fine branch | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---|---:|---|---:|---:|---:|---|
| C29 | vehicle electronics | 011070 | LG이노텍 | 192,900 | +47.7% | -11.2% | positive; Green requires fresh customer-program/model-mix/margin evidence |
| C29 | hydraulic component | 013570 | 디와이 | 5,760 | +11.1% | -25.8% | local 4B / Watch; OEM volume and margin bridge missing |
| C29 | drivetrain supplier | 122690 | 서진오토모티브 | 3,370 | +17.7% | -36.2% | hard 4C; drivetrain label failed OEM-volume/margin survival |
| C30 | cement | 183190 | 아세아시멘트 | 10,720 | +11.0% | -8.7% | capped positive; Green requires fresh volume/input-cost/receivables/margin evidence |
| C30 | glass/window/interior | 344820 | KCC글라스 | 40,400 | +8.4% | -5.1% | Watch/Yellow; remodeling/order/cashflow bridge missing |
| C30 | insulation material | 007210 | 벽산 | 2,480 | +4.6% | -25.0% | hard 4C; construction-volume/receivables/margin bridge missing |
| C31 | clinic/pharmacy platform | 032620 | 유비케어 | 5,000 | +58.2% | -30.8% | positive with 4B/Green cap after policy rerating |
| C31 | telemedicine hospital IT | 032850 | 비트컴퓨터 | 8,280 | +15.3% | -44.4% | hard 4C; policy-to-platform revenue bridge missing |
| C31 | EMR hospital platform | 099750 | 이지케어텍 | 17,740 | +31.1% | -27.1% | local positive / Watch-4B cap |
| C32 | holding-company portfolio | 000070 | 삼양홀딩스 | 73,700 | +19.3% | -12.3% | positive; Green requires capital-allocation execution refresh |
| C32 | holding NAV discount | 004990 | 롯데지주 | 31,250 | +8.0% | -28.2% | local 4B / Watch; capital allocation bridge missing |
| C32 | low-liquidity holding | 006840 | AK홀딩스 | 17,230 | +4.6% | -30.4% | hard 4C; low-PBR label failed minority-value execution |

---

## 5. R9 review — mobility supplier execution and margin

### 5.1 011070 LG이노텍

```text
entry_close: 192,900
peak_high: 285,000
MFE: +47.7%
worst_low_after_entry: 171,200
MAE: -11.2%
```

R13 interpretation:

```text
This is the constructive C29 vehicle-electronics case.
The positive is valid because MFE was large and drawdown stayed below the hard zone.
But the signal must be capped unless customer program, model mix,
utilization, cost pass-through, and margin evidence remain current.
```

Classification:

```text
positive_control = true
capped_positive = true
green_block_without_refreshed_customer_program_model_mix_margin = true
old_corporate_action_caveat = historical_only
```

### 5.2 013570 디와이

```text
entry_close: 5,760
peak_high: 6,400
MFE: +11.1%
worst_low_after_entry: 4,275
MAE: -25.8%
```

R13 interpretation:

```text
This is a hydraulic / mobility component local 4B.
The auto/mobility label had some price response,
but OEM/program volume, utilization, pass-through, working capital,
and margin evidence did not hold the path.
```

Classification:

```text
watch_or_cap = true
local_4b_overlay = true
oem_volume_model_mix_bridge_missing = true
row_presence_or_name_history_caveat = historical_only
```

### 5.3 122690 서진오토모티브

```text
entry_close: 3,370
peak_high: 3,965
MFE: +17.7%
worst_low_after_entry: 2,150
MAE: -36.2%
```

R13 interpretation:

```text
This is the drivetrain / powertrain hard guardrail.
A moderate MFE came first, but the later hard-zone MAE says the supplier label
did not convert into named OEM/model volume, cost pass-through, warranty/quality control,
and OP margin survival.
```

Classification:

```text
hard_4c_candidate = true
oem_volume_margin_bridge_missing = true
spac_name_history_or_row_presence_caveat = true
```

---

## 6. R10 review — building material volume, receivables, and FCF

### 6.1 183190 아세아시멘트

```text
entry_close: 10,720
peak_high: 11,900
MFE: +11.0%
worst_low_after_entry: 9,790
MAE: -8.7%
```

R13 interpretation:

```text
This is the capped cement/material positive.
The case is usable as a constructive control, but the MFE was modest.
Green requires fresh cement volume, selling price, input-cost, inventory,
receivables, and margin evidence.
```

Classification:

```text
capped_positive = true
green_block_without_refreshed_volume_input_cost_receivables_margin = true
old_corporate_action_caveat = historical_only
```

### 6.2 344820 KCC글라스

```text
entry_close: 40,400
peak_high: 43,800
MFE: +8.4%
worst_low_after_entry: 38,350
MAE: -5.1%
```

R13 interpretation:

```text
This is a glass / window / interior-material Watch cap.
The label is relevant, but price confirmation was shallow and the cashflow bridge
to remodeling demand, orders, receivables, and margin was not visible.
```

Classification:

```text
watch_yellow_cap = true
remodeling_order_cashflow_bridge_missing = true
short_listing_or_old_corporate_action_caveat = true
```

### 6.3 007210 벽산

```text
entry_close: 2,480
peak_high: 2,595
MFE: +4.6%
worst_low_after_entry: 1,860
MAE: -25.0%
```

R13 interpretation:

```text
This is the insulation / building-material hard guardrail.
A shallow label-only MFE plus hard-zone drawdown should block Actionable and Green.
The missing bridge is construction volume, remodeling demand, receivables,
cash collection, and margin/FCF survival.
```

Classification:

```text
hard_4c_candidate = true
construction_volume_receivables_margin_bridge_missing = true
row_presence_or_old_corporate_action_caveat = true
```

---

## 7. R11 review — telemedicine policy, adoption, and revenue conversion

### 7.1 032620 유비케어

```text
entry_close: 5,000
peak_high: 7,910
MFE: +58.2%
worst_low_after_entry: 3,460
MAE: -30.8%
```

R13 interpretation:

```text
This is the telemedicine / clinic-pharmacy platform positive,
but the later August drawdown forces a 4B/Green cap.
The policy label must convert into adoption, platform usage,
orders, renewals, revenue recognition, and OP margin.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
green_cap_after_policy_rerating = true
policy_to_adoption_order_margin_refresh_required = true
```

### 7.2 032850 비트컴퓨터

```text
entry_close: 8,280
peak_high_first_phase: 9,550
MFE: +15.3%
worst_low_after_entry: 4,605
MAE: -44.4%
```

R13 interpretation:

```text
This is the telemedicine / hospital-IT policy hard failure.
The policy door opened, but hospital/clinic platform order,
usage, renewal, revenue, and margin conversion did not appear from the first trigger.
Later rebounds require separate event windows.
```

Classification:

```text
hard_4c_candidate = true
policy_to_order_revenue_bridge_missing = true
event_window_separation_required = true
row_presence_or_old_corporate_action_caveat = historical_only
```

### 7.3 099750 이지케어텍

```text
entry_close: 17,740
peak_high: 23,250
MFE: +31.1%
worst_low_after_entry: 12,940
MAE: -27.1%
```

R13 interpretation:

```text
This is an EMR / hospital-platform local positive with Watch/4B cap.
The stock reacted to digital-health policy, but hospital order,
implementation, support-cost, renewal, and revenue/margin evidence were not durable enough for Green.
```

Classification:

```text
watch_or_cap = true
local_4b_overlay = true
hospital_order_implementation_margin_bridge_missing = true
short_listing_or_future_corporate_action_caveat = true
```

---

## 8. R12 review — holding-company NAV discount and minority-value execution

### 8.1 000070 삼양홀딩스

```text
entry_close: 73,700
peak_high: 87,900
MFE: +19.3%
worst_low_after_entry: 64,600
MAE: -12.3%
```

R13 interpretation:

```text
This is the holding-company portfolio-value positive.
NAV discount and Value-up salience worked, but Green must remain capped
unless capital allocation, buyback cancellation, dividend mechanics,
asset sale, restructuring, or minority-value delivery evidence refreshes.
```

Classification:

```text
positive_control = true
capped_positive = true
capital_allocation_execution_refresh_required = true
old_corporate_action_or_name_history_caveat = historical_only
```

### 8.2 004990 롯데지주

```text
entry_close: 31,250
peak_high_first_phase: 33,750
MFE: +8.0%
worst_low_after_entry: 22,450
MAE: -28.2%
```

R13 interpretation:

```text
This is a large holding-company local 4B / Watch case.
The first policy spike failed price survival because the market did not see
capital return, asset sale, restructuring, cancellation, or minority-value execution.
```

Classification:

```text
local_4b_overlay = true
watch_cap = true
capital_allocation_bridge_missing = true
row_presence_or_name_history_caveat = historical_only
```

### 8.3 006840 AK홀딩스

```text
entry_close: 17,230
peak_high: 18,030
MFE: +4.6%
worst_low_after_entry: 12,000
MAE: -30.4%
```

R13 interpretation:

```text
This is the low-liquidity holding-company hard guardrail.
The low-PBR / Value-up label did not open the vault.
Shallow MFE plus hard-zone MAE requires hard-4C routing unless execution evidence appears.
```

Classification:

```text
hard_4c_candidate = true
low_liquidity_row_trust_caveat = true
minority_value_execution_bridge_missing = true
```

---

## 9. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED

For mobility supplier, building-material, telemedicine-policy,
and holding-company governance archetypes:

  Do not open Stage2-Actionable or Stage3-Green from label salience alone.

  First classify the event type:
    - C29:
        vehicle electronics / hydraulic component / drivetrain supplier / mobility component
    - C30:
        cement / glass / window / insulation / interior building material
    - C31:
        telemedicine / digital health / medical access / EMR / hospital IT
    - C32:
        holding-company NAV discount / Value-up / governance / capital allocation

  Then require the matching bridge:
    - C29:
        named OEM/model/platform, production schedule, volume, model mix,
        utilization, cost pass-through, warranty/quality, working capital,
        customer concentration, and OP margin.
    - C30:
        product/channel, construction volume, selling price, input cost,
        inventory, receivables, cash collection, working capital,
        PF/remodeling/housing exposure, and margin/FCF conversion.
    - C31:
        policy/rule/payer/institution, clinic/hospital/pharmacy/patient adoption,
        platform usage, paid conversion, orders, renewal, workflow integration,
        compliance/support/cloud cost, revenue recognition, cash collection, and OP margin.
    - C32:
        capital allocation, buyback cancellation, dividend, asset sale,
        restructuring mechanics, control math, minority protection,
        board/shareholder approval, liquidity trust, and price survival.

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but bridge evidence decays:
    preserve as capped positive, Watch, or local 4B rather than Green.

  If MFE is shallow and the bridge is label-only:
    cap at Watch/Yellow.

  If later event-like rebounds appear after a failed first trigger:
    create a new event window; do not retroactively validate the earlier failed setup.

  If low-liquidity, row-presence, name-history, old corporate-action,
  short-listing, raw-discontinuity, SPAC history, or segment caveat appears:
    apply a trust cap and block contaminated windows.
```

### Quantitative trigger candidates

```text
hard_4c_label_to_execution_candidate:
  MFE < +18%
  AND MAE <= -30%
  AND company_specific_execution_bridge_missing == true

policy_or_platform_hard_4c_candidate:
  MFE < +20%
  AND MAE <= -40%
  AND policy_to_order_revenue_bridge_missing == true

shallow_label_watch_cap:
  MFE < +10%
  AND execution_bridge_missing == true
  AND hard_4c_threshold_not_crossed == true

local_4b_after_theme_mfe:
  MFE >= +15%
  AND later MAE is material
  AND fresh order/cashflow/margin/capital-allocation evidence is absent

capped_positive:
  MFE >= +15%
  AND MAE controlled or not hard-zone
  AND economic/legal bridge is plausible
  AND fresh execution evidence is required for Green

event_window_separation:
  later renewed event == true
  -> create a new event window; do not rescue failed first trigger
```

---

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L99_C29_011070","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"011070","name":"LG이노텍","entry_date":"2024-02-01","entry_price":192900,"mfe_pct":47.7,"mae_pct":-11.2,"r13_verdict":"positive_vehicle_electronics_but_green_cap_requires_refreshed_customer_program_model_mix_cost_pass_through_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C29_013570","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"013570","name":"디와이","entry_date":"2024-02-01","entry_price":5760,"mfe_pct":11.1,"mae_pct":-25.8,"r13_verdict":"local_4b_watch_hydraulic_mobility_component_label_without_oem_program_volume_cost_pass_through_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C29_122690","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"122690","name":"서진오토모티브","entry_date":"2024-02-01","entry_price":3370,"mfe_pct":17.7,"mae_pct":-36.2,"r13_verdict":"hard_4c_drivetrain_powertrain_supplier_label_without_named_oem_model_volume_cost_pass_through_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C30_183190","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"183190","name":"아세아시멘트","entry_date":"2024-02-01","entry_price":10720,"mfe_pct":11.0,"mae_pct":-8.7,"r13_verdict":"capped_positive_cement_material_spread_but_green_requires_fresh_volume_input_cost_receivables_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C30_344820","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"344820","name":"KCC글라스","entry_date":"2024-02-01","entry_price":40400,"mfe_pct":8.4,"mae_pct":-5.1,"r13_verdict":"watch_yellow_glass_window_interior_material_label_without_remodeling_order_receivables_cashflow_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C30_007210","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"007210","name":"벽산","entry_date":"2024-02-01","entry_price":2480,"mfe_pct":4.6,"mae_pct":-25.0,"r13_verdict":"hard_4c_insulation_building_material_label_without_construction_volume_receivables_cashflow_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C31_032620","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"032620","name":"유비케어","entry_date":"2024-02-01","entry_price":5000,"mfe_pct":58.2,"mae_pct":-30.8,"r13_verdict":"positive_clinic_pharmacy_telemedicine_platform_but_4b_green_cap_requires_fresh_adoption_order_usage_revenue_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C31_032850","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"032850","name":"비트컴퓨터","entry_date":"2024-02-01","entry_price":8280,"mfe_pct":15.3,"mae_pct":-44.4,"r13_verdict":"hard_4c_telemedicine_hospital_it_policy_label_without_platform_order_usage_revenue_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C31_099750","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"099750","name":"이지케어텍","entry_date":"2024-02-01","entry_price":17740,"mfe_pct":31.1,"mae_pct":-27.1,"r13_verdict":"local_positive_watch_4b_emr_hospital_platform_policy_label_without_sustained_order_implementation_renewal_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C32_000070","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"000070","name":"삼양홀딩스","entry_date":"2024-02-01","entry_price":73700,"mfe_pct":19.3,"mae_pct":-12.3,"r13_verdict":"positive_holding_company_portfolio_valueup_but_green_requires_refreshed_capital_allocation_minority_value_execution_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C32_004990","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"004990","name":"롯데지주","entry_date":"2024-02-01","entry_price":31250,"mfe_pct":8.0,"mae_pct":-28.2,"r13_verdict":"local_4b_watch_holding_company_nav_discount_policy_spike_without_capital_allocation_asset_sale_restructuring_minority_value_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L99_C32_006840","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"006840","name":"AK홀딩스","entry_date":"2024-02-01","entry_price":17230,"mfe_pct":4.6,"mae_pct":-30.4,"r13_verdict":"hard_4c_low_liquidity_holding_company_valueup_label_without_capital_allocation_and_minority_value_execution","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":12,"reviewed_original_canonical_count":4,"reviewed_original_canonical_ids":["C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"new_independent_case_count":0,"do_not_count_as_new_case_count":12,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"watch_yellow_cap_count":4,"local_burst_or_4b_watch_count":5,"hard_4c_candidate_count":4,"stage2_false_positive_or_high_mae_count":8,"mobility_supplier_execution_case_count":3,"building_material_cashflow_case_count":3,"telemedicine_policy_adoption_case_count":3,"holding_nav_governance_execution_case_count":3,"label_to_execution_bridge_case_count":12,"oem_volume_model_mix_bridge_missing_count":2,"building_material_receivables_margin_bridge_missing_count":2,"policy_to_adoption_order_revenue_bridge_missing_count":2,"capital_allocation_minority_value_bridge_missing_count":2,"liquidity_row_tradeability_trust_caveat_count":7,"old_corporate_action_or_name_history_caveat_count":9,"event_window_separation_required_count":3,"rejected_or_checked_not_used_candidate_count":3,"calibration_usable_review_count":12,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":99,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For mobility supplier, building-material, telemedicine-policy, and holding-company governance archetypes, do not open Stage2-Actionable or Stage3-Green from label salience alone. First classify the event type: C29 vehicle electronics/hydraulic/drivetrain mobility component; C30 cement/glass/window/insulation/interior building material; C31 telemedicine/digital health/EMR/hospital IT; or C32 holding-company NAV discount/Value-up/governance/capital allocation. Require the matching bridge: OEM/model/platform, production schedule, volume, model mix, utilization, cost pass-through, warranty/quality, working capital, customer concentration, and OP margin for C29; product/channel, construction volume, selling price, input cost, inventory, receivables, cash collection, working capital, PF/remodeling/housing exposure, and margin/FCF conversion for C30; policy/rule/payer/institution, hospital/clinic/pharmacy/patient adoption, platform usage, paid conversion, orders, renewal, workflow integration, compliance/support/cloud cost, revenue recognition, cash collection, and OP margin for C31; and capital allocation, buyback cancellation, dividend, asset sale, restructuring mechanics, control math, minority protection, board/shareholder approval, liquidity trust, and price survival for C32. Route shallow-MFE/large-MAE cases to hard-4C; keep meaningful-MFE but stale bridge evidence as capped positive, Watch, or local 4B; cap shallow label-only cases at Watch/Yellow; separate renewed event windows from failed first triggers; apply trust caps for low-liquidity, row-presence, name-history, old corporate-action, short-listing, raw-discontinuity, SPAC history, or segment caveats.","expected_effect":"Unifies loop99 R9-R12 label-to-execution guardrails so the model stops confusing mobility supplier, building-material, telemedicine-policy, or holding-company NAV labels with OEM volume, cash collection, adoption/order revenue, capital allocation, margin conversion, or tradeability trust.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":99,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"label_to_execution_cashflow_margin_capital_allocation_trust_guard","contribution":"Reviews twelve prior loop99 cases without adding independent evidence weight. Validates a shared label-to-execution guard across C29 mobility supplier margin, C30 building-material cashflow, C31 telemedicine policy adoption/order/revenue, and C32 holding-company capital allocation/minority-value execution.","do_not_count_as_global_weight_delta":true}
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original loop99 R9/R10/R11/R12 files:
   - C29 vehicle electronics / hydraulic / drivetrain mobility margin
   - C30 cement / glass / insulation building-material cashflow
   - C31 telemedicine / digital-health policy adoption/order/revenue
   - C32 holding-company NAV-discount capital allocation/minority-value execution
7. If enough R13 reviews agree, consider implementing a pre-scoring check for event/theme/value label archetypes:
   - classify the event type first,
   - identify the true company-level economic/legal/cashflow/adoption/capital-allocation bridge,
   - block label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B, Watch, or capped positive,
   - cap shallow label-only cases at Watch/Yellow,
   - separate renewed event windows from failed first triggers,
   - apply name-history/inactive-listing/short-listing/row-presence/raw-date/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 99
next_round = R1
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R13
completed_loop = 99
next_round = R1
next_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
```
