# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R3
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
fine_archetype_id = ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | JV_utilization_AMPC_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R3_loop_98_L3_BATTERY_EV_GREEN_MOBILITY_C13_BATTERY_JV_UTILIZATION_AMPC_IRA_research.md
```

This file is the corrected final output for this execution. The scheduler state after R2 loop 98 is R3 / loop 98. R3 is the L3 battery/EV/green-mobility round, and this run fills C13 battery JV utilization / AMPC / IRA behavior rather than repeating the immediately preceding R3 loop 97 C12 customer contract/call-off file or previous R3 C11/C13/C14 symbols.

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
JV_utilization_AMPC_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R3
scheduled_loop = 98
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
round_sector_consistency = pass
computed_next_round = R4
computed_next_loop = 98
```

C13 is a battery JV/utilization/AMPC archetype. A JV or IRA headline is the contract jacket; the useful signal appears only when customer call-off, capacity ramp, utilization, AMPC recognition, margin and revision are stitched together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C13_BATTERY_JV_UTILIZATION_AMPC_IRA = 23 rows / 16 symbols / good-bad Stage2 9-2 / 4B-4C 2-0
top covered symbols include 005070(3), 020150(3), 003670(2), 025900(2), 348370(2), 002710(1)
previous R3 loop-95 C13 symbols avoided: 014820, 093370, 450080
previous R3 loop-96 C11 symbols avoided: 006110, 079810, 417010
previous R3 loop-97 C12 symbols avoided: 011790, 243840, 419050
previous R2 loop-98 C09 symbols avoided: 110990, 405100, 389020
```

Selected rows avoid hard duplicates and top repeated C13 symbols:

```text
036830 / Stage2-Actionable / 2024-04-24
066970 / Stage2-Actionable / 2024-03-19
011500 / Stage4B / 2024-03-12
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
| 036830 | atlas/symbol_profiles/036/036830.json | selected 2024 window clean after old 2001/2004/2020 CA candidates |
| 066970 | atlas/symbol_profiles/066/066970.json | selected 2024 window clean after old 2016/2021 CA candidates |
| 011500 | atlas/symbol_profiles/011/011500.json | selected 2024 window clean after old 2008 CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 036830 | 2024-04-24 | yes | 180 | yes | yes | true |
| R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2 | 066970 | 2024-03-19 | yes | 180 | yes | yes | true |
| R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B | 011500 | 2024-03-12 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE | Positive Stage2 requires customer call-off, JV utilization, capacity ramp, AMPC/IRA economics, margin and revision bridge. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2 | Cathode/IRA-AMPC rebound watch without customer call-off and utilization/margin bridge can become false Stage2. |
| C13_BATTERY_JV_UTILIZATION_AMPC_IRA | SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B | Solid-state electrolyte/JV event premium should route to 4B when scale-up, utilization and margin bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE | 036830 | 솔브레인홀딩스 | positive | Battery electrolyte/JV utilization bridge produced very strong MFE, but later drawdown requires valuation watch. |
| R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2 | 066970 | 엘앤에프 | counterexample | Cathode IRA-AMPC rebound had limited incremental MFE and high MAE without durable call-off/utilization bridge. |
| R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B | 011500 | 한농화성 | counterexample / 4B | Solid-state electrolyte event premium capped near the March spike and then de-rated deeply. |

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
| Solbrain Holdings electrolyte/JV utilization AMPC bridge | historical public/report proxy | true | true | shadow-only positive |
| L&F cathode IRA-AMPC false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hannong Chemical solid-state electrolyte event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036830 | atlas/ohlcv_tradable_by_symbol_year/036/036830/2024.csv | atlas/symbol_profiles/036/036830.json |
| 066970 | atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv | atlas/symbol_profiles/066/066970.json |
| 011500 | atlas/ohlcv_tradable_by_symbol_year/011/011500/2024.csv | atlas/symbol_profiles/011/011500.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE | 036830 | Stage2-Actionable | 2024-04-24 | 50700 | positive | JV/utilization AMPC bridge worked, later valuation watch required |
| R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH | 066970 | Stage2-Actionable | 2024-03-19 | 178500 | counterexample | cathode IRA-AMPC high-MAE false Stage2 |
| R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP | 011500 | Stage4B | 2024-03-12 | 25750 | counterexample/4B | solid-state electrolyte event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE | 50700 | 83.83 | -6.21 | 83.83 | -16.47 | 83.83 | -16.47 | 2024-06-10 | 93200 | -54.56 |
| R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH | 178500 | 11.48 | -21.23 | 11.48 | -31.93 | 11.48 | -53.56 | 2024-03-25 | 199000 | -58.34 |
| R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP | 25750 | 4.66 | -34.41 | 4.66 | -47.96 | 4.66 | -48.66 | 2024-03-12 | 26950 | -50.95 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C13 Stage2 needs customer call-off / JV utilization / AMPC recognition / capacity ramp / margin / revision bridge |
| JV_utilization_AMPC_guardrail | strengthen: battery-JV/IRA/AMPC labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing cathode and solid-state electrolyte premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C13 rows cannot promote without durable utilization/margin bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether battery-JV/IRA/AMPC narrative becomes utilization, AMPC recognition and margin evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 036830 | good_stage2_with_later_watch | Utilization and margin bridge produced very strong MFE, but later drawdown requires valuation and 4B watch. |
| 066970 | bad_stage2 | Cathode IRA-AMPC watch lacked customer call-off/utilization bridge and suffered high MAE. |
| 011500 | good_4B | Solid-state electrolyte event premium peaked immediately and then drew down deeply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 066970 cathode IRA-AMPC false Stage2 | 0.90 | 0.90 | false Stage2 due missing customer call-off / JV utilization / margin bridge |
| 011500 solid-state electrolyte cap | 0.96 | 0.96 | good full-window 4B timing after solid-state electrolyte event premium |
| 036830 electrolyte/JV utilization bridge | n/a | n/a | positive Stage2, but later battery-JV utilization valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 066970 / 011500
```

No hard 4C candidate is introduced in this R3 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 battery JV/utilization/AMPC cases, Stage2 requires verified customer call-off, JV utilization, capacity ramp, AMPC/IRA recognition, ASP/mix, margin, or revision bridge. Battery, JV, IRA, AMPC, cathode, electrolyte, solid-state, utilization or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C13_BATTERY_JV_UTILIZATION_AMPC_IRA
rule = C13 should split true customer-calloff/JV-utilization/AMPC/margin positives from cathode IRA-AMPC false Stage2 and solid-state electrolyte event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 33.32 | -32.12 | 0.67 | mixed; C13 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 33.32 | -32.12 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L3 JV/utilization/AMPC bridge required | 2 | 47.66 | -24.20 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C13 bridge vs event-cap split | 2 | 47.66 | -24.20 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing battery-JV/AMPC themes as positive | 1 | 83.83 | -16.47 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 036830 electrolyte/JV bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 83.83 | -16.47 | battery_JV_utilization_AMPC_positive |
| 066970 cathode IRA-AMPC false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 11.48 | -31.93 | cathode_IRA_AMPC_false_stage2 |
| 011500 solid-state electrolyte cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 4.66 | -47.96 | solid_state_electrolyte_JV_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds R3 loop98 C13: Solbrain Holdings battery electrolyte/JV utilization AMPC positive, L&F cathode IRA-AMPC false Stage2, and Hannong Chemical solid-state electrolyte event-cap 4B while avoiding top repeated C13 and previous R3/R2 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, JV_utilization_AMPC_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: battery_JV_utilization_AMPC_positive, cathode_IRA_AMPC_false_stage2, solid_state_electrolyte_JV_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, JV_utilization_AMPC_guardrail, high_MAE_guardrail
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
- C13 battery JV/utilization/AMPC/IRA bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,C13_requires_customer_calloff_JV_utilization_AMPC_margin_revision_bridge,0,"C13 Stage2 should require customer call-off, JV utilization, capacity ramp, AMPC/IRA recognition, ASP/mix, margin, or revision bridge, not battery/JV/IRA/AMPC label alone","Solbrain Holdings positive worked; L&F and Hannong Chemical event/watch rows failed positive-stage promotion","R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE|R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH|R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,cap_bridge_missing_cathode_and_solid_state_electrolyte_JV_event_premiums_as_4B_watch,0,"Cathode IRA-AMPC and solid-state electrolyte premiums can peak before customer call-off, JV utilization, AMPC recognition and margin bridge is proven","L&F had high MAE after a limited recovery; Hannong Chemical showed 4B event-cap behavior after the March solid-state electrolyte spike","R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH|R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C13_BATTERY_JV_UTILIZATION_AMPC_IRA,configured,block_positive_stage_when_battery_JV_AMPC_theme_has_high_or_persistent_MAE_without_utilization_bridge,0,"High or persistent MAE after bridge-missing C13 entries should block Stage2/Stage3 promotion unless customer call-off, utilization and margin evidence survives","L&F MAE90=-31.93 and Hannong Chemical MAE90=-47.96","R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH|R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "symbol": "036830", "company_name": "솔브레인홀딩스", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "case_type": "structural_success_with_later_battery_JV_utilization_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Battery electrolyte / holdco-JV utilization and AMPC/IRA bridge produced very strong 30D/90D MFE after the April retest, but the later August drawdown shows why C13 positives still need valuation and utilization watch.", "current_profile_verdict": "current_profile_kept_but_C13_positive_requires_JV_utilization_customer_calloff_AMPC_margin_revision_bridge_not_battery_JV_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2004/2020 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "case_type": "failed_rerating_cathode_IRA_AMPC_utilization_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Cathode / IRA-AMPC recovery watch after the March rebound had limited incremental MFE and then severe MAE. C13 Stage2 should not be awarded without confirmed customer call-off, JV/utilization, ASP/mix, AMPC recognition, margin and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_cathode_IRA_AMPC_watch_counts_without_customer_calloff_JV_utilization_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2016/2021 corporate-action candidates. KOSDAQ GLOBAL→KOSPI market migration occurred in January but is not marked as a 2024 CA candidate in profile."}
{"row_type": "case", "case_id": "R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B", "symbol": "011500", "company_name": "한농화성", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Solid-state electrolyte / battery-material event premium capped near the March spike and then de-rated. C13 should route bridge-missing solid-state electrolyte/JV premiums to 4B unless customer/JV order, utilization, AMPC or subsidy economics, scale-up, margin and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_solid_state_electrolyte_JV_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2008 corporate-action candidate. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE", "case_id": "R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "symbol": "036830", "company_name": "솔브레인홀딩스", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "sector": "battery_electrolyte_holdco_JV_utilization_AMPC_IRA_margin", "primary_archetype": "JV_utilization_customer_calloff_AMPC_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | JV_utilization_AMPC_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-24", "entry_date": "2024-04-24", "entry_price": 50700.0, "evidence_available_at_that_date": "battery electrolyte / holdco-JV utilization, customer call-off recovery, AMPC/IRA optionality, margin and revision bridge proxy after April retest; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["JV_utilization_proxy", "customer_calloff_proxy", "AMPC_IRA_optional_proxy", "capacity_ramp_proxy", "margin_revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "later_drawdown_requires_4B_watch"], "stage4b_evidence_fields": ["later_battery_JV_utilization_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036830/2024.csv", "profile_path": "atlas/symbol_profiles/036/036830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 83.83, "MFE_90D_pct": 83.83, "MFE_180D_pct": 83.83, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.21, "MAE_90D_pct": -16.47, "MAE_180D_pct": -16.47, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-10", "peak_price": 93200.0, "drawdown_after_peak_pct": -54.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_battery_JV_utilization_valuation_4B_watch_needed", "four_b_evidence_type": ["JV_utilization_AMPC_bridge", "customer_calloff_margin", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_battery_electrolyte_JV_utilization_AMPC_bridge_success_with_later_4B_watch", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2004_2020_CA", "same_entry_group_id": "R3L98_C13_036830_2024-04-24_50700", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH", "case_id": "R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2", "symbol": "066970", "company_name": "엘앤에프", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "sector": "cathode_IRA_AMPC_customer_calloff_utilization_watch", "primary_archetype": "cathode_IRA_AMPC_watch_without_customer_calloff_utilization_margin_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | JV_utilization_AMPC_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-03-19", "entry_date": "2024-03-19", "entry_price": 178500.0, "evidence_available_at_that_date": "cathode / IRA-AMPC / battery utilization rebound watch without confirmed customer call-off, JV utilization, ASP/mix, AMPC recognition or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["cathode_IRA_AMPC_watch", "battery_rebound_theme", "relative_strength_rebound"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "high_MAE90", "customer_calloff_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/066/066970/2024.csv", "profile_path": "atlas/symbol_profiles/066/066970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.48, "MFE_90D_pct": 11.48, "MFE_180D_pct": 11.48, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.23, "MAE_90D_pct": -31.93, "MAE_180D_pct": -53.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-25", "peak_price": 199000.0, "drawdown_after_peak_pct": -58.34, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "cathode_IRA_AMPC_watch_was_false_stage2_due_missing_customer_calloff_JV_utilization_margin_revision_bridge", "four_b_evidence_type": ["cathode_IRA_AMPC_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_cathode_IRA_AMPC_watch_without_customer_calloff_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_cathode_IRA_AMPC_watch_counts_without_customer_calloff_JV_utilization_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2016_2021_CA", "same_entry_group_id": "R3L98_C13_066970_2024-03-19_178500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP", "case_id": "R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B", "symbol": "011500", "company_name": "한농화성", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "sector": "solid_state_electrolyte_battery_material_JV_event_premium", "primary_archetype": "solid_state_electrolyte_JV_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | JV_utilization_AMPC_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-12", "entry_date": "2024-03-12", "entry_price": 25750.0, "evidence_available_at_that_date": "solid-state electrolyte / battery-material event premium without confirmed customer/JV order, utilization, AMPC/subsidy economics, scale-up or margin revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["solid_state_electrolyte_event", "battery_material_JV_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "customer_JV_utilization_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011500/2024.csv", "profile_path": "atlas/symbol_profiles/011/011500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 4.66, "MFE_90D_pct": 4.66, "MFE_180D_pct": 4.66, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -34.41, "MAE_90D_pct": -47.96, "MAE_180D_pct": -48.66, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-12", "peak_price": 26950.0, "drawdown_after_peak_pct": -50.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_solid_state_electrolyte_JV_event_cap", "four_b_evidence_type": ["solid_state_electrolyte_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_solid_state_electrolyte_JV_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_solid_state_electrolyte_JV_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2008_CA", "same_entry_group_id": "R3L98_C13_011500_2024-03-12_25750", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L98_C13_SOLBRAINHOLDINGS_2024_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_POSITIVE", "trigger_id": "R3L98_C13_SOLBRAINHOLDINGS_2024_STAGE2_ACTIONABLE_ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE", "symbol": "036830", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 25, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 55, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 60, "policy_or_regulatory_score": 45, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "execution_risk_score"], "component_delta_explanation": "electrolyte_holdco_JV_utilization_AMPC_positive", "MFE_90D_pct": 83.83, "MAE_90D_pct": -16.47, "score_return_alignment_label": "battery_JV_utilization_AMPC_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L98_C13_LF_2024_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R3L98_C13_LF_2024_STAGE2_FALSE_POSITIVE_CATHODE_IRA_AMPC_UTILIZATION_WATCH", "symbol": "066970", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "cathode_IRA_AMPC_false_stage2", "MFE_90D_pct": 11.48, "MAE_90D_pct": -31.93, "score_return_alignment_label": "cathode_IRA_AMPC_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_cathode_IRA_AMPC_watch_counts_without_customer_calloff_JV_utilization_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R3L98_C13_HANNONG_2024_SOLID_STATE_ELECTROLYTE_EVENT_CAP_4B", "trigger_id": "R3L98_C13_HANNONG_2024_STAGE4B_SOLID_STATE_ELECTROLYTE_JV_EVENT_CAP", "symbol": "011500", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "solid_state_electrolyte_JV_event_cap_4B_guard", "MFE_90D_pct": 4.66, "MAE_90D_pct": -47.96, "score_return_alignment_label": "solid_state_electrolyte_JV_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_solid_state_electrolyte_JV_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R3", "loop": "98", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C13_BATTERY_JV_UTILIZATION_AMPC_IRA", "fine_archetype_id": "ELECTROLYTE_HOLDCO_JV_UTILIZATION_AMPC_BRIDGE_VS_CATHODE_IRA_AMPC_HIGH_MAE_FALSE_STAGE2_AND_SOLID_STATE_ELECTROLYTE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "JV_utilization_AMPC_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["battery_JV_utilization_AMPC_positive", "cathode_IRA_AMPC_false_stage2", "solid_state_electrolyte_JV_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C13_BATTERY_JV_UTILIZATION_AMPC_IRA","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C13 rows need explicit customer call-off, JV utilization, capacity ramp, AMPC/IRA recognition, ASP/mix, margin or revision bridge before positive promotion.
- In C13, bridge-missing battery JV/AMPC/IRA event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C13 battery JV/utilization/AMPC/IRA rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R3
completed_loop = 98
next_round = R4
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
