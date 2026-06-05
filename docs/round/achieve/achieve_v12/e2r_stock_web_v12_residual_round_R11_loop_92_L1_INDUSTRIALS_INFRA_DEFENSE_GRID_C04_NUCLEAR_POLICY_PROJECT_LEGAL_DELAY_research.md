# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_92_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

This file is the corrected final output for this execution. The scheduler state after R10 loop 92 is R11 / loop 92. R11 permits the L10 policy/event route or the L1 policy-defense/infra route; this run uses the L1 nuclear-policy / infrastructure route and fills under-covered C04.

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
scheduled_loop = 92
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 92
```

R11 loop 91 used C03 defense export-framework. This loop avoids that row family and uses C04 nuclear policy / project / legal-delay risk.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY = 12 rows / 7 symbols / good-bad Stage2 5-3 / 4B-4C 1-0
top covered symbols include 011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
previous R11 loop-88 C31 symbols avoided: 036460, 053290, 057030
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
previous R11 loop-90 C05 symbols avoided: 047040, 028050, 052690
previous R11 loop-91 C03 symbols avoided: 012450, 214430, 013810
previous R10 loop-92 C30 symbols avoided: 014790, 002780, 002410
```

Selected rows avoid hard duplicate keys:

```text
051600 / Stage2-Actionable / 2024-01-24
046120 / Stage2-Actionable / 2024-05-27
006910 / Stage4B / 2024-05-27
```

