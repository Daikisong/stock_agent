# E2R Stock-Web v12 Residual Research — R6 / Loop 96

```yaml
scheduled_round: R6
scheduled_loop: 96
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE

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
life_insurance_case_count: 2
nonlife_insurance_case_count: 1
valueup_confound_caveat_count: 3
reserve_capital_return_bridge_missing_count: 2
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 96
next_round: R7
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_96_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 96
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
```

This run returns to C22 after the R6 branch cycle, but avoids the C22 top-covered names and avoids the immediately previous C21 insurance/brokerage set:

```text
loop95 avoid: 016610, 001450, 085620
```

The selected fine branch is:

```text
life and non-life insurance
rate cycle, reserve quality, capital buffer, K-ICS/RBC style capital room,
shareholder-return execution, and price survival
vs generic Value-up insurance label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
rows: 37
symbols: 12
date_range: 2024-01-24~2024-08-22
good/bad S2: 10/11
4B/4C: 2/0
URL pending/proxy: 10/10
top covered symbols:
  000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
```

Selected symbols:

```text
032830 삼성생명
088350 한화생명
000400 롯데손해보험
```

They avoid the C22 top-covered list and recent R6 loop95 C21 names:

```text
C22 top-covered avoid:
  000370, 003690, 082640, 000540, 000810, 005830

R6 loop95 avoid:
  016610, 001450, 085620
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
032830: same archetype, new symbol, life-insurance rate/capital-return positive with Green cap
088350: same archetype, new symbol, life-insurance Value-up local burst followed by high-MAE 4B failure
000400: same archetype, new symbol, non-life insurance late spike hard-4C without reserve/capital trust survival
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
032830 삼성생명
  profile: atlas/symbol_profiles/032/032830.json
  first_date: 2010-05-12
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,883
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

088350 한화생명
  profile: atlas/symbol_profiles/088/088350.json
  name history:
    대한생명 until 2012-10-16
    한화생명 from 2012-10-17
  first_date: 2010-03-17
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,922
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

000400 롯데손해보험
  profile: atlas/symbol_profiles/000/000400.json
  name history:
    대한화재 until 2008-03-19
    롯데손해보험 from 2008-03-20
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,717
  non_tradable_zero_volume rows: 48
  corporate_action_candidate_dates:
    2001-02-23, 2002-01-28, 2006-05-17, 2012-12-26, 2015-06-25, 2019-10-25
  2024 entry~D+180 contamination: none
  caveat:
    historical raw discontinuity / row-presence caveat exists outside the 2024 validation window.
```

---

## 4. Archetype residual problem

C22 is about insurance rate cycle, reserve quality, capital buffer, and the conversion of Value-up or rate-cycle salience into durable shareholder economics. It is not a generic "insurance stock is low PBR" archetype.

The model can over-score:

```text
Korea Value-up policy headline
life-insurance low-PBR label
non-life rate-cycle label
interest-rate or duration sensitivity
IFRS17 / CSM / reserve-quality simplification
dividend or capital-return rumor
one-week insurance-stock volume spike
```

The C22 bridge must be stricter:

```text
insurance rate / reserve / capital event
  -> product mix and earnings quality
  -> reserve adequacy and liability-duration risk
  -> loss-ratio or claim-cost control where relevant
  -> K-ICS / RBC / capital buffer
  -> ALM and interest-rate sensitivity
  -> dividend / buyback / cancellation execution
  -> recurring ROE and earnings stability
  -> price survival after the first Value-up or rate-cycle spike
```

An insurance thesis is like a reservoir behind a dam. The headline says the water level is high, but C22 asks whether the dam is sound: reserves, capital ratios, claims, duration, and shareholder-return gates must hold before cash can safely flow to equity holders.

---

## 5. Case 1 — 032830 삼성생명

```yaml
case_id: C22_R6L96_032830_2024_02_01
symbol: "032830"
name: "삼성생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 76000
classification: positive_life_insurance_reserve_capital_return_valueup_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

삼성생명 is the constructive C22 control in this set.

The useful C22 read is not simply:

```text
보험주 / 저PBR 금융주가 강하다
```

It is:

```text
large life-insurance capital base
  -> Value-up discount compression
  -> capital buffer and shareholder-return optionality
  -> price survival after the initial rally
