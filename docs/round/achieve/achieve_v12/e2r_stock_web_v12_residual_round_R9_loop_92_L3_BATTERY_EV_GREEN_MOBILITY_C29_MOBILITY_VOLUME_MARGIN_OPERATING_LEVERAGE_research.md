# E2R Stock-Web v12 Residual Research — R9 / Loop 92

```yaml
scheduled_round: R9
scheduled_loop: 92
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF

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
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 92
next_round: R10
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_92_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 92
```

R9 can use:

```text
L3_BATTERY_EV_GREEN_MOBILITY
```

when the case is mobility / transport in nature. This file uses:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

The selected fine branch is:

```text
auto parts / tire / AS module margin operating leverage
vs EV-mobility label or peak-volume blowoff
```

This avoids the previous R9 loop91 ocean-shipping freight-rate branch.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rows: 60
symbols: 27
date_range: 2021-01-08~2024-08-26
good/bad S2: 26/13
4B/4C: 6/0
URL pending/proxy: 3/3
top covered symbols:
  011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
```

Recent R9 outputs already used:

```text
loop88: 002350, 009900, 012860
loop89: 025540, 073240, 033530
loop90: 091810, 003490, 089590
loop91: 011200, 028670, 005880
```

Selected symbols:

```text
012330 현대모비스
161390 한국타이어앤테크놀로지
204320 HL만도
```

They avoid the C29 top-covered list and avoid recent R9 loop88~91 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
012330: same archetype, new symbol, auto-parts module / AS margin operating leverage positive-control branch
161390: same archetype, new symbol, tire export/replacement margin local-positive but high-drawdown 4B branch
204320: same archetype, new symbol, EV/ADAS chassis parts peak-volume blowoff without durable margin bridge
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
012330 현대모비스
  profile: atlas/symbol_profiles/012/012330.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,753
  corporate_action_candidate_dates:
    1997-05-27, 1999-01-08, 1999-04-15, 1999-08-16, 1999-12-21
  2024 entry~D+180 contamination: none

161390 한국타이어앤테크놀로지
  profile: atlas/symbol_profiles/161/161390.json
  name history:
    한국타이어 until 2019-05-21
    한국타이어앤테크놀로지 from 2019-05-22
  first_date: 2012-10-04
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,285
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

204320 HL만도
  profile: atlas/symbol_profiles/204/204320.json
  name history:
    만도 until 2022-09-29
    HL만도 from 2022-09-30
  first_date: 2014-10-06
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,790
  corporate_action_candidate_dates:
    2018-05-08
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C29 is not a generic "mobility stock" or "EV parts stock" label.

The model can over-score:

```text
auto export strength
mobility parts label
ADAS / EV chassis label
tire margin rebound
replacement tire demand
AS module defensiveness
one-week auto-parts volume burst
```

The C29 bridge must map the actual operating leverage:

```text
vehicle production / replacement demand / logistics volume
  -> company-specific volume
  -> ASP / mix
  -> input-cost or FX pass-through
  -> utilization and fixed-cost absorption
  -> margin / OP conversion
  -> price survival after the first mobility rally
```

A mobility stock is like a drivetrain. The headline is only the ignition. Equity value comes when torque reaches the wheels through volume, mix, cost control, and margin.

---

## 5. Case 1 — 012330 현대모비스

```yaml
case_id: C29_R9L92_012330_2024_02_01
symbol: "012330"
name: "현대모비스"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 219500
classification: positive_capped_auto_parts_module_as_margin_bridge
calibration_usable: true
```

### Evidence interpretation

현대모비스 is the cleanest positive-control case in this set.

The useful C29 read is not:

```text
auto parts stock went up
```

It is:

```text
module / AS / core auto-parts earnings base
  -> vehicle production and service demand
  -> product mix and cost absorption
  -> margin and OP conversion
  -> controlled price survival
```

The price path gave moderate upside and relatively controlled drawdown.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 219,500
2024-02-02: high 232,500 / close 232,000
2024-02-19: high 244,500 / close 244,000
2024-03-14: high 268,000 / close 265,000
2024-03-18: high 270,000 / close 268,000
2024-08-05: low 200,500 / close 204,000
2024-09-13: high 224,500 / close 223,500
```

Approximate path from entry close:

```text
entry_close: 219,500
peak_high: 270,000
MFE: +23.0%
worst_low: 200,500
MAE: -8.7%
```

### Interpretation

This is a C29 positive, but capped:

```text
Stage2-Actionable: valid if module/AS margin and volume bridge are explicit.
Stage3-Green: requires sustained OP/margin and volume confirmation.
Local 4B: not mandatory at entry.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  mobility_volume_relevance: high
  module_as_margin_bridge: medium_high
  cost_absorption_visibility: medium
  price_confirmation: medium_high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 6. Case 2 — 161390 한국타이어앤테크놀로지

```yaml
case_id: C29_R9L92_161390_2024_01_25
symbol: "161390"
name: "한국타이어앤테크놀로지"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF
trigger_date: 2024-01-25
entry_date: 2024-01-25
entry_price_basis: close
entry_price: 49450
classification: local_positive_tire_export_replacement_margin_reversal_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

한국타이어앤테크놀로지 is a local-positive / 4B warning case.

The signal had a plausible C29 bridge:

```text
replacement tire and export demand
  -> raw-material and freight cost normalization
  -> ASP / mix
  -> margin operating leverage
```

The forward path delivered a useful MFE first, but later drawdown was large enough that the model should not keep Green open without refreshed margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-01-25: close 49,450
2024-02-14: high 54,500 / close 54,400
2024-02-21: high 58,400 / close 58,400
2024-02-23: high 59,600 / close 58,700
2024-03-27: high 56,800 / close 56,800
2024-08-05: low 37,850 / close 38,650
2024-10-04: low 38,150 / close 38,550
```

Approximate path from entry close:

```text
entry_close: 49,450
peak_high: 59,600
MFE: +20.5%
worst_low: 37,850
MAE: -23.5%
```

### Interpretation

This is not a failure at entry, because the positive MFE came first. But it is a local-positive / 4B case:

```text
Stage2-Actionable: valid if tire margin bridge is explicit.
Stage3-Green: blocked unless refreshed margin and volume evidence appears.
Local 4B: required after MFE > 20% followed by material drawdown.
Hard 4C: no for original entry.
```

### Stress-test components

```text
raw_component_score_proxy:
  tire_replacement_export_signal: high
  input_cost_normalization_bridge: medium_high
  price_confirmation: medium_high
  later_price_survival: weak
  drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 204320 HL만도

```yaml
case_id: C29_R9L92_204320_2024_06_05
symbol: "204320"
name: "HL만도"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF
trigger_date: 2024-06-05
entry_date: 2024-06-05
entry_price_basis: close
entry_price: 49600
classification: hard_4c_candidate_ev_adas_chassis_parts_peak_volume_without_margin_bridge
calibration_usable: true
```

### Evidence interpretation

HL만도 is the hard guardrail case.

The stock had a visible peak-volume mobility-parts spike, but the trigger was too late and the bridge was too weak. The model risk is:

```text
EV / ADAS / chassis parts label
  -> sudden price-volume spike
  -> model reads it as C29 operating leverage
  -> margin and volume bridge is not refreshed
  -> large MAE follows
```

### Price path

Key Stock-Web rows:

```text
2024-06-05: high 50,000 / close 49,600
2024-06-07: high 49,500 / close 47,550
2024-06-13: low 43,700 / close 44,000
2024-07-18: low 39,500 / close 40,200
2024-08-05: low 31,650 / close 32,600
2024-09-09: low 30,850 / close 32,050
2024-10-07: high 39,500 / close 38,900
```

Approximate path from entry close:

```text
entry_close: 49,600
peak_high: 50,000
MFE: +0.8%
worst_low: 30,850
MAE: -37.8%
```

### Interpretation

This is a hard C29 false-positive:

```text
Stage2-Watch: possible from EV/ADAS/mobility-parts label.
Stage2-Actionable: blocked at the peak-volume trigger unless margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  mobility_parts_label: high
  ev_adas_chassis_theme: high
  volume_margin_bridge: weak
  price_confirmation: failed_after_peak
  drawdown_penalty: high
  hard_4c_guard: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C29 mobility-parts grid:

```text
012330 현대모비스:
  module/AS margin bridge positive;
  moderate MFE and controlled MAE.

161390 한국타이어앤테크놀로지:
  tire export/replacement margin local positive;
  positive MFE came first, but later drawdown requires local 4B.

204320 HL만도:
  EV/ADAS/chassis label at peak volume failed;
  almost no MFE and high MAE, hard 4C candidate.
