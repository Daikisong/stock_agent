# E2R Stock-Web v12 Residual Research — R12 / Loop 91

```yaml
scheduled_round: R12
scheduled_loop: 91
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R12
completed_loop: 91
next_round: R13
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R11_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R12
scheduled_loop = 91
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R12 can use L10 policy/event or a relevant under-covered service/agri branch. This run uses a service-sector policy event:

```text
China visa-free travel policy
  -> Korean travel-service names
  -> booking conversion / package mix / take-rate bridge
```

This is distinct from:
- R12 loop90 payment-settlement policy,
- R11 loop91 AI semiconductor policy,
- R5 consumer/export distribution work.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rows: 97
symbols: 70
date_range: 2020-01-23~2025-01-17
good/bad S2: 35/25
4B/4C: 5/0
URL pending/proxy: 25/25
top covered symbols:
  013990(4), 003550(3), 015760(3), 032350(3), 114090(3), 000270(2)
```

Selected symbols:

```text
039130 하나투어
080160 모두투어
094850 참좋은여행
```

They avoid the C31 top-covered symbols and avoid the recent R12 service/education names and R11 semiconductor-policy names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
039130: same archetype, new symbol, large outbound travel agency booking-conversion branch
080160: same archetype, new symbol, mid travel agency theme-spike / weak durability branch
094850: same archetype, new symbol, small travel agency local-spike / high-volatility branch
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
039130 하나투어
  profile: atlas/symbol_profiles/039/039130.json
  first_date: 2000-11-28
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,221
  corporate_action_candidate_dates:
    2003-09-09, 2003-09-30, 2004-11-19
  2024 entry~D+180 contamination: none

080160 모두투어
  profile: atlas/symbol_profiles/080/080160.json
  first_date: 2005-07-26
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,076
  corporate_action_candidate_dates:
    2006-06-05, 2006-06-16, 2012-06-22, 2017-07-18
  2024 entry~D+180 contamination: none

094850 참좋은여행
  profile: atlas/symbol_profiles/094/094850.json
  first_date: 2007-04-30
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,636
  corporate_action_candidate_dates:
    2007-10-23, 2008-08-06, 2009-08-06
  2024 entry~D+180 contamination: none
```

---

## 4. Event frame and residual problem

Trigger frame:

```text
2024-11-04
Korean travel-service stocks react to China visa-free access / China travel-reopening policy flow.
```

Follow-up policy frame:

```text
2024-11-22
China expands the visa-free programme to additional countries and extends stay length, while Reuters notes prior arrangements with South Korea.
```

This is a C31 service-policy branch.

The model can over-score:

```text
China visa-free
China reopening
travel agency
tourism policy
outbound travel recovery
```

The correct bridge is narrower:

```text
policy access
  -> actual outbound package bookings
  -> seat/airline supply and product availability
  -> commission/take-rate
  -> cancellation and FX cost risk
  -> OP/EPS conversion
  -> price survival after first policy spike
```

A visa-free headline opens the gate. It does not fill every tour bus. The stock-level question is whether the agency sells profitable packages through that gate.

---

## 5. Case 1 — 039130 하나투어

```yaml
case_id: C31_R12L91_039130_2024_11_04
symbol: "039130"
name: "하나투어"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE
trigger_date: 2024-11-04
entry_date: 2024-11-04
entry_price_basis: close
entry_price: 50900
classification: positive_with_booking_bridge_watch
calibration_usable: true
```

### Evidence interpretation

하나투어 is the constructive service-policy case.

The company has the cleanest connection to outbound travel package conversion. The policy headline can plausibly convert into:

```text
China travel accessibility
  -> outbound package demand
  -> higher booking volume
  -> agency commission / package margin
  -> OP conversion
```

The stock path showed a controlled MFE and no immediate catastrophic failure. But even here, Green is not automatic because the policy must turn into profitable booking volume.

### Price path

Key Stock-Web rows:

```text
2024-11-04: close 50,900
2024-11-08: high 52,500 / close 51,800
2024-11-20: high 55,400 / close 54,900
2024-11-27: high 60,000 / close 59,800
2024-12-09: low 52,700 / close 53,000
2025-02-11: high 58,500 / close 58,500
2025-04-09: low 46,200 / close 47,500
```

Approximate path from entry close:

```text
entry_close: 50,900
peak_high: 60,000
MFE: +17.9%
worst_low: 46,200
MAE: -9.2%
```

### Interpretation

This is a positive but capped C31 service-policy case:

```text
Stage2-Actionable: allowed if actual booking / package margin bridge is explicit.
Stage3-Green: blocked from visa-policy headline alone.
4B: not required immediately, but monitor after policy-driven MFE.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  booking_conversion_bridge: medium_high
  channel/direct_customer_access: high
  margin_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: low_to_medium
