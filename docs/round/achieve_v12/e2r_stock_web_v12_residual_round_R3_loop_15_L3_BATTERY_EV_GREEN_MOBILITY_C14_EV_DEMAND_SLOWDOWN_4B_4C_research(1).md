# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R3
scheduled_loop = 15
completed_round = R3
completed_loop = 15
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C14_EV_DEMAND_SLOWDOWN_4B_4C
fine_archetype_id = EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET
output_file = e2r_stock_web_v12_residual_round_R3_loop_15_L3_BATTERY_EV_GREEN_MOBILITY_C14_EV_DEMAND_SLOWDOWN_4B_4C_research.md
round_schedule_status = valid
round_sector_consistency = pass
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R3/L3_BATTERY_EV_GREEN_MOBILITY/C14_EV_DEMAND_SLOWDOWN_4B_4C.

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

This MD does not re-prove those global axes. It stress-tests the C14 edge case: **pure EV-component utilization breaks should route faster to 4C, but diversified battery-material names with non-battery optionality must not be hard-4C routed from EV slowdown headlines alone.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R3 |
| scheduled_loop | 15 |
| large_sector_id | L3_BATTERY_EV_GREEN_MOBILITY |
| canonical_archetype_id | C14_EV_DEMAND_SLOWDOWN_4B_4C |
| fine_archetype_id | EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET |
| selected objective | coverage_gap_fill / counterexample_mining / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test / canonical_archetype_compression |

