# E2R Stock-Web v12 Residual Research — R9 / Loop 93

```yaml
scheduled_round: R9
scheduled_loop: 93
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE

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
corporate_action_caveat_avoided_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 93
next_round: R10
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_93_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 93
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
auto logistics / car carrier / parcel logistics / shipping volume-margin bridge
vs generic transport label or freight-theme spike
```

This deliberately avoids the prior R9 loop92 auto-parts/tire/ADAS branch and the prior loop91 ocean-shipping freight-rate branch.

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
```

Selected symbols:

```text
086280 현대글로비스
002320 한진
003280 흥아해운
```

They avoid the C29 top-covered list and avoid recent R9 loop88~92 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
086280: same archetype, new symbol, auto logistics / car carrier volume-margin positive branch after corporate-action candidate windows
002320: same archetype, new symbol, parcel/logistics label early spike then weak price-survival Watch/4C-border branch
003280: same archetype, new symbol, shipping/freight theme re-spike shallow-MFE high-MAE hard-4C branch
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
086280 현대글로비스
  profile: atlas/symbol_profiles/086/086280.json
  name history:
    글로비스 until 2011-04-01
    현대글로비스 from 2011-04-04
  first_date: 2005-12-26
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,970
  corporate_action_candidate_dates:
    2024-07-12, 2024-08-02
  selected entry:
    2024-08-06, after both 2024 corporate-action candidate windows
  entry~D+180 contamination: none after selected entry

002320 한진
  profile: atlas/symbol_profiles/002/002320.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,760
  non_tradable_zero_volume rows: 5
  corporate_action_candidate_dates:
    1999-07-27, 2000-03-13, 2020-11-18
  2024 entry~D+180 contamination: none

003280 흥아해운
  profile: atlas/symbol_profiles/003/003280.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,083
  non_tradable_zero_volume rows: 682
  corporate_action_candidate_dates:
    2004-03-16, 2006-04-25, 2009-07-07, 2016-05-11,
    2017-01-13, 2018-02-07, 2019-06-24, 2021-09-15
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C29 is not a generic "transport stock" or "freight rate went up" label.

The model can over-score:

```text
auto export strength
car carrier / logistics label
parcel volume rebound
shipping / freight theme
port congestion or geopolitical freight sympathy
one-week transport-stock volume spike
```

The C29 bridge must map the actual operating leverage:

```text
transport volume / freight rate / logistics demand
  -> company-specific volume
  -> contract rate, spot exposure, or take-rate
  -> fleet / network utilization
  -> fuel, labor, and FX cost pass-through
  -> fixed-cost absorption
  -> margin / OP conversion
  -> price survival after the first transport-theme rally
```

A transport stock is a truck convoy. A headline says the road is busy, but the stock only rerates when this company's trucks are full, pricing holds, fuel and labor are passed through, and the route earns margin.

---

## 5. Case 1 — 086280 현대글로비스

```yaml
case_id: C29_R9L93_086280_2024_08_06
symbol: "086280"
name: "현대글로비스"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE
trigger_date: 2024-08-06
entry_date: 2024-08-06
entry_price_basis: close
entry_price: 106800
classification: positive_capped_auto_logistics_car_carrier_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

현대글로비스 is the constructive control in this transport/logistics set.

The useful C29 read is not:

```text
transport stock went up
```

It is:

```text
auto logistics / car carrier / CKD and distribution volume
  -> contract or captive-customer stability
  -> fleet/network utilization
  -> cost pass-through
  -> price survival after corporate-action-adjusted window
```

Because the profile has 2024 corporate-action candidate dates on 2024-07-12 and 2024-08-02, the entry was deliberately selected after those windows. The post-entry path had controlled MAE and later made a new high.

### Price path

Key Stock-Web rows:

```text
2024-08-02: corporate-action candidate window area already passed
2024-08-06: close 106,800
2024-08-07: low 102,000 / close 107,100
2024-08-23: high 115,400 / close 114,100
2024-09-13: high 117,800 / close 115,700
2024-09-26: high 124,500 / close 124,500
2024-09-30: high 125,600 / close 122,100
```

Approximate path from entry close:

```text
entry_close: 106,800
peak_high: 125,600
MFE: +17.6%
worst_low_after_entry: 102,000
MAE: -4.5%
```

### Interpretation

This is a C29 positive, but capped:

```text
Stage2-Actionable: valid if volume, contract-rate, and margin bridge are explicit.
Stage3-Green: requires sustained OP/margin confirmation and cost-pass-through evidence.
Local 4B: not mandatory at entry, but monitor after extended rally.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  auto_logistics_relevance: high
  car_carrier_volume_bridge: medium_high
  captive_customer_or_contract_bridge: medium_high
  cost_pass_through_visibility: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 002320 한진

```yaml
case_id: C29_R9L93_002320_2024_01_30
symbol: "002320"
name: "한진"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE
trigger_date: 2024-01-30
entry_date: 2024-01-30
entry_price_basis: close
entry_price: 24250
classification: watch_cap_parcel_logistics_label_without_durable_margin_bridge
calibration_usable: true
```

### Evidence interpretation

한진 is the parcel/logistics Watch cap case.

The January spike had a plausible setup:

```text
parcel/logistics volume
  -> e-commerce and delivery demand
  -> fixed-cost absorption
  -> margin recovery
