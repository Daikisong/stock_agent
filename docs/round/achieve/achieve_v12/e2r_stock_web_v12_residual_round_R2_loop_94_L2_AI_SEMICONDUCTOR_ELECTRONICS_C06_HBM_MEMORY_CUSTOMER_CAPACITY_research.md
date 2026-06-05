# E2R Stock-Web v12 Residual Research — R2 / Loop 94

```yaml
scheduled_round: R2
scheduled_loop: 94
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA

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

completed_round: R2
completed_loop: 94
next_round: R3
next_loop: 94
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R1_loop_94_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R2
scheduled_loop = 94
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

R2 hard gate requires:

```text
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
```

Recent R2 branch usage already covered:

```text
loop90: C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH
loop91: C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
loop92: C09_ADVANCED_EQUIPMENT_VALUATION_BLOWOFF
loop93: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
```

This run selects the under-covered C06 branch:

```text
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
```

The selected fine branch is:

```text
AI memory / semiconductor materials / package substrate / display-material customer capacity bridge
vs broad memory-label beta
```

This deliberately avoids the C06 top-covered primary memory names and focuses on adjacent materials/substrate names where the model can confuse "AI memory capacity is tight" with direct company-specific order/margin conversion.

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C06_HBM_MEMORY_CUSTOMER_CAPACITY
rows: 7
symbols: 6
date_range: 2023-09-14~2024-07-05
good/bad S2: 4/1
4B/4C: 0/0
URL pending/proxy: 3/0
top covered symbols:
  000660(2), 005930(1), 009150(1), 014680(1), 067310(1), 402340(1)
```

Selected symbols:

```text
005290 동진쎄미켐
222800 심텍
272290 이녹스첨단소재
```

They avoid the C06 top-covered list and avoid the most recent R2 loop93 C10 names:

```text
036930, 053610, 083310
```

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
005290: same archetype, new symbol, semiconductor material local-positive with 4B after memory/AI-material rally
222800: same archetype, new symbol, package-substrate / memory capacity label hard-4C without customer order survival
272290: same archetype, new symbol, display/advanced-materials memory-readthrough Watch cap without direct HBM customer bridge
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
005290 동진쎄미켐
  profile: atlas/symbol_profiles/005/005290.json
  first_date: 1999-12-21
  last_date: 2026-02-20
  market: KOSDAQ
  tradable_ohlcv rows: 6,445
  corporate_action_candidate_dates:
    historical only in profile outside 2024 validation window
  2024 entry~D+180 contamination: none

222800 심텍
  profile: atlas/symbol_profiles/222/222800.json
  first_date: 2015-08-07
  last_date: 2026-02-20
  market:
    KOSDAQ until 2024-06-13
    KOSDAQ GLOBAL from 2024-06-14
  tradable_ohlcv rows: 2,584
  corporate_action_candidate_dates:
    2015-09-22, 2020-05-20
  2024 entry~D+180 contamination: none

272290 이녹스첨단소재
  profile: atlas/symbol_profiles/272/272290.json
  first_date: 2017-07-10
  last_date: 2026-02-20
  market:
    KOSDAQ until 2022-11-18
    KOSDAQ GLOBAL from 2022-11-21
  tradable_ohlcv rows: 2,112
  corporate_action_candidate_dates:
    2021-09-01, 2021-09-24
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C06 is about customer capacity and memory/HBM demand reaching the company. It is not a generic "AI memory is strong" or "semiconductor material stock" label.

The model can over-score:

```text
HBM / AI memory headline
DRAM/NAND recovery
semiconductor material label
package substrate label
advanced display/materials readthrough
one-week memory-material volume spike
```

The C06 bridge must be stricter:

```text
AI memory / HBM capacity tightness
  -> named customer capacity plan
  -> company-specific qualification or supply slot
  -> purchase order / shipment / utilization
  -> ASP, mix, or margin bridge
  -> working-capital and inventory risk check
  -> price survival after the first memory-material rally
```

A memory-capacity headline is like hearing a factory needs more parts. C06 asks whether this company is actually on the qualified vendor list, receives the order, ships the part, and keeps margin.

---

## 5. Case 1 — 005290 동진쎄미켐

