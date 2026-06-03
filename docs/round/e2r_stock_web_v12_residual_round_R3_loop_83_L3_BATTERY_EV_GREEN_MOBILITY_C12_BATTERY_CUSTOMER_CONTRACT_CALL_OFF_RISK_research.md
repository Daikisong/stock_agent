# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R3",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 83,
  "computed_next_round": "R4",
  "computed_next_loop": 83,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK",
  "fine_archetype_id": "COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
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

This loop adds **3 new independent cases**, **2 counterexamples**, and **3 residual errors** for `R3/L3_BATTERY_EV_GREEN_MOBILITY/C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK`.

The loop is **source-repair first**. All selected rows use actual Stock-Web OHLC paths and are calibration-usable for price-path measurement. The non-price layer is still marked `source_proxy_only=true / evidence_url_pending=true`, so the file must not be promoted into runtime weights before source repair.

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

This loop tests whether C12 needs a narrower customer-calloff guard:

```text
EV demand slowdown / customer order pacing risk
→ upstream material supplier shipment or utilization sensitivity
→ short restock MFE is allowed
→ Green blocked unless call-off / order-refresh bridge is repaired
→ local 4B watch if MFE fades into widening MAE
→ hard 4C only if explicit non-price thesis break appears
```

---

## 2. Round / Large Sector / Canonical Archetype Scope

Latest continuation used for this run:

```text
R2 loop 83 completed
next_round = R3
next_loop = 83
```

This file follows the corrected sequential scheduler:

```text
scheduled_round = R3
scheduled_loop = 83
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK
computed_next_round = R4
computed_next_loop = 83
```

R3 maps to `L3_BATTERY_EV_GREEN_MOBILITY`, so the round-sector gate passes.

---

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat snapshot for scheduled-round candidates:

```text
C11_BATTERY_ORDERBOOK_RERATING:
  rows = 79, symbols = 21, top-covered = 247540, 003670, 393890, 222080, 348370, 066970

C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK:
  rows = 68, symbols = 18, good/bad S2 = 15/2, 4B/4C = 15/5
  top-covered = 361610, 393890, 336370, 006110, 011790, 003670

C13_BATTERY_JV_UTILIZATION_AMPC_IRA:
  rows = 43, symbols = 11

C14_EV_DEMAND_SLOWDOWN_4B_4C:
  rows = 76, symbols = 15, 4B/4C heavy
```

`C12` was selected because R3 loop 82 already used C11, while C12 still benefits from upstream supplier call-off guardrail separation.

Hard duplicate key applied:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

Selected novelty:

```text
C12 + 020150 + Stage2-RiskWatch / Local4B + 2024-04-25
C12 + 278280 + Stage2-FalsePositive / CustomerCallOffRisk + 2024-04-25
C12 + 121600 + Stage2-Actionable-to-Local4B / CNTCustomerCallOffRisk + 2024-04-25
```

These are not in the visible C12 top-covered set. `121600` appears in other battery archetype contexts, but here it is mapped to C12 customer call-off / upstream material risk with a new trigger family and new hard key.

---

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Manifest context used by this run:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Per-symbol profile checks:

| symbol | company | profile_path | profile CA candidates | 180D status |
|---|---|---|---|---|
| 020150 | 롯데에너지머티리얼즈 | `atlas/symbol_profiles/020/020150.json` | none | clean |
| 278280 | 천보 | `atlas/symbol_profiles/278/278280.json` | none | clean |
| 121600 | 나노신소재 | `atlas/symbol_profiles/121/121600.json` | 2015-12-17 only | clean for 2024-04-25~180D |

---

## 5. Historical Eligibility Gate

| case_id | symbol | trigger_date | entry_date | 180D forward available | OHLC available | corporate-action contaminated 180D | usable |
|---|---:|---|---|---|---|---|---|
| R3L83-C12-020150-20240425 | 020150 | 2024-04-25 | 2024-04-25 | yes | yes | no | true |
| R3L83-C12-278280-20240425 | 278280 | 2024-04-25 | 2024-04-25 | yes | yes | no | true |
| R3L83-C12-121600-20240425 | 121600 | 2024-04-25 | 2024-04-25 | yes | yes | no | true |

Entry rule:

```text
trigger_date = 2024-04-25
entry_date = 2024-04-25 close
entry_price = stock-web c column
```

The trigger date is treated as a same-day market-visible sector risk checkpoint. Because evidence URLs are still pending, these rows are calibration-usable for price-path diagnostics but not promotion-ready.

