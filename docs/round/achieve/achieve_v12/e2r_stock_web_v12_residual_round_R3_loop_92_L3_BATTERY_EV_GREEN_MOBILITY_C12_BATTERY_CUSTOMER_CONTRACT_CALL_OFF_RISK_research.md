# E2R Stock-Web v12 Residual Research — R3 / Loop 92

```yaml
scheduled_round: R3
scheduled_loop: 92
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 92
next_round: R4
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 92
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
```

This run returns to C12, but uses a different fine branch:

```text
battery material / separator customer call-off and utilization bridge
vs contract, capacity, and customer-label spike
```

The goal is not to repeat battery orderbook rerating from loop91. The goal is to calibrate whether long-term customer or capacity language actually becomes called-off volume, utilization, ASP, margin, and price survival.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
rows: 28
symbols: 11
date_range: 2022-01-13~2024-07-02
good/bad S2: 9/6
4B/4C: 0/0
URL pending/proxy: 13/9
top covered symbols:
  121600(7), 278280(5), 020150(4), 348370(3), 091580(2), 137400(2)
```

Selected symbols:

```text
078600 대주전자재료
066970 엘앤에프
361610 SK아이이테크놀로지
```

They avoid the C12 top-covered symbols and avoid recent R3 symbols:

```text
011790, 020150, 006110, 373220, 006400, 096770
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
078600: same archetype, new symbol, silicon-anode/customer qualification positive with 4B watch
066970: same archetype, new symbol, cathode-material customer call-off / margin failure branch
361610: same archetype, new symbol, separator utilization / customer call-off hard-4C branch
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
078600 대주전자재료
  profile: atlas/symbol_profiles/078/078600.json
  first_date: 2004-12-10
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,230
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

066970 엘앤에프
  profile: atlas/symbol_profiles/066/066970.json
  first_date: 2003-01-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,711
  corporate_action_candidate_dates:
    2016-02-19, 2021-08-11
  2024 entry~D+180 contamination: none

361610 SK아이이테크놀로지
  profile: atlas/symbol_profiles/361/361610.json
  first_date: 2021-05-11
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,171
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C12 is not the same as C11 orderbook rerating.

C11 asks whether the market rerates a visible orderbook. C12 asks the harsher question:

```text
does the customer actually call off the contract volume?
```

The model can over-score:

```text
long-term supply contract
battery customer name
capacity expansion
separator / cathode / silicon-anode label
EV recovery hope
one-week customer-rumor spike
```

The bridge must be stricter:

```text
contract or customer label
  -> firm call-off volume
  -> utilization
  -> ASP / mix
  -> inventory and working-capital risk
  -> gross margin / OP conversion
  -> post-trigger price survival
```

A battery supply contract is like a reservation at a factory. It matters only when the customer arrives, takes the product, pays the price, and leaves margin after cost. A reservation that is delayed, reduced, or repriced can become a trap.

---

## 5. Case 1 — 078600 대주전자재료

```yaml
case_id: C12_R3L92_078600_2024_05_14
symbol: "078600"
name: "대주전자재료"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE
trigger_date: 2024-05-14
entry_date: 2024-05-14
entry_price_basis: close
entry_price: 100800
classification: positive_with_local_4b_silicon_anode_customer_qualification_calloff_bridge
calibration_usable: true
```

### Evidence interpretation

대주전자재료 is the constructive control in this set.

The useful C12 read is not "battery material stock went up." It is more specific:

```text
silicon-anode / advanced battery material relevance
  -> customer qualification or adoption expectation
  -> call-off and ramp possibility
  -> margin-rich material mix
  -> sharp price confirmation
```

The price path gave a large MFE in the early window. But the later drawdown was large enough that C12 should not keep Green open without new call-off or margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-05-14: close 100,800
2024-05-30: high 123,000 / close 121,300
2024-06-11: high 160,000 / close 155,800
2024-06-12: high 163,400 / close 160,000
2024-06-26: high 156,500 / close 151,600
2024-08-05: sharp market-low window, but price still above entry
2024-09-09: low 89,400 / close 93,200
2024-11-15: low 73,600 / close 82,600
```

Approximate path from entry close:

```text
entry_close: 100,800
peak_high: 163,400
MFE: +62.1%
worst_low: 73,600
MAE: -27.0%
peak_to_later_low_drawdown: -55.0%
```

### Interpretation

This is a positive entry, but with a mandatory local 4B overlay:

```text
Stage2-Actionable: valid if customer qualification / call-off / ramp bridge is explicit.
Stage3-Green: blocked without fresh call-off and margin confirmation after the blowoff.
Local 4B: required after +60% MFE and later high drawdown.
Hard 4C: no for initial positive path, but later deterioration must be watched.
```

### Stress-test components

```text
raw_component_score_proxy:
  advanced_material_relevance: high
  customer_qualification_signal: medium_high
  calloff_visibility: medium
  margin_mix_bridge: medium_high
  price_confirmation: very_high
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 066970 엘앤에프

