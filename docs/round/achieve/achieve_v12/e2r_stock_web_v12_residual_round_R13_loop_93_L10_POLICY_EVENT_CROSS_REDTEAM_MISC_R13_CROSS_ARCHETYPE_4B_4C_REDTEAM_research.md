# E2R Stock-Web v12 Residual Research — R13 / Loop 93

```yaml
scheduled_round: R13
scheduled_loop: 93
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
fine_archetype_id: REGIONAL_HOUSING_VALUEUP_AGRI_POLICY_BRIDGE_REDTEAM

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
  - REGIONAL_HOUSING_PF_PRESALE_BACKLOG_MARGIN_TRUST_BRIDGE_VS_SMALL_BUILDER_POLICY_RELIEF_SPIKE
  - KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE
  - FOOD_SECURITY_AGRI_INPUT_POLICY_DEMAND_MARGIN_BRIDGE_VS_AGRI_THEME_SPIKE

new_independent_case_count: 0
do_not_count_as_new_case_count: 9
independent_evidence_weight_total: 0.0

positive_control_count: 4
capped_positive_or_bridge_positive_count: 4
local_burst_or_4b_watch_count: 2
watch_yellow_cap_count: 2
stage2_false_positive_or_high_mae_count: 5
hard_4c_candidate_count: 3
trust_or_policy_bridge_case_count: 9
regional_housing_pf_case_count: 3
valueup_holding_company_case_count: 3
agri_food_security_policy_case_count: 3
calibration_usable_review_count: 9

loop_contribution_label: holdout_validation_passed
canonical_archetype_rule_candidate: true
cross_archetype_guardrail_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R13
completed_loop: 93
next_round: R1
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R12_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R13
scheduled_loop = 93
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = R13_CROSS_ARCHETYPE_4B_4C_REDTEAM
```

R13 is not a sector-specific new-case round. It is the cross-archetype checkpoint for:

```text
false positive
high MAE
4B too early / too late
4C late
accounting / listing / tradeability trust
price validation
policy label vs company-specific bridge
event cap / demand / monetization / trust
```

After this file:

```text
next_round = R1
next_loop = 94
```

---

## 2. Source set reviewed

This R13 review does not add new independent cases. It reviews the nine cases produced in loop93 R10~R12:

```text
R10 / C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
  - 035890 서희건설
  - 013120 동원개발
  - 017000 신원종합개발

R11 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 402340 SK스퀘어
  - 001040 CJ
  - 034730 SK

R12 / C31_POLICY_SUBSIDY_LEGISLATION_EVENT
  - 008040 사조동아원
  - 054050 농우바이오
  - 002900 TYM
```

No-repeat handling:

```text
row_type = review_case
new_independent_case_count = 0
do_not_count_as_new_case_count = 9
independent_evidence_weight_total = 0.0
```

The original R10/R11/R12 rows remain the usable calibration cases. This R13 file only validates cross-archetype guardrails and links the original cases into a shared policy/event failure grammar.

---

## 3. Cross-archetype question

The same structural error appears across three event families:

```text
C30 regional housing / PF / small-builder relief:
  policy relief, regional builder label, or small-builder spike exists,
  but equity value depends on PF exposure, presales, project cash, margin, and trust.

C31 Korea Value-up / holding-company NAV discount:
  policy pressure and low-PBR/NAV-discount label exist,
  but equity value depends on actual capital allocation, shareholder return, asset monetization, and price survival.

C31 food-security / agri-input policy:
  food security and agri-input salience exist,
  but equity value depends on paid demand, product spread, input-cost pass-through, order/shipment, and margin.
```

Shared false-positive mechanism:

```text
external policy / event salience
  -> sector or governance label becomes hot
  -> price reacts first
  -> model over-promotes the label to Stage2-Actionable / Stage3-Green
  -> company-specific economic bridge is missing
  -> shallow MFE, high MAE, Watch cap, local 4B, or hard 4C follows
```

Shared guardrail:

```text
The event rings the bell.
C30 asks whether the builder's beams and financing can hold the weight.
C31 Value-up asks whether the company turns policy pressure into actual shareholder return.
C31 agri asks whether food-security concern becomes paid demand and margin.
```

---

## 4. Reviewed case matrix

