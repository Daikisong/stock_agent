# E2R Stock-Web v12 Residual Research — R6 / Loop 92

```yaml
scheduled_round: R6
scheduled_loop: 92
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA

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
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 92
next_round: R7
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_92_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 92
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate requires:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Recent R6 branch usage already covered:

```text
loop88: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN — bank/value-up/capital-return bridge
loop89: C22_INSURANCE_RATE_CYCLE_RESERVE — insurance CSM/reserve/rate cycle
loop90: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN — securities/brokerage value-up bridge
loop91: C22_INSURANCE_RATE_CYCLE_RESERVE — insurance value-up late-entry bridge
```

This run returns to C21, but uses a different branch:

```text
card / regional bank / small securities value-up capital-return bridge
vs generic low-PBR financial beta
```

The purpose is not to repeat large-bank or brokerage cases. The goal is to distinguish:

```text
visible payout and ROE bridge
```

from:

```text
low-PBR financial label without fresh capital-return evidence.
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rows: 51
symbols: 19
date_range: 2021-08-06~2024-09-26
good/bad S2: 22/11
4B/4C: 7/0
URL pending/proxy: 11/14
top covered symbols:
  006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
```

Selected symbols:

```text
029780 삼성카드
175330 JB금융지주
030610 교보증권
```

They avoid the C21 top-covered names and the most recent R6 loop90 securities names:

```text
005940, 006800, 039490
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
029780: same archetype, new symbol, card-company dividend / stable payout bridge
175330: same archetype, new symbol, regional bank ROE / shareholder-return bridge with volatility
030610: same archetype, new symbol, small securities low-PBR label / weak capital-return bridge cap case
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
029780 삼성카드
  profile: atlas/symbol_profiles/029/029780.json
  first_date: 2007-06-27
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,598
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

175330 JB금융지주
  profile: atlas/symbol_profiles/175/175330.json
  first_date: 2013-07-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,089
  corporate_action_candidate_dates:
    2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26
  2024 entry~D+180 contamination: none

030610 교보증권
  profile: atlas/symbol_profiles/030/030610.json
  first_date: 1999-11-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,471
  corporate_action_candidate_dates:
    2020-07-09, 2023-09-20
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-02-26
Korea Corporate Value-up / low-PBR financial shareholder-return policy follow-through.
```

C21 is not:

```text
low PBR financial stock = Green
```

C21 is:

```text
ROE durability
  -> capital buffer
  -> payout / dividend / buyback visibility
  -> shareholder-return execution
  -> valuation rerating
  -> price survival
```

The model can over-score:

```text
low PBR
financial value-up
bank/securities/card label
dividend theme
one-week value-up spike
```

The bridge must be stricter:

```text
capital return headline
  -> company-specific payout capacity
  -> ROE quality
  -> capital adequacy
  -> credit cost or market-risk check
  -> dividend/buyback execution
  -> price survival after the policy spike
```

A low-PBR financial is like a locked safe. Value-up policy may put a spotlight on the safe, but the stock rerates only if the company can open it and hand cash back to shareholders.

---

## 5. Case 1 — 029780 삼성카드

```yaml
case_id: C21_R6L92_029780_2024_02_26
symbol: "029780"
name: "삼성카드"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 36200
classification: positive_card_company_dividend_capital_return_bridge
calibration_usable: true
```

### Evidence interpretation

삼성카드 is the clean card-company positive.

The useful C21 bridge is:

```text
stable consumer-finance earnings
  -> visible dividend capacity
  -> relatively clear payout identity
  -> controlled credit-cost risk
  -> low-PBR value-up rerating
```

The price path had controlled downside and later strong MFE. This supports C21 Actionable when payout capacity and ROE quality are explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-26: close 36,200
2024-03-22: high 41,450 / close 41,450
2024-04-11: low 35,050 / close 35,400
2024-07-31: high 42,200 / close 42,100
2024-08-23: high 44,950 / close 44,850
2024-08-29: high 46,000 / close 44,500
2024-09-25: low 40,250 / close 40,300
```

Approximate path from entry close:

```text
entry_close: 36,200
peak_high: 46,000
MFE: +27.1%
worst_low: 35,050
MAE: -3.2%
```

### Interpretation

This is a C21 positive:

```text
Stage2-Actionable: valid if dividend/payout bridge is explicit.
Stage3-Green: possible only with ROE durability and credit-cost check.
Local 4B: not required at entry, but monitor after MFE > 25%.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  payout_visibility: high
  roe_quality: medium_high
  credit_cost_risk: medium
  low_pbr_valueup_relevance: high
  price_confirmation: high
  drawdown_penalty: low
```

