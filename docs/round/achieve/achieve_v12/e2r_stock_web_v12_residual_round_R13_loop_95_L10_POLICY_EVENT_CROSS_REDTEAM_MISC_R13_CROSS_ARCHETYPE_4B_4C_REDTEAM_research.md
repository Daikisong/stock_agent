# E2R Stock-Web v12 Residual Research — R13 / Loop 95

```yaml
scheduled_round: R13
scheduled_loop: 95
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: PROJECT_CASHFLOW_TOURISM_TRAFFIC_CARBON_POLICY_EXECUTION_TRUST_REDTEAM

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
reviewed_original_canonical_count: 2
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE
  - TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE
  - CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
local_burst_or_4b_watch_count: 4
watch_yellow_cap_count: 1
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 4

construction_project_cashflow_case_count: 3
tourism_traffic_margin_case_count: 3
carbon_environment_project_case_count: 3
policy_event_execution_bridge_case_count: 9

market_transfer_caveat_count: 1
foreign_listing_caveat_count: 1
corporate_action_caveat_avoided_count: 1
row_presence_or_tradeability_caveat_count: 2
accounting_or_listing_trust_caveat_count: 4
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 95
next_round: R1
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 95
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a normal sector-specific expansion round. It is the cross-archetype checkpoint for:

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
next_loop = 96
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop95 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 028100 동아지질
  - 002150 도화엔지니어링
  - 025950 동신건설

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 034230 파라다이스
  - 950170 JTC
  - 008770 호텔신라

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 083420 그린케미칼
  - 448280 에코아이
  - 119650 KC코트렐
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
C30 engineering / groundwork / small-builder construction:
  construction or infrastructure policy salience exists,
  but equity value depends on project cash collection, receivables, backlog quality, funding terms, cost risk, margin, and trust.

C31 tourism / inbound / casino / duty-free policy:
  tourism or travel-flow salience exists,
  but equity value depends on visitor traffic, spend, channel costs, FX, revenue recognition, and margin.

C31 carbon / CCUS / environmental EPC policy:
  climate-policy or green-policy salience exists,
  but equity value depends on verified project, monetizable credit, certification, cash collection, revenue recognition, margin, and tradeability trust.
```

Shared false-positive mechanism:

```text
external policy / event salience
  -> recognizable sector label becomes hot
  -> price reacts first
  -> model over-promotes label to Stage2-Actionable / Stage3-Green
  -> company-specific execution bridge is missing or stale
  -> shallow MFE, high MAE, Watch cap, local 4B, or hard 4C follows
```

Shared guardrail:

```text
The event rings the bell.
C30 asks whether project cash and trust hold the scaffolding.
C31 tourism asks whether visitors arrive, spend, and leave margin.
C31 carbon asks whether the green permit becomes verified credits, paid projects, collected cash, and operating margin.
```

---

## 4. Reviewed case matrix

| Original canonical | Fine branch | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---|---:|---|---:|---:|---:|---|
| C30 | project cashflow / trust | 028100 | 동아지질 | 13,320 | +16.9% | -13.3% | capped groundwork/infrastructure positive; project cashflow and trust required |
| C30 | project cashflow / trust | 002150 | 도화엔지니어링 | 7,840 | +5.6% | -19.0% | Watch/Yellow cap; engineering label without cashflow bridge |
| C30 | project cashflow / trust | 025950 | 동신건설 | 30,850 | +3.2% | -43.2% | hard 4C; small-builder policy spike with row/tradeability caveat |
| C31 | tourism / inbound | 034230 | 파라다이스 | 12,930 | +21.5% | -22.3% | local casino/inbound positive; 4B after later MAE and market-transfer caveat |
| C31 | tourism / inbound | 950170 | JTC | 3,940 | +49.5% | -1.5% | duty-free inbound positive; foreign-listing/FX caveat and 4B watch |
| C31 | tourism / inbound | 008770 | 호텔신라 | 58,900 | +7.0% | -31.2% | hard 4C; duty-free/hotel label without traffic-to-margin survival |
| C31 | carbon / environment | 083420 | 그린케미칼 | 7,340 | +29.3% | -25.2% | CCUS/green-chemical local positive; 4B after later MAE |
| C31 | carbon / environment | 448280 | 에코아이 | 39,800 | +4.6% | -58.6% | hard 4C; carbon-credit label without verified project/revenue survival |
| C31 | carbon / environment | 119650 | KC코트렐 | 1,403 | +2.4% | -74.9% | hard 4C; environmental EPC label with cashflow/trust failure |