| Original canonical | Symbol | Name | Entry | MFE | MAE | R13 verdict |
|---|---:|---|---:|---:|---:|---|
| C30 | 035890 | 서희건설 | 1,405 | +15.4% | -1.9% | regional housing capped positive; PF/presale bridge still required |
| C30 | 013120 | 동원개발 | 3,100 | +1.3% | -20.6% | Watch/Yellow cap; regional developer label without repair bridge |
| C30 | 017000 | 신원종합개발 | 4,080 | +4.9% | -33.6% | hard 4C; small-builder relief spike without trust bridge |
| C31 | 402340 | SK스퀘어 | 67,300 | +42.9% | -4.6% | clean Value-up NAV/shareholder-return positive |
| C31 | 001040 | CJ | 94,300 | +49.1% | -2.5% | positive with local 4B after large MFE |
| C31 | 034730 | SK | 190,200 | +5.1% | -32.5% | hard 4C; holding-company label without durable NAV/return bridge |
| C31 | 008040 | 사조동아원 | 1,009 | +17.7% | -5.4% | food-security grain/feed capped positive |
| C31 | 054050 | 농우바이오 | 8,480 | +4.0% | -17.6% | Watch/Yellow cap; seed label without demand-margin bridge |
| C31 | 002900 | TYM | 6,220 | +1.0% | -56.2% | hard 4C; farm-machinery label without order-margin bridge |

---

## 5. R10 review — regional housing, PF, presales, and trust

### 5.1 035890 서희건설

```text
entry_close: 1,405
peak_high: 1,621
MFE: +15.4%
worst_low_after_entry: 1,378
MAE: -1.9%
```

R13 interpretation:

```text
This was the constructive C30 regional-housing case.
The price path did not behave like a one-day policy spike.
Controlled MAE and gradual MFE support a capped positive.
```

Classification:

```text
positive_control = true
green_cap = true
pf_presale_backlog_bridge_required = true
```

This is the C30 "regional housing can work" case. But the model still needs company-specific PF exposure, presale quality, project cash collection, and margin trust before treating it as Green.

### 5.2 013120 동원개발

```text
entry_close: 3,100
peak_high: 3,140
MFE: +1.3%
worst_low_after_entry: 2,460
MAE: -20.6%
```

R13 interpretation:

```text
This is the stable regional-developer cap.
It did not implode, but it gave almost no upside and then accumulated drawdown.
```

Classification:

```text
watch_yellow_cap = true
actionable_block_without_pf_cashflow_bridge = true
```

The lesson is over-certainty. A stable regional developer is not automatically a PF-repair thesis.

### 5.3 017000 신원종합개발

```text
entry_close: 4,080
peak_high: 4,280
MFE: +4.9%
worst_low_after_entry: 2,710
MAE: -33.6%
```

R13 interpretation:

```text
This is the hard failure.
Small-builder policy or political beta created the spike, but no durable repair bridge followed.
```

Classification:

```text
hard_4c_candidate = true
small_builder_spike_guard = true
stage2_actionable_block = true
```

The model must not confuse small-builder heat with balance-sheet trust.

---

## 6. R11 review — Korea Value-up and holding-company NAV discount

### 6.1 402340 SK스퀘어

```text
entry_close: 67,300
peak_high: 96,200
MFE: +42.9%
worst_low_after_entry: 64,200
MAE: -4.6%
```

R13 interpretation:

```text
This is the cleanest Value-up positive in this holdout set.
The policy label was paired with NAV discount, asset-value readthrough, and strong price survival.
```

Classification:

```text
positive_control = true
valueup_nav_bridge_confirmed_by_price = true
green_possible_with_execution_evidence = true
```

This case proves C31 Value-up can work when policy pressure plausibly reaches company-specific NAV and shareholder-return economics.

### 6.2 001040 CJ

```text
entry_close: 94,300
peak_high: 140,600
MFE: +49.1%
worst_low_after_entry: 91,900
MAE: -2.5%
peak_to_later_low_drawdown: -29.1%
```

R13 interpretation:

```text
This was a good Value-up entry, but after the large MFE, it becomes a 4B discipline case.
The model should preserve the positive entry and block stale Green without fresh return evidence.
```

Classification:

```text
positive_control = true
local_4b_after_large_mfe = true
shareholder_return_refresh_required = true
```

The lesson is that a correct policy bridge still ages. After a large move, the model needs new buyback, cancellation, dividend, or asset-monetization evidence.

### 6.3 034730 SK

```text
entry_close: 190,200
peak_high: 199,900
MFE: +5.1%
worst_low_after_entry: 128,400
MAE: -32.5%
```

R13 interpretation:

```text
This is the holding-company false positive.
The label was strong, but the company-specific NAV-unlock and return bridge did not validate.
```

Classification:

```text
hard_4c_candidate = true
holding_company_label_false_positive = true
green_block_without_return_execution = true
```

The lesson is that holding-company relevance is not shareholder-return execution.

---

## 7. R12 review — food security, agri input, and order-margin conversion

### 7.1 008040 사조동아원

