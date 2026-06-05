# E2R Stock-Web v12 Residual Research — R1 / Loop 99

```yaml
scheduled_round: R1
scheduled_loop: 99
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE

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
hard_4c_candidate_count: 0
ship_engine_order_backlog_case_count: 1
machine_tool_event_burst_case_count: 1
industrial_casting_parts_case_count: 1
order_backlog_delivery_margin_bridge_missing_count: 1
cost_passthrough_working_capital_bridge_missing_count: 1
large_mfe_green_cap_count: 2
name_change_or_share_count_caveat_count: 1
row_presence_or_old_corporate_action_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 99
next_round: R2
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 99
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop95: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop96: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop97: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop98: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

This run returns to C01 after the R1 branch cycle, but avoids C01 top-covered names and recent R1 / R9 / R10 names.

Selected fine branch:

```text
ship engine / machine tool / industrial casting and metal parts
order backlog, named customer or channel, delivery schedule, inspection/acceptance,
raw-material and labor cost pass-through, working capital, warranty/quality risk,
and margin conversion
vs generic industrial equipment / order backlog label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
rows: 25
symbols: 14
date_range: 2023-01-31~2024-08-30
good/bad S2: 16/4
4B/4C: 1/0
URL pending/proxy: 8/8
top covered symbols:
  042660(5), 071970(3), 100090(3), 329180(3), 010140(2), 009540(1)
```

Selected symbols:

```text
082740 한화엔진
010660 화천기계
054540 삼영엠텍
```

They avoid the C01 top-covered list and the recent R1 loop95~98 names:

```text
C01 top-covered avoid:
  042660, 071970, 100090, 329180, 010140, 009540

recent R1 avoid:
  loop98 C05: 017960, 014620, 105740
  loop97 C04: 051600, 052690, 130660
  loop96 C01: 267270, 210540, 241560
  loop95 C03: 064350, 272210, 448710
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
082740: same archetype, new symbol, ship-engine / marine engine order-backlog positive with Green cap and 2024 name-change/share-count caveat
010660: same archetype, new symbol, machine-tool / industrial-equipment event burst followed by severe giveback, local 4B failure
054540: same archetype, new symbol, industrial casting / shipbuilding-engine parts positive with Green cap and row-trust caveat
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
082740 한화엔진
  profile: atlas/symbol_profiles/082/082740.json
  name history:
    두산엔진 -> HSD엔진 -> 한화엔진
  selected 2024 early trigger name:
    HSD엔진
  later 2024 name:
    한화엔진 from 2024-03-15
  first_date: 2011-01-04
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,710
  non_tradable_zero_volume rows: 10
  corporate_action_candidate_dates:
    2018-06-19, 2021-03-17, 2022-08-25
  2024 entry~D+180 contamination:
    no raw-price corporate-action candidate in profile,
    but share-count / name-change caveat is visible around March 2024.
  caveat:
    name-change and share-count trust cap; do not treat as raw corporate-action contamination unless price discontinuity appears.

010660 화천기계
  profile: atlas/symbol_profiles/010/010660.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,749
  non_tradable_zero_volume rows: 15
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    2019-05-15
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity and row-presence caveat exists outside selected 2024 validation window.

054540 삼영엠텍
  profile: atlas/symbol_profiles/054/054540.json
  first_date: 2001-11-15
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,984
  non_tradable_zero_volume rows: 2
  corporate_action_candidate_dates:
    2002-05-06, 2008-07-02
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity caveat exists outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C01 is about order backlog and margin bridge. It is not a generic "industrial equipment is strong" or "order backlog headline" archetype.

The model can over-score:

```text
shipbuilding / marine engine order backlog label
industrial equipment or machine-tool label
casting / metal-parts / plant-parts label
customer capex recovery headline
group acquisition / name-change salience
one-week industrial-stock volume spike
late chase after an order-backlog rerating
```

The C01 bridge must be stricter:

```text
industrial order-backlog event
  -> named customer, shipyard, industry, product, or program
  -> enforceable order and backlog quality
  -> delivery schedule and customer acceptance
  -> utilization / capacity and production bottleneck
  -> steel / casting / labor / energy / logistics cost pass-through
  -> warranty / quality / delay-penalty risk
  -> inventory and working-capital timing
  -> revenue recognition and cash collection
  -> margin / OP conversion
  -> price survival after the first order-backlog spike
```

A C01 industrial backlog thesis is like a machine part waiting at the factory gate. The order ticket is only the first knock. Equity value appears only when the part is built, delivered, accepted, paid for, and still leaves margin after steel, labor, logistics, warranty, and working-capital strain.

---

## 5. Case 1 — 082740 한화엔진

