# E2R Stock-Web v12 Residual Research — R13 / Loop 92

```yaml
scheduled_round: R13
scheduled_loop: 92
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: POLICY_GOVERNANCE_SERVICE_EVENT_CAP_TRUST_AND_MONETIZATION_GUARDRAIL

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

review_trigger_count: 9
reviewed_original_canonical_count: 3
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - PF_WORKOUT_PARENT_SUPPORT_REGIONAL_BUILDER_BALANCE_SHEET_TRUST_BRIDGE_VS_POLICY_RELIEF_BETA
  - PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE
  - MEDICAL_SCHOOL_QUOTA_EDUCATION_POLICY_TO_ENROLLMENT_REVENUE_BRIDGE_VS_EDU_THEME_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 3
capped_positive_or_event_arb_count: 5
local_burst_or_4b_watch_count: 5
watch_yellow_cap_count: 2
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 3
accounting_or_listing_trust_caveat_count: 3
tender_or_delisting_cap_case_count: 3
education_policy_theme_case_count: 3
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 92
next_round: R1
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 92
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a sector-specific research round. It is the cross-archetype checkpoint for:

```text
false positive
high MAE
4B too early / too late
4C late
accounting / listing / tradeability trust
price validation
event cap and residual spread
policy-to-company monetization bridge
```

After this file:

```text
next_round = R1
next_loop = 93
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop92 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 034300 신세계건설
  - 009410 태영건설
  - 002460 HS화성 / 화성산업

R11 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 003410 쌍용C&E
  - 115390 락앤락
  - 119860 커넥트웨이브

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 133750 메가엠디
  - 053290 NE능률
  - 215200 메가스터디교육
```

No-repeat handling:

```text
row_type = review_case
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
independent_evidence_weight_total = 0.0
```

The original R10/R11/R12 rows remain the usable calibration cases. This R13 file only validates cross-archetype guardrails and links the original cases into a common failure grammar.

---

## 3. Cross-archetype question

The same structural error appears across three different event families:

```text
C30 PF / construction balance-sheet break:
  policy support, parent support, or workout attention exists,
  but the equity value depends on repair, trust, and cash-flow bridge.

C32 governance / tender cap:
  public tender or control premium exists,
  but upside is capped by the offer price and residual spread.

C31 education policy:
  medical-school quota policy exists,
  but the company must convert it into paid enrollment, course demand, and margin.
```

Shared false-positive mechanism:

```text
external event
  -> sector or governance label becomes hot
  -> price reacts first
  -> model over-promotes the label to Stage2-Actionable / Stage3-Green
  -> company-specific economic bridge, cap, or trust issue is missing
  -> high MAE, 4B failure, or no residual upside follows
