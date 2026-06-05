# E2R Stock-Web v12 Residual Research — R12 / Loop 96

```yaml
scheduled_round: R12
scheduled_loop: 96
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
low_birthrate_policy_case_count: 3
baby_product_case_count: 3
short_listing_caveat_count: 1
row_presence_or_tradeability_caveat_count: 1
policy_to_revenue_margin_bridge_missing_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 96
next_round: R13
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 96
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy / event / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

The selected fine branch is:

```text
low birthrate / childcare / baby product policy
birth-support policy demand, channel sell-through, subsidy conversion, revenue, and margin bridge
vs generic low-birthrate policy-label spike
```

This deliberately avoids:
- the R11 loop96 C32 governance / tender branch;
- the R12 loop95 carbon / CCUS / environmental-policy branch;
- the R11 loop95 tourism / inbound / casino / duty-free branch;
- the R12 loop94 education-policy branch;
- the R12 loop93 food-security / agri-input policy branch;
- the R12 loop91 travel-service branch;
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
407400 꿈비
159580 제로투세븐
014100 메디앙스
```

They avoid the C31 top-covered list and recent L10 policy/governance names:

```text
R11 loop96 avoid: 119860, 115390, 008930
R12 loop95 avoid: 083420, 448280, 119650
R11 loop95 avoid: 034230, 950170, 008770
R12 loop94 avoid: 096240, 072870, 095720
R11 loop94 avoid: 003920, 001750, 003240
R12 loop93 avoid: 008040, 054050, 002900
R12 loop92 avoid: 133750, 053290, 215200
R12 loop91 avoid: 039130, 080160, 094850
C31 top-covered avoid: 013990, 003550, 015760, 032350, 114090, 000270
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
407400: same archetype, new symbol, childcare / baby-product policy local positive with 4B after later MAE
159580: same archetype, new symbol, infant-product low-birthrate policy label local burst followed by high-MAE 4B failure
014100: same archetype, new symbol, baby/infant-care policy event spike hard-4C with row/tradeability caveat
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
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
407400 꿈비
  profile: atlas/symbol_profiles/407/407400.json
  first_date: 2023-02-09
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 738
  corporate_action_candidate_dates:
    2023-07-19
  2024 entry~D+180 contamination: none
  caveat:
    short listing history; 2023 corporate-action candidate is outside the selected 2024 validation window.

159580 제로투세븐
  profile: atlas/symbol_profiles/159/159580.json
  first_date: 2013-02-19
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,192
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2018-11-13
  2024 entry~D+180 contamination: none

014100 메디앙스
  profile: atlas/symbol_profiles/014/014100.json
  name history:
    보령메디앙스 until 2020-01-13
    메디앙스 from 2020-01-14
  first_date: 1996-07-08
  raw_first_date: 1996-07-01
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,176
  non_tradable_zero_volume rows: 1,246
  corporate_action_candidate_dates:
    1999-11-12, 1999-11-22, 2021-03-15
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count and raw-discontinuity caveat exist outside the 2024 validation window.
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024 Korea low-birthrate policy / childcare subsidy / birth-support / infant-product policy salience
```

This is a C31 policy/event branch. The investment question is not simply:

```text
저출산 정책이 나온다
```

The C31 low-birthrate policy question is:

```text
policy headline or subsidy event
  -> actual household purchasing power or childcare budget
  -> company-specific product demand
  -> channel sell-through
  -> inventory and markdown risk control
  -> online/offline distribution conversion
  -> promotion, logistics, and raw-material cost containment
  -> revenue and gross margin conversion
  -> price survival after the first policy-label spike
```

The model can over-score:

```text
low-birthrate policy headline
childcare subsidy / birth-support headline
baby product / infant-care label
stroller / crib / nursery goods label
China or domestic childcare demand label
one-day baby-product stock volume spike
small-cap policy beta
```

The bridge must be stricter:

```text
low-birthrate / childcare policy event
  -> named policy benefit or budget channel
  -> addressable households and real purchase conversion
  -> product category directly tied to the policy
  -> sell-through and channel inventory
  -> subsidy timing and payment friction
  -> promotion and logistics cost
  -> gross margin / OP conversion
  -> tradeability and small-cap trust
  -> price survival after the first policy spike
```

