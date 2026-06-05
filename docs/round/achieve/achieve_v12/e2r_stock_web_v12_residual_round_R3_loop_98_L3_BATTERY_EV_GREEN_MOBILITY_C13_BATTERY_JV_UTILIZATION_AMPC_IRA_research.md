# E2R Stock-Web v12 Residual Research — R3 / Loop 98

```yaml
scheduled_round: R3
scheduled_loop: 98
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
separator_jv_utilization_case_count: 1
silicon_anode_material_case_count: 1
electrolyte_material_cross_readthrough_case_count: 1
battery_jv_utilization_bridge_missing_count: 2
customer_order_margin_bridge_missing_count: 2
ampc_ira_bridge_missing_count: 2
market_segment_or_old_corporate_action_caveat_count: 2
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 98
next_round: R4
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_98_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 98
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
loop97: C14_EV_DEMAND_SLOWDOWN_4B_4C
```

This run returns to C13 after the R3 branch cycle, but avoids the C13 top-covered symbols and recent R3 loop93~97 names.

Selected fine branch:

```text
separator / silicon-anode / electrolyte or battery-materials cross-readthrough
JV utilization, AMPC/IRA, customer qualification, line loading, inventory, ASP,
cost pass-through, working capital, and margin bridge
vs generic battery-material label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rows: 23
symbols: 16
date_range: 2023-01-31~2024-07-16
good/bad S2: 9/2
4B/4C: 2/0
URL pending/proxy: 10/10
top covered symbols:
  005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1)
```

Selected symbols:

```text
078600 대주전자재료
361610 SK아이이테크놀로지
357780 솔브레인
```

They avoid C13 top-covered names and recent R3 branch names:

```text
C13 top-covered avoid:
  005070, 020150, 003670, 025900, 348370, 002710

recent R3 avoid:
  loop97 C14: 079810, 217820, 382480
  loop96 C12: 011790, 005070, 051910
  loop95 C11: 008730, 006110, 277880
  loop94 C13: 121600, 393890, 450080
  loop93 C14: 014820, 336370, 222080
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
078600: same archetype, new symbol, silicon-anode/battery-material positive with large MFE and Green cap
361610: same archetype, new symbol, separator/JV utilization hard-4C after shallow MFE and severe MAE
357780: same archetype, new symbol, electrolyte/material cross-readthrough local 4B failure after meaningful MFE and material MAE
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
  market: KOSDAQ
  tradable_ohlcv rows: 5,230
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

361610 SK아이이테크놀로지
  profile: atlas/symbol_profiles/361/361610.json
  first_date: 2021-05-11
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,171
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus older battery peers, but no 2024 corporate-action contamination.

357780 솔브레인
  profile: atlas/symbol_profiles/357/357780.json
  first_date: 2020-08-06
  last_date: 2026-02-20
  market:
    KOSDAQ in 2024
    KOSDAQ GLOBAL from 2025-06-13
  tradable_ohlcv rows: 1,357
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    market segment changes after the selected 2024 window; not contamination for this case.
```

---

## 4. Archetype residual problem

C13 is about battery JV utilization, AMPC / IRA economics, factory loading, customer qualification, and margin. It is not a generic "battery materials are hot" archetype.

The model can over-score:

```text
separator / electrolyte / silicon-anode material label
battery materials sympathy
US IRA / AMPC headline
customer JV or North America capacity headline
cell-maker utilization hope
EV demand recovery label
one-week battery-material stock spike
late chase after battery-material rerating
```

The C13 bridge must be stricter:

```text
battery material / JV / AMPC event
  -> named customer, JV, plant, region, or qualified product
  -> cell-maker utilization and customer call-off
  -> production line loading and yield
  -> AMPC / IRA eligibility and recognition timing
  -> ASP / mix / cost pass-through
  -> inventory and working-capital timing
  -> capex and depreciation burden
  -> FX / logistics / raw-material cost
  -> margin / OP conversion
  -> price survival after the first battery-material spike
```

A C13 battery-material thesis is like a separator film or silicon-anode powder sitting next to a cell line. The material may be strategic, but equity value appears only when the customer line actually runs, the product is qualified, orders are called off, AMPC/IRA economics are recognized, and cost plus depreciation still leaves margin.

---

## 5. Case 1 — 078600 대주전자재료