```

Shared guardrail:

```text
The event opens a door.
C30 asks whether the balance sheet can walk through.
C32 asks whether the door is already priced at a fixed exit.
C31 asks whether students actually enroll and pay.
```

---

## 4. Reviewed case matrix

| Original canonical | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---:|---|---:|---:|---:|---|
| C30 | 034300 | 신세계건설 | 11,460 | +62.7% | -14.0% | local positive, parent-support repair, 4B/trust cap |
| C30 | 009410 | 태영건설 | 3,765 | +9.2% | -42.1% | hard 4C, PF workout attention without equity repair |
| C30 | 002460 | HS화성 / 화성산업 | 10,500 | +7.0% | -19.3% | Watch/Yellow cap, regional-builder relief without repair |
| C32 | 003410 | 쌍용C&E | 6,940 | +1.4% | -2.3% | late-entry tender cap, Green blocked by no residual spread |
| C32 | 115390 | 락앤락 | 8,180 | +8.7% | ~0.0% | tender positive, event-arb only after cap convergence |
| C32 | 119860 | 커넥트웨이브 | 15,570 | +17.5% | ~0.0% | clean tender positive, finite cap not open-ended Green |
| C31 | 133750 | 메가엠디 | 2,995 | +18.7% | -45.0% | local policy burst, 4B failure without enrollment bridge |
| C31 | 053290 | NE능률 | 5,240 | +14.5% | -47.6% | hard 4C, education label without direct monetization |
| C31 | 215200 | 메가스터디교육 | 63,100 | +9.2% | -33.0% | hard 4C, quality platform without direct policy revenue bridge |

---

## 5. R10 review — PF support, parent support, and trust

### 5.1 034300 신세계건설

```text
entry_close: 11,460
peak_high: 18,650
MFE: +62.7%
worst_low_after_entry: 9,850
MAE: -14.0%
```

R13 interpretation:

```text
This was a valid local positive.
The parent-support / repair-perception frame compressed PF risk premium.
But later row-presence / inactive-like caveat means Green must remain capped.
```

Classification:

```text
positive_control = true
local_4b_watch = true
listing_or_tradeability_trust_cap = true
green_block_without_repair_terms = true
```

This is the C30 "repair can work" case. But the repair must be explicit, and later listing/trust context prevents treating it as ordinary Stage3-Green.

### 5.2 009410 태영건설

```text
entry_close: 3,765
peak_high: 4,110
MFE: +9.2%
worst_low_before_long_gap: 2,180
MAE: -42.1%
```

R13 interpretation:

```text
This is the hard failure.
PF workout attention did not equal equity repair.
The row gap / tradeability caveat makes the trust penalty central, not incidental.
```

Classification:

```text
hard_4c_candidate = true
tradeability_trust_penalty = true
stage2_actionable_block = true
```

The model must not confuse crisis visibility with investability.

### 5.3 002460 HS화성 / 화성산업

```text
entry_close: 10,500
peak_high: 11,230
MFE: +7.0%
worst_low: 8,470
MAE: -19.3%
```

R13 interpretation:

```text
This is the regional-builder cap case.
It did not implode, but it also did not validate an Actionable thesis.
```

Classification:

```text
watch_yellow_cap = true
green_block_without_pf_repair = true
```

The lesson is over-certainty. Stable regional-builder label plus PF policy relief is not enough.

---

## 6. R11 review — tender cap and residual spread

### 6.1 003410 쌍용C&E

```text
entry_close: 6,940
peak_high: 7,040
MFE: +1.4%
worst_low_after_entry: 6,780
MAE: -2.3%
```

R13 interpretation:

```text
The tender/delisting event was real.
The problem was late entry after price had already converged to the offer cap.
```

Classification:

```text
late_entry_tender_cap = true
stage3_green_block = true
event_arb_only = true
```

This is a no-upside counterexample, not a price-drawdown disaster. It blocks Green because the upside was already consumed.

### 6.2 115390 락앤락

```text
entry_close: 8,180
peak_high: 8,890
MFE: +8.7%
worst_post_entry_low_checked: 8,630
MAE: ~0.0% from close entry after the cap zone
```

R13 interpretation:

```text
This is a tender positive.
The event worked, but once the stock pinned near the offer, the remaining signal became residual spread only.
```

Classification:

```text
positive_control = true
local_4b_after_cap_convergence = true
green_cap = true
```

The model should preserve the event-arb positive and simultaneously block open-ended Green.

### 6.3 119860 커넥트웨이브

```text
entry_close: 15,570
peak_high: 18,300
MFE: +17.5%
worst_post_entry_low_checked: 17,760
MAE: ~0.0% from close entry after the gap
```

R13 interpretation:

```text
This is the cleanest tender-cap positive.
It proves C32 can be profitable, but only while residual spread remains.
```

Classification:

```text
positive_control = true
event_arb_cap = true
green_block_after_offer_convergence = true
```

This case should not be scored like a normal platform/SW rerating. The price path is an event spread converging to a fixed exit.

---

## 7. R12 review — education policy and paid enrollment conversion

### 7.1 133750 메가엠디

```text
entry_close: 2,995
peak_high: 3,555
MFE: +18.7%
worst_low: 1,647
MAE: -45.0%
```

R13 interpretation:

```text
This is the most direct medical-admissions policy exposure.
It produced tradable MFE, but later failed price survival.
```

Classification:

```text
local_4b_policy_burst = true
stage3_green_block = true
hard_4c_if_reentry_without_enrollment_bridge = true
```

The case says "direct label can trade" but not "direct label is Green."

### 7.2 053290 NE능률

```text
entry_close: 5,240
peak_high: 6,000
MFE: +14.5%
worst_low: 2,745
MAE: -47.6%
```

R13 interpretation:

```text
This is the broad education-theme failure.
Education relevance was too indirect.
```

Classification:

```text
hard_4c_candidate = true
education_label_false_positive = true
```

The model must require direct paid enrollment conversion.

### 7.3 215200 메가스터디교육

```text
entry_close: 63,100
peak_high: 68,900
MFE: +9.2%
worst_low: 42,300
MAE: -33.0%
```

R13 interpretation:

```text
This is the quality-platform guardrail.
A high-quality education business still failed the medical-quota Green test without a direct revenue bridge.
```

Classification:

```text
hard_4c_candidate = true
quality_label_not_policy_monetization = true
```

This case protects the model from upgrading company quality into policy monetization.

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_EVENT_CAP_TRUST_AND_MONETIZATION_BRIDGE_REQUIRED

For policy, governance, tender, and service-event archetypes:

  Do not open Stage2-Actionable or Stage3-Green from event existence alone.

  First classify the event type:
    - balance-sheet repair event
    - tender/control premium cap event
    - policy monetization event

  Then require the relevant bridge:
    - C30: PF repair, cash collection, refinancing, parent/lender support, trust
    - C32: offer price, residual spread, completion probability, liquidity endpoint
    - C31: paid enrollment, course demand, pricing, margin conversion

  If the event is already priced near a fixed cap:
    block Green and classify as Watch/event-arb only.

  If the event gives high MFE but later high MAE:
    preserve as local 4B/event burst, not Green.

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If trust or tradeability caveat appears:
    apply trust penalty before Actionable/Green promotion.
```

### Quantitative trigger candidates