---

## 5. R10 review — construction project cashflow, backlog, and trust

### 5.1 028100 동아지질

```text
entry_close: 13,320
peak_high: 15,570
MFE: +16.9%
worst_low_after_entry: 11,550
MAE: -13.3%
```

R13 interpretation:

```text
This is the constructive C30 case in the loop95 holdout set.
The move had enough post-trigger MFE to preserve a capped positive.
The drawdown was material but not hard-failure.
```

Classification:

```text
positive_control = true
capped_positive = true
green_block_without_project_cashflow_trust = true
```

This is the "specialty construction can work" case, but not a Green case. The model still needs project cash collection, receivables, backlog quality, execution timing, and margin trust.

### 5.2 002150 도화엔지니어링

```text
entry_close: 7,840
peak_high: 8,280
MFE: +5.6%
worst_low_after_entry: 6,350
MAE: -19.0%
```

R13 interpretation:

```text
This is the engineering-design Watch cap.
The label was relevant, but MFE was shallow and the project-cash bridge was weak.
```

Classification:

```text
watch_yellow_cap = true
actionable_block_without_project_cashflow_bridge = true
```

Controlled or moderate drawdown alone is not enough. Engineering/infrastructure relevance still has to become project orders, receivables, and margin.

### 5.3 025950 동신건설

```text
entry_close: 30,850
peak_high_after_entry: 31,850
MFE: +3.2%
worst_low_after_entry: 17,530
MAE: -43.2%
```

R13 interpretation:

```text
This is the hard C30 failure.
It behaved like a small-builder policy/political beta spike rather than a balance-sheet or project-cash repair event.
```

Classification:

```text
hard_4c_candidate = true
small_builder_policy_spike_guard = true
row_presence_or_tradeability_caveat = true
stage2_actionable_block = true
```

The model should not confuse small-builder price heat with PF/cashflow repair.

---

## 6. R11 review — tourism traffic, spend, FX, and margin

### 6.1 034230 파라다이스

```text
entry_close: 12,930
peak_high: 15,710
MFE: +21.5%
worst_low_after_entry: 10,050
MAE: -22.3%
market_transfer_caveat: KOSDAQ -> KOSPI in 2024
```

R13 interpretation:

```text
This is a casino/inbound local positive.
The trade worked first, but later drawdown shows that traffic-to-margin evidence must refresh before Green.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
market_transfer_caveat = true
tourism_traffic_margin_bridge_required = true
```

The model should hold this as local 4B after the initial rerating unless casino drop, occupancy, spend, and margin bridge refresh.

### 6.2 950170 JTC

```text
entry_close: 3,940
peak_high: 5,890
MFE: +49.5%
worst_low_after_entry: 3,880
MAE: -1.5%
foreign_listing_caveat: true
```

R13 interpretation:

```text
This is the strongest positive in the loop95 R13 review.
The path had large MFE and controlled MAE, but the thesis is still foreign-listing / FX / inbound-spend sensitive.
```

Classification:

```text
positive_control = true
capped_positive = true
foreign_listing_caveat = true
local_4b_watch_after_large_mfe = true
```

The model may preserve positive classification, but Green should stay capped unless sales, duty-free basket, FX, and margin evidence refresh.

### 6.3 008770 호텔신라

```text
entry_close: 58,900
peak_high: 63,000
MFE: +7.0%
worst_low_after_entry: 40,500
MAE: -31.2%
```

R13 interpretation:

```text
This is the duty-free/hotel hard failure.
Tourism relevance existed, but rent, commission, promotion, inventory, and China demand mix broke the traffic-to-margin bridge.
```

Classification:

```text
hard_4c_candidate = true
tourism_label_false_positive = true
green_block_without_margin_bridge = true
```

The model should not promote hotel/duty-free inbound labels without visible traffic-to-sales and margin conversion.

---

## 7. R12 review — carbon policy, verified project, revenue, and trust

### 7.1 083420 그린케미칼

```text
entry_close: 7,340
peak_high: 9,490
MFE: +29.3%
worst_low_after_entry: 5,490
MAE: -25.2%
```

R13 interpretation:

```text
This is the constructive carbon/CCUS local positive.
The first move worked, but the project/revenue/margin bridge did not refresh enough for Green.
```

Classification:

```text
positive_control = true
local_4b_overlay = true
green_block_without_project_revenue_margin_bridge = true
```

The model should keep the local positive but attach 4B after material MAE unless verified project and revenue evidence appears.

### 7.2 448280 에코아이