```text
entry_close: 1,009
peak_high: 1,188
MFE: +17.7%
worst_low_after_entry: 955
MAE: -5.4%
```

R13 interpretation:

```text
This is the constructive food-security/agri-input case.
The grain/feed/milling label produced useful MFE and controlled downside.
```

Classification:

```text
positive_control = true
capped_positive = true
spread_margin_bridge_required = true
```

This is not unlimited Green. It remains a capped positive unless input-cost pass-through, product spread, and margin conversion become explicit.

### 7.2 054050 농우바이오

```text
entry_close: 8,480
peak_high: 8,820
MFE: +4.0%
worst_low_after_entry: 6,990
MAE: -17.6%
```

R13 interpretation:

```text
This is the seed/agri-input Watch cap.
Food-security relevance was real enough for monitoring, but not enough for Actionable.
```

Classification:

```text
watch_yellow_cap = true
paid_demand_bridge_missing = true
```

The lesson is that seed relevance must become paid demand, channel sell-through, and margin.

### 7.3 002900 TYM

```text
entry_close: 6,220
peak_high: 6,280
MFE: +1.0%
worst_low_after_entry: 2,725
MAE: -56.2%
```

R13 interpretation:

```text
This is the hard agri-policy false positive.
Farm-machinery and productivity-policy labels did not become orders, shipments, or margin.
```

Classification:

```text
hard_4c_candidate = true
farm_machinery_policy_label_false_positive = true
order_margin_bridge_missing = true
```

The model must not promote mechanization policy relevance into Green without order and shipment evidence.

---

## 8. Cross-archetype guardrail

### Proposed R13 cross-rule

```text
R13_POLICY_LABEL_TO_COMPANY_BRIDGE_REQUIRED

For policy/event archetypes in construction, governance/value-up, and agri/service themes:

  Do not open Stage2-Actionable or Stage3-Green from policy label or event salience alone.

  First classify the event type:
    - balance-sheet / PF trust event
    - capital-market / Value-up NAV event
    - food-security / agri-demand event

  Then require the matching bridge:
    - C30: PF exposure, presales/backlog, project cash, debt maturity, margin trust
    - C31 Value-up: NAV discount path, shareholder return, buyback/cancellation/dividend, asset monetization
    - C31 agri: paid demand, order/shipment, input-cost pass-through, price spread, margin

  If MFE is shallow and MAE is large:
    route to hard 4C.

  If MFE is meaningful but the bridge is not refreshed:
    preserve as capped positive or local 4B, not Green.

  If MAE is controlled and bridge is plausible:
    allow capped Actionable but require execution evidence for Green.
```

### Quantitative trigger candidates

