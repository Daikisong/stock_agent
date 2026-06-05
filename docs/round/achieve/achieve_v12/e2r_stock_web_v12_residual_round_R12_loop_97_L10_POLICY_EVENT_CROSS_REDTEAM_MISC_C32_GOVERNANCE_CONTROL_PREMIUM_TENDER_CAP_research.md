# E2R Stock-Web v12 Residual Research — R12 / Loop 97

```yaml
scheduled_round: R12
scheduled_loop: 97
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE

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
control_premium_discount_case_count: 3
capital_allocation_execution_case_count: 1
ordinary_low_pbr_governance_label_case_count: 2
governance_discount_bridge_missing_count: 2
event_window_or_execution_evidence_missing_count: 2
old_corporate_action_caveat_outside_window_count: 3
row_presence_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 97
next_round: R13
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 97
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy / event / governance / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

Selected fine branch:

```text
holding company / governance discount / Korea Value-up / control-premium optionality
capital allocation, buyback/cancellation, asset-sale, restructuring, minority protection,
event-window execution, and price-survival bridge
vs generic governance-discount or holding-company label spike
```

This deliberately avoids:
- C32 top-covered names:
  `010130`, `036560`, `000150`, `041510`, `241560`, `000990`
- R11 loop96 C32 tender / governance branch:
  `119860`, `115390`, `008930`
- R11 loop97 C31 environmental-policy branch:
  `029960`, `067900`, `009440`
- R12 loop96 C31 low-birthrate branch:
  `407400`, `159580`, `014100`

Selected symbols:

```text
028260 삼성물산
034730 SK
000880 한화
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

The selected symbols avoid the C32 top-covered list and the recent R11/R12 L10 outputs. The hard duplicate key is:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
028260: same archetype, new symbol, holding-company governance discount / Value-up local positive with 4B after later evidence decay
034730: same archetype, new symbol, holding-company / governance discount hard-4C after shallow MFE and high MAE
000880: same archetype, new symbol, holding-company / defense-chemical conglomerate Watch cap without concrete capital-allocation execution bridge
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
028260 삼성물산
  profile: atlas/symbol_profiles/028/028260.json
  name history:
    제일모직 until 2015-09-14
    삼성물산 from 2015-09-15
  first_date: 2014-12-18
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,741
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2015-09-15
  2024 entry~D+180 contamination: none
  caveat:
    historical merger/name-transition candidate is outside the selected 2024 validation window.

034730 SK
  profile: atlas/symbol_profiles/034/034730.json
  name history:
    SK C&C until 2015-08-13
    SK from 2015-08-17
  first_date: 2009-11-11
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,007
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2015-08-17
  2024 entry~D+180 contamination: none
  caveat:
    old merger/name-transition candidate is outside selected 2024 validation window.
    Also appears in prior cross-archetype false-positive review universe, so classification should be strict.

000880 한화
  profile: atlas/symbol_profiles/000/000880.json
  name history:
    한화 plus old formatted name "한    화"
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,763
  non_tradable_zero_volume rows: 1
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1996-01-03, 1999-01-04, 1999-07-16
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / row-presence caveat exists outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C32 is about governance, control premium, tender offers, minority exit, and event-risk caps. This R12 fine branch extends the same discipline to holding-company discount and Value-up situations. It is not a generic "지주사 discount is cheap" or "governance reform may happen" archetype.

The model can over-score:

```text
holding company discount label
Korea Value-up policy headline
governance reform expectation
asset-sale or restructuring rumor
buyback / cancellation headline without execution
control-premium optionality
family succession or group restructuring narrative
one-week holding-company volume spike
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
  -> liquidity / tradeability trust
  -> price survival inside the event window
```

A C32 holding-company thesis is like a locked holding-company vault. The market sees assets inside the vault, but equity value appears only when the key is real: buybacks are cancelled, capital is returned, assets are sold or restructured, control math is clear, and minority shareholders can actually receive value rather than just hear the lock rattle.

---

## 5. Case 1 — 028260 삼성물산

```yaml
case_id: C32_R12L97_028260_2024_02_01
symbol: "028260"
name: "삼성물산"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 148700
classification: local_positive_holding_company_valueup_discount_compression_with_4b_after_later_evidence_decay
calibration_usable: true
```

### Evidence interpretation

삼성물산 is the constructive but capped C32 holding-company case.

