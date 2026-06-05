# E2R Stock-Web v12 Residual Research — R11 / Loop 98

```yaml
scheduled_round: R11
scheduled_loop: 98
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE

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
hard_4c_secondary_guard_count: 1
digital_textbook_policy_case_count: 3
edtech_platform_case_count: 2
textbook_curriculum_case_count: 2
public_education_budget_case_count: 3
policy_to_order_revenue_bridge_missing_count: 2
platform_retention_margin_bridge_missing_count: 2
late_event_window_separation_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
name_history_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 98
next_round: R12
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_98_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 98
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use the L10 policy / event / miscellaneous branch. This run uses:

```text
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Selected fine branch:

```text
digital textbook / edtech / public education curriculum policy
public budget, school adoption, textbook or platform order visibility,
teacher/student usage, renewal and retention, content production cost,
platform operation cost, revenue recognition, and margin bridge
vs generic education-policy label spike
```

This deliberately avoids:
- C31 top-covered names:
  `013990`, `003550`, `015760`, `032350`, `114090`, `000270`
- R11 loop97 environmental-policy branch:
  `029960`, `067900`, `009440`
- R12 loop96 low-birthrate / baby-product policy branch:
  `407400`, `159580`, `014100`
- R12 loop95 carbon / CCUS branch:
  `083420`, `448280`, `119650`
- R11 loop95 tourism branch:
  `034230`, `950170`, `008770`
- R12 loop94 education branch:
  `096240`, `072870`, `095720`

Selected symbols:

```text
100220 비상교육
053290 NE능률
057030 YBM넷
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
100220: same archetype, new symbol, education/digital textbook policy positive with 4B/Green cap after large MFE and later drawdown.
053290: same archetype, new symbol, textbook/curriculum policy label hard-4C candidate after initial policy spike failed revenue/margin survival.
057030: same archetype, new symbol, edtech/online education local 4B failure with hard-4C secondary guard and later event-window separation.
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
100220 비상교육
  profile: atlas/symbol_profiles/100/100220.json
  name history:
    비유와상징 -> 비상교육
  first_date: 2008-06-30
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,353
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2011-04-18
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside selected 2024 validation window.

053290 NE능률
  profile: atlas/symbol_profiles/053/053290.json
  name history:
    능률영어사 -> 능률교육 -> NE능률
  first_date: 2002-12-10
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,723
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2007-10-19, 2007-10-31, 2009-07-17
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity candidates are outside selected 2024 validation window.

057030 YBM넷
  profile: atlas/symbol_profiles/057/057030.json
  name history:
    시사닷컴 -> YBM시사닷컴 -> 와이비엠넷 -> YBM넷
  first_date: 2004-06-08
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,360
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2005-04-21, 2010-01-25
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity candidates are outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C31 is a policy / subsidy / legislation / event archetype. In this fine branch, the event is digital textbook, edtech, curriculum, and public education policy. It is not a generic "education stock" or "policy theme" archetype.

The model can over-score:

```text
digital textbook policy label
AI education / edtech headline
public education budget headline
curriculum revision story
online education / LMS / testing platform label
private education stock sympathy
one-day education-policy volume spike
later policy-event spike after a failed first trigger
```

The C31 bridge must be stricter:

```text
education / digital-textbook policy event
  -> named policy, grade, subject, budget, or adoption schedule
  -> school / teacher / student adoption path
  -> textbook, content, platform, or service order visibility
  -> paid conversion, renewal, retention, and usage data
  -> public procurement, private academy, or B2C channel split
  -> content production, teacher support, cloud/platform, and sales cost
  -> revenue recognition and cash collection
  -> gross margin / OP conversion
  -> event-window separation after a failed first trigger
  -> price survival after the first education-policy spike
```

A C31 digital-textbook thesis is like a textbook placed on a classroom desk. The policy headline prints the cover, but equity value appears only when schools adopt it, teachers use it, students stay on the platform, budgets become orders, renewal follows usage, and content/cloud/support cost still leaves margin.

---

## 5. Case 1 — 100220 비상교육

```yaml
case_id: C31_R11L98_100220_2024_02_01
symbol: "100220"
name: "비상교육"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5210
classification: positive_digital_textbook_public_education_policy_revenue_bridge_with_4b_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

비상교육 is the constructive education-policy control in this set.

The useful C31 read is not simply:

```text
교육정책 / 디지털교과서 테마가 강하다
```

It is:

```text
education publisher / digital textbook relevance
  -> curriculum and public education policy readthrough
  -> textbook / platform order and adoption optionality
  -> strong February price confirmation
  -> later 4B / Green cap because order, usage, renewal, and margin evidence must refresh
```

