# E2R Stock-Web v12 Residual Research — R11 / Loop 95

```yaml
scheduled_round: R11
scheduled_loop: 95
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE

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
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
tourism_inbound_policy_case_count: 3
casino_resort_case_count: 1
dutyfree_case_count: 2
market_transfer_caveat_count: 1
foreign_listing_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 95
next_round: R12
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_95_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 95
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use L10 policy/event/cross-redteam miscellaneous. This file uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

The selected fine branch is:

```text
tourism / inbound / casino / duty-free policy traffic
revenue and margin bridge
vs generic tourism-label spike
```

This deliberately avoids:
- the loop94 R11 C32 governance/control-premium branch using `003920`, `001750`, `003240`;
- the loop94 R12 C31 education-policy branch using `096240`, `072870`, `095720`;
- the loop93 R12 food-security/agri-input policy branch;
- the loop91 travel-service branch names `039130`, `080160`, `094850`;
- the C31 top-covered names.

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
034230 파라다이스
950170 JTC
008770 호텔신라
```

They avoid the C31 top-covered symbols and recent R11/R12 policy names:

```text
R11 loop94 avoid: 003920, 001750, 003240
R12 loop94 avoid: 096240, 072870, 095720
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
034230: same archetype, new symbol, casino / inbound tourism traffic local positive with KOSDAQ-to-KOSPI market-transfer caveat
950170: same archetype, new symbol, duty-free inbound tourism positive with foreign-listing caveat and later 4B watch
008770: same archetype, new symbol, duty-free / hotel inbound label hard-4C without traffic-to-margin survival
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
034230 파라다이스
  profile: atlas/symbol_profiles/034/034230.json
  first_date: 2002-11-05
  last_date: 2026-02-20
  market:
    KOSDAQ until 2024-06-21
    KOSPI from 2024-06-24
  tradable_ohlcv rows: 5,749
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    KOSDAQ-to-KOSPI market transfer occurs inside the 2024 validation year.
    It is not a corporate-action raw-price discontinuity, but it should cap causal interpretation.

950170 JTC
  profile: atlas/symbol_profiles/950/950170.json
  first_date: 2018-04-06
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,931
  corporate_action_candidate_dates:
    2022-12-29
  2024 entry~D+180 contamination: none
  caveat:
    foreign listing / inbound duty-free sensitivity can amplify FX and policy beta.

008770 호텔신라
  profile: atlas/symbol_profiles/008/008770.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,764
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    1999-01-20, 1999-07-20
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024 tourism / inbound / visa-normalization / China-Japan-Korea travel recovery / casino-dutifree demand salience
```

This is a C31 policy/event branch. The investment question is not simply:

```text
inbound tourism is back
```

The C31 tourism question is:

```text
policy or travel-flow event
  -> actual inbound traffic
  -> casino drop / hotel occupancy / duty-free sales
  -> conversion into revenue
  -> labor, rent, commission, promotion, and inventory cost containment
  -> margin / OP conversion
  -> price survival
```

The model can over-score:

```text
tourism policy headline
China / Japan inbound recovery label
casino / duty-free / hotel label
visa easing or group-tour recovery
one-day tourism-stock volume spike
market-transfer or listing headline
```

The bridge must be stricter:

```text
tourism-policy or inbound event
  -> visitor traffic by geography
  -> spend per visitor / casino drop / hotel occupancy / duty-free basket
  -> channel or commission economics
  -> FX and inventory risk
  -> fixed-cost and promotion-cost leverage
  -> margin / OP conversion
  -> post-trigger price survival
```

A tourism-policy headline is like opening an airport gate. C31 asks whether travelers actually arrive, spend money at the company counter, and leave enough margin after rent, labor, promotion, and inventory cost.

---

## 5. Case 1 — 034230 파라다이스

```yaml
case_id: C31_R11L95_034230_2024_02_01
symbol: "034230"
name: "파라다이스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12930
classification: local_positive_casino_inbound_tourism_traffic_with_4b_after_market_transfer_and_later_mae
calibration_usable: true
```

