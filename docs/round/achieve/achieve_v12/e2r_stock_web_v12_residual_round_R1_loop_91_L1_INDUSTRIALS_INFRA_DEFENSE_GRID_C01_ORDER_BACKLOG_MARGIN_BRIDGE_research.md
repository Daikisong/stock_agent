# E2R Stock-Web v12 Residual Research — R1 / Loop 91

```yaml
scheduled_round: R1
scheduled_loop: 91
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA

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
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3

loop_contribution_label: residual_error_found
canonical_archetype_rule_candidate: true
do_not_propose_new_weight_delta: true

completed_round: R1
completed_loop: 91
next_round: R2
next_loop: 91
round_schedule_status: valid
round_sector_consistency: pass
```

---

## 1. Schedule resolution

Previous completed file in the active sequence was:

```text
e2r_stock_web_v12_residual_round_R13_loop_90_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_R13_CROSS_ARCHETYPE_4B_4C_REDTEAM_research.md
```

Under v12:

```text
R1 -> R2 -> R3 -> R4 -> R5 -> R6 -> R7 -> R8 -> R9 -> R10 -> R11 -> R12 -> R13 -> R1
```

Therefore:

```text
scheduled_round = R1
scheduled_loop = 91
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
```

Recent R1 branch usage already covered:

```text
loop88: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
loop89: C02_POWER_GRID_DATACENTER_CAPEX
loop90: C03_DEFENSE_EXPORT_FRAMEWORK_BACKLOG
```

This run therefore selects:

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
```

The research goal is not to repeat power-grid or defense-export logic. The focus is the industrial order/backlog margin bridge:

```text
shipbuilding / engine / machinery orderbook
  -> delivery schedule
  -> cost escalation discipline
  -> product mix
  -> margin recovery
  -> OP/EPS conversion
  -> price survival
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
010620 HD현대미포
082740 한화엔진
267270 HD현대건설기계
```

These avoid the top-covered C01 symbols and also avoid the recent R1 loop90 defense names.

Hard duplicate key:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Novelty classification:

```text
010620: same archetype, new symbol, shipbuilding backlog / small-mid vessel margin conversion branch
082740: same archetype, new symbol, marine-engine backlog / ownership-integration / margin conversion branch
267270: same archetype, new symbol, machinery cycle / construction-equipment order headline false-positive branch
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
markets: KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
raw_shard_root: atlas/ohlcv_raw_by_symbol_year
schema_path: atlas/schema.json
universe_path: atlas/universe/all_symbols.csv
```

Profile checks:

```text
010620 HD현대미포
  profile: atlas/symbol_profiles/010/010620.json
  first_date: 1995-05-02
  last_date: 2025-11-26
  raw_last_date: 2025-12-12
  tradable_ohlcv rows: 7,707
  corporate_action_candidate_dates:
    1999-07-14, 2004-01-29, 2018-12-04, 2018-12-26
  2024 entry~D+180 contamination: none
  note: status_inferred is inactive_or_delisted_like because stock-web row presence ends before 2026; use raw/unadjusted historical shard only.

082740 한화엔진
  profile: atlas/symbol_profiles/082/082740.json
  first_date: 2011-01-04
  last_date: 2026-02-20
  tradable_ohlcv rows: 3,710
  corporate_action_candidate_dates:
    2018-06-19, 2021-03-17, 2022-08-25
  2024 entry~D+180 contamination: none

267270 HD현대건설기계
  profile: atlas/symbol_profiles/267/267270.json
  first_date: 2017-05-10
  last_date: 2026-02-20
  tradable_ohlcv rows: 2,154
  corporate_action_candidate_dates:
    2017-11-14, 2017-11-23, 2017-12-06, 2018-11-19, 2018-12-18, 2026-01-26
  2024 entry~D+180 contamination: none
```

---

## 4. Archetype residual problem

C01 is easy to over-score because “order backlog” feels like a bridge by itself.

It is not.

For industrial names, a backlog is like a stack of signed work tickets on the factory desk. It proves future work exists, but it does not prove the work will be profitable. The bridge has to show:

```text
signed backlog
  -> delivery timing
  -> cost lock-in or pass-through
  -> product mix improvement
  -> utilization
  -> margin revision
  -> OP/EPS conversion
```

The failure mode is:

```text
order headline / cycle beta
  -> model opens Stage2-Actionable
  -> margin bridge is missing
  -> MFE is shallow or drawdown arrives first