```

But the path did not validate a durable operating-leverage thesis. MFE was not disastrous, but the later drawdown was too large to allow Actionable/Green without fresh margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-01-29: high 24,150 / close 23,550
2024-01-30: high 27,300 / close 24,250
2024-02-02: high 26,700 / close 26,400
2024-03-22: high 24,150 / close 24,100
2024-04-16: low 20,350 / close 20,550
2024-08-05: low 17,000 / close 17,260
2024-10-16: high 20,300 / close 20,300
```

Approximate path from entry close:

```text
entry_close: 24,250
peak_high: 27,300
MFE: +12.6%
worst_low_after_entry: 17,000
MAE: -29.9%
```

### Interpretation

This is a Watch/Yellow cap case, close to a 4C boundary:

```text
Stage2-Watch: valid from logistics-volume relevance.
Stage2-Actionable: blocked unless parcel volume, pricing, and OP leverage bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MFE was near mid-teens, but re-entry without margin bridge should route to 4C.
```

### Stress-test components

```text
raw_component_score_proxy:
  parcel_logistics_relevance: high
  volume_growth_bridge: weak_to_medium
  pricing_or_take_rate_bridge: weak
  cost_absorption_bridge: weak
  price_confirmation: shallow_to_medium
  drawdown_penalty: high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 003280 흥아해운

```yaml
case_id: C29_R9L93_003280_2024_08_06
symbol: "003280"
name: "흥아해운"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE
trigger_date: 2024-08-06
entry_date: 2024-08-06
entry_price_basis: close
entry_price: 2965
classification: hard_4c_candidate_shipping_freight_theme_respike_without_margin_survival_bridge
calibration_usable: true
```

### Evidence interpretation

흥아해운 is the hard guardrail case.

It had repeated freight/shipping theme spikes in 2024, and the August trigger looked like another transport momentum restart:

```text
shipping / freight rate theme
  -> geopolitical route or freight sympathy
  -> huge turnover
  -> model could mistake theme heat for C29 margin leverage
```

The forward path failed badly. The stock had almost no additional MFE after the 2024-08-06 close and then lost price survival.

### Price path

Key Stock-Web rows:

```text
2024-08-01: high 2,715 / close 2,650
2024-08-02: high 2,980 / close 2,800
2024-08-05: high 2,995 / close 2,695
2024-08-06: high 2,965 / close 2,965
2024-08-07: high 3,075 / close 2,790
2024-08-16: low 2,370 / close 2,375
2024-09-09: low 1,875 / close 1,940
2024-11-01: low 1,870 / close 1,878
```

Approximate path from entry close:

```text
entry_close: 2,965
peak_high: 3,075
MFE: +3.7%
worst_low_after_entry: 1,870
MAE: -36.9%
```

### Interpretation

This is a hard C29 false-positive:

```text
Stage2-Watch: possible from shipping/freight theme relevance.
Stage2-Actionable: blocked without freight-rate, utilization, cost, and margin bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that transport theme turnover is not freight-margin operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  shipping_theme_relevance: high
  freight_rate_bridge: weak
  fleet_utilization_bridge: weak
  fuel_cost_pass_through: unclear
  price_confirmation: failed_after_trigger
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
calibration_usable_trigger_count: 3
```

The three-case C29 logistics/transport grid:

```text
086280 현대글로비스:
  auto logistics / car-carrier positive;
  controlled MAE and later MFE, but Green still requires contract-rate and margin bridge.

002320 한진:
  parcel/logistics label had some MFE,
  but later drawdown caps it at Watch/Yellow without pricing and margin evidence.

003280 흥아해운:
  shipping/freight theme re-spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C29 is not "transport stock volume is hot."