```yaml
case_id: C13_R3L98_078600_2024_02_01
symbol: "078600"
name: "대주전자재료"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 71200
classification: positive_silicon_anode_battery_material_customer_qualification_utilization_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

대주전자재료 is the constructive C13 material positive.

The useful C13 read is not simply:

```text
2차전지 소재주가 강하다
```

It is:

```text
silicon-anode / advanced battery material relevance
  -> customer qualification and adoption optionality
  -> cell-line utilization and material call-off bridge
  -> very strong price confirmation from March to August
  -> Green cap after large rerating because order/margin evidence must refresh
```

The forward path produced a very large MFE with controlled early drawdown. That preserves positive classification. However, after the large rerating, C13 Green requires fresh evidence that qualification, utilization, customer call-off, and margin conversion remain current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 72,000 / low 68,300 / close 71,200
2024-02-22: high 84,000 / close 77,400
2024-03-12: high 95,100 / close 94,900
2024-03-25: high 102,000 / close 102,000
2024-07-30: high 119,200 / close 114,200
2024-08-14: high 128,700 / close 126,200
2024-08-16: high 129,400 / close 122,200
2024-09-06: low 92,500 / close 92,900
```

Approximate path from entry close:

```text
entry_close: 71,200
peak_high: 129,400
MFE: +81.7%
worst_low_after_entry: 67,800
MAE: -4.8%
```

### Interpretation

This is a C13 positive with Green cap:

```text
Stage2-Actionable: possible if customer qualification, line utilization, call-off visibility, and margin bridge are explicit.
Stage3-Green: blocked after +80% MFE unless fresh customer/order/margin evidence appears.
Local 4B: monitor if the material story outruns utilization or margin evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  silicon_anode_material_relevance: high
  customer_qualification_bridge: medium_high
  utilization_calloff_bridge: medium_high
  ampc_ira_bridge: weak_to_medium
  asp_mix_margin_bridge: medium
  price_confirmation: very_high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 361610 SK아이이테크놀로지

```yaml
case_id: C13_R3L98_361610_2024_02_01
symbol: "361610"
name: "SK아이이테크놀로지"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 74800
classification: hard_4c_candidate_separator_jv_utilization_label_without_customer_calloff_margin_survival
calibration_usable: true
```

### Evidence interpretation

SK아이이테크놀로지 is the separator / JV utilization hard guardrail.

The label can fool the model:

```text
battery separator
North America / JV / IRA readthrough
cell-maker utilization recovery hope
strategic battery-material status
```

But from the selected February entry, the forward path produced only shallow MFE and then severe drawdown. The bridge from separator/JV relevance to customer call-off, line loading, utilization, AMPC/IRA recognition, and margin survival failed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 74,800 / close 74,800
2024-02-02: high 80,800 / close 76,000
2024-04-17: low 59,800 / close 59,800
2024-08-05: low 30,950 / close 32,000
2024-09-10: low 30,050 / close 30,050
2024-10-07: high 38,750 / close 38,100
2024-10-25: low 30,800 / close 30,800
```

Approximate path from entry close:

```text
entry_close: 74,800
peak_high_after_entry: 80,800
MFE: +8.0%
worst_low_after_entry: 30,050
MAE: -59.8%
```

### Interpretation

This is a hard C13 false-positive:

```text
Stage2-Watch: possible from separator and battery-material relevance.
Stage2-Actionable: blocked unless customer call-off, utilization, AMPC/IRA recognition, cost control, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
Shorter-listing caveat: yes, but no 2024 contamination.
```

The lesson is that separator strategic relevance is not utilization or margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  separator_material_relevance: high
  jv_ira_readthrough: medium_high
  customer_calloff_bridge: weak
  line_utilization_bridge: weak
  ampc_ira_recognition_bridge: weak
  margin_op_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 357780 솔브레인

```yaml
case_id: C13_R3L98_357780_2024_02_01
symbol: "357780"
name: "솔브레인"
canonical_archetype_id: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id: SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 270000
classification: local_burst_electrolyte_material_cross_readthrough_high_mae_4b_failure_without_refreshed_battery_utilization_margin_bridge
calibration_usable: true
```

### Evidence interpretation

솔브레인 is the materials cross-readthrough / 4B failure.

The setup had plausible C13 relevance:

```text
battery electrolyte/materials and process-chemical optionality
  -> customer utilization and materials demand readthrough
  -> early memory/battery materials rerating
  -> meaningful MFE into March/April
```

