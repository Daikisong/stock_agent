# E2R Stock-Web v12 Residual Research — R5 / Loop 98

```yaml
scheduled_round: R5
scheduled_loop: 98
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE

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
k_food_export_case_count: 2
instant_noodle_export_case_count: 1
icecream_dairy_export_case_count: 1
health_food_online_channel_case_count: 1
channel_reorder_sellthrough_bridge_missing_count: 1
margin_promotion_logistics_bridge_missing_count: 1
large_mfe_green_cap_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
channel_inventory_or_promotion_cost_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 98
next_round: R6
next_loop: 98
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_98_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 98
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage:

```text
loop94: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop95: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop96: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop97: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

This run returns to C18 after the R5 branch cycle.

Selected fine branch:

```text
K-food / instant noodle / ice cream / health-food online channel
global distributor reorder, sell-through, channel inventory, promotion/logistics cost,
FX, gross margin, and OP bridge
vs generic consumer-export label spike
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

Selected symbols:

```text
004370 농심
005180 빙그레
290720 푸드나무
```

They avoid the C18 top-covered list and recent R5 branch names:

```text
loop97 C20 avoid:
  018250, 051900, 090430

loop96 C19 avoid:
  023530, 069960, 031430

loop95 C18 avoid:
  111770, 081660, 007980

loop94 C20 avoid:
  003230, 271560, 017810

C18 top-covered avoid:
  001680, 280360, 049770, 271560, 003960
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
004370: same archetype, new symbol, K-food instant-noodle export/channel reorder positive with Green cap
005180: same archetype, new symbol, ice-cream/dairy export-channel positive with very large MFE and later 4B/Green cap
290720: same archetype, new symbol, health-food online consumer-channel label hard-4C after shallow MFE and severe MAE
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
004370 농심
  profile: atlas/symbol_profiles/004/004370.json
  name history:
    농심 plus old formatted name "농    심"
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,742
  non_tradable_zero_volume rows: 22
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1997-05-08, 1997-07-21, 2000-07-28, 2003-07-18
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity / row-presence caveats exist outside selected 2024 validation window.

005180 빙그레
  profile: atlas/symbol_profiles/005/005180.json
  name history:
    빙그레 plus old formatted name "빙 그 레"
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,764
  non_tradable_zero_volume rows: 0
  invalid_zero_ohlc rows: 1
  corporate_action_candidate_dates:
    1995-09-29, 1996-09-25, 1998-12-15
  2024 entry~D+180 contamination: none
  caveat:
    old raw-discontinuity caveats are outside selected 2024 validation window.

290720 푸드나무
  profile: atlas/symbol_profiles/290/290720.json
  first_date: 2018-10-04
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,812
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2022-12-29, 2023-01-27, 2024-12-30
  selected 2024 entry~D+180 contamination: none
  caveat:
    2024-12-30 candidate is outside the selected first-half validation window.
```

---

## 4. Archetype residual problem

C18 is about consumer export channel reorder. It is not a generic "K-food / consumer export label is hot" archetype.

The model can over-score:

```text
K-food / instant noodle / ice cream / snack / health-food label
overseas channel expansion headline
US / China / Southeast Asia / global distribution readthrough
export sales growth headline
online channel or D2C platform label
reorder or distributor restocking rumor
one-week consumer-export stock volume spike
late chase after a consumer-export rerating
```

The C18 bridge must be stricter:

```text
consumer export / channel reorder event
  -> named product, geography, retailer, platform, or distributor
  -> sell-through and reorder visibility
  -> channel inventory and shipment timing
  -> ASP / mix / FX
  -> raw material, packaging, freight, and promotion cost
  -> distributor margin and local competition
  -> revenue recognition and cash collection
  -> gross margin / OP conversion
  -> price survival after the first export-label spike
```

A C18 consumer-export thesis is like a box of ramen or ice cream entering a foreign retail shelf. The headline says the product is on the shelf, but equity value appears only when consumers buy it, the distributor reorders, inventory clears, promotion and freight do not eat the margin, and the next shipment leaves cash behind.

---

## 5. Case 1 — 004370 농심

```yaml
case_id: C18_R5L98_004370_2024_02_01
symbol: "004370"
name: "농심"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 375000
classification: positive_k_food_instant_noodle_export_channel_reorder_sellthrough_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

농심 is the constructive K-food export-channel control.

The useful C18 read is not simply:

```text
K-food / 라면 수출주가 강하다
```

It is:

```text
instant-noodle brand with global channel relevance
  -> overseas sell-through and distributor reorder optionality
  -> shipment mix / FX / gross-margin bridge
  -> large May-June price confirmation
  -> Green cap after the rerating
```

