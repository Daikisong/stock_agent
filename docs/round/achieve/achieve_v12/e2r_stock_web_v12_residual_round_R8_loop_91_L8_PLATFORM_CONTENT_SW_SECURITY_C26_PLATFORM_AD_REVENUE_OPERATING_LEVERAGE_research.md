# E2R Stock-Web v12 Residual Research — R8 / Loop 91

```yaml
scheduled_round: R8
scheduled_loop: 91
large_sector_id: L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R8
completed_loop: 91
next_round: R9
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R7_loop_91_L7_BIO_HEALTHCARE_MEDICAL_C25_MEDICAL_DEVICE_EXPORT_REIMBURSEMENT_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R8
scheduled_loop = 91
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
```

This run returns to C26, but with a different branch:

```text
streaming platform traffic migration / ad-reward technology / operating leverage bridge
```

The goal is not to repeat ordinary platform-ad recovery. The goal is to separate:

```text
real platform traffic migration with monetizable engagement
```

from:

```text
small-cap ad-tech or reward-ad labels that produce only local spikes.
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
067160 SOOP
273060 와이즈버즈
236810 엔비티
```

They avoid the C26 top-covered symbols and avoid the most recent R8 loop90 C27 content/IP names:

```text
225570, 251270, 194480
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
067160: same archetype, new symbol, live-streaming platform traffic migration / monetizable engagement branch
273060: same archetype, new symbol, ad-tech local spike without revenue operating leverage branch
236810: same archetype, new symbol, reward-ad platform label without durable ad revenue bridge branch
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
067160 SOOP
  profile: atlas/symbol_profiles/067/067160.json
  2024 name transition:
    아프리카TV until 2024-04-22
    SOOP from 2024-04-23
  first_date: 2003-12-19
  last_date: 2026-02-20
  tradable_ohlcv rows: 5,450
  corporate_action_candidate_dates:
    2005-12-27, 2007-06-05, 2007-06-14, 2008-01-24, 2011-01-27
  2024 entry~D+180 contamination: none

273060 와이즈버즈
  profile: atlas/symbol_profiles/273/273060.json
  first_date: 2017-08-07
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,999
  corporate_action_candidate_dates:
    2020-08-05
  2024 entry~D+180 contamination: none

236810 엔비티
  profile: atlas/symbol_profiles/236/236810.json
  first_date: 2021-01-21
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,245
  corporate_action_candidate_dates:
    2022-05-30, 2022-06-21
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C26 should capture platform operating leverage:

```text
traffic / users / engagement
  -> ad inventory or paid interaction
  -> monetization rate
  -> fixed-cost leverage
  -> revenue / OP conversion
  -> price survival after the first platform headline
```

The model can over-score:

```text
platform traffic headline
ad-tech label
reward-ad label
AI advertising theme
small-cap online-ad spike
```

A platform is like a marketplace square. A crowd matters only if the stalls can charge rent, sell inventory, or collect transaction fees. If the crowd only passes through, there is no operating leverage.

---

## 5. Case 1 — 067160 SOOP

```yaml
case_id: C26_R8L91_067160_2024_01_08
symbol: "067160"
name_at_trigger: "아프리카TV"
current_or_latest_name: "SOOP"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE
trigger_date: 2024-01-08
entry_date: 2024-01-08
entry_price_basis: close
entry_price: 98800
classification: positive_with_local_4b_streaming_traffic_migration_monetization_bridge
calibration_usable: true
```

### Evidence interpretation

SOOP / 아프리카TV is the positive control.

The trigger family is not a generic "platform stock" or "ads may recover" label. The specific bridge is:

```text
live-streaming traffic migration
  -> creator and viewer activity concentration
  -> ad inventory / donation / paid interaction opportunity
  -> operating leverage because the platform infrastructure is already built
  -> strong price confirmation
```

This is the proper shape of C26. Traffic has to land on the company's own platform and then become monetizable engagement.

### Price path

Key Stock-Web rows:

```text
2024-01-08: close 98,800
2024-01-09: high 108,200 / close 106,800
2024-02-28: high 139,600 / close 129,900
2024-06-28: high 137,500 / close 131,300
2024-07-01: high 142,000 / close 137,000
2024-07-11: high 143,800 / close 134,600
2024-08-05: low 84,900 / close 89,600
```

Approximate path from entry close:

```text
entry_close: 98,800
peak_high: 143,800
MFE: +45.5%
worst_low_after_entry_in_checked_window: 84,900
MAE: -14.1%
peak_to_later_low_drawdown: -41.0%
```

### Interpretation

This is a real positive, but not a clean "hold forever" Green.

```text
Stage2-Actionable: valid if traffic migration and monetization bridge are explicit.
Stage3-Green: requires ad/paid interaction revenue and OP conversion.
Local 4B: needed after the strong MFE and later peak drawdown.
Hard 4C: no.
```

### Raw component stress test

```text
raw_component_score_proxy:
  traffic_migration_quality: high
  owned_platform_monetization: high
  ad_or_paid_interaction_bridge: medium_high
  operating_leverage_visibility: medium_high
  price_confirmation: high
  post_peak_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 273060 와이즈버즈

