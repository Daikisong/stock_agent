# E2R Stock-Web v12 Residual Research — R12 / Loop 99

```yaml
scheduled_round: R12
scheduled_loop: 99
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE

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
old_corporate_action_or_name_history_caveat_count: 3
checked_but_not_used_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 99
next_round: R13
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 99
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy / event / governance / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Selected fine branch:

```text
holding company / NAV discount / Korea Value-up / capital allocation execution
buyback, cancellation, dividend, asset sale, portfolio restructuring, control math,
minority protection, timing, approval, liquidity, row trust, and price-survival bridge
vs generic holding-company / NAV-discount label spike
```

This deliberately avoids:
- C32 top-covered names:
  `010130`, `036560`, `000150`, `041510`, `241560`, `000990`
- R12 loop98 names:
  `001040`, `003550`, `003240`
- R12 loop97 names:
  `028260`, `034730`, `000880`
- R11 loop99 telemedicine branch:
  `032620`, `032850`, `099750`

Selected symbols:

```text
000070 삼양홀딩스
004990 롯데지주
006840 AK홀딩스
```

Checked but not used:

```text
078930 GS
  holding-company relevance is valid, but 2024 price path was weaker than the selected positive/control grid.
```

---

## 2. No-repeat / novelty check

No-Repeat Index snapshot for C32:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows: 55
guidance: 지배구조 premium, tender cap, minority risk 보강
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
000070: same archetype, new symbol, holding-company / food-chem-biopharma portfolio Value-up positive with Green cap.
004990: same archetype, new symbol, holding-company / consumer-retail NAV-discount local 4B / Watch cap after first policy spike failed execution survival.
006840: same archetype, new symbol, low-liquidity holding-company label hard-4C candidate after shallow MFE and hard-zone MAE.
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
000070 삼양홀딩스
  profile: atlas/symbol_profiles/000/000070.json
  name history:
    삼양사 / 삼 양 사 -> 삼양홀딩스
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,719
  non_tradable_zero_volume rows: 45
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1996-06-28, 2011-12-05, 2012-07-25
  2024 entry~D+180 contamination: none
  caveat:
    old name-history / raw-discontinuity / row-presence caveats are outside selected 2024 validation window.

004990 롯데지주
  profile: atlas/symbol_profiles/004/004990.json
  name history:
    롯데제과 -> 롯데지주
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,661
  non_tradable_zero_volume rows: 104
  corporate_action_candidate_dates:
    2016-05-17, 2017-10-30, 2018-04-13
  2024 entry~D+180 contamination: none
  caveat:
    old holding-company transition / raw-discontinuity and row-presence caveats are outside selected 2024 validation window.

006840 AK홀딩스
  profile: atlas/symbol_profiles/006/006840.json
  name history:
    애경유화 -> AK홀딩스
  first_date: 1999-08-11
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,528
  non_tradable_zero_volume rows: 12
  corporate_action_candidate_dates:
    2011-11-24, 2012-09-17, 2012-11-05, 2013-01-07
  2024 entry~D+180 contamination: none
  caveat:
    old name-history / holding-company transition / raw-discontinuity caveats are outside selected 2024 validation window.

Checked but not used:
078930 GS
  profile has no corporate-action candidate and clean row status.
  It was not used because this run needed a clearer positive / local-4B / hard-4C grid.
```

---

## 4. Archetype residual problem

C32 is about governance, control premium, tender offers, minority exit, and event-risk caps. In this holding-company branch, the model must not treat every NAV discount or Value-up label as executable shareholder value.

The model can over-score:

```text
holding-company discount label
Korea Value-up policy headline
NAV discount or portfolio-value story
asset-sale / restructuring rumor
buyback or dividend headline without cancellation / execution
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

A C32 holding-company thesis is like a locked vault. NAV discount shows assets through the glass, but equity value appears only when the lock opens: capital is returned, buybacks are cancelled, assets are sold or restructured, control math is clear, and minority shareholders can actually receive value.

---

## 5. Case 1 — 000070 삼양홀딩스

```yaml
case_id: C32_R12L99_000070_2024_02_01
symbol: "000070"
name: "삼양홀딩스"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 73700
classification: positive_holding_company_portfolio_valueup_nav_discount_execution_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

삼양홀딩스 is the constructive C32 control in this set.

The useful C32 read is not simply:

```text
지주사 / 저PBR / Value-up 수혜주가 강하다
```

It is:

```text
holding company with portfolio-value salience
  -> NAV discount compression
  -> capital-allocation / shareholder-return optionality
  -> strong September price confirmation
  -> Green cap because execution evidence must stay current
```

The forward path produced meaningful MFE and avoided hard drawdown. This is a C32 positive, but not an unrestricted Green. The score needs refreshed evidence of actual capital allocation, buyback cancellation, dividend mechanics, asset sale, restructuring, or minority-value delivery.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 73,900 / low 67,300 / close 73,700
2024-02-08: high 75,200 / close 74,000
2024-03-26: high 75,200 / close 73,700
2024-08-05: low 64,600 / close 65,800
2024-09-19: high 75,900 / close 75,900
2024-09-20: high 81,600 / close 81,500
2024-09-23: high 87,900 / close 86,900
2024-10-25: low 70,000 / close 70,000
```

Approximate path from entry close:

```text
entry_close: 73,700
peak_high: 87,900
MFE: +19.3%
worst_low_after_entry: 64,600
MAE: -12.3%
```

### Interpretation

This is a C32 positive with Green cap:

```text
Stage2-Actionable: possible if capital allocation, dividend, buyback/cancellation, asset-sale, restructuring, or minority-return bridge is explicit.
Stage3-Green: blocked unless execution evidence refreshes after the rerating.
Local 4B: monitor if portfolio-value price outruns shareholder-return mechanics.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_valueup_relevance: high
  nav_discount_bridge: medium_high
  capital_allocation_execution_bridge: medium
  minority_value_bridge: medium
  liquidity_row_trust: medium
  price_confirmation: medium_high
  drawdown_penalty: moderate
  green_cap: required
```

---

## 6. Case 2 — 004990 롯데지주

```yaml
case_id: C32_R12L99_004990_2024_02_01
symbol: "004990"
name: "롯데지주"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 31250
classification: local_4b_holding_company_consumer_retail_nav_discount_label_without_sustained_capital_allocation_execution
calibration_usable: true
```

### Evidence interpretation

롯데지주 is the local 4B / Watch case.

The setup had real C32 relevance:

```text
large holding company
  -> consumer / retail portfolio discount
  -> Korea Value-up and NAV compression readthrough
  -> early February policy-event spike
```

However, the initial rerating failed price survival. The bridge from holding-company discount to actual capital allocation, restructuring, asset-sale, dividend, cancellation, or minority-value delivery was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 33,000 / close 31,250
2024-02-08: high 33,700 / close 33,100
2024-02-13: high 33,750 / close 33,000
2024-04-17: low 24,950 / close 24,950
2024-08-05: low 22,450 / close 23,150
2024-09-03: high 25,400 / close 25,150
2024-11-05: low 23,150 / close 23,200
```

Approximate path from entry close:

```text
entry_close: 31,250
peak_high_first_phase: 33,750
MFE: +8.0%
worst_low_after_entry: 22,450
MAE: -28.2%
```

### Interpretation

This is a C32 local 4B / Watch cap:

```text
Stage2-Watch: valid from holding-company and NAV-discount relevance.
Stage2-Actionable: blocked unless capital-return / asset-sale / restructuring / cancellation evidence is explicit.
Stage3-Green: blocked.
Local 4B: required because first policy spike failed price survival.
Hard 4C: not primary because drawdown did not cross the stricter hard threshold, but stale entries should be penalized.
```

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_discount_label: high
  valueup_policy_salience: high
  capital_allocation_execution_bridge: weak
  restructuring_asset_sale_bridge: weak_to_medium
  minority_value_bridge: weak
  price_confirmation: shallow
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 006840 AK홀딩스

```yaml
case_id: C32_R12L99_006840_2024_02_01
symbol: "006840"
name: "AK홀딩스"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 17230
classification: hard_4c_candidate_low_liquidity_holding_company_valueup_label_without_minoriy_value_execution_survival
calibration_usable: true
```

### Evidence interpretation

AK홀딩스 is the hard C32 guardrail in this set.

The label can fool the model:

```text
holding company / low-PBR label
portfolio-value story
Korea Value-up sympathy
small-cap holding-company rerating hope
```

