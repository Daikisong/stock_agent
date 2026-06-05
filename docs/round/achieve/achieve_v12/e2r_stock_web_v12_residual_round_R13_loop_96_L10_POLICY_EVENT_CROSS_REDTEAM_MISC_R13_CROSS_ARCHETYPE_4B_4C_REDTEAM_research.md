# E2R Stock-Web v12 Residual Research — R13 / Loop 96

```yaml
scheduled_round: R13
scheduled_loop: 96
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: CONSTRUCTION_PROJECT_CASHFLOW_GOVERNANCE_TENDER_LOW_BIRTHRATE_POLICY_EXECUTION_TRUST_REDTEAM

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
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE
  - TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
  - LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
local_burst_or_4b_watch_count: 3
watch_yellow_cap_count: 0
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 4

construction_project_cashflow_case_count: 3
governance_tender_control_case_count: 3
low_birthrate_policy_case_count: 3
event_label_to_execution_bridge_case_count: 9

name_change_caveat_count: 1
delisting_or_inactive_profile_caveat_count: 2
short_listing_caveat_count: 1
row_presence_or_tradeability_caveat_count: 3
event_window_separation_required_count: 1
accounting_listing_tradeability_trust_caveat_count: 6
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 96
next_round: R1
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 96
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a normal new sector-expansion round. It is a cross-archetype checkpoint for:

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
next_loop = 97
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop96 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 028050 삼성엔지니어링 / 삼성E&A
  - 097230 HJ중공업
  - 026150 특수건설

R11 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 119860 커넥트웨이브
  - 115390 락앤락
  - 008930 한미사이언스

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 407400 꿈비
  - 159580 제로투세븐
  - 014100 메디앙스
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
C30 EPC / construction / infrastructure:
  project, EPC, construction, infrastructure, or contractor label exists,
  but equity value depends on project cash collection, receivables, backlog quality,
  cost overrun control, funding, margin, FCF, and tradeability trust.

C32 governance / tender / control:
  governance or control-premium salience exists,
  but equity value depends on binding offer or control path, offer spread,
  financing, acceptance math, minority exit, event-window separation, and liquidity/tradeability.

C31 low-birthrate / childcare / baby product policy:
  policy and baby-product salience exists,
  but equity value depends on household purchase conversion, channel sell-through,
  inventory, subsidy friction, promotion/logistics cost, revenue, margin, and tradeability trust.
```

Shared false-positive mechanism:

```text
external event or policy salience
  -> recognizable sector/governance label becomes hot
  -> price reacts first
  -> model over-promotes label to Stage2-Actionable / Stage3-Green
  -> company-specific execution bridge is missing or stale
  -> shallow MFE, high MAE, local 4B, or hard 4C follows
```

Shared guardrail:

```text
The headline rings the bell.
C30 asks whether project cash and receivables hit the ledger.
C32 asks whether the exit door has a binding price, financing, acceptance math, and minority path.
C31 low-birthrate asks whether the policy voucher reaches households, turns into product sell-through, and leaves margin.
```

---

## 4. Reviewed case matrix

| Original canonical | Fine branch | Symbol | Name | Entry | MFE | MAE / post-close metric | R13 verdict |
|---|---|---:|---|---:|---:|---:|---|
| C30 | EPC / project cashflow | 028050 | 삼성엔지니어링 / 삼성E&A | 23,250 | +26.0% | -24.5% | local EPC positive; 4B required when project-cashflow evidence stale |
| C30 | mixed contractor trust | 097230 | HJ중공업 | 3,480 | +7.3% | -37.4% | hard 4C; mixed construction/shipbuilding label without cashflow trust |
| C30 | civil specialty construction | 026150 | 특수건설 | 7,920 | +2.8% | -30.9% | hard 4C candidate; infrastructure spike without project cashflow |
| C32 | tender / delisting | 119860 | 커넥트웨이브 | 15,570 | +15.9% | +13.7% post-close low vs entry | capped tender positive; inactive/delisting caveat |
| C32 | tender / minority exit | 115390 | 락앤락 | 8,180 | +8.7% | +1.1% post-close low vs entry | capped tender positive; ordinary Green blocked |
| C32 | control dispute | 008930 | 한미사이언스 | 44,350 | +6.0% | -41.9% first-phase | hard 4C; later renewed event must be separate |
| C31 | low-birthrate policy | 407400 | 꿈비 | 8,040 | +22.1% | -27.9% | childcare policy local positive; 4B after later MAE |
| C31 | infant-product policy | 159580 | 제로투세븐 | 6,500 | +13.8% | -41.5% | local 4B failure; policy label failed survival |
| C31 | baby-product policy | 014100 | 메디앙스 | 3,690 | +0.9% | -45.8% | hard 4C; event spike without sell-through/margin trust |

