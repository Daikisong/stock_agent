# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 101
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | EPC_project_margin_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_101_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. Priority 0 has been locally supplemented, and Priority 1 already added C03, C16 and C04. C05 is the next unsupplemented Priority 1 gap below the 50-row practical calibration zone. Since R1 loop98/99/100 were used locally for C01/C03/C04, this file uses R1 loop101 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
EPC_project_margin_bridge_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 101
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C05 is an EPC/project backlog-to-margin archetype. A mega contract headline is the crane on the skyline; the usable signal is whether backlog, execution schedule, cost control, working capital, contract margin and revision actually pour the concrete.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 33 rows / Priority 1
top covered C05 symbols avoided: 028050, 000720, 100840, 006360, 028100, 045100
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04
```

Selected rows avoid hard duplicates and add new C05 trigger families:

```text
294870 / Stage2-Actionable / 2024-01-23
047040 / Stage2-Actionable / 2024-01-10
375500 / Stage4B / 2024-01-10
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
| 294870 | atlas/symbol_profiles/294/294870.json | selected 2024 window clean after old 2020 CA candidate |
| 047040 | atlas/symbol_profiles/047/047040.json | selected 2024 window clean after old 2001/2003/2011 CA candidates |
| 375500 | atlas/symbol_profiles/375/375500.json | selected 2024 window clean after old 2022 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE | 294870 | 2024-01-23 | yes | 180 | yes | yes | true |
| R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2 | 047040 | 2024-01-10 | yes | 180 | yes | yes | true |
| R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B | 375500 | 2024-01-10 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE | Positive Stage2 requires executable backlog, cost control, working-capital recovery, margin and revision bridge. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC_MARGIN_GAP_FALSE_STAGE2 | EPC/project recovery watch without margin and working-capital bridge can become false Stage2. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC_EVENT_CAP_4B | EPC/project-margin event premium should route to 4B when contract margin and cost-pass-through bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE | 294870 | HDC현대산업개발 | positive | Project backlog/margin bridge produced strong MFE with limited early MAE. |
| R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2 | 047040 | 대우건설 | counterexample | EPC margin recovery watch had tiny 30D/90D MFE and meaningful MAE without contract-margin bridge. |
| R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B | 375500 | DL이앤씨 | counterexample / 4B | EPC/project premium capped after the February high and then drew down. |

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
| HDC Hyundai Development project backlog/margin bridge | historical public/report proxy | true | true | shadow-only positive |
| Daewoo E&C EPC margin gap false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| DL E&C EPC project-margin event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 294870 | atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv | atlas/symbol_profiles/294/294870.json |
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json |
| 375500 | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | atlas/symbol_profiles/375/375500.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE | 294870 | Stage2-Actionable | 2024-01-23 | 15570 | positive | project backlog/margin bridge worked |
| R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH | 047040 | Stage2-Actionable | 2024-01-10 | 4260 | counterexample | EPC margin gap false Stage2 |
| R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP | 375500 | Stage4B | 2024-01-10 | 40750 | counterexample/4B | EPC project event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE | 15570 | 31.98 | -3.79 | 31.98 | -3.79 | 40.98 | -3.79 | 2024-07-17 | 21950 | -23.46 |
| R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH | 4260 | 1.88 | -9.15 | 1.88 | -15.49 | 16.55 | -15.49 | 2024-07-18 | 4965 | -17.02 |
| R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP | 40750 | 7.48 | -6.50 | 7.48 | -21.60 | 7.48 | -23.19 | 2024-02-01 | 43800 | -28.54 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C05 Stage2 needs executable project backlog / cost control / working capital / contract margin / revision bridge |
| EPC_project_margin_bridge_guardrail | strengthen: EPC or project label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing EPC/project premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C05 rows cannot promote without durable margin/working-capital bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether project/EPC narrative becomes executable backlog, cost and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 294870 | good_stage2_with_later_watch | Backlog/margin bridge produced strong MFE and limited early MAE, but later balance-sheet/valuation watch remains necessary. |
| 047040 | bad_stage2 | EPC margin recovery watch lacked contract-margin and working-capital bridge, producing tiny MFE. |
| 375500 | good_4B | EPC event premium peaked early and then drew down without durable margin bridge. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 047040 EPC false Stage2 | 0.98 | 0.86 | false Stage2 due missing contract-margin / cost-control / working-capital bridge |
| 375500 EPC event cap | 0.93 | 0.93 | good 4B timing after EPC/project-margin event premium |
| 294870 project margin bridge | n/a | n/a | positive Stage2, but later project-margin valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = PF_or_cost_gap_watch_only for 047040
four_c_protection_label = cost_gap_watch_only for 375500
```

No hard 4C candidate is introduced in this C05 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 EPC mega-contract margin-gap cases, Stage2 requires verified executable backlog, project delivery schedule, cost control, working-capital recovery, contract margin and revision bridge. EPC, mega contract, project recovery, housing/redevelopment or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rule = C05 should split true executable backlog/contract-margin positives from EPC margin-gap false Stage2 and project-premium event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 13.78 | -13.63 | 0.67 | mixed; C05 executable-margin bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 13.78 | -13.63 | 0.67 | weaker C05 bridge split |
| P1 sector_specific_candidate_profile | L1 executable backlog/margin bridge required | 2 | 16.93 | -9.64 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C05 bridge vs event-cap split | 2 | 16.93 | -9.64 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing EPC/project themes as positive | 1 | 31.98 | -3.79 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 294870 project backlog bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 31.98 | -3.79 | EPC_project_margin_positive |
| 047040 EPC margin false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 1.88 | -15.49 | EPC_margin_gap_false_stage2 |
| 375500 EPC event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 7.48 | -21.60 | EPC_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C05 is the next unsupplemented Priority 1 archetype after C03/C16/C04 and still remains below the practical 50-row calibration zone. This run adds HDC Hyundai Development, Daewoo E&C, and DL E&C while avoiding top-covered C05 symbols 028050, 000720, 100840, 006360, 028100 and 045100."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, EPC_project_margin_bridge_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: EPC_project_margin_positive, EPC_margin_gap_false_stage2, EPC_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, EPC_project_margin_bridge_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C05 EPC mega-contract margin-gap bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,C05_requires_project_backlog_execution_cost_working_capital_margin_revision_bridge,0,"C05 Stage2 should require executable project backlog, delivery/execution schedule, cost control, working-capital recovery, contract margin and revision bridge, not EPC/project label alone","HDC Hyundai Development positive worked; Daewoo E&C and DL E&C event/watch rows failed positive-stage promotion","R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE|R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH|R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,cap_bridge_missing_EPC_margin_gap_and_project_event_premiums_as_4B_watch,0,"EPC/project margin premiums can peak before contract margin, cost pass-through and working-capital bridge is proven","Daewoo E&C had tiny 90D MFE after January margin watch; DL E&C showed 4B event-cap behavior after February project-margin premium","R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH|R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,block_positive_stage_when_EPC_project_theme_has_high_or_persistent_MAE_without_contract_margin_bridge,0,"High or persistent MAE after bridge-missing C05 entries should block Stage2/Stage3 promotion unless executable backlog, working capital and contract margin evidence survives","Daewoo E&C MAE90=-15.49 and DL E&C MAE90=-21.60","R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH|R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "case_type": "structural_success_with_later_project_margin_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Large project / redevelopment backlog and margin bridge produced strong 30D/90D/180D MFE from the January project-margin base, with limited initial MAE. C05 works when backlog is tied to executable project schedule, cost control, working-capital discipline, margin and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C05_positive_requires_project_backlog_execution_cost_working_capital_margin_revision_bridge_not_project_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "case_type": "failed_rerating_EPC_margin_gap_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EPC / overseas project-margin recovery watch at the January high had tiny 30D/90D MFE and meaningful MAE. C05 Stage2 should not be awarded without fresh contract margin, execution cost control, working-capital recovery and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EPC_margin_recovery_watch_counts_without_contract_margin_cost_control_working_capital_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2003/2011 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B", "symbol": "375500", "company_name": "DL이앤씨", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EPC/project-margin event premium capped after the February spike and then drew down sharply. C05 should route bridge-missing EPC/project premiums to 4B unless contract margin, execution schedule, cost-pass-through, working capital, order backlog and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_EPC_project_margin_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2022 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE", "case_id": "R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE", "symbol": "294870", "company_name": "HDC현대산업개발", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "sector": "large_project_redevelopment_backlog_margin_bridge", "primary_archetype": "project_backlog_execution_cost_working_capital_margin_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | EPC_project_margin_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-23", "entry_date": "2024-01-23", "entry_price": 15570.0, "evidence_available_at_that_date": "large redevelopment/project backlog and margin recovery proxy after January project-margin base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["project_backlog_proxy", "execution_schedule_proxy", "cost_control_proxy", "working_capital_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "limited_initial_MAE"], "stage4b_evidence_fields": ["later_project_margin_valuation_watch", "PF_balance_sheet_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/294/294870/2024.csv", "profile_path": "atlas/symbol_profiles/294/294870.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.98, "MFE_90D_pct": 31.98, "MFE_180D_pct": 40.98, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.79, "MAE_90D_pct": -3.79, "MAE_180D_pct": -3.79, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 21950.0, "drawdown_after_peak_pct": -23.46, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_project_margin_valuation_and_balance_sheet_4B_watch_needed", "four_b_evidence_type": ["project_backlog_margin_bridge", "working_capital", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_large_project_backlog_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_CA", "same_entry_group_id": "R1L101_C05_294870_2024-01-23_15570", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH", "case_id": "R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "047040", "company_name": "대우건설", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "sector": "EPC_project_margin_gap_recovery_watch", "primary_archetype": "EPC_margin_watch_without_contract_margin_cost_control_working_capital_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | EPC_project_margin_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 4260.0, "evidence_available_at_that_date": "EPC / overseas project-margin recovery watch without confirmed fresh margin bridge, execution cost control, working capital or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EPC_margin_recovery_watch", "large_project_theme", "relative_strength_high"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["tiny_MFE90", "meaningful_MAE90", "contract_margin_bridge_missing"], "stage4c_evidence_fields": ["PF_or_cost_gap_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.88, "MFE_90D_pct": 1.88, "MFE_180D_pct": 16.55, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.15, "MAE_90D_pct": -15.49, "MAE_180D_pct": -15.49, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 4965.0, "drawdown_after_peak_pct": -17.02, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.86, "four_b_timing_verdict": "EPC_margin_gap_watch_was_false_stage2_due_missing_contract_margin_cost_control_working_capital_revision_bridge", "four_b_evidence_type": ["EPC_margin_gap_premium", "bridge_missing", "tiny_MFE90"], "four_c_protection_label": "PF_or_cost_gap_watch_only", "trigger_outcome_label": "bad_stage2_EPC_margin_gap_watch_without_contract_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EPC_margin_recovery_watch_counts_without_contract_margin_cost_control_working_capital_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2003_2011_CA", "same_entry_group_id": "R1L101_C05_047040_2024-01-10_4260", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP", "case_id": "R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B", "symbol": "375500", "company_name": "DL이앤씨", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "sector": "EPC_project_margin_event_premium", "primary_archetype": "EPC_project_margin_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | EPC_project_margin_bridge_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-10", "entry_date": "2024-01-10", "entry_price": 40750.0, "evidence_available_at_that_date": "EPC/project-margin event premium without confirmed contract-margin, execution-cost, working-capital, cost-pass-through or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EPC_event_premium", "project_margin_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "contract_margin_bridge_recheck"], "stage4c_evidence_fields": ["cost_gap_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.48, "MFE_90D_pct": 7.48, "MFE_180D_pct": 7.48, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.5, "MAE_90D_pct": -21.6, "MAE_180D_pct": -23.19, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-01", "peak_price": 43800.0, "drawdown_after_peak_pct": -28.54, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing_EPC_project_margin_event_cap_due_missing_contract_margin_working_capital_bridge", "four_b_evidence_type": ["EPC_project_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "cost_gap_watch_only", "trigger_outcome_label": "event_cap_4B_success_EPC_project_margin_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_EPC_project_margin_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA", "same_entry_group_id": "R1L101_C05_375500_2024-01-10_40750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L101_C05_HDCDEV_2024_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R1L101_C05_HDCDEV_2024_STAGE2_ACTIONABLE_LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE", "symbol": "294870", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 25, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "large_project_backlog_margin_positive", "MFE_90D_pct": 31.98, "MAE_90D_pct": -3.79, "score_return_alignment_label": "EPC_project_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L101_C05_DAEWOOE&C_2024_EPC_MARGIN_GAP_FALSE_STAGE2", "trigger_id": "R1L101_C05_DAEWOOE&C_2024_STAGE2_FALSE_POSITIVE_EPC_MARGIN_GAP_WATCH", "symbol": "047040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 55, "customer_quality_score": 30, "policy_or_regulatory_score": 15, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EPC_margin_gap_false_stage2", "MFE_90D_pct": 1.88, "MAE_90D_pct": -15.49, "score_return_alignment_label": "EPC_margin_gap_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EPC_margin_recovery_watch_counts_without_contract_margin_cost_control_working_capital_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R1L101_C05_DLENC_2024_EPC_EVENT_PREMIUM_MARGIN_GAP_4B", "trigger_id": "R1L101_C05_DLENC_2024_STAGE4B_EPC_EVENT_PREMIUM_MARGIN_GAP_CAP", "symbol": "375500", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 5, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EPC_project_margin_event_cap_4B_guard", "MFE_90D_pct": 7.48, "MAE_90D_pct": -21.6, "score_return_alignment_label": "EPC_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_EPC_project_margin_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "101", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "LARGE_PROJECT_BACKLOG_MARGIN_BRIDGE_VS_EPC_MARGIN_GAP_FALSE_STAGE2_AND_EPC_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "EPC_project_margin_bridge_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["EPC_project_margin_positive", "EPC_margin_gap_false_stage2", "EPC_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C05 rows need explicit executable project backlog, project delivery schedule, cost control, working-capital recovery, contract margin and revision bridge before positive promotion.
- In C05, bridge-missing EPC/project event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C05 EPC mega-contract margin-gap rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R1
completed_loop = 101
completed_canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
