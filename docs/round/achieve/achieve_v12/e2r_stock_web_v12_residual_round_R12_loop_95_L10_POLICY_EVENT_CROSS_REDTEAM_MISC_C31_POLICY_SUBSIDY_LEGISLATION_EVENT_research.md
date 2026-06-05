# E2R Stock-Web v12 Residual Research — R12 / Loop 95

```yaml
scheduled_round: R12
scheduled_loop: 95
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE

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

new_independent_case_count: 3
same_archetype_new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
carbon_credit_policy_case_count: 1
ccus_chemical_case_count: 1
environmental_epc_case_count: 1
corporate_action_caveat_avoided_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 95
next_round: R13
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 95
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy / event / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

The selected fine branch is:

```text
carbon credit / CCUS / environmental EPC policy
revenue, project cashflow, compliance, and margin bridge
vs generic green-policy label spike
```

This deliberately avoids:
- the loop95 R11 C31 tourism / inbound / casino / duty-free branch;
- the loop94 R12 C31 education-policy branch;
- the loop93 food-security / agri-input policy branch;
- the loop91 travel-service policy branch names;
- the C31 top-covered symbols.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows: 97
symbols: 70
date_range: 2020-01-23~2025-01-17
good/bad S2: 35/25
4B/4C: 5/0
URL pending/proxy: 25/25
top covered symbols:
  013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
```

Selected symbols:

```text
083420 그린케미칼
448280 에코아이
119650 KC코트렐
```

They avoid the C31 top-covered symbols and recent L10 policy names:

```text
R11 loop95 avoid: 034230, 950170, 008770
R12 loop94 avoid: 096240, 072870, 095720
R11 loop94 avoid: 003920, 001750, 003240
R12 loop93 avoid: 008040, 054050, 002900
R12 loop92 avoid: 133750, 053290, 215200
R12 loop91 avoid: 039130, 080160, 094850
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
083420: same archetype, new symbol, CCUS / green-chemical policy local positive with 4B after later MAE
448280: same archetype, new symbol, carbon-credit policy label hard-4C without project/revenue survival
119650: same archetype, new symbol, environmental EPC / carbon-policy label hard-4C with corporate-action and tradeability trust caveat
```

---

## 3. Price-atlas validation

Manifest fields checked from stock-web:

```text
source_name: FinanceData/marcap
source_repo_url: https://github.com/FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
inactive_or_delisted_like_symbol_count: 2,546
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/all_symbols.csv
```

Profile checks:

```text
083420 그린케미칼
  profile: atlas/symbol_profiles/083/083420.json
  name history:
    그린소프트켐 -> KPX그린케미칼 -> 그린케미칼
  first_date: 2005-10-20
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,991
  non_tradable_zero_volume rows: 26
  corporate_action_candidate_dates:
    2010-05-11, 2019-12-26
  2024 entry~D+180 contamination: none

448280 에코아이
  profile: atlas/symbol_profiles/448/448280.json
  first_date: 2023-11-21
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 546
  corporate_action_candidate_dates:
    2025-05-08, 2025-05-28
  2024 entry~D+180 contamination: none
  caveat:
    short listing history; 2025 corporate-action candidates are outside the selected 2024 validation window.

119650 KC코트렐
  profile: atlas/symbol_profiles/119/119650.json
  first_date: 2010-01-29
  last_date: 2025-03-19 in tradable profile, raw_last_date 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,727
  non_tradable_zero_volume rows: 226
  corporate_action_candidate_dates include:
    2024-03-25
  selected validation:
    use post-candidate entry after 2024-03-25.
  caveat:
    2024 corporate-action candidate and row-presence/tradeability trust caveat apply.
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024 carbon-credit / CCUS / environmental regulation / climate-policy / environmental EPC salience
```

This is a C31 policy/event branch. The investment question is not simply:

```text
green policy is in the news
```

The C31 environmental-policy question is:

```text
climate-policy or carbon-credit event
  -> company-specific project, credit volume, order, or compliance demand
  -> revenue recognition
  -> project cash collection or credit monetization
  -> subsidy / regulation / tender durability
  -> margin / OP conversion
  -> price survival
```

The model can over-score:

```text
carbon-neutrality policy headline
carbon-credit label
CCUS / CO2 capture label
environmental EPC / dust collector / pollution-control label
green chemical label
one-day green-policy stock volume spike
```

