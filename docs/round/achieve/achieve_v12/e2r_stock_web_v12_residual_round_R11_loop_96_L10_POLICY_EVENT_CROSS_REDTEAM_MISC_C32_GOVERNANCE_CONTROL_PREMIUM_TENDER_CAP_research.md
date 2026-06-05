# E2R Stock-Web v12 Residual Research — R11 / Loop 96

```yaml
scheduled_round: R11
scheduled_loop: 96
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE

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
tender_offer_case_count: 2
control_dispute_case_count: 1
delisting_or_inactive_profile_caveat_count: 2
control_premium_event_risk_case_count: 1
governance_bridge_missing_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 96
next_round: R12
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_96_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 96
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use L10 policy / event / governance / miscellaneous branches. This run uses:

```text
canonical_archetype_id = C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
```

The selected fine branch is:

```text
tender offer / delisting / control dispute
spread, financing, acceptance ratio, regulatory approval, minority exit, and trust bridge
vs generic governance or control-premium label spike
```

This deliberately avoids:
- C32 top-covered names `010130`, `036560`, `000150`, `041510`, `241560`, `000990`;
- the prior R11 loop94 governance set `003920`, `001750`, `003240`;
- the R11 loop95 C31 tourism branch `034230`, `950170`, `008770`;
- the R12 loop95 C31 carbon/environment branch `083420`, `448280`, `119650`.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
rows: 41
symbols: 22
date_range: 2020-02-12~2024-10-31
good/bad S2: 16/12
4B/4C: 3/0
URL pending/proxy: 8/8
top covered symbols:
  010130(4), 036560(4), 000150(3), 041510(3), 241560(3), 000990(2)
```

Selected symbols:

```text
119860 커넥트웨이브
115390 락앤락
008930 한미사이언스
```

They avoid the C32 top-covered list and avoid recent R11/R12 policy/governance names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
119860: same archetype, new symbol, tender-offer / delisting spread positive with inactive-profile caveat
115390: same archetype, new symbol, tender-offer cap positive with delisting/inactive-profile caveat
008930: same archetype, new symbol, control-dispute local spike / hard-4C first-phase failure before later renewed control event
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
119860 커넥트웨이브
  profile: atlas/symbol_profiles/119/119860.json
  name history:
    다나와 until 2022-12-15
    커넥트웨이브 from 2022-12-16 to 2024-09-23
  market: KOSDAQ
  first_date: 2011-01-24
  last_date: 2024-09-03 in tradable profile
  raw_last_date: 2024-09-23
  tradable_ohlcv rows: 3,354
  non_tradable_zero_volume rows: 11
  corporate_action_candidate_dates:
    2016-12-28, 2017-01-19, 2022-12-16
  2024 tender window contamination: none from corporate-action candidate dates
  caveat:
    inactive/delisted-like profile by row presence. This is a feature for tender/delisting cases, but the actionability must be capped by spread and execution terms.

115390 락앤락
  profile: atlas/symbol_profiles/115/115390.json
  first_date: 2010-01-28
  last_date: 2024-11-19 in tradable profile
  raw_last_date: 2024-12-06
  market: KOSPI
  tradable_ohlcv rows: 3,637
  non_tradable_zero_volume rows: 27
  corporate_action_candidate_dates: none
  2024 tender window contamination: none
  caveat:
    inactive/delisted-like profile by row presence. Tender-positive classification is valid only as capped spread / minority-exit analysis, not ordinary operating Green.

008930 한미사이언스
  profile: atlas/symbol_profiles/008/008930.json
  name history:
    한미약품 -> 한미홀딩스 -> 한미사이언스
  market: KOSPI
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,726
  non_tradable_zero_volume rows: 38
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1999-04-19, 2010-07-30, 2010-10-21, 2012-05-14
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action windows are outside the selected 2024 validation window.
    Governance/control dispute path requires separation between first event phase and later renewed control event.
```

---

## 4. Archetype residual problem

C32 is about governance, control premium, tender offers, minority exit, and event-risk caps. It is not a generic "governance issue" or "control premium might exist" archetype.

The model can over-score:

```text
tender offer headline
voluntary delisting label
private-equity / sponsor label
control dispute or shareholder meeting headline
founder-family conflict
M&A rumor or strategic buyer rumor
one-day governance-stock volume spike
```

The C32 bridge must be stricter:

```text
governance / tender / control event
  -> binding offer or concrete voting/control event
  -> offer price, spread, and acceptance period
  -> financing / sponsor credibility
  -> minimum tender threshold or control math
  -> regulatory / court / shareholder-meeting risk
  -> minority exit terms and delisting probability
  -> downside if event fails or gets delayed
  -> liquidity and tradeability trust
  -> price survival inside the event window
