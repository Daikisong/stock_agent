# E2R Stock-Web v12 Residual Research — R10 / Loop 99

```yaml
scheduled_round: R10
scheduled_loop: 99
large_sector_id: L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE

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

cement_material_spread_case_count: 1
glass_window_interior_material_case_count: 1
insulation_building_material_case_count: 1
construction_volume_input_cost_bridge_missing_count: 2
receivables_working_capital_margin_bridge_missing_count: 2
housing_demand_or_remodeling_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
short_listing_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R10
completed_loop: 99
next_round: R11
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R9_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R10
scheduled_loop = 99
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
```

R10 is the hard construction / real-estate / housing round. The selected canonical archetype is:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
```

Selected fine branch:

```text
cement / glass / window / insulation / interior building materials
construction volume, regional demand, remodeling and housing demand, product selling price,
coal/electricity/fuel/freight/input cost, inventory, receivables, working capital,
and margin / FCF bridge
vs generic construction-material / low-PBR building-material label spike
```

This deliberately avoids:
- C30 top-covered names:
  `002990`, `294870`, `375500`, `004960`, `013580`, `006360`
- R10 loop98 names:
  `300720`, `004980`, `317400`
- R10 loop97 names:
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
183190 아세아시멘트
344820 KCC글라스
007210 벽산
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
183190: same archetype, new symbol, cement / building-material spread capped positive.
344820: same archetype, new symbol, glass/window/interior material Watch cap with shallow MFE and missing remodeling-demand margin bridge.
007210: same archetype, new symbol, insulation / building-material hard-4C candidate after shallow MFE and hard-zone MAE.
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
183190 아세아시멘트
  profile: atlas/symbol_profiles/183/183190.json
  first_date: 2013-11-06
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,013
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2022-04-06
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

344820 KCC글라스
  profile: atlas/symbol_profiles/344/344820.json
  name history:
    케이씨씨글라스 -> KCC글라스
  first_date: 2020-01-21
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,493
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2020-12-18
  2024 entry~D+180 contamination: none
  caveat:
    short post-spinoff listing history and old corporate-action candidate outside selected 2024 validation window.

007210 벽산
  profile: atlas/symbol_profiles/007/007210.json
  name history:
    벽    산 / 벽산
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,677
  non_tradable_zero_volume rows: 87
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1997-02-18, 2012-05-10
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity and row-presence caveats require trust cap.
```

---

## 4. Archetype residual problem

C30 is about construction, PF, receivables, working capital, input-cost spread, and cash conversion. In this fine branch, the model should not treat every cement, glass, window, insulation, or interior-material label as a Green signal.

The model can over-score:

```text
cement / building-material label
glass / window / interior-material label
insulation / construction material label
remodeling or housing demand headline
input-cost relief headline
regional construction demand headline
low-PBR building-material rerating
one-week construction-material volume spike
```

The C30 bridge must be stricter:

```text
construction-material / housing-material event
  -> named product, region, end-market, project, or customer channel
  -> construction volume and order visibility
  -> selling-price / ASP / product mix
  -> coal / electricity / fuel / freight / raw-material cost check
  -> inventory and working-capital timing
  -> receivables and cash collection
  -> housing, remodeling, PF, developer, or counterparty exposure
  -> maintenance capex and balance-sheet trust
  -> margin / FCF conversion
  -> price survival after the first construction-material label spike
```

A C30 building-material thesis is like a cement truck or glass shipment leaving the plant. The product label gets the truck moving, but equity value appears only when real construction volume arrives, selling price covers fuel and freight, receivables become cash, and margin survives the housing-cycle balance-sheet stress.

---

## 5. Case 1 — 183190 아세아시멘트

```yaml
case_id: C30_R10L99_183190_2024_02_01
symbol: "183190"
name: "아세아시멘트"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10720
classification: capped_positive_cement_material_spread_volume_input_cost_margin_bridge
calibration_usable: true
```

### Evidence interpretation

아세아시멘트 is the capped positive in this set.

The useful C30 read is not simply:

```text
시멘트 / 건자재주가 움직였다
```

It is:

```text
cement and building-material spread relevance
  -> construction volume and regional shipment sensitivity
  -> selling price versus coal / electricity / fuel / freight cost
  -> inventory and receivables timing
  -> July-August price confirmation
```