The bridge must be stricter:

```text
environmental-policy event
  -> named project / customer / credit vintage / tender / regulation
  -> enforceable project or monetizable credit
  -> delivery / verification / certification path
  -> cash collection and receivables
  -> subsidy or policy durability
  -> margin / OP conversion
  -> accounting / listing / tradeability trust
  -> post-trigger price survival
```

A carbon-policy headline is like seeing a green permit on a factory wall. C31 asks whether the permit becomes a verified credit, a paid project, collected cash, and operating margin rather than just a green sticker.

---

## 5. Case 1 — 083420 그린케미칼

```yaml
case_id: C31_R12L95_083420_2024_03_12
symbol: "083420"
name: "그린케미칼"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE
trigger_date: 2024-03-12
entry_date: 2024-03-12
entry_price_basis: close
entry_price: 7340
classification: local_positive_ccus_green_chemical_policy_spike_with_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

그린케미칼 is the constructive local-positive in this set.

The useful C31 environmental read is not simply:

```text
탄소중립 / CCUS 관련주가 움직였다
```

It is:

```text
green chemical / CCUS relevance
  -> policy salience and potential compliance demand
  -> strong local price confirmation
  -> later requirement for project, revenue, and margin evidence
```

The forward path delivered a large local MFE into March. However, the later price path lost survival into August and October. This is a local positive with 4B, not a Green.

### Price path

Key Stock-Web rows:

```text
2024-03-12: high 8,100 / close 7,340
2024-03-19: high 9,490 / close 8,780
2024-03-25: high 8,900 / close 8,310
2024-08-05: low 5,490 / close 5,600
2024-10-25: low 5,630 / close 5,670
```

Approximate path from entry close:

```text
entry_close: 7,340
peak_high: 9,490
MFE: +29.3%
worst_low_after_entry: 5,490
MAE: -25.2%
```

### Interpretation

This is a C31 local positive with 4B:

```text
Stage2-Actionable: possible only if project, compliance demand, customer, revenue, and margin bridge are explicit.
Stage3-Green: blocked without verified project or revenue conversion evidence.
Local 4B: required after +29% MFE and later material MAE.
Hard 4C: no, because meaningful MFE came first and MAE did not cross the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  ccus_green_chemical_relevance: high
  policy_salience: high
  project_revenue_bridge: weak_to_medium
  certification_or_compliance_bridge: weak
  margin_op_bridge: weak_to_medium
  price_confirmation: high_initial
  post_rerating_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 448280 에코아이

```yaml
case_id: C31_R12L95_448280_2024_02_22
symbol: "448280"
name: "에코아이"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 39800
classification: hard_4c_candidate_carbon_credit_policy_label_without_verified_project_revenue_survival
calibration_usable: true
```

### Evidence interpretation

에코아이는 the carbon-credit hard guardrail.

The label looked attractive:

```text
carbon credit / climate policy / overseas environmental project
  -> carbon-neutrality demand
  -> credit price and verification optionality
  -> green-policy premium
```

But the selected 2024 trigger did not survive. The immediate MFE was shallow, while later MAE became extreme. The case shows that carbon-credit labels should not be promoted without project-level credit generation, verification, sales, and cash collection evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 41,650 / close 39,800
2024-02-26: high 41,100 / close 39,850
2024-03-19: high 35,700 / close 34,050
2024-04-17: low 26,200 / close 26,400
2024-08-05: low 16,480 / close 17,630
2024-10-25: low 18,700 / close 18,800
```

Approximate path from entry close:

```text
entry_close: 39,800
peak_high_after_entry: 41,650
MFE: +4.6%
worst_low_after_entry: 16,480
MAE: -58.6%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from carbon-credit and policy relevance.
Stage2-Actionable: blocked unless verified credit generation, project economics, revenue recognition, and cash collection are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
```

The lesson is that carbon-credit salience is not credit monetization.

### Stress-test components

```text
raw_component_score_proxy:
  carbon_credit_label: high
  climate_policy_relevance: high
  verified_credit_project_bridge: weak
  revenue_cash_collection_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 119650 KC코트렐

```yaml
case_id: C31_R12L95_119650_2024_03_26
symbol: "119650"
name: "KC코트렐"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE
trigger_date: 2024-03-26
entry_date: 2024-03-26
entry_price_basis: close
entry_price: 1403
classification: hard_4c_candidate_environmental_epc_policy_label_without_project_cashflow_tradeability_trust
calibration_usable: true
```

