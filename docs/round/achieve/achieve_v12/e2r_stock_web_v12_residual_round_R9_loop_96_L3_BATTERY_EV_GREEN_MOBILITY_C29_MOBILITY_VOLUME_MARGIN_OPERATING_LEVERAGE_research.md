# E2R Stock-Web v12 Residual Research — R9 / Loop 96

```yaml
scheduled_round: R9
scheduled_loop: 96
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL

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
auto_interior_case_count: 1
ev_drivetrain_case_count: 1
small_auto_parts_case_count: 1
customer_volume_margin_bridge_missing_count: 2
row_presence_or_tradeability_caveat_count: 1
name_history_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 96
next_round: R10
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_96_L8_PLATFORM_CONTENT_SW_SECURITY_C28_SOFTWARE_SECURITY_CONTRACT_RETENTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 96
```

R9 can use the mobility branch under L3 when the cases are auto / mobility / transport in nature. This run uses:

```text
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

The selected fine branch is:

```text
auto interior / EV drivetrain / small auto parts
OEM customer volume, model mix, utilization, cost pass-through, and margin bridge
vs generic auto-parts label reversal
```

This deliberately avoids:
- loop95 rental / used-car / car-sharing C29 branch;
- loop94 auto component / powertrain / interior / NVH C29 branch;
- loop93 auto-logistics / car-carrier / parcel / shipping C29 branch;
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
loop95: 089860, 381970, 403550
```

Selected symbols:

```text
200880 서연이화
064960 SNT모티브
053270 구영테크
```

They avoid the C29 top-covered list and avoid recent R9 loop88~95 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
200880: same archetype, new symbol, auto interior / OEM-volume local positive with later 4B after customer-volume margin bridge decayed
064960: same archetype, new symbol, EV drivetrain / motor-component Watch cap without strong incremental customer-volume margin bridge
053270: same archetype, new symbol, small auto-parts event spike hard-4C candidate with row/tradeability caveat
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
200880 서연이화
  profile: atlas/symbol_profiles/200/200880.json
  name history:
    한일이화 until 2016-01-13
    서연이화 from 2016-01-14
  first_date: 2014-08-08
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,829
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

064960 SNT모티브
  profile: atlas/symbol_profiles/064/064960.json
  name history:
    대우정밀 -> S&T대우 -> S&T모티브 -> SNT모티브
  selected 2024 trigger name:
    SNT모티브
  first_date: 2002-03-11
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 5,911
  corporate_action_candidate_dates:
    historical only, none in 2024 validation window
  2024 entry~D+180 contamination: none

053270 구영테크
  profile: atlas/symbol_profiles/053/053270.json
  first_date: 2002-02-07
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,927
  non_tradable_zero_volume rows: 2
  corporate_action_candidate_dates:
    2004-01-13, 2005-11-25, 2018-10-01
  2024 entry~D+180 contamination: none
  caveat:
    historical raw-discontinuity and row-presence caveat exists outside the selected 2024 validation window.
```

---

## 4. Archetype residual problem

C29 is about mobility volume, utilization, and margin. It is not a generic "auto parts stock moved" archetype.

The model can over-score:

```text
auto-parts label
interior / seat / trim / NVH label
EV drivetrain or motor-component label
global OEM volume recovery
hybrid / EV model mix headline
low-PBR auto-parts rerating
one-week auto-parts volume spike
```

The C29 bridge must be stricter:

```text
auto / mobility / parts event
  -> named OEM or model channel
  -> order visibility or production schedule
  -> customer volume and utilization
  -> model mix and ASP
  -> raw-material and labor cost pass-through
  -> FX / logistics / warranty risk
  -> inventory and working-capital burden
  -> margin / OP conversion
  -> price survival after the first auto-parts spike
```

An auto-parts thesis is like a seat frame on an assembly line. The label says a car is being built, but C29 asks whether this supplier is on the actual model, whether the OEM volume comes through, whether material and labor cost are passed through, and whether the part leaves margin after logistics and warranty.

---

## 5. Case 1 — 200880 서연이화

```yaml
case_id: C29_R9L96_200880_2024_02_01
symbol: "200880"
name: "서연이화"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 18000
classification: local_positive_auto_interior_oem_volume_mix_margin_bridge_with_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

