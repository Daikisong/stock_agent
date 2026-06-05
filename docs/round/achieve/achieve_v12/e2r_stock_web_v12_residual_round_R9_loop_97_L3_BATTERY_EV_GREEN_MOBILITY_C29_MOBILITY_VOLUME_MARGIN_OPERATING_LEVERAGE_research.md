# E2R Stock-Web v12 Residual Research — R9 / Loop 97

```yaml
scheduled_round: R9
scheduled_loop: 97
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE

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
auto_thermal_control_case_count: 1
aluminum_ev_parts_case_count: 1
rubber_sealing_auto_parts_case_count: 1
customer_volume_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
market_transfer_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R9
completed_loop: 97
next_round: R10
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R9
scheduled_loop = 97
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
```

R9 can use the mobility branch under L3 when the cases are auto / mobility / transport in nature. This run uses:

```text
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
```

The selected fine branch is:

```text
auto thermal control / aluminum EV parts / rubber sealing parts
OEM customer volume, program mix, utilization, raw-material and labor pass-through,
warranty/logistics risk, working capital, and margin bridge
vs generic auto-parts label spike
```

This deliberately avoids:
- loop96 auto interior / EV drivetrain / small-parts set: `200880`, `064960`, `053270`;
- loop95 rental / used-car / car-sharing C29 branch: `089860`, `381970`, `403550`;
- loop94 component / interior / NVH set: `092200`, `067570`, `024900`;
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
loop96: 200880, 064960, 053270
```

Selected symbols:

```text
023800 인지컨트롤스
122350 삼기
013520 화승코퍼레이션
```

They avoid the C29 top-covered list and avoid recent R9 loop88~96 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
023800: same archetype, new symbol, auto thermal-control local positive with later 4B after customer-volume margin bridge decayed
122350: same archetype, new symbol, aluminum / EV auto-parts label hard-4C candidate with row/trust cap
013520: same archetype, new symbol, rubber/sealing auto-parts Watch cap without strong incremental customer-volume margin bridge
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
023800 인지컨트롤스
  profile: atlas/symbol_profiles/023/023800.json
  name history:
    공화 / 인지 / 인지컨트롤스
  first_date: 1996-07-01
  last_date: 2026-02-20
  market:
    KOSDAQ until 1997-06-21
    KOSPI from 1997-06-23
  tradable_ohlcv rows: 7,280
  non_tradable_zero_volume rows: 142
  corporate_action_candidate_dates:
    1997-06-25, 1998-04-27
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / market-transfer / row-presence caveat exists outside selected 2024 validation window.

122350 삼기
  profile: atlas/symbol_profiles/122/122350.json
  name history:
    현대증권스팩1호 -> 삼기오토모티브 -> 삼기
  first_date: 2010-03-19
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,876
  non_tradable_zero_volume rows: 43
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    2012-04-12, 2014-08-12, 2014-09-01
  2024 entry~D+180 contamination: none
  caveat:
    old SPAC/name-change raw-discontinuity and row-presence caveat exists outside selected 2024 validation window.

013520 화승코퍼레이션
  profile: atlas/symbol_profiles/013/013520.json
  name history:
    화승화학 -> 화승알앤에이 -> 화승코퍼레이션
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,737
  non_tradable_zero_volume rows: 27
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1997-12-17, 1999-01-22, 2017-05-18, 2021-03-15
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action and name-history caveats exist outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C29 is about mobility volume, utilization, and margin. It is not a generic "auto parts stock moved" archetype.

The model can over-score:

```text
auto-parts label
thermal management / sensor / control part label
aluminum EV component label
rubber / sealing / weatherstrip / hose label
hybrid / EV model-mix headline
OEM volume recovery headline
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

An auto-parts thesis is like a thermal valve or sealing strip sitting on the assembly line. The part looks essential, but equity value appears only when the part is on the actual model, the OEM volume arrives, material and labor inflation are passed through, and warranty/logistics do not swallow the margin.

---

## 5. Case 1 — 023800 인지컨트롤스

```yaml
case_id: C29_R9L97_023800_2024_02_01
symbol: "023800"
name: "인지컨트롤스"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 7500
classification: local_positive_auto_thermal_control_oem_volume_mix_margin_bridge_with_4b_after_later_mae
calibration_usable: true
```

### Evidence interpretation

인지컨트롤스 is the auto thermal-control local-positive case.