```

This run tests that failure mode across shipbuilder, engine supplier, and construction-equipment machinery.

---

## 5. Case 1 — 010620 HD현대미포

```yaml
case_id: C01_R1L91_010620_2024_06_24
symbol: "010620"
name: "HD현대미포"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA
trigger_date: 2024-06-24
entry_date: 2024-06-24
entry_price_basis: close
entry_price: 86900
classification: positive_shipbuilding_backlog_margin_bridge
calibration_usable: true
```

### Evidence interpretation

HD현대미포 is the clean shipbuilding positive control. The signal is not just “shipbuilding orders are good.” The price path works because the market appears to reward the more specific bridge:

```text
small/mid vessel shipbuilding backlog
  -> delivery and yard utilization
  -> price discipline
  -> cost normalization
  -> margin recovery expectation
```

The path after entry had a strong MFE before any meaningful drawdown versus entry.

### Price path

Key Stock-Web rows:

```text
2024-06-24: close 86,900
2024-06-25: high 91,700 / close 88,900
2024-07-10: high 102,700 / close 100,100
2024-07-26: high 114,900 / close 113,200
2024-08-01: high 121,900 / close 120,000
2024-11-19: high 121,700 / close 118,200
2025-01-21: high 144,300 / close 141,800
```

Approximate return path from 2024-06-24 close:

```text
entry_close: 86,900
180D_peak_high: 121,900
180D_MFE: +40.3%
extended_peak_high: 144,300
extended_MFE: +66.1%
worst_forward_low_after_entry_in_checked_window: no meaningful break below entry in fetched path
```

### Interpretation

This is a C01 positive:

```text
Stage2-Actionable: valid.
Stage3-Green: allowed only if backlog quality and margin revision are explicit.
Local 4B: not immediate, but monitor after extended +60% path.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  order_backlog_quality: high
  delivery_visibility: medium_high
  margin_recovery_visibility: high
  price_confirmation: high
  drawdown_penalty: low
  local_4b_watch_after_extended_mfe: yes
```

---

## 6. Case 2 — 082740 한화엔진

```yaml
case_id: C01_R1L91_082740_2024_10_04
symbol: "082740"
name: "한화엔진"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA
trigger_date: 2024-10-04
entry_date: 2024-10-04
entry_price_basis: close
entry_price: 14040
classification: positive_with_local_4b_engine_backlog_margin_bridge
calibration_usable: true
```

### Evidence interpretation

한화엔진 is the engine-supplier positive, but with a sharper 4B warning. Marine-engine suppliers can look like pure beta to shipbuilding orders. C01 should not give Green for “shipbuilding up, engine supplier up” alone.

The bridge must be:

```text
engine backlog
  -> capacity allocation
  -> shipyard delivery schedule
  -> parts/labor cost control
  -> ASP and margin expansion
  -> operating leverage
```

The price path after 2024-10-04 confirmed the bridge strongly, but the scale of the 2025 move demands local 4B discipline.

### Price path

Key Stock-Web rows:

```text
2024-10-04: close 14,040
2024-10-17: high 16,500 / close 16,140
2024-11-11: high 16,700 / close 16,390
2025-01-08: high 23,050 / close 21,850
2025-01-15: high 26,250 / close 26,250
2025-02-14: high 28,750 / close 24,350
2025-03-18: high 27,800 / close 26,950
```

Approximate return path from 2024-10-04 close:

```text
entry_close: 14,040
peak_high: 28,750
MFE: +104.8%
worst_forward_low_after_entry_in_checked_window: no material break below entry before the move
```

### Interpretation

This is a positive-with-local-4B case:

```text
Stage2-Actionable: valid if engine backlog/margin bridge exists.
Stage3-Green: possible only with explicit margin and delivery bridge.
Local 4B: required after +100% MFE.
Hard 4C: no.
```

### Stress-test components

```text
raw_component_score_proxy:
  order_backlog_quality: high
  ownership/integration_context: medium
  margin_conversion_visibility: medium_high
  price_confirmation: very_high
  blowoff_4b_risk: high
```

---

## 7. Case 3 — 267270 HD현대건설기계

```yaml
case_id: C01_R1L91_267270_2024_07_16
symbol: "267270"
name: "HD현대건설기계"
canonical_archetype_id: C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id: SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA
trigger_date: 2024-07-16
entry_date: 2024-07-16
entry_price_basis: close
entry_price: 64200
classification: hard_4c_candidate_machinery_cycle_order_headline_without_margin_bridge
calibration_usable: true
```

### Evidence interpretation

HD현대건설기계 is the counterexample. The company sits in the same broad industrial bucket, but construction-equipment demand is not the same as shipyard backlog or marine-engine delivery leverage. A generic “industrial/machinery order cycle” headline can look like a C01 setup, yet fail if the model cannot verify:

```text
end-market demand
  -> backlog quality
  -> dealer/channel inventory
  -> price realization
  -> cost/mix control
  -> operating margin conversion
