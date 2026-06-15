# E2R Stock-Web v12 Residual Research — R6 / Loop 99

```yaml
scheduled_round: R6
scheduled_loop: 99
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE

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
regional_bank_case_count: 2
small_securities_low_liquidity_case_count: 1
roe_pbr_valueup_case_count: 3
capital_return_execution_bridge_count: 2
low_pbr_label_only_case_count: 1
capital_return_execution_bridge_missing_count: 1
liquidity_row_trust_caveat_count: 1
old_corporate_action_or_name_history_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 99
next_round: R7
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_99_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 99
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 is the financial / capital-return / digital-finance round. The selected canonical archetype is:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

Recent R6 branch usage:

```text
loop96: C22_INSURANCE_RATE_CYCLE_RESERVE
loop97: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop98: C22_INSURANCE_RATE_CYCLE_RESERVE
```

This run returns to C21 after the R6 branch cycle.

Selected fine branch:

```text
regional bank / small securities / low-PBR financial Value-up
ROE quality, CET1 or capital buffer, RWA discipline, credit cost,
deposit beta and NIM, shareholder return, buyback/cancellation/dividend execution,
liquidity / row trust, and price-survival bridge
vs generic low-PBR financial / Value-up label spike
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
175330 JB금융지주
138930 BNK금융지주
003460 유화증권
```

They avoid the C21 top-covered list and avoid the most recent C22 insurance set:

```text
C21 top-covered avoid:
  006220, 016360, 071050, 105560, 138040, 139130

recent R6 loop98 C22 avoid:
  085620, 244920, 211050

recent R6 loop96 C22 avoid:
  032830, 088350, 000400
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
175330: same archetype, new symbol, regional bank ROE/PBR capital-return positive with Green cap.
138930: same archetype, new symbol, regional bank Value-up / shareholder-yield positive with Green cap.
003460: same archetype, new symbol, low-liquidity securities / low-PBR financial label Watch cap because price confirmation was shallow and execution bridge was weak.
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
175330 JB금융지주
  profile: atlas/symbol_profiles/175/175330.json
  first_date: 2013-07-18
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,089
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2014-01-29, 2014-09-26, 2015-12-01, 2018-10-26
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

138930 BNK금융지주
  profile: atlas/symbol_profiles/138/138930.json
  name history:
    BS금융지주 -> BNK금융지주
  first_date: 2011-03-30
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,663
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2014-07-25, 2016-02-05
  2024 entry~D+180 contamination: none
  caveat:
    old name / raw-discontinuity candidates are outside selected 2024 validation window.

003460 유화증권
  profile: atlas/symbol_profiles/003/003460.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,713
  non_tradable_zero_volume rows: 51
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    2020-04-14
  2024 entry~D+180 contamination: none
  caveat:
    low-liquidity / row-presence and old corporate-action caveat require trust cap.
```

---

## 4. Archetype residual problem

C21 is about financial ROE, PBR, and capital return. It is not a generic "low-PBR financial stock is cheap" archetype.

The model can over-score:

```text
low-PBR financial label
Korea Value-up financial headline
bank / regional bank / securities label
dividend yield headline without payout durability
buyback headline without cancellation / execution
ROE headline without RWA / credit-cost check
rate-cycle or NIM headline without deposit beta
one-week financial stock volume spike
low-liquidity deep-value financial spike
```

The C21 bridge must be stricter:

```text
financial ROE / PBR / capital-return event
  -> business type and balance-sheet model
  -> ROE quality and earnings recurrence
  -> CET1 / capital buffer / regulatory room
  -> RWA growth and risk-weight discipline
  -> credit cost, delinquency, provisioning, and asset quality
  -> NIM, deposit beta, funding cost, and duration risk
  -> shareholder-return policy, payout ratio, dividend, buyback, and cancellation mechanics
  -> minority-value delivery and board / regulatory approval
  -> liquidity / row / tradeability trust
  -> price survival after the first low-PBR / Value-up spike
```

A C21 thesis is like a bank balance sheet with a dividend valve. The low PBR shows the tank is discounted, but equity value appears only when ROE is real, capital is sufficient, credit cost does not leak the tank, and management can open the dividend or cancellation valve without weakening the balance sheet.

---

## 5. Case 1 — 175330 JB금융지주

```yaml
case_id: C21_R6L99_175330_2024_02_01
symbol: "175330"
name: "JB금융지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12580
classification: positive_regional_bank_roe_pbr_capital_return_shareholder_yield_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

JB금융지주 is the constructive C21 regional-bank control.

The useful C21 read is not simply:

```text
저PBR 은행주 / Value-up 수혜주가 강하다
```

It is:

```text
regional bank ROE / shareholder-return relevance
  -> capital buffer and payout room
  -> RWA / credit-cost discipline
  -> dividend / buyback / cancellation expectation
  -> strong October price confirmation
```

The forward path produced meaningful MFE and avoided a hard drawdown. This preserves positive classification. However, after the large rerating, C21 Green should remain capped unless ROE quality, CET1/capital buffer, RWA growth, credit cost, payout/cancellation, and shareholder-return evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,790 / low 11,520 / close 12,580
2024-02-27: high 13,930 / close 13,610
2024-04-11: low 11,390 / close 12,180
2024-08-05: low 12,980 / close 13,480
2024-10-17: high 17,210 / close 17,150
2024-10-25: high 18,710 / close 18,290
```

Approximate path from entry close:

```text
entry_close: 12,580
peak_high: 18,710
MFE: +48.7%
worst_low_after_entry: 11,390
MAE: -9.5%
```

### Interpretation

This is a C21 positive with Green cap:

```text
Stage2-Actionable: possible if ROE quality, CET1/capital buffer, credit cost, payout policy, and buyback/cancellation bridge are explicit.
Stage3-Green: blocked after +45% MFE unless fresh capital-return execution evidence appears.
Local 4B: monitor if low-PBR/Value-up price outruns balance-sheet evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  regional_bank_relevance: high
  roe_pbr_valueup_signal: high
  capital_buffer_bridge: medium_high
  credit_cost_rwa_bridge: medium
  payout_buyback_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 138930 BNK금융지주

```yaml
case_id: C21_R6L99_138930_2024_02_01
symbol: "138930"
name: "BNK금융지주"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 7870
classification: positive_regional_bank_valueup_capital_return_roe_credit_cost_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

BNK금융지주 is the second regional-bank Value-up positive.

The setup had real C21 relevance:

```text
regional financial holding company
  -> low-PBR / shareholder-return policy readthrough
  -> ROE and credit-cost sensitivity
  -> capital buffer and payout optionality
```

The price path validated the setup with a clean first-half base and a strong late-summer rerating. Still, C21 should not keep the score as unrestricted Green without current evidence on capital ratio, RWA, credit cost, provisioning, payout policy, and buyback/cancellation execution.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,960 / low 7,520 / close 7,870
2024-02-19: high 8,070 / close 8,020
2024-03-14: high 8,410 / close 8,340
2024-04-12: low 7,460 / close 7,510
2024-08-26: high 10,340 / close 10,210
2024-10-25: high 10,050 / close 9,910
```

Approximate path from entry close:

```text
entry_close: 7,870
peak_high: 10,340
MFE: +31.4%
worst_low_after_entry: 7,320
MAE: -7.0%
```

### Interpretation

This is a C21 positive with Green cap:

```text
Stage2-Actionable: possible if capital buffer, credit-cost trend, RWA discipline, NIM/funding cost, and capital-return mechanics are explicit.
Stage3-Green: blocked unless shareholder-return execution and balance-sheet quality are fresh.
Local 4B: monitor if late-summer rerating outruns capital-quality evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  regional_bank_relevance: high
  low_pbr_valueup_signal: high
  capital_buffer_bridge: medium
  credit_cost_bridge: medium
  shareholder_return_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  green_cap: yes
```

---

## 7. Case 3 — 003460 유화증권

```yaml
case_id: C21_R6L99_003460_2024_02_01
symbol: "003460"
name: "유화증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 2290
classification: watch_cap_low_liquidity_securities_low_pbr_capital_return_label_without_execution_or_price_confirmation
calibration_usable: true
```

### Evidence interpretation

유화증권 is the low-liquidity securities / low-PBR financial Watch cap.

The label can fool the model:

```text
securities company
low-PBR financial label
dividend / shareholder-yield look-through
low-liquidity deep-value salience
```

