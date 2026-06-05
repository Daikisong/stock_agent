# E2R Stock-Web v12 Residual Research — R8 / Loop 97

```yaml
scheduled_round: R8
scheduled_loop: 97
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
media_studio_case_count: 2
kids_animation_ip_case_count: 1
global_distribution_windowing_case_count: 2
content_ip_monetization_bridge_missing_count: 2
market_segment_or_name_history_caveat_count: 2
short_listing_caveat_count: 1
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 97
next_round: R9
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_97_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 97
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage:

```text
loop94: C27_CONTENT_IP_GLOBAL_MONETIZATION
loop95: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop96: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

This run returns to C27 after the R8 branch cycle, but avoids the C27 top-covered names and prior loop94 C27 set.

Selected fine branch:

```text
media studio / broadcaster-commerce hybrid / kids animation IP
global distribution, windowing, licensing, merchandising, ad/subscriber economics, production cost, and margin bridge
vs generic content/IP label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C27_CONTENT_IP_GLOBAL_MONETIZATION
rows: 39
symbols: 15
date_range: 2021-01-22~2024-09-26
good/bad S2: 20/6
4B/4C: 3/1
URL pending/proxy: 6/6
top covered symbols:
  263750(5), 112040(4), 122870(4), 293490(4), 259960(3), 376300(3)
```

Selected symbols:

```text
035760 CJ ENM
036420 콘텐트리중앙
419530 SAMG엔터
```

They avoid the C27 top-covered list and recent R8 branch names:

```text
C27 top-covered avoid:
  263750, 112040, 122870, 293490, 259960, 376300

R8 loop94 C27 avoid:
  251270, 035900, 253450

R8 loop95 C26 avoid:
  060250, 064260, 216050

R8 loop96 C28 avoid:
  136540, 060850, 053800
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
035760: same archetype, new symbol, media/studio-commerce content IP local positive with Green cap after later evidence decay
036420: same archetype, new symbol, studio/content production local burst followed by high-MAE 4B failure
419530: same archetype, new symbol, kids animation / character IP hard-4C candidate from first-half label failure before later new event window
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
035760 CJ ENM
  profile: atlas/symbol_profiles/035/035760.json
  name history includes:
    CJ39쇼핑, CJ홈쇼핑, CJ오쇼핑, CJ ENM
  selected 2024 trigger name:
    CJ ENM
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  first_date: 1999-11-23
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,448
  non_tradable_zero_volume rows: 20
  corporate_action_candidate_dates:
    2006-09-12, 2010-09-30, 2018-07-18
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action and name-history windows are outside the selected 2024 validation window.

036420 콘텐트리중앙
  profile: atlas/symbol_profiles/036/036420.json
  name history includes:
    한길무역, 일간스포츠, ISPLUS, 제이콘텐트리, 콘텐트리중앙
  selected 2024 trigger name:
    콘텐트리중앙
  market:
    KOSDAQ until 2019-10-17
    KOSPI from 2019-10-18
  first_date: 2000-03-23
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,356
  non_tradable_zero_volume rows: 31
  corporate_action_candidate_dates:
    historical only, latest 2019-08-02
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action and market-transfer history are outside the selected 2024 validation window.

419530 SAMG엔터
  profile: atlas/symbol_profiles/419/419530.json
  first_date: 2022-12-06
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 782
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    short listing history. Later September 2024 event window must be separated from the first-half trigger.
```

---

## 4. Archetype residual problem

C27 is about content IP global monetization. It is not a generic "content stock" or "K-content label is hot" archetype.

The model can over-score:

```text
K-content / drama / movie / animation label
global OTT distribution headline
studio production slate
box-office or theatrical release buzz
game / character / kids IP label
merchandising or licensing rumor
one-week content-stock volume spike
late chase after content/IP event rerating
```

The C27 bridge must be stricter:

```text
content / IP monetization event
  -> named title, franchise, platform, geography, or channel
  -> distribution window and release schedule
  -> contract structure and revenue recognition
  -> advertising, subscription, box office, licensing, or merchandising conversion
  -> production cost, participation cost, and marketing cost
  -> hit-rate / slate concentration risk
  -> recoupment, cash collection, and margin / OP conversion
  -> price survival after the first content-label spike
```

A C27 content thesis is like a film leaving the editing room. The poster creates attention, but equity value appears only when the title reaches paying windows, distributors reorder or platforms pay, merchandise or licensing converts, production and marketing costs are recouped, and the IP leaves cash rather than just applause.

---

## 5. Case 1 — 035760 CJ ENM

