# E2R Stock-Web v12 Residual Research — R2 / Loop 92

```yaml
scheduled_round: R2
scheduled_loop: 92
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE

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
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R2
completed_loop: 92
next_round: R3
next_loop: 92
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 92
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires L2 semiconductor / AI / electronics work. Recent R2 branch usage already covered:

```text
loop89: C06_HBM_MEMORY_CUSTOMER_CAPACITY
loop90: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop91: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
```

This run therefore selects the under-covered C09 branch:

```text
canonical_archetype_id = C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
rows: 17
symbols: 11
date_range: 2023-07-14~2024-09-24
good/bad S2: 7/3
4B/4C: 1/0
URL pending/proxy: 7/7
top covered symbols:
  322310(3), 348210(3), 089030(2), 140860(2), 031980(1), 064290(1)
```

Selected symbols:

```text
084370 유진테크
240810 원익IPS
036810 에프에스티
```

These avoid the C09 top-covered symbols and also avoid recent R2 loop90/91 symbols such as:

```text
031980, 039030, 403870, 232140, 131970, 330860
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
084370: same archetype, new symbol, deposition/advanced equipment rerating with valuation-4B watch
240810: same archetype, new symbol, large-cap equipment cycle label false-positive branch
036810: same archetype, new symbol, EUV/pellicle/advanced materials equipment local-burst branch
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
084370 유진테크
  profile: atlas/symbol_profiles/084/084370.json
  first_date: 2006-01-17
  last_date: 2026-02-20
  tradable_ohlcv rows: 4,955
  corporate_action_candidate_dates:
    2007-05-17, 2010-01-22, 2012-06-07
  2024 entry~D+180 contamination: none

240810 원익IPS
  profile: atlas/symbol_profiles/240/240810.json
  first_date: 2016-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,405
  corporate_action_candidate_dates: none
  2024 entry~D+180 contamination: none

036810 에프에스티
  profile: atlas/symbol_profiles/036/036810.json
  first_date: 2000-01-18
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,430
  corporate_action_candidate_dates:
    2000-05-02, 2004-06-17
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C09 is not a normal semiconductor equipment-cycle archetype. It is the point where a genuine advanced-equipment thesis starts to overheat.

The model can over-score:

```text
advanced semiconductor equipment
HBM equipment
EUV / pellicle / mask / deposition label
memory capex recovery
AI semiconductor equipment sympathy
one-week equipment blowoff
```

The real C09 bridge is narrower:

```text
advanced equipment capability
  -> customer qualification
  -> order or shipment visibility
  -> delivery timing
  -> margin and utilization bridge
  -> valuation discipline after price acceleration
  -> local 4B / 4C routing when the price outruns evidence
```

A semi-equipment stock is like a precision machine on the factory floor. The machine can be valuable, but the stock can still overheat if investors price ten factory lines before the first line is actually installed and paid for.

---

## 5. Case 1 — 084370 유진테크

```yaml
case_id: C09_R2L92_084370_2024_03_21
symbol: "084370"
name: "유진테크"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-03-21
entry_date: 2024-03-21
entry_price_basis: close
entry_price: 41450
classification: positive_with_local_4b_deposition_equipment_rerating
calibration_usable: true
```

### Evidence interpretation

유진테크 is the positive control in this set. It had real advanced equipment / deposition-cycle relevance and the price path validated the theme beyond a single-day spike.

But this is still C09, not a clean C07 or C10 equipment-cycle case. The stock ran far enough that the model should attach a 4B watch rather than keep Green open purely from the equipment label.

### Price path

Key Stock-Web rows:

```text
2024-03-21: close 41,450
2024-03-29: high 44,700 / close 44,000
2024-04-05: high 50,500 / close 49,950
2024-04-17: high 54,900 / close 52,100
2024-05-07: high 58,700 / close 57,600
2024-05-28: high 60,000 / close 56,500
2024-09-11: low 35,350 / close 35,500
```

Approximate path from entry close:

```text
entry_close: 41,450
peak_high: 60,000
MFE: +44.8%
worst_low: 35,350
MAE: -14.7%
peak_to_later_low_drawdown: -41.1%
```

### Interpretation

This is a C09 positive with local 4B watch:

```text
Stage2-Actionable: valid if customer/order/margin bridge is explicit.
Stage3-Green: possible only with delivery and revision evidence.
Local 4B: required after +40% MFE and >40% peak drawdown.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  advanced_equipment_relevance: high
  customer_order_bridge: medium_high
  margin_utilization_bridge: medium
  valuation_blowoff_risk: high
  price_confirmation: high
  peak_drawdown_penalty: high
  local_4b_overlay: required
```

---

## 6. Case 2 — 240810 원익IPS

```yaml
case_id: C09_R2L92_240810_2024_03_20
symbol: "240810"
name: "원익IPS"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-03-20
entry_date: 2024-03-20
entry_price_basis: close
entry_price: 37400
classification: hard_4c_candidate_large_equipment_cycle_label_without_revision_bridge
calibration_usable: true
```

