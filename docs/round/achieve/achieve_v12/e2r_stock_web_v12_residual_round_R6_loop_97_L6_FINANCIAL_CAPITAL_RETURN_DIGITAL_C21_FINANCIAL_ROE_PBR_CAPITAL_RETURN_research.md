# E2R Stock-Web v12 Residual Research — R6 / Loop 97

```yaml
scheduled_round: R6
scheduled_loop: 97
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE

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
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
bank_holding_case_count: 2
digital_finance_case_count: 1
valueup_low_pbr_case_count: 3
capital_return_execution_case_count: 2
capital_return_bridge_missing_count: 1
digital_finance_growth_valuation_case_count: 1
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 97
next_round: R7
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 97
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate requires:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Recent R6 branch usage:

```text
loop93: C22_INSURANCE_RATE_CYCLE_RESERVE
loop94: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop95: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop96: C22_INSURANCE_RATE_CYCLE_RESERVE
```

This run returns to C21 after the R6 branch cycle, but avoids the C21 top-covered names and uses a narrower fine branch:

```text
bank holding / digital finance / Korea Value-up
ROE, CET1, dividend, buyback, cancellation, capital-allocation execution,
and valuation discipline bridge
vs generic low-PBR financial label spike
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
086790 하나금융지주
377300 카카오페이
```

They avoid the C21 top-covered list and recent R6 branch names:

```text
C21 top-covered avoid:
  006220, 016360, 071050, 105560, 138040, 139130

R6 loop95 C21 avoid:
  016610, 001450, 085620

R6 loop96 C22 avoid:
  032830, 088350, 000400
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
055550: same archetype, new symbol, bank-holding Value-up capital-return positive with Green cap after large MFE
086790: same archetype, new symbol, bank-holding ROE/CET1/shareholder-return positive with capital-buffer cap
377300: same archetype, new symbol, digital-finance/fintech Value-up late spike hard-4C without ROE/capital-return bridge
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
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

086790 하나금융지주
  profile: atlas/symbol_profiles/086/086790.json
  first_date: 2005-12-12
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,980
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

377300 카카오페이
  profile: atlas/symbol_profiles/377/377300.json
  first_date: 2021-11-03
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,050
  non_tradable_zero_volume rows: 2
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    shorter listed history and minor row-presence caveat.
    Digital-finance platform valuation should not be treated as bank-like capital-return execution.
```

---

## 4. Archetype residual problem

C21 is about financial ROE, PBR, and capital return. It is not a generic "financial stock is cheap" or "Korea Value-up label" archetype.

The model can over-score:

```text
low-PBR financial label
Korea Value-up policy headline
bank holding company label
dividend or buyback rumor
CET1 / capital buffer simplification
digital bank or fintech platform financial label
one-week financial-stock volume spike
late chase after a Value-up rerating
```

The C21 bridge must be stricter:

```text
financial ROE / PBR / capital-return event
  -> recurring ROE and earnings quality
  -> CET1 / capital buffer and regulatory room
  -> credit cost and asset-quality risk
  -> NIM / fee / non-interest income sustainability
  -> dividend, buyback, and cancellation execution
  -> dilution / share-count path
  -> valuation discipline after the first Value-up spike
  -> price survival after rerating
```

A C21 bank thesis is like a reservoir behind a dividend valve. The Value-up headline raises the water level, but equity value appears only when ROE keeps filling the reservoir, CET1 stays above the gate, credit losses do not crack the dam, and buybacks or dividends actually release cash to shareholders.

---

## 5. Case 1 — 055550 신한지주

```yaml
case_id: C21_R6L97_055550_2024_02_01
symbol: "055550"
name: "신한지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 42500
classification: positive_bank_holding_valueup_capital_return_execution_with_green_cap_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

신한지주 is the constructive C21 bank-holding control in this set.

The useful C21 read is not simply:

```text
저PBR 금융주가 강하다
```

It is:

```text
bank holding company
  -> recurring ROE and earnings quality
  -> CET1 / capital buffer room
  -> dividend, buyback, and cancellation optionality
  -> strong price confirmation after Value-up salience
```

