# E2R Stock-Web v12 Residual Research — R8 / Loop 95

```yaml
scheduled_round: R8
scheduled_loop: 95
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE

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
payment_platform_case_count: 2
adtech_platform_case_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 95
next_round: R9
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_95_L7_BIO_HEALTHCARE_MEDICAL_C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 95
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires platform / content / software / security:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage:

```text
loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop92: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop93: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop94: C27_CONTENT_IP_GLOBAL_MONETIZATION
```

This run returns to C26 but avoids the prior C26 top-covered symbols and recent R8 names. The selected fine branch is:

```text
payment / adtech / commerce platform traffic
take-rate, transaction volume, ad-demand, and margin bridge
vs generic platform-label spike
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
060250 NHN KCP
064260 다날
216050 인크로스
```

They avoid the C26 top-covered list and avoid recent R8 loop91~94 names:

```text
loop91 avoid: 067160, 273060, 236810
loop92 avoid: C28 software/security names
loop93 avoid: 230360, 214320, 089600
loop94 avoid: 251270, 035900, 253450
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
060250: same archetype, new symbol, payment-commerce platform transaction-volume local positive with 4B after later high MAE
064260: same archetype, new symbol, mobile-payment/content-platform local burst and near-hard 4B cap
216050: same archetype, new symbol, adtech/media-rep label hard-4C without ad-demand or margin survival
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
060250 NHN KCP
  profile: atlas/symbol_profiles/060/060250.json
  name history:
    시스네트 -> 한국사이버결제 -> NHN한국사이버결제 -> NHN KCP
  selected 2024 name:
    NHN KCP
  first_date: 2002-01-08
  last_date: 2026-02-20
  market:
    KOSDAQ, with KOSDAQ GLOBAL segment from 2022-11-21 to 2025-06-12
  tradable_ohlcv rows: 5,930
  non_tradable_zero_volume rows: 21
  corporate_action_candidate_dates:
    2005-11-18, 2005-11-29, 2006-02-10, 2007-04-03, 2014-12-16, 2021-12-20
  2024 entry~D+180 contamination: none

064260 다날
  profile: atlas/symbol_profiles/064/064260.json
  first_date: 2004-07-23
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 5,327
  corporate_action_candidate_dates:
    2004-12-29, 2005-01-28, 2016-06-28, 2016-07-06
  2024 entry~D+180 contamination: none

216050 인크로스
  profile: atlas/symbol_profiles/216/216050.json
  first_date: 2016-10-31
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 2,283
  corporate_action_candidate_dates:
    2017-11-14, 2017-12-04, 2022-07-11
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C26 is about platform ad revenue, transaction traffic, take-rate, and operating leverage. It is not a generic "platform stock" or "digital economy label" archetype.

The model can over-score:

```text
platform / adtech / payment label
commerce traffic recovery
digital advertising recovery
payment transaction volume
AI / data / targeting readthrough
one-week platform-stock volume spike
low-price digital-platform sympathy
```

The C26 bridge must be stricter:

```text
platform traffic or ad-demand event
  -> active user / merchant / advertiser / transaction volume
  -> take-rate or commission economics
  -> ad fill-rate / CPC / CPM / ROAS where relevant
  -> payment volume / TPV and fee mix where relevant
  -> operating cost and sales/marketing leverage
  -> margin / OP conversion
  -> price survival after the first platform-label spike
```

A platform thesis is like a toll road. Traffic matters, but C26 asks whether cars pass through the company gate, whether the toll rate holds, whether maintenance and marketing cost stay contained, and whether the traffic becomes operating profit.

---

## 5. Case 1 — 060250 NHN KCP

```yaml
case_id: C26_R8L95_060250_2024_02_01
symbol: "060250"
name: "NHN KCP"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 11290
classification: local_positive_payment_commerce_platform_volume_take_rate_with_4b_after_high_mae
calibration_usable: true
```

### Evidence interpretation

NHN KCP is the constructive local-positive control, but not an unrestricted Green.