---

## 6. Canonical Archetype Compression Map

| canonical | fine/deep route | Stage2 bridge | Green blocker | 4B/4C use |
|---|---|---|---|---|
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | COPPER_FOIL_CUSTOMER_CALLOFF_RISK | supplier demand survives only if shipment/order-refresh evidence exists | upstream beta alone | local 4B if MFE fades and MAE widens |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | ELECTROLYTE_ADDITIVE_UTILIZATION_FADE | utilization/customer order pacing must improve | commodity/material rebound without customer bridge | Stage2 false positive / 4B watch |
| C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | CNT_CUSTOMER_CALLOFF_SHORT_MFE_FADE | strong MFE allowed, but only with call-off bridge repaired | post-MFE drawdown without order refresh | high-MFE false positive / local 4B |

C12 is not “battery material stocks fell.”  
It is a customer-pacing mechanism: if the customer taps the brake, the upstream supplier feels the seatbelt first.

---

## 7. Case Selection Summary

| case_id | symbol | company | role | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---|
| R3L83-C12-020150-20240425 | 020150 | 롯데에너지머티리얼즈 | risk_positive_local4b | 2024-04-25 | 47,600 | 24.37 | -24.89 | 24.37 | -52.63 | current_profile_4B_too_late |
| R3L83-C12-278280-20240425 | 278280 | 천보 | counterexample_failed_rerating | 2024-04-25 | 73,000 | 12.6 | -21.37 | 12.6 | -51.51 | current_profile_false_positive |
| R3L83-C12-121600-20240425 | 121600 | 나노신소재 | counterexample_short_mfe_fade | 2024-04-25 | 114,100 | 31.29 | -27.08 | 31.29 | -49.96 | current_profile_4B_too_late |

