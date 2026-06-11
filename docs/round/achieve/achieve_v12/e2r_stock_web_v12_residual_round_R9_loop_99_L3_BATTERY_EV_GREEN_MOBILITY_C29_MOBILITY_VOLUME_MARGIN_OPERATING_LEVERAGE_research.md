# E2R Stock-Web v12 Residual Research — R9 / Loop 99

```yaml
scheduled_round: R9
scheduled_loop: 99
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE

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
vehicle_camera_electronics_case_count: 1
hydraulic_mobility_component_case_count: 1
drivetrain_powertrain_supplier_case_count: 1
oem_volume_model_mix_bridge_missing_count: 2
cost_passthrough_margin_bridge_missing_count: 2
customer_concentration_working_capital_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
rejected_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 99
next_round: R10
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_99_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 99
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R9 uses the mobility branch when the cases are auto / mobility / transport in nature. This run uses:

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

Selected fine branch:

```text
vehicle camera / automotive electronics / hydraulic and drivetrain components
OEM volume, model mix, production schedule, customer concentration,
raw material and labor cost pass-through, warranty/quality/logistics,
working capital, and OP margin bridge
vs generic auto / mobility / vehicle-electronics label spike
```

This deliberately avoids:
- C29 top-covered names:
  `011210`, `000270`, `005380`, `005850`, `010690`, `018880`
- recent R9 loop98 names:
  `024120`, `010100`, `005710`
- recent R9 loop88~97 names:
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
011070 LG이노텍
013570 디와이
122690 서진오토모티브
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
011070: same archetype, new symbol, vehicle camera / automotive electronics positive with Green cap.
013570: same archetype, new symbol, hydraulic / mobility component local 4B after modest MFE and material MAE.
122690: same archetype, new symbol, drivetrain / transmission supplier hard-4C candidate after moderate MFE and hard-zone MAE.
```

Rejected candidate:

```text
123040 엠에스오토텍:
  checked as an auto body / OEM volume candidate,
  but profile has 2024-08-30 corporate-action candidate.
  It is not used as a clean 2024 primary validation row in this file.
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
011070 LG이노텍
  profile: atlas/symbol_profiles/011/011070.json
  name history:
    엘지이노텍 -> LG이노텍
  first_date: 2008-07-24
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,335
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2009-07-16
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

013570 디와이
  profile: atlas/symbol_profiles/013/013570.json
  name history:
    동양기전 -> 디와이
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,726
  non_tradable_zero_volume rows: 39
  corporate_action_candidate_dates:
    1996-01-26, 1997-01-03, 2003-04-14, 2007-12-11, 2015-01-15, 2015-10-23
  2024 entry~D+180 contamination: none
  caveat:
    historical name/raw-discontinuity and row-presence caveats exist outside selected 2024 validation window.

122690 서진오토모티브
  profile: atlas/symbol_profiles/122/122690.json
  name history:
    신한스팩1호 -> 서진오토모티브
  first_date: 2010-05-25
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,815
  non_tradable_zero_volume rows: 60
  corporate_action_candidate_dates:
    2012-04-19, 2012-07-18, 2012-08-09, 2012-11-14, 2018-01-19
  2024 entry~D+180 contamination: none
  caveat:
    SPAC/name-history and row-presence caveats exist outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C29 is about mobility volume, model mix, utilization, and margin. In this fine branch, the model should not treat every vehicle-electronics, hydraulic, or drivetrain supplier label as operating leverage.

The model can over-score:

```text
auto / mobility label
vehicle camera or autonomous-driving electronics label
hydraulic / actuator / industrial-mobility component label
drivetrain / transmission / powertrain parts label
hybrid / EV / ADAS model-mix headline
OEM volume recovery headline
customer concentration or anchor-customer sympathy
one-week auto-parts volume spike
```

The C29 bridge must be stricter:

```text
auto / mobility / component event
  -> named OEM, model, platform, or supply channel
  -> customer volume and production schedule
  -> model mix and ASP
  -> utilization and fixed-cost absorption
  -> raw-material / resin / steel / copper / labor / energy cost pass-through
  -> logistics, warranty, quality-claim, and recall-risk control
  -> inventory and working-capital burden
  -> customer concentration and program rollover risk
  -> margin / OP conversion
  -> row/tradeability trust
  -> price survival after the first auto / mobility label spike
