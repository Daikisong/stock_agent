# E2R Stock-Web v12 Residual Research — R3 / Loop 95

```yaml
scheduled_round: R3
scheduled_loop: 95
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 95
next_round: R4
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_95_L2_AI_SEMICONDUCTOR_ELECTRONICS_C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 95
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate requires:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage:

```text
loop91: C11_BATTERY_ORDERBOOK_RERATING
loop92: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop93: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop94: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

This run returns to C11 but avoids the top-covered C11 names and uses a different fine branch:

```text
battery foil / pouch film / mixing equipment
orderbook rerating and delivery-margin bridge
vs orderbook-label reversal
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C11_BATTERY_ORDERBOOK_RERATING
rows: 21
symbols: 14
date_range: 2023-01-31~2024-06-21
good/bad S2: 8/4
4B/4C: 1/0
URL pending/proxy: 10/10
top covered symbols:
  137400(4), 299030(3), 003670(2), 302430(2), 001570(1), 005070(1)
```

Selected symbols:

```text
008730 율촌화학
006110 삼아알미늄
277880 티에스아이
```

They avoid the C11 top-covered symbols and avoid recent R3 loop92~94 names:

```text
loop92 avoid: 078600, 066970, 361610
loop93 avoid: 014820, 336370, 222080
loop94 avoid: 121600, 393890, 450080
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
008730: same archetype, new symbol, pouch-film orderbook rerating positive with later 4B after demand/call-off reversal
006110: same archetype, new symbol, aluminum-foil orderbook local burst followed by high-MAE 4B failure
277880: same archetype, new symbol, battery mixing-equipment label hard-4C without orderbook delivery survival
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
008730 율촌화학
  profile: atlas/symbol_profiles/008/008730.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,761
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    1999-01-20, 1999-04-06
  2024 entry~D+180 contamination: none

006110 삼아알미늄
  profile: atlas/symbol_profiles/006/006110.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,041
  non_tradable_zero_volume rows: 724
  corporate_action_candidate_dates:
    2000-10-16, 2000-11-14, 2007-05-04, 2011-04-26, 2023-02-09
  2024 entry~D+180 contamination: none
  caveat:
    high non-tradable zero-volume history exists outside the 2024 validation window.

277880 티에스아이
  profile: atlas/symbol_profiles/277/277880.json
  first_date: 2017-10-30
  last_date: 2026-02-20
  market:
    KONEX until 2020-07-21
    KOSDAQ from 2020-07-22
  tradable_ohlcv rows: 1,713
  non_tradable_zero_volume rows: 326
  corporate_action_candidate_dates:
    2019-06-03, 2021-03-08, 2021-03-30
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C11 is about battery orderbook rerating. It is not a generic "battery material stock" or "long-term EV supply chain" label.

The model can over-score:

```text
battery material orderbook headline
foil / pouch film / mixing equipment label
cell-maker capacity expansion
long-term supply agreement or MOU label
one-week battery-component volume spike
rerating after a past contract without current call-off evidence
```

The bridge must be stricter:

```text
battery orderbook / long-term supply event
  -> named customer and product
  -> firm order or enforceable supply agreement
  -> call-off / delivery schedule
  -> capacity and utilization readiness
  -> ASP / mix / FX / raw-material pass-through
  -> working-capital and inventory risk
  -> margin / OP conversion
  -> price survival after the first orderbook rally
