# E2R Stock-Web v12 Residual Research — R3 / Loop 93

```yaml
scheduled_round: R3
scheduled_loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA

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
completed_loop: 93
next_round: R4
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_93_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 93
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate requires:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage already covered:

```text
loop88: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop89: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop90: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
loop91: C11_BATTERY_ORDERBOOK_RERATING
loop92: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
```

This run returns to C14 but uses a different fine branch:

```text
battery can / copper foil / battery equipment demand slowdown and price-survival bridge
vs generic EV/battery label beta
```

The purpose is to distinguish:

```text
battery names that still have mix, cost, or customer bridge
```

from:

```text
battery equipment/material labels whose price path collapses when EV demand and customer capex slow.
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
014820 동원시스템즈
336370 솔루스첨단소재
222080 씨아이에스
```

They avoid C14 top-covered symbols and avoid recent R3 loop91~92 names:

```text
loop91 avoid: 011790, 020150, 006110, 373220, 006400, 096770
loop92 avoid: 078600, 066970, 361610
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
014820: same archetype, new symbol, battery can / packaging mix and price-survival positive branch
336370: same archetype, new symbol, copper foil / battery material local burst then high-MAE 4B failure
222080: same archetype, new symbol, battery equipment CAPEX label shallow-MFE / high-MAE hard-4C branch
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
014820 동원시스템즈
  profile: atlas/symbol_profiles/014/014820.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,741
  corporate_action_candidate_dates:
    1999-04-26, 2002-05-31, 2005-03-15, 2013-01-28
  2024 entry~D+180 contamination: none

336370 솔루스첨단소재
  profile: atlas/symbol_profiles/336/336370.json
  name history:
    두산솔루스 until 2020-12-23
    솔루스첨단소재 from 2020-12-24
  first_date: 2019-10-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,557
  corporate_action_candidate_dates:
    2024-01-08, 2024-01-30
  selected entry after 2024-01-30 candidate; entry~D+180 direct contamination avoided
  caveat:
    candidate dates are before selected March trigger, so do not use January rows for calibration.

222080 씨아이에스
  profile: atlas/symbol_profiles/222/222080.json
  first_date: 2015-09-02
  latest market transitions:
    KOSDAQ until 2025-06-12
    KOSDAQ GLOBAL from 2025-06-13
  tradable_ohlcv rows: 2,529
  corporate_action_candidate_dates:
    2017-01-20
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C14 is the EV-demand slowdown guardrail. It is not a normal battery-positive archetype.

The model can over-score:

```text
battery equipment order hope
battery can / cylindrical cell label
copper foil / battery material label
EV recovery hope
customer capex rebound
one-week battery-theme volume spike
```

The C14 bridge must be stricter:

```text
EV demand / customer capex environment
  -> customer production and call-off schedule
  -> utilization / shipment visibility
  -> ASP / mix / cost pass-through
  -> inventory or working-capital risk
  -> margin / OP conversion
  -> price survival after the first battery-theme spike
```

A battery label is like a charging cable. It matters only if the car is actually plugged in and drawing current. C14 asks whether demand is flowing through the cable, or whether the cable is just lying on the floor.

---

## 5. Case 1 — 014820 동원시스템즈

```yaml
case_id: C14_R3L93_014820_2024_03_07
symbol: "014820"
name: "동원시스템즈"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA
trigger_date: 2024-03-07
entry_date: 2024-03-07
entry_price_basis: close
entry_price: 41600
classification: positive_capped_battery_can_packaging_mix_price_survival_bridge
calibration_usable: true
```

### Evidence interpretation

동원시스템즈 is the constructive control in this C14 set.

It is not a pure EV-demand beta case. The useful bridge is more specific:

```text
battery can / packaging and materials mix
  -> customer adoption or cylindrical-cell supply-chain relevance
  -> product mix and cost pass-through
  -> price survival despite battery-sector volatility
```

The path was volatile, but it preserved the entry better than copper-foil and equipment names, and it later made new highs. That makes it a capped positive rather than an unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-03-07: high 45,850 / close 41,600
2024-03-21: high 52,200 / close 50,700
2024-08-05: low 37,050 / close 38,000
2024-10-07: high 50,400 / close 48,400
2024-10-10: high 54,000 / close 53,600
2024-10-11: high 54,200 / close 51,500
```

Approximate path from entry close:

```text
entry_close: 41,600
peak_high: 54,200
MFE: +30.3%
worst_low: 37,050
MAE: -10.9%
```

### Interpretation

This is a C14 capped positive:

```text
Stage2-Actionable: allowed if battery-can/product-mix and cost bridge are explicit.
Stage3-Green: blocked unless customer adoption, volume, and margin conversion confirm.
Local 4B: monitor after MFE > 30%, but the initial price survival is constructive.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  ev_demand_slowdown_exposure: medium
  battery_can_packaging_bridge: medium_high
  mix_cost_pass_through: medium
  price_survival: medium_high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 6. Case 2 — 336370 솔루스첨단소재

