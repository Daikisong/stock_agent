# E2R Stock-Web v12 Residual Research — R1 / Loop 98

```yaml
scheduled_round: R1
scheduled_loop: 98
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE

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
lng_project_material_case_count: 1
plant_pipe_fittings_case_count: 1
instrumentation_valve_fittings_case_count: 1
late_chase_case_count: 1
project_order_delivery_acceptance_bridge_missing_count: 1
margin_gap_or_cost_pass_through_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 98
next_round: R2
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 98
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop93: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop94: C02_POWER_GRID_DATACENTER_CAPEX
loop95: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop96: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop97: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
```

This run returns to C05 after a full R1 branch cycle, but avoids C05 top-covered symbols and avoids recent R1/R10 construction names.

Selected branch:

```text
LNG / plant / industrial project equipment
pipe fittings, instrumentation valves, cryogenic materials, project delivery,
customer acceptance, raw-material cost, FX/logistics, and margin bridge
vs generic EPC / plant project label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rows: 10
symbols: 9
date_range: 2023-03-31~2024-07-12
good/bad S2: 3/4
4B/4C: 0/0
URL pending/proxy: 0/0
top covered symbols:
  053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1)
```

Selected symbols:

```text
017960 한국카본
014620 성광벤드
105740 디케이락
```

They avoid C05 top-covered names and recent R1/R10 names:

```text
C05 top-covered avoid:
  053690, 002150, 011560, 023350, 023960, 054930

recent R1 avoid:
  loop97 C04: 051600, 052690, 130660
  loop96 C01: 267270, 210540, 241560
  loop95 C03: 064350, 272210, 448710

recent R10 avoid:
  011560, 010400, 016250
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
017960: same archetype, new symbol, LNG/project material positive with project-delivery and margin cap
014620: same archetype, new symbol, plant pipe-fitting positive with large MFE and cost/pass-through margin cap
105740: same archetype, new symbol, instrumentation valve/fitting late-chase hard-4C after project-equipment spike
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
017960 한국카본
  profile: atlas/symbol_profiles/017/017960.json
  first_date: 1995-10-10 in tradable profile
  raw_first_date: 1995-07-08
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,574
  non_tradable_zero_volume rows: 136
  corporate_action_candidate_dates:
    1996-01-03, 1999-04-26, 1999-09-13, 2012-12-27
  2024 entry~D+180 contamination: none
  caveat:
    historical row-presence/raw-discontinuity caveat exists outside selected 2024 validation window.

014620 성광벤드
  profile: atlas/symbol_profiles/014/014620.json
  first_date: 2001-01-11
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,194
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

105740 디케이락
  profile: atlas/symbol_profiles/105/105740.json
  first_date: 2010-11-12
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,756
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

Rejected candidate note:

```text
100840 SNT에너지 was checked but not used because its profile has 2024 corporate-action candidate dates
2024-04-16 and 2024-05-17. The raw-price window is therefore not a clean C05 validation candidate.
```

---

## 4. Archetype residual problem

C05 is about EPC mega-contract and long-cycle project margin gap. It is not a generic "plant equipment stock is strong" archetype.

The model can over-score:

```text
EPC / plant / LNG project label
mega-contract headline
shipbuilding / LNG carrier / offshore project readthrough
industrial equipment or fittings label
customer capex recovery headline
one-week project-equipment volume spike
late chase after project-equipment rerating
```

The C05 bridge must be stricter:

```text
EPC / mega-project / project-equipment event
  -> named project, client, geography, shipyard, or EPC package
  -> enforceable order / backlog / call-off visibility
  -> delivery, installation, inspection, and acceptance schedule
  -> raw-material / labor / energy / logistics cost pass-through
  -> FX and working-capital burden
  -> warranty / quality / delay penalty risk
  -> revenue recognition and cash collection
  -> margin / OP conversion
  -> valuation discipline after project-label spike
  -> price survival after the first project-equipment rerating
```

A C05 thesis is like a valve or cryogenic panel waiting to be installed inside a giant project. The project headline turns on the factory lights, but equity value appears only when the part is ordered, delivered, inspected, accepted, paid for, and the margin survives raw-material, FX, logistics, and delay penalties.

---

## 5. Case 1 — 017960 한국카본

```yaml
case_id: C05_R1L98_017960_2024_02_01
symbol: "017960"
name: "한국카본"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10540
classification: positive_lng_project_material_order_delivery_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

한국카본 is the constructive C05 LNG/project-material control.

