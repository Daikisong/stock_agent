# E2R Stock-Web v12 Residual Research — R5 / Loop 99

```yaml
scheduled_round: R5
scheduled_loop: 99
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE

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
hard_4c_candidate_count: 2
apparel_footwear_oem_case_count: 1
premium_brand_inventory_case_count: 1
outdoor_lifestyle_brand_case_count: 1
sellthrough_reorder_bridge_missing_count: 2
inventory_promotion_discount_bridge_missing_count: 2
gross_margin_op_bridge_missing_count: 2
short_listing_or_old_corporate_action_caveat_count: 3
channel_inventory_cost_caveat_count: 3
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 99
next_round: R6
next_loop: 99
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_99_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 99
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 is the consumer / brand / distribution round. The selected canonical archetype is:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
```

Recent R5 branch usage:

```text
loop95: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop96: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop97: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop98: C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

This run returns to C19 after the R5 branch cycle.

Selected fine branch:

```text
apparel / footwear OEM / outdoor lifestyle brand / premium fashion brand
sell-through, channel inventory, wholesale vs DTC mix, reorder, promotion and discount cost,
freight / FX / raw-material cost, working capital, and gross-margin / OP bridge
vs generic brand-retail inventory recovery label spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN
rows: 38
symbols: 13
date_range: 2022-02-11~2024-09-27
good/bad S2: 8/9
4B/4C: 3/0
URL pending/proxy: 23/17
top covered symbols:
  282330(9), 004170(4), 007070(4), 093050(4), 337930(4), 139480(3)
```

Selected symbols:

```text
241590 화승엔터프라이즈
383220 F&F
298540 더네이쳐홀딩스
```

They avoid the C19 top-covered list and recent R5 names:

```text
C19 top-covered avoid:
  282330, 004170, 007070, 093050, 337930, 139480

recent R5 avoid:
  loop98 C18: 004370, 005180, 290720
  loop97 C20: 018250, 051900, 090430
  loop96 C19: 023530, 069960, 031430
  loop95 C18: 111770, 081660, 007980
  loop94 C20: 003230, 271560, 017810
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
241590: same archetype, new symbol, footwear OEM / global brand channel recovery positive with Green cap.
383220: same archetype, new symbol, premium apparel brand inventory / China-DTC mix hard-4C candidate after moderate MFE and high MAE.
298540: same archetype, new symbol, outdoor lifestyle brand label hard-4C candidate after shallow MFE and severe inventory-margin drawdown.
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
241590 화승엔터프라이즈
  profile: atlas/symbol_profiles/241/241590.json
  first_date: 2016-10-04
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,302
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2018-06-08, 2018-07-02
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.

383220 F&F
  profile: atlas/symbol_profiles/383/383220.json
  first_date: 2021-05-21
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 1,161
  non_tradable_zero_volume rows: 3
  corporate_action_candidate_dates:
    2022-04-13
  2024 entry~D+180 contamination: none
  caveat:
    short post-spinoff listing history and old corporate-action candidate outside selected 2024 validation window.

298540 더네이쳐홀딩스
  profile: atlas/symbol_profiles/298/298540.json
  first_date: 2020-07-27
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 1,365
  non_tradable_zero_volume rows: 0
  corporate_action_candidate_dates:
    2021-08-02, 2021-08-30
  2024 entry~D+180 contamination: none
  caveat:
    old corporate-action candidates are outside selected 2024 validation window.
```

---

## 4. Archetype residual problem

C19 is about brand / retail / inventory / margin. It is not a generic "consumer brand is recovering" archetype.

The model can over-score:

```text
apparel / sportswear / outdoor brand label
footwear OEM or global brand channel label
China / DTC / wholesale recovery story
brand premium or lifestyle IP label
retail reopening or channel restocking rumor
inventory normalization headline
discount / promotion easing headline
one-week brand-retail stock volume spike
late chase after a brand rerating
```

The C19 bridge must be stricter:

```text
brand / retail / inventory event
  -> named brand, customer, geography, channel, or SKU group
  -> sell-through and reorder visibility
  -> channel inventory and shipment timing
  -> wholesale vs DTC / online / outlet channel mix
  -> ASP / mix / FX
  -> raw material, freight, labor, rent, and promotion / discount cost
  -> inventory write-down and working-capital timing
  -> distributor / franchisee / OEM customer margin check
  -> gross margin / OP conversion
  -> price survival after the first brand-retail spike
