# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R2",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 83,
  "computed_next_round": "R3",
  "computed_next_loop": 83,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE",
  "fine_archetype_id": "MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "memory_recovery_equipment_cycle_order_refresh_guardrail",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

This loop adds **3 new independent cases**, **2 counterexamples**, and **3 residual errors** for `R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE`.

The result is intentionally **source-repair first**. All selected rows use Stock-Web OHLC paths, but the non-price evidence layer is marked `source_proxy_only=true / evidence_url_pending=true`. Therefore this file should not create an immediate runtime weight change.

---

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
active_no_repeat_ledger_profile = e2r_2_2_rolling_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing calibrated axes are treated as baseline, not re-proposed globally:

```text
stage2_actionable_evidence_bonus
stage3_yellow_total_min
stage3_green_total_min
stage3_green_revision_min
stage3_cross_evidence_green_buffer
price_only_blowoff_blocks_positive_stage
full_4b_requires_non_price_evidence
hard_4c_thesis_break_routes_to_4c
```

This loop tests whether **C10 memory-recovery equipment cycle** needs a narrower bridge:

```text
memory recovery / capex restart
→ process-equipment or inspection-equipment order visibility
→ revenue and utilization conversion
→ margin bridge
→ order-refresh check before Green
→ local 4B watch if the move is theme-led and the bridge fails to refresh
```

---

## 2. Round / Large Sector / Canonical Archetype Scope

Latest visible continuation before this run:

```text
R13 loop 82 completed → R1 loop 83 completed → next = R2 loop 83
```

This file follows the sequential scheduler:

```text
scheduled_round = R2
scheduled_loop = 83
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
computed_next_round = R3
computed_next_loop = 83
```

R2 maps to `L2_AI_SEMICONDUCTOR_ELECTRONICS`, so the round-sector gate passes.

---

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat index snapshot for C10:

```text
C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  rows = 31
  symbols = 10
  date_range = 2023-03-17~2024-06-07
  good/bad Stage2 = 15/4
  4B/4C = 2/0
  top-covered symbols = 036930, 240810, 084370, 095610, 테스, 000660
```

Hard duplicate key applied:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected cases avoid the top-covered C10 names:

| case_id | symbol | company | trigger_type | entry_date | duplicate stance |
|---|---:|---|---|---|---|
| R2L83-C10-01 | 319660 | 피에스케이 | Stage2-Actionable + Local4BWatch | 2024-02-29 | new C10 symbol / new trigger family |
| R2L83-C10-02 | 079370 | 제우스 | Stage2-FalsePositive / Post-CA equipment theme fade | 2024-02-22 | new C10 symbol / post-CA theme-fade failure mode |
| R2L83-C10-03 | 064290 | 인텍플러스 | Stage2-FalsePositive / inspection equipment theme fade | 2024-02-20 | new C10 symbol / inspection-equipment fade failure mode |

Novelty result:

```text
new_independent_case_count = 3
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
hard_duplicate_reuse = false
```

---

## 4. Stock-Web OHLC Input / Price Source Validation

```text
source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
manifest_max_date = 2026-02-20
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
tradable_row_count = 14354401
symbol_count = 5414
```

Profile checks:

| symbol | profile_path | latest name | corporate_action_candidate_dates | 180D window status |
|---:|---|---|---|---|
| 319660 | `atlas/symbol_profiles/319/319660.json` | 피에스케이 | 2022-09-21, 2022-10-20 | clean for 2024-02-29~180D |
| 079370 | `atlas/symbol_profiles/079/079370.json` | 제우스 | 2024-01-16, 2024-02-08 | entry is after last CA candidate; 180D forward path treated clean |
| 064290 | `atlas/symbol_profiles/064/064290.json` | 인텍플러스 | none | clean |

---

## 5. Historical Eligibility Gate

| case_id | symbol | trigger_date | entry_date | entry_price | forward_window_trading_days | MFE/MAE 30/90/180D computed | corporate-action contaminated 180D | calibration_usable |
|---|---:|---|---|---:|---:|---|---|---|
| R2L83-C10-01 | 319660 | 2024-02-28 | 2024-02-29 | 25400 | 180 | yes | no | true |
| R2L83-C10-02 | 079370 | 2024-02-21 | 2024-02-22 | 20500 | 180 | yes | no, but post-CA validation flag | true |
| R2L83-C10-03 | 064290 | 2024-02-19 | 2024-02-20 | 35750 | 180 | yes | no | true |

