# E2R Stock-Web v12 Residual Research — R13 / Loop 98

```yaml
scheduled_round: R13
scheduled_loop: 98
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CONSTRUCTION_MATERIALS_EDUCATION_POLICY_HOLDING_NAV_EXECUTION_TRUST_REDTEAM

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

review_trigger_count: 9
reviewed_original_canonical_count: 3
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
  - DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE
  - HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
watch_yellow_cap_count: 1
local_burst_or_4b_watch_count: 4
hard_4c_candidate_count: 2
hard_4c_secondary_guard_count: 1
stage2_false_positive_or_high_mae_count: 5

construction_materials_cashflow_case_count: 3
education_policy_order_revenue_case_count: 3
holding_nav_governance_case_count: 3
event_label_to_execution_bridge_case_count: 9

input_cost_volume_margin_bridge_missing_count: 1
project_receivables_pf_bridge_missing_count: 1
policy_to_order_revenue_bridge_missing_count: 2
platform_retention_margin_bridge_missing_count: 2
capital_allocation_execution_bridge_missing_count: 2
minority_value_realization_bridge_missing_count: 1
event_window_separation_required_count: 2
accounting_listing_tradeability_trust_caveat_count: 7
old_corporate_action_or_name_history_caveat_count: 5
low_liquidity_or_row_presence_caveat_count: 2
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 98
next_round: R1
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 98
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
next_loop = 99
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop98 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 300720 한일시멘트
  - 004980 성신양회
  - 317400 자이에스앤디

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 100220 비상교육
  - 053290 NE능률
  - 057030 YBM넷

R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 001040 CJ
  - 003550 LG
  - 003240 태광산업
```

No-repeat handling:

```text
row_type = review_case
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
independent_evidence_weight_total = 0.0
```

The original R10/R11/R12 rows remain the usable calibration cases. This R13 file only validates cross-archetype guardrails and links the original cases into a shared failure grammar.

---

## 3. Cross-archetype question

The same structural error appears across three event families:

```text
C30 cement / building materials / housing service:
  construction-material or housing-service label exists,
  but equity value depends on volume, selling price,
  coal/electricity/fuel/freight/input cost, inventory,
  receivables, PF/counterparty exposure, cash collection,
  working capital, margin / FCF conversion, and row trust.

C31 digital textbook / edtech / public education policy:
  public policy or digital-textbook salience exists,
  but equity value depends on named policy and budget,
  school adoption, order visibility, platform usage,
  renewal / retention, procurement channel, content and cloud cost,
  revenue recognition, cash collection, and OP margin.

C32 holding-company NAV discount / governance:
  NAV discount, Value-up, or holding-company salience exists,
  but equity value depends on capital allocation execution,
  buyback cancellation, dividend, asset sale, restructuring mechanics,
  control math, minority protection, approval path, timing, liquidity,
  and price survival.
```

Shared false-positive mechanism:

```text
external policy, cycle, or governance salience
  -> recognizable label becomes hot
  -> price reacts first
  -> model over-promotes the label to Stage2-Actionable / Stage3-Green
  -> company-specific execution bridge is missing or stale
  -> shallow MFE, high MAE, local 4B, Watch cap, or hard 4C follows
```

Shared guardrail:

```text
The headline opens the door.
C30 asks whether cement or housing-service volume becomes cash and margin.
C31 asks whether policy becomes adoption, orders, usage, renewal, revenue, and margin.
C32 asks whether the holding-company vault opens through real capital allocation and minority-value delivery.
```

---

## 4. Reviewed case matrix