```

A C32 event is like an exit door with a price tag. The door only works if the buyer has financing, the acceptance math clears, regulators and courts do not block it, and minorities can actually walk through. A governance headline alone is just a sign on the wall.

---

## 5. Case 1 — 119860 커넥트웨이브

```yaml
case_id: C32_R11L96_119860_2024_04_26
symbol: "119860"
name: "커넥트웨이브"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-04-26
entry_date: 2024-04-26
entry_price_basis: close
entry_price: 15570
classification: positive_capped_tender_offer_delisting_spread_with_inactive_profile_caveat
calibration_usable: true
```

### Evidence interpretation

커넥트웨이브 is the constructive tender-offer / delisting-spread case.

The useful C32 read is not simply:

```text
공개매수 / 상장폐지 뉴스가 있다
```

It is:

```text
tender offer / delisting event
  -> concrete offer-price anchor
  -> spread compression toward the cap
  -> low post-event volatility
  -> liquidity/tradeability caveat because the stock later exits the tradable profile
```

The price path moved toward a tight cap around 18,000 after the event. This is a positive, but it is not a normal Green. The expected return is bounded by the offer spread, and the key risk is execution: acceptance ratio, financing, regulatory/trading-calendar mechanics, and minority-exit terms.

### Price path

Key Stock-Web rows:

```text
2024-04-26: high 16,100 / close 15,570
2024-04-29: high 17,880 / close 17,880
2024-05-10: close 17,900
2024-07-24: high 18,010 / close 18,000
2024-08-05: low 17,700 / close 17,810
2024-09-03: high 18,010 / close 18,000
```

Approximate post-entry path from entry close:

```text
entry_close: 15,570
peak_high: 18,040
MFE: +15.9%
post_close_worst_low: 17,700
post_close_MAE: +13.7% relative to entry close
```

The same-day intraday low before the close is not counted as post-entry MAE because the entry basis is close.

### Interpretation

This is a C32 capped positive:

```text
Stage2-Actionable: valid only as tender-spread / delisting execution trade.
Stage3-Green: blocked as ordinary operating Green.
Local 4B: monitor if spread widens or tender mechanics fail.
Hard 4C: no.
Inactive/delisted-like caveat: yes, expected for the event family.
```

### Stress-test components

```text
raw_component_score_proxy:
  tender_offer_specificity: high
  offer_price_anchor: high
  spread_compression: high
  financing_sponsor_bridge: medium_high
  acceptance_threshold_bridge: medium
  minority_exit_terms: medium
  downside_if_failed: high
  tradeability_exit_caveat: high
```

---

## 6. Case 2 — 115390 락앤락

```yaml
case_id: C32_R11L96_115390_2024_04_17
symbol: "115390"
name: "락앤락"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-04-17
entry_date: 2024-04-17
entry_price_basis: close
entry_price: 8180
classification: positive_capped_tender_offer_minority_exit_with_delisting_profile_caveat
calibration_usable: true
```

### Evidence interpretation

락앤락 is the second tender-cap positive.

The setup is a classic C32 case:

```text
tender-offer / minority-exit event
  -> immediate price convergence toward the offer zone
  -> very low volatility after the event
  -> later inactive/delisted-like profile
```

Again, this is not a normal Green. The upside is bounded by the offer price area and execution mechanics. If the spread is tight, the model must not score it like a broad operating rerating.

### Price path

Key Stock-Web rows:

```text
2024-04-17: high 8,290 / close 8,180
2024-04-18: high 8,720 / close 8,680
2024-05-08: high 8,890 / close 8,700
2024-07-24: close 8,750
2024-08-05: low 8,750 / close 8,750
2024-10-11: low 8,270 / close 8,600
2024-11-07: close 8,650
```

Approximate post-entry path from entry close:

```text
entry_close: 8,180
peak_high: 8,890
MFE: +8.7%
post_close_worst_low: 8,270
post_close_MAE: +1.1% relative to entry close
```

The same-day intraday low before the close is not counted as post-entry MAE because the entry basis is close.

### Interpretation

This is a C32 capped positive:

```text
Stage2-Actionable: valid only as tender-spread / minority-exit execution trade.
Stage3-Green: blocked as ordinary operating Green.
Local 4B: monitor if the spread widens, tender fails, or delisting mechanics become uncertain.
Hard 4C: no.
Inactive/delisted-like caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  tender_offer_specificity: high
  minority_exit_bridge: high
  spread_compression: high
  financing_bridge: medium_high
  regulatory_delisting_bridge: medium
  ordinary_operating_green_block: required
  tradeability_exit_caveat: high
