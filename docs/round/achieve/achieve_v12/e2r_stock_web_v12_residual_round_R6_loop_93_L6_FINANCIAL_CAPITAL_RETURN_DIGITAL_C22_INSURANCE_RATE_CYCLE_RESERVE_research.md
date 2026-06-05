# E2R Stock-Web v12 Residual Research — R6 / Loop 93

```yaml
scheduled_round: R6
scheduled_loop: 93
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 93
next_round: R7
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_93_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 93
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

R6 hard gate requires:

```text
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
```

Recent R6 branch usage already covered:

```text
loop89: C22_INSURANCE_RATE_CYCLE_RESERVE
loop90: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
loop91: C22_INSURANCE_RATE_CYCLE_RESERVE
loop92: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

This run returns to C22, but avoids the heavily covered insurance names and uses a different fine branch:

```text
life insurance Value-up / CSM / K-ICS capital buffer
vs M&A/speculative insurer label
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
088350 한화생명
032830 삼성생명
000400 롯데손해보험
```

They avoid the C22 top-covered names and avoid the most recent R6 loop92 C21 names:

```text
029780, 175330, 030610
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
088350: same archetype, new symbol, life-insurance value-up/rate-cycle positive with 4B watch
032830: same archetype, new symbol, large life-insurance capital-buffer and shareholder-return positive
000400: same archetype, new symbol, speculative insurer/M&A label without reserve-capital-return bridge
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
088350 한화생명
  profile: atlas/symbol_profiles/088/088350.json
  name history:
    대한생명 until 2012-10-16
    한화생명 from 2012-10-17
  first_date: 2010-03-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,922
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

032830 삼성생명
  profile: atlas/symbol_profiles/032/032830.json
  first_date: 2010-05-12
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,883
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

000400 롯데손해보험
  profile: atlas/symbol_profiles/000/000400.json
  name history:
    대한화재 until 2008-03-19
    롯데손해보험 from 2008-03-20
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,717
  corporate_action_candidate_dates:
    2001-02-23, 2002-01-28, 2006-05-17, 2012-12-26, 2015-06-25, 2019-10-25
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C22 is about the insurance rate cycle, reserve quality, capital buffer, and shareholder-return translation. It is not a generic "insurance stock went up" or "low-PBR financial" label.

The model can over-score:

```text
insurance value-up policy
life insurer rate sensitivity
CSM / reserve accounting label
K-ICS / capital buffer label
M&A speculation
one-week insurance price spike
```

The bridge must be stricter:

```text
insurance rate / reserve / CSM cycle
  -> company-specific CSM or reserve quality
  -> capital adequacy / K-ICS buffer
  -> liability or crediting-rate sensitivity
  -> dividend / buyback / capital-return execution
  -> earnings and book-value quality
  -> price survival after the first value-up spike
```

An insurer's balance sheet is like a dam. The headline says water is high, but equity value depends on whether the dam wall, reserve assumptions, and spillway can safely turn that water into distributable cash.

---

## 5. Case 1 — 088350 한화생명

```yaml
case_id: C22_R6L93_088350_2024_01_30
symbol: "088350"
name: "한화생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL
trigger_date: 2024-01-30
entry_date: 2024-01-30
entry_price_basis: close
entry_price: 3010
classification: positive_life_insurance_valueup_rate_cycle_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

한화생명 is the life-insurance value-up positive with 4B discipline.

The useful C22 read is:

```text
life-insurance value-up / rate-cycle relevance
  -> capital-return expectation
  -> reserve and capital-buffer sensitivity
  -> price confirmation
```

The forward path delivered meaningful MFE quickly, but the later drawdown warns that life-insurance value-up names should not remain Green without refreshed capital-return and reserve-quality evidence.

### Price path

Key Stock-Web rows:

```text
2024-01-30: close 3,010
2024-02-01: high 3,585 / close 3,355
2024-02-05: high 3,740 / close 3,690
2024-02-13: high 3,815 / close 3,550
2024-04-12: low 2,620 / close 2,630
2024-04-23: high 2,865 / close 2,825
2024-07-11: high 3,240 / close 3,150
2024-08-05: low 2,700 / close 2,730
```

Approximate path from entry close:

```text
entry_close: 3,010
peak_high: 3,815
MFE: +26.7%
worst_low_after_entry: 2,580 on 2024-04-16
MAE: -14.3%
```

### Interpretation

This is a positive entry, but not unrestricted Green:

```text
Stage2-Actionable: valid if CSM/reserve quality and capital-return bridge are explicit.
Stage3-Green: blocked without refreshed capital buffer and shareholder-return evidence.
Local 4B: required after +25% MFE and material drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  life_insurance_rate_relevance: high
  reserve_csm_bridge: medium
  capital_return_bridge: medium_high
  price_confirmation: high
  later_drawdown_penalty: medium
  local_4b_overlay: required
```

---

