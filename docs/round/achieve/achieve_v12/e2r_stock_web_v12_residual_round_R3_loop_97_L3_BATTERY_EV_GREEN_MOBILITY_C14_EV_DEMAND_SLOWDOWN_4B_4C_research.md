# E2R Stock-Web v12 Residual Research — R3 / Loop 97

```yaml
scheduled_round: R3
scheduled_loop: 97
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND

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
long_positive_case_count: 0
guardrail_positive_case_count: 3
counterexample_count: 3
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
battery_equipment_case_count: 3
formation_aging_charger_equipment_case_count: 1
slot_die_coating_equipment_case_count: 1
small_battery_equipment_event_spike_case_count: 1
ev_demand_slowdown_bridge_missing_count: 3
corporate_action_caveat_outside_window_count: 3
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 97
next_round: R4
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_97_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 97
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate requires:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage:

```text
loop93: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop94: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
loop95: C11_BATTERY_ORDERBOOK_RERATING
loop96: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

This run returns to C14 after the R3 branch cycle, but avoids the C14 top-covered names and uses a narrower fine branch:

```text
battery equipment / formation equipment / slot-die coating / process parts
EV demand slowdown, customer order conversion, backlog quality, utilization, and margin bridge
vs generic battery-equipment rebound
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C
rows: 21
symbols: 14
date_range: 2023-01-31~2025-03-05
good/bad S2: 3/3
4B/4C: 6/4
URL pending/proxy: 3/3
top covered symbols:
  006400(3), 373220(3), 095500(2), 247540(2), 278280(2), 003670(1)
```

Selected symbols:

```text
079810 디이엔티
217820 원익피앤이
382480 지아이텍
```

They avoid the C14 top-covered list and avoid recent R3 loop93~96 names:

```text
loop93 C14 avoid: 014820, 336370, 222080
loop94 C13 avoid: 121600, 393890, 450080
loop95 C11 avoid: 008730, 006110, 277880
loop96 C12 avoid: 011790, 005070, 051910
C14 top-covered avoid: 006400, 373220, 095500, 247540, 278280, 003670
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
079810: same archetype, new symbol, battery-equipment local burst followed by high-MAE 4B failure
217820: same archetype, new symbol, formation/charging equipment local burst followed by high-MAE 4B failure
382480: same archetype, new symbol, small battery-equipment event spike hard-4C candidate
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
079810 디이엔티
  profile: atlas/symbol_profiles/079/079810.json
  first_date: 2005-01-26
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,198
  corporate_action_candidate_dates:
    2023-09-25
  2024 entry~D+180 contamination: none
  caveat:
    2023 candidate is outside the selected 2024 validation window.

217820 원익피앤이
  profile: atlas/symbol_profiles/217/217820.json
  name history:
    엔에스 until 2022-11-28
    원익피앤이 from 2022-11-29
  first_date: 2015-12-07
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,502
  corporate_action_candidate_dates:
    2019-09-23, 2019-10-14, 2022-11-29
  2024 entry~D+180 contamination: none

382480 지아이텍
  profile: atlas/symbol_profiles/382/382480.json
  first_date: 2021-10-21
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,058
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2022-04-05
  2024 entry~D+180 contamination: none
  caveat:
    shorter listing history and minor row-presence caveat, but no direct 2024 contamination.
```

---

## 4. Archetype residual problem

C14 is a guardrail archetype: it is meant to stop battery/EV labels from being promoted when EV demand, customer inventory, utilization, or capex timing has turned against the trade. It is not a generic "battery-equipment rebound" archetype.

The model can over-score:

```text
secondary battery equipment label
formation / aging / charger / tester label
slot-die / coating / battery process-parts label
customer capex recovery hope
battery order backlog label
EV demand recovery label
one-week battery-equipment volume spike
```

The C14 bridge must be stricter:

```text
battery/EV equipment event
  -> named customer, equipment type, or process step
  -> enforceable order or backlog
  -> delivery / installation / acceptance schedule
  -> customer call-off and utilization
  -> EV demand and customer inventory risk check
  -> ASP / mix / raw-material and labor cost pass-through
  -> working-capital and capex burden
  -> margin / OP conversion
  -> price survival after the first equipment-label rebound
```