The forward path delivered a large MFE and avoided hard drawdown. This supports positive classification. However, after a +50% rerating, Green should be capped unless ROE, credit cost, CET1, and actual shareholder-return execution remain current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 42,500 / close 42,500
2024-03-14: high 51,500 / close 51,500
2024-07-29: high 64,200 / close 60,700
2024-08-26: high 64,600 / close 61,400
2024-08-05: low 51,600 / close 52,800
2024-10-25: high 59,900 / close 58,000
```

Approximate path from entry close:

```text
entry_close: 42,500
peak_high: 64,600
MFE: +52.0%
worst_low_after_entry: 39,850
MAE: -6.2%
```

### Interpretation

This is a C21 positive with Green cap:

```text
Stage2-Actionable: possible if ROE, CET1, credit cost, and shareholder-return execution are explicit.
Stage3-Green: blocked unless fresh capital-return execution and earnings-quality evidence appears after large MFE.
Local 4B: monitor after +50% MFE if evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  bank_holding_relevance: very_high
  valueup_discount_compression: high
  recurring_roe_bridge: high
  cet1_capital_buffer_bridge: high
  dividend_buyback_cancellation_bridge: medium_high
  credit_cost_risk_check: medium
  price_confirmation: high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 086790 하나금융지주

```yaml
case_id: C21_R6L97_086790_2024_02_01
symbol: "086790"
name: "하나금융지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 52000
classification: positive_bank_holding_roe_cet1_shareholder_return_bridge_with_capital_buffer_cap
calibration_usable: true
```

### Evidence interpretation

하나금융지주 is the second C21 bank-holding positive.

The setup had strong C21 relevance:

```text
bank holding / low-PBR Value-up rerating
  -> high recurring profitability
  -> CET1 and capital-return capacity
  -> shareholder-return execution optionality
  -> low post-trigger drawdown
```

The price path validated the rerating with meaningful MFE and very controlled MAE. The case should remain positive. Still, C21 Green is not opened from PBR compression alone. It requires ongoing capital-buffer, ROE, credit-cost, NIM, and payout evidence.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 52,200 / close 52,000
2024-02-19: high 59,000 / close 58,900
2024-03-14: high 64,600 / close 64,600
2024-07-29: high 66,400 / close 63,000
2024-08-27: high 69,300 / close 66,000
2024-10-25: high 69,200 / close 66,500
```

Approximate path from entry close:

```text
entry_close: 52,000
peak_high: 69,300
MFE: +33.3%
worst_low_after_entry: 51,200
MAE: -1.5%
```

### Interpretation

This is a C21 positive with capital-return cap:

```text
Stage2-Actionable: valid when ROE, CET1, payout policy, and asset-quality bridge are explicit.
Stage3-Green: possible only with fresh capital-return execution and credit-cost evidence.
Local 4B: monitor after +30% MFE if the rerating outruns execution evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  bank_holding_relevance: very_high
  valueup_pbr_compression: high
  recurring_roe_bridge: high
  cet1_bridge: high
  shareholder_return_execution_bridge: medium_high
  asset_quality_bridge: medium
  price_confirmation: high
  drawdown_penalty: very_low
  green_cap: yes
```

---

## 7. Case 3 — 377300 카카오페이

```yaml
case_id: C21_R6L97_377300_2024_02_15
symbol: "377300"
name: "카카오페이"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-15
entry_date: 2024-02-15
entry_price_basis: close
entry_price: 48800
classification: hard_4c_candidate_digital_finance_valueup_late_spike_without_roe_capital_return_survival
calibration_usable: true
```

### Evidence interpretation

카카오페이 is the digital-finance / fintech hard C21 guardrail.

The label can fool the model:

```text
digital finance platform
payment / fintech financial label
rate-cut or growth-stock rebound
financial-sector Value-up sympathy
one-day volume spike
```

But C21 is not merely about being a financial platform. It requires recurring ROE, capital-return room, regulatory capital or capital-allocation discipline, shareholder return, and valuation discipline. From the selected late-spike entry, MFE was shallow while the later drawdown was severe.

### Price path

Key Stock-Web rows:

```text
2024-02-15: high 51,800 / close 48,800
2024-02-16: high 50,500 / close 49,400
2024-03-06: low 39,550 / close 40,150
2024-04-17: low 32,600 / close 32,700
2024-08-05: low 21,950 / close 22,600
2024-10-25: low 22,850 / close 23,050
```

Approximate path from late-spike close:

```text
entry_close: 48,800
peak_high_after_entry: 50,500
MFE: +3.5%
worst_low_after_entry: 21,950
MAE: -55.0%
```

### Interpretation

This is a hard C21 false-positive:

```text
Stage2-Watch: possible from digital-finance and fintech relevance.
Stage2-Actionable: blocked unless recurring ROE, monetization, capital allocation, and shareholder-return bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
Short-listing / minor row-presence caveat: yes.
```

The lesson is that a digital-finance label is not bank-like capital-return execution.

### Stress-test components

```text
raw_component_score_proxy:
  digital_finance_label: high
  fintech_growth_rebound: medium_high
  recurring_roe_bridge: weak
  capital_return_execution_bridge: weak
  valuation_discipline: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