서연이화 is the auto-interior local-positive case.

The useful C29 read is not simply:

```text
자동차 부품주가 강하다
```

It is:

```text
auto interior / module supplier relevance
  -> OEM volume and model-mix leverage
  -> utilization and cost pass-through optionality
  -> strong early price confirmation
```

The forward path produced a large early MFE in February. However, the later price path failed to preserve the move, especially through the August shock and subsequent September weakness. Therefore this is a local positive with 4B discipline, not a durable Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 18,320 / close 18,000
2024-02-02: high 23,150 / close 22,450
2024-02-05: high 24,400 / close 23,100
2024-02-07: high 25,000 / close 22,550
2024-03-11: low 18,500 / close 18,530
2024-08-05: low 12,610 / close 13,150
2024-09-11: low 12,550 / close 12,570
2024-10-25: low 13,260 / close 13,310
```

Approximate path from entry close:

```text
entry_close: 18,000
peak_high: 25,000
MFE: +38.9%
worst_low_after_entry: 12,550
MAE: -30.3%
```

### Interpretation

This is a C29 local positive / 4B failure:

```text
Stage2-Watch: valid from auto-interior and OEM-volume relevance.
Stage2-Actionable: possible only if customer volume, model mix, utilization, and pass-through margin bridge are explicit.
Stage3-Green: blocked after later high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original trigger because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  auto_interior_relevance: high
  oem_volume_bridge: medium_high
  model_mix_bridge: medium
  cost_pass_through_bridge: weak_to_medium
  price_confirmation: high_initial
  margin_survival: failed_later
  local_4b_overlay: required
```

---

## 6. Case 2 — 064960 SNT모티브

```yaml
case_id: C29_R9L96_064960_2024_02_01
symbol: "064960"
name: "SNT모티브"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 44600
classification: watch_cap_ev_drivetrain_motor_component_label_without_strong_incremental_customer_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

SNT모티브 is the EV drivetrain / motor-component Watch cap.

The label is relevant:

```text
motor / drivetrain / automotive component
  -> EV and hybrid model-mix optionality
  -> OEM volume and customer-program readthrough
  -> stable quality component franchise
```

The price path was better than a failure case, but it did not justify unrestricted Actionable/Green from the selected entry. MFE was modest and the August drawdown was controlled but real. This should be a Watch/Yellow cap unless incremental customer program, delivery, utilization, and margin evidence is explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 45,950 / close 44,600
2024-03-06: high 46,850 / close 46,650
2024-04-30: high 46,650 / close 46,400
2024-08-05: low 39,500 / close 39,900
2024-08-20: high 48,500 / close 47,500
2024-09-12: high 49,650 / close 47,200
2024-10-25: low 45,750 / close 46,050
```

Approximate path from entry close:

```text
entry_close: 44,600
peak_high: 49,650
MFE: +11.3%
worst_low_after_entry: 39,500
MAE: -11.4%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from EV drivetrain and component relevance.
Stage2-Actionable: blocked unless OEM program, volume, delivery, cost pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no.
```

The lesson is that high-quality component relevance is not automatically incremental operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  ev_drivetrain_component_relevance: high
  oem_program_bridge: weak_to_medium
  volume_utilization_bridge: medium
  cost_pass_through_bridge: medium
  price_confirmation: modest
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 053270 구영테크

```yaml
case_id: C29_R9L96_053270_2024_03_08
symbol: "053270"
name: "구영테크"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL
trigger_date: 2024-03-08
entry_date: 2024-03-08
entry_price_basis: close
entry_price: 2880
classification: hard_4c_candidate_small_auto_parts_event_spike_without_customer_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

구영테크 is the small auto-parts hard guardrail.

The setup can fool a mobility model:

```text
small auto-parts supplier
  -> auto-parts sympathy
  -> OEM volume or EV/hybrid readthrough
  -> one-day volume spike
```