A C14 battery-equipment thesis is like a factory line waiting for the customer to pull the next tool into production. The label says the line exists, but C14 asks whether the customer still wants the capacity, whether the tool is delivered and accepted, and whether the supplier gets paid at margin after the EV demand slowdown.

---

## 5. Case 1 — 079810 디이엔티

```yaml
case_id: C14_R3L97_079810_2024_02_01
symbol: "079810"
name: "디이엔티"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12540
classification: local_burst_battery_equipment_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

디이엔티 is a battery-equipment local burst that later validates the C14 guardrail.

The setup had real R3 relevance:

```text
battery equipment / process equipment label
  -> customer capex and equipment-order readthrough
  -> strong February momentum
  -> meaningful local MFE
```

But the forward path failed badly after the February equipment rebound. The case should not be treated as a Green battery-equipment order rerating. The later EV-demand and customer capex reality required a 4B downgrade.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,630 / close 12,540
2024-02-15: high 14,320 / close 14,170
2024-02-21: high 17,380 / close 17,000
2024-04-17: low 10,890 / close 10,910
2024-08-05: low 6,650 / close 6,890
2024-10-25: low 7,210 / close 7,220
```

Approximate path from entry close:

```text
entry_close: 12,540
peak_high: 17,420
MFE: +38.9%
worst_low_after_entry: 6,650
MAE: -47.0%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from battery-equipment relevance.
Stage2-Actionable: possible only if customer order, delivery/acceptance, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  battery_equipment_relevance: high
  customer_order_bridge: weak_to_medium
  delivery_acceptance_bridge: weak
  ev_demand_slowdown_risk: high
  working_capital_margin_bridge: weak
  price_confirmation: high_initial
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 217820 원익피앤이

```yaml
case_id: C14_R3L97_217820_2024_02_01
symbol: "217820"
name: "원익피앤이"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5600
classification: local_burst_formation_charging_equipment_ev_capex_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

원익피앤이 is the formation / charging-equipment local burst.

The setup had plausible C14 relevance:

```text
formation / charging / battery production equipment
  -> cell capex and capacity-readthrough optionality
  -> early February battery-equipment rally
  -> meaningful local MFE
```

But the later price path failed price survival. This is the exact C14 problem: an equipment label can move first, then customer capex, utilization, and EV demand risk break the bridge.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,650 / close 5,600
2024-02-07: high 6,210 / close 5,970
2024-02-15: high 7,300 / close 6,870
2024-04-17: low 5,040 / close 5,140
2024-08-05: low 2,890 / close 3,045
2024-10-25: low 2,815 / close 2,815
```

Approximate path from entry close:

```text
entry_close: 5,600
peak_high: 7,300
MFE: +30.4%
worst_low_after_entry: 2,800
MAE: -50.0%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from formation/charging equipment relevance.
Stage2-Actionable: possible only if customer capex, firm backlog, delivery/acceptance, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  formation_charging_equipment_relevance: high
  capex_recovery_readthrough: medium_high
  customer_backlog_bridge: weak_to_medium
  delivery_acceptance_bridge: weak
  margin_op_bridge: weak
  ev_demand_slowdown_risk: high
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 382480 지아이텍

```yaml
case_id: C14_R3L97_382480_2024_03_12
symbol: "382480"
name: "지아이텍"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND
trigger_date: 2024-03-12
entry_date: 2024-03-12
entry_price_basis: close
entry_price: 3365
classification: hard_4c_candidate_small_battery_equipment_slotdie_process_event_spike_without_customer_order_margin_survival
calibration_usable: true
```

### Evidence interpretation

지아이텍 is the hard C14 guardrail.

The setup can fool a battery-equipment model:

```text
slot-die / coating / battery process-parts label
  -> secondary battery capex readthrough
  -> one-day high-volume event spike
  -> small-cap battery equipment beta
```