---

## 6. Case 2 — 175330 JB금융지주

```yaml
case_id: C21_R6L92_175330_2024_02_26
symbol: "175330"
name: "JB금융지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 13360
classification: positive_regional_bank_roe_payout_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

JB금융지주 is the regional-bank positive with more volatility.

The constructive C21 read is:

```text
regional bank ROE
  -> relatively explicit shareholder-return identity
  -> value-up rerating
  -> later price confirmation
```

However, the path had an early drawdown and then a strong rerating into autumn. This supports Actionable only if the ROE/payout bridge is present, and it requires 4B discipline after the extended move.

### Price path

Key Stock-Web rows:

```text
2024-02-26: close 13,360
2024-03-07: high 14,080 / close 14,010
2024-04-11: low 11,390 / close 12,180
2024-08-21: high 15,500 / close 15,400
2024-09-24: high 15,800 / close 15,560
2024-10-25: high 18,710 / close 18,290
2024-11-04: low 17,320 / close 17,760
```

Approximate path from entry close:

```text
entry_close: 13,360
peak_high: 18,710
MFE: +40.0%
worst_low: 11,390
MAE: -14.7%
```

### Interpretation

This is a positive with local 4B watch:

```text
Stage2-Actionable: valid if ROE and payout bridge are explicit.
Stage3-Green: requires capital adequacy, credit cost, and payout execution.
Local 4B: attach after +40% MFE because the move is value-up rerating plus policy beta.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  roe_quality: high
  payout_bridge: medium_high
  regional_credit_risk: medium_high
  price_confirmation: high
  early_drawdown_penalty: medium
  local_4b_overlay: required_after_extended_mfe
```

---

## 7. Case 3 — 030610 교보증권

```yaml
case_id: C21_R6L92_030610_2024_02_26
symbol: "030610"
name: "교보증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-26
entry_date: 2024-02-26
entry_price_basis: close
entry_price: 5220
classification: watch_cap_small_securities_low_pbr_label_without_strong_capital_return_bridge
calibration_usable: true
```

### Evidence interpretation

교보증권 is the cap case.

It is not a catastrophic failure, but it is a useful guardrail because the path did not justify C21 Green from the value-up label alone.

The model risk:

```text
low-PBR securities label
  -> value-up policy relevance
  -> model opens Actionable/Green
  -> no strong new capital-return or ROE bridge
  -> price only grinds, with shallow MFE
```

### Price path

Key Stock-Web rows:

```text
2024-02-26: close 5,220
2024-03-22: high 5,420 / close 5,400
2024-04-15: low 4,745 / close 4,855
2024-06-04: high 5,220 / close 4,950
2024-08-05: low 4,775 / close 4,800
2024-09-27: high 5,580 / close 5,500
2024-10-11: high 5,870 / close 5,450
```

Approximate path from entry close:

```text
entry_close: 5,220
peak_high: 5,870
MFE: +12.5%
worst_low: 4,745
MAE: -9.1%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from low-PBR securities value-up relevance.
Stage2-Actionable: blocked unless payout/buyback/ROE bridge is explicit.
Stage3-Green: blocked.
Hard 4C: no.
```

The important lesson is over-certainty rather than catastrophic loss. A low-PBR financial can be relevant and still not be actionable without company-specific capital-return evidence.

### Stress-test components

```text
raw_component_score_proxy:
  low_pbr_valueup_relevance: medium_high
  payout_bridge: weak_to_medium
  roe_quality_visibility: weak_to_medium
  securities_market_beta: medium
  price_confirmation: shallow
  actionability_cap: Watch/Yellow
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3
```

The three-case C21 grid:

```text
029780 삼성카드:
  card-company payout bridge positive;
  controlled MAE and strong later MFE.

175330 JB금융지주:
  regional-bank ROE/payout positive;
  stronger MFE but local 4B after extended value-up rerating.

030610 교보증권:
  small securities low-PBR label without strong capital-return bridge;
  Watch/Yellow cap, not Green.
