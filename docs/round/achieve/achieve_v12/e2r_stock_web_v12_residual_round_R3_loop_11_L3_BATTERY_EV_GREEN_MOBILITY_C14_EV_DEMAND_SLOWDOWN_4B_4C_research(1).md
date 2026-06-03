# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R3",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R3",
  "completed_loop": 11,
  "next_round": "R4",
  "next_loop": 11,
  "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY",
  "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C",
  "fine_archetype_id": "EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_4B_4C",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "green_strictness_stress_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 2,
  "diversity_score_summary": "estimated +41; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_entry_group_penalty=0; schema_rematerialization_penalty=0",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

No production scoring is changed. All rows are shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 11
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_4B_4C
round_schedule_status = valid
round_sector_consistency = pass
```

This file follows the R2 loop 11 handoff state and continues to R3 rather than jumping to a higher coverage gap elsewhere.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately relevant prior R3 file in local working artifacts was loop 10 / C13_BATTERY_JV_UTILIZATION_AMPC_IRA. That loop used LG에너지솔루션, 삼성SDI, and SK이노베이션/SK On narrative-only paths. This R3 loop intentionally avoids those representative symbols and moves to C14 with 에코프로비엠, 포스코퓨처엠, and 엘앤에프.

```text
same_canonical_archetype_research = not a duplicate because C14 differs from prior C13
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | profile corporate-action candidates | selected window status |
|---:|---|---|---|---|
| 247540 | 에코프로비엠 | atlas/symbol_profiles/247/247540.json | 2022-06-27, 2022-07-15 | clean for 2023/2024 windows |
| 003670 | 포스코퓨처엠 | atlas/symbol_profiles/003/003670.json | 2015-05-04, 2021-02-03 | clean for 2023/2024 windows |
| 066970 | 엘앤에프 | atlas/symbol_profiles/066/066970.json | 2016-02-19, 2021-08-11 | clean for 2023/2024 windows |
| 086520 | 에코프로 | atlas/symbol_profiles/086/086520.json | 2024-04-25 included | narrative-only / avoided for weight calibration |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false for representative rows
calibration_usable = true for representative rows
```

The 에코프로 path is deliberately not used quantitatively because the profile has a 2024-04-25 corporate-action candidate that can contaminate long windows.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| CATHODE_EV_DEMAND_SLOWDOWN_MARGIN_INVENTORY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Cathode/material names where EV demand slowdown turns into inventory, utilization and margin pressure. |
| BATTERY_MATERIAL_EV_DEMAND_SLOWDOWN_VALUATION_COMPRESSION | C14_EV_DEMAND_SLOWDOWN_4B_4C | Battery material valuation compression after 2023 rerating. |
| CATHODE_DEMAND_SLOWDOWN_HARD_4C_LATE_FALSE_BREAK | C14_EV_DEMAND_SLOWDOWN_4B_4C | Hard 4C risk when signal fires after capitulation rather than before damage. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R3L11_C14_247540_ECOPROBM_EV_SLOWDOWN_20240425 | 247540 | 에코프로비엠 | positive 4C-watch | Demand slowdown/inventory pressure had low MFE and deep MAE. |
| R3L11_C14_003670_POSCOFUTUREM_EV_SLOWDOWN_20240425 | 003670 | 포스코퓨처엠 | positive 4C-watch | Battery-material valuation compression had low MFE and deep MAE. |
| R3L11_C14_066970_LNF_HARD_4C_FALSE_BREAK_20231031 | 066970 | 엘앤에프 | counterexample | Hard 4C after price collapse would have caught a local bottom and missed a large rebound. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 2
4C_case_count = 3
```

