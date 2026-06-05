# E2R Stock-Web v12 Residual Research — R5 / Loop 95

```yaml
scheduled_round: R5
scheduled_loop: 95
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE

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
name_change_caveat_count: 2
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R5
completed_loop: 95
next_round: R6
next_loop: 95
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R4_loop_95_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R5
scheduled_loop = 95
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

R5 hard gate requires:

```text
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
```

Recent R5 branch usage:

```text
loop92: C18_CONSUMER_EXPORT_CHANNEL_REORDER
loop93: C19_BRAND_RETAIL_INVENTORY_MARGIN
loop94: C20_BEAUTY_FOOD_GLOBAL_DISTRIBUTION
```

This run returns to C18, but avoids the top-covered C18 names and uses a different fine branch:

```text
apparel OEM / global brand / export-channel reorder
sell-through, inventory, FX, logistics, and margin bridge
vs consumer export label spike
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
111770 영원무역
081660 휠라홀딩스 / 미스토홀딩스
007980 태평양물산 / TP
```

They avoid the C18 top-covered symbols and avoid recent R5 loop92~94 names:

```text
loop92 avoid: 352480, 018290, 002790
loop93 avoid: 105630, 383220, 298540
loop94 avoid: 003230, 271560, 017810
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
111770: same archetype, new symbol, apparel OEM/export channel reorder capped positive with 4B watch
081660: same archetype, new symbol, global brand/channel label Watch cap without fresh incremental reorder-margin bridge
007980: same archetype, new symbol, apparel OEM/channel reorder label hard-4C without sell-through and margin survival
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
111770 영원무역
  profile: atlas/symbol_profiles/111/111770.json
  first_date: 2009-07-30
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 4,080
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

081660 휠라홀딩스 / 미스토홀딩스
  profile: atlas/symbol_profiles/081/081660.json
  name history:
    휠라코리아 until 2020-01-14
    휠라홀딩스 from 2020-01-15 to 2025-04-17
    미스토홀딩스 from 2025-04-18
  selected 2024 name:
    휠라홀딩스
  first_date: 2010-09-28
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 3,786
  corporate_action_candidate_dates:
    2018-05-09
  2024 entry~D+180 contamination: none

007980 태평양물산 / TP
  profile: atlas/symbol_profiles/007/007980.json
  name history:
    태평양물산 until 2024-04-19
    TP from 2024-04-22
  selected trigger name:
    태평양물산
  current/latest name:
    TP
  first_date: 1995-05-02
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 7,742
  non_tradable_zero_volume rows: 23
  corporate_action_candidate_dates:
    1997-01-03, 1999-03-23, 1999-07-09, 2013-05-22, 2013-11-28
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C18 is about consumer export channel reorder. It is not a generic "consumer export" or "global brand" label.

The model can over-score:

```text
apparel OEM export label
global sportswear brand
fashion retail overseas channel
consumer export recovery
US / Europe inventory normalization
one-week apparel-stock volume spike
brand-quality or low-PBR consumer label
```

The C18 bridge must be stricter:

```text
consumer export / channel recovery event
  -> overseas sell-through
  -> distributor or buyer reorder
  -> inventory normalization at the channel
  -> ASP / mix / FX benefit
  -> production utilization and supplier cost control
  -> freight / logistics cost containment
  -> margin / OP conversion
  -> price survival after the first export-channel rally
```

A consumer export thesis is like a warehouse receiving a reorder slip. The brand name opens the door, but C18 asks whether goods actually sell through, buyers reorder, inventory clears, FX and mix help, and the shipment leaves margin after logistics and supplier cost.

---

## 5. Case 1 — 111770 영원무역

```yaml
case_id: C18_R5L95_111770_2024_07_24
symbol: "111770"
name: "영원무역"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 39150
classification: positive_capped_apparel_oem_export_channel_reorder_margin_bridge_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

영원무역 is the constructive C18 control in this set.

The useful C18 read is not simply:

```text
의류 OEM / 수출주가 움직였다
```

It is:

```text
apparel OEM export relevance
  -> channel inventory normalization
  -> buyer reorder and sell-through bridge
  -> FX / mix / utilization margin optionality
  -> post-trigger price survival