### Evidence interpretation

원익IPS is the large-equipment false-positive. It has a credible semiconductor-equipment label, but that is exactly the trap. C09 requires more than label quality. It asks whether the price acceleration has a new order, margin, and delivery bridge strong enough to justify the valuation.

The forward path after the March equipment surge did not survive.

### Price path

Key Stock-Web rows:

```text
2024-03-20: close 37,400
2024-03-29: high 43,400 / close 41,500
2024-04-08: high 44,850 / close 41,650
2024-05-13: low 33,500 / close 33,900
2024-08-05: low 30,550 / close 31,200
2024-09-11: low 27,800 / close 28,000
2024-11-14: low 22,200 / close 22,650
```

Approximate path from entry close:

```text
entry_close: 37,400
peak_high: 44,850
MFE: +19.9%
worst_low: 22,200
MAE: -40.6%
```

### Interpretation

This is a hard C09 guardrail case:

```text
Stage2-Watch: valid from equipment-cycle label.
Stage2-Actionable: blocked unless fresh order / delivery / margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is that a top-tier equipment name can still be a false positive if the entry is driven by broad equipment beta rather than a fresh company-specific revision bridge.

### Stress-test components

```text
raw_component_score_proxy:
  equipment_label_quality: high
  fresh_order_bridge: weak_to_medium
  delivery_timing_bridge: weak
  margin_revision_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 036810 에프에스티

```yaml
case_id: C09_R2L92_036810_2024_04_09
symbol: "036810"
name: "에프에스티"
canonical_archetype_id: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
fine_archetype_id: ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE
trigger_date: 2024-04-09
entry_date: 2024-04-09
entry_price_basis: close
entry_price: 27900
classification: local_burst_high_mae_euv_pellicle_advanced_label_without_durable_order_bridge
calibration_usable: true
```

### Evidence interpretation

에프에스티 is the local-burst case. The EUV / pellicle / advanced semiconductor-materials label can create a violent rerating burst. But C09 specifically exists because that burst can outrun firm order and margin evidence.

The path is a useful 4B boundary:

```text
MFE was large enough to reward event traders.
MAE later became too large for durable Green.
```

### Price path

Key Stock-Web rows:

```text
2024-04-09: close 27,900
2024-04-15: high 35,700 / close 32,300
2024-04-29: high 38,400 / close 33,700
2024-05-28: high 38,200 / close 35,450
2024-06-11: high 41,850 / close 40,200
2024-08-05: low 27,850 / close 28,500
2024-09-09: low 22,300 / close 23,150
2024-11-20: low 16,200 / close 16,230
```

Approximate path from entry close:

```text
entry_close: 27,900
peak_high: 41,850
MFE: +50.0%
worst_low: 16,200
MAE: -41.9%
peak_to_later_low_drawdown: -61.3%
```

### Interpretation

This is a local-burst / high-MAE counterexample:

```text
Stage2-Watch: allowed.
Stage2-Actionable: only as event-trading / local 4B unless order bridge is explicit.
Stage3-Green: blocked.
Hard 4C: borderline by MAE, but primary classification is local burst failure.
```

The stock gave enough MFE to be called a tradable event, but the lack of price survival prevents Green.

### Stress-test components

```text
raw_component_score_proxy:
  advanced_equipment_label: high
  euv_pellicle_label: high
  customer_order_bridge: weak_to_medium
  margin_bridge: weak
  local_price_burst: very_high
  post_burst_survival: failed
  local_4b_overlay: required
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 1
counterexample_count: 2
local_4b_overlay_case_count: 2
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C09 grid:

```text
084370 유진테크:
  advanced deposition/equipment rerating worked,
  but local 4B is required after large MFE and peak drawdown.

240810 원익IPS:
  large equipment-cycle label failed without fresh order/margin bridge;
  shallow MFE and high MAE make it hard 4C.

036810 에프에스티:
  EUV/pellicle/advanced label produced a large local burst,
  but failed price survival and should be 4B/event-burst, not Green.
