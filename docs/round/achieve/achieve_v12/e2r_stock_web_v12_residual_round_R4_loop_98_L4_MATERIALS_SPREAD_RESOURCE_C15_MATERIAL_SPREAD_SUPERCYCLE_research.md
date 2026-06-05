# E2R Stock-Web v12 Residual Research — R4 / Loop 98

```yaml
scheduled_round: R4
scheduled_loop: 98
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE

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
rebar_steel_spread_case_count: 2
structural_steel_service_center_case_count: 1
scrap_energy_cost_bridge_missing_count: 2
demand_inventory_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
name_history_or_old_raw_discontinuity_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R4
completed_loop: 98
next_round: R5
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 98
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage:

```text
loop95: C15_MATERIAL_SPREAD_SUPERCYCLE
loop96: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop97: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

This run returns to C15 after the R4 branch cycle, but avoids the C15 top-covered names and recent R4 outputs.

Selected fine branch:

```text
rebar / construction steel / structural steel service center
scrap, electricity, energy, inventory timing, construction demand, utilization,
working capital, and margin bridge
vs generic steel/material spread label spike
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
104700 한국철강
084010 대한제강
008260 NI스틸
```

They avoid the C15 top-covered list and avoid recent R4 names:

```text
loop95 C15 avoid:
  001430, 005010, 002240

loop96 C16 avoid:
  006260, 000670, 011810

loop97 C17 avoid:
  014830, 009830, 298000

C15 top-covered avoid:
  103140, 012800, 025820, 004560, 021050, 001780
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
104700: same archetype, new symbol, rebar steel spread positive with large MFE and Green cap
084010: same archetype, new symbol, rebar/construction steel Watch cap after shallow initial MFE and material drawdown before later rerating
008260: same archetype, new symbol, structural steel/service-center hard-4C candidate after shallow MFE and high MAE
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
104700 한국철강
  profile: atlas/symbol_profiles/104/104700.json
  first_date: 2008-09-29
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,287
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2018-05-04
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

084010 대한제강
  profile: atlas/symbol_profiles/084/084010.json
  first_date: 2005-10-31
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 5,001
  non_tradable_zero_volume rows: 9
  corporate_action_candidate_dates:
    2009-03-11, 2026-01-05, 2026-01-26
  2024 entry~D+180 contamination: none
  caveat:
    old and future corporate-action candidate windows are outside selected 2024 validation window.

008260 NI스틸
  profile: atlas/symbol_profiles/008/008260.json
  name history:
    동성철강 -> NI테크 -> NI스틸
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,691
  non_tradable_zero_volume rows: 74
  corporate_action_candidate_dates:
    1997-12-04, 1999-01-29, 2001-03-30, 2004-04-20
  2024 entry~D+180 contamination: none
  caveat:
    historical name/raw-discontinuity and row-presence caveats exist outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C15 is about material spread and supercycle behavior. In this fine branch, the trigger is not simply "steel is strong." It is the spread between finished steel selling prices, scrap/iron input costs, electricity and energy costs, construction demand, inventory timing, and utilization.

The model can over-score:

```text
steel / rebar / structural steel label
construction steel demand headline
scrap price relief headline
China stimulus or infrastructure readthrough
low-PBR steel rerating
one-week steel-stock volume spike
late chase after a material-spread rerating
```

The C15 bridge must be stricter:

```text
steel / material-spread event
  -> named product and end-market
  -> input cost and output selling-price direction
  -> scrap / iron / electricity / energy-cost check
  -> utilization and inventory timing
  -> construction demand and customer order visibility
  -> working-capital burden
  -> export/import and FX risk where relevant
  -> margin / OP conversion
  -> balance-sheet and row/tradeability trust
  -> price survival after the first steel-label spike
```

A C15 steel-spread thesis is like a furnace. The flame is visible, but equity value appears only when the input charge, electricity bill, selling price, inventory timing, and customer demand leave a clean margin after the heat cools.

---

## 5. Case 1 — 104700 한국철강

```yaml
case_id: C15_R4L98_104700_2024_02_01
symbol: "104700"
name: "한국철강"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6970
classification: positive_rebar_steel_spread_inventory_margin_bridge_with_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

한국철강 is the constructive C15 rebar spread control.

