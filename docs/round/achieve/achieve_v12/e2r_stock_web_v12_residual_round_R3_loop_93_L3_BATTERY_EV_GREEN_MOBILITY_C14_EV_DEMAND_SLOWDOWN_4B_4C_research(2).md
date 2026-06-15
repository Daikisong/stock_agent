# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
schema_family: v12_sector_archetype_residual
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
selected_round: R3
selected_loop: 93
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id: C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id: EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK
loop_objective: coverage_gap_fill | counterexample_mining | 4B_4C_protection_test | stage2_actionable_bonus_stress_test | canonical_archetype_compression
generated_at: 2026-06-06
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 1. Current Calibrated Profile Assumption

Current proxy profile:

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

C14 is not a positive promotion archetype. It is a red-watch / 4B / 4C archetype. The important distinction is whether a battery/EV name is declining because of a real non-price thesis break, such as utilization cuts, customer call-off, order deferral, inventory, or price pressure, versus a headline-only fear that later recovers.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| selected_round | R3 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK |
| rule scope | canonical_archetype_specific |

Canonical compression:

```text
EV demand slowdown
→ utilization cut / inventory build / call-off / price pressure
→ Stage4B watch if non-price slowdown evidence is visible
→ Stage4C only if thesis evidence is broken
→ headline-only fear is not enough for hard 4C
```

## 3. Previous Coverage / Duplicate Avoidance Check

The No-Repeat Index marks C14 as Priority 0 with 21 rows and 9 more rows needed to reach the 30-row minimum. Top covered C14 symbols listed there include 336370, 222080, 361610, 011790, 014820, and 025900. This loop avoids those top-covered symbols and uses 373220, 247540, and 006400 as new C14 symbol/family coverage.

Duplicate policy used:

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
selected symbols are not top-covered C14 symbols
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web symbol profile checks:

| symbol | company | profile path | year shard | corporate-action window status |
|---|---|---|---|---|
| 373220 | LG에너지솔루션 | atlas/symbol_profiles/373/373220.json | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | clean_180D_window |
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | clean_180D_window |
| 006400 | 삼성SDI | atlas/symbol_profiles/006/006400.json | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | clean_180D_window |

## 5. Historical Eligibility Gate

All representative triggers below use a historical trigger date, have a tradable entry row in the Stock-Web shard, include high/low/close/volume, and have enough subsequent trading days within the Stock-Web atlas to observe the 180D window.

| case_id | entry_date | entry_price | forward_window_trading_days | calibration_usable | block reasons |
|---|---:|---:|---:|---|---|
| C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK | 2024-01-22 | 372000 | 180 | true | [] |
| C14_247540_2024_CATHODE_4B_SUCCESS | 2024-03-25 | 291000 | 180 | true | [] |
| C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS | 2024-03-25 | 486000 | 180 | true | [] |

## 6. Canonical Archetype Compression Map