However, the later path failed price survival materially. The battery-materials or electrolyte cross-readthrough did not maintain enough customer utilization, order, margin, or working-capital proof to preserve Green. This is not a pure hard 4C because a meaningful MFE came first, but it is a local 4B failure.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 274,000 / close 270,000
2024-03-21: high 322,000 / close 313,500
2024-04-08: high 321,000 / close 308,500
2024-08-05: low 221,000 / close 222,500
2024-09-06: low 211,500 / close 215,500
2024-10-25: low 192,900 / close 195,000
2024-10-31: low 191,400 / close 204,000
```

Approximate path from entry close:

```text
entry_close: 270,000
peak_high: 322,000
MFE: +19.3%
worst_low_after_entry: 191,400
MAE: -29.1%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from battery-material/electrolyte and process-chemical cross-readthrough.
Stage2-Actionable: possible only if customer utilization, order, ASP/mix, and margin bridge are explicit.
Stage3-Green: blocked after later material MAE.
Local 4B: required.
Hard 4C: not primary because MFE was meaningful and MAE did not cross the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  electrolyte_material_cross_readthrough: medium_high
  customer_utilization_bridge: weak_to_medium
  order_visibility_bridge: weak_to_medium
  asp_mix_margin_bridge: weak_to_medium
  working_capital_bridge: weak
  price_confirmation: medium_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
separator_jv_utilization_case_count: 1
silicon_anode_material_case_count: 1
electrolyte_material_cross_readthrough_case_count: 1
battery_jv_utilization_bridge_missing_count: 2
customer_order_margin_bridge_missing_count: 2
ampc_ira_bridge_missing_count: 2
market_segment_or_old_corporate_action_caveat_count: 2
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C13 battery JV/utilization grid:

```text
078600 대주전자재료:
  silicon-anode / advanced battery material positive;
  very large MFE and low MAE, but Green requires fresh qualification, utilization, call-off, and margin evidence.

361610 SK아이이테크놀로지:
  separator / JV utilization label failed;
  shallow MFE and extreme MAE, hard 4C.

357780 솔브레인:
  electrolyte/material cross-readthrough local burst;
  meaningful MFE first, then material MAE, local 4B failure.
```

Shared rule:

```text
C13 is not "battery material label is strategic."
C13 is "customer qualification, cell-line utilization, customer call-off, AMPC/IRA recognition, cost pass-through, working capital, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C13_R3L98_078600_2024_02_01","scheduled_round":"R3","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE","symbol":"078600","name":"대주전자재료","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":71200,"peak_high":129400,"peak_date":"2024-08-16","worst_low_after_entry":67800,"worst_low_after_entry_date":"2024-02-14","mfe_pct":81.7,"mae_pct":-4.8,"classification":"positive_silicon_anode_battery_material_customer_qualification_utilization_margin_bridge_with_green_cap","calibration_usable":true,"evidence_family":"silicon_anode_advanced_battery_material_customer_qualification_utilization_calloff_margin_bridge","residual_error":"positive_battery_material_path_requires_green_cap_after_large_mfe_without_refreshed_qualification_utilization_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_customer_qualification_utilization_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C13_R3L98_361610_2024_02_01","scheduled_round":"R3","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE","symbol":"361610","name":"SK아이이테크놀로지","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":74800,"peak_high":80800,"peak_date":"2024-02-02","worst_low_after_entry":30050,"worst_low_after_entry_date":"2024-09-10","mfe_pct":8.0,"mae_pct":-59.8,"classification":"hard_4c_candidate_separator_jv_utilization_label_without_customer_calloff_margin_survival","calibration_usable":true,"short_listing_or_row_presence_caveat":true,"evidence_family":"separator_jv_ira_readthrough_without_customer_calloff_line_utilization_ampc_recognition_margin_bridge","residual_error":"separator_strategic_label_can_fail_when_utilization_and_margin_bridge_missing","shadow_rule_candidate":"route_separator_jv_utilization_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_customer_calloff_bridge_missing"}
{"row_type":"case","case_id":"C13_R3L98_357780_2024_02_01","scheduled_round":"R3","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE","symbol":"357780","name":"솔브레인","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":270000,"peak_high":322000,"peak_date":"2024-03-21","worst_low_after_entry":191400,"worst_low_after_entry_date":"2024-10-31","mfe_pct":19.3,"mae_pct":-29.1,"classification":"local_burst_electrolyte_material_cross_readthrough_high_mae_4b_failure_without_refreshed_battery_utilization_margin_bridge","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"battery_electrolyte_material_process_chemical_cross_readthrough_without_sustained_customer_utilization_order_margin_survival","residual_error":"battery_material_cross_readthrough_can_create_mfe_but_fail_green_without_utilization_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_battery_material_cross_readthrough_cases_as_local_4b_not_green"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","fine_archetype_id":"SEPARATOR_SILICON_ANODE_ELECTROLYTE_MATERIALS_JV_UTILIZATION_AMPC_IRA_CUSTOMER_ORDER_MARGIN_BRIDGE_VS_BATTERY_MATERIAL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"separator_jv_utilization_case_count":1,"silicon_anode_material_case_count":1,"electrolyte_material_cross_readthrough_case_count":1,"battery_jv_utilization_bridge_missing_count":2,"customer_order_margin_bridge_missing_count":2,"ampc_ira_bridge_missing_count":2,"market_segment_or_old_corporate_action_caveat_count":2,"short_listing_or_row_presence_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":98,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","rule_id":"C13_BATTERY_JV_UTILIZATION_AMPC_CUSTOMER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C13 battery JV/utilization/AMPC/IRA cases, do not open Stage2-Actionable or Stage3-Green from separator, electrolyte, silicon-anode, battery materials, IRA/AMPC, customer JV, North America capacity, cell-maker utilization hope, EV demand recovery, one-week battery-material volume spike, or late chase after battery-material rerating labels alone. Require named customer/JV/plant/region/qualified product, cell-maker utilization and customer call-off, production line loading and yield, AMPC/IRA eligibility and recognition timing, ASP/mix/cost pass-through, inventory and working-capital timing, capex/depreciation burden, FX/logistics/raw-material cost, margin/OP conversion, and post-trigger price survival. Silicon-anode positives with very large MFE may be capped Actionable when qualification, call-off, and margin bridge are explicit, but Green requires fresh evidence. Separator/JV labels with shallow MFE and extreme MAE should route to hard-4C when customer call-off and margin bridge are missing. Battery-material cross-readthrough cases with meaningful MFE followed by material MAE should remain local 4B, not Green.","expected_effect":"Preserve true battery-material/JV utilization positives while reducing separator, electrolyte/material, IRA/AMPC, and battery-label false positives where customer call-off, utilization, AMPC recognition, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":98,"canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","residual_type":"battery_jv_utilization_ampc_customer_margin_guard","contribution":"Adds one silicon-anode positive, one separator/JV hard-4C, and one electrolyte/material local 4B failure to calibrate C13 customer qualification, line utilization, call-off, AMPC/IRA recognition, working capital, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C13_BATTERY_JV_UTILIZATION_AMPC_CUSTOMER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C13_BATTERY_JV_UTILIZATION_AMPC_IRA:

  Do not open Stage3-Green from:
    - separator / electrolyte / silicon-anode material label alone
    - generic battery materials sympathy alone
    - US IRA / AMPC headline alone
    - customer JV or North America capacity headline alone
    - cell-maker utilization hope alone
    - EV demand recovery label alone
    - one-week battery-material stock volume spike alone
    - late chase after battery-material rerating alone

  Require at least two of:
    - named customer / JV / plant / region / qualified product
    - cell-maker utilization and customer call-off
    - production line loading and yield
    - AMPC / IRA eligibility and recognition timing
    - ASP / mix / cost pass-through
    - inventory / working-capital timing
    - capex / depreciation burden control
    - FX / logistics / raw-material cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the battery-material headline

  If MFE < 10% and MAE < -35%:
    route to C13 hard-4C candidate.

  If MFE > 30% but qualification/call-off/margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but utilization and AMPC bridge are missing:
    attach 4B until customer call-off and margin evidence refreshes.

  Distinguish:
    - materials where customer qualification becomes line loading, call-off, AMPC/IRA recognition, and margin
    - from strategic battery labels where utilization, inventory, depreciation, or cost breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C13 battery JV/utilization/AMPC cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C13_BATTERY_JV_UTILIZATION_AMPC_CUSTOMER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C13 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C13 cases agree, consider implementing a canonical guard that:
   - blocks battery-material Green without named customer/JV/plant, line utilization, customer call-off, AMPC/IRA recognition, and margin bridge,
   - preserves silicon-anode positives only with price survival and fresh qualification/call-off evidence,
   - routes shallow-MFE/extreme-MAE separator/JV labels to hard-4C,
   - treats meaningful-MFE/material-MAE battery-material cross-readthrough as local 4B,
   - applies short-listing, market-segment, and old corporate-action caveats when needed.

Expected next schedule:
completed_round = R3
completed_loop = 98
next_round = R4
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 98
next_round = R4
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
