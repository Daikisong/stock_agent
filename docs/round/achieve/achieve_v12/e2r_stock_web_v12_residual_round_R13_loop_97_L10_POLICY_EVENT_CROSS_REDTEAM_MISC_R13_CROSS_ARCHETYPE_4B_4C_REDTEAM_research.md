# E2R Stock-Web v12 Residual Research — R13 / Loop 97

```yaml
scheduled_round: R13
scheduled_loop: 97
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: PROJECT_CASHFLOW_ENVIRONMENT_POLICY_HOLDING_COMPANY_EXECUTION_TRUST_REDTEAM

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
  - MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
  - WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE
  - HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 3
capped_positive_or_bridge_positive_count: 3
watch_yellow_cap_count: 3
local_burst_or_4b_watch_count: 2
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 3

construction_project_cashflow_case_count: 3
environment_policy_cashflow_case_count: 3
holding_company_governance_case_count: 3
event_label_to_execution_bridge_case_count: 9

project_cashflow_receivables_bridge_missing_count: 2
policy_to_cashflow_margin_bridge_missing_count: 2
capital_allocation_execution_bridge_missing_count: 2
event_window_or_execution_evidence_missing_count: 4
accounting_listing_tradeability_trust_caveat_count: 7
old_corporate_action_or_name_history_caveat_count: 5
inactive_or_row_presence_caveat_count: 2
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 97
next_round: R1
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 97
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
next_loop = 98
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop97 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 011560 세보엠이씨
  - 010400 우진아이엔에스
  - 016250 SGC E&C / SGC이테크건설

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 029960 코엔텍
  - 067900 와이엔텍
  - 009440 KC그린홀딩스

R12 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 028260 삼성물산
  - 034730 SK
  - 000880 한화
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
C30 MEP / building-services / industrial EPC:
  construction or project contractor label exists,
  but equity value depends on project exposure, receivables,
  cash collection, backlog quality, cost control, working capital,
  margin / FCF conversion, and listing / row trust.

C31 environmental / waste-treatment policy:
  environmental regulation or waste-treatment salience exists,
  but equity value depends on permitted capacity, volume, unit price,
  contract durability, capex, utilization, cash collection,
  FCF / OP conversion, and tradeability or event trust.

C32 holding-company governance / Value-up:
  governance discount, low-PBR, or holding-company salience exists,
  but equity value depends on capital-allocation execution,
  buyback cancellation, asset sale, restructuring mechanics,
  minority protection, approval path, timing, and price survival.
```

Shared false-positive mechanism:

```text
external event or policy salience
  -> recognizable sector / policy / governance label becomes hot
  -> price reacts first
  -> model over-promotes the label to Stage2-Actionable / Stage3-Green
  -> company-specific execution bridge is missing or stale
  -> shallow MFE, high MAE, local 4B, Watch cap, or hard 4C follows
```

Shared guardrail:

```text
The headline rings the bell.
C30 asks whether project cash and receivables hit the ledger.
C31 asks whether regulation becomes permitted volume, unit price, cash collection, and margin.
C32 asks whether the locked holding-company vault is opened by real capital allocation.
```

---

## 4. Reviewed case matrix

| Original canonical | Fine branch | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---|---:|---|---:|---:|---:|---|
| C30 | MEP / project cashflow | 011560 | 세보엠이씨 | 8,520 | +75.4% | -0.7% | capped positive; Green requires fresh receivables/cashflow/margin evidence |
| C30 | building services contractor | 010400 | 우진아이엔에스 | 5,200 | +4.0% | -42.3% | hard 4C; contractor label without project-cashflow survival |
| C30 | industrial EPC | 016250 | SGC E&C / SGC이테크건설 | 18,790 | +1.7% | -22.3% | Watch/Yellow cap; shallow MFE, project-cashflow bridge stale |
| C31 | waste treatment / permit | 029960 | 코엔텍 | 6,600 | +37.3% | -1.8% | capped positive; inactive/event caveat blocks ordinary Green |
| C31 | waste environmental service | 067900 | 와이엔텍 | 7,310 | +7.1% | -15.9% | Watch/Yellow cap; no strong incremental volume/unit-price bridge |
| C31 | environmental holding | 009440 | KC그린홀딩스 | 3,010 | +10.1% | -76.6% | hard 4C; environmental label without cashflow/trust survival |
| C32 | holding-company Value-up | 028260 | 삼성물산 | 148,700 | +15.5% | -23.0% | local positive / 4B; governance evidence decayed |
| C32 | holding-company discount | 034730 | SK | 197,000 | +7.6% | -35.2% | hard 4C; execution bridge missing |
| C32 | diversified group holding | 000880 | 한화 | 30,000 | +7.3% | -13.8% | Watch/Yellow cap; no concrete capital-allocation bridge |