The forward path produced a large MFE in February, validating policy salience. But the later drawdown into August shows why C31 education-policy Green cannot stay open from policy label alone.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,330 / low 5,100 / close 5,210
2024-02-06: high 6,450 / close 5,060
2024-02-20: high 7,000 / close 7,000
2024-02-21: high 8,420 / close 7,360
2024-08-05: low 3,990 / close 4,125
2024-08-19: high 5,340 / close 5,120
2024-11-05: high 7,600 / close 7,100
```

Approximate path from entry close:

```text
entry_close: 5,210
peak_high_first_major_window: 8,420
MFE: +61.6%
worst_low_after_entry: 3,990
MAE: -23.4%
```

### Interpretation

This is a C31 positive with 4B / Green cap:

```text
Stage2-Actionable: possible if policy adoption, grade/subject scope, order visibility, platform usage, and margin bridge are explicit.
Stage3-Green: blocked after +60% MFE unless fresh adoption, renewal, revenue, and margin evidence appears.
Local 4B: required if price outruns order/revenue evidence.
Hard 4C: no, because large MFE came first and MAE did not cross the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  digital_textbook_policy_relevance: high
  curriculum_budget_bridge: medium_high
  school_adoption_order_bridge: medium
  platform_usage_retention_bridge: weak_to_medium
  revenue_margin_bridge: medium
  price_confirmation: very_high
  later_drawdown_penalty: material
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 053290 NE능률

```yaml
case_id: C31_R11L98_053290_2024_02_01
symbol: "053290"
name: "NE능률"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 5360
classification: hard_4c_candidate_textbook_curriculum_policy_label_without_order_revenue_margin_survival
calibration_usable: true
```

### Evidence interpretation

NE능률 is the hard education-policy guardrail.

The label can fool the model:

```text
textbook / curriculum / English education
  -> digital textbook and education-policy readthrough
  -> curriculum reform or public education theme
  -> one-day policy-stock volume spike
```

The February policy spike produced only a modest MFE before a severe drawdown. Later August/September education-policy spikes must be treated as new event windows, not a rescue of the February trigger. The bridge from policy label to orders, platform adoption, renewal, retention, and margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 5,480 / low 5,250 / close 5,360
2024-02-06: high 6,300 / low 5,240 / close 5,240
2024-02-20: high 5,990 / close 5,790
2024-03-22: low 4,530 / close 4,725
2024-08-05: low 2,745 / close 2,880
2024-08-20: high 4,835 / close 4,270
2024-08-28: high 5,200 / close 4,345
```

Approximate path from entry close:

```text
entry_close: 5,360
peak_high_first_phase: 6,300
MFE: +17.5%
worst_low_after_entry: 2,745
MAE: -48.8%
```

### Interpretation

This is a hard C31 false-positive candidate:

```text
Stage2-Watch: possible from textbook/curriculum and education-policy relevance.
Stage2-Actionable: blocked unless school adoption, order, usage, renewal, and revenue/margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and severe MAE.
Event-window separation: yes; August education-policy spikes are new windows, not validation of the February trigger.
```

The lesson is that education-policy salience is not textbook/platform revenue survival.

### Stress-test components

```text
raw_component_score_proxy:
  textbook_curriculum_policy_label: high
  digital_textbook_readthrough: medium_high
  order_visibility_bridge: weak
  adoption_usage_bridge: weak
  renewal_retention_bridge: weak
  margin_op_bridge: weak
  price_confirmation_after_entry: modest
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 057030 YBM넷

```yaml
case_id: C31_R11L98_057030_2024_02_01
symbol: "057030"
name: "YBM넷"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4580
classification: local_burst_edtech_online_education_policy_label_high_mae_4b_failure_with_hard_4c_secondary_guard
calibration_usable: true
```

### Evidence interpretation

YBM넷 is the edtech / online-education local-burst failure.

The setup had real C31 relevance:

```text
online education / language learning platform
  -> digital textbook and edtech-policy readthrough
  -> platform usage and school/learner adoption optionality
  -> February and April event spikes
```