The useful C32 read is not simply:

```text
지주사 / 저PBR / Value-up 수혜주가 강하다
```

It is:

```text
holding-company discount compression
  -> group-level governance and capital-allocation salience
  -> buyback/cancellation or shareholder-return expectation
  -> early price confirmation
  -> later evidence-decay and 4B requirement
```

The forward path delivered meaningful MFE in February and March. But the later path decayed materially into the fourth quarter. That makes this a local positive or capped positive, not an unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 148,800 / close 148,700
2024-02-19: high 171,700 / close 170,400
2024-03-14: high 170,800 / close 170,800
2024-04-17: low 137,300 / close 138,800
2024-08-05: low 132,800 / close 135,300
2024-10-31: low 117,000 / close 117,000
2024-12-20: low 114,500 / close 116,900
2024-12-30: low 114,800 / close 114,800
```

Approximate path from entry close:

```text
entry_close: 148,700
peak_high: 171,700
MFE: +15.5%
worst_low_after_entry: 114,500
MAE: -23.0%
```

### Interpretation

This is a C32 local positive with 4B:

```text
Stage2-Actionable: possible if capital allocation, cancellation, asset sale, restructuring, or shareholder-return execution is explicit.
Stage3-Green: blocked without fresh execution evidence after the rerating.
Local 4B: required after MFE and later material MAE.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_discount_relevance: high
  valueup_governance_salience: high
  capital_allocation_bridge: medium
  buyback_cancellation_execution_bridge: weak_to_medium
  minority_value_bridge: medium
  price_confirmation: medium_high_initial
  later_price_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 034730 SK

```yaml
case_id: C32_R12L97_034730_2024_02_01
symbol: "034730"
name: "SK"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 197000
classification: hard_4c_candidate_holding_company_valueup_governance_discount_label_without_capital_allocation_execution_survival
calibration_usable: true
```

### Evidence interpretation

SK is the hard C32 guardrail.

The label can fool the model:

```text
holding company discount
Korea Value-up / governance reform expectation
asset-portfolio restructuring optionality
control premium or capital-allocation narrative
```

But from the selected February trigger, the forward path produced only shallow MFE before a large drawdown. The bridge from governance-discount label to binding capital allocation, asset sale, cancellation, minority return, or event execution was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 198,300 / close 197,000
2024-02-19: high 209,500 / close 207,500
2024-02-23: high 212,000 / close 204,000
2024-04-17: low 156,400 / close 157,000
2024-08-05: low 128,400 / close 131,300
2024-12-09: low 127,600 / close 127,600
2024-12-30: low 131,500 / close 131,500
```

Approximate path from entry close:

```text
entry_close: 197,000
peak_high: 212,000
MFE: +7.6%
worst_low_after_entry: 127,600
MAE: -35.2%
```

### Interpretation

This is a hard C32 false-positive candidate:

```text
Stage2-Watch: possible from holding-company and governance-discount relevance.
Stage2-Actionable: blocked unless concrete capital allocation, asset-sale, buyback/cancellation, or control event mechanics are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -35%+ MAE.
```

The lesson is that a holding-company discount can remain a locked vault when execution is missing.

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_discount_label: high
  valueup_policy_salience: high
  capital_allocation_execution_bridge: weak
  asset_sale_restructuring_bridge: weak_to_medium
  minority_return_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 000880 한화

```yaml
case_id: C32_R12L97_000880_2024_02_01
symbol: "000880"
name: "한화"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 30000
classification: watch_cap_group_holding_company_valueup_defense_chemical_conglomerate_label_without_concrete_capital_allocation_bridge
calibration_usable: true
```

### Evidence interpretation

한화 is the Watch/Yellow cap case.

The setup has real C32 relevance:

```text
group holding / conglomerate discount
defense, chemical, energy, and finance portfolio optionality
Value-up and capital-allocation expectation
```

But the selected February entry did not validate Actionable/Green. MFE was shallow and the drawdown was material. The stock later had isolated event-like spikes, but the path did not show a durable governance/capital-allocation execution bridge from the first trigger.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 30,750 / close 30,000
2024-02-02: high 32,200 / close 31,100
2024-04-03: high 31,950 / close 28,650
2024-04-17: low 25,850 / close 25,850
2024-07-31: high 32,150 / close 31,200
2024-08-05: low 27,800 / close 28,450
2024-11-06: low 26,200 / close 27,000
2024-12-09: low 26,000 / close 26,300
```

