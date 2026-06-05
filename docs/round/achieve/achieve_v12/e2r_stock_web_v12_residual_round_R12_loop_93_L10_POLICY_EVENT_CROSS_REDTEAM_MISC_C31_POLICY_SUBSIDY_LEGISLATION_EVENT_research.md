# E2R Stock-Web v12 Residual Research — R12 / Loop 93

```yaml
scheduled_round: R12
scheduled_loop: 93
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE

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
hard_4c_candidate_count: 1
agri_food_security_policy_case_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 93
next_round: R13
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 93
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy/event or relevant under-covered service/agri sector. This run uses:

```text
food-security / agri-input / farm-machinery / seed-policy monetization
```

This is distinct from:
- R11 loop93 Korea Value-up / holding-company branch,
- R12 loop92 medical-school quota education-policy branch,
- R12 loop91 travel-service policy branch.

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
008040 사조동아원
054050 농우바이오
002900 TYM
```

They avoid the C31 top-covered symbols and avoid recent R11/R12 policy names:

```text
R11 loop93 avoid: 402340, 001040, 034730
R12 loop92 avoid: 133750, 053290, 215200
R12 loop91 avoid: 039130, 080160, 094850
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
008040: same archetype, new symbol, food-security grain/feed/milling price-survival positive branch
054050: same archetype, new symbol, seed/agri-input policy relevance with weak demand-margin bridge Watch cap
002900: same archetype, new symbol, farm-machinery policy/export label hard-4C without order-margin bridge
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
008040 사조동아원
  profile: atlas/symbol_profiles/008/008040.json
  name history includes:
    신촌사료 -> 에스씨에프 -> 동아에스에프 -> 동아원 -> 사조동아원
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,743
  corporate_action_candidate_dates:
    2000-01-10, 2000-12-06, 2005-10-04, 2006-03-31, 2009-01-06, 2017-09-19
  2024 entry~D+180 contamination: none

054050 농우바이오
  profile: atlas/symbol_profiles/054/054050.json
  first_date: 2002-04-02
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,895
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

002900 TYM
  profile: atlas/symbol_profiles/002/002900.json
  name history:
    동양물산 until 2021-04-13
    TYM from 2021-04-14
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,737
  corporate_action_candidate_dates:
    2016-05-02, 2019-11-13, 2023-05-22, 2023-06-16
  selected 2024 trigger after 2023 candidate windows; entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024 food security / agri-input / farm-machinery policy and supply-chain salience
```

This is a C31 service/agri-policy branch. The investment question is not "food security is important." The C31 question is:

```text
policy or supply salience
  -> company-specific demand
  -> pricing or volume
  -> inventory and input-cost pass-through
  -> margin / OP conversion
  -> price survival
```

The model can over-score:

```text
food security headline
grain / feed / seed label
fertilizer / agri-input label
farm-machinery export or subsidy hope
smart-farm / mechanization policy label
one-day agri-theme volume spike
```

The bridge must be stricter:

```text
policy / food-security event
  -> company-specific order or sell-through
  -> price or spread improvement
  -> input-cost control
  -> inventory risk containment
  -> channel demand
  -> margin / OP conversion
  -> post-trigger price survival
```

Food-security policy is a pantry alarm. It says supply matters. But equity value comes only when this company sells more seed, feed, milling product, or machinery at a spread that survives input costs and inventory risk.

---

## 5. Case 1 — 008040 사조동아원

```yaml
case_id: C31_R12L93_008040_2024_07_24
symbol: "008040"
name: "사조동아원"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 1009
classification: positive_capped_food_security_grain_feed_milling_price_survival_bridge
calibration_usable: true
```

### Evidence interpretation

사조동아원 is the constructive control in this set.

The useful C31 read is:

```text
grain / feed / milling food-security relevance
  -> input-price and product-spread monitoring
  -> theme volume with price survival
  -> controlled downside after entry
```

The path gave a meaningful MFE while keeping MAE relatively contained. This is not a large Green, but it is a valid capped positive for the food-security/agri-input branch.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 1,009
2024-08-02: high 1,060 / close 1,057
2024-08-07: high 1,086 / close 1,085
2024-08-09: high 1,158 / close 1,078
2024-09-09: low 955 / close 984
2024-10-15: high 1,188 / close 1,051
```

Approximate path from entry close:

```text
entry_close: 1,009
peak_high: 1,188
MFE: +17.7%
worst_low_after_entry: 955
MAE: -5.4%
```

### Interpretation

This is a C31 capped positive:

```text
Stage2-Actionable: allowed if grain/feed/milling spread and demand bridge are explicit.
Stage3-Green: blocked without input-cost pass-through and margin evidence.
Local 4B: monitor after event-volume spike, but price survival is constructive.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  food_security_relevance: high
  grain_feed_milling_bridge: medium_high
  input_cost_pass_through: medium
  price_survival: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 054050 농우바이오

