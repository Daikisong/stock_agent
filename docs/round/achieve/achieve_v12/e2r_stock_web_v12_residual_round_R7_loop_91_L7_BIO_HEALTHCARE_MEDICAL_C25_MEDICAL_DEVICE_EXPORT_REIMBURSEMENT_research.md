# E2R Stock-Web v12 Residual Research — R7 / Loop 91

```yaml
scheduled_round: R7
scheduled_loop: 91
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE

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
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 91
next_round: R8
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 91
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage already covered:

```text
loop88: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop89: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop90: C24_BIO_TRIAL_DATA_EVENT_RISK
```

This run returns to C25, but with a different branch:

```text
aesthetic / dental / biomaterial device export-reimbursement bridge
vs broad medical-device label and local spike
```

The intent is not to repeat the previous C25 coverage. The goal is to isolate the rule for when a medical-device or aesthetic-device label becomes an investable export/reimbursement rerating, and when it is only a sector label.

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
214450 파마리서치
228670 레이
042520 한스바이오메드
```

These avoid the C25 top-covered symbols and avoid the latest R7 C23/C24 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
214450: same archetype, new symbol, aesthetic medical-product export/sell-through and margin bridge
228670: same archetype, new symbol, dental device export/channel false-positive branch
042520: same archetype, new symbol, biomaterial/aesthetic implant local-spike without reimbursement/export bridge
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
214450 파마리서치
  profile: atlas/symbol_profiles/214/214450.json
  first_date: 2015-07-24
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,594
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

228670 레이
  profile: atlas/symbol_profiles/228/228670.json
  first_date: 2019-08-08
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,603
  corporate_action_candidate_dates:
    2021-06-03, 2021-06-23
  2024 entry~D+180 contamination: none

042520 한스바이오메드
  profile: atlas/symbol_profiles/042/042520.json
  first_date: 2009-10-09
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,030
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C25 is not a generic medical-device label.

The model can over-score:

```text
aesthetic medical device
dental equipment export
biomaterial / implant
medical reimbursement theme
China / Asia distribution
FDA / CE / overseas certification headline
```

The actual bridge is narrower:

```text
device/product capability
  -> regulatory or reimbursement access
  -> distributor / hospital / clinic channel
  -> repeat utilization or consumable pull-through
  -> export revenue
  -> margin / OP conversion
  -> post-trigger price survival
```

Medical-device exports are like installing equipment in a clinic network. The first sale matters, but the rerating comes when the equipment is used repeatedly, consumables or procedures recur, and reimbursement/channel economics make the revenue durable.

---

## 5. Case 1 — 214450 파마리서치

```yaml
case_id: C25_R7L91_214450_2024_03_25
symbol: "214450"
name: "파마리서치"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE
trigger_date: 2024-03-25
entry_date: 2024-03-25
entry_price_basis: close
entry_price: 98700
classification: positive_with_local_4b_aesthetic_export_margin_bridge
calibration_usable: true
```

### Evidence interpretation

파마리서치 is the positive control in this set.

The useful C25 thesis is not simply "aesthetic healthcare is popular." The stronger bridge is:

```text
aesthetic medical product / procedure ecosystem
  -> clinic-level repeat demand
  -> overseas distribution and sell-through
  -> product mix and margin support
  -> OP/EPS rerating
  -> sustained price confirmation
```

The price path validates the entry strongly. However, the later move was large enough that C25 should attach a local 4B overlay rather than blindly keep Green without a new revision bridge.

### Price path

Key Stock-Web rows:

```text
2024-03-25: close 98,700
2024-03-27: high 102,100 / close 99,800
2024-04-01: high 110,900 / close 108,000
2024-06-27: high 157,100 / close 156,200
2024-08-05: low 121,300 / close 129,900
2024-08-14: high 185,400 / close 184,400
2024-09-20: high 205,500 / close 201,000
2024-09-23: high 208,500 / close 198,200
```

Approximate path from entry close:

```text
entry_close: 98,700
peak_high: 208,500
MFE: +111.2%
worst_low_after_entry_in_checked_window: 96,000 on 2024-03-26
MAE: -2.7%
peak_to_near_later_low_in_checked_window: not fully measurable from fetched 2024 rows after 2024-09-23, but +100% MFE itself requires local 4B discipline
```

### Interpretation

This is a strong C25 positive:

```text
Stage2-Actionable: valid.
Stage3-Green: allowed only if export/channel/procedure-repeat and margin bridge are explicit.
Local 4B: mandatory after +100% MFE unless a fresh revision bridge appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  product/procedure_repeatability: high
  export/channel_bridge: high
  margin_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low
  blowoff_4b_risk: high_after_100pct_mfe
```

---

## 6. Case 2 — 228670 레이

