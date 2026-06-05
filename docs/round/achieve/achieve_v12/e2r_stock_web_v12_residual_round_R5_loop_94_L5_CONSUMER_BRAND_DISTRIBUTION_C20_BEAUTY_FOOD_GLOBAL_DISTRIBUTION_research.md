# E2R Stock-Web v12 Residual Research — R5 / Loop 94

```yaml
scheduled_round: R5
scheduled_loop: 94
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE

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

completed_round: R5
completed_loop: 94
next_round: R6
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_94_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 94
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage:

```text
loop91: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop92: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop93: C19_BRAND_RETAIL_INVENTORY_MARGIN
```

This run returns to C20, but avoids the top-covered beauty/food names and uses a different fine branch:

```text
K-food global distribution / export reorder / channel-margin bridge
vs brand-label late chase
```

The aim is to separate:

```text
real global distribution and reorder engines
```

from:

```text
food brand familiarity, stable overseas label, or late K-food theme chase without margin evidence.
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
rows: 19
symbols: 11
date_range: 2023-01-30~2024-06-14
good/bad S2: 8/2
4B/4C: 4/0
URL pending/proxy: 7/0
top covered symbols:
  226320(3), 161890(2), 192820(2), 214420(2), 241710(2), 439090(2)
```

Selected symbols:

```text
003230 삼양식품
271560 오리온
017810 풀무원
```

They avoid the C20 top-covered symbols and avoid recent R5 loop91~93 names:

```text
loop91 avoid: 004370, 097950, 007310
loop92 avoid: 352480, 018290, 002790
loop93 avoid: 105630, 383220, 298540
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
003230: same archetype, new symbol, K-ramen global export distribution positive with post-multibagger 4B watch
271560: same archetype, new symbol, stable global confectionery/food label Watch cap without strong incremental channel-margin bridge
017810: same archetype, new symbol, K-food/plant-based brand late-chase hard-4C without reorder-margin bridge
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
003230 삼양식품
  profile: atlas/symbol_profiles/003/003230.json
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,704
  corporate_action_candidate_dates:
    2003-07-25
  2024 entry~D+180 contamination: none

271560 오리온
  profile: atlas/symbol_profiles/271/271560.json
  first_date: 2017-07-07
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,113
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

017810 풀무원
  profile: atlas/symbol_profiles/017/017810.json
  name history includes:
    풀무원, 풀무원홀딩스
  first_date: 1995-10-27
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,550
  corporate_action_candidate_dates:
    1996-01-03, 1999-03-17, 1999-07-19, 2008-07-29, 2008-09-29, 2019-05-07
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C20 is about global beauty/food distribution and monetization. It is not a generic consumer brand or K-food/K-beauty label.

The model can over-score:

```text
K-food brand
ramen / confectionery / plant-based label
global distribution headline
export growth sympathy
retail channel expansion
one-week food-stock volume spike
late chase after a global-brand rerating
```

The C20 bridge must be stricter:

```text
brand / product export demand
  -> overseas sell-through
  -> distributor reorder / channel expansion
  -> SKU or geography expansion
  -> ASP / mix / FX benefit
  -> manufacturing utilization and logistics cost control
  -> margin / OP conversion
  -> price survival after the first global-distribution rally
```

A global food brand is like a product leaving a Korean port. C20 asks whether it reaches shelves abroad, sells through, gets reordered, and returns home as margin, not just as a famous label.

---

## 5. Case 1 — 003230 삼양식품

```yaml
case_id: C20_R5L94_003230_2024_03_04
symbol: "003230"
name: "삼양식품"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE
trigger_date: 2024-03-04
entry_date: 2024-03-04
entry_price_basis: close
entry_price: 191000
classification: positive_k_ramen_global_distribution_export_reorder_margin_bridge_with_4b_after_multibagger
calibration_usable: true
```

### Evidence interpretation

삼양식품 is the constructive C20 control.

