# E2R Stock-Web v12 Residual Research — R12 / Loop 98

```yaml
scheduled_round: R12
scheduled_loop: 98
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
holding_company_valueup_case_count: 3
nav_discount_case_count: 3
capital_allocation_execution_case_count: 1
minority_value_realization_bridge_missing_count: 2
buyback_cancellation_asset_sale_bridge_missing_count: 2
low_liquidity_or_row_presence_caveat_count: 2
old_corporate_action_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 98
next_round: R13
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 98
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy / event / governance / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Selected fine branch:

```text
holding company / Korea Value-up / NAV discount / capital allocation execution
buyback, cancellation, dividend, asset sale, portfolio restructuring, control math,
minority protection, liquidity / row trust, and price-survival bridge
vs generic governance-discount / holding-company label spike
```

This deliberately avoids:
- C32 top-covered names:
  `010130`, `036560`, `000150`, `041510`, `241560`, `000990`
- R12 loop97 C32 holding-company branch:
  `028260`, `034730`, `000880`
- R11 loop98 C31 education-policy branch:
  `100220`, `053290`, `057030`
- R11 loop97 C31 environmental-policy branch:
  `029960`, `067900`, `009440`

Selected symbols:

```text
001040 CJ
003550 LG
003240 태광산업
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows: 41
symbols: 22
date_range: 2020-02-12~2024-10-31
good/bad S2: 16/12
4B/4C: 3/0
URL pending/proxy: 8/8
top covered symbols:
  010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
001040: same archetype, new symbol, holding-company / consumer-portfolio NAV discount positive with Green cap
003550: same archetype, new symbol, large holding-company Value-up local positive but 4B after evidence decay
003240: same archetype, new symbol, deep NAV-discount / governance label hard-4C after first trigger failed minority-value execution
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
001040 CJ
  profile: atlas/symbol_profiles/001/001040.json
  name history:
    제일제당 -> CJ
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,745
  non_tradable_zero_volume rows: 19
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1998-06-30, 1999-01-29, 2007-09-28, 2008-01-22
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / name-history caveats are outside selected 2024 validation window.

003550 LG
  profile: atlas/symbol_profiles/003/003550.json
  name history:
    엘지화학 -> LG화학 -> LGCI -> LG
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,689
  non_tradable_zero_volume rows: 75
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1999-04-23, 2001-04-25, 2001-09-20, 2002-01-02, 2003-03-11, 2004-08-05
  2024 entry~D+180 contamination: none
  caveat:
    old holding-company formation / raw-discontinuity windows are outside selected 2024 validation window.

003240 태광산업
  profile: atlas/symbol_profiles/003/003240.json
  first_date: 1995-05-06 in tradable profile
  raw_first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,608
  non_tradable_zero_volume rows: 157
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    high historical non-tradable zero-volume count and low-liquidity / row-trust caveat.
```

---

## 4. Archetype residual problem

C32 is about governance, control premium, tender offers, minority exit, and event-risk caps. This fine branch extends the same discipline to holding-company discount and Value-up situations. It is not a generic "holding company is cheap" or "NAV discount can narrow" archetype.

The model can over-score:

```text
holding company discount label
Korea Value-up policy headline
NAV discount or portfolio value story
asset-sale / restructuring rumor
buyback or dividend headline without cancellation/execution
control-premium optionality
family succession or group restructuring narrative
one-week holding-company volume spike
low-liquidity deep-value spike
```

The C32 bridge must be stricter:

```text
governance / holding-company / control-premium event
  -> concrete capital-allocation action or binding governance event
  -> buyback, cancellation, dividend, asset sale, or restructuring mechanics
  -> control math, minority protection, and board/shareholder approval path
  -> timing, financing, tax, and regulatory risk
  -> NAV discount compression with execution evidence
  -> downside if event fails or delays
  -> liquidity / tradeability / row trust
  -> price survival inside the event window
```

A C32 holding-company thesis is like a locked vault. The market may see assets inside, but equity value appears only when the key is real: buybacks are cancelled, capital is returned, assets are sold or restructured, control math is clear, and minority shareholders can actually receive value rather than just hear the lock rattle.

---

## 5. Case 1 — 001040 CJ

```yaml
case_id: C32_R12L98_001040_2024_02_01
symbol: "001040"
name: "CJ"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 100900
classification: positive_holding_company_consumer_portfolio_valueup_nav_discount_execution_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

