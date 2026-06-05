# E2R Stock-Web v12 Residual Research — R9 / Loop 90

```yaml
scheduled_round: R9
scheduled_loop: 90
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 90
next_round: R10
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_90_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

Under the v12 scheduler:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 90
```

R9 can use:

```text
L3_BATTERY_EV_GREEN_MOBILITY
```

when the case is mobility / transport in nature. This file uses C29 with the airline sub-branch:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine branch = airline traffic / route / yield / operating leverage
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

Prior recent R9 outputs already used:

```text
loop88: 002350, 009900, 012860
loop89: 025540, 073240, 033530
```

Selected symbols:

```text
091810 티웨이항공
003490 대한항공
089590 제주항공
```

These are not in the top-covered C29 list and avoid recent R9 symbols.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
091810: same archetype, new symbol, airline route-capacity expansion bridge
003490: same archetype, new symbol, airline consolidation/integration bridge
089590: same archetype, new symbol, LCC passenger recovery / safety-risk / margin bridge
```

---

## 3. Price-atlas validation

Manifest fields checked:

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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
091810 티웨이항공
  profile: atlas/symbol_profiles/091/091810.json
  first_date: 2018-08-01
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,838
  corporate_action_candidate_dates:
    2020-11-27, 2022-05-12, 2023-02-23, 2025-09-15, 2026-01-13
  2024-03 entry~D+180 contamination: none
  2025 corporate-action candidate is outside this 180D window.

003490 대한항공
  profile: atlas/symbol_profiles/003/003490.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,732
  corporate_action_candidate_dates:
    1998-04-25, 2015-04-01, 2017-03-28, 2020-07-29, 2021-03-24
  2024-12 entry~D+180 contamination: none

089590 제주항공
  profile: atlas/symbol_profiles/089/089590.json
  first_date: 2015-11-06
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,513
  corporate_action_candidate_dates:
    2020-09-03, 2021-11-12, 2022-11-24
  2024-01 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

C29 is about mobility volume / margin / operating leverage.

For airlines, the model can overread:

```text
passenger traffic recovery
route opening
merger/integration
LCC consolidation
international capacity recovery
travel demand normalization
```

as if they were automatically equal to operating leverage.

The necessary bridge is more concrete:

```text
traffic volume
  -> yield / load factor / fuel and FX cost
  -> route economics
  -> aircraft utilization
  -> balance-sheet burden
  -> safety/event risk
  -> OP/EPS/FCF conversion
```

Airlines are especially good at producing false positives because the top-line signal is visible while the margin bridge is hidden in fuel, FX, lease cost, maintenance, and safety risk.

---

## 5. Case 1 — 091810 티웨이항공

```yaml
case_id: C29_R9L90_091810_2024_03_07
symbol: "091810"
name: "티웨이항공"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE
trigger_date: 2024-03-07
entry_date: 2024-03-07
entry_price_basis: close
entry_price: 2770
classification: positive_with_local_4b_watch
calibration_usable: true
```

### Evidence interpretation

T'way was the route-capacity positive in this airline grid. The trigger family is not generic "travel demand recovery." It is more specific:

```text
Korean Air / Asiana merger remedies
  -> T'way gains European long-haul route opportunity
  -> aircraft / crew support from Korean Air
  -> differentiated growth option in a crowded LCC market
```

This is a better C29 setup than a generic LCC recovery headline because there is a route/capacity bridge.

### Price path

Key Stock-Web rows:

```text
2024-03-07: close 2,770
2024-03-28: high 2,790 / close 2,780
2024-04-01: high 2,900 / close 2,885
2024-07-02: high 3,010 / close 2,755
2024-08-05: low 2,305 / close 2,430
2024-09-20: high 3,300 / close 3,295
2024-10-08: high 3,315 / close 3,200
2024-10-11: high 3,950 / close 3,475
2024-10-15: low 2,920 / close 2,940
```

Approximate path from entry close:

```text
entry_close: 2,770
peak_high: 3,950
MFE: +42.6%
worst_low: 2,305
MAE: -16.8%
peak_to_post_peak_low: -26.1%
```

### Interpretation

This is a positive, but not a free Green.

```text
Stage2-Actionable: allowed if route economics and capacity support are explicit.
Stage3-Green: requires yield/load-factor/fuel/FX and OP bridge.
Local 4B: needed after the October route/speculation spike.
```

The stock did produce a real forward MFE. But the path was volatile and the business bridge remained operationally fragile.

### Stress-test components

```text
raw_component_score_proxy:
  route_expansion_specificity: high
  traffic_growth_option: high
  margin/yield_visibility: medium_low
  fuel_fx_sensitivity: high
  balance_sheet_risk: medium
  price_confirmation: high
  drawdown_penalty: medium
