# E2R Stock-Web v12 Residual Research — R12 / Loop 94

```yaml
scheduled_round: R12
scheduled_loop: 94
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE

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
education_policy_service_case_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 94
next_round: R13
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 94
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy/event or relevant under-covered service/policy branches. This run uses:

```text
education policy / private academy / content enrollment / recurring service demand
```

This is distinct from:
- R11 loop94 C32 governance / control-premium branch,
- R12 loop93 food-security / agri-input policy branch,
- R12 loop92 medical-school quota education-policy branch,
- R12 loop91 travel-service policy branch.

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
096240 크레버스
072870 메가스터디
095720 웅진씽크빅
```

They avoid the C31 top-covered symbols and avoid recent R11/R12 policy names:

```text
R11 loop94 avoid: 003920, 001750, 003240
R12 loop93 avoid: 008040, 054050, 002900
R12 loop92 avoid: 133750, 053290, 215200
R12 loop91 avoid: 039130, 080160, 094850
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
096240: same archetype, new symbol, premium education content / recurring enrollment positive with 4B watch
072870: same archetype, new symbol, stable education holding / enrollment label Watch cap without incremental monetization bridge
095720: same archetype, new symbol, edtech / children learning policy-label spike hard-4C without paid enrollment margin bridge
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
096240 크레버스
  profile: atlas/symbol_profiles/096/096240.json
  name history:
    씨디아이 until 2008-09-30
    청담러닝 until 2022-03-16
    크레버스 from 2022-03-17
  first_date: 2008-06-27
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 4,353
  corporate_action_candidate_dates:
    2022-03-17
  2024 entry~D+180 contamination: none

072870 메가스터디
  profile: atlas/symbol_profiles/072/072870.json
  first_date: 2004-12-21
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,198
  corporate_action_candidate_dates:
    2015-05-04, 2018-06-18, 2018-07-09
  2024 entry~D+180 contamination: none

095720 웅진씽크빅
  profile: atlas/symbol_profiles/095/095720.json
  first_date: 2007-05-31
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,603
  corporate_action_candidate_dates:
    2019-01-31, 2019-04-08
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024 education / private academy / edtech / childcare-learning policy salience
```

This is a C31 policy/service branch. The investment question is not simply:

```text
education policy is in the news
```

The C31 education question is:

```text
policy or exam-cycle salience
  -> company-specific paid enrollment
  -> content renewal / reorder
  -> ARPU / pricing / retention
  -> teacher and platform cost control
  -> margin / OP conversion
  -> price survival
```

The model can over-score:

```text
education policy headline
medical-school quota or exam-cycle label
private academy brand
edtech / children learning label
online content platform label
one-day education-theme volume spike
```

The bridge must be stricter:

```text
education-policy or exam-cycle event
  -> paid enrollment or renewal
  -> content / curriculum demand
  -> retention and ARPU
  -> offline/online channel economics
  -> marketing and teacher-cost containment
  -> margin / OP conversion
  -> post-trigger price survival
```

An education-policy headline is a school bell. It makes everyone look toward the classroom, but equity value comes only when students enroll, parents renew, content gets paid for, and the classroom earns margin after teacher and marketing costs.

---

## 5. Case 1 — 096240 크레버스

```yaml
case_id: C31_R12L94_096240_2024_02_01
symbol: "096240"
name: "크레버스"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 16550
classification: positive_capped_premium_education_content_recurring_enrollment_margin_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

크레버스 is the constructive control in this set.

The useful C31 education read is not simply:

```text
교육주 / 학원주가 움직였다
```

It is:

```text
premium education content and academy relevance
  -> recurring enrollment and curriculum demand
  -> pricing / ARPU and retention optionality
  -> local price confirmation
```

The forward path delivered meaningful MFE into March/April and did not cross a hard drawdown threshold. That makes it a capped positive. However, the later drawdown means the model should attach 4B after the initial rerating unless fresh enrollment and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 16,550
2024-02-16: high 17,950 / close 17,950
2024-03-28: high 19,010 / close 18,900
2024-04-18: high 19,450 / close 19,120
2024-08-05: low 15,510 / close 15,650
2024-09-09: low 14,720 / close 15,000
2024-10-25: high 15,800 / close 15,770
```

Approximate path from entry close:

```text
entry_close: 16,550
peak_high: 19,450
MFE: +17.5%
worst_low_after_entry: 14,720
MAE: -11.1%
```

### Interpretation

This is a capped positive with 4B watch:

```text
Stage2-Actionable: valid if paid enrollment, content renewal, and margin bridge are explicit.
Stage3-Green: blocked without refreshed retention / ARPU / OP evidence.
Local 4B: monitor after +15% MFE and later drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  education_policy_relevance: medium_high
  premium_content_enrollment_bridge: high
  retention_arpu_bridge: medium
  margin_op_bridge: medium
  price_confirmation: medium_high
  later_drawdown_penalty: medium
  local_4b_overlay: required_after_rerating
```