```

Shared rule:

```text
C21 is not "low-PBR financial."
C21 is "ROE and capital buffer convert into dividend, buyback, and durable rerating."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L92_029780_2024_02_26","scheduled_round":"R6","scheduled_loop":92,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"029780","name":"삼성카드","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":36200,"peak_high":46000,"peak_date":"2024-08-29","worst_low":35050,"worst_low_date":"2024-04-11","mfe_pct":27.1,"mae_pct":-3.2,"classification":"positive_card_company_dividend_capital_return_bridge","calibration_usable":true,"evidence_family":"card_company_dividend_payout_roe_valueup_bridge","residual_error":"none_for_actionable_if_payout_roe_credit_cost_bridge_explicit","shadow_rule_candidate":"allow_actionable_when_payout_capacity_and_roe_quality_confirm"}
{"row_type":"case","case_id":"C21_R6L92_175330_2024_02_26","scheduled_round":"R6","scheduled_loop":92,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"175330","name":"JB금융지주","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":13360,"peak_high":18710,"peak_date":"2024-10-25","worst_low":11390,"worst_low_date":"2024-04-11","mfe_pct":40.0,"mae_pct":-14.7,"classification":"positive_regional_bank_roe_payout_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"regional_bank_roe_payout_valueup_rerating_bridge","residual_error":"positive_entry_but_large_valueup_mfe_requires_local_4b_and_credit_cost_check","shadow_rule_candidate":"allow_actionable_with_roe_payout_bridge_but_attach_4b_after_extended_mfe"}
{"row_type":"case","case_id":"C21_R6L92_030610_2024_02_26","scheduled_round":"R6","scheduled_loop":92,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"030610","name":"교보증권","trigger_date":"2024-02-26","entry_date":"2024-02-26","entry_price":5220,"peak_high":5870,"peak_date":"2024-10-11","worst_low":4745,"worst_low_date":"2024-04-15","mfe_pct":12.5,"mae_pct":-9.1,"classification":"watch_cap_small_securities_low_pbr_label_without_strong_capital_return_bridge","calibration_usable":true,"evidence_family":"small_securities_low_pbr_valueup_label_without_strong_payout_roe_bridge","residual_error":"low_pbr_financial_label_can_overpromote_to_green_without_company_specific_capital_return","shadow_rule_candidate":"cap_low_pbr_small_securities_names_at_watch_yellow_without_payout_buyback_roe_bridge"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":92,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"CARD_REGIONAL_BANK_SECURITIES_VALUEUP_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":92,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_PAYOUT_ROE_CAPITAL_BUFFER_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21, do not open Stage2-Actionable or Stage3-Green from low-PBR financial, value-up policy, dividend label, or financial-sector beta alone. Require company-specific ROE quality, capital buffer, payout/dividend/buyback visibility, credit-cost or market-risk check, execution of shareholder return, and post-trigger price survival. Card and regional-bank positives may be Actionable when payout and ROE bridge are explicit. Small securities or weak-capital-return names should cap at Watch/Yellow unless buyback/payout and ROE bridge are explicit. If MFE extends beyond 35-40%, attach local 4B watch unless new capital-return evidence appears.","expected_effect":"Preserve financial value-up positives with payout/ROE evidence while reducing generic low-PBR financial false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":92,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"financial_valueup_payout_roe_guard","contribution":"Adds one card-company payout positive, one regional-bank ROE/payout positive with 4B watch, and one small-securities Watch cap case to calibrate C21 capital-return requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C21_PAYOUT_ROE_CAPITAL_BUFFER_BRIDGE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:

  Do not open Stage3-Green from:
    - low-PBR label alone
    - Korea Value-up policy headline alone
    - dividend theme alone
    - bank / card / securities label alone
    - one-week financial-sector rally alone

  Require at least two of:
    - durable ROE quality
    - capital adequacy / capital buffer
    - dividend payout capacity
    - buyback or shareholder-return execution
    - credit-cost or market-risk containment
    - earnings stability
    - low-MAE post-trigger price survival

  If MFE > 35% and MAE was nontrivial:
    preserve positive classification but attach local 4B watch.

  If MFE < 15% and payout/ROE bridge is weak:
    cap at Watch/Yellow, not Green.

  Distinguish:
    - card / regional-bank names with explicit payout and ROE bridge
    - from small securities or generic low-PBR names without new capital-return execution.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 financial value-up / capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_PAYOUT_ROE_CAPITAL_BUFFER_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 cases agree, consider implementing a canonical guard that:
   - blocks low-PBR financial Green without payout/ROE/capital buffer bridge,
   - preserves card/regional-bank positives with low MAE and shareholder-return visibility,
   - attaches local 4B after extended value-up rerating,
   - caps small securities names at Watch/Yellow without buyback/payout/ROE execution.

Expected next schedule:
completed_round = R6
completed_loop = 92
next_round = R7
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 92
next_round = R7
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
