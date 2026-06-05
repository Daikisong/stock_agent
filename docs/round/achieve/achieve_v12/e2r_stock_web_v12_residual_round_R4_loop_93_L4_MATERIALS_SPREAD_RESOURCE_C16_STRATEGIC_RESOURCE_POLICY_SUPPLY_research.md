# E2R Stock-Web v12 Residual Research — R4 / Loop 93

```yaml
scheduled_round: R4
scheduled_loop: 93
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE

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

completed_round: R4
completed_loop: 93
next_round: R5
next_loop: 93
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R3_loop_93_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R4
scheduled_loop = 93
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

R4 hard gate requires:

```text
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
```

Recent R4 branch usage already covered:

```text
loop90: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
loop91: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
loop92: C15_MATERIAL_SPREAD_SUPERCYCLE
```

This run returns to C16, but avoids the top-covered strategic-resource names and uses a different fine branch:

```text
lithium recycling / POSCO resource readthrough / industrial mineral supply bridge
vs generic strategic-resource theme spike
```

---

## 2. No-repeat / novelty check

No-Repeat Index coverage snapshot:

```text
C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
rows: 36
symbols: 23
date_range: 2022-10-20~2024-10-11
good/bad S2: 14/9
4B/4C: 2/0
URL pending/proxy: 17/17
top covered symbols:
  047400(6), 005490(3), 012320(3), 001570(2), 081150(2), 101670(2)
```

Selected symbols:

```text
005420 코스모화학
009520 포스코엠텍
014580 태경비케이
```

They avoid the C16 top-covered symbols and avoid recent R4 loop91~92 names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
005420: same archetype, new symbol, lithium/recycling strategic-resource rebound positive with local 4B watch
009520: same archetype, new symbol, POSCO resource readthrough / lithium-theme false-positive branch
014580: same archetype, new symbol, industrial mineral / supply theme shallow-MFE high-MAE guardrail branch
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
005420 코스모화학
  profile: atlas/symbol_profiles/005/005420.json
  name history:
    한국티타늄 until 2003-07-07
    코스모화학 from 2003-07-08
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,697
  corporate_action_candidate_dates:
    1998-12-21, 2000-04-11, 2000-08-14, 2001-09-28,
    2003-06-18, 2004-05-06, 2019-12-24
  2024 entry~D+180 contamination: none

009520 포스코엠텍
  profile: atlas/symbol_profiles/009/009520.json
  name history:
    삼정강업 until 2001-04-18
    삼정피앤에이 until 2011-03-30
    포스코엠텍 from 2011-03-31
  market:
    KOSDAQ until 2024-06-13
    KOSDAQ GLOBAL from 2024-06-14
  first_date: 1997-11-10
  last_date: 2026-02-20
  tradable_ohlcv rows: 6,770
  corporate_action_candidate_dates:
    1999-03-30, 1999-04-22, 2011-01-05, 2012-05-14
  2024 entry~D+180 contamination: none

014580 태경비케이
  profile: atlas/symbol_profiles/014/014580.json
  name history:
    백광소재 until 2020-04-21
    태경비케이 from 2020-04-22
  first_date: 1995-05-02
  last_date: 2026-02-20
  tradable_ohlcv rows: 7,738
  corporate_action_candidate_dates:
    1997-01-03, 2005-05-17, 2015-05-13
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C16 is about strategic-resource policy and supply, not a generic "resource theme."

The model can over-score:

```text
lithium / recycling / rare-metal label
POSCO resource readthrough
industrial mineral / graphite / lime / supply-chain label
critical-mineral policy headline
one-day resource-theme volume spike
```

The C16 bridge must be stricter:

```text
strategic-resource policy or supply shock
  -> company-specific resource exposure
  -> supply availability or processing capacity
  -> customer / offtake / pricing bridge
  -> input-cost and inventory risk
  -> margin / OP conversion
  -> price survival after the first resource-theme spike