---

## 6. Case 2 — 072870 메가스터디

```yaml
case_id: C31_R12L94_072870_2024_02_01
symbol: "072870"
name: "메가스터디"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10990
classification: watch_cap_stable_education_holding_label_without_incremental_paid_enrollment_margin_bridge
calibration_usable: true
```

### Evidence interpretation

메가스터디 is the Watch/Yellow cap.

The label is relevant:

```text
education brand
exam-cycle / private academy relevance
education-policy visibility
```

But the forward path did not validate a strong incremental demand or margin bridge. The stock was stable, but MFE was shallow. A stable low-MAE path can still fail Actionable if it does not show paid enrollment growth, retention, ARPU, or margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 10,990 / close 10,990
2024-02-06: high 11,590 / close 11,380
2024-03-20: high 11,590 / close 11,540
2024-08-05: low 10,600 / close 10,860
2024-08-13: high 11,500 / close 11,440
2024-10-23: low 11,000 / close 11,030
```

Approximate path from entry close:

```text
entry_close: 10,990
peak_high: 11,590
MFE: +5.5%
worst_low_after_entry: 10,600
MAE: -3.5%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from education-brand relevance.
Stage2-Actionable: blocked unless incremental paid enrollment, renewal, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MAE was controlled.
```

The lesson is that a stable education brand is not automatically policy monetization.

### Stress-test components

```text
raw_component_score_proxy:
  education_brand_quality: high
  policy_exam_cycle_relevance: medium
  incremental_enrollment_bridge: weak
  arpu_retention_bridge: weak_to_medium
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: low
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 095720 웅진씽크빅

```yaml
case_id: C31_R12L94_095720_2024_02_21
symbol: "095720"
name: "웅진씽크빅"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 2525
classification: hard_4c_candidate_children_learning_edtech_policy_label_without_paid_enrollment_margin_bridge
calibration_usable: true
```

### Evidence interpretation

웅진씽크빅 is the hard guardrail case.

The setup had a plausible education-service story:

```text
children learning / edtech label
education policy salience
platform or content transformation hope
one-day volume spike
```

But the price path did not validate paid enrollment, renewal, platform monetization, or margin conversion. The MFE was shallow relative to the later downside, and the later drawdown crossed the hard-4C area.

### Price path

Key Stock-Web rows:

```text
2024-02-21: high 2,780 / close 2,525
2024-03-04: low 2,400 / close 2,415
2024-04-17: low 2,060 / close 2,080
2024-08-05: low 1,641 / close 1,708
2024-09-09: low 1,640 / close 1,700
2024-10-11: high 2,190 / close 2,040
```

Approximate path from entry close:

```text
entry_close: 2,525
peak_high: 2,780
MFE: +10.1%
worst_low_after_entry: 1,640
MAE: -35.0%
```

### Interpretation

This is a hard C31 education-policy false-positive:

```text
Stage2-Watch: possible from children-learning / edtech relevance.
Stage2-Actionable: blocked without paid enrollment, renewal, ARPU, and margin bridge.
Stage3-Green: blocked.
Hard 4C: yes by modest MFE and -35% MAE.
```

The lesson is that education-policy salience is not paid enrollment or margin.

### Stress-test components

```text
raw_component_score_proxy:
  children_learning_label: high
  edtech_policy_relevance: medium_high
  paid_enrollment_bridge: weak
  renewal_arpu_bridge: weak
  margin_op_bridge: weak
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
hard_4c_candidate_count: 1
education_policy_service_case_count: 3
calibration_usable_trigger_count: 3
```

The three-case C31 education-service grid:

```text
096240 크레버스:
  premium education content / recurring enrollment positive;
  useful MFE and non-hard MAE, but Green requires refreshed retention and margin bridge.

072870 메가스터디:
  stable education brand / holding label;
  controlled MAE but shallow MFE, Watch/Yellow cap.

095720 웅진씽크빅:
  children-learning / edtech label failed;
  modest MFE and high MAE, hard 4C.
```

Shared rule:

```text
C31 education policy is not "education stock is relevant."
C31 education policy is "policy or exam-cycle salience becomes paid enrollment, content renewal, ARPU, retention, and margin conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L94_096240_2024_02_01","scheduled_round":"R12","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE","symbol":"096240","name":"크레버스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":16550,"peak_high":19450,"peak_date":"2024-04-18","worst_low_after_entry":14720,"worst_low_after_entry_date":"2024-09-09","mfe_pct":17.5,"mae_pct":-11.1,"classification":"positive_capped_premium_education_content_recurring_enrollment_margin_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"premium_education_content_recurring_enrollment_retention_arpu_margin_bridge","residual_error":"positive_education_service_path_requires_4b_and_green_block_without_refreshed_enrollment_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_paid_enrollment_content_renewal_and_margin_bridge_confirm_but_attach_4b_after_rerating"}
{"row_type":"case","case_id":"C31_R12L94_072870_2024_02_01","scheduled_round":"R12","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE","symbol":"072870","name":"메가스터디","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10990,"peak_high":11590,"peak_date":"2024-02-06","worst_low_after_entry":10600,"worst_low_after_entry_date":"2024-08-05","mfe_pct":5.5,"mae_pct":-3.5,"classification":"watch_cap_stable_education_holding_label_without_incremental_paid_enrollment_margin_bridge","calibration_usable":true,"evidence_family":"stable_education_brand_policy_exam_cycle_label_without_incremental_enrollment_margin_bridge","residual_error":"stable_education_brand_can_overpromote_without_fresh_paid_enrollment_and_op_conversion","shadow_rule_candidate":"cap_stable_education_brand_at_watch_yellow_if_mfe_shallow_and_incremental_bridge_missing"}
{"row_type":"case","case_id":"C31_R12L94_095720_2024_02_21","scheduled_round":"R12","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE","symbol":"095720","name":"웅진씽크빅","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":2525,"peak_high":2780,"peak_date":"2024-02-21","worst_low_after_entry":1640,"worst_low_after_entry_date":"2024-09-09","mfe_pct":10.1,"mae_pct":-35.0,"classification":"hard_4c_candidate_children_learning_edtech_policy_label_without_paid_enrollment_margin_bridge","calibration_usable":true,"evidence_family":"children_learning_edtech_policy_label_without_paid_enrollment_renewal_arpu_margin_bridge","residual_error":"education_policy_salience_can_fail_when_paid_enrollment_and_margin_bridge_missing","shadow_rule_candidate":"route_children_learning_edtech_label_to_hard_4c_if_mfe_modest_mae_large_and_paid_enrollment_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":94,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"EDUCATION_POLICY_ENROLLMENT_CONTENT_REORDER_MARGIN_BRIDGE_VS_EDUCATION_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"education_policy_service_case_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":94,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_EDUCATION_POLICY_PAID_ENROLLMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 education-policy/service events, do not open Stage2-Actionable or Stage3-Green from education policy, exam-cycle, medical-school quota, private academy, edtech, children learning, online content, or one-week education-stock spike labels alone. Require company-specific paid enrollment or renewal, curriculum/content demand, retention and ARPU, offline/online channel economics, marketing and teacher-cost containment, margin/OP conversion, and post-trigger price survival. Premium education content names with meaningful MFE may be capped positives when enrollment and margin bridge are explicit, but 4B should attach after rerating unless fresh evidence appears. Stable education brands with shallow MFE should cap at Watch/Yellow without incremental paid-demand evidence. Children-learning/edtech labels with modest MFE and high MAE should route to hard-4C when paid enrollment and margin bridge are missing.","expected_effect":"Reduce education-policy and edtech-label false positives while preserving true education-service positives with paid enrollment, renewal, ARPU, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":94,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"education_policy_paid_enrollment_margin_guard","contribution":"Adds one premium-education capped positive, one stable-education Watch cap, and one children-learning hard-4C counterexample to calibrate C31 education-service monetization requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_EDUCATION_POLICY_PAID_ENROLLMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [education_policy, exam_cycle, private_academy, edtech, children_learning, content_education]:

  Do not open Stage3-Green from:
    - education policy headline alone
    - exam-cycle or medical-school quota label alone
    - private academy brand alone
    - edtech / children-learning label alone
    - online content platform label alone
    - one-week education-stock volume spike alone

  Require at least two of:
    - paid enrollment growth
    - renewal / retention improvement
    - curriculum or content demand
    - ARPU / pricing improvement
    - offline/online channel economics
    - marketing / teacher-cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the education-policy headline

  If MFE < 12% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE is shallow and MAE is controlled:
    cap at Watch/Yellow unless incremental enrollment and margin bridge are explicit.

  If MFE > 15% but the bridge is not refreshed:
    preserve as capped positive or local 4B, not Green.

  Distinguish:
    - education-service names where enrollment and renewal become margin
    - from education labels where policy salience does not reach paid demand.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_94_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 education-policy/service cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_EDUCATION_POLICY_PAID_ENROLLMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 education-policy cases agree, consider implementing a canonical guard that:
   - blocks education-policy Green without paid enrollment/renewal/ARPU/margin bridge,
   - preserves premium education content positives only with price survival and margin evidence,
   - caps stable education brands at Watch/Yellow without incremental paid-demand evidence,
   - routes modest-MFE/high-MAE edtech or children-learning labels to hard-4C.

Expected next schedule:
completed_round = R12
completed_loop = 94
next_round = R13
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 94
next_round = R13
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
