# E2R Stock-Web v12 Residual Research — R8 / Loop 93

```yaml
scheduled_round: R8
scheduled_loop: 93
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL

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
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 93
next_round: R9
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_93_L7_BIO_HEALTHCARE_MEDICAL_C24_BIO_TRIAL_DATA_EVENT_RISK_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 93
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

R8 hard gate requires:

```text
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
```

Recent R8 branch usage already covered:

```text
loop88: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop89: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
loop90: C27_CONTENT_IP_GLOBAL_MONETIZATION
loop91: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
loop92: C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
```

This run returns to the under-covered C26 branch, but avoids the top-covered platform / ad names and uses a different fine branch:

```text
digital ad agency / media-rep / commerce-marketing operating leverage
vs generic ad-recovery label
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
214320 이노션
089600 KT나스미디어 / 나스미디어
```

They avoid the C26 top-covered names and avoid recent R8 loop91~92 names:

```text
loop91 avoid: 067160, 273060, 236810
loop92 avoid: 136540, 053800, 356680
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
230360: same archetype, new symbol, performance-marketing / commerce operating leverage positive with 4B watch
214320: same archetype, new symbol, large ad-agency stable label / weak operating-leverage cap case
089600: same archetype, new symbol, media-rep ad-recovery label without durable revenue-margin bridge
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
universe_path: atlas/all_symbols.csv or atlas/universe/all_symbols.csv
```

Profile checks:

```text
230360 에코마케팅
  profile: atlas/symbol_profiles/230/230360.json
  first_date: 2016-08-08
  last_date: 2026-02-20
  market:
    KOSDAQ active across full profile
    KOSDAQ GLOBAL segment 2022-11-21~2024-06-13
  tradable_ohlcv rows: 2,338
  corporate_action_candidate_dates:
    2018-02-23, 2018-03-16, 2020-08-20, 2020-09-10
  2024 entry~D+180 contamination: none

214320 이노션
  profile: atlas/symbol_profiles/214/214320.json
  first_date: 2015-07-17
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,599
  corporate_action_candidate_dates:
    2023-11-29, 2023-12-21
  selected 2024 entry after candidate windows; entry~D+180 contamination: none

089600 KT나스미디어 / 나스미디어
  profile: atlas/symbol_profiles/089/089600.json
  name history:
    나스미디어 until 2025-04-24
    KT나스미디어 from 2025-04-25
  first_date: 2013-07-17
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 3,090
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C26 is about platform/ad revenue operating leverage, not a generic "advertising recovery" or "platform stock" label.

The model can over-score:

```text
digital ad recovery
media-rep label
platform traffic
commerce-marketing label
brand advertising rebound
AI/adtech sympathy
one-week ad-sector price spike
```

The C26 bridge must be stricter:

```text
traffic / ad demand / campaign budget recovery
  -> platform or agency take-rate
  -> advertiser retention and budget expansion
  -> performance-marketing efficiency
  -> operating leverage after fixed costs
  -> margin / OP conversion
  -> price survival after the first ad-recovery spike
```

Ad revenue is like wind for a sailboat. The headline says the wind is back, but C26 asks whether this company's sail is actually open, whether the boat keeps the wind, and whether the extra speed reaches operating profit.

---

## 5. Case 1 — 230360 에코마케팅

```yaml
case_id: C26_R8L93_230360_2024_02_23
symbol: "230360"
name: "에코마케팅"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL
trigger_date: 2024-02-23
entry_date: 2024-02-23
entry_price_basis: close
entry_price: 10190
classification: positive_performance_marketing_commerce_operating_leverage_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

에코마케팅 is the constructive control in this set.

The useful C26 bridge is:

```text
performance marketing / commerce marketing capability
  -> campaign efficiency
  -> advertiser or brand budget conversion
  -> commerce-linked revenue growth
  -> operating leverage
  -> strong price confirmation
```

The stock produced a clear MFE after the February trigger and retained a meaningful part of the move for several months. However, the August and September drawdowns show that C26 should attach 4B after a large move unless fresh revenue and margin evidence appears.

### Price path

Key Stock-Web rows:

```text
2024-02-23: high 10,290 / close 10,190
2024-02-26: high 10,630 / close 10,390
2024-03-20: high 13,410 / close 12,950
2024-04-12: high 14,630 / close 14,570
2024-04-17: high 14,990 / close 14,600
2024-08-05: low 9,520 / close 9,720
2024-09-06: high 11,500 / close 11,130
2024-11-07: high 10,800 / close 10,700
```

Approximate path from entry close:

```text
entry_close: 10,190
peak_high: 14,990
MFE: +47.1%
worst_low_after_entry: 9,520
MAE: -6.6%
```

### Interpretation

This is a C26 positive with local 4B watch:

```text
Stage2-Actionable: valid if revenue, campaign-efficiency, and operating-leverage bridge are explicit.
Stage3-Green: possible only with margin/OP confirmation and advertiser-budget durability.
Local 4B: required after +40% MFE unless fresh evidence renews the bridge.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  digital_ad_recovery_relevance: high
  performance_marketing_bridge: high
  commerce_revenue_bridge: medium_high
  operating_leverage_visibility: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 214320 이노션

