# E2R Stock-Web v12 Residual Research — R7 / Loop 96

```yaml
scheduled_round: R7
scheduled_loop: 96
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL

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
platform_license_or_biologic_validation_case_count: 1
clinical_trial_event_case_count: 2
corporate_action_caveat_avoided_count: 2
large_mfe_rerating_cap_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 96
next_round: R8
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_96_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 96
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage:

```text
loop92: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop93: C24_BIO_TRIAL_DATA_EVENT_RISK
loop94: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop95: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

This run returns to C24 but avoids the top-covered C24 names and uses a different fine branch:

```text
bio platform license / clinical validation / trial-event rerating
development, partner, milestone, data-quality, and commercialization bridge
vs generic trial-label event-risk reversal
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
rows: 30
symbols: 20
date_range: 2022-01-12~2024-08-26
good/bad S2: 13/9
4B/4C: 0/2
URL pending/proxy: 10/10
top covered symbols:
  298380(3), 323990(3), 007390(2), 087010(2), 141080(2), 226950(2)
```

Selected symbols:

```text
196170 알테오젠
235980 메드팩토
217730 강스템바이오텍
```

They avoid the C24 top-covered list and avoid recent R7 loop95 C23 and loop94 C25 names:

```text
loop95 C23 avoid: 207940, 068270, 086900
loop94 C25 avoid: 335890, 041830, 228670
C24 top-covered avoid: 298380, 323990, 007390, 087010, 141080, 226950
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
196170: same archetype, new symbol, platform-license / biologic validation positive with extreme MFE and Green cap
235980: same archetype, new symbol, oncology clinical-event local burst followed by high-MAE 4B failure
217730: same archetype, new symbol, stem-cell clinical-event late spike hard-4C without data/regulatory bridge survival
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
196170 알테오젠
  profile: atlas/symbol_profiles/196/196170.json
  first_date: 2014-12-12
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 2,745
  corporate_action_candidate_dates:
    2017-12-07, 2017-12-28, 2020-07-23, 2020-08-13, 2021-04-12
  2024 entry~D+180 contamination: none

235980 메드팩토
  profile: atlas/symbol_profiles/235/235980.json
  first_date: 2019-12-19
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,513
  corporate_action_candidate_dates:
    2020-06-02, 2023-12-28
  selected 2024 entry is after the 2023-12-28 candidate window.
  2024 entry~D+180 contamination: avoided

217730 강스템바이오텍
  profile: atlas/symbol_profiles/217/217730.json
  first_date: 2015-12-21
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,492
  corporate_action_candidate_dates:
    2018-08-09, 2021-11-02, 2023-11-20, 2025-09-04
  selected 2024 entry is after the 2023-11-20 candidate window and before the 2025-09-04 candidate.
  2024 entry~D+180 contamination: avoided
```

---

## 4. Archetype residual problem

C24 is about bio trial-data event risk. It is not a generic "bio stock with a data or platform story" archetype.

The model can over-score:

```text
clinical-trial headline
platform technology or license optionality
oncology or stem-cell label
partner / milestone / global pharma readthrough
conference abstract or data-preview hype
one-week bio-stock volume spike
```

The C24 bridge must be stricter:

```text
bio trial or platform-validation event
  -> named asset, indication, partner, or mechanism
  -> credible clinical data quality
  -> endpoint / safety / durability / comparator check
  -> regulatory path and next trial design
  -> milestone / royalty / partner economics
  -> cash runway and dilution risk
  -> commercialization or licensing path
  -> price survival after the first bio-event spike
```

A C24 bio event is like a lab result pinned to a door. The market reads the headline first, but C24 asks whether the data is strong enough, whether the endpoint matters, whether safety holds, whether regulators can use it, and whether a partner can turn it into cash.

---

## 5. Case 1 — 196170 알테오젠

```yaml
case_id: C24_R7L96_196170_2024_02_01
symbol: "196170"
name: "알테오젠"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 71400
classification: positive_platform_license_biologic_validation_rerating_with_extreme_mfe_and_green_cap
calibration_usable: true
```

### Evidence interpretation

알테오젠 is the constructive C24 control in this set.

