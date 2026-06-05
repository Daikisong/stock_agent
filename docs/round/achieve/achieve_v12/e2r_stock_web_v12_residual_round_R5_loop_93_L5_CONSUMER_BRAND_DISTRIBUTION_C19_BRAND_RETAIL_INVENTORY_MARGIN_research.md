# E2R Stock-Web v12 Residual Research — R5 / Loop 93

```yaml
scheduled_round: R5
scheduled_loop: 93
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE

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
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 93
next_round: R6
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_93_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 93
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage already covered:

```text
loop89: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop90: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop91: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
loop92: C18_CONSUMER_EXPORT_CHANNEL_REORDER
```

This run returns to C19, but uses a different fine branch:

```text
apparel OEM / outdoor brand / brand inventory normalization margin bridge
vs brand-label restocking spike
```

This deliberately avoids the recent K-beauty export-channel and K-food distribution branches.

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
105630 한세실업
383220 F&F
298540 더네이쳐홀딩스
```

They avoid the C19 top-covered symbols and avoid recent R5 loop90~92 symbols:

```text
loop90 avoid: 257720, 090430, 051900
loop91 avoid: 004370, 097950, 007310
loop92 avoid: 352480, 018290, 002790
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
105630: same archetype, new symbol, apparel OEM inventory restocking / margin bridge local-positive branch
383220: same archetype, new symbol, premium apparel brand / China inventory margin false-positive branch
298540: same archetype, new symbol, outdoor/lifestyle brand inventory normalization failure branch
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
105630 한세실업
  profile: atlas/symbol_profiles/105/105630.json
  first_date: 2009-03-20
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,172
  corporate_action_candidate_dates:
    2011-11-30
  2024 entry~D+180 contamination: none

383220 F&F
  profile: atlas/symbol_profiles/383/383220.json
  first_date: 2021-05-21
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,161
  corporate_action_candidate_dates:
    2022-04-13
  2024 entry~D+180 contamination: none

298540 더네이쳐홀딩스
  profile: atlas/symbol_profiles/298/298540.json
  first_date: 2020-07-27
  last_date: 2026-02-20
  tradable_ohlcv rows: 1,365
  corporate_action_candidate_dates:
    2021-08-02, 2021-08-30
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C19 is about brand/retail inventory margin, not a generic consumer brand label.

The model can over-score:

```text
apparel brand popularity
outdoor / lifestyle brand label
China retail recovery
inventory normalization headline
OEM restocking hope
one-week brand-stock price spike
```

The C19 bridge must be stricter:

```text
brand / retail / OEM recovery
  -> channel inventory normalization
  -> sell-through or customer reorder
  -> discount-rate reduction
  -> gross margin and operating leverage
  -> working-capital release
  -> price survival after the first restocking spike
```

A retail inventory cycle is like a closet after winter. It is not enough that the door opens; the old stock must clear without discounts, the new items must sell through, and cash must come back without filling the closet with another pile.

---

## 5. Case 1 — 105630 한세실업

```yaml
case_id: C19_R5L93_105630_2024_03_07
symbol: "105630"
name: "한세실업"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE
trigger_date: 2024-03-07
entry_date: 2024-03-07
entry_price_basis: close
entry_price: 18220
classification: local_positive_apparel_oem_restocking_margin_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

한세실업 is the constructive control, but it is not a clean Green.

The useful C19 read is:

```text
US/apparel customer inventory normalization
  -> OEM order restocking
  -> utilization and operating leverage
  -> gross margin / OP bridge
  -> price confirmation
```

The stock produced a useful MFE after the March drawdown. But the later high MAE shows that a restocking thesis needs refreshed order and margin evidence before staying Green.

### Price path

Key Stock-Web rows:

```text
2024-03-07: close 18,220
2024-03-19: high 20,700 / close 20,300
2024-04-29: high 21,850 / close 21,850
2024-05-09: high 22,600 / close 21,750
2024-08-05: low 17,060 / close 17,310
2024-09-11: low 14,430 / close 14,500
```

Approximate path from entry close:

```text
entry_close: 18,220
peak_high: 22,600
MFE: +24.0%
worst_low: 14,430
MAE: -20.8%
```

### Interpretation

This is a local-positive / 4B-watch C19 case:

```text
Stage2-Actionable: allowed if customer reorder and margin bridge are explicit.
Stage3-Green: blocked without refreshed sell-through / reorder / OP evidence.
Local 4B: required after useful MFE followed by material drawdown.
Hard 4C: no for original early-cycle entry.
```

### Stress-test components

```text
raw_component_score_proxy:
  apparel_oem_restocking_signal: high
  channel_inventory_bridge: medium_high
  margin_op_bridge: medium
  price_confirmation: medium_high
  later_price_survival: weak
  local_4b_overlay: required
```

---