The two positive cases say: once EV slowdown, inventory pressure and margin bridge damage are visible, positive Stage2/Yellow promotion should be capped. The counterexample says: once the chart is already broken and the evidence is mostly price collapse, hard 4C may be too late. C14 therefore behaves like a smoke alarm: it is useful when it catches the burning insulation, but noisy when it only rings after the fire has already been extinguished.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
|---:|---|---|---|
| 247540 | EV demand slowdown, cathode inventory and margin pressure | public result/news/report summary; exact URL enrichment required | quantitative |
| 003670 | battery-material demand slowdown and valuation compression | public result/news/report summary; exact URL enrichment required | quantitative |
| 066970 | already-discounted demand slowdown / price-collapse false break | public result/news/report summary; exact URL enrichment required | quantitative counterexample |
| 086520 | battery blowoff path | profile contaminated for long window | narrative-only |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 247540 | atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv and 2025.csv | atlas/symbol_profiles/247/247540.json | 2024-04-25 | usable |
| 003670 | atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv and 2025.csv | atlas/symbol_profiles/003/003670.json | 2024-04-25 | usable |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv and 2024.csv | atlas/symbol_profiles/066/066970.json | 2023-10-31 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 에코프로비엠 EV slowdown / inventory | 247540 | 4C-Watch | 2024-04-25 | 234,000 | +5.13% | +5.13% | +5.13% | -22.44% | -30.30% | -55.13% | 4C protection success |
| 포스코퓨처엠 EV slowdown / material valuation | 003670 | 4C-Watch | 2024-04-25 | 280,500 | +5.70% | +5.70% | +5.70% | -11.05% | -30.30% | -51.41% | 4C protection success |
| 엘앤에프 hard-4C late false break | 066970 | 4C-Hard-FalseBreak | 2023-10-31 | 130,400 | +51.84% | +66.41% | +66.41% | -1.92% | -1.92% | -6.83% | counterexample / hard 4C too late |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate:

| metric | 247540 | 003670 | 066970 |
|---|---:|---:|---:|
| entry_price | 234,000 | 280,500 | 130,400 |
| MFE_30D_pct | +5.13 | +5.70 | +51.84 |
| MFE_90D_pct | +5.13 | +5.70 | +66.41 |
| MFE_180D_pct | +5.13 | +5.70 | +66.41 |
| MAE_30D_pct | -22.44 | -11.05 | -1.92 |
| MAE_90D_pct | -30.30 | -30.30 | -1.92 |
| MAE_180D_pct | -55.13 | -51.41 | -6.83 |

Aggregate interpretation:

```text
positive_4C_watch_avg_MFE_90D_pct = 5.42
positive_4C_watch_avg_MAE_90D_pct = -30.30
positive_4C_watch_avg_MFE_180D_pct = 5.42
positive_4C_watch_avg_MAE_180D_pct = -53.27
hard_4C_false_break_MFE_90D_pct = 66.41
hard_4C_false_break_MAE_90D_pct = -1.92
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| 247540 EV slowdown | may remain Stage2/Yellow too long if customer quality/backlog language is still present | MFE stayed low and MAE became severe | current_profile_4C_too_late |
| 003670 EV/material slowdown | likely capped or demoted if slowdown evidence is recognized | low MFE / high MAE confirms cap | current_profile_correct |
| 066970 hard 4C after collapse | hard 4C routing could fire too late if price collapse is over-weighted | large rebound followed | current_profile_4C_too_late |

Axis verdict:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_strengthened for C14 when EV slowdown/inventory pressure is public
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_weakened for price-only capitulation after severe downleg
```

## 14. Stage2 / Yellow / Green Comparison

C14 differs from C11/C13 because backlog/orderbook or IRA subsidy language can linger while the demand signal has already turned. The correct split is:

```text
Stage2/Yellow allowed:
  policy/customer quality exists, but demand slowdown is not yet confirmed

Stage2/Yellow capped:
  EV demand slowdown + inventory pressure + margin bridge deterioration are visible

Green blocked:
  no fresh order/revision bridge after slowdown evidence

4C watch:
  slowdown evidence is non-price and still early enough to protect capital

Hard 4C:
  confirmed order cut, utilization break, liquidity/accounting issue, or customer loss

Hard 4C blocked:
  price-only capitulation after a large drawdown
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| 247540 2023-07-26 overlay | 1.00 | 1.00 | excellent risk overlay but not full 4B without non-price evidence |
| 003670 2023-07-26 overlay | 1.00 | 1.00 | excellent risk overlay but not full 4B without non-price evidence |
| 247540 2024-04-25 4C watch | not_applicable | not_applicable | non-price slowdown/demand evidence, not peak-only |
| 003670 2024-04-25 4C watch | not_applicable | not_applicable | non-price slowdown/demand evidence, not peak-only |

## 16. 4C Protection Audit

```text
247540: hard_4c_success_if_non_price_thesis_break_confirmed
003670: hard_4c_success_if_non_price_thesis_break_confirmed
066970: false_break_price_only_hard_4c
```

The 247540 and 003670 cases show that 4C-watch can protect capital when slowdown evidence is still economically live. The L&F case shows that a hard 4C after a deep prior drawdown can behave like locking the barn after the horse has already returned.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
candidate_axis = ev_slowdown_positive_stage_cap
```

Candidate rule:

```text
In L3 battery/EV names, EV demand slowdown plus inventory/margin pressure should cap positive Stage2/Yellow promotion unless a fresh order, revision, utilization or margin bridge reappears.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
new_axis_proposed:
  - c14_positive_stage_cap_on_ev_demand_slowdown
  - c14_price_only_collapse_routes_to_watch_not_hard4c
  - c14_blowoff_overlay_requires_later_non_price_confirmation
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | current representative | +25.75 | -20.84 | +25.75 | -37.79 | 0.33 | 0 | 1 | not_applicable | mixed; hard 4C false-break remains |
| P0b e2r_2_0_baseline_reference | 3 | current representative | +25.75 | -20.84 | +25.75 | -37.79 | 0.33 | 0 | 1 | not_applicable | too blunt on slowdown vs capitulation |
| P1 sector_specific_candidate_profile | 3 | C14 cap/watch | +5.42 protected / +66.41 blocked | -30.30 protected / -1.92 blocked | +5.42 protected / +66.41 blocked | -53.27 protected / -6.83 blocked | 0.00 | 0 | 0 | not_applicable | better separation |
| P2 canonical_archetype_candidate_profile | 3 | C14 cap/watch | +5.42 protected / +66.41 blocked | -30.30 protected / -1.92 blocked | +5.42 protected / +66.41 blocked | -53.27 protected / -6.83 blocked | 0.00 | 0 | 0 | not_applicable | best explanatory fit |
| P3 counterexample_guard_profile | 3 | hard 4C requires fresh non-price break | +25.75 | -20.84 | +25.75 | -37.79 | 0.00 hard-4C false-break | 0 | 0 | not_applicable | conservative but safer |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90/MAE90 | alignment |
|---|---:|---|---:|---|---|---|
| 247540 | 70.0 | Stage2-Watch_or_LateYellow | 58.0 | 4C-Thesis-Break-Watch | +5.13 / -30.30 | cap aligned |
| 003670 | 72.0 | Stage2-Actionable_too_generous | 60.0 | 4C-Thesis-Break-Watch | +5.70 / -30.30 | cap aligned |
| 066970 | 48.0 | 4C-Hard | 56.0 | 4C-WatchOnly_after_price_collapse | +66.41 / -1.92 | hard 4C too late |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_DEMAND_SLOWDOWN_INVENTORY_MARGIN_4B_4C | 2 | 1 | 2 | 3 | 3 | 0 | 5 | 3 | 2 | true | true | C14 now has two demand-slowdown 4C-watch successes and one hard-4C false-break counterexample; still needs more non-Korean EV OEM supplier holdouts. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - ev_slowdown_positive_stage_cap_needed
  - battery_material_inventory_margin_4c_watch_success
  - price_only_hard_4c_false_break_after_capitulation
  - price_only_blowoff_good_overlay_not_full_4b
new_axis_proposed:
  - c14_positive_stage_cap_on_ev_demand_slowdown
  - c14_price_only_collapse_routes_to_watch_not_hard4c
  - c14_blowoff_overlay_requires_later_non_price_confirmation
existing_axis_strengthened:
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened:
  - hard_4c_thesis_break_routes_to_4c, but only for price-only capitulation after severe downleg
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted price basis
- profile availability and corporate-action caveats for 247540, 003670, 066970, 086520
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE proxy calculations
- clean 180D corporate-action windows for selected quantitative rows
- R3/L3/C14 schedule consistency
```