The useful C24 read is not simply:

```text
바이오 플랫폼주가 강하다
```

It is:

```text
biologic delivery / platform-license relevance
  -> partner validation and milestone optionality
  -> global biologics commercialization readthrough
  -> strong price confirmation
  -> low-MAE price survival
```

The forward path delivered an extraordinary MFE with controlled MAE. That supports positive classification. However, C24 should not treat the entire rerating as proof that every bio trial/platform label deserves Green. Extreme MFE requires a Green cap unless partner economics, development progress, milestone visibility, and commercial conversion are refreshed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 79,500 / low 70,500 / close 71,400
2024-02-23: high 136,500 / close 131,200
2024-03-26: high 225,500 / close 219,500
2024-07-24: high 306,500 / close 304,500
2024-08-05: low 249,500 / close 261,500
2024-09-20: high 363,500 / close 363,000
2024-10-22: high 402,000 / close 383,500
```

Approximate path from entry close:

```text
entry_close: 71,400
peak_high: 402,000
MFE: +463.0%
worst_low_after_entry: 70,500
MAE: -1.3%
```

### Interpretation

This is a C24 positive with strict Green cap:

```text
Stage2-Actionable: possible when platform validation, partner, milestone, and development bridge are explicit.
Stage3-Green: possible only with fresh partner economics, clinical/regulatory progress, and commercialization bridge.
Local 4B: monitor after extreme MFE when new evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  platform_license_relevance: very_high
  partner_validation_bridge: high
  milestone_economics_bridge: medium_high
  clinical_regulatory_bridge: medium
  price_confirmation: extreme
  drawdown_penalty: low
  green_cap: required_after_extreme_mfe
```

---

## 6. Case 2 — 235980 메드팩토

```yaml
case_id: C24_R7L96_235980_2024_02_01
symbol: "235980"
name: "메드팩토"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10750
classification: local_burst_oncology_clinical_event_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

메드팩토 is the oncology clinical-event local-burst / 4B failure.

The setup had real C24 relevance:

```text
oncology pipeline / clinical-data optionality
  -> data-event and partner-readthrough expectation
  -> early price confirmation
  -> meaningful local MFE
```

The forward path produced a meaningful MFE into March, so the original trigger is not pure hard-4C. But the later path failed price survival. In C24 terms, the data/partner/cash-runway bridge did not remain strong enough to support Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 11,050 / close 10,750
2024-02-23: high 13,860 / close 13,190
2024-03-05: high 16,900 / close 16,200
2024-03-25: high 17,240 / close 16,940
2024-04-19: low 8,590 / close 9,210
2024-08-05: low 6,370 / close 6,760
2024-11-07: low 4,985 / close around 5,100
```

Approximate path from entry close:

```text
entry_close: 10,750
peak_high: 17,240
MFE: +60.4%
worst_low_after_entry: 4,985
MAE: -53.6%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from oncology clinical-event relevance.
Stage2-Actionable: possible only if endpoint quality, safety, partner economics, and regulatory path are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original entry because meaningful MFE came first.
Corporate-action caveat: avoided by using 2024 rows after the 2023-12-28 candidate window.
```

### Stress-test components

```text
raw_component_score_proxy:
  oncology_clinical_event_relevance: high
  endpoint_quality_bridge: weak_to_medium
  partner_economics_bridge: weak_to_medium
  cash_runway_bridge: weak
  price_confirmation: high_initial
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 217730 강스템바이오텍

```yaml
case_id: C24_R7L96_217730_2024_04_25
symbol: "217730"
name: "강스템바이오텍"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price_basis: close
entry_price: 2975
classification: hard_4c_candidate_stem_cell_clinical_event_late_spike_without_data_regulatory_cashrunway_survival
calibration_usable: true
```

### Evidence interpretation

강스템바이오텍 is the hard C24 guardrail.

The setup looked tempting:

```text
stem-cell / regenerative-medicine label
clinical-event and data-readthrough optionality
post-event volume spike
small bio risk-on rebound
```

But from the selected late-spike entry, the stock produced shallow MFE and then fell into a hard drawdown. The clinical data, regulatory path, cash runway, and commercialization bridge were not strong enough to support Actionable/Green.