The forward path produced a large MFE with controlled drawdown. This supports positive classification. However, after a large export rerating, C18 Green should remain capped unless sell-through, reorder, channel inventory, freight/promotion cost, and margin evidence are refreshed.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 378,000 / close 375,000
2024-04-25: high 402,000 / close 399,500
2024-05-28: high 474,500 / close 469,000
2024-06-10: high 541,000 / close 528,000
2024-06-13: high 599,000 / close 547,000
2024-08-05: low 433,000 / close 444,000
2024-10-25: low 356,000 / close 358,000
```

Approximate path from entry close:

```text
entry_close: 375,000
peak_high: 599,000
MFE: +59.7%
worst_low_after_entry: 347,500
MAE: -7.3%
```

### Interpretation

This is a C18 positive with Green cap:

```text
Stage2-Actionable: possible if geography/channel sell-through, reorder, shipment, and margin bridge are explicit.
Stage3-Green: blocked after +50% MFE unless fresh channel inventory and margin evidence appears.
Local 4B: monitor if export-label price outruns reorder evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  k_food_brand_relevance: very_high
  overseas_channel_bridge: high
  sellthrough_reorder_bridge: medium_high
  fx_mix_bridge: medium
  freight_promotion_cost_bridge: medium
  margin_op_bridge: medium_high
  price_confirmation: very_high
  drawdown_penalty: low
  green_cap: required_after_large_mfe
```

---

## 6. Case 2 — 005180 빙그레

```yaml
case_id: C18_R5L98_005180_2024_02_01
symbol: "005180"
name: "빙그레"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 52700
classification: positive_icecream_dairy_k_food_export_channel_reorder_with_4b_green_cap_after_very_large_mfe
calibration_usable: true
```

### Evidence interpretation

빙그레 is the ice-cream / dairy K-food export positive.

The setup had strong C18 relevance:

```text
ice-cream and dairy consumer brand
  -> overseas channel and K-food export readthrough
  -> sell-through and distributor reorder optionality
  -> very large May-June price confirmation
```

The price path validated the export-channel rerating with a very large MFE. But the subsequent giveback from the June peak proves that the model must not leave the name as unrestricted Green after the rerating. It needs current evidence on reorder, channel inventory, seasonality, promotion cost, freight, FX, and margin.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 53,800 / close 52,700
2024-04-22: high 69,600 / close 69,300
2024-05-17: high 94,400 / close 88,300
2024-05-22: high 97,700 / close 92,700
2024-06-10: high 115,500 / close 112,100
2024-06-11: high 118,400 / close 109,000
2024-08-05: low 73,600 / close 77,100
2024-09-09: low 59,200 / close 62,300
```

Approximate path from entry close:

```text
entry_close: 52,700
peak_high: 118,400
MFE: +124.7%
worst_low_after_entry: 52,000
MAE: -1.3%
```

### Interpretation

This is a very strong C18 positive with 4B/Green cap:

```text
Stage2-Actionable: valid if overseas channel, sell-through, distributor reorder, seasonality, and margin bridge are explicit.
Stage3-Green: blocked after +100% MFE unless fresh reorder and gross-margin evidence appears.
Local 4B: required if price outruns channel evidence or if post-peak giveback accelerates.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  icecream_dairy_export_relevance: high
  global_channel_bridge: high
  reorder_sellthrough_bridge: medium_high
  seasonality_inventory_bridge: medium
  promotion_freight_cost_bridge: medium
  price_confirmation: extreme
  valuation_overheat_risk: high
  green_cap: required_after_extreme_mfe
```

---

## 7. Case 3 — 290720 푸드나무

```yaml
case_id: C18_R5L98_290720_2024_02_01
symbol: "290720"
name: "푸드나무"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 8000
classification: hard_4c_candidate_health_food_online_channel_label_without_reorder_margin_survival
calibration_usable: true
```

### Evidence interpretation

푸드나무 is the consumer online-channel hard C18 guardrail.

The label can fool the model:

```text
health-food / diet-food brand
online channel / D2C consumer platform
consumer channel recovery or reorder hope
small-cap food-channel beta
```