Entry rule:

```text
source_proxy trigger timing is treated as unknown or after-market.
entry_date = next stock-web tradable date close unless the same-day row is explicitly used as the reaction close.
```

Because these rows are source-proxy rows, `source_repair_required=true` for every case.

---

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | PROCESS_EQUIPMENT_CAPEX_RESTART_ORDER_VISIBILITY | allow Stage2-Actionable when memory recovery is tied to equipment order / capex restart / utilization bridge |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | POST_CA_EQUIPMENT_THEME_FADE | block positive promotion when post-CA or split-adjusted theme move lacks order-refresh evidence |
| C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | INSPECTION_EQUIPMENT_HBM_THEME_FADE | treat as local 4B / false-positive if inspection-equipment rally fades before revenue/margin bridge confirms |

C10은 “메모리 반등 느낌”이 아니다.  
메모리 사이클이 다시 도는 것과 장비업체의 매출·마진 톱니가 실제로 맞물리는 것은 다른 일이다.  
이번 루프의 핵심은 **불이 켜진 FAB 그림**과 **장비 발주·납품·매출 인식 장부**를 분리하는 것이다.

---

## 7. Case Selection Summary

| case_id | role | why selected |
|---|---|---|
| R2L83-C10-01 / PSK | positive lifecycle + local 4B watch | new C10 symbol with strong 180D MFE, but post-peak drawdown shows order-refresh/local-4B timing guard is still needed |
| R2L83-C10-02 / Zeus | counterexample | post-CA equipment theme produced a small MFE and deep MAE; bridge should be treated as weak until order/revenue refresh is repaired |
| R2L83-C10-03 / Intekplus | counterexample / local 4B | inspection-equipment HBM theme produced early MFE but then severe drawdown; price-only Stage2/Green should be blocked |

---

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 3
4C_case_count = 0
calibration_usable_case_count = 3
minimum_positive_case_count = pass
minimum_counterexample_count = pass
minimum_calibration_usable_case_count = pass
```

This is not a broad bullish C10 patch. It is a guardrail loop:

```text
C10 Stage2 may be early enough when order visibility exists.
C10 Green should remain strict unless order/revenue/margin bridge refreshes.
C10 local 4B should activate when a memory-recovery beta move peaks without non-price refresh.
```

---

## 9. Evidence Source Map

| case_id | evidence status | evidence_available_at_that_date | evidence_source | repair action |
|---|---|---|---|---|
| R2L83-C10-01 | source_proxy_only | memory capex recovery / process-equipment order visibility proxy around 2024-02-28 | source proxy; URL pending | verify report/disclosure/news before runtime promotion |
| R2L83-C10-02 | source_proxy_only | equipment theme / post-CA recovery proxy around 2024-02-21 | source proxy; URL pending | verify whether order/revenue bridge existed; otherwise keep as counterexample |
| R2L83-C10-03 | source_proxy_only | HBM/inspection-equipment theme proxy around 2024-02-19 | source proxy; URL pending | verify customer/order bridge; otherwise keep as false-positive guard |

```text
source_proxy_only_count = 3
evidence_url_pending_count = 3
source_repair_required = true
do_not_propose_new_weight_delta = true
```

---

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry row source | 180D path source |
|---:|---|---|---|---|
| 319660 | `atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv` | `atlas/symbol_profiles/319/319660.json` | 2024-02-29 row, close 25400 | 2024-02-29 through ~2024-11-25 rows |
| 079370 | `atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv` | `atlas/symbol_profiles/079/079370.json` | 2024-02-22 row, close 20500 | 2024-02-22 through ~2024-11 rows |
| 064290 | `atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv` | `atlas/symbol_profiles/064/064290.json` | 2024-02-20 row, close 35750 | 2024-02-20 through ~2024-11 rows |

---

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | company | trigger_type | trigger_date | entry_date | entry_price | evidence fields | current_profile_verdict |
|---|---|---:|---|---|---|---|---:|---|---|
| R2L83-C10-01-T1 | R2L83-C10-01 | 319660 | 피에스케이 | Stage2-Actionable | 2024-02-28 | 2024-02-29 | 25400 | memory recovery + process equipment capex restart proxy + RS | current_profile_4B_too_late |
| R2L83-C10-02-T1 | R2L83-C10-02 | 079370 | 제우스 | Stage2-FalsePositive | 2024-02-21 | 2024-02-22 | 20500 | post-CA equipment theme proxy, weak order bridge | current_profile_false_positive |
| R2L83-C10-03-T1 | R2L83-C10-03 | 064290 | 인텍플러스 | Stage2-FalsePositive | 2024-02-19 | 2024-02-20 | 35750 | inspection-equipment theme proxy, weak refresh | current_profile_false_positive |

---

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger backtest

| trigger_id | symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | below_entry_30D | below_entry_90D |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| R2L83-C10-01-T1 | 319660 | 2024-02-29 | 25400 | 28.15 | -11.02 | 53.94 | -11.02 | 53.94 | -32.28 | 2024-07-11 | 39100 | -56.01 | false | false |
| R2L83-C10-02-T1 | 079370 | 2024-02-22 | 20500 | 11.22 | -14.63 | 11.22 | -18.63 | 11.22 | -48.78 | 2024-02-28 | 22800 | -53.95 | true | true |
| R2L83-C10-03-T1 | 064290 | 2024-02-20 | 35750 | 14.41 | -11.47 | 14.41 | -41.26 | 14.41 | -64.64 | 2024-03-07 | 40900 | -69.10 | true | true |

### 12.2 Calculation caveat

```text
MFE/MAE values are connector-manual calculations from Stock-Web shard rows read during this run.
30D/90D/180D are usable for calibration triage.
1Y/2Y are not used in this connector run and are marked not_calculated_connector_run in JSONL fields.
```

---

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected judgement | actual price path | verdict |
|---|---|---|---|
| R2L83-C10-01 | Stage2-Actionable or Yellow if equipment order visibility is trusted | high MFE but deep post-peak drawdown | current_profile_4B_too_late |
| R2L83-C10-02 | could become Stage2 if post-CA theme is over-weighted | MFE small, MAE severe | current_profile_false_positive |
| R2L83-C10-03 | could become Stage2 if HBM inspection theme is over-weighted | early peak, severe MAE | current_profile_false_positive |

Questions required by v12:

```text
1. current calibrated profile judgement:
   - PSK: not wrong on early Stage2, but should demand order-refresh / local4B watch.
   - Zeus/Intekplus: too permissive if theme proxy is counted as Stage2 evidence.

