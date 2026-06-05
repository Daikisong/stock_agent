# E2R Stock-Web v12 Residual Research — R7 / Loop 97

```yaml
scheduled_round: R7
scheduled_loop: 97
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE

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
orthopedic_implant_case_count: 1
ophthalmic_device_case_count: 1
xray_diagnostic_device_case_count: 1
export_reimbursement_channel_bridge_missing_count: 2
old_corporate_action_caveat_outside_window_count: 2
row_presence_or_market_transfer_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 97
next_round: R8
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 97
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage:

```text
loop93: C24_BIO_TRIAL_DATA_EVENT_RISK
loop94: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop95: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop96: C24_BIO_TRIAL_DATA_EVENT_RISK
```

This run returns to C25 after the R7 branch cycle, but avoids the C25 top-covered names and the prior loop94 C25 set:

```text
medical device / export / reimbursement / channel
orthopedic implant, ophthalmic device, dental or diagnostic X-ray device
reorder, distributor inventory, reimbursement, ASP, FX, and margin bridge
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
226400 오스테오닉
065510 휴비츠
263690 디알젬
```

They avoid the C25 top-covered list and recent R7 names:

```text
loop96 C24 avoid: 196170, 235980, 217730
loop95 C23 avoid: 207940, 068270, 086900
loop94 C25 avoid: 335890, 041830, 228670
C25 top-covered avoid: 336570, 100120, 060280, 099190, 145720, 214150
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
226400: same archetype, new symbol, orthopedic implant / medical device export-channel positive with Green cap
065510: same archetype, new symbol, ophthalmic device export label local burst followed by high-MAE 4B failure
263690: same archetype, new symbol, diagnostic X-ray device export/reimbursement label hard-4C without channel-margin survival
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
226400 오스테오닉
  profile: atlas/symbol_profiles/226/226400.json
  first_date: 2016-05-04
  last_date: 2026-02-20
  market history:
    KONEX from 2016-05-04 to 2018-02-21
    KOSDAQ from 2018-02-22 to 2026-02-20
  tradable_ohlcv rows: 2,373
  non_tradable_zero_volume rows: 30
  corporate_action_candidate_dates:
    2018-02-22, 2020-07-15
  2024 entry~D+180 contamination: none
  caveat:
    KONEX to KOSDAQ migration and old raw-discontinuity windows are outside the selected 2024 validation window.
    Minor row-presence/tradeability trust cap applies.

065510 휴비츠
  profile: atlas/symbol_profiles/065/065510.json
  first_date: 2003-10-31
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,506
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2004-04-22, 2004-05-21
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

263690 디알젬
  profile: atlas/symbol_profiles/263/263690.json
  first_date: 2018-11-22
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,778
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C25 is about medical device export, reimbursement, distributor channels, installation, utilization, and margin. It is not a generic "medical device stock is strong" archetype.

The model can over-score:

```text
medical device label
aesthetic / dental / orthopedic / ophthalmic / diagnostic device label
export growth headline
FDA / CE / overseas approval headline
reimbursement or hospital adoption rumor
distributor expansion label
one-week medical-device volume spike
late chase after device export rerating
```

The C25 bridge must be stricter:

```text
medical device / reimbursement / export event
  -> named product, geography, distributor, hospital channel, or procedure
  -> regulatory approval and reimbursement status
  -> distributor reorder or hospital installation
  -> utilization / procedure volume
  -> ASP / FX / distributor margin
  -> inventory and receivables timing
  -> marketing, education, service, and warranty cost
  -> gross margin / OP conversion
  -> price survival after the first device-label spike
```

A C25 medical-device thesis is like a surgical tray entering an operating room. The product being approved or exported is only the first door; the thesis needs hospital adoption, repeat procedures, distributor reorders, reimbursement friction clearing, and enough margin after service, training, warranty, and FX.

---

## 5. Case 1 — 226400 오스테오닉

