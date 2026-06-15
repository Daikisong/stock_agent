# E2R Stock-Web v12 Residual Research — R11 / Loop 99

```yaml
scheduled_round: R11
scheduled_loop: 99
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE

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
hard_4c_candidate_count: 1

telemedicine_policy_case_count: 3
digital_health_platform_case_count: 2
emr_hospital_platform_case_count: 1
pharmacy_clinic_platform_case_count: 1
policy_to_order_revenue_bridge_missing_count: 2
platform_adoption_retention_margin_bridge_missing_count: 2
financing_or_smallcap_event_beta_caveat_count: 2
event_window_separation_required_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
direct_2024_corporate_action_rejected_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 99
next_round: R12
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_99_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 99
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use the L10 policy / event / miscellaneous branch. This run uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Selected fine branch:

```text
telemedicine / digital health / EMR / clinic and pharmacy platform policy
medical-access policy, temporary or permanent telemedicine rules,
hospital / clinic / pharmacy adoption, public or insurer reimbursement,
platform traffic, order/revenue conversion, compliance, support cost,
renewal/retention, and margin bridge
vs generic telemedicine / digital-health policy label spike
```

This deliberately avoids:
- C31 top-covered names:
  `013990`, `003550`, `015760`, `032350`, `114090`, `000270`
- R11 loop98 education-policy branch:
  `100220`, `053290`, `057030`
- R11 loop97 environmental-policy branch:
  `029960`, `067900`, `009440`
- R12 loop96 low-birthrate policy branch:
  `407400`, `159580`, `014100`
- R12 loop95 carbon / CCUS policy branch:
  `083420`, `448280`, `119650`
- R11 loop95 tourism branch:
  `034230`, `950170`, `008770`
- R12 loop94 education branch:
  `096240`, `072870`, `095720`

Selected symbols:

```text
032620 유비케어
032850 비트컴퓨터
099750 이지케어텍
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows: 97
symbols: 70
date_range: 2020-01-23~2025-01-17
good/bad S2: 35/25
4B/4C: 5/0
URL pending/proxy: 25/25
top covered symbols:
  013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
032620: same archetype, new symbol, clinic/pharmacy platform telemedicine policy positive with 4B/Green cap after large MFE and later drawdown.
032850: same archetype, new symbol, telemedicine / hospital IT policy label hard-4C candidate after initial event spike failed policy-to-revenue survival.
099750: same archetype, new symbol, EMR / hospital platform telemedicine policy local positive / Watch cap after policy spike but weak durable order and margin bridge.
```

Rejected candidate:

```text
033230 인성정보:
  checked as a telemedicine / remote-care infrastructure candidate.
  rejected from primary rows because profile has a 2024-07-12 corporate-action candidate,
  contaminating a first-half 2024 policy-event validation window.
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
032620 유비케어
  profile: atlas/symbol_profiles/032/032620.json
  name history:
    메디다스 -> UBCARE -> 이수유비케어 -> 유비케어
  first_date: 1997-05-07 in tradable profile
  raw_first_date: 1997-05-02
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,890
  non_tradable_zero_volume rows: 288
  corporate_action_candidate_dates:
    1998-01-06, 1999-08-30, 1999-10-21, 1999-11-05, 1999-12-07, 2018-05-11
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / row-presence caveats exist outside selected 2024 validation window.

032850 비트컴퓨터
  profile: atlas/symbol_profiles/032/032850.json
  first_date: 1997-07-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 7,004
  non_tradable_zero_volume rows: 123
  corporate_action_candidate_dates:
    1999-06-22, 1999-07-16, 1999-11-15, 2000-02-25, 2000-04-25
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / row-presence caveats exist outside selected 2024 validation window.

099750 이지케어텍
  profile: atlas/symbol_profiles/099/099750.json
  first_date: 2019-03-22
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,699
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2025-12-18, 2026-01-08
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history versus old healthcare IT names; future corporate-action candidates are outside selected 2024 validation window.

Rejected:
033230 인성정보
  profile: atlas/symbol_profiles/033/033230.json
  corporate_action_candidate_dates include 2024-07-12.
  rejected from primary clean validation set.
