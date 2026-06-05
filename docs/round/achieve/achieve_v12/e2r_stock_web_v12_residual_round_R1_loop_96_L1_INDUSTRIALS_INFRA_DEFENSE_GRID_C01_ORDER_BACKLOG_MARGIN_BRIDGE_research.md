# E2R Stock-Web v12 Residual Research — R1 / Loop 96

```yaml
scheduled_round: R1
scheduled_loop: 96
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE

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
construction_machinery_case_count: 2
hydraulic_component_case_count: 1
name_change_or_listing_caveat_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 96
next_round: R2
next_loop: 96
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_95_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12, after R13 closes, the next round is:

```text
scheduled_round = R1
scheduled_loop = previous_loop + 1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 96
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

R1 hard gate requires:

```text
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage:

```text
loop91: C01_ORDER_BACKLOG_MARGIN_BRIDGE
loop92: C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
loop93: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop94: C02_POWER_GRID_DATACENTER_CAPEX
loop95: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

This run returns to C01 after one full R1 branch cycle, but avoids the top-covered C01 names and uses a different fine branch:

```text
construction machinery / compact equipment / hydraulic component
export order backlog, shipment, dealer inventory, and margin bridge
vs global equipment late chase
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE
rows: 25
symbols: 14
date_range: 2023-01-31~2024-08-30
good/bad S2: 16/4
4B/4C: 1/0
URL pending/proxy: 8/8
top covered symbols:
  042660(5), 071970(3), 100090(3), 329180(3), 010140(2), 009540(1)
```

Selected symbols:

```text
267270 HD현대건설기계
210540 디와이파워
241560 두산밥캣
```

They avoid the C01 top-covered list and avoid recent R1 loop92~95 names:

```text
loop95 C03 avoid: 064350, 272210, 448710
loop94 C02 avoid: 103590, 199820, 237750
loop93 C05 avoid: recent EPC names
loop92 C04 avoid: recent nuclear-policy names
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
267270: same archetype, new symbol, construction-machinery export/order/backlog positive with Green cap
210540: same archetype, new symbol, hydraulic cylinder / machinery component Watch cap without strong incremental order-margin bridge
241560: same archetype, new symbol, compact-equipment late-chase hard-4C candidate without fresh backlog/dealer-inventory margin survival
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
267270 HD현대건설기계
  profile: atlas/symbol_profiles/267/267270.json
  name history:
    현대건설기계 until 2023-04-18
    HD현대건설기계 from 2023-04-19 to 2026-01-23
    HD건설기계 from 2026-01-26
  selected 2024 trigger name:
    HD현대건설기계
  first_date: 2017-05-10
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,154
  corporate_action_candidate_dates:
    2017-11-14, 2017-11-23, 2017-12-06, 2018-11-19, 2018-12-18, 2026-01-26
  2024 entry~D+180 contamination: none
  caveat:
    later 2026 name/candidate date is outside the selected validation window.

210540 디와이파워
  profile: atlas/symbol_profiles/210/210540.json
  first_date: 2015-01-15
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,724
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

241560 두산밥캣
  profile: atlas/symbol_profiles/241/241560.json
  first_date: 2016-11-18
  last_date: 2026-02-20
  market: KOSPI
  tradable_ohlcv rows: 2,269
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C01 is about order backlog, delivery conversion, and margin bridge. It is not a generic "industrial equipment stock" or "global machinery demand" label.

The model can over-score:

```text
construction equipment export label
North America / emerging market machinery demand
compact equipment / skid-steer / excavator label
hydraulic cylinder component label
dealer inventory normalization headline
one-week machinery-stock volume spike
```

The C01 bridge must be stricter:

```text
industrial order / backlog event
  -> named end-market, region, or customer channel
  -> firm orders or backlog visibility
  -> shipment / delivery schedule
  -> dealer inventory and channel destocking risk
  -> ASP / mix / FX / raw-material cost pass-through
  -> warranty, logistics, and working-capital risk
  -> margin / OP conversion
  -> price survival after the first machinery rally
```

A construction-machinery order thesis is like a dealer yard full of machines. The headline says equipment demand is returning, but C01 asks whether dealers actually reorder, factories ship at utilization, inventory clears, and machines leave enough margin after freight, warranty, financing, and steel cost.

---

## 5. Case 1 — 267270 HD현대건설기계

```yaml
case_id: C01_R1L96_267270_2024_02_01
symbol: "267270"
name_at_trigger: "HD현대건설기계"
current_or_latest_name: "HD건설기계"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 51700
classification: positive_construction_machinery_export_order_backlog_delivery_margin_bridge_with_green_cap
calibration_usable: true
```

### Evidence interpretation

HD현대건설기계 is the constructive C01 control in this set.

The useful C01 read is not simply:

```text
건설기계주가 강하다
```

It is:

```text
construction machinery export and regional demand relevance
  -> order/backlog and dealer-channel readthrough
  -> shipment and utilization bridge
  -> ASP / FX / mix / margin optionality
  -> post-trigger price survival