```yaml
case_id: C25_R7L97_226400_2024_02_01
symbol: "226400"
name: "오스테오닉"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4780
classification: positive_orthopedic_implant_medical_device_export_channel_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

오스테오닉 is the constructive C25 control in this set.

The useful C25 read is not simply:

```text
의료기기주가 강하다
```

It is:

```text
orthopedic implant / medical device relevance
  -> export channel and procedure-volume optionality
  -> distributor reorder and hospital-use bridge
  -> controlled drawdown after early 2024 entry
  -> strong later price confirmation
```

The forward path produced a meaningful MFE with non-hard MAE. This preserves positive classification. However, C25 Green should remain capped unless export reorder, hospital/procedure utilization, reimbursement, ASP, and margin evidence is fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,795 / close 4,780
2024-02-15: high 5,460 / close 5,390
2024-02-27: high 6,000 / close 5,740
2024-04-05: low 4,150 / close 4,350
2024-08-05: low 4,150 / close 4,265
2024-09-23: high 6,150 / close 6,030
2024-10-16: high 6,530 / close 6,350
2024-11-06: high 6,770 / close 6,280
```

Approximate path from entry close:

```text
entry_close: 4,780
peak_high: 6,770
MFE: +41.6%
worst_low_after_entry: 4,150
MAE: -13.2%
```

### Interpretation

This is a C25 positive with Green cap:

```text
Stage2-Actionable: possible if product/export channel, hospital adoption, reorder, and margin bridge are explicit.
Stage3-Green: blocked without fresh export/reimbursement/procedure-volume evidence.
Local 4B: monitor after +40% MFE if evidence becomes stale.
Hard 4C: no.
Market-transfer / row-presence caveat: minor, outside selected 2024 contamination window.
```

### Stress-test components

```text
raw_component_score_proxy:
  orthopedic_implant_relevance: high
  export_channel_bridge: medium_high
  hospital_procedure_bridge: medium
  reimbursement_bridge: weak_to_medium
  distributor_reorder_bridge: medium
  margin_op_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 6. Case 2 — 065510 휴비츠

```yaml
case_id: C25_R7L97_065510_2024_02_01
symbol: "065510"
name: "휴비츠"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 18000
classification: local_burst_ophthalmic_device_export_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

휴비츠 is the ophthalmic-device local-burst / high-MAE failure.

The setup had real C25 relevance:

```text
ophthalmic diagnostic / optical medical device label
export channel and hospital/clinic equipment demand
device export optionality
```

The early February spike generated meaningful MFE, so this is not a pure zero-response false-positive. But the later price path failed severely. The export/device label did not become durable reorder, utilization, reimbursement, or margin survival.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 18,380 / close 18,000
2024-02-05: high 21,900 / close 18,220
2024-02-27: low 15,530 / close 15,530
2024-04-08: low 12,550 / close 12,560
2024-08-05: low 8,500 / close 8,860
2024-10-25: low 8,690 / close 8,770
2024-11-07: low 8,600 / close 8,800
```

Approximate path from entry close:

```text
entry_close: 18,000
peak_high: 21,900
MFE: +21.7%
worst_low_after_entry: 8,500
MAE: -52.8%
```

### Interpretation

This is a C25 local burst / 4B failure:

```text
Stage2-Watch: valid from ophthalmic-device export relevance.
Stage2-Actionable: possible only if distributor reorder, hospital/clinic demand, utilization, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  ophthalmic_device_relevance: high
  export_channel_bridge: medium
  distributor_reorder_bridge: weak_to_medium
  hospital_utilization_bridge: weak
  asp_fx_margin_bridge: weak_to_medium
  price_confirmation: medium_high_initial
  later_drawdown_penalty: extreme
  local_4b_overlay: required
```

---

## 7. Case 3 — 263690 디알젬

```yaml
case_id: C25_R7L97_263690_2024_02_01
symbol: "263690"
name: "디알젬"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10550
classification: hard_4c_candidate_diagnostic_xray_device_export_reimbursement_label_without_channel_margin_survival
calibration_usable: true
```

### Evidence interpretation

디알젬 is the diagnostic X-ray / medical-device hard guardrail.

The label can fool the model:

```text
diagnostic X-ray / imaging device label
medical equipment export optionality
hospital channel / distributor expansion
low-liquidity device stock
```

But from the selected February entry, the price path produced only shallow MFE and then a large drawdown. The bridge from device label to named distributor reorder, hospital installation, reimbursement, service revenue, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 10,700 / close 10,550
2024-02-21: high 10,900 / close 10,500
2024-05-09: high 11,240 / close 9,700
2024-08-05: low 7,170 / close 7,280
2024-10-25: low 7,000 / close 7,090
2024-11-07: low 6,680 / close 6,700
```

