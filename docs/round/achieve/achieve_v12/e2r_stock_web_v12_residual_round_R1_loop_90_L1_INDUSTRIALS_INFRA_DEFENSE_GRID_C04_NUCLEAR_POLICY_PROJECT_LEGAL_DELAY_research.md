# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
fine_archetype_id = NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_90_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md
```

This loop starts loop 90 after the completed R13 loop 89 review. It adds 3 C04 nuclear policy/project cases: one nuclear O&M / policy-project bridge positive, one nuclear-instrument false Stage2, and one nuclear-maintenance 4B event-cap counterexample.

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
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R1
scheduled_loop = 90
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 90
```

R1 permits industrial / infrastructure / defense / grid research. Previous R1 loop 89 used C02 and R11 loop 89 already used C03, so this loop fills C04 nuclear policy/project residuals.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY = 12 rows / 7 symbols / good-bad Stage2 5-3 / 4B-4C 1-0
top covered symbols include 011700(4), 083650(3), 006910(1), 034020(1), 042370(1), 046120(1)
previous R1 loop-89 C02 symbols avoided: 103590, 199820, 060370
previous R11 loop-89 C03 symbols avoided: 064350, 010820, 099320
```

Selected rows avoid those repeated combinations:

```text
130660 / Stage2-Actionable / 2024-06-07
105840 / Stage2-Actionable / 2024-01-24
094820 / Stage4B / 2024-04-05
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
| 130660 | atlas/symbol_profiles/130/130660.json | no corporate-action candidate |
| 105840 | atlas/symbol_profiles/105/105840.json | selected 2024 window clean; CA candidates are 2012 |
| 094820 | atlas/symbol_profiles/094/094820.json | selected 2024 window clean; CA candidates are 2011 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L90_C04_KEPCOIND_2024_NUCLEAR_OM_POLICY_PROJECT_BRIDGE_POSITIVE | 130660 | 2024-06-07 | yes | 180 | yes | yes | true |
| R1L90_C04_WOOJIN_2024_NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2 | 105840 | 2024-01-24 | yes | 180 | yes | yes | true |
| R1L90_C04_ILJINPOWER_2024_NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B | 094820 | 2024-04-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_OM_POLICY_PROJECT_BRIDGE | Positive Stage2 requires policy/project/O&M/order/service-revenue/margin bridge. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2 | Instrument/equipment theme without bridge can become false Stage2. |
| C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B | Nuclear maintenance/policy premium should route to 4B when bridge is capped or unverified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L90_C04_KEPCOIND_2024_NUCLEAR_OM_POLICY_PROJECT_BRIDGE_POSITIVE | 130660 | 한전산업 | positive | Nuclear O&M/policy project bridge produced explosive MFE after a clean entry. |
| R1L90_C04_WOOJIN_2024_NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2 | 105840 | 우진 | counterexample | Nuclear instrument theme had brief upside but failed durable bridge confirmation. |
| R1L90_C04_ILJINPOWER_2024_NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B | 094820 | 일진파워 | counterexample / 4B | Nuclear maintenance/policy premium capped at the April spike and then drew down. |

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
| KEPCO Industrial nuclear O&M/project | historical public/news proxy | true | true | shadow-only positive |
| Woojin nuclear instrument theme | historical public/news proxy | true | true | false-Stage2 guardrail |
| Iljin Power nuclear maintenance cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 130660 | atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv; 2025.csv | atlas/symbol_profiles/130/130660.json |
| 105840 | atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv | atlas/symbol_profiles/105/105840.json |
| 094820 | atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv | atlas/symbol_profiles/094/094820.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE | 130660 | Stage2-Actionable | 2024-06-07 | 9500 | positive | nuclear O&M/policy project bridge worked |
| R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME | 105840 | Stage2-Actionable | 2024-01-24 | 9090 | counterexample | nuclear instrument theme false Stage2 |
| R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP | 094820 | Stage4B | 2024-04-05 | 13520 | counterexample/4B | nuclear maintenance/policy event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE | 9500 | 105.26 | 0.00 | 105.26 | 0.00 | 105.26 | -2.95 | 2024-07-18 | 19500 | -52.72 |
| R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME | 9090 | 15.51 | -11.44 | 15.51 | -15.07 | 23.21 | -21.67 | 2024-05-27 | 11200 | -36.43 |
| R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP | 13520 | 3.11 | -15.16 | 3.11 | -18.57 | 3.11 | -37.06 | 2024-04-05 | 13940 | -38.95 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C04 Stage2 needs policy/project/O&M/order/service-revenue/margin bridge |
| local_4b_watch_guard | strengthen: nuclear equipment/maintenance theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 130660 | good_stage2 | Nuclear O&M / policy-project bridge produced explosive upside. |
| 105840 | bad_stage2 | Instrument/equipment theme had weak durability without project/order bridge. |
| 094820 | good_4B | Maintenance/policy theme premium capped near the April spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 105840 nuclear instrument false Stage2 | 0.94 | 0.94 | nuclear instrument theme spike was false Stage2 event cap |
| 094820 nuclear maintenance cap | 1.00 | 1.00 | good full-window 4B timing |
| 130660 O&M/project bridge | n/a | n/a | positive Stage2, but later nuclear-policy valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 105840 / 094820
```

No hard 4C candidate is proposed. R1 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 nuclear policy/project cases, Stage2 requires verified policy-to-project, O&M/service revenue, signed order, backlog, customer, margin, or revision bridge. Nuclear, SMR, instrument, maintenance, or policy-theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY
rule = C04 should split nuclear O&M/project bridge positives from nuclear-instrument false Stage2 and nuclear-maintenance event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 41.29 | -11.21 | 0.67 | mixed; C04 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 41.29 | -11.21 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 nuclear bridge required | 2 | 60.39 | -7.54 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C04 bridge vs event-cap split | 2 | 60.39 | -7.54 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing nuclear themes as positive | 1 | 105.26 | 0.00 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 130660 O&M/project bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 105.26 | 0.00 | nuclear_OM_policy_project_bridge_positive |
| 105840 instrument false | 66 | Stage2-Actionable | 54 | Stage1/Watch | 15.51 | -15.07 | nuclear_instrument_theme_false_stage2 |
| 094820 maintenance cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.11 | -18.57 | nuclear_maintenance_theme_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C04 nuclear O&M/project bridge positive, nuclear-instrument theme false Stage2, and nuclear-maintenance policy theme event-cap 4B split using non-top-covered symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: nuclear_OM_policy_project_bridge_positive, nuclear_instrument_theme_false_stage2, nuclear_maintenance_theme_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard
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
- C04 nuclear policy/project bridge vs nuclear theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,C04_requires_policy_project_OM_order_or_margin_bridge,0,"C04 Stage2 should require policy/project/O&M/service revenue/order/margin bridge, not nuclear policy or nuclear equipment label alone","KEPCO Industrial positive worked; Woojin and Iljin Power theme/event rows failed positive-stage promotion","R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE|R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME|R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,configured,cap_nuclear_equipment_and_maintenance_theme_premiums_as_4B_watch,0,"Nuclear equipment/maintenance theme premiums can peak before verified project/order/margin bridge appears","Woojin and Iljin Power showed bridge-missing event cap / false Stage2 behavior","R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME|R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L90_C04_KEPCOIND_2024_NUCLEAR_OM_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "130660", "company_name": "한전산업", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear O&M / public-utility policy project bridge produced explosive 30D/90D upside with limited drawdown into the early entry path; C04 works only when policy/project economics can map into service revenue, O&M, order, or margin visibility.", "current_profile_verdict": "current_profile_kept_but_C04_positive_requires_policy_project_OM_revenue_or_order_bridge_not_nuclear_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R1L90_C04_WOOJIN_2024_NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "case_type": "failed_rerating_theme_spike", "positive_or_counterexample": "counterexample", "best_trigger": "R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear instrument / small-equipment theme spike had only brief upside and then a sustained de-rating; C04 Stage2 should not be granted without project/order/revenue bridge.", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrument_theme_counts_without_project_order_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Old 2012 CA candidates are outside selected 2024 window. Source-proxy only."}
{"row_type": "case", "case_id": "R1L90_C04_ILJINPOWER_2024_NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B", "symbol": "094820", "company_name": "일진파워", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Nuclear maintenance / policy theme premium capped around the April spike and then drew down; theme premium should route to 4B unless confirmed order, project, O&M, or margin bridge appears.", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_maintenance_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Old 2011 CA candidates are outside selected 2024 window. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE", "case_id": "R1L90_C04_KEPCOIND_2024_NUCLEAR_OM_POLICY_PROJECT_BRIDGE_POSITIVE", "symbol": "130660", "company_name": "한전산업", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "sector": "nuclear_OM_policy_project", "primary_archetype": "nuclear_OM_policy_project_revenue_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-07", "entry_date": "2024-06-07", "entry_price": 9500.0, "evidence_available_at_that_date": "nuclear O&M / utility-policy project bridge, service-revenue and project pipeline proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_policy_tailwind", "OM_service_revenue_proxy", "project_pipeline_visibility", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "limited_entry_MAE"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_nuclear_policy_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/130/130660/2024.csv|atlas/ohlcv_tradable_by_symbol_year/130/130660/2025.csv", "profile_path": "atlas/symbol_profiles/130/130660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 105.26, "MFE_90D_pct": 105.26, "MFE_180D_pct": 105.26, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": 0.0, "MAE_90D_pct": 0.0, "MAE_180D_pct": -2.95, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2024-07-18", "peak_price": 19500.0, "drawdown_after_peak_pct": -52.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_nuclear_policy_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "policy_event_premium", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_nuclear_OM_policy_project_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L90_C04_130660_2024-06-07_9500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME", "case_id": "R1L90_C04_WOOJIN_2024_NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2", "symbol": "105840", "company_name": "우진", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "sector": "nuclear_instrument_equipment_theme", "primary_archetype": "nuclear_instrument_theme_without_project_order_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 9090.0, "evidence_available_at_that_date": "nuclear instrument/equipment policy theme spike proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_instrument_theme", "policy_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "project_order_margin_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105840/2024.csv", "profile_path": "atlas/symbol_profiles/105/105840.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 15.51, "MFE_90D_pct": 15.51, "MFE_180D_pct": 23.21, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.44, "MAE_90D_pct": -15.07, "MAE_180D_pct": -21.67, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-27", "peak_price": 11200.0, "drawdown_after_peak_pct": -36.43, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.94, "four_b_full_window_peak_proximity": 0.94, "four_b_timing_verdict": "nuclear_instrument_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_nuclear_instrument_theme_without_project_order_bridge", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrument_theme_counts_without_project_order_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L90_C04_105840_2024-01-24_9090", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP", "case_id": "R1L90_C04_ILJINPOWER_2024_NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B", "symbol": "094820", "company_name": "일진파워", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "sector": "nuclear_maintenance_policy_theme", "primary_archetype": "nuclear_maintenance_policy_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-04-05", "entry_date": "2024-04-05", "entry_price": 13520.0, "evidence_available_at_that_date": "nuclear maintenance / policy theme premium after April spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["nuclear_maintenance_theme", "policy_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/094/094820/2024.csv", "profile_path": "atlas/symbol_profiles/094/094820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "MFE_180D_pct": 3.11, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.16, "MAE_90D_pct": -18.57, "MAE_180D_pct": -37.06, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-05", "peak_price": 13940.0, "drawdown_after_peak_pct": -38.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_nuclear_maintenance_policy_theme_cap", "four_b_evidence_type": ["policy_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_maintenance_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L90_C04_094820_2024-04-05_13520", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L90_C04_KEPCOIND_2024_NUCLEAR_OM_POLICY_PROJECT_BRIDGE_POSITIVE", "trigger_id": "R1L90_C04_KEPCOIND_2024_STAGE2_ACTIONABLE_NUCLEAR_OM_POLICY_PROJECT_BRIDGE", "symbol": "130660", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 50, "margin_bridge_score": 50, "revision_score": 45, "relative_strength_score": 75, "customer_quality_score": 40, "policy_or_regulatory_score": 70, "valuation_repricing_score": 55, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "nuclear_OM_policy_project_bridge_positive", "MFE_90D_pct": 105.26, "MAE_90D_pct": 0.0, "score_return_alignment_label": "nuclear_OM_policy_project_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L90_C04_WOOJIN_2024_NUCLEAR_INSTRUMENT_THEME_FALSE_STAGE2", "trigger_id": "R1L90_C04_WOOJIN_2024_STAGE2_FALSE_POSITIVE_NUCLEAR_INSTRUMENT_THEME", "symbol": "105840", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "nuclear_instrument_theme_false_stage2", "MFE_90D_pct": 15.51, "MAE_90D_pct": -15.07, "score_return_alignment_label": "nuclear_instrument_theme_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nuclear_instrument_theme_counts_without_project_order_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L90_C04_ILJINPOWER_2024_NUCLEAR_MAINTENANCE_THEME_EVENT_CAP_4B", "trigger_id": "R1L90_C04_ILJINPOWER_2024_STAGE4B_NUCLEAR_MAINTENANCE_THEME_CAP", "symbol": "094820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 30, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 65, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 45, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["policy_or_regulatory_score", "contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "execution_risk_score"], "component_delta_explanation": "nuclear_maintenance_theme_event_cap_4B_guard", "MFE_90D_pct": 3.11, "MAE_90D_pct": -18.57, "score_return_alignment_label": "nuclear_maintenance_theme_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_nuclear_maintenance_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "90", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY", "fine_archetype_id": "NUCLEAR_OM_POLICY_PROJECT_BRIDGE_VS_INSTRUMENT_AND_MAINTENANCE_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["nuclear_OM_policy_project_bridge_positive", "nuclear_instrument_theme_false_stage2", "nuclear_maintenance_theme_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_round = R1
completed_loop = 90
next_round = R2
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
