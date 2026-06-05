# E2R Stock-Web v12 Residual Research — R9 / Loop 94

```yaml
scheduled_round: R9
scheduled_loop: 94
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE

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
completed_loop: 94
next_round: R10
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_94_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 94
```

R9 can use:

```text
L3_BATTERY_EV_GREEN_MOBILITY
```

when the case is mobility / auto / transport in nature. This run therefore uses:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

The selected fine branch is:

```text
auto component / powertrain / interior / NVH
volume and margin bridge
vs generic auto-parts theme spike
```

This deliberately avoids the prior R9 loop93 auto-logistics / car-carrier / parcel / shipping branch and the loop92 auto-parts/tire/ADAS branch.

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
```

Selected symbols:

```text
092200 디아이씨
067570 엔브이에이치코리아
024900 덕양산업 / 디와이덕양
```

They avoid the C29 top-covered list and avoid recent R9 loop88~93 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
092200: same archetype, new symbol, powertrain / drivetrain component local-positive with 4B after later drawdown
067570: same archetype, new symbol, NVH / interior / thermal-auto-component Watch cap without strong volume-margin bridge
024900: same archetype, new symbol, auto interior / cockpit module late spike hard-4C without durable volume-margin bridge
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
092200 디아이씨
  profile: atlas/symbol_profiles/092/092200.json
  first_date: 2007-10-18
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,514
  non_tradable_zero_volume rows: 9
  corporate_action_candidate_dates:
    2008-05-14, 2019-08-28
  2024 entry~D+180 contamination: none
  status_inferred: active_like

067570 엔브이에이치코리아
  profile: atlas/symbol_profiles/067/067570.json
  first_date: 2013-12-03
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,997
  corporate_action_candidate_dates:
    2023-08-16
  2024 entry~D+180 contamination: none
  status_inferred: active_like

024900 덕양산업 / 디와이덕양
  profile: atlas/symbol_profiles/024/024900.json
  name history:
    덕양산업 until 2025-04-16
    디와이덕양 from 2025-04-17
  first_date: 1996-07-30
  last_date: 2026-02-20
  market:
    KOSDAQ until 1997-06-21
    KOSPI from 1997-06-23
  tradable_ohlcv rows: 7,178
  non_tradable_zero_volume rows: 244
  corporate_action_candidate_dates:
    1997-06-23, 1998-12-24, 1999-01-28, 2014-10-23
  2024 entry~D+180 contamination: none
  status_inferred: active_like
```

---

## 4. Archetype residual problem

C29 is about mobility volume, rate, utilization, cost pass-through, and operating leverage. It is not a generic "auto parts stock" or "EV component label" archetype.

The model can over-score:

```text
auto-parts label
EV component sympathy
interior / cockpit module label
NVH / thermal / soundproofing label
powertrain / reducer / drivetrain label
OEM production rebound
one-week auto-parts volume spike
```

The C29 bridge must be stricter:

```text
mobility / auto production event
  -> company-specific OEM volume
  -> model or platform allocation
  -> take-rate / content per vehicle
  -> utilization and fixed-cost absorption
  -> raw-material / labor / FX cost pass-through
  -> margin / OP conversion
  -> price survival after the first auto-parts rally
```

An auto-parts thesis is like a supplier on an assembly line. The carmaker's line may speed up, but C29 asks whether this supplier's part is on that model, ships in volume, captures content per vehicle, and keeps margin after labor and material cost.

---

## 5. Case 1 — 092200 디아이씨

```yaml
case_id: C29_R9L94_092200_2024_02_01
symbol: "092200"
name: "디아이씨"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4350
classification: positive_powertrain_drivetrain_component_volume_margin_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

디아이씨 is the constructive control in this auto-component set.

The useful C29 read is not simply:

```text
자동차 부품주가 올랐다
```

It is:

```text
powertrain / drivetrain component relevance
  -> OEM production and platform-volume readthrough
  -> component shipment / content-per-vehicle bridge
  -> price confirmation
```

The stock produced a meaningful MFE after the February trigger and later held materially above the August market shock low. But because the move later faded, it still needs 4B discipline unless fresh order, volume, or margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 4,350
2024-02-14: high 5,240 / close 5,050
2024-03-29: high 5,690 / close 5,630
2024-04-22: high 6,300 / close 6,180
2024-08-05: low 3,720 / close 3,800
2024-10-22: low 3,635 / close 3,650
2024-11-07: low 3,515 / close 3,680
```

Approximate path from entry close:

```text
entry_close: 4,350
peak_high: 6,300
MFE: +44.8%
worst_low_after_entry: 3,515
MAE: -19.2%
```

### Interpretation

This is a C29 positive with 4B watch:

```text
Stage2-Actionable: valid if OEM volume, component shipment, and margin bridge are explicit.
Stage3-Green: possible only with sustained platform allocation, utilization, and OP evidence.
Local 4B: required after +40% MFE and later material drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  auto_component_relevance: high
  powertrain_drivetrain_bridge: medium_high
  oem_volume_bridge: medium
  margin_cost_pass_through_bridge: medium
  price_confirmation: high
  later_drawdown_penalty: medium
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 067570 엔브이에이치코리아

```yaml
case_id: C29_R9L94_067570_2024_02_05
symbol: "067570"
name: "엔브이에이치코리아"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE
trigger_date: 2024-02-05
entry_date: 2024-02-05
entry_price_basis: close
entry_price: 2610
classification: watch_cap_nvh_interior_auto_component_label_without_strong_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

엔브이에이치코리아 is the Watch/Yellow cap case.

The label is plausible:

```text
NVH / interior / thermal or soundproofing component
  -> OEM production recovery
  -> EV and auto-part content-per-vehicle readthrough
```

But the price path did not validate Actionable/Green. It had a small initial spike and then accumulated a material drawdown. The later August rally was useful, but from the February entry the bridge was not strong enough.

### Price path

Key Stock-Web rows:

```text
2024-02-05: close 2,610
2024-02-06: high 2,895 / close 2,595
2024-03-19: low 2,445 / close 2,455
2024-04-17: low 2,410 / close 2,430
2024-08-05: low 2,035 / close 2,350
2024-08-20: high 2,835 / close 2,655
2024-10-25: low 2,410 / close 2,440
```

Approximate path from entry close:

```text
entry_close: 2,610
peak_high: 2,895
MFE: +10.9%
worst_low_after_entry: 2,035
MAE: -22.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from auto-component and NVH/interior relevance.
Stage2-Actionable: blocked unless OEM volume, platform allocation, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MFE was above 10% and MAE did not cross the hard threshold.
```

The lesson is that content-per-vehicle adjacency is not operating leverage unless utilization and margin are visible.

### Stress-test components

```text
raw_component_score_proxy:
  nvh_interior_component_relevance: medium_high
  oem_volume_bridge: weak_to_medium
  content_per_vehicle_bridge: weak_to_medium
  utilization_margin_bridge: weak
  price_confirmation: shallow_to_medium
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 024900 덕양산업 / 디와이덕양

```yaml
case_id: C29_R9L94_024900_2024_04_15
symbol: "024900"
name_at_trigger: "덕양산업"
current_or_latest_name: "디와이덕양"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE
trigger_date: 2024-04-15
entry_date: 2024-04-15
entry_price_basis: close
entry_price: 5720
classification: hard_4c_candidate_auto_interior_cockpit_module_late_spike_without_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

덕양산업 is the hard guardrail case.

The trigger had exactly the trap shape:

```text
auto interior / cockpit module label
  -> EV and smart-mobility parts sympathy
  -> high-volume one-day spike
  -> model could read the move as operating leverage
```

But from the close after the spike, the stock produced almost no additional MFE and then suffered a severe drawdown. This should be routed to hard-4C unless company-specific OEM volume, platform allocation, and margin evidence exists.

### Price path

Key Stock-Web rows:

```text
2024-04-12: close 4,600
2024-04-15: high 5,980 / close 5,720
2024-04-16: high 5,910 / close 5,480
2024-05-09: low 4,885 / close 4,885
2024-08-05: low 2,990 / close 3,155
2024-08-20: high 4,735 / close 4,245
2024-10-24: low 3,180 / close 3,200
```

Approximate path from entry close:

```text
entry_close: 5,720
peak_high_after_entry: 5,980
MFE: +4.5%
worst_low_after_entry: 2,990
MAE: -47.7%
```

### Interpretation

This is a hard C29 false-positive:

```text
Stage2-Watch: possible from cockpit/interior module and EV-parts relevance.
Stage2-Actionable: blocked unless platform-volume and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and very large MAE.
```

The lesson is that auto interior theme heat is not OEM volume-margin conversion.

### Stress-test components

```text
raw_component_score_proxy:
  auto_interior_label: high
  ev_parts_theme_sympathy: high
  platform_volume_bridge: weak
  margin_cost_pass_through_bridge: weak
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
calibration_usable_trigger_count: 3
```

The three-case C29 auto-component grid:

```text
092200 디아이씨:
  powertrain / drivetrain component positive;
  strong MFE came first, but later drawdown requires 4B.

067570 엔브이에이치코리아:
  NVH / interior auto-component relevance;
  modest MFE and material MAE, Watch/Yellow cap.

024900 덕양산업 / 디와이덕양:
  auto interior / cockpit module late spike failed;
  shallow MFE and severe MAE, hard 4C.
```

Shared rule:

```text
C29 is not "auto-parts label."
C29 is "OEM volume, platform allocation, content per vehicle, utilization, cost pass-through, and margin conversion are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L94_092200_2024_02_01","scheduled_round":"R9","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE","symbol":"092200","name":"디아이씨","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4350,"peak_high":6300,"peak_date":"2024-04-22","worst_low_after_entry":3515,"worst_low_after_entry_date":"2024-11-07","mfe_pct":44.8,"mae_pct":-19.2,"classification":"positive_powertrain_drivetrain_component_volume_margin_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"powertrain_drivetrain_component_oem_volume_margin_bridge","residual_error":"positive_auto_component_path_requires_4b_after_large_mfe_without_fresh_volume_margin_evidence","shadow_rule_candidate":"preserve_positive_when_platform_volume_and_margin_bridge_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C29_R9L94_067570_2024_02_05","scheduled_round":"R9","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE","symbol":"067570","name":"엔브이에이치코리아","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":2610,"peak_high":2895,"peak_date":"2024-02-06","worst_low_after_entry":2035,"worst_low_after_entry_date":"2024-08-05","mfe_pct":10.9,"mae_pct":-22.0,"classification":"watch_cap_nvh_interior_auto_component_label_without_strong_volume_margin_bridge","calibration_usable":true,"evidence_family":"nvh_interior_thermal_component_label_without_strong_oem_volume_margin_bridge","residual_error":"content_per_vehicle_adjacency_can_overpromote_without_platform_allocation_and_utilization_margin","shadow_rule_candidate":"cap_nvh_interior_auto_component_label_at_watch_yellow_if_mfe_modest_and_margin_bridge_missing"}
{"row_type":"case","case_id":"C29_R9L94_024900_2024_04_15","scheduled_round":"R9","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE","symbol":"024900","name_at_trigger":"덕양산업","current_or_latest_name":"디와이덕양","trigger_date":"2024-04-15","entry_date":"2024-04-15","entry_price":5720,"peak_high":5980,"peak_date":"2024-04-15","worst_low_after_entry":2990,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.5,"mae_pct":-47.7,"classification":"hard_4c_candidate_auto_interior_cockpit_module_late_spike_without_volume_margin_survival","calibration_usable":true,"evidence_family":"auto_interior_cockpit_module_theme_spike_without_platform_volume_margin_bridge","residual_error":"auto_interior_theme_heat_can_fail_when_oem_volume_and_margin_conversion_missing","shadow_rule_candidate":"route_auto_interior_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_volume_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":94,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_COMPONENT_POWERTRAIN_INTERIOR_NVH_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":94,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_AUTO_COMPONENT_PLATFORM_VOLUME_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 auto-component names, do not open Stage2-Actionable or Stage3-Green from auto-parts, EV component, interior/cockpit, NVH/thermal, powertrain/drivetrain, OEM production rebound, or one-week auto-parts spike labels alone. Require company-specific OEM volume, model/platform allocation, take-rate or content per vehicle, utilization and fixed-cost absorption, raw-material/labor/FX cost pass-through, margin/OP conversion, and post-trigger price survival. Powertrain/drivetrain positives with large MFE should attach local 4B unless fresh volume and margin evidence appears. NVH/interior names with modest MFE and material MAE should cap at Watch/Yellow without platform allocation evidence. Auto-interior late spikes with shallow MFE and large MAE should route to hard-4C when OEM volume and margin bridge are missing.","expected_effect":"Preserve true auto-component operating-leverage positives while reducing auto-parts label and EV-component theme false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":94,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"auto_component_platform_volume_margin_guard","contribution":"Adds one powertrain component positive with 4B watch, one NVH/interior Watch cap, and one auto-interior late-spike hard-4C counterexample to calibrate C29 auto-component volume and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_AUTO_COMPONENT_PLATFORM_VOLUME_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [auto_component, powertrain, drivetrain, interior, cockpit_module, nvh, thermal_component]:

  Do not open Stage3-Green from:
    - auto-parts label alone
    - EV component sympathy alone
    - interior / cockpit module label alone
    - NVH / thermal / soundproofing label alone
    - powertrain / drivetrain label alone
    - OEM production rebound headline alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - company-specific OEM volume growth
    - model / platform allocation
    - take-rate or content-per-vehicle increase
    - utilization / fixed-cost absorption
    - raw-material / labor / FX cost pass-through
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the auto-parts headline

  If MFE < 10% and MAE < -30%:
    route to C29 hard-4C candidate.

  If MFE > 30% but later MAE is material:
    preserve positive classification but attach local 4B unless fresh volume/margin evidence appears.

  If MFE is modest and platform/margin bridge is weak:
    cap at Watch/Yellow.

  Distinguish:
    - suppliers with visible platform volume and content-per-vehicle leverage
    - from auto-parts theme spikes where OEM line speed does not translate into margin.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_94_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 auto-component platform-volume/margin cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_AUTO_COMPONENT_PLATFORM_VOLUME_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 auto-component cases agree, consider implementing a canonical guard that:
   - blocks auto-parts Green without OEM volume/platform/content-per-vehicle/margin bridge,
   - preserves powertrain/drivetrain positives only with price survival and margin evidence,
   - attaches local 4B after large MFE with later drawdown,
   - caps NVH/interior labels at Watch/Yellow without platform allocation evidence,
   - routes shallow-MFE/high-MAE interior/cockpit late spikes to hard-4C.

Expected next schedule:
completed_round = R9
completed_loop = 94
next_round = R10
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 94
next_round = R10
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
