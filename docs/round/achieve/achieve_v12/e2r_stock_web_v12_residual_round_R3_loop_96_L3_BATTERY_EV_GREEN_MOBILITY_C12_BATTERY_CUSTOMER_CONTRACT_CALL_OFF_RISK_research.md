# E2R Stock-Web v12 Residual Research — R3 / Loop 96

```yaml
scheduled_round: R3
scheduled_loop: 96
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL

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
cross_theme_confound_caveat_count: 1
large_cap_customer_calloff_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R3
completed_loop: 96
next_round: R4
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R2_loop_96_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R3
scheduled_loop = 96
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R3 hard gate requires:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

Recent R3 branch usage:

```text
loop92: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
loop93: C14_EV_DEMAND_SLOWDOWN_4B_4C
loop94: C13_BATTERY_JV_UTILIZATION_AMPC_IRA
loop95: C11_BATTERY_ORDERBOOK_RERATING
```

This run returns to C12 after the R3 branch cycle, but avoids the C12 top-covered names and uses a different fine branch:

```text
copper foil / cathode material / large chemical battery exposure
customer call-off, delivery, pass-through, and margin bridge
vs battery contract label reversal
```

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
011790 SKC
005070 코스모신소재
051910 LG화학
```

They avoid the C12 top-covered list and avoid recent R3 loop92~95 names:

```text
loop92 avoid: 078600, 066970, 361610
loop93 avoid: 014820, 336370, 222080
loop94 avoid: 121600, 393890, 450080
loop95 avoid: 008730, 006110, 277880
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
011790: same archetype, new symbol, copper-foil / battery-material exposure positive but with cross-theme confound cap
005070: same archetype, new symbol, cathode-material customer-demand local burst followed by high-MAE 4B failure
051910: same archetype, new symbol, large chemical / battery-material late chase hard-4C after call-off and demand bridge failed
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
011790 SKC
  profile: atlas/symbol_profiles/011/011790.json
  first_date: 1997-07-18
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,105
  non_tradable_zero_volume rows: 11
  corporate_action_candidate_dates:
    1998-01-03, 2001-12-21
  2024 entry~D+180 contamination: none

005070 코스모신소재
  profile: atlas/symbol_profiles/005/005070.json
  name history:
    새한미디어 until 2011-04-11
    코스모신소재 from 2011-04-12
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,706
  non_tradable_zero_volume rows: 58
  corporate_action_candidate_dates:
    historical only, latest 2019-11-13
  2024 entry~D+180 contamination: none
  caveat:
    historical row/corporate-action caveats exist outside the selected 2024 validation window.

051910 LG화학
  profile: atlas/symbol_profiles/051/051910.json
  first_date: 2001-04-25
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,110
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C12 is about battery customer contracts, call-off risk, delivery conversion, and margin survival. It is not a generic "battery material contract" or "large customer exposure" label.

The model can over-score:

```text
long-term battery supply agreement
copper foil / cathode / precursor / separator / electrolyte material label
major cell-maker customer exposure
capacity expansion headline
EV demand recovery hope
one-week battery-material volume spike
cross-theme rerating that is not actually battery call-off
```

The C12 bridge must be stricter:

```text
battery customer or supply contract event
  -> named customer and product
  -> enforceable order or call-off schedule
  -> delivery / shipment conversion
  -> customer inventory and demand risk
  -> ASP / mix / FX / raw-material pass-through
  -> working-capital and capex burden
  -> margin / OP conversion
  -> price survival after the first contract-label rally
```

A battery supply contract is like a factory waiting for the customer to pull pallets from the warehouse. The contract may look full, but C12 asks whether the customer actually calls off volume, whether the supplier ships on time, whether raw material cost is passed through, and whether margin survives the pull.

---

## 5. Case 1 — 011790 SKC

```yaml
case_id: C12_R3L96_011790_2024_02_01
symbol: "011790"
name: "SKC"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 76900
classification: positive_copper_foil_battery_material_exposure_with_cross_theme_confound_and_green_cap
calibration_usable: true
```

### Evidence interpretation

SKC is the constructive control, but with a cross-theme cap.

The useful C12 read is not simply:

```text
배터리 소재주가 강하다
```

It is:

```text
copper foil / battery material exposure
  -> customer call-off and delivery optionality
  -> raw-material pass-through and margin bridge
  -> strong price confirmation
