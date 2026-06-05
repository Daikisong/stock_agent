# E2R Stock-Web v12 Residual Research — R13 / Loop 91

```yaml
scheduled_round: R13
scheduled_loop: 91
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: POLICY_EVENT_RECIPIENT_MAPPING_EARNINGS_BRIDGE_AND_PRICE_SURVIVAL_REDTEAM

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
reviewed_original_canonical_count: 2
reviewed_original_canonical_ids:
  - C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT
reviewed_fine_branch_count: 3
reviewed_fine_branches:
  - SMALL_BUILDER_PF_POLICY_RELIEF_TO_BALANCE_SHEET_REPAIR_BRIDGE_VS_POLITICAL_CONSTRUCTION_BETA
  - AI_SEMICONDUCTOR_POLICY_FUND_TO_COMPANY_EARNINGS_BRIDGE_VS_GENERIC_CHIP_POLICY_BETA
  - CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 3
delayed_or_capped_positive_count: 2
local_burst_or_4b_watch_count: 4
stage2_false_positive_or_high_mae_count: 6
hard_4c_candidate_count: 4
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 91
next_round: R1
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 91
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a new sector-specific research round. It is a cross-archetype checkpoint for:

```text
false positive
high MAE
4B too early / too late
4C late
accounting or listing trust
price validation
```

After this file:

```text
next_round = R1
next_loop = 92
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop91 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 013360 일성건설
  - 001470 삼부토건
  - 002410 범양건영

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 000660 SK하이닉스
  - 005930 삼성전자
  - 000990 DB하이텍

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 039130 하나투어
  - 080160 모두투어
  - 094850 참좋은여행
```

No-repeat handling:

```text
row_type = R13 review row
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
```

The underlying C30/C31 rows remain valid calibration candidates in their original files. This R13 file only reviews them as a holdout guardrail set.

---

## 3. Cross-archetype question

The same structural error appeared in three different event families:

```text
C30 small-builder PF policy:
  government support exists
  but company-specific PF/cash-flow repair may not exist.

C31 AI semiconductor policy:
  national policy/fund exists
  but the company may not have a direct product/customer/margin bridge.

C31 travel visa policy:
  visa-free access exists
  but bookings, packages, seats, and margins may not convert.
```

Shared false-positive mechanism:

```text
external policy event
  -> sector label becomes hot
  -> early spike or relief rally appears
  -> model over-promotes to Stage2-Actionable / Stage3-Green
  -> company-specific economic recipient is not mapped
  -> MAE or local 4B failure follows