The useful C29 read is not simply:

```text
자동차 부품주가 강하다
```

It is:

```text
thermal-control / electronic-control auto component relevance
  -> OEM model volume and program-mix readthrough
  -> utilization and cost pass-through optionality
  -> strong February price confirmation
```

The forward path produced a large local MFE in February. However, the move did not survive the later year; August and September price action showed that customer-volume and margin evidence did not refresh enough for durable Green. This is a local positive with 4B discipline.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,530 / close 7,500
2024-02-07: high 8,210 / close 8,020
2024-02-15: high 10,070 / close 9,090
2024-04-17: low 7,530 / close 7,560
2024-08-05: low 5,510 / close 5,770
2024-09-09: low 5,820 / close 5,950
2024-10-17: high 6,990 / close 6,520
```

Approximate path from entry close:

```text
entry_close: 7,500
peak_high: 10,070
MFE: +34.3%
worst_low_after_entry: 5,510
MAE: -26.5%
```

### Interpretation

This is a C29 local positive / 4B failure:

```text
Stage2-Watch: valid from thermal-control and OEM-volume relevance.
Stage2-Actionable: possible only if OEM model, production schedule, volume, utilization, and pass-through margin bridge are explicit.
Stage3-Green: blocked after later material-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  thermal_control_component_relevance: high
  oem_program_bridge: medium_high
  volume_utilization_bridge: medium
  cost_pass_through_bridge: weak_to_medium
  warranty_logistics_bridge: weak_to_medium
  price_confirmation: high_initial
  margin_survival: failed_later
  local_4b_overlay: required
```

---

## 6. Case 2 — 122350 삼기

```yaml
case_id: C29_R9L97_122350_2024_02_01
symbol: "122350"
name: "삼기"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 2015
classification: hard_4c_candidate_aluminum_ev_auto_parts_label_without_customer_volume_margin_survival
calibration_usable: true
```

### Evidence interpretation

삼기 is the aluminum / EV auto-parts hard C29 guardrail.

The label can fool the model:

```text
aluminum die-casting / EV component
auto-parts sympathy
customer-volume or model-mix readthrough
small-cap auto-parts event beta
```

But from the selected February entry, the forward path produced shallow MFE and then a hard-zone drawdown. The bridge from EV/aluminum component relevance to named customer program, production schedule, utilization, pass-through, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 2,020 / close 2,015
2024-02-02: high 2,150 / close 2,100
2024-05-08: high 2,170 / close 2,035
2024-08-05: low 1,320 / close 1,345
2024-09-13: high 1,770 / close 1,512
2024-10-23: high 1,900 / close 1,555
2024-10-29: low 1,410 / close 1,427
```

Approximate path from entry close:

```text
entry_close: 2,015
peak_high_after_entry: 2,170
MFE: +7.7%
worst_low_after_entry: 1,320
MAE: -34.5%
```

### Interpretation

This is a hard C29 false-positive candidate:

```text
Stage2-Watch: possible from aluminum / EV component relevance.
Stage2-Actionable: blocked unless named OEM, order/program volume, utilization, pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and -30%+ MAE.
Row/tradeability caveat: yes.
```

The lesson is that EV aluminum component salience is not customer-volume margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  aluminum_ev_component_label: high
  oem_volume_readthrough: medium
  customer_program_bridge: weak
  cost_pass_through_bridge: weak
  working_capital_margin_bridge: weak
  price_confirmation_after_entry: shallow
  row_trust_caveat: medium
  hard_4c_guard: yes
```

---

## 7. Case 3 — 013520 화승코퍼레이션

```yaml
case_id: C29_R9L97_013520_2024_02_01
symbol: "013520"
name: "화승코퍼레이션"
canonical_archetype_id: C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id: AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 2285
classification: watch_cap_rubber_sealing_auto_parts_label_without_strong_incremental_oem_volume_margin_bridge
calibration_usable: true
```

### Evidence interpretation

화승코퍼레이션 is the rubber / sealing auto-parts Watch cap.

The label is relevant:

```text
rubber / sealing / hose / auto-parts supplier
  -> OEM production volume readthrough
  -> cost pass-through and product-mix optionality