```yaml
case_id: C25_R7L91_228670_2024_03_12
symbol: "228670"
name: "레이"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE
trigger_date: 2024-03-12
entry_date: 2024-03-12
entry_price_basis: close
entry_price: 16870
classification: hard_4c_candidate_dental_device_export_label_without_channel_margin_bridge
calibration_usable: true
```

### Evidence interpretation

레이 is the dental-device false-positive. The company has a plausible medical-device/export label. But the forward price path did not validate a C25 Actionable thesis.

The model risk:

```text
dental equipment / dental solution label
  -> overseas device/export possibility
  -> local rebound
  -> no durable channel/reimbursement/margin confirmation
  -> high MAE
```

For C25, the bridge must be very specific:

```text
clinic or dental channel penetration
equipment placement
software/consumable or repeat procedure economics
reimbursement or regulatory access
margin conversion
```

### Price path

Key Stock-Web rows:

```text
2024-03-12: close 16,870
2024-03-13: high 17,300 / close 17,020
2024-03-18: high 17,650 / close 17,520
2024-03-19: high 17,680 / close 17,480
2024-03-26: low 14,760 / close 14,820
2024-08-05: low 8,860 / close 8,860
2024-09-10: low 7,600 / close 7,670
```

Approximate path from entry close:

```text
entry_close: 16,870
peak_high: 17,680
MFE: +4.8%
worst_low: 7,600
MAE: -54.9%
```

### Interpretation

This is a hard C25 guardrail case:

```text
Stage2-Watch: allowed from device/export label.
Stage2-Actionable: blocked without channel/reimbursement/margin bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is clear: "medical device export potential" is not enough. The model must see channel and economic conversion.

### Stress-test components

```text
raw_component_score_proxy:
  medical_device_label: high
  export_channel_bridge: weak
  reimbursement_bridge: weak
  margin_conversion: weak
  price_confirmation: failed
  drawdown_penalty: extreme
  4c_guard_required: yes
```

---

## 7. Case 3 — 042520 한스바이오메드

```yaml
case_id: C25_R7L91_042520_2024_02_29
symbol: "042520"
name: "한스바이오메드"
canonical_archetype_id: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
fine_archetype_id: AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE
trigger_date: 2024-02-29
entry_date: 2024-02-29
entry_price_basis: close
entry_price: 14380
classification: hard_4c_candidate_biomaterial_aesthetic_implant_local_spike_without_export_reimbursement_bridge
calibration_usable: true
```

### Evidence interpretation

한스바이오메드 is the biomaterial/aesthetic implant local-spike false-positive.

The label can look attractive:

```text
biomaterial
aesthetic implant
medical device
export / regulatory recovery possibility
```

But the price path says the bridge did not hold. A local spike appeared, but there was no durable price survival. The model should not equate a one-month medical-device rebound with a C25 export/reimbursement rerating.

### Price path

Key Stock-Web rows:

```text
2024-02-29: close 14,380
2024-03-08: high 15,180 / close 15,090
2024-03-11: high 15,740 / close 15,320
2024-03-19: high 16,600 / close 15,080
2024-04-08: low 13,220 / close 13,250
2024-08-05: low 9,400 / close 9,820
2024-09-09: low 8,700 / close 9,100
```

Approximate path from entry close:

```text
entry_close: 14,380
peak_high: 16,600
MFE: +15.4%
worst_low: 8,700
MAE: -39.5%
```

### Interpretation

This is the 4B/4C boundary case, classified as hard 4C candidate because the later MAE was too large:

```text
Stage2-Watch: possible.
Stage2-Actionable: blocked unless export/reimbursement/channel economics are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The initial MFE was not enough to compensate for the missing durable bridge.

### Stress-test components

```text
raw_component_score_proxy:
  biomaterial_device_label: high
  export_or_reimbursement_bridge: weak
  channel_repeatability: weak
  local_price_burst: medium
  post_burst_survival: failed
  drawdown_penalty: high
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C25 grid:

```text
214450 파마리서치:
  aesthetic medical product / procedure-repeat / export-channel positive;
  strong MFE and low MAE, but local 4B after +100% MFE.

228670 레이:
  dental device/export label failed without channel/reimbursement/margin bridge;
  shallow MFE and extreme MAE, hard 4C candidate.

042520 한스바이오메드:
  biomaterial/aesthetic implant local spike failed price survival;
  hard 4C candidate unless export/reimbursement bridge becomes explicit.