```

The common rule is simple:

```text
A policy opens a gate.
It does not prove which company sells tickets at that gate.
```

R13 therefore tests whether the model should first identify:

```text
actual economic recipient
cost or dilution bearer
revenue bridge
margin bridge
price survival
```

before promoting a policy event.

---

## 4. Reviewed case matrix

| Original canonical | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---:|---|---:|---:|---:|---|
| C30 | 013360 | 일성건설 | 1,267 | +46.8% | -6.2% | positive local relief, 4B watch, not Green without PF repair |
| C30 | 001470 | 삼부토건 | 1,993 | +8.6% | -77.0% | hard 4C, policy/political beta without trust bridge |
| C30 | 002410 | 범양건영 | 1,611 | +10.2% | -30.9% | hard 4C, small-builder PF repair bridge missing |
| C31 | 000660 | SK하이닉스 | 182,900 | +35.9% | -17.7% | direct policy-recipient positive, but 4B watch after peak drawdown |
| C31 | 005930 | 삼성전자 | 83,600 | +6.0% | -40.3% | hard 4C, national champion halo without execution bridge |
| C31 | 000990 | DB하이텍 | 44,300 | +33.0% | -29.1% | local burst, not Green without AI revenue/margin bridge |
| C31 | 039130 | 하나투어 | 50,900 | +17.9% | -9.2% | positive/capped, booking margin bridge required |
| C31 | 080160 | 모두투어 | 11,400 | +9.2% | -19.1% | false-positive Watch/Yellow cap |
| C31 | 094850 | 참좋은여행 | 6,070 | +30.0% | -21.5% | local 4B event burst, not Green |

---

## 5. R10 review — PF support vs company-specific repair

### 5.1 013360 일성건설

```text
entry_close: 1,267
peak_high: 1,860
MFE: +46.8%
worst_low: 1,189
MAE: -6.2%
```

R13 interpretation:

```text
This was a valid local positive.
The policy relief frame compressed small-builder risk premium.
But this should not become Stage3-Green without company-specific PF repair.
```

Classification:

```text
positive_control = true
local_4b_watch = true
green_block_without_pf_repair = true
```

The important point is not that all builders worked. The point is that a low-MAE relief rally can be tradable, but Green still needs refinancing, liquidity repair, and cash-flow evidence.

### 5.2 001470 삼부토건

```text
entry_close: 1,993
peak_high: 2,165
MFE: +8.6%
worst_low: 458
MAE: -77.0%
```

R13 interpretation:

```text
This is the hard failure.
Construction-policy beta and political construction theme did not protect the equity path.
```

Classification:

```text
hard_4c_candidate = true
accounting_or_listing_trust_penalty = true
stage2_false_positive_guard = true
```

The later row-presence caveat reinforces trust risk, but the 2024 price path already fails by itself.

### 5.3 002410 범양건영

```text
entry_close: 1,611
peak_high: 1,775
MFE: +10.2%
worst_low: 1,114
MAE: -30.9%
```

R13 interpretation:

```text
Small-builder support headline did not convert into equity repair.
Shallow MFE and high MAE justify hard-4C routing.
```

Classification:

```text
hard_4c_candidate = true
stage2_actionable_block = true
```

---

## 6. R11 review — semiconductor policy vs direct product/customer bridge

### 6.1 000660 SK하이닉스

```text
entry_close: 182,900
peak_high: 248,500
MFE: +35.9%
worst_low_after_peak: 150,500
MAE vs entry: -17.7%
peak_to_later_low_drawdown: -39.4%
```

R13 interpretation:

```text
This is the direct-recipient positive.
AI policy mapped to HBM / AI memory exposure, product/customer demand, and margin revision.
```

Classification:

```text
positive_control = true
local_4b_watch = true
green_requires_new_revision_bridge = true
```

The case supports Actionable when policy maps directly into the product stack. But the post-peak drawdown says C31 still needs 4B discipline.

### 6.2 005930 삼성전자

```text
entry_close: 83,600
peak_high: 88,600
MFE: +6.0%
worst_low: 49,900
MAE: -40.3%
```

R13 interpretation:

```text
This is the national-champion halo failure.
Policy relevance was high, but execution bridge was not enough at the trigger.
```

Classification:

```text
hard_4c_candidate = true
national_champion_halo_guard = true
```

The model must not treat policy salience as earnings conversion.

### 6.3 000990 DB하이텍

```text
entry_close: 44,300
peak_high: 58,900
MFE: +33.0%
worst_low: 31,400
MAE: -29.1%
peak_to_later_low_drawdown: -46.7%
```

R13 interpretation:

```text
This was a policy-label local burst.
The foundry/system-semiconductor label produced a tradable move, but did not survive as Green.
```

Classification:

```text
local_burst_or_4b = true
stage3_green_block = true
```

The case is important because high MFE alone is not enough. Without direct AI revenue and margin bridge, the move belongs in 4B / event-burst classification.

---

## 7. R12 review — visa-free policy vs booking and margin conversion

### 7.1 039130 하나투어

```text
entry_close: 50,900
peak_high: 60,000
MFE: +17.9%
worst_low: 46,200
MAE: -9.2%
```

R13 interpretation:

```text
This is the service-policy positive control.
The company has direct booking-channel exposure, and the price path was controlled.
```

Classification:

```text
positive_control = true
stage2_actionable_allowed_if_booking_margin_bridge_confirms = true
stage3_green_from_policy_headline_alone = false
```

This is not a large blowoff. It is a measured positive that still needs booking and package-margin confirmation.

### 7.2 080160 모두투어

```text
entry_close: 11,400
peak_high: 12,450
MFE: +9.2%
worst_low: 9,220
MAE: -19.1%
```

R13 interpretation:

```text
Policy relevance existed, but price survival was weak.
Booking / package-margin bridge was not strong enough.
```

Classification:

```text
false_positive_guard = true
watch_yellow_cap = true
```

### 7.3 094850 참좋은여행

```text
entry_close: 6,070
peak_high: 7,890
MFE: +30.0%
worst_low: 4,765
MAE: -21.5%
```

R13 interpretation:

```text
This was the small-agency policy burst.
The event created a sharp move, but price survival failed quickly.
```

Classification:

```text
local_4b_event_burst = true
hard_4c_candidate_borderline = true
green_block = true
```

The first move was the spark. The missing booking/margin bridge prevented it from becoming a furnace.

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_POLICY_EVENT_RECIPIENT_EARNINGS_BRIDGE_AND_PRICE_SURVIVAL_REQUIRED

For C30/C31 and related policy/event archetypes:

  Do not open Stage2-Actionable or Stage3-Green from policy-event existence alone.

  First identify the actual recipient:
    - builder balance sheet
    - AI-memory product line
    - national champion halo
    - foundry/system-semiconductor label
    - large travel agency booking channel
    - small travel-agency policy beta

  Then require:
    - company-specific economic bridge
    - product/customer/channel conversion
    - cost or execution-risk check
    - margin or OP conversion
    - low-MAE post-trigger price survival

  If the event creates high MFE but later high MAE:
    preserve as local 4B / event burst, not Green.

  If MFE is shallow and MAE is large:
    route to false-positive or hard 4C.

  If MFE is moderate and MAE is controlled:
    allow Actionable only if the recipient bridge is explicit.
```

