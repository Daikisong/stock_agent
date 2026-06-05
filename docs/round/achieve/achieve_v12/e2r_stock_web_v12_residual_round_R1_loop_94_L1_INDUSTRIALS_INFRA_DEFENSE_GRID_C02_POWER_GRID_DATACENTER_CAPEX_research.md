# E2R Stock-Web v12 Residual Research — R1 / Loop 94

```yaml
scheduled_round: R1
scheduled_loop: 94
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE

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
corporate_action_caveat_avoided_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 94
next_round: R2
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12, when R1~R13 completes:

```text
scheduled_round = R1
scheduled_loop = max_completed_loop + 1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 94
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop89: C02_POWER_GRID_DATACENTER_CAPEX
loop90: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
loop91: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop92: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop93: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
```

This run returns to C02 but avoids its top-covered symbols and uses a different fine branch:

```text
power cable / switchgear / control-equipment grid CAPEX
order-delivery-margin bridge
vs generic power-grid theme spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C02_POWER_GRID_DATACENTER_CAPEX
rows: 22
symbols: 12
date_range: 2024-01-03~2024-07-09
good/bad S2: 11/4
4B/4C: 2/0
URL pending/proxy: 6/6
top covered symbols:
  000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2)
```

Selected symbols:

```text
103590 일진전기
199820 제일일렉트릭
237750 피앤씨테크
```

They avoid the C02 top-covered list and avoid the most recent R1 loop93 C05 names:

```text
016250, 028050, 028100
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
103590: same archetype, new symbol, power cable / transformer-grid CAPEX order-delivery positive branch
199820: same archetype, new symbol, switchgear / low-voltage equipment post-corporate-action local 4B branch
237750: same archetype, new symbol, power automation / control-equipment theme spike hard-4C branch
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
103590 일진전기
  profile: atlas/symbol_profiles/103/103590.json
  first_date: 2008-08-01
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,329
  corporate_action_candidate_dates:
    2024-02-13
  selected entry:
    2024-02-26, after the 2024-02-13 candidate window
  entry~D+180 contamination: avoided

199820 제일일렉트릭
  profile: atlas/symbol_profiles/199/199820.json
  name history:
    제일전기공업 until 2024-05-07
    제일일렉트릭 from 2024-05-08
  first_date: 2020-11-26
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,282
  corporate_action_candidate_dates:
    2024-05-21, 2024-06-11
  selected entry:
    2024-08-23, after both 2024 corporate-action candidate windows
  entry~D+180 contamination: avoided

237750 피앤씨테크
  profile: atlas/symbol_profiles/237/237750.json
  first_date: 2016-07-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,363
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C02 is not a generic "power-grid stock went up" archetype.

The model can over-score:

```text
power-grid CAPEX headline
AI datacenter electricity demand
transformer / cable / switchgear label
control-equipment / automation label
one-week power-theme volume spike
Korea/US grid investment readthrough
```

The C02 bridge must be stricter:

```text
power-grid or datacenter CAPEX
  -> company-specific product exposure
  -> backlog / purchase order
  -> delivery timing and capacity
  -> copper / steel / component cost pass-through
  -> utilization and working-capital risk
  -> margin / OP conversion
  -> price survival after the first grid-theme spike
```

A grid-CAPEX headline is like a city announcing it needs more roads. C02 asks whether this company owns the asphalt plant, has the signed road order, can deliver on time, and keeps margin after input costs.

---

## 5. Case 1 — 103590 일진전기

```yaml
case_id: C02_R1L94_103590_2024_02_26
symbol: "103590"
name: "일진전기"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 10820
classification: positive_power_cable_transformer_grid_capex_order_delivery_bridge_with_4b_after_multibagger
calibration_usable: true
```

### Evidence interpretation

일진전기 is the clean constructive control in this R1 set.

The useful C02 read is not simply:

```text
전력망 테마가 강하다
```

It is:

```text
power cable / electric equipment exposure
  -> grid CAPEX and transformer/cable demand
  -> order-delivery visibility
  -> price confirmation
  -> long price survival after the February corporate-action window
```