| Original canonical | Fine branch | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---|---:|---|---:|---:|---:|---|
| C30 | cement/building materials | 300720 | 한일시멘트 | 12,100 | +29.8% | -2.7% | positive; Green requires fresh volume/input-cost/inventory/margin evidence |
| C30 | cement/material spread | 004980 | 성신양회 | 8,120 | +23.2% | -6.3% | positive with 4B/Green cap if input-cost and demand evidence stale |
| C30 | housing-service/project cashflow | 317400 | 자이에스앤디 | 4,810 | +1.7% | -25.2% | Watch/Yellow cap; project receivables/PF/cashflow bridge missing |
| C31 | digital textbook policy | 100220 | 비상교육 | 5,210 | +61.6% | -23.4% | positive with 4B/Green cap after policy rerating |
| C31 | textbook/curriculum policy | 053290 | NE능률 | 5,360 | +17.5% | -48.8% | hard 4C; policy label failed order/revenue/margin survival |
| C31 | edtech/online education | 057030 | YBM넷 | 4,580 | +21.8% | -35.4% | local 4B with hard-4C secondary guard |
| C32 | holding-company NAV discount | 001040 | CJ | 100,900 | +39.3% | -9.7% | positive; Green requires fresh capital-allocation execution |
| C32 | large holding-company Value-up | 003550 | LG | 88,100 | +17.6% | -16.5% | local positive / 4B after execution evidence decay |
| C32 | deep NAV discount / governance | 003240 | 태광산업 | 943,000 | +0.7% | -45.9% | hard 4C; minority-value execution missing |

---

## 5. R10 review — cement, building materials, housing service, and project cashflow

### 5.1 300720 한일시멘트

```text
entry_close: 12,100
peak_high: 15,700
MFE: +29.8%
worst_low_after_entry: 11,770
MAE: -2.7%
```

R13 interpretation:

```text
This is the constructive C30 cement case.
The move had strong price survival and low MAE.
The positive is valid only when cement volume, selling price,
coal/electricity/fuel/freight cost, inventory, working capital,
and margin evidence remain current.
```

Classification:

```text
positive_control = true
capped_positive = true
green_block_without_refreshed_volume_input_cost_margin = true
row_presence_or_old_corporate_action_caveat = historical_only
```

### 5.2 004980 성신양회

```text
entry_close: 8,120
peak_high: 10,000
MFE: +23.2%
worst_low_after_entry: 7,610
MAE: -6.3%
```

R13 interpretation:

```text
This is a second C30 cement / construction-material positive.
It produced enough MFE and avoided hard failure.
However, the February spike and July rerating should not become unrestricted Green
unless cement spread, demand, input cost, freight, and cashflow evidence refresh.
```

Classification:

```text
positive_control = true
capped_positive = true
local_4b_watch = true
input_cost_energy_freight_bridge_refresh_required = true
```

### 5.3 317400 자이에스앤디

```text
entry_close: 4,810
peak_high_after_entry: 4,890
MFE: +1.7%
worst_low_after_entry: 3,600
MAE: -25.2%
```

R13 interpretation:

```text
This is a housing-service / project-cashflow Watch cap.
The label is relevant, but MFE was shallow and the later drawdown was material.
It should not become Actionable unless project receivables, cash collection,
PF/counterparty exposure, and margin bridge are explicit.
```

Classification:

```text
watch_yellow_cap = true
project_cashflow_receivables_bridge_missing = true
pf_counterparty_margin_bridge_missing = true
short_listing_or_segment_trust_caveat = true
```

---

## 6. R11 review — digital textbook, edtech, public education policy

### 6.1 100220 비상교육

```text
entry_close: 5,210
peak_high: 8,420
MFE: +61.6%
worst_low_after_entry: 3,990
MAE: -23.4%
```

R13 interpretation:

```text
This is the education-policy positive.
The policy label had real price power.
But the later drawdown proves why education-policy Green must be capped:
school adoption, order visibility, usage, renewal, revenue recognition,
and margin evidence must refresh after the first rerating.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
green_cap_after_policy_rerating = true
policy_to_order_revenue_bridge_refresh_required = true
```

### 6.2 053290 NE능률

```text
entry_close: 5,360
peak_high_first_phase: 6,300
MFE: +17.5%
worst_low_after_entry: 2,745
MAE: -48.8%
```