But from the selected February entry, the forward path produced almost no MFE and then entered a severe drawdown. The bridge from channel label to sell-through, repeat purchase, reorder, inventory, freight/promotion cost, cash collection, and margin was not proven. Later July/August event-like spikes should be treated as new event windows, not a rescue of the first trigger.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 8,000 / close 8,000
2024-02-05: high 8,050 / close 7,960
2024-03-19: low 6,520 / close 6,610
2024-04-17: low 5,290 / close 5,340
2024-07-30: high 4,210 / low 2,490 / close 4,005
2024-09-24: low 2,900 / close 3,095
2024-10-25: low 3,190 / close 3,280
```

Approximate path from entry close:

```text
entry_close: 8,000
peak_high_first_phase: 8,050
MFE: +0.6%
worst_low_after_entry: 2,490
MAE: -68.9%
```

### Interpretation

This is a hard C18 false-positive:

```text
Stage2-Watch: possible from health-food and online-channel relevance.
Stage2-Actionable: blocked unless repeat purchase, sell-through, reorder, inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and severe MAE.
Event-window caveat: later July/August spikes are new event windows, not validation of the February trigger.
```

The lesson is that an online food-channel label is not reorder-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  health_food_online_channel_label: high
  export_or_reorder_bridge: weak
  repeat_purchase_bridge: weak
  inventory_freight_promotion_bridge: weak
  margin_cashflow_bridge: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: extreme
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
k_food_export_case_count: 2
instant_noodle_export_case_count: 1
icecream_dairy_export_case_count: 1
health_food_online_channel_case_count: 1
channel_reorder_sellthrough_bridge_missing_count: 1
margin_promotion_logistics_bridge_missing_count: 1
large_mfe_green_cap_count: 2
row_presence_or_old_corporate_action_caveat_count: 3
channel_inventory_or_promotion_cost_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C18 consumer export-channel grid:

```text
004370 농심:
  instant-noodle / K-food export-channel positive;
  large MFE and controlled MAE, but Green requires fresh sell-through/reorder/margin evidence.

005180 빙그레:
  ice-cream / dairy export-channel positive;
  extreme MFE, but 4B/Green cap required after post-peak giveback risk.

290720 푸드나무:
  health-food online-channel label failed;
  shallow MFE and severe MAE, hard 4C candidate.