```

A battery orderbook is like a warehouse full of signed-looking boxes. C11 asks whether the customer actually calls the boxes off, whether the factory can ship on time, whether raw material cost is passed through, and whether the boxes leave margin rather than inventory strain.

---

## 5. Case 1 — 008730 율촌화학

```yaml
case_id: C11_R3L95_008730_2024_02_05
symbol: "008730"
name: "율촌화학"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL
trigger_date: 2024-02-05
entry_date: 2024-02-05
entry_price_basis: close
entry_price: 30850
classification: positive_pouch_film_orderbook_rerating_with_4b_after_calloff_margin_reversal
calibration_usable: true
```

### Evidence interpretation

율촌화학 is the constructive C11 control, but with a strict 4B after the early rerating.

The useful C11 read is not simply:

```text
배터리 포장재 / 파우치필름 테마가 강하다
```

It is:

```text
pouch film / battery packaging relevance
  -> orderbook or long-term customer expectation
  -> early price confirmation
  -> later need for call-off, delivery, utilization, and margin evidence
```

The forward path delivered strong MFE in February. But the path later lost price survival, especially around late July and the August shock. This makes it a valid C11 positive at the first trigger, while requiring 4B once the orderbook bridge stops refreshing.

### Price path

Key Stock-Web rows:

```text
2024-02-05: high 32,850 / close 30,850
2024-02-13: high 39,400 / close 39,400
2024-02-16: high 47,000 / close 45,250
2024-02-23: high 49,100 / close 48,450
2024-03-08: high 47,000 / close 43,400
2024-07-31: low 21,100 / close 24,450
2024-08-05: low 20,200 / close 21,400
2024-10-15: high 28,850 / close 28,800
```

Approximate path from entry close:

```text
entry_close: 30,850
peak_high: 49,100
MFE: +59.2%
worst_low_after_entry: 20,200
MAE: -34.5%
```

### Interpretation

This is a C11 positive with later 4B:

```text
Stage2-Actionable: valid only if customer/product, call-off, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal unless fresh orderbook/call-off evidence appears.
Local 4B: required after +50% MFE and later -30%+ MAE.
Hard 4C: not primary because strong MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  pouch_film_orderbook_relevance: high
  customer_supply_bridge: medium_high
  calloff_delivery_bridge: weak_to_medium
  margin_raw_material_bridge: weak_to_medium
  price_confirmation: very_high_initial
  post_rerating_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 006110 삼아알미늄

```yaml
case_id: C11_R3L95_006110_2024_02_14
symbol: "006110"
name: "삼아알미늄"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL
trigger_date: 2024-02-14
entry_date: 2024-02-14
entry_price_basis: close
entry_price: 91300
classification: local_burst_aluminum_foil_orderbook_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

삼아알미늄 is the aluminum-foil local burst / high-MAE case.

The label can look highly relevant:

```text
battery aluminum foil
cell-maker capacity expansion
battery material orderbook rerating
```

The forward path produced an immediate burst and a meaningful MFE. But the later path failed badly. This is not a clean hard-4C from the original entry, because tradable MFE came first. It is a local 4B failure: the orderbook story needed current call-off, utilization, and margin evidence but did not keep price survival.

### Price path

Key Stock-Web rows:

```text
2024-02-14: high 92,500 / close 91,300
2024-02-16: high 102,400 / close 99,500
2024-02-20: high 114,100 / close 108,600
2024-02-21: high 116,400 / close 110,700
2024-03-28: low 85,500 / close 85,500
2024-08-05: low 39,600 / close 42,000
2024-09-10: low 40,300 / close 40,500
2024-10-10: high 61,200 / close 58,700
```

Approximate path from entry close:

```text
entry_close: 91,300
peak_high: 116,400
MFE: +27.5%
worst_low_after_entry: 39,600
MAE: -56.6%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from aluminum-foil battery relevance.
Stage2-Actionable: possible only if supply agreement, call-off, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for original entry because MFE was meaningful before the collapse.
```

### Stress-test components

```text
raw_component_score_proxy:
  aluminum_foil_battery_relevance: high
  orderbook_label: high
  calloff_schedule_bridge: weak
  raw_material_pass_through_bridge: weak_to_medium
  price_confirmation: high_initial
  post_burst_survival: failed
  row_presence_caveat: historical_zero_volume_count_outside_2024
  local_4b_overlay: required
