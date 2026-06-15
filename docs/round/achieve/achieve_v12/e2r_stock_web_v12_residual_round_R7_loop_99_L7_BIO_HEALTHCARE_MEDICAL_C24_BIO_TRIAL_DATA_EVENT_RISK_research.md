# E2R Stock-Web v12 Residual Research — R7 / Loop 99

```yaml
scheduled_round: R7
scheduled_loop: 99
large_sector_id: L7_BIO_HEALTHCARE_MEDICAL
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
cell_therapy_trial_case_count: 2
immuno_oncology_platform_case_count: 1
clinical_data_event_case_count: 3
trial_endpoint_safety_bridge_missing_count: 2
patient_enrollment_followup_bridge_missing_count: 2
financing_dilution_bridge_caveat_count: 2
data_window_separation_required_count: 1
direct_2024_corporate_action_rejected_count: 2
old_corporate_action_or_name_history_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R7
completed_loop: 99
next_round: R8
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R6_loop_99_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R7
scheduled_loop = 99
large_sector_id = L7_BIO_HEALTHCARE_MEDICAL
```

R7 is the bio / healthcare / medical round. The selected canonical archetype is:

```text
C24_BIO_TRIAL_DATA_EVENT_RISK
```

Recent R7 branch usage:

```text
loop95: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
loop96: C24_BIO_TRIAL_DATA_EVENT_RISK
loop97: C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT
loop98: C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION
```

This run returns to C24 after the R7 branch cycle.

Selected fine branch:

```text
cell therapy / immuno-oncology / clinical-stage platform
trial endpoint, patient enrollment, follow-up duration, safety profile,
data-window separation, regulatory path, partner optionality, financing/dilution,
and survival-to-next-catalyst bridge
vs generic clinical-data / trial-progress label spike
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
115450 HLB테라퓨틱스
174900 앱클론
950220 네오이뮨텍
```

They avoid the C24 top-covered list and recent R7 names:

```text
C24 top-covered avoid:
  298380, 323990, 007390, 087010, 141080, 226950

recent R7 avoid:
  loop98 C23: 000250, 145020, 206650
  loop97 C25: 226400, 065510, 263690
  loop96 C24: 196170, 235980, 217730
  loop95 C23: 207940, 068270, 086900
```

Rejected candidates:

```text
314130 지놈앤컴퍼니:
  profile has 2024-08-06 and 2024-08-27 corporate-action candidate dates.
  It showed a hard drawdown path, but the selected 2024 validation window is too contaminated for a clean C24 case.

288330 브릿지바이오테라퓨틱스 / 파라택시스코리아:
  profile has 2024-08-08 corporate-action candidate and later 2025 name change.
  It is useful as a caveat example, not as a clean primary case in this file.
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
115450: same archetype, new symbol, clinical-stage / HLB-group trial-data event positive with Green cap after extreme MFE.
174900: same archetype, new symbol, cell-therapy / CAR-T trial-data local 4B after meaningful MFE and later material MAE.
950220: same archetype, new symbol, immuno-oncology platform Watch/Yellow cap after local data spikes failed durable endpoint / financing / margin-survival bridge.
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
115450 HLB테라퓨틱스
  profile: atlas/symbol_profiles/115/115450.json
  name history:
    디지탈아리아 -> 지트리비앤티 -> 에이치엘비테라퓨틱스 -> HLB테라퓨틱스
  first_date: 2010-03-26
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,915
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2011-12-15, 2014-02-12, 2023-03-15, 2023-04-11
  2024 entry~D+180 contamination: none
  caveat:
    historical name / raw-discontinuity candidates are outside selected 2024 validation window.

174900 앱클론
  profile: atlas/symbol_profiles/174/174900.json
  first_date: 2017-09-18
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,063
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2020-07-16, 2020-08-05
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

950220 네오이뮨텍
  profile: atlas/symbol_profiles/950/950220.json
  name history:
    네오이뮨텍(Reg.S) -> 네오이뮨텍
  first_date: 2021-03-16
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,210
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2025-09-30
  2024 entry~D+180 contamination: none
  caveat:
    Reg.S / short listing history and future corporate-action candidate are outside selected 2024 validation window.

Rejected:
314130 지놈앤컴퍼니
  profile: KONEX -> KOSDAQ history.
  corporate_action_candidate_dates include 2024-08-06 and 2024-08-27.
  Rejected from primary three-case set.

288330 브릿지바이오테라퓨틱스 / 파라택시스코리아
  profile has 2024-08-08 corporate-action candidate and later 2025 name change.
  Rejected from primary clean validation set.
```