```

The stock produced an extraordinary forward MFE from the February entry. However, the magnitude and timing also require cross-theme caution. The positive should not automatically imply that battery customer call-off alone explained the rerating. C12 should preserve the positive price path, but cap Green unless company-specific call-off, customer shipment, and battery-margin evidence is current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 76,900
2024-03-19: high 127,300 / close 123,800
2024-04-08: high 147,500 / close 145,300
2024-07-24: high 147,500 / close 143,200
2024-09-26: high 146,900 / close 146,900
2024-10-14: high 171,400 / close 160,200
2024-10-25: low 139,600 / close 140,000
```

Approximate path from entry close:

```text
entry_close: 76,900
peak_high: 171,400
MFE: +122.9%
worst_low_after_entry: 74,400
MAE: -3.3%
```

### Interpretation

This is a C12 positive with cross-theme cap:

```text
Stage2-Actionable: possible if customer/product, call-off schedule, delivery, and margin bridge are explicit.
Stage3-Green: blocked unless the battery-specific call-off and margin bridge is refreshed.
Local 4B: monitor after extreme MFE, especially if non-battery catalyst or cross-theme rerating dominates.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  battery_material_relevance: medium_high
  copper_foil_customer_bridge: medium
  calloff_delivery_bridge: weak_to_medium
  margin_pass_through_bridge: weak_to_medium
  price_confirmation: very_high
  cross_theme_confound: high
  green_cap: required
```

---

## 6. Case 2 — 005070 코스모신소재

```yaml
case_id: C12_R3L96_005070_2024_02_01
symbol: "005070"
name: "코스모신소재"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 139900
classification: local_burst_cathode_material_customer_demand_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

코스모신소재 is the cathode-material local-burst / high-MAE case.

The setup had real battery-material relevance:

```text
cathode / battery material exposure
  -> customer demand and contract-readthrough
  -> early February battery-material rerating
  -> meaningful local MFE
```

But the later path failed price survival. The original trigger should not be pure hard-4C because meaningful MFE came first. It is a 4B failure: customer call-off, shipment, inventory, and margin evidence did not keep the rerating alive.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 139,900
2024-02-16: high 180,000 / close 175,800
2024-02-21: high 194,300 / close 184,500
2024-08-05: low 100,100 / close 106,800
2024-09-10: low 96,500 / close 96,500
2024-09-26: high 132,900 / close 132,400
2024-10-25: low 100,700 / close 101,000
```

Approximate path from entry close:

```text
entry_close: 139,900
peak_high: 194,300
MFE: +38.9%
worst_low_after_entry: 96,500
MAE: -31.0%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from cathode-material relevance.
Stage2-Actionable: possible only if named customer, call-off, delivery, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  cathode_material_relevance: high
  customer_contract_label: medium_high
  calloff_schedule_bridge: weak
  inventory_demand_risk: high
  raw_material_margin_bridge: weak_to_medium
  price_confirmation: high_initial
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 051910 LG화학

```yaml
case_id: C12_R3L96_051910_2024_02_16
symbol: "051910"
name: "LG화학"
canonical_archetype_id: C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
fine_archetype_id: COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL
trigger_date: 2024-02-16
entry_date: 2024-02-16
entry_price_basis: close
entry_price: 504000
classification: hard_4c_candidate_large_chemical_battery_material_late_chase_without_calloff_margin_survival
calibration_usable: true
```

### Evidence interpretation

LG화학 is the large-cap battery-material late-chase hard guardrail.

The setup can look safe:

```text
large chemical platform
battery material / cathode exposure
major customer and long-term demand label
large-cap quality and EV recovery hope
```

But from the selected late February entry, the stock produced only shallow incremental MFE and then fell into a severe drawdown. This is the exact C12 trap: a high-quality battery-exposed name does not become Actionable/Green unless the customer call-off, shipment, material-cost pass-through, and margin bridge are current.

### Price path

Key Stock-Web rows:

```text
2024-02-16: high 515,000 / close 504,000
2024-02-19: high 520,000 / close 508,000
2024-04-17: low 375,500 / close 375,500
2024-08-05: low 263,500 / close 272,500
2024-09-27: high 368,500 / close 357,500
2024-10-29: low 312,000 / close 318,500
```

Approximate path from late entry close:

```text
entry_close: 504,000
peak_high_after_entry: 520,000
MFE: +3.2%
worst_low_after_entry: 263,500
MAE: -47.7%
```

### Interpretation

This is a hard C12 false-positive:

```text
Stage2-Watch: possible from battery-material and large-chemical relevance.
Stage2-Actionable: blocked unless customer call-off, shipment, inventory, pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE after a late chase.
```

The lesson is that large-cap quality and battery exposure do not protect a stale contract/call-off thesis.

### Stress-test components

```text
raw_component_score_proxy:
  large_chemical_battery_exposure: high
  customer_contract_label: high
  incremental_calloff_bridge: weak
  material_pass_through_bridge: weak_to_medium
  price_confirmation_after_entry: failed
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
cross_theme_confound_caveat_count: 1
large_cap_customer_calloff_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C12 customer call-off grid:

```text
011790 SKC:
  battery-material/copper-foil positive price path;
  extreme MFE and low MAE, but cross-theme confound and battery-specific call-off evidence cap Green.

005070 코스모신소재:
  cathode-material customer-demand local burst;
  meaningful MFE first, then high MAE, local 4B failure.

051910 LG화학:
  large chemical / battery-material late chase failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C12 is not "battery customer contract label."
C12 is "customer call-off, delivery, inventory, pass-through, working capital, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C12_R3L96_011790_2024_02_01","scheduled_round":"R3","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL","symbol":"011790","name":"SKC","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76900,"peak_high":171400,"peak_date":"2024-10-14","worst_low_after_entry":74400,"worst_low_after_entry_date":"2024-02-01","mfe_pct":122.9,"mae_pct":-3.3,"classification":"positive_copper_foil_battery_material_exposure_with_cross_theme_confound_and_green_cap","calibration_usable":true,"cross_theme_confound_caveat":true,"evidence_family":"copper_foil_battery_material_customer_calloff_delivery_margin_bridge_with_cross_theme_confound","residual_error":"positive_price_path_must_not_auto_green_without_battery_specific_calloff_margin_evidence","shadow_rule_candidate":"preserve_positive_but_cap_green_when_cross_theme_rerating_may_dominate_battery_calloff_evidence"}
{"row_type":"case","case_id":"C12_R3L96_005070_2024_02_01","scheduled_round":"R3","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL","symbol":"005070","name":"코스모신소재","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":139900,"peak_high":194300,"peak_date":"2024-02-21","worst_low_after_entry":96500,"worst_low_after_entry_date":"2024-09-10","mfe_pct":38.9,"mae_pct":-31.0,"classification":"local_burst_cathode_material_customer_demand_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"cathode_material_customer_contract_label_without_sustained_calloff_inventory_margin_survival","residual_error":"battery_material_contract_label_can_create_mfe_but_fail_green_without_calloff_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_cathode_material_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C12_R3L96_051910_2024_02_16","scheduled_round":"R3","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL","symbol":"051910","name":"LG화학","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":504000,"peak_high":520000,"peak_date":"2024-02-19","worst_low_after_entry":263500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.2,"mae_pct":-47.7,"classification":"hard_4c_candidate_large_chemical_battery_material_late_chase_without_calloff_margin_survival","calibration_usable":true,"evidence_family":"large_chemical_battery_material_late_chase_without_customer_calloff_shipment_pass_through_margin_bridge","residual_error":"large_cap_battery_quality_can_fail_when_incremental_calloff_and_margin_bridge_missing","shadow_rule_candidate":"route_large_chemical_battery_material_late_chase_to_hard_4c_if_mfe_shallow_mae_large_and_calloff_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R3","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_CATHODE_MATERIAL_MAJOR_CHEMICAL_CUSTOMER_CALLOFF_DELIVERY_MARGIN_BRIDGE_VS_BATTERY_CONTRACT_LABEL_REVERSAL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"cross_theme_confound_caveat_count":1,"large_cap_customer_calloff_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R3","scheduled_loop":96,"canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","rule_id":"C12_CUSTOMER_CALLOFF_DELIVERY_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C12, do not open Stage2-Actionable or Stage3-Green from battery customer contract, copper foil, cathode material, precursor, separator, electrolyte, major cell-maker customer exposure, capacity expansion, EV recovery, or one-week battery-material volume spike labels alone. Require named customer and product, enforceable order or call-off schedule, delivery/shipment conversion, customer inventory and demand risk check, ASP/mix/FX/raw-material pass-through, working-capital and capex burden, margin/OP conversion, and post-trigger price survival. Positive price paths with possible cross-theme rerating should cap Green unless battery-specific call-off and margin evidence is current. Material names with meaningful MFE followed by high MAE should be local 4B, not Green. Large chemical or battery-material late chases with shallow MFE and high MAE should route to hard-4C when customer call-off and pass-through margin bridge are missing.","expected_effect":"Preserve true battery customer call-off positives while reducing contract-label, material-label, and large-cap battery-exposure false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R3","scheduled_loop":96,"canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","residual_type":"customer_calloff_delivery_passthrough_margin_guard","contribution":"Adds one copper-foil/battery-material positive with cross-theme cap, one cathode-material local 4B failure, and one large-chemical battery-material hard-4C counterexample to calibrate C12 call-off, shipment, pass-through, working-capital, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C12_CUSTOMER_CALLOFF_DELIVERY_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK:

  Do not open Stage3-Green from:
    - battery customer contract headline alone
    - copper foil / cathode / precursor / separator / electrolyte label alone
    - major cell-maker customer exposure alone
    - capacity expansion headline alone
    - EV demand recovery hope alone
    - one-week battery-material volume spike alone
    - cross-theme rerating that is not battery-specific call-off evidence

  Require at least two of:
    - named customer and product
    - enforceable order / firm supply agreement
    - call-off / delivery schedule
    - shipment conversion
    - customer inventory and demand risk control
    - ASP / mix / FX / raw-material pass-through
    - working-capital / capex burden containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the contract/customer headline

  If MFE < 8% and MAE < -35%:
    route to C12 hard-4C candidate.

  If MFE > 20% but later MAE < -30%:
    preserve as local 4B / event burst, not Green, unless current call-off and margin evidence appears.

  If MFE is extraordinary but the catalyst may be cross-theme:
    cap Green until battery-specific call-off evidence is proven.

  Distinguish:
    - enforceable contracts that become call-off, shipment, pass-through, and margin
    - from battery-material labels where customer demand or EV cycle breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R3_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C12 battery customer contract / call-off risk cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C12_CUSTOMER_CALLOFF_DELIVERY_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C12 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C12 cases agree, consider implementing a canonical guard that:
   - blocks battery-contract Green without customer/product, call-off, shipment, pass-through, and margin bridge,
   - preserves battery-material positives only with price survival and fresh execution evidence,
   - caps cross-theme rerating positives until battery-specific call-off evidence is proven,
   - treats meaningful-MFE/high-MAE material names as local 4B,
   - routes shallow-MFE/high-MAE large-cap battery late chases to hard-4C.

Expected next schedule:
completed_round = R3
completed_loop = 96
next_round = R4
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R3
completed_loop = 96
next_round = R4
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