```

But the forward path did not validate Actionable/Green. MFE was shallow, and the drawdown was material even though it did not cross the hard threshold. This is a Watch/Yellow cap unless incremental OEM program, volume, pass-through, and margin evidence is explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 2,290 / close 2,285
2024-02-05: high 2,450 / close 2,245
2024-03-22: low 1,818 / close 1,845
2024-04-16: low 1,703 / close 1,741
2024-08-05: low 1,770 / close 1,854
2024-10-25: low 1,858 / close 1,871
```

Approximate path from entry close:

```text
entry_close: 2,285
peak_high_after_entry: 2,450
MFE: +7.2%
worst_low_after_entry: 1,703
MAE: -25.5%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from rubber/sealing auto-parts relevance.
Stage2-Actionable: blocked unless named OEM/model, customer volume, material/labor pass-through, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross the hard threshold.
Old corporate-action/name-history caveat: yes, outside 2024 window.
```

The lesson is that auto rubber/sealing supplier relevance is not incremental operating leverage by itself.

### Stress-test components

```text
raw_component_score_proxy:
  rubber_sealing_auto_parts_relevance: high
  oem_volume_bridge: weak_to_medium
  raw_material_labor_pass_through_bridge: weak
  margin_op_bridge: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: material
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
auto_thermal_control_case_count: 1
aluminum_ev_parts_case_count: 1
rubber_sealing_auto_parts_case_count: 1
customer_volume_margin_bridge_missing_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
market_transfer_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C29 auto-parts grid:

```text
023800 인지컨트롤스:
  auto thermal-control / OEM-volume local positive;
  meaningful MFE first, later material MAE, local 4B required.

122350 삼기:
  aluminum / EV component label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.

013520 화승코퍼레이션:
  rubber/sealing auto-parts relevance;
  shallow MFE and material MAE, Watch/Yellow cap.
