# E2R Stock-Web v12 Residual Research — R13 / Loop 90

```yaml
scheduled_round: R13
scheduled_loop: 90
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: POLICY_EVENT_BRIDGE_FAILURE_4B_4C_REDTEAM_PF_GOVERNANCE_PAYMENT_SETTLEMENT

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
  - C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - C31_POLICY_SUBSIDY_LEGISLATION_EVENT

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 2
delayed_positive_count: 1
local_burst_or_4b_watch_count: 4
stage2_false_positive_or_high_mae_count: 7
hard_4c_candidate_count: 4

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 90
next_round: R1
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 90
```

R13 is not an ordinary sector research round. It must be a cross-archetype checkpoint:

```text
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

After R13, the next state is:

```text
next_round = R1
next_loop = 91
```

---

## 2. Source set reviewed

This R13 review does not introduce new independent cases. It reviews the nine cases produced in loop90 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 014790 HL D&I
  - 010780 아이에스동서
  - 005960 동부건설

R11 / C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
  - 454910 두산로보틱스
  - 034020 두산에너빌리티
  - 241560 두산밥캣

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 060250 NHN KCP
  - 035600 KG이니시스
  - 377300 카카오페이
```

No-repeat handling:

```text
row_type = R13 review row
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
```

The reviewed underlying C30/C31/C32 cases remain valid calibration candidates in their original files, but this R13 file only tests guardrails across them.

---

## 3. Cross-archetype question

The same error appeared in three different costumes:

```text
C30:
  policy firewall for construction/PF liquidity
  vs company-specific PF repair and cash-flow bridge

C32:
  governance/control restructuring headline
  vs share-class-specific value capture or value transfer

C31:
  settlement protection / merchant support policy
  vs company-specific fund-flow, escrow, compliance-cost, and take-rate bridge
```

Shared false-positive mechanism:

```text
headline exists
  -> market imagines a policy or control premium
  -> early price spike or sector relief appears
  -> model opens Stage2-Actionable too early
  -> company-specific bridge is missing
  -> high MAE, local 4B failure, or hard 4C follows
```

This is not three separate bugs. It is one structural bug:

```text
the model confuses an external umbrella with an internal engine.
```

A policy umbrella can keep the rain off a sector. It does not start every company’s engine. C30, C31, and C32 need the same conceptual guard: identify **who actually receives the cash-flow benefit** and **who absorbs the cost, dilution, or compliance burden**.

---

## 4. Reviewed case matrix

| Original canonical | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---:|---|---:|---:|---:|---|
| C30 | 014790 | HL D&I | 2,010 | +43.3% | -2.1% | positive control, but Green needs PF repair bridge |
| C30 | 010780 | 아이에스동서 | 29,250 | +4.1% | -30.4% | hard 4C candidate |
| C30 | 005960 | 동부건설 | 5,030 | +0.8% | -17.0% | shallow-MFE policy false positive |
| C32 | 454910 | 두산로보틱스 | 85,300 | +28.1% | -36.8% | local burst / 4B required, not Green |
| C32 | 034020 | 두산에너빌리티 | 21,850 | +14.4% | -30.7% | hard 4C candidate |
| C32 | 241560 | 두산밥캣 | 52,000 | +14.4% | -35.9% | hard 4C candidate, minority-transfer risk |
| C31 | 060250 | NHN KCP | 9,050 | +1.0% | -21.5% | hard 4C candidate |
| C31 | 035600 | KG이니시스 | 10,600 | +14.3% | -18.1% | local burst failed durability |
| C31 | 377300 | 카카오페이 | 26,000 | +35.4% extended | -15.6% initial | delayed positive only |

---

## 5. C30 review — PF policy firewall vs company-specific repair

### 5.1 014790 HL D&I

HL D&I was the useful positive control:

```text
entry_close: 2,010
peak_high: 2,880
MFE: +43.3%
worst_low: 1,968
MAE: -2.1%
```

R13 conclusion:

```text
C30 Actionable can work when price confirms with low MAE.
But Green still needs company-specific PF exposure repair, refinancing, cash collection, and order-margin bridge.
```

This case is not a free pass for all builders. It is the exception that proves the bridge requirement.

### 5.2 010780 아이에스동서

아이에스동서 failed the PF-policy read:

```text
entry_close: 29,250
peak_high: 30,450
MFE: +4.1%
worst_low: 20,350
MAE: -30.4%
```

R13 conclusion:

```text
hard_4c_candidate = true
```