## 6. Case 2 — 383220 F&F

```yaml
case_id: C19_R5L93_383220_2024_04_01
symbol: "383220"
name: "F&F"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE
trigger_date: 2024-04-01
entry_date: 2024-04-01
entry_price_basis: close
entry_price: 76500
classification: hard_4c_candidate_premium_apparel_brand_china_inventory_margin_failure
calibration_usable: true
```

### Evidence interpretation

F&F is the premium-brand guardrail case.

The company has real brand relevance, but C19 should not promote:

```text
premium apparel brand
China retail recovery
inventory normalization hope
one-day brand rebound
```

into Green unless sell-through, channel inventory, discount-rate, and margin evidence are present. The 2024 path after the April rebound did not survive.

### Price path

Key Stock-Web rows:

```text
2024-04-01: high 77,400 / close 76,500
2024-05-03: high 73,500 / close 72,800
2024-07-29: low 57,400 / close 59,000
2024-08-05: low 47,150 / close 48,000
2024-09-27: high 71,900 / close 69,200
2024-10-25: low 57,000 / close 57,200
```

Approximate path from entry close:

```text
entry_close: 76,500
peak_high: 77,400
MFE: +1.2%
worst_low: 47,150
MAE: -38.4%
```

### Interpretation

This is a hard C19 false-positive:

```text
Stage2-Watch: possible from premium brand and retail recovery relevance.
Stage2-Actionable: blocked unless channel inventory and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by near-zero MFE and large MAE.
```

The lesson is that brand quality is not inventory-margin conversion.

### Stress-test components

```text
raw_component_score_proxy:
  brand_quality: high
  china_recovery_label: medium_high
  sellthrough_bridge: weak
  channel_inventory_bridge: weak
  margin_recovery_visibility: weak
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 298540 더네이쳐홀딩스

```yaml
case_id: C19_R5L93_298540_2024_04_01
symbol: "298540"
name: "더네이쳐홀딩스"
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE
trigger_date: 2024-04-01
entry_date: 2024-04-01
entry_price_basis: close
entry_price: 15780
classification: hard_4c_candidate_outdoor_lifestyle_brand_inventory_margin_failure
calibration_usable: true
```

### Evidence interpretation

더네이쳐홀딩스 is the outdoor/lifestyle brand false-positive.

The trigger had a plausible setup:

```text
outdoor brand
inventory normalization hope
spring/summer sell-through recovery
retail channel restocking
```

But the price path did not confirm. The move after the April spike had almost no follow-through, then drifted into a persistent drawdown.

### Price path

Key Stock-Web rows:

```text
2024-04-01: high 15,790 / close 15,780
2024-04-02: high 15,820 / close 15,720
2024-04-16: low 12,950 / close 13,850
2024-08-05: low 10,000 / close 10,920
2024-09-27: high 11,710 / close 11,680
2024-10-22: low 9,760 / close 9,760
```

Approximate path from entry close:

```text
entry_close: 15,780
peak_high: 15,820
MFE: +0.3%
worst_low: 9,760
MAE: -38.1%
```

### Interpretation

This is a hard C19 guardrail case:

```text
Stage2-Watch: possible from outdoor/lifestyle brand relevance.
Stage2-Actionable: blocked unless inventory clearance and sell-through bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by near-zero MFE and high MAE.
```

The lesson is that seasonal brand relevance can be a mirage when inventory and discount pressure remain unresolved.

### Stress-test components

```text
raw_component_score_proxy:
  outdoor_brand_label: medium_high
  seasonal_retail_recovery_label: medium
  inventory_clearance_bridge: weak
  discount_rate_bridge: weak
  price_confirmation: failed
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
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C19 grid:

```text
105630 한세실업:
  apparel OEM restocking local positive;
  useful MFE came first, but later drawdown requires local 4B and fresh margin evidence.

383220 F&F:
  premium apparel brand label failed after post-spike entry;
  near-zero MFE and high MAE, hard 4C.

298540 더네이쳐홀딩스:
  outdoor/lifestyle brand inventory normalization hope failed;
  near-zero MFE and high MAE, hard 4C.
```

Shared rule:

```text
C19 is not "consumer brand is known."
C19 is "inventory clears, sell-through improves, discount pressure falls, and margin converts."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C19_R5L93_105630_2024_03_07","scheduled_round":"R5","scheduled_loop":93,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE","symbol":"105630","name":"한세실업","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":18220,"peak_high":22600,"peak_date":"2024-05-09","worst_low":14430,"worst_low_date":"2024-09-11","mfe_pct":24.0,"mae_pct":-20.8,"classification":"local_positive_apparel_oem_restocking_margin_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"apparel_oem_restocking_customer_reorder_margin_bridge","residual_error":"positive_restocking_path_requires_4b_after_later_drawdown_without_fresh_margin_evidence","shadow_rule_candidate":"allow_actionable_when_customer_reorder_and_margin_bridge_confirm_but_attach_4b_after_material_mae"}
{"row_type":"case","case_id":"C19_R5L93_383220_2024_04_01","scheduled_round":"R5","scheduled_loop":93,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE","symbol":"383220","name":"F&F","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":76500,"peak_high":77400,"peak_date":"2024-04-01","worst_low":47150,"worst_low_date":"2024-08-05","mfe_pct":1.2,"mae_pct":-38.4,"classification":"hard_4c_candidate_premium_apparel_brand_china_inventory_margin_failure","calibration_usable":true,"evidence_family":"premium_apparel_brand_china_recovery_label_without_sellthrough_inventory_margin_bridge","residual_error":"brand_quality_can_overpromote_without_channel_inventory_and_discount_rate_repair","shadow_rule_candidate":"route_premium_brand_post_spike_entry_to_hard_4c_if_mfe_near_zero_and_inventory_margin_bridge_missing"}
{"row_type":"case","case_id":"C19_R5L93_298540_2024_04_01","scheduled_round":"R5","scheduled_loop":93,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE","symbol":"298540","name":"더네이쳐홀딩스","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":15780,"peak_high":15820,"peak_date":"2024-04-02","worst_low":9760,"worst_low_date":"2024-10-22","mfe_pct":0.3,"mae_pct":-38.1,"classification":"hard_4c_candidate_outdoor_lifestyle_brand_inventory_margin_failure","calibration_usable":true,"evidence_family":"outdoor_lifestyle_brand_inventory_normalization_label_without_sellthrough_discount_margin_bridge","residual_error":"seasonal_brand_recovery_label_can_fail_when_inventory_and_discount_pressure_remain","shadow_rule_candidate":"route_outdoor_brand_inventory_label_to_hard_4c_if_mfe_near_zero_and_mae_large"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":93,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_OEM_OUTDOOR_BRAND_INVENTORY_NORMALIZATION_MARGIN_BRIDGE_VS_BRAND_LABEL_RESTOCK_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":93,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","rule_id":"C19_INVENTORY_SELLTHROUGH_DISCOUNT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C19, do not open Stage2-Actionable or Stage3-Green from apparel/OEM/outdoor brand, China recovery, inventory normalization, seasonal sell-through, or one-week brand-stock spike labels alone. Require channel inventory normalization, sell-through or customer reorder, discount-rate reduction, gross margin or OP conversion, working-capital release, and post-trigger price survival. Apparel OEM restocking positives may be Actionable when customer reorder and margin bridge are explicit, but material later MAE should attach local 4B. Premium or outdoor brand names with near-zero MFE and high MAE should route to hard-4C when inventory and discount-pressure repair are missing.","expected_effect":"Reduce consumer brand/inventory false positives while preserving true restocking positives with sell-through, reorder, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":93,"canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","residual_type":"brand_retail_inventory_sellthrough_margin_guard","contribution":"Adds one apparel-OEM restocking local positive with 4B watch and two premium/outdoor brand hard-4C counterexamples to calibrate C19 inventory and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C19_INVENTORY_SELLTHROUGH_DISCOUNT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C19_BRAND_RETAIL_INVENTORY_MARGIN:

  Do not open Stage3-Green from:
    - apparel / outdoor / lifestyle brand label alone
    - China retail recovery label alone
    - inventory normalization headline alone
    - seasonal restocking label alone
    - one-week brand-stock price spike alone

  Require at least two of:
    - channel inventory normalization
    - sell-through improvement
    - customer reorder or retailer replenishment
    - discount-rate reduction
    - gross margin / OP conversion
    - working-capital release
    - low-MAE post-trigger price survival
    - fresh revision after the inventory headline

  If MFE < 5% and MAE < -30%:
    route to C19 hard-4C candidate.

  If MFE > 20% but later MAE < -20%:
    preserve local positive but attach 4B unless fresh sell-through/margin evidence appears.

  Distinguish:
    - apparel OEM cases with customer reorder and utilization bridge
    - from premium/outdoor brand labels where channel inventory and discount pressure remain unresolved.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_93_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C19 apparel/brand inventory-margin cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C19_INVENTORY_SELLTHROUGH_DISCOUNT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C19 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C19 cases agree, consider implementing a canonical guard that:
   - blocks consumer-brand Green without inventory, sell-through, discount-rate, and margin bridge,
   - preserves apparel-OEM positives only with customer reorder and low-MAE price survival,
   - attaches local 4B after meaningful MFE followed by material drawdown,
   - routes near-zero-MFE/high-MAE premium/outdoor brand labels to hard-4C.

Expected next schedule:
completed_round = R5
completed_loop = 93
next_round = R6
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 93
next_round = R6
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
