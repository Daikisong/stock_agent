# E2R Stock-Web v12 Residual Research — R6 / Loop 90

```yaml
scheduled_round: R6
scheduled_loop: 90
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA

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
watch_or_cap_case_count: 1
counterexample_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 90
next_round: R7
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 90
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate allows the financial sector and ordinary C21/C22 financial research. Recent R6 files already used:

```text
loop88: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN — bank/value-up/capital-return bridge
loop89: C22_INSURANCE_RATE_CYCLE_RESERVE — insurance CSM/reserve/rate cycle
```

This file returns to C21 but uses a different failure mode:

```text
securities / brokerage / capital-market value-up beta
```

The aim is not to repeat bank capital-return logic. The aim is to separate:

```text
low-PBR financial sector beta
```

from:

```text
securities company ROE / trading-volume / IB / shareholder-return conversion bridge
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
005940 NH투자증권
006800 미래에셋증권
039490 키움증권
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

These three are not in the listed top-covered C21 symbols. The symbol set also avoids recently used R6 loop88 names:

```text
086790, 316140, 323410
```

Novelty classification:

```text
005940: same archetype, new symbol, securities capital-return bridge
006800: same archetype, new symbol, securities low-PBR beta false-positive
039490: same archetype, new symbol, brokerage revenue bridge / shallow-MFE cap case
```

---

## 3. Price-atlas validation

Manifest fields checked:

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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
005940 NH투자증권
  profile: atlas/symbol_profiles/005/005940.json
  current/latest name: NH투자증권
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,765
  corporate_action_candidate_dates:
    1999-04-14, 1999-11-01, 2000-01-31, 2011-12-08, 2015-01-20
  2024 entry~D+180 contamination: none

006800 미래에셋증권
  profile: atlas/symbol_profiles/006/006800.json
  current/latest name: 미래에셋증권
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,765
  corporate_action_candidate_dates:
    1999-09-27, 1999-10-14, 2000-05-22, 2001-11-23, 2011-11-16, 2017-01-20
  2024 entry~D+180 contamination: none

039490 키움증권
  profile: atlas/symbol_profiles/039/039490.json
  current/latest name: 키움증권
  first_date: 2004-04-23
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,390
  corporate_action_candidate_dates:
    2008-12-24
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame

Trigger frame:

```text
2024-02-28
Korea Corporate Value-up / shareholder-return pressure follow-up after the late-February reform package
```

The 2024 policy package targeted Korea's low valuation problem by encouraging listed firms to improve shareholder returns and market value. But for C21 this is only sector-level beta. A financial stock should not become Stage3-Green just because the policy exists.

For securities companies, the bridge must be narrower:

```text
brokerage/trading-volume sensitivity
IB/advisory/WM earnings quality
ROE visibility
capital return or balance-sheet efficiency
shareholder-return plan
sustainable payout capacity
```

---

## 5. Archetype residual problem

C21 has already learned a lot from banks and insurers. The residual problem is different for securities firms.

Bank and insurer capital-return logic often centers on:

```text
CET1 / solvency / CSM / reserve quality / payout
```

Securities firms instead need:

```text
market turnover
retail trading participation
margin loan balance
IB pipeline
proprietary book volatility
wealth-management asset growth
actual buyback/dividend policy
```

The model can over-credit the following:

```text
low PBR
financial sector value-up beta
short-term KOSPI/KOSDAQ risk-on move
brokerage sector rally
```

without confirming whether earnings and capital return can actually persist.

---

## 6. Case 1 — 005940 NH투자증권

```yaml
case_id: C21_R6L90_005940_2024_02_28
symbol: "005940"
name: "NH투자증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 11550
classification: positive_capital_return_brokerage_bridge
calibration_usable: true
```

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 11,550
2024-02-29: high 11,740 / close 11,740
2024-03-13: high 13,000 / close 12,840
2024-03-14: high 13,100 / close 13,060
2024-04-01: low 11,190 / close 11,280
2024-08-01: high 14,400 / close 14,170
2025-02-26: high 15,340 / close 15,280
```

Approximate path from entry close:

```text
entry_close: 11,550
180D_peak_high: 14,400
180D_MFE: +24.7%
forward_local_low_after_entry: 11,190
180D_MAE: -3.1%
extended_2025_peak_high: 15,340
```

### Interpretation

This is the constructive securities-company example.

The price path did not behave like a pure one-day value-up headline. The stock had low drawdown from entry and produced a controlled MFE. That suggests the market saw more than a shallow "financial beta" trade.

C21 read:

```text
Stage2-Actionable: valid
Stage3-Green: allowed only if actual ROE / payout / brokerage revenue bridge is present
local_4B: not immediate
hard_4C: no
```

### Raw component stress test

```text
raw_component_score_proxy:
  financial_valueup_policy_beta: medium
  low_pbr_value_signal: medium
  shareholder_return_visibility: medium
  roe_visibility: medium
  brokerage_volume_sensitivity: medium
  evidence_quality: medium_high
  price_confirmation: high
  drawdown_penalty: low