## 6. Case 2 — 032830 삼성생명

```yaml
case_id: C22_R6L93_032830_2024_02_21
symbol: "032830"
name: "삼성생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 88300
classification: positive_large_life_insurance_capital_buffer_shareholder_return_bridge
calibration_usable: true
```

### Evidence interpretation

삼성생명 is the clean large-life-insurer positive in this set.

The useful C22 bridge is:

```text
large life-insurer balance-sheet quality
  -> capital buffer / K-ICS resilience
  -> shareholder-return optionality
  -> value-up rerating
  -> price survival
```

The forward path had a strong MFE and later recovered again after the April drawdown. This is closer to a C22 positive than a pure one-day insurance beta move.

### Price path

Key Stock-Web rows:

```text
2024-02-21: close 88,300
2024-02-23: high 97,300 / close 95,600
2024-02-28: high 102,900 / close 102,900
2024-03-05: high 107,800 / close 104,500
2024-03-08: high 108,500 / close 105,100
2024-04-19: low 76,600 / close 77,300
2024-09-03: high 102,000 / close 100,500
2024-11-01: high 104,900 / close 103,800
```

Approximate path from entry close:

```text
entry_close: 88,300
peak_high: 108,500
MFE: +22.9%
worst_low_after_entry: 76,600
MAE: -13.3%
```

### Interpretation

This is a C22 positive:

```text
Stage2-Actionable: valid if capital buffer and shareholder-return bridge are explicit.
Stage3-Green: possible only with reserve quality, capital adequacy, and execution evidence.
Local 4B: monitor after +20% MFE, but price survival and later recovery are constructive.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  insurer_balance_sheet_quality: high
  capital_buffer_bridge: high
  shareholder_return_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: medium
  positive_preserved: yes
```

---

## 7. Case 3 — 000400 롯데손해보험

```yaml
case_id: C22_R6L93_000400_2024_04_23
symbol: "000400"
name: "롯데손해보험"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL
trigger_date: 2024-04-23
entry_date: 2024-04-23
entry_price_basis: close
entry_price: 3850
classification: hard_4c_candidate_speculative_insurer_ma_label_without_capital_reserve_bridge
calibration_usable: true
```

### Evidence interpretation

롯데손해보험 is the speculative insurer / M&A-label guardrail.

It had insurance-sector relevance and event-like price movement, but the trigger did not provide the C22 bridge:

```text
reserve quality
capital adequacy
sustainable earnings
dividend or buyback execution
```

Instead, the path behaved like a speculative label spike. The stock had almost no follow-through and then broke down.

### Price path

Key Stock-Web rows:

```text
2024-04-23: close 3,850
2024-04-24: high 3,960 / close 3,795
2024-04-25: high 4,035 / close 3,745
2024-06-26: high 4,090 / close 4,000
2024-06-28: low 2,900 / close 2,915
2024-08-05: low 2,515 / close 2,560
2024-09-11: low 2,400 / close 2,450
2024-10-10: low 2,175
```

Approximate path from entry close:

```text
entry_close: 3,850
peak_high: 4,090
MFE: +6.2%
worst_low_after_entry: 2,175
MAE: -43.5%
```

### Interpretation

This is a hard C22 false-positive:

```text
Stage2-Watch: possible from insurance-sector / M&A speculation relevance.
Stage2-Actionable: blocked without reserve/capital buffer/shareholder-return bridge.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is that insurance event speculation is not the same as reserve-cycle or capital-return quality.

### Stress-test components

```text
raw_component_score_proxy:
  insurance_label: high
  speculative_ma_label: high
  reserve_quality_bridge: weak
  capital_buffer_bridge: weak
  shareholder_return_bridge: weak
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
calibration_usable_trigger_count: 3
```

The three-case C22 grid:

```text
088350 한화생명:
  life-insurance value-up / rate-cycle positive;
  useful MFE, but material drawdown requires 4B and refreshed capital-return evidence.

032830 삼성생명:
  large-life-insurer capital-buffer and shareholder-return positive;
  better quality bridge and price recovery.

000400 롯데손해보험:
  speculative insurer/M&A label failed.
  Shallow MFE and large MAE, hard 4C.