### Evidence interpretation

파라다이스 is the casino/inbound local-positive case.

The useful C31 tourism read is not simply:

```text
관광주가 강하다
```

It is:

```text
casino / integrated resort exposure
  -> inbound traffic and high-value customer spend
  -> casino drop and hotel occupancy bridge
  -> revenue and margin conversion
  -> price confirmation
```

The forward path produced meaningful MFE into April/May. However, the later drawdown was material and the stock moved from KOSDAQ to KOSPI during the 2024 validation year. This is not a raw corporate-action contamination, but it is enough to keep the case capped and attach 4B after the local move.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 12,930
2024-03-27: high 14,450 / close 14,420
2024-04-01: high 15,310 / close 15,310
2024-05-02: high 15,710 / close 15,400
2024-06-24: KOSPI market segment begins
2024-08-05: low 10,330 / close 10,470
2024-10-25: low 10,050 / close 10,100
```

Approximate path from entry close:

```text
entry_close: 12,930
peak_high: 15,710
MFE: +21.5%
worst_low_after_entry: 10,050
MAE: -22.3%
```

### Interpretation

This is a C31 local positive with 4B:

```text
Stage2-Actionable: possible if inbound traffic, casino drop, hotel occupancy, and margin bridge are explicit.
Stage3-Green: blocked without fresh traffic-to-margin evidence after the rerating.
Local 4B: required after +20% MFE and later material MAE.
Hard 4C: no.
Market-transfer caveat: yes, KOSDAQ to KOSPI in June 2024.
```

### Stress-test components

```text
raw_component_score_proxy:
  casino_inbound_relevance: high
  visitor_traffic_bridge: medium_high
  spend_per_visitor_bridge: medium
  margin_op_bridge: weak_to_medium
  price_confirmation: medium_high_initial
  post_rerating_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 950170 JTC

```yaml
case_id: C31_R11L95_950170_2024_02_01
symbol: "950170"
name: "JTC"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3940
classification: positive_dutyfree_inbound_tourism_spend_recovery_with_foreign_listing_caveat_and_4b_watch
calibration_usable: true
```

### Evidence interpretation

JTC is the constructive duty-free tourism control.

The useful read is:

```text
Japan-related duty-free / inbound travel sensitivity
  -> visitor traffic and spending recovery
  -> basket size and FX optionality
  -> price confirmation with controlled downside
```

The path produced large MFE into April/May and did not experience a hard drawdown from the selected entry. It is a valid positive. However, because the company is a foreign listing and the move depends on tourism spend, FX, and duty-free basket economics, the rule should still cap Green unless revenue and margin evidence refreshes the thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 3,940
2024-02-26: high 4,605 / close 4,570
2024-03-26: high 4,885 / close 4,750
2024-04-30: high 5,890 / close 5,880
2024-05-02: high 5,860 / close 5,680
2024-08-05: low 4,540 / close 5,110
2024-10-22: low 3,905 / close 3,955
```

Approximate path from entry close:

```text
entry_close: 3,940
peak_high: 5,890
MFE: +49.5%
worst_low_after_entry: 3,880
MAE: -1.5%
```

### Interpretation

This is a C31 positive with 4B watch after rerating:

```text
Stage2-Actionable: valid if visitor traffic, duty-free sales, basket size, FX, and margin bridge are explicit.
Stage3-Green: possible only with fresh sales/margin evidence.
Local 4B: monitor after +40% MFE.
Hard 4C: no.
Foreign-listing / FX caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  dutyfree_inbound_relevance: high
  visitor_spending_bridge: high
  fx_basket_bridge: medium_high
  margin_op_bridge: medium
  price_confirmation: high
  drawdown_penalty: low
  foreign_listing_caveat: yes
  green_cap: yes
