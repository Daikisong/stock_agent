# E2R Stock-Web v12 Residual Research — R10 / Loop 98

```yaml
scheduled_round: R10
scheduled_loop: 98
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE

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
hard_4c_candidate_count: 0
cement_building_material_case_count: 2
housing_service_project_cashflow_case_count: 1
construction_material_spread_case_count: 2
housing_pf_cashflow_bridge_missing_count: 1
input_cost_energy_freight_bridge_missing_count: 1
project_cashflow_receivables_bridge_missing_count: 1
row_presence_or_old_corporate_action_caveat_count: 3
short_listing_or_segment_trust_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 98
next_round: R11
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 98
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is the hard L9 construction / real-estate / housing round.

The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

The selected fine branch is:

```text
cement / building materials / housing-service contractor
cement volume, regional demand, fuel/electricity/freight/input cost,
ready-mix and construction demand, housing-service cashflow, receivables,
working capital, margin, and row-trust bridge
vs generic construction-material / housing-service label spike
```

This deliberately avoids:
- C30 top-covered names:
  `002990`, `294870`, `375500`, `004960`, `013580`, `006360`
- recent R10 loop97 MEP / EPC names:
  `011560`, `010400`, `016250`
- recent R10 loop88~96 construction names:
  `047040`, `012630`, `021320`,
  `000720`, `003070`, `002780`,
  `014790`, `010780`, `005960`,
  `013360`, `001470`, `002410`,
  `034300`, `009410`, `002460`,
  `035890`, `013120`, `017000`,
  `001260`, `010960`, `001840`,
  `028100`, `002150`, `025950`,
  `028050`, `097230`, `026150`

Selected symbols:

```text
300720 한일시멘트
004980 성신양회
317400 자이에스앤디
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rows: 81
symbols: 31
date_range: 2022-01-12~2024-08-26
good/bad S2: 16/29
4B/4C: 3/4
URL pending/proxy: 20/25
top covered symbols:
  002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
300720: same archetype, new symbol, cement / building-material spread positive with Green cap after large MFE
004980: same archetype, new symbol, cement / construction material positive but 4B/Green cap after input-cost and demand evidence risk
317400: same archetype, new symbol, housing-service / small-project contractor Watch cap with shallow MFE and material MAE
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
300720 한일시멘트
  profile: atlas/symbol_profiles/300/300720.json
  first_date: 2018-08-06
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,847
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2020-08-14, 2021-09-13
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

004980 성신양회
  profile: atlas/symbol_profiles/004/004980.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,757
  non_tradable_zero_volume rows: 7
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1998-12-11, 1999-03-15, 2001-02-01
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity caveats are outside selected 2024 validation window.

317400 자이에스앤디
  profile: atlas/symbol_profiles/317/317400.json
  first_date: 2019-11-06
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,544
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2021-05-13
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus old construction names, but no direct 2024 corporate-action contamination.
```

---

## 4. Archetype residual problem

C30 is not merely about whether a construction or building-materials stock moves. It is about whether a project, housing, or construction-material label can survive the balance-sheet, PF, receivables, working-capital, input-cost, and margin checks.

The model can over-score:

```text
cement / building-material label
housing-service / small construction contractor label
ready-mix or regional construction demand headline
PF stabilization policy headline
construction-material price hike or input-cost relief headline
low-PBR construction / materials rerating
one-week construction-material stock volume spike
```

The C30 bridge must be stricter:

```text
construction / housing / building-material event
  -> named end-market, region, project, or customer channel
  -> construction volume and order visibility
  -> cement / ready-mix / material selling price
  -> coal / electricity / fuel / freight / input-cost check
  -> inventory and working-capital timing
  -> housing-service receivables and cash collection
  -> PF / developer / counterparty exposure
  -> maintenance capex and balance-sheet trust
  -> margin / FCF conversion
  -> price survival after the first construction-material label spike
```

A C30 cement or housing-service thesis is like a cement truck leaving the plant. The headline says demand exists, but equity value appears only when the truck is full, the customer pays, fuel and freight do not eat the spread, receivables become cash, and PF or housing exposure does not crack the ledger.

---

## 5. Case 1 — 300720 한일시멘트

```yaml
case_id: C30_R10L98_300720_2024_02_01
symbol: "300720"
name: "한일시멘트"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12100
classification: positive_cement_building_material_volume_input_cost_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