```text
entry_close: 39,800
peak_high: 41,650
MFE: +4.6%
worst_low_after_entry: 16,480
MAE: -58.6%
```

R13 interpretation:

```text
This is the carbon-credit hard failure.
Carbon-credit salience did not become verified credit generation, credit sales, revenue recognition, or cash collection.
```

Classification:

```text
hard_4c_candidate = true
carbon_credit_label_false_positive = true
green_block_without_verified_credit_monetization = true
```

The model must not promote carbon-credit labels without project-level monetization and certification.

### 7.3 119650 KC코트렐

```text
entry_close: 1,403
peak_high_after_entry: 1,437
MFE: +2.4%
worst_low_after_entry: 352
MAE: -74.9%
corporate_action_caveat_avoided: entry after 2024-03-25 candidate
row_presence_or_tradeability_caveat: true
```

R13 interpretation:

```text
This is the environmental EPC / accounting-trust hard failure.
Even after avoiding the immediate corporate-action candidate window, the post-trigger path failed severely.
```

Classification:

```text
hard_4c_candidate = true
environmental_epc_label_false_positive = true
corporate_action_caveat_avoided = true
row_presence_or_tradeability_caveat = true
project_cashflow_trust_bridge_missing = true
```

The model should route environmental EPC labels to hard 4C when named project, receivables, cash collection, and tradeability trust are missing.

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_POLICY_EVENT_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED

For policy/event archetypes across construction, tourism, and carbon/environment:

  Do not open Stage2-Actionable or Stage3-Green from event salience or sector label alone.

  First classify the event type:
    - C30 construction / project cashflow / backlog / trust event
    - C31 tourism / visitor traffic / spend / margin event
    - C31 carbon / credit / CCUS / environmental project event

  Then require the matching bridge:
    - C30: project cash, receivables, backlog, funding, cost risk, margin, tradeability trust
    - C31 tourism: visitor traffic, spend, casino drop, hotel occupancy, duty-free basket, FX, cost structure, margin
    - C31 carbon/environment: named project, monetizable credit, verification, cash collection, revenue recognition, margin, trust

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but execution evidence is not refreshed:
    preserve as capped positive or local 4B rather than Green.

  If MFE is shallow and MAE is moderate:
    cap at Watch/Yellow unless the execution bridge is explicit.

  If corporate-action, market-transfer, foreign-listing, row-presence, or tradeability caveat appears:
    apply additional trust cap and block contaminated windows.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +10%
  AND MAE <= -30%
  AND company_specific_execution_bridge_missing == true

extreme_hard_4c_event_candidate:
  MFE < +8%
  AND MAE <= -50%
  AND project_or_monetization_bridge_missing == true

watch_cap_event_candidate:
  MFE < +8%
  AND MAE is controlled or moderate
  AND event relevance exists
  AND company-specific economic bridge is weak

capped_positive_event_candidate:
  MFE >= +15%
  AND MAE is not hard-failure
  AND event-company bridge is plausible
  BUT Green bridge is incomplete

local_4b_after_event_mfe:
  MFE >= +15%
  AND later MAE is material
  AND fresh execution evidence is absent