---

## 4. Archetype residual problem

C24 is about clinical trial data and event risk. It is not a generic "bio pipeline stock is moving" archetype.

The model can over-score:

```text
clinical trial data label
phase 1/2 progress headline
CAR-T / cell therapy / immuno-oncology platform label
HLB-group or partner readthrough
patient enrollment / dose escalation headline
orphan / rare-disease / oncology optionality
poster / conference / abstract rumor
one-week bio-stock volume spike
late chase after a trial-data rerating
```

The C24 bridge must be stricter:

```text
clinical data / trial event
  -> named asset, indication, trial phase, and geography
  -> endpoint clarity and statistical interpretation
  -> patient number, follow-up duration, response durability, and comparator context
  -> safety profile and dose-limiting toxicity check
  -> enrollment pace and next data window
  -> regulatory path and partner / license-out optionality
  -> cash runway, financing, dilution, and going-concern risk
  -> manufacturing / CMC feasibility for cell therapy or biologics
  -> event-window separation after the first data spike
  -> price survival after the clinical-data rerating
```

A C24 thesis is like a trial readout under a microscope. A headline can make the slide glow, but equity value appears only when the endpoint is interpretable, the patient count is real, follow-up is durable, safety is acceptable, the next regulatory step is fundable, and the company survives long enough to reach the next data window.

---

## 5. Case 1 — 115450 HLB테라퓨틱스

```yaml
case_id: C24_R7L99_115450_2024_02_01
symbol: "115450"
name: "HLB테라퓨틱스"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 6800
classification: positive_clinical_stage_event_readthrough_with_extreme_mfe_green_cap
calibration_usable: true
```

### Evidence interpretation

HLB테라퓨틱스 is the constructive C24 positive in this set.

The useful C24 read is not simply:

```text
HLB그룹 / 임상 기대주가 강하다
```

It is:

```text
clinical-stage event and group readthrough
  -> trial / regulatory optionality
  -> partner and next-data-window expectation
  -> extreme March-April price confirmation
  -> Green cap because endpoint / safety / regulatory path / financing evidence must refresh
```

The forward path produced extreme MFE and avoided a hard drawdown from the February entry. This validates a positive C24 event case. However, after such a rerating, unrestricted Green is dangerous unless the endpoint, safety, next regulatory path, cash runway, and financing bridge remain current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,030 / low 6,390 / close 6,800
2024-02-05: high 9,200 / close 8,510
2024-03-13: high 10,920 / close 9,720
2024-03-26: high 15,790 / close 14,600
2024-04-08: high 17,700 / close 16,490
2024-08-05: low 7,580 / close 7,850
2024-09-24: high 10,800 / close 10,510
2024-10-21: high 9,870 / close 9,700
```

Approximate path from entry close:

```text
entry_close: 6,800
peak_high: 17,700
MFE: +160.3%
worst_low_after_entry: 6,390
MAE: -6.0%
```

### Interpretation

This is a C24 positive with Green cap:

```text
Stage2-Actionable: possible if asset, trial phase, endpoint, safety, next regulatory path, and financing bridge are explicit.
Stage3-Green: blocked after +160% MFE unless fresh endpoint / safety / financing evidence appears.
Local 4B: monitor if price outruns the next data window.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  clinical_event_relevance: high
  group_readthrough_signal: high
  endpoint_safety_bridge: medium
  regulatory_path_bridge: medium
  financing_runway_bridge: medium
  price_confirmation: extreme
  drawdown_penalty: low
  green_cap: required_after_extreme_mfe
```

---

## 6. Case 2 — 174900 앱클론

```yaml
case_id: C24_R7L99_174900_2024_02_01
symbol: "174900"
name: "앱클론"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 14020
classification: local_positive_cell_therapy_trial_data_mfe_with_4b_after_followup_financing_evidence_decay
calibration_usable: true
```

### Evidence interpretation

앱클론 is the cell-therapy / CAR-T local positive with 4B discipline.

The setup had real C24 relevance:

```text
cell therapy / CAR-T platform
  -> clinical data and response-rate readthrough
  -> patient enrollment and follow-up optionality
  -> February-March price confirmation
  -> later drawdown and evidence-decay risk