---

## 5. R10 review — construction project cashflow, receivables, and trust

### 5.1 028050 삼성엔지니어링 / 삼성E&A

```text
entry_close: 23,250
peak_high: 29,300
MFE: +26.0%
worst_low_after_entry: 17,550
MAE: -24.5%
name_change_caveat: 삼성엔지니어링 -> 삼성E&A in 2024
```

R13 interpretation:

```text
This is the constructive C30 case in the loop96 holdout set.
The move produced enough MFE to preserve a local positive.
The later drawdown proves that EPC/backlog label should not stay Green without refreshed project-cashflow, receivables, cost, and margin evidence.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
green_block_without_project_cashflow_trust = true
```

### 5.2 097230 HJ중공업

```text
entry_close: 3,480
peak_high: 3,735
MFE: +7.3%
worst_low_after_entry: 2,180
MAE: -37.4%
```

R13 interpretation:

```text
This is the mixed-contractor hard failure.
Construction/infrastructure relevance existed, but the path did not validate project-cashflow repair.
The construction/shipbuilding identity also creates a cross-sector caveat.
```

Classification:

```text
hard_4c_candidate = true
project_cashflow_trust_bridge_missing = true
cross_sector_confound_caveat = true
row_presence_or_tradeability_caveat = true
```

### 5.3 026150 특수건설

```text
entry_close: 7,920
peak_high_after_entry: 8,140
MFE: +2.8%
worst_low_after_entry: 5,470
MAE: -30.9%
```

R13 interpretation:

```text
This is the civil-specialty construction event-spike guardrail.
The tunnel/rail/infrastructure label did not become named project cashflow, receivables, cost control, or margin.
The high historical non-tradable zero-volume count adds a trust cap.
```

Classification:

```text
hard_4c_candidate = true
civil_specialty_event_spike_guard = true
row_presence_or_tradeability_caveat = true
```

---

## 6. R11 review — governance tender, spread, and event-window separation

### 6.1 119860 커넥트웨이브

```text
entry_close: 15,570
peak_high: 18,040
MFE: +15.9%
post_close_worst_low: 17,700
post_close_mae_pct: +13.7% relative to entry
inactive/delisted-like profile caveat: true
```

R13 interpretation:

```text
This is a true C32 tender/delisting positive.
It worked because the event had a price anchor and the stock compressed toward the tender cap.
It must not be scored as ordinary operating Green because the upside is bounded by offer spread and execution mechanics.
```

Classification:

```text
positive_control = true
capped_positive = true
ordinary_green_block = true
delisting_or_inactive_profile_caveat = true
```

### 6.2 115390 락앤락

```text
entry_close: 8,180
peak_high: 8,890
MFE: +8.7%
post_close_worst_low: 8,270
post_close_mae_pct: +1.1% relative to entry
inactive/delisted-like profile caveat: true
```

R13 interpretation:

```text
This is the second C32 tender/minority-exit positive.
The event window behaved like capped spread convergence.
It should remain Actionable only as a tender spread/minority exit trade, not as operating Green.
```

Classification:

```text
positive_control = true
capped_positive = true
ordinary_green_block = true
delisting_or_inactive_profile_caveat = true
```

### 6.3 008930 한미사이언스

```text
entry_close: 44,350
peak_high_first_phase: 47,000
MFE: +6.0%
worst_low_before_later_reignition: 25,750
MAE: -41.9%
later renewed event: October 2024
```

R13 interpretation:

```text
This is the control-dispute hard failure for the first event phase.
The later renewed October control event cannot retroactively validate the March trigger.
C32 must separate event windows.
```

Classification:

```text
hard_4c_candidate = true
event_window_separation_required = true
binding_control_path_missing = true
```

---

## 7. R12 review — low-birthrate policy to household purchase and margin

### 7.1 407400 꿈비

```text
entry_close: 8,040
peak_high: 9,820
MFE: +22.1%
worst_low_after_entry: 5,800
MAE: -27.9%
short_listing_caveat: true
```

R13 interpretation:

```text
This is the constructive low-birthrate policy local positive.
The first move worked, but later price survival failed.
The policy-to-household-purchase-to-margin bridge did not refresh enough for Green.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
short_listing_caveat = true
green_block_without_purchase_margin_bridge = true
```

### 7.2 159580 제로투세븐

```text
entry_close: 6,500
peak_high: 7,400
MFE: +13.8%
worst_low_after_entry: 3,805
MAE: -41.5%
```

R13 interpretation:

```text
This is the infant-product local burst / 4B failure.
The label had real policy relevance, but household conversion, sell-through, channel inventory, and margin survival failed.
```

Classification:

```text
local_4b_failure = true
stage2_false_positive_or_high_mae = true
green_block_without_sellthrough_margin_bridge = true
```

### 7.3 014100 메디앙스

```text
entry_close: 3,690
peak_high_after_entry: 3,725
MFE: +0.9%
worst_low_after_entry: 2,000
MAE: -45.8%
row_presence_or_tradeability_caveat: true
```

R13 interpretation:

```text
This is the baby-product policy hard failure.
The policy heat did not become household purchase, channel sell-through, inventory control, or margin.
The high historical zero-volume row count adds a trust cap.
```

Classification:

```text
hard_4c_candidate = true
baby_product_policy_event_spike_guard = true
row_presence_or_tradeability_caveat = true
```

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_SPREAD_PURCHASE_MARGIN_TRUST_BRIDGE_REQUIRED

For construction, governance/tender, and low-birthrate policy event archetypes:

  Do not open Stage2-Actionable or Stage3-Green from event salience or sector/governance label alone.

  First classify the event type:
    - C30: construction / EPC / project-cashflow / receivables / trust
    - C32: tender / delisting / control dispute / minority exit
    - C31 low-birthrate: childcare policy / household purchase / baby-product demand

  Then require the matching bridge:
    - C30:
        project exposure, backlog quality, receivables, cash collection,
        funding, cost risk, margin, FCF, and tradeability trust.
    - C32:
        binding offer or concrete control event, offer spread,
        financing, acceptance math, regulatory/court/shareholder-meeting path,
        minority exit, event-window separation, and liquidity/tradeability.
    - C31 low-birthrate:
        named policy benefit, addressable households, purchase conversion,
        sell-through, channel inventory, subsidy friction, promotion/logistics cost,
        gross margin, OP conversion, and tradeability trust.

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but execution evidence is not refreshed:
    preserve as capped positive or local 4B rather than Green.

  If a tender/delisting event is concrete:
    score it as capped spread / minority-exit trade, not ordinary operating Green.

  If a later renewed event appears:
    create a new event window; do not retroactively validate a failed earlier trigger.

  If name-change, inactive/delisted-like, short-listing, row-presence, or tradeability caveat appears:
    apply an additional trust cap.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +10%
  AND MAE <= -30%
  AND company_specific_execution_bridge_missing == true

extreme_hard_4c_event_candidate:
  MFE < +5%
  AND MAE <= -40%
  AND cashflow_or_purchase_or_control_bridge_missing == true

local_4b_after_event_mfe:
  MFE >= +12%
  AND later MAE is material
  AND fresh execution evidence is absent

tender_capped_positive:
  concrete tender/delisting event == true
  AND offer spread compresses
  AND post-close downside is controlled
  -> Actionable only as capped spread trade, not ordinary Green

event_window_separation:
  later renewed event == true
  -> create new event window; do not rescue failed first trigger