```yaml
case_id: C27_R8L97_035760_2024_02_01
symbol: "035760"
name: "CJ ENM"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 73900
classification: local_positive_media_studio_commerce_content_ip_global_windowing_with_green_cap_after_later_decay
calibration_usable: true
```

### Evidence interpretation

CJ ENM is the constructive C27 control in this set.

The useful C27 read is not simply:

```text
콘텐츠 / K-content 대형주가 움직였다
```

It is:

```text
media studio and commerce hybrid
  -> content IP / channel / platform monetization optionality
  -> studio slate and advertising/subscription/commerce bridge
  -> early February price confirmation
  -> later evidence-decay and Green cap
```

The forward path produced meaningful MFE early in the window. The later path did not become a hard failure, but it did decay materially into October. That makes this a local positive or capped positive, not an unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 74,000 / close 73,900
2024-02-07: high 84,800 / close 83,400
2024-02-08: high 89,300 / close 86,200
2024-04-01: high 86,800 / close 86,000
2024-08-05: low 70,000 / close 73,600
2024-10-25: low 60,400 / close 61,300
```

Approximate path from entry close:

```text
entry_close: 73,900
peak_high: 89,300
MFE: +20.8%
worst_low_after_entry: 60,400
MAE: -18.3%
```

### Interpretation

This is a C27 local positive with Green cap:

```text
Stage2-Actionable: possible if named title/slate/channel, distribution window, revenue recognition, and margin bridge are explicit.
Stage3-Green: blocked without fresh windowing, platform, ad/subscriber, licensing, and margin evidence.
Local 4B: monitor after +20% MFE if execution evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  media_studio_relevance: high
  global_distribution_bridge: medium_high
  ad_subscription_commerce_bridge: medium
  content_cost_recoupment_bridge: medium
  price_confirmation: medium_high_initial
  later_evidence_decay: medium
  green_cap: required
```

---

## 6. Case 2 — 036420 콘텐트리중앙

```yaml
case_id: C27_R8L97_036420_2024_02_01
symbol: "036420"
name: "콘텐트리중앙"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12030
classification: local_burst_studio_content_label_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

콘텐트리중앙 is the studio/content local-burst 4B failure.

The setup had real C27 relevance:

```text
studio / drama / film content label
  -> distribution and release-slate optionality
  -> early 2024 content-sector rebound
  -> meaningful local MFE into spring
```

The path then failed price survival badly. This means the first content-label response should not be scored as durable Green unless the monetization bridge is refreshed: named titles, windowing, platform economics, cost recoupment, and OP conversion.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,150 / close 12,030
2024-02-21: high 13,390 / close 13,390
2024-04-22: high 14,980 / close 14,440
2024-08-05: low 8,040 / close 8,280
2024-09-24: high 11,210 / close 11,100
2024-11-07: low 8,790 / close 9,000
```

Approximate path from entry close:

```text
entry_close: 12,030
peak_high: 14,980
MFE: +24.5%
worst_low_after_entry: 8,040
MAE: -33.2%
```

### Interpretation

This is a C27 local burst / 4B failure:

```text
Stage2-Watch: valid from studio/content relevance.
Stage2-Actionable: possible only if title pipeline, platform/distributor contract, recoupment, and margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  studio_content_relevance: high
  release_slate_bridge: medium
  global_distribution_bridge: weak_to_medium
  cost_recoupment_bridge: weak
  margin_op_bridge: weak
  price_confirmation: high_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 419530 SAMG엔터

```yaml
case_id: C27_R8L97_419530_2024_02_01
symbol: "419530"
name: "SAMG엔터"
canonical_archetype_id: C27_CONTENT_IP_GLOBAL_MONETIZATION
fine_archetype_id: MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 16360
classification: hard_4c_candidate_kids_animation_ip_first_phase_without_merchandising_margin_survival_before_later_reignition
calibration_usable: true
```

### Evidence interpretation

SAMG엔터 is the kids animation / character-IP hard guardrail for the first event phase.

The label can fool the model:

```text
kids animation / character IP
  -> merchandising and licensing optionality
  -> global animation / toy channel readthrough
  -> small-cap IP beta
```