A low-birthrate policy headline is like a voucher printed by the government. C31 asks whether that voucher reaches a household, gets spent on this company's product, clears the channel, and leaves margin after promotion and logistics.

---

## 5. Case 1 — 407400 꿈비

```yaml
case_id: C31_R12L96_407400_2024_04_22
symbol: "407400"
name: "꿈비"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-04-22
entry_date: 2024-04-22
entry_price_basis: close
entry_price: 8040
classification: local_positive_childcare_baby_product_policy_demand_with_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

꿈비 is the constructive local-positive case in this C31 low-birthrate branch.

The useful read is not simply:

```text
저출산 관련주가 올랐다
```

It is:

```text
childcare / baby-product relevance
  -> policy salience and household demand optionality
  -> product category directly tied to infant-care spending
  -> local price confirmation
```

The forward path produced a meaningful MFE into early May and later August. But the drawdown into the autumn shows that the first policy rerating did not become durable revenue/margin survival. Therefore this is a local positive with 4B discipline, not a durable Green.

### Price path

Key Stock-Web rows:

```text
2024-04-22: high 8,990 / close 8,040
2024-04-30: high 8,830 / close 8,790
2024-05-02: high 9,820 / close 8,720
2024-07-25: high 8,780 / close 8,120
2024-08-28: high 8,450 / close 8,410
2024-08-29: high 8,900 / close 7,130
2024-10-25: low 5,800 / close 5,820
```

Approximate path from entry close:

```text
entry_close: 8,040
peak_high: 9,820
MFE: +22.1%
worst_low_after_entry: 5,800
MAE: -27.9%
```

### Interpretation

This is a C31 local positive with 4B:

```text
Stage2-Actionable: possible only if policy benefit, household conversion, product demand, sell-through, and margin bridge are explicit.
Stage3-Green: blocked without fresh revenue and margin evidence.
Local 4B: required after +20% MFE and later material MAE.
Hard 4C: no, because meaningful MFE came first and MAE did not cross hard threshold.
Short-listing caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  childcare_product_relevance: high
  low_birthrate_policy_signal: high
  household_demand_bridge: medium
  sellthrough_inventory_bridge: weak_to_medium
  margin_op_bridge: weak_to_medium
  price_confirmation: medium_high_initial
  post_rerating_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 159580 제로투세븐

```yaml
case_id: C31_R12L96_159580_2024_02_01
symbol: "159580"
name: "제로투세븐"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6500
classification: local_burst_infant_product_low_birthrate_policy_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

제로투세븐 is the infant-product local-burst / high-MAE case.

The setup had real C31 relevance:

```text
infant / childcare product label
low-birthrate policy salience
childcare support and household spending optionality
```

The forward path produced a meaningful early MFE into mid-February, so the original trigger is not a pure hard-4C. But the later path failed price survival badly. The policy label did not convert into durable sell-through, revenue, or margin.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,730 / close 6,500
2024-02-14: high 7,400 / close 7,140
2024-05-02: high 6,830 / close 5,970
2024-08-05: low 3,820 / close 4,035
2024-09-09: low 3,805 / close 4,015
2024-10-25: low 4,125 / close 4,130
```

Approximate path from entry close:

```text
entry_close: 6,500
peak_high: 7,400
MFE: +13.8%
worst_low_after_entry: 3,805
MAE: -41.5%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from infant-product and policy relevance.
Stage2-Actionable: possible only if product sell-through, channel inventory, subsidy conversion, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original trigger because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  infant_product_relevance: high
  low_birthrate_policy_label: high
  household_purchase_conversion: weak
  channel_inventory_bridge: weak_to_medium
  gross_margin_bridge: weak
  price_confirmation: medium_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 014100 메디앙스

```yaml
case_id: C31_R12L96_014100_2024_03_21
symbol: "014100"
name: "메디앙스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-03-21
entry_date: 2024-03-21
entry_price_basis: close
entry_price: 3690
classification: hard_4c_candidate_baby_product_policy_event_spike_without_sellthrough_margin_tradeability_trust
calibration_usable: true
```

### Evidence interpretation

메디앙스 is the hard C31 low-birthrate guardrail.

The setup can fool a policy model:

```text
baby / infant-care product label
low-birthrate policy headline
one-day policy-stock volume spike
small-cap childcare beta
```

But from the selected event-spike close, the stock produced almost no incremental MFE and then entered a hard drawdown zone. The bridge from policy headline to household purchase, sell-through, inventory control, and margin was not proven. The high historical non-tradable zero-volume count adds a trust cap.

### Price path

Key Stock-Web rows:

```text
2024-03-21: high 3,690 / close 3,690
2024-03-22: high 3,725 / close 3,330
2024-04-30: high 3,385 / close 3,385
2024-08-05: low 2,185 / close 2,400
2024-09-10: low 2,000 / close 2,115
2024-10-25: low 2,155 / close 2,215
2024-11-07: low 2,095 / close 2,095
```

Approximate path from event-spike close:

```text
entry_close: 3,690
peak_high_after_entry: 3,725
MFE: +0.9%
worst_low_after_entry: 2,000
MAE: -45.8%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from baby-product and low-birthrate policy relevance.
Stage2-Actionable: blocked unless household purchase conversion, sell-through, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
Row/tradeability caveat: yes, high historical non-tradable zero-volume count.
```

The lesson is that low-birthrate policy heat is not baby-product revenue conversion.

### Stress-test components

```text
raw_component_score_proxy:
  baby_product_policy_label: high
  childcare_subsidy_readthrough: medium_high
  household_purchase_bridge: weak
  sellthrough_inventory_bridge: weak
  margin_op_bridge: weak
  price_confirmation_after_entry: failed
  row_tradeability_trust: weak
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
low_birthrate_policy_case_count: 3
baby_product_case_count: 3
short_listing_caveat_count: 1
row_presence_or_tradeability_caveat_count: 1
policy_to_revenue_margin_bridge_missing_count: 2
calibration_usable_trigger_count: 3
```

The three-case C31 low-birthrate / childcare grid:

```text
407400 꿈비:
  childcare / baby-product policy local positive;
  meaningful MFE first, later material MAE, 4B required.

159580 제로투세븐:
  infant-product policy local burst;
  meaningful MFE first, then high MAE, local 4B failure.

014100 메디앙스:
  baby-product policy event spike failed;
  shallow MFE and high MAE, hard 4C with row/tradeability caveat.
