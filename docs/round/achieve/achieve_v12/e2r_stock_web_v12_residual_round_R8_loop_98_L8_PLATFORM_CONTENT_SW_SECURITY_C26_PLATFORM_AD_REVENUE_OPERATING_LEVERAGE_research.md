# E2R Stock-Web v12 Residual Research — R8 / Loop 98

```yaml
scheduled_round: R8
scheduled_loop: 98
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
digital_ad_media_rep_case_count: 1
performance_marketing_case_count: 1
small_ad_agency_event_spike_case_count: 1
ad_revenue_take_rate_bridge_missing_count: 2
client_budget_operating_leverage_bridge_missing_count: 2
platform_algorithm_or_channel_mix_caveat_count: 2
market_segment_or_name_change_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 98
next_round: R9
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_98_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 98
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
loop97: C27_CONTENT_IP_GLOBAL_MONETIZATION
```

This run returns to C26 after the R8 branch cycle.

Selected fine branch:

```text
digital ad media rep / performance marketing / small ad agency
advertiser budget, take-rate, client retention, channel mix, platform algorithm risk,
gross-profit leverage, labor and traffic-acquisition cost, and OP bridge
vs generic platform/ad-revenue label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
rows: 13
symbols: 10
date_range: 2023-12-06~2024-07-23
good/bad S2: 2/6
4B/4C: 0/1
URL pending/proxy: 0/0
top covered symbols:
  042000(2), 214270(2), 237820(2), 030000(1), 035420(1), 035720(1)
```

Selected symbols:

```text
230360 에코마케팅
123570 이엠넷
089600 나스미디어 / KT나스미디어
```

They avoid the C26 top-covered names and recent R8 branch names:

```text
loop97 C27 avoid:
  035760, 036420, 419530

loop96 C28 avoid:
  136540, 060850, 053800

loop95 C26 avoid:
  060250, 064260, 216050

loop94 C27 avoid:
  251270, 035900, 253450

C26 top-covered avoid:
  042000, 214270, 237820, 030000, 035420, 035720
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
230360: same archetype, new symbol, performance marketing / commerce-linked ad operating leverage positive with Green cap
123570: same archetype, new symbol, small digital ad agency event burst followed by high-MAE 4B failure
089600: same archetype, new symbol, media-rep / ad-revenue label hard-4C after shallow MFE and high MAE
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
230360 에코마케팅
  profile: atlas/symbol_profiles/230/230360.json
  first_date: 2016-08-08
  last_date: 2026-02-20
  market history:
    KOSDAQ from 2016-08-08 to 2026-02-20
    KOSDAQ GLOBAL from 2022-11-21 to 2024-06-13
  tradable_ohlcv rows: 2,338
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2018-02-23, 2018-03-16, 2020-08-20, 2020-09-10
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.
    KOSDAQ GLOBAL segment ended in 2024, but no raw-price discontinuity candidate inside the selected validation window.

123570 이엠넷
  profile: atlas/symbol_profiles/123/123570.json
  first_date: 2011-11-25
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,497
  non_tradable_zero_volume rows: 1
  corporate_action_candidate_dates:
    2016-08-11, 2016-09-06, 2018-06-14, 2018-07-10
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action / raw-discontinuity candidates are outside selected 2024 validation window.

089600 나스미디어 / KT나스미디어
  profile: atlas/symbol_profiles/089/089600.json
  selected 2024 trigger name:
    나스미디어
  later name:
    KT나스미디어 from 2025-04-25
  first_date: 2013-07-17
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,090
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
  caveat:
    2025 name-change is outside the selected 2024 validation window.
```

---

## 4. Archetype residual problem

C26 is about platform / ad revenue / operating leverage. It is not a generic "platform stock" or "digital advertising is recovering" archetype.

The model can over-score:

```text
digital advertising label
media rep / ad agency / performance marketing label
platform traffic recovery headline
online commerce / D2C marketing readthrough
advertiser budget recovery hope
AI / targeting / ad-tech label
one-week platform/ad stock volume spike
late chase after an ad-revenue rerating
```

The C26 bridge must be stricter:

```text
platform / ad revenue / operating leverage event
  -> named advertiser vertical, platform, channel, or client group
  -> ad-budget recovery and campaign volume
  -> take-rate / gross profit per campaign
  -> client retention and concentration
  -> traffic acquisition cost and media-buying cost
  -> platform algorithm or policy risk
  -> labor / salesforce / outsourcing cost discipline
  -> revenue recognition and working-capital timing
  -> operating leverage and OP conversion
  -> price survival after the first ad-label spike
```

A C26 ad-platform thesis is like an ad campaign running through an auction. The impression volume may rise, but equity value appears only when client budgets convert into campaigns, the platform keeps take-rate, media-buying cost does not leak the spread, and fixed operating cost lets gross profit drop to OP.