```

---

## 4. Archetype residual problem

C31 is a policy / subsidy / legislation / event archetype. In this fine branch, the event is telemedicine, digital health, EMR, hospital IT, and clinic/pharmacy platform policy. It is not a generic "remote medical care policy is hot" archetype.

The model can over-score:

```text
telemedicine policy label
digital health / medical access headline
hospital IT / EMR / clinic platform label
pharmacy / clinic network readthrough
temporary non-face-to-face treatment policy rumor
public reimbursement or insurer integration story
remote-care infrastructure label
one-day healthcare IT policy volume spike
later policy-like spike after first-window failure
```

The C31 bridge must be stricter:

```text
telemedicine / digital-health policy event
  -> named policy, rule, payer, region, institution, or adoption schedule
  -> hospital / clinic / pharmacy / patient adoption path
  -> platform traffic and paid conversion
  -> order visibility, renewal, retention, and usage data
  -> EMR / prescription / payment / claims workflow integration
  -> public procurement, insurer, enterprise hospital, clinic, or B2C channel split
  -> compliance, security, support, cloud, labor, and sales cost
  -> revenue recognition and cash collection
  -> gross margin / OP conversion
  -> event-window separation after failed first trigger
  -> price survival after the first telemedicine-policy spike
```

A C31 telemedicine thesis is like opening a digital clinic door. The policy headline unlocks access, but equity value appears only when doctors, clinics, pharmacies, and patients actually use the system, usage becomes paid orders or renewals, compliance and support costs do not eat the margin, and cash reaches the software provider.

---

## 5. Case 1 — 032620 유비케어

```yaml
case_id: C31_R11L99_032620_2024_02_01
symbol: "032620"
name: "유비케어"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5000
classification: positive_clinic_pharmacy_platform_telemedicine_policy_with_4b_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

유비케어 is the constructive telemedicine / clinic-pharmacy platform control in this set.

The useful C31 read is not simply:

```text
원격의료 / 디지털헬스 정책주가 강하다
```

It is:

```text
clinic / pharmacy healthcare IT platform
  -> non-face-to-face treatment and medical-access policy salience
  -> clinic and pharmacy workflow adoption optionality
  -> February policy-event price confirmation
  -> later 4B / Green cap because adoption, paid conversion, renewal, and margin evidence must refresh
```

The forward path produced a large MFE in February. However, the later drawdown into August shows why the model should not leave the name as ordinary Green from policy label alone. The bridge from policy to clinic/pharmacy adoption, order, usage, renewal, revenue recognition, and OP must be refreshed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,980 / low 4,990 / close 5,000
2024-02-16: high 6,200 / close 6,200
2024-02-19: high 7,370 / close 6,570
2024-02-23: high 7,910 / close 7,170
2024-04-17: low 4,630 / close 4,630
2024-08-05: low 3,460 / close 3,570
2024-08-27: high 5,220 / close 4,495
2024-11-01: high 4,950 / close 4,540
```

Approximate path from entry close:

```text
entry_close: 5,000
peak_high: 7,910
MFE: +58.2%
worst_low_after_entry: 3,460
MAE: -30.8%
```

### Interpretation

This is a C31 positive with 4B / Green cap:

```text
Stage2-Actionable: possible if clinic/pharmacy adoption, policy rule, usage, renewal, and revenue/margin bridge are explicit.
Stage3-Green: blocked after large MFE and later high MAE unless fresh adoption/order evidence appears.
Local 4B: required after the August drawdown.
Hard 4C: no, because large MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  clinic_pharmacy_platform_relevance: high
  telemedicine_policy_signal: high
  adoption_order_bridge: medium
  renewal_retention_bridge: weak_to_medium
  compliance_support_cost_bridge: weak_to_medium
  revenue_margin_bridge: medium
  price_confirmation: very_high_initial
  later_drawdown_penalty: high
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 032850 비트컴퓨터

```yaml
case_id: C31_R11L99_032850_2024_02_01
symbol: "032850"
name: "비트컴퓨터"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 8280
classification: hard_4c_candidate_telemedicine_hospital_it_policy_label_without_platform_revenue_margin_survival
calibration_usable: true
```

### Evidence interpretation

비트컴퓨터 is the hard C31 telemedicine-policy guardrail.

The label can fool the model:

```text
telemedicine / hospital IT / medical software
  -> policy access and remote-care readthrough
  -> medical platform optionality
  -> one-day healthcare IT event spike
```

