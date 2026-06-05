# E2R Stock-Web v12 Residual Research — R11 / Loop 93

```yaml
scheduled_round: R11
scheduled_loop: 93
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE

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
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
holding_company_valueup_case_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 93
next_round: R12
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_93_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 93
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use:

```text
L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

unless the event is explicitly policy-defense-linked. This run is a Korea Corporate Value-up / capital-market policy / holding-company discount event family, so L10 is the correct large-sector gate.

Recent R11 branch usage:

```text
loop91: C31_POLICY_SUBSIDY_LEGISLATION_EVENT — AI semiconductor policy branch
loop92: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP — public tender / delisting cap branch
```

This run returns to C31 but uses a different fine branch:

```text
Korea Value-up / holding-company NAV discount / shareholder-return bridge
vs policy-label spike
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

Selected symbols:

```text
402340 SK스퀘어
001040 CJ
034730 SK
```

They avoid the C31 top-covered symbols and avoid recent R11/R12 policy names:

```text
R11 loop91 avoid: 000660, 005930, 000990
R11 loop92 avoid: 003410, 115390, 119860
R12 loop92 avoid: 133750, 053290, 215200
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
402340: same archetype, new symbol, holding-company NAV discount / shareholder-return policy positive
001040: same archetype, new symbol, diversified holding-company value-up positive with 4B watch
034730: same archetype, new symbol, holding-company value-up label without durable NAV/return bridge
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
402340 SK스퀘어
  profile: atlas/symbol_profiles/402/402340.json
  first_date: 2021-11-29
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,034
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

001040 CJ
  profile: atlas/symbol_profiles/001/001040.json
  name history:
    제일제당 until 2002-11-01
    CJ from 2002-11-04
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,745
  corporate_action_candidate_dates:
    1998-06-30, 1999-01-29, 2007-09-28, 2008-01-22
  2024 entry~D+180 contamination: none

034730 SK
  profile: atlas/symbol_profiles/034/034730.json
  name history:
    SK C&C until 2015-08-13
    SK from 2015-08-17
  first_date: 2009-11-11
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,007
  corporate_action_candidate_dates:
    2015-08-17
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-02-26
Korea Corporate Value-up / capital-market reform / low-PBR and holding-company discount policy focus.
```

This is C31 because the investment question is a policy-to-company bridge:

```text
policy headline
  -> corporate action incentive
  -> shareholder-return or governance execution
  -> NAV-discount narrowing
  -> price survival
```

The model can over-score:

```text
Korea Value-up policy
low-PBR label
holding-company discount
NAV discount
shareholder-return expectation
governance reform label
one-week policy rally
```

The C31 bridge must be stricter:

```text
policy event
  -> company-specific balance-sheet or NAV unlock
  -> buyback / cancellation / dividend / capital-allocation evidence
  -> listed-subsidiary value or asset monetization bridge
  -> governance execution
  -> price survival after the first policy spike
```

A Value-up policy headline is a key placed on the table. C31 asks whether this company actually turns the key in its own lock: cancels shares, returns cash, monetizes assets, or narrows NAV discount.

---

## 5. Case 1 — 402340 SK스퀘어

```yaml
case_id: C31_R11L93_402340_2024_02_26
symbol: "402340"
name: "SK스퀘어"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 67300
classification: positive_holding_company_nav_discount_valueup_shareholder_return_bridge
calibration_usable: true
```

### Evidence interpretation

SK스퀘어 is the cleanest holding-company value-up positive in this set.

The useful C31 read is not simply:

```text
low-PBR / holding-company label
```

It is:

```text
holding-company NAV discount
  -> listed-subsidiary / asset value readthrough
  -> capital-allocation or shareholder-return optionality
  -> repeated price confirmation after the policy event
```

The forward path showed controlled MAE and later much higher highs. This is what a real policy-to-company bridge should look like.

### Price path

Key Stock-Web rows:

```text
2024-02-26: close 67,300
2024-02-27: low 64,200 / close 65,300
2024-03-22: high 81,000 / close 80,000
2024-04-24: high 86,500 / close 85,500
2024-08-05: low 67,900 / close 70,400
2024-09-26: high 86,300 / close 85,500
2024-10-25: high 96,200 / close 95,500
```

Approximate path from entry close:

```text
entry_close: 67,300
peak_high: 96,200
MFE: +42.9%
worst_low_after_entry: 64,200
MAE: -4.6%
```

### Interpretation

This is a C31 positive:

```text
Stage2-Actionable: valid if NAV-discount and shareholder-return bridge are explicit.
Stage3-Green: possible only with actual capital-allocation execution and price survival.
Local 4B: monitor after +40% MFE, but controlled MAE supports positive classification.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  holding_company_nav_discount_bridge: high
  shareholder_return_bridge: medium_high
  asset_value_readthrough: high
  price_confirmation: high
  drawdown_penalty: low
