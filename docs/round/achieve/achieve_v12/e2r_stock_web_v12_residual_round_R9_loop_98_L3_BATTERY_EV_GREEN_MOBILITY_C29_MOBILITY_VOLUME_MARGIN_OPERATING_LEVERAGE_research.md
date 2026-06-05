# E2R Stock-Web v12 Residual Research — R9 / Loop 98

```yaml
scheduled_round: R9
scheduled_loop: 98
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_secondary_candidate_count: 1
auto_chassis_driveline_case_count: 1
auto_seat_interior_supplier_case_count: 1
brake_friction_aftermarket_oem_case_count: 1
oem_volume_model_mix_bridge_missing_count: 2
cost_passthrough_margin_bridge_missing_count: 2
low_liquidity_or_row_presence_caveat_count: 3
name_history_or_old_corporate_action_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 98
next_round: R10
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_98_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 98
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R9 uses the mobility branch under L3 when the cases are auto / mobility / transport in nature. This run uses:

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Selected fine branch:

```text
auto seat / chassis-driveline / brake friction and related small-cap auto suppliers
OEM volume, model mix, production schedule, utilization, raw-material and labor pass-through,
warranty/logistics risk, low-liquidity row trust, working capital, and margin bridge
vs generic auto-parts label spike
```

This deliberately avoids:
- C29 top-covered names:
  `011210`, `000270`, `005380`, `005850`, `010690`, `018880`
- recent R9 loop88~97 outputs:
  `002350`, `009900`, `012860`,
  `025540`, `073240`, `033530`,
  `091810`, `003490`, `089590`,
  `011200`, `028670`, `005880`,
  `012330`, `161390`, `204320`,
  `086280`, `002320`, `003280`,
  `092200`, `067570`, `024900`,
  `089860`, `381970`, `403550`,
  `200880`, `064960`, `053270`,
  `023800`, `122350`, `013520`

Selected symbols:

```text
010100 한국무브넥스
005710 대원산업
024120 KB오토시스
```

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

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
024120: same archetype, new symbol, brake-friction / aftermarket-OEM supplier capped positive with 4B watch
010100: same archetype, new symbol, chassis/driveline label local burst followed by extreme MAE, local 4B with hard-4C secondary guard
005710: same archetype, new symbol, auto-seat / interior supplier Watch cap with shallow MFE and weak incremental volume-margin bridge
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
010100 한국무브넥스
  profile: atlas/symbol_profiles/010/010100.json
  name history:
    한국프랜지 / 한국프랜지공업 -> 한국무브넥스
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,725
  non_tradable_zero_volume rows: 39
  suspicious_ohlc_repaired_candidate rows: 1
  corporate_action_candidate_dates:
    1996-12-06, 2002-11-12, 2004-12-02, 2018-05-04
  2024 entry~D+180 contamination: none
  caveat:
    historical name/raw-discontinuity and row-presence caveats exist outside selected 2024 validation window.

005710 대원산업
  profile: atlas/symbol_profiles/005/005710.json
  first_date: 1996-07-26 in tradable profile
  raw_first_date: 1996-07-01
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,720
  non_tradable_zero_volume rows: 702
  corporate_action_candidate_dates:
    1996-08-27, 1997-12-23, 1998-01-16, 1999-06-03, 2004-11-24, 2011-04-07
  2024 entry~D+180 contamination: none
  caveat:
    high historical zero-volume count and old corporate-action windows require trust cap.

024120 KB오토시스
  profile: atlas/symbol_profiles/024/024120.json
  name history:
    한국베랄 -> KB오토시스
  first_date: 1996-07-26 in tradable profile
  raw_first_date: 1996-07-01
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,595
  non_tradable_zero_volume rows: 827
  corporate_action_candidate_dates:
    1999-11-08, 2000-03-08, 2009-06-30
  2024 entry~D+180 contamination: none
  caveat:
    high historical zero-volume count and old raw-discontinuity windows require trust cap.
```

---

## 4. Archetype residual problem

C29 is about mobility volume, model mix, utilization, and margin. In this branch, the model should not treat every auto supplier label as operating leverage.