The February trigger had a large event-day high, but the path failed price survival. MFE from the close was only moderate, and the stock later crossed a severe drawdown zone. The bridge from policy label to adoption, usage, order/revenue, renewal, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 9,550 / close 8,280
2024-02-16: high 8,800 / close 8,380
2024-02-23: high 9,050 / close 8,310
2024-04-09: low 5,850 / close 5,850
2024-08-05: low 4,605 / close 4,740
2024-08-27: high 6,600 / close 5,650
2024-10-25: low 4,750 / close 4,770
```

Approximate path from entry close:

```text
entry_close: 8,280
peak_high_first_phase: 9,550
MFE: +15.3%
worst_low_after_entry: 4,605
MAE: -44.4%
```

### Interpretation

This is a hard C31 false-positive candidate:

```text
Stage2-Watch: possible from telemedicine / hospital IT policy relevance.
Stage2-Actionable: blocked unless policy adoption, hospital/clinic platform order, usage, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by moderate MFE and severe MAE.
Event-window separation: later August healthcare IT rebound should be separated from the failed February trigger.
```

The lesson is that a policy door can open, but the software vendor still needs actual platform adoption and cash conversion.

### Stress-test components

```text
raw_component_score_proxy:
  telemedicine_hospital_it_label: high
  policy_access_signal: high
  hospital_clinic_order_bridge: weak
  usage_retention_bridge: weak
  revenue_margin_bridge: weak
  price_confirmation: moderate_event_day
  later_drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 099750 이지케어텍

```yaml
case_id: C31_R11L99_099750_2024_02_01
symbol: "099750"
name: "이지케어텍"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 17740
classification: local_positive_emr_hospital_platform_telemedicine_policy_mfe_with_watch_4b_cap
calibration_usable: true
```

### Evidence interpretation

이지케어텍 is the EMR / hospital-platform local positive with Watch/4B cap.

The setup had real C31 relevance:

```text
hospital EMR / medical IT platform
  -> telemedicine and digital-health policy readthrough
  -> hospital system order optionality
  -> February event price confirmation
  -> later drawdown and weak durable order bridge
```

The price path produced meaningful MFE, but the later drawdown and low-trade-volume drift mean it should not be ordinary Green. It needs explicit hospital order, implementation, renewal, support-cost, revenue-recognition, and margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 18,780 / close 17,740
2024-02-16: high 21,400 / close 20,550
2024-02-19: high 23,250 / close 20,950
2024-04-17: low 15,920 / close 15,990
2024-08-05: low 12,940 / close 14,750
2024-10-10: high 17,550 / close 17,480
2024-10-24: low 16,230 / close 16,230
```

Approximate path from entry close:

```text
entry_close: 17,740
peak_high: 23,250
MFE: +31.1%
worst_low_after_entry: 12,940
MAE: -27.1%
```

### Interpretation

This is a C31 local positive / Watch-4B cap:

```text
Stage2-Watch: valid from EMR / hospital-platform and digital-health policy relevance.
Stage2-Actionable: possible only if hospital order, implementation, renewal, support cost, and revenue bridge are explicit.
Stage3-Green: blocked after material MAE and stale order evidence.
Local 4B: required.
Hard 4C: no, because meaningful MFE came first and MAE did not cross hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  emr_hospital_platform_relevance: high
  digital_health_policy_signal: medium_high
  hospital_order_bridge: weak_to_medium
  implementation_support_cost_bridge: weak
  renewal_retention_bridge: weak_to_medium
  revenue_margin_bridge: weak_to_medium
  price_confirmation: meaningful_initial
  later_drawdown_penalty: material
  actionability_cap: Watch/4B
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
telemedicine_policy_case_count: 3
digital_health_platform_case_count: 2
emr_hospital_platform_case_count: 1
pharmacy_clinic_platform_case_count: 1
policy_to_order_revenue_bridge_missing_count: 2
platform_adoption_retention_margin_bridge_missing_count: 2
financing_or_smallcap_event_beta_caveat_count: 2
event_window_separation_required_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
direct_2024_corporate_action_rejected_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 telemedicine / digital-health policy grid:

```text
032620 유비케어:
  clinic/pharmacy platform telemedicine-policy positive;
  large MFE first, then high MAE, 4B/Green cap.

032850 비트컴퓨터:
  telemedicine / hospital IT policy label failed;
  moderate MFE and severe MAE, hard 4C candidate.

099750 이지케어텍:
  EMR / hospital-platform local positive;
  meaningful MFE and material MAE, Watch/4B cap.
```

