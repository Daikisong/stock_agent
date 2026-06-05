# E2R Stock-Web v12 Residual Research — R9 / Loop 95

```yaml
scheduled_round: R9
scheduled_loop: 95
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE

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
rental_fleet_case_count: 1
used_car_platform_case_count: 1
carsharing_platform_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 95
next_round: R10
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_95_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 95
```

R9 may use an L3 mobility branch when the case is mobility / auto / transport in nature. This run uses:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

The selected fine branch is:

```text
rental fleet / used-car platform / car-sharing platform
fleet utilization, residual value, unit economics, and margin bridge
vs generic mobility-service label spike
```

This deliberately avoids:
- the loop94 auto component / powertrain / interior / NVH C29 branch;
- the loop93 auto-logistics / car-carrier / parcel / shipping C29 branch;
- the C29 top-covered symbols.

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
loop92: 012330, 161390, 204320
loop93: 086280, 002320, 003280
loop94: 092200, 067570, 024900
```

Selected symbols:

```text
089860 롯데렌탈
381970 케이카
403550 쏘카
```

They avoid the C29 top-covered list and avoid recent R9 loop88~94 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
089860: same archetype, new symbol, rental-fleet utilization / residual-value positive with Green cap
381970: same archetype, new symbol, used-car platform Watch cap without strong incremental unit-economics bridge
403550: same archetype, new symbol, car-sharing platform event spike hard-4C candidate without fleet-utilization margin survival
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
089860 롯데렌탈
  profile: atlas/symbol_profiles/089/089860.json
  first_date: 2021-08-19
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,101
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

381970 케이카
  profile: atlas/symbol_profiles/381/381970.json
  first_date: 2021-10-13
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,067
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

403550 쏘카
  profile: atlas/symbol_profiles/403/403550.json
  first_date: 2022-08-22
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 854
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C29 is about mobility volume, utilization, operating leverage, and margin. It is not a generic "mobility service" or "transport platform" label.

The model can over-score:

```text
rental-car label
used-car platform label
car-sharing platform label
mobility-service traffic
fleet expansion or asset-light claim
secondhand-car price normalization
one-week mobility-stock volume spike
```

The C29 bridge must be stricter:

```text
mobility / rental / platform event
  -> fleet utilization or transaction volume
  -> residual value and used-car price risk
  -> procurement / depreciation / financing cost
  -> take-rate or service fee economics
  -> maintenance / insurance / marketing cost control
  -> margin / OP conversion
  -> price survival after the first mobility-service spike
```

A mobility platform is like a fleet depot. The label says cars are available, but C29 asks whether they are rented often enough, resold at a good residual value, financed cheaply enough, maintained efficiently enough, and converted into operating profit.

---

## 5. Case 1 — 089860 롯데렌탈

```yaml
case_id: C29_R9L95_089860_2024_02_23
symbol: "089860"
name: "롯데렌탈"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE
trigger_date: 2024-02-23
entry_date: 2024-02-23
entry_price_basis: close
entry_price: 27650
classification: positive_capped_rental_fleet_utilization_residual_value_margin_bridge
calibration_usable: true
```

### Evidence interpretation

롯데렌탈 is the constructive C29 control in this set.

The useful C29 read is not simply:

```text
렌터카 / 모빌리티 주식이 움직였다
```

It is:

```text
rental fleet and used-car disposal relevance
  -> utilization and residual-value economics
  -> fleet financing and depreciation cost control
  -> margin and operating-leverage bridge
  -> price survival after the trigger
```

The forward path delivered a meaningful MFE while keeping the drawdown controlled. This is a capped positive. It still requires utilization, residual-value, and financing-cost evidence before unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-02-23: high 27,750 / close 27,650
2024-04-17: low 26,400 / close 26,450
2024-06-20: high 30,500 / close 30,400
2024-08-05: low 26,550 / close 27,050
2024-08-28: high 32,350 / close 32,050
2024-09-24: high 32,050 / close 31,900
2024-10-25: low 28,000 / close 28,550
```

Approximate path from entry close:

```text
entry_close: 27,650
peak_high: 32,350
MFE: +17.0%
worst_low_after_entry: 26,400
MAE: -4.5%
```

### Interpretation

This is a C29 capped positive:

```text
Stage2-Actionable: possible if fleet utilization, residual value, financing cost, and margin bridge are explicit.
Stage3-Green: blocked without refreshed fleet economics and OP evidence.
Local 4B: monitor after mid-teen MFE if residual-value or financing-cost evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  rental_fleet_relevance: high
  utilization_bridge: medium_high
  residual_value_bridge: medium_high
  financing_depreciation_bridge: medium
  margin_op_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 381970 케이카

```yaml
case_id: C29_R9L95_381970_2024_07_24
symbol: "381970"
name: "케이카"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 12550
classification: watch_cap_used_car_platform_label_without_strong_incremental_unit_economics_bridge
calibration_usable: true
```

### Evidence interpretation

케이카 is the used-car platform Watch cap.

The setup is relevant:

```text
used-car platform / retail channel
  -> used-car price normalization
  -> inventory turn and gross profit per unit
  -> platform or retail operating leverage