---

## 5. Case 1 — 230360 에코마케팅

```yaml
case_id: C26_R8L98_230360_2024_02_01
symbol: "230360"
name: "에코마케팅"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 9640
classification: positive_performance_marketing_commerce_ad_revenue_operating_leverage_with_green_cap
calibration_usable: true
```

### Evidence interpretation

에코마케팅 is the constructive C26 positive in this set.

The useful C26 read is not simply:

```text
광고 / 플랫폼주가 강하다
```

It is:

```text
performance marketing and commerce-linked advertising
  -> advertiser budget and campaign conversion
  -> gross-profit / take-rate bridge
  -> fixed-cost operating leverage
  -> strong February-April price confirmation
```

The forward path produced a meaningful MFE and did not cross a hard drawdown zone in the selected validation window. This supports positive classification. However, after the rerating, C26 Green should remain capped unless client budget, retention, take-rate, media-buying cost, and OP conversion evidence are current.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 9,710 / close 9,640
2024-02-29: high 10,640 / close 10,510
2024-03-20: high 13,410 / close 12,950
2024-04-12: high 14,630 / close 14,570
2024-04-18: high 14,920 / close 14,840
2024-08-05: low 9,520 / close 9,720
2024-09-06: high 11,500 / close 11,130
2024-10-25: high 10,700 / close 10,620
```

Approximate path from entry close:

```text
entry_close: 9,640
peak_high: 14,990
MFE: +55.5%
worst_low_after_entry: 9,520
MAE: -1.2%
```

### Interpretation

This is a C26 positive with Green cap:

```text
Stage2-Actionable: possible if advertiser budget, client cohort, take-rate, media cost, and OP bridge are explicit.
Stage3-Green: blocked after +50% MFE unless fresh client-budget / margin evidence appears.
Local 4B: monitor if ad-label rerating outruns operating evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  performance_marketing_relevance: high
  advertiser_budget_bridge: medium_high
  take_rate_gross_profit_bridge: medium_high
  media_buying_cost_bridge: medium
  op_leverage_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 123570 이엠넷

```yaml
case_id: C26_R8L98_123570_2024_02_01
symbol: "123570"
name: "이엠넷"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3200
classification: local_burst_small_digital_ad_agency_event_spike_high_mae_4b_failure
calibration_usable: true
```

### Evidence interpretation

이엠넷 is the small ad-agency / event-burst 4B failure.

The setup had real C26 relevance:

```text
digital advertising agency
  -> advertiser budget and online marketing recovery readthrough
  -> platform / ad-tech event beta
  -> strong February-March local MFE
```

The initial price response was strong, so this is not a zero-response hard failure. But the later path failed price survival and entered a high-MAE zone. This should be local 4B, not Green, unless advertiser budget, client retention, take-rate, media-buying cost, and OP conversion evidence refresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 3,225 / close 3,200
2024-02-02: high 3,980 / close 3,655
2024-02-26: high 4,285 / close 3,650
2024-03-05: high 4,615 / close 4,615
2024-03-06: high 5,230 / close 4,800
2024-04-17: low 3,580 / close 3,590
2024-08-05: low 2,300 / close 2,425
2024-10-08: high 2,825 / close 2,660
```

Approximate path from entry close:

```text
entry_close: 3,200
peak_high: 5,230
MFE: +63.4%
worst_low_after_entry: 2,300
MAE: -28.1%
```

### Interpretation

This is a C26 local burst / 4B failure:

```text
Stage2-Watch: valid from digital ad-agency relevance.
Stage2-Actionable: possible only if client budget, campaign volume, take-rate, retention, and OP bridge are explicit.
Stage3-Green: blocked after high-MAE reversal.
Local 4B: required.
Hard 4C: not primary because meaningful MFE came first and MAE did not cross the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  small_digital_ad_agency_relevance: high
  advertiser_budget_recovery_signal: medium_high
  client_retention_bridge: weak_to_medium
  take_rate_margin_bridge: weak_to_medium
  op_leverage_bridge: weak
  price_confirmation: very_high_initial
  later_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 7. Case 3 — 089600 나스미디어 / KT나스미디어

```yaml
case_id: C26_R8L98_089600_2024_02_01
symbol: "089600"
name_at_trigger: "나스미디어"
later_name: "KT나스미디어"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 23650
classification: hard_4c_candidate_media_rep_ad_revenue_label_without_budget_take_rate_op_leverage_survival
calibration_usable: true
```

### Evidence interpretation

나스미디어 is the media-rep / digital ad-revenue hard guardrail.

The label can fool the model:

```text
digital advertising / media rep
  -> platform traffic and ad-budget recovery
  -> connected-TV / mobile / display ad readthrough
  -> low-PBR or ad-cycle recovery label
```

