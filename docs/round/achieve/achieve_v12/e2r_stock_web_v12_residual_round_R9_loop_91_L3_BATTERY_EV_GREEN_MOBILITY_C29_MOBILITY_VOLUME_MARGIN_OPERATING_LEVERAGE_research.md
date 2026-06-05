# E2R Stock-Web v12 Residual Research — R9 / Loop 91

```yaml
scheduled_round: R9
scheduled_loop: 91
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 91
next_round: R10
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 91
```

R9 can use:

```text
L3_BATTERY_EV_GREEN_MOBILITY
```

when the case is mobility / transport in nature. This file uses:

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine branch = ocean shipping / freight rate / vessel utilization / cost pass-through / margin bridge
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

Recent R9 outputs already used:

```text
loop88: 002350, 009900, 012860
loop89: 025540, 073240, 033530
loop90: 091810, 003490, 089590
```

Selected symbols:

```text
011200 HMM
028670 팬오션
005880 대한해운
```

They avoid the C29 top-covered symbols and avoid recent R9 symbols.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
011200: same archetype, new symbol, direct container freight-rate bridge branch
028670: same archetype, new symbol, dry-bulk shipping label / indirect freight-rate false-positive branch
005880: same archetype, new symbol, small shipping local-burst / high-MAE freight-rate sympathy branch
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
011200 HMM
  profile: atlas/symbol_profiles/011/011200.json
  first_date: 1995-10-13
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,607
  corporate_action_candidate_dates include:
    1996-01-03, 1998-12-07, 1999-04-12, 2000-01-07,
    2006-07-04, 2015-03-25, 2016-05-09, 2016-08-05,
    2017-12-27, 2021-11-16, 2023-11-10
  2024 entry~D+180 contamination: none

028670 팬오션
  profile: atlas/symbol_profiles/028/028670.json
  first_date: 2007-09-21
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,455
  corporate_action_candidate_dates:
    2008-12-12, 2014-01-24, 2014-05-07, 2014-11-06,
    2015-07-27, 2015-07-30
  2024 entry~D+180 contamination: none

005880 대한해운
  profile: atlas/symbol_profiles/005/005880.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,650
  corporate_action_candidate_dates:
    1999-04-07, 2010-12-27, 2011-11-24, 2012-04-05,
    2013-05-09, 2013-11-14, 2020-10-12, 2021-06-30
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-05-31
Red Sea rerouting, container freight rate surge, Asia port congestion, container shortage, and peak-season freight squeeze.
```

C29 is about mobility / transport volume and margin operating leverage.

For shipping, the model can overread:

```text
freight rates are up
Red Sea rerouting is disruptive
shipping stocks are active
container rates are rising
dry-bulk names are related
small-cap shipping stocks spike
```

as if they were automatically the same signal.

They are not. The bridge must map:

```text
freight-rate shock
  -> company freight mix
  -> spot vs contract exposure
  -> vessel utilization
  -> bunker/fuel and rerouting cost
  -> charter-in cost / fleet ownership
  -> operating margin
  -> OP/EPS/FCF conversion
  -> price survival after the first rate spike
```

Shipping is a toll road on water. A higher headline toll helps only if the company owns the lane, the cars actually pass through, and fuel/charter costs do not eat the toll.

---

## 5. Case 1 — 011200 HMM

```yaml
case_id: C29_R9L91_011200_2024_05_31
symbol: "011200"
name: "HMM"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE
trigger_date: 2024-05-31
entry_date: 2024-05-31
entry_price_basis: close
entry_price: 18000
classification: watch_positive_direct_container_rate_bridge_not_green
calibration_usable: true
```

### Evidence interpretation

HMM is the direct container-carrier case. It is the cleanest candidate to benefit from a container freight-rate squeeze, but even here the price path argues against automatic Green.

The constructive bridge:

```text
container freight rates
  -> direct carrier exposure
  -> spot/contract mix
  -> vessel utilization
  -> operating leverage