R3 is consistent with L3_BATTERY_EV_GREEN_MOBILITY. The filename, metadata, and next-round state are aligned.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 research artifacts already include R3 Loop 10 through Loop 14: C13, C14, C12, C11, and C14. Those covered LG에너지솔루션, 삼성SDI, LG화학, 포스코퓨처엠, 엘앤에프, 에코프로비엠, and SK이노베이션 narrative-only comparison anchors. This loop deliberately selects **361610 / 020150 / 011790**, none of which appears as a counted R3 C14 representative case in the prior local R3 C14 set.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
minimum_new_symbol_count = pass
minimum_counterexample_count = pass
minimum_positive_case_count = pass
```

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_data_source | Songdaiki/stock-web |
| source_repo_url | https://github.com/Songdaiki/stock-web |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX / KOSDAQ / KOSDAQ GLOBAL / KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The run uses stock-web manifest max_date, not current calendar date, to decide forward-window availability.

## 5. Historical Eligibility Gate

| symbol | profile_path | first_date | last_date | corporate action candidate dates relevant to window | eligibility |
|---|---|---:|---:|---|---|
| 361610 | atlas/symbol_profiles/361/361610.json | 2021-05-11 | 2026-02-20 | none | usable |
| 020150 | atlas/symbol_profiles/020/020150.json | 2011-03-04 | 2026-02-20 | none | usable |
| 011790 | atlas/symbol_profiles/011/011790.json | 1997-07-18 | 2026-02-20 | old 1998/2001 only, outside tested window | usable |

All representative triggers have entry rows in tradable shards, positive OHLCV, at least 180 forward trading rows, and no 180D corporate-action contamination.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| PURE_SEPARATOR_UTILIZATION_BREAK | C14_EV_DEMAND_SLOWDOWN_4B_4C | Pure separator utilization/order-drawdown evidence maps to hard 4C protection. |
| COPPERFOIL_SLOWDOWN_BUT_RELIEF_RALLY | C14_EV_DEMAND_SLOWDOWN_4B_4C | Copper foil slowdown is C14, but hard 4C requires confirmed call-off/utilization collapse. |
| DIVERSIFIED_BATTERY_MATERIAL_WITH_AI_OPTIONALITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV slowdown evidence is diluted by non-battery optionality; C14 should cap positive promotion but not force hard 4C. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | current_profile_verdict | notes |
|---|---:|---|---|---|---|---|
| R3L15-C14-361610-SKIET-SEPARATOR-UTILIZATION-BREAK-20240425 | 361610 | SK아이이테크놀로지 | 4C_success | positive | current_profile_4C_too_late | Pure EV separator exposure behaved like a thesis-break/protection case: little upside after late-April 2024 and deep 90D/180D MAE. The useful rule is not generic EV fear, but separator utilization/order-drawdown evidence. |
| R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425 | 020150 | 롯데에너지머티리얼즈 | high_mae_success | counterexample | current_profile_4C_too_early | Copper-foil EV slowdown evidence was real, but a late-April hard 4C label would have missed a +24% 90D MFE before the later collapse. It should be Stage2/4B-watch until utilization/order cuts confirm. |
| R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425 | 011790 | SKC | false_break | counterexample | current_profile_4C_too_early | Battery copper-foil weakness was offset by non-battery/semiconductor optionality. The stock produced very large 30D/90D MFE, so C14 must not route diversified material names to hard 4C from EV slowdown alone. |

## 8. Positive vs Counterexample Balance

| metric | value |
|---|---:|
| positive_case_count | 1 |
| counterexample_count | 2 |
| calibration_usable_case_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| current_profile_error_count | 3 |

The balance is intentionally asymmetric: C14 has many obvious hard-4C-looking battery cases, but the residual problem is **when the same slowdown evidence is too early or too blunt**.

## 9. Evidence Source Map

| symbol | evidence family | trigger evidence | stage implication |
|---:|---|---|---|
| 361610 | separator utilization/order drawdown | pure EV separator exposure with no offset option | hard 4C should fire faster |
| 020150 | copper foil slowdown | slowdown/inventory digestion visible but no immediate confirmed call-off | Stage2/4B watch first, hard 4C later |
| 011790 | diversified copper foil + non-battery optionality | EV slowdown exists, but semiconductor/glass-substrate optionality dominates price path | block hard 4C false break |

## 10. Price Data Source Map

| symbol | company | tradable_shard_used | profile_path | corporate action status |
|---:|---|---|---|---|
| 361610 | SK아이이테크놀로지 | atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv | atlas/symbol_profiles/361/361610.json | clean_180D_window |
| 020150 | 롯데에너지머티리얼즈 | atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv | atlas/symbol_profiles/020/020150.json | clean_180D_window |
| 011790 | SKC | atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv | atlas/symbol_profiles/011/011790.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | current_profile_verdict | aggregate_role |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| TRG-R3L15-C14-361610-4C-20240425 | 361610 | 4C-Thesis-Break | 2024-04-25 | 2024-04-25 | 61700 | 4.05 | -30.79 | 4.05 | -49.84 | 4.05 | -64.59 | 2024-04-29 | 64200 | current_profile_4C_too_late | representative |
| TRG-R3L15-C14-020150-STAGE2-WATCH-20240425 | 020150 | Stage2-Risk-Watch | 2024-04-25 | 2024-04-25 | 47600 | 19.75 | -7.14 | 24.37 | -35.92 | 24.37 | -52.63 | 2024-06-18 | 59200 | current_profile_4C_too_early | representative |
| TRG-R3L15-C14-020150-4B-OVERLAY-20240618 | 020150 | 4B-Overlay-Watch | 2024-06-18 | 2024-06-18 | 57300 | 3.32 | -36.65 | 3.32 | -46.77 | 3.32 | -64.66 | 2024-06-18 | 59200 | current_profile_correct | 4B_overlay_only |
| TRG-R3L15-C14-011790-STAGE2-WATCH-20240425 | 011790 | Stage2-Risk-Watch | 2024-04-25 | 2024-04-25 | 108400 | 62.64 | -6.55 | 84.5 | -6.55 | 84.5 | -6.55 | 2024-06-18 | 200000 | current_profile_4C_too_early | representative |
| TRG-R3L15-C14-011790-4B-OVERLAY-20240618 | 011790 | 4B-Overlay-Watch | 2024-06-18 | 2024-06-18 | 182000 | 9.89 | -19.12 | 9.89 | -42.69 | 9.89 | -42.75 | 2024-06-18 | 200000 | current_profile_correct | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative trigger return path

| symbol | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | interpretation |
|---:|---:|---:|---|---|---|---|
| 361610 | 2024-04-25 | 61700 | +4.05 / -30.79 | +4.05 / -49.84 | +4.05 / -64.59 | pure separator hard-4C success |
| 020150 | 2024-04-25 | 47600 | +19.75 / -7.14 | +24.37 / -35.92 | +24.37 / -52.63 | slowdown real, but hard 4C at entry too early |
| 011790 | 2024-04-25 | 108400 | +62.64 / -6.55 | +84.50 / -6.55 | +84.50 / -6.55 | EV slowdown false break because non-battery optionality dominated |

### 12.2 Peak / drawdown audit

| symbol | entry_price | full_window_peak | peak_date | drawdown_after_peak_pct | lesson |
|---:|---:|---:|---:|---:|---|
| 361610 | 61700 | 64200 | 2024-04-29 | -65.97 | 4C protection should not wait for price-only trend confirmation. |
| 020150 | 47600 | 59200 | 2024-06-18 | -61.91 | Hard 4C at initial slowdown would be early; 4B watch at relief peak is better. |
| 011790 | 108400 | 200000 | 2024-06-18 | -47.90 | Diversified optionality can overwhelm EV slowdown; use offset guard. |

## 13. Current Calibrated Profile Stress Test

| case_id | likely current behavior | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| R3L15-C14-361610-SKIET-SEPARATOR-UTILIZATION-BREAK-20240425 | May wait for explicit hard 4C thesis break and miss early protection. | MFE90 only +4.05 while MAE90 -49.84. | current_profile_4C_too_late |
| R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425 | Could over-route EV component slowdown to hard 4C. | MFE90 +24.37 before collapse, so initial hard 4C is early. | current_profile_4C_too_early |
| R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425 | Could misread battery weakness as hard 4C. | MFE90 +84.50; hard 4C would be a false break. | current_profile_4C_too_early |

## 14. Stage2 / Yellow / Green Comparison

No representative case receives a new Stage3-Green promotion. The useful C14 behavior is protective/risk routing, not positive entry scoring.

| symbol | Stage2/Watch entry | Green trigger | green_lateness_ratio | reason |
|---:|---:|---|---|---|
| 361610 | 2024-04-25 | none | not_applicable | hard 4C/risk case, not positive Green |
| 020150 | 2024-04-25 | none | not_applicable | slowdown watch; relief rally does not create durable Green |
| 011790 | 2024-04-25 | none | not_applicable | non-battery optionality prevents hard 4C but does not validate C14 Green |

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B watch entry | local peak proximity | full-window peak proximity | verdict |
|---:|---:|---:|---:|---|
| 020150 | 2024-06-18 close 57300 | 0.84 | 0.84 | Good 4B watch, but not full 4B without confirmed utilization/order evidence. |
| 011790 | 2024-06-18 close 182000 | 0.80 | 0.80 | Price-only 4B watch worked as risk overlay; still not positive scoring evidence. |
| 361610 | none | null | null | Direct 4C case, not a 4B peak-timing case. |

## 16. 4C Protection Audit

| symbol | 4C protection label | protection interpretation |
|---:|---|---|
| 361610 | hard_4c_success | Pure separator utilization break deserves faster hard-4C protection. |
| 020150 | false_break_if_applied_on_initial_watch | Hard 4C needs confirmation; early slowdown had +24.37% 90D MFE. |
| 011790 | false_break | Diversified optionality makes EV slowdown alone insufficient for hard 4C. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
candidate_axis_1 = C14_pure_separator_utilization_break_fast_4C
candidate_axis_2 = C14_diversified_optionality_offset_hard4c_guard
candidate_axis_3 = C14_price_only_peak_4B_watch_not_full4B
```