### Price path

Key Stock-Web rows:

```text
2024-04-02: high 2,460 / close 2,460
2024-04-03: high 3,050 / close 2,530
2024-04-23: high 2,760 / close 2,700
2024-04-25: high 3,110 / close 2,975
2024-04-30: low 2,600 / close 2,635
2024-08-05: low 1,503 / close 1,557
2024-09-09: low 1,388 / close 1,442
```

Approximate path from late entry close:

```text
entry_close: 2,975
peak_high_after_entry: 3,110
MFE: +4.5%
worst_low_after_entry: 1,388
MAE: -53.3%
```

### Interpretation

This is a hard C24 false-positive:

```text
Stage2-Watch: possible from stem-cell and clinical-event relevance.
Stage2-Actionable: blocked unless data quality, endpoint, safety, regulatory path, and cash runway are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE after a late spike.
Corporate-action caveat: avoided by using 2024 rows after the 2023-11-20 candidate window.
```

The lesson is that stem-cell clinical-event heat is not data/regulatory survival.

### Stress-test components

```text
raw_component_score_proxy:
  stem_cell_clinical_event_label: high
  data_quality_bridge: weak
  regulatory_path_bridge: weak
  cash_runway_bridge: weak
  partner_commercial_bridge: weak
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
platform_license_or_biologic_validation_case_count: 1
clinical_trial_event_case_count: 2
corporate_action_caveat_avoided_count: 2
large_mfe_rerating_cap_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C24 bio event grid:

```text
196170 알테오젠:
  platform-license / biologic validation positive;
  extreme MFE and low MAE, but Green requires refreshed partner/development/commercial bridge.

235980 메드팩토:
  oncology clinical-event local burst;
  meaningful MFE first, then high MAE, local 4B failure.

217730 강스템바이오텍:
  stem-cell clinical-event late spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C24 is not "bio event label is hot."