2. MFE/MAE alignment:
   - PSK: tradable MFE validates early entry, but post-peak drawdown demands 4B overlay.
   - Zeus/Intekplus: weak MFE and severe MAE validate false-positive guard.

3. Stage2 bonus:
   - sufficient only when capex restart is tied to order visibility.
   - too generous for post-CA or theme-only equipment beta.

4. Yellow 75:
   - keep. Do not lower for C10.

5. Green 87 / revision 55:
   - keep or strengthen by requiring order/revenue refresh.

6. price-only blowoff guard:
   - appropriate.

7. full 4B non-price requirement:
   - appropriate. These are local-4B/watch rows, not full non-price 4B.

8. hard 4C:
   - no hard 4C without non-price thesis break.
```

---

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2-Actionable timing | Yellow timing | Green timing | green_lateness_ratio | interpretation |
|---|---|---|---|---|---|
| R2L83-C10-01 | useful early entry if order bridge is repaired | possible after March RS/revision refresh | should require order/revenue refresh; not just price | not_applicable | no confirmed Green trigger in source-proxy run |
| R2L83-C10-02 | should be blocked or risk-watch only | not eligible | not eligible | not_applicable | post-CA theme move should not become Green |
| R2L83-C10-03 | should be blocked or risk-watch only | not eligible | not eligible | not_applicable | inspection theme lacks durable bridge |

---

## 15. 4B Local vs Full-window Timing Audit

| case_id | local peak date | local peak price | proposed 4B evidence type | local proximity | full-window proximity | 4B verdict |
|---|---|---:|---|---:|---:|---|
| R2L83-C10-01 | 2024-07-11 | 39100 | price_only + revision_slowdown_watch | 1.00 | 1.00 | good local 4B watch, not full 4B until non-price refresh fails |
| R2L83-C10-02 | 2024-02-28 | 22800 | price_only + post_CA_theme_fade | 1.00 | 1.00 | price-only local 4B, not full 4B |
| R2L83-C10-03 | 2024-03-07 | 40900 | price_only + theme_fade | 1.00 | 1.00 | price-only local 4B, not full 4B |

```text
do_not_treat_as_full_4B = true
reason = non-price 4B evidence not repaired in this run
```

---

## 16. 4C Protection Audit

| case_id | 4C label | reason |
|---|---|---|
| R2L83-C10-01 | thesis_break_watch_only | deep drawdown, but no verified non-price thesis break |
| R2L83-C10-02 | thesis_break_watch_only | post-CA/theme fade, no verified order cancellation or thesis break |
| R2L83-C10-03 | thesis_break_watch_only | severe MAE, but no verified non-price thesis break |

Hard 4C remains gated by non-price evidence.

---

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
candidate_axis = C10_order_refresh_required_after_memory_recovery_beta
proposal_type = shadow_only_source_repair_required
production_scoring_changed = false
```