```

---

## 6. Case 2 — 080160 모두투어

```yaml
case_id: C31_R12L91_080160_2024_11_04
symbol: "080160"
name: "모두투어"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE
trigger_date: 2024-11-04
entry_date: 2024-11-04
entry_price_basis: close
entry_price: 11400
classification: counterexample_theme_spike_without_durable_booking_margin_bridge
calibration_usable: true
```

### Evidence interpretation

모두투어 is the weaker agency case. It had a policy/theme spike, but the forward path failed durability.

The model risk:

```text
visa-free policy
  -> all travel agencies look like beneficiaries
  -> entry after spike
  -> booking/margin bridge not verified
  -> drawdown arrives
```

### Price path

Key Stock-Web rows:

```text
2024-11-04: close 11,400
2024-11-04: high 12,450
2024-11-13: low 9,220 / close 9,350
2024-11-25: high 12,110 / close 10,410
2024-12-30: low 9,280 / close 9,700
2025-02-03: low 9,270 / close 9,380
2025-03-26: high 11,280 / close 11,160
```

Approximate path from entry close:

```text
entry_close: 11,400
peak_high: 12,450
MFE: +9.2%
worst_low: 9,220
MAE: -19.1%
```

### Interpretation

This is a false-positive / Watch-Yellow cap case:

```text
Stage2-Watch: allowed from policy relevance.
Stage2-Actionable: blocked unless booking margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: not quite, but false-positive guard applies.
```

The initial policy spike was not enough to support a durable C31 positive.

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: high
  booking_bridge: weak_to_medium
  margin_bridge: weak
  local_price_spike: medium
  price_survival: weak
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 094850 참좋은여행

```yaml
case_id: C31_R12L91_094850_2024_11_04
symbol: "094850"
name: "참좋은여행"
canonical_archetype_id: C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id: CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE
trigger_date: 2024-11-04
entry_date: 2024-11-04
entry_price_basis: close
entry_price: 6070
classification: local_burst_high_mae_small_travel_agency_counterexample
calibration_usable: true
```

### Evidence interpretation

참좋은여행 is the local-burst case. It had the strongest first reaction, but the path immediately showed why C31 needs a bridge requirement.

The company can be a real travel-service name, but the stock path says the event was mostly:

```text
small-cap policy/theme burst
```

rather than confirmed booking and margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-11-04: close 6,070
2024-11-05: high 7,890 / close 6,340
2024-11-14: low 4,765 / close 4,790
2024-11-26: high 6,480 / close 5,660
2024-12-26: high 6,530 / close 5,610
2025-02-13: high 6,370 / close 5,400
2025-04-02: high 7,020 / close 5,860
```

Approximate path from entry close:

```text
entry_close: 6,070
peak_high: 7,890
MFE: +30.0%
worst_low: 4,765
MAE: -21.5%
```

### Interpretation

This is a local-burst / high-MAE counterexample:

```text
Stage2-Watch: allowed.
Stage2-Actionable: only as event-trading / local 4B, not durable Green.
Stage3-Green: blocked without booking and margin bridge.
Hard 4C: borderline, but primary classification is local-burst failure.
```

The first reaction was large, but the drawdown came too quickly. That is the 4B/Green boundary.

### Stress-test components

```text
raw_component_score_proxy:
  policy_relevance: medium_high
  small_travel_agency_beta: high
  booking_conversion_bridge: weak
  local_price_burst: high
  price_survival: failed
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C31 travel-service grid:

```text
039130 하나투어:
  policy-relevant large travel agency;
  controlled MFE and manageable MAE, but Green requires booking/margin bridge.

080160 모두투어:
  policy/theme spike did not survive enough;
  Watch/Yellow cap without clear booking conversion.

094850 참좋은여행:
  strong local burst but high-MAE path;
  4B/event-trading bucket, not Green.