---

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 3
4C_case_count = 0
calibration_usable_case_count = 3
new_independent_case_count = 3
```

The positive case is a **risk-positive guardrail case**, not a bullish durable Stage3-Green case.  
The useful signal is that C12 should permit local 4B/RiskWatch even when early MFE exists.

---

## 9. Evidence Source Map

| symbol | evidence status | evidence family | runtime promotion status |
|---|---|---|---|
| 020150 | source_proxy_only=true / evidence_url_pending=true | 2024Q2 EV customer pacing / copper foil supplier risk | source repair required |
| 278280 | source_proxy_only=true / evidence_url_pending=true | 2024Q2 electrolyte-additive utilization and demand fade | source repair required |
| 121600 | source_proxy_only=true / evidence_url_pending=true | 2024Q2 CNT customer call-off / short restock MFE fade | source repair required |

No production scoring change is allowed from proxy-only evidence.

---

## 10. Price Data Source Map

| symbol | 2024 shard | 2025 shard | profile |
|---|---|---|---|
| 020150 | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv` | `atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv` | `atlas/symbol_profiles/020/020150.json` |
| 278280 | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv` | `atlas/ohlcv_tradable_by_symbol_year/278/278280/2025.csv` | `atlas/symbol_profiles/278/278280.json` |
| 121600 | `atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv` | `atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv` | `atlas/symbol_profiles/121/121600.json` |

---

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R3L83-C12-020150-T1 | 020150 | Stage2-RiskWatch / Local4B | 2024-04-25 | 2024-04-25 | 47,600 | 23.74 | -7.14 | 24.37 | -24.89 | 24.37 | -52.63 | 2024-06-18 | 59,200 | -61.91 |
| R3L83-C12-278280-T1 | 278280 | Stage2-FalsePositive / CustomerCallOffRisk | 2024-04-25 | 2024-04-25 | 73,000 | 12.6 | -2.6 | 12.6 | -21.37 | 12.6 | -51.51 | 2024-06-12 | 82,200 | -56.93 |
| R3L83-C12-121600-T1 | 121600 | Stage2-Actionable-to-Local4B / CNTCustomerCallOffRisk | 2024-04-25 | 2024-04-25 | 114,100 | 31.29 | -12.18 | 31.29 | -27.08 | 31.29 | -49.96 | 2024-06-11 | 149,800 | -61.88 |

---

## 12. Trigger-Level OHLC Backtest Tables

### 020150 / 롯데에너지머티리얼즈

```text
entry_date = 2024-04-25
entry_price = 47,600
30D high/low proxy = 58,900 / 44,200
90D high/low proxy = 59,200 / 35,750
180D high/low proxy = 59,200 / 22,550
peak_date = 2024-06-18
peak_price = 59,200
drawdown_after_peak_pct = -61.91
```

### 278280 / 천보

```text
entry_date = 2024-04-25
entry_price = 73,000
30D high/low proxy = 82,200 / 71,100
90D high/low proxy = 82,200 / 57,400
180D high/low proxy = 82,200 / 35,400
peak_date = 2024-06-12
peak_price = 82,200
drawdown_after_peak_pct = -56.93
```

### 121600 / 나노신소재

```text
entry_date = 2024-04-25
entry_price = 114,100
30D high/low proxy = 149,800 / 100,200
90D high/low proxy = 149,800 / 83,200
180D high/low proxy = 149,800 / 57,100
peak_date = 2024-06-11
peak_price = 149,800
drawdown_after_peak_pct = -61.88
```

---

## 13. Current Calibrated Profile Stress Test

| symbol | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| 020150 | Stage2-Actionable allowed after battery-material rebound | +24.37% MFE, then -52.63% MAE | current_profile_4B_too_late |
| 278280 | Stage2-Actionable or Yellow candidate if material beta treated positively | +12.60% MFE, then -51.51% MAE | current_profile_false_positive |
| 121600 | Stage2/Yellows because early MFE was strong | +31.29% MFE, then -49.96% MAE | current_profile_4B_too_late |

Answers to v12 stress-test questions:

```text
1. current calibrated profile would likely give early Stage2/Actionable credit to supplier rebound beta.
2. That was only partly aligned: MFE existed, but MAE and drawdown later dominated.
3. Stage2 actionable bonus is too permissive when customer call-off/order-refresh evidence is absent.
4. Yellow threshold 75 is not the main problem; the bridge quality gate is.
5. Green threshold 87 / revision 55 should remain strict.
6. price-only blowoff guard remains correct.
7. full 4B non-price requirement remains correct, but C12 local 4B watch should trigger earlier on call-off risk.
8. hard 4C routing should remain non-price-gated; none of these rows should become hard 4C by price alone.
```

---

## 14. Stage2 / Yellow / Green Comparison

| label | C12 interpretation |
|---|---|
| Stage2 | allowed only as RiskWatch if customer pacing risk is visible |
| Stage2-Actionable | blocked unless shipment/order-refresh evidence exists |
| Stage3-Yellow | requires revised visibility, not just short restock MFE |
| Stage3-Green | inappropriate for these proxy-only supplier rows |
| 4B Local | appropriate when early MFE fades into high MAE and call-off risk is present |
| 4C | not triggered without explicit contract cancellation, capacity collapse, covenant issue, or hard thesis break |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

---

## 15. 4B Local vs Full-window Timing Audit

| symbol | local 4B interpretation | full-window 4B interpretation | verdict |
|---|---|---|---|
| 020150 | local 4B watch would be useful after June peak if call-off evidence repaired | full 4B requires non-price evidence | current_profile_4B_too_late |
| 278280 | weak MFE and later MAE justify earlier false-positive/4B watch | full 4B requires non-price evidence | current_profile_false_positive |
| 121600 | strong MFE created a trap; local 4B watch should not wait for hard thesis break | full 4B requires non-price evidence | current_profile_4B_too_late |

```text
four_b_evidence_type = margin_or_backlog_slowdown | revision_slowdown | valuation_blowoff
do_not_treat_price_only_peak_as_full_4B = true
```

---

## 16. 4C Protection Audit

No row is promoted to hard 4C.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_price_only_allowed_count = 0
hard_4c_thesis_break_routes_to_4c = kept
```

---

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_name = L3_battery_upstream_supplier_calloff_risk_requires_order_refresh

candidate:
  In L3 upstream battery-material suppliers, generic EV/material rebound or short restock MFE
  should not receive full Stage2-Actionable or Green credit unless there is repaired
  evidence of customer call-off resilience, shipment recovery, capacity utilization, or
  order-refresh visibility.

effect:
  - keep Stage2 as RiskWatch when evidence is proxy-only
  - keep Green strict
  - allow local 4B watch when MFE fades into widening MAE
  - do not hard-4C without explicit non-price thesis break

promotion_status:
  shadow_only
  source_repair_required
```

---

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK

candidate:
  C12 should add an order-refresh / customer-calloff-resilience bridge before
  upstream supplier rows can graduate from Stage2-RiskWatch to Stage2-Actionable or Yellow.

proposed_axis:
  C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable

status:
  canonical_archetype_rule_candidate
  do_not_propose_new_weight_delta = true
  reason = source_proxy_only / evidence_url_pending
```