```

---

## 7. Case 3 — 008770 호텔신라

```yaml
case_id: C31_R11L95_008770_2024_02_01
symbol: "008770"
name: "호텔신라"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 58900
classification: hard_4c_candidate_dutyfree_hotel_inbound_label_without_traffic_margin_survival
calibration_usable: true
```

### Evidence interpretation

호텔신라 is the hard C31 tourism guardrail.

The label looked plausible:

```text
hotel / duty-free
China and inbound-tourism recovery
airport and downtown retail exposure
tourism policy normalization
```

But the forward price path did not validate the traffic-to-margin bridge. MFE was shallow and the later MAE crossed the hard-failure area. The model should not treat duty-free relevance as automatic margin conversion, especially when rent, commission, promotion, inventory, and China demand mix can break the bridge.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 58,900
2024-02-07: high 61,800 / close 60,900
2024-04-01: high 63,000 / close 62,900
2024-04-17: low 55,500 / close 55,900
2024-08-05: low 44,750 / close 46,050
2024-10-25: low 42,600 / close 43,000
2024-11-04: low 40,500 / close 41,050
```

Approximate path from entry close:

```text
entry_close: 58,900
peak_high: 63,000
MFE: +7.0%
worst_low_after_entry: 40,500
MAE: -31.2%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from hotel/duty-free and inbound-tourism relevance.
Stage2-Actionable: blocked unless traffic, basket size, commission/rent/promotion cost, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that inbound-tourism traffic is not duty-free margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  dutyfree_hotel_label: high
  inbound_tourism_relevance: high
  traffic_to_sales_bridge: weak_to_medium
  rent_commission_promotion_cost_bridge: weak
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
tourism_inbound_policy_case_count: 3
casino_resort_case_count: 1
dutyfree_case_count: 2
market_transfer_caveat_count: 1
foreign_listing_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 tourism/inbound grid:

```text
034230 파라다이스:
  casino / inbound traffic local positive;
  meaningful MFE first, later material MAE, 4B required.

950170 JTC:
  duty-free / inbound spend positive;
  large MFE and controlled MAE, but foreign-listing and FX caveat cap Green.

008770 호텔신라:
  hotel / duty-free inbound label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C31 tourism policy is not "inbound tourism label."