```yaml
case_id: C26_R8L91_273060_2024_02_20
symbol: "273060"
name: "와이즈버즈"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE
trigger_date: 2024-02-20
entry_date: 2024-02-20
entry_price_basis: close
entry_price: 1446
classification: local_burst_but_high_mae_adtech_label_without_operating_leverage_bridge
calibration_usable: true
```

### Evidence interpretation

와이즈버즈 is the ad-tech local-burst case. It can look like a C26 candidate because the labels fit:

```text
digital advertising
ad-tech
platform campaign management
AI / performance marketing sympathy
```

But this is not enough. The model needs proof that the label becomes revenue growth and margin expansion. The price path says the initial local spike did not survive.

### Price path

Key Stock-Web rows:

```text
2024-02-20: close 1,446
2024-02-23: high 1,570 / close 1,570
2024-03-05: high 1,636 / close 1,585
2024-03-06: high 1,834 / close 1,621
2024-04-12: continued fade below the trigger region
2024-08-05: low 864 / close 881
2024-09-09: low 820 / close 866
```

Approximate path from entry close:

```text
entry_close: 1,446
peak_high: 1,834
MFE: +26.8%
worst_low: 820
MAE: -43.3%
```

### Interpretation

This is the C26 4B/4C boundary:

```text
Stage2-Watch: allowed.
Stage2-Actionable: possible only as short-term local burst, not durable Green.
Stage3-Green: blocked.
Hard 4C: not the strongest, but high-MAE false-positive guard applies.
```

The useful lesson is that a +20~30% local burst can still be a bad Stage3 signal if the operating leverage bridge is missing.

### Raw component stress test

```text
raw_component_score_proxy:
  adtech_label_relevance: high
  owned_platform_monetization: low_to_medium
  revenue_visibility: weak
  margin_bridge: weak
  price_confirmation_initial: medium
  post_burst_survival: failed
  drawdown_penalty: high
```

---

## 7. Case 3 — 236810 엔비티

```yaml
case_id: C26_R8L91_236810_2024_02_20
symbol: "236810"
name: "엔비티"
canonical_archetype_id: C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE
fine_archetype_id: STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE
trigger_date: 2024-02-20
entry_date: 2024-02-20
entry_price_basis: close
entry_price: 8620
classification: hard_4c_candidate_reward_ad_platform_label_without_revenue_margin_bridge
calibration_usable: true
```

### Evidence interpretation

엔비티 is the hard guardrail case. It is a reward-ad / ad platform name, so a label-based model can place it into C26 easily. That is exactly the error.

The bridge should ask:

```text
Is user traffic growing?
Is ad inventory owned or merely brokered?
Is reward traffic monetized at improving take rate?
Does revenue growth exceed user-acquisition or reward cost?
Does OP margin expand?
```

Without those answers, the label is not enough.

### Price path

Key Stock-Web rows:

```text
2024-02-20: close 8,620
2024-02-20: high 9,160
2024-03-25: high 7,140 / close 6,960
2024-07-23: high 5,460 / close 4,525
2024-08-05: low 3,670 / close 4,015
2024-09-09: low 3,225 / close 3,440
```

Approximate path from entry close:

```text
entry_close: 8,620
peak_high: 9,160
MFE: +6.3%
worst_low: 3,225
MAE: -62.6%
```

### Interpretation

This is the hard C26 false-positive.

```text
Stage2-Watch: possible from the ad-platform label.
Stage2-Actionable: blocked unless revenue/margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The signal failed immediately: shallow MFE, then long decay.

### Raw component stress test

```text
raw_component_score_proxy:
  reward_ad_platform_label: high
  owned_traffic_quality: weak
  monetization_rate_bridge: weak
  cost_leverage_visibility: weak
  price_confirmation: failed
  drawdown_penalty: extreme
  hard_4c_guard: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C26 grid:

```text
067160 SOOP:
  real owned-platform traffic migration and monetizable engagement positive;
  local 4B required after peak drawdown.

273060 와이즈버즈:
  ad-tech label created a local burst,
  but no durable operating leverage bridge; high-MAE false-positive guard.

236810 엔비티:
  reward-ad platform label failed badly;
  hard 4C candidate without revenue/margin bridge.
```

Shared rule:

```text
C26 is not "digital ad stock went up."
C26 is "owned traffic becomes monetizable ad or paid interaction revenue, and fixed-cost leverage converts that revenue into OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C26_R8L91_067160_2024_01_08","scheduled_round":"R8","scheduled_loop":91,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE","symbol":"067160","name_at_trigger":"아프리카TV","current_or_latest_name":"SOOP","trigger_date":"2024-01-08","entry_date":"2024-01-08","entry_price":98800,"peak_high":143800,"peak_date":"2024-07-11","worst_low":84900,"worst_low_date":"2024-08-05","mfe_pct":45.5,"mae_pct":-14.1,"peak_to_later_low_drawdown_pct":-41.0,"classification":"positive_with_local_4b_streaming_traffic_migration_monetization_bridge","calibration_usable":true,"evidence_family":"owned_streaming_platform_traffic_migration_ad_paid_interaction_operating_leverage","residual_error":"positive_entry_but_peak_drawdown_requires_local_4b_overlay","shadow_rule_candidate":"allow_actionable_when_owned_traffic_and_monetization_bridge_confirm; attach_4b_after_large_mfe_drawdown"}
{"row_type":"case","case_id":"C26_R8L91_273060_2024_02_20","scheduled_round":"R8","scheduled_loop":91,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE","symbol":"273060","name":"와이즈버즈","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":1446,"peak_high":1834,"peak_date":"2024-03-06","worst_low":820,"worst_low_date":"2024-09-09","mfe_pct":26.8,"mae_pct":-43.3,"classification":"local_burst_but_high_mae_adtech_label_without_operating_leverage_bridge","calibration_usable":true,"evidence_family":"adtech_label_local_burst_without_revenue_margin_bridge","residual_error":"local_adtech_spike_can_be_mistaken_for_platform_operating_leverage","shadow_rule_candidate":"keep_adtech_label_spike_as_local_4b_or_watch_not_green_if_price_survival_fails"}
{"row_type":"case","case_id":"C26_R8L91_236810_2024_02_20","scheduled_round":"R8","scheduled_loop":91,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE","symbol":"236810","name":"엔비티","trigger_date":"2024-02-20","entry_date":"2024-02-20","entry_price":8620,"peak_high":9160,"peak_date":"2024-02-20","worst_low":3225,"worst_low_date":"2024-09-09","mfe_pct":6.3,"mae_pct":-62.6,"classification":"hard_4c_candidate_reward_ad_platform_label_without_revenue_margin_bridge","calibration_usable":true,"evidence_family":"reward_ad_platform_label_without_owned_traffic_monetization_margin_bridge","residual_error":"reward_ad_label_can_create_catastrophic_false_positive_without_operating_leverage","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_revenue_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R8","scheduled_loop":91,"large_sector_id":"L8_PLATFORM_CONTENT_SW_SECURITY","canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","fine_archetype_id":"STREAMING_PLATFORM_TRAFFIC_MIGRATION_AND_AD_REWARD_TECH_OPERATING_LEVERAGE_BRIDGE_VS_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R8","scheduled_loop":91,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","rule_id":"C26_OWNED_TRAFFIC_MONETIZATION_OP_LEVERAGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C26, do not open Stage2-Actionable or Stage3-Green from digital ad, ad-tech, reward-ad, platform, or traffic headline alone. Require owned or strongly controlled user traffic, monetizable ad inventory or paid interaction, take-rate or ARPU bridge, fixed-cost operating leverage, revenue/OP conversion, and post-trigger price survival. Local ad-tech spikes should remain Watch/4B, not Green. Shallow-MFE/high-MAE reward-ad or brokered-ad names should route to hard-4C.","expected_effect":"Preserve true owned-platform traffic migration positives while reducing ad-tech and reward-ad label false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R8","scheduled_loop":91,"canonical_archetype_id":"C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE","residual_type":"platform_ad_revenue_operating_leverage_bridge_guard","contribution":"Adds one owned streaming-platform positive and two ad-tech/reward-ad false positives to calibrate C26 traffic monetization, OP leverage, 4B, and hard-4C routing.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C26_OWNED_TRAFFIC_MONETIZATION_OP_LEVERAGE_REQUIRED

IF canonical_archetype_id == C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE:

  Do not open Stage3-Green from:
    - digital advertising label alone
    - ad-tech / reward-ad label alone
    - platform traffic headline alone
    - creator/user migration headline alone
    - one-week local volume spike alone

  Require at least two of:
    - owned or strongly controlled user traffic
    - engagement retention after the traffic event
    - monetizable ad inventory or paid interaction
    - ARPU / take-rate / ad fill-rate bridge
    - fixed-cost leverage into OP margin
    - revenue or OP revision confirmation
    - low-MAE post-trigger price survival

  If MFE < 10% and MAE < -40%:
    route to C26 hard-4C candidate.

  If MFE > 20% but later MAE < -40%:
    classify as local burst / 4B failure, not Green.

  If MFE > 40% and peak-to-later-low drawdown exceeds -35%:
    preserve positive entry but attach local 4B watch.

  Distinguish:
    - owned streaming/community platform traffic migration positives
    - from ad-tech agencies or reward-ad labels where traffic and monetization are not controlled.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R8_loop_91_L8_PLATFORM_CONTENT_SW_SECURITY_C26_PLATFORM_AD_REVENUE_OPERATING_LEVERAGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C26 platform/ad revenue operating leverage cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C26_OWNED_TRAFFIC_MONETIZATION_OP_LEVERAGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C26 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C26 cases agree, consider implementing a canonical guard that:
   - blocks platform/ad-tech label Green without owned traffic and monetization bridge,
   - preserves owned-platform traffic migration positives with price survival,
   - attaches local 4B after large MFE and deep drawdown,
   - routes shallow-MFE/high-MAE reward-ad cases to C26 hard-4C.

Expected next schedule:
completed_round = R8
completed_loop = 91
next_round = R9
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R8
completed_loop = 91
next_round = R9
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