CJ is the constructive C32 holding-company / NAV-discount control in this set.

The useful C32 read is not simply:

```text
지주사 / 저PBR / Value-up 수혜주가 강하다
```

It is:

```text
holding-company and consumer-portfolio discount compression
  -> portfolio asset-value salience
  -> shareholder-return / capital-allocation expectation
  -> strong March-May price confirmation
  -> Green cap after rerating because execution evidence must remain current
```

The forward path produced a strong MFE and did not enter hard-failure territory. This preserves positive classification. However, C32 Green still needs fresh evidence: concrete capital allocation, buyback/cancellation, asset sale, restructuring, dividend policy, minority-value realization, or binding governance mechanics.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 103,500 / close 100,900
2024-02-07: high 108,900 / close 108,600
2024-03-29: high 132,800 / close 129,800
2024-05-08: high 140,600 / close 133,400
2024-08-05: low 108,600 / close 110,400
2024-10-31: low 99,700 / close 102,800
```

Approximate path from entry close:

```text
entry_close: 100,900
peak_high: 140,600
MFE: +39.3%
worst_low_after_entry: 91,100
MAE: -9.7%
```

### Interpretation

This is a C32 positive with Green cap:

```text
Stage2-Actionable: possible if capital allocation, asset-sale, buyback/cancellation, dividend, or restructuring mechanics are explicit.
Stage3-Green: blocked without fresh execution evidence after large MFE.
Local 4B: monitor if NAV-discount price rerating outruns actual capital return.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_discount_relevance: high
  valueup_policy_salience: high
  portfolio_asset_value_bridge: medium_high
  capital_allocation_execution_bridge: medium
  minority_value_bridge: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 003550 LG

```yaml
case_id: C32_R12L98_003550_2024_02_01
symbol: "003550"
name: "LG"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 88100
classification: local_positive_holding_company_valueup_discount_compression_with_4b_after_execution_evidence_decay
calibration_usable: true
```

### Evidence interpretation

LG is the large holding-company local positive with 4B discipline.

The setup had real C32 relevance:

```text
large holding company
  -> NAV discount and Value-up readthrough
  -> dividend / buyback / capital-allocation expectation
  -> strong February price confirmation
```

But the move faded by spring and did not show durable price survival. The case should remain a local positive, not Green. C32 should require concrete execution mechanics, not just holding-company discount salience.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 93,700 / close 88,100
2024-02-19: high 103,600 / close 103,500
2024-04-18: low 73,900 / close 76,200
2024-08-05: low 77,400 / close 78,100
2024-10-25: low 74,900 / close 75,400
2024-11-01: low 73,600 / close 76,700
```

Approximate path from entry close:

```text
entry_close: 88,100
peak_high: 103,600
MFE: +17.6%
worst_low_after_entry: 73,600
MAE: -16.5%
```

### Interpretation

This is a C32 local positive / 4B case:

```text
Stage2-Watch: valid from holding-company and Value-up relevance.
Stage2-Actionable: possible only if capital allocation, cancellation, dividend, asset sale, or restructuring bridge is explicit.
Stage3-Green: blocked after later evidence decay and material MAE.
Local 4B: required.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_discount_label: high
  valueup_salience: high
  capital_allocation_execution_bridge: weak_to_medium
  nav_discount_bridge: medium
  minority_return_bridge: weak_to_medium
  price_confirmation: medium_initial
  later_evidence_decay: medium_high
  local_4b_overlay: required
```

---

## 7. Case 3 — 003240 태광산업

```yaml
case_id: C32_R12L98_003240_2024_02_01
symbol: "003240"
name: "태광산업"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 943000
classification: hard_4c_candidate_deep_nav_discount_governance_label_without_minority_value_execution_survival
calibration_usable: true
```

### Evidence interpretation

태광산업 is the hard C32 guardrail.

The label can fool the model:

```text
deep NAV-discount / holding-value label
governance reform expectation
control-premium optionality
low-liquidity value spike
asset-value realization hope
```

But from the selected February entry, the forward path produced only negligible MFE and then entered a severe drawdown. The bridge from deep-value governance label to binding capital allocation, asset sale, buyback/cancellation, tender, minority protection, or shareholder-value realization was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 950,000 / close 943,000
2024-02-06: low 774,000 / close 810,000
2024-02-27: low 713,000 / close 733,000
2024-04-17: low 621,000 / close 621,000
2024-08-05: low 510,000 / close 546,000
2024-09-24: high 647,000 / close 646,000
2024-11-05: high 673,000 / close 669,000
```