The forward path validated the early entry very strongly. However, the MFE became so large that the model should still attach 4B after the move unless fresh backlog/margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-13: corporate-action candidate date in profile
2024-02-26: close 10,820
2024-03-04: high 12,450 / close 11,960
2024-03-18: high 18,500 / close 17,200
2024-03-28: high 22,400 / close 20,450
2024-04-26: high 23,900 / close 23,300
2024-05-13: high 28,400 / close 25,450
2024-05-29: high 30,250 / close 28,600
2024-08-05: low 18,000 / close 19,050
2024-10-17: high 26,350 / close 26,100
2024-11-05: high 28,600 / close 27,500
```

Approximate path from entry close:

```text
entry_close: 10,820
peak_high: 30,250
MFE: +179.6%
worst_low_after_entry: 10,340 on 2024-02-28
MAE: -4.4%
```

### Interpretation

This is a C02 positive with post-rerating 4B discipline:

```text
Stage2-Actionable: valid if order/delivery and margin bridge are explicit.
Stage3-Green: possible only with backlog, delivery capacity, and OP/margin conversion evidence.
Local 4B: mandatory after multi-bagger MFE unless fresh backlog/margin evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  grid_capex_relevance: very_high
  power_cable_transformer_bridge: high
  order_delivery_visibility: medium_high
  cost_pass_through_bridge: medium
  price_confirmation: very_high
  price_survival: high
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 199820 제일일렉트릭

```yaml
case_id: C02_R1L94_199820_2024_08_23
symbol: "199820"
name: "제일일렉트릭"
name_at_earlier_2024: "제일전기공업"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE
trigger_date: 2024-08-23
entry_date: 2024-08-23
entry_price_basis: close
entry_price: 7990
classification: local_positive_switchgear_low_voltage_equipment_theme_with_4b_watch_after_corporate_action_window
calibration_usable: true
```

### Evidence interpretation

제일일렉트릭 is a local-positive / 4B-watch case.

The company has plausible C02 relevance:

```text
switchgear / low-voltage equipment / electric distribution equipment
  -> datacenter and building electrification sympathy
  -> power-infrastructure theme relaunch
```

But this case has two important caveats:

```text
2024 corporate-action candidate windows existed on 2024-05-21 and 2024-06-11.
The selected entry is after those windows, on 2024-08-23.
```

The price path after entry first drew down, then later rallied strongly. That makes the case usable, but not a clean Green.

### Price path

Key Stock-Web rows:

```text
2024-05-21: corporate-action candidate window in profile
2024-06-11: corporate-action candidate window in profile
2024-08-23: close 7,990
2024-08-26: high 9,280 / close 8,470
2024-09-09: low 6,340 / close 6,640
2024-09-20: high 10,400 / close 9,870
2024-09-27: high 11,000 / close 9,700
2024-10-07: high 10,630 / close 10,290
2024-10-25: low 8,810 / close 8,810
```

Approximate path from entry close:

```text
entry_close: 7,990
peak_high: 11,000
MFE: +37.7%
worst_low_after_entry: 6,340
MAE: -20.7%
```

### Interpretation

This is a local positive with 4B, not an unrestricted Green:

```text
Stage2-Watch: valid from switchgear/electric distribution relevance.
Stage2-Actionable: allowed only if order, delivery, and margin bridge are explicit.
Stage3-Green: blocked without fresh order/margin evidence after the rally.
Local 4B: required because MFE was meaningful but MAE also material.
Hard 4C: no for the selected post-corporate-action entry.
```

### Stress-test components

```text
raw_component_score_proxy:
  switchgear_equipment_relevance: medium_high
  grid_capex_label: high
  order_delivery_bridge: weak_to_medium
  corporate_action_caveat_avoided: yes
  price_confirmation: high_after_delay
  drawdown_penalty: medium_high
  local_4b_overlay: required
```

---

## 7. Case 3 — 237750 피앤씨테크