From the selected first-half trigger, the path failed first. A later September 2024 surge is a renewed event window and should not retroactively validate the February entry. C27 must separate first-phase IP-label failure from later event-window re-ignition.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 16,830 / close 16,360
2024-03-04: high 18,500 / close 15,720
2024-04-17: low 12,900 / close 12,980
2024-08-05: low 9,940 / close 10,500
2024-09-09: high 15,610 / close 15,610
2024-09-13: high 19,630 / close 19,310
2024-10-25: low 12,880 / close 12,880
```

Approximate first-phase path from entry close:

```text
entry_close: 16,360
peak_high_first_phase: 18,500
MFE: +13.1%
worst_low_before_later_reignition: 9,940
MAE: -39.2%
```

### Interpretation

This is a C27 hard-4C candidate for the first event phase:

```text
Stage2-Watch: possible from kids animation / character-IP relevance.
Stage2-Actionable: blocked unless merchandising, licensing, distributor reorder, and margin bridge are explicit.
Stage3-Green: blocked for the February entry.
Hard 4C candidate: yes, because the first phase had high MAE before later renewed event.
Later event caveat: September 2024 should be treated as a new event window, not a rescue of the February trigger.
Short-listing caveat: yes.
```

### Stress-test components

```text
raw_component_score_proxy:
  kids_animation_ip_label: high
  merchandise_licensing_bridge: weak
  global_channel_bridge: weak_to_medium
  cost_inventory_bridge: weak
  price_confirmation_first_phase: shallow_to_medium
  event_window_separation_required: high
  drawdown_penalty: high
  hard_4c_guard: candidate
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
media_studio_case_count: 2
kids_animation_ip_case_count: 1
global_distribution_windowing_case_count: 2
content_ip_monetization_bridge_missing_count: 2
market_segment_or_name_history_caveat_count: 2
short_listing_caveat_count: 1
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C27 content/IP grid:

```text
035760 CJ ENM:
  media/studio-commerce content IP local positive;
  meaningful MFE and moderate MAE, but Green requires fresh content monetization and margin evidence.

036420 콘텐트리중앙:
  studio/content local burst;
  meaningful MFE first, then high MAE, local 4B failure.

419530 SAMG엔터:
  kids animation / character-IP first phase failed before later renewed event;
  hard 4C candidate with event-window separation.
```

Shared rule:

```text
C27 is not "content label is hot."
C27 is "named IP, release window, platform/distributor economics, licensing/merchandising, cost recoupment, cash collection, and OP margin are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C27_R8L97_035760_2024_02_01","scheduled_round":"R8","scheduled_loop":97,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE","symbol":"035760","name":"CJ ENM","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":73900,"peak_high":89300,"peak_date":"2024-02-08","worst_low_after_entry":60400,"worst_low_after_entry_date":"2024-10-25","mfe_pct":20.8,"mae_pct":-18.3,"classification":"local_positive_media_studio_commerce_content_ip_global_windowing_with_green_cap_after_later_decay","calibration_usable":true,"market_segment_or_name_history_caveat":true,"evidence_family":"media_studio_content_ip_global_distribution_windowing_ad_subscription_commerce_margin_bridge","residual_error":"content_ip_positive_requires_green_cap_without_refreshed_windowing_platform_cost_recoupment_margin_evidence","shadow_rule_candidate":"preserve_media_studio_local_positive_but_cap_green_when_content_monetization_bridge_is_stale"}
{"row_type":"case","case_id":"C27_R8L97_036420_2024_02_01","scheduled_round":"R8","scheduled_loop":97,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE","symbol":"036420","name":"콘텐트리중앙","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12030,"peak_high":14980,"peak_date":"2024-04-22","worst_low_after_entry":8040,"worst_low_after_entry_date":"2024-08-05","mfe_pct":24.5,"mae_pct":-33.2,"classification":"local_burst_studio_content_label_high_mae_4b_failure","calibration_usable":true,"market_segment_or_name_history_caveat":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"studio_drama_film_content_label_without_sustained_platform_distribution_recoupment_margin_survival","residual_error":"studio_content_label_can_create_mfe_but_fail_green_without_named_title_windowing_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_studio_content_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C27_R8L97_419530_2024_02_01","scheduled_round":"R8","scheduled_loop":97,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE","symbol":"419530","name":"SAMG엔터","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":16360,"peak_high_first_phase":18500,"peak_date":"2024-03-04","worst_low_before_later_reignition":9940,"worst_low_before_later_reignition_date":"2024-08-05","mfe_pct":13.1,"mae_pct":-39.2,"classification":"hard_4c_candidate_kids_animation_ip_first_phase_without_merchandising_margin_survival_before_later_reignition","calibration_usable":true,"short_listing_caveat":true,"event_window_separation_required":true,"evidence_family":"kids_animation_character_ip_label_without_merchandising_licensing_distribution_margin_bridge","residual_error":"character_ip_first_phase_can_fail_before_later_reignition_and_must_not_be_retroactively_validated","shadow_rule_candidate":"route_kids_animation_ip_first_phase_to_hard_4c_if_mae_large_before_new_event_window"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":97,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","fine_archetype_id":"MEDIA_STUDIO_KIDS_ANIMATION_CONTENT_IP_GLOBAL_DISTRIBUTION_WINDOWING_MARGIN_BRIDGE_VS_CONTENT_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"media_studio_case_count":2,"kids_animation_ip_case_count":1,"global_distribution_windowing_case_count":2,"content_ip_monetization_bridge_missing_count":2,"market_segment_or_name_history_caveat_count":2,"short_listing_caveat_count":1,"row_presence_or_old_corporate_action_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":97,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","rule_id":"C27_CONTENT_IP_WINDOWING_RECOUPMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C27 content/IP global monetization cases, do not open Stage2-Actionable or Stage3-Green from K-content, drama, movie, animation, game IP, character IP, global OTT distribution, studio production slate, box-office buzz, merchandising/licensing rumor, one-week content-stock volume spike, or late chase after content/IP event rerating labels alone. Require named title/franchise/platform/geography/channel, distribution window and release schedule, contract structure and revenue recognition, advertising/subscription/box office/licensing/merchandising conversion, production/participation/marketing cost recoupment, hit-rate and slate concentration risk check, cash collection and margin/OP conversion, and post-trigger price survival. Media/studio positives with meaningful MFE may be capped Actionable when windowing and margin bridge are explicit, but Green requires fresh evidence. Studio/content labels with meaningful MFE followed by high MAE should remain local 4B, not Green. Kids animation/character-IP first phases with high MAE before a later renewed event should route to hard-4C candidate, with later event windows separated from earlier failed triggers.","expected_effect":"Preserve true content/IP monetization positives while reducing generic K-content, studio, character-IP, and late-reignition false positives where windowing, recoupment, licensing, merchandising, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":97,"canonical_archetype_id":"C27_CONTENT_IP_GLOBAL_MONETIZATION","residual_type":"content_ip_windowing_recoupment_margin_guard","contribution":"Adds one media/studio local positive, one studio/content local 4B failure, and one kids-animation character-IP hard-4C candidate to calibrate C27 title/windowing, distribution, contract economics, cost recoupment, licensing/merchandising, event-window separation, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C27_CONTENT_IP_WINDOWING_RECOUPMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C27_CONTENT_IP_GLOBAL_MONETIZATION:

  Do not open Stage3-Green from:
    - K-content / drama / movie / animation label alone
    - game IP / character IP label alone
    - global OTT distribution headline alone
    - studio production slate alone
    - box-office / theatrical release buzz alone
    - merchandising or licensing rumor alone
    - one-week content-stock volume spike alone
    - late chase after a content/IP rerating alone

  Require at least two of:
    - named title / franchise / platform / geography / channel
    - distribution window and release schedule
    - contract structure and revenue recognition
    - advertising / subscription / box office / licensing / merchandising conversion
    - production / participation / marketing cost recoupment
    - hit-rate / slate concentration risk check
    - cash collection and margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the content/IP headline

  If MFE < 10% and MAE < -30%:
    route to C27 hard-4C candidate.

  If MFE > 15% but later MAE is high:
    preserve as local 4B / event burst, not Green, unless current monetization and margin evidence appears.

  If a later renewed IP event appears:
    create a new event window; do not retroactively validate a failed earlier trigger.

  Distinguish:
    - companies where titles become paying windows, licensing, merchandising, cash collection, and OP
    - from content labels where production cost, weak windowing, or slate concentration breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_97_L8_PLATFORM_CONTENT_SW_SECURITY_C27_CONTENT_IP_GLOBAL_MONETIZATION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C27 content/IP global monetization cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C27_CONTENT_IP_WINDOWING_RECOUPMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C27 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C27 cases agree, consider implementing a canonical guard that:
   - blocks content/IP Green without title/franchise/platform/windowing/revenue-recognition/recoupment/margin bridge,
   - preserves media/studio positives only with price survival and fresh monetization evidence,
   - treats meaningful-MFE/high-MAE studio/content labels as local 4B,
   - routes first-phase kids animation/character-IP failures to hard-4C when merchandising/licensing evidence is missing,
   - separates later renewed event windows from earlier failed IP triggers,
   - applies market segment, name-history, old corporate-action, and short-listing caveats.

Expected next schedule:
completed_round = R8
completed_loop = 97
next_round = R9
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 97
next_round = R9
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