```

The problem:

```text
MFE was useful but not explosive.
MAE was not catastrophic, but the path required business bridge confirmation.
```

### Price path

Key Stock-Web rows:

```text
2024-05-31: close 18,000
2024-06-03: high 19,440 / close 19,130
2024-06-07: high 19,720 / close 19,500
2024-06-25: high 19,960 / close 19,180
2024-07-03: high 20,800 / close 19,900
2024-08-05: low 15,800 / close 16,280
2024-09-27: high 18,920 / close 18,860
```

Approximate path from 2024-05-31 close:

```text
entry_close: 18,000
peak_high: 20,800
MFE: +15.6%
worst_low: 15,800
MAE: -12.2%
```

### Interpretation

This is a watch-positive / capped-positive case:

```text
Stage2-Watch: valid.
Stage2-Actionable: allowed only if spot/contract and margin bridge are explicit.
Stage3-Green: blocked from headline alone.
Hard 4C: no.
```

The direct carrier exposure matters. But C29 should not treat container-rate headlines as a full rerating unless margin conversion appears.

### Stress-test components

```text
raw_component_score_proxy:
  direct_container_rate_exposure: high
  spot_contract_mix_visibility: medium
  fuel_rerouting_cost_risk: high
  price_confirmation: medium
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow unless margin bridge confirms
```

---

## 6. Case 2 — 028670 팬오션

```yaml
case_id: C29_R9L91_028670_2024_05_31
symbol: "028670"
name: "팬오션"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE
trigger_date: 2024-05-31
entry_date: 2024-05-31
entry_price_basis: close
entry_price: 4305
classification: hard_4c_candidate_dry_bulk_label_without_container_rate_margin_bridge
calibration_usable: true
```

### Evidence interpretation

팬오션 is the indirect shipping-label false-positive. It can rally with shipping headlines, but C29 must distinguish:

```text
container freight-rate shock
```

from:

```text
dry-bulk exposure, charter cost, commodity volume, and fleet mix.
```

A Red Sea / container-rate headline does not automatically become a Pan Ocean earnings bridge.

### Price path

Key Stock-Web rows:

```text
2024-05-31: close 4,305
2024-06-03: high 4,530 / close 4,460
2024-07-02: high 4,435 / close 4,180
2024-08-05: low 3,345 / close 3,410
2024-09-09: low 3,270 / close 3,360
2024-09-27: high 4,055 / close 4,015
```

Approximate path from 2024-05-31 close:

```text
entry_close: 4,305
peak_high: 4,530
MFE: +5.2%
worst_low: 3,270
MAE: -24.0%
```

### Interpretation

This is the hard C29 guardrail case:

```text
Stage2-Watch: allowed from shipping-sector volatility.
Stage2-Actionable: blocked unless dry-bulk freight / vessel utilization / margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

This is the simplest rule: shipping label is not shipping leverage.

### Stress-test components

```text
raw_component_score_proxy:
  shipping_label_relevance: high
  direct_container_rate_exposure: low_to_medium
  dry_bulk_rate_bridge: unclear
  margin_bridge: weak
  price_confirmation: failed
  drawdown_penalty: high
```

---

## 7. Case 3 — 005880 대한해운

```yaml
case_id: C29_R9L91_005880_2024_05_31
symbol: "005880"
name: "대한해운"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE
trigger_date: 2024-05-31
entry_date: 2024-05-31
entry_price_basis: close
entry_price: 2490
classification: local_burst_but_high_mae_shipping_sympathy_counterexample
calibration_usable: true
```

### Evidence interpretation

대한해운 is the local-burst case. It had a strong sympathy move after the freight-rate shock, but the move did not survive.

This case is important because it prevents the model from treating a high initial MFE as sufficient evidence.

The bridge must ask:

```text
Is this company exposed to the exact freight segment that repriced?
Are the contracts spot or long-term?
Does rerouting raise revenue more than cost?
Does fleet utilization improve?
Does OP convert?
```

Without those answers, the move is a 4B/local-burst candidate, not Green.

### Price path

Key Stock-Web rows:

```text
2024-05-31: close 2,490
2024-06-03: high 2,560 / close 2,440
2024-06-25: high 2,710 / close 2,455
2024-06-28: high 2,985 / close 2,895
2024-08-05: low 1,772 / close 1,851
2024-09-09: low 1,754 / close 1,831
```

Approximate path from 2024-05-31 close:

```text
entry_close: 2,490
peak_high: 2,985
MFE: +19.9%
worst_low: 1,754
MAE: -29.6%
peak_to_later_low_drawdown: -41.2%
```

### Interpretation

This is a local-burst / high-MAE counterexample:

```text
Stage2-Watch: valid.
Stage2-Actionable: only as event-trading / local 4B, not durable Green.
Stage3-Green: blocked.
Hard 4C: borderline, but primary label is local burst failure.
```

The signal generated a tradable burst, but not a durable operating-leverage rerating.

### Stress-test components

```text
raw_component_score_proxy:
  shipping_sympathy_signal: high
  exact_freight_segment_bridge: weak
  contract_mix_visibility: weak
  cost_pass_through_visibility: weak
  local_price_confirmation: medium
  post_burst_survival: failed
  drawdown_penalty: high
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

The three-case C29 shipping grid:

```text
011200 HMM:
  direct container-rate exposure can support Watch/Actionable,
  but Green requires spot/contract, utilization, and margin bridge.

028670 팬오션:
  shipping label alone failed.
  Shallow MFE and high MAE make it a hard 4C candidate.

005880 대한해운:
  freight-rate sympathy created a local burst,
  but the move failed price survival and needs 4B/high-MAE routing.