```yaml
case_id: C31_R12L93_054050_2024_02_19
symbol: "054050"
name: "농우바이오"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE
trigger_date: 2024-02-19
entry_date: 2024-02-19
entry_price_basis: close
entry_price: 8480
classification: watch_cap_seed_agri_input_policy_label_without_strong_demand_margin_bridge
calibration_usable: true
```

### Evidence interpretation

농우바이오 is the seed/agri-input Watch cap.

The label is relevant:

```text
seed / agri input
food security / crop productivity
policy and supply-chain salience
```

But the price path did not validate an Actionable/Green policy-to-company bridge. MFE was shallow and later MAE was material, although not catastrophic.

### Price path

Key Stock-Web rows:

```text
2024-02-19: high 8,480 / close 8,480
2024-02-20: high 8,550 / close 8,530
2024-02-21: high 8,820 / close 8,470
2024-08-05: low 7,330 / close 7,420
2024-09-09: low 6,990 / close 7,060
2024-10-14: high 7,530 / close 7,500
2024-11-04: high 7,700 / close 7,290
```

Approximate path from entry close:

```text
entry_close: 8,480
peak_high: 8,820
MFE: +4.0%
worst_low_after_entry: 6,990
MAE: -17.6%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from food-security/seed relevance.
Stage2-Actionable: blocked unless seed demand, channel sell-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not extreme, but false-positive guard applies.
```

The lesson is that seed relevance is not automatically paid demand or margin conversion.

### Stress-test components

```text
raw_component_score_proxy:
  seed_policy_relevance: high
  demand_conversion_bridge: weak_to_medium
  channel_sellthrough_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 002900 TYM

```yaml
case_id: C31_R12L93_002900_2024_01_12
symbol: "002900"
name: "TYM"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE
trigger_date: 2024-01-12
entry_date: 2024-01-12
entry_price_basis: close
entry_price: 6220
classification: hard_4c_candidate_farm_machinery_policy_export_label_without_order_margin_bridge
calibration_usable: true
```

### Evidence interpretation

TYM is the farm-machinery hard guardrail.

The label can look attractive:

```text
farm mechanization
agri machinery exports
food-security policy
smart-farm / productivity theme
```

But the forward path shows why the model cannot promote the label without order, shipment, utilization, and margin evidence. The MFE was almost nonexistent and the later drawdown was severe.

### Price path

Key Stock-Web rows:

```text
2024-01-12: high 6,280 / close 6,220
2024-02-29: low 5,250 / close 5,300
2024-03-19: high 6,020 / close 5,960
2024-04-08: low 4,950 / close 4,985
2024-07-29: low 3,330 / close 3,440
2024-08-05: low 2,725 / close 2,830
2024-11-07: high 3,400 / close 3,360
```

Approximate path from entry close:

```text
entry_close: 6,220
peak_high: 6,280
MFE: +1.0%
worst_low_after_entry: 2,725
MAE: -56.2%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from farm-machinery/agri-policy relevance.
Stage2-Actionable: blocked unless order, shipment, margin, and export-demand bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by near-zero MFE and extreme MAE.
```

The lesson is that farm-machinery policy relevance is not order-margin conversion.

### Stress-test components

```text
raw_component_score_proxy:
  farm_machinery_policy_label: high
  export_or_subsidy_bridge: weak
  order_shipment_bridge: weak
  margin_conversion_visibility: weak
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
hard_4c_candidate_count: 1
agri_food_security_policy_case_count: 3
calibration_usable_trigger_count: 3
```

The three-case C31 food-security/agri grid:

```text
008040 사조동아원:
  grain/feed/milling food-security capped positive;
  controlled MAE and useful MFE.

054050 농우바이오:
  seed/agri-input relevance, but weak demand-margin conversion;
  Watch/Yellow cap.

002900 TYM:
  farm-machinery/agri policy label failed badly;
  near-zero MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C31 agri policy is not "food security theme."