The model can over-score:

```text
auto parts label
seat / interior supplier label
chassis / driveline / flange supplier label
brake-pad / friction material / aftermarket label
hybrid / EV model-mix headline
OEM volume recovery headline
low-PBR auto-parts rerating
one-week auto-parts volume spike
```

The C29 bridge must be stricter:

```text
auto / mobility / component event
  -> named OEM, model, platform, or supply channel
  -> customer volume and production schedule
  -> model mix and ASP
  -> utilization and fixed-cost absorption
  -> raw-material, resin, steel, copper, labor, and energy pass-through
  -> logistics, warranty, quality-claim, and recall risk
  -> inventory and working-capital burden
  -> aftermarket vs OEM channel mix
  -> margin / OP conversion
  -> row/tradeability trust where small-cap liquidity is thin
  -> price survival after the first auto-parts label spike
```

A C29 auto-supplier thesis is like a component sitting beside an OEM assembly line. The part may be essential, but equity value appears only when the model actually runs, the customer volume arrives, the supplier passes through cost inflation, warranty and logistics do not leak cash, and the margin line carries the volume.

---

## 5. Case 1 — 024120 KB오토시스

```yaml
case_id: C29_R9L98_024120_2024_02_01
symbol: "024120"
name: "KB오토시스"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4290
classification: capped_positive_brake_friction_aftermarket_oem_volume_margin_bridge_with_4b_watch_and_row_trust_cap
calibration_usable: true
```

### Evidence interpretation

KB오토시스 is the constructive but capped C29 case in this set.

The useful C29 read is not simply:

```text
자동차 부품주가 움직였다
```

It is:

```text
brake friction / replacement and OEM supplier relevance
  -> OEM and aftermarket channel mix optionality
  -> material-cost pass-through and product mix sensitivity
  -> gradual March-April price confirmation
  -> row/trust cap because liquidity and historical row caveats are high
```

The forward path produced a meaningful MFE without crossing the hard-failure zone. This supports a capped positive. However, the drawdown into August and the high historical row caveat mean Green should remain blocked unless OEM volume, aftermarket channel mix, raw-material pass-through, quality/warranty, and OP evidence refresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,350 / close 4,290
2024-02-19: high 4,740 / close 4,565
2024-03-08: high 5,040 / close 4,305
2024-04-25: high 4,995 / close 4,765
2024-04-30: high 5,210 / close 4,830
2024-08-05: low 3,350 / close 3,425
2024-08-23: high 4,570 / close 3,835
2024-09-23: high 4,270 / close 3,700
2024-11-01: close 3,600
```

Approximate path from entry close:

```text
entry_close: 4,290
peak_high_first_window: 5,210
MFE: +21.4%
worst_low_after_entry: 3,350
MAE: -21.9%
```

The late-August and September rebounds are not enough to override the February-to-August drawdown; they require refreshed OEM/aftermarket channel and margin evidence.

### Interpretation

This is a C29 capped positive with 4B watch:

```text
Stage2-Actionable: possible if OEM/aftermarket channel, volume, cost pass-through, and margin bridge are explicit.
Stage3-Green: blocked without fresh margin and row-trust evidence.
Local 4B: monitor because the path included material MAE before the later event spike.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  brake_friction_supplier_relevance: high
  oem_aftermarket_channel_bridge: medium
  customer_volume_bridge: weak_to_medium
  raw_material_pass_through_bridge: weak_to_medium
  warranty_quality_bridge: weak
  row_trust_caveat: high
  price_confirmation: medium_initial
  actionability_cap: capped_positive_4b_watch
```

---

## 6. Case 2 — 010100 한국무브넥스

```yaml
case_id: C29_R9L98_010100_2024_02_01
symbol: "010100"
name: "한국무브넥스"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6430
classification: local_burst_chassis_driveline_auto_parts_label_extreme_mae_4b_failure_with_hard_4c_secondary_guard
calibration_usable: true
```

### Evidence interpretation

한국무브넥스 is the chassis / driveline auto-parts local burst and high-MAE failure.

The setup had real C29 relevance:

```text
chassis / driveline / flange auto supplier
  -> OEM volume and model-mix readthrough
  -> low-PBR auto-parts event beta
  -> one-day February price spike