```

Residual contribution:

```text
This case supports C21 securities positives when price confirmation comes with low MAE and visible securities-business bridge.
```

---

## 7. Case 2 — 006800 미래에셋증권

```yaml
case_id: C21_R6L90_006800_2024_02_28
symbol: "006800"
name: "미래에셋증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 9010
classification: hard_4c_candidate_low_pbr_securities_beta_without_bridge
calibration_usable: true
```

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 9,010
2024-02-29: high 9,160 / close 9,020
2024-03-04: high 9,130 / close 9,000
2024-03-12: low 7,750 / close 7,820
2024-08-05: low 6,600 / close 6,660
2025-03-13: high 9,750 / close 9,630
2025-04-09: low 8,410 / close 8,500
```

Approximate path from entry close:

```text
entry_close: 9,010
180D_peak_high: 9,160
180D_MFE: +1.7%
180D_worst_low: 6,600
180D_MAE: -26.7%
extended_2025_peak_high: 9,750
```

### Interpretation

This is the clearest false-positive in the set.

A low-PBR / value-up / securities beta model could promote the stock too early, but the forward path gave almost no usable MFE and then suffered a large drawdown.

C21 read:

```text
Stage2-Watch: possible
Stage2-Actionable: blocked unless company-specific capital return / ROE bridge appears
Stage3-Green: blocked
hard_4c_candidate: yes
```

### Raw component stress test

```text
raw_component_score_proxy:
  financial_valueup_policy_beta: medium
  low_pbr_value_signal: medium
  shareholder_return_visibility: low_to_medium
  roe_visibility: low
  brokerage_volume_sensitivity: medium
  evidence_quality: low
  price_confirmation: weak
  drawdown_penalty: high
```

Residual contribution:

```text
This case shows that "financial value-up beta" alone can produce a serious C21 Stage2 false positive in securities names.
```

---

## 8. Case 3 — 039490 키움증권

```yaml
case_id: C21_R6L90_039490_2024_02_28
symbol: "039490"
name: "키움증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 124900
classification: watch_or_cap_case_brokerage_beta_needs_trading_revenue_bridge
calibration_usable: true
```

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 124,900
2024-02-29: high 128,600 / close 125,700
2024-03-14: high 136,500 / close 134,700
2024-07-11: high 146,200 / close 144,600
2024-07-16: high 146,400 / close 143,100
2024-08-05: low 115,200 / close 118,500
2025-03-19: high 136,000 / close 133,900
2025-04-07: low 107,000 / close 109,200
```

Approximate path from entry close:

```text
entry_close: 124,900
180D_peak_high: 146,400
180D_MFE: +17.2%
180D_worst_low: 115,200
180D_MAE: -7.8%
extended_2025_low: 107,000
```

### Interpretation

This is not a hard failure like 미래에셋증권. But it is not a clean C21 Green either.

The stock had some MFE and did not collapse during the 180D window. However, the return profile was not strong enough to justify treating generic securities-sector beta as a fully validated rerating. It needs an explicit trading-volume / retail-flow / brokerage earnings bridge.

C21 read:

```text
Stage2-Watch or Stage2-Yellow: valid
Stage2-Actionable: requires stronger brokerage revenue bridge
Stage3-Green: cap unless ROE/capital-return evidence is explicit
hard_4c: no within 180D
```

### Raw component stress test

```text
raw_component_score_proxy:
  financial_valueup_policy_beta: medium
  brokerage_volume_sensitivity: high
  shareholder_return_visibility: medium
  roe_visibility: medium
  evidence_quality: medium
  price_confirmation: medium
  drawdown_penalty: medium
```

Residual contribution:

```text
This case calibrates the middle zone: brokerage beta can be real, but without a stronger revenue/ROE bridge it should be capped below Green.
```

---

## 9. Aggregate calibration takeaways

```text
positive_case_count: 1
watch_or_cap_case_count: 1
hard_4c_candidate_count: 1
```

The three cases form a useful C21 securities mini-grid:

```text
NH투자증권:
  low-MAE positive path; C21 Actionable can work if brokerage/capital-return bridge exists.

미래에셋증권:
  shallow MFE + large MAE; low-PBR securities beta can become hard 4C without bridge.

키움증권:
  middle-zone watch/cap case; retail brokerage sensitivity needs revenue/ROE confirmation before Green.