```yaml
case_id: C01_R1L99_082740_2024_02_01
symbol: "082740"
name_at_trigger: "HSD엔진"
later_2024_name: "한화엔진"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 8360
classification: positive_ship_engine_order_backlog_delivery_margin_bridge_with_name_change_share_count_green_cap
calibration_usable: true
```

### Evidence interpretation

한화엔진 is the constructive C01 control in this set.

The useful C01 read is not simply:

```text
조선 기자재 / 엔진주가 강하다
```

It is:

```text
ship engine / marine engine backlog
  -> shipyard order cycle and engine delivery schedule
  -> utilization and production-capacity leverage
  -> cost pass-through and warranty / quality-risk discipline
  -> very strong March-July price confirmation
```

The forward path produced a very large MFE and controlled early drawdown. This is a positive C01 case. However, after the large rerating, Green should remain capped unless backlog quality, delivery, acceptance, cost pass-through, and margin evidence refresh. The March 2024 name-change and share-count caveat also requires trust discipline.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 8,640 / close 8,360
2024-02-28: high 9,170 / close 9,090
2024-03-15: high 9,910 / close 9,500
2024-03-19: high 9,700 / close 8,140
2024-04-24: high 13,890 / close 12,450
2024-07-24: high 17,160 / close 15,880
2024-08-05: low 11,000 / close 12,000
2024-10-17: high 16,500 / close 16,140
```

Approximate path from entry close:

```text
entry_close: 8,360
peak_high: 17,160
MFE: +105.3%
worst_low_after_entry: 7,990
MAE: -4.4%
```

### Interpretation

This is a C01 positive with Green cap:

```text
Stage2-Actionable: possible if customer / shipyard backlog, delivery schedule, acceptance, and margin bridge are explicit.
Stage3-Green: blocked after +100% MFE unless fresh backlog/delivery/margin evidence appears.
Local 4B: monitor if group/name-change or order-backlog salience outruns margin evidence.
Hard 4C: no.
Name-change / share-count caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  ship_engine_backlog_relevance: high
  named_customer_shipyard_bridge: medium_high
  delivery_acceptance_bridge: medium
  utilization_capacity_bridge: high
  cost_pass_through_bridge: medium
  warranty_quality_bridge: medium
  price_confirmation: extreme
  drawdown_penalty: low
  green_cap: required_after_large_mfe
  trust_caveat: name_change_share_count
```

---

## 6. Case 2 — 010660 화천기계

```yaml
case_id: C01_R1L99_010660_2024_02_01
symbol: "010660"
name: "화천기계"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3280
classification: local_burst_machine_tool_industrial_equipment_label_high_mae_4b_failure_without_order_margin_survival
calibration_usable: true
```

### Evidence interpretation

화천기계 is the machine-tool / industrial-equipment local burst failure.

The label can fool the model:

```text
machine tool / industrial equipment
  -> capex recovery or factory automation readthrough
  -> small-cap industrial event beta
  -> one-month volume spike
```

The price path produced a huge local MFE, so this is not a no-response failure. But the later collapse shows that the industrial equipment label was not enough. There was no durable bridge from order backlog to delivery, acceptance, working capital, and margin survival.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,285 / close 3,280
2024-02-13: high 4,075 / close 3,630
2024-02-26: high 5,120 / close 4,600
2024-03-18: high 8,130 / close 8,130
2024-03-19: high 9,700 / close 8,140
2024-04-17: low 3,655 / close 3,680
2024-08-05: low 2,500 / close 2,600
2024-09-24: high 3,780 / close 3,780
```

Approximate path from entry close:

```text
entry_close: 3,280
peak_high: 9,700
MFE: +195.7%
worst_low_after_entry: 2,500
MAE: -23.8%
```

### Interpretation

This is a C01 local burst / 4B failure:

```text
Stage2-Watch: possible from machine-tool and industrial-equipment relevance.
Stage2-Actionable: possible only if order backlog, customer capex, delivery, acceptance, and margin bridge are explicit.
Stage3-Green: blocked after severe post-rerating giveback.
Local 4B: required.
Hard 4C: not primary because MFE was extreme before the drawdown.
```

### Stress-test components

```text
raw_component_score_proxy:
  machine_tool_label: high
  customer_order_bridge: weak
  delivery_acceptance_bridge: weak
  cost_pass_through_bridge: weak
  working_capital_bridge: weak
  price_confirmation: extreme_initial
  later_margin_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 054540 삼영엠텍

```yaml
case_id: C01_R1L99_054540_2024_02_01
symbol: "054540"
name: "삼영엠텍"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3985
classification: positive_industrial_casting_shipbuilding_parts_order_backlog_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

삼영엠텍 is the industrial casting / parts positive with Green cap.