```yaml
case_id: C02_R1L94_237750_2024_05_02
symbol: "237750"
name: "피앤씨테크"
canonical_archetype_id: C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id: POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE
trigger_date: 2024-05-02
entry_date: 2024-05-02
entry_price_basis: close
entry_price: 7310
classification: hard_4c_candidate_power_automation_control_equipment_theme_spike_without_order_margin_bridge
calibration_usable: true
```

### Evidence interpretation

피앤씨테크 is the hard guardrail case.

The stock had the kind of one-week move that can fool a C02 model:

```text
power automation / protection and control equipment label
  -> grid modernization sympathy
  -> May power-equipment theme spike
  -> no durable order/delivery/margin bridge
```

The forward path had almost no incremental upside from the selected close and then a long drawdown. This is exactly why C02 should block Green from the label alone.

### Price path

Key Stock-Web rows:

```text
2024-04-29: high 7,340 / close 6,550
2024-05-02: high 7,470 / close 7,310
2024-05-08: high 7,640 / close 6,990
2024-05-13: low 5,860 / close 6,210
2024-08-05: low 4,440 / close 4,440
2024-09-06: low 4,450 / close 4,495
2024-10-28: low 4,375 / close 4,405
```

Approximate path from entry close:

```text
entry_close: 7,310
peak_high: 7,640
MFE: +4.5%
worst_low_after_entry: 4,375
MAE: -40.2%
```

### Interpretation

This is a hard C02 false-positive:

```text
Stage2-Watch: possible from power-automation relevance.
Stage2-Actionable: blocked unless order, delivery, backlog, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that control-equipment adjacency does not automatically become grid-CAPEX monetization.

### Stress-test components

```text
raw_component_score_proxy:
  power_automation_label: high
  grid_modernization_sympathy: medium_high
  order_delivery_bridge: weak
  margin_bridge: weak
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
corporate_action_caveat_avoided_count: 2
calibration_usable_trigger_count: 3
```

The three-case C02 grid:

```text
103590 일진전기:
  power cable / transformer-grid CAPEX positive;
  very strong MFE and controlled MAE, but post-rerating 4B needed.

199820 제일일렉트릭:
  switchgear / low-voltage equipment local positive after corporate-action windows;
  useful MFE but material MAE, local 4B.

237750 피앤씨테크:
  power automation/control-equipment theme spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C02 is not "power-grid label."