한일시멘트 is the constructive C30 cement / building-materials control in this set.

The useful C30 read is not simply:

```text
시멘트 / 건자재주가 강하다
```

It is:

```text
cement / building-material volume and spread relevance
  -> construction demand and regional shipment visibility
  -> cement selling price versus coal / electricity / fuel / freight cost
  -> working-capital and inventory timing
  -> strong price confirmation into July-August
```

The forward path produced a meaningful MFE with controlled early drawdown. This preserves positive classification. However, Green should remain capped unless volume, input-cost, inventory, receivables, and margin evidence is fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,350 / close 12,100
2024-02-05: high 12,670 / close 12,650
2024-04-29: high 13,160 / close 13,160
2024-07-31: high 15,490 / close 14,550
2024-08-23: high 15,700 / close 15,500
2024-09-23: low 13,760 / close 13,830
2024-10-02: low 13,100 / close 13,180
```

Approximate path from entry close:

```text
entry_close: 12,100
peak_high: 15,700
MFE: +29.8%
worst_low_after_entry: 11,770
MAE: -2.7%
```

### Interpretation

This is a C30 positive with Green cap:

```text
Stage2-Actionable: possible if cement shipment, selling-price, input-cost, inventory, and margin bridge are explicit.
Stage3-Green: blocked after a large rerating unless fresh volume and margin evidence appears.
Local 4B: monitor if construction-material price outruns input-cost and demand evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  cement_building_material_relevance: high
  construction_volume_bridge: medium_high
  selling_price_input_cost_spread: medium_high
  inventory_working_capital_bridge: medium
  receivables_cashflow_bridge: medium
  price_confirmation: high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 004980 성신양회

```yaml
case_id: C30_R10L98_004980_2024_02_01
symbol: "004980"
name: "성신양회"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 8120
classification: positive_cement_material_spread_rerating_with_4b_green_cap_if_input_cost_demand_evidence_stale
calibration_usable: true
```

### Evidence interpretation

성신양회 is the second cement / construction-material positive.

The setup had real C30 relevance:

```text
cement and construction-material supplier
  -> construction material price / volume sensitivity
  -> fuel, electricity, freight, and raw-material cost sensitivity
  -> initial February spike and July rerating
```

The price path produced a meaningful MFE and did not become a hard failure. Still, the path also shows label risk: a one-day February spike and a later July spike can make the model over-promote the name if the cement spread and demand bridge is not current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 8,130 / close 8,120
2024-02-21: high 9,590 / close 8,770
2024-04-30: high 8,920 / close 8,870
2024-07-31: high 10,000 / close 9,110
2024-08-05: low 7,610 / close 7,910
2024-09-06: low 8,070 / close 8,100
2024-10-25: low 7,810 / close 7,900
```

Approximate path from entry close:

```text
entry_close: 8,120
peak_high: 10,000
MFE: +23.2%
worst_low_after_entry: 7,610
MAE: -6.3%
```

### Interpretation

This is a C30 positive with 4B / Green cap:

```text
Stage2-Actionable: valid if product spread, construction demand, input-cost, and cashflow bridge are explicit.
Stage3-Green: blocked unless fresh cement demand and margin evidence appears after the rerating.
Local 4B: monitor if spikes are event-label driven rather than margin-evidence driven.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  cement_material_relevance: high
  construction_demand_bridge: medium
  fuel_electricity_freight_bridge: medium
  price_confirmation: medium_high
  demand_inventory_bridge: weak_to_medium
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 7. Case 3 — 317400 자이에스앤디

```yaml
case_id: C30_R10L98_317400_2024_02_01
symbol: "317400"
name: "자이에스앤디"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4810
classification: watch_cap_housing_service_project_cashflow_label_without_strong_receivables_pf_margin_bridge
calibration_usable: true
```

### Evidence interpretation

자이에스앤디 is the housing-service / project-cashflow Watch cap.

The label is relevant:

```text
housing service / small construction service / residential project exposure
  -> housing-cycle and project-cashflow sensitivity
  -> receivables and PF/counterparty exposure
  -> low-PBR construction-service readthrough
```