```

A strategic-resource headline is a map with a red circle on it. C16 asks whether the company actually owns the mine, refinery, process, customer contract, or price spread inside that circle.

---

## 5. Case 1 — 005420 코스모화학

```yaml
case_id: C16_R4L93_005420_2024_09_02
symbol: "005420"
name: "코스모화학"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE
trigger_date: 2024-09-02
entry_date: 2024-09-02
entry_price_basis: close
entry_price: 21450
classification: local_positive_lithium_recycling_resource_rebound_with_4b_watch
calibration_usable: true
```

### Evidence interpretation

코스모화학 is the constructive control, but with a local 4B cap.

The useful C16 read is not simply:

```text
lithium / battery raw-material name
```

It is:

```text
lithium/recycling/resource-processing relevance
  -> resource theme rebound
  -> visible price confirmation
  -> later price survival check
```

The price path produced a meaningful rebound from the September trigger, but the path was volatile and should not be treated as unlimited Green without customer/offtake/margin evidence.

### Price path

Key Stock-Web rows:

```text
2024-09-02: high 22,550 / close 21,450
2024-09-10: low 17,450 / close 17,530
2024-09-26: high 24,200 / close 24,150
2024-09-27: high 25,600 / close 25,100
2024-09-30: high 25,750 / close 23,550
2024-10-16: low 21,900 / close 22,000
2024-11-07: low 18,620 area after later weakness
```

Approximate path from entry close:

```text
entry_close: 21,450
peak_high: 25,750
MFE: +20.0%
worst_low_after_entry_checked: 17,450
MAE: -18.6%
```

### Interpretation

This is a local-positive / capped case:

```text
Stage2-Actionable: allowed if lithium/recycling supply and margin bridge are explicit.
Stage3-Green: blocked without customer/offtake, processing capacity, and margin evidence.
Local 4B: required because MAE was material even though MFE was useful.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  strategic_resource_relevance: high
  lithium_recycling_processing_bridge: medium_high
  customer_offtake_visibility: medium_or_unclear
  price_confirmation: medium_high
  drawdown_penalty: medium_high
  local_4b_overlay: required
```

---

## 6. Case 2 — 009520 포스코엠텍

```yaml
case_id: C16_R4L93_009520_2024_02_21
symbol: "009520"
name: "포스코엠텍"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE
trigger_date: 2024-02-21
entry_date: 2024-02-21
entry_price_basis: close
entry_price: 25250
classification: hard_4c_candidate_posco_resource_readthrough_without_company_specific_margin_bridge
calibration_usable: true
```

### Evidence interpretation

포스코엠텍 is the POSCO-resource readthrough false-positive.

The model can be tempted by:

```text
POSCO group resource ecosystem
lithium / secondary battery materials readthrough
strategic mineral policy theme
```

But C16 should not promote readthrough into Green unless the company-specific bridge is explicit. The forward path after the February trigger had almost no useful MFE and a large drawdown.

### Price path

Key Stock-Web rows:

```text
2024-02-21: high 25,700 / close 25,250
2024-02-22: high 26,100 / close 25,250
2024-03-08: low 23,150 / close 23,450
2024-04-17: low 18,700 / close 18,700
2024-08-05: low 14,660 / close 14,820
2024-09-02: high 20,550 / close 19,190
```

Approximate path from entry close:

```text
entry_close: 25,250
peak_high: 26,100
MFE: +3.4%
worst_low: 14,660
MAE: -41.9%
```

### Interpretation

This is a hard C16 guardrail case:

```text
Stage2-Watch: possible from strategic-resource / POSCO ecosystem relevance.
Stage2-Actionable: blocked unless company-specific resource processing, offtake, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes.
```

The lesson is that ecosystem readthrough is not operating leverage.

### Stress-test components

```text
raw_component_score_proxy:
  group_resource_readthrough: high
  direct_resource_margin_bridge: weak
  offtake_or_pricing_visibility: weak
  price_confirmation: failed
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 7. Case 3 — 014580 태경비케이

```yaml
case_id: C16_R4L93_014580_2024_05_17
symbol: "014580"
name: "태경비케이"
canonical_archetype_id: C16_STRATEGIC_RESOURCE_POLICY_SUPPLY
fine_archetype_id: LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE
trigger_date: 2024-05-17
entry_date: 2024-05-17
entry_price_basis: close
entry_price: 6010
classification: hard_4c_candidate_industrial_mineral_supply_theme_without_durable_spread_bridge
calibration_usable: true
```

### Evidence interpretation

태경비케이 is the industrial-mineral supply-theme guardrail.

