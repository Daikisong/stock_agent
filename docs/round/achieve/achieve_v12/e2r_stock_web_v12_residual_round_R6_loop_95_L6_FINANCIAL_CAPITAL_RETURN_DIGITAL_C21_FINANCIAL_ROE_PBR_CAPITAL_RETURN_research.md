# E2R Stock-Web v12 Residual Research — R6 / Loop 95

```yaml
scheduled_round: R6
scheduled_loop: 95
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE

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
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
name_change_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 95
next_round: R7
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 95
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
```

This run returns to C21 but avoids the previous loop94 bank-holding branch:

```text
loop94 avoid: 055550, 316140, 001510
```

The selected fine branch is:

```text
insurance / brokerage Value-up
ROE, reserve, capital-return, trading-income and discount-compression bridge
vs generic financial-label spike
```

A pure C22 set was considered first, but the non-duplicative insurance universe outside top-covered and recent C22 names was too narrow. R6 permits general C21/C22 financial research, so the final selection uses C21 and treats insurance/brokerage names through the ROE/PBR/capital-return lens.

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
016610 DB금융투자 / DB증권
001450 현대해상
085620 미래에셋생명
```

They avoid the C21 top-covered list and avoid recent R6 loop94 names:

```text
055550, 316140, 001510
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
016610: same archetype, new symbol, brokerage Value-up / capital-market beta positive with 4B after large MFE
001450: same archetype, new symbol, P&C insurance ROE/rate-cycle label Watch cap without durable capital-return bridge
085620: same archetype, new symbol, life-insurance late spike hard-4C without reserve/ROE/capital-return survival
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
016610 DB금융투자 / DB증권
  profile: atlas/symbol_profiles/016/016610.json
  name history:
    동부증권 until 2017-11-20
    DB금융투자 from 2017-11-21 to 2025-04-17
    DB증권 from 2025-04-18
  selected 2024 trigger name:
    DB금융투자
  current/latest name:
    DB증권
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,765
  corporate_action_candidate_dates:
    1997-03-29, 2007-12-21
  2024 entry~D+180 contamination: none

001450 현대해상
  profile: atlas/symbol_profiles/001/001450.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,761
  corporate_action_candidate_dates:
    2004-07-13
  2024 entry~D+180 contamination: none

085620 미래에셋생명
  profile: atlas/symbol_profiles/085/085620.json
  first_date: 2015-07-08
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,606
  corporate_action_candidate_dates:
    2018-03-23
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C21 is about ROE, PBR, capital return, and the execution path from financial-sector Value-up rhetoric to shareholder economics. It is not a generic low-PBR financial label.

The model can over-score:

```text
Korea Value-up policy
low-PBR financial label
insurance rate-cycle label
brokerage beta / trading-income label
dividend-yield label
one-week financial-stock volume spike
```

The C21 bridge must be stricter:

```text
financial Value-up / ROE-PBR event
  -> company-specific ROE quality
  -> reserve / credit / duration risk control where relevant
  -> CET1, RBC/K-ICS, or capital buffer
  -> dividend / buyback / cancellation execution
  -> earnings stability
  -> discount compression
  -> price survival after the first financial rally
```

A financial Value-up trade is like opening a vault. Low PBR says the vault may be underpriced, but C21 asks whether earnings fill it, capital rules allow cash out, and management actually returns that cash to shareholders.

---

## 5. Case 1 — 016610 DB금융투자 / DB증권

```yaml
case_id: C21_R6L95_016610_2024_02_01
symbol: "016610"
name_at_trigger: "DB금융투자"
current_or_latest_name: "DB증권"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 4210
classification: positive_brokerage_valueup_capital_market_beta_with_4b_after_large_mfe
calibration_usable: true
```

### Evidence interpretation

DB금융투자 is the constructive C21 control in this set.

The useful C21 read is not simply:

```text
증권주 / 저PBR 금융주가 움직였다
```

It is:

```text
brokerage / capital-market beta
  -> trading-income and market-activity optionality
  -> Value-up financial discount compression
  -> controlled downside after entry
  -> strong later price confirmation
```

The price path worked well from the early Value-up window. It produced large MFE and avoided a hard drawdown. However, after a large rerating it still needs 4B discipline unless fresh earnings and capital-return evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,310 / close 4,210
2024-02-19: high 4,665 / close 4,605
2024-08-05: low 3,915 / close 4,000
2024-09-06: high 6,280 / close 5,900
2024-09-13: high 6,130 / close 6,100
2024-10-14: low 5,210 / close 5,290
```

Approximate path from entry close:

```text
entry_close: 4,210
peak_high: 6,280
MFE: +49.2%
worst_low_after_entry: 3,915
MAE: -7.0%
```

### Interpretation

This is a C21 positive with 4B after rerating:

```text
Stage2-Actionable: possible if ROE, earnings stability, capital buffer, and shareholder-return bridge are explicit.
Stage3-Green: blocked without refreshed return-execution and earnings-quality evidence after the large move.
Local 4B: required after +40% MFE unless fresh evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  brokerage_beta_relevance: high
  valueup_discount_compression: high
  earnings_quality_bridge: medium
  capital_return_bridge: weak_to_medium
  price_confirmation: high
  drawdown_penalty: low
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 001450 현대해상

```yaml
case_id: C21_R6L95_001450_2024_02_01
symbol: "001450"
name: "현대해상"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 35450
classification: watch_cap_pnc_insurance_rate_cycle_low_pbr_label_without_durable_capital_return_bridge
calibration_usable: true
```

### Evidence interpretation

현대해상 is the Watch/Yellow cap.

The label is highly relevant:

```text
P&C insurance
rate cycle and loss ratio
financial Value-up / low-PBR relevance
capital-return expectation
```

But the forward path did not validate Actionable/Green from the 2024-02-01 trigger. The post-trigger MFE was shallow, and the stock later drew down materially. That does not mean the business is irrelevant. It means the model must require more than an insurance-rate or low-PBR label.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 36,150 / close 35,450
2024-02-05: high 36,800 / close 35,750
2024-02-26: low 31,800 / close 32,200
2024-04-12: low 28,700 / close 28,750
2024-07-31: high 36,750 / close 36,050
2024-08-05: low 31,500 / close 32,000
2024-10-24: low 29,800 / close 30,000
```

Approximate path from entry close:

```text
entry_close: 35,450
peak_high: 36,800
MFE: +3.8%
worst_low_after_entry: 28,700
MAE: -19.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from insurance-rate and financial Value-up relevance.
Stage2-Actionable: blocked unless reserve, loss-ratio, capital buffer, and shareholder-return bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not primary because MAE did not cross hard threshold.
```

The lesson is that an insurance rate-cycle label is not capital-return execution.

### Stress-test components

```text
raw_component_score_proxy:
  pnc_insurance_relevance: high
  rate_cycle_label: high
  reserve_loss_ratio_bridge: weak_to_medium
  capital_return_bridge: weak_to_medium
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 085620 미래에셋생명

```yaml
case_id: C21_R6L95_085620_2024_02_05
symbol: "085620"
name: "미래에셋생명"
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE
trigger_date: 2024-02-05
entry_date: 2024-02-05
entry_price_basis: close
entry_price: 6390
classification: hard_4c_candidate_life_insurance_valueup_late_spike_without_reserve_roe_capital_return_survival
calibration_usable: true
```

### Evidence interpretation

미래에셋생명 is the hard C21 guardrail.

The trap shape is clear:

```text
life-insurance / low-PBR financial label
  -> Value-up policy attention
  -> high-volume early February spike
  -> model can mistake spike for sustainable ROE/capital-return rerating
```

