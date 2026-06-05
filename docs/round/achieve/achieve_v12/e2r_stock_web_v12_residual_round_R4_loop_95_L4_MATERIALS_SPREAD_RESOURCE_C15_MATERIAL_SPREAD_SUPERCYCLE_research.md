# E2R Stock-Web v12 Residual Research — R4 / Loop 95

```yaml
scheduled_round: R4
scheduled_loop: 95
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE

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
row_presence_or_zero_volume_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 95
next_round: R5
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 95
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage:

```text
loop92: C15_MATERIAL_SPREAD_SUPERCYCLE
loop93: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop94: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

This run returns to C15 but avoids the top-covered C15 names and uses a different fine branch:

```text
specialty steel / steel pipe / wire-rope and industrial steel products
product-mix, spread, cost pass-through, and margin bridge
vs generic material-label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C15_MATERIAL_SPREAD_SUPERCYCLE
rows: 28
symbols: 11
date_range: 2024-01-10~2024-05-21
good/bad S2: 13/0
4B/4C: 3/0
URL pending/proxy: 9/9
top covered symbols:
  103140(6), 012800(5), 025820(5), 004560(3), 021050(3), 001780(1)
```

Selected symbols:

```text
001430 세아베스틸지주
005010 휴스틸
002240 고려제강
```

They avoid the C15 top-covered list and avoid the most recent R4 loop94 C17 names:

```text
loop94 avoid: 002380, 011170, 161000
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
001430: same archetype, new symbol, specialty steel / alloy product-mix positive with 4B watch
005010: same archetype, new symbol, steel-pipe material spread local burst followed by high-MAE 4B failure
002240: same archetype, new symbol, wire-rope / specialty steel late-spike hard-4C without product-spread margin survival
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
001430 세아베스틸지주
  profile: atlas/symbol_profiles/001/001430.json
  name history:
    기아특수강 -> 세아베스틸 -> 세아베스틸지주
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,728
  corporate_action_candidate_dates:
    historical only, none inside the 2024 validation window from the inspected profile context
  2024 entry~D+180 contamination: none

005010 휴스틸
  profile: atlas/symbol_profiles/005/005010.json
  name history:
    한국강관 -> 신호스틸 -> 휴스틸
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,700
  non_tradable_zero_volume rows: 65
  corporate_action_candidate_dates:
    1996-04-30, 2001-07-31, 2002-04-09, 2022-07-13, 2022-12-27
  2024 entry~D+180 contamination: none
  caveat:
    row-presence caveat from historical non-tradable zero-volume rows, but not inside selected 2024 window.

002240 고려제강
  profile: atlas/symbol_profiles/002/002240.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,544
  non_tradable_zero_volume rows: 221
  corporate_action_candidate_dates:
    1999-01-28, 2001-04-30, 2004-05-19, 2009-01-30, 2015-01-30
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C15 is about material spread supercycle and product-mix margin power. It is not a generic "steel/material stock went up" archetype.

The model can over-score:

```text
steel / specialty steel label
steel pipe / energy infra label
wire rope / industrial material label
China or infrastructure demand readthrough
one-week materials-stock volume spike
low-PBR cyclicals moving together
```

The C15 bridge must be stricter:

```text
material demand / spread event
  -> company-specific product mix
  -> raw-material input cost and selling-price spread
  -> cost pass-through or contract lag
  -> utilization and fixed-cost absorption
  -> export / FX / inventory risk
  -> margin / OP conversion
  -> price survival after the first materials spike
```

A material-spread story is like a blast furnace. The market sees the flame first, but C15 asks whether ore, alloy, energy cost, selling price, inventory, and utilization line up so the heat becomes operating profit instead of smoke.

---

## 5. Case 1 — 001430 세아베스틸지주

```yaml
case_id: C15_R4L95_001430_2024_02_01
symbol: "001430"
name: "세아베스틸지주"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 22900
classification: positive_capped_specialty_steel_product_mix_spread_margin_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

세아베스틸지주 is the constructive C15 control in this set.

The useful C15 read is not simply:

```text
철강주가 올랐다
```

It is:

```text
specialty steel / alloy product mix
  -> material spread and industrial demand readthrough
  -> cost pass-through and margin optionality
  -> early price confirmation
```

The forward path produced a meaningful February MFE. However, the later drawdown into August was material, so this is a capped positive with 4B discipline rather than an unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 23,200 / close 22,900
2024-02-07: high 24,250 / close 24,050
2024-02-23: high 26,450 / close 26,300
2024-02-26: high 27,350 / close 26,200
2024-03-07: low 22,550 / close 22,950
2024-08-05: low 16,640 / close 17,380
2024-10-16: high 20,900 / close 20,900
```

Approximate path from entry close:

```text
entry_close: 22,900
peak_high: 27,350
MFE: +19.4%
worst_low_after_entry: 16,640
MAE: -27.3%
```

### Interpretation

This is a C15 capped positive with 4B watch:

```text
Stage2-Actionable: possible if product-mix, spread, utilization, and margin bridge are explicit.
Stage3-Green: blocked without fresh spread/margin evidence after the rerating.
Local 4B: required because useful MFE later became material MAE.
Hard 4C: no, because MAE did not cross the hard threshold and a meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  specialty_steel_relevance: high
  product_mix_bridge: medium_high
  spread_cost_pass_through_bridge: medium
  utilization_margin_bridge: medium
  price_confirmation: medium_high_initial
  post_rerating_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 005010 휴스틸