C24 is "clinical data, endpoint quality, safety, regulatory path, partner economics, cash runway, and commercialization bridge are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C24_R7L96_196170_2024_02_01","scheduled_round":"R7","scheduled_loop":96,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL","symbol":"196170","name":"알테오젠","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":71400,"peak_high":402000,"peak_date":"2024-10-22","worst_low_after_entry":70500,"worst_low_after_entry_date":"2024-02-01","mfe_pct":463.0,"mae_pct":-1.3,"classification":"positive_platform_license_biologic_validation_rerating_with_extreme_mfe_and_green_cap","calibration_usable":true,"evidence_family":"platform_license_biologic_validation_partner_milestone_commercial_bridge","residual_error":"positive_extreme_bio_platform_path_requires_green_cap_without_refreshed_partner_development_commercial_evidence","shadow_rule_candidate":"preserve_platform_license_positive_but_cap_green_after_extreme_mfe_without_fresh_partner_economics"}
{"row_type":"case","case_id":"C24_R7L96_235980_2024_02_01","scheduled_round":"R7","scheduled_loop":96,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL","symbol":"235980","name":"메드팩토","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10750,"peak_high":17240,"peak_date":"2024-03-25","worst_low_after_entry":4985,"worst_low_after_entry_date":"2024-11-07","mfe_pct":60.4,"mae_pct":-53.6,"classification":"local_burst_oncology_clinical_event_label_high_mae_4b_failure","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"oncology_clinical_event_label_without_sustained_endpoint_partner_cashrunway_survival","residual_error":"oncology_clinical_event_label_can_create_mfe_but_fail_green_without_data_partner_and_cashrunway_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_oncology_event_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C24_R7L96_217730_2024_04_25","scheduled_round":"R7","scheduled_loop":96,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL","symbol":"217730","name":"강스템바이오텍","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":2975,"peak_high":3110,"peak_date":"2024-04-25","worst_low_after_entry":1388,"worst_low_after_entry_date":"2024-09-09","mfe_pct":4.5,"mae_pct":-53.3,"classification":"hard_4c_candidate_stem_cell_clinical_event_late_spike_without_data_regulatory_cashrunway_survival","calibration_usable":true,"corporate_action_caveat_avoided":true,"evidence_family":"stem_cell_clinical_event_late_spike_without_data_quality_regulatory_cashrunway_bridge","residual_error":"stem_cell_clinical_event_heat_can_fail_when_data_quality_and_regulatory_cashrunway_bridge_missing","shadow_rule_candidate":"route_stem_cell_clinical_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_data_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":96,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_LICENSE_CLINICAL_DATA_RERATING_VS_TRIAL_LABEL_EVENT_RISK_REVERSAL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"platform_license_or_biologic_validation_case_count":1,"clinical_trial_event_case_count":2,"corporate_action_caveat_avoided_count":2,"large_mfe_rerating_cap_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":96,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","rule_id":"C24_DATA_ENDPOINT_PARTNER_CASHRUNWAY_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C24, do not open Stage2-Actionable or Stage3-Green from clinical-trial headline, platform technology, license optionality, oncology/stem-cell label, partner/milestone/global pharma readthrough, conference abstract/data-preview hype, or one-week bio-stock volume spike alone. Require named asset/indication/partner/mechanism, credible clinical data quality, endpoint/safety/durability/comparator check, regulatory path and next trial design, milestone/royalty/partner economics, cash runway and dilution-risk control, commercialization or licensing path, and post-trigger price survival. Platform-license positives with extreme MFE may be capped Actionable when partner validation is explicit, but Green requires refreshed development and commercial evidence. Oncology or clinical-event names with meaningful MFE followed by high MAE should be local 4B, not Green. Stem-cell or trial-event late spikes with shallow MFE and high MAE should route to hard-4C when data quality, regulatory path, and cash runway are missing.","expected_effect":"Preserve true bio platform or clinical-validation positives while reducing generic trial-label, abstract-hype, and late-spike false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":96,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"data_endpoint_partner_cashrunway_guard","contribution":"Adds one platform-license positive with extreme-MFE cap, one oncology clinical-event local 4B failure, and one stem-cell clinical-event hard-4C counterexample to calibrate C24 data quality, endpoint, partner economics, regulatory path, cash runway, and commercialization requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C24_DATA_ENDPOINT_PARTNER_CASHRUNWAY_BRIDGE_REQUIRED

IF canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK:

  Do not open Stage3-Green from:
    - clinical-trial headline alone
    - platform technology or license optionality alone
    - oncology / stem-cell / regenerative-medicine label alone
    - partner / milestone / global pharma readthrough alone
    - conference abstract / data-preview hype alone
    - one-week bio-stock volume spike alone

  Require at least two of:
    - named asset / indication / partner / mechanism
    - credible clinical data quality
    - endpoint / safety / durability / comparator check
    - regulatory path and next trial design
    - milestone / royalty / partner economics
    - cash runway / dilution-risk containment
    - commercialization or licensing path
    - low-MAE post-trigger price survival
    - fresh evidence after the bio-event headline

  If MFE < 8% and MAE < -35%:
    route to C24 hard-4C candidate.

  If MFE > 30% but later MAE is high:
    preserve as local 4B / event burst, not Green, unless current data/partner/cashrunway evidence appears.

  If MFE is extreme:
    cap Green until development and partner economics refresh.

  If a corporate-action candidate is near the window:
    select post-candidate rows only or block contaminated validation.

  Distinguish:
    - platform/clinical names where data and partners become milestones and commercial value
    - from bio-event labels where endpoint, safety, regulatory path, or cash runway breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_96_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C24 bio trial-data/event-risk cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C24_DATA_ENDPOINT_PARTNER_CASHRUNWAY_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C24 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C24 cases agree, consider implementing a canonical guard that:
   - blocks trial-label Green without asset/indication/data/endpoint/safety/regulatory/cashrunway bridge,
   - preserves platform-license positives only with price survival and current partner economics,
   - caps extreme-MFE bio-platform reratings until development evidence refreshes,
   - treats meaningful-MFE/high-MAE oncology events as local 4B,
   - routes shallow-MFE/high-MAE stem-cell or trial-event late spikes to hard-4C.

Expected next schedule:
completed_round = R7
completed_loop = 96
next_round = R8
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 96
next_round = R8
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