The useful C15 read is not simply:

```text
철강주가 올랐다
```

It is:

```text
rebar / construction steel spread relevance
  -> finished steel price vs scrap/electricity cost
  -> construction demand and inventory timing
  -> utilization and working-capital discipline
  -> strong price confirmation into April/May
```

The forward path produced a large MFE with controlled early downside. This preserves positive classification. However, after the strong rerating, Green should remain capped unless product spread, scrap/electricity cost, construction demand, inventory, and margin evidence are fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,000 / close 6,970
2024-03-19: high 8,950 / close 8,470
2024-04-12: high 11,440 / close 11,440
2024-04-23: high 12,640 / close 12,600
2024-04-26: high 12,680 / close 11,740
2024-08-05: low 7,590 / close 7,700
2024-10-18: low 7,690 / close 7,850
2024-11-01: high 9,220 / close 9,220
```

Approximate path from entry close:

```text
entry_close: 6,970
peak_high: 12,680
MFE: +81.9%
worst_low_after_entry: 6,690
MAE: -4.0%
```

### Interpretation

This is a C15 positive with Green cap:

```text
Stage2-Actionable: possible if rebar spread, scrap/electricity cost, inventory timing, and construction-demand bridge are explicit.
Stage3-Green: blocked after +80% MFE unless fresh margin evidence appears.
Local 4B: monitor if price outruns spread and demand evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  rebar_steel_relevance: high
  product_spread_bridge: medium_high
  scrap_electricity_cost_bridge: medium_high
  construction_demand_bridge: medium
  inventory_working_capital_bridge: medium
  price_confirmation: very_high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 084010 대한제강

```yaml
case_id: C15_R4L98_084010_2024_02_01
symbol: "084010"
name: "대한제강"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 13480
classification: watch_cap_rebar_construction_steel_label_without_strong_incremental_spread_demand_margin_bridge_before_later_rerating
calibration_usable: true
```

### Evidence interpretation

대한제강 is the rebar / construction steel Watch cap.

The label is relevant:

```text
rebar / construction steel
  -> construction demand and material-spread optionality
  -> scrap and energy-cost spread sensitivity
```

But from the selected February trigger, the first phase did not validate Actionable/Green. MFE was shallow and the stock later moved into a material drawdown by August. A later September-November rerating should be treated as a refreshed event window unless the original spread/demand evidence is updated. This case therefore supports Watch/Yellow cap and 4B discipline.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 13,790 / close 13,480
2024-02-19: high 14,250 / close 14,100
2024-04-18: high 14,180 / close 13,840
2024-08-05: low 10,360 / close 10,950
2024-09-03: high 13,060 / close 12,950
2024-10-17: high 14,060 / close 13,980
2024-11-04: high 15,800 / close 15,000
```

Approximate first-phase path from entry close:

```text
entry_close: 13,480
peak_high_before_later_rerating: 14,250
MFE: +5.7%
worst_low_after_entry: 10,360
MAE: -23.1%
```

### Interpretation

This is a C15 Watch/Yellow cap:

```text
Stage2-Watch: valid from rebar / construction steel relevance.
Stage2-Actionable: blocked unless spread, construction demand, inventory, utilization, and margin bridge are explicit.
Stage3-Green: blocked for the February trigger.
Hard 4C: no, because MAE did not cross hard threshold.
Later event caveat: September-November rerating should be treated as a refreshed event window.
```

### Stress-test components

```text
raw_component_score_proxy:
  rebar_steel_label: high
  product_spread_bridge: weak_to_medium
  construction_demand_bridge: weak_to_medium
  scrap_energy_cost_bridge: weak_to_medium
  inventory_working_capital_bridge: weak
  price_confirmation_first_phase: shallow
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 008260 NI스틸

```yaml
case_id: C15_R4L98_008260_2024_02_01
symbol: "008260"
name: "NI스틸"
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5280
classification: hard_4c_candidate_structural_steel_service_center_label_without_spread_margin_survival
calibration_usable: true
```

### Evidence interpretation

NI스틸 is the hard C15 guardrail.

The label can fool the model:

```text
structural steel / steel service center
  -> construction material spread readthrough
  -> steel-stock sympathy
  -> small-cap material beta
```