```

---

## 6. Case 2 — 003490 대한항공

```yaml
case_id: C29_R9L90_003490_2024_12_12
symbol: "003490"
name: "대한항공"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE
trigger_date: 2024-12-12
entry_date: 2024-12-12
entry_price_basis: close
entry_price: 24200
classification: counterexample_consolidation_headline_without_immediate_operating_leverage
calibration_usable: true
```

### Evidence interpretation

The event frame is Korean Air's completion of the Asiana acquisition.

The event is real and strategically important. But C29 does not ask whether consolidation is strategically meaningful. It asks whether the event immediately converts into volume/margin/operating leverage for the equity holder.

The integration bridge is complicated:

```text
merger completion
  -> integration cost / labor / routes / fleet
  -> cargo/passenger mix
  -> competitive safeguards
  -> LCC restructuring
  -> OP/EPS conversion
```

A consolidation headline without an immediate margin bridge can be a false Stage2-Actionable.

### Price path

Key Stock-Web rows:

```text
2024-12-12: close 24,200
2024-12-18: high 24,850 / close 24,800
2024-12-30: low 22,600 / close 22,600
2025-01-31: high 24,800 / close 24,800
2025-02-27: high 24,950 / close 24,400
2025-04-09: low 19,990 / close 20,150
2025-07-14: high 26,750 / close 26,250
2025-09-26: low 22,550 / close 22,700
```

Approximate path from 2024-12-12 close through fetched forward window:

```text
entry_close: 24,200
early_180D_peak_high_before_April_low: 24,950
early_MFE: +3.1%
worst_low_before_recovery: 19,990
MAE: -17.4%
later_peak_high: 26,750
later_MFE: +10.5%
```

### Interpretation

This is a counterexample, not because the merger is unimportant, but because the immediate trigger did not give a clean C29 operating-leverage path.

```text
Stage2-Watch: allowed from strategic consolidation.
Stage2-Actionable: requires integration synergy / yield / cost bridge.
Stage3-Green: blocked at trigger because MFE was shallow and MAE came first.
```

The later 2025 high is a reminder not to label the business event as irrelevant. But for trigger-level calibration, the December 2024 entry was not clean enough to be Green.

### Stress-test components

```text
raw_component_score_proxy:
  strategic_event_quality: high
  integration_complexity: high
  immediate_margin_bridge: low
  price_confirmation: weak_initially
  drawdown_penalty: medium_high
  delayed_recovery_signal: medium
```

---

## 7. Case 3 — 089590 제주항공

```yaml
case_id: C29_R9L90_089590_2024_01_18
symbol: "089590"
name: "제주항공"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE
trigger_date: 2024-01-18
entry_date: 2024-01-18
entry_price_basis: close
entry_price: 13490
classification: hard_4c_candidate_lcc_traffic_recovery_without_margin_safety_bridge
calibration_usable: true
```

### Evidence interpretation

This is the LCC recovery false-positive case.

The early 2024 frame looked simple:

```text
international passenger traffic recovery
Japan / Southeast Asia travel normalization
LCC utilization recovery
```

But that is not enough for C29. The real bridge is:

```text
load factor + yield + fuel/FX + maintenance + safety + balance sheet
```

Jeju Air failed the forward price test badly.

### Price path

Key Stock-Web rows:

```text
2024-01-18: close 13,490
2024-01-18: high 13,590
2024-02-13: low 11,310 / close 11,470
2024-04-01: high 11,550 / close 11,540
2024-07-08: close 10,000
2024-08-05: low 8,300 / close 8,770
2024-10-30: high 9,610 / close 9,560
2024-12-30: low 6,920 / close 7,500
2025-04-09: low 6,260 / close 6,280
```

Approximate path from 2024-01-18 close:

```text
entry_close: 13,490
180D_peak_high: 13,590
180D_MFE: +0.7%
180D_worst_low: 8,300
180D_MAE: -38.5%
extended_low_after_crash_period: 6,260
extended_MAE: -53.5%
```

### Interpretation

This is a hard C29 false-positive guard.

```text
Stage2-Watch: possible from traffic recovery.
Stage2-Actionable: blocked without yield/margin bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

Even before the later crash-period pressure, the 180D window already failed. The later aviation-safety shock only underlines why LCC volume recovery must never be separated from safety, balance-sheet, and margin risk.

### Stress-test components

```text
raw_component_score_proxy:
  passenger_recovery_headline: medium_high
  yield_visibility: low
  fuel_fx_sensitivity: high
  balance_sheet_risk: medium_high
  safety_event_tail_risk: high
  price_confirmation: failed
  drawdown_penalty: extreme
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The airline C29 grid:

```text
091810 티웨이항공:
  route/capacity bridge can create a valid positive,
  but Green requires yield/load-factor/cost conversion and local 4B after route-speculation spike.

003490 대한항공:
  consolidation completion is strategic,
  but trigger-level Actionable/Green needs integration and margin bridge.

089590 제주항공:
  LCC traffic recovery headline without margin/safety bridge is a hard false-positive.
