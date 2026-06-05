# E2R Stock-Web v12 Residual Research — R7 / Loop 94

```yaml
scheduled_round: R7
scheduled_loop: 94
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE

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
listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 94
next_round: R8
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_94_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 94
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage:

```text
loop91: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop92: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop93: C24_BIO_TRIAL_DATA_EVENT_RISK
```

This run returns to C25, but avoids the top-covered C25 names and uses a different fine branch:

```text
aesthetic device / body-composition device / dental digital device
export reorder and margin bridge
vs generic medical-device label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
rows: 33
symbols: 16
date_range: 2023-02-13~2024-07-16
good/bad S2: 13/6
4B/4C: 3/2
URL pending/proxy: 13/7
top covered symbols:
  336570(6), 100120(3), 060280(2), 099190(2), 145720(2), 214150(2)
```

Selected symbols:

```text
335890 비올
041830 인바디
228670 레이
```

They avoid the C25 top-covered symbols and avoid recent R7 loop92~93 names:

```text
loop92 avoid: C23 regulatory approval/commercialization names
loop93 avoid: 196170, 235980, 950220
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
335890: same archetype, new symbol, aesthetic device export reorder positive with post-rerating 4B and row-presence caveat
041830: same archetype, new symbol, body-composition device export label Watch cap without strong reimbursement/reorder margin bridge
228670: same archetype, new symbol, dental digital device export label hard-4C without demand/margin survival
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
335890 비올
  profile: atlas/symbol_profiles/335/335890.json
  name history:
    IBKS제11호스팩 until 2020-11-25
    비올 from 2020-11-26 to 2025-12-09
  first_date: 2019-12-03
  last_date: 2025-12-09
  market: KOSDAQ
  tradable_ohlcv rows: 1,399
  corporate_action_candidate_dates:
    2020-11-26
  2024 entry~D+180 contamination: none
  caveat:
    profile status is inactive_or_delisted_like after 2025-12-09, but this is outside the 2024 validation window.

041830 인바디
  profile: atlas/symbol_profiles/041/041830.json
  name history:
    바이오스페이 -> 바이오스페이스 -> 인바디
  first_date: 2000-12-14
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,209
  corporate_action_candidate_dates:
    2010-04-23, 2010-05-18
  2024 entry~D+180 contamination: none

228670 레이
  profile: atlas/symbol_profiles/228/228670.json
  first_date: 2019-08-08
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,603
  corporate_action_candidate_dates:
    2021-06-03, 2021-06-23
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C25 is about medical-device export, reimbursement, procedure adoption, and commercialization quality. It is not a generic "medical device stock" or "healthcare export" label.

The model can over-score:

```text
aesthetic device export
dental digital device label
body-composition or diagnostic-device label
overseas distributor headline
FDA / CE / reimbursement label
one-week medical-device volume spike
```

The C25 bridge must be stricter:

```text
medical-device export / reimbursement event
  -> overseas sell-through or distributor reorder
  -> procedure volume or installed-base utilization
  -> regulatory or reimbursement access
  -> consumable / recurring revenue mix
  -> ASP / FX / gross margin bridge
  -> marketing and channel cost
  -> price survival after the first device-theme spike
```

A medical-device story is like placing a machine in a clinic. C25 asks whether physicians use it, patients pay, distributors reorder, consumables repeat, reimbursement supports the procedure, and the margin survives the channel cost.

---

## 5. Case 1 — 335890 비올

```yaml
case_id: C25_R7L94_335890_2024_03_13
symbol: "335890"
name: "비올"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-03-13
entry_date: 2024-03-13
entry_price_basis: close
entry_price: 8480
classification: positive_aesthetic_device_export_reorder_margin_bridge_with_4b_watch_and_row_presence_caveat
calibration_usable: true
```

### Evidence interpretation

비올 is the constructive C25 control.

The useful C25 read is not simply:

```text
미용의료기기 테마가 강하다
```

It is:

```text
aesthetic device export / distributor reorder relevance
  -> procedure-volume and installed-base pull
  -> consumable or recurring revenue optionality
  -> gross margin / FX bridge
  -> strong price confirmation
```

The 2024 path produced a strong MFE after the March trigger and did not collapse below the entry until the August market shock. That is a valid C25 positive. Because the move was already large, it still requires 4B discipline after rerating unless fresh reorder and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-03-13: high 8,800 / close 8,480
2024-03-14: high 9,500 / close 9,400
2024-03-25: high 10,780 / close 10,350
2024-04-01: high 12,030 / close 11,730
2024-08-05: low 7,490 / close 8,070
2024-10-16: high 10,050 / close 9,670
```

Approximate path from entry close:

```text
entry_close: 8,480
peak_high: 12,030
MFE: +41.9%
worst_low_after_entry: 7,490
MAE: -11.7%
```

### Interpretation

This is a C25 positive with 4B watch:

```text
Stage2-Actionable: valid if distributor reorder, procedure demand, and margin bridge are explicit.
Stage3-Green: possible only with recurring/consumable or channel-margin evidence.
Local 4B: required after +40% MFE unless fresh reorder/margin evidence refreshes the bridge.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  aesthetic_device_export_relevance: high
  distributor_reorder_bridge: medium_high
  procedure_volume_bridge: medium_high
  margin_fx_bridge: medium
  price_confirmation: high
  drawdown_penalty: medium
  row_presence_caveat: post_2025_only_not_in_2024_window
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 041830 인바디