---

## 5. R10 review — construction project cashflow, receivables, and margin trust

### 5.1 011560 세보엠이씨

```text
entry_close: 8,520
peak_high: 14,940
MFE: +75.4%
worst_low_after_entry: 8,460
MAE: -0.7%
```

R13 interpretation:

```text
This is the constructive C30 case in the loop97 holdout set.
The move produced enough MFE to preserve a positive.
The extremely low MAE helps price validation.
However, the large MFE creates a Green cap:
without fresh project-cash collection, receivables, cost discipline, and margin evidence,
the score should not remain unrestricted Green.
```

Classification:

```text
positive_control = true
capped_positive = true
green_block_without_refreshed_project_cashflow_margin = true
row_presence_or_old_corporate_action_caveat = historical_only
```

### 5.2 010400 우진아이엔에스

```text
entry_close: 5,200
peak_high_after_entry: 5,410
MFE: +4.0%
worst_low_after_entry: 3,000
MAE: -42.3%
```

R13 interpretation:

```text
This is the building-services contractor hard failure.
The construction label existed, but the path did not validate project-cashflow repair.
The setup lacked named project, backlog, receivables, cost control, and margin bridge.
```

Classification:

```text
hard_4c_candidate = true
project_cashflow_receivables_bridge_missing = true
construction_label_false_positive = true
```

### 5.3 016250 SGC E&C / SGC이테크건설

```text
entry_close: 18,790
peak_high_after_entry: 19,110
MFE: +1.7%
worst_low_after_entry: 14,600
MAE: -22.3%
```

R13 interpretation:

```text
This is the industrial EPC Watch cap.
The label is relevant, but the price path does not justify Actionable or Green.
It should remain Watch/Yellow unless project exposure, receivables, working capital, and margin evidence refresh.
```

Classification:

```text
watch_yellow_cap = true
industrial_epc_label_overpromotion_risk = true
name_change_caveat = true
```

---

## 6. R11 review — environmental policy, permitted capacity, cashflow, and trust

### 6.1 029960 코엔텍

```text
entry_close: 6,600
peak_high: 9,060
MFE: +37.3%
worst_low_after_entry: 6,480
MAE: -1.8%
```

R13 interpretation:

```text
This is a true waste-treatment / permit-capacity positive.
The path had strong price survival and low MAE.
However, the later inactive/delisted-like row-presence inference makes this a capped positive,
not ordinary environmental-policy Green.
The economic bridge and event/listing trust must both be checked.
```

Classification:

```text
positive_control = true
capped_positive = true
inactive_or_row_presence_caveat = true
ordinary_green_block = true
```

### 6.2 067900 와이엔텍

```text
entry_close: 7,310
peak_high: 7,830
MFE: +7.1%
worst_low_after_entry: 6,150
MAE: -15.9%
```

R13 interpretation:

```text
This is the waste-treatment Watch cap.
The business label is relevant, but MFE is shallow and the bridge from policy to incremental volume,
unit price, contract durability, and margin is not strong enough.
```

Classification:

```text
watch_yellow_cap = true
unit_price_volume_bridge_missing = true
stage2_actionable_block = true
```

### 6.3 009440 KC그린홀딩스

```text
entry_close: 3,010
peak_high_first_phase: 3,315
MFE: +10.1%
worst_low_after_entry: 705
MAE: -76.6%
```

R13 interpretation:

```text
This is the environmental holding hard failure.
The green / pollution-control label was not enough.
The first trigger failed before later event-like September/October spikes.
Those later spikes must be separated as new event windows.
```

Classification:

```text
hard_4c_candidate = true
cashflow_margin_trust_bridge_missing = true
event_window_separation_required = true
inactive_or_row_presence_caveat = true
```

---

## 7. R12 review — holding-company governance, Value-up, and execution bridge

### 7.1 028260 삼성물산

```text
entry_close: 148,700
peak_high: 171,700
MFE: +15.5%
worst_low_after_entry: 114,500
MAE: -23.0%
```

R13 interpretation:

```text
This is the constructive holding-company / Value-up case.
The first rerating worked, but later evidence decay and material MAE mean it should be local 4B,
not unrestricted Green.
The bridge must be concrete capital allocation, buyback/cancellation, asset sale, restructuring, or minority-value realization.
```

Classification:

```text
local_positive = true
local_4b_overlay = true
capital_allocation_execution_refresh_required = true
```

### 7.2 034730 SK

```text
entry_close: 197,000
peak_high: 212,000
MFE: +7.6%
worst_low_after_entry: 127,600
MAE: -35.2%
```

R13 interpretation:

```text
This is the holding-company discount hard failure.
The setup had governance and Value-up salience, but execution was missing.
Shallow MFE plus high MAE requires hard-4C routing.
```