```

Shared rule:

```text
C29 shipping is not "freight rates are up."
C29 shipping is "this company captures that exact freight-rate move through owned capacity, contract mix, utilization, cost pass-through, and margin conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L91_011200_2024_05_31","scheduled_round":"R9","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE","symbol":"011200","name":"HMM","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":18000,"peak_high":20800,"peak_date":"2024-07-03","worst_low":15800,"worst_low_date":"2024-08-05","mfe_pct":15.6,"mae_pct":-12.2,"classification":"watch_positive_direct_container_rate_bridge_not_green","calibration_usable":true,"evidence_family":"direct_container_freight_rate_spot_contract_margin_bridge","residual_error":"direct_freight_rate_exposure_still_needs_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_only_if_spot_contract_utilization_margin_bridge_confirms"}
{"row_type":"case","case_id":"C29_R9L91_028670_2024_05_31","scheduled_round":"R9","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE","symbol":"028670","name":"팬오션","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":4305,"peak_high":4530,"peak_date":"2024-06-03","worst_low":3270,"worst_low_date":"2024-09-09","mfe_pct":5.2,"mae_pct":-24.0,"classification":"hard_4c_candidate_dry_bulk_label_without_container_rate_margin_bridge","calibration_usable":true,"evidence_family":"dry_bulk_shipping_label_without_exact_freight_margin_bridge","residual_error":"shipping_label_can_overpromote_without_exact_rate_segment_and_margin_conversion","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_exact_freight_bridge_missing"}
{"row_type":"case","case_id":"C29_R9L91_005880_2024_05_31","scheduled_round":"R9","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE","symbol":"005880","name":"대한해운","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":2490,"peak_high":2985,"peak_date":"2024-06-28","worst_low":1754,"worst_low_date":"2024-09-09","mfe_pct":19.9,"mae_pct":-29.6,"peak_to_later_low_drawdown_pct":-41.2,"classification":"local_burst_but_high_mae_shipping_sympathy_counterexample","calibration_usable":true,"evidence_family":"shipping_sympathy_local_burst_without_contract_mix_cost_pass_through_bridge","residual_error":"freight_rate_sympathy_can_create_local_burst_but_fail_operating_leverage_green","shadow_rule_candidate":"keep_sympathy_burst_as_4b_watch_not_green_if_price_survival_fails"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":91,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"OCEAN_SHIPPING_FREIGHT_RATE_VOLUME_MARGIN_BRIDGE_VS_GENERIC_SHIPPING_RATE_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":91,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_SHIPPING_FREIGHT_SEGMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 shipping/transport names, do not open Stage2-Actionable or Stage3-Green from freight-rate spike, Red Sea disruption, shipping-sector label, or one-day volume burst alone. Require exact freight segment exposure, spot/contract mix, vessel utilization, fleet ownership or charter-in cost, fuel/rerouting cost pass-through, margin/OP conversion, and post-trigger price survival. Direct container carriers may be Watch/Actionable if bridge evidence exists; indirect dry-bulk or sympathy names should cap at Watch/4B unless exact economics are explicit. Shallow-MFE/high-MAE cases route to hard-4C.","expected_effect":"Reduce generic shipping-rate false positives while preserving direct freight-rate positives that show contract, utilization, and margin conversion.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":91,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"shipping_freight_rate_operating_leverage_guard","contribution":"Adds one direct container-carrier watch-positive, one dry-bulk hard-4C candidate, and one local shipping-sympathy burst failure to calibrate C29 transport/shipping bridge requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_SHIPPING_FREIGHT_SEGMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [shipping, container_carrier, dry_bulk, logistics_transport]:

  Do not open Stage3-Green from:
    - freight-rate spike headline alone
    - Red Sea rerouting headline alone
    - shipping-sector label alone
    - small-cap shipping volume burst alone
    - one-week freight-rate sympathy move alone

  Require at least two of:
    - exact freight segment exposure
    - spot vs contract freight mix
    - vessel utilization or capacity tightness
    - owned fleet vs charter-in cost advantage
    - bunker/fuel and rerouting cost pass-through
    - margin / OP / EPS conversion
    - low-MAE post-trigger price survival

  If direct container carrier has MFE > 10% and MAE remains controlled:
    allow Watch/Actionable only with spot/contract and margin bridge.

  If MFE < 10% and MAE < -20%:
    route to C29 hard-4C candidate.

  If MFE > 15% but later peak-to-trough drawdown > -35%:
    classify as local 4B / sympathy burst failure, not Green.

  Distinguish:
    - direct container-rate exposure
    - from dry-bulk or generic shipping sympathy without exact freight-margin bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_91_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 shipping/transport cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_SHIPPING_FREIGHT_SEGMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 transport/shipping cases agree, consider implementing a canonical guard that:
   - blocks freight-rate headline Green without segment/contract/utilization/margin bridge,
   - preserves direct container-carrier positives only when price survival and margin bridge confirm,
   - routes shallow-MFE/high-MAE dry-bulk or generic-shipping names to hard-4C,
   - keeps high-MFE/high-MAE shipping sympathy moves as local 4B only.

Expected next schedule:
completed_round = R9
completed_loop = 91
next_round = R10
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 91
next_round = R10
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