But from the selected February entry, the forward path produced shallow MFE and then crossed a hard drawdown zone by October. The bridge from holding label to actual capital allocation, buyback/cancellation, dividend, asset-sale, restructuring, or minority-value execution was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 17,460 / close 17,230
2024-02-06: high 17,800 / close 17,750
2024-02-19: high 18,030 / close 17,910
2024-08-05: low 12,500 / close 12,670
2024-09-12: high 13,330 / close 13,200
2024-10-25: low 12,100 / close 12,230
2024-10-28: low 12,000 / close 12,280
```

Approximate path from entry close:

```text
entry_close: 17,230
peak_high: 18,030
MFE: +4.6%
worst_low_after_entry: 12,000
MAE: -30.4%
```

### Interpretation

This is a hard C32 false-positive candidate:

```text
Stage2-Watch: possible from holding-company / low-PBR relevance.
Stage2-Actionable: blocked unless capital-allocation mechanics and minority-value delivery are explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes by shallow MFE and hard-zone MAE.
Liquidity / row-trust cap: yes.
```

The lesson is that a small holding-company discount can stay locked without actual execution.

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_low_pbr_label: high
  valueup_salience: medium_high
  capital_allocation_execution_bridge: weak
  minority_value_realization_bridge: weak
  liquidity_row_trust: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: hard_zone
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
old_corporate_action_or_name_history_caveat_count: 3
checked_but_not_used_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C32 holding-company grid:

```text
000070 삼양홀딩스:
  holding-company / portfolio-value Value-up positive;
  meaningful MFE and non-hard MAE, but Green requires fresh capital-allocation execution evidence.

004990 롯데지주:
  large holding-company NAV-discount local 4B / Watch;
  shallow MFE and high MAE, policy spike failed execution survival.

006840 AK홀딩스:
  low-liquidity holding-company / low-PBR label failed;
  shallow MFE and hard-zone MAE, hard 4C candidate.