```

The forward path delivered a strong MFE and the drawdown remained controlled. That supports positive classification. However, even here, the model should not open unrestricted Green unless reserve quality, capital buffer, ALM/rate sensitivity, and actual shareholder-return execution are explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 76,800 / close 76,000
2024-02-08: high 83,400 / close 83,000
2024-02-23: high 97,300 / close 95,600
2024-02-28: high 102,900 / close 102,900
2024-03-08: high 108,500 / close 105,100
2024-04-17: low 77,300 / close 78,000
2024-08-05: low 82,500 / close 84,000
2024-10-22: high 103,300 / close 102,800
```

Approximate path from entry close:

```text
entry_close: 76,000
peak_high: 108,500
MFE: +42.8%
worst_low_after_entry: 73,600
MAE: -3.2%
```

### Interpretation

This is a C22 positive with Green cap:

```text
Stage2-Actionable: possible if reserve/capital buffer, ALM, ROE, and return-execution bridge are explicit.
Stage3-Green: possible only with fresh capital-return and reserve-quality evidence.
Local 4B: monitor after +40% MFE if Value-up rerating outruns execution.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  life_insurance_relevance: very_high
  valueup_discount_compression: high
  reserve_quality_bridge: medium_high
  capital_buffer_bridge: high
  shareholder_return_bridge: medium
  price_confirmation: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 088350 한화생명

```yaml
case_id: C22_R6L96_088350_2024_02_01
symbol: "088350"
name: "한화생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3355
classification: local_burst_life_insurance_valueup_rate_reserve_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

한화생명 is the life-insurance local-burst / 4B failure.

The setup looked plausible:

```text
life-insurance low-PBR / Value-up label
rate and duration sensitivity
capital-return optionality
high-volume early February insurance rally
```

The forward path produced a meaningful early MFE, so the original entry is not a pure hard-4C. But the later path failed price survival. The model should classify it as local 4B unless reserve quality, ALM, capital buffer, and shareholder-return execution keep refreshing.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,585 / close 3,355
2024-02-05: high 3,740 / close 3,690
2024-02-13: high 3,815 / close 3,550
2024-04-12: low 2,620 / close 2,630
2024-08-05: low 2,700 / close 2,730
2024-10-08: low 2,185 / close 2,235
2024-10-25: low 2,845 / close 2,890
```

Approximate path from entry close:

```text
entry_close: 3,355
peak_high: 3,815
MFE: +13.7%
worst_low_after_entry: 2,185
MAE: -34.9%
```

### Interpretation

This is a local burst / 4B failure:

```text
Stage2-Watch: valid from life-insurance and Value-up relevance.
Stage2-Actionable: possible only if reserve quality, ALM, capital buffer, and shareholder-return bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary for the original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  life_insurance_valueup_label: high
  rate_cycle_relevance: medium_high
  reserve_quality_bridge: weak_to_medium
  capital_buffer_bridge: medium
  shareholder_return_bridge: weak
  price_confirmation: medium_initial
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 7. Case 3 — 000400 롯데손해보험

```yaml
case_id: C22_R6L96_000400_2024_04_23
symbol: "000400"
name: "롯데손해보험"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE
trigger_date: 2024-04-23
entry_date: 2024-04-23
entry_price_basis: close
entry_price: 3850
classification: hard_4c_candidate_nonlife_insurance_late_spike_without_reserve_capital_return_trust_survival
calibration_usable: true
```

### Evidence interpretation

롯데손해보험 is the hard C22 guardrail.

The selected trigger is a late-spike entry after earlier insurance-rally episodes. The label can fool a financial model:

```text
non-life insurance / rate-cycle label
M&A or capital-return optionality
loss-ratio / reserve normalization hope
high-volume insurance-stock spike
```

But from the selected late-April close, the price path did not validate reserve quality, capital buffer, loss-ratio stability, or shareholder-return execution. MFE was shallow and later MAE crossed the hard-failure zone.

### Price path

Key Stock-Web rows:

```text
2024-04-23: high 3,885 / close 3,850
2024-04-25: high 4,035 / close 3,745
2024-05-02: low 3,350 / close 3,355
2024-08-05: low 2,515 / close 2,560
2024-10-10: low 2,175 / close 2,180
2024-10-25: low 2,150 / close 2,195
```

Approximate path from late entry close:

```text
entry_close: 3,850
peak_high_after_entry: 4,035
MFE: +4.8%
worst_low_after_entry: 2,150
MAE: -44.2%
```

### Interpretation

This is a hard C22 false-positive:

```text
Stage2-Watch: possible from non-life insurance and rate-cycle relevance.
Stage2-Actionable: blocked unless reserve adequacy, loss-ratio, capital buffer, and shareholder-return bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE after a late spike.
Row/tradeability caveat: historical raw discontinuity / zero-volume caveat exists outside the 2024 window.
```

The lesson is that non-life insurance spike heat is not reserve/capital-return survival.

### Stress-test components

```text
raw_component_score_proxy:
  nonlife_insurance_relevance: high
  rate_cycle_label: medium_high
  reserve_loss_ratio_bridge: weak
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
life_insurance_case_count: 2
nonlife_insurance_case_count: 1
valueup_confound_caveat_count: 3
reserve_capital_return_bridge_missing_count: 2
row_presence_or_tradeability_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C22 insurance grid:

```text
032830 삼성생명:
  large life-insurance positive;
  strong MFE and controlled MAE, but Green requires reserve/capital-return evidence.

088350 한화생명:
  life-insurance Value-up local burst;
  meaningful MFE first, then high MAE, local 4B failure.

000400 롯데손해보험:
  non-life insurance late spike failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C22 is not "insurance stock is cheap."
C22 is "reserve quality, capital buffer, ALM/rate risk, loss-ratio control, recurring ROE, and shareholder-return execution are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C22_R6L96_032830_2024_02_01","scheduled_round":"R6","scheduled_loop":96,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE","symbol":"032830","name":"삼성생명","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":76000,"peak_high":108500,"peak_date":"2024-03-08","worst_low_after_entry":73600,"worst_low_after_entry_date":"2024-02-02","mfe_pct":42.8,"mae_pct":-3.2,"classification":"positive_life_insurance_reserve_capital_return_valueup_bridge_with_green_cap","calibration_usable":true,"evidence_family":"life_insurance_valueup_reserve_quality_capital_buffer_shareholder_return_bridge","residual_error":"positive_insurance_valueup_path_still_requires_green_cap_without_refreshed_reserve_capital_return_evidence","shadow_rule_candidate":"allow_actionable_when_reserve_capital_buffer_and_return_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C22_R6L96_088350_2024_02_01","scheduled_round":"R6","scheduled_loop":96,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE","symbol":"088350","name":"한화생명","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3355,"peak_high":3815,"peak_date":"2024-02-13","worst_low_after_entry":2185,"worst_low_after_entry_date":"2024-10-08","mfe_pct":13.7,"mae_pct":-34.9,"classification":"local_burst_life_insurance_valueup_rate_reserve_label_high_mae_4b_failure","calibration_usable":true,"evidence_family":"life_insurance_valueup_rate_reserve_label_without_sustained_capital_return_survival","residual_error":"life_insurance_valueup_label_can_create_mfe_but_fail_green_without_reserve_alm_and_return_execution","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_life_insurance_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C22_R6L96_000400_2024_04_23","scheduled_round":"R6","scheduled_loop":96,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE","symbol":"000400","name":"롯데손해보험","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":3850,"peak_high":4035,"peak_date":"2024-04-25","worst_low_after_entry":2150,"worst_low_after_entry_date":"2024-10-25","mfe_pct":4.8,"mae_pct":-44.2,"classification":"hard_4c_candidate_nonlife_insurance_late_spike_without_reserve_capital_return_trust_survival","calibration_usable":true,"row_presence_or_tradeability_caveat":true,"evidence_family":"nonlife_insurance_rate_cycle_late_spike_without_reserve_loss_ratio_capital_return_trust_bridge","residual_error":"nonlife_insurance_late_spike_can_fail_when_reserve_quality_capital_buffer_and_shareholder_return_bridge_missing","shadow_rule_candidate":"route_nonlife_insurance_late_spike_to_hard_4c_if_mfe_shallow_mae_large_and_reserve_capital_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":96,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_AND_NONLIFE_INSURANCE_RATE_RESERVE_CAPITAL_BUFFER_SHAREHOLDER_RETURN_BRIDGE_VS_VALUEUP_INSURANCE_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"life_insurance_case_count":2,"nonlife_insurance_case_count":1,"valueup_confound_caveat_count":3,"reserve_capital_return_bridge_missing_count":2,"row_presence_or_tradeability_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":96,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","rule_id":"C22_RESERVE_CAPITAL_RETURN_ALM_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C22, do not open Stage2-Actionable or Stage3-Green from Korea Value-up, low-PBR insurance, life-insurance label, non-life rate-cycle label, duration/rate sensitivity, IFRS17/CSM simplification, dividend or capital-return rumor, or one-week insurance-stock volume spike alone. Require product mix and earnings quality, reserve adequacy and liability-duration risk control, loss-ratio or claim-cost control where relevant, K-ICS/RBC/capital buffer, ALM and interest-rate sensitivity, dividend/buyback/cancellation execution, recurring ROE and earnings stability, and post-trigger price survival. Large life-insurance positives with strong MFE and low MAE may be capped Actionable when reserve/capital-return bridge is explicit, but Green requires refreshed execution. Life-insurance Value-up bursts with meaningful MFE followed by high MAE should remain local 4B, not Green. Non-life insurance late spikes with shallow MFE and high MAE should route to hard-4C when reserve quality, loss ratio, capital buffer, and return execution are missing.","expected_effect":"Preserve true insurance rate/reserve/capital-return positives while reducing low-PBR insurance and late-spike false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":96,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"reserve_capital_return_alm_guard","contribution":"Adds one large life-insurance positive, one life-insurance local 4B failure, and one non-life insurance hard-4C counterexample to calibrate C22 reserve quality, ALM, capital buffer, recurring ROE, and shareholder-return requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C22_RESERVE_CAPITAL_RETURN_ALM_BRIDGE_REQUIRED