But from the selected event-spike close, the price path delivered only shallow MFE and then moved into a hard-failure drawdown zone by August. The bridge from auto-parts label to named customer volume, utilization, cost pass-through, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-03-08: high 3,170 / close 2,880
2024-03-12: low 2,850 / close 2,850
2024-04-08: low 2,645 / close 2,665
2024-08-05: low 1,998 / close 2,025
2024-08-29: high 2,650 / close 2,650
2024-10-21: high 2,720 / close 2,490
2024-10-25: low 2,215 / close 2,215
```

Approximate path from event-spike close:

```text
entry_close: 2,880
peak_high_after_entry: 3,170
MFE: +10.1%
worst_low_after_entry: 1,998
MAE: -30.6%
```

### Interpretation

This is a hard C29 false-positive candidate:

```text
Stage2-Watch: possible from small auto-parts and customer-volume relevance.
Stage2-Actionable: blocked unless named OEM, order/production schedule, utilization, pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and -30%+ MAE.
Row/tradeability caveat: minor historical raw-discontinuity / zero-volume caveat exists outside the 2024 validation window.
```

The lesson is that a small auto-parts spike is not customer-volume margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  small_auto_parts_label: high
  oem_volume_readthrough: medium
  customer_program_bridge: weak
  cost_pass_through_bridge: weak
  margin_op_bridge: weak
  price_confirmation_after_entry: shallow
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
auto_interior_case_count: 1
ev_drivetrain_case_count: 1
small_auto_parts_case_count: 1
customer_volume_margin_bridge_missing_count: 2
row_presence_or_tradeability_caveat_count: 1
name_history_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C29 auto-parts grid:

```text
200880 서연이화:
  auto interior / OEM-volume local positive;
  meaningful MFE first, then high MAE, local 4B failure.

064960 SNT모티브:
  EV drivetrain / motor-component relevance;
  modest MFE and controlled MAE, Watch/Yellow cap.

053270 구영테크:
  small auto-parts event spike failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C29 is not "auto-parts label is hot."
