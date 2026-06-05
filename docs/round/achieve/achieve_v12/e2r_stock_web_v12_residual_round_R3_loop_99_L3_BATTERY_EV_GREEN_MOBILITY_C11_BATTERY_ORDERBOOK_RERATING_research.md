# E2R Stock-Web v12 Residual Research — R3 / Loop 99

```yaml
scheduled_round: R3
scheduled_loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
hard_4c_secondary_guard_count: 1
battery_automation_equipment_case_count: 1
battery_material_equipment_case_count: 1
thermal_processing_equipment_case_count: 1
post_failed_first_window_positive_case_count: 1
orderbook_delivery_acceptance_bridge_missing_count: 2
customer_calloff_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
short_listing_or_old_corporate_action_caveat_count: 3
inactive_candidate_rejected_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 99
next_round: R4
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_99_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 99
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage:

```text
loop95: C11_BATTERY_ORDERBOOK_RERATING
loop96: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop97: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop98: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
```

This run returns to C11 after the R3 branch cycle.

Selected fine branch:

```text
battery equipment / automation / thermal processing / de-magnetization equipment
orderbook quality, named customer, delivery, inspection/acceptance,
customer call-off, utilization, cost pass-through, working capital,
revenue recognition, valuation discipline, and margin bridge
vs generic battery orderbook rerating label spike
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
382840 원준
290670 대보마그네틱
282880 코윈테크
```

They avoid the C11 top-covered list and recent R3 names:

```text
C11 top-covered avoid:
  137400, 299030, 003670, 302430, 001570, 005070

recent R3 avoid:
  loop98 C13: 078600, 361610, 357780
  loop97 C14: 079810, 217820, 382480
  loop96 C12: 011790, 005070, 051910
  loop95 C11: 008730, 006110, 277880
```

Rejected candidate:

```text
131390 원익피앤이 was checked but rejected because its tradable profile ends in 2022.
It is not a clean 2024 C11 validation candidate.
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
382840: same archetype, new symbol, thermal-processing / battery equipment positive from refreshed post-failure window with Green cap
290670: same archetype, new symbol, battery material / de-magnetization equipment local 4B failure with hard-4C secondary guard
282880: same archetype, new symbol, battery automation equipment hard-4C candidate after orderbook label failed customer call-off and margin survival
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
382840 원준
  profile: atlas/symbol_profiles/382/382840.json
  first_date: 2021-10-07
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,070
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2022-07-12, 2022-07-29
  selected late entry~D+180 contamination: none
  caveat:
    short listing and old corporate-action candidates are outside selected 2024 validation window.
    February-to-August first window failed; September 2024 positive case must be separated as a refreshed event window.

290670 대보마그네틱
  profile: atlas/symbol_profiles/290/290670.json
  first_date: 2018-11-06
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,790
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2019-11-06, 2019-11-26
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

282880 코윈테크
  profile: atlas/symbol_profiles/282/282880.json
  first_date: 2019-08-05
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,606
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus older industrial/battery equipment names, but no direct 2024 corporate-action contamination.

Rejected:
131390 원익피앤이
  profile ends in tradable 2022, raw 2022; inferred inactive/delisted-like by row presence.
  Not used as 2024 validation case.
```

---

## 4. Archetype residual problem

C11 is about battery orderbook rerating. It is not merely a generic "battery equipment stock has order backlog" archetype.

The model can over-score:

```text
battery equipment label
battery automation / formation / thermal processing label
de-magnetization / separator / materials equipment label
customer orderbook headline
cell-maker capex recovery hope
secondary-battery supply-chain sympathy
one-week battery equipment stock volume spike
late chase after an orderbook rerating
```

The C11 bridge must be stricter:

```text
battery orderbook / equipment event
  -> named customer, line, region, chemistry, tool, or process step
  -> enforceable order and backlog quality
  -> delivery / installation / inspection / customer acceptance
  -> customer call-off and capex timing
  -> line utilization and customer factory loading
  -> ASP / mix / service or consumables revenue
  -> raw-material, labor, logistics, warranty, and yield cost
  -> inventory and working-capital timing
  -> revenue recognition and cash collection
  -> margin / OP conversion
  -> valuation discipline after the first orderbook spike
  -> price survival after the rerating