```

Shared rule:

```text
C31 low-birthrate policy is not "baby-product label is hot."
C31 low-birthrate policy is "policy benefits reach households, households buy this product, channels sell through, inventory and promotions stay controlled, and gross margin reaches OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L96_407400_2024_04_22","scheduled_round":"R12","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"407400","name":"꿈비","trigger_date":"2024-04-22","entry_date":"2024-04-22","entry_price":8040,"peak_high":9820,"peak_date":"2024-05-02","worst_low_after_entry":5800,"worst_low_after_entry_date":"2024-10-25","mfe_pct":22.1,"mae_pct":-27.9,"classification":"local_positive_childcare_baby_product_policy_demand_with_4b_after_later_mae","calibration_usable":true,"short_listing_caveat":true,"evidence_family":"childcare_baby_product_low_birthrate_policy_household_demand_sellthrough_margin_bridge","residual_error":"childcare_policy_positive_requires_4b_after_material_mae_without_refreshed_revenue_margin_evidence","shadow_rule_candidate":"preserve_childcare_policy_local_positive_but_attach_4b_after_mfe_when_sellthrough_margin_bridge_is_not_refreshed"}
{"row_type":"case","case_id":"C31_R12L96_159580_2024_02_01","scheduled_round":"R12","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"159580","name":"제로투세븐","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6500,"peak_high":7400,"peak_date":"2024-02-14","worst_low_after_entry":3805,"worst_low_after_entry_date":"2024-09-09","mfe_pct":13.8,"mae_pct":-41.5,"classification":"local_burst_infant_product_low_birthrate_policy_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"infant_product_low_birthrate_policy_label_without_sustained_household_purchase_sellthrough_margin_bridge","residual_error":"infant_product_policy_label_can_create_mfe_but_fail_green_without_purchase_conversion_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_infant_policy_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C31_R12L96_014100_2024_03_21","scheduled_round":"R12","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"014100","name":"메디앙스","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":3690,"peak_high":3725,"peak_date":"2024-03-22","worst_low_after_entry":2000,"worst_low_after_entry_date":"2024-09-10","mfe_pct":0.9,"mae_pct":-45.8,"classification":"hard_4c_candidate_baby_product_policy_event_spike_without_sellthrough_margin_tradeability_trust","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"baby_product_low_birthrate_policy_event_spike_without_household_purchase_inventory_margin_trust_bridge","residual_error":"baby_product_policy_spike_can_fail_when_sellthrough_margin_and_tradeability_trust_bridge_missing","shadow_rule_candidate":"route_baby_product_policy_event_spike_to_hard_4c_if_mfe_shallow_mae_large_and_revenue_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"LOW_BIRTHRATE_CHILDCARE_BABY_PRODUCT_POLICY_DEMAND_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"low_birthrate_policy_case_count":3,"baby_product_case_count":3,"short_listing_caveat_count":1,"row_presence_or_tradeability_caveat_count":1,"policy_to_revenue_margin_bridge_missing_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":96,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_LOW_BIRTHRATE_POLICY_HOUSEHOLD_PURCHASE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 low-birthrate/childcare/baby-product policy events, do not open Stage2-Actionable or Stage3-Green from low-birthrate policy, childcare subsidy, birth-support, baby product, infant-care, stroller/crib/nursery goods, China/domestic childcare demand, small-cap policy beta, or one-day baby-product stock spike labels alone. Require named policy benefit or budget channel, addressable households and real purchase conversion, product category directly tied to the policy, sell-through and channel inventory, subsidy timing and payment-friction check, promotion/logistics/raw-material cost control, gross-margin/OP conversion, tradeability trust, and post-trigger price survival. Childcare/baby-product positives with meaningful MFE followed by material MAE should remain local 4B unless sell-through and margin evidence refreshes. Infant-product labels with meaningful MFE followed by high MAE should not remain Green. Baby-product policy event spikes with shallow MFE and high MAE should route to hard-4C when purchase conversion and margin bridge are missing, especially with row/tradeability caveats.","expected_effect":"Reduce low-birthrate policy and baby-product label false positives while preserving true policy-to-household-purchase-to-margin positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":96,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"low_birthrate_policy_household_purchase_margin_guard","contribution":"Adds one childcare-product local positive, one infant-product local 4B failure, and one baby-product hard-4C counterexample to calibrate C31 low-birthrate policy household purchase, sell-through, inventory, subsidy conversion, promotion/logistics cost, margin, and tradeability-trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_LOW_BIRTHRATE_POLICY_HOUSEHOLD_PURCHASE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [low_birthrate, childcare_subsidy, birth_support, baby_product, infant_care]:

  Do not open Stage3-Green from:
    - low-birthrate policy headline alone
    - childcare subsidy / birth-support headline alone
    - baby product / infant-care label alone
    - stroller / crib / nursery goods label alone
    - China or domestic childcare demand label alone
    - one-day baby-product stock volume spike alone
    - small-cap policy beta alone

  Require at least two of:
    - named policy benefit or budget channel
    - addressable households and purchase conversion
    - product category directly tied to policy benefit
    - sell-through and channel inventory control
    - subsidy timing / payment friction check
    - promotion / logistics / raw-material cost containment
    - gross margin / OP conversion
    - tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the policy headline

  If MFE < 8% and MAE < -35%:
    route to C31 hard-4C candidate.

  If MFE > 12% but later MAE is material:
    preserve as local 4B / capped positive, not Green, unless household purchase and margin evidence appears.

  If MFE is meaningful but policy-to-revenue bridge is stale:
    attach 4B until sell-through evidence refreshes.

  If row-presence or short-listing caveat exists:
    apply additional trust cap.

  Distinguish:
    - companies where policy benefits reach households and become product sales with margin
    - from baby-product labels where policy heat does not overcome demand, inventory, promotion, or logistics cost.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 low-birthrate / childcare / baby-product policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_LOW_BIRTHRATE_POLICY_HOUSEHOLD_PURCHASE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 low-birthrate-policy cases agree, consider implementing a canonical guard that:
   - blocks baby-product/low-birthrate-policy Green without household purchase, sell-through, inventory, subsidy conversion, and margin bridge,
   - preserves childcare-product positives only with price survival and fresh sell-through evidence,
   - treats meaningful-MFE/high-MAE infant-product policy cases as local 4B,
   - routes shallow-MFE/high-MAE baby-product policy spikes to hard-4C,
   - applies short-listing and row/tradeability trust caps.

Expected next schedule:
completed_round = R12
completed_loop = 96
next_round = R13
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 96
next_round = R13
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
