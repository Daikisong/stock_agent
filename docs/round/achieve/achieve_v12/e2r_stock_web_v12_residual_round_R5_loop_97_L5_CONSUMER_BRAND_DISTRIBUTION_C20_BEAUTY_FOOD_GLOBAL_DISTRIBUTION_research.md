# E2R Stock-Web v12 Residual Research — R5 / Loop 97

```yaml
scheduled_round: R5
scheduled_loop: 97
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE

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
beauty_brand_case_count: 3
global_channel_reorder_case_count: 2
dutyfree_china_us_channel_case_count: 2
late_chase_case_count: 1
global_channel_margin_bridge_missing_count: 1
row_presence_or_old_corporate_action_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 97
next_round: R6
next_loop: 97
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_97_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 97
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage:

```text
loop93: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop94: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop95: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop96: C19_BRAND_RETAIL_INVENTORY_MARGIN
```

This run returns to C20 after the R5 branch cycle, but avoids the C20 top-covered names and uses a different fine branch:

```text
K-beauty brand / duty-free / China-US-global channel reorder
sell-through, channel inventory, marketing cost, revenue, and margin bridge
vs generic beauty-label late chase
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
018250 애경산업
051900 LG생활건강
090430 아모레퍼시픽
```

They avoid the C20 top-covered list and recent R5 loop94~96 names:

```text
loop94 C20 avoid: 003230, 271560, 017810
loop95 C18 avoid: 111770, 081660, 007980
loop96 C19 avoid: 023530, 069960, 031430
C20 top-covered avoid: 226320, 161890, 192820, 214420, 241710, 439090
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
018250: same archetype, new symbol, K-beauty / household-care brand global-channel positive with Green cap
051900: same archetype, new symbol, premium beauty / global distribution positive with channel-margin refresh cap
090430: same archetype, new symbol, K-beauty global-channel late-chase hard-4C after rerating outran sell-through and margin evidence
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
018250 애경산업
  profile: atlas/symbol_profiles/018/018250.json
  first_date: 2018-03-22
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,942
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

051900 LG생활건강
  profile: atlas/symbol_profiles/051/051900.json
  first_date: 2001-04-25
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 6,125
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

090430 아모레퍼시픽
  profile: atlas/symbol_profiles/090/090430.json
  first_date: 2006-06-29
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,834
  non_tradable_zero_volume rows: 10
  corporate_action_candidate_dates:
    2015-05-08
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidate is outside the selected 2024 validation window.
```

---

## 4. Archetype residual problem

C20 is about beauty / food / global distribution. It is not a generic "beauty stock is hot" or "China consumer is back" archetype.

The model can over-score:

```text
K-beauty label
China reopening or duty-free recovery label
US / Japan / global channel expansion headline
brand relaunch or marketing campaign
online/offline distribution recovery
consumer export reorder label
one-week beauty-stock volume spike
late chase after a K-beauty rerating
```

The C20 bridge must be stricter:

```text
beauty / food / global-distribution event
  -> named geography, channel, platform, or distributor
  -> sell-through and reorder visibility
  -> channel inventory and discounting
  -> gross margin and mix
  -> marketing / promotion / logistics cost
  -> FX and local competition
  -> operating leverage
  -> revenue / OP conversion
  -> price survival after the first beauty-label spike
```

A C20 beauty thesis is like a shelf in a duty-free store. The headline says the product is visible, but equity value appears only when consumers actually buy it, the distributor reorders, channel inventory clears, and marketing/logistics cost does not eat the gross margin.

---

## 5. Case 1 — 018250 애경산업

```yaml
case_id: C20_R5L97_018250_2024_02_01
symbol: "018250"
name: "애경산업"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 16440
classification: positive_k_beauty_household_care_global_channel_sellthrough_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

애경산업 is the constructive C20 control in this set.

The useful C20 read is not simply:

```text
화장품 / 생활소비재가 움직였다
```

It is:

```text
K-beauty and household-care brand relevance
  -> channel recovery and reorder optionality
  -> sell-through and promotion discipline
  -> strong price confirmation into April/May
  -> controlled drawdown after the rerating
```