C31 agri policy is "policy salience becomes company-specific demand, pricing, input-cost pass-through, and margin conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L93_008040_2024_07_24","scheduled_round":"R12","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE","symbol":"008040","name":"사조동아원","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":1009,"peak_high":1188,"peak_date":"2024-10-15","worst_low_after_entry":955,"worst_low_after_entry_date":"2024-09-09","mfe_pct":17.7,"mae_pct":-5.4,"classification":"positive_capped_food_security_grain_feed_milling_price_survival_bridge","calibration_usable":true,"evidence_family":"grain_feed_milling_food_security_input_cost_price_survival_bridge","residual_error":"positive_path_still_needs_input_cost_pass_through_and_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_grain_feed_milling_spread_and_demand_bridge_confirm_but_cap_green_without_margin_evidence"}
{"row_type":"case","case_id":"C31_R12L93_054050_2024_02_19","scheduled_round":"R12","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE","symbol":"054050","name":"농우바이오","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":8480,"peak_high":8820,"peak_date":"2024-02-21","worst_low_after_entry":6990,"worst_low_after_entry_date":"2024-09-09","mfe_pct":4.0,"mae_pct":-17.6,"classification":"watch_cap_seed_agri_input_policy_label_without_strong_demand_margin_bridge","calibration_usable":true,"evidence_family":"seed_agri_input_policy_relevance_without_channel_demand_margin_bridge","residual_error":"seed_food_security_label_can_overpromote_without_paid_demand_and_margin_conversion","shadow_rule_candidate":"cap_seed_policy_label_at_watch_yellow_if_mfe_shallow_and_margin_bridge_missing"}
{"row_type":"case","case_id":"C31_R12L93_002900_2024_01_12","scheduled_round":"R12","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE","symbol":"002900","name":"TYM","trigger_date":"2024-01-12","entry_date":"2024-01-12","entry_price":6220,"peak_high":6280,"peak_date":"2024-01-12","worst_low_after_entry":2725,"worst_low_after_entry_date":"2024-08-05","mfe_pct":1.0,"mae_pct":-56.2,"classification":"hard_4c_candidate_farm_machinery_policy_export_label_without_order_margin_bridge","calibration_usable":true,"evidence_family":"farm_machinery_policy_export_label_without_order_shipment_margin_bridge","residual_error":"farm_machinery_policy_relevance_can_fail_without_order_and_margin_conversion","shadow_rule_candidate":"route_farm_machinery_policy_label_to_hard_4c_if_mfe_near_zero_mae_extreme_and_order_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"agri_food_security_policy_case_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":93,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_AGRI_POLICY_DEMAND_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 food-security/agri-input events, do not open Stage2-Actionable or Stage3-Green from food-security, grain/feed, seed, fertilizer, farm-machinery, smart-farm, agri-export, or one-week agri-theme spike labels alone. Require company-specific demand or orders, sell-through or channel demand, price/spread improvement, input-cost pass-through, inventory-risk containment, margin/OP conversion, and post-trigger price survival. Grain/feed/milling names with controlled MAE may be capped positives when spread and price-survival bridge are explicit. Seed/agri-input names with shallow MFE should cap at Watch/Yellow without paid demand and margin evidence. Farm-machinery labels with near-zero MFE and extreme MAE should route to hard-4C when order and shipment bridge are missing.","expected_effect":"Reduce food-security/agri-theme false positives while preserving true agri-policy positives with demand, price/spread, input-cost, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":93,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"agri_policy_demand_margin_guard","contribution":"Adds one grain/feed/milling capped positive, one seed/agri-input Watch cap, and one farm-machinery hard-4C counterexample to calibrate C31 food-security/agri-input policy monetization requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_AGRI_POLICY_DEMAND_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [food_security, agri_input, seed, fertilizer, farm_machinery, smart_farm]:

  Do not open Stage3-Green from:
    - food-security headline alone
    - grain / feed / milling label alone
    - seed or agri-input label alone
    - farm-machinery / smart-farm label alone
    - agri-export / subsidy hope alone
    - one-week agri-theme volume spike alone

  Require at least two of:
    - company-specific demand or order growth
    - channel sell-through / paid demand
    - price or spread improvement
    - input-cost pass-through
    - inventory-risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the policy headline

  If MFE < 5% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE < 5% and MAE is material:
    cap at Watch/Yellow unless demand and margin bridge is explicit.

  If MFE > 15% and MAE remains controlled:
    allow capped Actionable only if price/spread and demand bridge are explicit.

  Distinguish:
    - grain/feed/milling names where food-security pressure can become product spread
    - from seed or farm-machinery labels where policy salience does not directly create orders or margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 food-security / agri-input policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_AGRI_POLICY_DEMAND_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 agri-policy cases agree, consider implementing a canonical guard that:
   - blocks food-security/agri-theme Green without demand/spread/input-cost/margin bridge,
   - preserves grain/feed/milling positives only with controlled MAE and product-spread evidence,
   - caps seed/agri-input names at Watch/Yellow without paid demand,
   - routes near-zero-MFE/extreme-MAE farm-machinery labels to hard-4C.

Expected next schedule:
completed_round = R12
completed_loop = 93
next_round = R13
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 93
next_round = R13
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