The path produced meaningful but not extreme MFE, and drawdown stayed controlled. This supports capped positive classification. But the signal is not strong enough for ordinary Green unless cement volume, input-cost spread, inventory, receivables, and margin evidence are fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 10,770 / low 10,460 / close 10,720
2024-02-20: high 11,470 / close 11,300
2024-03-05: high 11,610 / close 11,600
2024-04-12: low 9,790 / close 9,800
2024-07-31: high 11,900 / close 11,580
2024-08-05: low 10,380 / close 10,400
2024-10-16: high 11,550 / close 11,550
```

Approximate path from entry close:

```text
entry_close: 10,720
peak_high: 11,900
MFE: +11.0%
worst_low_after_entry: 9,790
MAE: -8.7%
```

### Interpretation

This is a C30 capped positive:

```text
Stage2-Actionable: possible if cement volume, selling price, input cost, receivables, and margin bridge are explicit.
Stage3-Green: blocked without fresh volume and margin evidence.
Local 4B: monitor if the signal is only cement-label / low-PBR rerating.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  cement_material_relevance: high
  construction_volume_bridge: medium
  selling_price_input_cost_spread: medium
  receivables_cashflow_bridge: weak_to_medium
  margin_fcf_bridge: medium
  price_confirmation: modest_positive
  drawdown_penalty: low_to_medium
  green_cap: required
```

---

## 6. Case 2 — 344820 KCC글라스

```yaml
case_id: C30_R10L99_344820_2024_02_01
symbol: "344820"
name: "KCC글라스"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 40400
classification: watch_cap_glass_window_interior_material_label_without_strong_remodeling_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

KCC글라스 is the glass / window / interior-material Watch cap.

The setup had plausible C30 relevance:

```text
glass / window / interior building material
  -> remodeling and housing-material demand readthrough
  -> construction-material spread and input-cost sensitivity
  -> early February local spike
```

But the forward path did not validate Actionable or Green. MFE was shallow, and most of the year was range-bound or drifting. The bridge from glass/interior-material label to remodeling demand, channel order, selling price, input cost, receivables, and margin was not strong.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 40,750 / close 40,400
2024-02-08: high 43,350 / close 43,350
2024-02-20: high 43,800 / close 43,050
2024-08-05: low 39,000 / close 39,200
2024-10-16: low 38,750 / close 38,750
2024-10-30: low 38,350 / close 38,550
```

Approximate path from entry close:

```text
entry_close: 40,400
peak_high: 43,800
MFE: +8.4%
worst_low_after_entry: 38,350
MAE: -5.1%
```

### Interpretation

This is a C30 Watch / Yellow cap:

```text
Stage2-Watch: valid from glass/window/interior material relevance.
Stage2-Actionable: blocked unless remodeling/housing demand, order visibility, selling price, input cost, receivables, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because drawdown was controlled.
Short listing / spinoff trust cap: yes.
```

The lesson is that building-material relevance is not incremental cashflow or margin by itself.

### Stress-test components

```text
raw_component_score_proxy:
  glass_window_material_relevance: high
  remodeling_demand_bridge: weak_to_medium
  channel_order_bridge: weak
  selling_price_input_cost_bridge: weak_to_medium
  receivables_cashflow_bridge: weak
  price_confirmation: shallow
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 007210 벽산

```yaml
case_id: C30_R10L99_007210_2024_02_01
symbol: "007210"
name: "벽산"
canonical_archetype_id: C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id: CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 2480
classification: hard_4c_candidate_insulation_building_material_label_without_housing_volume_receivables_margin_survival
calibration_usable: true
```

### Evidence interpretation

벽산 is the insulation / building-material hard guardrail.

The label can fool the model:

```text
insulation / building material
  -> construction recovery or remodeling readthrough
  -> input-cost relief hope
  -> policy or low-PBR construction-material sympathy
```