```

The shared rule:

```text
C29 airline is not "traffic is back."
C29 airline is "traffic + yield + load factor + cost/fuel/FX + safety/balance-sheet + OP/EPS conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L90_091810_2024_03_07","scheduled_round":"R9","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE","symbol":"091810","name":"티웨이항공","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":2770,"peak_high":3950,"peak_date":"2024-10-11","worst_low":2305,"worst_low_date":"2024-08-05","mfe_pct":42.6,"mae_pct":-16.8,"peak_to_post_peak_low_pct":-26.1,"classification":"positive_with_local_4b_watch","calibration_usable":true,"evidence_family":"eu_route_remedy_capacity_support_airline_operating_leverage","residual_error":"positive_route_bridge_needs_yield_cost_and_local_4b_guard","shadow_rule_candidate":"allow_actionable_for_specific_route_capacity_bridge_but_require_yield_cost_op_bridge_for_green"}
{"row_type":"case","case_id":"C29_R9L90_003490_2024_12_12","scheduled_round":"R9","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE","symbol":"003490","name":"대한항공","trigger_date":"2024-12-12","entry_date":"2024-12-12","entry_price":24200,"early_peak_high":24950,"early_peak_date":"2025-02-27","worst_low":19990,"worst_low_date":"2025-04-09","later_peak_high":26750,"later_peak_date":"2025-07-14","early_mfe_pct":3.1,"mae_pct":-17.4,"later_mfe_pct":10.5,"classification":"counterexample_consolidation_headline_without_immediate_operating_leverage","calibration_usable":true,"evidence_family":"airline_merger_completion_integration_synergy_bridge","residual_error":"strategic_consolidation_headline_can_overpromote_without_integration_margin_bridge","shadow_rule_candidate":"cap_merger_completion_at_watch_until_integration_yield_cost_synergy_bridge_confirms"}
{"row_type":"case","case_id":"C29_R9L90_089590_2024_01_18","scheduled_round":"R9","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE","symbol":"089590","name":"제주항공","trigger_date":"2024-01-18","entry_date":"2024-01-18","entry_price":13490,"peak_high":13590,"peak_date":"2024-01-18","worst_low_180d":8300,"worst_low_180d_date":"2024-08-05","extended_worst_low":6260,"extended_worst_low_date":"2025-04-09","mfe_pct":0.7,"mae_pct":-38.5,"extended_mae_pct":-53.5,"classification":"hard_4c_candidate_lcc_traffic_recovery_without_margin_safety_bridge","calibration_usable":true,"evidence_family":"lcc_passenger_recovery_without_margin_safety_bridge","residual_error":"generic_lcc_traffic_recovery_can_be_catastrophic_false_positive","shadow_rule_candidate":"block_actionable_green_for_lcc_recovery_without_yield_cost_balance_sheet_safety_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":90,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AIRLINE_TRAFFIC_YIELD_INTEGRATION_OPERATING_LEVERAGE_BRIDGE_VS_PASSENGER_RECOVERY_AND_ROUTE_HEADLINE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":90,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_AIRLINE_VOLUME_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 airline/transport names, do not open Stage2-Actionable or Stage3-Green from passenger recovery, route launch, or merger completion headline alone. Require traffic volume plus yield/load factor, fuel/FX/cost bridge, utilization, safety/balance-sheet check, and OP/EPS conversion. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If route-specific MFE is large but volatile, attach local 4B watch.","expected_effect":"Reduce airline mobility false positives while preserving route/capacity positives with real operating leverage bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":90,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"airline_transport_operating_leverage_guard","contribution":"Adds three airline/transport C29 cases to separate traffic or route headlines from yield, cost, safety, and operating leverage conversion.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_AIRLINE_VOLUME_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [airline, LCC, airport/route transport, passenger mobility]:

  Do not open Stage3-Green from:
    - passenger recovery headline alone
    - new route or slot headline alone
    - merger/integration completion headline alone
    - LCC consolidation expectation alone
    - one-day traffic or booking headline alone

  Require at least two of:
    - load factor / traffic volume confirmation
    - yield / fare / cargo mix confirmation
    - fuel and FX cost bridge
    - aircraft utilization / route economics
    - balance-sheet and lease burden check
    - safety or operational risk check
    - OP/EPS/FCF conversion evidence
    - price path survival after the first traffic headline

  If MFE < 10% and MAE < -20%:
    route to C29 false-positive / hard-4C candidate.

  If MFE > 30% but post-peak drawdown > -20%:
    preserve positive entry classification but attach local 4B watch.

  For merger/integration headlines:
    cap at Watch/Yellow until synergy, cost, and capacity optimization bridge is explicit.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 airline/transport cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_AIRLINE_VOLUME_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 airline cases agree, consider implementing a canonical guard that:
   - blocks passenger recovery / route / merger headlines from Green without yield-cost-OP bridge,
   - allows route-specific Actionable when capacity and price confirmation are real,
   - attaches local 4B after route-speculation blowoff,
   - routes shallow-MFE/high-MAE airline cases to false-positive or hard-4C.

Expected next schedule:
completed_round = R9
completed_loop = 90
next_round = R10
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
