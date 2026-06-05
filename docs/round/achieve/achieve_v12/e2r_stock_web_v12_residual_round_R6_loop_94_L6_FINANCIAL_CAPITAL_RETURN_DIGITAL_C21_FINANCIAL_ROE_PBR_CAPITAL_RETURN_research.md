# E2R Stock-Web v12 Residual Research — R6 / Loop 94

```yaml
scheduled_round: R6
scheduled_loop: 94
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE

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
bank_holding_valueup_case_count: 2
small_brokerage_false_positive_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 94
next_round: R7
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_94_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 94
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate requires:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Recent R6 branch usage:

```text
loop92: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop93: C22_INSURANCE_RATE_CYCLE_RESERVE
```

This run returns to C21, but avoids the top-covered financial names and uses a different fine branch:

```text
bank holding Value-up / ROE-PBR / capital-return execution bridge
vs small brokerage PBR-label spike
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
055550 신한지주
316140 우리금융지주
001510 SK증권
```

They avoid the C21 top-covered symbols and avoid recent R6 loop92~93 symbols:

```text
loop92 avoid: 029780, 175330, 030610
loop93 avoid: 088350, 032830, 000400
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
055550: same archetype, new symbol, large bank holding Value-up / ROE-PBR / capital-return positive
316140: same archetype, new symbol, bank holding capital-return positive with later 4B watch
001510: same archetype, new symbol, small brokerage low-PBR/value-up label hard-4C without ROE-return bridge
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
055550 신한지주
  profile: atlas/symbol_profiles/055/055550.json
  first_date: 2001-09-10
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,031
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

316140 우리금융지주
  profile: atlas/symbol_profiles/316/316140.json
  first_date: 2019-02-13
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,725
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

001510 SK증권
  profile: atlas/symbol_profiles/001/001510.json
  name history:
    선경증권 until 1998-01-20
    SK증권 from 1998-01-21
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,752
  corporate_action_candidate_dates:
    1998-03-28, 1999-01-08, 1999-08-27, 1999-10-21, 2018-12-24
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C21 is about ROE, PBR, capital return, and execution. It is not a generic "financial stock is low PBR" or "Value-up policy exists" label.

The model can over-score:

```text
Korea Value-up policy
low-PBR financial label
bank holding company label
brokerage low-price sympathy
one-week financial-stock rally
dividend yield label
```

The C21 bridge must be stricter:

```text
financial Value-up or ROE/PBR event
  -> company-specific ROE quality
  -> CET1 or capital buffer
  -> dividend / buyback / cancellation execution
  -> earnings stability and credit-cost control
  -> valuation discount compression
  -> price survival after the first financial rally
```

A financial Value-up thesis is like a bank vault. The label says the vault is underpriced, but C21 asks whether earnings fill it, capital rules allow cash out, and management actually opens the door for shareholders.

---

## 5. Case 1 — 055550 신한지주

```yaml
case_id: C21_R6L94_055550_2024_02_01
symbol: "055550"
name: "신한지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 42500
classification: positive_large_bank_holding_valueup_roe_capital_return_bridge
calibration_usable: true
```

### Evidence interpretation

신한지주 is the clean constructive control.

The useful C21 bridge is:

```text
large bank holding company
  -> ROE and book-value quality
  -> capital buffer
  -> dividend / buyback / cancellation optionality
  -> Value-up discount compression
  -> strong price confirmation
```

The forward path delivered strong MFE with controlled MAE. This is the shape of a real C21 positive, not just a low-PBR headline.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 42,500 / close 42,500
2024-03-14: high 51,500 / close 51,500
2024-04-17: low 40,450 / close 40,550
2024-07-26: high 58,400 / close 58,000
2024-07-29: high 64,200 / close 60,700
2024-08-26: high 64,600 / close 61,400
2024-10-25: high 59,900 / close 58,000
```

Approximate path from entry close:

```text
entry_close: 42,500
peak_high: 64,600
MFE: +52.0%
worst_low_after_entry: 39,850 on 2024-02-26
MAE: -6.2%
```

### Interpretation

This is a C21 positive:

```text
Stage2-Actionable: valid if ROE, CET1/capital buffer, and shareholder-return bridge are explicit.
Stage3-Green: possible with actual dividend/buyback/cancellation execution and price survival.
Local 4B: required after +50% MFE unless fresh capital-return evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  bank_holding_quality: high
  roe_pbr_valueup_bridge: high
  capital_buffer_bridge: high
  shareholder_return_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 316140 우리금융지주