The forward path produced a meaningful MFE and the later drawdown remained controlled. This preserves positive classification. However, Green still requires fresh evidence of sell-through, channel inventory, marketing cost, and gross-margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 16,470 / close 16,440
2024-03-28: high 18,800 / close 18,250
2024-04-24: high 21,000 / close 21,000
2024-05-09: high 22,050 / close 20,200
2024-08-05: low 16,000 / close 17,510
2024-10-25: low 15,610 / close 15,670
2024-11-01: low 15,260 / close 15,310
```

Approximate path from entry close:

```text
entry_close: 16,440
peak_high: 22,050
MFE: +34.1%
worst_low_after_entry: 15,260
MAE: -7.2%
```

### Interpretation

This is a C20 positive with Green cap:

```text
Stage2-Actionable: possible if channel sell-through, reorder, inventory, and margin bridge are explicit.
Stage3-Green: blocked without fresh global-channel and gross-margin evidence.
Local 4B: monitor after +30% MFE if channel evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  k_beauty_household_brand_relevance: high
  channel_reorder_bridge: medium_high
  sellthrough_inventory_bridge: medium
  marketing_cost_bridge: medium
  margin_op_bridge: medium_high
  price_confirmation: high
  drawdown_penalty: low
  green_cap: yes
```

---

## 6. Case 2 — 051900 LG생활건강

```yaml
case_id: C20_R5L97_051900_2024_03_21
symbol: "051900"
name: "LG생활건강"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE
trigger_date: 2024-03-21
entry_date: 2024-03-21
entry_price_basis: close
entry_price: 376500
classification: capped_positive_premium_beauty_global_distribution_recovery_with_channel_margin_refresh_required
calibration_usable: true
```

### Evidence interpretation

LG생활건강 is the premium-beauty / global-distribution capped positive.

The setup had real C20 relevance:

```text
premium beauty and household-consumer brand
  -> China / duty-free / global channel recovery readthrough
  -> brand mix and margin optionality
  -> price confirmation into late April and early May
```

The forward path delivered a tradable MFE and the later drawdown did not cross a hard-failure zone. However, the move was still a rerating that required continuing proof: China/duty-free sell-through, channel inventory, brand mix, marketing spend, and margin conversion.

### Price path

Key Stock-Web rows:

```text
2024-03-21: high 377,000 / close 376,500
2024-04-01: high 408,000 / close 405,000
2024-04-30: high 420,000 / close 420,000
2024-05-08: high 440,000 / close 437,000
2024-08-05: low 321,000 / close 327,000
2024-09-27: high 391,500 / close 383,500
2024-10-31: low 326,000 / close 331,500
```

Approximate path from entry close:

```text
entry_close: 376,500
peak_high: 440,000
MFE: +16.9%
worst_low_after_entry: 321,000
MAE: -14.7%
```

### Interpretation

This is a capped positive:

```text
Stage2-Actionable: possible if duty-free/global-channel reorder and margin bridge are explicit.
Stage3-Green: blocked without fresh sell-through, channel inventory, brand mix, and promotion-cost evidence.
Local 4B: monitor because the rerating needed evidence refresh after May.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  premium_beauty_relevance: very_high
  china_dutyfree_global_channel_bridge: medium_high
  brand_mix_margin_bridge: medium
  marketing_cost_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: medium
  green_cap: yes