```

A C11 thesis is like a battery equipment module waiting at a customer line. The orderbook headline is the purchase order; equity value appears only when the tool is delivered, installed, accepted, called off into running capacity, and the order becomes cash with margin.

---

## 5. Case 1 — 382840 원준

```yaml
case_id: C11_R3L99_382840_2024_09_23
symbol: "382840"
name: "원준"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE
trigger_date: 2024-09-23
entry_date: 2024-09-23
entry_price_basis: close
entry_price: 12720
classification: positive_refreshed_thermal_processing_battery_equipment_orderbook_window_with_green_cap_after_prior_failed_window
calibration_usable: true
```

### Evidence interpretation

원준 is the constructive C11 control, but only from the refreshed September window.

The February window was not used as a positive because it suffered a severe August drawdown. The selected entry deliberately starts from the September 23 refreshed event window, after the first window had failed. The useful C11 read is:

```text
battery thermal-processing equipment relevance
  -> refreshed orderbook / process-equipment salience
  -> customer tool delivery and acceptance optionality
  -> price confirmation into October
  -> Green cap because refreshed event still needs order-to-cash and margin evidence
```

This case is not a retroactive rescue of the failed first-half trigger. It is a separate event window.

### Price path

Key Stock-Web rows:

```text
2024-09-23: high 13,750 / low 11,240 / close 12,720
2024-09-24: high 15,500 / close 14,380
2024-10-07: high 17,400 / close 16,900
2024-10-25: low 14,020 / close 14,020
2024-11-05: high 16,140 / close 14,740
```

Approximate path from refreshed entry close:

```text
entry_close: 12,720
peak_high: 17,400
MFE: +36.8%
worst_low_after_entry: 11,240
MAE: -11.6%
```

### Interpretation

This is a C11 capped positive:

```text
Stage2-Actionable: possible if customer line, process step, delivery, acceptance, and margin bridge are explicit.
Stage3-Green: blocked unless fresh orderbook quality, customer call-off, delivery/acceptance, and margin evidence appears.
Local 4B: monitor because the same symbol had a failed first-half window.
Hard 4C: no.
Event-window separation: required.
```

### Stress-test components

```text
raw_component_score_proxy:
  thermal_processing_equipment_relevance: high
  refreshed_orderbook_signal: high
  customer_line_bridge: medium
  delivery_acceptance_bridge: medium
  cost_working_capital_bridge: weak_to_medium
  price_confirmation: high
  event_window_separation: required
  green_cap: yes
```

---

## 6. Case 2 — 290670 대보마그네틱

```yaml
case_id: C11_R3L99_290670_2024_02_01
symbol: "290670"
name: "대보마그네틱"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 27500
classification: local_burst_battery_material_demetalization_equipment_orderbook_label_high_mae_4b_failure_with_hard_4c_secondary_guard
calibration_usable: true
```

### Evidence interpretation

대보마그네틱 is the battery material / de-magnetization equipment local 4B failure.

The setup had plausible C11 relevance:

```text
battery material / separator / de-magnetization equipment
  -> battery capex and orderbook readthrough
  -> customer equipment delivery optionality
  -> February-March local MFE
```

But the path failed price survival. The label created meaningful MFE first, but the later drawdown crossed a hard zone. This means the model should classify it as local 4B and attach a hard-4C secondary guard for stale or late entries.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 27,500 / close 27,500
2024-02-21: high 31,200 / close 30,400
2024-03-08: high 33,200 / close 30,850
2024-04-17: low 23,600 / close 23,600
2024-08-05: low 15,400 / close 16,010
2024-09-11: high 20,000 / close 17,670
2024-10-25: low 16,040 / close 16,090
```

