# E2R Stock-Web v12 Residual Research — R4 / Loop 92

```yaml
scheduled_round: R4
scheduled_loop: 92
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL

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
local_4b_overlay_case_count: 0
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 92
next_round: R5
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_92_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 92
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage already covered:

```text
loop89: C15_MATERIAL_SPREAD_SUPERCYCLE
loop90: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop91: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

This run returns to C15, but avoids the top-covered copper/aluminum small-cap cluster and uses a different fine branch:

```text
steel pipe / special steel / blast-furnace material spread bridge
vs generic material supercycle label
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
306200 세아제강
001430 세아베스틸지주
004020 현대제철
```

They avoid the top-covered C15 symbols and avoid recent R4 loop90/91 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
306200: same archetype, new symbol, steel pipe / energy tubular spread and demand bridge
001430: same archetype, new symbol, special steel supercycle label without sustained margin bridge
004020: same archetype, new symbol, blast-furnace steel supercycle label / China-demand false-positive branch
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
306200 세아제강
  profile: atlas/symbol_profiles/306/306200.json
  first_date: 2018-10-05
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,811
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

001430 세아베스틸지주
  profile: atlas/symbol_profiles/001/001430.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,728
  corporate_action_candidate_dates:
    1996-01-03, 1997-01-03, 1999-04-08, 1999-05-18, 2003-12-26
  2024 entry~D+180 contamination: none

004020 현대제철
  profile: atlas/symbol_profiles/004/004020.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,764
  corporate_action_candidate_dates:
    1997-01-03, 1997-10-16, 1999-03-25, 1999-07-14, 2000-04-12, 2014-01-24
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C15 is about material spread/supercycle, not a generic “raw-materials are strong” label.

The model can over-score:

```text
commodity supercycle
steel price rebound
energy-pipe demand
special steel label
China restocking
infrastructure cycle
materials relative strength
```

The bridge must be stricter:

```text
material price / demand cycle
  -> company-specific product spread
  -> volume and utilization
  -> inventory discipline
  -> input-cost pass-through
  -> margin / OP conversion
  -> price survival after the first cycle rally
```

A material supercycle is a rising tide, but each company owns a different boat. Steel pipe, special steel, and blast-furnace steel do not float the same way. The model must not treat the tide as if every hull is watertight.

---

## 5. Case 1 — 306200 세아제강

```yaml
case_id: C15_R4L92_306200_2024_01_24
symbol: "306200"
name: "세아제강"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL
trigger_date: 2024-01-24
entry_date: 2024-01-24
entry_price_basis: close
entry_price: 121800
classification: positive_capped_steel_pipe_spread_demand_bridge
calibration_usable: true
```

### Evidence interpretation

세아제강 is the constructive control in this set.

The useful C15 read is not “steel went up.” It is more specific:

```text
steel pipe / tubular exposure
  -> energy or infrastructure demand bridge
  -> product spread and export mix
  -> margin defensiveness
  -> price survival better than generic steel names
```

The price path had moderate upside and relatively contained drawdown compared with the two counterexamples. It is not a huge Green, but it is a valid capped positive.

### Price path

Key Stock-Web rows:

```text
2024-01-24: close 121,800
2024-02-13: high 139,700 / close 138,200
2024-03-07: high 141,200 / close 138,900
2024-03-22: high 143,800 / close 140,000
2024-07-18: high 140,200 / close 138,300
2024-08-05: low 118,000 / close 118,000
2024-09-11: low 108,700 / close 109,200
```

Approximate path from entry close:

```text
entry_close: 121,800
peak_high: 143,800
MFE: +18.1%
worst_low: 108,700
MAE: -10.8%
```

### Interpretation

This is a C15 capped positive:

```text
Stage2-Actionable: allowed if steel-pipe demand/spread bridge is explicit.
Stage3-Green: blocked unless product spread, export mix, and margin conversion are clear.
Local 4B: not mandatory, but monitor if MFE expands without fresh spread evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  product_spread_specificity: medium_high
  generic_material_beta: medium
  demand_bridge: medium
  margin_bridge: medium
  price_survival: medium_high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 6. Case 2 — 001430 세아베스틸지주

```yaml
case_id: C15_R4L92_001430_2024_02_23
symbol: "001430"
name: "세아베스틸지주"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL
trigger_date: 2024-02-23
entry_date: 2024-02-23
entry_price_basis: close
entry_price: 26300
classification: hard_4c_candidate_special_steel_label_without_durable_spread_margin_bridge
calibration_usable: true
```

### Evidence interpretation

세아베스틸지주 is the special-steel false-positive.

The label can look good:

```text
special steel
auto / machinery / industrial cycle
materials recovery
steel spread rebound
```

But the forward path did not validate a durable C15 rerating. The initial MFE was shallow and later drawdown was large.

### Price path

Key Stock-Web rows:

```text
2024-02-23: close 26,300
2024-02-26: high 27,350 / close 26,200
2024-03-07: low 22,550 / close 22,950
2024-04-05: low 21,150 / close 21,800
2024-07-26: low 19,100 / close 19,160
2024-08-05: low 16,640 / close 17,380
2024-09-24: high 20,450 / close 20,450
```

Approximate path from entry close:

```text
entry_close: 26,300
peak_high: 27,350
MFE: +4.0%
worst_low: 16,640
MAE: -36.7%
```

### Interpretation

This is a hard C15 guardrail case:

```text
Stage2-Watch: allowed from special-steel cycle relevance.
Stage2-Actionable: blocked unless spread and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is that special-steel label alone is not a supercycle bridge.

### Stress-test components

```text
raw_component_score_proxy:
  material_label_quality: medium_high
  spread_bridge: weak
  utilization_bridge: weak
  margin_conversion_visibility: weak
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 004020 현대제철

```yaml
case_id: C15_R4L92_004020_2024_02_07
symbol: "004020"
name: "현대제철"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL
trigger_date: 2024-02-07
entry_date: 2024-02-07
entry_price_basis: close
entry_price: 37000
classification: hard_4c_candidate_blast_furnace_steel_supercycle_label_without_china_demand_margin_bridge
calibration_usable: true
```

### Evidence interpretation

현대제철 is the generic blast-furnace steel / China-demand supercycle false-positive.

The company is large and real, but that is not enough for C15. The trigger can look attractive if the model reads:

```text
steel rebound
China restocking
infrastructure cycle
automotive steel demand
materials value rotation
```

as if those automatically become margin improvement. The price path says they did not.

### Price path

Key Stock-Web rows:

```text
2024-02-07: close 37,000
2024-02-08: high 37,400 / close 36,350
2024-02-13: high 37,500 / close 36,350
2024-03-19: low 32,150 / close 32,250
2024-07-24: low 26,650 / close 26,900
2024-08-05: low 24,350 / close 24,800
2024-09-12: low 23,750 / close 23,800
```

Approximate path from entry close:

```text
entry_close: 37,000
peak_high: 37,500
MFE: +1.4%
worst_low: 23,750
MAE: -35.8%
```

### Interpretation

This is the cleanest C15 false-positive wall:

```text
Stage2-Watch: possible from broad materials/steel exposure.
Stage2-Actionable: blocked without hard product-spread and margin evidence.
Stage3-Green: blocked.
Hard 4C: yes.
```

Generic steel beta is not a spread supercycle rerating.

### Stress-test components

```text
raw_component_score_proxy:
  broad_steel_supercycle_label: high
  company_specific_spread_bridge: weak
  China_demand_bridge: weak
  input_cost_pass_through: unclear
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C15 grid:

```text
306200 세아제강:
  steel-pipe/product-spread case;
  modest positive with controlled MAE,
  but Green needs explicit product spread and margin bridge.

001430 세아베스틸지주:
  special-steel label failed;
  shallow MFE and high MAE, hard 4C candidate.

004020 현대제철:
  broad steel supercycle label failed more cleanly;
  almost no MFE and large MAE, hard 4C candidate.
```

Shared rule:

```text
C15 is not "materials cycle is up."
C15 is "this company's product spread, volume, utilization, and pass-through convert the cycle into margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C15_R4L92_306200_2024_01_24","scheduled_round":"R4","scheduled_loop":92,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL","symbol":"306200","name":"세아제강","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":121800,"peak_high":143800,"peak_date":"2024-03-22","worst_low":108700,"worst_low_date":"2024-09-11","mfe_pct":18.1,"mae_pct":-10.8,"classification":"positive_capped_steel_pipe_spread_demand_bridge","calibration_usable":true,"evidence_family":"steel_pipe_product_spread_energy_infra_demand_margin_bridge","residual_error":"positive_path_still_needs_company_specific_product_spread_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_product_spread_and_margin_bridge_confirm_but_cap_green_without_explicit_conversion"}
{"row_type":"case","case_id":"C15_R4L92_001430_2024_02_23","scheduled_round":"R4","scheduled_loop":92,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL","symbol":"001430","name":"세아베스틸지주","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":26300,"peak_high":27350,"peak_date":"2024-02-26","worst_low":16640,"worst_low_date":"2024-08-05","mfe_pct":4.0,"mae_pct":-36.7,"classification":"hard_4c_candidate_special_steel_label_without_durable_spread_margin_bridge","calibration_usable":true,"evidence_family":"special_steel_material_cycle_label_without_utilization_spread_margin_bridge","residual_error":"special_steel_label_can_overpromote_without_spread_margin_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_product_spread_bridge_missing"}
{"row_type":"case","case_id":"C15_R4L92_004020_2024_02_07","scheduled_round":"R4","scheduled_loop":92,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL","symbol":"004020","name":"현대제철","trigger_date":"2024-02-07","entry_date":"2024-02-07","entry_price":37000,"peak_high":37500,"peak_date":"2024-02-13","worst_low":23750,"worst_low_date":"2024-09-12","mfe_pct":1.4,"mae_pct":-35.8,"classification":"hard_4c_candidate_blast_furnace_steel_supercycle_label_without_china_demand_margin_bridge","calibration_usable":true,"evidence_family":"blast_furnace_steel_supercycle_label_without_china_demand_input_cost_margin_bridge","residual_error":"generic_steel_supercycle_label_can_fail_without_company_specific_margin_conversion","shadow_rule_candidate":"route_broad_steel_supercycle_label_to_hard_4c_if_mfe_near_zero_and_mae_large"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":92,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_SPECIAL_STEEL_BLAST_FURNACE_MATERIAL_SPREAD_BRIDGE_VS_GENERIC_SUPERCYCLE_LABEL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":92,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","rule_id":"C15_PRODUCT_SPREAD_MARGIN_CONVERSION_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C15, do not open Stage2-Actionable or Stage3-Green from materials supercycle, steel rebound, China restocking, infrastructure cycle, or product-label exposure alone. Require company-specific product spread, volume/utilization, inventory discipline, input-cost pass-through, margin/OP conversion, and post-trigger price survival. Steel-pipe names may be capped positives when product spread and demand bridge are visible. Special-steel or blast-furnace names with shallow MFE and large MAE should route to hard-4C unless spread and margin bridge are explicit.","expected_effect":"Reduce broad materials/steel supercycle false positives while preserving product-spread positives with controlled MAE and margin bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":92,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_type":"material_supercycle_product_spread_margin_guard","contribution":"Adds one capped steel-pipe positive and two special-steel/blast-furnace hard-4C counterexamples to calibrate C15 product-spread and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C15_PRODUCT_SPREAD_MARGIN_CONVERSION_REQUIRED

IF canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE:

  Do not open Stage3-Green from:
    - materials supercycle label alone
    - steel price rebound label alone
    - China restocking headline alone
    - infrastructure / machinery cycle label alone
    - one-month material-stock relative strength alone

  Require at least two of:
    - company-specific product spread expansion
    - volume or utilization improvement
    - inventory discipline
    - input-cost pass-through
    - product mix / export mix bridge
    - margin or OP conversion
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -30%:
    route to C15 hard-4C candidate.

  If MFE > 15% but MAE is still material and spread bridge is not explicit:
    cap at Watch/Yellow or Actionable, not Green.

  Distinguish:
    - steel pipe / specialized product spread names with controlled MAE
    - from special-steel or blast-furnace generic steel beta where China-demand and margin bridge are unconfirmed.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_92_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C15 material-spread/supercycle cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C15_PRODUCT_SPREAD_MARGIN_CONVERSION_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C15 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C15 cases agree, consider implementing a canonical guard that:
   - blocks generic material/steel supercycle Green without product-spread and margin bridge,
   - preserves capped positives only where product spread and low-MAE price survival confirm,
   - routes shallow-MFE/high-MAE special-steel and blast-furnace cases to hard-4C,
   - separates product-spread winners from broad commodity beta.

Expected next schedule:
completed_round = R4
completed_loop = 92
next_round = R5
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 92
next_round = R5
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
