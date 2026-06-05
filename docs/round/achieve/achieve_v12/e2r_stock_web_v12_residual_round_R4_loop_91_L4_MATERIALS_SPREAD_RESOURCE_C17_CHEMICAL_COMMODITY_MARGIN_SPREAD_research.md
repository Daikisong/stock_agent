# E2R Stock-Web v12 Residual Research — R4 / Loop 91

```yaml
scheduled_round: R4
scheduled_loop: 91
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA

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
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 91
next_round: R5
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C11_BATTERY_ORDERBOOK_RERATING_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 91
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage already covered:

```text
loop88: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
loop89: C15_MATERIAL_SPREAD_SUPERCYCLE
loop90: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
```

This run returns to C17, but uses a different branch:

```text
chemical/material spread margin bridge vs generic restocking / low-base cycle beta
```

The file avoids strategic-resource policy and battery-orderbook logic from the prior runs.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rows: 21
symbols: 15
date_range: 2020-08-07~2024-03-21
good/bad S2: 8/3
4B/4C: 4/0
URL pending/proxy: 0/0
top covered symbols:
  004000(3), 006650(2), 011780(2), 014680(2), 298020(2), 001390(1)
```

Selected symbols:

```text
002380 KCC
011170 롯데케미칼
009830 한화솔루션
```

These avoid the top-covered C17 symbols and avoid the latest R4 loop90 C16 symbols:

```text
036460, 004090, 024060
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
002380: same archetype, new symbol, specialty material/silicone-paint margin bridge positive branch
011170: same archetype, new symbol, petrochemical spread false-positive branch
009830: same archetype, new symbol, chemical/solar commodity spread and low-base false-positive branch
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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
002380 KCC
  profile: atlas/symbol_profiles/002/002380.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,740
  corporate_action_candidate_dates:
    2000-04-17
  2024 entry~D+180 contamination: none

011170 롯데케미칼
  profile: atlas/symbol_profiles/011/011170.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,764
  corporate_action_candidate_dates:
    2023-02-13
  2024 entry~D+180 contamination: none

009830 한화솔루션
  profile: atlas/symbol_profiles/009/009830.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,741
  corporate_action_candidate_dates:
    1999-04-20, 2008-07-04
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C17 is about commodity and chemical spread conversion, not a broad materials rally.

The model can over-score:

```text
petrochemical restocking
naphtha spread rebound
commodity price bounce
silicone / paint / film material label
solar-polysilicon low-base recovery
inventory-cycle recovery
```

The bridge must be stricter:

```text
feedstock/input cost
  -> product ASP
  -> spread durability
  -> volume/utilization
  -> inventory normalization
  -> gross margin / OP conversion
  -> price survival after the first restocking bounce
```

A chemical spread is like a toll road between input cost and product price. The car count can rise, but if the toll is squeezed, shareholders still do not receive the cash.

---

## 5. Case 1 — 002380 KCC

```yaml
case_id: C17_R4L91_002380_2024_01_17
symbol: "002380"
name: "KCC"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA
trigger_date: 2024-01-17
entry_date: 2024-01-17
entry_price_basis: close
entry_price: 203500
classification: positive_specialty_material_margin_bridge_with_local_4b_watch
calibration_usable: true
```

### Evidence interpretation

KCC is the positive control. It is not a simple petrochemical beta name. The more constructive read is:

```text
specialty material / silicone / paint and construction-material mix
  -> margin and balance-sheet repair expectation
  -> value and spread-quality rerating
  -> sustained price confirmation
```

The stock produced a controlled and extended rerating after the January low area. This supports C17 when the material spread story is tied to actual margin quality rather than only commodity restocking language.

### Price path

Key Stock-Web rows:

```text
2024-01-17: close 203,500
2024-01-29: high 238,500 / close 233,500
2024-02-01: high 269,500 / close 266,000
2024-03-08: high 293,000 / close 291,500
2024-06-28: high 320,500 / close 308,500
2024-07-15: high 342,500 / close 335,000
2024-08-05: low 270,500 / close 278,000
```

Approximate return path from 2024-01-17 close:

```text
entry_close: 203,500
peak_high: 344,500
peak_date: 2024-07-26
MFE: +69.3%
worst_low_after_entry_checked: 199,900 on 2024-01-18
initial_MAE: -1.8%
post_peak_checked_low: 270,500 on 2024-08-05
peak_to_later_low_drawdown: -21.5%
```

### Interpretation

This is the C17 positive:

```text
Stage2-Actionable: valid when specialty material spread and margin bridge exist.
Stage3-Green: possible only when margin/OP conversion is explicit.
Local 4B: attach after +50% MFE and post-peak drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  material_spread_quality: high
  commodity_beta_contamination: medium
  margin_conversion_visibility: medium_high
  price_confirmation: high
  drawdown_penalty: moderate_after_peak
  local_4b_overlay: required