| fine trigger family | compressed canonical interpretation | C14 role |
|---|---|---|
| headline_only_ev_demand_fear | EV demand headline without company-level utilization or order break | counterexample / false break |
| cathode_margin_inventory_slowdown | cathode price pressure + inventory + demand slowdown | 4B/4C positive guardrail |
| cell_utilization_mix_slowdown | cell maker utilization/mix pressure + EV demand cut | 4C positive guardrail |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | positive_or_counterexample | best_trigger |
|---|---|---|---|---|---|
| C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK | 373220 | LG에너지솔루션 | false_break | counterexample | Stage4C-Watch |
| C14_247540_2024_CATHODE_4B_SUCCESS | 247540 | 에코프로비엠 | 4B_overlay_success | positive | Stage4B |
| C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS | 006400 | 삼성SDI | 4C_success | positive | Stage4C |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
```

Interpretation:

- 247540 and 006400 support a C14 guardrail: when EV slowdown evidence is visible through margin/inventory/utilization channels, Stage4B/4C routing protects against large subsequent MAE.
- 373220 is the counterexample: broad EV demand fear alone, without a company-specific utilization/call-off/margin break, should remain watch-only rather than hard 4C.

## 9. Evidence Source Map

This loop uses source-proxy historical evidence labels rather than direct disclosure URLs. It is therefore valid for residual calibration but should be marked `evidence_url_pending=true` for later evidence repair.

| case | evidence available at trigger date | evidence source type | caveat |
|---|---|---|---|
| 373220 | EV demand fear, sector selloff, battery cell valuation de-rating | source_proxy_sector_news | headline-only; no hard company-specific thesis break in row |
| 247540 | cathode price pressure, inventory/demand slowdown, high valuation rebound | source_proxy_sector_news | use as 4B/4C, not positive Stage2 promotion |
| 006400 | cell utilization/mix pressure, EV slowdown, capacity/margin risk | source_proxy_sector_news | use as hard 4C candidate once non-price weakness confirmed |

## 10. Price Data Source Map

| symbol | shard path | key observed rows |
|---|---|---|
| 373220 | atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv | 2024-01-22 close 372000; 2024-07-25 low 313000; 2024-08-29 close 391000 |
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv | 2024-03-25 close 291000; 2024-04-17 low 215000; 2024-06-27 close 178000 |
| 006400 | atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv | 2024-03-25 close 486000; 2024-04-30 high 439500 after later date; 2024-11-15 low 235500 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | trigger family | outcome |
|---|---|---|---|---|---:|---|---|
| C14_373220_T1 | 373220 | Stage4C-Watch | 2024-01-19 | 2024-01-22 | 372000 | headline_only_ev_demand_fear | false_break_watch_only |
| C14_247540_T1 | 247540 | Stage4B | 2024-03-22 | 2024-03-25 | 291000 | cathode_margin_inventory_slowdown | good_4b_timing |
| C14_247540_T2 | 247540 | Stage4C | 2024-05-21 | 2024-05-22 | 204000 | cathode_demand_thesis_break | hard_4c_success |
| C14_006400_T1 | 006400 | Stage4C | 2024-03-22 | 2024-03-25 | 486000 | cell_utilization_mix_slowdown | hard_4c_success |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger metrics

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| C14_373220_T1 | 372000 | 13.4% | -3.8% | 13.4% | -11.2% | 15.5% | -15.9% | 2024-09-02 | 416500 | -24.8% |
| C14_247540_T1 | 291000 | 2.6% | -26.1% | 2.6% | -38.8% | 2.6% | -53.8% | 2024-03-27 | 298500 | -53.8% |
| C14_006400_T1 | 486000 | 1.7% | -16.5% | 1.7% | -27.8% | 1.7% | -51.5% | 2024-03-25 | 494500 | -52.4% |

### Interpretation

- 247540 and 006400 show a classic C14 pattern: small residual MFE after the trigger but very large downside once non-price demand/margin/utilization pressure is visible.
- 373220 shows why headline-only C14 cannot be routed directly to hard 4C. It had a material drawdown, but also meaningful MFE and later recovery; this is a watch-only false-break counterexample.

## 13. Current Calibrated Profile Stress Test

| case | current profile likely verdict | price alignment | residual error |
|---|---|---|---|
| 373220 | price-only / headline-only should not be hard 4C | correct if watch-only, false if hard 4C | headline_only_false_break |
| 247540 | 4B/4C if cathode margin/inventory evidence used | correct but may be late without C14-specific bridge | residual_4B_timing |
| 006400 | hard 4C if utilization/mix pressure evidence used | correct; protects against large subsequent drawdown | residual_4C_timing |

Stress answers:

```text
stage2_actionable_evidence_bonus: not relevant for positive promotion; should not rescue C14 names.
yellow threshold: not the key axis; C14 is red-watch-first.
green threshold: should remain strict; no Green unlock from price rebound.
price_only_blowoff guard: correct.
full_4b_requires_non_price_evidence: correct and should be C14-strengthened.
hard_4c_thesis_break routing: correct when utilization/call-off/margin evidence is present.
```

## 14. Stage2 / Yellow / Green Comparison

C14 should not loosen Stage2 or Stage3 gates. A battery/EV rebound during a demand slowdown can look like Stage2 or Yellow if one only watches relative strength. The proposed shadow rule requires explicit non-price bridge evidence before any positive stage label is allowed.

| case | Stage2-Actionable | Stage3-Yellow | Stage3-Green |
|---|---|---|---|
| 373220 | watch-only if no non-price break | no | no |
| 247540 | no positive Stage2; 4B overlay | no | no |
| 006400 | no positive Stage2; hard 4C | no | no |

## 15. 4B Local vs Full-window Timing Audit

| trigger | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---|---|
| C14_373220_T1 | n/a | n/a | price_only/headline_only | do_not_treat_as_full_4C |
| C14_247540_T1 | 0.97 | 0.97 | valuation_blowoff + margin_or_backlog_slowdown | good_full_window_4B_timing |
| C14_006400_T1 | 0.98 | 0.98 | revision_slowdown + margin_or_backlog_slowdown | good_full_window_4B_to_4C_timing |

## 16. 4C Protection Audit

| trigger | 4C label | protection verdict |
|---|---|---|
| C14_373220_T1 | thesis_break_watch_only | false_break if hard 4C |
| C14_247540_T2 | hard_4c_success | post-trigger MAE remains materially negative; avoids treating rebounds as Stage2 |
| C14_006400_T1 | hard_4c_success | strong protection against later drawdown |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
rule_candidate = In L3 battery/EV names, do not allow a positive Stage2/Yellow upgrade during an EV demand slowdown unless there is non-price proof of utilization recovery, call-off reversal, or margin/revision recovery.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
new_axis_proposed = c14_utilization_calloff_margin_break_routes_to_4c_shadow_only
```