Approximate path from entry close:

```text
entry_close: 10,550
peak_high: 11,240
MFE: +6.5%
worst_low_after_entry: 6,680
MAE: -36.7%
```

### Interpretation

This is a hard C25 false-positive:

```text
Stage2-Watch: possible from diagnostic imaging device and export relevance.
Stage2-Actionable: blocked unless distributor reorder, hospital installation, reimbursement path, service revenue, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that an X-ray device export label is not channel-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  xray_diagnostic_device_relevance: high
  export_reimbursement_signal: medium_high
  distributor_reorder_bridge: weak
  hospital_installation_bridge: weak
  service_warranty_margin_bridge: weak
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
orthopedic_implant_case_count: 1
ophthalmic_device_case_count: 1
xray_diagnostic_device_case_count: 1
export_reimbursement_channel_bridge_missing_count: 2
old_corporate_action_caveat_outside_window_count: 2
row_presence_or_market_transfer_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C25 medical-device grid:

```text
226400 오스테오닉:
  orthopedic implant / export-channel positive;
  large MFE and non-hard MAE, but Green requires fresh export, reorder, procedure-volume, and margin evidence.

065510 휴비츠:
  ophthalmic-device export local burst;
  meaningful MFE first, then extreme MAE, local 4B failure.

263690 디알젬:
  diagnostic X-ray device label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C25 is not "medical device label is high quality."