```

---

## 6. Case 2 — 001040 CJ

```yaml
case_id: C31_R11L93_001040_2024_02_26
symbol: "001040"
name: "CJ"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 94300
classification: positive_diversified_holding_company_valueup_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

CJ is the diversified holding-company positive with 4B watch.

The useful bridge is:

```text
holding-company discount
  -> listed/non-listed asset value
  -> policy-driven shareholder-return expectation
  -> NAV discount compression
  -> price confirmation
```

The stock rallied strongly after the value-up window. However, the later path pulled back materially from the peak. This is still positive from the entry, but it needs 4B after the extended move unless new shareholder-return or asset-monetization evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-26: close 94,300
2024-02-28: low 91,900 / close 95,000
2024-03-15: high 109,200 / close 109,200
2024-03-29: high 132,800 / close 129,800
2024-05-08: high 140,600 / close 133,400
2024-08-05: low 108,600 / close 110,400
2024-10-31: low 99,700 / close 102,800
```

Approximate path from entry close:

```text
entry_close: 94,300
peak_high: 140,600
MFE: +49.1%
worst_low_after_entry: 91,900
MAE: -2.5%
peak_to_later_low_drawdown: -29.1%
```

### Interpretation

This is a C31 positive with 4B watch:

```text
Stage2-Actionable: valid if NAV discount and shareholder-return bridge are explicit.
Stage3-Green: possible only with execution evidence.
Local 4B: required after +49% MFE and later peak-to-trough drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  diversified_holding_company_discount_bridge: high
  shareholder_return_execution_visibility: medium
  asset_monetization_bridge: medium
  price_confirmation: very_high
  post_peak_drawdown_penalty: medium_high
  local_4b_overlay: required_after_large_mfe
```

---

## 7. Case 3 — 034730 SK

```yaml
case_id: C31_R11L93_034730_2024_02_26
symbol: "034730"
name: "SK"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 190200
classification: hard_4c_candidate_holding_company_valueup_label_without_durable_nav_return_bridge
calibration_usable: true
```

### Evidence interpretation

SK is the holding-company value-up false-positive.

The company has obvious holding-company and governance relevance. That is exactly why this is a useful guardrail. The model can over-score:

```text
large holding company
low-PBR / NAV-discount label
Korea Value-up policy relevance
shareholder-return expectation
```

But the forward path did not validate an actionable policy-to-company bridge from the 2024-02-26 trigger. The MFE was shallow and the later MAE was large.

### Price path

Key Stock-Web rows:

```text
2024-02-26: high 199,900 / close 190,200
2024-02-28: high 195,800 / close 193,600
2024-02-29: high 196,700 / close 191,800
2024-03-29: low 178,300 / close 178,600
2024-04-19: low 153,400 / close 155,500
2024-08-05: low 128,400 / close 131,300
2024-09-20: high 156,700 / close 154,000
```

Approximate path from entry close:

```text
entry_close: 190,200
peak_high: 199,900
MFE: +5.1%
worst_low_after_entry: 128,400
MAE: -32.5%
```

### Interpretation

This is a hard C31 false-positive:

```text
Stage2-Watch: valid from holding-company / value-up policy relevance.
Stage2-Actionable: blocked unless specific shareholder-return, asset-monetization, or NAV-unlock bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and large MAE.
```

The lesson is that holding-company relevance is not shareholder-return execution.

### Stress-test components

```text
raw_component_score_proxy:
  holding_company_label: high
  valueup_policy_relevance: high
  direct_nav_unlock_bridge: weak
  shareholder_return_execution: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
holding_company_valueup_case_count: 3
calibration_usable_trigger_count: 3
```

The three-case C31 value-up / holding-company grid:

```text
402340 SK스퀘어:
  NAV discount / asset readthrough / shareholder-return positive;
  controlled MAE and strong later MFE.

001040 CJ:
  diversified holding-company value-up positive;
  strong MFE, but later peak drawdown requires local 4B after the move.

034730 SK:
  holding-company label failed from the policy trigger;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C31 Value-up is not "holding-company label."