```

But from the selected July entry, the price path was not strong enough for Actionable/Green. MFE was modest, and the early August drawdown was meaningful. The model should require incremental unit economics, inventory turn, financing, and marketing cost evidence.

### Price path

Key Stock-Web rows:

```text
2024-07-24: close 12,550
2024-08-05: low 11,100 / close 12,010
2024-08-21: high 13,800 / close 13,670
2024-08-26: high 13,930 / close 13,670
2024-09-09: low 12,750 / close 12,850
2024-10-25: low 12,840 / close 12,850
```

Approximate path from entry close:

```text
entry_close: 12,550
peak_high: 13,930
MFE: +11.0%
worst_low_after_entry: 11,100
MAE: -11.6%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from used-car platform and inventory-turn relevance.
Stage2-Actionable: blocked unless transaction volume, gross profit per unit, inventory risk, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no.
```

The lesson is that used-car platform relevance is not automatically unit-economics leverage.

### Stress-test components

```text
raw_component_score_proxy:
  used_car_platform_relevance: high
  inventory_turn_bridge: weak_to_medium
  residual_value_bridge: medium
  financing_marketing_cost_bridge: weak
  price_confirmation: modest
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 403550 쏘카

```yaml
case_id: C29_R9L95_403550_2024_03_25
symbol: "403550"
name: "쏘카"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE
trigger_date: 2024-03-25
entry_date: 2024-03-25
entry_price_basis: close
entry_price: 22200
classification: hard_4c_candidate_carsharing_platform_event_spike_without_fleet_utilization_margin_survival
calibration_usable: true
```

### Evidence interpretation

쏘카 is the hard C29 guardrail.

The setup had the classic mobility-platform spike shape:

```text
car-sharing platform
  -> mobility service / app traffic label
  -> fleet utilization and platform optionality
  -> event-driven price spike
```

But from the selected close after the March spike, the stock produced almost no additional MFE and then fell into a large drawdown. The bridge from traffic or platform salience to fleet utilization, depreciation, financing, insurance, marketing cost, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-03-25: high 22,550 / close 22,200
2024-04-05: high 22,450 / close 22,000
2024-04-12: low 16,850 / close 19,780
2024-08-05: low 17,700 / close 18,320
2024-09-25: low 17,810 / close 17,880
2024-10-22: low 17,370 / close 17,380
```

Approximate path from entry close:

```text
entry_close: 22,200
peak_high_after_entry: 22,550
MFE: +1.6%
worst_low_after_entry: 16,850
MAE: -24.1%
```

### Interpretation

This is a hard C29 false-positive candidate:

```text
Stage2-Watch: possible from car-sharing and mobility-platform relevance.
Stage2-Actionable: blocked unless fleet utilization, unit economics, financing/depreciation, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by near-zero MFE and large MAE in a platform event-spike pattern.
```

The lesson is that mobility app salience is not fleet-level operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  carsharing_platform_label: high
  traffic_or_app_relevance: medium_high
  fleet_utilization_bridge: weak
  depreciation_financing_bridge: weak
  insurance_marketing_cost_bridge: weak
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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
rental_fleet_case_count: 1
used_car_platform_case_count: 1
carsharing_platform_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C29 mobility-service grid:

```text
089860 롯데렌탈:
  rental fleet / residual-value economics positive;
  meaningful MFE and controlled MAE, but Green requires fleet-utilization and margin evidence.

381970 케이카:
  used-car platform relevance;
  modest MFE and medium drawdown, Watch/Yellow cap without incremental unit economics.

403550 쏘카:
  car-sharing platform event spike failed;
  near-zero MFE and large MAE, hard 4C candidate.
