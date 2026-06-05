# E2R Stock-Web v12 Residual Research — R6 / Loop 91

```yaml
scheduled_round: R6
scheduled_loop: 91
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY

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
local_4b_overlay_case_count: 0
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R6
completed_loop: 91
next_round: R7
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R5_loop_91_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R6
scheduled_loop = 91
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
```

This run returns to C22, but with a different branch:

```text
insurance value-up / rate / reserve / CSM / capital-return bridge
vs low-PBR financial beta after the initial insurance rally
```

The key is late-entry risk. The model must distinguish a true insurer capital/reserve-quality rerating from a late low-PBR financial-beta chase.

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
001450 현대해상
```

These avoid the C22 top-covered symbols and avoid the most recent R6 loop90 securities names:

```text
005940, 006800, 039490
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
032830: same archetype, new symbol, life-insurer value-up late-entry / capital-return bridge failure mode
088350: same archetype, new symbol, lower-priced life-insurer beta / reserve-CSM-payout bridge failure mode
001450: same archetype, new symbol, P&C insurer reserve-quality / payout bridge positive-control branch
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
  tradable_ohlcv rows: 3,883
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

088350 한화생명
  profile: atlas/symbol_profiles/088/088350.json
  first_date: 2010-03-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,922
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

001450 현대해상
  profile: atlas/symbol_profiles/001/001450.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,761
  corporate_action_candidate_dates:
    2004-07-13
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C22 is supposed to separate insurance-specific value from generic low-PBR financial beta.

A naive model can over-score:

```text
insurance stocks rallied with Korea Value-up
interest rates are favorable
life insurer has low PBR
CSM exists
reserve risk is improving
capital return may increase
```

The actual C22 bridge is narrower:

```text
rate cycle
  -> asset/liability sensitivity
  -> CSM quality or reserve adequacy
  -> solvency / K-ICS / capital buffer
  -> dividend or buyback capacity
  -> OP/EPS / embedded-value conversion
  -> price survival after the first value-up burst
```

Insurance is a balance sheet business. A headline can make the roof shine, but the foundation is reserves and capital. If reserve quality or capital return is not explicit, a late entry can become only a low-PBR financial-beta chase.

---

## 5. Shared event frame

Trigger frame:

```text
2024-02-28
Korea Corporate Value-up / shareholder-return policy follow-through,
after the late-January and February financial-value-up rally.
```

This is intentionally a late-entry trigger. C22 already saw strong insurance stock moves in late January and early February. The residual question is:

```text
After the initial insurance value-up rally, can the model still open Stage2-Actionable or Green?
```

The answer must depend on company-specific reserve quality, CSM, solvency, and payout bridge.

---

## 6. Case 1 — 032830 삼성생명

```yaml
case_id: C22_R6L91_032830_2024_02_28
symbol: "032830"
name: "삼성생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 102900
classification: counterexample_life_insurer_valueup_late_entry_high_mae
calibration_usable: true
```

### Evidence interpretation

삼성생명 is the late-entry life-insurer counterexample.

The stock had already moved sharply before 2024-02-28. If the model opens a fresh C22 Green on the policy headline alone, it is no longer buying reserve/capital-return alpha. It may be chasing a financial-beta move after the market has already repriced part of the story.

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 102,900
2024-03-05: high 107,800 / close 104,500
2024-03-08: high 108,500 / close 105,100
2024-03-29: close 92,300
2024-04-09: low 89,300 / close 89,500
2024-08-05: low 82,500 / close 84,000
2024-09-19: high 103,100 / close 100,400
```

Approximate path from entry close:

```text
entry_close: 102,900
peak_high: 108,500
MFE: +5.4%
worst_low: 82,500
MAE: -19.8%
```

### Interpretation

This is not a claim that 삼성생명 is a weak insurer. The calibration point is trigger quality:

```text
Stage2-Watch: allowed.
Stage2-Actionable: blocked unless fresh payout / solvency / reserve-quality bridge is explicit.
Stage3-Green: blocked at this late entry.
Hard 4C: not quite, but high-MAE false-positive guard applies.
```

### Stress-test components

```text
raw_component_score_proxy:
  low_pbr_valueup_beta: high
  insurance_rate_cycle_relevance: medium
  reserve_csm_bridge_visibility: medium_or_unclear
  capital_return_specificity: medium_or_unclear
  price_confirmation_after_trigger: weak
  drawdown_penalty: high
  late_entry_penalty: high