But from the selected February entry, the forward path produced shallow MFE and then crossed a hard drawdown zone. The bridge from steel/material label to finished-steel spread, inventory timing, construction demand, utilization, and margin survival was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,460 / close 5,280
2024-02-02: high 5,570 / close 5,440
2024-04-17: low 4,380 / close 4,400
2024-08-05: low 3,705 / close 3,835
2024-10-25: low 3,735 / close 3,765
2024-10-31: low 3,650 / close 3,920
2024-11-08: low 3,765
```

Approximate path from entry close:

```text
entry_close: 5,280
peak_high_after_entry: 5,570
MFE: +5.5%
worst_low_after_entry: 3,650
MAE: -30.9%
```

### Interpretation

This is a hard C15 false-positive candidate:

```text
Stage2-Watch: possible from structural steel and service-center relevance.
Stage2-Actionable: blocked unless product spread, inventory cycle, demand, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and -30%+ MAE.
Row/name-history caveat: historical only, outside 2024 window.
```

The lesson is that steel label sympathy is not material-spread margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  structural_steel_service_center_label: high
  product_spread_bridge: weak
  inventory_timing_bridge: weak
  construction_demand_bridge: weak
  utilization_margin_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
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
rebar_steel_spread_case_count: 2
structural_steel_service_center_case_count: 1
scrap_energy_cost_bridge_missing_count: 2
demand_inventory_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
name_history_or_old_raw_discontinuity_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C15 steel-spread grid:

```text
104700 한국철강:
  rebar / steel spread positive;
  very large MFE and low MAE, but Green requires fresh spread and margin evidence.

084010 대한제강:
  rebar / construction steel relevance;
  shallow first-phase MFE and material MAE, Watch/Yellow cap with later-event separation.

008260 NI스틸:
  structural steel / service-center label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C15 is not "steel label is cyclically relevant."