```

---

## 7. Case 3 — 277880 티에스아이

```yaml
case_id: C11_R3L95_277880_2024_03_12
symbol: "277880"
name: "티에스아이"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL
trigger_date: 2024-03-12
entry_date: 2024-03-12
entry_price_basis: close
entry_price: 9060
classification: hard_4c_candidate_battery_mixing_equipment_orderbook_label_without_delivery_margin_survival
calibration_usable: true
```

### Evidence interpretation

티에스아이 is the hard C11 guardrail.

The setup looked plausible:

```text
battery mixing equipment
cell capacity expansion
equipment orderbook expectation
small battery-equipment label
```

But from the selected trigger, the price path produced almost no incremental upside and then a deep drawdown. This is the kind of small battery-equipment orderbook label that should be hard-4C unless firm orders, delivery schedule, and margin bridge are current.

### Price path

Key Stock-Web rows:

```text
2024-03-12: high 9,290 / close 9,060
2024-03-14: high 9,170 / close 8,880
2024-04-08: low 7,300 / close 7,830
2024-08-05: low 5,400 / close 5,620
2024-09-09: low 6,290 / close 6,530
2024-10-25: low 5,950 / close 6,030
```

Approximate path from entry close:

```text
entry_close: 9,060
peak_high: 9,290
MFE: +2.5%
worst_low_after_entry: 5,400
MAE: -40.4%
```

### Interpretation

This is a hard C11 false-positive:

```text
Stage2-Watch: possible from battery mixing-equipment relevance.
Stage2-Actionable: blocked unless firm order, customer, delivery, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that equipment orderbook label is not delivery-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  battery_equipment_label: medium_high
  orderbook_expectation: medium
  firm_order_bridge: weak
  delivery_margin_bridge: weak
  price_confirmation: failed
  drawdown_penalty: high
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
calibration_usable_trigger_count: 3
```

The three-case C11 battery orderbook grid:

```text
008730 율촌화학:
  pouch-film orderbook rerating worked strongly first;
  later high MAE requires 4B and call-off/margin refresh.

006110 삼아알미늄:
  aluminum-foil orderbook local burst;
  meaningful MFE first, then deep MAE, local 4B failure.

277880 티에스아이:
  battery mixing-equipment orderbook label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C11 is not "battery orderbook label."