```

The forward path shows the danger.

### Price path

Key Stock-Web rows:

```text
2024-07-16: close 64,200
2024-07-22: high 69,200 / close 68,500
2024-07-23: high 71,000 / close 67,300
2024-08-05: sharp market-low window, fetched follow-up shows post-drop recovery but not clean survival
2024-09-06: low 46,450 / close 46,850
2024-09-27: high 53,600 / close 53,200
```

Approximate return path from 2024-07-16 close:

```text
entry_close: 64,200
peak_high: 71,000
MFE: +10.6%
worst_low: 46,450
MAE: -27.6%
```

### Interpretation

This is a hard C01 guardrail case.

```text
Stage2-Watch: allowed if industrial cycle evidence exists.
Stage2-Actionable: blocked unless backlog/margin bridge is explicit.
Stage3-Green: blocked.
Hard 4C candidate: yes.
```

The model must not lump all industrial order headlines together. Shipyard backlog with improving margin and construction-equipment channel cycle are different machines.

### Stress-test components

```text
raw_component_score_proxy:
  order/cycle_headline: medium
  backlog_quality: unclear
  end-market/channel_inventory_risk: high
  margin_conversion_visibility: low
  price_confirmation: shallow
  drawdown_penalty: high
  hard_4c_guard: yes
```

---

## 8. Aggregate calibration takeaways

```text
positive_case_count: 2
counterexample_count: 1
local_4b_overlay_case_count: 1
hard_4c_candidate_count: 1
calibration_usable_trigger_count: 3
```

The three-case C01 grid:

```text
010620 HD현대미포:
  shipbuilding backlog + margin conversion positive.

082740 한화엔진:
  marine-engine backlog positive,
  but +100% MFE requires local 4B overlay.

267270 HD현대건설기계:
  machinery/order-cycle headline failed without margin bridge;
  shallow MFE and high MAE make it a hard 4C candidate.