```

Shared rule:

```text
C09 is not "advanced equipment stock went up."
C09 is "advanced equipment evidence supports the valuation after the spike through customer orders, delivery timing, margin, and price survival."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C09_R2L92_084370_2024_03_21","scheduled_round":"R2","scheduled_loop":92,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE","symbol":"084370","name":"유진테크","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":41450,"peak_high":60000,"peak_date":"2024-05-28","worst_low":35350,"worst_low_date":"2024-09-11","mfe_pct":44.8,"mae_pct":-14.7,"peak_to_later_low_drawdown_pct":-41.1,"classification":"positive_with_local_4b_deposition_equipment_rerating","calibration_usable":true,"evidence_family":"advanced_deposition_equipment_customer_order_margin_bridge","residual_error":"positive_entry_but_valuation_blowoff_requires_local_4b_after_peak_drawdown","shadow_rule_candidate":"allow_actionable_when_customer_order_margin_bridge_confirms; attach_4b_after_large_mfe_drawdown"}
{"row_type":"case","case_id":"C09_R2L92_240810_2024_03_20","scheduled_round":"R2","scheduled_loop":92,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE","symbol":"240810","name":"원익IPS","trigger_date":"2024-03-20","entry_date":"2024-03-20","entry_price":37400,"peak_high":44850,"peak_date":"2024-04-08","worst_low":22200,"worst_low_date":"2024-11-14","mfe_pct":19.9,"mae_pct":-40.6,"classification":"hard_4c_candidate_large_equipment_cycle_label_without_revision_bridge","calibration_usable":true,"evidence_family":"large_semiconductor_equipment_cycle_label_without_fresh_order_margin_bridge","residual_error":"equipment_cycle_label_can_overpromote_without_company_specific_revision_bridge","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_order_margin_bridge_missing"}
{"row_type":"case","case_id":"C09_R2L92_036810_2024_04_09","scheduled_round":"R2","scheduled_loop":92,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE","symbol":"036810","name":"에프에스티","trigger_date":"2024-04-09","entry_date":"2024-04-09","entry_price":27900,"peak_high":41850,"peak_date":"2024-06-11","worst_low":16200,"worst_low_date":"2024-11-20","mfe_pct":50.0,"mae_pct":-41.9,"peak_to_later_low_drawdown_pct":-61.3,"classification":"local_burst_high_mae_euv_pellicle_advanced_label_without_durable_order_bridge","calibration_usable":true,"evidence_family":"euv_pellicle_advanced_equipment_label_local_burst_without_durable_order_margin_bridge","residual_error":"advanced_equipment_label_can_create_large_mfe_but_fail_green_without_price_survival","shadow_rule_candidate":"classify_high_mfe_high_mae_advanced_label_spikes_as_local_4b_not_green"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":92,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","fine_archetype_id":"ADVANCED_SEMI_EQUIPMENT_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_VS_EUV_HBM_EQUIPMENT_LABEL_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"local_4b_overlay_case_count":2,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":92,"canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","rule_id":"C09_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C09, do not open Stage3-Green from advanced equipment, EUV/pellicle, HBM equipment, memory capex, or AI semiconductor equipment label alone. Require customer qualification, order or shipment visibility, delivery timing, utilization, margin bridge, valuation discipline, and post-trigger price survival. If MFE is shallow and MAE is large, route to hard-4C. If MFE is large but peak-to-later-low drawdown is large, classify as local 4B/event burst unless a fresh revision bridge appears.","expected_effect":"Reduce advanced-equipment valuation blowoff false positives while preserving true equipment positives with order, delivery, margin, and price-survival evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":92,"canonical_archetype_id":"C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF","residual_type":"advanced_equipment_valuation_blowoff_guard","contribution":"Adds one advanced-equipment positive with 4B watch, one large-equipment hard-4C candidate, and one EUV/pellicle local-burst failure to calibrate C09 valuation and price-survival routing.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C09_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF:

  Do not open Stage3-Green from:
    - advanced semiconductor equipment label alone
    - EUV / pellicle / mask / deposition label alone
    - HBM equipment readthrough alone
    - memory capex recovery label alone
    - one-week equipment-volume spike alone

  Require at least two of:
    - customer qualification
    - order or shipment visibility
    - delivery timing
    - utilization improvement
    - margin or OP bridge
    - valuation discipline after price acceleration
    - low-MAE post-trigger price survival
    - fresh revision after the initial spike

  If MFE < 20% and MAE < -35%:
    route to C09 hard-4C candidate.

  If MFE > 35% but peak-to-later-low drawdown < -35%:
    preserve positive or event-burst label only with local 4B watch.

  If MFE > 45% and MAE < -40%:
    classify as local 4B / blowoff failure, not Green, unless a new order/margin revision bridge appears.

  Distinguish:
    - equipment names with real order/margin bridge and price survival
    - from broad equipment-beta or advanced-label spikes where valuation outruns evidence.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_92_L2_AI_SEMICONDUCTOR_ELECTRONICS_C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C09 advanced equipment valuation blowoff cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C09_VALUATION_BLOWOFF_ORDER_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C09 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C09 cases agree, consider implementing a canonical guard that:
   - blocks advanced-equipment Green without order/delivery/margin bridge,
   - preserves true equipment positives with price survival,
   - attaches local 4B after large MFE and deep peak drawdown,
   - routes shallow-MFE/high-MAE equipment-cycle cases to hard-4C,
   - treats high-MFE/high-MAE EUV/pellicle spikes as local 4B rather than Green.

Expected next schedule:
completed_round = R2
completed_loop = 92
next_round = R3
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 92
next_round = R3
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```
