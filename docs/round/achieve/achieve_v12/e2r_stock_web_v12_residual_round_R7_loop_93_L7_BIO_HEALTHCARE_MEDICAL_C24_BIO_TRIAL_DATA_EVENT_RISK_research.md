# E2R Stock-Web v12 Residual Research — R7 / Loop 93

```yaml
scheduled_round: R7
scheduled_loop: 93
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 93
next_round: R8
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_93_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 93
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 hard gate requires:

```text
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

Recent R7 branch usage already covered:

```text
loop89: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop90: C24_BIO_TRIAL_DATA_EVENT_RISK
loop91: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop92: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

This run returns to C24, but avoids the top-covered C24 names and uses a different fine branch:

```text
bio platform / oncology-immunotherapy trial-data optionality / partner readthrough
vs event-spike price-survival failure
```

The goal is not to repeat generic drug approval or medical device export cases. The goal is to test whether a bio event becomes:

```text
validated data, partner economics, probability of success, cash runway, and price survival
```

rather than just:

```text
oncology / immunotherapy / platform label + event volume.
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
950220 네오이뮨텍
```

They avoid the C24 top-covered symbols and avoid recent R7 loop91~92 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
196170: same archetype, new symbol, bio-platform partner optionality positive with massive price survival
235980: same archetype, new symbol, oncology data/local burst followed by high-MAE 4B failure
950220: same archetype, new symbol, immunotherapy event spike with shallow MFE and hard-4C routing
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
  tradable_ohlcv rows: 1,513
  corporate_action_candidate_dates:
    2020-06-02, 2023-12-28
  selected 2024 trigger after 2023-12-28 candidate; entry~D+180 direct contamination avoided

950220 네오이뮨텍
  profile: atlas/symbol_profiles/950/950220.json
  name history:
    네오이뮨텍(Reg.S) until 2022-03-15
    네오이뮨텍 from 2022-03-16
  first_date: 2021-03-16
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,210
  corporate_action_candidate_dates:
    2025-09-30
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C24 is about trial-data and bio-event risk. It is not a generic "biotech stock went up" archetype.

The model can over-score:

```text
oncology data event
immunotherapy label
bio-platform label
partner optionality
global pharma readthrough
conference / abstract / phase data headline
one-week bio event volume spike
```

The C24 bridge must be stricter:

```text
trial / data / platform event
  -> data quality and endpoint clarity
  -> addressable population and comparator
  -> partner economics or milestone visibility
  -> probability of success
  -> cash runway and dilution risk
  -> commercialization or licensing path
  -> price survival after the first event spike
```

A bio event is a microscope slide. The first glance can look promising, but the stock only deserves higher confidence when the image stays clear under magnification: endpoint, comparator, safety, partner terms, runway, and follow-up data.

---

## 5. Case 1 — 196170 알테오젠

```yaml
case_id: C24_R7L93_196170_2024_02_22
symbol: "196170"
name: "알테오젠"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE
trigger_date: 2024-02-22
entry_date: 2024-02-22
entry_price_basis: close
entry_price: 105000
classification: positive_bio_platform_partner_optionality_with_price_survival_and_4b_watch
calibration_usable: true
```

### Evidence interpretation

알테오젠 is the constructive control in this set.

The useful C24 read is not simply:

```text
biotech platform stock went up
```

It is:

```text
platform optionality / partner economics
  -> global pharma readthrough
  -> follow-on price confirmation
  -> repeated new highs
  -> market treating the event as more than a one-day spike
```

The price path was extremely strong and never revisited the entry close in the checked post-entry window. However, the magnitude of MFE means C24 still needs 4B discipline after major rerating unless fresh partner/milestone/economic evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-22: high 105,000 / close 105,000
2024-02-23: high 136,500 / close 131,200
2024-02-26: high 161,700 / close 156,600
2024-03-05: high 194,000 / close 192,200
2024-03-25: high 216,000 / close 213,500
2024-07-31: high 328,500 / close 315,000
2024-09-20: high 363,500 / close 363,000
2024-10-22: high 402,000 / close 383,500
```

Approximate path from entry close:

```text
entry_close: 105,000
peak_high: 402,000
MFE: +282.9%
worst_post_entry_low_checked: above entry after 2024-02-22 close
MAE: 0.0% from close-entry perspective
```

### Interpretation

This is a C24 positive, but it is not a rule to Green all bio-platform events:

```text
Stage2-Actionable: valid if partner/economic bridge is explicit.
Stage3-Green: possible only with endpoint / platform economics / milestone quality / runway evidence.
Local 4B: mandatory after multi-bagger MFE unless fresh evidence renews the bridge.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  platform_partner_relevance: very_high
  endpoint_or_product_specificity: medium_high
  partner_economics_visibility: medium_high
  cash_runway_dilution_risk: medium
  price_confirmation: extreme
  price_survival: very_high
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 235980 메드팩토

```yaml
case_id: C24_R7L93_235980_2024_02_21
symbol: "235980"
name: "메드팩토"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 11920
classification: local_burst_high_mae_oncology_data_event_without_durable_probability_bridge
calibration_usable: true
```

### Evidence interpretation

메드팩토 is the local-burst / high-MAE case.

The February and March price action made the event look attractive:

```text
oncology / biomarker / clinical data optionality
  -> sharp trial-event price response
  -> meaningful MFE
