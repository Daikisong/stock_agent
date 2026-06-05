# E2R Stock-Web v12 Residual Research — R2 / Loop 93

```yaml
scheduled_round: R2
scheduled_loop: 93
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 93
next_round: R3
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_93_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 93
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires L2 semiconductor / AI / electronics work. Recent R2 branch usage already covered:

```text
loop89: C06_HBM_MEMORY_CUSTOMER_CAPACITY
loop90: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop91: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
loop92: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

This run selects the remaining R2 branch:

```text
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
rows: 29
symbols: 18
date_range: 2023-03-31~2024-06-14
good/bad S2: 15/5
4B/4C: 1/0
URL pending/proxy: 16/10
top covered symbols:
  089970(3), 281820(3), 319660(3), 042700(2), 064290(2), 079370(2)
```

Selected symbols:

```text
036930 주성엔지니어링
053610 프로텍
083310 엘오티베큠
```

They avoid the C10 top-covered symbols and avoid recent R2 loop90~92 names:

```text
042700, 064760, 031980, 039030, 403870, 232140, 131970, 330860, 084370, 240810, 036810
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
036930: same archetype, new symbol, ALD/deposition equipment memory-recovery positive with local 4B failure
053610: same archetype, new symbol, packaging/dispenser equipment cycle label without durable margin-delivery bridge
083310: same archetype, new symbol, vacuum equipment memory-cycle label without sustained order/utilization bridge
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
036930 주성엔지니어링
  profile: atlas/symbol_profiles/036/036930.json
  first_date: 1999-12-24
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 6,444
  corporate_action_candidate_dates:
    2000-06-22
  2024 entry~D+180 contamination: none

053610 프로텍
  profile: atlas/symbol_profiles/053/053610.json
  first_date: 2001-08-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,027
  corporate_action_candidate_dates:
    2005-11-24, 2006-02-28
  2024 entry~D+180 contamination: none

083310 엘오티베큠
  profile: atlas/symbol_profiles/083/083310.json
  first_date: 2005-10-05
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,028
  corporate_action_candidate_dates:
    2007-05-29, 2007-06-19
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C10 is about a memory-recovery equipment cycle, not a generic "semiconductor equipment stock."

The model can over-score:

```text
memory capex recovery
HBM / DRAM / NAND cycle
semiconductor equipment label
deposition / vacuum / dispenser equipment
customer capex hope
one-week equipment-volume spike
```

The C10 bridge must be stricter:

```text
memory recovery
  -> customer capex plan
  -> tool qualification
  -> purchase order / delivery timing
  -> utilization or shipment visibility
  -> margin / OP conversion
  -> price survival after the first capex-cycle rally
```

A memory recovery is like a factory waking up after a cold night. The lights turning on is not the same as every machine receiving a paid purchase order. C10 must check whether the recovery reaches the company's order book, delivery schedule, and margin.

---

## 5. Case 1 — 036930 주성엔지니어링

```yaml
case_id: C10_R2L93_036930_2024_02_22
symbol: "036930"
name: "주성엔지니어링"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 31900
classification: positive_with_local_4b_ald_deposition_memory_recovery_equipment_cycle
calibration_usable: true
```

### Evidence interpretation

주성엔지니어링 is the constructive control, but it is not a clean hold-through Green.

The useful C10 bridge is:

```text
memory capex recovery
  -> deposition / ALD equipment relevance
  -> equipment cycle participation
  -> order or delivery expectations
  -> price confirmation
```

The price path rewarded the early cycle entry, but later drawdown was too large to keep Green open without fresh order/delivery/margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-22: close 31,900
2024-02-28: high 40,750 / close 40,000
2024-04-08: high 41,450 / close 36,500
2024-08-05: low 22,150 / close 23,200
2024-09-10: low 22,050 / close 22,300
2024-11-04: high 34,050 / close 32,400
```

Approximate path from entry close:

```text
entry_close: 31,900
peak_high: 41,450
MFE: +29.9%
worst_low: 22,050
MAE: -30.9%
```

### Interpretation

This is a positive entry with local 4B discipline:

```text
Stage2-Actionable: valid if customer capex / order / delivery bridge is explicit.
Stage3-Green: blocked after the drawdown unless fresh order or margin revision appears.
Local 4B: required because the positive MFE later became high-MAE.
Hard 4C: no for the original early entry, but late re-entry without evidence would be false-positive risk.
```

### Stress-test components