```

A C29 mobility-supplier thesis is like a camera module or drivetrain part waiting beside an OEM assembly line. The part can be technically important, but equity value appears only when the target model is actually produced, order volume arrives, the supplier passes through cost inflation, warranty/logistics do not leak cash, and OP margin carries the volume.

---

## 5. Case 1 — 011070 LG이노텍

```yaml
case_id: C29_R9L99_011070_2024_02_01
symbol: "011070"
name: "LG이노텍"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 192900
classification: positive_vehicle_camera_electronics_mobility_model_mix_operating_leverage_with_green_cap
calibration_usable: true
```

### Evidence interpretation

LG이노텍 is the constructive C29 vehicle-electronics positive in this set.

The useful C29 read is not simply:

```text
전장 / 카메라모듈 / 모빌리티 부품주가 강하다
```

It is:

```text
vehicle camera / electronics relevance
  -> model mix and premium device / vehicle-electronics optionality
  -> customer program and volume recovery
  -> utilization and margin leverage
  -> strong April-July price confirmation
```

The forward path produced a large MFE and avoided hard-zone drawdown. This preserves positive classification. However, after the large rerating, C29 Green should remain capped unless customer program, volume, model mix, cost pass-through, and margin evidence remain current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 193,600 / low 189,000 / close 192,900
2024-04-24: high 210,000 / close 209,000
2024-05-07: high 240,000 / close 239,500
2024-07-24: high 285,000 / close 274,500
2024-08-05: low 211,000 / close 217,500
2024-10-25: low 171,200 / close 172,300
```

Approximate path from entry close:

```text
entry_close: 192,900
peak_high: 285,000
MFE: +47.7%
worst_low_after_entry: 171,200
MAE: -11.2%
```

### Interpretation

This is a C29 positive with Green cap:

```text
Stage2-Actionable: possible if named customer/program, model mix, utilization, and margin bridge are explicit.
Stage3-Green: blocked after +45% MFE unless fresh model/program volume and margin evidence appears.
Local 4B: monitor if vehicle-electronics label price outruns margin proof.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  vehicle_camera_electronics_relevance: high
  customer_program_bridge: medium_high
  model_mix_asp_bridge: medium_high
  utilization_margin_bridge: medium
  cost_pass_through_bridge: medium
  customer_concentration_risk: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 013570 디와이

```yaml
case_id: C29_R9L99_013570_2024_02_01
symbol: "013570"
name: "디와이"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5760
classification: local_4b_hydraulic_mobility_component_label_without_sustained_oem_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

디와이 is the hydraulic / mobility component local 4B case.

The setup had real C29 relevance:

```text
hydraulic / actuator / mobility component
  -> industrial and vehicle-equipment volume readthrough
  -> customer program and model-mix optionality
  -> initial February price confirmation
```

However, the path did not sustain price survival. The stock produced modest MFE first and then moved into a material drawdown by August. This is not a hard 4C, but it should not become Green without OEM/program, utilization, pass-through, working-capital, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,780 / close 5,760
2024-02-29: high 6,400 / close 6,210
2024-04-16: high 5,940 / close 5,680
2024-08-05: low 4,275 / close 4,300
2024-09-19: high 5,490 / close 4,995
2024-10-25: low 4,465 / close 4,570
```

Approximate path from entry close:

```text
entry_close: 5,760
peak_high: 6,400
MFE: +11.1%
worst_low_after_entry: 4,275
MAE: -25.8%
```

### Interpretation

This is a C29 local 4B / Watch cap:

```text
Stage2-Watch: valid from hydraulic and mobility-component relevance.
Stage2-Actionable: possible only if customer program, volume, cost pass-through, and margin bridge are explicit.
Stage3-Green: blocked after material MAE.
Local 4B: required.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  hydraulic_mobility_component_relevance: high
  oem_program_bridge: weak_to_medium
  volume_utilization_bridge: weak_to_medium
  cost_pass_through_bridge: weak
  working_capital_bridge: weak
  price_confirmation: modest_initial
  drawdown_penalty: material
  local_4b_overlay: required
```

---

## 7. Case 3 — 122690 서진오토모티브

```yaml
case_id: C29_R9L99_122690_2024_02_01
symbol: "122690"
name: "서진오토모티브"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3370
classification: hard_4c_candidate_drivetrain_powertrain_supplier_label_without_oem_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

서진오토모티브 is the drivetrain / powertrain hard C29 guardrail.

The label can fool the model:

```text
drivetrain / transmission / powertrain supplier
  -> OEM volume and model-mix readthrough
  -> hybrid / EV / auto-parts recovery sympathy
  -> small-cap auto-parts event beta
```