Not validated:

```text
- production stock_agent source code
- live watchlist or current candidates
- brokerage execution
- exact original disclosure/report URLs for evidence text
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c14_positive_stage_cap_on_ev_demand_slowdown,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,+1,+1,"When EV demand slowdown plus inventory/margin pressure is public, cap Stage2/Yellow positive promotion unless fresh order/revision bridge reappears","247540 and 003670 showed MFE<=5.70 pct with 90D MAE around -30 pct","R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH|R3L11_T02_POSCOFUTUREM_20240425_EV_SLOWDOWN_4C_WATCH",3,3,1,medium,canonical_shadow_only,"not production; exact evidence URLs needed"
shadow_weight,c14_price_only_collapse_routes_to_watch_not_hard4c,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,-1,-1,"Price-only capitulation after a severe downleg can be a false break; require fresh order cut, liquidity, accounting, or customer loss for hard 4C","L&F 2023-10-31 hard 4C would have faced +66.41 pct 90D MFE with only -1.92 pct MAE","R3L11_T03_LNF_20231031_HARD_4C_FALSE_BREAK",3,3,1,medium,guardrail_shadow_only,"weakens hard 4C routing only when evidence is price-only and already late"
shadow_weight,c14_blowoff_overlay_requires_later_non_price_confirmation,sector_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,+0.5,+0.5,"2023 battery blowoff was excellent risk overlay but should not be promoted to full 4B without later demand/margin evidence","price-only July 2023 overlays had >23 pct MFE but >58 pct MAE over 90D; treat as watch/overlay, not standalone full 4B","R3L11_T01B_ECOPROBM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY|R3L11_T02B_POSCOFUTUREM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY",3,3,1,low,sector_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R3L11_C14_247540_ECOPROBM_EV_SLOWDOWN_20240425","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_MARGIN_INVENTORY","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Demand-slowdown / inventory-margin evidence aligned with low MFE and deep forward MAE.","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Positive C14 protection case: once EV demand slowdown and margin/inventory pressure were public, positive Stage labels should be capped unless order/revision bridge reappears."}
{"row_type":"case","case_id":"R3L11_C14_003670_POSCOFUTUREM_EV_SLOWDOWN_20240425","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EV_DEMAND_SLOWDOWN_VALUATION_COMPRESSION","case_type":"4C_success","positive_or_counterexample":"positive","best_trigger":"R3L11_T02_POSCOFUTUREM_20240425_EV_SLOWDOWN_4C_WATCH","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C-watch cap aligned: upside was small while 90D/180D downside was large.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C14 case with material demand slowdown and valuation compression; not a price-only peak trigger."}
{"row_type":"case","case_id":"R3L11_C14_066970_LNF_HARD_4C_FALSE_BREAK_20231031","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_DEMAND_SLOWDOWN_HARD_4C_LATE_FALSE_BREAK","case_type":"4C_late","positive_or_counterexample":"counterexample","best_trigger":"R3L11_T03_LNF_20231031_HARD_4C_FALSE_BREAK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Hard 4C at capitulation was too late; price-only collapse plus already-discounted slowdown rebounded sharply.","current_profile_verdict":"current_profile_4C_too_late","price_source":"Songdaiki/stock-web","notes":"Counterexample: C14 should not hard-route to 4C from price collapse alone after a severe downleg; require fresh thesis break, order cut, or liquidity/accounting failure."}
{"row_type":"trigger","trigger_id":"R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH","case_id":"R3L11_C14_247540_ECOPROBM_EV_SLOWDOWN_20240425","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_MARGIN_INVENTORY","sector":"2차전지·전기차·친환경","primary_archetype":"EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["coverage_gap_fill","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test","sector_specific_rule_discovery","canonical_archetype_compression"],"trigger_type":"4C-Thesis-Break-Watch","trigger_date":"2024-04-25","evidence_available_at_that_date":"EV demand slowdown, cathode material inventory/margin pressure, and weak positive-stage conversion after the 2023 battery rerating.","evidence_source":"public results/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["call_off_or_order_cut","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2024.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":234000,"MFE_30D_pct":5.13,"MFE_90D_pct":5.13,"MFE_180D_pct":5.13,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-22.44,"MAE_90D_pct":-30.3,"MAE_180D_pct":-55.13,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-30","peak_price":246000,"drawdown_after_peak_pct":-57.32,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_full_4B_late_4C_watch","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success_if_non_price_thesis_break_confirmed","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_247540_20240425_234000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_T01B_ECOPROBM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY","case_id":"R3L11_C14_247540_ECOPROBM_EV_SLOWDOWN_20240425","symbol":"247540","company_name":"에코프로비엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_EV_DEMAND_SLOWDOWN_MARGIN_INVENTORY","sector":"2차전지·전기차·친환경","primary_archetype":"EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["coverage_gap_fill","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test","sector_specific_rule_discovery","canonical_archetype_compression"],"trigger_type":"4B-Overlay-PriceOnly-LocalPeak","trigger_date":"2023-07-26","evidence_available_at_that_date":"Battery-sector price blowoff and positioning overheat before confirmed EV slowdown evidence.","evidence_source":"public results/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv","profile_path":"atlas/symbol_profiles/247/247540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":455000,"MFE_30D_pct":28.35,"MFE_90D_pct":28.35,"MFE_180D_pct":28.35,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-34.4,"MAE_90D_pct":-58.77,"MAE_180D_pct":-58.77,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":584000,"drawdown_after_peak_pct":-67.88,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_247540_20230726_455000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"price-only blowoff comparison row; not representative for aggregate positive promotion","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R3L11_T02_POSCOFUTUREM_20240425_EV_SLOWDOWN_4C_WATCH","case_id":"R3L11_C14_003670_POSCOFUTUREM_EV_SLOWDOWN_20240425","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EV_DEMAND_SLOWDOWN_VALUATION_COMPRESSION","sector":"2차전지·전기차·친환경","primary_archetype":"EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["coverage_gap_fill","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test","sector_specific_rule_discovery","canonical_archetype_compression"],"trigger_type":"4C-Thesis-Break-Watch","trigger_date":"2024-04-25","evidence_available_at_that_date":"Battery-material demand slowdown and valuation compression after 2023 rerating; positive-stage thesis required reset.","evidence_source":"public results/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2024.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-25","entry_price":280500,"MFE_30D_pct":5.7,"MFE_90D_pct":5.7,"MFE_180D_pct":5.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.05,"MAE_90D_pct":-30.3,"MAE_180D_pct":-51.41,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-25","peak_price":296500,"drawdown_after_peak_pct":-54.03,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"non_price_4C_watch_after_blowoff","four_b_evidence_type":["valuation_blowoff","revision_slowdown"],"four_c_protection_label":"hard_4c_success_if_non_price_thesis_break_confirmed","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_003670_20240425_280500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R3L11_T02B_POSCOFUTUREM_20230726_PRICE_ONLY_BLOWOFF_OVERLAY","case_id":"R3L11_C14_003670_POSCOFUTUREM_EV_SLOWDOWN_20240425","symbol":"003670","company_name":"포스코퓨처엠","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"BATTERY_MATERIAL_EV_DEMAND_SLOWDOWN_VALUATION_COMPRESSION","sector":"2차전지·전기차·친환경","primary_archetype":"EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["coverage_gap_fill","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test","sector_specific_rule_discovery","canonical_archetype_compression"],"trigger_type":"4B-Overlay-PriceOnly-LocalPeak","trigger_date":"2023-07-26","evidence_available_at_that_date":"Battery-material price blowoff/retail overheat before confirmed demand-slowdown evidence.","evidence_source":"public results/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv","profile_path":"atlas/symbol_profiles/003/003670.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-07-26","entry_price":560000,"MFE_30D_pct":23.93,"MFE_90D_pct":23.93,"MFE_180D_pct":23.93,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-28.57,"MAE_90D_pct":-58.66,"MAE_180D_pct":-58.66,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-07-26","peak_price":694000,"drawdown_after_peak_pct":-66.64,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_peak_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_003670_20230726_560000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"price-only blowoff comparison row; not representative for aggregate positive promotion","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R3L11_T03_LNF_20231031_HARD_4C_FALSE_BREAK","case_id":"R3L11_C14_066970_LNF_HARD_4C_FALSE_BREAK_20231031","symbol":"066970","company_name":"엘앤에프","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","fine_archetype_id":"CATHODE_DEMAND_SLOWDOWN_HARD_4C_LATE_FALSE_BREAK","sector":"2차전지·전기차·친환경","primary_archetype":"EV_DEMAND_SLOWDOWN_4B_4C","loop_objective":["coverage_gap_fill","counterexample_mining","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test","green_strictness_stress_test","sector_specific_rule_discovery","canonical_archetype_compression"],"trigger_type":"4C-Hard-FalseBreak","trigger_date":"2023-10-31","evidence_available_at_that_date":"Price had already collapsed after EV demand/inventory concern; hard 4C from price collapse alone would have sold the local bottom.","evidence_source":"public results/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv","profile_path":"atlas/symbol_profiles/066/066970.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-10-31","entry_price":130400,"MFE_30D_pct":51.84,"MFE_90D_pct":66.41,"MFE_180D_pct":66.41,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.92,"MAE_90D_pct":-1.92,"MAE_180D_pct":-6.83,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-01-02","peak_price":217000,"drawdown_after_peak_pct":-44.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_break_price_only_hard_4c","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R3L11_066970_20231031_130400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C14_247540_ECOPROBM_EV_SLOWDOWN_20240425","trigger_id":"R3L11_T01_ECOPROBM_20240425_EV_SLOWDOWN_4C_WATCH","symbol":"247540","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":38,"customer_quality_score":58,"policy_or_regulatory_score":0,"valuation_repricing_score":48,"execution_risk_score":62,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":72,"utilization_score":28,"positioning_overheat_score":54,"thesis_break_score":58},"weighted_score_before":70.0,"stage_label_before":"Stage2-Watch_or_LateYellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":22,"relative_strength_score":24,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":36,"execution_risk_score":76,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":86,"utilization_score":14,"positioning_overheat_score":64,"thesis_break_score":78},"weighted_score_after":58.0,"stage_label_after":"4C-Thesis-Break-Watch","changed_components":["revision_score","relative_strength_score","execution_risk_score","inventory_pressure_score","utilization_score","thesis_break_score"],"component_delta_explanation":"EV demand slowdown and inventory pressure cap positive stage; customer quality alone cannot offset utilization and margin break.","MFE_90D_pct":5.13,"MAE_90D_pct":-30.3,"score_return_alignment_label":"4C-watch cap aligned with low MFE/high MAE.","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C14_003670_POSCOFUTUREM_EV_SLOWDOWN_20240425","trigger_id":"R3L11_T02_POSCOFUTUREM_20240425_EV_SLOWDOWN_4C_WATCH","symbol":"003670","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":44,"relative_strength_score":42,"customer_quality_score":60,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":56,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":66,"utilization_score":30,"positioning_overheat_score":60,"thesis_break_score":56},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable_too_generous","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":26,"relative_strength_score":31,"customer_quality_score":52,"policy_or_regulatory_score":0,"valuation_repricing_score":40,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":82,"utilization_score":18,"positioning_overheat_score":66,"thesis_break_score":74},"weighted_score_after":60.0,"stage_label_after":"4C-Thesis-Break-Watch","changed_components":["revision_score","valuation_repricing_score","execution_risk_score","inventory_pressure_score","utilization_score","thesis_break_score"],"component_delta_explanation":"Battery-material valuation cannot remain positive when demand slowdown and inventory pressure depress the margin/revision bridge.","MFE_90D_pct":5.7,"MAE_90D_pct":-30.3,"score_return_alignment_label":"4C-watch cap aligned with small upside and deep drawdown.","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R3L11_C14_066970_LNF_HARD_4C_FALSE_BREAK_20231031","trigger_id":"R3L11_T03_LNF_20231031_HARD_4C_FALSE_BREAK","symbol":"066970","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":12,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":28,"execution_risk_score":84,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":82,"utilization_score":12,"positioning_overheat_score":10,"thesis_break_score":88},"weighted_score_before":48.0,"stage_label_before":"4C-Hard","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":20,"relative_strength_score":12,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":28,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"inventory_pressure_score":76,"utilization_score":12,"positioning_overheat_score":10,"thesis_break_score":62},"weighted_score_after":56.0,"stage_label_after":"4C-WatchOnly_after_price_collapse","changed_components":["execution_risk_score","inventory_pressure_score","thesis_break_score"],"component_delta_explanation":"At capitulation, price collapse alone should not be hard 4C unless fresh order cut/liquidity/accounting evidence appears.","MFE_90D_pct":66.41,"MAE_90D_pct":-1.92,"score_return_alignment_label":"Hard 4C was too late and would have missed a large rebound.","current_profile_verdict":"current_profile_4C_too_late"}
{"row_type":"residual_contribution","round":"R3","loop":"11","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["ev_slowdown_positive_stage_cap_needed","battery_material_inventory_margin_4c_watch_success","price_only_hard_4c_false_break_after_capitulation","price_only_blowoff_good_overlay_not_full_4b"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R3L11_C14_086520_ECOPRO_PRICE_PATH_BLOCKED","symbol":"086520","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"Ecopro 2023/2024 price path is relevant to battery blowoff but profile has a 2024-04-25 corporate-action candidate that can overlap long 2023/2024 windows, so this loop avoids using it for weight calibration.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not treat schema_rematerialization_only or duplicate_low_value_loop as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- price-only rows cannot promote Stage2/Stage3.
- If a v12 MD weakens an already applied axis, log it as residual counterexample rather than immediately reverting.
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
completed_round = R3
completed_loop = 11
next_round = R4
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json
- 247540 profile: atlas/symbol_profiles/247/247540.json
- 003670 profile: atlas/symbol_profiles/003/003670.json
- 066970 profile: atlas/symbol_profiles/066/066970.json
- 086520 profile: atlas/symbol_profiles/086/086520.json, narrative-only because of 2024-04-25 corporate-action candidate.
- 247540 OHLC: atlas/ohlcv_tradable_by_symbol_year/247/247540/2023.csv, 2024.csv, 2025.csv.
- 003670 OHLC: atlas/ohlcv_tradable_by_symbol_year/003/003670/2023.csv, 2024.csv, 2025.csv.
- 066970 OHLC: atlas/ohlcv_tradable_by_symbol_year/066/066970/2023.csv, 2024.csv.
- Evidence-source URLs require enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