```yaml
case_id: C12_R3L92_066970_2024_03_20
symbol: "066970"
name: "엘앤에프"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 178000
classification: hard_4c_candidate_cathode_material_customer_calloff_margin_failure
calibration_usable: true
```

### Evidence interpretation

엘앤에프 is the cathode-material customer/call-off false-positive.

It had all the right labels:

```text
cathode material
large EV customer ecosystem
battery supply-chain relevance
capacity and contract language
```

But C12 exists because these labels are not enough. The forward path shows that customer call-off, ASP, inventory, and margin risk were not resolved at the trigger.

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 178,000
2024-03-25: high 199,000 / close 186,300
2024-04-17: low 140,600 / close 140,600
2024-06-13: high 177,000 / close 171,600
2024-06-28: low 134,100 / close 135,300
2024-09-10: low 82,900 / close 82,900
2024-10-08: high 120,600 / close 118,700
2024-11-15: low 93,500 / close 97,500
```

Approximate path from entry close:

```text
entry_close: 178,000
peak_high: 199,000
MFE: +11.8%
worst_low: 82,900
MAE: -53.4%
```

### Interpretation

This is a hard C12 guardrail case:

```text
Stage2-Watch: allowed from cathode/customer relevance.
Stage2-Actionable: blocked unless call-off, utilization, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is simple: customer ecosystem relevance is not customer volume realization.

### Stress-test components

```text
raw_component_score_proxy:
  customer_contract_label: high
  calloff_visibility: weak
  utilization_bridge: weak
  margin_bridge: weak
  inventory_working_capital_risk: high
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 361610 SK아이이테크놀로지

```yaml
case_id: C12_R3L92_361610_2024_03_20
symbol: "361610"
name: "SK아이이테크놀로지"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 74900
classification: hard_4c_candidate_separator_utilization_calloff_failure
calibration_usable: true
```

### Evidence interpretation

SK아이이테크놀로지 is the separator utilization / call-off failure case.

The battery separator label can look safe because it sounds like a critical component. But C12 should not promote it unless the model can prove:

```text
customer call-off
separator plant utilization
pricing / spread
inventory normalization
margin recovery
```

The forward path was severe.

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 74,900
2024-03-26: high 77,700 / close 75,500
2024-04-17: low 59,800 / close 59,800
2024-05-31: low 43,100 / close 43,150
2024-06-20: high 49,400 / close 46,150
2024-08-05: market-low window; price remained far below entry
2024-09-10: low 30,050 / close 30,050
2024-11-15: low 24,350 / close 25,150
```

Approximate path from entry close:

```text
entry_close: 74,900
peak_high: 77,700
MFE: +3.7%
worst_low: 24,350
MAE: -67.5%
```

### Interpretation

This is a hard C12 false-positive:

```text
Stage2-Watch: possible from separator/customer relevance.
Stage2-Actionable: blocked without utilization and margin bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

This case shows why C12 must be harsher than C11. A component can be critical, but if utilization collapses or call-off is delayed, the equity path can still fail.

### Stress-test components

```text
raw_component_score_proxy:
  separator_component_relevance: high
  customer_calloff_visibility: weak
  utilization_bridge: weak
  margin_recovery: weak
  price_confirmation: failed
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C12 grid:

```text
078600 대주전자재료:
  advanced silicon-anode material positive with strong MFE,
  but local 4B required after blowoff and later drawdown.

066970 엘앤에프:
  cathode customer/contract label failed.
  Shallow MFE and deep MAE make it hard 4C.

361610 SK아이이테크놀로지:
  separator critical-component label failed badly.
  Utilization/call-off bridge missing, hard 4C.
```

Shared rule:

```text
C12 is not "customer or contract label exists."
C12 is "customer call-off, utilization, ASP, and margin actually convert."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C12_R3L92_078600_2024_05_14","scheduled_round":"R3","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE","symbol":"078600","name":"대주전자재료","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":100800,"peak_high":163400,"peak_date":"2024-06-12","worst_low":73600,"worst_low_date":"2024-11-15","mfe_pct":62.1,"mae_pct":-27.0,"peak_to_later_low_drawdown_pct":-55.0,"classification":"positive_with_local_4b_silicon_anode_customer_qualification_calloff_bridge","calibration_usable":true,"evidence_family":"silicon_anode_customer_qualification_calloff_margin_bridge","residual_error":"positive_entry_but_large_mfe_requires_4b_when_calloff_margin_bridge_not_refreshed","shadow_rule_candidate":"allow_actionable_when_customer_qualification_calloff_margin_bridge_confirms; attach_4b_after_large_mfe_drawdown"}
{"row_type":"case","case_id":"C12_R3L92_066970_2024_03_20","scheduled_round":"R3","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE","symbol":"066970","name":"엘앤에프","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":178000,"peak_high":199000,"peak_date":"2024-03-25","worst_low":82900,"worst_low_date":"2024-09-10","mfe_pct":11.8,"mae_pct":-53.4,"classification":"hard_4c_candidate_cathode_material_customer_calloff_margin_failure","calibration_usable":true,"evidence_family":"cathode_material_customer_contract_label_without_calloff_margin_bridge","residual_error":"customer_contract_label_can_overpromote_without_calloff_utilization_margin_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_calloff_margin_bridge_missing"}
{"row_type":"case","case_id":"C12_R3L92_361610_2024_03_20","scheduled_round":"R3","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE","symbol":"361610","name":"SK아이이테크놀로지","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":74900,"peak_high":77700,"peak_date":"2024-03-26","worst_low":24350,"worst_low_date":"2024-11-15","mfe_pct":3.7,"mae_pct":-67.5,"classification":"hard_4c_candidate_separator_utilization_calloff_failure","calibration_usable":true,"evidence_family":"separator_customer_calloff_utilization_margin_failure","residual_error":"critical_component_label_can_fail_when_customer_calloff_and_utilization_collapse","shadow_rule_candidate":"route_separator_component_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_utilization_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"BATTERY_MATERIAL_CUSTOMER_CALL_OFF_UTILIZATION_MARGIN_BRIDGE_VS_CONTRACT_AND_CAPACITY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":92,"canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","rule_id":"C12_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C12, do not open Stage2-Actionable or Stage3-Green from battery customer, long-term contract, capacity expansion, separator/cathode/silicon-anode label, or one-week customer-rumor spike alone. Require customer call-off volume, utilization, ASP or mix, inventory/working-capital risk check, margin/OP conversion, and post-trigger price survival. If MFE is shallow and MAE is large, route to hard-4C. If MFE is large but peak-to-later-low drawdown is high and no fresh call-off evidence appears, preserve positive entry but attach local 4B watch.","expected_effect":"Reduce battery contract/customer false positives while preserving true advanced-material positives where customer qualification, call-off, utilization, and margin conversion are visible.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":92,"canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","residual_type":"battery_customer_calloff_utilization_margin_guard","contribution":"Adds one silicon-anode positive with local 4B watch and two cathode/separator hard-4C counterexamples to calibrate C12 call-off, utilization, margin, and price-survival routing.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C12_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK:

  Do not open Stage3-Green from:
    - customer name or ecosystem label alone
    - long-term supply contract headline alone
    - capacity expansion headline alone
    - cathode / separator / silicon-anode material label alone
    - one-week battery material spike alone

  Require at least two of:
    - customer call-off volume
    - utilization / ramp schedule
    - ASP or product-mix bridge
    - inventory / working-capital risk check
    - margin or OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after contract or customer headline

  If MFE < 15% and MAE < -35%:
    route to C12 hard-4C candidate.

  If MFE > 50% but peak-to-later-low drawdown < -40%:
    preserve positive entry but attach local 4B watch unless fresh call-off/margin bridge appears.

  If component is critical but utilization/call-off is weak:
    cap at Watch or route to false-positive guard.

  Distinguish:
    - advanced materials with customer qualification and price confirmation
    - from contract/customer labels where volume, utilization, and margin are not actually realized.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C12 battery customer/call-off cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C12_CUSTOMER_CALLOFF_UTILIZATION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C12 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C12 cases agree, consider implementing a canonical guard that:
   - blocks customer/contract/capacity label Green without call-off and utilization bridge,
   - preserves advanced-material positives only with price survival and margin confirmation,
   - attaches local 4B after large MFE and deep peak drawdown,
   - routes shallow-MFE/high-MAE cathode/separator names to hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 92
next_round = R4
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 92
next_round = R4
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