Candidate rule:

```text
For C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE:
  Stage2-Actionable may activate on memory recovery + capex restart + equipment order visibility.
  But Stage3-Green should require one of:
    - named customer/order or capex allocation,
    - backlog/delivery evidence,
    - revenue recognition or margin bridge,
    - revision refresh.
  If MFE appears without that bridge and MAE widens after the local peak,
  keep the row as local 4B watch / false-positive guard, not full 4B or hard 4C.
```

---

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = C10_MEMORY_RECOVERY_ORDER_REFRESH_GREEN_GATE
```

Shadow gate:

| component | proposed C10 interpretation |
|---|---|
| contract_score | only count when equipment order/customer/capex allocation is repaired |
| backlog_visibility_score | require backlog/delivery or capex restart visibility |
| margin_bridge_score | require utilization/revenue/margin bridge before Green |
| relative_strength_score | useful for Stage2 timing, not sufficient for Green |
| execution_risk_score | increases when post-peak drawdown follows no order refresh |
| valuation_repricing_score | cap if MFE is price-only and evidence_url_pending |

---

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | baseline proxy | 3 | 26.52 | -23.64 | 26.52 | -48.57 | 66.7% | too permissive if source-proxy theme is counted |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | 26.52 | -23.64 | 26.52 | -48.57 | 66.7% | slower but still cannot solve theme fade alone |
| P1_C10_order_refresh_green_gate | canonical shadow | 3 | 26.52 | -23.64 | 26.52 | -48.57 | 33.3% | keeps PSK as lifecycle; blocks Zeus/Intekplus positive promotion |
| P2_C10_local4B_watch_guard | canonical shadow | 3 | 26.52 | -23.64 | 26.52 | -48.57 | 33.3% | converts all three to local 4B watch after bridge failure |
| P3_C10_counterexample_guard | canonical shadow | 3 | 26.52 | -23.64 | 26.52 | -48.57 | 0.0% for Green | strictest; no Green without source repair |

---

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score_return_alignment_label |
|---|---:|---|---:|---|---|
| R2L83-C10-01-T1 | 78 | Stage2-Actionable | 76 | Stage2-Actionable + Local4BWatch | early entry aligned, Green blocked |
| R2L83-C10-02-T1 | 66 | Stage2-Watch | 56 | Blocked / Counterexample | score should fall because bridge is weak |
| R2L83-C10-03-T1 | 68 | Stage2-Watch | 55 | Blocked / Local4BWatch | score should fall because theme faded |

---

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE | MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE | 1 | 2 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | false | true | C10 gains 3 new symbols but still needs evidence URL repair |

---

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_4B_too_late
  - current_profile_false_positive
  - source_proxy_bridge_insufficient
new_axis_proposed: null
existing_axis_strengthened: C10_order_refresh_required_after_memory_recovery_beta
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

Because all three cases remain `source_proxy_only=true`, this MD should be used as a **source-repair and validation queue**, not as a production-weight patch.

---

## 23. Validation Scope / Non-Validation Scope

### Validation scope

```text
validated:
  - scheduled round/loop/sector consistency
  - No-Repeat top-covered symbol avoidance
  - Stock-Web manifest/schema/profile path availability
  - entry_date/entry_price from tradable rows
  - MFE/MAE/peak/drawdown 30D/90D/180D from Stock-Web rows
  - corporate-action window triage at profile level
```

### Non-validation scope

```text
not_validated_in_this_run:
  - full evidence URL repair
  - official disclosure/report URL mapping
  - exact intraday trigger timestamp
  - production scoring implementation
  - 1Y/2Y numeric MFE/MAE
```

---

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C10_order_refresh_required_after_memory_recovery_beta,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE,0,1,+1,"C10 theme/price-only beta created 2 false positives and 1 late local-4B need","blocks Zeus/Intekplus positive promotion; keeps PSK as Stage2 lifecycle with local4B watch","R2L83-C10-01-T1|R2L83-C10-02-T1|R2L83-C10-03-T1",3,3,2,low,source_repair_shadow_only,"not production; all rows evidence_url_pending"
```