The useful C20 read is not simply:

```text
K-food brand is famous
```

It is:

```text
ramen export demand
  -> global shelf expansion and distributor reorder
  -> SKU/geography pull
  -> manufacturing utilization
  -> FX / ASP / mix support
  -> margin and OP conversion
  -> repeated price confirmation
```

The forward path delivered an extraordinary rerating. That makes it a true C20 positive. However, after a multi-bagger MFE, the model must attach local 4B unless fresh reorder/margin evidence refreshes the bridge.

### Price path

Key Stock-Web rows:

```text
2024-03-04: close 191,000
2024-03-25: high 212,500 / close 206,500
2024-04-22: high 293,000 / close 293,000
2024-05-07: high 315,500 / close 305,500
2024-07-24: high 686,000 / close 679,000
2024-08-05: low 486,000 / close 528,000
2024-10-16: high 580,000 / close 569,000
2024-11-05: high 607,000 / close 602,000
```

Approximate path from entry close:

```text
entry_close: 191,000
peak_high: 686,000
MFE: +259.2%
worst_low_after_entry: 184,700
MAE: -3.3%
```

### Interpretation

This is a C20 positive with post-rerating 4B discipline:

```text
Stage2-Actionable: valid if overseas sell-through, reorder, and margin bridge are explicit.
Stage3-Green: possible only with continuing channel/margin evidence.
Local 4B: mandatory after multi-bagger MFE unless fresh reorder / margin / capacity evidence appears.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  k_food_global_distribution_relevance: very_high
  export_reorder_bridge: high
  sku_geography_expansion_bridge: high
  margin_op_bridge: high
  price_confirmation: extreme
  price_survival: high
  local_4b_overlay: required_after_large_mfe
```

---

## 6. Case 2 — 271560 오리온

```yaml
case_id: C20_R5L94_271560_2024_02_16
symbol: "271560"
name: "오리온"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE
trigger_date: 2024-02-16
entry_date: 2024-02-16
entry_price_basis: close
entry_price: 97200
classification: watch_cap_global_confectionery_food_label_without_strong_incremental_channel_margin_bridge
calibration_usable: true
```

### Evidence interpretation

오리온 is the stable global-food Watch cap.

The company has real overseas brand and distribution relevance. That is why it is a useful guardrail. C20 should not promote:

```text
established food brand
overseas confectionery distribution
stable global revenue label
```

into Actionable/Green unless the incremental bridge is visible:

```text
new channel expansion
reorder acceleration
SKU/geography growth
margin or FX/mix improvement
```

The forward path after the trigger had shallow MFE and then a medium drawdown. It was not a hard collapse, but it did not validate a strong global-distribution rerating.

### Price path

Key Stock-Web rows:

```text
2024-02-16: high 98,300 / close 97,200
2024-02-19: high 99,400 / close 97,700
2024-04-08: high 98,600 / close 97,200
2024-08-05: low 81,800 / close 83,900
2024-09-10: low 87,100 / close 87,300
2024-10-10: high 101,500 / close 101,000
2024-10-21: high 101,800 / close 99,500
```

Approximate path from entry close:

```text
entry_close: 97,200
peak_high: 101,800
MFE: +4.7%
worst_low_after_entry: 81,800
MAE: -15.8%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from global food distribution relevance.
Stage2-Actionable: blocked unless incremental channel, reorder, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: not extreme.
```

The lesson is that global brand quality is not the same as fresh distribution operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  global_food_brand_quality: high
  overseas_distribution_base: high
  incremental_channel_bridge: weak_to_medium
  reorder_acceleration_bridge: weak
  margin_mix_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 017810 풀무원

```yaml
case_id: C20_R5L94_017810_2024_07_24
symbol: "017810"
name: "풀무원"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 14320
classification: hard_4c_candidate_k_food_plant_based_brand_late_chase_without_reorder_margin_bridge
calibration_usable: true
```