```

Shared rule:

```text
C32 is not "holding-company NAV discount is cheap."
C32 is "capital allocation, cancellation, dividend, asset sale, restructuring, control math, minority protection, approval path, liquidity trust, and price survival are visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R12L99_000070_2024_02_01","scheduled_round":"R12","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE","symbol":"000070","name":"삼양홀딩스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":73700,"peak_high":87900,"peak_date":"2024-09-23","worst_low_after_entry":64600,"worst_low_after_entry_date":"2024-08-05","mfe_pct":19.3,"mae_pct":-12.3,"classification":"positive_holding_company_portfolio_valueup_nav_discount_execution_bridge_with_green_cap","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"row_presence_caveat":true,"evidence_family":"holding_company_portfolio_valueup_nav_discount_capital_allocation_shareholder_return_bridge","residual_error":"holding_company_valueup_positive_requires_green_cap_without_refreshed_capital_allocation_execution_evidence","shadow_rule_candidate":"allow_capped_actionable_when_nav_discount_and_capital_allocation_bridge_confirm_but_cap_green_without_fresh_execution_evidence"}
{"row_type":"case","case_id":"C32_R12L99_004990_2024_02_01","scheduled_round":"R12","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE","symbol":"004990","name":"롯데지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":31250,"peak_high_first_phase":33750,"peak_date":"2024-02-13","worst_low_after_entry":22450,"worst_low_after_entry_date":"2024-08-05","mfe_pct":8.0,"mae_pct":-28.2,"classification":"local_4b_holding_company_consumer_retail_nav_discount_label_without_sustained_capital_allocation_execution","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"row_presence_caveat":true,"evidence_family":"large_holding_company_consumer_retail_nav_discount_label_without_capital_allocation_asset_sale_restructuring_minority_value_bridge","residual_error":"holding_company_valueup_label_can_create_policy_spike_but_fail_when_capital_allocation_execution_bridge_missing","shadow_rule_candidate":"classify_shallow_mfe_high_mae_holding_company_nav_discount_cases_as_local_4b_watch_not_green"}
{"row_type":"case","case_id":"C32_R12L99_006840_2024_02_01","scheduled_round":"R12","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE","symbol":"006840","name":"AK홀딩스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":17230,"peak_high":18030,"peak_date":"2024-02-19","worst_low_after_entry":12000,"worst_low_after_entry_date":"2024-10-28","mfe_pct":4.6,"mae_pct":-30.4,"classification":"hard_4c_candidate_low_liquidity_holding_company_valueup_label_without_minoriy_value_execution_survival","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"liquidity_row_trust_caveat":true,"evidence_family":"low_liquidity_holding_company_low_pbr_label_without_capital_allocation_buyback_cancellation_asset_sale_minority_value_bridge","residual_error":"small_holding_company_valueup_label_can_fail_when_vault_stays_locked_and_minority_value_execution_missing","shadow_rule_candidate":"route_low_liquidity_holding_company_label_to_hard_4c_if_mfe_shallow_mae_hard_zone_and_execution_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":99,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_NAV_DISCOUNT_VALUEUP_CAPITAL_ALLOCATION_MINORity_RETURN_TRUST_BRIDGE_VS_HOLDING_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"holding_company_valueup_case_count":3,"nav_discount_case_count":3,"capital_allocation_execution_case_count":1,"minority_value_realization_bridge_missing_count":2,"buyback_cancellation_asset_sale_bridge_missing_count":2,"low_liquidity_or_row_presence_caveat_count":2,"old_corporate_action_or_name_history_caveat_count":3,"checked_but_not_used_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":99,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_MINORity_VALUE_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32 holding-company NAV-discount and governance/control-premium cases, do not open Stage2-Actionable or Stage3-Green from holding-company discount, Korea Value-up policy headline, NAV discount or portfolio-value story, asset-sale/restructuring rumor, dividend or buyback headline without cancellation/execution, control-premium optionality, family-succession or group-restructuring narrative, one-week holding-company volume spike, or low-liquidity deep-value spike alone. Require concrete capital-allocation action or binding governance event, buyback/cancellation/dividend/asset-sale/restructuring mechanics, control math and minority-protection path, board/shareholder approval path, timing/financing/tax/regulatory risk check, NAV discount compression with execution evidence, downside if the event fails or gets delayed, liquidity/tradeability/row trust, and post-trigger price survival. Holding-company positives with meaningful MFE may be capped Actionable when capital-allocation bridge is explicit, but Green requires fresh execution evidence. Holding-company NAV-discount labels with shallow MFE and high MAE should remain local 4B/Watch. Low-liquidity holding-company labels with shallow MFE and hard-zone MAE should route to hard-4C when minority-value execution is missing.","expected_effect":"Preserve true holding-company capital-allocation positives while reducing generic NAV-discount, Value-up, low-liquidity, and governance-label false positives where execution, minority protection, liquidity, and price survival fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"checked_not_used","scheduled_round":"R12","scheduled_loop":99,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","symbol":"078930","name":"GS","reason":"Profile and rows were checked, but 2024 path was less suitable than the selected positive / local-4B / hard-4C grid for this loop. Do not count as independent evidence.","do_not_count_as_global_weight_delta":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":99,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"holding_nav_discount_capital_allocation_minority_value_trust_guard","contribution":"Adds one holding-company Value-up positive, one large holding-company local 4B/Watch case, and one low-liquidity holding-company hard-4C counterexample to calibrate C32 capital allocation, buyback/cancellation, asset-sale/restructuring, control math, minority protection, liquidity, row trust, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_MINORity_VALUE_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
AND governance_event_family in [holding_company_discount, nav_discount, valueup_governance, capital_allocation, control_premium, group_restructuring]:

  Do not open Stage3-Green from:
    - holding-company discount label alone
    - Korea Value-up policy headline alone
    - NAV discount or portfolio-value story alone
    - asset-sale / restructuring rumor alone
    - dividend or buyback headline without cancellation / execution alone
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

  If MFE < 6% and MAE <= -30%:
    route to C32 hard-4C candidate.

  If MFE is shallow and MAE is material:
    cap at Watch/4B unless actual execution bridge appears.

  If MFE is meaningful but execution evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If low-liquidity or row-trust caveat exists:
    block Green unless event mechanics and price survival are both clean.

  Distinguish:
    - holding companies where discount becomes actual capital return, asset sale, restructuring, tender, or minority-value realization
    - from holding labels where the vault stays locked.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_99_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 holding-company NAV-discount / capital-allocation cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_HOLDING_NAV_DISCOUNT_CAPITAL_ALLOCATION_MINORity_VALUE_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. Do not count checked_not_used rows as independent evidence.
8. If enough C32 cases agree, consider implementing a canonical guard that:
   - blocks holding-company / NAV-discount / Value-up Green without capital allocation, cancellation, dividend, asset-sale, restructuring, control math, and minority-protection bridge,
   - preserves holding-company positives only with price survival and fresh execution evidence,
   - treats shallow-MFE/high-MAE large holding-company labels as local 4B/Watch,
   - routes shallow-MFE/hard-MAE low-liquidity holding labels to hard-4C,
   - applies old corporate-action, name-history, row-presence, low-liquidity, and tradeability caveats.

Expected next schedule:
completed_round = R12
completed_loop = 99
next_round = R13
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 99
next_round = R13
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