IF canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:

  Do not open Stage3-Green from:
    - Korea Value-up policy headline alone
    - low-PBR insurance label alone
    - life-insurance label alone
    - non-life rate-cycle label alone
    - interest-rate / duration sensitivity alone
    - IFRS17 / CSM / reserve-quality simplification alone
    - dividend or capital-return rumor alone
    - one-week insurance-stock volume spike alone

  Require at least two of:
    - product mix and earnings quality
    - reserve adequacy / liability-duration risk control
    - loss-ratio / claim-cost control where relevant
    - K-ICS / RBC / capital buffer
    - ALM / interest-rate sensitivity control
    - dividend / buyback / cancellation execution
    - recurring ROE and earnings stability
    - low-MAE post-trigger price survival
    - fresh evidence after the Value-up or rate-cycle headline

  If MFE < 8% and MAE < -30%:
    route to C22 hard-4C candidate.

  If MFE > 10% but later MAE < -30%:
    preserve as local 4B / event burst, not Green, unless reserve/capital-return evidence refreshes.

  If MFE is large but the catalyst is broad Value-up:
    cap Green until company-specific reserve, ALM, and capital-return execution is proven.

  Distinguish:
    - insurance names where reserves, capital buffer, ALM, and shareholder returns support recurring ROE
    - from cheap insurance labels where rate or policy heat does not survive reserve and capital gates.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_96_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C22 insurance rate/reserve/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C22_RESERVE_CAPITAL_RETURN_ALM_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C22 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C22 cases agree, consider implementing a canonical guard that:
   - blocks insurance-label Green without reserve/capital-buffer/ALM/shareholder-return bridge,
   - preserves life-insurance positives only with price survival and fresh execution evidence,
   - caps broad Value-up insurance bursts at local 4B when bridge is stale,
   - routes shallow-MFE/high-MAE non-life late spikes to hard-4C,
   - applies row-presence/tradeability trust caps.

Expected next schedule:
completed_round = R6
completed_loop = 96
next_round = R7
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 96
next_round = R7
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