The rule is not global. It belongs to R3/C14 because the same EV slowdown evidence can mean three different things depending on business mix: immediate thesis break for pure utilization names, delayed watch for copper foil with relief-rally risk, and false hard-4C for diversified names with non-battery optionality.

## 18. Canonical-Archetype Rule Candidate

C14 should split the hard-4C route into two required questions:

1. **Is the company a pure EV component utilization name?** If yes, direct utilization/order-drawdown evidence can accelerate hard 4C.
2. **Is there offsetting non-battery optionality?** If yes, slowdown evidence should cap positive scoring and open a watch overlay, but not trigger hard 4C.

## 19. Before / After Backtest Comparison

| profile_id | selected cases | avg MFE90 | avg MAE90 | false positive/false break behavior |
|---|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 37.64 | -30.77 | Too blunt: can be late for pure separator and early for optionality names. |
| P0b e2r_2_0_baseline_reference | 3 | 37.64 | -30.77 | More likely to miss hard 4C and over-promote relief rallies. |
| P1 sector_specific_candidate_profile | 3 | 37.64 | -30.77 | Adds L3 EV-component utilization segmentation. |
| P2 canonical_archetype_candidate_profile | 3 | 37.64 | -30.77 | Best fit: C14 directness/optionality split. |
| P3 counterexample_guard_profile | 3 | 37.64 | -30.77 | Blocks hard-4C false breaks in 020150/011790. |

