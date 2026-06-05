# E2R Stock-Web v12 Residual Research — R12 / Loop 92

```yaml
scheduled_round: R12
scheduled_loop: 92
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE

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
hard_4c_candidate_count: 2
education_policy_theme_case_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 92
next_round: R13
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 92
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy/event or relevant under-covered service/agri sector. This run uses a service-sector policy branch:

```text
medical-school quota expansion policy
  -> education / admissions service names
  -> enrollment, course conversion, and revenue bridge
```

This is distinct from:
- R12 loop91 China visa-free travel-service policy,
- R11 loop92 public tender / delisting control-premium cap,
- R11 loop91 AI semiconductor policy.

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

Selected symbols:

```text
133750 메가엠디
053290 NE능률
215200 메가스터디교육
```

They avoid the C31 top-covered symbols and avoid the recent R11/R12 policy names:

```text
R11 loop91 avoid: 000660, 005930, 000990
R12 loop91 avoid: 039130, 080160, 094850
R11 loop92 avoid: 003410, 115390, 119860
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
133750: same archetype, new symbol, medical-admissions education policy local-positive / 4B failure branch
053290: same archetype, new symbol, education-theme policy spike without enrollment-revenue bridge
215200: same archetype, new symbol, large education platform brand without direct medical-quota revenue bridge
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
133750 메가엠디
  profile: atlas/symbol_profiles/133/133750.json
  first_date: 2015-12-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,493
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

053290 NE능률
  profile: atlas/symbol_profiles/053/053290.json
  first_date: 2002-12-10
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,723
  corporate_action_candidate_dates:
    2007-10-19, 2007-10-31, 2009-07-17
  2024 entry~D+180 contamination: none

215200 메가스터디교육
  profile: atlas/symbol_profiles/215/215200.json
  first_date: 2015-05-04
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 2,642
  corporate_action_candidate_dates:
    2018-08-29
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-02-06
South Korea medical-school quota expansion policy:
  government plan to add about 2,000 medical-school admissions from 2025,
  raising the policy salience of medical-admissions and education-service names.
```

This is a C31 service-policy branch.

The model can over-score:

```text
medical-school quota policy
medical admissions
education service label
online education platform
exam-prep brand
one-day policy spike
```

The correct C31 bridge is narrower:

```text
policy quota increase
  -> addressable student pool
  -> course enrollment / conversion
  -> pricing and renewal
  -> content or instructor capacity
  -> marketing cost
  -> revenue / margin conversion
  -> price survival after the first policy spike
```

An education-policy headline opens a classroom door. The stock-level question is whether students actually enroll, pay, stay, and leave margin after marketing and instructor costs.

---

## 5. Case 1 — 133750 메가엠디

```yaml
case_id: C31_R12L92_133750_2024_02_06
symbol: "133750"
name: "메가엠디"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE
trigger_date: 2024-02-06
entry_date: 2024-02-06
entry_price_basis: close
entry_price: 2995
classification: local_positive_medical_admission_policy_burst_with_4b_failure
calibration_usable: true
```

### Evidence interpretation

메가엠디 is the most direct education-policy theme case. The company label is closest to medical / professional admissions demand.

The useful bridge is:

```text
medical-school quota policy
  -> professional admissions demand
  -> course sign-ups / online content conversion
  -> repeat enrollment or package sales
  -> margin conversion
```

The price path did produce tradable MFE after the initial policy event. However, the later drawdown was large enough to show that the event remained a local policy burst rather than a durable Stage3-Green thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-06: high 3,670 / close 2,995
2024-02-19: high 3,280 / close 3,135
2024-02-20: high 3,450 / close 3,325
2024-03-05: high 3,555 / close 3,240
2024-08-05: low 1,647 / close 1,740
2024-08-19: high 2,705 / close 2,500
2024-10-22: low 2,000 / close 2,005
```

Approximate path from entry close:

```text
entry_close: 2,995
peak_high_after_entry_window: 3,555
MFE: +18.7%
worst_low: 1,647
MAE: -45.0%
```

### Interpretation

This is a local-positive / 4B failure case:

```text
Stage2-Watch: valid from direct medical-admissions relevance.
Stage2-Actionable: possible only as event-trading unless enrollment/revenue bridge is explicit.
Stage3-Green: blocked.
Local 4B: required after local MFE and later high MAE.
Hard 4C: not for initial event-trading entry, but re-entry without enrollment evidence would be 4C.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  direct_medical_admissions_relevance: high
  enrollment_conversion_bridge: weak_to_medium
  revenue_margin_bridge: weak
  local_price_confirmation: medium
  post_event_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 053290 NE능률

```yaml
case_id: C31_R12L92_053290_2024_02_06
symbol: "053290"
name: "NE능률"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE
trigger_date: 2024-02-06
entry_date: 2024-02-06
entry_price_basis: close
entry_price: 5240
classification: hard_4c_candidate_education_policy_theme_without_direct_enrollment_bridge
calibration_usable: true
```

### Evidence interpretation

NE능률 is the broad education-theme false-positive.

The model risk is:

```text
education stock
  -> medical-school quota policy
  -> one-day policy volume
  -> no direct medical-admissions revenue bridge
  -> large drawdown
```

The company has real education-content relevance, but that is not enough for C31. The bridge needs direct enrollment conversion and revenue/margin visibility.

### Price path

Key Stock-Web rows:

```text
2024-02-06: high 6,300 / close 5,240
2024-02-20: high 5,990 / close 5,790
2024-02-29: high 6,000 / close 5,700
2024-03-22: low 4,530 / close 4,725
2024-08-05: low 2,745 / close 2,880
2024-08-19: high 4,540 / close 4,380
2024-08-28: high 5,200 / close 4,345
```

Approximate path from entry close:

```text
entry_close: 5,240
peak_high_after_entry_window: 6,000
MFE: +14.5%
worst_low: 2,745
MAE: -47.6%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: possible from broad education-policy relevance.
Stage2-Actionable: blocked unless direct enrollment/revenue bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that education label is not education-policy monetization.

### Stress-test components

```text
raw_component_score_proxy:
  broad_education_label: high
  direct_medical_admission_bridge: weak
  enrollment_conversion_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 215200 메가스터디교육

```yaml
case_id: C31_R12L92_215200_2024_02_06
symbol: "215200"
name: "메가스터디교육"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE
trigger_date: 2024-02-06
entry_date: 2024-02-06
entry_price_basis: close
entry_price: 63100
classification: hard_4c_candidate_large_education_platform_without_direct_medical_quota_revenue_bridge
calibration_usable: true
```

### Evidence interpretation

메가스터디교육 is the large-platform guardrail case.

The company is a real and high-quality education platform. That is exactly why the guardrail matters. C31 should not promote quality brand relevance into a medical-school quota Green unless the policy creates a direct revenue bridge.

The forward path shows that:

```text
large education brand
  -> policy relevance
  -> shallow initial MFE
  -> later drawdown
```

did not become a durable policy-recipient rerating.

### Price path

Key Stock-Web rows:

```text
2024-02-06: high 65,200 / close 63,100
2024-02-08: high 68,900 / close 67,800
2024-02-20: high 66,900 / close 65,200
2024-04-18: high 64,600 / close 63,300
2024-08-05: low 46,500 / close 46,650
2024-09-10: low 45,400 / close 45,400
2024-10-22: low 42,300 / close 42,300
```

Approximate path from entry close:

```text
entry_close: 63,100
peak_high: 68,900
MFE: +9.2%
worst_low: 42,300
MAE: -33.0%
```

### Interpretation

This is a hard C31 guardrail case:

```text
Stage2-Watch: valid from education-platform relevance.
Stage2-Actionable: blocked without direct medical-quota enrollment and revenue bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that even high-quality education platforms need company-specific policy monetization.

### Stress-test components

```text
raw_component_score_proxy:
  education_platform_quality: high
  medical_quota_policy_relevance: medium
  direct_enrollment_bridge: weak
  margin_conversion_visibility: weak
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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 2
education_policy_theme_case_count: 3
calibration_usable_trigger_count: 3
```

The three-case C31 education-policy grid:

```text
133750 메가엠디:
  most direct medical-admissions policy exposure;
  local positive, but later high-MAE 4B failure without enrollment/revenue confirmation.

053290 NE능률:
  broad education-policy label failed.
  Shallow MFE and high MAE, hard 4C.

215200 메가스터디교육:
  large education platform quality did not convert to medical-quota Green.
  Shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C31 education policy is not "quota policy = all education stocks Green."
C31 education policy is "policy change becomes paid enrollment, recurring course demand, pricing power, and margin conversion for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L92_133750_2024_02_06","scheduled_round":"R12","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE","symbol":"133750","name":"메가엠디","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":2995,"peak_high":3555,"peak_date":"2024-03-05","worst_low":1647,"worst_low_date":"2024-08-05","mfe_pct":18.7,"mae_pct":-45.0,"classification":"local_positive_medical_admission_policy_burst_with_4b_failure","calibration_usable":true,"evidence_family":"medical_admissions_policy_theme_without_confirmed_enrollment_revenue_margin_bridge","residual_error":"direct_policy_theme_can_generate_local_mfe_but_fail_green_without_paid_enrollment_conversion","shadow_rule_candidate":"preserve_event_burst_as_local_4b_not_green_when_enrollment_revenue_bridge_missing"}
{"row_type":"case","case_id":"C31_R12L92_053290_2024_02_06","scheduled_round":"R12","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE","symbol":"053290","name":"NE능률","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":5240,"peak_high":6000,"peak_date":"2024-02-29","worst_low":2745,"worst_low_date":"2024-08-05","mfe_pct":14.5,"mae_pct":-47.6,"classification":"hard_4c_candidate_education_policy_theme_without_direct_enrollment_bridge","calibration_usable":true,"evidence_family":"broad_education_policy_theme_without_medical_admission_enrollment_bridge","residual_error":"education_label_can_overpromote_to_green_without_company_specific_policy_monetization","shadow_rule_candidate":"route_broad_education_policy_theme_to_hard_4c_if_mfe_shallow_mae_large"}
{"row_type":"case","case_id":"C31_R12L92_215200_2024_02_06","scheduled_round":"R12","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE","symbol":"215200","name":"메가스터디교육","trigger_date":"2024-02-06","entry_date":"2024-02-06","entry_price":63100,"peak_high":68900,"peak_date":"2024-02-08","worst_low":42300,"worst_low_date":"2024-10-22","mfe_pct":9.2,"mae_pct":-33.0,"classification":"hard_4c_candidate_large_education_platform_without_direct_medical_quota_revenue_bridge","calibration_usable":true,"evidence_family":"large_education_platform_quality_without_direct_medical_quota_revenue_bridge","residual_error":"quality_education_platform_can_fail_policy_green_without_direct_enrollment_revenue_conversion","shadow_rule_candidate":"block_green_for_large_education_platforms_when_policy_relevance_is_indirect_and_price_survival_fails"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"education_policy_theme_case_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":92,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_EDUCATION_POLICY_ENROLLMENT_REVENUE_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 education-policy events, do not open Stage2-Actionable or Stage3-Green from medical-school quota policy, education label, exam-prep label, online education platform, or one-day policy spike alone. Require company-specific paid enrollment conversion, course/package demand, recurring or repeat purchase, pricing power, marketing-cost containment, margin/OP conversion, and post-trigger price survival. Direct admissions-policy names with local MFE but high MAE should remain local 4B/event burst unless enrollment revenue evidence appears. Broad education names or large education platforms with shallow MFE and high MAE should route to hard-4C when policy monetization is indirect.","expected_effect":"Reduce education-policy theme false positives while preserving only directly monetizable admissions-policy positives with enrollment and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":92,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"education_policy_enrollment_revenue_guard","contribution":"Adds one medical-admissions local-positive/4B failure and two education-policy hard-4C counterexamples to calibrate C31 education-service policy monetization requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_EDUCATION_POLICY_ENROLLMENT_REVENUE_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [medical_school_quota, education_policy, admissions_policy]:

  Do not open Stage3-Green from:
    - medical-school quota headline alone
    - education stock label alone
    - exam-prep / online-education label alone
    - one-day policy-volume spike alone
    - broad professional-admissions sympathy alone

  Require at least two of:
    - company-specific paid enrollment conversion
    - course / package demand
    - repeat purchase or recurring enrollment
    - pricing power
    - marketing-cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the policy headline

  If MFE < 15% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE > 15% but MAE < -40%:
    classify as local 4B / policy burst, not Green, unless enrollment-revenue bridge is confirmed.

  Distinguish:
    - direct medical-admissions names with actual enrollment conversion
    - from broad education labels and large platforms where policy relevance is indirect.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 education-policy / medical-school quota cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_EDUCATION_POLICY_ENROLLMENT_REVENUE_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 education-policy cases agree, consider implementing a canonical guard that:
   - blocks quota-policy Green without paid enrollment, course demand, pricing, and margin bridge,
   - keeps direct admissions-policy local MFE names as 4B unless revenue evidence appears,
   - routes broad education labels with shallow-MFE/high-MAE to hard-4C,
   - distinguishes direct admissions monetization from indirect platform quality.

Expected next schedule:
completed_round = R12
completed_loop = 92
next_round = R13
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 92
next_round = R13
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