Classification:

```text
hard_4c_candidate = true
holding_company_discount_false_positive = true
capital_allocation_execution_bridge_missing = true
```

### 7.3 000880 한화

```text
entry_close: 30,000
peak_high: 32,200
MFE: +7.3%
worst_low_after_entry: 25,850
MAE: -13.8%
```

R13 interpretation:

```text
This is a diversified group holding Watch cap.
The portfolio and Value-up label are relevant, but the path does not justify Actionable or Green.
Concrete buyback/cancellation, asset sale, capital return, or restructuring execution is required.
```

Classification:

```text
watch_yellow_cap = true
capital_allocation_execution_bridge_missing = true
ordinary_governance_discount_green_block = true
```

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_POLICY_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED

For construction/project-cashflow, environmental-policy, and holding-company governance archetypes:

  Do not open Stage2-Actionable or Stage3-Green from event salience,
  sector label, policy label, governance discount label, or holding-company label alone.

  First classify the event type:
    - C30: MEP / building services / industrial EPC / project cashflow / receivables
    - C31: environmental regulation / waste treatment / permitted capacity / unit price
    - C32: holding-company discount / governance / Value-up / capital allocation

  Then require the matching bridge:
    - C30:
        company-specific project exposure, backlog quality, receivables,
        cash collection, cost risk, working capital, margin / FCF, and row trust.
    - C31:
        named regulation or public demand, permitted capacity, disposal volume,
        unit price, capex / utilization, contracts, cash collection, FCF / OP margin,
        and event / listing / tradeability trust.
    - C32:
        concrete capital allocation, buyback cancellation, dividend, asset sale,
        restructuring mechanics, control math, minority protection,
        approval path, timing / financing / tax / regulatory risk, and price survival.

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but execution evidence decays:
    preserve as capped positive or local 4B rather than Green.

  If MFE is shallow and the bridge is label-only:
    cap at Watch/Yellow.

  If inactive/delisted-like, name-change, old corporate-action, row-presence,
  raw-last-date divergence, or event-window caveat appears:
    apply a trust cap and block contaminated windows.

  If later event-like spikes appear after a failed first trigger:
    create a new event window; do not retroactively validate the earlier failed setup.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +10%
  AND MAE <= -30%
  AND company_specific_execution_bridge_missing == true

extreme_hard_4c_event_candidate:
  MAE <= -50%
  AND cashflow_or_margin_or_capital_allocation_bridge_missing == true

local_4b_after_event_mfe:
  MFE >= +12%
  AND later MAE is material
  AND fresh execution evidence is absent

watch_yellow_label_cap:
  MFE < +8%
  AND MAE is not yet hard
  AND bridge is label-only

capped_positive_with_trust_caveat:
  MFE >= +15%
  AND MAE controlled
  AND economic bridge is plausible
  AND listing/event/tradeability caveat exists
  -> capped positive, not ordinary Green