```

Shared rule:

```text
C22 is not "insurance stock is in a value-up rally."
C22 is "reserve quality, CSM, capital buffer, and shareholder-return capacity convert into durable equity rerating."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C22_R6L93_088350_2024_01_30","scheduled_round":"R6","scheduled_loop":93,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL","symbol":"088350","name":"한화생명","trigger_date":"2024-01-30","entry_date":"2024-01-30","entry_price":3010,"peak_high":3815,"peak_date":"2024-02-13","worst_low_after_entry":2580,"worst_low_after_entry_date":"2024-04-16","mfe_pct":26.7,"mae_pct":-14.3,"classification":"positive_life_insurance_valueup_rate_cycle_with_4b_watch","calibration_usable":true,"evidence_family":"life_insurance_valueup_rate_cycle_csm_capital_return_bridge","residual_error":"positive_life_insurance_move_requires_4b_after_material_drawdown_without_refreshed_capital_return_evidence","shadow_rule_candidate":"allow_actionable_when_csm_reserve_capital_return_bridge_confirms_but_attach_4b_after_valueup_mfe"}
{"row_type":"case","case_id":"C22_R6L93_032830_2024_02_21","scheduled_round":"R6","scheduled_loop":93,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL","symbol":"032830","name":"삼성생명","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":88300,"peak_high":108500,"peak_date":"2024-03-08","worst_low_after_entry":76600,"worst_low_after_entry_date":"2024-04-19","mfe_pct":22.9,"mae_pct":-13.3,"classification":"positive_large_life_insurance_capital_buffer_shareholder_return_bridge","calibration_usable":true,"evidence_family":"large_life_insurer_capital_buffer_shareholder_return_reserve_quality_bridge","residual_error":"positive_case_but_green_requires_reserve_quality_capital_adequacy_and_return_execution","shadow_rule_candidate":"preserve_large_life_positive_when_capital_buffer_and_price_survival_confirm"}
{"row_type":"case","case_id":"C22_R6L93_000400_2024_04_23","scheduled_round":"R6","scheduled_loop":93,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL","symbol":"000400","name":"롯데손해보험","trigger_date":"2024-04-23","entry_date":"2024-04-23","entry_price":3850,"peak_high":4090,"peak_date":"2024-06-26","worst_low_after_entry":2175,"worst_low_after_entry_date":"2024-10-10","mfe_pct":6.2,"mae_pct":-43.5,"classification":"hard_4c_candidate_speculative_insurer_ma_label_without_capital_reserve_bridge","calibration_usable":true,"evidence_family":"speculative_insurer_ma_label_without_reserve_capital_return_bridge","residual_error":"insurance_event_speculation_can_overpromote_without_reserve_quality_and_capital_buffer","shadow_rule_candidate":"route_speculative_insurer_label_to_hard_4c_if_mfe_shallow_mae_large_and_reserve_capital_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":93,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_VALUEUP_CSM_KICS_CAPITAL_BUFFER_VS_MA_SPECULATIVE_INSURER_LABEL","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":93,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","rule_id":"C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C22, do not open Stage2-Actionable or Stage3-Green from insurance value-up, rate-cycle, CSM/reserve label, K-ICS label, M&A speculation, or one-week insurance-sector price spike alone. Require company-specific reserve quality, CSM durability, capital adequacy/K-ICS buffer, liability or crediting-rate sensitivity check, dividend/buyback/shareholder-return execution, earnings and book-value quality, and post-trigger price survival. Life-insurance positives may be Actionable when CSM/reserve and capital-return bridge are explicit, but material later MAE should attach local 4B. Speculative insurer/M&A labels with shallow MFE and large MAE should route to hard-4C when reserve and capital bridge are missing.","expected_effect":"Preserve insurance value-up positives with reserve/capital-return evidence while reducing speculative insurer-label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":93,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_reserve_csm_capital_return_guard","contribution":"Adds one life-insurance value-up positive with 4B watch, one large-life capital-buffer positive, and one speculative insurer/M&A hard-4C counterexample to calibrate C22 reserve, CSM, capital buffer, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIRED

IF canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:

  Do not open Stage3-Green from:
    - insurance value-up label alone
    - life/non-life insurer label alone
    - rate-cycle or CSM headline alone
    - K-ICS / capital buffer label alone
    - M&A or insurer sale speculation alone
    - one-week insurance-sector volume spike alone

  Require at least two of:
    - reserve quality or CSM durability
    - capital adequacy / K-ICS buffer
    - liability or crediting-rate sensitivity check
    - earnings and book-value quality
    - dividend / buyback / shareholder-return execution
    - low-MAE post-trigger price survival
    - fresh revision after the insurance value-up headline

  If MFE < 10% and MAE < -30%:
    route to C22 hard-4C candidate.

  If MFE > 20% but later MAE is material:
    preserve positive but attach local 4B unless fresh capital-return evidence appears.

  Distinguish:
    - large life insurers with capital buffer and shareholder-return bridge
    - from speculative insurer/M&A labels where reserve quality and capital-return visibility are weak.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_93_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C22 insurance rate-cycle/reserve/capital-return cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C22_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C22 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C22 cases agree, consider implementing a canonical guard that:
   - blocks insurance Green without reserve/CSM/capital buffer/shareholder-return bridge,
   - preserves life-insurance positives with price survival and capital-return evidence,
   - attaches local 4B after value-up MFE followed by material drawdown,
   - routes shallow-MFE/high-MAE speculative insurer/M&A labels to hard-4C.

Expected next schedule:
completed_round = R6
completed_loop = 93
next_round = R7
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R6
completed_loop = 93
next_round = R7
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
