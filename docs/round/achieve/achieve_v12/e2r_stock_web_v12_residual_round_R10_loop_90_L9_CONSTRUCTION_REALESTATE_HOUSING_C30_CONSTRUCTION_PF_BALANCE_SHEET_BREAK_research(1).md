# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R10
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
fine_archetype_id = LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R10_loop_90_L9_CONSTRUCTION_REALESTATE_HOUSING_C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK_research.md
```

This loop corrects the current run to the scheduled R10 / loop 90 state. It adds 3 C30 construction/PF balance-sheet cases: one large-builder PF discount-repair positive, one regional-construction false Stage2, and one political/construction 4B event-cap counterexample.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R10
scheduled_loop = 90
large_sector_id = L9_CONSTRUCTION_REALESTATE_HOUSING
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
round_sector_consistency = pass
computed_next_round = R11
computed_next_loop = 90
```

R10 is the L9 construction/PF round. Previous R10 loop 89 used C30 with different symbols, so this loop stays in C30 but avoids the previous R10 rows and high-repeat coverage symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK = 81 rows / 31 symbols / good-bad Stage2 16-29 / 4B-4C 3-4
top covered symbols include 002990(6), 294870(6), 375500(6), 004960(5), 013580(5), 006360(4)
previous R10 loop-88 symbols avoided: 035890, 028100, 009410
previous R10 loop-89 symbols avoided: 010780, 005960, 001470
previous R9 loop-90 C29 symbols avoided: 123410, 092200, 023810
```

Selected rows avoid those repeated combinations:

```text
000720 / Stage2-Actionable / 2024-01-24
002460 / Stage2-Actionable / 2024-02-01
013360 / Stage4B / 2024-07-23
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
| 000720 | atlas/symbol_profiles/000/000720.json | selected 2024 window clean; CA candidates are 2004 or earlier |
| 002460 | atlas/symbol_profiles/002/002460.json | selected 2024 window clean; CA candidates are 2002 or earlier |
| 013360 | atlas/symbol_profiles/013/013360.json | selected 2024 window clean; CA candidates are 2017 or earlier |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R10L90_C30_HYUNDAICONST_2024_LARGE_BUILDER_PF_DISCOUNT_REPAIR_POSITIVE | 000720 | 2024-01-24 | yes | 180 | yes | yes | true |
| R10L90_C30_HSWHASUNG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2 | 002460 | 2024-02-01 | yes | 180 | yes | yes | true |
| R10L90_C30_ILSUNGCONST_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B | 013360 | 2024-07-23 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LARGE_BUILDER_PF_DISCOUNT_REPAIR | Positive Stage2 requires PF/cashflow/balance-sheet repair plus order quality/funding capacity. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | REGIONAL_CONSTRUCTION_FALSE_STAGE2 | Regional construction beta without PF/cashflow bridge can become weak-MFE false Stage2. |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | POLITICAL_CONSTRUCTION_EVENT_CAP_4B | Political/construction event premium should route to 4B when PF/cashflow bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R10L90_C30_HYUNDAICONST_2024_LARGE_BUILDER_PF_DISCOUNT_REPAIR_POSITIVE | 000720 | 현대건설 | positive | Large-builder PF discount-repair path had controlled MAE and clean rerating. |
| R10L90_C30_HSWHASUNG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2 | 002460 | HS화성 | counterexample | Regional construction/PF normalization watch had weak MFE and persistent drawdown. |
| R10L90_C30_ILSUNGCONST_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B | 013360 | 일성건설 | counterexample / 4B | Political/construction event premium capped at the July spike and then de-rated. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 3
calibration_usable_trigger_count = 3
```

## 9. Evidence Source Map

| case | evidence status | evidence_url_pending | source_proxy_only | usage |
|---|---|---|---|---|
| Hyundai Construction PF repair | historical public/report proxy | true | true | shadow-only positive |
| HS Hwasung regional false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| Ilsung Construction political cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 000720 | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | atlas/symbol_profiles/000/000720.json |
| 002460 | atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv | atlas/symbol_profiles/002/002460.json |
| 013360 | atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv | atlas/symbol_profiles/013/013360.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR | 000720 | Stage2-Actionable | 2024-01-24 | 31400 | positive | large-builder PF discount-repair bridge worked |
| R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION | 002460 | Stage2-Actionable | 2024-02-01 | 10840 | counterexample | regional construction false Stage2 |
| R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 013360 | Stage4B | 2024-07-23 | 1663 | counterexample/4B | political construction event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR | 31400 | 13.06 | -0.64 | 14.65 | -0.64 | 14.65 | -7.48 | 2024-05-09 | 36000 | -19.31 |
| R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION | 10840 | 3.60 | -8.12 | 3.60 | -13.38 | 3.60 | -19.74 | 2024-02-19 | 11230 | -22.53 |
| R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP | 1663 | 11.84 | -22.55 | 11.84 | -23.63 | 11.84 | -29.16 | 2024-07-23 | 1860 | -36.67 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C30 Stage2 needs PF/cashflow/balance repair bridge |
| local_4b_watch_guard | strengthen: regional construction beta and political/event premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE construction event rows cannot promote without durable PF bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is PF/cashflow bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 000720 | good_stage2 | PF/balance repair path had controlled drawdown and stable rerating. |
| 002460 | bad_stage2 | Regional construction beta had weak MFE and persistent drawdown. |
| 013360 | good_4B | Political construction premium capped at the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 002460 regional construction false Stage2 | 0.03 | 0.03 | regional construction watch was false Stage2 due missing PF/cashflow bridge |
| 013360 political construction event cap | 1.00 | 1.00 | good full-window 4B timing |
| 000720 PF repair bridge | n/a | n/a | positive Stage2, but later PF repair valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 002460 / 013360
```

