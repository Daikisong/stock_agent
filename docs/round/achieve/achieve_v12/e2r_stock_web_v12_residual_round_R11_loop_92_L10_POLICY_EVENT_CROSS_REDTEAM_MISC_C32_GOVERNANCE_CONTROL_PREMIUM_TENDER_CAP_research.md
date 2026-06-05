# E2R Stock-Web v12 Residual Research — R11 / Loop 92

```yaml
scheduled_round: R11
scheduled_loop: 92
large_sector_id: L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE

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
watch_or_cap_case_count: 3
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
accounting_or_listing_trust_caveat_count: 0
tender_or_delisting_cap_case_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R11
completed_loop: 92
next_round: R12
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R10_loop_92_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R11
scheduled_loop = 92
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

R11 can use:

```text
L10_POLICY_EVENT_CROSS_REDTEAM_MISC
```

unless the event is explicitly policy-defense-linked. This run is a governance / control-premium / tender-offer event family, so L10 is the correct large-sector gate.

Recent R11 branch usage:

```text
loop90: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP — Doosan governance/control branch
loop91: C31_POLICY_SUBSIDY_LEGISLATION_EVENT — AI semiconductor policy branch
```

This run returns to C32 but uses a different fine branch:

```text
public tender / voluntary delisting / control-premium cap
vs post-announcement Green chase
```

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
003410 쌍용C&E
115390 락앤락
119860 커넥트웨이브
```

These avoid the top-covered C32 symbols and avoid the recent R11 loop90/91 names:

```text
loop90 avoid: 454910, 034020, 241560
loop91 avoid: 000660, 005930, 000990
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
003410: same archetype, new symbol, tender/delisting cap late-entry counterexample
115390: same archetype, new symbol, public tender cap positive with narrow post-announcement upside
119860: same archetype, new symbol, public tender/delisting positive with clean cap and low-MAE path
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
003410 쌍용C&E
  profile: atlas/symbol_profiles/003/003410.json
  first_date: 1995-05-02
  raw_last_date: 2024-07-08
  tradable last_date: 2024-06-20
  latest_close: 7,000
  latest_market: KOSPI
  row_status_counts:
    tradable_ohlcv: 7,305
    non_tradable_zero_volume: 67
  corporate_action_candidate_dates:
    1999-05-20, 1999-06-15, 2000-11-15, 2004-01-07, 2005-12-19, 2018-07-11
  2024 entry~D+180 contamination: none
  status_inferred: inactive_or_delisted_like

115390 락앤락
  profile: atlas/symbol_profiles/115/115390.json
  first_date: 2010-01-28
  raw_last_date: 2024-12-06
  tradable last_date: 2024-11-19
  latest_close: 8,660
  latest_market: KOSPI
  row_status_counts:
    tradable_ohlcv: 3,637
    non_tradable_zero_volume: 27
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  status_inferred: inactive_or_delisted_like

119860 커넥트웨이브
  profile: atlas/symbol_profiles/119/119860.json
  name history:
    다나와 until 2022-12-15
    커넥트웨이브 from 2022-12-16 to 2024-09-23
  first_date: 2011-01-24
  raw_last_date: 2024-09-23
  tradable last_date: 2024-09-03
  latest_close: 18,000
  latest_market: KOSDAQ
  row_status_counts:
    tradable_ohlcv: 3,354
    non_tradable_zero_volume: 11
  corporate_action_candidate_dates:
    2016-12-28, 2017-01-19, 2022-12-16
  2024 entry~D+180 contamination: none
  status_inferred: inactive_or_delisted_like
```

---

## 4. Archetype residual problem

C32 is not a normal operational rerating archetype.

The model can over-score:

```text
public tender offer
voluntary delisting
control premium
governance improvement
private-equity acquisition
minority squeeze-out
one-day control-premium gap-up
```

as if the stock has open-ended upside.

C32 must instead ask:

```text
tender or control event
  -> offer price / cap
  -> probability of completion
  -> residual spread
  -> liquidity / delisting path
  -> minority-shareholder risk
  -> price survival and opportunity cost
```

