# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK
loop_objective = coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
```

This loop continues loop 88 after R2. It adds 3 C14 battery/EV demand-slowdown cases: one true 4C protection row, one EV materials 4B-to-4C cap row, and one false-hard-4C recovery row.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
hard_4c_thesis_break_routes_to_4c = existing_axis_refined
local_4b_watch_guard = existing_axis_strengthened
stage2_required_bridge = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 88
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 88
```

R3 permits L3 battery/EV research. C14 is a risk/protection archetype: the issue is not merely that a stock went down, but whether the decline was backed by durable non-price evidence such as EV demand slowdown, customer call-off, utilization loss, price/margin collapse, or guidance break.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C14_EV_DEMAND_SLOWDOWN_4B_4C = 21 rows / 14 symbols / good-bad Stage2 3-3 / 4B-4C 6-4
top covered symbols include 006400(3), 373220(3), 095500(2), 247540(2), 278280(2), 003670(1)
```

Selected rows avoid the high-repeat C14 top list:

```text
361610 / Stage4C / 2024-01-05
051910 / Stage4B / 2023-07-26
011790 / Stage4C false-break / 2024-01-22
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| manifest | atlas/manifest.json |
| stock_web_manifest_max_date | 2026-02-20 |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |

| symbol | profile path | CA window status |
|---|---|---|
| 361610 | atlas/symbol_profiles/361/361610.json | no corporate-action candidate |
| 051910 | atlas/symbol_profiles/051/051910.json | no corporate-action candidate |
| 011790 | atlas/symbol_profiles/011/011790.json | selected 2024 window clean; CA candidates are 1998/2001 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C | 361610 | 2024-01-05 | yes | 180 | yes | yes | true |
| R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN | 051910 | 2023-07-26 | yes | 180 | yes | yes | true |
| R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY | 011790 | 2024-01-22 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C14_EV_DEMAND_SLOWDOWN_4B_4C | SEPARATOR_UTILIZATION_TRUE_4C | Durable utilization/customer slowdown can justify hard 4C protection. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_MATERIALS_4B_TO_4C_CAP | Materials premium can peak first; 4B should trigger before full thesis break is obvious. |
| C14_EV_DEMAND_SLOWDOWN_4B_4C | COPPERFOIL_FALSE_HARD_4C | Price break alone can be false if a new catalyst or non-EV rerating path appears. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C | 361610 | SK아이이테크놀로지 | true 4C / protection positive | Weak MFE and severe 180D MAE after separator demand/utilization break. |
| R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN | 051910 | LG화학 | counterexample / 4B-to-4C | EV materials premium peaked and converted into high MAE. |
| R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY | 011790 | SKC | counterexample / false hard 4C | January weakness recovered sharply; hard 4C would have been too aggressive. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 2
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

The positive row is a **risk-protection positive**, not a long-side positive.

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| SKIET separator true 4C | historical public/report proxy | true | true | hard-4C protection calibration |
| LG Chem EV materials 4B-to-4C | historical public/report proxy | true | true | 4B/4C timing calibration |
| SKC copperfoil false hard 4C | historical public/report proxy | true | true | hard-4C false-break guardrail |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 361610 | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | atlas/symbol_profiles/361/361610.json |
| 051910 | atlas/ohlcv_tradable_by_symbol_year/051/051910/2023.csv | atlas/symbol_profiles/051/051910.json |
| 011790 | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | atlas/symbol_profiles/011/011790.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK | 361610 | Stage4C | 2024-01-05 | 85200 | protection positive | true 4C |
| R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN | 051910 | Stage4B | 2023-07-26 | 728000 | counterexample/4B | 4B-to-4C cap |
| R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY | 011790 | Stage4C | 2024-01-22 | 75800 | false-break counterexample | hard 4C too aggressive |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK | 85200 | 1.53 | -23.59 | 1.53 | -24.18 | 1.53 | -64.73 | 2024-01-05 | 86500 | -65.26 |
| R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN | 728000 | 7.55 | -24.73 | 7.55 | -33.24 | 7.55 | -40.00 | 2023-07-26 | 783000 | -37.93 |
| R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY | 75800 | 25.33 | -5.15 | 94.59 | -5.15 | 94.59 | -5.15 | 2024-04-09 | 149700 | -15.23 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| hard_4c_thesis_break_routes_to_4c | refine: true when utilization/customer/margin break is durable; too hard when based on price break alone |
| local_4b_watch_guard | strengthen: EV materials premium can require 4B before full 4C confirmation |
| full_4b_requires_non_price_evidence | keep |
| stage2_required_bridge | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green Comparison