The useful C26 read is not simply:

```text
결제 플랫폼 / 커머스 플랫폼이 움직였다
```

It is:

```text
online payment gateway and commerce transaction relevance
  -> transaction volume and take-rate optionality
  -> payment fee mix and operating leverage
  -> strong local price confirmation
```

The early forward path delivered a strong MFE into February. But the later path failed price survival and crossed a high-MAE zone. This makes the original trigger a local positive, while requiring 4B unless fresh TPV, take-rate, and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,200 / close 11,290
2024-02-15: high 13,720 / close 13,040
2024-02-19: high 14,500 / close 13,730
2024-02-20: high 15,600 / close 13,800
2024-03-07: low 12,370 / close 12,580
2024-08-05: low 7,100 / close 7,220
2024-10-25: low 7,020 / close 7,030
```

Approximate path from entry close:

```text
entry_close: 11,290
peak_high: 15,600
MFE: +38.2%
worst_low_after_entry: 7,020
MAE: -37.8%
```

### Interpretation

This is a C26 local positive with 4B:

```text
Stage2-Actionable: possible if TPV, merchant growth, take-rate, and fee/margin bridge are explicit.
Stage3-Green: blocked after high-MAE reversal unless fresh transaction and margin evidence appears.
Local 4B: required because +38% MFE later became -37% MAE.
Hard 4C: not primary for original entry because meaningful MFE came first.
```

### Stress-test components

```text
raw_component_score_proxy:
  payment_platform_relevance: high
  transaction_volume_bridge: medium_high
  take_rate_fee_mix_bridge: medium
  margin_op_bridge: weak_to_medium
  price_confirmation: high_initial
  post_rally_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 064260 다날

```yaml
case_id: C26_R8L95_064260_2024_02_01
symbol: "064260"
name: "다날"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 3945
classification: local_burst_mobile_payment_content_platform_near_hard_4b_cap_without_margin_survival
calibration_usable: true
```

### Evidence interpretation

다날 is the mobile-payment / content-platform local-burst case.

The setup had plausible C26 relevance:

```text
mobile payment and digital content platform
  -> transaction traffic / payment fee optionality
  -> consumer digital-platform sentiment
  -> early February local burst
```

But the bridge did not survive. MFE was meaningful, yet the later drawdown approached the hard-failure zone. This should be handled as a 4B cap or event burst, not a Green.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 4,040 / close 3,945
2024-02-13: high 4,695 / close 4,260
2024-02-15: high 4,600 / close 4,440
2024-02-20: high 4,540 / close 4,520
2024-03-05: high 4,650 / close 4,445
2024-08-05: low 2,770 / close 3,000
2024-09-03: high 3,680 / close 3,490
2024-10-25: low 3,030 / close 3,035
```

Approximate path from entry close:

```text
entry_close: 3,945
peak_high: 4,695
MFE: +19.0%
worst_low_after_entry: 2,770
MAE: -29.8%
```

### Interpretation

This is a local burst / near-hard 4B cap:

```text
Stage2-Watch: valid from mobile payment and platform relevance.
Stage2-Actionable: possible only if transaction volume, take-rate, fee mix, and margin bridge are explicit.
Stage3-Green: blocked after near -30% MAE.
Local 4B: required.
Hard 4C: borderline but not primary because MFE came first and MAE stayed just above the hard threshold.
```

### Stress-test components

```text
raw_component_score_proxy:
  mobile_payment_relevance: medium_high
  digital_content_platform_label: medium
  transaction_fee_bridge: weak_to_medium
  take_rate_margin_bridge: weak
  price_confirmation: medium_initial
  post_burst_survival: weak
  local_4b_overlay: required
```

---

## 7. Case 3 — 216050 인크로스

```yaml
case_id: C26_R8L95_216050_2024_02_01
symbol: "216050"
name: "인크로스"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 10990
classification: hard_4c_candidate_adtech_media_rep_label_without_ad_demand_margin_survival
calibration_usable: true
```

### Evidence interpretation

인크로스 is the hard C26 guardrail.

The setup can fool a platform model:

```text
digital ad / media rep label
  -> ad-market recovery hope
  -> platform data or targeting readthrough
  -> low-volume platform-label rebound