```yaml
case_id: C15_R4L95_005010_2024_02_01
symbol: "005010"
name: "휴스틸"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5340
classification: local_burst_steel_pipe_energy_infra_material_spread_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

휴스틸 is the steel-pipe local-burst / high-MAE 4B case.

The setup looked plausible:

```text
steel pipe / energy infrastructure material
  -> steel spread or energy-infra demand readthrough
  -> low-PBR cyclical materials rally
```

The price path gave an immediate tradable MFE. But the later drawdown crossed the high-MAE zone. This should not remain Green. It should be treated as a local event burst requiring 4B unless product-spread and margin evidence is refreshed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,420 / close 5,340
2024-02-02: high 6,170 / close 5,500
2024-02-13: high 5,990 / close 5,870
2024-03-04: high 5,040 / close 5,000
2024-04-08: low 4,500 / close 4,515
2024-08-05: low 3,620 / close 3,815
2024-08-27: high 5,000 / close 4,410
2024-10-25: low 3,935 / close 3,935
```

Approximate path from entry close:

```text
entry_close: 5,340
peak_high: 6,170
MFE: +15.5%
worst_low_after_entry: 3,620
MAE: -32.2%
```

### Interpretation

This is a local-burst / 4B failure:

```text
Stage2-Watch: valid from steel-pipe and energy-infra material relevance.
Stage2-Actionable: possible only if steel spread, contract pricing, and margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  steel_pipe_material_relevance: high
  energy_infra_readthrough: medium
  product_spread_bridge: weak_to_medium
  cost_pass_through_bridge: weak
  local_price_confirmation: medium
  post_burst_survival: failed
  row_presence_caveat: historical_zero_volume_count_outside_2024
  local_4b_overlay: required
```

---

## 7. Case 3 — 002240 고려제강

```yaml
case_id: C15_R4L95_002240_2024_02_20
symbol: "002240"
name: "고려제강"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-20
entry_date: 2024-02-20
entry_price_basis: close
entry_price: 31250
classification: hard_4c_candidate_wire_rope_specialty_steel_late_spike_without_spread_margin_survival
calibration_usable: true
```

### Evidence interpretation

고려제강 is the hard C15 guardrail.

The setup had the classic material-label late-chase shape:

```text
wire rope / specialty steel
  -> industrial material spread sympathy
  -> sudden materials-sector volume spike
  -> model may confuse spike with durable product-spread margin power
```

From the selected close after the spike, the stock delivered only shallow incremental MFE and then fell into a large drawdown. This should route to hard 4C unless direct product-spread, order, utilization, and margin evidence exists.

### Price path

Key Stock-Web rows:

```text
2024-02-07: high 26,500 / close 26,500
2024-02-08: high 33,400 / close 29,750
2024-02-14: high 35,650 / close 30,950
2024-02-20: high 33,000 / close 31,250
2024-02-23: low 24,150 / close 24,200
2024-04-08: low 20,050 / close 20,200
2024-04-29: high 22,350 / close 22,000
```

Approximate path from entry close:

```text
entry_close: 31,250
peak_high_after_entry: 33,000
MFE: +5.6%
worst_low_after_entry: 20,050
MAE: -35.8%
```

### Interpretation

This is a hard C15 false-positive:

```text
Stage2-Watch: possible from wire-rope / specialty steel and materials relevance.
Stage2-Actionable: blocked unless product-spread, cost pass-through, utilization, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that a steel-material spike is not margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  wire_rope_specialty_steel_label: high
  material_spread_sympathy: high
  product_mix_bridge: weak
  cost_pass_through_bridge: weak
  margin_survival: failed
  price_confirmation_after_entry: shallow
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
row_presence_or_zero_volume_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C15 steel/materials grid:

```text
001430 세아베스틸지주:
  specialty steel product-mix spread positive;
  meaningful MFE came first, but later drawdown requires 4B.

005010 휴스틸:
  steel-pipe / energy-infra material local burst;
  meaningful MFE first, then high MAE, local 4B failure.

002240 고려제강:
  wire-rope / specialty steel late spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C15 is not "materials label is hot."