A real sector policy did not create a stock-level escape route. The bridge from support policy to company-specific balance-sheet repair was missing.

### 5.3 005960 동부건설

동부건설 was a quieter failure:

```text
entry_close: 5,030
peak_high: 5,070
MFE: +0.8%
worst_low: 4,175
MAE: -17.0%
```

R13 conclusion:

```text
Stage2-Watch allowed.
Stage2-Actionable blocked.
Stage3-Green blocked.
```

The error is not dramatic, but it is still useful. Shallow MFE says the policy headline did not become investable evidence.

---

## 6. C32 review — governance event vs share-class value capture

### 6.1 454910 두산로보틱스

두산로보틱스 was the apparent favored vehicle:

```text
entry_close: 85,300
peak_high: 109,300
MFE: +28.1%
worst_low: 53,900
MAE: -36.8%
```

R13 conclusion:

```text
local_burst = true
4B_required = true
Stage3-Green = blocked
```

Even the apparent beneficiary leg failed price survival. A favored control vehicle can burn bright for one day, but the flame is not a furnace.

### 6.2 034020 두산에너빌리티

두산에너빌리티 was the intermediate leg:

```text
entry_close: 21,850
peak_high: 25,000
MFE: +14.4%
worst_low: 15,150
MAE: -30.7%
```

R13 conclusion:

```text
hard_4c_candidate = true
```

The model must not score group-restructuring relevance as if it were direct value capture for this listed share class.

### 6.3 241560 두산밥캣

두산밥캣 was the minority-risk leg:

```text
entry_close: 52,000
peak_high: 59,500
MFE: +14.4%
worst_low: 33,350
MAE: -35.9%
```

R13 conclusion:

```text
hard_4c_candidate = true
minority_value_transfer_guard = required
```

This is the clearest C32 guardrail case. The question is not “does a governance event exist?” The question is “does this exact share class receive or surrender value?”

---

## 7. C31 review — payment-policy shock vs fund-flow exposure

### 7.1 060250 NHN KCP

NHN KCP was the direct-PG hard 4C:

```text
entry_close: 9,050
peak_high: 9,140
MFE: +1.0%
worst_low: 7,100
MAE: -21.5%
extended_worst_low: 6,860
extended_MAE: -24.2%
```

R13 conclusion:

```text
hard_4c_candidate = true
```

“Settlement protection” is not automatically good for direct PG firms. It may create compliance, escrow, settlement-cycle, and chargeback ambiguity.

### 7.2 035600 KG이니시스

KG이니시스 was a local-burst failure:

```text
entry_close: 10,600
local_peak_high: 12,120
MFE: +14.3%
worst_low_180d: 8,680
MAE: -18.1%
extended_worst_low: 7,980
extended_MAE: -24.7%
```

R13 conclusion:

```text
local_burst = true
durable_green = false
```

The one-week flare did not survive. The bridge from policy shock to take-rate / volume / cost economics was missing.

### 7.3 377300 카카오페이

카카오페이 was the delayed-positive exception:

```text
entry_close: 26,000
initial_worst_low: 21,950
initial_MAE: -15.6%
extended_peak_high: 35,200
extended_MFE: +35.4%
```

R13 conclusion:

```text
delayed_positive = true
immediate_green = false
```

This case prevents overfitting the guard too negatively. Wallet/platform names can recover if the market later differentiates them from direct merchant-settlement risk. But the initial drawdown means the policy event itself did not justify immediate Green.

---

## 8. Cross-archetype guardrail

### Proposed R13 guard

```text
R13_POLICY_EVENT_BRIDGE_AND_RECIPIENT_MAP_REQUIRED

For C30, C31, C32 and similar policy/event archetypes:

  Do not open Stage2-Actionable or Stage3-Green from headline existence alone.

  Before scoring, identify the actual economic recipient:
    - company balance sheet
    - specific share class
    - direct regulated entity
    - indirect platform
    - minority-risk subsidiary
    - creditor / merchant / customer / government

  Require bridge evidence:
    - cash-flow conversion
    - cost containment
    - settlement/refinancing mechanism
    - contract or legal protection
    - value-transfer fairness
    - price survival after the first spike

  If early MFE is shallow and MAE is large:
    route to false positive or hard 4C.

  If early MFE is large but later MAE exceeds -30%:
    keep local burst / 4B watch, not Green.

  If initial MAE occurs first but later MFE confirms:
    allow delayed-positive classification only after the separate bridge appears.
```

### Quantitative trigger candidates