```

---

## 7. Case 3 — 008930 한미사이언스

```yaml
case_id: C32_R11L96_008930_2024_03_28
symbol: "008930"
name: "한미사이언스"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE
trigger_date: 2024-03-28
entry_date: 2024-03-28
entry_price_basis: close
entry_price: 44350
classification: hard_4c_candidate_control_dispute_first_phase_without_durable_control_premium_survival_before_later_reignition
calibration_usable: true
```

### Evidence interpretation

한미사이언스 is the hard C32 guardrail.

The setup had real governance/event salience:

```text
founder-family / control dispute
shareholder meeting and voting-control narrative
potential control-premium optionality
large event-volume spike
```

But from the selected first-phase event close, the near-term control-premium did not survive. The stock produced shallow incremental MFE before falling sharply. A later renewed October governance/control event should not retroactively validate the first event phase. C32 must separate event windows.

### Price path

Key Stock-Web rows:

```text
2024-03-28: high 47,000 / close 44,350
2024-03-29: close 38,300
2024-04-17: low 31,700 / close 31,750
2024-08-05: low 25,750 / close 26,750
2024-10-18: high 37,300 / close 36,350
2024-10-24: high 42,150 / close 39,150
2024-10-30: high 52,500 / close 52,100
2024-11-01: low 34,500 / close 36,250
```

Approximate first-phase path from entry close, before later renewed control-event phase:

```text
entry_close: 44,350
peak_high_first_phase: 47,000
MFE: +6.0%
worst_low_before_later_reignition: 25,750
MAE: -41.9%
```

### Interpretation

This is a hard C32 false-positive for the first event phase:

```text
Stage2-Watch: valid from governance/control-dispute relevance.
Stage2-Actionable: blocked unless concrete control math, binding transaction, financing, voting path, and minority economics are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow first-phase MFE and high MAE.
Later event caveat: later October control-action is a new event window, not validation of the March entry.
```

The lesson is that a control-dispute headline is not durable control premium.

### Stress-test components

```text
raw_component_score_proxy:
  control_dispute_salience: high
  voting_control_path: medium
  binding_transaction_bridge: weak
  financing_or_tender_bridge: weak
  minority_exit_bridge: weak
  price_confirmation_first_phase: shallow
  event_window_separation_required: high
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
tender_offer_case_count: 2
control_dispute_case_count: 1
delisting_or_inactive_profile_caveat_count: 2
control_premium_event_risk_case_count: 1
governance_bridge_missing_count: 1
calibration_usable_trigger_count: 3
```

The three-case C32 governance/tender grid:

```text
119860 커넥트웨이브:
  tender-offer / delisting spread positive;
  capped upside, tight spread, inactive-profile caveat.

115390 락앤락:
  tender-offer / minority-exit positive;
  capped upside, low volatility, inactive-profile caveat.

008930 한미사이언스:
  control-dispute first-phase failed;
  shallow MFE and high MAE before later renewed event, hard 4C.