C31 tourism policy is "visitors arrive, spend at this company, and leave margin after rent, commission, promotion, labor, inventory, and FX effects."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L95_034230_2024_02_01","scheduled_round":"R11","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"034230","name":"파라다이스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12930,"peak_high":15710,"peak_date":"2024-05-02","worst_low_after_entry":10050,"worst_low_after_entry_date":"2024-10-25","mfe_pct":21.5,"mae_pct":-22.3,"classification":"local_positive_casino_inbound_tourism_traffic_with_4b_after_market_transfer_and_later_mae","calibration_usable":true,"market_transfer_caveat":true,"evidence_family":"casino_inbound_tourism_traffic_spend_margin_bridge_with_later_mae","residual_error":"tourism_casino_positive_requires_4b_after_mfe_and_fresh_traffic_margin_evidence","shadow_rule_candidate":"preserve_casino_inbound_positive_but_attach_4b_after_mfe_if_traffic_margin_bridge_stale"}
{"row_type":"case","case_id":"C31_R11L95_950170_2024_02_01","scheduled_round":"R11","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"950170","name":"JTC","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3940,"peak_high":5890,"peak_date":"2024-04-30","worst_low_after_entry":3880,"worst_low_after_entry_date":"2024-11-06","mfe_pct":49.5,"mae_pct":-1.5,"classification":"positive_dutyfree_inbound_tourism_spend_recovery_with_foreign_listing_caveat_and_4b_watch","calibration_usable":true,"foreign_listing_caveat":true,"evidence_family":"dutyfree_inbound_tourism_visitor_spend_fx_basket_margin_bridge","residual_error":"dutyfree_inbound_positive_requires_green_cap_after_large_mfe_without_fresh_sales_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_visitor_spend_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C31_R11L95_008770_2024_02_01","scheduled_round":"R11","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","symbol":"008770","name":"호텔신라","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":58900,"peak_high":63000,"peak_date":"2024-04-01","worst_low_after_entry":40500,"worst_low_after_entry_date":"2024-11-04","mfe_pct":7.0,"mae_pct":-31.2,"classification":"hard_4c_candidate_dutyfree_hotel_inbound_label_without_traffic_margin_survival","calibration_usable":true,"evidence_family":"dutyfree_hotel_inbound_tourism_label_without_traffic_to_sales_rent_commission_margin_bridge","residual_error":"dutyfree_inbound_label_can_fail_when_traffic_does_not_reach_margin","shadow_rule_candidate":"route_dutyfree_hotel_inbound_label_to_hard_4c_if_mfe_shallow_mae_large_and_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":95,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TOURISM_INBOUND_CASINO_DUTYFREE_POLICY_TRAFFIC_REVENUE_MARGIN_BRIDGE_VS_TOURISM_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"tourism_inbound_policy_case_count":3,"casino_resort_case_count":1,"dutyfree_case_count":2,"market_transfer_caveat_count":1,"foreign_listing_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":95,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_TOURISM_TRAFFIC_SPEND_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 tourism/inbound/casino/duty-free policy events, do not open Stage2-Actionable or Stage3-Green from tourism policy, inbound recovery, visa easing, China/Japan travel normalization, casino, duty-free, hotel, airport retail, market-transfer, or one-week tourism-stock spike labels alone. Require visitor traffic by geography, spend per visitor or casino drop or hotel occupancy or duty-free basket, commission/rent/promotion/labor/inventory cost containment, FX risk check, revenue recognition, margin/OP conversion, and post-trigger price survival. Casino/inbound positives with meaningful MFE but later material MAE should remain local 4B unless fresh traffic-to-margin evidence appears. Duty-free positives with large MFE should cap Green unless sales/margin evidence refreshes. Duty-free/hotel labels with shallow MFE and high MAE should route to hard-4C when traffic does not reach margin.","expected_effect":"Reduce tourism-label and inbound-policy false positives while preserving true visitor-traffic-to-margin positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":95,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"tourism_traffic_spend_margin_guard","contribution":"Adds one casino/inbound local positive, one duty-free inbound positive, and one hotel/duty-free hard-4C counterexample to calibrate C31 tourism traffic, spend, cost, FX, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_TOURISM_TRAFFIC_SPEND_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [tourism_policy, inbound_recovery, visa_easing, casino, dutyfree, hotel, travel_retail]:

  Do not open Stage3-Green from:
    - tourism policy headline alone
    - China / Japan inbound recovery label alone
    - visa easing or group-tour recovery label alone
    - casino / duty-free / hotel label alone
    - market-transfer or listing headline alone
    - one-week tourism-stock volume spike alone

  Require at least two of:
    - visitor traffic by geography
    - spend per visitor / casino drop / hotel occupancy / duty-free basket
    - channel / commission / rent / promotion cost control
    - FX and inventory-risk containment
    - revenue recognition
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the tourism-policy headline

  If MFE < 10% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE > 15% but later MAE is material:
    preserve as local 4B / capped positive, not Green, unless fresh traffic-to-margin evidence appears.

  If MFE is large but the bridge is foreign-listing / FX-sensitive:
    cap Green until sales and margin evidence refreshes.

  Distinguish:
    - companies where inbound traffic becomes revenue and margin
    - from tourism labels where rent, commission, promotion, inventory, or demand mix breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 tourism/inbound/casino/duty-free policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_TOURISM_TRAFFIC_SPEND_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 tourism-policy cases agree, consider implementing a canonical guard that:
   - blocks tourism-label Green without visitor traffic, spend, cost, FX, revenue, and margin bridge,
   - preserves casino/inbound positives only with price survival and fresh traffic-to-margin evidence,
   - caps foreign-listing duty-free positives at Actionable/4B after large MFE,
   - routes shallow-MFE/high-MAE hotel/duty-free labels to hard-4C.

Expected next schedule:
completed_round = R11
completed_loop = 95
next_round = R12
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 95
next_round = R12
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