No hard 4C candidate is proposed. R10 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L9 construction/PF cases, Stage2 requires verified PF, cashflow, debt maturity, balance-sheet repair, funding capacity, order quality, or margin/revision bridge. Construction beta, regional contractor, political theme, and event premium alone remain watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
rule = C30 should split real PF/cashflow repair positives from regional construction false Stage2 and political/construction event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 10.03 | -12.55 | 0.67 | mixed; C30 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 10.03 | -12.55 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L9 PF/cashflow repair required | 2 | 9.13 | -7.01 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C30 repair vs beta/event-cap split | 2 | 9.13 | -7.01 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing construction themes as positive | 1 | 14.65 | -0.64 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 000720 PF repair | 66 | Stage2-Watch | 74 | Stage2-Actionable | 14.65 | -0.64 | large_builder_PF_discount_repair_positive |
| 002460 regional false | 66 | Stage2-Actionable | 54 | Stage1/Watch | 3.60 | -13.38 | regional_construction_false_stage2 |
| 013360 political event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.84 | -23.63 | political_construction_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C30 large-builder PF discount-repair positive, regional-construction false Stage2, and political-construction event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: large_builder_PF_discount_repair_positive, regional_construction_false_stage2, political_construction_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
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
- C30 PF/cashflow repair vs regional construction / political-event cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,C30_requires_PF_cashflow_balance_repair_bridge,0,"C30 Stage2 should require verified PF/cashflow/balance-sheet repair, funding capacity, order quality, or margin/revision bridge, not construction beta or political/event label alone","Hyundai Construction positive worked; HS Hwasung and Ilsung Construction event/beta rows failed positive-stage promotion","R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR|R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION|R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,cap_regional_construction_beta_and_political_event_premiums_as_4B_watch,0,"Regional construction beta and political/construction event premiums can peak before durable PF/cashflow repair appears","HS Hwasung showed weak MFE; Ilsung Construction showed full-window event-cap behavior and high MAE","R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION|R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,configured,block_positive_stage_when_construction_event_has_high_MAE_without_PF_bridge,0,"High MAE after construction theme/event entries should block Stage2/Stage3 promotion unless PF/cashflow evidence survives the drawdown","Ilsung Construction MAE180=-29.16; HS Hwasung MAE180=-19.74 with weak MFE","R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION|R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R10L90_C30_HYUNDAICONST_2024_LARGE_BUILDER_PF_DISCOUNT_REPAIR_POSITIVE", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Large-builder PF discount repair / balance-sheet resilience bridge produced controlled entry MAE and a clean 90D rerating path; C30 works when PF/cashflow/balance-sheet risk is repaired by order quality and funding capacity.", "current_profile_verdict": "current_profile_kept_but_C30_positive_requires_PF_cashflow_balance_repair_not_construction_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2004 or earlier. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R10L90_C30_HSWHASUNG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "symbol": "002460", "company_name": "HS화성", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "case_type": "failed_rerating_regional_construction_beta", "positive_or_counterexample": "counterexample", "best_trigger": "R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional construction / PF-normalization watch produced weak MFE and persistent 180D drawdown; C30 Stage2 should not be awarded without PF/cashflow/balance-sheet repair evidence.", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_beta_counts_without_PF_cashflow_balance_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2002 or earlier. Source-proxy only."}
{"row_type": "case", "case_id": "R10L90_C30_ILSUNGCONST_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Political/construction theme premium capped around the July spike and then de-rated; bridge-missing construction event premium should route to 4B/watch, not Stage3-Green.", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2017 or earlier. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR", "case_id": "R10L90_C30_HYUNDAICONST_2024_LARGE_BUILDER_PF_DISCOUNT_REPAIR_POSITIVE", "symbol": "000720", "company_name": "현대건설", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "sector": "large_builder_PF_discount_repair", "primary_archetype": "large_builder_cashflow_balance_order_quality_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 31400.0, "evidence_available_at_that_date": "large-builder PF discount repair / cashflow-balance resilience / order-quality proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["PF_discount_repair_proxy", "cashflow_balance_bridge_proxy", "order_quality_backlog_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["controlled_MAE30", "controlled_MAE90", "positive_MFE90"], "stage4b_evidence_fields": ["valuation_watch_after_PF_discount_repair"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.06, "MFE_90D_pct": 14.65, "MFE_180D_pct": 14.65, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.64, "MAE_90D_pct": -0.64, "MAE_180D_pct": -7.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 36000.0, "drawdown_after_peak_pct": -19.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_PF_repair_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "PF_discount_repair"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_large_builder_PF_discount_repair_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L90_C30_000720_2024-01-24_31400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION", "case_id": "R10L90_C30_HSWHASUNG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "symbol": "002460", "company_name": "HS화성", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "sector": "regional_construction_PF_watch", "primary_archetype": "regional_construction_beta_without_PF_cashflow_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 10840.0, "evidence_available_at_that_date": "regional construction / PF normalization and balance-risk repair watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["regional_construction_beta", "PF_normalization_watch", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "PF_cashflow_bridge_missing", "post_watch_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002460/2024.csv", "profile_path": "atlas/symbol_profiles/002/002460.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.6, "MFE_90D_pct": 3.6, "MFE_180D_pct": 3.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.12, "MAE_90D_pct": -13.38, "MAE_180D_pct": -19.74, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 11230.0, "drawdown_after_peak_pct": -22.53, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.03, "four_b_full_window_peak_proximity": 0.03, "four_b_timing_verdict": "regional_construction_watch_was_false_stage2_due_missing_PF_cashflow_bridge", "four_b_evidence_type": ["price_only", "positioning_overheat", "PF_cashflow_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_regional_construction_without_PF_cashflow_bridge", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_beta_counts_without_PF_cashflow_balance_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L90_C30_002460_2024-02-01_10840", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "case_id": "R10L90_C30_ILSUNGCONST_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "sector": "political_construction_event_premium", "primary_archetype": "political_construction_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-23", "entry_date": "2024-07-23", "entry_price": 1663.0, "evidence_available_at_that_date": "political/construction event premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["political_construction_theme", "event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "post_peak_drawdown", "PF_cashflow_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv", "profile_path": "atlas/symbol_profiles/013/013360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.84, "MFE_90D_pct": 11.84, "MFE_180D_pct": 11.84, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -22.55, "MAE_90D_pct": -23.63, "MAE_180D_pct": -29.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-23", "peak_price": 1860.0, "drawdown_after_peak_pct": -36.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_political_construction_event_cap", "four_b_evidence_type": ["event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R10L90_C30_013360_2024-07-23_1663", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L90_C30_HYUNDAICONST_2024_LARGE_BUILDER_PF_DISCOUNT_REPAIR_POSITIVE", "trigger_id": "R10L90_C30_HYUNDAICONST_2024_STAGE2_ACTIONABLE_PF_DISCOUNT_REPAIR", "symbol": "000720", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 30, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 30, "policy_or_regulatory_score": 5, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "large_builder_PF_discount_repair_positive", "MFE_90D_pct": 14.65, "MAE_90D_pct": -0.64, "score_return_alignment_label": "large_builder_PF_discount_repair_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L90_C30_HSWHASUNG_2024_REGIONAL_CONSTRUCTION_FALSE_STAGE2", "trigger_id": "R10L90_C30_HSWHASUNG_2024_STAGE2_FALSE_POSITIVE_REGIONAL_CONSTRUCTION", "symbol": "002460", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "regional_construction_false_stage2", "MFE_90D_pct": 3.6, "MAE_90D_pct": -13.38, "score_return_alignment_label": "regional_construction_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_regional_construction_beta_counts_without_PF_cashflow_balance_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L90_C30_ILSUNGCONST_2024_POLITICAL_CONSTRUCTION_EVENT_CAP_4B", "trigger_id": "R10L90_C30_ILSUNGCONST_2024_STAGE4B_POLITICAL_CONSTRUCTION_EVENT_CAP", "symbol": "013360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 5, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 20}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "political_construction_event_cap_4B_guard", "MFE_90D_pct": 11.84, "MAE_90D_pct": -23.63, "score_return_alignment_label": "political_construction_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_political_construction_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R10", "loop": "90", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_BUILDER_PF_DISCOUNT_REPAIR_VS_REGIONAL_CONSTRUCTION_AND_POLITICAL_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["large_builder_PF_discount_repair_positive", "regional_construction_false_stage2", "political_construction_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L9_CONSTRUCTION_REALESTATE_HOUSING","canonical_archetype_id":"C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R10
completed_loop = 90
next_round = R11
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