From the selected late close, the stock produced almost no incremental MFE and later drew down more than 30%. This should route to hard 4C unless reserve, ROE, capital buffer, and shareholder-return bridge are explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-05: high 6,490 / close 6,390
2024-02-06: high 6,500 / close 6,240
2024-02-13: high 6,420 / close 5,950
2024-02-23: low 5,210 / close 5,300
2024-03-29: low 4,445 / close 4,500
2024-04-09: high 5,360 / close 4,790
2024-08-05: low 4,660 / close 4,950
```

Approximate path from entry close:

```text
entry_close: 6,390
peak_high_after_entry: 6,500
MFE: +1.7%
worst_low_after_entry: 4,445
MAE: -30.4%
```

### Interpretation

This is a hard C21 false-positive:

```text
Stage2-Watch: possible from life-insurance and low-PBR Value-up relevance.
Stage2-Actionable: blocked unless reserve, ROE, capital buffer, and capital-return bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that life-insurance low-PBR spike is not reserve-quality or shareholder-return execution.

### Stress-test components

```text
raw_component_score_proxy:
  life_insurance_valueup_label: high
  low_pbr_financial_relevance: high
  reserve_quality_bridge: weak
  capital_buffer_bridge: weak_to_medium
  shareholder_return_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
name_change_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C21 insurance/brokerage grid:

```text
016610 DB금융투자 / DB증권:
  brokerage Value-up / capital-market beta positive;
  large MFE and controlled MAE, but 4B required after rerating.

001450 현대해상:
  P&C insurance rate-cycle / low-PBR label;
  shallow MFE and material MAE, Watch/Yellow cap.

085620 미래에셋생명:
  life-insurance Value-up late spike failed;
  shallow MFE and -30%+ MAE, hard 4C.