trust_caveat_cap:
  name_change_caveat == true
  OR inactive/delisted_like_profile == true
  OR short_listing_caveat == true
  OR row_presence_tradeability_caveat == true
  -> cap actionability and block contaminated windows
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L96_C30_028050","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"028050","name":"삼성엔지니어링/삼성E&A","entry_date":"2024-02-01","entry_price":23250,"mfe_pct":26.0,"mae_pct":-24.5,"r13_verdict":"local_positive_epc_engineering_project_backlog_cashflow_bridge_but_4b_required_without_refreshed_project_cashflow_margin_evidence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C30_097230","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"097230","name":"HJ중공업","entry_date":"2024-02-01","entry_price":3480,"mfe_pct":7.3,"mae_pct":-37.4,"r13_verdict":"hard_4c_mixed_construction_shipbuilding_label_without_project_cashflow_trust_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C30_026150","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"EPC_ENGINEERING_CIVIL_SPECIALTY_CONTRACTOR_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_LABEL_SPIKE","symbol":"026150","name":"특수건설","entry_date":"2024-07-30","entry_price":7920,"mfe_pct":2.8,"mae_pct":-30.9,"r13_verdict":"hard_4c_candidate_civil_specialty_construction_event_spike_without_project_cashflow_margin_trust_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C32_119860","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"119860","name":"커넥트웨이브","entry_date":"2024-04-26","entry_price":15570,"mfe_pct":15.9,"post_close_mae_pct":13.7,"r13_verdict":"positive_capped_tender_offer_delisting_spread_with_inactive_profile_caveat_not_ordinary_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C32_115390","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"115390","name":"락앤락","entry_date":"2024-04-17","entry_price":8180,"mfe_pct":8.7,"post_close_mae_pct":1.1,"r13_verdict":"positive_capped_tender_offer_minority_exit_with_delisting_profile_caveat_not_ordinary_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C32_008930","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","original_fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"008930","name":"한미사이언스","entry_date":"2024-03-28","entry_price":44350,"mfe_pct":6.0,"mae_pct":-41.9,"r13_verdict":"hard_4c_control_dispute_first_phase_without_binding_control_path_before_later_reignition","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C31_LOW_BIRTHRATE_407400","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"407400","name":"꿈비","entry_date":"2024-04-22","entry_price":8040,"mfe_pct":22.1,"mae_pct":-27.9,"r13_verdict":"local_positive_childcare_policy_baby_product_but_4b_required_without_refreshed_household_purchase_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C31_LOW_BIRTHRATE_159580","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"159580","name":"제로투세븐","entry_date":"2024-02-01","entry_price":6500,"mfe_pct":13.8,"mae_pct":-41.5,"r13_verdict":"local_4b_failure_infant_product_low_birthrate_policy_label_without_purchase_conversion_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L96_C31_LOW_BIRTHRATE_014100","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"014100","name":"메디앙스","entry_date":"2024-03-21","entry_price":3690,"mfe_pct":0.9,"mae_pct":-45.8,"r13_verdict":"hard_4c_baby_product_policy_event_spike_without_sellthrough_margin_tradeability_trust","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"local_burst_or_4b_watch_count":3,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":4,"construction_project_cashflow_case_count":3,"governance_tender_control_case_count":3,"low_birthrate_policy_case_count":3,"event_label_to_execution_bridge_case_count":9,"name_change_caveat_count":1,"delisting_or_inactive_profile_caveat_count":2,"short_listing_caveat_count":1,"row_presence_or_tradeability_caveat_count":3,"event_window_separation_required_count":1,"accounting_listing_tradeability_trust_caveat_count":6,"calibration_usable_review_count":9,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":96,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_SPREAD_PURCHASE_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For construction, governance/tender, and low-birthrate policy event archetypes, do not open Stage2-Actionable or Stage3-Green from event salience, sector label, governance headline, or policy label alone. Classify the event type first: C30 construction/project cashflow/receivables/trust; C32 tender/delisting/control dispute/minority exit; or C31 low-birthrate/childcare/household purchase/baby-product demand. Require the matching bridge: project exposure, backlog, receivables, cash collection, funding, cost risk, margin, FCF, and tradeability trust for C30; binding offer or concrete control event, spread, financing, acceptance math, legal/regulatory/shareholder-meeting path, minority exit, event-window separation, and liquidity/tradeability for C32; named policy benefit, household conversion, sell-through, channel inventory, subsidy friction, promotion/logistics cost, gross margin, OP conversion, and tradeability trust for C31 low-birthrate. Route shallow-MFE/high-MAE cases to hard-4C; keep meaningful-MFE but unrefreshed bridges as capped positive or local 4B; score concrete tender/delisting positives as capped spread trades rather than ordinary Green; separate later renewed event windows from failed first triggers; apply additional trust caps for name-change, inactive/delisted-like, short-listing, row-presence, or tradeability caveats.","expected_effect":"Unifies R10-R12 loop96 event-label guardrails so the model stops confusing construction/EPC labels, tender/control headlines, or low-birthrate policy salience with project cashflow, binding spread mechanics, household purchase conversion, margin conversion, or tradeability trust.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":96,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"event_label_to_execution_cashflow_spread_purchase_margin_trust_guard","contribution":"Reviews nine prior loop96 cases without adding independent evidence weight. Validates a shared event-label-to-execution guard across C30 project cashflow/trust, C32 tender/control spread mechanics, and C31 low-birthrate household-purchase-to-margin policy conversion.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_EVENT_LABEL_TO_EXECUTION_CASHFLOW_SPREAD_PURCHASE_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop96 files:
   - C30 EPC/civil/mixed-contractor project cashflow/trust
   - C32 tender/delisting/control-dispute spread and event-window mechanics
   - C31 low-birthrate/childcare/baby-product policy-to-purchase/margin conversion
7. If enough R13 reviews agree, consider implementing a pre-scoring check for event/policy/governance archetypes:
   - classify the event type first,
   - identify the true company-level economic/legal/cashflow bridge,
   - block event-label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - score tender/delisting cases as capped spread trades, not ordinary Green,
   - separate renewed event windows from failed first triggers,
   - apply name-change/inactive-listing/short-listing/row-presence/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 96
next_round = R1
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 96
next_round = R1
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