## 20. Score-Return Alignment Matrix

| profile_id | symbol | before_stage | before_score | after_stage | after_score | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---:|---|
| e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow | 361610 | 4C-Watch_too_late | 66 | Hard-4C | 58 | 4.05 | -49.84 | hard_4c_success_pure_separator_utilization_break |
| e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow | 020150 | 4C-Hard_too_early | 72 | Stage2-Risk-Watch | 64 | 24.37 | -35.92 | slowdown_watch_had_large_MFE_before_drawdown |
| counterexample_guard_profile | 020150 | 4B-PriceOnly-Watch | 74 | 4B-WatchOnly_not_Full4B | 69 | 3.32 | -46.77 | overlay_worked_but_not_positive_promotion |
| e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow | 011790 | 4C-Hard_false_break | 70 | Stage2-Risk-Watch_with_Optionality_Offset | 76 | 84.5 | -6.55 | battery_slowdown_false_4c_due_non_battery_optionality |
| counterexample_guard_profile | 011790 | 4B-PriceOnly-Watch | 74 | 4B-WatchOnly_not_Full4B | 69 | 9.89 | -42.69 | overlay_worked_but_not_positive_promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L3_BATTERY_EV_GREEN_MOBILITY | C14_EV_DEMAND_SLOWDOWN_4B_4C | EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET | 1 | 2 | 2 | 1 | 3 | 0 | 5 | 3 | 3 | false | true | More holdout needed for non-KOSPI small-cap component suppliers, but C14 directness/optionality split is now covered. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c, price_only_blowoff_blocks_positive_stage
residual_error_types_found: pure_separator_4c_too_late, copperfoil_hard_4c_too_early, diversified_optionality_false_break
new_axis_proposed: C14_pure_separator_utilization_break_fast_4C; C14_diversified_optionality_offset_hard4c_guard; C14_price_only_peak_4B_watch_not_full4B
existing_axis_strengthened: full_4b_requires_non_price_evidence
existing_axis_weakened: hard_4c_thesis_break_routes_to_4c needs C14 directness/optionality guard, not global rollback
existing_axis_kept: price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-Web manifest max_date and price basis.
- Tradable OHLC rows for 361610, 020150, 011790.
- 30D/90D/180D MFE and MAE on representative entry triggers.
- 4B local/full-window proximity split for relief-rally peaks.
- No 180D corporate-action contamination for selected windows.