```

But the move did not survive. The later path shows why C24 must separate tradable event bursts from durable data validation. Without endpoint clarity, partner economics, cash runway, and probability upgrade, the model should not keep Green open.

### Price path

Key Stock-Web rows:

```text
2024-02-21: high 12,170 / close 11,920
2024-02-23: high 13,860 / close 13,190
2024-02-27: high 15,860 / close 15,110
2024-03-05: high 16,900 / close 16,200
2024-03-25: high 17,240 / close 16,940
2024-04-19: low 8,590 / close 9,210
2024-08-05: low 6,370 / close 6,760
2024-11-07: low near 4,985 area
```

Approximate path from entry close:

```text
entry_close: 11,920
peak_high: 17,240
MFE: +44.6%
worst_low_checked: 4,985
MAE: -58.2%
```

### Interpretation

This is a local 4B / event-burst failure:

```text
Stage2-Watch: valid from clinical-event relevance.
Stage2-Actionable: possible only as event-trading unless data/partner/probability bridge is explicit.
Stage3-Green: blocked after the later drawdown.
Local 4B: required after +40% MFE and later -50%+ MAE.
Hard 4C: not the original label because MFE came first, but late re-entry without new data would be hard-4C.
```

### Stress-test components

```text
raw_component_score_proxy:
  oncology_event_relevance: high
  data_quality_bridge: weak_to_medium
  partner_economics_bridge: weak
  cash_runway_dilution_risk: high
  price_confirmation: high_initial
  price_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 950220 네오이뮨텍

```yaml
case_id: C24_R7L93_950220_2024_03_22
symbol: "950220"
name: "네오이뮨텍"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE
trigger_date: 2024-03-22
entry_date: 2024-03-22
entry_price_basis: close
entry_price: 1800
classification: hard_4c_candidate_immunotherapy_event_spike_without_endpoint_partner_cash_bridge
calibration_usable: true
```

### Evidence interpretation

네오이뮨텍 is the hard guardrail case.

The stock generated repeated event-like spikes:

```text
immunotherapy label
clinical-event readthrough
conference / data / oncology theme trading
```

But the March close-entry did not become a durable C24 positive. The MFE was shallow relative to the later downside, and the event did not produce a clear endpoint/partner/cash-runway bridge.

### Price path

Key Stock-Web rows:

```text
2024-03-22: high 1,893 / close 1,800
2024-03-25: high 1,977 / close 1,878
2024-04-08: low 1,475 / close 1,506
2024-04-25: high 1,818 / close 1,651
2024-04-30: high 2,010 / close 1,830
2024-08-05: low 1,200 / close 1,340
2024-09-09: high 1,745 / close 1,745
2024-11-07: low near 1,369 area
```

Approximate path from entry close:

```text
entry_close: 1,800
peak_high: 2,010
MFE: +11.7%
worst_low: 1,200
MAE: -33.3%
```

### Interpretation

This is a hard C24 false-positive:

```text
Stage2-Watch: possible from immunotherapy event relevance.
Stage2-Actionable: blocked unless endpoint, partner, and cash-runway bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The later September spike shows the stock can trade as an event, but the March entry did not prove a durable data-value conversion.

### Stress-test components

```text
raw_component_score_proxy:
  immunotherapy_label: high
  clinical_event_relevance: medium_high
  endpoint_clarity: weak
  partner_economics_bridge: weak
  cash_runway_risk: high
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C24 grid:

```text
196170 알테오젠:
  bio-platform / partner optionality positive with extraordinary price survival;
  still requires local 4B after multi-bagger MFE.

235980 메드팩토:
  oncology-data event local burst;
  meaningful MFE first, but later high-MAE means 4B/event-burst, not Green.

950220 네오이뮨텍:
  immunotherapy event spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C24 is not "bio event or clinical label."
C24 is "data quality, endpoint clarity, partner economics, runway, and follow-up probability survive the event spike."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C24_R7L93_196170_2024_02_22","scheduled_round":"R7","scheduled_loop":93,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE","symbol":"196170","name":"알테오젠","trigger_date":"2024-02-22","entry_date":"2024-02-22","entry_price":105000,"peak_high":402000,"peak_date":"2024-10-22","worst_post_entry_low_checked":119000,"worst_post_entry_low_checked_date":"2024-02-23","mfe_pct":282.9,"mae_pct":0.0,"classification":"positive_bio_platform_partner_optionality_with_price_survival_and_4b_watch","calibration_usable":true,"evidence_family":"bio_platform_partner_optionality_price_survival_milestone_bridge","residual_error":"positive_platform_event_still_requires_4b_after_multibagger_mfe_without_fresh_partner_milestone_evidence","shadow_rule_candidate":"preserve_positive_when_partner_economics_and_price_survival_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C24_R7L93_235980_2024_02_21","scheduled_round":"R7","scheduled_loop":93,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE","symbol":"235980","name":"메드팩토","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":11920,"peak_high":17240,"peak_date":"2024-03-25","worst_low_checked":4985,"worst_low_checked_date":"2024-11-07","mfe_pct":44.6,"mae_pct":-58.2,"classification":"local_burst_high_mae_oncology_data_event_without_durable_probability_bridge","calibration_usable":true,"evidence_family":"oncology_data_event_local_burst_without_endpoint_partner_cash_bridge","residual_error":"clinical_event_can_create_large_mfe_but_fail_green_without_data_quality_and_runway_bridge","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_bio_data_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C24_R7L93_950220_2024_03_22","scheduled_round":"R7","scheduled_loop":93,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE","symbol":"950220","name":"네오이뮨텍","trigger_date":"2024-03-22","entry_date":"2024-03-22","entry_price":1800,"peak_high":2010,"peak_date":"2024-04-30","worst_low":1200,"worst_low_date":"2024-08-05","mfe_pct":11.7,"mae_pct":-33.3,"classification":"hard_4c_candidate_immunotherapy_event_spike_without_endpoint_partner_cash_bridge","calibration_usable":true,"evidence_family":"immunotherapy_event_spike_without_endpoint_partner_cash_runway_bridge","residual_error":"immunotherapy_label_event_spike_can_fail_when_endpoint_and_cash_bridge_missing","shadow_rule_candidate":"route_shallow_mfe_high_mae_immunotherapy_event_spikes_to_hard_4c"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":93,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"BIO_PLATFORM_TRIAL_DATA_PARTNER_OPTIONALITY_PRICE_SURVIVAL_VS_ONCOLOGY_IMMUNOTHERAPY_EVENT_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":93,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","rule_id":"C24_DATA_ENDPOINT_PARTNER_RUNWAY_PRICE_SURVIVAL_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C24, do not open Stage2-Actionable or Stage3-Green from oncology, immunotherapy, platform, conference, phase-data, partner-readthrough, or one-week bio-event spike labels alone. Require data quality, endpoint clarity, addressable population, comparator or safety context, partner economics or milestone visibility, probability-of-success upgrade, cash runway/dilution risk check, and post-trigger price survival. Bio-platform positives with strong price survival may be Actionable but should attach local 4B after very large MFE unless fresh partner/milestone evidence appears. Bio data events with meaningful MFE followed by high MAE should remain local 4B, not Green. Immunotherapy/event spikes with shallow MFE and high MAE should route to hard-4C when endpoint, partner, and cash-runway bridge are missing.","expected_effect":"Preserve true bio-platform/data positives with price survival while reducing oncology/immunotherapy event-spike false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":93,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"bio_trial_data_endpoint_partner_runway_guard","contribution":"Adds one bio-platform price-survival positive, one oncology-data local 4B failure, and one immunotherapy hard-4C counterexample to calibrate C24 data quality, partner economics, runway, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C24_DATA_ENDPOINT_PARTNER_RUNWAY_PRICE_SURVIVAL_REQUIRED

IF canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK:

  Do not open Stage3-Green from:
    - oncology / immunotherapy label alone
    - bio-platform label alone
    - conference / abstract / phase-data headline alone
    - partner readthrough alone
    - one-week bio-event volume spike alone

  Require at least two of:
    - endpoint clarity
    - data quality and comparator context
    - safety/tolerability context
    - addressable patient population
    - partner economics / milestone visibility
    - probability-of-success upgrade
    - cash runway and dilution-risk containment
    - low-MAE post-trigger price survival
    - fresh follow-up data after the first event

  If MFE < 15% and MAE < -30%:
    route to C24 hard-4C candidate.

  If MFE > 30% but later MAE < -40%:
    preserve as local 4B / event burst, not Green, unless fresh data or partner economics appear.

  If MFE is extraordinary and MAE stays controlled:
    preserve positive classification but attach local 4B after the move unless new milestone evidence refreshes the thesis.

  Distinguish:
    - platform/partner events that keep making higher highs
    - from oncology/immunotherapy labels where initial data excitement decays into dilution/runway risk.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_93_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C24 bio trial/data-event cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C24_DATA_ENDPOINT_PARTNER_RUNWAY_PRICE_SURVIVAL_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C24 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C24 cases agree, consider implementing a canonical guard that:
   - blocks bio-event Green without endpoint/data/partner/runway bridge,
   - preserves platform positives only with price survival and milestone evidence,
   - attaches local 4B after huge MFE or meaningful MFE followed by high MAE,
   - routes shallow-MFE/high-MAE immunotherapy event spikes to hard-4C.

Expected next schedule:
completed_round = R7
completed_loop = 93
next_round = R8
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 93
next_round = R8
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