C29 is "customer volume, model mix, utilization, pass-through, working capital, warranty/logistics, and margin conversion are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L96_200880_2024_02_01","scheduled_round":"R9","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL","symbol":"200880","name":"서연이화","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":18000,"peak_high":25000,"peak_date":"2024-02-07","worst_low_after_entry":12550,"worst_low_after_entry_date":"2024-09-11","mfe_pct":38.9,"mae_pct":-30.3,"classification":"local_positive_auto_interior_oem_volume_mix_margin_bridge_with_4b_after_later_mae","calibration_usable":true,"evidence_family":"auto_interior_oem_volume_model_mix_cost_pass_through_margin_bridge","residual_error":"auto_interior_volume_positive_requires_4b_after_high_mae_when_margin_bridge_not_refreshed","shadow_rule_candidate":"preserve_auto_parts_local_positive_but_attach_4b_after_large_mfe_followed_by_high_mae"}
{"row_type":"case","case_id":"C29_R9L96_064960_2024_02_01","scheduled_round":"R9","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL","symbol":"064960","name":"SNT모티브","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":44600,"peak_high":49650,"peak_date":"2024-09-12","worst_low_after_entry":39500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":11.3,"mae_pct":-11.4,"classification":"watch_cap_ev_drivetrain_motor_component_label_without_strong_incremental_customer_volume_margin_bridge","calibration_usable":true,"name_history_caveat":true,"evidence_family":"ev_drivetrain_motor_component_label_without_incremental_oem_program_volume_margin_bridge","residual_error":"high_quality_ev_component_relevance_can_overpromote_without_incremental_customer_program_and_margin_evidence","shadow_rule_candidate":"cap_ev_drivetrain_component_label_at_watch_yellow_if_mfe_modest_and_customer_volume_bridge_missing"}
{"row_type":"case","case_id":"C29_R9L96_053270_2024_03_08","scheduled_round":"R9","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL","symbol":"053270","name":"구영테크","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":2880,"peak_high":3170,"peak_date":"2024-03-08","worst_low_after_entry":1998,"worst_low_after_entry_date":"2024-08-05","mfe_pct":10.1,"mae_pct":-30.6,"classification":"hard_4c_candidate_small_auto_parts_event_spike_without_customer_volume_margin_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"small_auto_parts_event_spike_without_named_oem_volume_utilization_cost_pass_through_margin_bridge","residual_error":"small_auto_parts_label_can_fail_when_customer_volume_and_margin_bridge_missing","shadow_rule_candidate":"route_small_auto_parts_event_spike_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_customer_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":96,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_INTERIOR_EV_DRIVETRAIN_SMALL_PARTS_CUSTOMER_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_REVERSAL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"auto_interior_case_count":1,"ev_drivetrain_case_count":1,"small_auto_parts_case_count":1,"customer_volume_margin_bridge_missing_count":2,"row_presence_or_tradeability_caveat_count":1,"name_history_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":96,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 auto-parts and mobility-supplier cases, do not open Stage2-Actionable or Stage3-Green from auto-parts, interior/seat/trim/NVH, EV drivetrain, motor-component, global OEM volume recovery, hybrid/EV model-mix headline, low-PBR auto-parts rerating, or one-week auto-parts volume spike labels alone. Require named OEM or model channel, order visibility or production schedule, customer volume and utilization, model mix and ASP, raw-material/labor cost pass-through, FX/logistics/warranty risk control, inventory and working-capital burden containment, margin/OP conversion, and post-trigger price survival. Auto-interior positives with meaningful MFE followed by high MAE should remain local 4B unless customer-volume and margin evidence refreshes. EV drivetrain component labels with modest MFE should cap at Watch/Yellow without incremental OEM program evidence. Small auto-parts event spikes with shallow MFE and hard-zone MAE should route to hard-4C when customer-volume and margin bridge are missing.","expected_effect":"Preserve true mobility supplier operating-leverage positives while reducing generic auto-parts, EV-component, and small-parts event-spike false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":96,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"auto_parts_customer_volume_passthrough_margin_guard","contribution":"Adds one auto-interior local positive, one EV drivetrain Watch cap, and one small auto-parts hard-4C candidate to calibrate C29 OEM volume, model mix, pass-through, working-capital, warranty/logistics, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [auto_parts, interior_supplier, ev_drivetrain_component, small_auto_parts_supplier]:

  Do not open Stage3-Green from:
    - auto-parts label alone
    - interior / seat / trim / NVH label alone
    - EV drivetrain / motor-component label alone
    - global OEM volume recovery headline alone
    - hybrid / EV model-mix headline alone
    - low-PBR auto-parts rerating alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - named OEM or model channel
    - order visibility / production schedule
    - customer volume and utilization
    - model mix / ASP improvement
    - raw-material and labor cost pass-through
    - FX / logistics / warranty risk containment
    - inventory / working-capital burden control
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the auto-parts headline

  If MFE < 12% and MAE <= -30%:
    route to C29 hard-4C candidate.

  If MFE > 20% but later MAE is high:
    preserve as local 4B / event burst, not Green, unless customer-volume and margin evidence appears.

  If MFE is modest and the bridge is component-quality only:
    cap at Watch/Yellow.

  Distinguish:
    - suppliers where OEM volume and model mix become utilization and margin
    - from auto-parts labels where cost, warranty, logistics, or working capital breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_96_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 auto-parts / mobility-supplier cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 cases agree, consider implementing a canonical guard that:
   - blocks auto-parts Green without named OEM/model, production schedule, customer volume, pass-through, and margin bridge,
   - preserves auto-interior positives only with price survival and fresh margin evidence,
   - caps EV drivetrain component labels at Watch/Yellow without incremental OEM program evidence,
   - routes shallow-MFE/hard-zone-MAE small auto-parts spikes to hard-4C,
   - applies row-presence/tradeability caveats.

Expected next schedule:
completed_round = R9
completed_loop = 96
next_round = R10
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 96
next_round = R10
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