```text
hard_4c_policy_candidate:
  MFE < +10%
  AND MAE <= -30%
  AND company_specific_bridge_missing == true

watch_cap_policy_candidate:
  MFE < +5%
  AND MAE between -15% and -30%
  AND policy relevance exists
  AND company-specific bridge is weak

capped_positive_policy_candidate:
  MFE >= +15%
  AND MAE controlled
  AND event-company bridge plausible
  BUT Green bridge incomplete

local_4b_after_large_policy_mfe:
  MFE >= +40%
  AND no fresh execution evidence after peak
  OR peak_to_later_drawdown >= -25%

green_bridge_required:
  policy_event_type == true
  AND direct execution evidence missing
  -> block Stage3-Green
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"review_case","review_id":"R13_L93_C30_035890","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"035890","name":"서희건설","entry_date":"2024-08-20","entry_price":1405,"mfe_pct":15.4,"mae_pct":-1.9,"r13_verdict":"positive_capped_regional_housing_presale_backlog_price_survival_but_pf_cashflow_trust_bridge_required","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C30_013120","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"013120","name":"동원개발","entry_date":"2024-02-05","entry_price":3100,"mfe_pct":1.3,"mae_pct":-20.6,"r13_verdict":"watch_yellow_cap_regional_developer_policy_relief_without_pf_cashflow_repair_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C30_017000","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","symbol":"017000","name":"신원종합개발","entry_date":"2024-08-20","entry_price":4080,"mfe_pct":4.9,"mae_pct":-33.6,"r13_verdict":"hard_4c_small_builder_policy_relief_spike_without_repair_trust_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_402340","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"402340","name":"SK스퀘어","entry_date":"2024-02-26","entry_price":67300,"mfe_pct":42.9,"mae_pct":-4.6,"r13_verdict":"positive_valueup_nav_discount_shareholder_return_bridge_with_price_survival","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_001040","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"001040","name":"CJ","entry_date":"2024-02-26","entry_price":94300,"mfe_pct":49.1,"mae_pct":-2.5,"r13_verdict":"positive_diversified_holding_company_valueup_but_local_4b_after_large_mfe_without_fresh_return_execution","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_034730","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"034730","name":"SK","entry_date":"2024-02-26","entry_price":190200,"mfe_pct":5.1,"mae_pct":-32.5,"r13_verdict":"hard_4c_holding_company_valueup_label_without_nav_unlock_or_shareholder_return_execution","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_008040","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"008040","name":"사조동아원","entry_date":"2024-07-24","entry_price":1009,"mfe_pct":17.7,"mae_pct":-5.4,"r13_verdict":"positive_capped_food_security_grain_feed_milling_price_survival_but_margin_bridge_required","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_054050","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"054050","name":"농우바이오","entry_date":"2024-02-19","entry_price":8480,"mfe_pct":4.0,"mae_pct":-17.6,"r13_verdict":"watch_yellow_cap_seed_agri_input_policy_label_without_paid_demand_margin_bridge","do_not_count_as_new_case":true}
{"row_type":"review_case","review_id":"R13_L93_C31_002900","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","original_canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","symbol":"002900","name":"TYM","entry_date":"2024-01-12","entry_price":6220,"mfe_pct":1.0,"mae_pct":-56.2,"r13_verdict":"hard_4c_farm_machinery_policy_export_label_without_order_shipment_margin_bridge","do_not_count_as_new_case":true}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R13","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","review_trigger_count":9,"reviewed_original_canonical_count":2,"reviewed_original_canonical_ids":["C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","C31_POLICY_SUBSIDY_LEGISLATION_EVENT"],"reviewed_fine_branch_count":3,"new_independent_case_count":0,"do_not_count_as_new_case_count":9,"positive_control_count":4,"capped_positive_or_bridge_positive_count":4,"local_burst_or_4b_watch_count":2,"watch_yellow_cap_count":2,"stage2_false_positive_or_high_mae_count":5,"hard_4c_candidate_count":3,"trust_or_policy_bridge_case_count":9,"regional_housing_pf_case_count":3,"valueup_holding_company_case_count":3,"agri_food_security_policy_case_count":3,"loop_contribution_label":"holdout_validation_passed","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R13","scheduled_loop":93,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","rule_id":"R13_POLICY_LABEL_TO_COMPANY_BRIDGE_REQUIRED","rule_type":"cross_archetype_guardrail","rule_text":"For policy/event archetypes in construction, governance/value-up, and agri/service themes, do not open Stage2-Actionable or Stage3-Green from policy label or event salience alone. Classify the event as balance-sheet/PF trust, capital-market/Value-up NAV, or food-security/agri-demand. Require the matching company bridge: PF exposure/presales/project cash/margin trust for C30, NAV discount/shareholder return/asset monetization for C31 Value-up, and paid demand/order/spread/input-cost/margin for C31 agri. If MFE is shallow and MAE is large, route to hard 4C. If MFE is meaningful but execution evidence is not refreshed, preserve as capped positive or local 4B rather than Green. If MAE is controlled and the bridge is plausible, allow capped Actionable but require direct execution evidence for Green.","expected_effect":"Unifies policy/event guardrails so the model stops confusing policy salience with company-specific monetization, balance-sheet repair, shareholder return, or margin conversion.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R13","scheduled_loop":93,"canonical_archetype_id":"R13_CROSS_ARCHETYPE_4B_4C_REDTEAM","residual_type":"policy_label_to_company_bridge_guard","contribution":"Reviews nine prior loop93 cases without adding new independent evidence weight. Validates a shared policy/event guard across regional housing PF trust, Korea Value-up holding-company NAV/shareholder return, and food-security/agri policy demand-margin cases.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this R13 review file as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R13_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Mark all review_case rows as do_not_count_as_new_case=true.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a cross-archetype shadow guard:
   R13_POLICY_LABEL_TO_COMPANY_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Link review rows back to the original R10/R11/R12 loop93 files:
   - C30 regional housing / PF / small-builder relief
   - C31 Korea Value-up / holding-company NAV discount
   - C31 food-security / agri-input policy
7. If enough R13 reviews agree, consider implementing a pre-scoring check for policy/event archetypes:
   - classify the event type first,
   - identify the true company-level economic bridge,
   - block event-label-only Green,
   - route shallow-MFE/high-MAE to hard 4C,
   - keep meaningful-MFE but unrefreshed bridges as local 4B or capped positive,
   - allow capped positives only after explicit bridge evidence.

Expected next schedule:
completed_round = R13
completed_loop = 93
next_round = R1
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 11. Required round-state footer

```text
completed_round = R13
completed_loop = 93
next_round = R1
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