Approximate path from entry close:

```text
entry_close: 943,000
peak_high_after_entry: 950,000
MFE: +0.7%
worst_low_after_entry: 510,000
MAE: -45.9%
```

### Interpretation

This is a hard C32 false-positive candidate:

```text
Stage2-Watch: possible from deep NAV-discount and governance relevance.
Stage2-Actionable: blocked unless actual capital allocation, tender, cancellation, asset-sale, or minority-return mechanics are explicit.
Stage3-Green: blocked.
Hard 4C: yes by near-zero MFE and severe MAE.
Low-liquidity / row-trust caveat: yes.
```

The lesson is that a locked vault can stay locked even when the assets inside look valuable.

### Stress-test components

```text
raw_component_score_proxy:
  deep_nav_discount_label: high
  governance_reform_salience: medium_high
  capital_allocation_execution_bridge: weak
  minority_value_realization_bridge: weak
  tender_or_control_event_bridge: weak
  liquidity_row_trust_caveat: high
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
holding_company_valueup_case_count: 3
nav_discount_case_count: 3
capital_allocation_execution_case_count: 1
minority_value_realization_bridge_missing_count: 2
buyback_cancellation_asset_sale_bridge_missing_count: 2
low_liquidity_or_row_presence_caveat_count: 2
old_corporate_action_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C32 holding-company governance grid:

```text
001040 CJ:
  holding-company / consumer-portfolio Value-up positive;
  large MFE and controlled MAE, but Green requires fresh capital-allocation execution.

003550 LG:
  large holding-company Value-up local positive;
  meaningful MFE first, then evidence decay and material MAE, local 4B.

003240 태광산업:
  deep NAV-discount / governance label failed;
  near-zero MFE and severe MAE, hard 4C.