```

But the price path failed price survival badly. This is the classic C29 failure: the component label made a short MFE, yet the bridge from customer volume, model mix, cost pass-through, warranty/logistics, and margin did not persist. Because the later MAE is extreme, the case deserves a 4B overlay and a secondary hard-4C guard for future late or label-only entries.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,700 / close 6,430
2024-02-02: high 7,890 / close 7,250
2024-03-12: low 5,490 / close 5,520
2024-04-17: low 4,640 / close 4,670
2024-08-05: low 3,200 / close 3,445
2024-09-06: low 3,395 / close 3,555
2024-10-24: low 3,360 / close 3,415
```

Approximate path from entry close:

```text
entry_close: 6,430
peak_high: 7,890
MFE: +22.7%
worst_low_after_entry: 3,200
MAE: -50.2%
```

### Interpretation

This is a C29 local burst / high-MAE 4B failure:

```text
Stage2-Watch: valid from chassis/driveline supplier relevance.
Stage2-Actionable: blocked unless OEM model, production schedule, customer volume, pass-through, and margin bridge are explicit.
Stage3-Green: blocked after extreme MAE.
Local 4B: required.
Hard 4C secondary guard: future entries with shallow MFE or stale evidence should be routed to hard 4C quickly.
```

### Stress-test components

```text
raw_component_score_proxy:
  chassis_driveline_relevance: high
  oem_volume_bridge: weak_to_medium
  model_mix_bridge: weak_to_medium
  cost_pass_through_bridge: weak
  warranty_logistics_bridge: weak
  row_trust_caveat: medium
  price_confirmation: high_initial
  later_margin_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 005710 대원산업

```yaml
case_id: C29_R9L98_005710_2024_02_01
symbol: "005710"
name: "대원산업"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6520
classification: watch_cap_auto_seat_interior_supplier_label_without_strong_incremental_oem_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

대원산업 is the seat / interior supplier Watch cap.

The label is relevant:

```text
auto seat / interior supplier
  -> OEM production volume readthrough
  -> model mix and fixed-cost absorption optionality
```

But the February trigger did not validate Actionable or Green. MFE was shallow, liquidity was thin, and the later drawdown was material. The price path says the model should not promote a seat/interior supplier label without explicit OEM program, volume, utilization, pass-through, working-capital, and OP evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 6,520 / close 6,520
2024-02-02: high 6,770 / close 6,610
2024-04-24: high 6,920 / close 6,510
2024-08-05: low 5,570 / close 5,570
2024-09-09: low 5,740 / close 5,780
2024-11-01: high 6,770 / close 5,850
```

Approximate path from entry close:

```text
entry_close: 6,520
peak_high: 6,920
MFE: +6.1%
worst_low_after_entry: 5,570
MAE: -14.6%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from auto-seat and interior supplier relevance.
Stage2-Actionable: blocked unless named OEM/model, volume, utilization, material/labor pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MAE did not cross hard threshold.
Row/liquidity caveat: yes.
```

The lesson is that a stable component supplier label is not incremental operating leverage by itself.

### Stress-test components

```text
raw_component_score_proxy:
  auto_seat_interior_relevance: high
  named_oem_model_bridge: weak_to_medium
  volume_utilization_bridge: weak
  raw_material_labor_pass_through_bridge: weak
  op_margin_bridge: weak_to_medium
  row_trust_caveat: high
  price_confirmation: shallow
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_secondary_candidate_count: 1
auto_chassis_driveline_case_count: 1
auto_seat_interior_supplier_case_count: 1
brake_friction_aftermarket_oem_case_count: 1
oem_volume_model_mix_bridge_missing_count: 2
cost_passthrough_margin_bridge_missing_count: 2
low_liquidity_or_row_presence_caveat_count: 3
name_history_or_old_corporate_action_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C29 auto-supplier grid:

```text
024120 KB오토시스:
  brake-friction / aftermarket-OEM supplier capped positive;
  meaningful MFE and material MAE, 4B watch and row-trust cap.

010100 한국무브넥스:
  chassis/driveline auto-parts local burst failed;
  meaningful MFE first, then extreme MAE, local 4B with hard-4C secondary guard.

005710 대원산업:
  auto-seat / interior supplier relevance;
  shallow MFE and material drawdown, Watch/Yellow cap.
```

Shared rule:

```text
C29 is not "auto-parts label is relevant."
C29 is "named OEM/model, production schedule, customer volume, model mix, cost pass-through, warranty/logistics, working capital, and OP margin conversion are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L98_024120_2024_02_01","scheduled_round":"R9","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"024120","name":"KB오토시스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4290,"peak_high_first_window":5210,"peak_date":"2024-04-30","worst_low_after_entry":3350,"worst_low_after_entry_date":"2024-08-05","mfe_pct":21.4,"mae_pct":-21.9,"classification":"capped_positive_brake_friction_aftermarket_oem_volume_margin_bridge_with_4b_watch_and_row_trust_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"brake_friction_aftermarket_oem_channel_volume_cost_pass_through_warranty_margin_bridge","residual_error":"brake_friction_supplier_positive_requires_4b_row_trust_cap_without_refreshed_oem_aftermarket_margin_evidence","shadow_rule_candidate":"preserve_brake_friction_positive_but_cap_green_when_row_trust_and_cost_pass_through_evidence_are_stale"}
{"row_type":"case","case_id":"C29_R9L98_010100_2024_02_01","scheduled_round":"R9","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"010100","name":"한국무브넥스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6430,"peak_high":7890,"peak_date":"2024-02-02","worst_low_after_entry":3200,"worst_low_after_entry_date":"2024-08-05","mfe_pct":22.7,"mae_pct":-50.2,"classification":"local_burst_chassis_driveline_auto_parts_label_extreme_mae_4b_failure_with_hard_4c_secondary_guard","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"name_history_or_old_raw_discontinuity_caveat":true,"evidence_family":"chassis_driveline_auto_parts_label_without_sustained_oem_volume_model_mix_cost_pass_through_margin_survival","residual_error":"chassis_driveline_label_can_create_mfe_but_fail_green_when_oem_volume_and_margin_bridge_break","shadow_rule_candidate":"classify_meaningful_mfe_then_extreme_mae_chassis_driveline_cases_as_local_4b_with_hard_4c_secondary_guard"}
{"row_type":"case","case_id":"C29_R9L98_005710_2024_02_01","scheduled_round":"R9","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"005710","name":"대원산업","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6520,"peak_high":6920,"peak_date":"2024-04-24","worst_low_after_entry":5570,"worst_low_after_entry_date":"2024-08-05","mfe_pct":6.1,"mae_pct":-14.6,"classification":"watch_cap_auto_seat_interior_supplier_label_without_strong_incremental_oem_volume_margin_bridge","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"auto_seat_interior_supplier_label_without_named_oem_model_volume_utilization_cost_pass_through_margin_bridge","residual_error":"auto_seat_supplier_relevance_can_overpromote_without_incremental_oem_volume_and_margin_evidence","shadow_rule_candidate":"cap_auto_seat_interior_supplier_label_at_watch_yellow_if_mfe_shallow_and_volume_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":98,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_SEAT_CHASSIS_BRAKE_FRICTION_OEM_VOLUME_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_secondary_candidate_count":1,"auto_chassis_driveline_case_count":1,"auto_seat_interior_supplier_case_count":1,"brake_friction_aftermarket_oem_case_count":1,"oem_volume_model_mix_bridge_missing_count":2,"cost_passthrough_margin_bridge_missing_count":2,"low_liquidity_or_row_presence_caveat_count":3,"name_history_or_old_corporate_action_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":98,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_AUTO_SUPPLIER_OEM_VOLUME_COST_PASSTHROUGH_OP_MARGIN_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 auto-supplier cases, do not open Stage2-Actionable or Stage3-Green from auto parts, seat/interior supplier, chassis/driveline/flange supplier, brake/friction/aftermarket supplier, hybrid/EV model-mix, OEM volume recovery, low-PBR auto-parts rerating, or one-week auto-parts volume-spike labels alone. Require named OEM/model/platform/channel, customer volume and production schedule, model mix and ASP, utilization and fixed-cost absorption, raw-material/resin/steel/copper/labor/energy cost pass-through, logistics/warranty/quality-claim/recall risk control, inventory and working-capital burden containment, aftermarket vs OEM channel mix, margin/OP conversion, row/tradeability trust for thin-liquidity names, and post-trigger price survival. Brake/friction positives with meaningful MFE may be capped Actionable when OEM/aftermarket channel and margin bridge are explicit, but Green requires fresh evidence and row-trust cap. Chassis/driveline labels with meaningful MFE followed by extreme MAE should remain local 4B and receive hard-4C secondary guard when evidence is stale. Seat/interior supplier labels with shallow MFE should cap at Watch/Yellow without incremental OEM volume and pass-through evidence.","expected_effect":"Preserve true auto-supplier operating-leverage positives while reducing generic seat, chassis, brake/friction, low-PBR auto-parts, and small-cap label false positives where OEM volume, model mix, cost pass-through, warranty/logistics, working capital, and OP evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":98,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"auto_supplier_oem_volume_cost_passthrough_op_margin_trust_guard","contribution":"Adds one brake/friction capped positive, one chassis/driveline local 4B failure, and one auto-seat Watch cap to calibrate C29 OEM volume, model mix, utilization, cost pass-through, warranty/logistics, row trust, working capital, and OP margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_AUTO_SUPPLIER_OEM_VOLUME_COST_PASSTHROUGH_OP_MARGIN_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [auto_seat, interior_supplier, chassis_driveline, flange_supplier, brake_friction, aftermarket_oem_supplier]:

  Do not open Stage3-Green from:
    - auto-parts label alone
    - seat / interior supplier label alone
    - chassis / driveline / flange supplier label alone
    - brake-pad / friction material / aftermarket label alone
    - hybrid / EV model-mix headline alone
    - OEM volume recovery headline alone
    - low-PBR auto-parts rerating alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - named OEM / model / platform / supply channel
    - customer volume and production schedule
    - model mix and ASP
    - utilization and fixed-cost absorption
    - raw-material / resin / steel / copper / labor / energy cost pass-through
    - logistics / warranty / quality-claim / recall-risk containment
    - inventory / working-capital burden control
    - aftermarket vs OEM channel mix
    - margin / OP conversion
    - row / tradeability trust for thin-liquidity names
    - low-MAE post-trigger price survival
    - fresh evidence after the auto-parts headline

  If MFE < 8% and MAE <= -30%:
    route to C29 hard-4C candidate.

  If MFE > 15% but later MAE is material:
    preserve as capped positive or local 4B, not Green, unless customer-volume and margin evidence appears.

  If MAE <= -45% after an initial auto-parts event burst:
    attach a hard-4C secondary guard for future stale/late entries.

  If MFE is shallow and bridge is supplier-label only:
    cap at Watch/Yellow.

  If row-presence, old corporate-action, or name-history caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.

  Distinguish:
    - suppliers where OEM volume, channel mix, and pass-through become OP
    - from auto-parts labels where material cost, warranty, logistics, liquidity, or working capital breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 auto supplier cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_AUTO_SUPPLIER_OEM_VOLUME_COST_PASSTHROUGH_OP_MARGIN_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 cases agree, consider implementing a canonical guard that:
   - blocks auto-supplier Green without named OEM/model/channel, production schedule, volume, model mix, pass-through, warranty/logistics, and OP bridge,
   - preserves brake/friction positives only with price survival and fresh OEM/aftermarket margin evidence,
   - treats meaningful-MFE/extreme-MAE chassis/driveline labels as local 4B with hard-4C secondary guard,
   - caps shallow-MFE seat/interior supplier labels at Watch/Yellow,
   - applies row-presence, old corporate-action, and name-history trust caveats.

Expected next schedule:
completed_round = R9
completed_loop = 98
next_round = R10
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 98
next_round = R10
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
