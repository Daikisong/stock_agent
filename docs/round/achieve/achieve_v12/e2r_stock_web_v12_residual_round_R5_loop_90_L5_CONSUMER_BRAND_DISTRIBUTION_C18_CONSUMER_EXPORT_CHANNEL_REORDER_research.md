# E2R Stock-Web v12 Residual Research — R5 / Loop 90

```yaml
scheduled_round: R5
scheduled_loop: 90
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE

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

completed_round: R5
completed_loop: 90
next_round: R6
next_loop: 90
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the working sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_90_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

Under v12 sequential scheduler:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 90
```

R5 maps to:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 coverage already used:

```text
loop88: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop89: C19_BRAND_RETAIL_INVENTORY_MARGIN
```

This run therefore uses:

```text
canonical_archetype_id = C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C18_CONSUMER_EXPORT_CHANNEL_REORDER
rows: 38
symbols: 19
date_range: 2023-01-18~2024-06-26
good/bad S2: 17/9
4B/4C: 0/0
URL pending/proxy: 10/10
top covered symbols:
  001680(4), 280360(4), UNKNOWN_SYMBOL(4), 049770(3), 271560(3), 003960(2)
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected symbols:

```text
257720 실리콘투
090430 아모레퍼시픽
051900 LG생활건강
```

These symbols are not in the C18 top-covered list. The run intentionally avoids the recently used R5 symbols from C20/C19 such as `003230`, `005180`, `271560`, `069960`, `023530`, and `008770`.

Novelty classification:

```text
257720: same archetype, new symbol, new trigger family
090430: same archetype, new symbol, new trigger family
051900: same archetype, new symbol, new trigger family
```

---

## 3. Price-atlas validation

Manifest fields checked:

```text
source_name: FinanceData/marcap
price_adjustment_status: raw_unadjusted_marcap
min_date: 1995-05-02
max_date: 2026-02-20
tradable_row_count: 14,354,401
raw_row_count: 15,214,118
symbol_count: 5,414
active_like_symbol_count: 2,868
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
257720 실리콘투
  profile: atlas/symbol_profiles/257/257720.json
  first_date: 2021-09-29
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,074
  corporate_action_candidate_dates: 2022-07-14, 2022-08-02
  2024 entry~D+180 contamination: none

090430 아모레퍼시픽
  profile: atlas/symbol_profiles/090/090430.json
  first_date: 2006-06-29
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,834
  corporate_action_candidate_dates: 2015-05-08
  2024 entry~D+180 contamination: none

051900 LG생활건강
  profile: atlas/symbol_profiles/051/051900.json
  first_date: 2001-04-25
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,125
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype problem

C18 is supposed to identify cases where export/channel data show that a consumer product is not merely enjoying a one-off headline, but is moving through repeated overseas sell-through and reorder loops.

The failure mode is subtle:

```text
A K-beauty / K-food / consumer-export headline can be real,
but still not be investable as Stage3-Green unless there is evidence that:
  1. overseas channel inventory is moving,
  2. retailers or distributors are reordering,
  3. geographic exposure is broad enough,
  4. sales convert to OP/EPS,
  5. margin is not consumed by marketing, inventory, or channel mix.
```

The market often misreads:

```text
"China recovery"
"duty-free rebound"
"K-beauty global popularity"
"brand recognition overseas"
```

as if they were equivalent to:

```text
repeat channel reorder + sell-through + margin bridge
```

They are not the same signal.

---

## 5. Case 1 — 257720 실리콘투

```yaml
case_id: C18_R5L90_257720_2024_05_09
symbol: "257720"
name: "실리콘투"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE
trigger_date: 2024-05-09
entry_date: 2024-05-09
entry_price_basis: close
entry_price: 20200
classification: positive_with_local_4b_watch
calibration_usable: true
```

### Evidence interpretation

This is the cleanest positive in the set.

The trigger family is not simply "K-beauty is popular." The investable thesis is closer to:

```text
multi-brand K-beauty distributor / platform
  -> global retail and e-commerce channel access
  -> repeated cross-border order flow
  -> revenue and earnings acceleration
  -> price rerating
```

The 2024 price path behaves like a real C18 positive.

### Price path

Key Stock-Web rows:

```text
2024-05-09: close 20,200
2024-05-10: high 26,250 / close 26,250
2024-05-16: close 28,900
2024-05-31: high 41,350 / close 37,750
2024-06-19: high 54,200 / close 50,700
2024-08-05: low 32,150 / close 36,250
2024-11-14: low 27,000 / close 28,250
2024-12-09: low 23,300 / close 23,550
```

Approximate return path from 2024-05-09 close:

```text
entry_close: 20,200
peak_high_in_window: 54,200
MFE: +168.3%
worst_forward_low_after_entry_window: 23,300
MAE vs entry: +15.3% if using forward low after entry
drawdown_from_peak_to_later_low: -57.0%
```

Interpretation:

```text
Stage2 / Stage3-Green was justified only if the model recognized real export-channel reorder evidence.
A local 4B overlay is still needed because the post-peak drawdown was deep.
This should not be treated as a clean "buy and forget" Green.
```

### Scoring stress test

```text
current_calibrated_profile_expected:
  evidence_bonus: high
  revision_score: high
  price_only_blowoff_block: not triggered initially, because non-price evidence exists
  4B_local_watch: yes after +100%+ MFE and peak drawdown
  hard_4c: no

shadow_rule_effect:
  allow Stage3-Green only when export/channel reorder evidence is explicit.
  after large MFE, require local 4B watch even if the business thesis remains intact.
```

---

## 6. Case 2 — 090430 아모레퍼시픽

```yaml
case_id: C18_R5L90_090430_2024_04_30
symbol: "090430"
name: "아모레퍼시픽"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE
trigger_date: 2024-04-30
entry_date: 2024-04-30
entry_price_basis: close
entry_price: 169500
classification: counterexample_high_mae_legacy_china_recovery_headline
calibration_usable: true
```

### Evidence interpretation

아모레퍼시픽 had legitimate global-brand assets, including brands with North America relevance. However, this case is not the same as a clean C18 reorder-platform case.

The failure mode:

```text
legacy K-beauty brand + China/duty-free recovery expectation
  -> local price bounce
  -> not enough evidence of repeat channel sell-through and margin bridge
  -> later drawdown
```

In C18, large-cap brand recognition is not enough. The model must demand the bridge from global channel demand into reported margin and EPS.

### Price path

Key Stock-Web rows:

```text
2024-04-30: close 169,500
2024-05-21: high 185,000 / close 184,800
2024-05-31: high 200,500 / close 194,200
2024-07-03: low 147,000 / close 151,500
2024-09-25: high 157,600 / close 150,700
2024-11-14: low 107,000 / close 107,000
2024-12-02: low 102,900 / close 103,300
```

Approximate return path from 2024-04-30 close:

```text
entry_close: 169,500
peak_high_in_window: 200,500
MFE: +18.3%
worst_low_in_window: 102,900
MAE: -39.3%
```

Interpretation:

```text
The local rally did not reach a clean 4B-level profit cushion.
The later MAE was large.
This is a Stage2 false-positive / hard 4C candidate if the model treats legacy K-beauty recovery as equivalent to channel reorder.
```

### Scoring stress test

```text
current_calibrated_profile_risk:
  likely over-credits global K-beauty headline if evidence is not separated by channel.
  likely over-credits price response if early May rally is read as confirmation.
  misses that MFE was shallow relative to MAE.

shadow_rule_effect:
  if export thesis is mostly China/duty-free/brand recovery:
    cap at Stage2-Watch or Stage2-Yellow
  if no repeated overseas sell-through / retailer expansion / channel revenue bridge:
    block Stage3-Green
  if MFE < 20% and MAE > 30%:
    classify as C18 false-positive or hard-4C candidate
```

---

## 7. Case 3 — 051900 LG생활건강

```yaml
case_id: C18_R5L90_051900_2024_04_30
symbol: "051900"
name: "LG생활건강"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE
trigger_date: 2024-04-30
entry_date: 2024-04-30
entry_price_basis: close
entry_price: 420000
classification: counterexample_legacy_china_duty_free_recovery_not_reorder
calibration_usable: true
```

### Evidence interpretation

LG생활건강 is a major consumer brand company, but this case shows why C18 needs a stricter distinction between:

```text
large legacy brand recovering from depressed expectations
```

and:

```text
fresh export-channel reorder compounding
```

A rebound in China/duty-free sentiment or broad K-beauty attention can produce a tradable bounce, but that is not automatically a durable C18 reorder signal.

### Price path

Key Stock-Web rows:

```text
2024-04-30: close 420,000
2024-05-10: high 479,000 / close 466,000
2024-05-23: high 480,000 / close 460,000
2024-06-28: low 342,500 / close 345,500
2024-09-27: high 391,500 / close 383,500
2024-11-21: low 314,000 / close 314,000
2024-11-29: low 309,500 / close 310,500
```

Approximate return path from 2024-04-30 close:

```text
entry_close: 420,000
peak_high_in_window: 480,000
MFE: +14.3%
worst_low_in_window: 309,500
MAE: -26.3%
```

Interpretation:

```text
This is not a hard 4C like the Amore case, but it is still a counterexample.
The upside was shallow, the drawdown was material, and the thesis needed channel-level evidence that was not visible from the broad K-beauty / China recovery headline alone.
```

### Scoring stress test

```text
current_calibrated_profile_risk:
  may confuse low-base rebound and true channel reorder.
  may treat brand size as evidence quality.
  may over-credit "K-beauty recovery" when the actual bridge is legacy-channel normalization.

shadow_rule_effect:
  require export-channel reorder evidence before Actionable/Green.
  cap legacy China/duty-free rebound at Watch/Yellow unless margin and non-China channel mix confirm.
```

---