Industrial minerals and resource-supply labels can create a plausible C16 story:

```text
mineral supply / lime / industrial material label
resource policy sympathy
commodity-supply bottleneck theme
```

But the forward path did not support Actionable or Green. The initial MFE was shallow and later MAE was large.

### Price path

Key Stock-Web rows:

```text
2024-05-17: close 6,010
2024-05-21: high 6,050 / close 6,000
2024-05-22: high 6,320 / close 6,070
2024-06-14: low 5,350 / close 5,360
2024-08-05: low 3,925 / close 4,230
2024-09-09: low 4,125 / close 4,265
```

Approximate path from entry close:

```text
entry_close: 6,010
peak_high: 6,320
MFE: +5.2%
worst_low: 3,925
MAE: -34.7%
```

### Interpretation

This is a hard C16 false-positive:

```text
Stage2-Watch: possible from industrial-mineral / supply-chain label.
Stage2-Actionable: blocked unless resource spread, customer demand, and margin bridge are explicit.
Stage3-Green: blocked.
Hard 4C: yes by shallow MFE and high MAE.
```

The lesson is that resource-supply adjacency does not automatically create strategic-resource pricing power.

### Stress-test components

```text
raw_component_score_proxy:
  industrial_mineral_label: medium_high
  strategic_resource_directness: weak_to_medium
  spread_margin_bridge: weak
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
hard_4c_candidate_count: 2
calibration_usable_trigger_count: 3
```

The three-case C16 grid:

```text
005420 코스모화학:
  lithium/recycling resource rebound worked locally,
  but it requires 4B and fresh offtake/margin bridge before Green.

009520 포스코엠텍:
  POSCO-resource readthrough failed.
  Shallow MFE and high MAE, hard 4C.

014580 태경비케이:
  industrial-mineral supply label failed.
  Shallow MFE and high MAE, hard 4C.
```

Shared rule:

```text
C16 is not "strategic resource label."
C16 is "the company has direct resource exposure, supply control, processing capacity, pricing/offtake bridge, and margin conversion."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C16_R4L93_005420_2024_09_02","scheduled_round":"R4","scheduled_loop":93,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE","symbol":"005420","name":"코스모화학","trigger_date":"2024-09-02","entry_date":"2024-09-02","entry_price":21450,"peak_high":25750,"peak_date":"2024-09-30","worst_low_after_entry":17450,"worst_low_after_entry_date":"2024-09-10","mfe_pct":20.0,"mae_pct":-18.6,"classification":"local_positive_lithium_recycling_resource_rebound_with_4b_watch","calibration_usable":true,"evidence_family":"lithium_recycling_resource_processing_rebound_without_fresh_offtake_margin_bridge","residual_error":"local_resource_rebound_requires_4b_and_green_block_without_customer_offtake_margin_evidence","shadow_rule_candidate":"allow_actionable_when_resource_processing_offtake_margin_bridge_confirms_but_attach_4b_after_material_mae"}
{"row_type":"case","case_id":"C16_R4L93_009520_2024_02_21","scheduled_round":"R4","scheduled_loop":93,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE","symbol":"009520","name":"포스코엠텍","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":25250,"peak_high":26100,"peak_date":"2024-02-22","worst_low":14660,"worst_low_date":"2024-08-05","mfe_pct":3.4,"mae_pct":-41.9,"classification":"hard_4c_candidate_posco_resource_readthrough_without_company_specific_margin_bridge","calibration_usable":true,"evidence_family":"posco_resource_lithium_readthrough_without_company_specific_offtake_margin_bridge","residual_error":"resource_ecosystem_readthrough_can_overpromote_without_direct_margin_conversion","shadow_rule_candidate":"route_group_resource_readthrough_to_hard_4c_if_mfe_shallow_mae_large_and_direct_bridge_missing"}
{"row_type":"case","case_id":"C16_R4L93_014580_2024_05_17","scheduled_round":"R4","scheduled_loop":93,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE","symbol":"014580","name":"태경비케이","trigger_date":"2024-05-17","entry_date":"2024-05-17","entry_price":6010,"peak_high":6320,"peak_date":"2024-05-22","worst_low":3925,"worst_low_date":"2024-08-05","mfe_pct":5.2,"mae_pct":-34.7,"classification":"hard_4c_candidate_industrial_mineral_supply_theme_without_durable_spread_bridge","calibration_usable":true,"evidence_family":"industrial_mineral_supply_label_without_resource_spread_margin_bridge","residual_error":"resource_supply_adjacency_can_fail_without_pricing_power_and_margin_conversion","shadow_rule_candidate":"route_industrial_mineral_supply_label_to_hard_4c_if_mfe_shallow_mae_large_and_spread_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R4","scheduled_loop":93,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","fine_archetype_id":"LITHIUM_RECYCLING_POSCO_RESOURCE_INDUSTRIAL_MINERAL_SUPPLY_BRIDGE_VS_STRATEGIC_RESOURCE_THEME_SPIKE","case_count":3,"positive_case_count":1,"counterexample_count":2,"watch_or_cap_case_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":2,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R4","scheduled_loop":93,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","rule_id":"C16_DIRECT_RESOURCE_SUPPLY_OFFTAKE_MARGIN_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C16, do not open Stage2-Actionable or Stage3-Green from strategic-resource policy, lithium/recycling, POSCO-resource readthrough, industrial-mineral, critical-mineral, or one-day resource-theme spike labels alone. Require direct resource exposure, supply availability or processing capacity, customer/offtake or pricing bridge, input-cost and inventory risk check, margin/OP conversion, and post-trigger price survival. Local resource rebounds with material MAE should remain local 4B unless fresh offtake/margin evidence appears. Group ecosystem readthrough or industrial-mineral adjacency with shallow MFE and high MAE should route to hard-4C when direct resource economics are missing.","expected_effect":"Reduce strategic-resource label false positives while preserving true resource-supply positives with direct exposure, offtake, pricing, and margin evidence.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R4","scheduled_loop":93,"canonical_archetype_id":"C16_STRATEGIC_RESOURCE_POLICY_SUPPLY","residual_type":"strategic_resource_supply_offtake_margin_guard","contribution":"Adds one lithium/recycling local-positive with 4B watch and two resource-readthrough/industrial-mineral hard-4C counterexamples to calibrate C16 direct-supply and margin-conversion requirements.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C16_DIRECT_RESOURCE_SUPPLY_OFFTAKE_MARGIN_BRIDGE_REQUIRED

IF canonical_archetype_id == C16_STRATEGIC_RESOURCE_POLICY_SUPPLY:

  Do not open Stage3-Green from:
    - strategic-resource policy headline alone
    - lithium / recycling / rare-metal label alone
    - group ecosystem resource readthrough alone
    - industrial-mineral / supply-chain adjacency alone
    - one-day resource-theme volume spike alone

  Require at least two of:
    - direct resource exposure
    - supply availability or processing capacity
    - customer / offtake contract
    - pricing or spread bridge
    - input-cost / inventory risk containment
    - margin / OP conversion
    - low-MAE post-trigger price survival
    - fresh revision after the resource-policy headline

  If MFE < 10% and MAE < -30%:
    route to C16 hard-4C candidate.

  If MFE > 15% but MAE is material and bridge is not explicit:
    preserve as local 4B / Watch, not Green.

  Distinguish:
    - true resource-processing names with direct supply and offtake economics
    - from group readthrough or industrial-mineral labels where the strategic-resource economics are indirect.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R4_loop_93_L4_MATERIALS_SPREAD_RESOURCE_C16_STRATEGIC_RESOURCE_POLICY_SUPPLY_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C16 strategic-resource policy/supply cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C16_DIRECT_RESOURCE_SUPPLY_OFFTAKE_MARGIN_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C16 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C16 cases agree, consider implementing a canonical guard that:
   - blocks resource-label Green without direct exposure, offtake, pricing, and margin bridge,
   - preserves local lithium/recycling positives only with price survival or fresh evidence,
   - attaches local 4B after meaningful MFE with material MAE,
   - routes shallow-MFE/high-MAE group-resource readthrough and industrial-mineral labels to hard-4C.

Expected next schedule:
completed_round = R4
completed_loop = 93
next_round = R5
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R4
completed_loop = 93
next_round = R5
next_loop = 93
round_schedule_status = valid
round_sector_consistency = pass
```