```

---

## 7. Case 2 — 088350 한화생명

```yaml
case_id: C22_R6L91_088350_2024_02_28
symbol: "088350"
name: "한화생명"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 3100
classification: counterexample_life_insurer_beta_without_fresh_reserve_payout_bridge
calibration_usable: true
```

### Evidence interpretation

한화생명 is the second life-insurance guardrail case. It shows that a lower-priced life-insurer can still be over-promoted if the model only sees:

```text
low PBR
financial value-up theme
life-insurer rate sensitivity
prior rally
```

For C22, the specific bridge should be:

```text
K-ICS / capital buffer
CSM quality
reserve adequacy
dividend or buyback visibility
earnings quality
```

The price path after 2024-02-28 was not enough to justify Green.

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 3,100
2024-02-29: high 3,185 / close 3,150
2024-03-04: high 3,310 / close 3,245
2024-03-15: high 3,345 / close 3,250
2024-03-29: low 2,810 / close 2,835
2024-08-05: low 2,700 / close 2,730
2024-09-11: low 2,760 / close 2,790
```

Approximate path from entry close:

```text
entry_close: 3,100
peak_high: 3,345
MFE: +7.9%
worst_low: 2,700
MAE: -12.9%
```

### Interpretation

This is a C22 Watch/Yellow cap case:

```text
Stage2-Watch: valid.
Stage2-Actionable: blocked unless fresh reserve/capital-return bridge appears.
Stage3-Green: blocked.
Hard 4C: no.
```

The important residual error is not catastrophic loss. It is over-certainty. A shallow MFE plus nontrivial MAE says the policy label did not become a fresh insurer-specific rerating.

### Stress-test components

```text
raw_component_score_proxy:
  low_pbr_valueup_beta: high
  rate_sensitivity: medium
  csm_reserve_bridge: weak_to_medium
  payout_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 8. Case 3 — 001450 현대해상

```yaml
case_id: C22_R6L91_001450_2024_02_28
symbol: "001450"
name: "현대해상"
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 31450
classification: positive_pnc_insurer_reserve_payout_bridge_low_mae
calibration_usable: true
```

### Evidence interpretation

현대해상 is the positive control in this grid. It is still not a huge Green, but the path is much cleaner than the two life-insurer late-entry cases.

The constructive read is:

```text
P&C insurer reserve / loss-ratio / capital-return bridge
  -> value-up relevance
  -> controlled drawdown after entry
  -> later price confirmation
```

The 180D path gave a reasonable MFE with very low MAE, which is useful for C22 calibration.

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 31,450
2024-03-14: high 35,450 / close 34,850
2024-03-28: low 30,600 / close 30,850
2024-07-31: high 36,750 / close 36,050
2024-08-05: low 31,500 / close 32,000
2024-08-20: high 36,650 / close 36,150
2024-09-09: low 33,100 / close 33,400
```

Approximate path from entry close:

```text
entry_close: 31,450
peak_high: 36,750
MFE: +16.9%
worst_low: 30,600
MAE: -2.7%
```

### Interpretation

This is a positive control, but not a broad Green stamp.

```text
Stage2-Actionable: allowed if reserve quality / loss ratio / payout bridge is explicit.
Stage3-Green: requires stronger capital-return and earnings bridge.
4B: not needed.
Hard 4C: no.
```

The case says C22 should preserve P&C insurer positives when the price path has low MAE and the evidence points to reserve-quality or payout conversion rather than generic low-PBR beta.

### Stress-test components

```text
raw_component_score_proxy:
  reserve_quality_bridge: medium_high
  loss_ratio_or_underwriting_bridge: medium
  capital_return_visibility: medium
  price_confirmation: medium_high
  drawdown_penalty: low
  actionability_allowed: yes_if_bridge_explicit
```

---

## 9. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 0
hard_4c_candidate_count: 0
calibration_usable_trigger_count: 3
```

The three-case C22 grid:

```text
032830 삼성생명:
  strong insurer and major value-up name,
  but the late 2024-02-28 entry had shallow MFE and high MAE.
  Block Green without fresh payout/CSM/reserve bridge.

088350 한화생명:
  lower-priced life-insurer beta,
  shallow MFE and medium MAE.
  Watch/Yellow cap unless reserve and payout bridge is explicit.

001450 현대해상:
  P&C insurer positive control,
  reasonable MFE and very low MAE.
  Actionable can work if reserve/loss-ratio/capital-return bridge is visible.