```

Shared rule:

```text
C29 is not "mobility platform is relevant."
C29 is "fleet utilization, transaction volume, residual value, financing/depreciation, cost control, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L95_089860_2024_02_23","scheduled_round":"R9","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE","symbol":"089860","name":"롯데렌탈","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":27650,"peak_high":32350,"peak_date":"2024-08-28","worst_low_after_entry":26400,"worst_low_after_entry_date":"2024-04-17","mfe_pct":17.0,"mae_pct":-4.5,"classification":"positive_capped_rental_fleet_utilization_residual_value_margin_bridge","calibration_usable":true,"evidence_family":"rental_fleet_utilization_residual_value_financing_depreciation_margin_bridge","residual_error":"positive_mobility_rental_path_requires_green_cap_without_refreshed_fleet_utilization_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_fleet_utilization_residual_value_and_margin_bridge_confirm"}
{"row_type":"case","case_id":"C29_R9L95_381970_2024_07_24","scheduled_round":"R9","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE","symbol":"381970","name":"케이카","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":12550,"peak_high":13930,"peak_date":"2024-08-26","worst_low_after_entry":11100,"worst_low_after_entry_date":"2024-08-05","mfe_pct":11.0,"mae_pct":-11.6,"classification":"watch_cap_used_car_platform_label_without_strong_incremental_unit_economics_bridge","calibration_usable":true,"evidence_family":"used_car_platform_inventory_turn_residual_value_label_without_incremental_unit_economics_margin_bridge","residual_error":"used_car_platform_relevance_can_overpromote_without_inventory_turn_gppu_and_margin_evidence","shadow_rule_candidate":"cap_used_car_platform_label_at_watch_yellow_if_mfe_modest_and_unit_economics_bridge_missing"}
{"row_type":"case","case_id":"C29_R9L95_403550_2024_03_25","scheduled_round":"R9","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE","symbol":"403550","name":"쏘카","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":22200,"peak_high":22550,"peak_date":"2024-03-25","worst_low_after_entry":16850,"worst_low_after_entry_date":"2024-04-12","mfe_pct":1.6,"mae_pct":-24.1,"classification":"hard_4c_candidate_carsharing_platform_event_spike_without_fleet_utilization_margin_survival","calibration_usable":true,"evidence_family":"carsharing_platform_event_spike_without_fleet_utilization_depreciation_financing_margin_bridge","residual_error":"mobility_app_platform_label_can_fail_when_fleet_level_unit_economics_and_margin_bridge_missing","shadow_rule_candidate":"route_carsharing_platform_event_spike_to_hard_4c_if_mfe_near_zero_mae_large_and_fleet_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":95,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"RENTAL_USED_CAR_CARSHARING_FLEET_UTILIZATION_RESIDUAL_VALUE_MARGIN_BRIDGE_VS_MOBILITY_SERVICE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"rental_fleet_case_count":1,"used_car_platform_case_count":1,"carsharing_platform_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":95,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_FLEET_UTILIZATION_RESIDUAL_VALUE_UNIT_ECONOMICS_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 mobility-service names, do not open Stage2-Actionable or Stage3-Green from rental-car, used-car platform, car-sharing platform, app traffic, fleet expansion, asset-light, used-car price normalization, or one-week mobility-service stock spike labels alone. Require fleet utilization or transaction volume, residual-value and used-car price risk check, procurement/depreciation/financing cost control, take-rate or service-fee economics, maintenance/insurance/marketing cost containment, margin/OP conversion, and post-trigger price survival. Rental-fleet positives with controlled MAE may be capped Actionable when utilization, residual value, and margin bridge are explicit. Used-car platform labels with modest MFE should cap at Watch/Yellow without inventory-turn and unit-economics evidence. Car-sharing platform event spikes with near-zero MFE and large MAE should route to hard-4C when fleet utilization and margin bridge are missing.","expected_effect":"Preserve true mobility operating-leverage positives while reducing rental/used-car/car-sharing platform label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":95,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"fleet_utilization_residual_value_unit_economics_guard","contribution":"Adds one rental-fleet capped positive, one used-car platform Watch cap, and one car-sharing hard-4C candidate to calibrate C29 fleet utilization, residual value, financing/depreciation, unit economics, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_FLEET_UTILIZATION_RESIDUAL_VALUE_UNIT_ECONOMICS_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [rental_fleet, used_car_platform, carsharing_platform, mobility_service]:

  Do not open Stage3-Green from:
    - rental-car label alone
    - used-car platform label alone
    - car-sharing platform label alone
    - mobility-service app traffic alone
    - fleet expansion or asset-light claim alone
    - used-car price normalization alone
    - one-week mobility-service volume spike alone

  Require at least two of:
    - fleet utilization / transaction-volume growth
    - residual value / used-car price risk control
    - procurement / depreciation / financing-cost control
    - take-rate or service-fee economics
    - maintenance / insurance / marketing-cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the mobility-service headline

  If MFE < 5% and MAE < -20%:
    route to C29 hard-4C candidate for mobility-service event spikes.

  If MFE is modest and unit-economics bridge is weak:
    cap at Watch/Yellow.

  If MFE is meaningful but the bridge is stale:
    preserve as capped positive or local 4B, not Green.

  Distinguish:
    - rental or used-car names where fleet economics become margin
    - from app/platform labels where traffic does not survive depreciation, insurance, financing, and marketing costs.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_95_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 mobility-service fleet/utilization/unit-economics cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_FLEET_UTILIZATION_RESIDUAL_VALUE_UNIT_ECONOMICS_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 mobility-service cases agree, consider implementing a canonical guard that:
   - blocks mobility-service Green without fleet utilization, residual value, financing/depreciation, unit economics, and margin bridge,
   - preserves rental-fleet positives only with controlled MAE and fresh margin evidence,
   - caps used-car platform labels at Watch/Yellow without inventory-turn and GPPU evidence,
   - routes near-zero-MFE/large-MAE car-sharing platform event spikes to hard-4C.

Expected next schedule:
completed_round = R9
completed_loop = 95
next_round = R10
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 95
next_round = R10
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