```yaml
case_id: C06_R2L94_005290_2024_02_28
symbol: "005290"
name: "동진쎄미켐"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA
trigger_date: 2024-02-28
entry_date: 2024-02-28
entry_price_basis: close
entry_price: 36800
classification: local_positive_semiconductor_material_memory_capacity_rebound_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

동진쎄미켐 is the constructive control, but only as a local-positive / 4B case.

The useful C06 read is:

```text
semiconductor materials relevance
  -> memory/customer capacity recovery readthrough
  -> local price confirmation
  -> but no durable price survival without fresh customer and margin bridge
```

The stock produced a meaningful local MFE into March/April, then gave back the move. That makes it a valid event/memory-material positive at entry, but not an unrestricted Green.

### Price path

Key Stock-Web rows:

```text
2024-02-28: close 36,800
2024-03-06: high 41,650 / close 41,500
2024-03-21: high 48,700 / close 47,950
2024-03-29: high 49,700 / close 48,250
2024-04-01: high 51,500 / close 50,100
2024-08-05: low 28,750 / close 29,650
2024-09-19: low 26,200 / close 27,250
```

Approximate path from entry close:

```text
entry_close: 36,800
peak_high: 51,500
MFE: +39.9%
worst_low_after_entry: 26,200
MAE: -28.8%
```

### Interpretation

This is a C06 local positive with 4B:

```text
Stage2-Actionable: allowed if customer capacity, qualification, and shipment bridge are explicit.
Stage3-Green: blocked without fresh order/margin evidence after the rally.
Local 4B: required because useful MFE later became material MAE.
Hard 4C: no for the original local-positive entry.
```

### Stress-test components

```text
raw_component_score_proxy:
  memory_material_relevance: high
  customer_capacity_bridge: medium
  qualification_shipment_bridge: weak_to_medium
  price_confirmation: high_initial
  post_rally_survival: failed
  local_4b_overlay: required
```

---

## 6. Case 2 — 222800 심텍

```yaml
case_id: C06_R2L94_222800_2024_03_21
symbol: "222800"
name: "심텍"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA
trigger_date: 2024-03-21
entry_date: 2024-03-21
entry_price_basis: close
entry_price: 31150
classification: hard_4c_candidate_package_substrate_memory_capacity_label_without_customer_order_survival
calibration_usable: true
```

### Evidence interpretation

심텍 is the package-substrate / memory-capacity hard guardrail.

The setup can look plausible:

```text
memory module / package substrate label
  -> AI memory and HBM capacity readthrough
  -> customer restocking hope
```

But the price path did not validate durable order, shipment, or margin conversion. MFE was shallow, and later MAE became extreme.

### Price path

Key Stock-Web rows:

```text
2024-03-21: high 31,400 / close 31,150
2024-04-02: high 34,450 / close 33,000
2024-05-09: high 33,600 / close 33,350
2024-08-05: low 22,950 / close 23,800
2024-09-06: low 17,380 / close 17,580
2024-10-25: low 15,700 / close 15,880
```

Approximate path from entry close:

```text
entry_close: 31,150
peak_high: 34,450
MFE: +10.6%
worst_low_after_entry: 15,700
MAE: -49.6%
```

### Interpretation

This is a hard C06 false-positive:

```text
Stage2-Watch: possible from substrate / memory-capacity relevance.
Stage2-Actionable: blocked unless named customer order, shipment, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and extreme MAE.
```

The lesson is that package-substrate adjacency is not customer capacity allocation.

### Stress-test components

```text
raw_component_score_proxy:
  package_substrate_label: high
  memory_capacity_readthrough: medium_high
  direct_customer_order_bridge: weak
  shipment_utilization_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: extreme
  hard_4c_guard: yes