```

The stock produced meaningful MFE first, but later fell materially into August. This should not become unrestricted Green. It is a local positive / 4B case unless fresh patient-count, response durability, safety, manufacturing, financing, and next-data-window evidence refreshes.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 14,730 / low 13,710 / close 14,020
2024-02-27: high 18,370 / close 17,150
2024-03-05: high 22,150 / close 21,100
2024-04-17: low 14,440 / close 14,450
2024-08-05: low 10,830 / close 11,080
2024-08-14: high 17,680 / close 17,450
2024-10-18: high 18,100 / close 16,930
```

Approximate path from entry close:

```text
entry_close: 14,020
peak_high: 22,150
MFE: +58.0%
worst_low_after_entry: 10,830
MAE: -22.8%
```

### Interpretation

This is a C24 local positive / 4B case:

```text
Stage2-Actionable: possible if asset, patient count, endpoint, durability, safety, and financing bridge are explicit.
Stage3-Green: blocked after later material MAE.
Local 4B: required.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  cell_therapy_trial_relevance: high
  endpoint_signal: medium_high
  patient_followup_bridge: weak_to_medium
  safety_cmc_bridge: weak_to_medium
  financing_runway_bridge: weak_to_medium
  price_confirmation: high_initial
  later_drawdown_penalty: material
  local_4b_overlay: required
```

---

## 7. Case 3 — 950220 네오이뮨텍

```yaml
case_id: C24_R7L99_950220_2024_02_01
symbol: "950220"
name: "네오이뮨텍"
canonical_archetype_id: C24_BIO_TRIAL_DATA_EVENT_RISK
fine_archetype_id: CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 1595
classification: watch_cap_immuno_oncology_platform_trial_label_without_durable_endpoint_financing_survival
calibration_usable: true
```

### Evidence interpretation

네오이뮨텍 is the immuno-oncology platform Watch cap.

The label can fool the model:

```text
immuno-oncology platform
  -> clinical trial progress readthrough
  -> poster / abstract / conference event beta
  -> short-lived data-window volume spikes
```

The path produced several local spikes, but the first trigger did not validate sustained Actionable / Green. MFE was meaningful but not enough to survive the later drawdown and financing/dilution risk. The September spike should be separated as a later event window rather than used to retroactively validate the February trigger.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 1,620 / low 1,568 / close 1,595
2024-02-28: high 1,806 / close 1,708
2024-03-25: high 1,977 / close 1,878
2024-04-30: high 2,010 / close 1,830
2024-08-05: low 1,200 / close 1,340
2024-09-09: high 1,745 / close 1,745
2024-10-17: high 1,670 / close 1,581
```

Approximate path from entry close:

```text
entry_close: 1,595
peak_high_first_window: 2,010
MFE: +26.0%
worst_low_after_entry: 1,200
MAE: -24.8%
```

### Interpretation

This is a C24 Watch / 4B cap:

```text
Stage2-Watch: valid from immuno-oncology platform and clinical-event relevance.
Stage2-Actionable: blocked unless endpoint, patient follow-up, safety, next data window, and financing bridge are explicit.
Stage3-Green: blocked.
Local 4B: monitor because local data spikes did not create durable price survival.
Hard 4C: no, because MAE did not cross hard threshold.
Event-window separation: September spike should be treated as a separate event window.
```

The lesson is that a trial-platform label can spark volume without converting into durable endpoint / financing survival.

### Stress-test components

```text
raw_component_score_proxy:
  immuno_oncology_platform_label: high
  trial_event_signal: medium_high
  endpoint_bridge: weak_to_medium
  patient_followup_bridge: weak
  financing_dilution_bridge: weak
  price_confirmation: local_only
  drawdown_penalty: material
  actionability_cap: Watch/4B
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
cell_therapy_trial_case_count: 2
immuno_oncology_platform_case_count: 1
clinical_data_event_case_count: 3
trial_endpoint_safety_bridge_missing_count: 2
patient_enrollment_followup_bridge_missing_count: 2
financing_dilution_bridge_caveat_count: 2
data_window_separation_required_count: 1
direct_2024_corporate_action_rejected_count: 2
old_corporate_action_or_name_history_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C24 clinical-data grid:

```text
115450 HLB테라퓨틱스:
  clinical-stage / HLB-group event positive;
  extreme MFE and low MAE, but Green requires fresh endpoint, safety, regulatory-path, and financing evidence.

174900 앱클론:
  cell-therapy / CAR-T local positive;
  meaningful MFE first, then material MAE, local 4B.

950220 네오이뮨텍:
  immuno-oncology platform Watch cap;
  local spikes but no durable endpoint / financing / price-survival bridge.
```

Shared rule:

```text
C24 is not "clinical data label is exciting."
C24 is "endpoint, patient count, follow-up durability, safety, next data window, regulatory path, cash runway, and financing survival are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C24_R7L99_115450_2024_02_01","scheduled_round":"R7","scheduled_loop":99,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE","symbol":"115450","name":"HLB테라퓨틱스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":6800,"peak_high":17700,"peak_date":"2024-04-08","worst_low_after_entry":6390,"worst_low_after_entry_date":"2024-02-01","mfe_pct":160.3,"mae_pct":-6.0,"classification":"positive_clinical_stage_event_readthrough_with_extreme_mfe_green_cap","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"evidence_family":"clinical_stage_hlb_group_trial_event_endpoint_safety_regulatory_path_financing_bridge","residual_error":"extreme_trial_event_positive_requires_green_cap_without_refreshed_endpoint_safety_regulatory_and_financing_evidence","shadow_rule_candidate":"allow_capped_actionable_when_endpoint_safety_regulatory_path_and_financing_bridge_confirm_but_cap_green_after_extreme_mfe"}
{"row_type":"case","case_id":"C24_R7L99_174900_2024_02_01","scheduled_round":"R7","scheduled_loop":99,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE","symbol":"174900","name":"앱클론","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":14020,"peak_high":22150,"peak_date":"2024-03-05","worst_low_after_entry":10830,"worst_low_after_entry_date":"2024-08-05","mfe_pct":58.0,"mae_pct":-22.8,"classification":"local_positive_cell_therapy_trial_data_mfe_with_4b_after_followup_financing_evidence_decay","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"cell_therapy_car_t_trial_data_endpoint_patient_followup_safety_cmc_financing_bridge","residual_error":"cell_therapy_trial_data_can_create_mfe_but_requires_4b_when_followup_safety_and_financing_evidence_decays","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_cell_therapy_trial_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C24_R7L99_950220_2024_02_01","scheduled_round":"R7","scheduled_loop":99,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE","symbol":"950220","name":"네오이뮨텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":1595,"peak_high_first_window":2010,"peak_date":"2024-04-30","worst_low_after_entry":1200,"worst_low_after_entry_date":"2024-08-05","mfe_pct":26.0,"mae_pct":-24.8,"classification":"watch_cap_immuno_oncology_platform_trial_label_without_durable_endpoint_financing_survival","calibration_usable":true,"short_listing_or_reg_s_caveat":true,"event_window_separation_required":true,"evidence_family":"immuno_oncology_platform_trial_event_label_without_endpoint_patient_followup_safety_financing_survival","residual_error":"immuno_oncology_platform_label_can_create_local_spikes_but_not_actionable_without_endpoint_and_financing_bridge","shadow_rule_candidate":"cap_immuno_oncology_trial_platform_label_at_watch_4b_if_mfe_local_and_financing_endpoint_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R7","scheduled_loop":99,"large_sector_id":"L7_BIO_HEALTHCARE_MEDICAL","canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","fine_archetype_id":"CELL_THERAPY_IMMUNO_ONCOLOGY_CLINICAL_DATA_PATIENT_ENROLLMENT_ENDPOINT_SAFETY_FINANCING_BRIDGE_VS_TRIAL_DATA_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":0,"cell_therapy_trial_case_count":2,"immuno_oncology_platform_case_count":1,"clinical_data_event_case_count":3,"trial_endpoint_safety_bridge_missing_count":2,"patient_enrollment_followup_bridge_missing_count":2,"financing_dilution_bridge_caveat_count":2,"data_window_separation_required_count":1,"direct_2024_corporate_action_rejected_count":2,"old_corporate_action_or_name_history_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R7","scheduled_loop":99,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","rule_id":"C24_TRIAL_ENDPOINT_SAFETY_FOLLOWUP_FINANCING_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C24 clinical-trial data/event-risk cases, do not open Stage2-Actionable or Stage3-Green from clinical-trial data, phase 1/2 progress, CAR-T/cell-therapy/immuno-oncology platform, group/partner readthrough, patient enrollment, dose escalation, rare-disease/oncology optionality, poster/conference/abstract rumor, one-week bio-stock volume spike, or late chase after trial-data rerating labels alone. Require named asset/indication/trial phase/geography, endpoint clarity and statistical interpretation, patient number/follow-up duration/response durability/comparator context, safety profile and dose-limiting toxicity check, enrollment pace and next data window, regulatory path and partner/license-out optionality, cash runway/financing/dilution/going-concern risk, manufacturing/CMC feasibility for cell therapy or biologics, event-window separation after failed first trigger, and post-trigger price survival. Extreme MFE trial-event positives may be capped Actionable when endpoint/safety/regulatory/financing bridge is explicit, but Green requires fresh evidence. Cell-therapy cases with meaningful MFE followed by material MAE should remain local 4B. Immuno-oncology platform labels with local spikes but weak endpoint/financing bridge should cap at Watch/4B.","expected_effect":"Preserve true clinical-data positives while reducing generic trial-label, platform, group-readthrough, poster/abstract, and late-chase false positives where endpoint, safety, follow-up, financing, CMC, and next-data-window evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"rejected_candidate","scheduled_round":"R7","scheduled_loop":99,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"314130","name":"지놈앤컴퍼니","reason":"Direct 2024 corporate-action candidate dates 2024-08-06 and 2024-08-27 contaminate an otherwise hard-drawdown clinical-stage path. Do not use as clean primary calibration row without adjusted-price review.","do_not_count_as_global_weight_delta":true}
{"row_type":"rejected_candidate","scheduled_round":"R7","scheduled_loop":99,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","symbol":"288330","name":"브릿지바이오테라퓨틱스 / 파라택시스코리아","reason":"2024-08-08 corporate-action candidate and later 2025 name change make it useful as a trust caveat example but not a clean primary row in this run.","do_not_count_as_global_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R7","scheduled_loop":99,"canonical_archetype_id":"C24_BIO_TRIAL_DATA_EVENT_RISK","residual_type":"trial_endpoint_safety_followup_financing_guard","contribution":"Adds one clinical-stage event positive, one cell-therapy local 4B case, and one immuno-oncology Watch/4B cap to calibrate C24 endpoint clarity, patient follow-up, safety, regulatory path, financing, CMC, event-window separation, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C24_TRIAL_ENDPOINT_SAFETY_FOLLOWUP_FINANCING_BRIDGE_REQUIRED

IF canonical_archetype_id == C24_BIO_TRIAL_DATA_EVENT_RISK:

  Do not open Stage3-Green from:
    - clinical trial data label alone
    - phase 1/2 progress headline alone
    - CAR-T / cell therapy / immuno-oncology platform label alone
    - group or partner readthrough alone
    - patient enrollment / dose escalation headline alone
    - orphan / rare-disease / oncology optionality alone
    - poster / conference / abstract rumor alone
    - one-week bio-stock volume spike alone
    - late chase after trial-data rerating alone

  Require at least two of:
    - named asset / indication / trial phase / geography
    - endpoint clarity and statistical interpretation
    - patient number / follow-up duration / response durability / comparator context
    - safety profile and dose-limiting toxicity check
    - enrollment pace and next data window
    - regulatory path and partner / license-out optionality
    - cash runway / financing / dilution / going-concern risk
    - manufacturing / CMC feasibility for cell therapy or biologics
    - event-window separation after failed first trigger
    - low-MAE post-trigger price survival
    - fresh evidence after the clinical-data headline

  If MFE > 50% but endpoint/safety/financing evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but later MAE is material:
    attach local 4B until follow-up / safety / financing evidence refreshes.

  If MFE is local only and bridge is platform-label only:
    cap at Watch/4B.

  If direct 2024 corporate-action or share-count caveat appears:
    reject from clean primary calibration unless adjusted-price review is available.

  Distinguish:
    - pipelines where data becomes interpretable endpoint, durable follow-up, regulatory path, financing survival, and next-catalyst visibility
    - from labels where the trial headline glows but the microscope slide does not yet prove value.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R7_loop_99_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C24 clinical trial data/event-risk cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C24_TRIAL_ENDPOINT_SAFETY_FOLLOWUP_FINANCING_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C24 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Do not ingest rejected_candidate rows as primary calibration cases.
8. If enough C24 cases agree, consider implementing a canonical guard that:
   - blocks trial-data Green without named asset/indication/phase, endpoint, patient number, follow-up, safety, and financing bridge,
   - preserves extreme-MFE clinical-event positives only with price survival and fresh endpoint/safety evidence,
   - treats meaningful-MFE/material-MAE cell-therapy cases as local 4B,
   - caps platform-label-only immuno-oncology cases at Watch/4B,
   - separates later event windows from first trigger windows,
   - rejects direct 2024 corporate-action contaminated rows unless adjusted-price review exists.

Expected next schedule:
completed_round = R7
completed_loop = 99
next_round = R8
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R7
completed_loop = 99
next_round = R8
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