---

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE 90D | avg MAE 90D | avg MFE 180D | avg MAE 180D | false-positive rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | existing calibrated profile | 3 | 22.75 | -24.45 | 22.75 | -51.37 | 0.67 | too permissive on supplier rebound beta |
| P0b e2r_2_0_baseline_reference | old baseline | 3 | 22.75 | -24.45 | 22.75 | -51.37 | 0.67 | lacks C12 risk separation |
| P1 sector_specific_candidate_profile | L3 supplier call-off bridge required | 3 | 22.75 | -24.45 | 22.75 | -51.37 | 0.33 | better, but source repair required |
| P2 canonical_archetype_candidate_profile | C12 order-refresh guard | 3 | 22.75 | -24.45 | 22.75 | -51.37 | 0.33 | best explanatory fit |
| P3 counterexample_guard_profile | force local 4B watch on high-MAE proxy-only supplier rebound | 3 | 22.75 | -24.45 | 22.75 | -51.37 | 0.00 | conservative; may overblock true restock cycles |

---

## 20. Score-Return Alignment Matrix

| symbol | MFE_180D | MAE_180D | drawdown_after_peak | score-return alignment |
|---|---:|---:|---:|---|
| 020150 | 24.37 | -52.63 | -61.91 | MFE existed, but C12 local 4B needed earlier |
| 278280 | 12.60 | -51.51 | -56.93 | weak MFE / high MAE false positive |
| 121600 | 31.29 | -49.96 | -61.88 | strong MFE trap; call-off bridge missing |

```text
median_MFE_180D_pct = 24.37
median_MAE_180D_pct = -51.51
median_drawdown_after_peak_pct = -61.88
score_return_alignment_verdict = C12_upstream_supplier_MFE_does_not_equal_durable_rerating
```

---

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK | COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE | 1 | 2 | 3 | 0 | 3 | 0 | 3 | 3 | 3 | yes | yes | source repair and exact-key validation still required |

---

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 2
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - upstream supplier Stage2 false positive
  - local 4B too late after short MFE fade
  - missing customer call-off / order-refresh bridge
new_axis_proposed: null
existing_axis_strengthened:
  - C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: L3_battery_upstream_supplier_calloff_risk_requires_order_refresh
canonical_archetype_rule_candidate: C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
reason: source_proxy_only / evidence_url_pending
```

---

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web manifest/schema basis checked.
- Tradable raw OHLC shards used.
- 020150 / 278280 / 121600 symbol profiles checked.
- 2024 and early-2025 forward windows were used for 180D price-path diagnostics.
- 30D / 90D / 180D MFE and MAE were calculated from Stock-Web OHLC rows.
```

Non-validation scope:

```text
- No live stock discovery.
- No production scoring change.
- No source URL repair executed inside this run.
- No brokerage, trading, or current recommendation logic.
- No hard 4C promotion without explicit non-price thesis break.
```