event_window_separation:
  later renewed event == true
  -> create a new event window; do not rescue failed first trigger
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L97_C30_011560","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"011560","name":"세보엠이씨","entry_date":"2024-02-01","entry_price":8520,"mfe_pct":75.4,"mae_pct":-0.7,"r13_verdict":"positive_mep_project_cashflow_bridge_but_green_cap_required_after_large_mfe_without_refreshed_receivables_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C30_010400","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"010400","name":"우진아이엔에스","entry_date":"2024-02-01","entry_price":5200,"mfe_pct":4.0,"mae_pct":-42.3,"r13_verdict":"hard_4c_building_services_contractor_label_without_project_cashflow_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C30_016250","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"MEP_BUILDING_SERVICES_INDUSTRIAL_EPC_PROJECT_CASHFLOW_RECEIVABLES_MARGIN_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"016250","name":"SGC E&C / SGC이테크건설","entry_date":"2024-02-01","entry_price":18790,"mfe_pct":1.7,"mae_pct":-22.3,"r13_verdict":"watch_yellow_industrial_epc_label_without_fresh_project_cashflow_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C31_ENV_029960","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"029960","name":"코엔텍","entry_date":"2024-02-01","entry_price":6600,"mfe_pct":37.3,"mae_pct":-1.8,"r13_verdict":"positive_waste_treatment_permit_capacity_cashflow_bridge_but_inactive_profile_event_caveat_blocks_ordinary_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C31_ENV_067900","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"067900","name":"와이엔텍","entry_date":"2024-02-01","entry_price":7310,"mfe_pct":7.1,"mae_pct":-15.9,"r13_verdict":"watch_yellow_waste_treatment_environmental_service_label_without_incremental_volume_unit_price_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C31_ENV_009440","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"WASTE_ENVIRONMENTAL_REGULATION_PUBLIC_TREATMENT_CAPACITY_PERMIT_CASHFLOW_MARGIN_BRIDGE_VS_ENVIRONMENT_POLICY_LABEL_SPIKE","symbol":"009440","name":"KC그린홀딩스","entry_date":"2024-02-01","entry_price":3010,"mfe_pct":10.1,"mae_pct":-76.6,"r13_verdict":"hard_4c_environmental_pollution_control_holding_label_without_policy_cashflow_margin_trust_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C32_028260","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"028260","name":"삼성물산","entry_date":"2024-02-01","entry_price":148700,"mfe_pct":15.5,"mae_pct":-23.0,"r13_verdict":"local_positive_holding_company_valueup_discount_compression_but_4b_required_after_capital_allocation_evidence_decay","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C32_034730","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"034730","name":"SK","entry_date":"2024-02-01","entry_price":197000,"mfe_pct":7.6,"mae_pct":-35.2,"r13_verdict":"hard_4c_holding_company_governance_discount_label_without_capital_allocation_execution_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L97_C32_000880","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"000880","name":"한화","entry_date":"2024-02-01","entry_price":30000,"mfe_pct":7.3,"mae_pct":-13.8,"r13_verdict":"watch_yellow_group_holding_company_label_without_concrete_capital_allocation_bridge","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":3,"capped_positive_or_bridge_positive_count":3,"watch_yellow_cap_count":3,"local_burst_or_4b_watch_count":2,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":3,"construction_project_cashflow_case_count":3,"environment_policy_cashflow_case_count":3,"holding_company_governance_case_count":3,"event_label_to_execution_bridge_case_count":9,"project_cashflow_receivables_bridge_missing_count":2,"policy_to_cashflow_margin_bridge_missing_count":2,"capital_allocation_execution_bridge_missing_count":2,"event_window_or_execution_evidence_missing_count":4,"accounting_listing_tradeability_trust_caveat_count":7,"old_corporate_action_or_name_history_caveat_count":5,"inactive_or_row_presence_caveat_count":2,"calibration_usable_review_count":9,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":97,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_POLICY_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For construction/project-cashflow, environmental-policy, and holding-company governance archetypes, do not open Stage2-Actionable or Stage3-Green from event salience, sector label, policy label, governance discount label, or holding-company label alone. First classify the event type: C30 MEP/building-services/industrial-EPC/project-cashflow/receivables; C31 environmental regulation/waste treatment/permitted capacity/unit price; or C32 holding-company discount/governance/Value-up/capital allocation. Require the matching bridge: company-specific project exposure, backlog quality, receivables, cash collection, cost risk, working capital, margin/FCF, and row trust for C30; named regulation or public demand, permitted capacity, disposal volume, unit price, capex/utilization, contracts, cash collection, FCF/OP margin, and event/listing/tradeability trust for C31; concrete capital allocation, buyback cancellation, dividend, asset sale, restructuring mechanics, control math, minority protection, approval path, timing/financing/tax/regulatory risk, and price survival for C32. Route shallow-MFE/high-MAE cases to hard-4C; keep meaningful-MFE but unrefreshed execution evidence as capped positive or local 4B; cap label-only cases at Watch/Yellow; apply trust caps for inactive/delisted-like, name-change, old corporate-action, row-presence, raw-last-date divergence, and event-window caveats; separate later event-like spikes from failed first triggers.","expected_effect":"Unifies R10-R12 loop97 event-label guardrails so the model stops confusing MEP/EPC labels, environmental-policy labels, or holding-company Value-up salience with project cashflow, permitted waste-treatment economics, capital-allocation execution, margin conversion, or tradeability trust.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":97,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"event_label_to_execution_cashflow_policy_capital_allocation_trust_guard","contribution":"Reviews nine prior loop97 cases without adding independent evidence weight. Validates a shared event-label-to-execution guard across C30 project cashflow/receivables/trust, C31 environmental policy-to-cashflow/margin/tradeability, and C32 holding-company capital-allocation/governance execution.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_POLICY_CAPITAL_ALLOCATION_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop97 files:
   - C30 MEP/building-services/industrial-EPC project cashflow and receivables
   - C31 environmental/waste-treatment policy-to-capacity/cashflow/margin
   - C32 holding-company Value-up/governance capital-allocation execution
7. If enough R13 reviews agree, consider implementing a pre-scoring check for event/policy/governance archetypes:
   - classify the event type first,
   - identify the true company-level economic/legal/cashflow/capital-allocation bridge,
   - block event-label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - cap shallow label-only cases at Watch/Yellow,
   - separate renewed event windows from failed first triggers,
   - apply name-change/inactive-listing/short-listing/row-presence/raw-date/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 97
next_round = R1
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 97
next_round = R1
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