But from the selected February entry, the path did not validate Actionable or Green. Price confirmation was shallow, trading value was thin, and the bridge from low-PBR securities label to durable ROE, capital return, buyback/cancellation, shareholder-value realization, and liquidity/tradeability trust was not strong.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 2,290 / low 2,185 / close 2,290
2024-03-12: high 2,390 / close 2,265
2024-08-05: low 2,085 / close 2,120
2024-09-27: high 2,385 / close 2,335
2024-10-25: low 2,205 / close 2,240
```

Approximate path from entry close:

```text
entry_close: 2,290
peak_high: 2,390
MFE: +4.4%
worst_low_after_entry: 2,085
MAE: -9.0%
```

### Interpretation

This is a C21 Watch / Yellow cap:

```text
Stage2-Watch: possible from securities / low-PBR relevance.
Stage2-Actionable: blocked unless ROE quality, capital-return execution, buyback/cancellation, liquidity, and shareholder-value bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because drawdown was not hard-zone.
Liquidity / row-trust cap: required.
```

The lesson is that a low-PBR financial label is not capital-return execution.

### Stress-test components

```text
raw_component_score_proxy:
  low_pbr_securities_label: high
  shareholder_yield_signal: weak_to_medium
  roe_quality_bridge: weak
  capital_return_execution_bridge: weak
  liquidity_tradeability_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: low_to_medium
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
regional_bank_case_count: 2
small_securities_low_liquidity_case_count: 1
roe_pbr_valueup_case_count: 3
capital_return_execution_bridge_count: 2
low_pbr_label_only_case_count: 1
capital_return_execution_bridge_missing_count: 1
liquidity_row_trust_caveat_count: 1
old_corporate_action_or_name_history_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C21 financial ROE/PBR grid:

```text
175330 JB금융지주:
  regional bank ROE/PBR capital-return positive;
  large MFE and controlled MAE, but Green requires fresh capital and shareholder-return evidence.

138930 BNK금융지주:
  regional bank Value-up positive;
  meaningful MFE and low MAE, but Green requires fresh credit-cost / capital-return execution evidence.

003460 유화증권:
  low-liquidity securities / low-PBR financial label;
  shallow MFE and low liquidity, Watch/Yellow cap.
```

Shared rule:

```text
C21 is not "financial low-PBR label is cheap."
C21 is "ROE quality, capital buffer, RWA discipline, credit cost, funding cost, payout/cancellation execution, liquidity trust, and price survival are visible."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L99_175330_2024_02_01","scheduled_round":"R6","scheduled_loop":99,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE","symbol":"175330","name":"JB금융지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12580,"peak_high":18710,"peak_date":"2024-10-25","worst_low_after_entry":11390,"worst_low_after_entry_date":"2024-04-11","mfe_pct":48.7,"mae_pct":-9.5,"classification":"positive_regional_bank_roe_pbr_capital_return_shareholder_yield_bridge_with_green_cap","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"regional_bank_roe_pbr_valueup_cet1_rwa_credit_cost_payout_buyback_capital_return_bridge","residual_error":"regional_bank_valueup_positive_requires_green_cap_after_large_mfe_without_refreshed_capital_return_and_credit_cost_evidence","shadow_rule_candidate":"allow_capped_actionable_when_roe_capital_buffer_credit_cost_and_shareholder_return_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C21_R6L99_138930_2024_02_01","scheduled_round":"R6","scheduled_loop":99,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE","symbol":"138930","name":"BNK금융지주","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":7870,"peak_high":10340,"peak_date":"2024-08-26","worst_low_after_entry":7320,"worst_low_after_entry_date":"2024-02-28","mfe_pct":31.4,"mae_pct":-7.0,"classification":"positive_regional_bank_valueup_capital_return_roe_credit_cost_bridge_with_green_cap","calibration_usable":true,"old_corporate_action_or_name_history_caveat":true,"evidence_family":"regional_financial_holding_low_pbr_valueup_capital_buffer_credit_cost_nim_payout_capital_return_bridge","residual_error":"regional_bank_valueup_path_requires_green_cap_without_refreshed_credit_cost_capital_buffer_and_payout_execution_evidence","shadow_rule_candidate":"preserve_regional_bank_positive_but_cap_green_after_mfe_if_capital_return_execution_and_asset_quality_evidence_are_stale"}
{"row_type":"case","case_id":"C21_R6L99_003460_2024_02_01","scheduled_round":"R6","scheduled_loop":99,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE","symbol":"003460","name":"유화증권","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":2290,"peak_high":2390,"peak_date":"2024-03-12","worst_low_after_entry":2085,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.4,"mae_pct":-9.0,"classification":"watch_cap_low_liquidity_securities_low_pbr_capital_return_label_without_execution_or_price_confirmation","calibration_usable":true,"liquidity_row_trust_caveat":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"low_liquidity_securities_low_pbr_shareholder_yield_label_without_roe_quality_capital_return_execution_liquidity_bridge","residual_error":"low_pbr_securities_label_can_overpromote_without_capital_return_execution_and_liquidity_trust","shadow_rule_candidate":"cap_low_liquidity_securities_low_pbr_label_at_watch_yellow_if_mfe_shallow_and_execution_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":99,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"REGIONAL_BANK_SECURITIES_ROE_PBR_CAPITAL_RETURN_CET1_RWA_CREDIT_COST_SHAREHOLDER_YIELD_BRIDGE_VS_LOW_PBR_VALUEUP_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":0,"regional_bank_case_count":2,"small_securities_low_liquidity_case_count":1,"roe_pbr_valueup_case_count":3,"capital_return_execution_bridge_count":2,"low_pbr_label_only_case_count":1,"capital_return_execution_bridge_missing_count":1,"liquidity_row_trust_caveat_count":1,"old_corporate_action_or_name_history_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":99,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_ROE_PBR_CAPITAL_RETURN_CREDIT_COST_EXECUTION_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21 financial ROE/PBR/capital-return cases, do not open Stage2-Actionable or Stage3-Green from low-PBR financial, Korea Value-up, bank/regional-bank/securities label, dividend-yield headline without payout durability, buyback headline without cancellation/execution, ROE headline without RWA and credit-cost check, rate-cycle/NIM headline without deposit beta, one-week financial-stock volume spike, or low-liquidity deep-value spike alone. Require business type and balance-sheet model, ROE quality and earnings recurrence, CET1/capital buffer/regulatory room, RWA growth and risk-weight discipline, credit cost/delinquency/provisioning/asset quality, NIM/deposit beta/funding cost/duration risk, shareholder-return policy, payout ratio, dividend/buyback/cancellation mechanics, minority-value delivery and board/regulatory approval, liquidity/row/tradeability trust, and post-trigger price survival. Regional-bank positives with meaningful MFE may be capped Actionable when ROE, capital buffer, credit cost, and shareholder-return bridge are explicit, but Green requires fresh evidence. Low-liquidity securities/low-PBR labels with shallow MFE should cap at Watch/Yellow unless capital-return execution and liquidity trust are explicit.","expected_effect":"Preserve true bank capital-return positives while reducing generic low-PBR financial, securities, dividend-yield, and Value-up label false positives where ROE quality, capital buffer, credit cost, payout execution, cancellation, and liquidity evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":99,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"roe_pbr_capital_return_credit_cost_execution_trust_guard","contribution":"Adds two regional-bank capital-return positives and one low-liquidity securities Watch cap to calibrate C21 ROE quality, capital buffer, RWA, credit cost, shareholder-return execution, buyback/cancellation mechanics, liquidity trust, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C21_ROE_PBR_CAPITAL_RETURN_CREDIT_COST_EXECUTION_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:

  Do not open Stage3-Green from:
    - low-PBR financial label alone
    - Korea Value-up financial headline alone
    - bank / regional bank / securities label alone
    - dividend yield headline without payout durability alone
    - buyback headline without cancellation / execution alone
    - ROE headline without RWA / credit-cost check alone
    - rate-cycle or NIM headline without deposit beta alone
    - one-week financial-stock volume spike alone
    - low-liquidity deep-value financial spike alone

  Require at least two of:
    - business type and balance-sheet model
    - ROE quality and earnings recurrence
    - CET1 / capital buffer / regulatory room
    - RWA growth and risk-weight discipline
    - credit cost / delinquency / provisioning / asset quality
    - NIM / deposit beta / funding cost / duration risk
    - shareholder-return policy, payout ratio, dividend, buyback, cancellation mechanics
    - minority-value delivery and board / regulatory approval
    - liquidity / row / tradeability trust
    - low-MAE post-trigger price survival
    - fresh evidence after the low-PBR / Value-up headline

  If MFE < 8% and bridge is label-only:
    cap at Watch/Yellow.

  If MFE > 20% but capital-return evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If liquidity/row-trust caveat exists:
    block Green unless execution and price survival are clean.

  Distinguish:
    - financials where ROE and capital buffer become real shareholder return
    - from labels where low PBR remains a locked balance-sheet discount.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_99_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 financial ROE/PBR/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_ROE_PBR_CAPITAL_RETURN_CREDIT_COST_EXECUTION_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 cases agree, consider implementing a canonical guard that:
   - blocks financial Value-up Green without ROE quality, capital buffer, RWA, credit cost, and shareholder-return execution bridge,
   - preserves regional-bank positives only with price survival and fresh capital-return / asset-quality evidence,
   - caps low-liquidity securities low-PBR labels at Watch/Yellow without execution and liquidity trust,
   - applies old corporate-action, name-history, low-liquidity, and row-presence caveats.

Expected next schedule:
completed_round = R6
completed_loop = 99
next_round = R7
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 99
next_round = R7
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