---

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK,0,1,+1,"short MFE in upstream suppliers failed to protect against 180D MAE without customer call-off/order-refresh bridge","avg_MFE_180D=22.75; avg_MAE_180D=-51.37; avg_drawdown_after_peak=-60.24","R3L83-C12-020150-T1|R3L83-C12-278280-T1|R3L83-C12-121600-T1",3,3,2,low,canonical_shadow_only,"not production; source_proxy_only/evidence_url_pending"
```

---

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L83-C12-020150-20240425","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","case_type":"risk_guard_success","positive_or_counterexample":"positive","best_trigger":"R3L83-C12-020150-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"risk_guard_success_with_late_damage","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Short MFE was tradable, but the path later behaved like customer call-off risk, not durable orderbook rerating."}
{"row_type":"case","case_id":"R3L83-C12-278280-20240425","symbol":"278280","company_name":"천보","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R3L83-C12-278280-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"The early bounce was insufficient to offset later MAE; C12 should not treat generic battery-material rebound as orderbook rerating."}
{"row_type":"case","case_id":"R3L83-C12-121600-20240425","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","case_type":"short_mfe_fade","positive_or_counterexample":"counterexample","best_trigger":"R3L83-C12-121600-T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_MFE_but_bridge_failed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"This is the clearest C12 stress case: large tradable MFE existed, but the missing call-off bridge turned it into a high-drawdown lifecycle."}
{"row_type":"trigger","trigger_id":"R3L83-C12-020150-T1","case_id":"R3L83-C12-020150-20240425","symbol":"020150","company_name":"롯데에너지머티리얼즈","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","sector":"battery / EV / green mobility","primary_archetype":"battery customer contract call-off risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-RiskWatch / Local4B","trigger_date":"2024-04-25","evidence_available_at_that_date":"source_proxy_only=true; evidence_url_pending=true; sector-level EV demand/customer pacing risk at trigger date; source repair required before runtime promotion","evidence_source":"source_proxy:C12_EV_DEMAND_CUSTOMER_CALLOFF_RISK_2024Q2","stage2_evidence_fields":["copper-foil supplier exposure","EV/customer pacing risk","short restock MFE but no durable call-off bridge"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["customer call-off risk","post-peak drawdown","upstream supplier sensitivity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv|atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv","profile_path":"atlas/symbol_profiles/020/020150.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":47600,"MFE_30D_pct":23.74,"MFE_90D_pct":24.37,"MFE_180D_pct":24.37,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.14,"MAE_90D_pct":-24.89,"MAE_180D_pct":-52.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-18","peak_price":59200,"drawdown_after_peak_pct":-61.91,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_local_4B_watch_if_non_price_calloff_evidence_repaired","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"risk_guard_success_with_late_damage","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; no profile-level corporate-action candidate","same_entry_group_id":"R3L83-C12-020150-20240425-20240425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83-C12-278280-T1","case_id":"R3L83-C12-278280-20240425","symbol":"278280","company_name":"천보","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","sector":"battery / EV / green mobility","primary_archetype":"battery customer contract call-off risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive / CustomerCallOffRisk","trigger_date":"2024-04-25","evidence_available_at_that_date":"source_proxy_only=true; evidence_url_pending=true; sector-level EV demand/customer pacing risk at trigger date; source repair required before runtime promotion","evidence_source":"source_proxy:C12_EV_DEMAND_CUSTOMER_CALLOFF_RISK_2024Q2","stage2_evidence_fields":["electrolyte-additive supplier exposure","EV demand/customer pacing risk","weak order-refresh evidence"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin/utilization risk","post-peak drawdown","customer call-off sensitivity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv|atlas/ohlcv_tradable_by_symbol_year/278/278280/2025.csv","profile_path":"atlas/symbol_profiles/278/278280.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":73000,"MFE_30D_pct":12.6,"MFE_90D_pct":12.6,"MFE_180D_pct":12.6,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.6,"MAE_90D_pct":-21.37,"MAE_180D_pct":-51.51,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-12","peak_price":82200,"drawdown_after_peak_pct":-56.93,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.72,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_local_4B_watch_if_non_price_calloff_evidence_repaired","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; no profile-level corporate-action candidate","same_entry_group_id":"R3L83-C12-278280-20240425-20240425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L83-C12-121600-T1","case_id":"R3L83-C12-121600-20240425","symbol":"121600","company_name":"나노신소재","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","fine_archetype_id":"COPPER_FOIL_ELECTROLYTE_CNT_CUSTOMER_CALLOFF_RISK_VS_SHORT_RESTOCK_MFE_FADE","sector":"battery / EV / green mobility","primary_archetype":"battery customer contract call-off risk","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable-to-Local4B / CNTCustomerCallOffRisk","trigger_date":"2024-04-25","evidence_available_at_that_date":"source_proxy_only=true; evidence_url_pending=true; sector-level EV demand/customer pacing risk at trigger date; source repair required before runtime promotion","evidence_source":"source_proxy:C12_EV_DEMAND_CUSTOMER_CALLOFF_RISK_2024Q2","stage2_evidence_fields":["CNT conductive-additive supplier exposure","customer utilization/call-off risk","short squeeze-like restock MFE"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["post-peak drawdown","upstream customer pacing sensitivity","valuation reset"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv|atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv","profile_path":"atlas/symbol_profiles/121/121600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":114100,"MFE_30D_pct":31.29,"MFE_90D_pct":31.29,"MFE_180D_pct":31.29,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.18,"MAE_90D_pct":-27.08,"MAE_180D_pct":-49.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":149800,"drawdown_after_peak_pct":-61.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":0.95,"four_b_timing_verdict":"good_local_4B_watch_if_non_price_calloff_evidence_repaired","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown","valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_MFE_but_bridge_failed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate-action candidate is 2015-12-17, outside window","same_entry_group_id":"R3L83-C12-121600-20240425-20240425","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L83-C12-020150-20240425","trigger_id":"R3L83-C12-020150-T1","symbol":"020150","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":68,"stage_label_after":"Stage2-RiskWatch + Local4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 requires a customer call-off/order-pacing bridge. When evidence is only upstream material beta plus price MFE, execution risk and 4B watch should rise while Stage2/Green support falls.","MFE_90D_pct":24.37,"MAE_90D_pct":-24.89,"score_return_alignment_label":"risk_guard_success_with_late_damage","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L83-C12-278280-20240425","trigger_id":"R3L83-C12-278280-T1","symbol":"278280","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-FalsePositive / Local4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 requires a customer call-off/order-pacing bridge. When evidence is only upstream material beta plus price MFE, execution risk and 4B watch should rise while Stage2/Green support falls.","MFE_90D_pct":12.6,"MAE_90D_pct":-21.37,"score_return_alignment_label":"failed_rerating_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L83-C12-121600-20240425","trigger_id":"R3L83-C12-121600-T1","symbol":"121600","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","raw_component_scores_before":{"contract_score":3,"backlog_visibility_score":4,"margin_bridge_score":3,"revision_score":3,"relative_strength_score":6,"customer_quality_score":3,"policy_or_regulatory_score":2,"valuation_repricing_score":6,"execution_risk_score":6,"legal_or_contract_risk_score":1,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":79,"stage_label_before":"Stage2-Actionable / Yellow-candidate","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":2,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":4,"customer_quality_score":2,"policy_or_regulatory_score":1,"valuation_repricing_score":4,"execution_risk_score":8,"legal_or_contract_risk_score":2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-RiskWatch + Local4B-watch","changed_components":["backlog_visibility_score","margin_bridge_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C12 requires a customer call-off/order-pacing bridge. When evidence is only upstream material beta plus price MFE, execution risk and 4B watch should rise while Stage2/Green support falls.","MFE_90D_pct":31.29,"MAE_90D_pct":-27.08,"score_return_alignment_label":"high_MFE_but_bridge_failed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"residual_contribution","round":"R3","loop":"83","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["Stage2 false positive risk in upstream material suppliers","4B too late when short MFE fades into high MAE","customer call-off bridge missing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":true}
```