```text
hard_4c_event_candidate:
  MFE < +15%
  AND MAE <= -30%
  AND company_specific_bridge_missing == true

local_4b_event_burst_candidate:
  MFE >= +15%
  AND MAE <= -35%
  AND monetization_or_repair_bridge_missing == true

tender_green_block_candidate:
  residual_spread_to_offer <= 1~2%
  OR price_pinned_near_offer == true

trust_penalty_candidate:
  row_gap_or_tradeability_caveat == true
  OR inactive_like_status appears before/around validation endpoint
  OR listing endpoint creates ambiguous exit risk

capped_positive_event_candidate:
  MFE >= +8%
  AND MAE controlled
  AND event mechanics explicit
  BUT upside finite or Green bridge incomplete
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L92_C30_034300","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"034300","name":"신세계건설","entry_date":"2024-02-07","entry_price":11460,"mfe_pct":62.7,"mae_pct":-14.0,"r13_verdict":"local_parent_support_repair_positive_but_4b_and_listing_trust_cap_required","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C30_009410","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"009410","name":"태영건설","entry_date":"2024-01-11","entry_price":3765,"mfe_pct":9.2,"mae_pct":-42.1,"r13_verdict":"hard_4c_pf_workout_attention_without_equity_repair_and_tradeability_trust","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C30_002460","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002460","name":"HS화성","entry_date":"2024-01-29","entry_price":10500,"mfe_pct":7.0,"mae_pct":-19.3,"r13_verdict":"watch_yellow_cap_regional_builder_relief_without_pf_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C32_003410","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"003410","name":"쌍용C&E","entry_date":"2024-02-05","entry_price":6940,"mfe_pct":1.4,"mae_pct":-2.3,"r13_verdict":"late_entry_tender_cap_no_green_residual_spread_consumed","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C32_115390","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"115390","name":"락앤락","entry_date":"2024-04-17","entry_price":8180,"mfe_pct":8.7,"mae_pct":0.0,"r13_verdict":"positive_tender_gap_then_cap_event_arb_only_after_convergence","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C32_119860","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"119860","name":"커넥트웨이브","entry_date":"2024-04-26","entry_price":15570,"mfe_pct":17.5,"mae_pct":0.0,"r13_verdict":"clean_tender_cap_positive_but_finite_offer_cap_blocks_open_ended_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C31_133750","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"133750","name":"메가엠디","entry_date":"2024-02-06","entry_price":2995,"mfe_pct":18.7,"mae_pct":-45.0,"r13_verdict":"local_4b_medical_admissions_policy_burst_not_green_without_paid_enrollment_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C31_053290","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"053290","name":"NE능률","entry_date":"2024-02-06","entry_price":5240,"mfe_pct":14.5,"mae_pct":-47.6,"r13_verdict":"hard_4c_broad_education_policy_theme_without_direct_enrollment_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L92_C31_215200","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"215200","name":"메가스터디교육","entry_date":"2024-02-06","entry_price":63100,"mfe_pct":9.2,"mae_pct":-33.0,"r13_verdict":"hard_4c_quality_education_platform_without_direct_policy_revenue_bridge","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":3,"capped_positive_or_event_arb_count":5,"local_burst_or_4b_watch_count":5,"watch_yellow_cap_count":2,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":3,"accounting_or_listing_trust_caveat_count":3,"tender_or_delisting_cap_case_count":3,"education_policy_theme_case_count":3,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":92,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_EVENT_CAP_TRUST_AND_MONETIZATION_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy, governance, tender, and service-event archetypes, do not open Stage2-Actionable or Stage3-Green from event existence alone. Classify the event as balance-sheet repair, tender/control cap, or policy monetization. Require the matching company-specific bridge: PF repair/trust for C30, offer price/residual spread/completion mechanics for C32, and paid enrollment/revenue/margin bridge for C31 education policy. If price is already near a fixed offer cap, block Green and classify as Watch/event-arb. If MFE is high but later MAE is high, keep as local 4B/event burst. If MFE is shallow and MAE is large, route to hard 4C. If row gap, trading halt, listing endpoint, or inactive-like status creates trust ambiguity, apply trust penalty before any Green promotion.","expected_effect":"Unifies PF repair, tender cap, and education policy guardrails so the model stops confusing event salience with open-ended company earnings power.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":92,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"event_cap_trust_and_monetization_guard","contribution":"Reviews nine prior loop92 cases without adding new independent evidence weight. Validates a shared event guard across PF repair/trust, public tender cap, and medical-school quota education-policy monetization cases.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_EVENT_CAP_TRUST_AND_MONETIZATION_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop92 files:
   - C30 PF/workout/parent-support/regional-builder balance-sheet trust
   - C32 public tender / delisting / control-premium cap
   - C31 medical-school quota education policy
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/governance/service events:
   - classify the event type first,
   - identify true economic recipient and cost/trust burden,
   - block event-existence-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep high-MFE/high-MAE as local 4B,
   - cap tender names once residual spread is exhausted,
   - allow capped positives only after explicit bridge evidence.

Expected next schedule:
completed_round = R13
completed_loop = 92
next_round = R1
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 92
next_round = R1
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