```text
hard_4c_policy_event_candidate:
  MFE < +10%
  AND MAE <= -20%
  AND company_specific_bridge is missing

local_4b_not_green_candidate:
  MFE >= +20%
  AND later_MAE <= -30%
  AND event bridge remains contested

delayed_positive_candidate:
  initial_MAE <= -10%
  AND later_MFE >= +30%
  AND business exposure is more indirect / lower-risk than first read
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L90_C30_014790","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"014790","name":"HL D&I","entry_date":"2024-03-27","entry_price":2010,"mfe_pct":43.3,"mae_pct":-2.1,"r13_verdict":"positive_control_but_green_needs_pf_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C30_010780","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"010780","name":"아이에스동서","entry_date":"2024-03-27","entry_price":29250,"mfe_pct":4.1,"mae_pct":-30.4,"r13_verdict":"hard_4c_candidate_policy_support_without_company_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C30_005960","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"005960","name":"동부건설","entry_date":"2024-03-27","entry_price":5030,"mfe_pct":0.8,"mae_pct":-17.0,"r13_verdict":"shallow_mfe_policy_false_positive_watch_only","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C32_454910","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"454910","name":"두산로보틱스","entry_date":"2024-07-11","entry_price":85300,"mfe_pct":28.1,"mae_pct":-36.8,"r13_verdict":"local_burst_4b_required_not_green","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C32_034020","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"034020","name":"두산에너빌리티","entry_date":"2024-07-11","entry_price":21850,"mfe_pct":14.4,"mae_pct":-30.7,"r13_verdict":"hard_4c_candidate_intermediate_share_class_value_bridge_unclear","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C32_241560","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"241560","name":"두산밥캣","entry_date":"2024-07-11","entry_price":52000,"mfe_pct":14.4,"mae_pct":-35.9,"r13_verdict":"hard_4c_candidate_minority_value_transfer_risk","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C31_060250","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"060250","name":"NHN KCP","entry_date":"2024-07-26","entry_price":9050,"mfe_pct":1.0,"mae_pct":-21.5,"r13_verdict":"hard_4c_candidate_direct_pg_exposure_without_settlement_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C31_035600","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"035600","name":"KG이니시스","entry_date":"2024-07-26","entry_price":10600,"mfe_pct":14.3,"mae_pct":-18.1,"r13_verdict":"local_burst_failed_durability_watch_yellow_only","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L90_C31_377300","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"377300","name":"카카오페이","entry_date":"2024-07-26","entry_price":26000,"initial_mae_pct":-15.6,"extended_mfe_pct":35.4,"r13_verdict":"delayed_positive_only_after_exposure_mapping_and_price_confirmation","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":90,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":3,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":2,"delayed_positive_count":1,"local_burst_or_4b_watch_count":4,"stage2_false_positive_or_high_mae_count":7,"hard_4c_candidate_count":4,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":90,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_POLICY_EVENT_BRIDGE_AND_RECIPIENT_MAP_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy/event/governance archetypes, do not open Stage2-Actionable or Stage3-Green from event headline existence alone. First map the actual economic recipient and burden bearer: company balance sheet, share class, direct regulated entity, indirect platform, minority-risk subsidiary, creditor, merchant, customer, or government. Require a bridge to cash-flow conversion, cost containment, settlement/refinancing mechanism, legal or contractual protection, value-transfer fairness, and price survival. Shallow-MFE/high-MAE cases route to hard 4C. Large-MFE/high-MAE cases remain local burst/4B watch, not Green. Initial-MAE/later-MFE cases require delayed-positive confirmation.","expected_effect":"Unifies C30, C31, and C32 guardrails so the model stops mistaking policy umbrellas, governance bursts, or settlement headlines for company-specific economic engines.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":90,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"cross_policy_event_recipient_mapping_guard","contribution":"Validates a shared guard across PF policy, governance restructuring, and payment-settlement policy events. Reviews nine prior loop90 cases without adding new independent evidence weight.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_POLICY_EVENT_BRIDGE_AND_RECIPIENT_MAP_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop90 files:
   - C30 PF balance-sheet break
   - C32 governance/control-premium/tender-cap
   - C31 payment/e-commerce settlement policy
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/event archetypes:
   - identify the true economic recipient,
   - identify who bears cost/dilution/compliance risk,
   - block headline-only Stage3-Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep high-MFE/high-MAE as local 4B only,
   - allow delayed-positive only after independent bridge and price confirmation.

Expected next schedule:
completed_round = R13
completed_loop = 90
next_round = R1
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 90
next_round = R1
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