```

The forward path from the July entry produced a meaningful MFE and a controlled drawdown. This is a capped positive, not a free Green. The model should still require fresh buyer reorder, channel inventory, and margin evidence before promoting it.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 39,400 / close 39,150
2024-08-05: low 34,850 / close 36,150
2024-08-16: high 41,350 / close 41,350
2024-09-09: low 35,000 / close 36,550
2024-10-16: high 44,950 / close 43,700
2024-10-25: low 39,750 / close 40,100
```

Approximate path from entry close:

```text
entry_close: 39,150
peak_high: 44,950
MFE: +14.8%
worst_low_after_entry: 34,850
MAE: -11.0%
```

### Interpretation

This is a C18 capped positive with 4B watch:

```text
Stage2-Actionable: possible if buyer reorder, sell-through, and margin bridge are explicit.
Stage3-Green: blocked without fresh channel inventory and OP evidence.
Local 4B: monitor after mid-teen MFE because the bridge is cyclical and export-channel evidence must refresh.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  apparel_oem_export_relevance: high
  buyer_reorder_bridge: medium_high
  inventory_normalization_bridge: medium
  fx_mix_margin_bridge: medium
  price_confirmation: medium_high
  drawdown_penalty: medium
  green_cap: yes
  local_4b_overlay: watch
```

---

## 6. Case 2 — 081660 휠라홀딩스 / 미스토홀딩스

```yaml
case_id: C18_R5L95_081660_2024_07_24
symbol: "081660"
name_at_trigger: "휠라홀딩스"
current_or_latest_name: "미스토홀딩스"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 40750
classification: watch_cap_global_sportswear_brand_channel_label_without_incremental_reorder_margin_bridge
calibration_usable: true
```

### Evidence interpretation

휠라홀딩스 is the global-brand Watch cap.

The company has clear C18 relevance:

```text
global sportswear brand
overseas retail / wholesale channel
inventory normalization and brand recovery optionality
```

But C18 should not promote a stable global brand label into Actionable/Green unless the incremental bridge is visible:

```text
sell-through
reorder acceleration
channel inventory reduction
ASP / mix / margin improvement
```

The forward path had a modest MFE and controlled MAE, but not enough to confirm an export-channel rerating.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 40,900 / close 40,750
2024-07-31: high 43,000 / close 42,800
2024-08-01: high 44,550 / close 44,450
2024-08-06: low 37,400 / close 39,950
2024-08-29: high 44,150 / close 43,650
2024-09-25: high 44,950 / close 43,550
2024-10-29: low 37,950 / close 38,150
```

Approximate path from entry close:

```text
entry_close: 40,750
peak_high: 44,950
MFE: +10.3%
worst_low_after_entry: 37,400
MAE: -8.2%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from global brand/channel relevance.
Stage2-Actionable: blocked unless incremental sell-through, reorder, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: no, because MAE was controlled.
```

The lesson is that global brand quality is not the same as current channel reorder.

### Stress-test components

```text
raw_component_score_proxy:
  global_brand_relevance: high
  overseas_channel_base: high
  incremental_reorder_bridge: weak_to_medium
  inventory_margin_bridge: weak_to_medium
  price_confirmation: modest
  drawdown_penalty: low_to_medium
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 007980 태평양물산 / TP

```yaml
case_id: C18_R5L95_007980_2024_02_01
symbol: "007980"
name_at_trigger: "태평양물산"
current_or_latest_name: "TP"
canonical_archetype_id: C18_CONSUMER_EXPORT_CHANNEL_REORDER
fine_archetype_id: APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 1930
classification: hard_4c_candidate_apparel_oem_export_channel_label_without_sellthrough_margin_survival
calibration_usable: true
```

### Evidence interpretation

태평양물산 is the hard C18 guardrail.

The setup had the classic trap:

```text
apparel OEM / export label
US and global inventory normalization hope
low-priced consumer export stock
one-week channel-recovery spike
```