R13 interpretation:

```text
This is the textbook/curriculum policy hard failure.
The label had some first-phase response, but policy did not convert into
visible order, usage, renewal, revenue, or margin survival.
Later education-policy spikes should be separated as new windows.
```

Classification:

```text
hard_4c_candidate = true
policy_to_order_revenue_bridge_missing = true
event_window_separation_required = true
row_presence_or_old_corporate_action_caveat = historical_only
```

### 6.3 057030 YBM넷

```text
entry_close: 4,580
peak_high: 5,580
MFE: +21.8%
worst_low_after_entry: 2,960
MAE: -35.4%
```

R13 interpretation:

```text
This is an edtech / online-education local burst that failed price survival.
Because meaningful MFE came first, this is a local 4B rather than a pure zero-response failure.
Because MAE entered the hard zone, stale or late entries deserve a hard-4C secondary guard.
```

Classification:

```text
local_4b_overlay = true
hard_4c_secondary_guard = true
platform_retention_margin_bridge_missing = true
event_window_separation_required = true
```

---

## 7. R12 review — holding-company NAV discount, Value-up, governance execution

### 7.1 001040 CJ

```text
entry_close: 100,900
peak_high: 140,600
MFE: +39.3%
worst_low_after_entry: 91,100
MAE: -9.7%
```

R13 interpretation:

```text
This is the constructive holding-company / NAV-discount case.
The move had strong MFE and controlled MAE.
But C32 Green should remain blocked without fresh evidence of actual capital allocation,
buyback cancellation, dividend, asset sale, restructuring, or minority-value realization.
```

Classification:

```text
positive_control = true
capped_positive = true
capital_allocation_execution_refresh_required = true
old_corporate_action_or_name_history_caveat = historical_only
```

### 7.2 003550 LG

```text
entry_close: 88,100
peak_high: 103,600
MFE: +17.6%
worst_low_after_entry: 73,600
MAE: -16.5%
```

R13 interpretation:

```text
This is a large holding-company local positive.
The first Value-up rerating worked, then evidence and price survival decayed.
It should be local 4B unless capital-allocation execution evidence refreshes.
```

Classification:

```text
local_positive = true
local_4b_overlay = true
capital_allocation_execution_bridge_missing_or_stale = true
row_presence_caveat = historical_only
```

### 7.3 003240 태광산업

```text
entry_close: 943,000
peak_high_after_entry: 950,000
MFE: +0.7%
worst_low_after_entry: 510,000
MAE: -45.9%
```

R13 interpretation:

```text
This is the deep NAV-discount hard failure.
The vault stayed locked: assets and discount existed, but no concrete
minority-value execution bridge appeared from the selected trigger.
Near-zero MFE plus severe MAE requires hard-4C routing.
```

Classification:

```text
hard_4c_candidate = true
minority_value_realization_bridge_missing = true
low_liquidity_or_row_presence_caveat = true
deep_nav_discount_false_positive = true
```

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_LABEL_TO_EXECUTION_ORDER_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED

For construction-material / housing-service, education-policy / edtech,
and holding-company governance / NAV-discount archetypes:

  Do not open Stage2-Actionable or Stage3-Green from label salience alone.

  First classify the event type:
    - C30:
        cement / building materials / housing-service / project cashflow
    - C31:
        digital textbook / edtech / public education policy / curriculum
    - C32:
        holding-company NAV discount / governance / Value-up / capital allocation

  Then require the matching bridge:
    - C30:
        construction volume, selling price, input-cost control, inventory,
        working capital, receivables, PF/counterparty exposure,
        cash collection, margin/FCF conversion, and row trust.
    - C31:
        named policy, budget, grade, subject, adoption schedule,
        school adoption, order visibility, usage, renewal, revenue recognition,
        content/cloud/support cost, cash collection, and OP margin.
    - C32:
        concrete capital allocation, buyback cancellation, dividend,
        asset sale, restructuring mechanics, control math, minority protection,
        board/shareholder approval, timing/tax/regulatory risk,
        liquidity trust, and price survival.

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but bridge evidence decays:
    preserve as capped positive or local 4B rather than Green.

  If MFE is shallow and the bridge is label-only:
    cap at Watch/Yellow.

  If later event-like spikes appear after a failed first trigger:
    create a new event window; do not retroactively validate the earlier failed setup.

  If low-liquidity, row-presence, name-history, old corporate-action,
  raw-discontinuity, short-listing, or segment caveat appears:
    apply a trust cap and block contaminated windows.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +10%
  AND MAE <= -35%
  AND company_specific_execution_bridge_missing == true