```

A C19 thesis is like a warehouse full of shoes and outerwear. A brand headline opens the warehouse door, but equity value appears only when the product sells through, the channel reorders, stale inventory clears without deep discounting, freight and promotion do not eat the spread, and gross margin falls through to OP.

---

## 5. Case 1 — 241590 화승엔터프라이즈

```yaml
case_id: C19_R5L99_241590_2024_02_01
symbol: "241590"
name: "화승엔터프라이즈"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 7420
classification: positive_footwear_oem_global_brand_channel_inventory_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

화승엔터프라이즈 is the constructive C19 positive in this set.

The useful C19 read is not simply:

```text
의류 / 신발 OEM주가 강하다
```

It is:

```text
footwear OEM and global brand customer channel recovery
  -> sell-through and reorder optionality
  -> customer inventory normalization
  -> utilization and labor / freight cost bridge
  -> April and October price confirmation
```

The forward path produced meaningful MFE and did not enter a hard-failure zone. This preserves positive classification. However, Green should remain capped unless sell-through, reorder, customer inventory, utilization, cost pass-through, and OP margin evidence are fresh.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 7,680 / low 7,350 / close 7,420
2024-03-08: low 6,580 / close 6,660
2024-04-18: high 9,400 / close 8,990
2024-04-30: high 9,550 / close 9,410
2024-08-05: low 6,930 / close 7,100
2024-09-27: high 8,480 / close 8,210
2024-10-16: high 9,510 / close 8,990
```

Approximate path from entry close:

```text
entry_close: 7,420
peak_high: 9,550
MFE: +28.7%
worst_low_after_entry: 6,580
MAE: -11.3%
```

### Interpretation

This is a C19 positive with Green cap:

```text
Stage2-Actionable: possible if global customer reorder, channel inventory, utilization, and margin bridge are explicit.
Stage3-Green: blocked after +25% MFE unless fresh sell-through / reorder / margin evidence appears.
Local 4B: monitor if price outruns inventory normalization evidence.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  footwear_oem_relevance: high
  global_brand_customer_bridge: medium_high
  sellthrough_reorder_bridge: medium
  inventory_normalization_bridge: medium
  labor_freight_cost_bridge: medium
  op_margin_bridge: medium
  price_confirmation: high
  drawdown_penalty: medium
  green_cap: required_after_mfe
```

---

## 6. Case 2 — 383220 F&F

```yaml
case_id: C19_R5L99_383220_2024_02_01
symbol: "383220"
name: "F&F"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 69400
classification: hard_4c_candidate_premium_apparel_brand_inventory_channel_margin_label_without_sellthrough_survival
calibration_usable: true
```

### Evidence interpretation

F&F is the premium apparel / brand-inventory hard C19 guardrail.

The label can fool the model:

```text
premium apparel / lifestyle brand
  -> China / DTC / wholesale channel recovery
  -> brand power and retail margin readthrough
  -> inventory normalization hope
```

The first half produced only moderate MFE and then the stock entered a hard drawdown zone in August. A later September/October rebound should be treated as a refreshed event window, not a rescue of the February trigger. The bridge from brand label to sell-through, channel inventory clearance, discount discipline, and OP margin was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 70,900 / low 68,700 / close 69,400
2024-04-01: high 77,400 / close 76,500
2024-05-03: high 73,500 / close 72,800
2024-08-05: low 47,150 / close 48,000
2024-09-27: high 71,900 / close 69,200
2024-10-02: high 72,100 / close 69,900
2024-10-25: low 57,000 / close 57,200
```