The stock produced meaningful MFE, but later failed price survival into August. This is not a pure zero-response failure; it is a local 4B failure. However, because the drawdown crossed the hard zone, later stale or late entries should be routed to hard 4C quickly unless adoption and margin evidence is renewed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,680 / low 4,500 / close 4,580
2024-02-20: high 4,920 / close 4,870
2024-02-29: high 5,580 / close 4,905
2024-04-11: high 4,800 / close 4,030
2024-04-16: high 4,950 / close 4,100
2024-08-05: low 2,960 / close 3,100
2024-09-24: high 4,370 / close 4,135
```

Approximate path from entry close:

```text
entry_close: 4,580
peak_high: 5,580
MFE: +21.8%
worst_low_after_entry: 2,960
MAE: -35.4%
```

### Interpretation

This is a C31 local burst / high-MAE 4B failure:

```text
Stage2-Watch: valid from edtech / online education and education-policy relevance.
Stage2-Actionable: possible only if platform adoption, paid conversion, renewal, and margin bridge are explicit.
Stage3-Green: blocked after hard-zone MAE.
Local 4B: required because meaningful MFE came first.
Hard 4C secondary guard: yes for stale or late entries after the first event window fails.
Event-window separation: yes; September spike should be treated as a new window.
```

### Stress-test components

```text
raw_component_score_proxy:
  edtech_online_platform_relevance: high
  public_policy_signal: medium_high
  adoption_usage_bridge: weak_to_medium
  paid_conversion_renewal_bridge: weak
  platform_cost_margin_bridge: weak
  price_confirmation: meaningful_initial
  drawdown_penalty: high
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
hard_4c_secondary_guard_count: 1
digital_textbook_policy_case_count: 3
edtech_platform_case_count: 2
textbook_curriculum_case_count: 2
public_education_budget_case_count: 3
policy_to_order_revenue_bridge_missing_count: 2
platform_retention_margin_bridge_missing_count: 2
late_event_window_separation_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
name_history_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C31 education-policy grid:

```text
100220 비상교육:
  digital textbook / public education policy positive;
  large MFE and material MAE, 4B/Green cap required after policy rerating.

053290 NE능률:
  textbook/curriculum policy label failed;
  modest MFE and severe MAE, hard 4C candidate.

057030 YBM넷:
  edtech/online education local burst;
  meaningful MFE first, then hard-zone MAE, local 4B with hard-4C secondary guard.
```

Shared rule:

```text
C31 education policy is not "digital textbook or edtech label is hot."
C31 education policy is "policy budget becomes school adoption, adoption becomes orders and usage, usage becomes renewal, and content/platform/support cost still leaves OP margin."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L98_100220_2024_02_01","scheduled_round":"R11","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"100220","name":"비상교육","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5210,"peak_high":8420,"peak_date":"2024-02-21","worst_low_after_entry":3990,"worst_low_after_entry_date":"2024-08-05","mfe_pct":61.6,"mae_pct":-23.4,"classification":"positive_digital_textbook_public_education_policy_revenue_bridge_with_4b_green_cap_after_large_mfe","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"digital_textbook_public_education_policy_curriculum_adoption_order_platform_usage_revenue_margin_bridge","residual_error":"digital_textbook_policy_positive_requires_4b_green_cap_when_policy_rerating_outpaces_adoption_order_revenue_margin_evidence","shadow_rule_candidate":"preserve_education_policy_positive_but_cap_green_after_large_mfe_without_fresh_school_adoption_order_and_margin_evidence"}
{"row_type":"case","case_id":"C31_R11L98_053290_2024_02_01","scheduled_round":"R11","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"053290","name":"NE능률","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":5360,"peak_high_first_phase":6300,"peak_date":"2024-02-06","worst_low_after_entry":2745,"worst_low_after_entry_date":"2024-08-05","mfe_pct":17.5,"mae_pct":-48.8,"classification":"hard_4c_candidate_textbook_curriculum_policy_label_without_order_revenue_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"textbook_curriculum_education_policy_label_without_school_adoption_order_usage_renewal_revenue_margin_bridge","residual_error":"education_policy_label_can_fail_when_policy_does_not_convert_to_order_revenue_margin_survival","shadow_rule_candidate":"route_textbook_curriculum_policy_label_to_hard_4c_if_mfe_modest_mae_severe_and_order_revenue_bridge_missing"}
{"row_type":"case","case_id":"C31_R11L98_057030_2024_02_01","scheduled_round":"R11","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","symbol":"057030","name":"YBM넷","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4580,"peak_high":5580,"peak_date":"2024-02-29","worst_low_after_entry":2960,"worst_low_after_entry_date":"2024-08-05","mfe_pct":21.8,"mae_pct":-35.4,"classification":"local_burst_edtech_online_education_policy_label_high_mae_4b_failure_with_hard_4c_secondary_guard","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"event_window_separation_required":true,"evidence_family":"edtech_online_education_policy_platform_label_without_adoption_paid_conversion_renewal_platform_cost_margin_bridge","residual_error":"edtech_policy_label_can_create_mfe_but_fail_green_without_platform_usage_retention_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_hard_zone_mae_edtech_policy_cases_as_local_4b_with_hard_4c_secondary_guard"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"DIGITAL_TEXTBOOK_EDTECH_PUBLIC_EDUCATION_CURRICULUM_PLATFORM_REVENUE_MARGIN_BRIDGE_VS_EDUCATION_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"hard_4c_secondary_guard_count":1,"digital_textbook_policy_case_count":3,"edtech_platform_case_count":2,"textbook_curriculum_case_count":2,"public_education_budget_case_count":3,"policy_to_order_revenue_bridge_missing_count":2,"platform_retention_margin_bridge_missing_count":2,"late_event_window_separation_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"name_history_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":98,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_EDUCATION_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 digital-textbook/edtech/public-education policy cases, do not open Stage2-Actionable or Stage3-Green from digital textbook policy, AI education, edtech headline, public education budget, curriculum revision, online education/LMS/testing platform, private education sympathy, or one-day education-policy volume-spike labels alone. Require named policy/grade/subject/budget/adoption schedule, school/teacher/student adoption path, textbook/content/platform/service order visibility, paid conversion/renewal/retention/usage data, public procurement vs private academy vs B2C channel split, content production/teacher support/cloud/platform/sales cost control, revenue recognition and cash collection, gross-margin/OP conversion, event-window separation after failed first trigger, and post-trigger price survival. Education-policy positives with large MFE may be capped Actionable when adoption/order/revenue/margin bridge is explicit, but Green requires fresh evidence. Textbook/curriculum labels with modest MFE and severe MAE should route to hard-4C when policy-to-order bridge is missing. Edtech/online-education labels with meaningful MFE followed by hard-zone MAE should remain local 4B and receive hard-4C secondary guard for stale or late entries.","expected_effect":"Preserve true digital-textbook/education-policy positives while reducing education-policy, edtech, textbook, curriculum, and online-learning false positives where adoption, order, usage, renewal, revenue recognition, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":98,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"education_policy_adoption_order_revenue_margin_guard","contribution":"Adds one digital-textbook education-policy positive, one textbook/curriculum hard-4C candidate, and one edtech local 4B failure to calibrate C31 school adoption, order visibility, usage, renewal, public procurement, content/platform cost, revenue recognition, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_EDUCATION_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [digital_textbook, edtech, ai_education, curriculum_revision, public_education_budget]:

  Do not open Stage3-Green from:
    - digital textbook policy label alone
    - AI education / edtech headline alone
    - public education budget headline alone
    - curriculum revision story alone
    - online education / LMS / testing platform label alone
    - private education stock sympathy alone
    - one-day education-policy volume spike alone

  Require at least two of:
    - named policy / grade / subject / budget / adoption schedule
    - school / teacher / student adoption path
    - textbook / content / platform / service order visibility
    - paid conversion / renewal / retention / usage data
    - public procurement / private academy / B2C channel split
    - content production / teacher support / cloud / platform / sales cost control
    - revenue recognition and cash collection
    - gross margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the education-policy headline

  If MFE < 20% and MAE <= -40%:
    route to C31 hard-4C candidate.

  If MFE > 25% but adoption/order/revenue evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but later MAE enters hard zone:
    attach local 4B and hard-4C secondary guard for stale or late entries.

  If later policy-like spikes appear after first-phase failure:
    create a new event window; do not retroactively validate the failed first trigger.

  Distinguish:
    - companies where policy becomes adoption, orders, usage, renewal, revenue, and OP
    - from education labels where adoption, procurement, platform cost, or weak retention breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 education-policy / digital-textbook / edtech cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_EDUCATION_POLICY_ADOPTION_ORDER_REVENUE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 education-policy cases agree, consider implementing a canonical guard that:
   - blocks education-policy Green without named policy/budget/adoption schedule, school adoption, order, usage, renewal, revenue, and margin bridge,
   - preserves digital-textbook positives only with price survival and fresh adoption/order evidence,
   - routes modest-MFE/severe-MAE textbook/curriculum labels to hard-4C,
   - treats meaningful-MFE/hard-zone-MAE edtech labels as local 4B with hard-4C secondary guard,
   - separates later policy event windows from earlier failed triggers,
   - applies name-history, row-presence, and old corporate-action caveats when needed.

Expected next schedule:
completed_round = R11
completed_loop = 98
next_round = R12
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 98
next_round = R12
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