### Evidence interpretation

KC코트렐 is the environmental EPC / tradeability-trust hard guardrail.

The profile has a 2024-03-25 corporate-action candidate. The selected entry is 2024-03-26, after that candidate window. Even after avoiding the immediate raw-price discontinuity, the post-trigger path failed.

The model can be tempted by:

```text
environmental EPC
dust collector / pollution-control equipment
carbon-neutrality policy
plant retrofit and compliance spending
```

But the forward path did not validate project cash flow, receivables, margins, or tradeability trust. The later drawdown was extreme and the profile has row-presence/tradeability caveats.

### Price path

Key Stock-Web rows:

```text
2024-03-25: corporate-action candidate window in profile
2024-03-26: high 1,437 / close 1,403
2024-04-16: low 1,195 / close 1,197
2024-05-07: low 859 / close 880
2024-08-05: low 790 / close 834
2024-08-20: low 352 / close 377
2024-10-23: low 416 / close 416
```

Approximate path from post-candidate entry close:

```text
entry_close: 1,403
peak_high_after_entry: 1,437
MFE: +2.4%
worst_low_after_entry: 352
MAE: -74.9%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from environmental EPC / policy relevance.
Stage2-Actionable: blocked unless named project, receivables, order backlog, project cash collection, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
Corporate-action caveat: avoided by post-candidate entry, but trust cap remains.
Row/tradeability caveat: yes.
```

The lesson is that environmental EPC labels are especially dangerous without cashflow and accounting trust.

### Stress-test components

```text
raw_component_score_proxy:
  environmental_epc_label: high
  carbon_policy_relevance: medium_high
  project_order_bridge: weak
  cashflow_receivables_bridge: weak
  accounting_tradeability_trust: weak
  price_confirmation: failed
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
carbon_credit_policy_case_count: 1
ccus_chemical_case_count: 1
environmental_epc_case_count: 1
corporate_action_caveat_avoided_count: 1
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 carbon/environment grid:

```text
083420 그린케미칼:
  CCUS / green chemical policy local positive;
  meaningful MFE first, later material MAE, 4B required.

448280 에코아이:
  carbon-credit policy label failed;
  shallow MFE and extreme MAE, hard 4C.

119650 KC코트렐:
  environmental EPC policy label failed even after post-corporate-action entry;
  shallow MFE and extreme MAE, hard 4C with trust caveat.