The path produced moderate MFE first, but then crossed hard-zone drawdown by August. The bridge from auto-parts label to named OEM/model, customer volume, production schedule, cost pass-through, quality/warranty control, and OP margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,415 / close 3,370
2024-03-13: high 3,965 / close 3,845
2024-03-29: low 3,230 / close 3,230
2024-08-05: low 2,150 / close 2,300
2024-09-06: low 2,335 / close 2,400
2024-10-25: low 2,235 / close 2,265
```

Approximate path from entry close:

```text
entry_close: 3,370
peak_high: 3,965
MFE: +17.7%
worst_low_after_entry: 2,150
MAE: -36.2%
```

### Interpretation

This is a hard C29 false-positive candidate:

```text
Stage2-Watch: possible from drivetrain / powertrain supplier relevance.
Stage2-Actionable: blocked unless named OEM/model, production schedule, volume, pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by moderate MFE and hard-zone MAE.
SPAC/name-history and row-trust caveat: yes.
```

The lesson is that powertrain supplier relevance is not OEM-volume margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  drivetrain_powertrain_label: high
  oem_volume_bridge: weak_to_medium
  model_mix_bridge: weak_to_medium
  cost_pass_through_bridge: weak
  warranty_quality_bridge: weak
  working_capital_bridge: weak_to_medium
  price_confirmation: moderate_initial
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
vehicle_camera_electronics_case_count: 1
hydraulic_mobility_component_case_count: 1
drivetrain_powertrain_supplier_case_count: 1
oem_volume_model_mix_bridge_missing_count: 2
cost_passthrough_margin_bridge_missing_count: 2
customer_concentration_working_capital_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
rejected_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C29 mobility component grid:

```text
011070 LG이노텍:
  vehicle camera / automotive electronics positive;
  large MFE and non-hard MAE, but Green requires fresh customer program, model mix, utilization, and margin evidence.

013570 디와이:
  hydraulic / mobility component local 4B;
  modest MFE first, then material MAE, Watch/4B cap.

122690 서진오토모티브:
  drivetrain / powertrain supplier label failed;
  moderate MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C29 is not "auto/mobility supplier label is relevant."