Shared rule:

```text
C31 telemedicine is not "remote medical-care policy label is hot."
C31 telemedicine is "policy becomes hospital/clinic/pharmacy adoption, adoption becomes order/usage/renewal, and revenue survives compliance/support cost to reach OP margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L99_032620_2024_02_01","scheduled_round":"R11","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"032620","name":"유비케어","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5000,"peak_high":7910,"peak_date":"2024-02-23","worst_low_after_entry":3460,"worst_low_after_entry_date":"2024-08-05","mfe_pct":58.2,"mae_pct":-30.8,"classification":"positive_clinic_pharmacy_platform_telemedicine_policy_with_4b_green_cap_after_large_mfe","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"clinic_pharmacy_platform_telemedicine_policy_adoption_order_usage_renewal_revenue_margin_bridge","residual_error":"telemedicine_platform_policy_positive_requires_4b_green_cap_when_policy_rerating_outpaces_adoption_order_revenue_margin_evidence","shadow_rule_candidate":"preserve_clinic_pharmacy_platform_positive_but_cap_green_after_large_mfe_without_fresh_adoption_order_and_margin_evidence"}
{"row_type":"case","case_id":"C31_R11L99_032850_2024_02_01","scheduled_round":"R11","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"032850","name":"비트컴퓨터","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8280,"peak_high_first_phase":9550,"peak_date":"2024-02-01","worst_low_after_entry":4605,"worst_low_after_entry_date":"2024-08-05","mfe_pct":15.3,"mae_pct":-44.4,"classification":"hard_4c_candidate_telemedicine_hospital_it_policy_label_without_platform_revenue_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"telemedicine_hospital_it_policy_label_without_hospital_clinic_order_usage_revenue_margin_bridge","residual_error":"telemedicine_policy_label_can_fail_when_policy_access_does_not_convert_to_platform_order_and_cashflow","shadow_rule_candidate":"route_telemedicine_hospital_it_label_to_hard_4c_if_mfe_moderate_mae_severe_and_order_revenue_bridge_missing"}
{"row_type":"case","case_id":"C31_R11L99_099750_2024_02_01","scheduled_round":"R11","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"099750","name":"이지케어텍","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":17740,"peak_high":23250,"peak_date":"2024-02-19","worst_low_after_entry":12940,"worst_low_after_entry_date":"2024-08-05","mfe_pct":31.1,"mae_pct":-27.1,"classification":"local_positive_emr_hospital_platform_telemedicine_policy_mfe_with_watch_4b_cap","calibration_usable":true,"short_listing_or_future_corporate_action_caveat":true,"evidence_family":"emr_hospital_platform_digital_health_policy_label_without_sustained_hospital_order_implementation_renewal_margin_bridge","residual_error":"emr_hospital_platform_policy_label_can_create_mfe_but_needs_4b_when_order_implementation_and_margin_evidence_stale","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_emr_telemedicine_policy_cases_as_watch_4b_not_green"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"TELEMEDICINE_DIGITAL_HEALTH_MEDICAL_ACCESS_POLICY_PLATFORM_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_VS_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"telemedicine_policy_case_count":3,"digital_health_platform_case_count":2,"emr_hospital_platform_case_count":1,"pharmacy_clinic_platform_case_count":1,"policy_to_order_revenue_bridge_missing_count":2,"platform_adoption_retention_margin_bridge_missing_count":2,"financing_or_smallcap_event_beta_caveat_count":2,"event_window_separation_required_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"direct_2024_corporate_action_rejected_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":99,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_TELEMEDICINE_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 telemedicine/digital-health/medical-access policy cases, do not open Stage2-Actionable or Stage3-Green from telemedicine policy, digital health, hospital IT, EMR, clinic platform, pharmacy platform, temporary non-face-to-face treatment policy rumor, public reimbursement, insurer integration, remote-care infrastructure, one-day healthcare IT policy volume spike, or later policy-like rebound labels alone. Require named policy/rule/payer/region/institution/adoption schedule, hospital/clinic/pharmacy/patient adoption path, platform traffic and paid conversion, order visibility, renewal, retention and usage data, EMR/prescription/payment/claims workflow integration, public procurement vs insurer vs enterprise hospital vs clinic vs B2C channel split, compliance/security/support/cloud/labor/sales cost control, revenue recognition and cash collection, gross-margin/OP conversion, event-window separation after failed first trigger, and post-trigger price survival. Clinic/pharmacy platform positives with large MFE may be capped Actionable when adoption/order/revenue/margin bridge is explicit, but Green requires fresh evidence. Telemedicine/hospital IT labels with moderate MFE and severe MAE should route to hard-4C when policy-to-order bridge is missing. EMR/hospital-platform labels with meaningful MFE followed by material MAE should remain Watch/4B unless hospital order and implementation evidence refreshes. Rows with direct 2024 corporate-action candidates should be rejected from clean primary calibration unless adjusted-price review is available.","expected_effect":"Preserve true telemedicine/digital-health policy positives while reducing generic healthcare IT, remote-care, EMR, clinic/pharmacy platform, reimbursement, and policy-access false positives where adoption, order, usage, renewal, revenue recognition, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"rejected_candidate","scheduled_round":"R11","scheduled_loop":99,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"033230","name":"인성정보","reason":"Telemedicine/remote-care infrastructure candidate checked, but profile has 2024-07-12 corporate-action candidate inside the first-half validation path. Do not use as clean primary calibration row without adjusted-price review.","do_not_count_as_global_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":99,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"telemedicine_policy_adoption_order_revenue_margin_guard","contribution":"Adds one clinic/pharmacy platform telemedicine-policy positive, one telemedicine/hospital IT hard-4C counterexample, and one EMR/hospital-platform Watch/4B cap to calibrate C31 policy-to-adoption, order visibility, platform usage, renewal, compliance/support cost, revenue recognition, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_TELEMEDICINE_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [telemedicine, digital_health, medical_access, emr, hospital_it, clinic_platform, pharmacy_platform]:

  Do not open Stage3-Green from:
    - telemedicine policy label alone
    - digital health / medical access headline alone
    - hospital IT / EMR / clinic platform label alone
    - pharmacy / clinic network readthrough alone
    - temporary non-face-to-face treatment policy rumor alone
    - public reimbursement or insurer integration story alone
    - remote-care infrastructure label alone
    - one-day healthcare IT policy volume spike alone

  Require at least two of:
    - named policy / rule / payer / region / institution / adoption schedule
    - hospital / clinic / pharmacy / patient adoption path
    - platform traffic and paid conversion
    - order visibility / renewal / retention / usage data
    - EMR / prescription / payment / claims workflow integration
    - public procurement / insurer / enterprise hospital / clinic / B2C channel split
    - compliance / security / support / cloud / labor / sales cost control
    - revenue recognition and cash collection
    - gross margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the telemedicine-policy headline

  If MFE < 20% and MAE <= -40%:
    route to C31 hard-4C candidate.

  If MFE > 30% but adoption/order/revenue evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but later MAE is material:
    attach Watch/4B until hospital or platform order evidence refreshes.

  If later policy-like rebounds appear after first-phase failure:
    create a new event window; do not retroactively validate the failed first trigger.

  If direct 2024 corporate-action caveat appears:
    reject from clean primary calibration unless adjusted-price review is available.

  Distinguish:
    - companies where policy becomes adoption, platform usage, orders, renewal, revenue, and OP
    - from labels where telemedicine access opens but platform monetization and cash conversion fail.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 telemedicine / digital-health policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_TELEMEDICINE_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Do not ingest rejected_candidate rows as primary calibration cases.
8. If enough C31 telemedicine cases agree, consider implementing a canonical guard that:
   - blocks telemedicine/digital-health Green without named policy/payer/institution, adoption, platform usage, order, renewal, revenue, and margin bridge,
   - preserves clinic/pharmacy platform positives only with price survival and fresh adoption/order evidence,
   - routes moderate-MFE/severe-MAE telemedicine hospital IT labels to hard-4C,
   - treats meaningful-MFE/material-MAE EMR/hospital-platform labels as Watch/4B,
   - separates later policy rebound windows from earlier failed triggers,
   - rejects direct 2024 corporate-action contaminated rows unless adjusted-price review exists.

Expected next schedule:
completed_round = R11
completed_loop = 99
next_round = R12
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 99
next_round = R12
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