trust_caveat_cap:
  corporate_action_candidate_inside_window == true
  OR market_transfer_inside_validation_year == true
  OR foreign_listing_caveat == true
  OR row_presence_tradeability_caveat == true
  -> block contaminated rows and cap actionability
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L95_C30_028100","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"028100","name":"동아지질","entry_date":"2024-07-24","entry_price":13320,"mfe_pct":16.9,"mae_pct":-13.3,"r13_verdict":"positive_capped_groundwork_infra_project_execution_but_project_cashflow_trust_bridge_required_for_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C30_002150","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"002150","name":"도화엔지니어링","entry_date":"2024-07-24","entry_price":7840,"mfe_pct":5.6,"mae_pct":-19.0,"r13_verdict":"watch_yellow_cap_engineering_design_label_without_project_cashflow_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C30_025950","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","original_fine_archetype_id":"ENGINEERING_GROUNDWORK_SMALL_BUILDER_PF_PROJECT_CASHFLOW_TRUST_BRIDGE_VS_CONSTRUCTION_POLICY_SPIKE","symbol":"025950","name":"동신건설","entry_date":"2024-03-25","entry_price":30850,"mfe_pct":3.2,"mae_pct":-43.2,"r13_verdict":"hard_4c_small_builder_policy_spike_without_pf_project_cashflow_trust_bridge_with_tradeability_caveat","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_TOURISM_034230","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"034230","name":"파라다이스","entry_date":"2024-02-01","entry_price":12930,"mfe_pct":21.5,"mae_pct":-22.3,"r13_verdict":"local_positive_casino_inbound_tourism_traffic_with_4b_after_market_transfer_and_later_mae","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_TOURISM_950170","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"950170","name":"JTC","entry_date":"2024-02-01","entry_price":3940,"mfe_pct":49.5,"mae_pct":-1.5,"r13_verdict":"positive_dutyfree_inbound_tourism_spend_recovery_with_foreign_listing_caveat_and_4b_watch","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_TOURISM_008770","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"008770","name":"호텔신라","entry_date":"2024-02-01","entry_price":58900,"mfe_pct":7.0,"mae_pct":-31.2,"r13_verdict":"hard_4c_dutyfree_hotel_inbound_label_without_traffic_to_margin_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_CARBON_083420","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"083420","name":"그린케미칼","entry_date":"2024-03-12","entry_price":7340,"mfe_pct":29.3,"mae_pct":-25.2,"r13_verdict":"local_positive_ccus_green_chemical_policy_spike_with_4b_after_later_mae","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_CARBON_448280","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"448280","name":"에코아이","entry_date":"2024-02-22","entry_price":39800,"mfe_pct":4.6,"mae_pct":-58.6,"r13_verdict":"hard_4c_carbon_credit_policy_label_without_verified_project_revenue_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L95_C31_CARBON_119650","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","original_fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"119650","name":"KC코트렐","entry_date":"2024-03-26","entry_price":1403,"mfe_pct":2.4,"mae_pct":-74.9,"r13_verdict":"hard_4c_environmental_epc_policy_label_without_project_cashflow_tradeability_trust","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":2,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"local_burst_or_4b_watch_count":4,"watch_yellow_cap_count":1,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":4,"construction_project_cashflow_case_count":3,"tourism_traffic_margin_case_count":3,"carbon_environment_project_case_count":3,"policy_event_execution_bridge_case_count":9,"market_transfer_caveat_count":1,"foreign_listing_caveat_count":1,"corporate_action_caveat_avoided_count":1,"row_presence_or_tradeability_caveat_count":2,"accounting_or_listing_trust_caveat_count":4,"calibration_usable_review_count":9,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":95,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_POLICY_EVENT_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy/event archetypes across construction, tourism, and carbon/environment, do not open Stage2-Actionable or Stage3-Green from event salience or sector label alone. Classify the event type first: C30 construction/project-cashflow/backlog/trust, C31 tourism/visitor-traffic/spend/margin, or C31 carbon/credit/CCUS/environmental-project. Require the matching bridge: project cash, receivables, backlog, funding, cost risk, margin, and tradeability trust for C30; visitor traffic, spend, casino drop, hotel occupancy, duty-free basket, FX, cost structure, and margin for C31 tourism; named project, monetizable credit, verification, cash collection, revenue recognition, margin, and trust for C31 carbon/environment. Route shallow-MFE/high-MAE cases to hard 4C; keep meaningful-MFE but unrefreshed bridges as capped positive or local 4B; cap shallow-MFE/moderate-MAE labels at Watch/Yellow unless the execution bridge is explicit; apply additional trust caps when corporate-action, market-transfer, foreign-listing, row-presence, or tradeability caveats appear.","expected_effect":"Unifies L10 policy/event guardrails so the model stops confusing policy salience with company-specific cashflow, tourism spend, carbon-credit monetization, project execution, margin conversion, or tradeability trust.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":95,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"policy_event_label_to_execution_cashflow_margin_trust_guard","contribution":"Reviews nine prior loop95 cases without adding new independent evidence weight. Validates a shared policy-event label-to-execution guard across construction project cashflow, tourism traffic-to-margin, and carbon/environment project monetization.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_POLICY_EVENT_LABEL_TO_EXECUTION_CASHFLOW_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop95 files:
   - C30 engineering/groundwork/small-builder project cashflow/trust
   - C31 tourism/inbound/casino/duty-free traffic-to-margin
   - C31 carbon/CCUS/environmental EPC project/revenue/trust
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/event archetypes:
   - classify the event type first,
   - identify the true company-level economic/legal/cashflow bridge,
   - block event-label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - cap shallow-MFE/moderate-MAE labels at Watch/Yellow,
   - apply corporate-action/market-transfer/foreign-listing/row-presence/tradeability trust caps.

Expected next schedule:
completed_round = R13
completed_loop = 95
next_round = R1
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 95
next_round = R1
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