Approximate path from entry close:

```text
entry_close: 69,400
peak_high_first_phase: 77,400
MFE: +11.5%
worst_low_after_entry: 47,150
MAE: -32.1%
```

### Interpretation

This is a hard C19 false-positive candidate:

```text
Stage2-Watch: possible from premium brand and retail/channel relevance.
Stage2-Actionable: blocked unless sell-through, channel inventory, discount/promotion cost, and gross-margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by moderate MFE and -30%+ MAE.
Event-window separation: later September/October rebound should be separated.
```

The lesson is that a brand premium is not inventory-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  premium_apparel_brand_relevance: high
  china_dtc_wholesale_channel_signal: medium_high
  sellthrough_bridge: weak_to_medium
  channel_inventory_bridge: weak
  promotion_discount_bridge: weak
  gross_margin_op_bridge: weak_to_medium
  price_confirmation: moderate
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 298540 더네이쳐홀딩스

```yaml
case_id: C19_R5L99_298540_2024_02_01
symbol: "298540"
name: "더네이쳐홀딩스"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 15930
classification: hard_4c_candidate_outdoor_lifestyle_brand_label_without_channel_inventory_margin_survival
calibration_usable: true
```

### Evidence interpretation

더네이쳐홀딩스 is the outdoor lifestyle brand hard guardrail.

The label can fool the model:

```text
outdoor / lifestyle brand
  -> retail channel recovery hope
  -> inventory normalization and discount easing story
  -> international or licensing optionality
```

But from the selected February trigger, the forward path produced very shallow MFE and then a severe drawdown. The bridge from outdoor brand label to sell-through, reorder, channel inventory, promotion cost, gross margin, and OP was not proven.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 15,960 / close 15,930
2024-02-06: high 16,570 / close 16,030
2024-04-01: high 15,790 / close 15,780
2024-08-05: low 10,000 / close 10,920
2024-09-27: high 11,710 / close 11,680
2024-10-23: low 9,560 / close 10,090
```

Approximate path from entry close:

```text
entry_close: 15,930
peak_high: 16,570
MFE: +4.0%
worst_low_after_entry: 9,560
MAE: -40.0%
```

### Interpretation

This is a hard C19 false-positive candidate:

```text
Stage2-Watch: possible from outdoor / lifestyle brand relevance.
Stage2-Actionable: blocked unless sell-through, channel inventory, reorder, discount, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -40% MAE.
```

The lesson is that outdoor brand visibility is not channel-inventory margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  outdoor_lifestyle_brand_label: high
  channel_recovery_signal: medium
  sellthrough_reorder_bridge: weak
  inventory_clearance_bridge: weak
  promotion_discount_cost_bridge: weak
  gross_margin_op_bridge: weak
  price_confirmation: shallow
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
hard_4c_candidate_count: 2
apparel_footwear_oem_case_count: 1
premium_brand_inventory_case_count: 1
outdoor_lifestyle_brand_case_count: 1
sellthrough_reorder_bridge_missing_count: 2
inventory_promotion_discount_bridge_missing_count: 2
gross_margin_op_bridge_missing_count: 2
short_listing_or_old_corporate_action_caveat_count: 3
channel_inventory_cost_caveat_count: 3
calibration_usable_trigger_count: 3
```

The three-case C19 apparel / brand-inventory grid:

```text
241590 화승엔터프라이즈:
  footwear OEM / global brand customer channel positive;
  meaningful MFE and non-hard MAE, but Green requires fresh sell-through, reorder, inventory, and margin evidence.

383220 F&F:
  premium apparel brand label failed;
  moderate MFE and high MAE, hard 4C candidate.

298540 더네이쳐홀딩스:
  outdoor lifestyle brand label failed;
  shallow MFE and severe MAE, hard 4C candidate.
```

Shared rule:

```text
C19 is not "brand or retail label is recognizable."
C19 is "sell-through becomes reorder, channel inventory clears without excessive discounts, and gross margin reaches OP."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C19_R5L99_241590_2024_02_01","scheduled_round":"R5","scheduled_loop":99,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE","symbol":"241590","name":"화승엔터프라이즈","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":7420,"peak_high":9550,"peak_date":"2024-04-30","worst_low_after_entry":6580,"worst_low_after_entry_date":"2024-03-08","mfe_pct":28.7,"mae_pct":-11.3,"classification":"positive_footwear_oem_global_brand_channel_inventory_margin_bridge_with_green_cap","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"footwear_oem_global_brand_customer_sellthrough_reorder_inventory_utilization_labor_freight_margin_bridge","residual_error":"footwear_oem_channel_positive_requires_green_cap_without_refreshed_sellthrough_reorder_inventory_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_global_customer_reorder_inventory_and_margin_bridge_confirm_but_cap_green_after_mfe"}
{"row_type":"case","case_id":"C19_R5L99_383220_2024_02_01","scheduled_round":"R5","scheduled_loop":99,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE","symbol":"383220","name":"F&F","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":69400,"peak_high_first_phase":77400,"peak_date":"2024-04-01","worst_low_after_entry":47150,"worst_low_after_entry_date":"2024-08-05","mfe_pct":11.5,"mae_pct":-32.1,"classification":"hard_4c_candidate_premium_apparel_brand_inventory_channel_margin_label_without_sellthrough_survival","calibration_usable":true,"short_listing_or_old_corporate_action_caveat":true,"event_window_separation_required":true,"evidence_family":"premium_apparel_brand_china_dtc_wholesale_label_without_sellthrough_channel_inventory_discount_gross_margin_bridge","residual_error":"premium_brand_label_can_fail_when_inventory_and_discount_margin_bridge_missing","shadow_rule_candidate":"route_premium_apparel_brand_label_to_hard_4c_if_mfe_modest_mae_high_and_sellthrough_margin_bridge_missing"}
{"row_type":"case","case_id":"C19_R5L99_298540_2024_02_01","scheduled_round":"R5","scheduled_loop":99,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE","symbol":"298540","name":"더네이쳐홀딩스","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":15930,"peak_high":16570,"peak_date":"2024-02-06","worst_low_after_entry":9560,"worst_low_after_entry_date":"2024-10-23","mfe_pct":4.0,"mae_pct":-40.0,"classification":"hard_4c_candidate_outdoor_lifestyle_brand_label_without_channel_inventory_margin_survival","calibration_usable":true,"old_corporate_action_caveat_outside_window":true,"evidence_family":"outdoor_lifestyle_brand_label_without_sellthrough_reorder_channel_inventory_promotion_discount_gross_margin_bridge","residual_error":"outdoor_brand_label_can_fail_when_channel_inventory_and_margin_bridge_missing","shadow_rule_candidate":"route_outdoor_lifestyle_brand_label_to_hard_4c_if_mfe_shallow_mae_severe_and_inventory_margin_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":99,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_FOOTWEAR_OUTDOOR_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_PROMOTION_MARGIN_BRIDGE_VS_BRAND_RETAIL_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":2,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"apparel_footwear_oem_case_count":1,"premium_brand_inventory_case_count":1,"outdoor_lifestyle_brand_case_count":1,"sellthrough_reorder_bridge_missing_count":2,"inventory_promotion_discount_bridge_missing_count":2,"gross_margin_op_bridge_missing_count":2,"short_listing_or_old_corporate_action_caveat_count":3,"channel_inventory_cost_caveat_count":3,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":99,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","rule_id":"C19_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C19 brand/retail/inventory/margin cases, do not open Stage2-Actionable or Stage3-Green from apparel, sportswear, outdoor brand, footwear OEM, global brand customer channel, China/DTC/wholesale recovery, brand premium, lifestyle IP, retail reopening, channel restocking, inventory normalization, discount/promotion easing, one-week brand-retail volume spike, or late chase after brand rerating labels alone. Require named brand/customer/geography/channel/SKU group, sell-through and reorder visibility, channel inventory and shipment timing, wholesale vs DTC/online/outlet mix, ASP/mix/FX, raw-material/freight/labor/rent/promotion/discount cost containment, inventory write-down and working-capital timing, distributor/franchisee/OEM customer margin check, gross-margin/OP conversion, valuation discipline after the first brand spike, and post-trigger price survival. Footwear OEM positives with meaningful MFE may be capped Actionable when customer reorder, inventory normalization, utilization, and margin bridge are explicit, but Green requires fresh evidence. Premium apparel brand labels with modest MFE and high MAE should route to hard-4C when sell-through, channel inventory, discount, and gross-margin bridge are missing. Outdoor lifestyle brand labels with shallow MFE and severe MAE should route to hard-4C when channel inventory and margin bridge are missing.","expected_effect":"Preserve true footwear/apparel channel recovery positives while reducing generic brand, retail, outdoor, premium apparel, inventory-normalization, and channel-restocking false positives where sell-through, reorder, promotion/discount cost, working capital, and gross-margin evidence fail.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":99,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"brand_channel_inventory_sellthrough_margin_guard","contribution":"Adds one footwear OEM channel recovery positive and two apparel/outdoor brand hard-4C counterexamples to calibrate C19 sell-through, reorder, channel inventory, promotion/discount cost, working capital, and gross-margin/OP requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C19_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:

  Do not open Stage3-Green from:
    - apparel / sportswear / outdoor brand label alone
    - footwear OEM or global brand channel label alone
    - China / DTC / wholesale recovery story alone
    - brand premium or lifestyle IP label alone
    - retail reopening or channel restocking rumor alone
    - inventory normalization headline alone
    - discount / promotion easing headline alone
    - one-week brand-retail stock volume spike alone
    - late chase after brand rerating alone

  Require at least two of:
    - named brand / customer / geography / channel / SKU group
    - sell-through and reorder visibility
    - channel inventory and shipment timing
    - wholesale vs DTC / online / outlet channel mix
    - ASP / mix / FX
    - raw-material / freight / labor / rent / promotion / discount cost containment
    - inventory write-down and working-capital timing
    - distributor / franchisee / OEM customer margin check
    - gross margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the brand-retail headline

  If MFE < 8% and MAE <= -35%:
    route to C19 hard-4C candidate.

  If MFE < 15% and MAE <= -30%:
    route to C19 hard-4C if sell-through and margin bridge are missing.

  If MFE > 20% but channel inventory / margin evidence is stale:
    preserve as capped positive or local 4B, not Green.

  If later rebound appears after first-window failure:
    create a new event window; do not retroactively validate the failed first trigger.

  Distinguish:
    - brands/OEMs where sell-through becomes reorder, inventory clears, and margin reaches OP
    - from labels where channel inventory, discounting, freight, rent, or weak demand breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_99_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C19 brand/retail/inventory margin cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C19_BRAND_CHANNEL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C19 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C19 cases agree, consider implementing a canonical guard that:
   - blocks brand/retail Green without named brand/channel/SKU, sell-through, reorder, inventory, promotion/discount cost, and margin bridge,
   - preserves footwear OEM positives only with price survival and fresh reorder/inventory/margin evidence,
   - routes modest-MFE/high-MAE premium apparel brand labels to hard-4C,
   - routes shallow-MFE/severe-MAE outdoor lifestyle brand labels to hard-4C,
   - separates later rebounding event windows from failed first triggers,
   - applies short-listing, row-presence, and old corporate-action caveats.

Expected next schedule:
completed_round = R5
completed_loop = 99
next_round = R6
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 99
next_round = R6
next_loop = 99
round_schedule_status = valid
round_sector_consistency = pass
```