C15 is "finished steel price, scrap/energy cost, utilization, inventory timing, construction demand, working capital, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C15_R4L98_104700_2024_02_01","scheduled_round":"R4","scheduled_loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE","symbol":"104700","name":"한국철강","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6970,"peak_high":12680,"peak_date":"2024-04-26","worst_low_after_entry":6690,"worst_low_after_entry_date":"2024-02-01","mfe_pct":81.9,"mae_pct":-4.0,"classification":"positive_rebar_steel_spread_inventory_margin_bridge_with_green_cap_after_large_mfe","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"rebar_steel_spread_finished_price_scrap_electricity_construction_demand_inventory_margin_bridge","residual_error":"positive_steel_spread_path_requires_green_cap_after_large_mfe_without_refreshed_scrap_energy_inventory_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_product_spread_inventory_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C15_R4L98_084010_2024_02_01","scheduled_round":"R4","scheduled_loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE","symbol":"084010","name":"대한제강","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":13480,"peak_high_first_phase":14250,"peak_date":"2024-02-19","worst_low_after_entry":10360,"worst_low_after_entry_date":"2024-08-05","mfe_pct":5.7,"mae_pct":-23.1,"classification":"watch_cap_rebar_construction_steel_label_without_strong_incremental_spread_demand_margin_bridge_before_later_rerating","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"rebar_construction_steel_label_without_incremental_scrap_energy_demand_inventory_margin_bridge","residual_error":"rebar_steel_relevance_can_overpromote_without_incremental_spread_and_construction_demand_evidence","shadow_rule_candidate":"cap_rebar_construction_steel_label_at_watch_yellow_if_mfe_shallow_and_spread_bridge_missing"}
{"row_type":"case","case_id":"C15_R4L98_008260_2024_02_01","scheduled_round":"R4","scheduled_loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE","symbol":"008260","name":"NI스틸","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5280,"peak_high":5570,"peak_date":"2024-02-02","worst_low_after_entry":3650,"worst_low_after_entry_date":"2024-10-31","mfe_pct":5.5,"mae_pct":-30.9,"classification":"hard_4c_candidate_structural_steel_service_center_label_without_spread_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"name_history_or_old_raw_discontinuity_caveat":true,"evidence_family":"structural_steel_service_center_label_without_finished_price_scrap_inventory_demand_margin_bridge","residual_error":"structural_steel_label_can_fail_when_spread_inventory_and_margin_bridge_missing","shadow_rule_candidate":"route_structural_steel_service_center_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":98,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_STRUCTURAL_STEEL_SERVICE_CENTER_SCRAP_ENERGY_SPREAD_MARGIN_BRIDGE_VS_STEEL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"rebar_steel_spread_case_count":2,"structural_steel_service_center_case_count":1,"scrap_energy_cost_bridge_missing_count":2,"demand_inventory_margin_bridge_missing_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"name_history_or_old_raw_discontinuity_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":98,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","rule_id":"C15_STEEL_SPREAD_SCRAP_ENERGY_INVENTORY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C15 material-spread/supercycle steel cases, do not open Stage2-Actionable or Stage3-Green from steel, rebar, structural steel, construction steel demand, scrap-price relief, China stimulus, infrastructure readthrough, low-PBR steel rerating, one-week steel-stock spike, or late chase after material-spread rerating labels alone. Require named product and end-market, input cost and output selling-price direction, scrap/iron/electricity/energy-cost check, utilization and inventory timing, construction demand and customer order visibility, working-capital burden control, export/import and FX risk where relevant, margin/OP conversion, balance-sheet and row/tradeability trust, and post-trigger price survival. Rebar steel positives with large MFE may be capped Actionable when spread, inventory, and margin bridge are explicit, but Green requires fresh evidence. Rebar/construction steel labels with shallow MFE and material MAE should cap at Watch/Yellow without stronger spread and demand evidence. Structural steel/service-center labels with shallow MFE and hard-zone MAE should route to hard-4C when finished-price, inventory, and margin bridge are missing.","expected_effect":"Preserve true steel spread positives while reducing generic rebar, structural steel, construction-demand, and low-PBR material-label false positives where scrap/energy cost, inventory, demand, working capital, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":98,"canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","residual_type":"steel_spread_scrap_energy_inventory_margin_guard","contribution":"Adds one rebar steel-spread positive, one rebar Watch cap, and one structural-steel hard-4C counterexample to calibrate C15 finished-steel price, scrap/electricity cost, construction demand, inventory timing, working capital, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C15_STEEL_SPREAD_SCRAP_ENERGY_INVENTORY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE
AND material_family in [rebar, construction_steel, structural_steel, steel_service_center]:

  Do not open Stage3-Green from:
    - steel / rebar / structural steel label alone
    - construction steel demand headline alone
    - scrap price relief headline alone
    - China stimulus or infrastructure readthrough alone
    - low-PBR steel rerating alone
    - one-week steel-stock volume spike alone
    - late chase after material-spread rerating alone

  Require at least two of:
    - named product and end-market
    - input cost and output selling-price direction
    - scrap / iron / electricity / energy-cost check
    - utilization and inventory timing
    - construction demand and customer order visibility
    - working-capital burden control
    - export/import and FX risk where relevant
    - margin / OP conversion
    - balance-sheet and row/tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the steel/material-spread headline

  If MFE < 8% and MAE <= -30%:
    route to C15 hard-4C candidate.

  If MFE > 25% but spread/margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is shallow and bridge is steel label only:
    cap at Watch/Yellow.

  If later rerating appears after first-phase weakness:
    create a new event window; do not retroactively validate the earlier trigger.

  Distinguish:
    - companies where finished steel price minus scrap/energy/inventory/working-capital burden becomes operating margin
    - from steel labels where demand, inventory, or cost bridge breaks.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_98_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C15 steel/material-spread cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C15_STEEL_SPREAD_SCRAP_ENERGY_INVENTORY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C15 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C15 cases agree, consider implementing a canonical guard that:
   - blocks steel/rebar/material-spread Green without product/end-market, scrap/energy cost, utilization, inventory, demand, working capital, and margin bridge,
   - preserves rebar positives only with price survival and fresh spread evidence,
   - caps shallow-MFE/material-MAE rebar labels at Watch/Yellow,
   - routes shallow-MFE/hard-zone-MAE structural steel labels to hard-4C,
   - separates later refreshed rerating windows from earlier weak triggers,
   - applies row-presence, old corporate-action, and name-history caveats when needed.

Expected next schedule:
completed_round = R4
completed_loop = 98
next_round = R5
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 98
next_round = R5
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