bank_holding_case_count: 2
digital_finance_case_count: 1
valueup_low_pbr_case_count: 3
capital_return_execution_case_count: 2
capital_return_bridge_missing_count: 1
digital_finance_growth_valuation_case_count: 1
short_listing_or_row_presence_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C21 financial Value-up grid:

```text
055550 신한지주:
  bank-holding capital-return positive;
  large MFE and controlled MAE, but Green requires fresh ROE/CET1/shareholder-return execution evidence.

086790 하나금융지주:
  bank-holding ROE/CET1/shareholder-return positive;
  strong MFE and very low MAE, but still capped by capital-buffer and credit-cost evidence.

377300 카카오페이:
  digital-finance Value-up sympathy failed;
  shallow MFE and extreme MAE, hard 4C.
```

Shared rule:

```text
C21 is not "financial label is cheap."
C21 is "recurring ROE, capital buffer, asset quality, payout execution, buyback/cancellation, dilution control, and valuation discipline are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L97_055550_2024_02_01","scheduled_round":"R6","scheduled_loop":97,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE","symbol":"055550","name":"신한지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":42500,"peak_high":64600,"peak_date":"2024-08-26","worst_low_after_entry":39850,"worst_low_after_entry_date":"2024-02-26","mfe_pct":52.0,"mae_pct":-6.2,"classification":"positive_bank_holding_valueup_capital_return_execution_with_green_cap_after_large_mfe","calibration_usable":true,"evidence_family":"bank_holding_valueup_recurring_roe_cet1_dividend_buyback_cancellation_bridge","residual_error":"positive_bank_valueup_path_requires_green_cap_after_large_mfe_without_refreshed_roe_cet1_return_execution_evidence","shadow_rule_candidate":"allow_capped_actionable_when_roe_cet1_and_shareholder_return_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C21_R6L97_086790_2024_02_01","scheduled_round":"R6","scheduled_loop":97,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE","symbol":"086790","name":"하나금융지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":52000,"peak_high":69300,"peak_date":"2024-08-27","worst_low_after_entry":51200,"worst_low_after_entry_date":"2024-02-02","mfe_pct":33.3,"mae_pct":-1.5,"classification":"positive_bank_holding_roe_cet1_shareholder_return_bridge_with_capital_buffer_cap","calibration_usable":true,"evidence_family":"bank_holding_recurring_roe_cet1_capital_buffer_dividend_buyback_asset_quality_bridge","residual_error":"bank_valueup_positive_still_requires_capital_buffer_credit_cost_and_return_execution_refresh_before_green","shadow_rule_candidate":"preserve_bank_holding_positive_but_cap_green_without_fresh_cet1_credit_cost_and_payout_evidence"}
{"row_type":"case","case_id":"C21_R6L97_377300_2024_02_15","scheduled_round":"R6","scheduled_loop":97,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE","symbol":"377300","name":"카카오페이","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":48800,"peak_high":50500,"peak_date":"2024-02-16","worst_low_after_entry":21950,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.5,"mae_pct":-55.0,"classification":"hard_4c_candidate_digital_finance_valueup_late_spike_without_roe_capital_return_survival","calibration_usable":true,"short_listing_or_row_presence_caveat":true,"evidence_family":"digital_finance_fintech_valueup_sympathy_without_recurring_roe_capital_allocation_shareholder_return_bridge","residual_error":"digital_finance_label_can_fail_when_roe_capital_return_and_valuation_discipline_bridge_missing","shadow_rule_candidate":"route_digital_finance_valueup_late_spike_to_hard_4c_if_mfe_shallow_mae_extreme_and_capital_return_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":97,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_HOLDING_DIGITAL_FINANCE_VALUEUP_ROE_CET1_CAPITAL_RETURN_EXECUTION_BRIDGE_VS_LOW_PBR_FINANCIAL_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"bank_holding_case_count":2,"digital_finance_case_count":1,"valueup_low_pbr_case_count":3,"capital_return_execution_case_count":2,"capital_return_bridge_missing_count":1,"digital_finance_growth_valuation_case_count":1,"short_listing_or_row_presence_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":97,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_ROE_CET1_CAPITAL_RETURN_EXECUTION_VALUATION_DISCIPLINE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21 financial ROE/PBR/capital-return cases, do not open Stage2-Actionable or Stage3-Green from low-PBR financial, Korea Value-up, bank holding, dividend/buyback rumor, CET1 simplification, digital bank/fintech platform, one-week financial-stock spike, or late chase after a Value-up rerating labels alone. Require recurring ROE and earnings quality, CET1/capital buffer and regulatory room, credit cost and asset-quality risk check, NIM/fee/non-interest income sustainability, dividend/buyback/cancellation execution, dilution/share-count path, valuation discipline after the first Value-up spike, and post-trigger price survival. Bank-holding positives with large MFE may be capped Actionable when ROE, CET1, and shareholder-return bridge are explicit, but Green requires fresh evidence. Digital-finance/fintech labels with shallow MFE and extreme MAE should route to hard-4C when recurring ROE and capital-return bridge are missing.","expected_effect":"Preserve true bank-holding ROE/CET1/capital-return positives while reducing low-PBR financial-label, digital-finance, and Value-up late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":97,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"roe_cet1_capital_return_execution_valuation_guard","contribution":"Adds two bank-holding capital-return positives and one digital-finance hard-4C counterexample to calibrate C21 recurring ROE, CET1, credit cost, payout execution, buyback/cancellation, valuation discipline, and digital-finance false-positive guards.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C21_ROE_CET1_CAPITAL_RETURN_EXECUTION_VALUATION_DISCIPLINE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:

  Do not open Stage3-Green from:
    - low-PBR financial label alone
    - Korea Value-up policy headline alone
    - bank holding company label alone
    - dividend or buyback rumor alone
    - CET1 / capital-buffer simplification alone
    - digital bank or fintech platform label alone
    - one-week financial-stock volume spike alone
    - late chase after a Value-up rerating alone

  Require at least two of:
    - recurring ROE and earnings quality
    - CET1 / capital buffer and regulatory room
    - credit cost and asset-quality risk control
    - NIM / fee / non-interest income sustainability
    - dividend / buyback / cancellation execution
    - dilution / share-count path
    - valuation discipline after initial Value-up spike
    - low-MAE post-trigger price survival
    - fresh evidence after the low-PBR / Value-up headline

  If MFE < 8% and MAE < -35%:
    route to C21 hard-4C candidate.

  If MFE > 30% but evidence is broad Value-up only:
    preserve as capped positive, not Green, unless ROE/CET1/return evidence refreshes.

  If the company is digital-finance / fintech rather than bank-like capital-return issuer:
    require recurring ROE and capital-allocation proof before Actionable.

  Distinguish:
    - financial names where ROE and capital buffer become dividends, buybacks, cancellations, and share-count improvement
    - from financial labels where valuation multiple compresses briefly without return execution.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 financial ROE/PBR/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_ROE_CET1_CAPITAL_RETURN_EXECUTION_VALUATION_DISCIPLINE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 cases agree, consider implementing a canonical guard that:
   - blocks low-PBR/Value-up Green without ROE, CET1, credit-cost, payout, buyback/cancellation, and valuation discipline bridge,
   - preserves bank-holding positives only with price survival and fresh capital-return evidence,
   - caps broad Value-up bank reratings when execution evidence is stale,
   - routes shallow-MFE/extreme-MAE digital-finance Value-up late spikes to hard-4C,
   - applies short-listing/row-presence trust caveats.

Expected next schedule:
completed_round = R6
completed_loop = 97
next_round = R7
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 97
next_round = R7
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