```yaml
case_id: C14_R3L93_336370_2024_03_27
symbol: "336370"
name: "솔루스첨단소재"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA
trigger_date: 2024-03-27
entry_date: 2024-03-27
entry_price_basis: close
entry_price: 16970
classification: local_burst_high_mae_copper_foil_battery_material_without_demand_margin_bridge
calibration_usable: true
```

### Evidence interpretation

솔루스첨단소재 is the copper-foil / battery-material local-burst case.

The first move was strong. A naïve model could read it as:

```text
battery material recovery
  -> copper foil utilization rebound
  -> EV demand recovery
```

But the later path failed price survival. The signal belongs in C14 local 4B, not Green.

### Price path

Key Stock-Web rows:

```text
2024-03-27: high 16,970 / close 16,970
2024-03-28: high 19,590 / close 17,530
2024-04-11: high 21,650 / close 19,900
2024-04-12: high 21,700 / close 19,910
2024-05-30: high 17,970 / close 17,610
2024-08-05: low 11,920 / close 12,590
2024-09-10: low 11,200 / close 11,200
```

Approximate path from entry close:

```text
entry_close: 16,970
peak_high: 21,700
MFE: +27.9%
worst_low: 11,200
MAE: -34.0%
```

### Interpretation

This is a local-burst / high-MAE C14 case:

```text
Stage2-Watch: valid from battery-material relevance.
Stage2-Actionable: only as local 4B/event burst unless customer demand and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not the primary label because meaningful MFE came first, but re-entry after the burst without bridge would be 4C.
```

### Stress-test components

```text
raw_component_score_proxy:
  copper_foil_battery_label: high
  ev_demand_recovery_bridge: weak_to_medium
  utilization_margin_bridge: weak
  local_price_confirmation: high
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 222080 씨아이에스

```yaml
case_id: C14_R3L93_222080_2024_03_05
symbol: "222080"
name: "씨아이에스"
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA
trigger_date: 2024-03-05
entry_date: 2024-03-05
entry_price_basis: close
entry_price: 13150
classification: hard_4c_candidate_battery_equipment_capex_label_without_demand_calloff_bridge
calibration_usable: true
```

### Evidence interpretation

씨아이에스 is the battery-equipment hard guardrail.

The stock had an obvious March spike:

```text
battery equipment / electrode process equipment label
  -> one-day volume spike
  -> customer capex recovery hope
```

But C14 asks whether EV demand and customer capex actually support the bridge. The forward path says no: shallow MFE first, then severe MAE.

### Price path

Key Stock-Web rows:

```text
2024-03-05: high 13,800 / close 13,150
2024-03-11: high 15,110 / close 14,300
2024-03-12: high 15,100 / close 14,840
2024-04-17: low 10,330 / close 10,340
2024-08-05: low 7,800 / close 8,000
2024-08-20: high 12,230 / close 11,470
2024-10-18: low 7,920 / close 7,980
2024-11-05: high 11,390 / close 11,260
```

Approximate path from entry close:

```text
entry_close: 13,150
peak_high_before_failure: 15,110
MFE: +14.9%
worst_low: 7,800
MAE: -40.7%
```

### Interpretation

This is a hard C14 false-positive:

```text
Stage2-Watch: possible from battery-equipment relevance.
Stage2-Actionable: blocked without customer capex, order, delivery, and call-off evidence.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The later August and November spikes show that the stock can trade as an event, but the March entry was not a durable EV-demand recovery thesis.

### Stress-test components

```text
raw_component_score_proxy:
  battery_equipment_label: high
  customer_capex_bridge: weak
  ev_demand_calloff_bridge: weak
  order_delivery_visibility: weak
  price_confirmation: shallow
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

The three-case C14 grid:

```text
014820 동원시스템즈:
  battery can / packaging mix case;
  positive but capped, because Green still requires customer volume and margin bridge.

336370 솔루스첨단소재:
  copper foil / battery-material local burst;
  meaningful MFE first, but later high-MAE requires 4B/event-burst routing.

222080 씨아이에스:
  battery equipment CAPEX label failed;
  shallow MFE and high MAE, hard 4C candidate.