```

Shared rule:

```text
C29 is not "auto-parts label is hot."
C29 is "named OEM/model, customer volume, utilization, pass-through, warranty/logistics, working capital, and margin conversion are visible for this supplier."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C29_R9L97_023800_2024_02_01","scheduled_round":"R9","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"023800","name":"인지컨트롤스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":7500,"peak_high":10070,"peak_date":"2024-02-15","worst_low_after_entry":5510,"worst_low_after_entry_date":"2024-08-05","mfe_pct":34.3,"mae_pct":-26.5,"classification":"local_positive_auto_thermal_control_oem_volume_mix_margin_bridge_with_4b_after_later_mae","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"market_transfer_or_name_history_caveat":true,"evidence_family":"auto_thermal_control_component_oem_volume_mix_cost_pass_through_margin_bridge","residual_error":"auto_thermal_control_positive_requires_4b_after_material_mae_when_customer_volume_margin_bridge_not_refreshed","shadow_rule_candidate":"preserve_auto_parts_local_positive_but_attach_4b_after_large_mfe_followed_by_material_mae"}
{"row_type":"case","case_id":"C29_R9L97_122350_2024_02_01","scheduled_round":"R9","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"122350","name":"삼기","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":2015,"peak_high":2170,"peak_date":"2024-05-08","worst_low_after_entry":1320,"worst_low_after_entry_date":"2024-08-05","mfe_pct":7.7,"mae_pct":-34.5,"classification":"hard_4c_candidate_aluminum_ev_auto_parts_label_without_customer_volume_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"market_transfer_or_name_history_caveat":true,"evidence_family":"aluminum_ev_auto_parts_label_without_named_oem_program_volume_pass_through_margin_bridge","residual_error":"ev_aluminum_component_label_can_fail_when_customer_program_and_margin_bridge_missing","shadow_rule_candidate":"route_aluminum_ev_component_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_customer_margin_bridge_missing"}
{"row_type":"case","case_id":"C29_R9L97_013520_2024_02_01","scheduled_round":"R9","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","symbol":"013520","name":"화승코퍼레이션","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":2285,"peak_high":2450,"peak_date":"2024-02-05","worst_low_after_entry":1703,"worst_low_after_entry_date":"2024-04-16","mfe_pct":7.2,"mae_pct":-25.5,"classification":"watch_cap_rubber_sealing_auto_parts_label_without_strong_incremental_oem_volume_margin_bridge","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"rubber_sealing_auto_parts_label_without_incremental_oem_volume_raw_material_pass_through_margin_bridge","residual_error":"rubber_sealing_supplier_relevance_can_overpromote_without_oem_volume_and_margin_evidence","shadow_rule_candidate":"cap_rubber_sealing_auto_parts_label_at_watch_yellow_if_mfe_shallow_and_customer_volume_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R9","scheduled_loop":97,"large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","fine_archetype_id":"AUTO_THERMAL_ALUMINUM_EV_PARTS_RUBBER_SEALING_CUSTOMER_VOLUME_PASSTHROUGH_MARGIN_BRIDGE_VS_AUTO_PARTS_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"auto_thermal_control_case_count":1,"aluminum_ev_parts_case_count":1,"rubber_sealing_auto_parts_case_count":1,"customer_volume_margin_bridge_missing_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"market_transfer_or_name_history_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R9","scheduled_loop":97,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","rule_id":"C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_WARRANTY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C29 auto-parts and mobility-supplier cases, do not open Stage2-Actionable or Stage3-Green from auto-parts, thermal control, sensor/control part, aluminum EV component, rubber/sealing/weatherstrip/hose, hybrid/EV model-mix, OEM volume recovery, low-PBR auto-parts rerating, or one-week auto-parts volume-spike labels alone. Require named OEM or model channel, order visibility or production schedule, customer volume and utilization, model mix and ASP, raw-material/labor cost pass-through, FX/logistics/warranty-risk control, inventory and working-capital burden containment, margin/OP conversion, and post-trigger price survival. Thermal-control positives with meaningful MFE followed by material MAE should remain local 4B unless customer-volume and margin evidence refreshes. Aluminum/EV component labels with shallow MFE and hard-zone MAE should route to hard-4C when customer program and margin bridge are missing. Rubber/sealing labels with shallow MFE should cap at Watch/Yellow without incremental OEM volume and pass-through evidence.","expected_effect":"Preserve true mobility supplier operating-leverage positives while reducing generic thermal-control, aluminum EV-component, rubber/sealing, and low-PBR auto-parts false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R9","scheduled_loop":97,"canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","residual_type":"auto_parts_customer_volume_passthrough_warranty_margin_guard","contribution":"Adds one thermal-control local positive, one aluminum EV parts hard-4C candidate, and one rubber/sealing Watch cap to calibrate C29 OEM volume, model mix, cost pass-through, working capital, warranty/logistics, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_WARRANTY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
AND company_type in [thermal_control, aluminum_ev_parts, rubber_sealing_parts, auto_component_supplier]:

  Do not open Stage3-Green from:
    - auto-parts label alone
    - thermal management / sensor / control part label alone
    - aluminum EV component label alone
    - rubber / sealing / weatherstrip / hose label alone
    - hybrid / EV model-mix headline alone
    - OEM volume recovery headline alone
    - low-PBR auto-parts rerating alone
    - one-week auto-parts volume spike alone

  Require at least two of:
    - named OEM or model channel
    - order visibility / production schedule
    - customer volume and utilization
    - model mix / ASP improvement
    - raw-material and labor cost pass-through
    - FX / logistics / warranty-risk containment
    - inventory / working-capital burden control
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the auto-parts headline

  If MFE < 8% and MAE <= -30%:
    route to C29 hard-4C candidate.

  If MFE > 20% but later MAE is material:
    preserve as local 4B / event burst, not Green, unless customer-volume and margin evidence appears.

  If MFE is shallow and the bridge is component-quality only:
    cap at Watch/Yellow.

  If row-presence, old corporate-action, or market-transfer caveat exists:
    apply additional trust cap, but do not contaminate clean 2024 rows.

  Distinguish:
    - suppliers where OEM volume and model mix become utilization and margin
    - from auto-parts labels where material cost, warranty, logistics, or working capital breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R9_loop_97_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C29 auto thermal / aluminum EV parts / rubber sealing supplier cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C29_AUTO_PARTS_CUSTOMER_VOLUME_PASSTHROUGH_WARRANTY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C29 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C29 cases agree, consider implementing a canonical guard that:
   - blocks auto-parts Green without named OEM/model, production schedule, customer volume, pass-through, warranty/logistics, and margin bridge,
   - preserves thermal-control positives only with price survival and fresh margin evidence,
   - routes shallow-MFE/hard-zone-MAE aluminum EV-component labels to hard-4C,
   - caps shallow-MFE rubber/sealing labels at Watch/Yellow without OEM volume evidence,
   - applies old corporate-action, market-transfer, row-presence, and tradeability caveats.

Expected next schedule:
completed_round = R9
completed_loop = 97
next_round = R10
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R9
completed_loop = 97
next_round = R10
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