```yaml
case_id: C21_R6L94_316140_2024_02_01
symbol: "316140"
name: "우리금융지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 14410
classification: positive_bank_holding_capital_return_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

우리금융지주 is a second bank-holding positive, but with a more capped interpretation.

The useful bridge is:

```text
bank holding Value-up relevance
  -> capital return expectation
  -> ROE/PBR discount compression
  -> controlled drawdown
  -> later price confirmation
```

The path worked, but the move was smaller and more cyclical than 신한지주. It should remain a positive, while requiring capital-return execution evidence before Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 14,490 / close 14,410
2024-03-14: high 15,320 / close 15,160
2024-04-17: low 13,170 / close 13,170
2024-07-26: high 16,230 / close 16,180
2024-08-22: high 16,600 / close 16,600
2024-10-25: high 17,100 / close 17,080
```

Approximate path from entry close:

```text
entry_close: 14,410
peak_high: 17,100
MFE: +18.7%
worst_low_after_entry: 13,170
MAE: -8.6%
```

### Interpretation

This is a C21 positive with 4B watch:

```text
Stage2-Actionable: valid if capital buffer and shareholder-return bridge are explicit.
Stage3-Green: blocked without actual capital-return execution and sustained ROE quality.
Local 4B: monitor after late-year rally.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  bank_holding_valueup_relevance: high
  roe_pbr_discount_bridge: medium_high
  capital_return_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 7. Case 3 — 001510 SK증권

```yaml
case_id: C21_R6L94_001510_2024_02_01
symbol: "001510"
name: "SK증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 647
classification: hard_4c_candidate_small_brokerage_low_pbr_valueup_label_without_roe_capital_return_bridge
calibration_usable: true
```

### Evidence interpretation

SK증권 is the small-brokerage hard guardrail.

The setup can fool a C21 model:

```text
low-priced financial
brokerage label
low-PBR / Value-up sympathy
one-week financial-sector rally
```

But the forward path did not validate ROE quality, capital-return execution, or price survival. MFE was shallow, and the later drawdown crossed the hard-4C area.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 655 / close 647
2024-02-19: high 669 / close 665
2024-04-17: low 588 / close 588
2024-08-05: low 496 / close 501
2024-09-04: high 630 / close 540
2024-12-09: low 452 / close 452
2024-12-30: low 459 / close 463
```

Approximate path from entry close:

```text
entry_close: 647
peak_high: 669
MFE: +3.4%
worst_low_after_entry: 452
MAE: -30.1%
```

### Interpretation

This is a hard C21 false-positive:

```text
Stage2-Watch: possible from financial-sector / low-PBR relevance.
Stage2-Actionable: blocked without ROE quality, capital-return execution, or discount-compression evidence.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30% MAE.
```

The lesson is that low-price brokerage beta is not shareholder-return quality.

### Stress-test components

```text
raw_component_score_proxy:
  small_brokerage_label: high
  valueup_low_pbr_sympathy: medium_high
  roe_quality_bridge: weak
  capital_return_execution: weak
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
bank_holding_valueup_case_count: 2
small_brokerage_false_positive_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C21 financial grid:

```text
055550 신한지주:
  large bank holding Value-up / ROE-PBR / capital return positive;
  strong MFE and controlled MAE, but 4B after +50% MFE.

316140 우리금융지주:
  bank holding capital-return positive;
  moderate MFE and controlled MAE, Green capped without execution evidence.

001510 SK증권:
  small brokerage / low-PBR financial label failed;
  shallow MFE and -30% MAE, hard 4C.