Approximate path from entry close:

```text
entry_close: 30,000
peak_high: 32,200
MFE: +7.3%
worst_low_after_entry: 25,850
MAE: -13.8%
```

The later 26,000 low is also material, but the April 17 low is the first worst low after entry.

### Interpretation

This is a Watch/Yellow cap:

```text
Stage2-Watch: valid from group-holding and capital-allocation relevance.
Stage2-Actionable: blocked unless buyback/cancellation, asset sale, restructuring, capital return, or binding control event is explicit.
Stage3-Green: blocked.
Hard 4C: no, because MAE does not cross the hard threshold.
Old raw/corporate-action caveat: outside 2024 validation window.
```

The lesson is that a diversified group discount is not capital-allocation execution.

### Stress-test components

```text
raw_component_score_proxy:
  holding_conglomerate_relevance: high
  valueup_policy_label: medium_high
  defense_chemical_portfolio_confound: medium
  capital_allocation_bridge: weak
  shareholder_return_execution_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
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
control_premium_discount_case_count: 3
capital_allocation_execution_case_count: 1
ordinary_low_pbr_governance_label_case_count: 2
governance_discount_bridge_missing_count: 2
event_window_or_execution_evidence_missing_count: 2
old_corporate_action_caveat_outside_window_count: 3
row_presence_or_name_history_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C32 holding-company governance grid:

```text
028260 삼성물산:
  holding-company / Value-up local positive;
  meaningful MFE first, later material MAE, local 4B required.

034730 SK:
  holding-company / governance-discount label failed;
  shallow MFE and high MAE, hard 4C candidate.

000880 한화:
  conglomerate holding / capital-allocation relevance;
  shallow MFE and material but non-hard MAE, Watch/Yellow cap.