```

---

## 7. Case 3 — 090430 아모레퍼시픽

```yaml
case_id: C20_R5L97_090430_2024_05_31
symbol: "090430"
name: "아모레퍼시픽"
canonical_archetype_id: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
fine_archetype_id: K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE
trigger_date: 2024-05-31
entry_date: 2024-05-31
entry_price_basis: close
entry_price: 194200
classification: hard_4c_candidate_k_beauty_global_channel_late_chase_without_sellthrough_margin_survival
calibration_usable: true
```

### Evidence interpretation

아모레퍼시픽 is the late-chase C20 guardrail.

The label was high quality:

```text
K-beauty flagship brand
China / duty-free / global distribution recovery
brand and channel normalization
large-cap consumer quality
```

But from the selected late-May entry after a major rerating, the forward path did not validate incremental sell-through and margin survival. The same C20 label that was valuable early became dangerous when the entry was late and evidence was stale.

### Price path

Key Stock-Web rows:

```text
2024-05-31: high 200,500 / close 194,200
2024-06-12: high 194,100 / close 191,700
2024-07-24: high 185,000 / close 179,000
2024-08-05: low 152,100 / close 159,700
2024-08-13: low 115,900 / close 116,900
2024-10-25: low 117,000 / close 117,300
2024-10-31: low 114,600 / close 116,600
```

Approximate path from late entry close:

```text
entry_close: 194,200
peak_high_after_entry: 200,500
MFE: +3.2%
worst_low_after_entry: 114,600
MAE: -41.0%
```

### Interpretation

This is a hard C20 false-positive:

```text
Stage2-Watch: possible from K-beauty and global-channel relevance.
Stage2-Actionable: blocked unless sell-through, reorder, channel inventory, marketing cost, and margin bridge are explicit.
Stage3-Green: blocked from the selected late entry.
Hard 4C: yes by shallow MFE and high MAE.
Old corporate-action caveat: outside selected 2024 validation window.
```

The lesson is that a high-quality K-beauty label can become a late-chase trap when distribution and margin evidence stops refreshing.

### Stress-test components

```text
raw_component_score_proxy:
  k_beauty_flagship_label: very_high
  china_dutyfree_channel_recovery: high
  incremental_sellthrough_bridge: weak_from_late_entry
  channel_inventory_bridge: weak
  promotion_margin_bridge: weak_to_medium
  price_confirmation_after_entry: shallow
  drawdown_penalty: high
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
beauty_brand_case_count: 3
global_channel_reorder_case_count: 2
dutyfree_china_us_channel_case_count: 2
late_chase_case_count: 1
global_channel_margin_bridge_missing_count: 1
row_presence_or_old_corporate_action_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C20 beauty/global-channel grid:

```text
018250 애경산업:
  K-beauty / household-care positive;
  strong MFE and controlled MAE, but Green requires fresh sell-through and margin evidence.

051900 LG생활건강:
  premium beauty / global channel capped positive;
  meaningful MFE and moderate MAE, but needs channel inventory and brand-mix margin refresh.

090430 아모레퍼시픽:
  K-beauty late chase failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C20 is not "K-beauty label is strong."
C20 is "global channel demand becomes sell-through, sell-through becomes reorder, inventory clears, marketing and logistics costs are controlled, and gross margin reaches OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C20_R5L97_018250_2024_02_01","scheduled_round":"R5","scheduled_loop":97,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE","symbol":"018250","name":"애경산업","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":16440,"peak_high":22050,"peak_date":"2024-05-09","worst_low_after_entry":15260,"worst_low_after_entry_date":"2024-11-01","mfe_pct":34.1,"mae_pct":-7.2,"classification":"positive_k_beauty_household_care_global_channel_sellthrough_margin_bridge_with_green_cap","calibration_usable":true,"evidence_family":"k_beauty_household_care_channel_reorder_sellthrough_promotion_margin_bridge","residual_error":"positive_beauty_channel_path_still_requires_green_cap_without_refreshed_sellthrough_inventory_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_sellthrough_reorder_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C20_R5L97_051900_2024_03_21","scheduled_round":"R5","scheduled_loop":97,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE","symbol":"051900","name":"LG생활건강","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":376500,"peak_high":440000,"peak_date":"2024-05-08","worst_low_after_entry":321000,"worst_low_after_entry_date":"2024-08-05","mfe_pct":16.9,"mae_pct":-14.7,"classification":"capped_positive_premium_beauty_global_distribution_recovery_with_channel_margin_refresh_required","calibration_usable":true,"evidence_family":"premium_beauty_global_distribution_dutyfree_channel_brand_mix_margin_bridge","residual_error":"premium_beauty_rerating_requires_channel_inventory_brand_mix_and_margin_refresh_before_green","shadow_rule_candidate":"preserve_premium_beauty_positive_but_cap_green_when_channel_margin_evidence_is_stale"}
{"row_type":"case","case_id":"C20_R5L97_090430_2024_05_31","scheduled_round":"R5","scheduled_loop":97,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE","symbol":"090430","name":"아모레퍼시픽","trigger_date":"2024-05-31","entry_date":"2024-05-31","entry_price":194200,"peak_high":200500,"peak_date":"2024-05-31","worst_low_after_entry":114600,"worst_low_after_entry_date":"2024-10-31","mfe_pct":3.2,"mae_pct":-41.0,"classification":"hard_4c_candidate_k_beauty_global_channel_late_chase_without_sellthrough_margin_survival","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"k_beauty_flagship_global_channel_late_chase_without_incremental_sellthrough_inventory_margin_bridge","residual_error":"high_quality_k_beauty_label_can_fail_when_late_entry_lacks_fresh_channel_and_margin_evidence","shadow_rule_candidate":"route_k_beauty_global_channel_late_chase_to_hard_4c_if_mfe_shallow_mae_large_and_sellthrough_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":97,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","fine_archetype_id":"K_BEAUTY_BRAND_DUTYFREE_GLOBAL_CHANNEL_REORDER_REVENUE_MARGIN_BRIDGE_VS_BEAUTY_LABEL_LATE_CHASE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"beauty_brand_case_count":3,"global_channel_reorder_case_count":2,"dutyfree_china_us_channel_case_count":2,"late_chase_case_count":1,"global_channel_margin_bridge_missing_count":1,"row_presence_or_old_corporate_action_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":97,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","rule_id":"C20_GLOBAL_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C20 beauty/food/global-distribution cases, do not open Stage2-Actionable or Stage3-Green from K-beauty, China reopening, duty-free recovery, US/Japan/global channel expansion, brand relaunch, marketing campaign, online/offline distribution recovery, consumer export reorder, one-week beauty-stock spike, or late chase after K-beauty rerating labels alone. Require named geography/channel/platform/distributor, sell-through and reorder visibility, channel inventory and discounting check, gross-margin and mix improvement, marketing/promotion/logistics cost control, FX and local competition check, operating leverage, revenue/OP conversion, and post-trigger price survival. Beauty positives with large MFE and controlled MAE may be capped Actionable when sell-through and margin bridge are explicit, but Green requires fresh evidence. Premium beauty reratings should cap Green when channel inventory and brand-mix margin evidence is stale. K-beauty late chases with shallow MFE and high MAE should route to hard-4C when incremental sell-through and margin bridge are missing.","expected_effect":"Preserve true K-beauty/global-channel positives while reducing beauty-label and late-chase false positives where sell-through, reorder, inventory, promotion cost, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":97,"canonical_archetype_id":"C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION","residual_type":"global_channel_sellthrough_reorder_margin_guard","contribution":"Adds two beauty/global-channel positives and one K-beauty late-chase hard-4C counterexample to calibrate C20 sell-through, reorder, channel inventory, marketing/logistics cost, brand mix, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C20_GLOBAL_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION:

  Do not open Stage3-Green from:
    - K-beauty label alone
    - China reopening or duty-free recovery label alone
    - US / Japan / global channel expansion headline alone
    - brand relaunch or marketing campaign alone
    - online/offline distribution recovery alone
    - consumer export reorder label alone
    - one-week beauty-stock volume spike alone
    - late chase after a K-beauty rerating alone

  Require at least two of:
    - named geography / channel / platform / distributor
    - sell-through and reorder visibility
    - channel inventory and discounting control
    - gross margin and mix improvement
    - marketing / promotion / logistics-cost containment
    - FX and local competition check
    - operating leverage
    - revenue / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the beauty/global-channel headline

  If MFE < 8% and MAE < -35%:
    route to C20 hard-4C candidate.

  If MFE > 15% but channel evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If the case is a late chase after large prior rerating:
    require incremental sell-through and margin evidence before Actionable.

  Distinguish:
    - brands where global visibility becomes sell-through, reorder, inventory clearance, and margin
    - from beauty labels where channel inventory, promotion, FX, or local competition breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_97_L5_CONSUMER_BRAND_DISTRIBUTION_C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C20 beauty/global-distribution cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C20_GLOBAL_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C20 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C20 cases agree, consider implementing a canonical guard that:
   - blocks beauty/global-channel Green without geography/channel/distributor, sell-through, reorder, inventory, and margin bridge,
   - preserves K-beauty positives only with price survival and fresh channel evidence,
   - caps premium beauty reratings when channel inventory and brand-mix margin evidence is stale,
   - routes shallow-MFE/high-MAE K-beauty late chases to hard-4C,
   - applies row-presence / old corporate-action caveats when needed.

Expected next schedule:
completed_round = R5
completed_loop = 97
next_round = R6
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 97
next_round = R6
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```