```

Shared rule:

```text
C32 is not "holding-company discount is cheap."
C32 is "capital allocation, cancellation, dividend, asset sale, restructuring mechanics, control math, minority protection, timing, approval, liquidity trust, and price survival are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R12L98_001040_2024_02_01","scheduled_round":"R12","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"001040","name":"CJ","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":100900,"peak_high":140600,"peak_date":"2024-05-08","worst_low_after_entry":91100,"worst_low_after_entry_date":"2024-03-13","mfe_pct":39.3,"mae_pct":-9.7,"classification":"positive_holding_company_consumer_portfolio_valueup_nav_discount_execution_bridge_with_green_cap","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"evidence_family":"holding_company_consumer_portfolio_valueup_nav_discount_capital_allocation_execution_bridge","residual_error":"positive_holding_company_valueup_path_requires_green_cap_after_large_mfe_without_refreshed_capital_allocation_execution_evidence","shadow_rule_candidate":"allow_capped_actionable_when_nav_discount_and_capital_allocation_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C32_R12L98_003550_2024_02_01","scheduled_round":"R12","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"003550","name":"LG","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":88100,"peak_high":103600,"peak_date":"2024-02-19","worst_low_after_entry":73600,"worst_low_after_entry_date":"2024-11-01","mfe_pct":17.6,"mae_pct":-16.5,"classification":"local_positive_holding_company_valueup_discount_compression_with_4b_after_execution_evidence_decay","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"row_presence_caveat":true,"evidence_family":"large_holding_company_valueup_nav_discount_label_without_sustained_capital_allocation_execution_bridge","residual_error":"holding_company_valueup_label_can_create_mfe_but_requires_4b_when_execution_evidence_decays","shadow_rule_candidate":"classify_meaningful_mfe_then_material_mae_holding_company_valueup_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C32_R12L98_003240_2024_02_01","scheduled_round":"R12","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"003240","name":"태광산업","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":943000,"peak_high":950000,"peak_date":"2024-02-01","worst_low_after_entry":510000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":0.7,"mae_pct":-45.9,"classification":"hard_4c_candidate_deep_nav_discount_governance_label_without_minority_value_execution_survival","calibration_usable":true,"low_liquidity_or_row_presence_caveat":true,"evidence_family":"deep_nav_discount_governance_label_without_capital_allocation_tender_asset_sale_minority_value_bridge","residual_error":"deep_nav_discount_governance_label_can_fail_when_vault_stays_locked_and_minority_value_execution_missing","shadow_rule_candidate":"route_deep_nav_discount_governance_label_to_hard_4c_if_mfe_near_zero_mae_severe_and_execution_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":98,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"holding_company_valueup_case_count":3,"nav_discount_case_count":3,"capital_allocation_execution_case_count":1,"minority_value_realization_bridge_missing_count":2,"buyback_cancellation_asset_sale_bridge_missing_count":2,"low_liquidity_or_row_presence_caveat_count":2,"old_corporate_action_or_name_history_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":98,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32 holding-company NAV-discount and governance/control-premium cases, do not open Stage2-Actionable or Stage3-Green from holding-company discount, Korea Value-up, NAV discount, portfolio-value story, asset-sale or restructuring rumor, buyback/dividend headline without cancellation or execution, control-premium optionality, family-succession or group-restructuring narrative, one-week holding-company volume spike, or low-liquidity deep-value spike alone. Require concrete capital-allocation action or binding governance event, buyback/cancellation/dividend/asset-sale/restructuring mechanics, control math, minority-protection and board/shareholder approval path, timing/financing/tax/regulatory risk check, NAV discount compression with execution evidence, downside if the event fails or delays, liquidity/tradeability/row trust, and post-trigger price survival. Holding-company positives with large MFE may be capped Actionable when capital-allocation bridge is explicit, but Green requires fresh execution evidence. Holding-company Value-up labels with meaningful MFE followed by material MAE should remain local 4B. Deep NAV-discount labels with near-zero MFE and severe MAE should route to hard-4C when minority-value execution is missing.","expected_effect":"Preserve true holding-company capital-allocation positives while reducing generic NAV-discount, Value-up, low-liquidity, and governance-label false positives where execution, minority protection, liquidity, and price survival fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":98,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"holding_nav_discount_capital_allocation_execution_trust_guard","contribution":"Adds one holding-company Value-up positive, one large holding-company local 4B, and one deep-NAV-discount hard-4C counterexample to calibrate C32 capital allocation, cancellation, asset-sale, restructuring, control math, minority protection, liquidity, row trust, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
AND governance_event_family in [holding_company_discount, nav_discount, valueup_governance, capital_allocation, control_premium, group_restructuring]:

  Do not open Stage3-Green from:
    - holding-company discount label alone
    - Korea Value-up policy headline alone
    - NAV discount or portfolio-value story alone
    - asset-sale / restructuring rumor alone
    - dividend or buyback headline without cancellation/execution alone
    - control-premium optionality alone
    - family-succession or group-restructuring narrative alone
    - one-week holding-company volume spike alone
    - low-liquidity deep-value spike alone

  Require at least two of:
    - concrete capital-allocation action or binding governance event
    - buyback / cancellation / dividend / asset-sale / restructuring mechanics
    - control math and minority-protection path
    - board / shareholder approval path
    - timing / financing / tax / regulatory risk check
    - NAV discount compression with execution evidence
    - downside if event fails or gets delayed
    - liquidity / tradeability / row trust
    - low-MAE post-trigger price survival
    - fresh evidence after the governance-discount headline

  If MFE < 5% and MAE <= -35%:
    route to C32 hard-4C candidate.

  If MFE > 15% but capital-allocation evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but later MAE is material:
    attach local 4B until execution evidence refreshes.

  If low-liquidity or row-trust caveat exists:
    cap Actionable/Green unless event mechanics and price survival are both clean.

  Distinguish:
    - holding companies where discount becomes actual capital return, asset-sale, restructuring, tender, or minority-value realization
    - from holding labels where the vault stays locked.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_98_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 holding-company NAV-discount / governance execution cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_EXECUTION_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C32 cases agree, consider implementing a canonical guard that:
   - blocks holding-company / NAV-discount / Value-up Green without capital allocation, cancellation, dividend, asset-sale, restructuring, control math, and minority-protection bridge,
   - preserves holding-company positives only with price survival and fresh execution evidence,
   - treats meaningful-MFE/material-MAE large holding-company labels as local 4B,
   - routes near-zero-MFE/severe-MAE deep NAV-discount labels to hard-4C,
   - applies low-liquidity, old corporate-action, name-history, and row-presence caveats.

Expected next schedule:
completed_round = R12
completed_loop = 98
next_round = R13
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 98
next_round = R13
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