```yaml
case_id: C26_R8L93_214320_2024_04_25
symbol: "214320"
name: "이노션"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL
trigger_date: 2024-04-25
entry_date: 2024-04-25
entry_price_basis: close
entry_price: 22750
classification: watch_cap_large_ad_agency_label_without_strong_operating_leverage_bridge
calibration_usable: true
```

### Evidence interpretation

이노션 is the stable large-agency cap case.

It has real advertising-agency relevance, but C26 should not promote a stable agency label into Green unless the model can see actual:

```text
client budget expansion
take-rate improvement
international or captive-client growth
fixed-cost absorption
margin / OP conversion
```

The forward price path had a small positive window and then a drawdown. It is not a catastrophic failure, but it is not a strong Actionable/Green case.

### Price path

Key Stock-Web rows:

```text
2024-04-25: high 22,850 / close 22,750
2024-04-29: high 23,000 / close 23,000
2024-05-03: high 24,300 / close 23,750
2024-08-05: low 18,200 / close 18,700
2024-10-16: high 20,250 / close 20,250
2024-11-07: high 20,650 / close 20,300
```

Approximate path from entry close:

```text
entry_close: 22,750
peak_high: 24,300
MFE: +6.8%
worst_low_after_entry: 18,200
MAE: -20.0%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from ad-agency relevance.
Stage2-Actionable: blocked unless budget growth and OP leverage bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not extreme, but false-positive guard applies.
```

The key lesson is over-certainty. A real ad agency can still lack the operating leverage needed for C26 Green.

### Stress-test components

```text
raw_component_score_proxy:
  ad_agency_label_quality: high
  client_budget_bridge: weak_to_medium
  operating_leverage_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 089600 KT나스미디어 / 나스미디어

```yaml
case_id: C26_R8L93_089600_2024_04_09
symbol: "089600"
name_at_trigger: "나스미디어"
current_or_latest_name: "KT나스미디어"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 22750
classification: hard_4c_candidate_media_rep_ad_recovery_label_without_durable_revenue_margin_bridge
calibration_usable: true
```

### Evidence interpretation

나스미디어 is the media-rep / ad-recovery false-positive.

The model can be tempted by:

```text
media rep
digital ad inventory
ad-budget recovery
platform ad demand
```

But the forward path says the label did not become durable revenue or operating leverage at the trigger. The move was too shallow and the later MAE was too large.

### Price path

Key Stock-Web rows:

```text
2024-04-09: high 23,150 / close 22,750
2024-04-11: high 23,900 / close 23,700
2024-04-17: low 19,530 / close 19,620
2024-08-05: low 15,410 / close 15,730
2024-09-06: low 15,290 / close 15,350
2024-11-06: low 14,930
```

Approximate path from entry close:

```text
entry_close: 22,750
peak_high: 23,900
MFE: +5.1%
worst_low_after_entry: 14,930
MAE: -34.4%
```

### Interpretation

This is a hard C26 false-positive:

```text
Stage2-Watch: possible from media-rep / digital ad relevance.
Stage2-Actionable: blocked unless advertiser-budget, fill-rate, take-rate, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that ad inventory exposure is not the same as operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  media_rep_label: high
  ad_recovery_label: medium_high
  advertiser_budget_bridge: weak
  take_rate_or_fill_rate_bridge: weak
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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C26 grid:

```text
230360 에코마케팅:
  performance-marketing / commerce operating-leverage positive;
  strong MFE and manageable MAE, but 4B watch after large move.

214320 이노션:
  large agency label only partly worked;
  shallow MFE and medium MAE, Watch/Yellow cap.

089600 KT나스미디어 / 나스미디어:
  media-rep ad-recovery label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C26 is not "ad recovery label."
C26 is "traffic, advertiser budget, take-rate/fill-rate, and margin convert into operating leverage."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C26_R8L93_230360_2024_02_23","scheduled_round":"R8","scheduled_loop":93,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL","symbol":"230360","name":"에코마케팅","trigger_date":"2024-02-23","entry_date":"2024-02-23","entry_price":10190,"peak_high":14990,"peak_date":"2024-04-17","worst_low_after_entry":9520,"worst_low_after_entry_date":"2024-08-05","mfe_pct":47.1,"mae_pct":-6.6,"classification":"positive_performance_marketing_commerce_operating_leverage_with_4b_watch","calibration_usable":true,"evidence_family":"performance_marketing_commerce_revenue_operating_leverage_bridge","residual_error":"positive_ad_operating_leverage_path_requires_4b_after_large_mfe_without_fresh_margin_evidence","shadow_rule_candidate":"allow_actionable_when_campaign_efficiency_revenue_margin_bridge_confirms_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C26_R8L93_214320_2024_04_25","scheduled_round":"R8","scheduled_loop":93,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL","symbol":"214320","name":"이노션","trigger_date":"2024-04-25","entry_date":"2024-04-25","entry_price":22750,"peak_high":24300,"peak_date":"2024-05-03","worst_low_after_entry":18200,"worst_low_after_entry_date":"2024-08-05","mfe_pct":6.8,"mae_pct":-20.0,"classification":"watch_cap_large_ad_agency_label_without_strong_operating_leverage_bridge","calibration_usable":true,"evidence_family":"large_ad_agency_label_without_client_budget_margin_leverage_bridge","residual_error":"stable_ad_agency_label_can_overpromote_without_visible_budget_growth_and_op_leverage","shadow_rule_candidate":"cap_large_agency_ad_recovery_label_at_watch_yellow_if_mfe_shallow_and_operating_leverage_bridge_missing"}
{"row_type":"case","case_id":"C26_R8L93_089600_2024_04_09","scheduled_round":"R8","scheduled_loop":93,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL","symbol":"089600","name_at_trigger":"나스미디어","current_or_latest_name":"KT나스미디어","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":22750,"peak_high":23900,"peak_date":"2024-04-11","worst_low_after_entry":14930,"worst_low_after_entry_date":"2024-11-06","mfe_pct":5.1,"mae_pct":-34.4,"classification":"hard_4c_candidate_media_rep_ad_recovery_label_without_durable_revenue_margin_bridge","calibration_usable":true,"evidence_family":"media_rep_digital_ad_recovery_label_without_take_rate_fill_rate_margin_bridge","residual_error":"media_rep_ad_inventory_exposure_can_fail_without_durable_revenue_margin_conversion","shadow_rule_candidate":"route_media_rep_ad_recovery_label_to_hard_4c_if_mfe_shallow_mae_large_and_take_rate_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":93,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"DIGITAL_AD_AGENCY_MEDIARREP_COMMERCE_MARKETING_OPERATING_LEVERAGE_VS_AD_RECOVERY_LABEL","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":93,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","rule_id":"C26_AD_REVENUE_TAKE_RATE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C26, do not open Stage2-Actionable or Stage3-Green from ad recovery, media-rep label, platform traffic, commerce-marketing label, AI/adtech sympathy, or one-week ad-sector price spike alone. Require advertiser budget expansion, platform traffic quality, take-rate or fill-rate improvement, campaign efficiency, client retention, operating leverage after fixed costs, margin/OP conversion, and post-trigger price survival. Performance-marketing positives may be Actionable when revenue and margin bridge are explicit, but large MFE should attach local 4B unless fresh evidence appears. Large ad-agency labels with shallow MFE should cap at Watch/Yellow without budget and OP leverage evidence. Media-rep ad-recovery labels with shallow MFE and high MAE should route to hard-4C when take-rate/fill-rate/margin bridge is missing.","expected_effect":"Reduce generic ad-recovery false positives while preserving true performance-marketing and ad-operating-leverage positives with price survival and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":93,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"platform_ad_revenue_take_rate_margin_guard","contribution":"Adds one performance-marketing positive with 4B watch, one large-agency Watch cap, and one media-rep hard-4C counterexample to calibrate C26 ad revenue, take-rate/fill-rate, operating leverage, and price-survival requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C26_AD_REVENUE_TAKE_RATE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:

  Do not open Stage3-Green from:
    - ad recovery label alone
    - media-rep / ad-agency label alone
    - platform traffic label alone
    - commerce-marketing label alone
    - AI/adtech sympathy alone
    - one-week ad-sector volume spike alone

  Require at least two of:
    - advertiser budget expansion
    - traffic quality / user inventory improvement
    - take-rate or fill-rate improvement
    - campaign efficiency / ROAS improvement
    - client retention or budget expansion
    - operating leverage after fixed costs
    - margin / OP conversion
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -25%:
    route to C26 hard-4C candidate.

  If MFE > 40% and MAE remains controlled:
    preserve positive classification but attach local 4B unless fresh margin evidence appears.

  If MFE is shallow and operating-leverage bridge is weak:
    cap at Watch/Yellow.

  Distinguish:
    - performance-marketing names where campaign efficiency becomes revenue and margin
    - from media-rep or large-agency labels where ad recovery does not reach take-rate and OP leverage.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_93_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C26 ad-revenue operating-leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C26_AD_REVENUE_TAKE_RATE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C26 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C26 cases agree, consider implementing a canonical guard that:
   - blocks ad-recovery Green without budget/take-rate/fill-rate/margin bridge,
   - preserves performance-marketing positives only with price survival and margin evidence,
   - attaches local 4B after large MFE,
   - caps large ad-agency names at Watch/Yellow without OP leverage bridge,
   - routes shallow-MFE/high-MAE media-rep labels to hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 93
next_round = R9
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 93
next_round = R9
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