```

Shared rule:

```text
C31 travel policy is not "visa-free = all travel stocks Green."
C31 travel policy is "policy access converts into profitable bookings and margin through a company-specific channel."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C31_R12L91_039130_2024_11_04","scheduled_round":"R12","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE","symbol":"039130","name":"하나투어","trigger_date":"2024-11-04","entry_date":"2024-11-04","entry_price":50900,"peak_high":60000,"peak_date":"2024-11-27","worst_low":46200,"worst_low_date":"2025-04-09","mfe_pct":17.9,"mae_pct":-9.2,"classification":"positive_with_booking_bridge_watch","calibration_usable":true,"evidence_family":"large_travel_agency_policy_access_to_booking_margin_bridge","residual_error":"positive_path_still_needs_booking_and_margin_bridge_before_green","shadow_rule_candidate":"allow_actionable_when_booking_conversion_and_package_margin_bridge_confirm"}
{"row_type":"case","case_id":"C31_R12L91_080160_2024_11_04","scheduled_round":"R12","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE","symbol":"080160","name":"모두투어","trigger_date":"2024-11-04","entry_date":"2024-11-04","entry_price":11400,"peak_high":12450,"peak_date":"2024-11-04","worst_low":9220,"worst_low_date":"2024-11-13","mfe_pct":9.2,"mae_pct":-19.1,"classification":"counterexample_theme_spike_without_durable_booking_margin_bridge","calibration_usable":true,"evidence_family":"travel_agency_policy_spike_without_durable_booking_margin_bridge","residual_error":"policy_reopening_theme_can_overpromote_without_booking_conversion","shadow_rule_candidate":"cap_at_watch_yellow_when_mfe_shallow_and_booking_margin_bridge_weak"}
{"row_type":"case","case_id":"C31_R12L91_094850_2024_11_04","scheduled_round":"R12","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE","symbol":"094850","name":"참좋은여행","trigger_date":"2024-11-04","entry_date":"2024-11-04","entry_price":6070,"peak_high":7890,"peak_date":"2024-11-05","worst_low":4765,"worst_low_date":"2024-11-14","mfe_pct":30.0,"mae_pct":-21.5,"classification":"local_burst_high_mae_small_travel_agency_counterexample","calibration_usable":true,"evidence_family":"small_travel_agency_policy_burst_without_price_survival","residual_error":"small_cap_policy_burst_can_be_mistaken_for_green_without_booking_margin_bridge","shadow_rule_candidate":"classify_high_mfe_high_mae_small_travel_agency_as_4b_not_green"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R12","scheduled_loop":91,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"CHINA_VISA_FREE_TRAVEL_SERVICE_POLICY_TO_BOOKING_REVENUE_BRIDGE_VS_TRAVEL_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R12","scheduled_loop":91,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","rule_id":"C31_TRAVEL_POLICY_BOOKING_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C31 travel-service policy events, do not open Stage2-Actionable or Stage3-Green from visa-free, travel reopening, airline access, or tourism policy headline alone. Require company-specific booking conversion, package availability, seat supply, commission/take-rate, cancellation risk, FX/fuel cost check, margin/OP conversion, and post-trigger price survival. Large agencies may be Actionable when booking and margin bridge are explicit. Small travel-agency policy bursts with high MAE should remain local 4B or Watch, not Green.","expected_effect":"Reduce tourism-policy false positives while preserving large travel-agency positives when policy access converts into profitable bookings.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R12","scheduled_loop":91,"canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","residual_type":"travel_policy_booking_margin_guard","contribution":"Adds one large travel-agency positive, one mid-agency false-positive, and one small-agency local-burst failure to calibrate C31 service-policy bridge requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C31_TRAVEL_POLICY_BOOKING_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C31_POLICY_SUBSIDY_LEGISLATION_EVENT
AND policy_event_family in [visa_free, tourism_reopening, travel_access, airline_access]:

  Do not open Stage3-Green from:
    - visa-free headline alone
    - travel reopening label alone
    - one-day travel-agency spike alone
    - China travel theme alone
    - generic tourism policy headline alone

  Require at least two of:
    - company-specific booking conversion
    - China or relevant destination package inventory
    - seat supply / airline capacity
    - commission or take-rate bridge
    - cancellation / refund risk containment
    - FX/fuel cost bridge
    - margin / OP conversion
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -15%:
    cap at Watch/Yellow or false-positive guard.

  If MFE > 25% but MAE < -20%:
    classify as local 4B / event burst, not Green.

  Distinguish:
    - large agencies with booking-channel and margin conversion
    - from small travel-agency beta where policy creates only a liquidity spike.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R12_loop_91_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C31 travel-service policy cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C31_TRAVEL_POLICY_BOOKING_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C31 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C31 service-policy cases agree, consider implementing a canonical guard that:
   - blocks visa/travel-policy Green without booking and margin bridge,
   - preserves large-agency positives only with booking conversion and price survival,
   - routes shallow-MFE/high-MAE policy spikes to false-positive guard,
   - keeps high-MFE/high-MAE small travel-agency bursts as local 4B.

Expected next schedule:
completed_round = R12
completed_loop = 91
next_round = R13
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R12
completed_loop = 91
next_round = R13
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