```

Shared rule:

```text
C14 is not "battery label bounced."
C14 is "EV demand, customer capex, utilization, call-off, and margin survive the slowdown."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C14_R3L93_014820_2024_03_07","scheduled_round":"R3","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA","symbol":"014820","name":"동원시스템즈","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":41600,"peak_high":54200,"peak_date":"2024-10-11","worst_low":37050,"worst_low_date":"2024-08-05","mfe_pct":30.3,"mae_pct":-10.9,"classification":"positive_capped_battery_can_packaging_mix_price_survival_bridge","calibration_usable":true,"evidence_family":"battery_can_packaging_mix_cost_pass_through_price_survival_bridge","residual_error":"positive_path_still_needs_customer_volume_and_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_battery_can_product_mix_margin_bridge_confirms_but_cap_green_without_customer_volume_evidence"}
{"row_type":"case","case_id":"C14_R3L93_336370_2024_03_27","scheduled_round":"R3","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA","symbol":"336370","name":"솔루스첨단소재","trigger_date":"2024-03-27","entry_date":"2024-03-27","entry_price":16970,"peak_high":21700,"peak_date":"2024-04-12","worst_low":11200,"worst_low_date":"2024-09-10","mfe_pct":27.9,"mae_pct":-34.0,"classification":"local_burst_high_mae_copper_foil_battery_material_without_demand_margin_bridge","calibration_usable":true,"evidence_family":"copper_foil_battery_material_local_burst_without_utilization_margin_bridge","residual_error":"battery_material_theme_can_create_local_mfe_but_fail_green_under_ev_demand_slowdown","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_battery_material_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C14_R3L93_222080_2024_03_05","scheduled_round":"R3","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA","symbol":"222080","name":"씨아이에스","trigger_date":"2024-03-05","entry_date":"2024-03-05","entry_price":13150,"peak_high":15110,"peak_date":"2024-03-11","worst_low":7800,"worst_low_date":"2024-08-05","mfe_pct":14.9,"mae_pct":-40.7,"classification":"hard_4c_candidate_battery_equipment_capex_label_without_demand_calloff_bridge","calibration_usable":true,"evidence_family":"battery_equipment_capex_label_without_customer_order_delivery_calloff_bridge","residual_error":"battery_equipment_volume_spike_can_overpromote_without_ev_demand_and_customer_capex_bridge","shadow_rule_candidate":"route_shallow_mfe_high_mae_battery_equipment_cases_to_hard_4c_when_calloff_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_CAN_COPPER_FOIL_EQUIPMENT_DEMAND_SLOWDOWN_PRICE_SURVIVAL_BRIDGE_VS_EV_LABEL_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":93,"canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","rule_id":"C14_EV_DEMAND_CALLOFF_UTILIZATION_PRICE_SURVIVAL_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C14, do not open Stage2-Actionable or Stage3-Green from EV recovery, battery equipment, copper foil, battery can, battery material, or one-week battery-theme spike labels alone. Require customer production, customer capex or call-off schedule, utilization or shipment visibility, ASP/mix/cost pass-through, inventory/working-capital risk check, margin/OP conversion, and post-trigger price survival. Battery-can or packaging positives may be capped positives when product mix and price survival confirm. Copper-foil/material cases with meaningful MFE followed by high MAE should remain local 4B. Battery equipment cases with shallow MFE and high MAE should route to hard-4C unless order and delivery evidence appears.","expected_effect":"Reduce EV-demand slowdown false positives while preserving battery supply-chain positives that show product mix, customer volume, and margin resilience.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":93,"canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","residual_type":"ev_demand_slowdown_calloff_utilization_price_survival_guard","contribution":"Adds one battery-can capped positive, one copper-foil local 4B failure, and one battery-equipment hard-4C counterexample to calibrate C14 EV demand slowdown routing.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C14_EV_DEMAND_CALLOFF_UTILIZATION_PRICE_SURVIVAL_REQUIRED

IF canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C:

  Do not open Stage3-Green from:
    - EV recovery headline alone
    - battery equipment label alone
    - copper foil / battery material label alone
    - battery can / cylindrical-cell label alone
    - one-week battery-theme volume spike alone

  Require at least two of:
    - customer production visibility
    - customer capex or call-off schedule
    - utilization / shipment visibility
    - ASP / mix / cost pass-through
    - inventory / working-capital risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the battery-theme spike

  If MFE < 15% and MAE < -35%:
    route to C14 hard-4C candidate.

  If MFE > 20% but MAE < -30%:
    classify as local 4B / event burst, not Green, unless fresh demand and margin bridge appears.

  If MFE > 25% and MAE remains controlled:
    allow capped Actionable only if product mix and customer-volume bridge are explicit.

  Distinguish:
    - battery can / packaging names with price survival and mix bridge
    - from copper-foil or battery-equipment names where EV demand/capex slowdown breaks utilization and margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C14 EV-demand-slowdown cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C14_EV_DEMAND_CALLOFF_UTILIZATION_PRICE_SURVIVAL_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C14 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C14 cases agree, consider implementing a canonical guard that:
   - blocks EV/battery label Green without demand, call-off, utilization, and margin bridge,
   - preserves battery-can positives only with price survival and product-mix evidence,
   - routes copper-foil/material bursts with later high MAE to local 4B,
   - routes shallow-MFE/high-MAE battery equipment spikes to hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 93
next_round = R4
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 93
next_round = R4
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