The useful C05 read is not simply:

```text
LNG / 조선 / 프로젝트 수혜주가 강하다
```

It is:

```text
LNG carrier / cryogenic material / project-material relevance
  -> shipyard and LNG-project delivery readthrough
  -> order backlog and delivery schedule optionality
  -> price survival with controlled drawdown
  -> margin cap because project delivery and cost pass-through still matter
```

The forward path produced a meaningful MFE into July/August with low drawdown. This supports a positive classification. However, Green still needs fresh project/order, delivery, acceptance, raw-material cost, FX, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 10,690 / close 10,540
2024-04-24: high 11,680 / close 11,520
2024-07-24: high 12,540 / close 12,180
2024-07-29: high 12,950 / close 12,790
2024-08-05: low 10,230 / close 10,700
2024-08-20: high 13,350 / close 13,350
2024-10-25: low 10,640 / close 10,770
```

Approximate path from entry close:

```text
entry_close: 10,540
peak_high: 13,350
MFE: +26.7%
worst_low_after_entry: 9,870
MAE: -6.4%
```

### Interpretation

This is a C05 positive with Green cap:

```text
Stage2-Actionable: possible if shipyard/client project, delivery schedule, and margin bridge are explicit.
Stage3-Green: blocked without fresh order/delivery/acceptance and cost-pass-through evidence.
Local 4B: monitor after +25% MFE if project-margin evidence becomes stale.
Hard 4C: no.
Row/tradeability caveat: historical only, outside 2024 window.
```

### Stress-test components

```text
raw_component_score_proxy:
  lng_project_material_relevance: high
  named_project_customer_bridge: medium_high
  order_delivery_acceptance_bridge: medium
  raw_material_fx_cost_bridge: medium
  cash_collection_margin_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 014620 성광벤드

```yaml
case_id: C05_R1L98_014620_2024_02_01
symbol: "014620"
name: "성광벤드"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10790
classification: positive_plant_pipe_fittings_project_order_margin_bridge_with_4b_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

성광벤드 is the pipe-fittings / plant-project positive.

The setup has strong C05 relevance:

```text
pipe fittings / plant equipment
  -> LNG, shipbuilding, offshore, petrochemical, and industrial project readthrough
  -> customer order and project-delivery optionality
  -> strong price confirmation into August
```

The path produced a large MFE and did not fail the raw 2024 price test. Still, a project-equipment name can overheat if the score uses the project label without order-to-delivery-to-acceptance-to-margin evidence. The large MFE therefore deserves a 4B watch / Green cap.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 10,810 / close 10,790
2024-03-18: high 11,800 / close 11,650
2024-04-24: high 11,900 / close 11,600
2024-07-31: high 15,090 / close 14,310
2024-08-05: low 11,410 / close 12,380
2024-08-09: high 16,190 / close 15,300
2024-08-20: high 16,900 / close 16,350
2024-10-25: low 12,770 / close 12,770
```

Approximate path from entry close:

```text
entry_close: 10,790
peak_high: 16,900
MFE: +56.6%
worst_low_after_entry: 10,020
MAE: -7.1%
```

### Interpretation

This is a strong C05 positive with 4B/Green cap:

```text
Stage2-Actionable: valid if customer order, project package, delivery, and pass-through margin bridge are explicit.
Stage3-Green: blocked after large MFE unless fresh evidence confirms delivery/acceptance and margin.
Local 4B: monitor if project-label price outruns order/margin evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  plant_pipe_fittings_relevance: high
  lng_offshore_project_readthrough: high
  order_delivery_bridge: medium_high
  cost_pass_through_bridge: medium
  margin_op_bridge: medium_high
  price_confirmation: very_high
  valuation_overheat_risk: medium_high
  green_cap: required_after_large_mfe
```

---

## 7. Case 3 — 105740 디케이락

```yaml
case_id: C05_R1L98_105740_2024_07_29
symbol: "105740"
name: "디케이락"
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE
trigger_date: 2024-07-29
entry_date: 2024-07-29
entry_price_basis: close
entry_price: 9680
classification: hard_4c_candidate_instrumentation_valve_fittings_project_equipment_late_chase_without_delivery_margin_survival
calibration_usable: true
```

### Evidence interpretation

디케이락 is the late-chase C05 guardrail.

The label can fool the model:

```text
instrumentation valve / fittings / plant equipment
  -> LNG / petrochemical / offshore project readthrough
  -> one-day project-equipment volume spike
  -> small-cap project-equipment beta
```