C11 is "named customer, enforceable order, call-off schedule, capacity utilization, raw-material pass-through, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C11_R3L95_008730_2024_02_05","scheduled_round":"R3","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL","symbol":"008730","name":"율촌화학","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":30850,"peak_high":49100,"peak_date":"2024-02-23","worst_low_after_entry":20200,"worst_low_after_entry_date":"2024-08-05","mfe_pct":59.2,"mae_pct":-34.5,"classification":"positive_pouch_film_orderbook_rerating_with_4b_after_calloff_margin_reversal","calibration_usable":true,"evidence_family":"pouch_film_battery_packaging_orderbook_customer_supply_bridge_without_refreshed_calloff_margin","residual_error":"orderbook_rerating_positive_requires_4b_after_high_mae_without_current_calloff_margin_evidence","shadow_rule_candidate":"preserve_early_orderbook_positive_but_attach_4b_after_large_mfe_followed_by_high_mae"}
{"row_type":"case","case_id":"C11_R3L95_006110_2024_02_14","scheduled_round":"R3","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL","symbol":"006110","name":"삼아알미늄","trigger_date":"2024-02-14","entry_date":"2024-02-14","entry_price":91300,"peak_high":116400,"peak_date":"2024-02-21","worst_low_after_entry":39600,"worst_low_after_entry_date":"2024-08-05","mfe_pct":27.5,"mae_pct":-56.6,"classification":"local_burst_aluminum_foil_orderbook_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"aluminum_foil_battery_orderbook_label_without_calloff_raw_material_margin_survival","residual_error":"battery_foil_orderbook_label_can_create_mfe_but_fail_green_without_calloff_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_extreme_mae_battery_foil_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C11_R3L95_277880_2024_03_12","scheduled_round":"R3","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL","symbol":"277880","name":"티에스아이","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":9060,"peak_high":9290,"peak_date":"2024-03-12","worst_low_after_entry":5400,"worst_low_after_entry_date":"2024-08-05","mfe_pct":2.5,"mae_pct":-40.4,"classification":"hard_4c_candidate_battery_mixing_equipment_orderbook_label_without_delivery_margin_survival","calibration_usable":true,"evidence_family":"battery_mixing_equipment_orderbook_label_without_firm_order_delivery_margin_bridge","residual_error":"small_battery_equipment_orderbook_label_can_fail_when_delivery_and_margin_bridge_missing","shadow_rule_candidate":"route_mixing_equipment_orderbook_label_to_hard_4c_if_mfe_shallow_mae_large_and_firm_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_FOIL_POUCH_FILM_MIXING_EQUIPMENT_ORDERBOOK_RERATING_VS_ORDERBOOK_LABEL_REVERSAL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":95,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","rule_id":"C11_ORDERBOOK_CALLOFF_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C11, do not open Stage2-Actionable or Stage3-Green from battery orderbook, foil, pouch film, mixing equipment, cell-maker expansion, long-term supply agreement, MOU, or one-week battery-component volume spike labels alone. Require named customer and product, enforceable order or firm supply agreement, call-off or delivery schedule, capacity and utilization readiness, ASP/mix/FX/raw-material pass-through, working-capital and inventory risk check, margin/OP conversion, and post-trigger price survival. Orderbook positives with large MFE followed by high MAE should remain local 4B unless current call-off and margin evidence appears. Battery foil or pouch-film labels with meaningful MFE but extreme later MAE should not remain Green. Small battery-equipment labels with shallow MFE and high MAE should route to hard-4C when firm order and delivery-margin bridge are missing.","expected_effect":"Preserve true battery orderbook reratings while reducing orderbook-label, MOU, and late-cycle component false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":95,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"battery_orderbook_calloff_delivery_margin_guard","contribution":"Adds one pouch-film orderbook positive with later 4B, one aluminum-foil local-burst 4B failure, and one battery mixing-equipment hard-4C counterexample to calibrate C11 call-off, delivery, raw-material pass-through, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C11_ORDERBOOK_CALLOFF_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:

  Do not open Stage3-Green from:
    - battery orderbook headline alone
    - foil / pouch-film / equipment label alone
    - cell-maker capacity expansion readthrough alone
    - long-term supply agreement or MOU label alone
    - one-week battery-component volume spike alone

  Require at least two of:
    - named customer and product
    - enforceable order / firm supply agreement
    - call-off / delivery schedule
    - capacity and utilization readiness
    - ASP / mix / FX / raw-material pass-through
    - working-capital or inventory-risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the orderbook headline

  If MFE < 10% and MAE < -35%:
    route to C11 hard-4C candidate.

  If MFE > 20% but later MAE < -30%:
    preserve as local 4B / event burst, not Green, unless current call-off and margin evidence appears.

  If MFE is extraordinary but bridge is stale:
    attach local 4B until orderbook execution refreshes.

  Distinguish:
    - enforceable orderbook that becomes call-off, shipment, utilization, and margin
    - from battery component labels where past contract salience does not survive EV demand slowdown.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C11 battery orderbook rerating cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C11_ORDERBOOK_CALLOFF_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C11 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C11 cases agree, consider implementing a canonical guard that:
   - blocks orderbook-label Green without named customer, firm order, call-off, delivery, and margin bridge,
   - preserves orderbook positives only with price survival and current execution evidence,
   - attaches local 4B after large MFE followed by high MAE,
   - routes shallow-MFE/high-MAE battery equipment labels to hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 95
next_round = R4
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 95
next_round = R4
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