This loop does not introduce Stage3-Green. It is a protection/timing loop.

| symbol | stage quality | explanation |
|---|---|---|
| 361610 | true_4C | Very weak MFE and severe drawdown after separator/utilization weakness. |
| 051910 | good_4B | Peak/cap behavior appeared before the full drawdown was obvious. |
| 011790 | false_hard_4C | Price break alone would have exited before a strong recovery. |

```text
green_lateness_ratio = not_applicable
reason = C14 4B/4C protection/timing loop, no new Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 361610 separator break | 1.00 | 1.00 | true_4C_protection_after_EV_separator_utilization_break |
| 051910 EV materials cap | 1.00 | 1.00 | good_full_window_4B_timing_EV_materials_demand_slowdown |
| 011790 copperfoil false break | 0.00 | 0.00 | hard_4C_false_break_recovered_after_non_EV_catalyst_repricing |

## 16. 4C Protection Audit

| symbol | label | interpretation |
|---|---|---|
| 361610 | true_break | Hard 4C protection is justified when utilization/customer/margin break is durable. |
| 051910 | thesis_break_watch_only | 4B should come first; hard 4C needs more non-price confirmation. |
| 011790 | false_break | Price break alone should not become hard 4C. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery/EV, hard 4C requires durable non-price confirmation: customer call-off, utilization collapse, margin/price formula break, guidance cut, or capacity impairment. Price break alone should route to 4B/watch because new catalysts can create false hard-4C recovery.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
rule = C14 should split true demand/utilization thesis breaks from EV-materials event caps and false hard-4C price breaks. 4B should catch capped materials premium; hard 4C needs durable thesis-break evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_false_4C_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 34.56 | -20.86 | 0.67 | mixed; C14 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 34.56 | -20.86 | 0.67 | weaker 4B/4C distinction |
| P1 sector_specific_candidate_profile | L3 durable thesis-break required | 2 | 4.54 | -28.71 | 0.50 | better for protection |
| P2 canonical_archetype_candidate_profile | C14 true break vs false break split | 2 | 4.54 | -28.71 | 0.50 | best explanatory fit |
| P3 hard_4C_confirmation_profile | only durable break routes to hard 4C | 1 | 1.53 | -24.18 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 361610 separator break | 64 | Stage4B-watch | 50 | Stage4C | 1.53 | -24.18 | separator_utilization_true_4C_protection |
| 051910 EV materials cap | 70 | Stage3-Yellow-like | 55 | Stage4B-watch | 7.55 | -33.24 | EV_materials_event_cap_4B_guard |
| 011790 false hard 4C | 58 | Stage4C | 64 | Stage2-Watch/4B-watch | 94.59 | -5.15 | false_hard_4C_weakened_without_durable_break |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 2, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 1, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C14 separator true 4C, large-cap EV materials 4B-to-4C cap, and copper-foil false hard-4C recovery split."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence
residual_error_types_found: separator_utilization_true_4C, EV_materials_4B_to_4C_cap, copperfoil_price_break_false_hard_4C
new_axis_proposed: null
existing_axis_strengthened: local_4b_watch_guard
existing_axis_refined: hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: hard_4c only when based on price break without durable non-price thesis-break
existing_axis_kept: stage2_required_bridge, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C14 true 4C vs 4B event cap vs false hard-4C split
```

Non-validation scope:

```text
- Exact as-of evidence URLs remain pending for all selected cases.
- No production scoring update.
- No live candidate scan.
- No investment recommendation.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,hard_4c_confirmation,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,require_durable_customer_utilization_margin_break,0,"C14 hard 4C works when EV demand, utilization, customer call-off, or margin break is durable, but price break alone can be false","SKIET true 4C worked; SKC false hard-4C recovered strongly","R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK|R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,configured,cap_EV_materials_premium_as_4B_watch,0,"Large-cap EV materials premium can peak before full earnings downgrades; 4B watch should precede hard 4C if margin/call-off evidence is not complete","LG Chem 2023 peak converted into high MAE after EV materials cap","R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN",3,3,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "case_type": "risk_protection_success", "positive_or_counterexample": "positive", "best_trigger": "R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV separator demand/utilization break behaved like real C14 protection: very weak upside and severe 180D downside.", "current_profile_verdict": "current_profile_kept_true_4C_when_utilization_customer_calloff_and_margin_break_are_confirmed", "price_source": "Songdaiki/stock-web", "notes": "Risk/protection positive, not long-side positive. Exact as-of evidence URLs remain pending."}
{"row_type": "case", "case_id": "R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "case_type": "event_cap_4b_to_4c_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery-materials premium peaked around the trigger, then converted into large MAE; 4B/4C timing should be earlier than generic valuation watch.", "current_profile_verdict": "current_profile_4B_too_late_if_EV_materials_price_volume_margin_break_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Large-cap C14 risk path; source-proxy only."}
{"row_type": "case", "case_id": "R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "case_type": "false_break", "positive_or_counterexample": "counterexample", "best_trigger": "R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "A January EV/copper-foil weakness break would have been too hard as 4C because the price path later recovered sharply; hard 4C needs durable thesis-break confirmation.", "current_profile_verdict": "current_profile_4C_too_hard_if_price_break_without_durable_non_price_thesis_break", "price_source": "Songdaiki/stock-web", "notes": "False-hard-4C counterexample; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK", "case_id": "R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C", "symbol": "361610", "company_name": "SK아이이테크놀로지", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "sector": "battery_separator_EV_supply_chain", "primary_archetype": "separator_utilization_customer_calloff_true_4C", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-01-05", "entry_date": "2024-01-05", "entry_price": 85200.0, "evidence_available_at_that_date": "separator utilization / customer demand slowdown proxy; exact as-of report URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["EV_demand_slowdown", "margin_pressure_watch", "price_break"], "stage4c_evidence_fields": ["separator_utilization_break", "customer_calloff_risk", "sustained_downtrend_confirmation"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.53, "MFE_90D_pct": 1.53, "MFE_180D_pct": 1.53, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -23.59, "MAE_90D_pct": -24.18, "MAE_180D_pct": -64.73, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-05", "peak_price": 86500.0, "drawdown_after_peak_pct": -65.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "true_4C_protection_after_EV_separator_utilization_break", "four_b_evidence_type": ["margin_or_backlog_slowdown", "customer_calloff_risk", "positioning_overheat"], "four_c_protection_label": "true_break", "trigger_outcome_label": "true_4C_EV_separator_demand_slowdown_protection", "current_profile_verdict": "current_profile_kept_true_4C_when_utilization_customer_calloff_and_margin_break_are_confirmed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L88_C14_361610_2024-01-05_85200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN", "case_id": "R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN", "symbol": "051910", "company_name": "LG화학", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "sector": "battery_materials_large_cap", "primary_archetype": "EV_materials_price_volume_margin_break_4B_to_4C", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-07-26", "entry_date": "2023-07-26", "entry_price": 728000.0, "evidence_available_at_that_date": "EV/battery-materials price-volume and margin pressure proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["battery_materials_premium", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["EV_materials_peak", "post_peak_drawdown", "margin_or_price_pressure"], "stage4c_evidence_fields": ["demand_slowdown_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051910/2023.csv", "profile_path": "atlas/symbol_profiles/051/051910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.55, "MFE_90D_pct": 7.55, "MFE_180D_pct": 7.55, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -24.73, "MAE_90D_pct": -33.24, "MAE_180D_pct": -40.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-26", "peak_price": 783000.0, "drawdown_after_peak_pct": -37.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_EV_materials_demand_slowdown", "four_b_evidence_type": ["valuation_blowoff", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "EV_materials_4B_cap_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_EV_materials_price_volume_margin_break_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L88_C14_051910_2023-07-26_728000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY", "case_id": "R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY", "symbol": "011790", "company_name": "SKC", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "sector": "battery_copperfoil_materials", "primary_archetype": "copperfoil_weakness_false_hard_4C_recovery", "loop_objective": "coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4C", "trigger_date": "2024-01-22", "entry_date": "2024-01-22", "entry_price": 75800.0, "evidence_available_at_that_date": "EV/copper-foil weakness and price-break proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["EV_materials_weakness", "price_break_watch"], "stage4c_evidence_fields": ["hard_4C_not_confirmed_without_durable_thesis_break"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 25.33, "MFE_90D_pct": 94.59, "MFE_180D_pct": 94.59, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.15, "MAE_90D_pct": -5.15, "MAE_180D_pct": -5.15, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-09", "peak_price": 149700.0, "drawdown_after_peak_pct": -15.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "hard_4C_false_break_recovered_after_non_EV_catalyst_repricing", "four_b_evidence_type": ["price_only", "theme_rotation"], "four_c_protection_label": "false_break", "trigger_outcome_label": "hard_4C_false_break_recovered_strongly", "current_profile_verdict": "current_profile_4C_too_hard_if_price_break_without_durable_non_price_thesis_break", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R3L88_C14_011790_2024-01-22_75800", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_false_break_overlay", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L88_C14_SKIET_2024_SEPARATOR_UTILIZATION_TRUE_4C", "trigger_id": "R3L88_C14_SKIET_2024_STAGE4C_SEPARATOR_UTILIZATION_BREAK", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 40, "execution_risk_score": 65, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 64, "stage_label_before": "Stage4B-watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 50, "stage_label_after": "Stage4C", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "separator_utilization_true_4C_protection", "MFE_90D_pct": 1.53, "MAE_90D_pct": -24.18, "score_return_alignment_label": "separator_utilization_true_4C_protection", "current_profile_verdict": "current_profile_kept_true_4C_when_utilization_customer_calloff_and_margin_break_are_confirmed"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L88_C14_LGCHEM_2023_EV_MATERIALS_4B_TO_4C_SLOWDOWN", "trigger_id": "R3L88_C14_LGCHEM_2023_STAGE4B_EV_MATERIALS_DEMAND_SLOWDOWN", "symbol": "051910", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 40, "execution_risk_score": 65, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_materials_event_cap_4B_guard", "MFE_90D_pct": 7.55, "MAE_90D_pct": -33.24, "score_return_alignment_label": "EV_materials_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_EV_materials_price_volume_margin_break_not_capped"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L88_C14_SKC_2024_COPPERFOIL_FALSE_HARD_4C_RECOVERY", "trigger_id": "R3L88_C14_SKC_2024_STAGE4C_FALSE_BREAK_COPPERFOIL_GLASS_SUBSTRATE_RECOVERY", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 45, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 40, "execution_risk_score": 65, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 58, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 55, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 45, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2-Watch/4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "false_hard_4C_weakened_without_durable_break", "MFE_90D_pct": 94.59, "MAE_90D_pct": -5.15, "score_return_alignment_label": "false_hard_4C_weakened_without_durable_break", "current_profile_verdict": "current_profile_4C_too_hard_if_price_break_without_durable_non_price_thesis_break"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "SEPARATOR_CHEM_MATERIALS_EV_DEMAND_SLOWDOWN_TRUE_4C_VS_FALSE_BREAK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 2, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "hard_4c_thesis_break_routes_to_4c", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["separator_utilization_true_4C", "EV_materials_4B_to_4C_cap", "copperfoil_price_break_false_hard_4C"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C14_EV_DEMAND_SLOWDOWN_4B_4C","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 88
next_round = R4
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