---

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L83-C10-01","symbol":"319660","company_name":"피에스케이","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","case_type":"positive_lifecycle_with_local4b_watch","positive_or_counterexample":"positive","best_trigger":"R2L83-C10-01-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early Stage2 aligned but local 4B watch required after peak","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"source repair required before runtime promotion"}
{"row_type":"case","case_id":"R2L83-C10-02","symbol":"079370","company_name":"제우스","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","case_type":"counterexample_theme_fade","positive_or_counterexample":"counterexample","best_trigger":"R2L83-C10-02-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"small MFE and severe MAE; positive promotion should be blocked","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"post-CA validation/source repair required"}
{"row_type":"case","case_id":"R2L83-C10-03","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","case_type":"counterexample_inspection_equipment_theme_fade","positive_or_counterexample":"counterexample","best_trigger":"R2L83-C10-03-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early MFE collapsed into high MAE; Green must require order/revenue bridge","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","source_proxy_only":true,"evidence_url_pending":true,"notes":"source repair required"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R2L83-C10-01-T1","case_id":"R2L83-C10-01","symbol":"319660","company_name":"피에스케이","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","sector":"AI·반도체·전자","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable+Local4BWatch","trigger_date":"2024-02-28","evidence_available_at_that_date":"memory recovery / process equipment capex restart proxy; evidence_url_pending","evidence_source":"source_proxy_only","stage2_evidence_fields":["memory_recovery","process_equipment_capex_restart_proxy","relative_strength"],"stage3_evidence_fields":["order_refresh_required_not_verified"],"stage4b_evidence_fields":["post_peak_drawdown","local_4b_watch"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv","profile_path":"atlas/symbol_profiles/319/319660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-29","entry_price":25400,"MFE_30D_pct":28.15,"MFE_90D_pct":53.94,"MFE_180D_pct":53.94,"MFE_1Y_pct":"not_calculated_connector_run","MFE_2Y_pct":"not_calculated_connector_run","MAE_30D_pct":-11.02,"MAE_90D_pct":-11.02,"MAE_180D_pct":-32.28,"MAE_1Y_pct":"not_calculated_connector_run","below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-07-11","peak_price":39100,"drawdown_after_peak_pct":-56.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"local_4b_watch_not_full_4b_without_non_price_refresh","four_b_evidence_type":["price_only","revision_slowdown_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_lifecycle_with_late_local4b_need","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L83-C10-01-20240229-25400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L83-C10-02-T1","case_id":"R2L83-C10-02","symbol":"079370","company_name":"제우스","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","sector":"AI·반도체·전자","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-21","evidence_available_at_that_date":"post-CA equipment recovery theme proxy; evidence_url_pending","evidence_source":"source_proxy_only","stage2_evidence_fields":["equipment_theme_proxy","post_CA_validation_required"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_fade","high_MAE_180D"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv","profile_path":"atlas/symbol_profiles/079/079370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-22","entry_price":20500,"MFE_30D_pct":11.22,"MFE_90D_pct":11.22,"MFE_180D_pct":11.22,"MFE_1Y_pct":"not_calculated_connector_run","MFE_2Y_pct":"not_calculated_connector_run","MAE_30D_pct":-14.63,"MAE_90D_pct":-18.63,"MAE_180D_pct":-48.78,"MAE_1Y_pct":"not_calculated_connector_run","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-28","peak_price":22800,"drawdown_after_peak_pct":-53.95,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"entry_after_last_profile_CA_candidate_2024-02-08_post_CA_validation_flag","same_entry_group_id":"R2L83-C10-02-20240222-20500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L83-C10-03-T1","case_id":"R2L83-C10-03","symbol":"064290","company_name":"인텍플러스","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","fine_archetype_id":"MEMORY_RECOVERY_PROCESS_EQUIPMENT_AND_INSPECTION_ORDER_VISIBILITY_VS_POST_CA_THEME_FADE","sector":"AI·반도체·전자","primary_archetype":"memory recovery equipment cycle","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-19","evidence_available_at_that_date":"HBM / inspection-equipment theme proxy; evidence_url_pending","evidence_source":"source_proxy_only","stage2_evidence_fields":["inspection_equipment_theme_proxy","memory_recovery_beta"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["theme_fade","high_MAE_180D"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv","profile_path":"atlas/symbol_profiles/064/064290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-20","entry_price":35750,"MFE_30D_pct":14.41,"MFE_90D_pct":14.41,"MFE_180D_pct":14.41,"MFE_1Y_pct":"not_calculated_connector_run","MFE_2Y_pct":"not_calculated_connector_run","MAE_30D_pct":-11.47,"MAE_90D_pct":-41.26,"MAE_180D_pct":-64.64,"MAE_1Y_pct":"not_calculated_connector_run","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-07","peak_price":40900,"drawdown_after_peak_pct":-69.10,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"counterexample_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L83-C10-03-20240220-35750","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L83-C10-01","trigger_id":"R2L83-C10-01-T1","symbol":"319660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":3,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":76,"stage_label_after":"Stage2-Actionable+Local4BWatch","changed_components":["revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"large MFE validates early Stage2, but high post-peak drawdown requires order-refresh/local4B watch","MFE_90D_pct":53.94,"MAE_90D_pct":-11.02,"score_return_alignment_label":"early_entry_aligned_but_4B_watch_late","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L83-C10-02","trigger_id":"R2L83-C10-02-T1","symbol":"079370","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56,"stage_label_after":"BlockedCounterexample","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"post-CA equipment theme has insufficient order bridge and severe 180D MAE","MFE_90D_pct":11.22,"MAE_90D_pct":-18.63,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L83-C10-03","trigger_id":"R2L83-C10-03-T1","symbol":"064290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"BlockedCounterexample+Local4BWatch","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"inspection-equipment HBM theme had early peak but no durable bridge; high MAE demands guard","MFE_90D_pct":14.41,"MAE_90D_pct":-41.26,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":83,"large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive","source_proxy_bridge_insufficient"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":true}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R2L83-C10-SOURCE-REPAIR","symbol":"MULTI","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE","reason":"all selected non-price evidence remains source_proxy_only/evidence_url_pending; use as source repair queue before runtime weight promotion","price_source":"Songdaiki/stock-web","usage":"not_immediate_weight_calibration"}
```

---

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated E2R profile.

Do not blindly apply every shadow row.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `source_proxy_only=true` rows as production-ready.
- This loop proposes no production weight delta.
- First repair evidence URLs for:
  - `319660 / 피에스케이 / 2024-02-28~2024-02-29`
  - `079370 / 제우스 / 2024-02-21~2024-02-22`
  - `064290 / 인텍플러스 / 2024-02-19~2024-02-20`
- Then reassess whether `C10_order_refresh_required_after_memory_recovery_beta` should remain a canonical shadow rule.

### Candidate implementation target

```text
candidate_rule_id = C10_MEMORY_RECOVERY_ORDER_REFRESH_GREEN_GATE
scope = canonical_archetype_specific
production_default = hold
reason = evidence_url_pending_for_all_rows
```

### Validation tasks

```text
1. Verify source URLs for each trigger date.
2. Confirm exact evidence timing and whether same-day or next-day entry is correct.
3. Recompute Stock-Web 30D/90D/180D metrics directly from CSV.
4. Validate 079370 post-CA handling after 2024-02-08.
5. Do not promote a new production rule until source_proxy_only=false for at least two positive/counterexample rows.
```

---

## 27. Next Round State

```text
completed_round = R2
completed_loop = 83
next_round = R3
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
PRICE_ATLAS = Songdaiki/stock-web
MANIFEST = atlas/manifest.json
SCHEMA = atlas/schema.json
```

Connector-read Stock-Web artifacts used in this run:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/319/319660.json
atlas/symbol_profiles/079/079370.json
atlas/symbol_profiles/064/064290.json
atlas/ohlcv_tradable_by_symbol_year/319/319660/2024.csv
atlas/ohlcv_tradable_by_symbol_year/079/079370/2024.csv
atlas/ohlcv_tradable_by_symbol_year/064/064290/2024.csv
```

Final response fields:

```text
output_file: e2r_stock_web_v12_residual_round_R2_loop_83_L2_AI_SEMICONDUCTOR_ELECTRONICS_C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE_research.md
scheduled_round: R2
scheduled_loop: 83
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
new_independent_case_count: 3
reused_case_count: 0
new_symbol_count: 3
positive_case_count: 1
counterexample_count: 2
current_profile_error_count: 3
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
production_scoring_changed: false
shadow_weight_only: true
existing_axis_tested:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened: C10_order_refresh_required_after_memory_recovery_beta
existing_axis_weakened: null
next_round: R3
```