C02 is "grid/datacenter CAPEX becomes company-specific orders, delivery, capacity utilization, cost pass-through, and margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C02_R1L94_103590_2024_02_26","scheduled_round":"R1","scheduled_loop":94,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE","symbol":"103590","name":"일진전기","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":10820,"peak_high":30250,"peak_date":"2024-05-29","worst_low_after_entry":10340,"worst_low_after_entry_date":"2024-02-28","mfe_pct":179.6,"mae_pct":-4.4,"classification":"positive_power_cable_transformer_grid_capex_order_delivery_bridge_with_4b_after_multibagger","calibration_usable":true,"evidence_family":"power_cable_transformer_grid_capex_order_delivery_margin_bridge","residual_error":"positive_grid_capex_entry_still_requires_4b_after_multibagger_mfe_without_fresh_backlog_margin_evidence","shadow_rule_candidate":"preserve_positive_when_order_delivery_and_price_survival_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C02_R1L94_199820_2024_08_23","scheduled_round":"R1","scheduled_loop":94,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE","symbol":"199820","name":"제일일렉트릭","trigger_date":"2024-08-23","entry_date":"2024-08-23","entry_price":7990,"peak_high":11000,"peak_date":"2024-09-27","worst_low_after_entry":6340,"worst_low_after_entry_date":"2024-09-09","mfe_pct":37.7,"mae_pct":-20.7,"classification":"local_positive_switchgear_low_voltage_equipment_theme_with_4b_watch_after_corporate_action_window","calibration_usable":true,"evidence_family":"switchgear_low_voltage_power_equipment_grid_capex_theme_after_corporate_action_window","residual_error":"post_corporate_action_power_equipment_local_positive_requires_order_margin_bridge_before_green","shadow_rule_candidate":"classify_meaningful_mfe_with_material_mae_power_equipment_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C02_R1L94_237750_2024_05_02","scheduled_round":"R1","scheduled_loop":94,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE","symbol":"237750","name":"피앤씨테크","trigger_date":"2024-05-02","entry_date":"2024-05-02","entry_price":7310,"peak_high":7640,"peak_date":"2024-05-08","worst_low_after_entry":4375,"worst_low_after_entry_date":"2024-10-28","mfe_pct":4.5,"mae_pct":-40.2,"classification":"hard_4c_candidate_power_automation_control_equipment_theme_spike_without_order_margin_bridge","calibration_usable":true,"evidence_family":"power_automation_control_equipment_theme_spike_without_order_delivery_margin_bridge","residual_error":"grid_control_equipment_label_can_overpromote_without_signed_order_and_margin_conversion","shadow_rule_candidate":"route_power_automation_theme_spikes_to_hard_4c_if_mfe_shallow_mae_large_and_order_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":94,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","fine_archetype_id":"POWER_CABLE_SWITCHGEAR_CONTROL_EQUIPMENT_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_VS_POWER_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":94,"canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","rule_id":"C02_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C02, do not open Stage2-Actionable or Stage3-Green from power-grid CAPEX, AI datacenter electricity demand, transformer/cable/switchgear/control-equipment labels, or one-week power-theme volume spike alone. Require company-specific product exposure, backlog or purchase order, delivery timing and capacity, copper/steel/component cost pass-through, utilization and working-capital risk check, margin/OP conversion, and post-trigger price survival. Direct power cable/transformer positives with controlled MAE may be Actionable when order and delivery bridge are explicit, but large MFE should attach local 4B unless fresh backlog/margin evidence appears. Switchgear or control-equipment names with meaningful MFE but material MAE should remain local 4B. Control-equipment theme spikes with shallow MFE and high MAE should route to hard-4C when order and margin bridge are missing.","expected_effect":"Preserve true power-grid CAPEX positives with orders, delivery, and margin evidence while reducing generic power-theme false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":94,"canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","residual_type":"grid_capex_order_delivery_margin_guard","contribution":"Adds one direct power cable/transformer positive with 4B-after-large-MFE, one switchgear local 4B, and one power-automation hard-4C counterexample to calibrate C02 order-delivery-margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C02_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C02_POWER_GRID_DATACENTER_CAPEX:

  Do not open Stage3-Green from:
    - power-grid CAPEX headline alone
    - AI datacenter electricity-demand label alone
    - transformer / cable / switchgear label alone
    - control-equipment / power-automation label alone
    - one-week power-theme volume spike alone

  Require at least two of:
    - company-specific product exposure
    - purchase order / backlog
    - delivery timing / capacity
    - copper / steel / component cost pass-through
    - utilization / working-capital containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the grid-CAPEX headline

  If MFE < 10% and MAE < -30%:
    route to C02 hard-4C candidate.

  If MFE > 30% but MAE is material:
    preserve as local 4B unless fresh order/margin evidence appears.

  If MFE is extraordinary and MAE remains controlled:
    preserve positive classification but attach local 4B after the move unless backlog/margin evidence refreshes the thesis.

  Distinguish:
    - direct cable/transformer names with order-delivery bridge
    - from switchgear/control-equipment theme labels where grid CAPEX adjacency does not reach signed orders and margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_94_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C02 power-grid/datacenter CAPEX cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C02_GRID_CAPEX_ORDER_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C02 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C02 cases agree, consider implementing a canonical guard that:
   - blocks grid/power-theme Green without order/delivery/cost-pass-through/margin bridge,
   - preserves direct cable/transformer positives only with price survival and backlog evidence,
   - attaches local 4B after very large MFE or meaningful MFE followed by material MAE,
   - routes shallow-MFE/high-MAE power-automation/control-equipment spikes to hard-4C.

Expected next schedule:
completed_round = R1
completed_loop = 94
next_round = R2
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 94
next_round = R2
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