```

---

## 7. Case 3 — 272290 이녹스첨단소재

```yaml
case_id: C06_R2L94_272290_2024_02_29
symbol: "272290"
name: "이녹스첨단소재"
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA
trigger_date: 2024-02-29
entry_date: 2024-02-29
entry_price_basis: close
entry_price: 31650
classification: watch_cap_advanced_materials_memory_readthrough_without_direct_hbm_customer_bridge
calibration_usable: true
```

### Evidence interpretation

이녹스첨단소재 is the advanced-materials Watch cap.

The company can participate in electronics/materials recovery, but C06 should not promote:

```text
advanced materials
display / semiconductor materials readthrough
AI memory sympathy
```

into Green unless the memory/HBM customer bridge is direct. The price path gave only shallow MFE and then a material drawdown.

### Price path

Key Stock-Web rows:

```text
2024-02-29: close 31,650
2024-03-07: high 33,900 / close 33,100
2024-04-03: low 28,000 / close 28,100
2024-04-29: high 31,950 / close 31,700
2024-08-05: low 24,500 / close 25,200
2024-10-25: low 22,750 / close 22,900
```

Approximate path from entry close:

```text
entry_close: 31,650
peak_high: 33,900
MFE: +7.1%
worst_low_after_entry: 22,750
MAE: -28.1%
```

### Interpretation

This is a Watch/Yellow cap case:

```text
Stage2-Watch: valid from advanced-materials / electronics recovery relevance.
Stage2-Actionable: blocked unless direct memory customer capacity and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: borderline, but Watch/Yellow cap is more appropriate because MAE did not cross the extreme threshold.
```

The lesson is that broad advanced-materials relevance should not be used as a proxy for HBM capacity allocation.

### Stress-test components

```text
raw_component_score_proxy:
  advanced_materials_relevance: medium_high
  ai_memory_readthrough: medium
  direct_hbm_customer_bridge: weak
  shipment_margin_bridge: weak
  price_confirmation: shallow
  drawdown_penalty: medium_high
  actionability_cap: Watch/Yellow
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

The three-case C06 grid:

```text
005290 동진쎄미켐:
  semiconductor-material memory-capacity rebound worked locally;
  useful MFE came first, but later high MAE requires local 4B.

222800 심텍:
  package-substrate / memory-capacity label failed;
  shallow MFE and extreme MAE, hard 4C.

272290 이녹스첨단소재:
  advanced-materials readthrough did not validate direct HBM/customer capacity bridge;
  Watch/Yellow cap.
```

Shared rule:

```text
C06 is not "AI memory is hot."
C06 is "named customer capacity becomes qualified supply, order, shipment, utilization, and margin for this company."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C06_R2L94_005290_2024_02_28","scheduled_round":"R2","scheduled_loop":94,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA","symbol":"005290","name":"동진쎄미켐","trigger_date":"2024-02-28","entry_date":"2024-02-28","entry_price":36800,"peak_high":51500,"peak_date":"2024-04-01","worst_low_after_entry":26200,"worst_low_after_entry_date":"2024-09-19","mfe_pct":39.9,"mae_pct":-28.8,"classification":"local_positive_semiconductor_material_memory_capacity_rebound_with_4b_watch","calibration_usable":true,"evidence_family":"semiconductor_material_customer_capacity_rebound_without_fresh_order_margin_bridge","residual_error":"local_memory_material_positive_requires_4b_after_later_mae_without_customer_order_margin_evidence","shadow_rule_candidate":"allow_actionable_when_customer_capacity_qualification_shipment_bridge_confirms_but_attach_4b_after_material_mae"}
{"row_type":"case","case_id":"C06_R2L94_222800_2024_03_21","scheduled_round":"R2","scheduled_loop":94,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA","symbol":"222800","name":"심텍","trigger_date":"2024-03-21","entry_date":"2024-03-21","entry_price":31150,"peak_high":34450,"peak_date":"2024-04-02","worst_low_after_entry":15700,"worst_low_after_entry_date":"2024-10-25","mfe_pct":10.6,"mae_pct":-49.6,"classification":"hard_4c_candidate_package_substrate_memory_capacity_label_without_customer_order_survival","calibration_usable":true,"evidence_family":"package_substrate_memory_capacity_readthrough_without_customer_order_shipment_margin_bridge","residual_error":"substrate_adjacency_can_overpromote_without_customer_capacity_allocation","shadow_rule_candidate":"route_substrate_memory_capacity_label_to_hard_4c_if_mfe_shallow_mae_extreme_and_order_bridge_missing"}
{"row_type":"case","case_id":"C06_R2L94_272290_2024_02_29","scheduled_round":"R2","scheduled_loop":94,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA","symbol":"272290","name":"이녹스첨단소재","trigger_date":"2024-02-29","entry_date":"2024-02-29","entry_price":31650,"peak_high":33900,"peak_date":"2024-03-07","worst_low_after_entry":22750,"worst_low_after_entry_date":"2024-10-25","mfe_pct":7.1,"mae_pct":-28.1,"classification":"watch_cap_advanced_materials_memory_readthrough_without_direct_hbm_customer_bridge","calibration_usable":true,"evidence_family":"advanced_materials_memory_readthrough_without_direct_hbm_customer_capacity_bridge","residual_error":"broad_advanced_materials_relevance_can_overpromote_without_direct_memory_customer_bridge","shadow_rule_candidate":"cap_advanced_materials_memory_readthrough_at_watch_yellow_if_mfe_shallow_and_customer_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R2","scheduled_loop":94,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"AI_MEMORY_MATERIALS_SUBSTRATE_CUSTOMER_CAPACITY_BRIDGE_VS_MEMORY_LABEL_BETA","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R2","scheduled_loop":94,"canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","rule_id":"C06_CUSTOMER_CAPACITY_QUALIFICATION_SHIPMENT_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C06, do not open Stage2-Actionable or Stage3-Green from HBM/AI memory, DRAM/NAND recovery, semiconductor material, package substrate, advanced materials, or one-week memory-material spike labels alone. Require named customer capacity plan, qualification or approved-vendor status, purchase order or shipment visibility, utilization or supply-slot evidence, ASP/mix/margin bridge, working-capital/inventory risk check, and post-trigger price survival. Semiconductor-material positives with meaningful MFE but material later MAE should remain local 4B unless fresh customer/order/margin evidence appears. Package-substrate labels with shallow MFE and extreme MAE should route to hard-4C when order and capacity-allocation bridge are missing. Broad advanced-materials readthrough should cap at Watch/Yellow without direct HBM/customer bridge.","expected_effect":"Reduce AI-memory material/substrate false positives while preserving true customer-capacity positives with qualification, order, shipment, utilization, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R2","scheduled_loop":94,"canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","residual_type":"customer_capacity_qualification_shipment_margin_guard","contribution":"Adds one semiconductor-material local positive with 4B watch, one package-substrate hard-4C, and one advanced-materials Watch cap to calibrate C06 customer capacity and order-shipment requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C06_CUSTOMER_CAPACITY_QUALIFICATION_SHIPMENT_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C06_HBM_MEMORY_CUSTOMER_CAPACITY:

  Do not open Stage3-Green from:
    - HBM / AI memory headline alone
    - DRAM / NAND recovery label alone
    - semiconductor material label alone
    - package substrate label alone
    - advanced materials readthrough alone
    - one-week memory-material volume spike alone

  Require at least two of:
    - named customer capacity plan
    - qualification / approved-vendor status
    - purchase order or shipment visibility
    - utilization or supply-slot evidence
    - ASP / mix / margin bridge
    - working-capital or inventory-risk containment
    - low-MAE post-trigger price survival
    - fresh evidence after the memory-capacity headline

  If MFE < 15% and MAE < -40%:
    route to C06 hard-4C candidate.

  If MFE > 30% but later MAE is material:
    preserve as local 4B unless fresh customer/order/margin evidence appears.

  If MFE is shallow and the bridge is broad readthrough:
    cap at Watch/Yellow.

  Distinguish:
    - direct materials/substrate cases with named customer qualification and shipment
    - from broad semiconductor-material or advanced-material labels where AI-memory demand does not reach orders.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R2_loop_94_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C06 AI/HBM memory customer-capacity cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C06_CUSTOMER_CAPACITY_QUALIFICATION_SHIPMENT_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C06 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C06 cases agree, consider implementing a canonical guard that:
   - blocks AI-memory/material/substrate Green without named customer capacity, qualification, shipment, and margin bridge,
   - preserves local semiconductor-material positives only with price survival and fresh order evidence,
   - attaches local 4B after meaningful MFE followed by material MAE,
   - routes shallow-MFE/high-MAE substrate labels to hard-4C,
   - caps broad advanced-materials readthrough at Watch/Yellow.

Expected next schedule:
completed_round = R2
completed_loop = 94
next_round = R3
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R2
completed_loop = 94
next_round = R3
next_loop = 94
round_schedule_status = valid
round_sector_consistency = pass
```