The stock had earlier project-equipment momentum, but from the selected July 29 late-spike close, the forward path did not validate incremental order, delivery, customer acceptance, or margin survival. MFE was shallow and the August/September drawdown was hard-zone.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 9,280 / close 8,920
2024-07-29: high 10,300 / close 9,680
2024-08-05: low 6,690 / close 7,270
2024-08-21: high 9,190 / close 8,750
2024-09-06: low 7,570 / close 7,570
2024-10-25: low 7,100 / close 7,100
2024-11-07: high 8,290 / close 7,900
```

Approximate path from late entry close:

```text
entry_close: 9,680
peak_high_after_entry: 10,300
MFE: +6.4%
worst_low_after_entry: 6,690
MAE: -30.9%
```

### Interpretation

This is a hard C05 false-positive candidate:

```text
Stage2-Watch: possible from instrumentation valve/fittings and plant-equipment relevance.
Stage2-Actionable: blocked unless enforceable order, customer/project package, delivery/acceptance, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that a project-equipment late chase is not order-delivery-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  instrumentation_valve_fittings_relevance: high
  project_equipment_label: high
  named_customer_order_bridge: weak
  delivery_acceptance_bridge: weak
  cost_margin_bridge: weak_to_medium
  price_confirmation_after_entry: shallow
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
lng_project_material_case_count: 1
plant_pipe_fittings_case_count: 1
instrumentation_valve_fittings_case_count: 1
late_chase_case_count: 1
project_order_delivery_acceptance_bridge_missing_count: 1
margin_gap_or_cost_pass_through_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C05 project-equipment grid:

```text
017960 한국카본:
  LNG / project material positive;
  meaningful MFE and low MAE, but Green requires fresh order/delivery/acceptance and cost-pass-through evidence.

014620 성광벤드:
  plant pipe-fitting positive;
  large MFE and low MAE, but 4B/Green cap required after rerating.

105740 디케이락:
  instrumentation valve / plant-equipment late chase failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C05 is not "EPC or plant project label is hot."
C05 is "project order, customer package, delivery, inspection/acceptance, cash collection, raw-material/FX/logistics pass-through, and margin conversion are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C05_R1L98_017960_2024_02_01","scheduled_round":"R1","scheduled_loop":98,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE","symbol":"017960","name":"한국카본","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10540,"peak_high":13350,"peak_date":"2024-08-20","worst_low_after_entry":9870,"worst_low_after_entry_date":"2024-03-08","mfe_pct":26.7,"mae_pct":-6.4,"classification":"positive_lng_project_material_order_delivery_margin_bridge_with_green_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"lng_project_material_shipyard_customer_order_delivery_acceptance_cost_pass_through_margin_bridge","residual_error":"positive_lng_project_material_path_requires_green_cap_without_refreshed_order_delivery_acceptance_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_project_order_delivery_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C05_R1L98_014620_2024_02_01","scheduled_round":"R1","scheduled_loop":98,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE","symbol":"014620","name":"성광벤드","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10790,"peak_high":16900,"peak_date":"2024-08-20","worst_low_after_entry":10020,"worst_low_after_entry_date":"2024-04-17","mfe_pct":56.6,"mae_pct":-7.1,"classification":"positive_plant_pipe_fittings_project_order_margin_bridge_with_4b_after_large_mfe","calibration_usable":true,"evidence_family":"plant_pipe_fittings_lng_offshore_project_customer_order_delivery_cost_pass_through_margin_bridge","residual_error":"large_project_fitting_rerating_requires_4b_green_cap_if_delivery_acceptance_and_margin_evidence_not_refreshed","shadow_rule_candidate":"preserve_project_fittings_positive_but_attach_green_cap_after_large_mfe_without_fresh_margin_evidence"}
{"row_type":"case","case_id":"C05_R1L98_105740_2024_07_29","scheduled_round":"R1","scheduled_loop":98,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE","symbol":"105740","name":"디케이락","trigger_date":"2024-07-29","entry_date":"2024-07-29","entry_price":9680,"peak_high":10300,"peak_date":"2024-07-29","worst_low_after_entry":6690,"worst_low_after_entry_date":"2024-08-05","mfe_pct":6.4,"mae_pct":-30.9,"classification":"hard_4c_candidate_instrumentation_valve_fittings_project_equipment_late_chase_without_delivery_margin_survival","calibration_usable":true,"evidence_family":"instrumentation_valve_fittings_project_equipment_late_chase_without_named_customer_order_delivery_acceptance_margin_bridge","residual_error":"project_equipment_late_chase_can_fail_when_order_delivery_acceptance_and_margin_bridge_missing","shadow_rule_candidate":"route_instrumentation_fittings_late_chase_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_project_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":98,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","fine_archetype_id":"LNG_PLANT_PROJECT_EQUIPMENT_FITTINGS_LONG_CYCLE_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_VS_EPC_PROJECT_LABEL_LATE_CHASE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"lng_project_material_case_count":1,"plant_pipe_fittings_case_count":1,"instrumentation_valve_fittings_case_count":1,"late_chase_case_count":1,"project_order_delivery_acceptance_bridge_missing_count":1,"margin_gap_or_cost_pass_through_caveat_count":2,"row_presence_or_old_corporate_action_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":98,"canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","rule_id":"C05_PROJECT_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C05 EPC mega-contract / project-equipment cases, do not open Stage2-Actionable or Stage3-Green from EPC, plant, LNG project, mega-contract, shipbuilding/offshore project readthrough, industrial equipment/fittings, customer capex recovery, one-week project-equipment volume spike, or late chase after project-equipment rerating labels alone. Require named project/client/geography/shipyard/EPC package, enforceable order/backlog/call-off visibility, delivery/installation/inspection/acceptance schedule, raw-material/labor/energy/logistics cost pass-through, FX and working-capital burden check, warranty/quality/delay penalty risk control, revenue recognition and cash collection, margin/OP conversion, valuation discipline after the first project-label spike, and post-trigger price survival. LNG/project-material and pipe-fitting positives with large MFE may be capped Actionable when project-order and margin bridge are explicit, but Green requires fresh evidence. Instrumentation/fittings late chases with shallow MFE and hard-zone MAE should route to hard-4C when named customer order, delivery/acceptance, and margin bridge are missing.","expected_effect":"Preserve true LNG/plant project equipment positives while reducing EPC/project label and late-chase false positives where order, delivery, acceptance, cost pass-through, cash collection, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":98,"canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","residual_type":"project_order_delivery_acceptance_margin_guard","contribution":"Adds one LNG/project material positive, one plant pipe-fitting positive with Green cap, and one instrumentation-valve late-chase hard-4C candidate to calibrate C05 project order, delivery, acceptance, cost pass-through, working capital, cash collection, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C05_PROJECT_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP:

  Do not open Stage3-Green from:
    - EPC / plant / LNG project label alone
    - mega-contract headline alone
    - shipbuilding / LNG carrier / offshore project readthrough alone
    - industrial equipment / fittings label alone
    - customer capex recovery headline alone
    - one-week project-equipment volume spike alone
    - late chase after project-equipment rerating alone

  Require at least two of:
    - named project / client / geography / shipyard / EPC package
    - enforceable order / backlog / call-off visibility
    - delivery / installation / inspection / acceptance schedule
    - raw-material / labor / energy / logistics cost pass-through
    - FX / working-capital burden control
    - warranty / quality / delay-penalty risk containment
    - revenue recognition and cash collection
    - margin / OP conversion
    - valuation discipline after first project-label spike
    - low-MAE post-trigger price survival
    - fresh evidence after the project-equipment headline

  If MFE < 8% and MAE <= -30%:
    route to C05 hard-4C candidate.

  If MFE > 20% but project-order or delivery evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is large but raw-material / FX / logistics / warranty cost risk is unresolved:
    cap Green until margin evidence refreshes.

  Distinguish:
    - suppliers where project label becomes order, delivery, acceptance, cash collection, and margin
    - from project labels where late chase, cost pass-through, or delivery risk breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_98_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C05 EPC/project-equipment margin-gap cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C05_PROJECT_ORDER_DELIVERY_ACCEPTANCE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C05 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C05 cases agree, consider implementing a canonical guard that:
   - blocks EPC/project-equipment Green without named project, customer, enforceable order, delivery, acceptance, and margin bridge,
   - preserves LNG/project-material positives only with price survival and fresh order/delivery evidence,
   - caps pipe-fitting positives after large MFE when cost/pass-through evidence is stale,
   - routes shallow-MFE/hard-zone-MAE instrumentation/fittings late chases to hard-4C,
   - applies row-presence and old corporate-action caveats where needed.

Expected next schedule:
completed_round = R1
completed_loop = 98
next_round = R2
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 98
next_round = R2
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