```yaml
case_id: C25_R7L94_041830_2024_02_19
symbol: "041830"
name: "인바디"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-02-19
entry_date: 2024-02-19
entry_price_basis: close
entry_price: 28000
classification: watch_cap_body_composition_device_export_label_without_strong_reimbursement_reorder_margin_bridge
calibration_usable: true
```

### Evidence interpretation

인바디 is the body-composition device Watch cap.

The company has real device and export relevance:

```text
body-composition device
global health / fitness / clinical screening
installed base and replacement demand
```

But C25 should not promote that label into Actionable/Green unless export reorder, utilization, reimbursement or clinical-channel adoption, and margin evidence are visible. The forward path gave shallow MFE and a material drawdown.

### Price path

Key Stock-Web rows:

```text
2024-02-19: high 28,450 / close 28,000
2024-03-26: high 30,200 / close 30,050
2024-03-29: high 30,500 / close 30,150
2024-04-08: low 26,850 / close 26,850
2024-08-05: low 21,600 / close 21,750
2024-08-30: high 26,200 / close 25,750
2024-10-25: low 23,000 / close 23,250
```

Approximate path from entry close:

```text
entry_close: 28,000
peak_high: 30,500
MFE: +8.9%
worst_low_after_entry: 21,600
MAE: -22.9%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from body-composition device and export relevance.
Stage2-Actionable: blocked unless distributor reorder, installed-base utilization, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross the hard threshold, but false-positive guard applies.
```

### Stress-test components

```text
raw_component_score_proxy:
  device_export_relevance: medium_high
  reimbursement_or_clinical_channel_bridge: weak
  installed_base_utilization_bridge: medium
  reorder_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 228670 레이

```yaml
case_id: C25_R7L94_228670_2024_03_12
symbol: "228670"
name: "레이"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-03-12
entry_date: 2024-03-12
entry_price_basis: close
entry_price: 16870
classification: hard_4c_candidate_dental_digital_device_export_label_without_demand_margin_survival
calibration_usable: true
```

### Evidence interpretation

레이 is the hard C25 guardrail.

The label can look attractive:

```text
digital dentistry
dental imaging / CAD-CAM device
overseas sales and distributor expectation
medical-device export recovery
```

But the forward price path did not validate the export/reorder/margin bridge. The MFE after the selected March trigger was shallow, while later MAE became extreme.

### Price path

Key Stock-Web rows:

```text
2024-03-12: high 17,040 / close 16,870
2024-03-18: high 17,650 / close 17,520
2024-03-19: high 17,680 / close 17,480
2024-04-17: low 13,790 / close 13,810
2024-08-05: low 8,860 / close 8,860
2024-09-10: low 7,600 / close 7,670
2024-10-25: low 8,280 / close 8,300
```

Approximate path from entry close:

```text
entry_close: 16,870
peak_high: 17,680
MFE: +4.8%
worst_low_after_entry: 7,600
MAE: -54.9%
```

### Interpretation

This is a hard C25 false-positive:

```text
Stage2-Watch: possible from digital dental-device and export relevance.
Stage2-Actionable: blocked unless distributor reorder, installed-base utilization, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
```

The lesson is that dental-device export adjacency is not demand survival.

### Stress-test components

```text
raw_component_score_proxy:
  dental_device_export_label: high
  distributor_reorder_bridge: weak
  installed_base_utilization_bridge: weak
  margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
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
listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C25 medical-device grid:

```text
335890 비올:
  aesthetic device export/reorder positive;
  strong MFE and moderate MAE, but 4B required after rerating.

041830 인바디:
  body-composition device export label;
  shallow MFE and material MAE, Watch/Yellow cap.

228670 레이:
  dental digital-device export label failed;
  shallow MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C25 is not "medical-device label."
C25 is "device placement, procedure volume, distributor reorder, installed-base utilization, reimbursement/channel access, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C25_R7L94_335890_2024_03_13","scheduled_round":"R7","scheduled_loop":94,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"335890","name":"비올","trigger_date":"2024-03-13","entry_date":"2024-03-13","entry_price":8480,"peak_high":12030,"peak_date":"2024-04-01","worst_low_after_entry":7490,"worst_low_after_entry_date":"2024-08-05","mfe_pct":41.9,"mae_pct":-11.7,"classification":"positive_aesthetic_device_export_reorder_margin_bridge_with_4b_watch_and_row_presence_caveat","calibration_usable":true,"evidence_family":"aesthetic_device_export_distributor_reorder_procedure_volume_margin_bridge","residual_error":"positive_device_export_path_requires_4b_after_large_mfe_without_fresh_reorder_margin_evidence","shadow_rule_candidate":"preserve_device_export_positive_when_reorder_and_margin_bridge_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C25_R7L94_041830_2024_02_19","scheduled_round":"R7","scheduled_loop":94,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"041830","name":"인바디","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":28000,"peak_high":30500,"peak_date":"2024-03-29","worst_low_after_entry":21600,"worst_low_after_entry_date":"2024-08-05","mfe_pct":8.9,"mae_pct":-22.9,"classification":"watch_cap_body_composition_device_export_label_without_strong_reimbursement_reorder_margin_bridge","calibration_usable":true,"evidence_family":"body_composition_device_export_label_without_strong_reorder_reimbursement_margin_bridge","residual_error":"medical_device_quality_can_overpromote_without_reimbursement_or_reorder_margin_conversion","shadow_rule_candidate":"cap_body_composition_device_label_at_watch_yellow_if_mfe_shallow_and_margin_bridge_missing"}
{"row_type":"case","case_id":"C25_R7L94_228670_2024_03_12","scheduled_round":"R7","scheduled_loop":94,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"228670","name":"레이","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":16870,"peak_high":17680,"peak_date":"2024-03-19","worst_low_after_entry":7600,"worst_low_after_entry_date":"2024-09-10","mfe_pct":4.8,"mae_pct":-54.9,"classification":"hard_4c_candidate_dental_digital_device_export_label_without_demand_margin_survival","calibration_usable":true,"evidence_family":"dental_digital_device_export_label_without_distributor_reorder_installed_base_margin_bridge","residual_error":"dental_device_export_adjacency_can_fail_without_demand_and_margin_survival","shadow_rule_candidate":"route_dental_device_export_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_reorder_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":94,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_BODYCOMPOSITION_DENTAL_DEVICE_EXPORT_REORDER_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"listing_or_row_presence_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":94,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","rule_id":"C25_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C25, do not open Stage2-Actionable or Stage3-Green from medical-device, aesthetic-device, dental-device, body-composition, FDA/CE/reimbursement, export, or one-week medical-device spike labels alone. Require overseas sell-through or distributor reorder, procedure volume or installed-base utilization, regulatory/reimbursement/channel access, consumable or recurring revenue mix, ASP/FX/gross-margin bridge, marketing/channel-cost containment, and post-trigger price survival. Device export positives with large MFE should attach local 4B unless fresh reorder/margin evidence appears. Body-composition or stable device labels with shallow MFE should cap at Watch/Yellow without reimbursement/reorder evidence. Dental-device export labels with shallow MFE and extreme MAE should route to hard-4C when demand and margin bridge are missing.","expected_effect":"Preserve true device-export positives while reducing generic medical-device label and late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":94,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"device_export_reorder_reimbursement_margin_guard","contribution":"Adds one aesthetic-device export positive with 4B watch, one body-composition device Watch cap, and one dental-device hard-4C counterexample to calibrate C25 export/reorder/reimbursement/margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C25_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:

  Do not open Stage3-Green from:
    - medical-device label alone
    - aesthetic / dental / body-composition device label alone
    - FDA / CE / reimbursement label alone
    - overseas distributor headline alone
    - one-week medical-device volume spike alone

  Require at least two of:
    - overseas sell-through / distributor reorder
    - procedure volume / installed-base utilization
    - regulatory or reimbursement access
    - consumable or recurring revenue mix
    - ASP / FX / gross-margin bridge
    - marketing and channel-cost containment
    - low-MAE post-trigger price survival
    - fresh evidence after the device-export headline

  If MFE < 10% and MAE < -30%:
    route to C25 hard-4C candidate.

  If MFE is shallow and bridge is stable-label only:
    cap at Watch/Yellow.

  If MFE > 40%:
    preserve positive classification but attach local 4B unless reorder/margin evidence refreshes the thesis.

  Distinguish:
    - device names where installed-base and distributor reorder create margin
    - from device labels where export adjacency does not survive demand or channel costs.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_94_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C25 medical-device export/reimbursement cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C25_DEVICE_EXPORT_REORDER_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C25 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C25 cases agree, consider implementing a canonical guard that:
   - blocks medical-device Green without sell-through/reorder/procedure volume/reimbursement/margin bridge,
   - preserves aesthetic-device positives only with price survival and fresh reorder evidence,
   - attaches local 4B after large MFE,
   - caps stable body-composition device labels at Watch/Yellow without margin evidence,
   - routes shallow-MFE/high-MAE dental-device export labels to hard-4C.

Expected next schedule:
completed_round = R7
completed_loop = 94
next_round = R8
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 94
next_round = R8
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