```

Shared rule:

```text
C22 is not "insurance stock + value-up = Green."
C22 is "insurance balance sheet, reserves, CSM, solvency, and payout capacity convert into durable rerating."
```

---

## 10. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C22_R6L91_032830_2024_02_28","scheduled_round":"R6","scheduled_loop":91,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY","symbol":"032830","name":"삼성생명","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":102900,"peak_high":108500,"peak_date":"2024-03-08","worst_low":82500,"worst_low_date":"2024-08-05","mfe_pct":5.4,"mae_pct":-19.8,"classification":"counterexample_life_insurer_valueup_late_entry_high_mae","calibration_usable":true,"evidence_family":"life_insurer_valueup_low_pbr_without_fresh_reserve_csm_payout_bridge","residual_error":"late_entry_after_insurance_valueup_rally_can_overpromote_to_green","shadow_rule_candidate":"block_green_if_life_insurer_valueup_entry_has_shallow_mfe_high_mae_without_fresh_payout_reserve_bridge"}
{"row_type":"case","case_id":"C22_R6L91_088350_2024_02_28","scheduled_round":"R6","scheduled_loop":91,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY","symbol":"088350","name":"한화생명","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":3100,"peak_high":3345,"peak_date":"2024-03-15","worst_low":2700,"worst_low_date":"2024-08-05","mfe_pct":7.9,"mae_pct":-12.9,"classification":"counterexample_life_insurer_beta_without_fresh_reserve_payout_bridge","calibration_usable":true,"evidence_family":"low_pbr_life_insurer_beta_without_csm_reserve_payout_bridge","residual_error":"low_priced_life_insurer_beta_can_be_overpromoted_without_reserve_capital_bridge","shadow_rule_candidate":"cap_at_watch_yellow_when_mfe_shallow_and_payout_reserve_bridge_weak"}
{"row_type":"case","case_id":"C22_R6L91_001450_2024_02_28","scheduled_round":"R6","scheduled_loop":91,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY","symbol":"001450","name":"현대해상","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":31450,"peak_high":36750,"peak_date":"2024-07-31","worst_low":30600,"worst_low_date":"2024-03-28","mfe_pct":16.9,"mae_pct":-2.7,"classification":"positive_pnc_insurer_reserve_payout_bridge_low_mae","calibration_usable":true,"evidence_family":"pnc_insurer_reserve_loss_ratio_capital_return_bridge","residual_error":"none_for_actionable_if_reserve_payout_bridge_explicit","shadow_rule_candidate":"allow_actionable_for_pnc_insurer_when_low_mae_and_reserve_payout_bridge_confirm"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R6","scheduled_loop":91,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_VALUEUP_RATE_RESERVE_CSM_CAPITAL_RETURN_BRIDGE_VS_LOW_PBR_FINANCIAL_BETA_LATE_ENTRY","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":0,"hard_4c_candidate_count":0,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R6","scheduled_loop":91,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","rule_id":"C22_INSURANCE_RESERVE_CSM_PAYOUT_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C22, do not open Stage2-Actionable or Stage3-Green from low-PBR insurance value-up beta, rate-cycle label, or CSM headline alone. Require company-specific reserve quality, CSM durability, solvency/K-ICS buffer, loss-ratio or underwriting bridge, payout/buyback visibility, and post-trigger price survival. Late entries after the initial insurance rally should be capped at Watch/Yellow if MFE is shallow and MAE is material. P&C insurers may be Actionable when reserve/loss-ratio/capital-return bridge is explicit and MAE remains low.","expected_effect":"Reduce life-insurer value-up late-entry false positives while preserving P&C insurer positives with low MAE and explicit reserve/payout bridge.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R6","scheduled_loop":91,"canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","residual_type":"insurance_valueup_late_entry_reserve_bridge_guard","contribution":"Adds one P&C positive control and two life-insurer late-entry counterexamples to separate true insurance balance-sheet rerating from generic low-PBR value-up beta.","do_not_count_as_global_weight_delta":true}
```

---

## 11. Proposed canonical-archetype shadow rule

```text
C22_INSURANCE_RESERVE_CSM_PAYOUT_BRIDGE_REQUIRED

IF canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:

  Do not open Stage3-Green from:
    - insurance low-PBR label alone
    - Korea Value-up policy headline alone
    - rate-cycle tailwind alone
    - CSM headline alone
    - first insurance-sector rally alone

  Require at least two of:
    - reserve adequacy / reserve release quality
    - CSM durability and quality
    - solvency / K-ICS capital buffer
    - loss-ratio / underwriting improvement for P&C
    - asset/liability rate-cycle bridge for life insurers
    - dividend / buyback / payout policy visibility
    - OP/EPS or embedded-value conversion
    - low-MAE post-trigger price survival

  If entry occurs after a large initial insurance value-up rally:
    apply late_entry_penalty.

  If MFE < 10% and MAE < -15%:
    block Stage3-Green and cap at Watch/Yellow.

  If life insurer has shallow MFE and no fresh payout/reserve bridge:
    block Stage2-Actionable.

  If P&C insurer has MFE > 15% and MAE > -5% with reserve/loss-ratio bridge:
    allow Stage2-Actionable, but require stronger payout evidence before Green.
```

---

## 12. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C22 insurance/rate/reserve cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C22_INSURANCE_RESERVE_CSM_PAYOUT_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C22 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C22 cases agree, consider implementing a canonical guard that:
   - blocks low-PBR insurance value-up Green without reserve/CSM/payout bridge,
   - adds late-entry penalty after initial insurance value-up rally,
   - caps shallow-MFE/high-MAE life insurers at Watch/Yellow,
   - preserves low-MAE P&C insurer positives with reserve/loss-ratio/capital-return bridge.

Expected next schedule:
completed_round = R6
completed_loop = 91
next_round = R7
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 13. Required round-state footer

```text
completed_round = R6
completed_loop = 91
next_round = R7
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
