# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_90_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This loop continues loop 90 after R8. R9 allows the L3 mobility route or the L9 construction route. This run uses the L3 mobility route and adds 3 C29 mobility volume/margin operating-leverage cases: one hybrid mobility volume/margin positive, one EV reducer parts false Stage2, and one EV wire-harness 4B event-cap counterexample.

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
scheduled_round = R9
scheduled_loop = 90
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 90
```

Previous R9 loop 89 used C13 battery utilization. This loop avoids repeating that battery-specific axis and returns to C29 with non-top-covered symbols.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE = 60 rows / 27 symbols / good-bad Stage2 26-13 / 4B-4C 6-0
top covered symbols include 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
previous R9 loop-88 C29 symbols avoided: 161390, 003620, 204320
previous R9 loop-89 C13 symbols avoided: 004490, 243840, 393890
```

Selected rows avoid those repeated combinations and top repeated C29 symbols:

```text
123410 / Stage2-Actionable / 2024-01-24
092200 / Stage2-Actionable / 2024-06-26
023810 / Stage4B / 2024-03-20
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
| 123410 | atlas/symbol_profiles/123/123410.json | selected 2024 window clean; CA candidate is 2012-03-02 |
| 092200 | atlas/symbol_profiles/092/092200.json | selected 2024 window clean; CA candidate is 2019-08-28 |
| 023810 | atlas/symbol_profiles/023/023810.json | selected 2024 window clean; CA candidates are 2003 or earlier |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L90_C29_KOREAFT_2024_HYBRID_VOLUME_MARGIN_BRIDGE_POSITIVE | 123410 | 2024-01-24 | yes | 180 | yes | yes | true |
| R9L90_C29_DIC_2024_EV_REDUCER_PARTS_FALSE_STAGE2 | 092200 | 2024-06-26 | yes | 180 | yes | yes | true |
| R9L90_C29_INFAC_2024_EV_WIREHARNESS_EVENT_CAP_4B | 023810 | 2024-03-20 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE | Positive Stage2 requires volume, customer mix, operating leverage, margin, and revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_REDUCER_PARTS_FALSE_STAGE2 | EV reducer/parts label without volume-margin bridge can become high-MAE false Stage2. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | EV_WIREHARNESS_EVENT_CAP_4B | Wire-harness/mobility parts premium should route to 4B when the bridge is capped or unverified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L90_C29_KOREAFT_2024_HYBRID_VOLUME_MARGIN_BRIDGE_POSITIVE | 123410 | 코리아에프티 | positive | Hybrid/mobility volume-margin bridge produced high MFE with controlled entry MAE. |
| R9L90_C29_DIC_2024_EV_REDUCER_PARTS_FALSE_STAGE2 | 092200 | 디아이씨 | counterexample | EV reducer parts spike had weak MFE and deep MAE. |
| R9L90_C29_INFAC_2024_EV_WIREHARNESS_EVENT_CAP_4B | 023810 | 인팩 | counterexample / 4B | EV wire-harness theme premium capped around the March spike and de-rated. |

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
| KoreaFT hybrid volume/margin bridge | historical public/news proxy | true | true | shadow-only positive |
| DIC EV reducer parts false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| INFAC EV wire-harness cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 123410 | atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv | atlas/symbol_profiles/123/123410.json |
| 092200 | atlas/ohlcv_tradable_by_symbol_year/092/092200/2024.csv | atlas/symbol_profiles/092/092200.json |
| 023810 | atlas/ohlcv_tradable_by_symbol_year/023/023810/2024.csv | atlas/symbol_profiles/023/023810.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE | 123410 | Stage2-Actionable | 2024-01-24 | 4225 | positive | hybrid mobility volume/margin bridge worked |
| R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME | 092200 | Stage2-Actionable | 2024-06-26 | 6290 | counterexample | EV reducer parts false Stage2 |
| R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP | 023810 | Stage4B | 2024-03-20 | 10340 | counterexample/4B | EV wire-harness event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE | 4225 | 53.37 | -8.76 | 93.85 | -8.76 | 93.85 | -8.76 | 2024-04-26 | 8190 | -51.28 |
| R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME | 6290 | 10.02 | -26.07 | 10.02 | -40.78 | 10.02 | -49.68 | 2024-06-26 | 6920 | -54.26 |
| R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP | 10340 | 2.22 | -20.70 | 2.22 | -25.53 | 2.22 | -47.10 | 2024-03-20 | 10570 | -48.25 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs volume/customer mix/operating leverage/margin bridge |
| local_4b_watch_guard | strengthen: EV parts and wire-harness theme premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE auto-parts theme rows cannot promote without durable margin bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is mobility volume/margin bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 123410 | good_stage2 | Hybrid/mobility volume-margin bridge produced high MFE. |
| 092200 | bad_stage2 | EV reducer/parts theme had weak MFE and high MAE. |
| 023810 | good_4B | Wire-harness mobility premium capped at the event spike. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 092200 EV reducer parts false Stage2 | 1.00 | 1.00 | EV reducer parts theme spike was false Stage2 event cap |
| 023810 EV wire-harness cap | 1.00 | 1.00 | good full-window 4B timing |
| 123410 hybrid volume/margin bridge | n/a | n/a | positive Stage2, but later mobility-margin valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 092200 / 023810
```