```

Shared rule:

```text
C18 is not "K-food or consumer channel label is hot."
C18 is "sell-through becomes distributor reorder, channel inventory clears, promotion/freight/raw-material cost is controlled, and gross margin reaches OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C18_R5L98_004370_2024_02_01","scheduled_round":"R5","scheduled_loop":98,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE","symbol":"004370","name":"농심","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":375000,"peak_high":599000,"peak_date":"2024-06-13","worst_low_after_entry":347500,"worst_low_after_entry_date":"2024-02-29","mfe_pct":59.7,"mae_pct":-7.3,"classification":"positive_k_food_instant_noodle_export_channel_reorder_sellthrough_margin_bridge_with_green_cap","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"k_food_instant_noodle_overseas_channel_sellthrough_distributor_reorder_fx_mix_margin_bridge","residual_error":"positive_k_food_export_path_requires_green_cap_after_large_mfe_without_refreshed_channel_inventory_reorder_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_sellthrough_reorder_and_margin_bridge_confirm_but_cap_green_after_large_mfe"}
{"row_type":"case","case_id":"C18_R5L98_005180_2024_02_01","scheduled_round":"R5","scheduled_loop":98,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE","symbol":"005180","name":"빙그레","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":52700,"peak_high":118400,"peak_date":"2024-06-11","worst_low_after_entry":52000,"worst_low_after_entry_date":"2024-02-01","mfe_pct":124.7,"mae_pct":-1.3,"classification":"positive_icecream_dairy_k_food_export_channel_reorder_with_4b_green_cap_after_very_large_mfe","calibration_usable":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"icecream_dairy_k_food_global_channel_sellthrough_distributor_reorder_seasonality_promotion_margin_bridge","residual_error":"extreme_consumer_export_rerating_requires_4b_green_cap_when_channel_reorder_and_margin_evidence_not_refreshed","shadow_rule_candidate":"preserve_icecream_dairy_export_positive_but_attach_green_cap_after_extreme_mfe_without_fresh_reorder_margin_evidence"}
{"row_type":"case","case_id":"C18_R5L98_290720_2024_02_01","scheduled_round":"R5","scheduled_loop":98,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE","symbol":"290720","name":"푸드나무","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":8000,"peak_high_first_phase":8050,"peak_date":"2024-02-05","worst_low_after_entry":2490,"worst_low_after_entry_date":"2024-07-30","mfe_pct":0.6,"mae_pct":-68.9,"classification":"hard_4c_candidate_health_food_online_channel_label_without_reorder_margin_survival","calibration_usable":true,"event_window_separation_required":true,"row_presence_or_old_corporate_action_caveat":true,"evidence_family":"health_food_online_consumer_channel_label_without_repeat_purchase_sellthrough_reorder_inventory_margin_bridge","residual_error":"online_food_channel_label_can_fail_when_repeat_purchase_reorder_and_margin_bridge_missing","shadow_rule_candidate":"route_health_food_online_channel_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_reorder_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":98,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"K_FOOD_INSTANT_NOODLE_ICECREAM_HEALTH_FOOD_EXPORT_CHANNEL_REORDER_SELLTHROUGH_MARGIN_BRIDGE_VS_CONSUMER_EXPORT_LABEL_SPIKE","case_count":3,"positive_case_count":2,"counterexample_count":1,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"k_food_export_case_count":2,"instant_noodle_export_case_count":1,"icecream_dairy_export_case_count":1,"health_food_online_channel_case_count":1,"channel_reorder_sellthrough_bridge_missing_count":1,"margin_promotion_logistics_bridge_missing_count":1,"large_mfe_green_cap_count":2,"row_presence_or_old_corporate_action_caveat_count":3,"channel_inventory_or_promotion_cost_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":98,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","rule_id":"C18_EXPORT_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C18 consumer export/channel-reorder cases, do not open Stage2-Actionable or Stage3-Green from K-food, instant noodle, ice cream, snack, health-food, overseas channel expansion, US/China/Southeast Asia/global distribution, export sales growth, online channel/D2C platform, reorder/restocking rumor, one-week consumer-export stock spike, or late chase after consumer-export rerating labels alone. Require named product/geography/retailer/platform/distributor, sell-through and reorder visibility, channel inventory and shipment timing, ASP/mix/FX, raw-material/packaging/freight/promotion cost control, distributor margin and local competition check, revenue recognition and cash collection, gross-margin/OP conversion, and post-trigger price survival. K-food positives with large MFE may be capped Actionable when sell-through/reorder/margin bridge is explicit, but Green requires fresh evidence. Extreme ice-cream/dairy export reratings should attach 4B/Green cap when channel evidence is stale. Health-food/online-channel labels with shallow MFE and extreme MAE should route to hard-4C when repeat purchase, reorder, and margin bridge are missing, with later event windows separated from earlier failed triggers.","expected_effect":"Preserve true K-food export-channel positives while reducing consumer-export, online-channel, and reorder-label false positives where sell-through, channel inventory, freight/promotion cost, repeat purchase, and margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":98,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"export_channel_sellthrough_reorder_margin_guard","contribution":"Adds one instant-noodle export positive, one ice-cream/dairy export positive with 4B/Green cap, and one health-food online-channel hard-4C counterexample to calibrate C18 sell-through, reorder, inventory, promotion/freight cost, FX/mix, repeat purchase, and gross-margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C18_EXPORT_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER:

  Do not open Stage3-Green from:
    - K-food / instant noodle / ice cream / snack / health-food label alone
    - overseas channel expansion headline alone
    - US / China / Southeast Asia / global distribution readthrough alone
    - export sales growth headline alone
    - online channel / D2C platform label alone
    - reorder or distributor restocking rumor alone
    - one-week consumer-export stock volume spike alone
    - late chase after consumer-export rerating alone

  Require at least two of:
    - named product / geography / retailer / platform / distributor
    - sell-through and reorder visibility
    - channel inventory and shipment timing
    - ASP / mix / FX
    - raw-material / packaging / freight / promotion cost containment
    - distributor margin and local competition check
    - revenue recognition and cash collection
    - gross margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the consumer-export headline

  If MFE < 8% and MAE < -35%:
    route to C18 hard-4C candidate.

  If MFE > 30% but channel evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If MFE is extreme and post-peak giveback appears:
    attach 4B until distributor reorder and margin evidence refreshes.

  If later event-like spikes appear after severe first-phase failure:
    create a new event window; do not retroactively validate the earlier failed trigger.

  Distinguish:
    - products where shelf visibility becomes sell-through, reorder, shipment, cash collection, and margin
    - from export/channel labels where inventory, promotion, freight, or weak repeat purchase breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_98_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C18 consumer export/channel-reorder cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C18_EXPORT_CHANNEL_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C18 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C18 cases agree, consider implementing a canonical guard that:
   - blocks consumer-export Green without named product/geography/channel/distributor, sell-through, reorder, inventory, and margin bridge,
   - preserves K-food positives only with price survival and fresh reorder evidence,
   - caps extreme MFE ice-cream/dairy export reratings until channel and margin evidence refreshes,
   - routes shallow-MFE/extreme-MAE health-food online-channel labels to hard-4C,
   - separates later event windows from earlier failed online-channel triggers,
   - applies old corporate-action and row-presence caveats when needed.

Expected next schedule:
completed_round = R5
completed_loop = 98
next_round = R6
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 98
next_round = R6
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```