education_policy_hard_4c_candidate:
  MFE < +20%
  AND MAE <= -40%
  AND policy_to_order_revenue_bridge_missing == true

local_4b_after_policy_or_valueup_mfe:
  MFE >= +15%
  AND later MAE is material
  AND fresh adoption / cashflow / capital-allocation evidence is absent

watch_yellow_label_cap:
  MFE < +8%
  AND MAE is not yet hard
  AND bridge is label-only

capped_positive_with_trust_caveat:
  MFE >= +20%
  AND MAE controlled
  AND economic bridge is plausible
  AND row / listing / trust caveat exists
  -> capped positive, not ordinary Green

event_window_separation:
  later renewed event == true
  -> create a new event window; do not rescue failed first trigger
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L98_C30_300720","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"300720","name":"한일시멘트","entry_date":"2024-02-01","entry_price":12100,"mfe_pct":29.8,"mae_pct":-2.7,"r13_verdict":"positive_cement_material_spread_but_green_cap_requires_refreshed_volume_input_cost_inventory_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C30_004980","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"004980","name":"성신양회","entry_date":"2024-02-01","entry_price":8120,"mfe_pct":23.2,"mae_pct":-6.3,"r13_verdict":"positive_cement_material_rerating_but_4b_green_cap_if_input_cost_demand_cashflow_evidence_stale","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C30_317400","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"317400","name":"자이에스앤디","entry_date":"2024-02-01","entry_price":4810,"mfe_pct":1.7,"mae_pct":-25.2,"r13_verdict":"watch_yellow_housing_service_label_without_project_receivables_pf_cashflow_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C31_EDU_100220","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"100220","name":"비상교육","entry_date":"2024-02-01","entry_price":5210,"mfe_pct":61.6,"mae_pct":-23.4,"r13_verdict":"positive_digital_textbook_policy_rerating_but_4b_green_cap_requires_refreshed_school_adoption_order_usage_revenue_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C31_EDU_053290","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"053290","name":"NE능률","entry_date":"2024-02-01","entry_price":5360,"mfe_pct":17.5,"mae_pct":-48.8,"r13_verdict":"hard_4c_textbook_curriculum_policy_label_without_school_adoption_order_revenue_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C31_EDU_057030","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"057030","name":"YBM넷","entry_date":"2024-02-01","entry_price":4580,"mfe_pct":21.8,"mae_pct":-35.4,"r13_verdict":"local_4b_edtech_online_policy_label_with_hard_4c_secondary_guard_when_platform_adoption_retention_margin_bridge_missing","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C32_001040","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"001040","name":"CJ","entry_date":"2024-02-01","entry_price":100900,"mfe_pct":39.3,"mae_pct":-9.7,"r13_verdict":"positive_holding_company_nav_discount_valueup_but_green_cap_requires_refreshed_capital_allocation_execution_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C32_003550","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"003550","name":"LG","entry_date":"2024-02-01","entry_price":88100,"mfe_pct":17.6,"mae_pct":-16.5,"r13_verdict":"local_4b_large_holding_company_valueup_case_when_capital_allocation_execution_evidence_decays","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L98_C32_003240","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"003240","name":"태광산업","entry_date":"2024-02-01","entry_price":943000,"mfe_pct":0.7,"mae_pct":-45.9,"r13_verdict":"hard_4c_deep_nav_discount_governance_label_without_minority_value_execution_and_liquidity_trust_survival","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"watch_yellow_cap_count":1,"local_burst_or_4b_watch_count":4,"hard_4c_candidate_count":2,"hard_4c_secondary_guard_count":1,"stage2_false_positive_or_high_mae_count":5,"construction_materials_cashflow_case_count":3,"education_policy_order_revenue_case_count":3,"holding_nav_governance_case_count":3,"event_label_to_execution_bridge_case_count":9,"input_cost_volume_margin_bridge_missing_count":1,"project_receivables_pf_bridge_missing_count":1,"policy_to_order_revenue_bridge_missing_count":2,"platform_retention_margin_bridge_missing_count":2,"capital_allocation_execution_bridge_missing_count":2,"minority_value_realization_bridge_missing_count":1,"event_window_separation_required_count":2,"accounting_listing_tradeability_trust_caveat_count":7,"old_corporate_action_or_name_history_caveat_count":5,"low_liquidity_or_row_presence_caveat_count":2,"calibration_usable_review_count":9,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":98,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_LABEL_TO_EXECUTION_ORDER_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For construction-material/housing-service, education-policy/edtech, and holding-company governance/NAV-discount archetypes, do not open Stage2-Actionable or Stage3-Green from label salience alone. First classify the event type: C30 cement/building materials/housing-service/project-cashflow; C31 digital textbook/edtech/public education policy/curriculum; or C32 holding-company NAV discount/governance/Value-up/capital allocation. Require the matching bridge: construction volume, selling price, input-cost control, inventory, working capital, receivables, PF/counterparty exposure, cash collection, margin/FCF conversion, and row trust for C30; named policy, budget, grade, subject, adoption schedule, school adoption, order visibility, usage, renewal, revenue recognition, content/cloud/support cost, cash collection, and OP margin for C31; concrete capital allocation, buyback cancellation, dividend, asset sale, restructuring mechanics, control math, minority protection, board/shareholder approval, timing/tax/regulatory risk, liquidity trust, and price survival for C32. Route shallow-MFE/high-MAE cases to hard-4C; keep meaningful-MFE but stale execution evidence as capped positive or local 4B; cap shallow label-only cases at Watch/Yellow; separate renewed event windows from failed first triggers; apply trust caps for low-liquidity, row-presence, name-history, old corporate-action, raw-discontinuity, short-listing, or segment caveats.","expected_effect":"Unifies R10-R12 loop98 event-label guardrails so the model stops confusing cement/housing-service labels, digital-textbook/edtech policy labels, or holding-company NAV-discount salience with cash collection, adoption/order/revenue, capital-allocation execution, margin conversion, or tradeability trust.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":98,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"label_to_execution_order_cashflow_margin_capital_allocation_trust_guard","contribution":"Reviews nine prior loop98 cases without adding independent evidence weight. Validates a shared label-to-execution guard across C30 construction-material/housing-service cashflow, C31 education-policy adoption/order/revenue, and C32 holding-company capital-allocation/governance execution.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_LABEL_TO_EXECUTION_ORDER_CASHFLOW_MARGIN_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop98 files:
   - C30 cement/building-material/housing-service volume/input-cost/cashflow
   - C31 digital-textbook/edtech/public-education policy adoption/order/revenue
   - C32 holding-company NAV-discount/governance capital-allocation execution
7. If enough R13 reviews agree, consider implementing a pre-scoring check for event/policy/governance archetypes:
   - classify the event type first,
   - identify the true company-level economic/legal/cashflow/adoption/capital-allocation bridge,
   - block label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - cap shallow label-only cases at Watch/Yellow,
   - separate renewed event windows from failed first triggers,
   - apply name-history/inactive-listing/short-listing/row-presence/raw-date/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 98
next_round = R1
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 98
next_round = R1
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