Approximate path from entry close:

```text
entry_close: 27,500
peak_high: 33,200
MFE: +20.7%
worst_low_after_entry: 15,310
MAE: -44.3%
```

### Interpretation

This is a C11 local 4B failure:

```text
Stage2-Watch: valid from battery material equipment and orderbook relevance.
Stage2-Actionable: possible only if customer, process step, order, delivery, acceptance, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C secondary guard: yes for later stale entries when order-to-cash evidence is missing.
```

### Stress-test components

```text
raw_component_score_proxy:
  battery_material_equipment_relevance: high
  orderbook_signal: medium
  named_customer_bridge: weak
  delivery_acceptance_bridge: weak_to_medium
  working_capital_margin_bridge: weak
  price_confirmation: meaningful_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 282880 코윈테크

```yaml
case_id: C11_R3L99_282880_2024_02_01
symbol: "282880"
name: "코윈테크"
canonical_archetype_id: C11_BATTERY_ORDERBOOK_RERATING
fine_archetype_id: BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 25600
classification: hard_4c_candidate_battery_automation_equipment_orderbook_label_without_customer_calloff_margin_survival
calibration_usable: true
```

### Evidence interpretation

코윈테크 is the battery automation equipment hard C11 guardrail.

The label can fool the model:

```text
battery automation equipment
  -> cell-maker capex and orderbook recovery
  -> battery equipment sympathy
  -> customer factory automation optionality
```

But from the selected February entry, the forward path produced only modest MFE and then severe drawdown. The bridge from automation/orderbook label to customer call-off, delivery, acceptance, working capital, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 25,800 / close 25,600
2024-02-13: high 28,650 / close 27,050
2024-02-23: high 29,450 / close 28,150
2024-04-17: low 21,950 / close 22,000
2024-08-05: low 13,090 / close 13,450
2024-09-09: low 12,940 / close 13,580
2024-11-04: high 17,690 / close 17,690
```

Approximate path from entry close:

```text
entry_close: 25,600
peak_high_first_phase: 29,450
MFE: +15.0%
worst_low_after_entry: 12,940
MAE: -49.5%
```

### Interpretation

This is a hard C11 false-positive candidate:

```text
Stage2-Watch: possible from battery automation / equipment relevance.
Stage2-Actionable: blocked unless named customer order, delivery, acceptance, line loading, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and extreme MAE.
```

The lesson is that automation equipment orderbook salience is not customer call-off margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  battery_automation_equipment_label: high
  cell_maker_capex_readthrough: medium_high
  named_customer_order_bridge: weak
  delivery_acceptance_bridge: weak
  working_capital_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation: modest
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
hard_4c_secondary_guard_count: 1
battery_automation_equipment_case_count: 1
battery_material_equipment_case_count: 1
thermal_processing_equipment_case_count: 1
post_failed_first_window_positive_case_count: 1
orderbook_delivery_acceptance_bridge_missing_count: 2
customer_calloff_margin_bridge_missing_count: 2
valuation_late_chase_or_label_overheat_count: 2
short_listing_or_old_corporate_action_caveat_count: 3
inactive_candidate_rejected_count: 1
calibration_usable_trigger_count: 3
```

The three-case C11 battery orderbook grid:

```text
382840 원준:
  refreshed thermal-processing equipment positive;
  separate September event window, meaningful MFE, but Green requires fresh order-to-cash and margin evidence.

290670 대보마그네틱:
  battery material equipment local 4B failure;
  meaningful MFE first, then high MAE, hard-4C secondary guard.

282880 코윈테크:
  battery automation orderbook label failed;
  modest MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C11 is not "battery equipment orderbook label is hot."