A tender-offer stock is like a train approaching a fixed station. The early passenger can ride the gap. But after the train is already parked near the platform, the model must not call it a highway with unlimited distance.

---

## 5. Case 1 — 003410 쌍용C&E

```yaml
case_id: C32_R11L92_003410_2024_02_05
symbol: "003410"
name: "쌍용C&E"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE
trigger_date: 2024-02-05
entry_date: 2024-02-05
entry_price_basis: close
entry_price: 6940
classification: counterexample_late_entry_tender_cap_no_green
calibration_usable: true
```

### Evidence interpretation

쌍용C&E is the late-entry cap counterexample.

The public tender / delisting thesis was real, but by the 2024-02-05 close the price had already moved near the cap. From that point, the stock did not have a normal Stage3-Green upside profile. It had:

```text
small residual spread
high completion dependency
limited upside
delisting / liquidity endpoint
```

### Price path

Key Stock-Web rows:

```text
2024-02-01: close 6,320
2024-02-02: high 6,410 / close 6,410
2024-02-05: high 6,960 / close 6,940
2024-02-06: high 6,950 / close 6,920
2024-02-29: high 6,980 / close 6,980
2024-03-15: high 7,040 / close 7,000
2024-06-20: high 7,010 / close 7,000
```

Approximate path from entry close:

```text
entry_close: 6,940
peak_high: 7,040
MFE: +1.4%
worst_low_after_entry: 6,780 on 2024-03-05
MAE: -2.3%
```

### Interpretation

This is not a catastrophic failure. It is a Green-chase failure:

```text
Stage2-Watch: valid.
Stage2-Actionable: possible only as residual-spread / event-arb, not normal rerating.
Stage3-Green: blocked.
Hard 4C: no.
```

C32 must cap upside once price is already pinned near the tender price.

### Stress-test components

```text
raw_component_score_proxy:
  tender_event_relevance: very_high
  offer_price_cap_visibility: very_high
  residual_spread_after_entry: very_low
  completion_dependency: high
  liquidity_delisting_endpoint: high
  price_survival: high_but_capped
  green_cap: mandatory
```

---

## 6. Case 2 — 115390 락앤락

```yaml
case_id: C32_R11L92_115390_2024_04_17
symbol: "115390"
name: "락앤락"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE
trigger_date: 2024-04-17
entry_date: 2024-04-17
entry_price_basis: close
entry_price: 8180
classification: positive_public_tender_gap_then_cap_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

락앤락 is the clean tender positive, but it also shows the cap.

The useful C32 bridge is:

```text
public tender / private-equity control event
  -> tender price visibility
  -> high completion probability
  -> price pins near offer
  -> limited residual spread
  -> delisting endpoint
```

The stock had meaningful upside for the event entry, but once it pinned near 8,700~8,800, further Green was not justified.

### Price path

Key Stock-Web rows:

```text
2024-04-16: close 7,330
2024-04-17: high 8,290 / close 8,180
2024-04-18: high 8,720 / close 8,680
2024-05-08: high 8,890 / close 8,700
2024-06-11: high 8,820 / close 8,780
2024-07-24: price remains pinned near 8,750~8,760 area
```

Approximate path from entry close:

```text
entry_close: 8,180
peak_high: 8,890
MFE: +8.7%
worst_post_entry_low_checked: 8,630 on 2024-05-14
MAE: positive cushion after close entry
```

### Interpretation

This is a C32 positive, not C18/C19 consumer brand rerating:

```text
Stage2-Actionable: valid as tender/event-arb when spread and completion probability are explicit.
Stage3-Green: blocked after the cap is reached.
Local 4B: attach after gap-to-cap if no residual spread remains.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  tender_event_relevance: high
  offer_cap_visibility: high
  completion_probability: medium_high
  residual_spread_after_gap: low
  price_survival: high
  open_ended_rerating_score: low
  local_4b_overlay: required_after_cap