```

Shared rule:

```text
C01 is not "orders are high."
C01 is "orders convert into profitable deliveries."
```

---

## 9. Machine-readable JSONL rows

```jsonl
{"row_type":"case","case_id":"C01_R1L91_010620_2024_06_24","scheduled_round":"R1","scheduled_loop":91,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA","symbol":"010620","name":"HD현대미포","trigger_date":"2024-06-24","entry_date":"2024-06-24","entry_price":86900,"peak_high_180d":121900,"peak_date_180d":"2024-08-01","extended_peak_high":144300,"extended_peak_date":"2025-01-21","mfe_pct_180d":40.3,"extended_mfe_pct":66.1,"classification":"positive_shipbuilding_backlog_margin_bridge","calibration_usable":true,"evidence_family":"shipbuilding_backlog_delivery_margin_conversion","residual_error":"none_for_actionable_if_margin_bridge_explicit","shadow_rule_candidate":"allow_green_only_when_shipbuilding_backlog_quality_margin_revision_and_price_survival_confirm"}
{"row_type":"case","case_id":"C01_R1L91_082740_2024_10_04","scheduled_round":"R1","scheduled_loop":91,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA","symbol":"082740","name":"한화엔진","trigger_date":"2024-10-04","entry_date":"2024-10-04","entry_price":14040,"peak_high":28750,"peak_date":"2025-02-14","mfe_pct":104.8,"classification":"positive_with_local_4b_engine_backlog_margin_bridge","calibration_usable":true,"evidence_family":"marine_engine_backlog_delivery_operating_leverage","residual_error":"positive_entry_but_large_mfe_requires_local_4b_overlay","shadow_rule_candidate":"attach_local_4b_after_engine_backlog_mfe_exceeds_100_without_new_revision_bridge"}
{"row_type":"case","case_id":"C01_R1L91_267270_2024_07_16","scheduled_round":"R1","scheduled_loop":91,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA","symbol":"267270","name":"HD현대건설기계","trigger_date":"2024-07-16","entry_date":"2024-07-16","entry_price":64200,"peak_high":71000,"peak_date":"2024-07-23","worst_low":46450,"worst_low_date":"2024-09-06","mfe_pct":10.6,"mae_pct":-27.6,"classification":"hard_4c_candidate_machinery_cycle_order_headline_without_margin_bridge","calibration_usable":true,"evidence_family":"construction_equipment_order_cycle_without_margin_channel_bridge","residual_error":"generic_industrial_order_headline_can_overpromote_without_company_specific_margin_bridge","shadow_rule_candidate":"block_actionable_green_if_mfe_shallow_mae_large_and_margin_conversion_bridge_missing"}
```

```jsonl
{"row_type":"aggregate","scheduled_round":"R1","scheduled_loop":91,"large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","fine_archetype_id":"SHIPBUILDING_ENGINE_AND_MACHINERY_BACKLOG_MARGIN_CONVERSION_VS_ORDER_HEADLINE_CYCLE_BETA","case_count":3,"positive_case_count":2,"counterexample_count":1,"local_4b_overlay_case_count":1,"hard_4c_candidate_count":1,"calibration_usable_trigger_count":3,"loop_contribution_label":"residual_error_found","do_not_propose_new_weight_delta":true}
{"row_type":"shadow_rule","scheduled_round":"R1","scheduled_loop":91,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","rule_id":"C01_PROFITABLE_DELIVERY_BRIDGE_REQUIRED","rule_type":"canonical_archetype_specific_guard","rule_text":"For C01, do not open Stage2-Actionable or Stage3-Green from order/backlog headlines alone. Require delivery visibility, cost pass-through or cost normalization, product mix, utilization, margin revision, and OP/EPS conversion. Distinguish shipbuilding backlog and marine-engine backlog from generic machinery cycle beta. If MFE is shallow and MAE is large, route to false-positive or hard-4C. If MFE exceeds 50-100%, preserve positive classification but attach local 4B watch unless new revision bridge appears.","expected_effect":"Reduce industrial order-headline false positives while preserving shipbuilding and engine positives that show real margin conversion and price survival.","production_scoring_changed":false,"shadow_weight_only":true}
{"row_type":"residual_contribution","scheduled_round":"R1","scheduled_loop":91,"canonical_archetype_id":"C01_ORDER_BACKLOG_MARGIN_BRIDGE","residual_type":"industrial_order_backlog_profitability_bridge_guard","contribution":"Adds C01 cases separating profitable shipbuilding/engine backlog positives from machinery-cycle order headline high-MAE false positive.","do_not_count_as_global_weight_delta":true}
```

---

## 10. Proposed canonical-archetype shadow rule

```text
C01_PROFITABLE_DELIVERY_BRIDGE_REQUIRED

IF canonical_archetype_id == C01_ORDER_BACKLOG_MARGIN_BRIDGE:

  Do not open Stage3-Green from:
    - order headline alone
    - backlog size alone
    - sector cycle beta alone
    - one-day industrial relative strength alone
    - broad shipbuilding / machinery label alone

  Require at least two of:
    - delivery schedule visibility
    - cost pass-through or cost normalization
    - product mix improvement
    - utilization improvement
    - margin revision
    - OP/EPS conversion
    - low-MAE post-trigger price survival

  If company_type in [shipbuilder, marine_engine]:
    allow Actionable when backlog quality and price survival confirm,
    but require margin conversion before Green.

  If company_type in [construction_equipment, machinery_cycle]:
    raise evidence threshold because channel inventory and end-market cycle can break the order headline.

  If MFE < 15% and MAE < -25%:
    route to C01 false-positive / hard-4C candidate.

  If MFE > 50%:
    attach local 4B watch unless a new revision bridge appears.

  If MFE > 100%:
    local 4B overlay is mandatory even if the original thesis remains valid.
```

---

## 11. Deferred Coding Agent Handoff Prompt

```text
You are a coding agent working on Songdaiki/stock_agent.

Do not treat this research MD as production scoring by itself.
Batch it with other v12 residual research files.

Source file:
e2r_stock_web_v12_residual_round_R1_loop_91_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C01_ORDER_BACKLOG_MARGIN_BRIDGE_research.md

Task:
1. Parse machine-readable JSONL rows.
2. Add the three C01 industrial backlog/margin cases to calibration research ingestion.
3. Preserve production_scoring_changed=false.
4. Treat the proposed rule only as a shadow canonical-archetype guard candidate:
   C01_PROFITABLE_DELIVERY_BRIDGE_REQUIRED.
5. Do not change global weights directly.
6. Compare against existing C01 cases and deduplicate by:
   canonical_archetype_id + symbol + trigger_type + entry_date.
7. If enough C01 cases agree, consider implementing a canonical guard that:
   - blocks order/backlog headline Green without margin conversion bridge,
   - distinguishes shipbuilding/engine backlog positives from generic machinery-cycle false positives,
   - attaches local 4B after large MFE,
   - routes shallow-MFE/high-MAE machinery cases to C01 false-positive or hard-4C.

Expected next schedule:
completed_round = R1
completed_loop = 91
next_round = R2
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 12. Required round-state footer

```text
completed_round = R1
completed_loop = 91
next_round = R2
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```