```

Shared rule:

```text
C29 is not "mobility label."
C29 is "mobility volume, mix, cost absorption, and margin conversion reach the company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L92_012330_2024_02_01","scheduled_round":"R9","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF","symbol":"012330","name":"현대모비스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":219500,"peak_high":270000,"peak_date":"2024-03-18","worst_low":200500,"worst_low_date":"2024-08-05","mfe_pct":23.0,"mae_pct":-8.7,"classification":"positive_capped_auto_parts_module_as_margin_bridge","calibration_usable":true,"evidence_family":"auto_parts_module_as_margin_volume_cost_absorption_bridge","residual_error":"positive_path_still_needs_sustained_margin_and_volume_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_module_as_margin_volume_bridge_confirms_but_cap_green_without_sustained_op_evidence"}
{"row_type":"case","case_id":"C29_R9L92_161390_2024_01_25","scheduled_round":"R9","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF","symbol":"161390","name":"한국타이어앤테크놀로지","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":49450,"peak_high":59600,"peak_date":"2024-02-23","worst_low":37850,"worst_low_date":"2024-08-05","mfe_pct":20.5,"mae_pct":-23.5,"classification":"local_positive_tire_export_replacement_margin_reversal_with_4b_watch","calibration_usable":true,"evidence_family":"tire_export_replacement_input_cost_margin_bridge","residual_error":"positive_tire_margin_move_can_reverse_without_refreshed_volume_margin_evidence","shadow_rule_candidate":"preserve_local_positive_but_attach_4b_after_mfe_then_material_drawdown"}
{"row_type":"case","case_id":"C29_R9L92_204320_2024_06_05","scheduled_round":"R9","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF","symbol":"204320","name":"HL만도","trigger_date":"2024-06-05","entry_date":"2024-06-05","entry_price":49600,"peak_high":50000,"peak_date":"2024-06-05","worst_low":30850,"worst_low_date":"2024-09-09","mfe_pct":0.8,"mae_pct":-37.8,"classification":"hard_4c_candidate_ev_adas_chassis_parts_peak_volume_without_margin_bridge","calibration_usable":true,"evidence_family":"ev_adas_chassis_parts_peak_volume_without_volume_margin_bridge","residual_error":"mobility_parts_label_can_overpromote_at_peak_volume_without_margin_conversion","shadow_rule_candidate":"route_peak_volume_mobility_parts_label_to_hard_4c_if_mfe_near_zero_mae_large"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":92,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_PARTS_TIRE_AS_MARGIN_OPERATING_LEVERAGE_VS_EV_MOBILITY_LABEL_BLOWOFF","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":92,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_MOBILITY_VOLUME_MIX_COST_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 mobility/transport names, do not open Stage2-Actionable or Stage3-Green from auto export, mobility parts, tire, EV/ADAS/chassis, logistics, or one-week volume spike labels alone. Require company-specific volume, ASP or mix, input-cost/FX pass-through, utilization/fixed-cost absorption, margin/OP conversion, and post-trigger price survival. Auto-parts module/AS positives may be Actionable when volume and margin bridge are explicit. Tire margin positives with later material drawdown should attach local 4B. Peak-volume EV/ADAS parts names with near-zero MFE and large MAE should route to hard-4C.","expected_effect":"Preserve true mobility operating-leverage positives while reducing EV/mobility label and peak-volume auto-parts false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":92,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"auto_parts_tire_mobility_margin_guard","contribution":"Adds one auto-parts module/AS capped positive, one tire margin local-positive with 4B watch, and one EV/ADAS parts hard-4C candidate to calibrate C29 mobility margin-conversion and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_MOBILITY_VOLUME_MIX_COST_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [auto_parts, tire, module, as_parts, ev_adas_chassis, mobility_supplier]:

  Do not open Stage3-Green from:
    - auto export label alone
    - mobility parts label alone
    - EV / ADAS / chassis label alone
    - tire margin rebound label alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - company-specific volume growth
    - ASP / product-mix improvement
    - input-cost or FX pass-through
    - utilization / fixed-cost absorption
    - margin or OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the mobility headline

  If MFE < 5% and MAE < -30%:
    route to C29 hard-4C candidate.

  If MFE > 20% but later MAE < -20%:
    preserve as local positive but attach 4B watch unless new margin evidence appears.

  If MFE > 20% and MAE remains controlled:
    allow Actionable only if volume and margin bridge are explicit.

  Distinguish:
    - module/AS or tire names with real margin bridge
    - from EV/ADAS/chassis peak-volume names where valuation outruns earnings conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 auto-parts/tire mobility operating-leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_MOBILITY_VOLUME_MIX_COST_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 cases agree, consider implementing a canonical guard that:
   - blocks mobility-label Green without volume/mix/cost/margin bridge,
   - preserves module/AS positives with controlled MAE and margin evidence,
   - attaches local 4B after tire-margin MFE followed by material drawdown,
   - routes near-zero-MFE/high-MAE peak-volume EV/ADAS parts cases to hard-4C.

Expected next schedule:
completed_round = R9
completed_loop = 92
next_round = R10
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 92
next_round = R10
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