No hard 4C candidate is proposed. R9 loop 90 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3 mobility volume/margin cases, Stage2 requires verified volume, customer mix, utilization, operating leverage, gross-margin recovery, or revision bridge. Auto parts, EV reducer, wire-harness, hybrid, or mobility theme label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split true volume/margin operating-leverage positives from EV-parts false Stage2 and wire-harness event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 35.36 | -25.02 | 0.67 | mixed; C29 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 35.36 | -25.02 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L3 mobility volume/margin bridge required | 2 | 51.94 | -24.77 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 51.94 | -24.77 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing EV parts themes as positive | 1 | 93.85 | -8.76 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 123410 hybrid volume/margin bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 93.85 | -8.76 | hybrid_mobility_volume_margin_positive |
| 092200 EV reducer false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 10.02 | -40.78 | EV_reducer_parts_false_stage2 |
| 023810 wire-harness cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.22 | -25.53 | EV_wireharness_mobility_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 hybrid mobility volume/margin positive, EV reducer parts false Stage2, and EV wire-harness event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: hybrid_mobility_volume_margin_positive, EV_reducer_parts_false_stage2, EV_wireharness_mobility_event_cap_4B
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
- C29 mobility volume/margin bridge vs EV-parts event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_volume_customer_mix_margin_operating_leverage_bridge,0,"C29 Stage2 should require volume, customer mix, utilization, operating leverage, margin, or revision bridge, not auto-parts/EV theme label alone","KoreaFT positive worked; DIC and INFAC theme/event rows failed positive-stage promotion","R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE|R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME|R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_EV_parts_and_wireharness_mobility_theme_premiums_as_4B_watch,0,"EV parts and wire-harness mobility theme premiums can peak before confirmed volume/margin bridge appears","DIC and INFAC showed weak MFE with deep 90D/180D MAE after bridge-missing spikes","R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME|R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,block_positive_stage_when_EV_parts_theme_has_high_MAE_without_margin_bridge,0,"High MAE after an auto-parts theme spike should block promotion unless volume/margin evidence survives the drawdown","DIC MAE90=-40.78; INFAC MAE180=-47.10","R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME|R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L90_C29_KOREAFT_2024_HYBRID_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Hybrid/mobility volume and margin operating-leverage bridge produced high 30D/90D/180D MFE with controlled entry MAE; C29 works when mobility volume, customer mix, operating leverage, and margin/revision bridge are visible.", "current_profile_verdict": "current_profile_kept_but_C29_positive_requires_volume_margin_customer_mix_bridge_not_auto_parts_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; old 2012 SPAC/merger CA candidate is outside window. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R9L90_C29_DIC_2024_EV_REDUCER_PARTS_FALSE_STAGE2", "symbol": "092200", "company_name": "디아이씨", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV reducer / mobility parts recovery spike had weak forward MFE and deep 90D/180D MAE; C29 Stage2 should not be awarded without confirmed volume, customer mix, utilization, and margin/revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_parts_theme_counts_without_volume_margin_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; 2019 CA candidate outside selected window. Source-proxy only."}
{"row_type": "case", "case_id": "R9L90_C29_INFAC_2024_EV_WIREHARNESS_EVENT_CAP_4B", "symbol": "023810", "company_name": "인팩", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "EV wire-harness / mobility parts theme premium capped around the March spike and then de-rated; auto-parts theme premium should route to 4B unless volume and margin bridge remains expanding.", "current_profile_verdict": "current_profile_4B_too_late_if_EV_wireharness_mobility_theme_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; CA candidates are 2003 or earlier. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE", "case_id": "R9L90_C29_KOREAFT_2024_HYBRID_VOLUME_MARGIN_BRIDGE_POSITIVE", "symbol": "123410", "company_name": "코리아에프티", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "sector": "hybrid_mobility_volume_margin", "primary_archetype": "hybrid_vehicle_volume_customer_mix_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 4225.0, "evidence_available_at_that_date": "hybrid vehicle / mobility parts volume, customer mix, operating leverage and margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["hybrid_vehicle_volume_proxy", "customer_mix_quality", "operating_leverage_proxy", "margin_revision_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "very_high_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_mobility_margin_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/123/123410/2024.csv", "profile_path": "atlas/symbol_profiles/123/123410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 53.37, "MFE_90D_pct": 93.85, "MFE_180D_pct": 93.85, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -8.76, "MAE_90D_pct": -8.76, "MAE_180D_pct": -8.76, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-26", "peak_price": 8190.0, "drawdown_after_peak_pct": -51.28, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_mobility_margin_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "mobility_margin_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_hybrid_mobility_volume_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L90_C29_123410_2024-01-24_4225", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME", "case_id": "R9L90_C29_DIC_2024_EV_REDUCER_PARTS_FALSE_STAGE2", "symbol": "092200", "company_name": "디아이씨", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "sector": "EV_reducer_mobility_parts", "primary_archetype": "EV_reducer_parts_theme_without_volume_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 6290.0, "evidence_available_at_that_date": "EV reducer / mobility parts recovery theme and customer-volume watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_reducer_parts_theme", "customer_volume_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "deep_MAE90", "volume_margin_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/092/092200/2024.csv", "profile_path": "atlas/symbol_profiles/092/092200.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 10.02, "MFE_90D_pct": 10.02, "MFE_180D_pct": 10.02, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -26.07, "MAE_90D_pct": -40.78, "MAE_180D_pct": -49.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 6920.0, "drawdown_after_peak_pct": -54.26, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "EV_reducer_parts_theme_spike_was_false_stage2_event_cap", "four_b_evidence_type": ["price_only", "positioning_overheat", "volume_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_EV_reducer_parts_without_volume_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_parts_theme_counts_without_volume_margin_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L90_C29_092200_2024-06-26_6290", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP", "case_id": "R9L90_C29_INFAC_2024_EV_WIREHARNESS_EVENT_CAP_4B", "symbol": "023810", "company_name": "인팩", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "sector": "EV_wireharness_mobility_parts_theme", "primary_archetype": "EV_wireharness_theme_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-20", "entry_date": "2024-03-20", "entry_price": 10340.0, "evidence_available_at_that_date": "EV wire-harness / mobility parts premium after March spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["EV_wireharness_theme", "mobility_parts_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023810/2024.csv", "profile_path": "atlas/symbol_profiles/023/023810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.22, "MFE_90D_pct": 2.22, "MFE_180D_pct": 2.22, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -20.7, "MAE_90D_pct": -25.53, "MAE_180D_pct": -47.1, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-20", "peak_price": 10570.0, "drawdown_after_peak_pct": -48.25, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_EV_wireharness_mobility_theme_cap", "four_b_evidence_type": ["mobility_theme_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_EV_wireharness_mobility_theme_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L90_C29_023810_2024-03-20_10340", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L90_C29_KOREAFT_2024_HYBRID_VOLUME_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R9L90_C29_KOREAFT_2024_STAGE2_ACTIONABLE_HYBRID_VOLUME_MARGIN_BRIDGE", "symbol": "123410", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "hybrid_mobility_volume_margin_positive", "MFE_90D_pct": 93.85, "MAE_90D_pct": -8.76, "score_return_alignment_label": "hybrid_mobility_volume_margin_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L90_C29_DIC_2024_EV_REDUCER_PARTS_FALSE_STAGE2", "trigger_id": "R9L90_C29_DIC_2024_STAGE2_FALSE_POSITIVE_EV_REDUCER_PARTS_THEME", "symbol": "092200", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_reducer_parts_false_stage2", "MFE_90D_pct": 10.02, "MAE_90D_pct": -40.78, "score_return_alignment_label": "EV_reducer_parts_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_EV_reducer_parts_theme_counts_without_volume_margin_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L90_C29_INFAC_2024_EV_WIREHARNESS_EVENT_CAP_4B", "trigger_id": "R9L90_C29_INFAC_2024_STAGE4B_EV_WIREHARNESS_MOBILITY_THEME_CAP", "symbol": "023810", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 30, "revision_score": 30, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 30, "execution_risk_score": 85, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "EV_wireharness_mobility_event_cap_4B_guard", "MFE_90D_pct": 2.22, "MAE_90D_pct": -25.53, "score_return_alignment_label": "EV_wireharness_mobility_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_EV_wireharness_mobility_theme_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "90", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "HYBRID_MOBILITY_VOLUME_MARGIN_BRIDGE_VS_AUTO_PARTS_AND_EV_WIREHARNESS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["hybrid_mobility_volume_margin_positive", "EV_reducer_parts_false_stage2", "EV_wireharness_mobility_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L3_BATTERY_EV_GREEN_MOBILITY","canonical_archetype_id":"C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R9
completed_loop = 90
next_round = R10
next_loop = 90
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