```

Shared rule:

```text
C25 is not "medical device stock went up."
C25 is "device/product gets regulatory or reimbursement access, then channel adoption and repeat utilization convert into margin and OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C25_R7L91_214450_2024_03_25","scheduled_round":"R7","scheduled_loop":91,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE","symbol":"214450","name":"파마리서치","trigger_date":"2024-03-25","entry_date":"2024-03-25","entry_price":98700,"peak_high":208500,"peak_date":"2024-09-23","worst_low_after_entry":96000,"worst_low_after_entry_date":"2024-03-26","mfe_pct":111.2,"mae_pct":-2.7,"classification":"positive_with_local_4b_aesthetic_export_margin_bridge","calibration_usable":true,"evidence_family":"aesthetic_medical_product_export_channel_repeat_procedure_margin_bridge","residual_error":"positive_entry_but_100pct_mfe_requires_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_export_channel_repeat_procedure_and_margin_bridge_confirm; require_4b_after_100pct_mfe"}
{"row_type":"case","case_id":"C25_R7L91_228670_2024_03_12","scheduled_round":"R7","scheduled_loop":91,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE","symbol":"228670","name":"레이","trigger_date":"2024-03-12","entry_date":"2024-03-12","entry_price":16870,"peak_high":17680,"peak_date":"2024-03-19","worst_low":7600,"worst_low_date":"2024-09-10","mfe_pct":4.8,"mae_pct":-54.9,"classification":"hard_4c_candidate_dental_device_export_label_without_channel_margin_bridge","calibration_usable":true,"evidence_family":"dental_device_export_label_without_channel_reimbursement_margin_bridge","residual_error":"medical_device_export_label_can_overpromote_without_channel_economics","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_channel_reimbursement_bridge_missing"}
{"row_type":"case","case_id":"C25_R7L91_042520_2024_02_29","scheduled_round":"R7","scheduled_loop":91,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE","symbol":"042520","name":"한스바이오메드","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":14380,"peak_high":16600,"peak_date":"2024-03-19","worst_low":8700,"worst_low_date":"2024-09-09","mfe_pct":15.4,"mae_pct":-39.5,"classification":"hard_4c_candidate_biomaterial_aesthetic_implant_local_spike_without_export_reimbursement_bridge","calibration_usable":true,"evidence_family":"biomaterial_aesthetic_implant_local_spike_without_export_reimbursement_bridge","residual_error":"local_medical_device_spike_can_fail_without_durable_export_or_reimbursement_bridge","shadow_rule_candidate":"route_biomaterial_device_local_spike_to_4c_if_price_survival_fails"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":91,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","fine_archetype_id":"AESTHETIC_DENTAL_BIOMATERIAL_DEVICE_EXPORT_REIMBURSEMENT_BRIDGE_VS_DEVICE_LABEL_LOCAL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":91,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","rule_id":"C25_DEVICE_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C25, do not open Stage2-Actionable or Stage3-Green from medical-device, dental-device, biomaterial, aesthetic-device, export, certification, or reimbursement labels alone. Require regulatory or reimbursement access, distributor/hospital/clinic channel adoption, repeat utilization or consumable/procedure pull-through, export revenue, margin/OP conversion, and post-trigger price survival. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE exceeds 100%, preserve positive classification but attach local 4B unless a new revision bridge appears.","expected_effect":"Reduce medical-device label false positives while preserving aesthetic/product-platform positives with real channel, repeat-utilization, and margin bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":91,"canonical_archetype_id":"C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT","residual_type":"medical_device_export_reimbursement_channel_bridge_guard","contribution":"Adds one aesthetic medical-product positive and two dental/biomaterial device false positives to calibrate C25 channel, reimbursement, repeat-utilization, margin, and price-survival rules.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C25_DEVICE_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT:

  Do not open Stage3-Green from:
    - medical-device label alone
    - dental-device label alone
    - biomaterial / implant / aesthetic-device label alone
    - overseas certification headline alone
    - reimbursement headline alone
    - one-month local price spike alone

  Require at least two of:
    - regulatory access or reimbursement confirmation
    - distributor / hospital / clinic channel adoption
    - repeat procedure or consumable pull-through
    - export revenue conversion
    - gross margin or OP bridge
    - low-MAE post-trigger price survival
    - earnings revision after channel adoption

  If MFE < 10% and MAE < -30%:
    route to C25 false-positive / hard-4C candidate.

  If MFE > 10% but MAE < -35%:
    classify as local spike failure, not Green.

  If MFE > 100%:
    local 4B overlay is mandatory unless a new revision bridge appears.

  Distinguish:
    - aesthetic medical-product platforms with repeat procedure and export-channel economics
    - from dental/biomaterial/device labels where channel, reimbursement, and margin conversion are unconfirmed.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C25 medical-device/export/reimbursement cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C25_DEVICE_CHANNEL_REIMBURSEMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C25 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C25 cases agree, consider implementing a canonical guard that:
   - blocks medical-device label Green without regulatory/reimbursement/channel/margin bridge,
   - preserves aesthetic medical-product positives with repeat-procedure/export channel price survival,
   - attaches local 4B after >100% MFE,
   - routes shallow-MFE/high-MAE dental/biomaterial cases to C25 false-positive or hard-4C.

Expected next schedule:
completed_round = R7
completed_loop = 91
next_round = R8
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 91
next_round = R8
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