C29 is "transport volume, rate/take-rate, utilization, cost pass-through, and fixed-cost absorption convert into margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L93_086280_2024_08_06","scheduled_round":"R9","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE","symbol":"086280","name":"현대글로비스","trigger_date":"2024-08-06","entry_date":"2024-08-06","entry_price":106800,"peak_high":125600,"peak_date":"2024-09-30","worst_low_after_entry":102000,"worst_low_after_entry_date":"2024-08-07","mfe_pct":17.6,"mae_pct":-4.5,"classification":"positive_capped_auto_logistics_car_carrier_volume_margin_bridge","calibration_usable":true,"evidence_family":"auto_logistics_car_carrier_contract_volume_margin_bridge_after_corporate_action_candidate","residual_error":"positive_path_still_needs_contract_rate_cost_pass_through_and_op_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_volume_contract_rate_margin_bridge_confirms_but_cap_green_without_sustained_op_evidence"}
{"row_type":"case","case_id":"C29_R9L93_002320_2024_01_30","scheduled_round":"R9","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE","symbol":"002320","name":"한진","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":24250,"peak_high":27300,"peak_date":"2024-01-30","worst_low_after_entry":17000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":12.6,"mae_pct":-29.9,"classification":"watch_cap_parcel_logistics_label_without_durable_margin_bridge","calibration_usable":true,"evidence_family":"parcel_logistics_volume_label_without_durable_pricing_cost_absorption_margin_bridge","residual_error":"logistics_volume_label_can_overpromote_without_pricing_and_op_leverage","shadow_rule_candidate":"cap_logistics_label_at_watch_yellow_if_mfe_modest_and_later_mae_material_without_margin_bridge"}
{"row_type":"case","case_id":"C29_R9L93_003280_2024_08_06","scheduled_round":"R9","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE","symbol":"003280","name":"흥아해운","trigger_date":"2024-08-06","entry_date":"2024-08-06","entry_price":2965,"peak_high":3075,"peak_date":"2024-08-07","worst_low_after_entry":1870,"worst_low_after_entry_date":"2024-11-01","mfe_pct":3.7,"mae_pct":-36.9,"classification":"hard_4c_candidate_shipping_freight_theme_respike_without_margin_survival_bridge","calibration_usable":true,"evidence_family":"shipping_freight_theme_respike_without_freight_rate_utilization_margin_bridge","residual_error":"transport_theme_turnover_can_fail_when_freight_rate_and_margin_bridge_missing","shadow_rule_candidate":"route_shipping_theme_respike_to_hard_4c_if_mfe_shallow_mae_large_and_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":93,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_LOGISTICS_CAR_CARRIER_SHIPPING_VOLUME_MARGIN_BRIDGE_VS_TRANSPORT_LABEL_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"corporate_action_caveat_avoided_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":93,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_TRANSPORT_VOLUME_RATE_UTILIZATION_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 transport/logistics names, do not open Stage2-Actionable or Stage3-Green from auto logistics, parcel volume, shipping/freight, car-carrier, port congestion, geopolitical freight, or one-week transport-stock volume spike labels alone. Require company-specific volume, contract rate or take-rate, fleet/network utilization, fuel/labor/FX cost pass-through, fixed-cost absorption, margin/OP conversion, and post-trigger price survival. Auto-logistics/car-carrier positives may be Actionable when volume, contract, and cost bridge are explicit. Parcel/logistics names with modest MFE and material MAE should cap at Watch/Yellow. Shipping/freight theme spikes with shallow MFE and high MAE should route to hard-4C when freight-rate and margin bridge are missing.","expected_effect":"Preserve true transport operating-leverage positives while reducing logistics-label and freight-theme false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":93,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"transport_logistics_volume_rate_margin_guard","contribution":"Adds one auto-logistics/car-carrier capped positive, one parcel-logistics Watch cap, and one shipping/freight hard-4C counterexample to calibrate C29 transport volume, rate, utilization, cost-pass-through, and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_TRANSPORT_VOLUME_RATE_UTILIZATION_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [auto_logistics, car_carrier, parcel_logistics, shipping, freight, transport]:

  Do not open Stage3-Green from:
    - auto logistics or car-carrier label alone
    - parcel volume label alone
    - shipping / freight-rate theme alone
    - port congestion / geopolitical freight sympathy alone
    - one-week transport-stock volume spike alone

  Require at least two of:
    - company-specific transport volume growth
    - contract rate / spot rate / take-rate visibility
    - fleet or network utilization
    - fuel / labor / FX cost pass-through
    - fixed-cost absorption
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the transport headline

  If MFE < 5% and MAE < -30%:
    route to C29 hard-4C candidate.

  If MFE > 10% but MAE approaches -30% and bridge is weak:
    cap at Watch/Yellow unless new margin evidence appears.

  If MFE > 15% and MAE remains controlled:
    allow capped Actionable only if volume/rate/cost bridge is explicit.

  Distinguish:
    - auto-logistics names with contract/captive volume and cost pass-through
    - from parcel or shipping names where theme heat does not convert into margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 transport/logistics operating-leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_TRANSPORT_VOLUME_RATE_UTILIZATION_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 transport cases agree, consider implementing a canonical guard that:
   - blocks transport-label Green without volume/rate/utilization/cost/margin bridge,
   - preserves auto-logistics positives with controlled MAE and cost-pass-through evidence,
   - caps parcel/logistics names at Watch/Yellow without OP leverage,
   - routes shallow-MFE/high-MAE shipping theme spikes to hard-4C.

Expected next schedule:
completed_round = R9
completed_loop = 93
next_round = R10
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 93
next_round = R10
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