Proposed shadow-only rule:

```text
if canonical_archetype_id == C14_EV_DEMAND_SLOWDOWN_4B_4C:
    if evidence includes utilization_cut or customer_calloff or inventory_build or margin_price_pressure:
        route_to_4B_or_4C_guardrail
    if evidence is headline_only or price_only:
        do_not_route_to_hard_4C
        set watch_only = true
    positive Stage2/Yellow requires explicit reversal evidence:
        utilization_recovery + calloff_reversal + margin/revision recovery
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg MFE_90D | avg MAE_90D | false positive rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current calibrated profile | 3 | 5.9% | -25.9% | 33% | needs C14-specific hard-break distinction |
| P1 sector_specific_candidate_profile | L3 EV slowdown requires non-price bridge | 3 | 5.9% | -25.9% | 0% if headline-only remains watch |
| P2 canonical_archetype_candidate_profile | C14 utilization/call-off/margin break routes to 4C | 3 | 5.9% | -25.9% | 0% |
| P3 counterexample_guard_profile | hard 4C blocked for headline-only evidence | 3 | 5.9% | -25.9% | 0% |

## 20. Score-Return Alignment Matrix

| case | score before | stage before | score after | stage after | alignment |
|---|---:|---|---:|---|---|
| 373220 | 76 | Stage4C if headline over-weighted | 62 | Stage4C-Watch | improved_false_break_control |
| 247540 | 72 | Stage2/4B ambiguous | 84 | Stage4B | improved_downside_protection |
| 006400 | 74 | late 4B | 88 | Stage4C | improved_downside_protection |

Component basis:

```json
{
  "canonical_component_keys": [
    "contract_score",
    "backlog_visibility_score",
    "margin_bridge_score",
    "revision_score",
    "relative_strength_score",
    "customer_quality_score",
    "policy_or_regulatory_score",
    "valuation_repricing_score",
    "execution_risk_score",
    "legal_or_contract_risk_score",
    "dilution_cb_risk_score",
    "accounting_trust_risk_score"
  ]
}
```

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK | 2 | 1 | 1 | 2 | 3 | 0 | 4 | 2 | true | true | C14 remains Priority 0 but improves from 21 rows toward 30 |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - headline_only_false_break
  - residual_4b_timing
  - residual_4c_timing
new_axis_proposed: c14_utilization_calloff_margin_break_routes_to_4c_shadow_only
existing_axis_strengthened: full_4b_requires_non_price_evidence scoped to C14 EV slowdown
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Uses stock-web tradable_raw 1D OHLC rows.
- Computes trigger-level MFE/MAE and peak/drawdown.
- Adds C14 coverage with new symbols and trigger families.
- Tests existing 4B/4C guardrails.
```

Non-validation scope:

```text
- No live recommendation.
- No production scoring change.
- No code patch.
- Source-proxy evidence requires later URL repair before promotion.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_utilization_calloff_margin_break_routes_to_4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"EV demand slowdown needs non-price thesis-break evidence before hard 4C; headline-only stays watch","reduces false hard-4C on 373220 while preserving protection on 247540/006400","C14_373220_T1|C14_247540_T1|C14_006400_T1",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,full_4b_requires_non_price_evidence_C14_scope,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,1,1.2,+0.2,"C14 4B should require utilization/call-off/margin evidence, not just price peak","improves 4B timing quality","C14_247540_T1|C14_006400_T1",2,2,0,medium,existing_axis_strengthened,"strengthen scoped guard only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","case_type":"false_break","positive_or_counterexample":"counterexample","best_trigger":"Stage4C-Watch","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"headline_only_hard_4c_false_break","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Headline-only EV demand fear should remain watch-only unless utilization/call-off/margin evidence confirms thesis break."}
{"row_type":"case","case_id":"C14_247540_2024_CATHODE_4B_SUCCESS","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4B_guardrail_aligned","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Cathode price/inventory/demand slowdown after rebound shows good 4B/4C guardrail use."}
{"row_type":"case","case_id":"C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C_guardrail_aligned","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Cell utilization/mix slowdown route protects against large later drawdown."}
{"row_type":"trigger","trigger_id":"C14_373220_T1","case_id":"C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK","symbol":"373220","company_name":"LG에너지솔루션","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_test","trigger_type":"Stage4C-Watch","trigger_date":"2024-01-19","entry_date":"2024-01-22","entry_price":372000,"evidence_available_at_that_date":"EV demand headline fear without company-specific utilization or call-off confirmation","evidence_source":"source_proxy_sector_news","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken_watch_only"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv","profile_path":"atlas/symbol_profiles/373/373220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.4,"MFE_90D_pct":13.4,"MFE_180D_pct":15.5,"MAE_30D_pct":-3.8,"MAE_90D_pct":-11.2,"MAE_180D_pct":-15.9,"peak_date":"2024-09-02","peak_price":416500,"drawdown_after_peak_pct":-24.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"headline_only_false_break_watch_only","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_373220_2024_01_22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C14_247540_T1","case_id":"C14_247540_2024_CATHODE_4B_SUCCESS","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_protection_test","trigger_type":"Stage4B","trigger_date":"2024-03-22","entry_date":"2024-03-25","entry_price":291000,"evidence_available_at_that_date":"cathode margin/inventory pressure and EV demand slowdown after rebound","evidence_source":"source_proxy_sector_news","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.6,"MFE_90D_pct":2.6,"MFE_180D_pct":2.6,"MAE_30D_pct":-26.1,"MAE_90D_pct":-38.8,"MAE_180D_pct":-53.8,"peak_date":"2024-03-27","peak_price":298500,"drawdown_after_peak_pct":-53.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.97,"four_b_full_window_peak_proximity":0.97,"trigger_outcome_label":"good_full_window_4B_timing","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_247540_2024_03_25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C14_247540_T2","case_id":"C14_247540_2024_CATHODE_4B_SUCCESS","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","loop_objective":"4C_confirmation","trigger_type":"Stage4C","trigger_date":"2024-05-21","entry_date":"2024-05-22","entry_price":204000,"evidence_available_at_that_date":"post-rebound failure with demand/margin pressure and lower-high structure","evidence_source":"source_proxy_sector_news","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.8,"MFE_90D_pct":9.8,"MFE_180D_pct":9.8,"MAE_30D_pct":-12.3,"MAE_90D_pct":-14.1,"MAE_180D_pct":-34.1,"peak_date":"2024-06-07","peak_price":224000,"drawdown_after_peak_pct":-34.1,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_247540_2024_05_22","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_different_trigger_family_4C_confirmation","independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"C14_006400_T1","case_id":"C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS","symbol":"006400","company_name":"삼성SDI","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"EV_DEMAND_SLOWDOWN_UTILIZATION_CALLOFF_4B_4C_VS_HEADLINE_ONLY_FALSE_BREAK","loop_objective":"coverage_gap_fill|4C_protection_test","trigger_type":"Stage4C","trigger_date":"2024-03-22","entry_date":"2024-03-25","entry_price":486000,"evidence_available_at_that_date":"EV demand slowdown, cell utilization/mix pressure and margin risk after rebound","evidence_source":"source_proxy_sector_news","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv","profile_path":"atlas/symbol_profiles/006/006400.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.7,"MFE_90D_pct":1.7,"MFE_180D_pct":1.7,"MAE_30D_pct":-16.5,"MAE_90D_pct":-27.8,"MAE_180D_pct":-51.5,"peak_date":"2024-03-25","peak_price":494500,"drawdown_after_peak_pct":-52.4,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"trigger_outcome_label":"hard_4c_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C14_006400_2024_03_25","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C14_373220_2024_HEADLINE_ONLY_FALSE_BREAK","trigger_id":"C14_373220_T1","symbol":"373220","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":40,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage4C_if_headline_overweighted","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":20,"relative_strength_score":35,"customer_quality_score":20,"policy_or_regulatory_score":0,"valuation_repricing_score":45,"execution_risk_score":30,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage4C-Watch","changed_components":["execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"headline-only EV demand fear is not enough for hard 4C","MFE_90D_pct":13.4,"MAE_90D_pct":-11.2,"score_return_alignment_label":"improved_false_break_control","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"C14_247540_2024_CATHODE_4B_SUCCESS","trigger_id":"C14_247540_T1","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":60,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":65,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2_or_4B_ambiguous","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":35,"relative_strength_score":50,"customer_quality_score":15,"policy_or_regulatory_score":0,"valuation_repricing_score":85,"execution_risk_score":80,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":84,"stage_label_after":"Stage4B","changed_components":["revision_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"non-price demand/margin pressure turns rebound into 4B/4C guardrail, not positive Stage2","MFE_90D_pct":2.6,"MAE_90D_pct":-38.8,"score_return_alignment_label":"improved_downside_protection","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"canonical_archetype_candidate_profile","case_id":"C14_006400_2024_CELL_UTILIZATION_4C_SUCCESS","trigger_id":"C14_006400_T1","symbol":"006400","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":25,"revision_score":30,"relative_strength_score":50,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":65,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"late_4B","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":35,"revision_score":45,"relative_strength_score":35,"customer_quality_score":25,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":85,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"utilization/mix slowdown evidence routes to hard 4C","MFE_90D_pct":1.7,"MAE_90D_pct":-27.8,"score_return_alignment_label":"improved_downside_protection","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R3","loop":"93","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["headline_only_false_break","residual_4b_timing","residual_4c_timing"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

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

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- For C14, distinguish headline-only EV demand fear from utilization/call-off/margin thesis break.
- Production scoring must not change unless the user explicitly asks for another promotion batch.

### Expected repository tasks

1. Parse case / trigger / score_simulation / shadow_weight / residual_contribution rows.
2. Validate stock-web price source fields.
3. Validate large_sector_id and canonical_archetype_id.
4. Validate novelty and reuse fields.
5. Deduplicate same_entry_group_id and reused cases.
6. Aggregate by large_sector_id and canonical_archetype_id.
7. Update sector_shadow_profile and archetype_shadow_profile only.
8. Preserve global calibrated profile unless explicitly promoted.
9. Report new independent cases, counterexamples, and residual error types.
10. Add tests that duplicate low-value loops cannot change weights.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
selected_round: R3
selected_loop: 93
next_recommended_archetypes:
  - C11_BATTERY_ORDERBOOK_RERATING
  - C02_POWER_GRID_DATACENTER_CAPEX
  - C19_BRAND_RETAIL_INVENTORY_MARGIN
```

## 28. Source Notes

Primary rows were read from:

```text
docs/core/V12_Research_No_Repeat_Index.md
atlas/manifest.json
atlas/symbol_profiles/373/373220.json
atlas/symbol_profiles/247/247540.json
atlas/symbol_profiles/006/006400.json
atlas/ohlcv_tradable_by_symbol_year/373/373220/2024.csv
atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006400/2024.csv
```

This is historical calibration research only, not a live investment recommendation.