```

Shared rule:

```text
C32 is not "governance event is hot."
C32 is "there is a binding tender/control path, financing, acceptance math, legal/regulatory clearance, minority exit, and price survival within the event window."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R11L96_119860_2024_04_26","scheduled_round":"R11","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"119860","name":"커넥트웨이브","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":15570,"peak_high":18040,"peak_date":"2024-08-13","post_close_worst_low":17700,"post_close_worst_low_date":"2024-08-05","mfe_pct":15.9,"post_close_mae_pct":13.7,"classification":"positive_capped_tender_offer_delisting_spread_with_inactive_profile_caveat","calibration_usable":true,"delisting_or_inactive_profile_caveat":true,"evidence_family":"tender_offer_delisting_spread_offer_price_anchor_financing_acceptance_minority_exit_bridge","residual_error":"tender_positive_must_be_scored_as_capped_spread_not_ordinary_green","shadow_rule_candidate":"preserve_tender_spread_positive_but_cap_green_and_monitor_execution_terms"}
{"row_type":"case","case_id":"C32_R11L96_115390_2024_04_17","scheduled_round":"R11","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"115390","name":"락앤락","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":8180,"peak_high":8890,"peak_date":"2024-05-08","post_close_worst_low":8270,"post_close_worst_low_date":"2024-10-11","mfe_pct":8.7,"post_close_mae_pct":1.1,"classification":"positive_capped_tender_offer_minority_exit_with_delisting_profile_caveat","calibration_usable":true,"delisting_or_inactive_profile_caveat":true,"evidence_family":"tender_offer_minority_exit_spread_compression_financing_regulatory_delisting_bridge","residual_error":"minority_exit_tender_positive_is_capped_by_offer_terms_and_not_operating_green","shadow_rule_candidate":"allow_capped_actionable_for_tender_exit_but_block_ordinary_green"}
{"row_type":"case","case_id":"C32_R11L96_008930_2024_03_28","scheduled_round":"R11","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","symbol":"008930","name":"한미사이언스","trigger_date":"2024-03-28","entry_date":"2024-03-28","entry_price":44350,"peak_high_first_phase":47000,"peak_date":"2024-03-28","worst_low_before_later_reignition":25750,"worst_low_before_later_reignition_date":"2024-08-05","mfe_pct":6.0,"mae_pct":-41.9,"classification":"hard_4c_candidate_control_dispute_first_phase_without_durable_control_premium_survival_before_later_reignition","calibration_usable":true,"event_window_separation_required":true,"evidence_family":"control_dispute_shareholder_meeting_voting_control_label_without_binding_transaction_minority_exit_bridge","residual_error":"control_dispute_headline_can_fail_when_control_math_and_binding_transaction_bridge_missing","shadow_rule_candidate":"route_control_dispute_first_phase_to_hard_4c_if_mfe_shallow_mae_large_and_no_binding_control_path"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":96,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"TENDER_OFFER_DELISTING_CONTROL_DISPUTE_SPREAD_FINANCING_ACCEPTANCE_TRUST_BRIDGE_VS_GOVERNANCE_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"tender_offer_case_count":2,"control_dispute_case_count":1,"delisting_or_inactive_profile_caveat_count":2,"control_premium_event_risk_case_count":1,"governance_bridge_missing_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":96,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_BINDING_TENDER_CONTROL_PATH_SPREAD_TRUST_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32, do not open Stage2-Actionable or Stage3-Green from tender offer, voluntary delisting, private-equity sponsor, control dispute, founder-family conflict, M&A rumor, strategic buyer rumor, shareholder meeting headline, or one-day governance-stock spike labels alone. Require binding offer or concrete voting/control event, offer price and spread, acceptance period, financing or sponsor credibility, minimum tender threshold or control math, regulatory/court/shareholder-meeting risk check, minority exit terms and delisting probability, downside if event fails or gets delayed, liquidity/tradeability trust, and price survival within the event window. Tender-offer positives should be scored as capped spread trades, not ordinary operating Green. Control-dispute first phases with shallow MFE and high MAE should route to hard-4C when no binding control path or minority exit bridge exists. Later renewed control events should not retroactively validate earlier failed event windows.","expected_effect":"Preserve true tender/delisting spread positives while reducing governance headline and control-premium false positives, with explicit event-window separation and tradeability caps.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":96,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"binding_tender_control_path_spread_trust_guard","contribution":"Adds two tender-offer/delisting capped positives and one control-dispute hard-4C counterexample to calibrate C32 offer spread, financing, acceptance, minority exit, event-window separation, and tradeability trust requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_BINDING_TENDER_CONTROL_PATH_SPREAD_TRUST_BRIDGE_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:

  Do not open Stage3-Green from:
    - tender offer headline alone
    - voluntary delisting label alone
    - private-equity / sponsor label alone
    - control dispute or shareholder meeting headline alone
    - founder-family conflict alone
    - M&A rumor / strategic buyer rumor alone
    - one-day governance-stock volume spike alone

  Require at least two of:
    - binding offer or concrete voting/control event
    - offer price and current spread
    - acceptance period and tender mechanics
    - financing / sponsor credibility
    - minimum tender threshold or control math
    - regulatory / court / shareholder-meeting risk control
    - minority exit terms and delisting probability
    - downside if event fails or gets delayed
    - liquidity / tradeability trust
    - price survival inside the event window

  If tender or delisting path is concrete:
    score as capped spread / minority-exit trade, not ordinary operating Green.

  If MFE < 10% and MAE < -30%:
    route to C32 hard-4C candidate.

  If later renewed event appears:
    create a new event window; do not retroactively validate a failed earlier trigger.

  If inactive/delisted-like profile appears:
    require tradeability cap and do not treat final capped price as ordinary rerating.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_96_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 governance/tender/control-premium cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_BINDING_TENDER_CONTROL_PATH_SPREAD_TRUST_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C32 cases agree, consider implementing a canonical guard that:
   - blocks governance-label Green without binding offer/control path, spread, financing, acceptance, regulatory/court/shareholder-meeting, minority-exit, and tradeability bridge,
   - scores tender/delisting positives as capped spread trades rather than ordinary Green,
   - routes shallow-MFE/high-MAE control dispute phases to hard-4C when no binding path exists,
   - separates later renewed event windows from earlier failed control events,
   - applies inactive/delisted-like and tradeability caps.

Expected next schedule:
completed_round = R11
completed_loop = 96
next_round = R12
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 96
next_round = R12
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