---

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat schema_rematerialization_only or duplicate_low_value_loop rows as promotion candidates.
- Treat `source_proxy_only=true` / `evidence_url_pending=true` rows as source-repair tasks before runtime promotion.
- Preserve R3/L3/C12 scoping.
- Do not weaken the existing global non-price 4B and hard 4C guardrails.
- Use this MD as a candidate for a C12-specific upstream supplier call-off bridge only after source repair.

### Implementation TODO

```text
1. Parse price_source_validation, case, trigger, score_simulation, shadow_weight, and residual_contribution rows.
2. Verify exact hard duplicate keys against v12_trigger_rows_validated.jsonl:
   canonical_archetype_id + symbol + trigger_type + entry_date
3. Repair source URLs for:
   - 020150 2024Q2 customer call-off / copper-foil supplier risk
   - 278280 2024Q2 electrolyte-additive utilization and demand fade
   - 121600 2024Q2 CNT customer call-off / short MFE fade
4. Recalculate MFE/MAE from stock-web local clone for exact reproducibility.
5. If source repair passes, add a C12 scoped guard proposal:
   C12_customer_calloff_bridge_required_for_upstream_supplier_stage2_actionable.
6. Keep production scoring unchanged unless future batch validation confirms the rule across additional rows.
```

---

## 27. Next Round State

```text
completed_round = R3
completed_loop = 83
next_round = R4
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

---

## 28. Source Notes

```text
MAIN EXECUTION PROMPT:
docs/core/e2r_v12_prompt_round_scheduler_corrected.txt

NO-REPEAT INDEX:
docs/core/V12_Research_No_Repeat_Index.md

PRICE ATLAS:
Songdaiki/stock-web
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/020/020150.json
atlas/symbol_profiles/278/278280.json
atlas/symbol_profiles/121/121600.json
atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv
atlas/ohlcv_tradable_by_symbol_year/020/020150/2025.csv
atlas/ohlcv_tradable_by_symbol_year/278/278280/2024.csv
atlas/ohlcv_tradable_by_symbol_year/278/278280/2025.csv
atlas/ohlcv_tradable_by_symbol_year/121/121600/2024.csv
atlas/ohlcv_tradable_by_symbol_year/121/121600/2025.csv
```