### Evidence interpretation

풀무원 is the late-chase guardrail case.

The setup looked plausible:

```text
K-food / plant-based / fresh food brand
global distribution expectation
US or overseas channel hope
late momentum after a consumer-food theme move
```

But from the selected late entry, the stock produced only shallow MFE and then fell into a large drawdown. The model should not treat a familiar food brand or overseas-channel hope as C20 Green unless reorder and margin bridge are explicit.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 15,050 / close 14,320
2024-08-02: low 13,000 / close 13,120
2024-08-05: low 11,000 / close 11,920
2024-09-09: low 10,010 / close 10,320
2024-09-11: low 10,010 / close 10,140
2024-10-25: low 10,160 / close 10,220
```

Approximate path from entry close:

```text
entry_close: 14,320
peak_high: 15,050
MFE: +5.1%
worst_low_after_entry: 10,010
MAE: -30.1%
```

### Interpretation

This is a hard C20 false-positive:

```text
Stage2-Watch: possible from K-food / plant-based global-distribution relevance.
Stage2-Actionable: blocked without distributor reorder, channel sell-through, and margin bridge.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30% MAE.
```

The lesson is that a familiar brand can become a late-chase trap when the global-distribution bridge is not current.

### Stress-test components

```text
raw_component_score_proxy:
  k_food_plant_based_label: high
  global_distribution_hope: medium_high
  reorder_bridge: weak
  margin_bridge: weak
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

The three-case C20 K-food grid:

```text
003230 삼양식품:
  true K-food global distribution / export reorder positive;
  multi-bagger MFE and controlled MAE, but 4B required after rerating.

271560 오리온:
  real global food brand, but weak incremental channel/margin bridge;
  shallow MFE and medium MAE, Watch/Yellow cap.

017810 풀무원:
  K-food / plant-based late-chase failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C20 is not "K-food brand is known."
C20 is "overseas sell-through, distributor reorder, channel expansion, SKU/geography growth, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C20_R5L94_003230_2024_03_04","scheduled_round":"R5","scheduled_loop":94,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE","symbol":"003230","name":"삼양식품","trigger_date":"2024-03-04","entry_date":"2024-03-04","entry_price":191000,"peak_high":686000,"peak_date":"2024-07-24","worst_low_after_entry":184700,"worst_low_after_entry_date":"2024-03-14","mfe_pct":259.2,"mae_pct":-3.3,"classification":"positive_k_ramen_global_distribution_export_reorder_margin_bridge_with_4b_after_multibagger","calibration_usable":true,"evidence_family":"k_ramen_global_export_distribution_reorder_sku_geography_margin_bridge","residual_error":"positive_global_distribution_path_still_requires_4b_after_multibagger_mfe_without_fresh_reorder_margin_evidence","shadow_rule_candidate":"preserve_positive_when_export_reorder_channel_margin_bridge_confirms_but_attach_4b_after_large_mfe"}
{"row_type":"case","case_id":"C20_R5L94_271560_2024_02_16","scheduled_round":"R5","scheduled_loop":94,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE","symbol":"271560","name":"오리온","trigger_date":"2024-02-16","entry_date":"2024-02-16","entry_price":97200,"peak_high":101800,"peak_date":"2024-10-21","worst_low_after_entry":81800,"worst_low_after_entry_date":"2024-08-05","mfe_pct":4.7,"mae_pct":-15.8,"classification":"watch_cap_global_confectionery_food_label_without_strong_incremental_channel_margin_bridge","calibration_usable":true,"evidence_family":"global_confectionery_food_distribution_label_without_incremental_reorder_margin_bridge","residual_error":"global_food_brand_quality_can_overpromote_without_fresh_channel_expansion_and_margin_conversion","shadow_rule_candidate":"cap_stable_global_food_brand_at_watch_yellow_if_mfe_shallow_and_incremental_bridge_missing"}
{"row_type":"case","case_id":"C20_R5L94_017810_2024_07_24","scheduled_round":"R5","scheduled_loop":94,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE","symbol":"017810","name":"풀무원","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":14320,"peak_high":15050,"peak_date":"2024-07-24","worst_low_after_entry":10010,"worst_low_after_entry_date":"2024-09-09","mfe_pct":5.1,"mae_pct":-30.1,"classification":"hard_4c_candidate_k_food_plant_based_brand_late_chase_without_reorder_margin_bridge","calibration_usable":true,"evidence_family":"k_food_plant_based_global_distribution_late_chase_without_reorder_margin_bridge","residual_error":"familiar_food_brand_can_be_late_chase_false_positive_without_current_reorder_and_margin_evidence","shadow_rule_candidate":"route_late_k_food_brand_chase_to_hard_4c_if_mfe_shallow_mae_large_and_reorder_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":94,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_FOOD_GLOBAL_DISTRIBUTION_EXPORT_REORDER_MARGIN_BRIDGE_VS_BRAND_LABEL_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":94,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","rule_id":"C20_GLOBAL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C20, do not open Stage2-Actionable or Stage3-Green from K-food/K-beauty brand, ramen/confectionery/plant-based label, overseas distribution headline, export sympathy, retail channel expansion, or one-week consumer brand spike alone. Require overseas sell-through, distributor reorder, channel expansion, SKU/geography growth, ASP/mix/FX benefit, manufacturing utilization, logistics-cost control, margin/OP conversion, and post-trigger price survival. True K-food export positives may be Actionable when reorder and margin bridge are explicit, but multi-bagger MFE should attach local 4B unless fresh evidence appears. Stable global food brands with shallow MFE should cap at Watch/Yellow without incremental channel evidence. Late K-food/plant-based brand chases with shallow MFE and high MAE should route to hard-4C when reorder and margin bridge are missing.","expected_effect":"Preserve true global food/beauty distribution positives while reducing brand-label and late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":94,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","residual_type":"global_sellthrough_reorder_margin_guard","contribution":"Adds one K-ramen global-distribution positive with 4B-after-multibagger, one stable global-food Watch cap, and one K-food late-chase hard-4C counterexample to calibrate C20 sell-through, reorder, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C20_GLOBAL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:

  Do not open Stage3-Green from:
    - K-food / K-beauty brand label alone
    - ramen / confectionery / plant-based label alone
    - global distribution headline alone
    - export growth sympathy alone
    - retail channel expansion label alone
    - one-week food/beauty brand volume spike alone

  Require at least two of:
    - overseas sell-through
    - distributor reorder
    - channel expansion with paid demand
    - SKU or geography expansion
    - ASP / mix / FX benefit
    - manufacturing utilization
    - logistics-cost control
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the export/distribution headline

  If MFE < 10% and MAE < -30%:
    route to C20 hard-4C candidate.

  If MFE is shallow and the brand is stable but incremental bridge is weak:
    cap at Watch/Yellow.

  If MFE is extraordinary:
    preserve positive classification but attach local 4B unless reorder/margin evidence refreshes the thesis.

  Distinguish:
    - global distribution engines with real sell-through and reorder
    - from familiar food/beauty brands where the global label does not create incremental operating leverage.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_94_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C20 global food/beauty distribution cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C20_GLOBAL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C20 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C20 cases agree, consider implementing a canonical guard that:
   - blocks brand-label Green without overseas sell-through, reorder, channel expansion, and margin bridge,
   - preserves export/reorder positives only with price survival and refreshed evidence,
   - attaches local 4B after multi-bagger MFE,
   - caps stable global-food labels at Watch/Yellow without incremental channel bridge,
   - routes shallow-MFE/high-MAE late K-food chases to hard-4C.

Expected next schedule:
completed_round = R5
completed_loop = 94
next_round = R6
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 94
next_round = R6
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