The forward path had only shallow MFE and then a large drawdown. The company changed name to TP later in 2024, but the selected trigger uses the then-current name, and there is no 2024 corporate-action contamination in the entry window.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 1,948 / close 1,930
2024-02-02: high 2,030 / close 1,995
2024-03-06: high 2,115 / close 1,992
2024-04-17: high 1,797 / close 1,643
2024-08-05: low 1,349 / close 1,370
2024-09-09: low 1,264 / close 1,308
2024-10-25: low 1,301 / close 1,320
```

Approximate path from entry close:

```text
entry_close: 1,930
peak_high: 2,115
MFE: +9.6%
worst_low_after_entry: 1,264
MAE: -34.5%
```

### Interpretation

This is a hard C18 false-positive:

```text
Stage2-Watch: possible from apparel OEM/export relevance.
Stage2-Actionable: blocked unless sell-through, buyer reorder, channel inventory, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and -30%+ MAE.
```

The lesson is that apparel export label is not reorder-margin survival.

### Stress-test components

```text
raw_component_score_proxy:
  apparel_oem_export_label: high
  channel_recovery_hope: medium_high
  buyer_reorder_bridge: weak
  inventory_margin_bridge: weak
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
name_change_caveat_count: 2
calibration_usable_trigger_count: 3
```

The three-case C18 apparel/export grid:

```text
111770 영원무역:
  apparel OEM export-channel reorder capped positive;
  mid-teen MFE and controlled MAE, but Green requires fresh reorder/margin evidence.

081660 휠라홀딩스 / 미스토홀딩스:
  global sportswear brand/channel label;
  modest MFE and controlled MAE, Watch/Yellow cap without incremental bridge.

007980 태평양물산 / TP:
  apparel OEM export-channel label failed;
  shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C18 is not "consumer export label."