C29 is "named OEM/model, program volume, model mix, cost pass-through, warranty/quality control, working capital, and OP margin are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L99_011070_2024_02_01","scheduled_round":"R9","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE","symbol":"011070","name":"LG이노텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":192900,"peak_high":285000,"peak_date":"2024-07-24","worst_low_after_entry":171200,"worst_low_after_entry_date":"2024-10-25","mfe_pct":47.7,"mae_pct":-11.2,"classification":"positive_vehicle_camera_electronics_mobility_model_mix_operating_leverage_with_green_cap","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"vehicle_camera_electronics_customer_program_model_mix_utilization_cost_pass_through_margin_bridge","residual_error":"vehicle_electronics_positive_requires_green_cap_after_large_mfe_without_refreshed_customer_program_model_mix_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_customer_program_model_mix_utilization_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C29_R9L99_013570_2024_02_01","scheduled_round":"R9","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE","symbol":"013570","name":"디와이","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5760,"peak_high":6400,"peak_date":"2024-02-29","worst_low_after_entry":4275,"worst_low_after_entry_date":"2024-08-05","mfe_pct":11.1,"mae_pct":-25.8,"classification":"local_4b_hydraulic_mobility_component_label_without_sustained_oem_volume_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"name_history_caveat":true,"evidence_family":"hydraulic_mobility_component_label_without_sustained_oem_program_volume_cost_pass_through_margin_bridge","residual_error":"hydraulic_mobility_component_label_can_create_mfe_but_fail_green_when_oem_volume_and_margin_bridge_missing","shadow_rule_candidate":"classify_modest_mfe_then_material_mae_hydraulic_mobility_cases_as_local_4b_or_watch_not_green"}
{"row_type":"case","case_id":"C29_R9L99_122690_2024_02_01","scheduled_round":"R9","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE","symbol":"122690","name":"서진오토모티브","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3370,"peak_high":3965,"peak_date":"2024-03-13","worst_low_after_entry":2150,"worst_low_after_entry_date":"2024-08-05","mfe_pct":17.7,"mae_pct":-36.2,"classification":"hard_4c_candidate_drivetrain_powertrain_supplier_label_without_oem_volume_margin_survival","calibration_usable":true,"spac_name_history_or_row_presence_caveat":true,"evidence_family":"drivetrain_powertrain_supplier_label_without_named_oem_model_production_schedule_cost_pass_through_margin_bridge","residual_error":"drivetrain_supplier_label_can_fail_when_oem_volume_and_margin_bridge_missing","shadow_rule_candidate":"route_drivetrain_powertrain_supplier_label_to_hard_4c_if_mfe_moderate_mae_hard_zone_and_oem_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":99,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"VEHICLE_CAMERA_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MODEL_MIX_COST_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_MOBILITY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"vehicle_camera_electronics_case_count":1,"hydraulic_mobility_component_case_count":1,"drivetrain_powertrain_supplier_case_count":1,"oem_volume_model_mix_bridge_missing_count":2,"cost_passthrough_margin_bridge_missing_count":2,"customer_concentration_working_capital_caveat_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"rejected_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":99,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_VEHICLE_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 mobility volume/margin cases involving vehicle electronics, hydraulic components, drivetrain/powertrain suppliers, and adjacent mobility components, do not open Stage2-Actionable or Stage3-Green from auto/mobility label, vehicle camera/autonomous-driving electronics label, hydraulic/actuator/industrial-mobility component label, drivetrain/transmission/powertrain parts label, hybrid/EV/ADAS model-mix headline, OEM volume recovery headline, customer concentration or anchor-customer sympathy, or one-week auto-parts volume spike alone. Require named OEM/model/platform/supply channel, customer volume and production schedule, model mix and ASP, utilization and fixed-cost absorption, raw-material/resin/steel/copper/labor/energy cost pass-through, logistics/warranty/quality-claim/recall risk control, inventory and working-capital burden containment, customer concentration and program rollover risk check, margin/OP conversion, row/tradeability trust, and post-trigger price survival. Vehicle electronics positives with large MFE may be capped Actionable when customer program, model mix, utilization, and margin bridge are explicit, but Green requires fresh evidence. Hydraulic/mobility component labels with modest MFE followed by material MAE should remain local 4B or Watch without refreshed OEM volume and margin evidence. Drivetrain/powertrain supplier labels with moderate MFE and hard-zone MAE should route to hard-4C when named OEM/model and cost-pass-through margin bridge are missing.","expected_effect":"Preserve true mobility operating-leverage positives while reducing generic vehicle-electronics, hydraulic-component, drivetrain/powertrain, customer-sympathy, and auto-label false positives where OEM volume, model mix, cost pass-through, working capital, warranty/quality, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"rejected_candidate","scheduled_round":"R9","scheduled_loop":99,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","symbol":"123040","name":"엠에스오토텍","reason":"Profile has 2024-08-30 corporate-action candidate; not used as a clean 2024 C29 primary validation row without adjusted-price review.","do_not_count_as_global_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":99,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"vehicle_electronics_hydraulic_drivetrain_oem_volume_margin_guard","contribution":"Adds one vehicle-electronics positive, one hydraulic/mobility local 4B case, and one drivetrain/powertrain hard-4C counterexample to calibrate C29 named OEM/model, program volume, model mix, cost pass-through, warranty/quality, working capital, and OP margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_VEHICLE_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [vehicle_camera_electronics, automotive_electronics, hydraulic_component, actuator_component, drivetrain_supplier, powertrain_supplier]:

  Do not open Stage3-Green from:
    - auto / mobility label alone
    - vehicle camera / autonomous-driving electronics label alone
    - hydraulic / actuator / industrial-mobility component label alone
    - drivetrain / transmission / powertrain parts label alone
    - hybrid / EV / ADAS model-mix headline alone
    - OEM volume recovery headline alone
    - customer concentration or anchor-customer sympathy alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - named OEM / model / platform / supply channel
    - customer volume and production schedule
    - model mix and ASP
    - utilization and fixed-cost absorption
    - raw-material / resin / steel / copper / labor / energy cost pass-through
    - logistics / warranty / quality-claim / recall-risk containment
    - inventory / working-capital burden control
    - customer concentration and program rollover risk check
    - margin / OP conversion
    - row / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the auto/mobility headline

  If MFE < 8% and MAE <= -30%:
    route to C29 hard-4C candidate.

  If MFE is moderate but MAE enters hard zone:
    route to hard-4C unless named OEM/model and cost-pass-through margin bridge are explicit.

  If MFE is meaningful but later MAE is material:
    preserve as capped positive or local 4B, not Green, unless customer-volume and margin evidence appears.

  If row-presence, old corporate-action, SPAC/name-history, or customer-concentration caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.

  Distinguish:
    - suppliers where OEM program volume, model mix, and pass-through become OP
    - from labels where customer concentration, material cost, warranty, logistics, or working capital breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_99_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 vehicle electronics / hydraulic / drivetrain supplier cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_VEHICLE_ELECTRONICS_HYDRAULIC_DRIVETRAIN_OEM_VOLUME_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Do not ingest rejected_candidate rows as primary calibration cases.
8. If enough C29 cases agree, consider implementing a canonical guard that:
   - blocks mobility supplier Green without named OEM/model/platform, production schedule, volume, model mix, cost pass-through, warranty/quality, and OP bridge,
   - preserves vehicle electronics positives only with price survival and fresh customer-program / margin evidence,
   - treats modest-MFE/material-MAE hydraulic component labels as local 4B or Watch,
   - routes moderate-MFE/hard-MAE drivetrain labels to hard-4C when OEM/margin bridge is missing,
   - applies row-presence, old corporate-action, SPAC/name-history, and customer-concentration caveats.

Expected next schedule:
completed_round = R9
completed_loop = 99
next_round = R10
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 99
next_round = R10
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