C11 is "orderbook becomes delivery, delivery becomes acceptance, customer call-off fills a line, and cash collection leaves OP margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C11_R3L99_382840_2024_09_23","scheduled_round":"R3","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE","symbol":"382840","name":"원준","trigger_date":"2024-09-23","entry_date":"2024-09-23","entry_price":12720,"peak_high":17400,"peak_date":"2024-10-07","worst_low_after_entry":11240,"worst_low_after_entry_date":"2024-09-23","mfe_pct":36.8,"mae_pct":-11.6,"classification":"positive_refreshed_thermal_processing_battery_equipment_orderbook_window_with_green_cap_after_prior_failed_window","calibration_usable":true,"short_listing_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"thermal_processing_battery_equipment_refreshed_orderbook_delivery_acceptance_customer_calloff_margin_bridge","residual_error":"positive_refreshed_orderbook_window_requires_green_cap_without_refreshed_delivery_acceptance_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_refreshed_orderbook_delivery_and_margin_bridge_confirm_but_separate_from_failed_first_window"}
{"row_type":"case","case_id":"C11_R3L99_290670_2024_02_01","scheduled_round":"R3","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE","symbol":"290670","name":"대보마그네틱","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":27500,"peak_high":33200,"peak_date":"2024-03-08","worst_low_after_entry":15310,"worst_low_after_entry_date":"2024-09-09","mfe_pct":20.7,"mae_pct":-44.3,"classification":"local_burst_battery_material_demetalization_equipment_orderbook_label_high_mae_4b_failure_with_hard_4c_secondary_guard","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"battery_material_demetalization_equipment_orderbook_label_without_sustained_customer_delivery_acceptance_margin_survival","residual_error":"battery_material_equipment_orderbook_label_can_create_mfe_but_fail_green_when_order_to_cash_margin_bridge_breaks","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_battery_material_equipment_cases_as_local_4b_with_hard_4c_secondary_guard"}
{"row_type":"case","case_id":"C11_R3L99_282880_2024_02_01","scheduled_round":"R3","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE","symbol":"282880","name":"코윈테크","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":25600,"peak_high_first_phase":29450,"peak_date":"2024-02-23","worst_low_after_entry":12940,"worst_low_after_entry_date":"2024-09-09","mfe_pct":15.0,"mae_pct":-49.5,"classification":"hard_4c_candidate_battery_automation_equipment_orderbook_label_without_customer_calloff_margin_survival","calibration_usable":true,"short_listing_or_history_caveat":true,"evidence_family":"battery_automation_equipment_orderbook_label_without_named_customer_order_calloff_delivery_acceptance_margin_bridge","residual_error":"battery_automation_orderbook_label_can_fail_when_customer_calloff_and_margin_bridge_missing","shadow_rule_candidate":"route_battery_automation_orderbook_label_to_hard_4c_if_mfe_modest_mae_extreme_and_order_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","fine_archetype_id":"BATTERY_EQUIPMENT_AUTOMATION_THERMAL_PROCESSING_DEMAGNETIZATION_ORDERBOOK_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_ORDERBOOK_RERATING_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"hard_4c_secondary_guard_count":1,"battery_automation_equipment_case_count":1,"battery_material_equipment_case_count":1,"thermal_processing_equipment_case_count":1,"post_failed_first_window_positive_case_count":1,"orderbook_delivery_acceptance_bridge_missing_count":2,"customer_calloff_margin_bridge_missing_count":2,"valuation_late_chase_or_label_overheat_count":2,"short_listing_or_old_corporate_action_caveat_count":3,"inactive_candidate_rejected_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":99,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","rule_id":"C11_BATTERY_ORDERBOOK_DELIVERY_ACCEPTANCE_CALLOFF_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C11 battery orderbook/equipment rerating cases, do not open Stage2-Actionable or Stage3-Green from battery equipment, battery automation, formation equipment, thermal processing, de-magnetization/separator/materials equipment, customer orderbook headline, cell-maker capex recovery hope, secondary-battery supply-chain sympathy, one-week battery equipment volume spike, or late chase after orderbook rerating labels alone. Require named customer/line/region/chemistry/tool/process step, enforceable order and backlog quality, delivery/installation/inspection/customer acceptance, customer call-off and capex timing, line utilization and customer factory loading, ASP/mix/service or consumables revenue, raw-material/labor/logistics/warranty/yield cost control, inventory and working-capital timing, revenue recognition and cash collection, margin/OP conversion, valuation discipline after the first orderbook spike, and post-trigger price survival. Refreshed positive windows after a failed first window must be separated and capped unless delivery/acceptance/margin evidence refreshes. Battery material equipment labels with meaningful MFE followed by high MAE should remain local 4B with hard-4C secondary guard. Battery automation labels with modest MFE and extreme MAE should route to hard-4C when customer call-off and margin bridge are missing.","expected_effect":"Preserve true battery equipment orderbook positives while reducing generic orderbook, automation, material-equipment, capex recovery, and late-chase false positives where delivery, acceptance, call-off, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":99,"canonical_archetype_id":"C11_BATTERY_ORDERBOOK_RERATING","residual_type":"battery_orderbook_delivery_acceptance_calloff_margin_guard","contribution":"Adds one refreshed thermal-processing equipment positive, one battery material equipment local 4B failure, and one battery automation hard-4C counterexample to calibrate C11 orderbook quality, delivery, acceptance, customer call-off, working capital, valuation discipline, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C11_BATTERY_ORDERBOOK_DELIVERY_ACCEPTANCE_CALLOFF_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C11_BATTERY_ORDERBOOK_RERATING:

  Do not open Stage3-Green from:
    - battery equipment label alone
    - battery automation / formation / thermal processing label alone
    - de-magnetization / separator / materials equipment label alone
    - customer orderbook headline alone
    - cell-maker capex recovery hope alone
    - secondary-battery supply-chain sympathy alone
    - one-week battery-equipment stock volume spike alone
    - late chase after orderbook rerating alone

  Require at least two of:
    - named customer / line / region / chemistry / tool / process step
    - enforceable order and backlog quality
    - delivery / installation / inspection / customer acceptance
    - customer call-off and capex timing
    - line utilization and customer factory loading
    - ASP / mix / service or consumables revenue
    - raw-material / labor / logistics / warranty / yield cost containment
    - inventory and working-capital timing
    - revenue recognition and cash collection
    - margin / OP conversion
    - valuation discipline after initial orderbook spike
    - low-MAE post-trigger price survival
    - fresh evidence after the orderbook headline

  If MFE < 18% and MAE <= -40%:
    route to C11 hard-4C candidate.

  If MFE is meaningful but later MAE is high:
    preserve as local 4B and attach hard-4C secondary guard for stale or late entries.

  If a later renewed event appears after first-window failure:
    create a new event window; do not retroactively validate the failed first trigger.

  Distinguish:
    - equipment names where orderbook becomes delivery, acceptance, call-off, cash collection, and OP
    - from labels where orderbook salience rerates first and margin proof fails.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C11 battery orderbook/equipment cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C11_BATTERY_ORDERBOOK_DELIVERY_ACCEPTANCE_CALLOFF_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C11 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C11 cases agree, consider implementing a canonical guard that:
   - blocks battery orderbook Green without customer/line/tool, enforceable order, delivery, acceptance, call-off, and margin bridge,
   - separates refreshed event windows from failed first triggers,
   - preserves thermal-processing positives only with price survival and fresh delivery/margin evidence,
   - treats meaningful-MFE/high-MAE material-equipment cases as local 4B with hard-4C secondary guard,
   - routes modest-MFE/extreme-MAE automation equipment labels to hard-4C,
   - applies short-listing, inactive-profile, and old corporate-action caveats.

Expected next schedule:
completed_round = R3
completed_loop = 99
next_round = R4
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 99
next_round = R4
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