C15 is "product mix, raw-material cost, selling-price spread, utilization, inventory, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C15_R4L95_001430_2024_02_01","scheduled_round":"R4","scheduled_loop":95,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE","symbol":"001430","name":"세아베스틸지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":22900,"peak_high":27350,"peak_date":"2024-02-26","worst_low_after_entry":16640,"worst_low_after_entry_date":"2024-08-05","mfe_pct":19.4,"mae_pct":-27.3,"classification":"positive_capped_specialty_steel_product_mix_spread_margin_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"specialty_steel_alloy_product_mix_spread_cost_pass_through_margin_bridge","residual_error":"positive_material_spread_path_requires_4b_after_later_mae_without_fresh_margin_evidence","shadow_rule_candidate":"preserve_capped_positive_when_product_mix_spread_bridge_confirms_but_attach_4b_after_material_drawdown"}
{"row_type":"case","case_id":"C15_R4L95_005010_2024_02_01","scheduled_round":"R4","scheduled_loop":95,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE","symbol":"005010","name":"휴스틸","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5340,"peak_high":6170,"peak_date":"2024-02-02","worst_low_after_entry":3620,"worst_low_after_entry_date":"2024-08-05","mfe_pct":15.5,"mae_pct":-32.2,"classification":"local_burst_steel_pipe_energy_infra_material_spread_high_mae_4b_failure","calibration_usable":true,"row_presence_or_zero_volume_caveat":true,"evidence_family":"steel_pipe_energy_infra_material_spread_label_without_sustained_product_spread_margin_bridge","residual_error":"steel_pipe_material_label_can_create_local_mfe_but_fail_green_without_spread_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_steel_pipe_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C15_R4L95_002240_2024_02_20","scheduled_round":"R4","scheduled_loop":95,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE","symbol":"002240","name":"고려제강","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":31250,"peak_high":33000,"peak_date":"2024-02-20","worst_low_after_entry":20050,"worst_low_after_entry_date":"2024-04-08","mfe_pct":5.6,"mae_pct":-35.8,"classification":"hard_4c_candidate_wire_rope_specialty_steel_late_spike_without_spread_margin_survival","calibration_usable":true,"evidence_family":"wire_rope_specialty_steel_late_spike_without_product_spread_cost_pass_through_margin_bridge","residual_error":"materials_late_spike_can_fail_when_product_spread_and_margin_conversion_missing","shadow_rule_candidate":"route_wire_rope_specialty_steel_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":95,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"SPECIALTY_STEEL_STEEL_PIPE_WIRE_ROPE_PRODUCT_MIX_SPREAD_MARGIN_BRIDGE_VS_MATERIAL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"row_presence_or_zero_volume_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":95,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","rule_id":"C15_PRODUCT_MIX_SPREAD_COST_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C15, do not open Stage2-Actionable or Stage3-Green from steel, specialty steel, steel pipe, wire rope, industrial material, China/infrastructure demand, low-PBR cyclical, or one-week materials-stock volume spike labels alone. Require company-specific product mix, raw-material input cost and selling-price spread, cost pass-through or contract-lag visibility, utilization and fixed-cost absorption, export/FX/inventory risk check, margin/OP conversion, and post-trigger price survival. Specialty-steel positives with meaningful MFE but later material MAE should remain capped positive or local 4B unless fresh spread/margin evidence appears. Steel-pipe local bursts with high MAE should not remain Green. Wire-rope or industrial-material late spikes with shallow MFE and high MAE should route to hard-4C when product-spread and margin bridge are missing.","expected_effect":"Reduce generic materials and steel-label false positives while preserving true product-mix spread positives with cost pass-through and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":95,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_type":"material_product_mix_spread_margin_guard","contribution":"Adds one specialty-steel capped positive, one steel-pipe local 4B failure, and one wire-rope late-spike hard-4C counterexample to calibrate C15 product mix, cost pass-through, inventory, and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C15_PRODUCT_MIX_SPREAD_COST_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE:

  Do not open Stage3-Green from:
    - steel / specialty steel label alone
    - steel pipe / wire rope / industrial material label alone
    - China or infrastructure demand readthrough alone
    - low-PBR cyclicals moving together alone
    - one-week materials-stock volume spike alone

  Require at least two of:
    - company-specific product mix improvement
    - raw-material input cost movement
    - selling-price spread improvement
    - cost pass-through or contract-lag visibility
    - utilization / fixed-cost absorption
    - export / FX / inventory-risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the material-spread headline

  If MFE < 10% and MAE < -30%:
    route to C15 hard-4C candidate.

  If MFE > 15% but later MAE < -25%:
    preserve as capped positive or local 4B, not Green, unless current spread/margin evidence appears.

  If MFE is meaningful but the bridge is stale:
    attach 4B until margin evidence refreshes.

  Distinguish:
    - product-mix spread positives where cost pass-through reaches OP
    - from materials late spikes where theme heat does not survive inventory and margin risk.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_95_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C15 material spread supercycle cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C15_PRODUCT_MIX_SPREAD_COST_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C15 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C15 cases agree, consider implementing a canonical guard that:
   - blocks material-label Green without product-mix/spread/cost-pass-through/margin bridge,
   - preserves specialty-steel positives only with price survival and fresh margin evidence,
   - attaches local 4B after meaningful MFE followed by material MAE,
   - routes shallow-MFE/high-MAE industrial-material late spikes to hard-4C.

Expected next schedule:
completed_round = R4
completed_loop = 95
next_round = R5
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 95
next_round = R5
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