But from the selected February entry, the path produced only shallow MFE and then crossed a high-MAE zone. The bridge from ad-revenue label to client budget recovery, take-rate, media-buying cost control, client retention, and OP leverage was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 24,350 / close 23,650
2024-02-02: high 25,650 / close 25,500
2024-03-08: low 21,300 / close 21,450
2024-04-11: high 23,900 / close 23,700
2024-08-05: low 15,410 / close 15,730
2024-09-19: high 17,870 / close 15,390
2024-11-13: low 13,790 / close 13,880
2024-12-09: low 13,750 / close 13,750
```

Approximate path from entry close:

```text
entry_close: 23,650
peak_high_after_entry: 25,650
MFE: +8.5%
worst_low_after_entry: 13,720
MAE: -42.0%
```

### Interpretation

This is a hard C26 false-positive candidate:

```text
Stage2-Watch: possible from digital-ad / media-rep relevance.
Stage2-Actionable: blocked unless advertiser budget, channel mix, take-rate, client retention, cost, and OP bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
Name-change caveat: later 2025 KT나스미디어 name is outside 2024 window.
```

The lesson is that ad-cycle recovery salience is not operating leverage survival.

### Stress-test components

```text
raw_component_score_proxy:
  media_rep_ad_revenue_label: high
  ad_budget_recovery_signal: medium_high
  platform_traffic_bridge: weak_to_medium
  take_rate_bridge: weak
  media_buying_cost_bridge: weak
  op_leverage_bridge: weak
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
digital_ad_media_rep_case_count: 1
performance_marketing_case_count: 1
small_ad_agency_event_spike_case_count: 1
ad_revenue_take_rate_bridge_missing_count: 2
client_budget_operating_leverage_bridge_missing_count: 2
platform_algorithm_or_channel_mix_caveat_count: 2
market_segment_or_name_change_caveat_count: 2
row_presence_or_old_corporate_action_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C26 ad-revenue grid:

```text
230360 에코마케팅:
  performance marketing / commerce-linked ad operating leverage positive;
  large MFE and low MAE, but Green requires fresh client-budget / take-rate / OP evidence.

123570 이엠넷:
  small digital ad agency event burst;
  large MFE first, then high MAE, local 4B failure.

089600 나스미디어:
  media-rep / ad-revenue label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C26 is not "ad or platform label is recovering."
C26 is "advertiser budgets become campaigns, campaigns keep take-rate, media-buying cost is controlled, clients persist, and gross profit drops to OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C26_R8L98_230360_2024_02_01","scheduled_round":"R8","scheduled_loop":98,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE","symbol":"230360","name":"에코마케팅","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":9640,"peak_high":14990,"peak_date":"2024-04-17","worst_low_after_entry":9520,"worst_low_after_entry_date":"2024-08-05","mfe_pct":55.5,"mae_pct":-1.2,"classification":"positive_performance_marketing_commerce_ad_revenue_operating_leverage_with_green_cap","calibration_usable":true,"market_segment_or_old_corporate_action_caveat":true,"evidence_family":"performance_marketing_ad_budget_take_rate_media_cost_client_retention_op_leverage_bridge","residual_error":"positive_performance_marketing_path_requires_green_cap_after_large_mfe_without_refreshed_client_budget_take_rate_op_evidence","shadow_rule_candidate":"allow_capped_actionable_when_client_budget_take_rate_and_op_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C26_R8L98_123570_2024_02_01","scheduled_round":"R8","scheduled_loop":98,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE","symbol":"123570","name":"이엠넷","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3200,"peak_high":5230,"peak_date":"2024-03-06","worst_low_after_entry":2300,"worst_low_after_entry_date":"2024-08-05","mfe_pct":63.4,"mae_pct":-28.1,"classification":"local_burst_small_digital_ad_agency_event_spike_high_mae_4b_failure","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"small_digital_ad_agency_platform_event_budget_recovery_without_sustained_client_retention_take_rate_op_leverage","residual_error":"small_ad_agency_event_spike_can_create_mfe_but_fail_green_without_budget_retention_take_rate_and_op_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_high_mae_small_ad_agency_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C26_R8L98_089600_2024_02_01","scheduled_round":"R8","scheduled_loop":98,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE","symbol":"089600","name_at_trigger":"나스미디어","later_name":"KT나스미디어","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":23650,"peak_high":25650,"peak_date":"2024-02-02","worst_low_after_entry":13720,"worst_low_after_entry_date":"2024-11-15","mfe_pct":8.5,"mae_pct":-42.0,"classification":"hard_4c_candidate_media_rep_ad_revenue_label_without_budget_take_rate_op_leverage_survival","calibration_usable":true,"name_change_caveat_outside_window":true,"evidence_family":"media_rep_digital_ad_revenue_label_without_client_budget_take_rate_media_cost_retention_op_leverage_bridge","residual_error":"media_rep_ad_revenue_label_can_fail_when_ad_budget_take_rate_and_operating_leverage_bridge_missing","shadow_rule_candidate":"route_media_rep_ad_revenue_label_to_hard_4c_if_mfe_shallow_mae_high_and_op_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":98,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_MEDIA_REP_PERFORMANCE_MARKETING_PLATFORM_REVENUE_TAKE_RATE_OPERATING_LEVERAGE_BRIDGE_VS_AD_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"digital_ad_media_rep_case_count":1,"performance_marketing_case_count":1,"small_ad_agency_event_spike_case_count":1,"ad_revenue_take_rate_bridge_missing_count":2,"client_budget_operating_leverage_bridge_missing_count":2,"platform_algorithm_or_channel_mix_caveat_count":2,"market_segment_or_name_change_caveat_count":2,"row_presence_or_old_corporate_action_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":98,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","rule_id":"C26_AD_REVENUE_TAKE_RATE_CLIENT_BUDGET_OP_LEVERAGE_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C26 platform/ad-revenue/operating-leverage cases, do not open Stage2-Actionable or Stage3-Green from digital advertising, media rep, ad agency, performance marketing, platform traffic recovery, online commerce/D2C marketing readthrough, advertiser budget recovery, AI/targeting/ad-tech label, one-week platform/ad stock volume spike, or late chase after an ad-revenue rerating labels alone. Require named advertiser vertical/platform/channel/client group, ad-budget recovery and campaign volume, take-rate/gross profit per campaign, client retention and concentration, traffic acquisition cost and media-buying cost control, platform algorithm or policy risk check, labor/salesforce/outsourcing cost discipline, revenue recognition and working-capital timing, operating leverage and OP conversion, and post-trigger price survival. Performance-marketing positives with large MFE may be capped Actionable when client-budget/take-rate/OP bridge is explicit, but Green requires fresh evidence. Small ad-agency event spikes with meaningful MFE followed by high MAE should remain local 4B, not Green. Media-rep ad-revenue labels with shallow MFE and high MAE should route to hard-4C when budget, take-rate, cost, retention, and OP bridge are missing.","expected_effect":"Preserve true platform/ad-revenue operating-leverage positives while reducing generic ad-cycle, media-rep, ad-agency, and small-cap ad-tech label false positives where client budgets, take-rate, media-buying cost, retention, and OP evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":98,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"ad_revenue_take_rate_client_budget_op_leverage_guard","contribution":"Adds one performance-marketing positive, one small-ad-agency local 4B failure, and one media-rep hard-4C counterexample to calibrate C26 advertiser budget, campaign volume, take-rate, client retention, media-buying cost, and operating-leverage requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C26_AD_REVENUE_TAKE_RATE_CLIENT_BUDGET_OP_LEVERAGE_BRIDGE_REQUIRED

IF canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:

  Do not open Stage3-Green from:
    - digital advertising label alone
    - media rep / ad agency / performance marketing label alone
    - platform traffic recovery headline alone
    - online commerce / D2C marketing readthrough alone
    - advertiser budget recovery headline alone
    - AI / targeting / ad-tech label alone
    - one-week platform/ad stock volume spike alone
    - late chase after ad-revenue rerating alone

  Require at least two of:
    - named advertiser vertical / platform / channel / client group
    - ad-budget recovery and campaign volume
    - take-rate / gross profit per campaign
    - client retention and concentration
    - traffic acquisition cost / media-buying cost control
    - platform algorithm or policy risk check
    - labor / salesforce / outsourcing cost discipline
    - revenue recognition and working-capital timing
    - operating leverage and OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the ad-revenue headline

  If MFE < 10% and MAE <= -35%:
    route to C26 hard-4C candidate.

  If MFE > 20% but client-budget / take-rate evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is meaningful but later MAE is high:
    attach 4B until retention and OP evidence refreshes.

  Distinguish:
    - companies where ad budgets become campaigns, campaigns preserve take-rate, and gross profit drops to OP
    - from ad labels where media-buying cost, weak client retention, or platform algorithm changes break the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_98_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C26 platform/ad-revenue/operating-leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C26_AD_REVENUE_TAKE_RATE_CLIENT_BUDGET_OP_LEVERAGE_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C26 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C26 cases agree, consider implementing a canonical guard that:
   - blocks platform/ad-revenue Green without advertiser/client, campaign volume, take-rate, media-buying cost, retention, and OP bridge,
   - preserves performance-marketing positives only with price survival and fresh budget/take-rate evidence,
   - treats meaningful-MFE/high-MAE small ad-agency spikes as local 4B,
   - routes shallow-MFE/high-MAE media-rep ad labels to hard-4C,
   - applies market-segment, name-change, row-presence, and old corporate-action caveats.

Expected next schedule:
completed_round = R8
completed_loop = 98
next_round = R9
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 98
next_round = R9
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