C31 Value-up is "policy pressure converts into actual capital allocation, shareholder return, asset monetization, NAV discount compression, and price survival."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R11L93_402340_2024_02_26","scheduled_round":"R11","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"402340","name":"SK스퀘어","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":67300,"peak_high":96200,"peak_date":"2024-10-25","worst_low_after_entry":64200,"worst_low_after_entry_date":"2024-02-27","mfe_pct":42.9,"mae_pct":-4.6,"classification":"positive_holding_company_nav_discount_valueup_shareholder_return_bridge","calibration_usable":true,"evidence_family":"korea_valueup_holding_company_nav_discount_asset_value_shareholder_return_bridge","residual_error":"none_for_actionable_if_nav_discount_and_shareholder_return_bridge_explicit","shadow_rule_candidate":"preserve_valueup_positive_when_nav_discount_asset_value_and_price_survival_confirm"}
{"row_type":"case","case_id":"C31_R11L93_001040_2024_02_26","scheduled_round":"R11","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"001040","name":"CJ","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":94300,"peak_high":140600,"peak_date":"2024-05-08","worst_low_after_entry":91900,"worst_low_after_entry_date":"2024-02-28","mfe_pct":49.1,"mae_pct":-2.5,"peak_to_later_low_drawdown_pct":-29.1,"classification":"positive_diversified_holding_company_valueup_with_4b_watch","calibration_usable":true,"evidence_family":"diversified_holding_company_valueup_nav_discount_asset_monetization_shareholder_return_bridge","residual_error":"positive_valueup_move_requires_4b_after_large_mfe_without_fresh_return_execution","shadow_rule_candidate":"allow_actionable_when_nav_discount_shareholder_return_bridge_confirms_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C31_R11L93_034730_2024_02_26","scheduled_round":"R11","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE","symbol":"034730","name":"SK","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":190200,"peak_high":199900,"peak_date":"2024-02-26","worst_low_after_entry":128400,"worst_low_after_entry_date":"2024-08-05","mfe_pct":5.1,"mae_pct":-32.5,"classification":"hard_4c_candidate_holding_company_valueup_label_without_durable_nav_return_bridge","calibration_usable":true,"evidence_family":"large_holding_company_valueup_label_without_company_specific_nav_unlock_or_return_execution","residual_error":"holding_company_policy_relevance_can_overpromote_without_direct_shareholder_return_execution","shadow_rule_candidate":"route_holding_company_valueup_label_to_hard_4c_if_mfe_shallow_mae_large_and_nav_return_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":93,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUEUP_HOLDING_COMPANY_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_VS_POLICY_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"holding_company_valueup_case_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":93,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_VALUEUP_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 Korea Value-up and holding-company events, do not open Stage2-Actionable or Stage3-Green from value-up policy, low-PBR, holding-company label, NAV discount, governance reform, or one-week policy rally alone. Require company-specific NAV discount compression path, shareholder-return execution, buyback/cancellation/dividend evidence, asset monetization or listed-subsidiary value bridge, governance execution, and post-trigger price survival. Holding-company positives with controlled MAE may be Actionable when NAV and return bridge are explicit. Large MFE should attach local 4B unless fresh return-execution evidence appears. Holding-company labels with shallow MFE and high MAE should route to hard-4C when NAV-unlock and capital-return bridge are missing.","expected_effect":"Preserve true Korea Value-up positives with NAV/shareholder-return evidence while reducing holding-company label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":93,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"valueup_holding_company_nav_discount_shareholder_return_guard","contribution":"Adds two holding-company Value-up positives and one holding-company label hard-4C counterexample to calibrate C31 NAV-discount and shareholder-return bridge requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_VALUEUP_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [korea_valueup, capital_market_reform, holding_company_discount, governance_policy]:

  Do not open Stage3-Green from:
    - Korea Value-up policy headline alone
    - low-PBR label alone
    - holding-company label alone
    - NAV discount label alone
    - governance reform label alone
    - one-week policy-rally price spike alone

  Require at least two of:
    - company-specific NAV discount compression path
    - explicit buyback / cancellation / dividend / capital-return execution
    - listed-subsidiary or asset-value bridge
    - asset monetization or capital allocation improvement
    - governance execution
    - low-MAE post-trigger price survival
    - fresh evidence after the policy headline

  If MFE < 10% and MAE < -30%:
    route to C31 hard-4C candidate.

  If MFE > 40% but the bridge is not refreshed:
    preserve positive classification but attach local 4B.

  If holding-company label is strong but capital-return execution is weak:
    cap at Watch/Yellow or hard-4C depending on price survival.

  Distinguish:
    - holding companies where NAV/asset value and return execution are visible
    - from large holding-company labels where policy relevance does not become shareholder-return execution.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_93_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 Korea Value-up / holding-company NAV-discount cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_VALUEUP_NAV_DISCOUNT_SHAREHOLDER_RETURN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 value-up cases agree, consider implementing a canonical guard that:
   - blocks Value-up/holding-company Green without NAV-discount and shareholder-return execution bridge,
   - preserves holding-company positives only with price survival and capital-allocation evidence,
   - attaches local 4B after large MFE,
   - routes shallow-MFE/high-MAE holding-company labels to hard-4C.

Expected next schedule:
completed_round = R11
completed_loop = 93
next_round = R12
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 93
next_round = R12
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