```

Shared rule:

```text
C21 is not "financial stock is low PBR."
C21 is "ROE quality, reserve/credit/rate risk, capital buffer, shareholder-return execution, and discount compression are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C21_R6L95_016610_2024_02_01","scheduled_round":"R6","scheduled_loop":95,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE","symbol":"016610","name_at_trigger":"DB금융투자","current_or_latest_name":"DB증권","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":4210,"peak_high":6280,"peak_date":"2024-09-06","worst_low_after_entry":3915,"worst_low_after_entry_date":"2024-08-05","mfe_pct":49.2,"mae_pct":-7.0,"classification":"positive_brokerage_valueup_capital_market_beta_with_4b_after_large_mfe","calibration_usable":true,"evidence_family":"brokerage_valueup_capital_market_activity_roe_discount_compression_bridge","residual_error":"positive_financial_valueup_path_requires_4b_after_large_mfe_without_fresh_earnings_return_execution","shadow_rule_candidate":"preserve_positive_when_financial_roe_discount_compression_and_price_survival_confirm_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C21_R6L95_001450_2024_02_01","scheduled_round":"R6","scheduled_loop":95,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE","symbol":"001450","name":"현대해상","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":35450,"peak_high":36800,"peak_date":"2024-02-05","worst_low_after_entry":28700,"worst_low_after_entry_date":"2024-04-12","mfe_pct":3.8,"mae_pct":-19.0,"classification":"watch_cap_pnc_insurance_rate_cycle_low_pbr_label_without_durable_capital_return_bridge","calibration_usable":true,"evidence_family":"pnc_insurance_rate_cycle_low_pbr_label_without_reserve_loss_ratio_capital_return_bridge","residual_error":"insurance_rate_cycle_label_can_overpromote_without_reserve_quality_and_shareholder_return_execution","shadow_rule_candidate":"cap_insurance_rate_cycle_label_at_watch_yellow_if_mfe_shallow_and_capital_return_bridge_missing"}
{"row_type":"case","case_id":"C21_R6L95_085620_2024_02_05","scheduled_round":"R6","scheduled_loop":95,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE","symbol":"085620","name":"미래에셋생명","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":6390,"peak_high":6500,"peak_date":"2024-02-06","worst_low_after_entry":4445,"worst_low_after_entry_date":"2024-03-29","mfe_pct":1.7,"mae_pct":-30.4,"classification":"hard_4c_candidate_life_insurance_valueup_late_spike_without_reserve_roe_capital_return_survival","calibration_usable":true,"evidence_family":"life_insurance_low_pbr_valueup_late_spike_without_reserve_roe_capital_return_bridge","residual_error":"life_insurance_valueup_spike_can_fail_when_reserve_quality_and_shareholder_return_execution_missing","shadow_rule_candidate":"route_life_insurance_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_reserve_return_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":95,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"INSURANCE_BROKERAGE_VALUEUP_ROE_CAPITAL_RETURN_BRIDGE_VS_FINANCIAL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"name_change_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":95,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","rule_id":"C21_FINANCIAL_ROE_RESERVE_CAPITAL_RETURN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C21 insurance/brokerage/financial Value-up cases, do not open Stage2-Actionable or Stage3-Green from Korea Value-up, low-PBR financial, insurance rate-cycle, brokerage beta, dividend-yield, or one-week financial-stock rally labels alone. Require company-specific ROE quality, reserve/credit/duration or loss-ratio risk control where relevant, CET1/RBC/K-ICS/capital buffer, dividend/buyback/cancellation execution, earnings stability, valuation discount compression, and post-trigger price survival. Brokerage positives with large MFE should attach local 4B unless fresh earnings and capital-return evidence appears. Insurance labels with shallow MFE should cap at Watch/Yellow without reserve-quality and shareholder-return evidence. Life-insurance late spikes with shallow MFE and high MAE should route to hard-4C when reserve, ROE, and capital-return bridge are missing.","expected_effect":"Preserve true financial Value-up positives with ROE/capital-return evidence while reducing insurance/brokerage low-PBR label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":95,"canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","residual_type":"financial_roe_reserve_capital_return_guard","contribution":"Adds one brokerage Value-up positive with 4B-after-large-MFE, one P&C insurance Watch cap, and one life-insurance hard-4C counterexample to calibrate C21 ROE, reserve, capital-buffer, shareholder-return, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C21_FINANCIAL_ROE_RESERVE_CAPITAL_RETURN_BRIDGE_REQUIRED

IF canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:

  Do not open Stage3-Green from:
    - Korea Value-up policy headline alone
    - low-PBR financial label alone
    - insurance rate-cycle label alone
    - brokerage beta / trading-income label alone
    - dividend-yield label alone
    - one-week financial-stock volume spike alone

  Require at least two of:
    - company-specific ROE quality
    - reserve / duration / credit / loss-ratio risk control where relevant
    - CET1 / RBC / K-ICS / capital buffer
    - dividend / buyback / cancellation execution
    - earnings stability
    - valuation discount compression
    - low-MAE post-trigger price survival
    - fresh evidence after the Value-up headline

  If MFE < 5% and MAE < -30%:
    route to C21 hard-4C candidate.

  If MFE > 40%:
    preserve positive classification but attach local 4B unless earnings/capital-return evidence refreshes the thesis.

  If MFE is shallow and the bridge is insurance-rate label only:
    cap at Watch/Yellow unless reserve quality and shareholder-return evidence are explicit.

  Distinguish:
    - financial names where ROE and capital-return mechanics are visible
    - from low-PBR insurance/brokerage labels where policy does not reach shareholder economics.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_95_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C21 insurance/brokerage ROE/PBR/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C21_FINANCIAL_ROE_RESERVE_CAPITAL_RETURN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C21 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C21 cases agree, consider implementing a canonical guard that:
   - blocks financial-label Green without ROE/reserve/capital-buffer/shareholder-return bridge,
   - preserves brokerage positives only with price survival and fresh earnings evidence,
   - attaches local 4B after large MFE,
   - caps insurance rate-cycle labels at Watch/Yellow without reserve/capital-return evidence,
   - routes shallow-MFE/high-MAE life-insurance late spikes to hard-4C.

Expected next schedule:
completed_round = R6
completed_loop = 95
next_round = R7
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 95
next_round = R7
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