```

Shared rule:

```text
C32 is not "holding-company discount is cheap."
C32 is "capital allocation, buyback cancellation, asset sale, restructuring mechanics, control math, minority protection, and execution timing are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R12L97_028260_2024_02_01","scheduled_round":"R12","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"028260","name":"삼성물산","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":148700,"peak_high":171700,"peak_date":"2024-02-19","worst_low_after_entry":114500,"worst_low_after_entry_date":"2024-12-20","mfe_pct":15.5,"mae_pct":-23.0,"classification":"local_positive_holding_company_valueup_discount_compression_with_4b_after_later_evidence_decay","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"holding_company_valueup_discount_compression_capital_allocation_shareholder_return_execution_bridge","residual_error":"holding_company_valueup_positive_requires_4b_after_material_mae_without_refreshed_capital_allocation_execution_evidence","shadow_rule_candidate":"preserve_holding_company_valueup_local_positive_but_attach_4b_when_capital_allocation_evidence_decays"}
{"row_type":"case","case_id":"C32_R12L97_034730_2024_02_01","scheduled_round":"R12","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"034730","name":"SK","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":197000,"peak_high":212000,"peak_date":"2024-02-23","worst_low_after_entry":127600,"worst_low_after_entry_date":"2024-12-09","mfe_pct":7.6,"mae_pct":-35.2,"classification":"hard_4c_candidate_holding_company_valueup_governance_discount_label_without_capital_allocation_execution_survival","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"holding_company_governance_discount_label_without_binding_capital_allocation_asset_sale_minority_return_bridge","residual_error":"holding_company_governance_discount_label_can_fail_when_capital_allocation_execution_bridge_missing","shadow_rule_candidate":"route_holding_company_valueup_label_to_hard_4c_if_mfe_shallow_mae_large_and_execution_bridge_missing"}
{"row_type":"case","case_id":"C32_R12L97_000880_2024_02_01","scheduled_round":"R12","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","symbol":"000880","name":"한화","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":30000,"peak_high":32200,"peak_date":"2024-02-02","worst_low_after_entry":25850,"worst_low_after_entry_date":"2024-04-17","mfe_pct":7.3,"mae_pct":-13.8,"classification":"watch_cap_group_holding_company_valueup_defense_chemical_conglomerate_label_without_concrete_capital_allocation_bridge","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"row_presence_or_name_history_caveat":true,"evidence_family":"group_holding_conglomerate_valueup_label_without_concrete_buyback_cancellation_asset_sale_capital_return_bridge","residual_error":"diversified_group_discount_can_overpromote_without_capital_allocation_execution_evidence","shadow_rule_candidate":"cap_group_holding_valueup_label_at_watch_yellow_if_mfe_shallow_and_execution_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":97,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"HOLDING_COMPANY_VALUEUP_CONTROL_PREMIUM_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_VS_GOVERNANCE_DISCOUNT_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"holding_company_valueup_case_count":3,"control_premium_discount_case_count":3,"capital_allocation_execution_case_count":1,"ordinary_low_pbr_governance_label_case_count":2,"governance_discount_bridge_missing_count":2,"event_window_or_execution_evidence_missing_count":2,"old_corporate_action_caveat_outside_window_count":3,"row_presence_or_name_history_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":97,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_HOLDING_COMPANY_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32 holding-company governance-discount and Value-up cases, do not open Stage2-Actionable or Stage3-Green from holding-company discount, Korea Value-up, governance reform expectation, asset-sale or restructuring rumor, buyback/dividend headline without execution, control-premium optionality, family-succession or group-restructuring narrative, or one-week holding-company volume spike alone. Require concrete capital-allocation action or binding governance event, buyback/cancellation/dividend/asset-sale/restructuring mechanics, control math and minority-protection path, board/shareholder approval, timing/financing/tax/regulatory risk check, NAV discount compression with execution evidence, downside if the event fails or delays, liquidity/tradeability trust, and price survival inside the event window. Holding-company positives with meaningful MFE followed by material MAE should remain local 4B unless capital-allocation evidence refreshes. Holding-company discount labels with shallow MFE and high MAE should route to hard-4C when execution bridge is missing. Diversified group-holding labels with shallow MFE should cap at Watch/Yellow without concrete buyback/cancellation/asset-sale/capital-return evidence.","expected_effect":"Preserve true governance/control-premium and capital-allocation positives while reducing generic holding-company discount, low-PBR Value-up, and group-restructuring false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":97,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"holding_company_capital_allocation_execution_guard","contribution":"Adds one holding-company Value-up local positive, one holding-company hard-4C, and one diversified group Watch cap to calibrate C32 capital allocation, buyback/cancellation, asset-sale, restructuring, control math, minority protection, event timing, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_HOLDING_COMPANY_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
AND governance_event_family in [holding_company_discount, valueup_governance, capital_allocation, control_premium, group_restructuring]:

  Do not open Stage3-Green from:
    - holding-company discount label alone
    - Korea Value-up policy headline alone
    - governance reform expectation alone
    - asset-sale / restructuring rumor alone
    - dividend or buyback headline without cancellation/execution alone
    - control-premium optionality alone
    - family-succession or group-restructuring narrative alone
    - one-week holding-company volume spike alone

  Require at least two of:
    - concrete capital-allocation action or binding governance event
    - buyback / cancellation / dividend / asset-sale / restructuring mechanics
    - control math and minority-protection path
    - board / shareholder approval path
    - timing / financing / tax / regulatory risk check
    - NAV discount compression with execution evidence
    - downside if event fails or gets delayed
    - liquidity / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the governance-discount headline

  If MFE < 10% and MAE < -30%:
    route to C32 hard-4C candidate.

  If MFE > 12% but later MAE is material:
    preserve as local 4B / capped positive, not Green, unless capital-allocation evidence appears.

  If MFE is shallow and bridge is holding-company label only:
    cap at Watch/Yellow.

  If later renewed event appears:
    create a new event window; do not retroactively validate a failed first trigger.

  Distinguish:
    - holding companies where discount becomes actual capital return, asset-sale, restructuring, or minority-value realization
    - from holding labels where the vault stays locked.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_97_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 holding-company governance / capital-allocation cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_HOLDING_COMPANY_CAPITAL_ALLOCATION_EXECUTION_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C32 holding-company cases agree, consider implementing a canonical guard that:
   - blocks holding-company / low-PBR / Value-up Green without concrete capital-allocation execution,
   - preserves holding-company positives only as capped positives or local 4B when execution evidence decays,
   - routes shallow-MFE/high-MAE governance-discount labels to hard-4C,
   - caps diversified group labels at Watch/Yellow without buyback/cancellation/asset-sale evidence,
   - applies old corporate-action, name-history, and row-presence trust caveats.

Expected next schedule:
completed_round = R12
completed_loop = 97
next_round = R13
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 97
next_round = R13
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