But from the selected March event close, the path produced only shallow incremental MFE and then entered a hard drawdown. The bridge from process-equipment label to customer order, delivery, acceptance, utilization, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-03-12: high 3,565 / close 3,365
2024-03-29: low 3,090 / close 3,150
2024-04-17: low 2,760 / close 2,775
2024-08-05: low 1,930 / close 2,130
2024-08-20: high 3,090 / close 2,710
2024-10-25: low 2,250 / close 2,290
```

Approximate path from event-spike close:

```text
entry_close: 3,365
peak_high_after_entry: 3,565
MFE: +5.9%
worst_low_after_entry: 1,930
MAE: -42.6%
```

### Interpretation

This is a hard C14 false-positive:

```text
Stage2-Watch: possible from battery process-equipment relevance.
Stage2-Actionable: blocked unless customer order, backlog, delivery/acceptance, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
Short listing / minor row-presence caveat: yes.
```

The lesson is that a small battery-equipment event spike is not EV-demand or customer-order survival.

### Stress-test components

```text
raw_component_score_proxy:
  slot_die_process_equipment_label: high
  battery_capex_readthrough: medium_high
  customer_order_bridge: weak
  utilization_bridge: weak
  working_capital_margin_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
long_positive_case_count: 0
guardrail_positive_case_count: 3
counterexample_count: 3
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
battery_equipment_case_count: 3
formation_aging_charger_equipment_case_count: 1
slot_die_coating_equipment_case_count: 1
small_battery_equipment_event_spike_case_count: 1
ev_demand_slowdown_bridge_missing_count: 3
corporate_action_caveat_outside_window_count: 3
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C14 battery-equipment slowdown grid:

```text
079810 디이엔티:
  battery-equipment local burst;
  meaningful MFE first, later high MAE, local 4B failure.

217820 원익피앤이:
  formation/charging equipment local burst;
  meaningful MFE first, later high MAE, local 4B failure.

382480 지아이텍:
  small battery process-equipment event spike failed;
  shallow MFE and high MAE, hard 4C candidate.
```

Shared rule:

```text
C14 is not "battery-equipment label rebounded."
C14 is "customer orders, delivery/acceptance, EV demand, utilization, working capital, and margin survive after the equipment-label rebound."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C14_R3L97_079810_2024_02_01","scheduled_round":"R3","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND","symbol":"079810","name":"디이엔티","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12540,"peak_high":17420,"peak_date":"2024-02-22","worst_low_after_entry":6650,"worst_low_after_entry_date":"2024-08-05","mfe_pct":38.9,"mae_pct":-47.0,"classification":"local_burst_battery_equipment_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"battery_equipment_customer_capex_order_delivery_acceptance_margin_bridge_broken_by_ev_demand_slowdown","residual_error":"battery_equipment_rebound_can_create_mfe_but_fail_green_without_customer_order_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_battery_equipment_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C14_R3L97_217820_2024_02_01","scheduled_round":"R3","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND","symbol":"217820","name":"원익피앤이","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5600,"peak_high":7300,"peak_date":"2024-02-15","worst_low_after_entry":2800,"worst_low_after_entry_date":"2024-11-01","mfe_pct":30.4,"mae_pct":-50.0,"classification":"local_burst_formation_charging_equipment_ev_capex_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"formation_charging_equipment_capex_recovery_label_without_sustained_backlog_delivery_margin_survival","residual_error":"formation_equipment_label_can_create_mfe_but_fail_after_ev_customer_capex_slowdown","shadow_rule_candidate":"treat_formation_equipment_mfe_then_high_mae_cases_as_local_4b_guardrail_success"}
{"row_type":"case","case_id":"C14_R3L97_382480_2024_03_12","scheduled_round":"R3","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND","symbol":"382480","name":"지아이텍","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":3365,"peak_high":3565,"peak_date":"2024-03-12","worst_low_after_entry":1930,"worst_low_after_entry_date":"2024-08-05","mfe_pct":5.9,"mae_pct":-42.6,"classification":"hard_4c_candidate_small_battery_equipment_slotdie_process_event_spike_without_customer_order_margin_survival","calibration_usable":true,"short_listing_or_row_presence_caveat":true,"evidence_family":"small_battery_process_equipment_event_spike_without_customer_order_delivery_acceptance_utilization_margin_bridge","residual_error":"small_battery_equipment_event_spike_can_fail_when_customer_order_and_margin_bridge_missing","shadow_rule_candidate":"route_small_battery_equipment_event_spike_to_hard_4c_if_mfe_shallow_mae_high_and_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_EQUIPMENT_FORMATION_SLOTDIE_PROCESS_EV_DEMAND_SLOWDOWN_4B_4C_GUARD_VS_EQUIPMENT_LABEL_REBOUND","case_count":3,"long_positive_case_count":0,"guardrail_positive_case_count":3,"counterexample_count":3,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"battery_equipment_case_count":3,"formation_aging_charger_equipment_case_count":1,"slot_die_coating_equipment_case_count":1,"small_battery_equipment_event_spike_case_count":1,"ev_demand_slowdown_bridge_missing_count":3,"corporate_action_caveat_outside_window_count":3,"short_listing_or_row_presence_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":97,"canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","rule_id":"C14_BATTERY_EQUIPMENT_EV_DEMAND_ORDER_MARGIN_4B_4C_GUARD_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C14 battery/EV demand slowdown cases, do not open Stage2-Actionable or Stage3-Green from secondary-battery equipment, formation/aging/charging, slot-die/coating/process parts, customer capex recovery, battery order backlog, EV demand recovery, or one-week battery-equipment volume spike labels alone. Require named customer/equipment/process step, enforceable order or backlog, delivery/installation/acceptance schedule, customer call-off and utilization, EV demand and customer-inventory risk check, ASP/mix/raw-material/labor cost pass-through, working-capital/capex burden containment, margin/OP conversion, and post-trigger price survival. Battery-equipment names with meaningful MFE followed by high MAE should be local 4B, not Green. Small battery-equipment event spikes with shallow MFE and high MAE should route to hard-4C when order/delivery/margin bridge is missing. Corporate-action caveats outside the 2024 window should be noted but not contaminate clean 2024 rows.","expected_effect":"Improve C14 guardrail behavior so the model stops treating battery-equipment rebounds as durable positives when EV demand, customer capex, utilization, and margin bridges fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":97,"canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","residual_type":"battery_equipment_ev_demand_order_margin_4b_4c_guard","contribution":"Adds two battery-equipment local 4B failures and one small battery-equipment hard-4C candidate to calibrate C14 EV demand slowdown, customer capex, delivery/acceptance, utilization, working-capital, and margin guardrails.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C14_BATTERY_EQUIPMENT_EV_DEMAND_ORDER_MARGIN_4B_4C_GUARD_REQUIRED

IF canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C:

  Do not open Stage3-Green from:
    - secondary battery equipment label alone
    - formation / aging / charger / tester label alone
    - slot-die / coating / process-parts label alone
    - customer capex recovery headline alone
    - battery order backlog label alone
    - EV demand recovery label alone
    - one-week battery-equipment volume spike alone

  Require at least two of:
    - named customer / equipment type / process step
    - enforceable order or backlog
    - delivery / installation / acceptance schedule
    - customer call-off and utilization
    - EV demand and customer-inventory risk check
    - ASP / mix / raw-material / labor cost pass-through
    - working-capital / capex burden containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the battery-equipment rebound

  If MFE < 8% and MAE < -35%:
    route to C14 hard-4C candidate.

  If MFE > 20% but later MAE < -35%:
    preserve as local 4B / event burst, not Green, unless current order/delivery/margin evidence appears.

  If MFE is meaningful but EV-demand or customer-capex evidence is stale:
    attach 4B until customer call-off and utilization evidence refreshes.

  Distinguish:
    - equipment names where orders become delivery, acceptance, utilization, and margin
    - from equipment labels where EV demand slowdown or customer inventory breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C14 battery-equipment / EV demand slowdown cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C14_BATTERY_EQUIPMENT_EV_DEMAND_ORDER_MARGIN_4B_4C_GUARD_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C14 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C14 cases agree, consider implementing a canonical guard that:
   - blocks battery-equipment Green without customer/order/delivery/acceptance/utilization/margin bridge,
   - treats meaningful-MFE/high-MAE battery-equipment cases as local 4B,
   - routes shallow-MFE/high-MAE small battery-equipment event spikes to hard-4C,
   - applies EV-demand/customer-capex slowdown checks before Actionable,
   - keeps outside-window corporate-action caveats as trust notes but not contamination.

Expected next schedule:
completed_round = R3
completed_loop = 97
next_round = R4
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 97
next_round = R4
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