C25 is "regulatory/reimbursement status, distributor reorder, hospital installation, procedure volume, service cost, and gross margin are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C25_R7L97_226400_2024_02_01","scheduled_round":"R7","scheduled_loop":97,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"226400","name":"오스테오닉","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4780,"peak_high":6770,"peak_date":"2024-11-06","worst_low_after_entry":4150,"worst_low_after_entry_date":"2024-04-05","mfe_pct":41.6,"mae_pct":-13.2,"classification":"positive_orthopedic_implant_medical_device_export_channel_margin_bridge_with_green_cap","calibration_usable":true,"row_presence_or_market_transfer_caveat":true,"evidence_family":"orthopedic_implant_export_channel_hospital_procedure_reorder_margin_bridge","residual_error":"positive_medical_device_export_path_requires_green_cap_after_large_mfe_without_refreshed_reorder_procedure_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_export_channel_procedure_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C25_R7L97_065510_2024_02_01","scheduled_round":"R7","scheduled_loop":97,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"065510","name":"휴비츠","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":18000,"peak_high":21900,"peak_date":"2024-02-05","worst_low_after_entry":8500,"worst_low_after_entry_date":"2024-08-05","mfe_pct":21.7,"mae_pct":-52.8,"classification":"local_burst_ophthalmic_device_export_label_high_mae_4b_failure","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"ophthalmic_device_export_channel_label_without_sustained_distributor_reorder_utilization_margin_survival","residual_error":"ophthalmic_device_export_label_can_create_mfe_but_fail_green_without_channel_reorder_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_extreme_mae_ophthalmic_device_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C25_R7L97_263690_2024_02_01","scheduled_round":"R7","scheduled_loop":97,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","symbol":"263690","name":"디알젬","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10550,"peak_high":11240,"peak_date":"2024-05-09","worst_low_after_entry":6680,"worst_low_after_entry_date":"2024-11-07","mfe_pct":6.5,"mae_pct":-36.7,"classification":"hard_4c_candidate_diagnostic_xray_device_export_reimbursement_label_without_channel_margin_survival","calibration_usable":true,"evidence_family":"diagnostic_xray_device_export_reimbursement_label_without_distributor_hospital_service_margin_bridge","residual_error":"xray_device_export_label_can_fail_when_channel_reorder_and_service_margin_bridge_missing","shadow_rule_candidate":"route_diagnostic_xray_device_label_to_hard_4c_if_mfe_shallow_mae_large_and_channel_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":97,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"ORTHOPEDIC_IMPLANT_OPHTHALMIC_DENTAL_XRAY_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_VS_MEDICAL_DEVICE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"orthopedic_implant_case_count":1,"ophthalmic_device_case_count":1,"xray_diagnostic_device_case_count":1,"export_reimbursement_channel_bridge_missing_count":2,"old_corporate_action_caveat_outside_window_count":2,"row_presence_or_market_transfer_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":97,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","rule_id":"C25_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C25 medical-device export/reimbursement cases, do not open Stage2-Actionable or Stage3-Green from medical device, aesthetic/dental/orthopedic/ophthalmic/diagnostic device, export growth, FDA/CE/overseas approval, reimbursement or hospital adoption rumor, distributor expansion, one-week medical-device volume spike, or late chase after device export rerating labels alone. Require named product/geography/distributor/hospital channel/procedure, regulatory approval and reimbursement status, distributor reorder or hospital installation, utilization/procedure volume, ASP/FX/distributor margin, inventory and receivables timing, marketing/education/service/warranty cost control, gross-margin/OP conversion, and post-trigger price survival. Orthopedic implant positives with large MFE may be capped Actionable when export channel and procedure-margin bridge are explicit, but Green requires fresh evidence. Ophthalmic device labels with meaningful MFE followed by extreme MAE should remain local 4B, not Green. Diagnostic X-ray device labels with shallow MFE and high MAE should route to hard-4C when distributor, hospital, service, and margin bridge are missing.","expected_effect":"Preserve true medical-device export/reimbursement positives while reducing device-label, channel-reorder, and export-growth false positives where utilization, reimbursement, service cost, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":97,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"device_export_reimbursement_channel_margin_guard","contribution":"Adds one orthopedic implant positive, one ophthalmic-device local 4B failure, and one diagnostic X-ray hard-4C counterexample to calibrate C25 regulatory/reimbursement, distributor reorder, hospital installation, utilization/procedure volume, service/warranty cost, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C25_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:

  Do not open Stage3-Green from:
    - medical device label alone
    - aesthetic / dental / orthopedic / ophthalmic / diagnostic device label alone
    - export growth headline alone
    - FDA / CE / overseas approval headline alone
    - reimbursement or hospital adoption rumor alone
    - distributor expansion label alone
    - one-week medical-device volume spike alone
    - late chase after device export rerating alone

  Require at least two of:
    - named product / geography / distributor / hospital channel / procedure
    - regulatory approval and reimbursement status
    - distributor reorder or hospital installation
    - utilization / procedure volume
    - ASP / FX / distributor margin
    - inventory and receivables timing
    - marketing / education / service / warranty cost containment
    - gross margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the device/export headline

  If MFE < 8% and MAE < -30%:
    route to C25 hard-4C candidate.

  If MFE > 15% but later MAE is high:
    preserve as local 4B / event burst, not Green, unless current reorder/utilization/margin evidence appears.

  If MFE is large but export/reimbursement evidence is stale:
    cap Green until distributor reorder and utilization evidence refreshes.

  Distinguish:
    - device names where approval/export becomes reorder, hospital use, procedure volume, and margin
    - from device labels where channel inventory, reimbursement friction, service cost, or warranty breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C25 medical device export/reimbursement cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C25_DEVICE_EXPORT_REIMBURSEMENT_CHANNEL_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C25 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C25 cases agree, consider implementing a canonical guard that:
   - blocks medical-device Green without named product/channel, regulatory/reimbursement, reorder, installation, utilization, and margin bridge,
   - preserves orthopedic implant positives only with price survival and fresh export/procedure evidence,
   - treats meaningful-MFE/extreme-MAE ophthalmic-device export labels as local 4B,
   - routes shallow-MFE/high-MAE diagnostic X-ray device labels to hard-4C,
   - applies old corporate-action, market-transfer, and row-presence caveats when needed.

Expected next schedule:
completed_round = R7
completed_loop = 97
next_round = R8
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 97
next_round = R8
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