C18 is "sell-through, buyer reorder, channel inventory normalization, FX/mix, logistics cost, and margin conversion are visible for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C18_R5L95_111770_2024_07_24","scheduled_round":"R5","scheduled_loop":95,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE","symbol":"111770","name":"영원무역","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":39150,"peak_high":44950,"peak_date":"2024-10-16","worst_low_after_entry":34850,"worst_low_after_entry_date":"2024-08-05","mfe_pct":14.8,"mae_pct":-11.0,"classification":"positive_capped_apparel_oem_export_channel_reorder_margin_bridge_with_4b_watch","calibration_usable":true,"evidence_family":"apparel_oem_export_channel_reorder_inventory_normalization_fx_mix_margin_bridge","residual_error":"positive_export_channel_path_requires_green_cap_without_fresh_reorder_margin_evidence","shadow_rule_candidate":"allow_capped_actionable_when_buyer_reorder_sellthrough_and_margin_bridge_confirm_but_attach_4b_if_bridge_stale"}
{"row_type":"case","case_id":"C18_R5L95_081660_2024_07_24","scheduled_round":"R5","scheduled_loop":95,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE","symbol":"081660","name_at_trigger":"휠라홀딩스","current_or_latest_name":"미스토홀딩스","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":40750,"peak_high":44950,"peak_date":"2024-09-25","worst_low_after_entry":37400,"worst_low_after_entry_date":"2024-08-06","mfe_pct":10.3,"mae_pct":-8.2,"classification":"watch_cap_global_sportswear_brand_channel_label_without_incremental_reorder_margin_bridge","calibration_usable":true,"evidence_family":"global_sportswear_brand_overseas_channel_label_without_incremental_sellthrough_reorder_margin_bridge","residual_error":"global_brand_quality_can_overpromote_without_current_channel_reorder_and_margin_conversion","shadow_rule_candidate":"cap_global_brand_channel_label_at_watch_yellow_if_mfe_modest_and_incremental_bridge_missing"}
{"row_type":"case","case_id":"C18_R5L95_007980_2024_02_01","scheduled_round":"R5","scheduled_loop":95,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE","symbol":"007980","name_at_trigger":"태평양물산","current_or_latest_name":"TP","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":1930,"peak_high":2115,"peak_date":"2024-03-06","worst_low_after_entry":1264,"worst_low_after_entry_date":"2024-09-09","mfe_pct":9.6,"mae_pct":-34.5,"classification":"hard_4c_candidate_apparel_oem_export_channel_label_without_sellthrough_margin_survival","calibration_usable":true,"evidence_family":"apparel_oem_export_channel_recovery_label_without_buyer_reorder_inventory_margin_bridge","residual_error":"apparel_export_label_can_fail_when_sellthrough_reorder_and_margin_bridge_missing","shadow_rule_candidate":"route_apparel_oem_export_label_to_hard_4c_if_mfe_shallow_mae_large_and_reorder_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R5","scheduled_loop":95,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","fine_archetype_id":"APPAREL_OEM_GLOBAL_BRAND_EXPORT_CHANNEL_REORDER_MARGIN_BRIDGE_VS_CONSUMER_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"name_change_caveat_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R5","scheduled_loop":95,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","rule_id":"C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C18, do not open Stage2-Actionable or Stage3-Green from consumer export, apparel OEM, global brand, fashion retail overseas channel, inventory normalization, US/Europe recovery, low-PBR consumer, or one-week apparel-stock volume spike labels alone. Require overseas sell-through, distributor or buyer reorder, channel inventory normalization, ASP/mix/FX benefit, production utilization and supplier cost control, freight/logistics cost containment, margin/OP conversion, and post-trigger price survival. Apparel OEM positives with mid-teen MFE and controlled MAE may be capped Actionable only when buyer reorder and margin bridge are explicit. Stable global brand/channel labels with modest MFE should cap at Watch/Yellow without incremental reorder evidence. Apparel OEM export labels with shallow MFE and high MAE should route to hard-4C when sell-through and margin bridge are missing.","expected_effect":"Reduce consumer export and apparel-label false positives while preserving true export-channel reorder positives with sell-through, inventory, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R5","scheduled_loop":95,"canonical_archetype_id":"C18_CONSUMER_EXPORT_CHANNEL_REORDER","residual_type":"consumer_export_sellthrough_reorder_margin_guard","contribution":"Adds one apparel OEM export-channel capped positive, one global sportswear brand Watch cap, and one apparel OEM hard-4C counterexample to calibrate C18 sell-through, reorder, inventory, FX/mix, logistics, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C18_CONSUMER_EXPORT_CHANNEL_REORDER:

  Do not open Stage3-Green from:
    - consumer export label alone
    - apparel OEM export label alone
    - global brand or fashion retail label alone
    - US / Europe inventory normalization label alone
    - low-PBR consumer cyclical sympathy alone
    - one-week apparel-stock volume spike alone

  Require at least two of:
    - overseas sell-through
    - distributor / buyer reorder
    - channel inventory normalization
    - ASP / mix / FX benefit
    - production utilization / supplier-cost control
    - freight / logistics-cost containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the export-channel headline

  If MFE < 10% and MAE < -30%:
    route to C18 hard-4C candidate.

  If MFE is modest and the bridge is stable-brand only:
    cap at Watch/Yellow unless incremental reorder and margin evidence appears.

  If MFE is meaningful but bridge is stale:
    preserve as capped positive or local 4B, not Green.

  Distinguish:
    - export channel names where sell-through becomes buyer reorder and margin
    - from consumer brand/OEM labels where inventory or logistics cost breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R5_loop_95_L5_CONSUMER_BRAND_DISTRIBUTION_C18_CONSUMER_EXPORT_CHANNEL_REORDER_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C18 consumer export-channel reorder cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C18_EXPORT_SELLTHROUGH_REORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C18 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C18 cases agree, consider implementing a canonical guard that:
   - blocks consumer export/apparel Green without sell-through, reorder, inventory, and margin bridge,
   - preserves apparel OEM positives only with price survival and fresh buyer evidence,
   - caps global brand/channel labels at Watch/Yellow without incremental reorder evidence,
   - routes shallow-MFE/high-MAE apparel OEM export labels to hard-4C.

Expected next schedule:
completed_round = R5
completed_loop = 95
next_round = R6
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R5
completed_loop = 95
next_round = R6
next_loop = 95
round_schedule_status = valid
round_sector_consistency = pass
```