```

The forward path delivered a strong MFE into July and kept MAE controlled enough to preserve positive classification. However, the stock is still cyclical. Green should be capped unless fresh backlog, shipment, dealer inventory, and margin evidence refreshes the thesis.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 52,400 / close 51,700
2024-02-05: high 58,700 / close 56,700
2024-03-15: high 60,400 / close 56,900
2024-03-28: high 60,000 / close 58,500
2024-07-24: high 66,900 / close 63,900
2024-07-25: high 68,500 / close 63,700
2024-08-05: low 49,050 / close 51,700
2024-09-09: low 45,700 / close 47,300
2024-10-18: high 55,800 / close 55,700
```

Approximate path from entry close:

```text
entry_close: 51,700
peak_high: 68,500
MFE: +32.5%
worst_low_after_entry: 45,700
MAE: -11.6%
```

### Interpretation

This is a C01 positive with Green cap:

```text
Stage2-Actionable: possible if order/backlog, dealer inventory, shipment, and margin bridge are explicit.
Stage3-Green: possible only with fresh delivery, utilization, and margin evidence.
Local 4B: monitor after +30% MFE if evidence becomes stale.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  construction_machinery_relevance: high
  export_order_backlog_bridge: high
  dealer_inventory_bridge: medium_high
  shipment_delivery_bridge: medium_high
  asp_fx_margin_bridge: medium
  price_confirmation: high
  drawdown_penalty: low_to_medium
  green_cap: yes
```

---

## 6. Case 2 — 210540 디와이파워

```yaml
case_id: C01_R1L96_210540_2024_02_01
symbol: "210540"
name: "디와이파워"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE
trigger_date: 2024-02-01
entry_date: 2024-02-01
entry_price_basis: close
entry_price: 12600
classification: watch_cap_hydraulic_cylinder_machinery_component_label_without_strong_incremental_order_margin_bridge
calibration_usable: true
```

### Evidence interpretation

디와이파워 is the hydraulic machinery-component Watch cap.

The company has relevant exposure:

```text
hydraulic cylinder / construction machinery component
  -> excavator and equipment shipment readthrough
  -> component order and utilization optionality
```

But the forward path did not validate a strong C01 rerating. MFE was modest, MAE was controlled, and the path did not show a strong backlog-to-margin surge. This is a Watch/Yellow cap unless order conversion and margin evidence becomes explicit.

### Price path

Key Stock-Web rows:

```text
2024-02-01: high 12,850 / close 12,600
2024-02-13: high 13,770 / close 13,690
2024-02-26: high 13,920 / close 13,790
2024-03-28: high 13,830 / close 13,650
2024-08-05: low 12,000 / close 12,090
2024-09-09: low 11,730 / close 12,070
2024-10-28: low 11,680 / close 12,200
```

Approximate path from entry close:

```text
entry_close: 12,600
peak_high: 13,920
MFE: +10.5%
worst_low_after_entry: 11,680
MAE: -7.3%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from machinery-component and hydraulic-cylinder relevance.
Stage2-Actionable: blocked unless customer order, equipment shipment, utilization, and margin bridge are explicit.
Stage3-Green: blocked without fresh order-margin evidence.
Hard 4C: no.
```

The lesson is that machinery-component relevance is not automatically backlog-to-margin conversion.

### Stress-test components

```text
raw_component_score_proxy:
  hydraulic_component_relevance: high
  construction_equipment_readthrough: medium_high
  order_visibility_bridge: weak_to_medium
  utilization_margin_bridge: weak_to_medium
  price_confirmation: modest
  drawdown_penalty: low
  actionability_cap: Watch/Yellow
```

---

## 7. Case 3 — 241560 두산밥캣

```yaml
case_id: C01_R1L96_241560_2024_07_24
symbol: "241560"
name: "두산밥캣"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE
trigger_date: 2024-07-24
entry_date: 2024-07-24
entry_price_basis: close
entry_price: 47050
classification: hard_4c_candidate_compact_equipment_late_chase_without_fresh_backlog_dealer_inventory_margin_survival
calibration_usable: true
```

### Evidence interpretation

두산밥캣 is the hard/near-hard C01 guardrail.

The label is high quality:

```text
compact equipment / skid-steer / North America machinery
  -> global equipment demand
  -> dealer-channel and order-backlog readthrough
```

But the selected late July entry is not the same as an early backlog rerating. From this late entry, MFE was shallow, and the later drawdown approached the hard-failure zone. The model should not promote late machinery-label chases unless fresh backlog, dealer inventory, shipment, and margin evidence is current.

### Price path

Key Stock-Web rows:

```text
2024-07-24: high 48,600 / close 47,050
2024-07-25: high 47,950 / close 44,150
2024-07-31: low 39,800 / close 41,200
2024-08-05: low 33,350 / close 34,250
2024-08-29: high 45,950 / close 42,050
2024-10-18: high 44,350 / close 43,000
2024-10-25: low 37,700 / close 37,800
```

Approximate path from late entry close:

```text
entry_close: 47,050
peak_high_after_entry: 48,600
MFE: +3.3%
worst_low_after_entry: 33,350
MAE: -29.1%
```

### Interpretation

This is a hard-4C candidate / near-hard false-positive:

```text
Stage2-Watch: possible from compact equipment and global machinery relevance.
Stage2-Actionable: blocked unless fresh backlog, dealer inventory, shipment, and margin bridge are explicit.
Stage3-Green: blocked from the selected late entry.
Hard 4C candidate: yes by shallow MFE and near -30% MAE after a late chase.
```

The lesson is that a high-quality machinery label can still be a late-chase trap when dealer inventory and order-to-margin evidence is stale.

### Stress-test components

```text
raw_component_score_proxy:
  compact_equipment_label: very_high
  north_america_machinery_relevance: high
  fresh_order_backlog_bridge: weak_from_late_entry
  dealer_inventory_bridge: weak_from_late_entry
  margin_survival: weak
  price_confirmation_after_entry: failed
  drawdown_penalty: high
  hard_4c_guard: candidate
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
watch_or_cap_case_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
construction_machinery_case_count: 2
hydraulic_component_case_count: 1
name_change_or_listing_caveat_count: 1
calibration_usable_trigger_count: 3
```

The three-case C01 construction-machinery grid:

```text
267270 HD현대건설기계:
  construction machinery export/order-backlog positive;
  strong MFE and controlled MAE, but Green requires refreshed backlog/dealer inventory/margin evidence.

210540 디와이파워:
  hydraulic-cylinder machinery-component relevance;
  modest MFE and low MAE, Watch/Yellow cap without strong incremental order-margin bridge.

241560 두산밥캣:
  compact-equipment late chase failed from the selected July entry;
  shallow MFE and near-hard MAE, hard 4C candidate.
```

Shared rule:

```text
C01 is not "industrial machinery label is high quality."
C01 is "orders become backlog, backlog becomes shipment, shipment becomes utilization, and utilization becomes margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C01_R1L96_267270_2024_02_01","scheduled_round":"R1","scheduled_loop":96,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE","symbol":"267270","name_at_trigger":"HD현대건설기계","current_or_latest_name":"HD건설기계","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":51700,"peak_high":68500,"peak_date":"2024-07-25","worst_low_after_entry":45700,"worst_low_after_entry_date":"2024-09-09","mfe_pct":32.5,"mae_pct":-11.6,"classification":"positive_construction_machinery_export_order_backlog_delivery_margin_bridge_with_green_cap","calibration_usable":true,"evidence_family":"construction_machinery_export_order_backlog_dealer_inventory_delivery_margin_bridge","residual_error":"positive_order_backlog_path_still_requires_green_cap_without_refreshed_dealer_inventory_margin_evidence","shadow_rule_candidate":"allow_actionable_when_backlog_delivery_and_margin_bridge_confirm_but_cap_green_without_fresh_evidence"}
{"row_type":"case","case_id":"C01_R1L96_210540_2024_02_01","scheduled_round":"R1","scheduled_loop":96,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE","symbol":"210540","name":"디와이파워","trigger_date":"2024-02-01","entry_date":"2024-02-01","entry_price":12600,"peak_high":13920,"peak_date":"2024-02-26","worst_low_after_entry":11680,"worst_low_after_entry_date":"2024-10-28","mfe_pct":10.5,"mae_pct":-7.3,"classification":"watch_cap_hydraulic_cylinder_machinery_component_label_without_strong_incremental_order_margin_bridge","calibration_usable":true,"evidence_family":"hydraulic_cylinder_construction_machinery_component_label_without_incremental_order_utilization_margin_bridge","residual_error":"machinery_component_relevance_can_overpromote_without_customer_order_and_margin_conversion","shadow_rule_candidate":"cap_hydraulic_component_label_at_watch_yellow_if_mfe_modest_and_order_margin_bridge_missing"}
{"row_type":"case","case_id":"C01_R1L96_241560_2024_07_24","scheduled_round":"R1","scheduled_loop":96,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE","symbol":"241560","name":"두산밥캣","trigger_date":"2024-07-24","entry_date":"2024-07-24","entry_price":47050,"peak_high":48600,"peak_date":"2024-07-24","worst_low_after_entry":33350,"worst_low_after_entry_date":"2024-08-05","mfe_pct":3.3,"mae_pct":-29.1,"classification":"hard_4c_candidate_compact_equipment_late_chase_without_fresh_backlog_dealer_inventory_margin_survival","calibration_usable":true,"evidence_family":"compact_equipment_north_america_machinery_late_chase_without_fresh_backlog_dealer_inventory_margin_bridge","residual_error":"high_quality_machinery_label_can_fail_when_late_entry_lacks_current_backlog_and_dealer_inventory_evidence","shadow_rule_candidate":"route_compact_equipment_late_chase_to_hard_4c_candidate_if_mfe_shallow_mae_large_and_backlog_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":96,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"CONSTRUCTION_MACHINERY_HYDRAULIC_COMPONENT_EXPORT_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_GLOBAL_EQUIPMENT_LATE_CHASE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"construction_machinery_case_count":2,"hydraulic_component_case_count":1,"name_change_or_listing_caveat_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":96,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","rule_id":"C01_MACHINERY_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C01 construction machinery, compact equipment, and hydraulic-component cases, do not open Stage2-Actionable or Stage3-Green from construction equipment, compact equipment, North America or emerging-market demand, dealer inventory normalization, hydraulic component, export, or one-week machinery-stock volume spike labels alone. Require named end-market, region, or customer channel; firm orders or backlog visibility; shipment/delivery schedule; dealer inventory and destocking risk check; ASP/mix/FX/raw-material cost pass-through; warranty/logistics/working-capital risk check; margin/OP conversion; and post-trigger price survival. Construction-machinery positives with large MFE and controlled MAE may be capped Actionable when backlog/delivery/margin bridge is explicit, but Green requires fresh evidence. Hydraulic component labels with modest MFE should cap at Watch/Yellow without customer order and margin evidence. Compact equipment late chases with shallow MFE and large MAE should route to hard-4C candidate when fresh backlog and dealer-inventory bridge are missing.","expected_effect":"Preserve true machinery order-backlog positives while reducing global equipment label and late-chase false positives.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":96,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"machinery_order_backlog_delivery_margin_guard","contribution":"Adds one construction-machinery order/backlog positive, one hydraulic-component Watch cap, and one compact-equipment late-chase hard-4C candidate to calibrate C01 order, dealer inventory, shipment, cost pass-through, and margin requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C01_MACHINERY_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE
AND company_type in [construction_machinery, compact_equipment, hydraulic_component, industrial_equipment]:

  Do not open Stage3-Green from:
    - construction machinery label alone
    - compact equipment / skid-steer label alone
    - North America or emerging-market machinery demand alone
    - dealer inventory normalization headline alone
    - hydraulic-cylinder or machinery-component label alone
    - export demand label alone
    - one-week machinery-stock volume spike alone

  Require at least two of:
    - named end-market, region, or customer channel
    - firm orders or backlog visibility
    - shipment / delivery schedule
    - dealer inventory and destocking risk check
    - ASP / mix / FX / raw-material cost pass-through
    - warranty / logistics / working-capital risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh evidence after the machinery-demand headline

  If MFE < 5% and MAE < -25%:
    route to C01 hard-4C candidate for late machinery chases.

  If MFE is modest and order bridge is weak:
    cap at Watch/Yellow.

  If MFE is meaningful but evidence is stale:
    preserve as capped positive or local 4B, not Green.

  Distinguish:
    - equipment names where orders become backlog, shipment, utilization, and margin
    - from high-quality machinery labels where dealer inventory or cost pressure breaks the bridge.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_96_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C01 construction-machinery / hydraulic-component order-backlog cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C01_MACHINERY_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C01 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C01 machinery cases agree, consider implementing a canonical guard that:
   - blocks machinery-label Green without firm order/backlog, shipment, dealer inventory, and margin bridge,
   - preserves construction-machinery positives only with price survival and fresh execution evidence,
   - caps hydraulic-component labels at Watch/Yellow without customer order evidence,
   - routes shallow-MFE/large-MAE compact-equipment late chases to hard-4C candidate.

Expected next schedule:
completed_round = R1
completed_loop = 96
next_round = R2
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 96
next_round = R2
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```