```

Shared rule:

```text
C21 is not "financial stock is low PBR."
C21 is "ROE quality, capital buffer, dividend/buyback/cancellation, and discount compression are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L94_055550_2024_02_01","scheduled_round":"R6","scheduled_loop":94,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE","symbol":"055550","name":"신한지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":42500,"peak_high":64600,"peak_date":"2024-08-26","worst_low_after_entry":39850,"worst_low_after_entry_date":"2024-02-26","mfe_pct":52.0,"mae_pct":-6.2,"classification":"positive_large_bank_holding_valueup_roe_capital_return_bridge","calibration_usable":true,"evidence_family":"large_bank_holding_roe_pbr_capital_buffer_shareholder_return_bridge","residual_error":"positive_bank_valueup_path_requires_4b_after_large_mfe_without_fresh_return_execution","shadow_rule_candidate":"preserve_positive_when_roe_capital_return_and_price_survival_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C21_R6L94_316140_2024_02_01","scheduled_round":"R6","scheduled_loop":94,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE","symbol":"316140","name":"우리금융지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":14410,"peak_high":17100,"peak_date":"2024-10-25","worst_low_after_entry":13170,"worst_low_after_entry_date":"2024-04-17","mfe_pct":18.7,"mae_pct":-8.6,"classification":"positive_bank_holding_capital_return_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"bank_holding_valueup_capital_return_roe_pbr_discount_bridge","residual_error":"positive_but_green_requires_actual_return_execution_and_sustained_roe_quality","shadow_rule_candidate":"allow_capped_actionable_for_bank_holding_valueup_when_capital_buffer_and_price_survival_confirm"}
{"row_type":"case","case_id":"C21_R6L94_001510_2024_02_01","scheduled_round":"R6","scheduled_loop":94,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE","symbol":"001510","name":"SK증권","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":647,"peak_high":669,"peak_date":"2024-02-19","worst_low_after_entry":452,"worst_low_after_entry_date":"2024-12-09","mfe_pct":3.4,"mae_pct":-30.1,"classification":"hard_4c_candidate_small_brokerage_low_pbr_valueup_label_without_roe_capital_return_bridge","calibration_usable":true,"evidence_family":"small_brokerage_low_pbr_valueup_label_without_roe_quality_or_capital_return_bridge","residual_error":"low_price_financial_label_can_overpromote_without_roe_and_shareholder_return_execution","shadow_rule_candidate":"route_small_brokerage_low_pbr_label_to_hard_4c_if_mfe_shallow_mae_large_and_roe_return_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":94,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_SMALL_BROKERAGE_PBR_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"bank_holding_valueup_case_count":2,"small_brokerage_false_positive_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":94,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_ROE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21, do not open Stage2-Actionable or Stage3-Green from Korea Value-up, low-PBR financial label, bank holding label, brokerage label, dividend-yield label, or one-week financial-stock rally alone. Require company-specific ROE quality, CET1 or capital buffer, dividend/buyback/cancellation execution, earnings stability and credit-cost control, valuation discount compression, and post-trigger price survival. Large bank-holding positives may be Actionable when capital buffer and shareholder-return bridge are explicit, but large MFE should attach local 4B unless fresh execution evidence appears. Small brokerage or low-price financial labels with shallow MFE and high MAE should route to hard-4C when ROE and capital-return bridge are missing.","expected_effect":"Preserve true financial Value-up positives with ROE/capital-return evidence while reducing low-PBR and small-brokerage false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":94,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"financial_roe_capital_return_guard","contribution":"Adds two bank-holding Value-up positives and one small-brokerage hard-4C counterexample to calibrate C21 ROE, capital-buffer, shareholder-return, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C21_ROE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:

  Do not open Stage3-Green from:
    - Korea Value-up policy headline alone
    - low-PBR financial label alone
    - bank holding or brokerage label alone
    - dividend-yield label alone
    - one-week financial-stock volume spike alone

  Require at least two of:
    - company-specific ROE quality
    - CET1 / capital buffer
    - dividend / buyback / cancellation execution
    - earnings stability / credit-cost control
    - valuation discount compression
    - low-MAE post-trigger price survival
    - fresh evidence after the Value-up headline

  If MFE < 5% and MAE < -30%:
    route to C21 hard-4C candidate.

  If MFE > 40%:
    preserve positive classification but attach local 4B unless capital-return evidence refreshes the thesis.

  If MFE is moderate and MAE controlled:
    allow capped Actionable only if capital buffer and shareholder-return bridge are explicit.

  Distinguish:
    - large banks with visible ROE, capital buffer, and capital-return execution
    - from low-price brokerage or generic financial labels where the policy does not reach shareholder economics.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_94_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 financial ROE/PBR/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_ROE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 cases agree, consider implementing a canonical guard that:
   - blocks low-PBR financial Green without ROE/capital-buffer/shareholder-return bridge,
   - preserves large-bank positives only with price survival and capital-return evidence,
   - attaches local 4B after large MFE,
   - routes shallow-MFE/high-MAE small-brokerage labels to hard-4C.

Expected next schedule:
completed_round = R6
completed_loop = 94
next_round = R7
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 94
next_round = R7
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