```

This is a different residual error from bank CET1 or insurance CSM cases.

---

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L90_005940_2024_02_28","scheduled_round":"R6","scheduled_loop":90,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"005940","name":"NH투자증권","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":11550,"peak_high":14400,"peak_date":"2024-08-01","worst_low":11190,"worst_low_date":"2024-04-01","mfe_pct":24.7,"mae_pct":-3.1,"classification":"positive_capital_return_brokerage_bridge","calibration_usable":true,"evidence_family":"securities_valueup_brokerage_roe_capital_return_bridge","residual_error":"none_for_actionable_if_business_bridge_present","shadow_rule_candidate":"allow_actionable_when_low_mae_and_roe_payout_brokerage_bridge_confirm"}
{"row_type":"case","case_id":"C21_R6L90_006800_2024_02_28","scheduled_round":"R6","scheduled_loop":90,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"006800","name":"미래에셋증권","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":9010,"peak_high":9160,"peak_date":"2024-02-29","worst_low":6600,"worst_low_date":"2024-08-05","mfe_pct":1.7,"mae_pct":-26.7,"classification":"hard_4c_candidate_low_pbr_securities_beta_without_bridge","calibration_usable":true,"evidence_family":"low_pbr_financial_beta_without_roe_or_capital_return_bridge","residual_error":"stage2_false_positive_if_financial_valueup_beta_overweighted","shadow_rule_candidate":"block_green_and_actionable_when_securities_low_pbr_beta_lacks_roe_payout_revenue_bridge"}
{"row_type":"case","case_id":"C21_R6L90_039490_2024_02_28","scheduled_round":"R6","scheduled_loop":90,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","symbol":"039490","name":"키움증권","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":124900,"peak_high":146400,"peak_date":"2024-07-16","worst_low":115200,"worst_low_date":"2024-08-05","mfe_pct":17.2,"mae_pct":-7.8,"classification":"watch_or_cap_case_brokerage_beta_needs_trading_revenue_bridge","calibration_usable":true,"evidence_family":"brokerage_volume_beta_needs_revenue_roe_bridge","residual_error":"middle_zone_can_be_overpromoted_to_green","shadow_rule_candidate":"cap_at_yellow_until_brokerage_revenue_roe_capital_return_bridge_confirms"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":90,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SECURITIES_BROKERAGE_VALUEUP_ROE_TRADING_VOLUME_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA","case_count":3,"positive_case_count":1,"watch_or_cap_case_count":1,"counterexample_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":90,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_SECURITIES_BROKERAGE_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21 securities/brokerage names, low-PBR financial value-up beta is not enough for Stage2-Actionable or Stage3-Green. Require brokerage revenue, trading turnover sensitivity, IB/WM earnings quality, ROE visibility, and shareholder-return bridge. If MFE is shallow and MAE is material, route to false-positive or hard-4C candidate.","expected_effect":"Reduce securities-sector low-PBR false positives while preserving names with real capital-return and brokerage earnings bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":90,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"securities_low_pbr_beta_false_positive_guard","contribution":"Adds three non-bank C21 financial cases. Separates true securities capital-return / brokerage revenue bridge from generic financial value-up beta.","do_not_count_as_global_weight_delta":true}
```

---

## 11. Proposed canonical-archetype shadow rule

```text
C21_SECURITIES_BROKERAGE_BRIDGE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
AND company_type in [securities, brokerage, capital_market_financial]:

  Do not open Stage3-Green from:
    - low PBR alone
    - Korea Value-up headline alone
    - broad financial sector beta
    - short-term KOSPI/KOSDAQ turnover rebound alone

  Require at least two of:
    - brokerage commission revenue expansion
    - market turnover / margin loan / retail activity bridge
    - IB / WM pipeline visibility
    - ROE improvement or earnings revision
    - buyback / dividend / payout policy
    - balance-sheet efficiency / risk-asset discipline
    - low MAE price confirmation after trigger

  If MFE < 10% and MAE < -20%:
    route to hard-4C candidate.

  If MFE is 10~20% but business bridge is weak:
    cap at Watch / Yellow, not Green.

  If MFE > 20% and MAE remains small:
    Actionable may be allowed, but Green still requires ROE/capital-return bridge.
```

---

## 12. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_90_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 securities/brokerage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_SECURITIES_BROKERAGE_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 securities cases agree, consider implementing a canonical guard that:
   - blocks low-PBR / value-up securities beta from Green without revenue/ROE/capital-return bridge,
   - allows Actionable only when MFE is supported by low MAE and business bridge,
   - routes shallow-MFE / high-MAE securities cases to hard-4C or false-positive guard.

Expected next schedule:
completed_round = R6
completed_loop = 90
next_round = R7
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```