```

---

## 7. Case 3 — 119860 커넥트웨이브

```yaml
case_id: C32_R11L92_119860_2024_04_26
symbol: "119860"
name: "커넥트웨이브"
canonical_archetype_id: C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
fine_archetype_id: PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE
trigger_date: 2024-04-26
entry_date: 2024-04-26
entry_price_basis: close
entry_price: 15570
classification: positive_clean_tender_cap_low_mae_event_arb
calibration_usable: true
```

### Evidence interpretation

커넥트웨이브 is the cleanest C32 tender-cap positive in this set.

The price path jumped into the tender-cap zone and then became pinned near 17,900~18,000. This is exactly what C32 should recognize:

```text
real governance/control premium
but finite tender-price upside
```

The model should not mistake the pinned price for a normal platform/SW rerating.

### Price path

Key Stock-Web rows:

```text
2024-04-25: close 13,100
2024-04-26: high 16,100 / close 15,570
2024-04-29: high 17,880 / close 17,880
2024-05-10: high 17,930 / close 17,900
2024-06-18: high 18,010 / close 18,000
2024-06-26: high 18,300 / close 18,160
2024-07-23: price remains pinned near 18,000 area
```

Approximate path from entry close:

```text
entry_close: 15,570
peak_high: 18,300
MFE: +17.5%
worst_post_entry_low_checked: above entry after close entry
MAE: positive cushion after close entry
```

### Interpretation

This is a strong C32 positive, but Green is still capped:

```text
Stage2-Actionable: valid as event-arb / tender-cap trade.
Stage3-Green: blocked after price approaches offer cap.
Local 4B: required after cap convergence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  tender_event_relevance: very_high
  control_premium_visibility: high
  residual_spread_after_entry: medium_then_low
  completion_dependency: high
  price_survival: high
  liquidity_delisting_endpoint: high
  green_cap: mandatory
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
watch_or_cap_case_count: 3
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 0
tender_or_delisting_cap_case_count: 3
calibration_usable_trigger_count: 3
```

The three-case C32 tender-cap grid:

```text
003410 쌍용C&E:
  true tender/delisting event,
  but late entry near cap left almost no upside.
  Green-chase blocked.

115390 락앤락:
  tender positive,
  but once pinned near cap, it becomes event-arb / residual-spread only.

119860 커넥트웨이브:
  clean tender-cap positive,
  strongest MFE from event entry,
  but still capped after convergence.