```

Shared rule:

```text
C31 carbon/environment policy is not "green label is hot."
C31 carbon/environment policy is "verified project, credit, tender, compliance demand, cash collection, revenue recognition, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L95_083420_2024_03_12","scheduled_round":"R12","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"083420","name":"그린케미칼","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":7340,"peak_high":9490,"peak_date":"2024-03-19","worst_low_after_entry":5490,"worst_low_after_entry_date":"2024-08-05","mfe_pct":29.3,"mae_pct":-25.2,"classification":"local_positive_ccus_green_chemical_policy_spike_with_4b_after_later_mae","calibration_usable":true,"evidence_family":"ccus_green_chemical_policy_salience_without_refreshed_project_revenue_margin_bridge","residual_error":"green_policy_positive_requires_4b_after_mfe_when_project_revenue_margin_bridge_not_refreshed","shadow_rule_candidate":"preserve_ccus_green_chemical_local_positive_but_attach_4b_after_material_mae"}
{"row_type":"case","case_id":"C31_R12L95_448280_2024_02_22","scheduled_round":"R12","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"448280","name":"에코아이","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":39800,"peak_high":41650,"peak_date":"2024-02-22","worst_low_after_entry":16480,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.6,"mae_pct":-58.6,"classification":"hard_4c_candidate_carbon_credit_policy_label_without_verified_project_revenue_survival","calibration_usable":true,"evidence_family":"carbon_credit_policy_label_without_verified_credit_generation_revenue_cash_collection_margin_bridge","residual_error":"carbon_credit_salience_can_overpromote_without_project_monetization_and_cash_collection","shadow_rule_candidate":"route_carbon_credit_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_verified_project_bridge_missing"}
{"row_type":"case","case_id":"C31_R12L95_119650_2024_03_26","scheduled_round":"R12","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","symbol":"119650","name":"KC코트렐","trigger_date":"2024-03-26","entry_date":"2024-03-26","entry_price":1403,"peak_high":1437,"peak_date":"2024-03-26","worst_low_after_entry":352,"worst_low_after_entry_date":"2024-08-20","mfe_pct":2.4,"mae_pct":-74.9,"classification":"hard_4c_candidate_environmental_epc_policy_label_without_project_cashflow_tradeability_trust","calibration_usable":true,"corporate_action_caveat_avoided":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"environmental_epc_policy_label_without_named_project_receivables_cashflow_margin_accounting_trust_bridge","residual_error":"environmental_epc_label_can_fail_when_project_cashflow_and_tradeability_trust_bridge_missing","shadow_rule_candidate":"route_environmental_epc_policy_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_cashflow_trust_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CARBON_CREDIT_CCUS_ENVIRONMENTAL_EPC_POLICY_REVENUE_MARGIN_BRIDGE_VS_GREEN_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"carbon_credit_policy_case_count":1,"ccus_chemical_case_count":1,"environmental_epc_case_count":1,"corporate_action_caveat_avoided_count":1,"row_presence_or_tradeability_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":95,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_CARBON_POLICY_PROJECT_REVENUE_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 carbon-credit/CCUS/environmental-EPC policy events, do not open Stage2-Actionable or Stage3-Green from carbon-neutrality, carbon-credit, CCUS, CO2 capture, environmental EPC, dust-collector, pollution-control, green-chemical, climate-policy, or one-day green-policy stock spike labels alone. Require named project/customer/credit vintage/tender/regulation, enforceable project or monetizable credit, delivery/verification/certification path, cash collection and receivables, subsidy or policy durability, revenue recognition, margin/OP conversion, accounting/listing/tradeability trust, and post-trigger price survival. CCUS/green-chemical positives with meaningful MFE but later material MAE should remain local 4B unless project/revenue/margin evidence appears. Carbon-credit labels with shallow MFE and extreme MAE should route to hard-4C without verified credit monetization. Environmental EPC labels with corporate-action or row-presence caveats should carry additional trust caps and route to hard-4C when project cashflow is missing.","expected_effect":"Reduce green-policy and carbon-label false positives while preserving true environmental-policy positives with verified project, credit monetization, cash collection, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":95,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"carbon_policy_project_revenue_margin_trust_guard","contribution":"Adds one CCUS/green-chemical local positive, one carbon-credit hard-4C, and one environmental-EPC hard-4C with trust caveat to calibrate C31 carbon/environment policy project, revenue, margin, and trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_CARBON_POLICY_PROJECT_REVENUE_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [carbon_credit, ccus, carbon_neutrality, environmental_epc, green_chemical, climate_policy]:

  Do not open Stage3-Green from:
    - carbon-neutrality policy headline alone
    - carbon-credit label alone
    - CCUS / CO2 capture label alone
    - environmental EPC / pollution-control label alone
    - green chemical label alone
    - one-day green-policy stock volume spike alone

  Require at least two of:
    - named project / customer / credit vintage / tender / regulation
    - enforceable project or monetizable credit
    - delivery / verification / certification path
    - cash collection and receivables
    - subsidy or policy durability
    - revenue recognition
    - margin / OP conversion
    - accounting / listing / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the green-policy headline

  If MFE < 8% and MAE < -35%:
    route to C31 hard-4C candidate.

  If MFE is meaningful but MAE later becomes material:
    preserve as local 4B / capped positive, not Green, unless project/revenue/margin evidence refreshes.

  If row-presence, corporate-action, or tradeability caveat exists:
    apply additional trust cap and block contaminated windows.

  Distinguish:
    - companies where green policy becomes verified project, paid credit, cash collection, and margin
    - from green labels where policy heat does not reach revenue or trust.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 carbon/environment-policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_CARBON_POLICY_PROJECT_REVENUE_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 carbon/environment-policy cases agree, consider implementing a canonical guard that:
   - blocks green-policy Green without project/credit/revenue/cashflow/margin/trust bridge,
   - preserves CCUS/green-chemical positives only with price survival and fresh execution evidence,
   - routes shallow-MFE/extreme-MAE carbon-credit labels to hard-4C,
   - routes environmental EPC labels with missing cashflow/trust bridge to hard-4C,
   - applies corporate-action/row-presence/tradeability caps.

Expected next schedule:
completed_round = R12
completed_loop = 95
next_round = R13
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 95
next_round = R13
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