## 8. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C18_R5L90_257720_2024_05_09","scheduled_round":"R5","scheduled_loop":90,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE","symbol":"257720","name":"실리콘투","trigger_date":"2024-05-09","entry_date":"2024-05-09","entry_price":20200,"peak_high":54200,"peak_date":"2024-06-19","worst_low":23300,"worst_low_date":"2024-12-09","mfe_pct":168.3,"mae_pct":15.3,"peak_to_later_low_drawdown_pct":-57.0,"classification":"positive_with_local_4b_watch","calibration_usable":true,"evidence_family":"export_channel_reorder_platform_sell_through","residual_error":"none_for_entry_but_local_4b_needed_after_blowoff","shadow_rule_candidate":"allow_green_only_with_real_channel_reorder_bridge; add_4b_watch_after_large_mfe_drawdown"}
{"row_type":"case","case_id":"C18_R5L90_090430_2024_04_30","scheduled_round":"R5","scheduled_loop":90,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE","symbol":"090430","name":"아모레퍼시픽","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":169500,"peak_high":200500,"peak_date":"2024-05-31","worst_low":102900,"worst_low_date":"2024-12-02","mfe_pct":18.3,"mae_pct":-39.3,"classification":"counterexample_high_mae_legacy_china_recovery_headline","calibration_usable":true,"evidence_family":"legacy_k_beauty_china_duty_free_recovery_without_reorder_bridge","residual_error":"headline_and_local_bounce_can_overpromote_to_actionable","shadow_rule_candidate":"cap_legacy_brand_recovery_without_sell_through_bridge_at_watch_or_yellow; hard_4c_candidate_if_mfe_lt_20_and_mae_gt_30"}
{"row_type":"case","case_id":"C18_R5L90_051900_2024_04_30","scheduled_round":"R5","scheduled_loop":90,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE","symbol":"051900","name":"LG생활건강","trigger_date":"2024-04-30","entry_date":"2024-04-30","entry_price":420000,"peak_high":480000,"peak_date":"2024-05-23","worst_low":309500,"worst_low_date":"2024-11-29","mfe_pct":14.3,"mae_pct":-26.3,"classification":"counterexample_legacy_china_duty_free_recovery_not_reorder","calibration_usable":true,"evidence_family":"legacy_consumer_brand_recovery_without_channel_reorder_bridge","residual_error":"brand_size_and_recovery_headline_can_overstate_c18_quality","shadow_rule_candidate":"require_channel_sell_through_or_geographic_mix_bridge_before_stage2_actionable"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":90,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_BEAUTY_EXPORT_CHANNEL_REORDER_SELL_THROUGH_BRIDGE_VS_CHINA_DUTY_FREE_RECOVERY_HEADLINE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":90,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","rule_id":"C18_EXPORT_CHANNEL_REORDER_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C18, global consumer-export popularity, China recovery, or duty-free rebound is not sufficient for Stage2-Actionable or Stage3-Green. Require evidence of export-channel reorder, overseas sell-through, retailer/distributor expansion, geographic diversification, and OP/EPS conversion. Cap legacy China/duty-free rebound at Watch/Yellow unless the bridge is explicit.","expected_effect":"Reduce high-MAE false positives in legacy beauty/consumer names while preserving platform/channel reorder positives such as 257720.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":90,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"stage2_false_positive_guard","contribution":"Separates true export reorder/platform compounding from legacy brand recovery headlines. Adds one strong positive and two counterexamples for calibration balance.","do_not_count_as_global_weight_delta":true}
```

---

## 9. Proposed canonical-archetype shadow rule

```text
C18_EXPORT_CHANNEL_REORDER_BRIDGE_REQUIRED

IF canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER:

  Do not treat any of the following as enough for Stage2-Actionable / Stage3-Green:
    - K-beauty or K-food popularity headline
    - China recovery
    - duty-free rebound
    - large legacy brand recognition
    - one-quarter local price bounce

  Require at least two of:
    - overseas sell-through evidence
    - distributor or retailer reorder evidence
    - export/customs acceleration tied to the company/brand/channel
    - non-China geographic diversification
    - channel inventory normalization
    - gross margin or OP/EPS conversion
    - repeatable platform/wholesale revenue model

  If evidence is mostly China/duty-free/legacy-brand rebound:
    cap at Stage2-Watch or Stage2-Yellow.

  If MFE < 20% and MAE < -25% within the forward window:
    mark as false-positive guard candidate.

  If MFE > 50% but later peak drawdown > -40%:
    preserve positive classification but attach local 4B watch.
```

---

## 10. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_90_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C18 cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C18_EXPORT_CHANNEL_REORDER_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C18 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If later enough C18 cases agree, consider implementing a canonical guard that:
   - blocks China/duty-free/legacy-brand headlines from Stage3-Green without channel reorder bridge,
   - allows platform/channel reorder positives when revenue and sell-through evidence exist,
   - adds local 4B watch after large MFE and peak drawdown.

Expected next schedule:
completed_round = R5
completed_loop = 90
next_round = R6
next_loop = 90
```