Not validated:
- Live candidate status.
- Current market recommendation.
- Production scoring implementation.
- Broker/API execution.
- Any manifest max_date after 2026-02-20.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C14_pure_separator_utilization_break_fast_4C,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Pure separator exposure with direct utilization/order-drawdown evidence needs faster hard-4C routing.","361610 had MFE90 +4.05% vs MAE90 -49.84% and MAE180 -64.59%.",TRG-R3L15-C14-361610-4C-20240425,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_diversified_optionality_offset_hard4c_guard,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"EV slowdown alone must not hard-4C route copper-foil/diversified names when non-battery optionality or relief rally remains active.","020150 MFE90 +24.37% before collapse; 011790 MFE90 +84.50%.",TRG-R3L15-C14-020150-STAGE2-WATCH-20240425|TRG-R3L15-C14-011790-STAGE2-WATCH-20240425,3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C14_price_only_peak_4B_watch_not_full4B,canonical_archetype_specific,L3_BATTERY_EV_GREEN_MOBILITY,C14_EV_DEMAND_SLOWDOWN_4B_4C,0,1,+1,"Price proximity around relief-rally peaks is useful as 4B watch, but full 4B still requires non-price deterioration.","020150 and 011790 peak overlays worked as risk labels but are excluded from positive promotion.",TRG-R3L15-C14-020150-4B-OVERLAY-20240618|TRG-R3L15-C14-011790-4B-OVERLAY-20240618,2,0,0,medium,guardrail_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "source_name": "FinanceData/marcap", "min_date": "1995-05-02", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546, "markets": ["KONEX", "KOSDAQ", "KOSDAQ GLOBAL", "KOSPI"], "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R3L15-C14-361610-SKIET-SEPARATOR-UTILIZATION-BREAK-20240425", "symbol": "361610", "company_name": "SK아이이테크놀로지", "case_type": "4C_success", "positive_or_counterexample": "positive", "best_trigger": "TRG-R3L15-C14-361610-4C-20240425", "current_profile_verdict": "current_profile_4C_too_late", "score_price_alignment": "hard_4c_success_pure_separator_utilization_break", "notes": "Pure EV separator exposure behaved like a thesis-break/protection case: little upside after late-April 2024 and deep 90D/180D MAE. The useful rule is not generic EV fear, but separator utilization/order-drawdown evidence.", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L15-C14-020150-STAGE2-WATCH-20240425", "current_profile_verdict": "current_profile_4C_too_early", "score_price_alignment": "slowdown_watch_had_large_MFE_before_drawdown", "notes": "Copper-foil EV slowdown evidence was real, but a late-April hard 4C label would have missed a +24% 90D MFE before the later collapse. It should be Stage2/4B-watch until utilization/order cuts confirm.", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425", "symbol": "011790", "company_name": "SKC", "case_type": "false_break", "positive_or_counterexample": "counterexample", "best_trigger": "TRG-R3L15-C14-011790-STAGE2-WATCH-20240425", "current_profile_verdict": "current_profile_4C_too_early", "score_price_alignment": "battery_slowdown_false_4c_due_non_battery_optionality", "notes": "Battery copper-foil weakness was offset by non-battery/semiconductor optionality. The stock produced very large 30D/90D MFE, so C14 must not route diversified material names to hard 4C from EV slowdown alone.", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "trigger", "trigger_id": "TRG-R3L15-C14-361610-4C-20240425", "case_id": "R3L15-C14-361610-SKIET-SEPARATOR-UTILIZATION-BREAK-20240425", "symbol": "361610", "company_name": "SK아이이테크놀로지", "trigger_type": "4C-Thesis-Break", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 61700, "evidence_available_at_that_date": "Late-April 2024 EV separator chain pressure: utilization/order-drawdown risk visible in a pure separator supplier without offsetting non-battery optionality.", "evidence_source": "Sector Q1-2024 EV separator slowdown/utilization evidence; stock-web 361610 tradable shard rows around 2024-04-25, 2024-08-05, 2025-01-02.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "revision_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/361/361610/2024.csv", "profile_path": "atlas/symbol_profiles/361/361610.json", "MFE_30D_pct": 4.05, "MFE_90D_pct": 4.05, "MFE_180D_pct": 4.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -30.79, "MAE_90D_pct": -49.84, "MAE_180D_pct": -64.59, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-29", "peak_price": 64200, "drawdown_after_peak_pct": -65.97, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["margin_or_backlog_slowdown", "revision_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_4C_too_late", "same_entry_group_id": "R3L15-C14-361610-20240425-61700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "sector": "2차전지·전기차·친환경", "primary_archetype": "EV_DEMAND_SLOWDOWN_4B_4C", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "canonical_archetype_compression"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L15-C14-020150-STAGE2-WATCH-20240425", "case_id": "R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "trigger_type": "Stage2-Risk-Watch", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 47600, "evidence_available_at_that_date": "Copper-foil EV demand slowdown/inventory digestion risk was visible, but direct call-off/utilization collapse was not yet confirmed at the stock level.", "evidence_source": "Sector Q1-2024 copper-foil slowdown evidence; stock-web 020150 rows: 2024-04-25 close 47,600, 2024-06-18 high 59,200, 2025-01-02 low 22,550.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "revision_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "MFE_30D_pct": 19.75, "MFE_90D_pct": 24.37, "MFE_180D_pct": 24.37, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.14, "MAE_90D_pct": -35.92, "MAE_180D_pct": -52.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 59200, "drawdown_after_peak_pct": -61.91, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["revision_slowdown", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_false_break_if_applied_on_2024-04-25", "trigger_outcome_label": "high_mae_success_counterexample", "current_profile_verdict": "current_profile_4C_too_early", "same_entry_group_id": "R3L15-C14-020150-20240425-47600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "sector": "2차전지·전기차·친환경", "primary_archetype": "EV_DEMAND_SLOWDOWN_4B_4C", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "canonical_archetype_compression"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L15-C14-020150-4B-OVERLAY-20240618", "case_id": "R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425", "symbol": "020150", "company_name": "롯데에너지머티리얼즈", "trigger_type": "4B-Overlay-Watch", "trigger_date": "2024-06-18", "entry_date": "2024-06-18", "entry_price": 57300, "evidence_available_at_that_date": "After a relief rally, copper-foil slowdown plus price extension created a 4B watch candidate; it still needs non-price confirmation to become full 4B.", "evidence_source": "stock-web 020150 peak window; 2024-06-18 close 57,300 / high 59,200.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/020/020150/2024.csv", "profile_path": "atlas/symbol_profiles/020/020150.json", "MFE_30D_pct": 3.32, "MFE_90D_pct": 3.32, "MFE_180D_pct": 3.32, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -36.65, "MAE_90D_pct": -46.77, "MAE_180D_pct": -64.66, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 59200, "drawdown_after_peak_pct": -65.79, "green_lateness_ratio": "not_applicable_4B_overlay", "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "good_watch_overlay_but_not_full_4B_without_non_price_confirmation", "four_b_evidence_type": ["price_only", "revision_slowdown"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R3L15-C14-020150-20240618-57300", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "sector": "2차전지·전기차·친환경", "primary_archetype": "EV_DEMAND_SLOWDOWN_4B_4C", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "canonical_archetype_compression"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "reuse_reason": "same case; overlay trigger only; excluded from aggregate representative count", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TRG-R3L15-C14-011790-STAGE2-WATCH-20240425", "case_id": "R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425", "symbol": "011790", "company_name": "SKC", "trigger_type": "Stage2-Risk-Watch", "trigger_date": "2024-04-25", "entry_date": "2024-04-25", "entry_price": 108400, "evidence_available_at_that_date": "Battery copper-foil weakness existed, but SKC also carried non-battery semiconductor/glass-substrate optionality. EV slowdown alone was not enough for hard 4C.", "evidence_source": "Sector EV copper-foil slowdown plus stock-web 011790 rows: 2024-04-25 close 108,400, 2024-06-18 high 200,000, 2025-01-02 low 104,200.", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "MFE_30D_pct": 62.64, "MFE_90D_pct": 84.5, "MFE_180D_pct": 84.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.55, "MAE_90D_pct": -6.55, "MAE_180D_pct": -6.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 200000, "drawdown_after_peak_pct": -47.9, "green_lateness_ratio": "not_applicable_no_confirmed_stage3_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "false_break", "trigger_outcome_label": "false_break_counterexample", "current_profile_verdict": "current_profile_4C_too_early", "same_entry_group_id": "R3L15-C14-011790-20240425-108400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "sector": "2차전지·전기차·친환경", "primary_archetype": "EV_DEMAND_SLOWDOWN_4B_4C", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "canonical_archetype_compression"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TRG-R3L15-C14-011790-4B-OVERLAY-20240618", "case_id": "R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425", "symbol": "011790", "company_name": "SKC", "trigger_type": "4B-Overlay-Watch", "trigger_date": "2024-06-18", "entry_date": "2024-06-18", "entry_price": 182000, "evidence_available_at_that_date": "Price extension reached the full-window peak zone; because non-price 4B evidence was incomplete, this remains a 4B watch overlay rather than a full 4B exit rule.", "evidence_source": "stock-web 011790 peak window; 2024-06-18 close 182,000 / high 200,000.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011790/2024.csv", "profile_path": "atlas/symbol_profiles/011/011790.json", "MFE_30D_pct": 9.89, "MFE_90D_pct": 9.89, "MFE_180D_pct": 9.89, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -19.12, "MAE_90D_pct": -42.69, "MAE_180D_pct": -42.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-18", "peak_price": 200000, "drawdown_after_peak_pct": -47.9, "green_lateness_ratio": "not_applicable_4B_overlay", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "price_only_4B_watch_not_full_4B", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R3L15-C14-011790-20240618-182000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "fine_archetype_id": "EV_COMPONENT_UTILIZATION_BREAK_VS_OPTIONALITY_OFFSET", "sector": "2차전지·전기차·친환경", "primary_archetype": "EV_DEMAND_SLOWDOWN_4B_4C", "loop_objective": ["coverage_gap_fill", "counterexample_mining", "4B_non_price_requirement_stress_test", "4C_thesis_break_timing_test", "canonical_archetype_compression"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "reuse_reason": "same case; overlay trigger only; excluded from aggregate representative count", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "case_id": "R3L15-C14-361610-SKIET-SEPARATOR-UTILIZATION-BREAK-20240425", "trigger_id": "TRG-R3L15-C14-361610-4C-20240425", "symbol": "361610", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 18, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 22, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 78, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "ev_demand_slowdown_score": 88, "utilization_break_score": 90, "optionality_offset_score": 5}, "weighted_score_before": 66, "stage_label_before": "4C-Watch_too_late", "raw_component_scores_after": {"contract_score": 20, "backlog_visibility_score": 18, "margin_bridge_score": 12, "revision_score": 16, "relative_strength_score": 22, "customer_quality_score": 35, "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 78, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 8, "ev_demand_slowdown_score": 92, "utilization_break_score": 95, "optionality_offset_score": 0}, "weighted_score_after": 58, "stage_label_after": "Hard-4C", "changed_components": ["utilization_break_score", "ev_demand_slowdown_score", "optionality_offset_score"], "component_delta_explanation": "Pure separator names require faster hard-4C routing when utilization/order-drawdown evidence is direct and offset optionality is absent.", "MFE_90D_pct": 4.05, "MAE_90D_pct": -49.84, "score_return_alignment_label": "hard_4c_success_pure_separator_utilization_break", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "case_id": "R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425", "trigger_id": "TRG-R3L15-C14-020150-STAGE2-WATCH-20240425", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 34, "backlog_visibility_score": 32, "margin_bridge_score": 25, "revision_score": 28, "relative_strength_score": 48, "customer_quality_score": 45, "policy_or_regulatory_score": 40, "valuation_repricing_score": 45, "execution_risk_score": 58, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 7, "ev_demand_slowdown_score": 70, "utilization_break_score": 42, "optionality_offset_score": 22}, "weighted_score_before": 72, "stage_label_before": "4C-Hard_too_early", "raw_component_scores_after": {"contract_score": 34, "backlog_visibility_score": 32, "margin_bridge_score": 25, "revision_score": 28, "relative_strength_score": 48, "customer_quality_score": 45, "policy_or_regulatory_score": 40, "valuation_repricing_score": 45, "execution_risk_score": 58, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 7, "ev_demand_slowdown_score": 58, "utilization_break_score": 30, "optionality_offset_score": 28}, "weighted_score_after": 64, "stage_label_after": "Stage2-Risk-Watch", "changed_components": ["hard_4c_confirmation_required", "utilization_break_score", "ev_demand_slowdown_score"], "component_delta_explanation": "Copper-foil slowdown without confirmed call-off should stay as Stage2/4B watch; early hard 4C would have missed a large relief MFE.", "MFE_90D_pct": 24.37, "MAE_90D_pct": -35.92, "score_return_alignment_label": "slowdown_watch_had_large_MFE_before_drawdown", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L15-C14-020150-LEM-COPPERFOIL-SLOWDOWN-BUT-REBOUND-20240425", "trigger_id": "TRG-R3L15-C14-020150-4B-OVERLAY-20240618", "symbol": "020150", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 78, "execution_risk_score": 48, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5, "positioning_overheat_score": 84, "non_price_4b_confirmation_score": 20}, "weighted_score_before": 74, "stage_label_before": "4B-PriceOnly-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 78, "execution_risk_score": 48, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5, "positioning_overheat_score": 84, "non_price_4b_confirmation_score": 15}, "weighted_score_after": 69, "stage_label_after": "4B-WatchOnly_not_Full4B", "changed_components": ["non_price_4b_confirmation_score"], "component_delta_explanation": "Price proximity is allowed as a watch overlay, but full 4B remains blocked unless non-price deterioration confirms.", "MFE_90D_pct": 3.32, "MAE_90D_pct": -46.77, "score_return_alignment_label": "overlay_worked_but_not_positive_promotion", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C14_shadow", "case_id": "R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425", "trigger_id": "TRG-R3L15-C14-011790-STAGE2-WATCH-20240425", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 28, "backlog_visibility_score": 30, "margin_bridge_score": 22, "revision_score": 26, "relative_strength_score": 78, "customer_quality_score": 42, "policy_or_regulatory_score": 55, "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 6, "ev_demand_slowdown_score": 62, "utilization_break_score": 25, "optionality_offset_score": 88}, "weighted_score_before": 70, "stage_label_before": "4C-Hard_false_break", "raw_component_scores_after": {"contract_score": 28, "backlog_visibility_score": 30, "margin_bridge_score": 22, "revision_score": 26, "relative_strength_score": 78, "customer_quality_score": 42, "policy_or_regulatory_score": 55, "valuation_repricing_score": 72, "execution_risk_score": 45, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 6, "ev_demand_slowdown_score": 45, "utilization_break_score": 20, "optionality_offset_score": 95}, "weighted_score_after": 76, "stage_label_after": "Stage2-Risk-Watch_with_Optionality_Offset", "changed_components": ["optionality_offset_score", "hard_4c_block_for_diversified_optionality", "ev_demand_slowdown_score"], "component_delta_explanation": "Diversified battery-material names with non-battery AI/semiconductor optionality must not be hard-4C routed from EV slowdown evidence alone.", "MFE_90D_pct": 84.5, "MAE_90D_pct": -6.55, "score_return_alignment_label": "battery_slowdown_false_4c_due_non_battery_optionality", "current_profile_verdict": "current_profile_4C_too_early"}
{"row_type": "score_simulation", "profile_id": "counterexample_guard_profile", "case_id": "R3L15-C14-011790-SKC-COPPERFOIL-WEAKNESS-AI-OPTIONALITY-20240425", "trigger_id": "TRG-R3L15-C14-011790-4B-OVERLAY-20240618", "symbol": "011790", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 78, "execution_risk_score": 48, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5, "positioning_overheat_score": 84, "non_price_4b_confirmation_score": 20}, "weighted_score_before": 74, "stage_label_before": "4B-PriceOnly-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 25, "relative_strength_score": 82, "customer_quality_score": 30, "policy_or_regulatory_score": 25, "valuation_repricing_score": 78, "execution_risk_score": 48, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 5, "accounting_trust_risk_score": 5, "positioning_overheat_score": 84, "non_price_4b_confirmation_score": 15}, "weighted_score_after": 69, "stage_label_after": "4B-WatchOnly_not_Full4B", "changed_components": ["non_price_4b_confirmation_score"], "component_delta_explanation": "Price proximity is allowed as a watch overlay, but full 4B remains blocked unless non-price deterioration confirms.", "MFE_90D_pct": 9.89, "MAE_90D_pct": -42.69, "score_return_alignment_label": "overlay_worked_but_not_positive_promotion", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R3", "loop": "15", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C14_EV_DEMAND_SLOWDOWN_4B_4C", "scheduled_round": "R3", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "current_profile_error_count": 3, "diversity_score_summary": "estimated +47; new C14 symbols 361610/020150/011790; pure separator 4C success plus copper-foil/diversified false-break counterexamples; wrong_round_penalty=0", "tested_existing_calibrated_axes": ["full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["pure_separator_4c_too_late", "copperfoil_hard_4c_too_early", "diversified_optionality_false_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 15
next_round = R4
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest read in this execution: max_date=2026-02-20, price_adjustment_status=raw_unadjusted_marcap, calibration_shard_root=atlas/ohlcv_tradable_by_symbol_year.
- 361610 profile: corporate_action_candidate_count=0; tested rows include 2024-04-25 close 61,700, 2024-04-29 high 64,200, 2024-08-05 low 30,950, and 2025-01-02 low 21,850.
- 020150 profile: corporate_action_candidate_count=0; tested rows include 2024-04-25 close 47,600, 2024-06-18 high 59,200, and 2025-01-02 low 22,550.
- 011790 profile: corporate-action candidates are old 1998/2001 dates outside the tested window; tested rows include 2024-04-25 close 108,400, 2024-06-18 high 200,000, and 2025-01-02 low 104,200.