But from the selected February entry, the path produced shallow MFE and then moved into a hard-zone drawdown by August. The bridge from insulation/building-material label to construction volume, remodeling demand, order visibility, receivables, cash collection, and margin survival was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 2,505 / close 2,480
2024-02-21: high 2,595 / close 2,570
2024-04-09: low 2,130 / close 2,130
2024-07-31: high 2,380 / close 2,175
2024-08-05: low 1,860 / close 1,960
2024-10-25: low 1,981 / close 1,981
```

Approximate path from entry close:

```text
entry_close: 2,480
peak_high: 2,595
MFE: +4.6%
worst_low_after_entry: 1,860
MAE: -25.0%
```

### Interpretation

This is a hard C30 false-positive candidate:

```text
Stage2-Watch: possible from insulation / building-material relevance.
Stage2-Actionable: blocked unless construction volume, remodeling demand, input-cost spread, receivables, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and hard-zone MAE.
Row / old corporate-action caveat: yes.
```

The lesson is that insulation-material relevance is not housing-volume cashflow survival.

### Stress-test components

```text
raw_component_score_proxy:
  insulation_building_material_label: high
  construction_volume_bridge: weak
  remodeling_demand_bridge: weak
  input_cost_bridge: weak_to_medium
  receivables_cashflow_bridge: weak
  margin_fcf_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: hard_zone
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
cement_material_spread_case_count: 1
glass_window_interior_material_case_count: 1
insulation_building_material_case_count: 1
construction_volume_input_cost_bridge_missing_count: 2
receivables_working_capital_margin_bridge_missing_count: 2
housing_demand_or_remodeling_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
short_listing_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C30 building-material grid:

```text
183190 아세아시멘트:
  cement / building-material capped positive;
  modest positive MFE and controlled MAE, but Green requires fresh volume/input-cost/receivables/margin evidence.

344820 KCC글라스:
  glass / window / interior material Watch cap;
  shallow MFE and controlled MAE, but no Actionable without remodeling/order/cashflow bridge.

007210 벽산:
  insulation / building-material label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C30 is not "construction-material label is relevant."
C30 is "construction volume, selling price, input cost, inventory, receivables, cash collection, working capital, and margin/FCF are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C30_R10L99_183190_2024_02_01","scheduled_round":"R10","scheduled_loop":99,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"183190","name":"아세아시멘트","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10720,"peak_high":11900,"peak_date":"2024-07-31","worst_low_after_entry":9790,"worst_low_after_entry_date":"2024-04-12","mfe_pct":11.0,"mae_pct":-8.7,"classification":"capped_positive_cement_material_spread_volume_input_cost_margin_bridge","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"cement_building_material_volume_selling_price_input_cost_inventory_receivables_margin_bridge","residual_error":"cement_material_positive_requires_green_cap_without_refreshed_volume_input_cost_receivables_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_cement_volume_input_cost_receivables_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C30_R10L99_344820_2024_02_01","scheduled_round":"R10","scheduled_loop":99,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"344820","name":"KCC글라스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":40400,"peak_high":43800,"peak_date":"2024-02-20","worst_low_after_entry":38350,"worst_low_after_entry_date":"2024-10-30","mfe_pct":8.4,"mae_pct":-5.1,"classification":"watch_cap_glass_window_interior_material_label_without_strong_remodeling_volume_margin_bridge","calibration_usable":true,"short_listing_or_old_corporate_action_caveat":true,"evidence_family":"glass_window_interior_material_label_without_remodeling_order_receivables_cashflow_margin_bridge","residual_error":"glass_window_material_relevance_can_overpromote_without_incremental_remodeling_volume_and_cashflow_evidence","shadow_rule_candidate":"cap_glass_window_interior_material_label_at_watch_yellow_if_mfe_shallow_and_margin_bridge_missing"}
{"row_type":"case","case_id":"C30_R10L99_007210_2024_02_01","scheduled_round":"R10","scheduled_loop":99,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","symbol":"007210","name":"벽산","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":2480,"peak_high":2595,"peak_date":"2024-02-21","worst_low_after_entry":1860,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.6,"mae_pct":-25.0,"classification":"hard_4c_candidate_insulation_building_material_label_without_housing_volume_receivables_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"insulation_building_material_label_without_construction_volume_remodeling_demand_receivables_margin_survival","residual_error":"insulation_building_material_label_can_fail_when_housing_volume_cashflow_margin_bridge_missing","shadow_rule_candidate":"route_insulation_building_material_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_cashflow_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R10","scheduled_loop":99,"large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","fine_archetype_id":"CEMENT_GLASS_INSULATION_INTERIOR_BUILDING_MATERIALS_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_VS_CONSTRUCTION_MATERIAL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"cement_material_spread_case_count":1,"glass_window_interior_material_case_count":1,"insulation_building_material_case_count":1,"construction_volume_input_cost_bridge_missing_count":2,"receivables_working_capital_margin_bridge_missing_count":2,"housing_demand_or_remodeling_bridge_missing_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"short_listing_or_name_history_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R10","scheduled_loop":99,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","rule_id":"C30_BUILDING_MATERIAL_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C30 cement/glass/window/insulation/interior building-material cases, do not open Stage2-Actionable or Stage3-Green from cement, building-material, glass/window, insulation, interior-material, remodeling demand, housing demand, input-cost relief, regional construction demand, low-PBR construction-material rerating, or one-week construction-material stock volume-spike labels alone. Require named product/region/end-market/project/customer channel, construction volume and order visibility, selling-price/ASP/product mix, coal/electricity/fuel/freight/raw-material cost check, inventory and working-capital timing, receivables and cash collection, housing/remodeling/PF/developer/counterparty exposure check, maintenance capex and balance-sheet trust, margin/FCF conversion, and post-trigger price survival. Cement positives with modest MFE may be capped Actionable when volume/input-cost/receivables/margin bridge is explicit, but Green requires fresh evidence. Glass/window/interior-material labels with shallow MFE should cap at Watch/Yellow without remodeling/order/cashflow bridge. Insulation/building-material labels with shallow MFE and hard-zone MAE should route to hard-4C when construction volume, receivables, and margin survival are missing.","expected_effect":"Preserve true cement/building-material spread positives while reducing generic glass/window, insulation, interior-material, remodeling, housing-demand, and low-PBR construction-material false positives where volume, input cost, receivables, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R10","scheduled_loop":99,"canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","residual_type":"building_material_volume_input_cost_receivables_margin_guard","contribution":"Adds one cement capped positive, one glass/window/interior Watch cap, and one insulation/building-material hard-4C counterexample to calibrate C30 construction volume, input-cost spread, receivables, cash collection, working capital, and margin/FCF requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C30_BUILDING_MATERIAL_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
AND company_type in [cement, glass, window, insulation, interior_material, building_material]:

  Do not open Stage3-Green from:
    - cement / building-material label alone
    - glass / window / interior-material label alone
    - insulation / construction-material label alone
    - remodeling or housing demand headline alone
    - input-cost relief headline alone
    - regional construction demand headline alone
    - low-PBR construction-material rerating alone
    - one-week construction-material volume spike alone

  Require at least two of:
    - named product / region / end-market / project / customer channel
    - construction volume and order visibility
    - selling price / ASP / product mix
    - coal / electricity / fuel / freight / raw-material cost control
    - inventory and working-capital timing
    - receivables and cash collection
    - housing / remodeling / PF / developer / counterparty exposure check
    - maintenance capex and balance-sheet trust
    - margin / FCF conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the construction-material headline

  If MFE < 8% and MAE <= -25%:
    route to C30 hard-4C candidate when receivables/cashflow/margin bridge is missing.

  If MFE is shallow and drawdown is controlled:
    cap at Watch/Yellow unless a company-specific order/cashflow/margin bridge appears.

  If MFE is modest but bridge evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If row-presence, old corporate-action, name-history, or short-listing caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R10_loop_99_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C30 cement/glass/insulation building-material cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C30_BUILDING_MATERIAL_VOLUME_INPUT_COST_RECEIVABLES_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C30 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C30 cases agree, consider implementing a canonical guard that:
   - blocks building-material Green without named product/channel, volume, selling price, input-cost, receivables, cash collection, and margin bridge,
   - preserves cement positives only with price survival and fresh volume/input-cost/margin evidence,
   - caps glass/window/interior material labels at Watch/Yellow without remodeling/order/cashflow bridge,
   - routes shallow-MFE/hard-MAE insulation/building-material labels to hard-4C,
   - applies row-presence, name-history, short-listing, and old corporate-action caveats.

Expected next schedule:
completed_round = R10
completed_loop = 99
next_round = R11
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R10
completed_loop = 99
next_round = R11
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