```text
raw_component_score_proxy:
  memory_recovery_relevance: high
  deposition_equipment_relevance: high
  order_delivery_bridge: medium
  price_confirmation: high
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 053610 프로텍

```yaml
case_id: C10_R2L93_053610_2024_03_04
symbol: "053610"
name: "프로텍"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA
trigger_date: 2024-03-04
entry_date: 2024-03-04
entry_price_basis: close
entry_price: 49100
classification: hard_4c_candidate_packaging_dispenser_equipment_cycle_label_without_delivery_margin_bridge
calibration_usable: true
```

### Evidence interpretation

프로텍 is the packaging / dispenser equipment false-positive.

It had enough equipment-cycle relevance to look attractive in a broad R2 rally:

```text
semiconductor equipment label
advanced packaging / dispenser relevance
memory and AI equipment sympathy
```

But the price path says the label did not become durable order, delivery, or margin conversion at the trigger.

### Price path

Key Stock-Web rows:

```text
2024-03-04: close 49,100
2024-03-05: high 54,800 / close 52,800
2024-03-12: high 56,300 / close 53,100
2024-04-04: low 40,500 / close 46,000
2024-08-05: low 21,150 / close 21,750
2024-09-26: high 30,400 / close 29,900
2024-10-08: high 33,300 / close 33,150
```

Approximate path from entry close:

```text
entry_close: 49,100
peak_high: 56,300
MFE: +14.7%
worst_low: 21,150
MAE: -56.9%
```

### Interpretation

This is a hard C10 guardrail case:

```text
Stage2-Watch: possible from equipment-cycle relevance.
Stage2-Actionable: blocked unless order / delivery / margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
```

The lesson is that equipment relevance is not enough. The recovery must be seen in orders, shipment timing, utilization, and margin.

### Stress-test components

```text
raw_component_score_proxy:
  equipment_label_quality: medium_high
  memory_cycle_beta: medium_high
  order_delivery_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 083310 엘오티베큠

```yaml
case_id: C10_R2L93_083310_2024_02_22
symbol: "083310"
name: "엘오티베큠"
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
fine_archetype_id: MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 23350
classification: hard_4c_candidate_vacuum_equipment_memory_cycle_label_without_sustained_order_utilization_bridge
calibration_usable: true
```

### Evidence interpretation

엘오티베큠 is the vacuum-equipment memory-cycle false-positive.

The stock reacted sharply on 2024-02-22, so a naive model can treat it as:

```text
memory recovery + equipment label + cycle participation = Actionable
```

But the move was not sustained. The forward path failed badly without a durable order/utilization bridge.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 23,450 / close 23,350
2024-02-23: high 24,450 / close 22,400
2024-03-08: high 24,050 / close 23,500
2024-04-16: low 20,000 / close 20,150
2024-08-05: low 9,880 / close 10,200
2024-09-06: low 10,030 / close 10,040
2024-10-25: low 9,340 / close 9,340
```

Approximate path from entry close:

```text
entry_close: 23,350
peak_high: 24,450
MFE: +4.7%
worst_low: 9,340
MAE: -60.0%
```

### Interpretation

This is a hard C10 false-positive:

```text
Stage2-Watch: possible from vacuum equipment / memory capex relevance.
Stage2-Actionable: blocked without customer order, utilization, and margin bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

The label was close to the cycle, but the equity path did not survive.

### Stress-test components

```text
raw_component_score_proxy:
  vacuum_equipment_relevance: high
  memory_cycle_beta: medium_high
  order_delivery_bridge: weak
  utilization_bridge: weak
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
calibration_usable_trigger_count: 3
```

The three-case C10 grid:

```text
036930 주성엔지니어링:
  early memory-recovery/deposition-equipment positive,
  but later high MAE requires local 4B and fresh order/margin confirmation.

053610 프로텍:
  packaging/dispenser equipment-cycle label failed.
  Shallow MFE and extreme MAE, hard 4C.

083310 엘오티베큠:
  vacuum-equipment memory-cycle spike failed.
  Almost no durable MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C10 is not "semiconductor equipment cycle is back."
C10 is "customer capex becomes company-specific order, delivery, utilization, and margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C10_R2L93_036930_2024_02_22","scheduled_round":"R2","scheduled_loop":93,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA","symbol":"036930","name":"주성엔지니어링","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":31900,"peak_high":41450,"peak_date":"2024-04-08","worst_low":22050,"worst_low_date":"2024-09-10","mfe_pct":29.9,"mae_pct":-30.9,"classification":"positive_with_local_4b_ald_deposition_memory_recovery_equipment_cycle","calibration_usable":true,"evidence_family":"ald_deposition_equipment_memory_capex_recovery_order_delivery_margin_bridge","residual_error":"positive_early_cycle_entry_requires_4b_after_later_high_mae_without_fresh_order_margin_bridge","shadow_rule_candidate":"allow_actionable_when_customer_capex_order_delivery_bridge_confirms_but_attach_4b_after_high_mae"}
{"row_type":"case","case_id":"C10_R2L93_053610_2024_03_04","scheduled_round":"R2","scheduled_loop":93,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA","symbol":"053610","name":"프로텍","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":49100,"peak_high":56300,"peak_date":"2024-03-12","worst_low":21150,"worst_low_date":"2024-08-05","mfe_pct":14.7,"mae_pct":-56.9,"classification":"hard_4c_candidate_packaging_dispenser_equipment_cycle_label_without_delivery_margin_bridge","calibration_usable":true,"evidence_family":"packaging_dispenser_equipment_cycle_label_without_order_delivery_margin_bridge","residual_error":"equipment_cycle_label_can_overpromote_without_company_specific_order_and_margin_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_extreme_and_delivery_margin_bridge_missing"}
{"row_type":"case","case_id":"C10_R2L93_083310_2024_02_22","scheduled_round":"R2","scheduled_loop":93,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA","symbol":"083310","name":"엘오티베큠","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":23350,"peak_high":24450,"peak_date":"2024-02-23","worst_low":9340,"worst_low_date":"2024-10-25","mfe_pct":4.7,"mae_pct":-60.0,"classification":"hard_4c_candidate_vacuum_equipment_memory_cycle_label_without_sustained_order_utilization_bridge","calibration_usable":true,"evidence_family":"vacuum_equipment_memory_cycle_label_without_sustained_order_utilization_margin_bridge","residual_error":"vacuum_equipment_label_can_spike_with_memory_cycle_but_fail_price_survival","shadow_rule_candidate":"route_vacuum_equipment_cycle_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":93,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_SEMI_EQUIPMENT_ORDER_DELIVERY_MARGIN_BRIDGE_VS_CAPEX_LABEL_CYCLE_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":93,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","rule_id":"C10_CUSTOMER_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C10, do not open Stage2-Actionable or Stage3-Green from memory capex recovery, semiconductor equipment label, deposition/vacuum/packaging equipment label, or one-week equipment-cycle volume spike alone. Require customer capex plan, tool qualification, purchase order or delivery timing, utilization or shipment visibility, margin/OP conversion, and post-trigger price survival. Early cycle positives may be Actionable when order/delivery bridge is explicit, but later high MAE requires local 4B unless fresh order or margin evidence appears. Equipment names with shallow MFE and extreme MAE should route to hard-4C when company-specific order and utilization bridge are missing.","expected_effect":"Reduce memory-equipment cycle false positives while preserving early equipment positives with customer capex, delivery, utilization, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":93,"canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","residual_type":"memory_equipment_order_delivery_margin_guard","contribution":"Adds one ALD/deposition early-cycle positive with 4B watch and two packaging/vacuum equipment hard-4C counterexamples to calibrate C10 customer capex and order-delivery requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C10_CUSTOMER_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:

  Do not open Stage3-Green from:
    - memory capex recovery headline alone
    - semiconductor equipment label alone
    - deposition / vacuum / packaging equipment label alone
    - HBM / DRAM / NAND sympathy alone
    - one-week equipment-cycle volume spike alone

  Require at least two of:
    - customer capex plan
    - tool qualification
    - purchase order or shipment visibility
    - delivery timing
    - utilization or ramp schedule
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the capex headline

  If MFE < 15% and MAE < -40%:
    route to C10 hard-4C candidate.

  If MFE > 25% but later MAE < -30%:
    preserve positive early-cycle entry but attach local 4B unless fresh order/margin evidence appears.

  Distinguish:
    - early-cycle equipment names with real customer capex and delivery bridge
    - from equipment labels where cycle beta appears but order/utilization/margin conversion is not visible.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C10 memory-recovery equipment-cycle cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C10_CUSTOMER_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C10 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C10 cases agree, consider implementing a canonical guard that:
   - blocks equipment-cycle Green without customer capex/order/delivery/margin bridge,
   - preserves early-cycle ALD/deposition positives only with price survival or fresh evidence,
   - attaches local 4B after large MFE followed by high MAE,
   - routes shallow-MFE/high-MAE packaging/vacuum equipment labels to hard-4C.

Expected next schedule:
completed_round = R2
completed_loop = 93
next_round = R3
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 93
next_round = R3
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
