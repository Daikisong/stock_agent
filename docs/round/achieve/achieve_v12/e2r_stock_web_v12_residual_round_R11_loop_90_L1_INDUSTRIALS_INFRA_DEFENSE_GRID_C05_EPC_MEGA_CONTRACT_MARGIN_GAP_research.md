# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id = OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
```

R11 permits the L10 policy/event route or the L1 policy-defense/infra route. This run uses the L1 infrastructure-policy route and fills the low-coverage C05 EPC mega-contract margin-gap archetype.

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
scheduled_round = R11
scheduled_loop = 90
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 90
```

Previous R11 loop 89 used C03 defense export/framework. This loop avoids repeating C03/C31/C32 and uses C05 because it is still under-covered.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C05_EPC_MEGA_CONTRACT_MARGIN_GAP = 10 rows / 9 symbols / good-bad Stage2 3-4 / 4B-4C 0-0
top covered symbols include 053690(2), 002150(1), 011560(1), 023350(1), 023960(1), 054930(1)
previous R11 loop-88 C31 symbols avoided: 036460, 053290, 057030
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R10 loop-90 C30 symbols avoided: 000720, 002460, 013360
```

Selected rows avoid those repeated combinations and top repeated C05 symbols:

```text
047040 / Stage2-Actionable / 2024-07-09
028050 / Stage2-Actionable / 2024-02-28
052690 / Stage4B / 2024-03-11
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
| 047040 | atlas/symbol_profiles/047/047040.json | selected 2024 window clean; CA candidates are 2011 or earlier |
| 028050 | atlas/symbol_profiles/028/028050.json | selected 2024 window clean; CA candidates are 2016 or earlier |
| 052690 | atlas/symbol_profiles/052/052690.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE | 047040 | 2024-07-09 | yes | 180 | yes | yes | true |
| R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | 2024-02-28 | yes | 180 | yes | yes | true |
| R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B | 052690 | 2024-03-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE | Positive Stage2 requires project framework plus contract margin, funding/customer quality, and execution bridge. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | PLANT_EPC_MARGIN_GAP_FALSE_STAGE2 | Plant/EPC order label without margin and revision bridge can become false Stage2. |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | NUCLEAR_ENGINEERING_EPC_POLICY_EVENT_CAP_4B | Engineering/EPC policy premium should route to 4B when project-margin bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE | 047040 | 대우건설 | positive | Overseas EPC/project-policy bridge produced clear short-window rerating. |
| R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2 | 028050 | 삼성E&A | counterexample | EPC/project label lacked durable margin/revision bridge and drew down. |
| R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B | 052690 | 한전기술 | counterexample / 4B | Nuclear engineering policy premium capped around the March spike. |

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
| Daewoo E&C overseas EPC bridge | historical public/news proxy | true | true | shadow-only positive |
| Samsung E&A EPC margin-gap false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| KEPCO E&C nuclear engineering cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 047040 | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | atlas/symbol_profiles/047/047040.json |
| 028050 | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | atlas/symbol_profiles/028/028050.json |
| 052690 | atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv | atlas/symbol_profiles/052/052690.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE | 047040 | Stage2-Actionable | 2024-07-09 | 3890 | positive | overseas EPC contract/margin bridge worked |
| R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP | 028050 | Stage2-Actionable | 2024-02-28 | 26000 | counterexample | plant EPC margin-gap false Stage2 |
| R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP | 052690 | Stage4B | 2024-03-11 | 71800 | counterexample/4B | nuclear engineering EPC policy event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE | 3890 | 27.63 | -8.87 | 27.63 | -8.87 | 27.63 | -8.87 | 2024-07-18 | 4965 | -28.60 |
| R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP | 26000 | 8.27 | -6.54 | 8.27 | -16.92 | 8.27 | -16.92 | 2024-03-15 | 28150 | -23.27 |
| R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP | 71800 | 6.96 | -10.72 | 6.96 | -11.00 | 6.96 | -13.02 | 2024-03-11 | 76800 | -16.80 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C05 Stage2 needs contract/margin/execution/revision bridge |
| local_4b_watch_guard | strengthen: EPC policy and engineering theme premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: EPC project label cannot promote if margin/execution MAE appears |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is EPC contract-margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 047040 | good_stage2 | EPC/policy project bridge produced strong short-window MFE. |
| 028050 | bad_stage2 | EPC order label was not enough without margin/revision bridge. |
| 052690 | good_4B | Nuclear engineering/EPC policy premium capped around event peak. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 028050 plant EPC margin-gap false Stage2 | 0.83 | 0.83 | EPC order watch was false Stage2 due margin/execution gap |
| 052690 nuclear engineering policy cap | 1.00 | 1.00 | good full-window 4B timing |
| 047040 overseas EPC bridge | n/a | n/a | positive Stage2, but later EPC policy valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 028050 / 052690
```

No hard 4C candidate is proposed. R11 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 EPC/project-policy cases, Stage2 requires verified project award or framework plus contract margin, cost pass-through, funding/customer quality, execution risk control, and revision bridge. EPC, nuclear engineering, overseas project, or policy-event label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
rule = C05 should split contract-margin positives from EPC-margin-gap false Stage2 and policy/engineering event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 14.29 | -12.26 | 0.67 | mixed; C05 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 14.29 | -12.26 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 EPC margin bridge required | 2 | 17.95 | -12.90 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C05 bridge vs event-cap split | 2 | 17.95 | -12.90 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing EPC themes as positive | 1 | 27.63 | -8.87 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 047040 overseas EPC bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 27.63 | -8.87 | overseas_EPC_contract_margin_bridge_positive |
| 028050 plant EPC margin-gap | 66 | Stage2-Actionable | 53 | Stage1/Watch | 8.27 | -16.92 | plant_EPC_margin_gap_false_stage2 |
| 052690 nuclear engineering cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 6.96 | -11.00 | nuclear_engineering_EPC_policy_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C05 overseas EPC contract/margin positive, plant-EPC margin-gap false Stage2, and nuclear-engineering EPC policy event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: overseas_EPC_contract_margin_bridge_positive, plant_EPC_margin_gap_false_stage2, nuclear_engineering_EPC_policy_event_cap_4B
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
- C05 EPC mega-contract margin gap bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,C05_requires_contract_margin_execution_revision_bridge,0,"C05 Stage2 should require project award or framework plus contract margin, cost pass-through, funding/customer quality, execution risk, and revision bridge, not EPC/project label alone","Daewoo E&C positive worked; Samsung E&A and KEPCO E&C event rows failed positive-stage promotion","R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE|R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP|R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,cap_EPC_policy_and_engineering_theme_premiums_as_4B_watch,0,"EPC/nuclear-engineering policy premiums can peak before durable contract-margin and execution bridge appears","Samsung E&A had limited MFE and margin-gap drawdown; KEPCO E&C capped at the policy spike","R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP|R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,configured,block_positive_stage_when_EPC_project_label_has_margin_gap_or_execution_MAE,0,"High or persistent MAE after EPC/project label should block Stage2 promotion unless contract margin and execution evidence survives the drawdown","Samsung E&A MAE90=-16.92 and weak MFE; KEPCO E&C policy spike capped quickly","R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP|R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP",2,2,2,low,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE", "symbol": "047040", "company_name": "대우건설", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Overseas EPC / infrastructure-policy contract bridge produced a clear 30D/90D MFE before the event premium cooled. C05 works when a large project has margin, funding, customer, and execution bridge, not merely EPC headline value.", "current_profile_verdict": "current_profile_kept_but_C05_positive_requires_EPC_contract_margin_execution_bridge_not_project_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2011 or earlier. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "028050", "company_name": "삼성E&A", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "case_type": "failed_rerating_margin_gap", "positive_or_counterexample": "counterexample", "best_trigger": "R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Plant EPC / mega-project label had only modest MFE and then a material MAE path. C05 Stage2 should not be awarded without margin, execution-risk, cost-pass-through, and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EPC_order_label_counts_without_margin_execution_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; corporate-action candidates are 2016 or earlier. Source-proxy only."}
{"row_type": "case", "case_id": "R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear engineering / EPC policy premium capped around the March spike and then failed to sustain. Engineering-policy premium should route to 4B unless project award, margin, execution and revenue bridge are visible.", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_engineering_EPC_policy_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE", "case_id": "R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE", "symbol": "047040", "company_name": "대우건설", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "sector": "overseas_EPC_infra_policy_contract", "primary_archetype": "overseas_EPC_contract_margin_execution_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-09", "entry_date": "2024-07-09", "entry_price": 3890.0, "evidence_available_at_that_date": "overseas EPC / infrastructure policy contract, project pipeline, funding and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["overseas_EPC_project_pipeline", "policy_project_framework", "contract_margin_bridge_proxy", "execution_risk_watch", "relative_strength_reversal"], "stage3_evidence_fields": ["strong_MFE30", "controlled_MAE90", "project_policy_rerating"], "stage4b_evidence_fields": ["valuation_watch_after_EPC_policy_event_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.63, "MFE_90D_pct": 27.63, "MFE_180D_pct": 27.63, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.87, "MAE_90D_pct": -8.87, "MAE_180D_pct": -8.87, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 4965.0, "drawdown_after_peak_pct": -28.6, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_EPC_policy_valuation_watch_needed", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "EPC_contract_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_overseas_EPC_policy_contract_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L90_C05_047040_2024-07-09_3890", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP", "case_id": "R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2", "symbol": "028050", "company_name": "삼성E&A", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "sector": "plant_EPC_mega_contract_margin_gap", "primary_archetype": "EPC_project_label_without_margin_execution_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 26000.0, "evidence_available_at_that_date": "plant EPC / mega-project order and margin bridge watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["EPC_order_watch", "plant_project_pipeline", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "margin_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 8.27, "MFE_90D_pct": 8.27, "MFE_180D_pct": 8.27, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.54, "MAE_90D_pct": -16.92, "MAE_180D_pct": -16.92, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 28150.0, "drawdown_after_peak_pct": -23.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.83, "four_b_full_window_peak_proximity": 0.83, "four_b_timing_verdict": "plant_EPC_order_watch_was_false_stage2_due_margin_execution_gap", "four_b_evidence_type": ["price_only", "positioning_overheat", "margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_EPC_order_label_without_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EPC_order_label_counts_without_margin_execution_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L90_C05_028050_2024-02-28_26000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP", "case_id": "R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B", "symbol": "052690", "company_name": "한전기술", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "sector": "nuclear_engineering_EPC_policy_premium", "primary_archetype": "nuclear_engineering_EPC_policy_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-11", "entry_date": "2024-03-11", "entry_price": 71800.0, "evidence_available_at_that_date": "nuclear engineering / EPC policy premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_engineering_policy_theme", "EPC_design_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv", "profile_path": "atlas/symbol_profiles/052/052690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.96, "MFE_90D_pct": 6.96, "MFE_180D_pct": 6.96, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -10.72, "MAE_90D_pct": -11.0, "MAE_180D_pct": -13.02, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-11", "peak_price": 76800.0, "drawdown_after_peak_pct": -16.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_nuclear_engineering_EPC_policy_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_engineering_EPC_policy_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L90_C05_052690_2024-03-11_71800", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L90_C05_DAEWOOE_C_2024_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R11L90_C05_DAEWOOE_C_2024_STAGE2_ACTIONABLE_OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE", "symbol": "047040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 55, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 50, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "overseas_EPC_contract_margin_bridge_positive", "MFE_90D_pct": 27.63, "MAE_90D_pct": -8.87, "score_return_alignment_label": "overseas_EPC_contract_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L90_C05_SAMSUNGEA_2024_PLANT_EPC_MARGIN_GAP_FALSE_STAGE2", "trigger_id": "R11L90_C05_SAMSUNGEA_2024_STAGE2_FALSE_POSITIVE_PLANT_EPC_MARGIN_GAP", "symbol": "028050", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 35, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "plant_EPC_margin_gap_false_stage2", "MFE_90D_pct": 8.27, "MAE_90D_pct": -16.92, "score_return_alignment_label": "plant_EPC_margin_gap_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EPC_order_label_counts_without_margin_execution_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L90_C05_KEPCOE_C_2024_NUCLEAR_ENGINEERING_EPC_EVENT_CAP_4B", "trigger_id": "R11L90_C05_KEPCOE_C_2024_STAGE4B_NUCLEAR_ENGINEERING_EPC_POLICY_CAP", "symbol": "052690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 25, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 35, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "nuclear_engineering_EPC_policy_event_cap_4B_guard", "MFE_90D_pct": 6.96, "MAE_90D_pct": -11.0, "score_return_alignment_label": "nuclear_engineering_EPC_policy_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_engineering_EPC_policy_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "OVERSEAS_EPC_POLICY_CONTRACT_MARGIN_BRIDGE_VS_PLANT_EPC_MARGIN_GAP_AND_NUCLEAR_ENGINEERING_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["overseas_EPC_contract_margin_bridge_positive", "plant_EPC_margin_gap_false_stage2", "nuclear_engineering_EPC_policy_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C05_EPC_MEGA_CONTRACT_MARGIN_GAP","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R11
completed_loop = 90
next_round = R12
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