The setup had real C01 relevance:

```text
industrial casting / machinery and shipbuilding-related parts
  -> order cycle and delivery optionality
  -> casting / steel input cost and utilization bridge
  -> gradual price confirmation into July-August
```

The path produced meaningful MFE and avoided hard drawdown. This is a positive, but the score should stay capped because casting/parts labels can overstate the benefit unless order, delivery, acceptance, cost pass-through, and margin conversion are visible.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,020 / close 3,985
2024-04-24: high 4,170 / close 4,130
2024-05-13: high 4,570 / close 4,450
2024-07-29: high 5,590 / close 5,260
2024-08-09: high 6,110 / close 5,280
2024-08-26: low 4,485 / close 4,485
2024-09-06: low 3,850 / close 3,910
2024-11-07: high 4,595 / close 4,340
```

Approximate path from entry close:

```text
entry_close: 3,985
peak_high: 6,110
MFE: +53.3%
worst_low_after_entry: 3,575
MAE: -10.3%
```

### Interpretation

This is a C01 positive with Green cap:

```text
Stage2-Actionable: possible if customer program, order backlog, casting delivery, cost pass-through, and margin bridge are explicit.
Stage3-Green: blocked after +50% MFE unless fresh order/delivery/margin evidence appears.
Local 4B: monitor if parts-label price outruns real delivery acceptance.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  industrial_casting_parts_relevance: high
  customer_program_bridge: medium
  order_delivery_bridge: medium
  steel_casting_cost_bridge: medium
  utilization_margin_bridge: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
ship_engine_order_backlog_case_count: 1
machine_tool_event_burst_case_count: 1
industrial_casting_parts_case_count: 1
order_backlog_delivery_margin_bridge_missing_count: 1
cost_passthrough_working_capital_bridge_missing_count: 1
large_mfe_green_cap_count: 2
name_change_or_share_count_caveat_count: 1
row_presence_or_old_corporate_action_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C01 industrial order-backlog grid:

```text
082740 한화엔진:
  ship engine / order-backlog positive;
  extreme MFE and low MAE, but Green requires fresh backlog, delivery, acceptance, and margin evidence.

010660 화천기계:
  machine-tool / industrial-equipment local burst;
  extreme MFE first, then severe giveback, local 4B failure.

054540 삼영엠텍:
  industrial casting / shipbuilding parts positive;
  large MFE and controlled MAE, but Green requires fresh customer-order and cost-pass-through evidence.
```

Shared rule:

```text
C01 is not "industrial backlog label is hot."
C01 is "orders become delivery, delivery becomes acceptance, acceptance becomes cash collection, and cost pass-through leaves operating margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C01_R1L99_082740_2024_02_01","scheduled_round":"R1","scheduled_loop":99,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE","symbol":"082740","name_at_trigger":"HSD엔진","later_2024_name":"한화엔진","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8360,"peak_high":17160,"peak_date":"2024-07-24","worst_low_after_entry":7990,"worst_low_after_entry_date":"2024-02-20","mfe_pct":105.3,"mae_pct":-4.4,"classification":"positive_ship_engine_order_backlog_delivery_margin_bridge_with_name_change_share_count_green_cap","calibration_usable":true,"name_change_or_share_count_caveat":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"ship_engine_marine_engine_order_backlog_shipyard_delivery_acceptance_cost_pass_through_margin_bridge","residual_error":"ship_engine_order_backlog_positive_requires_green_cap_after_extreme_mfe_without_refreshed_delivery_acceptance_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_backlog_delivery_acceptance_and_margin_bridge_confirm_but_cap_green_after_extreme_mfe_or_name_change_caveat"}
{"row_type":"case","case_id":"C01_R1L99_010660_2024_02_01","scheduled_round":"R1","scheduled_loop":99,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE","symbol":"010660","name":"화천기계","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3280,"peak_high":9700,"peak_date":"2024-03-19","worst_low_after_entry":2500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":195.7,"mae_pct":-23.8,"classification":"local_burst_machine_tool_industrial_equipment_label_high_mae_4b_failure_without_order_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"machine_tool_industrial_equipment_event_burst_without_sustained_customer_order_delivery_working_capital_margin_bridge","residual_error":"machine_tool_equipment_label_can_create_extreme_mfe_but_fail_green_without_order_delivery_and_margin_survival","shadow_rule_candidate":"classify_extreme_mfe_then_material_mae_machine_tool_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C01_R1L99_054540_2024_02_01","scheduled_round":"R1","scheduled_loop":99,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE","symbol":"054540","name":"삼영엠텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3985,"peak_high":6110,"peak_date":"2024-08-09","worst_low_after_entry":3575,"worst_low_after_entry_date":"2024-04-16","mfe_pct":53.3,"mae_pct":-10.3,"classification":"positive_industrial_casting_shipbuilding_parts_order_backlog_margin_bridge_with_green_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"industrial_casting_shipbuilding_parts_customer_order_delivery_cost_pass_through_utilization_margin_bridge","residual_error":"industrial_casting_parts_positive_requires_green_cap_after_large_mfe_without_refreshed_order_delivery_cost_pass_through_margin_evidence","shadow_rule_candidate":"preserve_industrial_casting_order_positive_but_cap_green_after_large_mfe_if_delivery_margin_evidence_is_stale"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":99,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIP_ENGINE_MACHINE_TOOL_CASTING_ORDER_BACKLOG_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_INDUSTRIAL_EQUIPMENT_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"ship_engine_order_backlog_case_count":1,"machine_tool_event_burst_case_count":1,"industrial_casting_parts_case_count":1,"order_backlog_delivery_margin_bridge_missing_count":1,"cost_passthrough_working_capital_bridge_missing_count":1,"large_mfe_green_cap_count":2,"name_change_or_share_count_caveat_count":1,"row_presence_or_old_corporate_action_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":99,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","rule_id":"C01_ORDER_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C01 industrial order-backlog cases, do not open Stage2-Actionable or Stage3-Green from shipbuilding/marine-engine backlog, industrial equipment, machine tool, casting/metal-parts/plant-parts, customer capex recovery, group acquisition/name-change salience, one-week industrial-stock spike, or late chase after order-backlog rerating labels alone. Require named customer/shipyard/industry/product/program, enforceable order and backlog quality, delivery schedule and customer acceptance, utilization/capacity and production bottleneck, steel/casting/labor/energy/logistics cost pass-through, warranty/quality/delay-penalty risk control, inventory and working-capital timing, revenue recognition and cash collection, margin/OP conversion, and post-trigger price survival. Ship-engine and industrial casting positives with large MFE may be capped Actionable when backlog/delivery/acceptance/margin bridge is explicit, but Green requires fresh evidence and row/name-change trust caveats must cap. Machine-tool or industrial-equipment labels with extreme MFE followed by material MAE should remain local 4B, not Green, unless order-delivery-margin evidence is refreshed.","expected_effect":"Preserve true industrial order-backlog positives while reducing generic ship-engine, machine-tool, casting-parts, and industrial-equipment false positives where delivery, acceptance, cost pass-through, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":99,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"order_delivery_acceptance_cost_passthrough_margin_guard","contribution":"Adds one ship-engine order-backlog positive, one machine-tool local 4B failure, and one industrial casting positive to calibrate C01 customer order, delivery, acceptance, cost pass-through, working capital, warranty/quality, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C01_ORDER_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE:

  Do not open Stage3-Green from:
    - shipbuilding / marine-engine order backlog label alone
    - industrial equipment / machine-tool label alone
    - casting / metal-parts / plant-parts label alone
    - customer capex recovery headline alone
    - group acquisition / name-change salience alone
    - one-week industrial-stock volume spike alone
    - late chase after order-backlog rerating alone

  Require at least two of:
    - named customer / shipyard / industry / product / program
    - enforceable order and backlog quality
    - delivery schedule and customer acceptance
    - utilization / capacity and production bottleneck check
    - steel / casting / labor / energy / logistics cost pass-through
    - warranty / quality / delay-penalty risk containment
    - inventory and working-capital timing
    - revenue recognition and cash collection
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the industrial order-backlog headline

  If MFE < 8% and MAE <= -30%:
    route to C01 hard-4C candidate.

  If MFE > 25% but delivery/acceptance/margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is extreme but later MAE becomes material:
    attach 4B until order-to-cash and margin evidence refreshes.

  If name-change, share-count, row-presence, or old corporate-action caveat exists:
    apply trust cap and require price-continuity check.

  Distinguish:
    - companies where backlog becomes delivery, acceptance, cash collection, and OP
    - from industrial labels where production, cost, warranty, or working capital breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_99_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C01 industrial order-backlog cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C01_ORDER_DELIVERY_ACCEPTANCE_COST_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C01 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C01 cases agree, consider implementing a canonical guard that:
   - blocks order-backlog Green without named customer/product, enforceable order, delivery, acceptance, and margin bridge,
   - preserves ship-engine positives only with price survival and fresh backlog/delivery evidence,
   - treats extreme-MFE/material-MAE machine-tool event bursts as local 4B,
   - preserves industrial casting positives only with customer order and cost-pass-through evidence,
   - applies name-change, share-count, row-presence, and old corporate-action caveats where needed.

Expected next schedule:
completed_round = R1
completed_loop = 99
next_round = R2
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 99
next_round = R2
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