### Quantitative trigger candidates

```text
hard_4c_policy_event_candidate:
  MFE < +10%
  AND MAE <= -30%
  AND recipient_bridge_missing == true

local_4b_policy_burst_candidate:
  MFE >= +25%
  AND MAE <= -20%
  AND earnings_bridge_missing_or_unconfirmed == true

capped_positive_policy_candidate:
  MFE >= +15%
  AND MAE > -10%
  AND recipient_bridge_plausible == true
  BUT Green blocked until margin/OP confirmation

positive_with_4b_watch_candidate:
  MFE >= +30%
  AND peak_to_later_low_drawdown <= -35%
  AND original recipient bridge remains valid
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L91_C30_013360","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"013360","name":"일성건설","entry_date":"2024-03-27","entry_price":1267,"mfe_pct":46.8,"mae_pct":-6.2,"r13_verdict":"positive_local_relief_but_green_needs_pf_cashflow_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C30_001470","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"001470","name":"삼부토건","entry_date":"2024-03-27","entry_price":1993,"mfe_pct":8.6,"mae_pct":-77.0,"r13_verdict":"hard_4c_policy_political_beta_without_balance_sheet_trust_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C30_002410","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"002410","name":"범양건영","entry_date":"2024-03-27","entry_price":1611,"mfe_pct":10.2,"mae_pct":-30.9,"r13_verdict":"hard_4c_small_builder_policy_support_without_pf_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_000660","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000660","name":"SK하이닉스","entry_date":"2024-04-09","entry_price":182900,"mfe_pct":35.9,"mae_pct":-17.7,"peak_to_later_low_drawdown_pct":-39.4,"r13_verdict":"positive_direct_policy_recipient_but_local_4b_watch_required","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_005930","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"005930","name":"삼성전자","entry_date":"2024-04-09","entry_price":83600,"mfe_pct":6.0,"mae_pct":-40.3,"r13_verdict":"hard_4c_national_champion_policy_halo_without_execution_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_000990","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"000990","name":"DB하이텍","entry_date":"2024-04-09","entry_price":44300,"mfe_pct":33.0,"mae_pct":-29.1,"peak_to_later_low_drawdown_pct":-46.7,"r13_verdict":"local_4b_policy_label_burst_not_green_without_ai_revenue_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_039130","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"039130","name":"하나투어","entry_date":"2024-11-04","entry_price":50900,"mfe_pct":17.9,"mae_pct":-9.2,"r13_verdict":"capped_positive_large_agency_booking_bridge_required_before_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_080160","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"080160","name":"모두투어","entry_date":"2024-11-04","entry_price":11400,"mfe_pct":9.2,"mae_pct":-19.1,"r13_verdict":"watch_yellow_cap_theme_spike_without_durable_booking_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L91_C31_094850","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"094850","name":"참좋은여행","entry_date":"2024-11-04","entry_price":6070,"mfe_pct":30.0,"mae_pct":-21.5,"r13_verdict":"local_4b_small_agency_policy_burst_not_green","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":2,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":3,"delayed_or_capped_positive_count":2,"local_burst_or_4b_watch_count":4,"stage2_false_positive_or_high_mae_count":6,"hard_4c_candidate_count":4,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":91,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_POLICY_EVENT_RECIPIENT_EARNINGS_BRIDGE_AND_PRICE_SURVIVAL_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy/event archetypes, do not open Stage2-Actionable or Stage3-Green from external policy-event existence alone. First map the true economic recipient and burden bearer. Require company-specific product, project, booking, customer, channel, or balance-sheet bridge; execution and cost-risk check; margin or OP conversion; and post-trigger price survival. Shallow-MFE/high-MAE cases route to hard-4C. High-MFE/high-MAE cases remain local 4B/event bursts, not Green. Moderate-MFE/low-MAE cases may be capped positives only when recipient bridge is explicit.","expected_effect":"Unifies PF policy, AI semiconductor policy, and travel visa policy guardrails so the model stops confusing policy gates with company earnings engines.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":91,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"policy_event_recipient_mapping_and_price_survival_guard","contribution":"Validates a shared policy-event guard across small-builder PF support, AI semiconductor subsidy, and China visa-free travel-service cases. Reviews nine prior loop91 cases without adding new independent evidence weight.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_POLICY_EVENT_RECIPIENT_EARNINGS_BRIDGE_AND_PRICE_SURVIVAL_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop91 files:
   - C30 small-builder PF balance-sheet break
   - C31 AI semiconductor policy
   - C31 China visa-free travel-service policy
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/event archetypes:
   - identify the true economic recipient,
   - identify cost/execution/financing/listing-trust risks,
   - block policy-headline-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep high-MFE/high-MAE as local 4B,
   - allow capped positives only after explicit recipient and earnings bridge.

Expected next schedule:
completed_round = R13
completed_loop = 91
next_round = R1
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 91
next_round = R1
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