But the February trigger did not validate Actionable or Green. MFE was shallow, and the stock later moved into a material drawdown zone. This means the housing-service label should remain Watch/Yellow unless project exposure, receivables, cash collection, PF exposure, and margin evidence are explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,810 / close 4,810
2024-02-02: high 4,885 / close 4,860
2024-03-13: low 4,225 / close 4,230
2024-04-15: low 4,045 / close 4,045
2024-08-05: low 4,040 / close 4,150
2024-09-09: low 3,950 / close 4,065
2024-11-04: low 3,600 / close 3,750
```

Approximate path from entry close:

```text
entry_close: 4,810
peak_high_after_entry: 4,890
MFE: +1.7%
worst_low_after_entry: 3,600
MAE: -25.2%
```

### Interpretation

This is a C30 Watch/Yellow cap:

```text
Stage2-Watch: valid from housing-service and construction-cycle relevance.
Stage2-Actionable: blocked unless project exposure, receivables, cash collection, PF/counterparty, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross the hard threshold.
Short listing caveat: yes versus old construction names.
```

The lesson is that housing-service relevance is not project cash collection.

### Stress-test components

```text
raw_component_score_proxy:
  housing_service_relevance: high
  project_cashflow_bridge: weak
  receivables_collection_bridge: weak
  pf_counterparty_bridge: weak_to_medium
  margin_fcf_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
cement_building_material_case_count: 2
housing_service_project_cashflow_case_count: 1
construction_material_spread_case_count: 2
housing_pf_cashflow_bridge_missing_count: 1
input_cost_energy_freight_bridge_missing_count: 1
project_cashflow_receivables_bridge_missing_count: 1
row_presence_or_old_corporate_action_caveat_count: 3
short_listing_or_segment_trust_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C30 cement / housing-service grid:

```text
300720 한일시멘트:
  cement / building-material positive;
  meaningful MFE and low MAE, but Green requires fresh volume, input-cost, inventory, and margin evidence.

004980 성신양회:
  cement / construction-material positive;
  meaningful MFE and controlled MAE, but 4B/Green cap required if input-cost and demand evidence are stale.

317400 자이에스앤디:
  housing-service / project-cashflow relevance;
  shallow MFE and material MAE, Watch/Yellow cap.
```

Shared rule:

```text
C30 is not "construction-material or housing-service label is relevant."
C30 is "construction volume, price-cost spread, receivables, PF/counterparty exposure, working capital, cash collection, and margin/FCF conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L98_300720_2024_02_01","scheduled_round":"R10","scheduled_loop":98,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"300720","name":"한일시멘트","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12100,"peak_high":15700,"peak_date":"2024-08-23","worst_low_after_entry":11770,"worst_low_after_entry_date":"2024-03-11","mfe_pct":29.8,"mae_pct":-2.7,"classification":"positive_cement_building_material_volume_input_cost_margin_bridge_with_green_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"cement_building_material_volume_selling_price_input_cost_inventory_working_capital_margin_bridge","residual_error":"cement_material_positive_requires_green_cap_after_large_mfe_without_refreshed_volume_input_cost_inventory_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_cement_volume_input_cost_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C30_R10L98_004980_2024_02_01","scheduled_round":"R10","scheduled_loop":98,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"004980","name":"성신양회","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8120,"peak_high":10000,"peak_date":"2024-07-31","worst_low_after_entry":7610,"worst_low_after_entry_date":"2024-08-05","mfe_pct":23.2,"mae_pct":-6.3,"classification":"positive_cement_material_spread_rerating_with_4b_green_cap_if_input_cost_demand_evidence_stale","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"cement_construction_material_spread_input_cost_freight_energy_demand_cashflow_margin_bridge","residual_error":"construction_material_spike_can_overpromote_without_fresh_input_cost_demand_cashflow_margin_evidence","shadow_rule_candidate":"preserve_cement_material_positive_but_attach_green_cap_after_mfe_if_spread_margin_evidence_is_stale"}
{"row_type":"case","case_id":"C30_R10L98_317400_2024_02_01","scheduled_round":"R10","scheduled_loop":98,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"317400","name":"자이에스앤디","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4810,"peak_high":4890,"peak_date":"2024-07-26","worst_low_after_entry":3600,"worst_low_after_entry_date":"2024-11-04","mfe_pct":1.7,"mae_pct":-25.2,"classification":"watch_cap_housing_service_project_cashflow_label_without_strong_receivables_pf_margin_bridge","calibration_usable":true,"short_listing_or_segment_trust_caveat":true,"evidence_family":"housing_service_project_cashflow_label_without_receivables_pf_counterparty_margin_bridge","residual_error":"housing_service_relevance_can_overpromote_without_project_receivables_cash_collection_pf_margin_evidence","shadow_rule_candidate":"cap_housing_service_label_at_watch_yellow_if_mfe_shallow_and_project_cashflow_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":98,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_BUILDING_MATERIALS_HOUSING_SERVICE_VOLUME_INPUT_COST_PF_CASHFLOW_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"cement_building_material_case_count":2,"housing_service_project_cashflow_case_count":1,"construction_material_spread_case_count":2,"housing_pf_cashflow_bridge_missing_count":1,"input_cost_energy_freight_bridge_missing_count":1,"project_cashflow_receivables_bridge_missing_count":1,"row_presence_or_old_corporate_action_caveat_count":3,"short_listing_or_segment_trust_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":98,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_CEMENT_HOUSING_MATERIALS_PROJECT_CASHFLOW_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 cement/building-material/housing-service cases, do not open Stage2-Actionable or Stage3-Green from cement, ready-mix, building-material, construction-material, housing-service, PF-stabilization, input-cost relief, low-PBR construction-material rerating, or one-week construction-material stock volume-spike labels alone. Require named end-market/region/project/customer channel, construction volume and order visibility, cement/ready-mix/material selling price, coal/electricity/fuel/freight/input-cost check, inventory and working-capital timing, housing-service receivables and cash collection, PF/developer/counterparty exposure, maintenance capex and balance-sheet trust, margin/FCF conversion, and post-trigger price survival. Cement/building-material positives with meaningful MFE may be capped Actionable when volume, input-cost, inventory, and margin bridge are explicit, but Green requires fresh evidence. Housing-service labels with shallow MFE and material MAE should cap at Watch/Yellow without project receivables, PF/counterparty, and cash collection evidence.","expected_effect":"Preserve true cement/building-material spread positives while reducing generic construction-material, housing-service, PF-stabilization, and low-PBR false positives where volume, input-cost, receivables, cash collection, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":98,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"cement_housing_materials_project_cashflow_margin_guard","contribution":"Adds two cement/building-material positives and one housing-service Watch cap to calibrate C30 construction volume, input-cost spread, inventory, working capital, receivables, PF/counterparty exposure, and margin/FCF requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_CEMENT_HOUSING_MATERIALS_PROJECT_CASHFLOW_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [cement, ready_mix, building_materials, construction_materials, housing_service, residential_project_service]:

  Do not open Stage3-Green from:
    - cement / ready-mix / building-material label alone
    - construction-material price hike or input-cost relief headline alone
    - housing-service / small construction contractor label alone
    - PF stabilization policy headline alone
    - regional construction demand headline alone
    - low-PBR construction-material rerating alone
    - one-week construction-material stock volume spike alone

  Require at least two of:
    - named end-market / region / project / customer channel
    - construction volume and order visibility
    - cement / ready-mix / material selling price
    - coal / electricity / fuel / freight / input-cost control
    - inventory and working-capital timing
    - housing-service receivables and cash collection
    - PF / developer / counterparty exposure check
    - maintenance capex and balance-sheet trust
    - margin / FCF conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the construction-material headline

  If MFE < 8% and MAE <= -25%:
    cap at Watch/Yellow and escalate to hard-4C if receivables/PF trust deteriorates.

  If MFE > 20% but volume/input-cost/margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If the case is housing-service rather than cement/material spread:
    require project receivables, cash collection, PF/counterparty, and margin evidence before Actionable.

  If row-presence or old corporate-action caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_98_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 cement/building-material/housing-service cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_CEMENT_HOUSING_MATERIALS_PROJECT_CASHFLOW_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks cement/building-material Green without construction volume, selling price, input-cost, inventory, working capital, and margin bridge,
   - preserves cement positives only with price survival and fresh volume / input-cost evidence,
   - caps housing-service labels at Watch/Yellow without project receivables, PF/counterparty, and cash collection evidence,
   - applies row-presence, old corporate-action, and short-listing trust caveats.

Expected next schedule:
completed_round = R10
completed_loop = 98
next_round = R11
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 98
next_round = R11
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