```

Shared rule:

```text
C32 is not "control premium headline = unlimited rerating."
C32 is "control premium creates a finite tender-price spread whose upside disappears as price converges to the offer cap."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C32_R11L92_003410_2024_02_05","scheduled_round":"R11","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE","symbol":"003410","name":"쌍용C&E","trigger_date":"2024-02-05","entry_date":"2024-02-05","entry_price":6940,"peak_high":7040,"peak_date":"2024-03-15","worst_low_after_entry":6780,"worst_low_after_entry_date":"2024-03-05","mfe_pct":1.4,"mae_pct":-2.3,"classification":"counterexample_late_entry_tender_cap_no_green","calibration_usable":true,"evidence_family":"public_tender_delisting_cap_late_entry_residual_spread","residual_error":"tender_event_can_be_real_but_late_entry_has_no_green_upside","shadow_rule_candidate":"block_stage3_green_when_price_already_converged_to_offer_cap"}
{"row_type":"case","case_id":"C32_R11L92_115390_2024_04_17","scheduled_round":"R11","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE","symbol":"115390","name":"락앤락","trigger_date":"2024-04-17","entry_date":"2024-04-17","entry_price":8180,"peak_high":8890,"peak_date":"2024-05-08","worst_post_entry_low_checked":8630,"worst_post_entry_low_checked_date":"2024-05-14","mfe_pct":8.7,"mae_pct":0.0,"classification":"positive_public_tender_gap_then_cap_with_4b_watch","calibration_usable":true,"evidence_family":"public_tender_control_premium_gap_to_offer_cap","residual_error":"positive_event_path_becomes_capped_after_offer_convergence","shadow_rule_candidate":"allow_event_arb_actionable_but_attach_4b_and_block_green_after_cap"}
{"row_type":"case","case_id":"C32_R11L92_119860_2024_04_26","scheduled_round":"R11","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE","symbol":"119860","name":"커넥트웨이브","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":15570,"peak_high":18300,"peak_date":"2024-06-26","worst_post_entry_low_checked":17760,"worst_post_entry_low_checked_date":"2024-05-24","mfe_pct":17.5,"mae_pct":0.0,"classification":"positive_clean_tender_cap_low_mae_event_arb","calibration_usable":true,"evidence_family":"public_tender_delisting_control_premium_low_mae_cap_convergence","residual_error":"clean_tender_positive_still_has_finite_offer_cap_not_open_ended_green","shadow_rule_candidate":"preserve_tender_positive_as_event_arb_but_cap_stage3_green_after_convergence"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R11","scheduled_loop":92,"large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","fine_archetype_id":"PUBLIC_TENDER_DELISTING_CONTROL_PREMIUM_CAP_VS_POST_ANNOUNCEMENT_GREEN_CHASE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":3,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":0,"tender_or_delisting_cap_case_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R11","scheduled_loop":92,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","rule_id":"C32_TENDER_OFFER_CAP_AND_RESIDUAL_SPREAD_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C32, do not open Stage3-Green from public tender, voluntary delisting, control premium, private-equity acquisition, governance improvement, or minority squeeze-out headline alone. Require offer price, residual spread, completion probability, acceptance/tender risk, liquidity and delisting endpoint, and post-announcement price survival. If price is already within roughly 1-2% of the offer cap, block Green and classify as Watch/event-arb only. If event entry captures meaningful gap but then price pins near cap, preserve positive classification but attach local 4B. Delisting/inactive-like status after completion should not be treated as accounting failure by itself; it is the expected endpoint of a tender-cap case.","expected_effect":"Preserve real tender/control-premium positives while preventing post-announcement Green chase after the offer cap is reached.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R11","scheduled_loop":92,"canonical_archetype_id":"C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP","residual_type":"public_tender_delisting_cap_guard","contribution":"Adds one late-entry tender-cap counterexample and two tender/delisting positives to calibrate C32 residual spread, offer-cap convergence, event-arb actionability, and Green-block rules.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C32_TENDER_OFFER_CAP_AND_RESIDUAL_SPREAD_REQUIRED

IF canonical_archetype_id == C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP:

  Do not open Stage3-Green from:
    - public tender headline alone
    - voluntary delisting headline alone
    - control-premium headline alone
    - private-equity acquisition label alone
    - governance improvement label alone
    - one-day tender gap-up alone

  Require at least two of:
    - explicit offer price
    - residual spread to offer price
    - completion probability / acceptance condition
    - tender or squeeze-out mechanics
    - liquidity / delisting endpoint
    - low-MAE post-announcement price survival
    - event timeline visibility

  If price is already within roughly 1~2% of offer price:
    block Stage3-Green and cap at Watch / event-arb.

  If event entry captures MFE but price later pins near the offer:
    preserve positive event classification but attach local 4B.

  If delisting/inactive-like status appears after completion:
    do not automatically treat it as accounting failure;
    classify it as expected tender endpoint unless there is a separate trust problem.

  Distinguish:
    - early tender entries with residual spread
    - from late post-announcement entries where the upside has already been consumed.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R11_loop_92_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C32 public tender / delisting / control-premium cap cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C32_TENDER_OFFER_CAP_AND_RESIDUAL_SPREAD_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C32 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C32 cases agree, consider implementing a canonical guard that:
   - blocks Stage3-Green when price has already converged to tender/offer cap,
   - preserves early tender positives as event-arb / capped Actionable,
   - attaches local 4B after gap-to-cap convergence,
   - treats inactive/delisted-like status as expected endpoint when it follows a successful tender/delisting event.

Expected next schedule:
completed_round = R11
completed_loop = 92
next_round = R12
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R11
completed_loop = 92
next_round = R12
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