`046120` and `006910` are soft expansions because they appear lightly in C04 coverage, but their 2024 entry dates and failure families are new. They receive reduced evidence weight.

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
| 051600 | atlas/symbol_profiles/051/051600.json | no corporate-action candidate |
| 046120 | atlas/symbol_profiles/046/046120.json | selected 2024 window clean after old 2017 CA candidate |
| 006910 | atlas/symbol_profiles/006/006910.json | selected 2024 window clean after old 1996~2016 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L92_C04_KEPCOKPS_2024_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_POSITIVE | 051600 | 2024-01-24 | yes | 180 | yes | yes | true |
| R11L92_C04_ORBITECH_2024_NUCLEAR_INSPECTION_THEME_FALSE_STAGE2 | 046120 | 2024-05-27 | yes | 180 | yes | yes | true |
| R11L92_C04_BOSUNGPOWER_2024_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP_4B | 006910 | 2024-05-27 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE | Positive Stage2 requires project/service backlog, legal/regulatory clarity, execution capacity, margin and revision bridge. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_INSPECTION_FALSE_STAGE2 | Nuclear inspection/theme label without project/order and margin bridge can become high-MAE false Stage2. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | POWER_EQUIPMENT_EVENT_CAP_4B | Nuclear power-equipment event premium should route to 4B when project and legal-clarity bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L92_C04_KEPCOKPS_2024_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_POSITIVE | 051600 | 한전KPS | positive | Nuclear O&M / service project bridge produced positive MFE and controlled MAE. |
| R11L92_C04_ORBITECH_2024_NUCLEAR_INSPECTION_THEME_FALSE_STAGE2 | 046120 | 오르비텍 | counterexample | Nuclear inspection theme spike had weak MFE and severe 90D/180D MAE. |
| R11L92_C04_BOSUNGPOWER_2024_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP_4B | 006910 | 보성파워텍 | counterexample / 4B | Nuclear power-equipment premium capped near the May spike and then de-rated sharply. |

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
| KEPCO KPS nuclear O&M policy-project bridge | historical public/report proxy | true | true | shadow-only positive |
| Orbitech nuclear inspection false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Bosung Powertec nuclear power-equipment cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 051600 | atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv | atlas/symbol_profiles/051/051600.json |
| 046120 | atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv | atlas/symbol_profiles/046/046120.json |
| 006910 | atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv | atlas/symbol_profiles/006/006910.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE | 051600 | Stage2-Actionable | 2024-01-24 | 34050 | positive | nuclear O&M / policy-project bridge worked |
| R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME | 046120 | Stage2-Actionable | 2024-05-27 | 3400 | counterexample | nuclear inspection theme false Stage2 |
| R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP | 006910 | Stage4B | 2024-05-27 | 4225 | counterexample/4B | nuclear power-equipment event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE | 34050 | 16.01 | -0.73 | 16.01 | -3.23 | 39.35 | -3.23 | 2024-07-18 | 47450 | -24.45 |
| R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME | 3400 | 3.53 | -25.29 | 3.53 | -40.00 | 3.53 | -40.00 | 2024-05-29 | 3520 | -42.05 |
| R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP | 4225 | 10.18 | -18.34 | 10.18 | -39.41 | 10.18 | -39.41 | 2024-05-29 | 4655 | -45.01 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C04 Stage2 needs project/service backlog, execution, legal/regulatory clarity, margin and revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing nuclear policy/equipment premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE nuclear-theme rows cannot promote without durable project bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is policy/project bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 051600 | good_stage2_with_later_watch | Nuclear O&M / policy-project service bridge produced positive MFE and shallow drawdown. |
| 046120 | bad_stage2 | Nuclear inspection theme lacked project/backlog/margin bridge and suffered severe MAE. |
| 006910 | good_4B | Nuclear power-equipment event premium capped near May spike and de-rated. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 046120 nuclear inspection false Stage2 | 0.97 | 0.97 | false Stage2 due missing project/service margin bridge |
| 006910 nuclear power equipment cap | 0.91 | 0.91 | good full-window 4B timing after high-MAE event cap |
| 051600 nuclear O&M bridge | n/a | n/a | positive Stage2, but later nuclear-policy valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 046120 / 006910
```

No hard 4C candidate is proposed. R11 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 nuclear-policy / infrastructure cases, Stage2 requires verified project/service backlog, O&M/order visibility, legal/regulatory clarity, execution capacity, margin, or revision bridge. Nuclear policy, inspection, power equipment, SMR, or project-rumor label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rule = C04 should split true project/service backlog positives from nuclear-inspection false Stage2 and power-equipment event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 9.91 | -27.55 | 0.67 | mixed; C04 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 9.91 | -27.55 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 nuclear project/service bridge required | 2 | 9.77 | -21.62 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C04 bridge vs event-cap split | 2 | 9.77 | -21.62 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing nuclear themes as positive | 1 | 16.01 | -3.23 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 051600 nuclear O&M bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 16.01 | -3.23 | nuclear_O_and_M_policy_project_bridge_positive |
| 046120 nuclear inspection false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 3.53 | -40.00 | nuclear_inspection_theme_false_stage2 |
| 006910 nuclear equipment cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 10.18 | -39.41 | nuclear_power_equipment_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C04 nuclear O&M/policy-project bridge positive, nuclear-inspection false Stage2, and nuclear power-equipment event-cap 4B split using one new symbol plus two reduced-weight lightly covered symbols."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 1
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: nuclear_O_and_M_policy_project_bridge_positive, nuclear_inspection_theme_false_stage2, nuclear_power_equipment_event_cap_4B
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
- C04 nuclear policy/project legal-delay bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,C04_requires_project_service_backlog_execution_margin_legal_clarity_bridge,0,"C04 Stage2 should require project/service backlog, O&M or equipment order visibility, execution capacity, legal/regulatory clarity, margin, or revision bridge, not nuclear-policy/theme label alone","KEPCO KPS positive worked; Orbitech and Bosung Powertec event/theme rows failed positive-stage promotion","R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE|R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME|R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,cap_bridge_missing_nuclear_policy_and_equipment_event_premiums_as_4B_watch,0,"Nuclear policy/equipment event premiums can peak before project/service and legal-clarity evidence is proven","Orbitech had weak MFE and severe MAE; Bosung Powertec showed 4B event-cap behavior after May nuclear-equipment spike","R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME|R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,block_positive_stage_when_nuclear_theme_has_high_MAE_without_project_bridge,0,"High MAE after bridge-missing nuclear-policy/theme entries should block Stage2/Stage3 promotion unless project, legal, service backlog and margin evidence survives","Orbitech MAE90=-40.00 and Bosung Powertec MAE90=-39.41","R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME|R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L92_C04_KEPCOKPS_2024_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "051600", "company_name": "한전KPS", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "case_type": "structural_success_with_later_policy_project_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear O&M / plant service / policy-project bridge produced positive 30D/90D and strong 180D MFE with controlled MAE. C04 works when nuclear policy maps into maintenance/service backlog, regulated/project visibility, execution capacity, and margin/revision bridge rather than theme label alone.", "current_profile_verdict": "current_profile_kept_but_C04_positive_requires_project_service_backlog_execution_margin_bridge_not_nuclear_policy_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidates in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R11L92_C04_ORBITECH_2024_NUCLEAR_INSPECTION_THEME_FALSE_STAGE2", "symbol": "046120", "company_name": "오르비텍", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "case_type": "failed_rerating_nuclear_inspection_theme_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion: 046120 appears lightly in C04 coverage, but this row uses a fresh 2024 entry date and high-MAE inspection-theme failure family.", "independent_evidence_weight": 0.75, "score_price_alignment": "Nuclear inspection / aircraft-inspection adjacent theme spike produced weak forward MFE and then severe 90D/180D MAE. C04 Stage2 should not be awarded without confirmed project/order, inspection-service backlog, regulatory milestone, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_nuclear_inspection_theme_counts_without_project_service_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2017 corporate-action candidate. Reduced evidence weight because 046120 already appears lightly in C04 coverage."}
{"row_type": "case", "case_id": "R11L92_C04_BOSUNGPOWER_2024_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP_4B", "symbol": "006910", "company_name": "보성파워텍", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion: 006910 appears lightly in C04 coverage, but this row uses a new 2024 entry and event-cap/high-MAE family.", "independent_evidence_weight": 0.75, "score_price_alignment": "Nuclear power-equipment / policy-event premium capped near the May spike and then suffered high 90D/180D MAE. C04 should route bridge-missing nuclear equipment premiums to 4B unless project award, service/order backlog, legal/regulatory clarity and margin bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_power_equipment_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1996~2016 corporate-action candidates. Reduced evidence weight because 006910 appears lightly in C04 coverage."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE", "case_id": "R11L92_C04_KEPCOKPS_2024_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "051600", "company_name": "한전KPS", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "sector": "nuclear_O_and_M_policy_project_service_backlog", "primary_archetype": "nuclear_service_backlog_execution_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 34050.0, "evidence_available_at_that_date": "nuclear O&M / plant service project visibility, policy-linked maintenance/service backlog, execution capacity and margin/revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["nuclear_service_backlog_proxy", "policy_project_visibility_proxy", "execution_capacity_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "strong_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_nuclear_policy_valuation_watch", "post_peak_project_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv", "profile_path": "atlas/symbol_profiles/051/051600.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.01, "MFE_90D_pct": 16.01, "MFE_180D_pct": 39.35, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.73, "MAE_90D_pct": -3.23, "MAE_180D_pct": -3.23, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-18", "peak_price": 47450.0, "drawdown_after_peak_pct": -24.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_nuclear_policy_project_valuation_4B_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "nuclear_policy_project_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_nuclear_O_and_M_policy_project_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R11L92_C04_051600_2024-01-24_34050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME", "case_id": "R11L92_C04_ORBITECH_2024_NUCLEAR_INSPECTION_THEME_FALSE_STAGE2", "symbol": "046120", "company_name": "오르비텍", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "sector": "nuclear_inspection_service_theme", "primary_archetype": "nuclear_inspection_theme_without_project_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-05-27", "entry_date": "2024-05-27", "entry_price": 3400.0, "evidence_available_at_that_date": "nuclear inspection / service theme and nuclear-policy expectation proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_inspection_theme", "service_project_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "severe_MAE90", "project_backlog_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/046/046120/2024.csv", "profile_path": "atlas/symbol_profiles/046/046120.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.53, "MFE_90D_pct": 3.53, "MFE_180D_pct": 3.53, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -25.29, "MAE_90D_pct": -40.0, "MAE_180D_pct": -40.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 3520.0, "drawdown_after_peak_pct": -42.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.97, "four_b_full_window_peak_proximity": 0.97, "four_b_timing_verdict": "nuclear_inspection_theme_was_false_stage2_due_missing_project_backlog_margin_bridge", "four_b_evidence_type": ["nuclear_service_theme_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_nuclear_inspection_theme_without_project_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_nuclear_inspection_theme_counts_without_project_service_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2017_CA", "same_entry_group_id": "R11L92_C04_046120_2024-05-27_3400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_soft_expansion", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C04_symbol_new_entry_date_and_failure_family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP", "case_id": "R11L92_C04_BOSUNGPOWER_2024_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP_4B", "symbol": "006910", "company_name": "보성파워텍", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "sector": "nuclear_power_equipment_policy_event_premium", "primary_archetype": "nuclear_power_equipment_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-05-27", "entry_date": "2024-05-27", "entry_price": 4225.0, "evidence_available_at_that_date": "nuclear power-equipment / policy event premium after May spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_power_equipment_theme", "policy_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE90", "project_order_margin_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006910/2024.csv", "profile_path": "atlas/symbol_profiles/006/006910.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.18, "MFE_90D_pct": 10.18, "MFE_180D_pct": 10.18, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -18.34, "MAE_90D_pct": -39.41, "MAE_180D_pct": -39.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 4655.0, "drawdown_after_peak_pct": -45.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_full_window_4B_timing_nuclear_power_equipment_policy_event_cap", "four_b_evidence_type": ["nuclear_policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_nuclear_power_equipment_policy_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_power_equipment_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1996_2016_CA", "same_entry_group_id": "R11L92_C04_006910_2024-05-27_4225", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C04_symbol_new_entry_date_and_event_cap_family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L92_C04_KEPCOKPS_2024_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_POSITIVE", "trigger_id": "R11L92_C04_KEPCOKPS_2024_STAGE2_ACTIONABLE_NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE", "symbol": "051600", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 60, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "nuclear_O_and_M_policy_project_bridge_positive", "MFE_90D_pct": 16.01, "MAE_90D_pct": -3.23, "score_return_alignment_label": "nuclear_O_and_M_policy_project_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L92_C04_ORBITECH_2024_NUCLEAR_INSPECTION_THEME_FALSE_STAGE2", "trigger_id": "R11L92_C04_ORBITECH_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSPECTION_THEME", "symbol": "046120", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "nuclear_inspection_theme_false_stage2", "MFE_90D_pct": 3.53, "MAE_90D_pct": -40.0, "score_return_alignment_label": "nuclear_inspection_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nuclear_inspection_theme_counts_without_project_service_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L92_C04_BOSUNGPOWER_2024_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP_4B", "trigger_id": "R11L92_C04_BOSUNGPOWER_2024_STAGE4B_NUCLEAR_POWER_EQUIPMENT_EVENT_CAP", "symbol": "006910", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "policy_or_regulatory_score", "relative_strength_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "nuclear_power_equipment_event_cap_4B_guard", "MFE_90D_pct": 10.18, "MAE_90D_pct": -39.41, "score_return_alignment_label": "nuclear_power_equipment_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_power_equipment_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "92", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_O_AND_M_POLICY_PROJECT_BRIDGE_VS_NUCLEAR_INSPECTION_FALSE_STAGE2_AND_POWER_EQUIPMENT_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 1, "same_archetype_new_symbol_count": 1, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["nuclear_O_and_M_policy_project_bridge_positive", "nuclear_inspection_theme_false_stage2", "nuclear_power_equipment_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Soft-expansion rows should receive reduced evidence weight if the symbol already appears in the same archetype.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
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
10. Add tests that bridge-missing C04 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R11
completed_loop = 92
next_round = R12
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