```

But the forward price path did not validate ad-demand, fill-rate, CPC/CPM, advertiser budget, or margin conversion. The MFE after entry was shallow, while the later drawdown crossed the hard-4C zone.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 11,050 / close 10,990
2024-02-19: high 11,380 / close 11,240
2024-02-20: high 11,400 / close 11,240
2024-04-17: low 9,130 / close 9,170
2024-08-05: low 6,120 / close 6,320
2024-09-09: low 6,170 / close 6,370
2024-10-23: high 7,440 / close 7,320
```

Approximate path from entry close:

```text
entry_close: 10,990
peak_high: 11,400
MFE: +3.7%
worst_low_after_entry: 6,120
MAE: -44.3%
```

### Interpretation

This is a hard C26 false-positive:

```text
Stage2-Watch: possible from adtech / media-rep platform relevance.
Stage2-Actionable: blocked unless advertiser demand, ad pricing, fill-rate, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that adtech label is not ad-demand operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  adtech_media_rep_label: high
  ad_market_recovery_readthrough: medium
  advertiser_budget_bridge: weak
  pricing_fillrate_bridge: weak
  margin_op_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
payment_platform_case_count: 2
adtech_platform_case_count: 1
calibration_usable_trigger_count: 3
```

The three-case C26 platform grid:

```text
060250 NHN KCP:
  payment-commerce transaction platform local positive;
  strong MFE came first, but later high MAE requires 4B.

064260 다날:
  mobile-payment/content-platform local burst;
  meaningful MFE, near-hard MAE, 4B cap.

216050 인크로스:
  adtech/media-rep platform label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C26 is not "platform label is hot."
C26 is "traffic becomes transaction volume, ad demand, take-rate, pricing, fee mix, operating leverage, and margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C26_R8L95_060250_2024_02_01","scheduled_round":"R8","scheduled_loop":95,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE","symbol":"060250","name":"NHN KCP","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":11290,"peak_high":15600,"peak_date":"2024-02-20","worst_low_after_entry":7020,"worst_low_after_entry_date":"2024-10-25","mfe_pct":38.2,"mae_pct":-37.8,"classification":"local_positive_payment_commerce_platform_volume_take_rate_with_4b_after_high_mae","calibration_usable":true,"evidence_family":"payment_commerce_platform_transaction_volume_take_rate_fee_mix_margin_bridge","residual_error":"payment_platform_local_positive_requires_4b_after_later_high_mae_without_fresh_tpv_margin_evidence","shadow_rule_candidate":"preserve_local_positive_but_attach_4b_after_large_mfe_followed_by_high_mae"}
{"row_type":"case","case_id":"C26_R8L95_064260_2024_02_01","scheduled_round":"R8","scheduled_loop":95,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE","symbol":"064260","name":"다날","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":3945,"peak_high":4695,"peak_date":"2024-02-13","worst_low_after_entry":2770,"worst_low_after_entry_date":"2024-08-05","mfe_pct":19.0,"mae_pct":-29.8,"classification":"local_burst_mobile_payment_content_platform_near_hard_4b_cap_without_margin_survival","calibration_usable":true,"evidence_family":"mobile_payment_content_platform_transaction_fee_label_without_take_rate_margin_survival","residual_error":"mobile_payment_platform_label_can_create_local_mfe_but_fail_green_without_fee_mix_and_margin_survival","shadow_rule_candidate":"classify_meaningful_mfe_then_near_hard_mae_payment_platform_cases_as_local_4b_not_green"}
{"row_type":"case","case_id":"C26_R8L95_216050_2024_02_01","scheduled_round":"R8","scheduled_loop":95,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE","symbol":"216050","name":"인크로스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":10990,"peak_high":11400,"peak_date":"2024-02-20","worst_low_after_entry":6120,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.7,"mae_pct":-44.3,"classification":"hard_4c_candidate_adtech_media_rep_label_without_ad_demand_margin_survival","calibration_usable":true,"evidence_family":"adtech_media_rep_label_without_advertiser_demand_pricing_fillrate_margin_bridge","residual_error":"adtech_label_can_overpromote_without_ad_demand_and_operating_leverage","shadow_rule_candidate":"route_adtech_media_rep_label_to_hard_4c_if_mfe_shallow_mae_large_and_ad_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":95,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"PAYMENT_ADTECH_COMMERCE_PLATFORM_TRAFFIC_TAKE_RATE_MARGIN_BRIDGE_VS_PLATFORM_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"payment_platform_case_count":2,"adtech_platform_case_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":95,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","rule_id":"C26_TRAFFIC_TAKE_RATE_AD_DEMAND_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C26, do not open Stage2-Actionable or Stage3-Green from platform, adtech, payment, commerce traffic, digital advertising recovery, payment transaction volume, AI/data/targeting readthrough, or one-week platform-stock volume spike labels alone. Require active user/merchant/advertiser/transaction volume, take-rate or commission economics, ad fill-rate/CPC/CPM/ROAS where relevant, payment TPV and fee mix where relevant, operating cost and sales/marketing leverage, margin/OP conversion, and post-trigger price survival. Payment-platform positives with large MFE followed by high MAE should remain local 4B unless fresh TPV/take-rate/margin evidence appears. Mobile-payment/content-platform local bursts with near-hard MAE should not remain Green. Adtech/media-rep labels with shallow MFE and high MAE should route to hard-4C when advertiser demand and margin bridge are missing.","expected_effect":"Reduce generic platform, adtech, and payment-label false positives while preserving true traffic-to-margin operating leverage positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":95,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"platform_traffic_take_rate_ad_margin_guard","contribution":"Adds one payment-platform local positive with 4B after high MAE, one mobile-payment local 4B cap, and one adtech hard-4C counterexample to calibrate C26 traffic, take-rate, advertiser demand, fee mix, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C26_TRAFFIC_TAKE_RATE_AD_DEMAND_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:

  Do not open Stage3-Green from:
    - platform label alone
    - adtech / media-rep label alone
    - payment / commerce platform label alone
    - digital advertising recovery label alone
    - transaction-volume label alone
    - AI / data / targeting readthrough alone
    - one-week platform-stock volume spike alone

  Require at least two of:
    - active user / merchant / advertiser / transaction-volume growth
    - take-rate or commission economics
    - ad fill-rate / CPC / CPM / ROAS improvement
    - payment TPV and fee-mix improvement
    - operating cost and sales/marketing leverage
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the platform-traffic headline

  If MFE < 8% and MAE < -35%:
    route to C26 hard-4C candidate.

  If MFE > 15% but later MAE is material:
    preserve as local 4B / event burst, not Green, unless current traffic/take-rate/margin evidence appears.

  If MFE is meaningful but bridge is stale:
    attach 4B until transaction or ad-demand execution refreshes.

  Distinguish:
    - payment or ad platforms where traffic becomes take-rate and OP
    - from platform labels where traffic does not survive pricing, marketing cost, or advertiser-budget pressure.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_95_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C26 platform/ad/payment operating leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C26_TRAFFIC_TAKE_RATE_AD_DEMAND_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C26 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C26 cases agree, consider implementing a canonical guard that:
   - blocks platform-label Green without traffic/take-rate/ad-demand/payment-fee/margin bridge,
   - preserves payment-platform positives only with price survival and current TPV/take-rate evidence,
   - attaches local 4B after large MFE followed by high MAE,
   - caps mobile-payment local bursts at Watch/4B when bridge is stale,
   - routes shallow-MFE/high-MAE adtech/media-rep labels to hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 95
next_round = R9
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 95
next_round = R9
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