```

---

## 6. Case 2 — 011170 롯데케미칼

```yaml
case_id: C17_R4L91_011170_2024_01_24
symbol: "011170"
name: "롯데케미칼"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA
trigger_date: 2024-01-24
entry_date: 2024-01-24
entry_price_basis: close
entry_price: 128700
classification: hard_4c_candidate_petrochemical_restocking_without_spread_margin_bridge
calibration_usable: true
```

### Evidence interpretation

롯데케미칼 is the hard guardrail case. It can look like the obvious C17 candidate because it has petrochemical spread exposure. But C17 should not upgrade a stock only because:

```text
petrochemical cycle is depressed
China or global restocking may return
naphtha/product spread may improve later
```

The model needs actual spread durability, utilization, and margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-01-24: close 128,700
2024-01-25: high 137,000 / close 136,900
2024-02-01: high 140,800 / close 140,100
2024-03-20: low 116,800 / close 117,000
2024-07-24: close 100,800
2024-08-05: low 88,200 / close 89,100
2024-08-09: low 79,400 / close 79,800
2024-09-09: low 76,500 / close 79,000
```

Approximate return path from 2024-01-24 close:

```text
entry_close: 128,700
peak_high: 140,800
MFE: +9.4%
worst_low: 76,500
MAE: -40.6%
```

### Interpretation

This is the C17 false-positive wall.

```text
Stage2-Watch: allowed from cycle/spread exposure.
Stage2-Actionable: blocked without hard spread and margin bridge.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The lesson is simple: petrochemical exposure is not spread recovery.

### Stress-test components

```text
raw_component_score_proxy:
  petrochemical_cycle_exposure: high
  spread_recovery_confirmation: weak
  utilization_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 009830 한화솔루션

```yaml
case_id: C17_R4L91_009830_2024_02_01
symbol: "009830"
name: "한화솔루션"
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 35000
classification: counterexample_chemical_solar_spread_low_base_without_margin_bridge
calibration_usable: true
```

### Evidence interpretation

한화솔루션 is the chemical/solar low-base false-positive. It belongs in the C17 spread family because the model can be tempted by:

```text
chemical spread rebound
solar material low-base recovery
inventory normalization
policy or tariff speculation around solar supply chains
```

But the forward path shows that a spread label and low-base narrative were not enough. The model needs module/material spread, utilization, ASP, and OP bridge.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 35,000
2024-02-02: high 35,850 / close 34,700
2024-04-01: high 29,100 / close 29,050
2024-07-01: low 25,700 / close 26,500
2024-08-05: low 22,150 / close 22,950
2024-08-14: high 28,550 / close 28,100
2024-09-09: low 22,550 / close 23,300
```

Approximate return path from 2024-02-01 close:

```text
entry_close: 35,000
peak_high: 35,850
MFE: +2.4%
worst_low: 22,150
MAE: -36.7%
```

### Interpretation

This is a strong counterexample and close to hard-4C:

```text
Stage2-Watch: possible.
Stage2-Actionable: blocked without spread/margin bridge.
Stage3-Green: blocked.
Hard 4C candidate: yes if the model promoted from low-base recovery alone.
```

### Stress-test components

```text
raw_component_score_proxy:
  chemical/solar_low_base_label: high
  spread_bridge: weak
  ASP/utilization_bridge: weak
  price_confirmation: failed
  drawdown_penalty: high
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C17 grid:

```text
002380 KCC:
  specialty material / silicone / paint margin-quality positive.
  Strong MFE but local 4B after extended rerating.

011170 롯데케미칼:
  petrochemical spread exposure alone failed.
  Shallow MFE + large MAE creates a hard 4C candidate.

009830 한화솔루션:
  chemical/solar low-base spread story failed without ASP/utilization/margin bridge.
```

Shared rule:

```text
C17 is not "chemical cycle might recover."
C17 is "product price minus input cost converts into durable gross margin and operating profit."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C17_R4L91_002380_2024_01_17","scheduled_round":"R4","scheduled_loop":91,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA","symbol":"002380","name":"KCC","trigger_date":"2024-01-17","entry_date":"2024-01-17","entry_price":203500,"peak_high":344500,"peak_date":"2024-07-26","worst_low_after_entry":199900,"worst_low_after_entry_date":"2024-01-18","post_peak_low":270500,"post_peak_low_date":"2024-08-05","mfe_pct":69.3,"initial_mae_pct":-1.8,"peak_to_later_low_drawdown_pct":-21.5,"classification":"positive_specialty_material_margin_bridge_with_local_4b_watch","calibration_usable":true,"evidence_family":"specialty_material_silicone_paint_spread_margin_bridge","residual_error":"positive_entry_but_extended_rerating_requires_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_material_spread_margin_bridge_and_price_survival_confirm; attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C17_R4L91_011170_2024_01_24","scheduled_round":"R4","scheduled_loop":91,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA","symbol":"011170","name":"롯데케미칼","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":128700,"peak_high":140800,"peak_date":"2024-02-01","worst_low":76500,"worst_low_date":"2024-09-09","mfe_pct":9.4,"mae_pct":-40.6,"classification":"hard_4c_candidate_petrochemical_restocking_without_spread_margin_bridge","calibration_usable":true,"evidence_family":"petrochemical_spread_restocking_without_utilization_margin_bridge","residual_error":"petrochemical_cycle_label_can_overpromote_without_actual_spread_recovery","shadow_rule_candidate":"block_actionable_green_if_petrochemical_spread_exposure_has_shallow_mfe_and_large_mae"}
{"row_type":"case","case_id":"C17_R4L91_009830_2024_02_01","scheduled_round":"R4","scheduled_loop":91,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA","symbol":"009830","name":"한화솔루션","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35000,"peak_high":35850,"peak_date":"2024-02-02","worst_low":22150,"worst_low_date":"2024-08-05","mfe_pct":2.4,"mae_pct":-36.7,"classification":"counterexample_chemical_solar_spread_low_base_without_margin_bridge","calibration_usable":true,"evidence_family":"chemical_solar_low_base_spread_story_without_asp_utilization_margin_bridge","residual_error":"low_base_material_spread_story_can_fail_without_profit_conversion","shadow_rule_candidate":"cap_at_watch_or_route_to_4c_when_low_base_spread_story_mfe_shallow_mae_large"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":91,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_MATERIAL_SPREAD_MARGIN_BRIDGE_VS_GENERIC_RESTOCKING_AND_LOW_BASE_CYCLE_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":91,"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","rule_id":"C17_SPREAD_TO_MARGIN_CONVERSION_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C17, do not open Stage2-Actionable or Stage3-Green from commodity spread exposure, restocking, low-base cycle recovery, or chemical/material label alone. Require input cost to product ASP spread durability, utilization, inventory normalization, gross margin or OP conversion, and post-trigger price survival. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE is large but later drawdown appears, preserve positive classification with local 4B watch.","expected_effect":"Reduce petrochemical and chemical/solar low-base false positives while preserving specialty material spread positives with price survival and margin-quality bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":91,"canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","residual_type":"chemical_spread_margin_conversion_guard","contribution":"Adds one specialty-material positive and two petrochemical/chemical-solar false positives to separate spread exposure from durable margin conversion.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C17_SPREAD_TO_MARGIN_CONVERSION_REQUIRED

IF canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:

  Do not open Stage3-Green from:
    - petrochemical cycle label alone
    - naphtha/product spread hope alone
    - restocking headline alone
    - solar/chemical low-base recovery alone
    - one-quarter commodity price bounce alone

  Require at least two of:
    - input-cost to output-ASP spread expansion
    - utilization recovery
    - inventory normalization
    - gross margin or OP conversion
    - customer/volume durability
    - low-MAE price survival after the trigger
    - earnings revision confirmation

  If MFE < 10% and MAE < -30%:
    route to C17 false-positive / hard-4C candidate.

  If MFE > 50% but later drawdown exceeds -20%:
    preserve positive entry classification but attach local 4B watch.

  Distinguish:
    - specialty material names with margin-quality rerating
    - from petrochemical and solar/chemical low-base labels with no confirmed spread conversion.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_91_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C17 chemical/material spread cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C17_SPREAD_TO_MARGIN_CONVERSION_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C17 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C17 cases agree, consider implementing a canonical guard that:
   - blocks commodity/re-stocking/low-base Green without spread-to-margin conversion,
   - preserves specialty material margin positives with price survival,
   - attaches local 4B after large rerating,
   - routes shallow-MFE/high-MAE petrochemical and chemical-solar cases to C17 false-positive or hard-4C.

Expected next schedule:
completed_round = R4
completed_loop = 91
next_round = R5
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 91
next_round = R5
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
