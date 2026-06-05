# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R9
scheduled_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
fine_archetype_id = TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R9_loop_88_L3_BATTERY_EV_GREEN_MOBILITY_C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE_research.md
```

This loop continues loop 88 after R8. It adds 3 C29 mobility/transport cases: one tire volume/cost margin-bridge positive, one OEM turnaround false Stage2, and one auto-parts/mobility 4B event-cap counterexample.

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
scheduled_round = R9
scheduled_loop = 88
large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
round_sector_consistency = pass
computed_next_round = R10
computed_next_loop = 88
```

R9 permits the C29 mobility / volume / margin operating leverage bucket. This loop avoids the most repeated C29 symbols and sharpens the split between true volume-cost-margin bridge and OEM/auto-parts theme spikes.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE = 60 rows / 27 symbols / good-bad Stage2 26-13 / 4B-4C 6-0
top covered symbols include 011210(7), 000270(5), 005380(5), 005850(5), 010690(5), 018880(3)
```

Selected rows avoid those repeated combinations:

```text
161390 / Stage2-Actionable / 2024-01-02
003620 / Stage2-Actionable / 2024-01-02
204320 / Stage4B / 2024-06-26
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
| 161390 | atlas/symbol_profiles/161/161390.json | no corporate-action candidate |
| 003620 | atlas/symbol_profiles/003/003620.json | selected 2024 window clean after 2023-04-28 relisting/CA candidate |
| 204320 | atlas/symbol_profiles/204/204320.json | selected 2024 window clean; CA candidate is 2018-05-08 |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R9L88_C29_HANKOOKTIRE_2024_TIRE_MARGIN_BRIDGE_POSITIVE | 161390 | 2024-01-02 | yes | 180 | yes | yes | true |
| R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2 | 003620 | 2024-01-02 | yes | 180 | yes | yes-after-2023-CA | true |
| R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B | 204320 | 2024-06-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | TIRE_MARGIN_BRIDGE | Positive Stage2 requires volume, replacement/OE demand, cost relief, and margin/revision bridge. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | OEM_REBOUND_FALSE_STAGE2 | OEM rebound/turnaround label without volume-mix-cashflow bridge can be weak-MFE high-MAE. |
| C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE | AUTO_PARTS_MOBILITY_EVENT_CAP | Auto-parts/ADAS/mobility premium should route to 4B unless durable bridge is verified. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R9L88_C29_HANKOOKTIRE_2024_TIRE_MARGIN_BRIDGE_POSITIVE | 161390 | 한국타이어앤테크놀로지 | positive | Tire volume/cost margin bridge produced strong 90D MFE with low early MAE. |
| R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2 | 003620 | KG모빌리티 | counterexample | OEM turnaround/rebound watch failed; weak MFE and deep MAE. |
| R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B | 204320 | HL만도 | counterexample / 4B | Auto-parts/mobility premium capped quickly and drew down. |

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
| Hankook Tire margin bridge | historical public/report proxy | true | true | shadow-only positive |
| KG Mobility OEM false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| HL Mando auto-parts event cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 161390 | atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv | atlas/symbol_profiles/161/161390.json |
| 003620 | atlas/ohlcv_tradable_by_symbol_year/003/003620/2024.csv | atlas/symbol_profiles/003/003620.json |
| 204320 | atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv | atlas/symbol_profiles/204/204320.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE | 161390 | Stage2-Actionable | 2024-01-02 | 45350 | positive | tire margin bridge worked |
| R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND | 003620 | Stage2-Actionable | 2024-01-02 | 8740 | counterexample | OEM rebound false Stage2 |
| R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP | 204320 | Stage4B | 2024-06-26 | 45600 | counterexample/4B | auto-parts/mobility event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE | 45350 | 23.04 | -4.63 | 31.42 | -4.63 | 31.42 | -16.54 | 2024-02-23 | 59600 | -36.49 |
| R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND | 8740 | 1.60 | -13.04 | 1.60 | -34.90 | 1.60 | -40.27 | 2024-01-02 | 8880 | -41.22 |
| R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP | 45600 | 1.75 | -15.57 | 1.75 | -30.81 | 1.75 | -32.35 | 2024-06-26 | 46400 | -33.51 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C29 Stage2 needs volume/mix/margin/cashflow bridge |
| local_4b_watch_guard | strengthen: OEM and auto-parts/mobility theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 161390 | good_stage2 | Tire margin bridge produced strong 90D MFE and low early MAE. |
| 003620 | bad_stage2 | OEM rebound label did not produce upside and drew down sharply. |
| 204320 | good_4B | Auto-parts/mobility premium capped with weak forward MFE. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 204320 auto-parts cap | 1.00 | 1.00 | good_full_window_4B_timing_auto_parts_mobility_event_cap |
| 003620 OEM rebound false Stage2 | 0.00 | 0.00 | weak_MFE_high_MAE_false_stage2_OEM_turnaround_without_margin_bridge |
| 161390 tire bridge | n/a | n/a | positive Stage2; later valuation/peak watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 003620 / 204320
```

No hard 4C candidate is proposed. C29 residual here is Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L3/C29 mobility cases, Stage2 requires verified volume, mix, margin, cost, or cashflow bridge. OEM turnaround, ADAS, auto-parts, tire, or mobility label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE
rule = C29 should split tire/parts volume-margin positives from OEM rebound false positives and auto-parts mobility event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 11.59 | -23.45 | 0.67 | mixed; C29 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 11.59 | -23.45 | 0.67 | weaker bridge/theme guard |
| P1 sector_specific_candidate_profile | L3 mobility margin bridge required | 2 | 16.51 | -19.77 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C29 bridge vs event-cap split | 2 | 16.51 | -19.77 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject OEM/theme caps as positive | 1 | 31.42 | -4.63 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 161390 tire margin bridge | 66 | Stage2-Watch | 73 | Stage2-Actionable | 31.42 | -4.63 | tire_volume_cost_margin_bridge_positive |
| 003620 OEM false Stage2 | 65 | Stage2-Actionable | 52 | Stage1/Watch | 1.60 | -34.90 | OEM_turnaround_without_margin_bridge_false_stage2 |
| 204320 auto-parts cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.75 | -30.81 | auto_parts_mobility_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C29 tire margin-bridge positive, OEM rebound false Stage2, and auto-parts mobility event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: tire_margin_bridge_positive, OEM_rebound_false_stage2, auto_parts_mobility_event_cap_4B
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
- C29 mobility volume-margin bridge vs OEM/auto-parts event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,C29_requires_volume_mix_margin_cashflow_bridge,0,"C29 Stage2 should require verified volume/mix/margin/cashflow bridge, not OEM turnaround or mobility-theme label alone","Hankook Tire positive worked; KG Mobility and HL Mando event/rebound rows failed positive-stage promotion","R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE|R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND|R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L3_BATTERY_EV_GREEN_MOBILITY,C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE,configured,cap_OEM_and_auto_parts_theme_premium_as_4B_watch,0,"OEM turnaround and auto-parts/mobility premiums can peak before verified margin and cashflow bridge appears","KG Mobility and HL Mando showed weak MFE90 and high MAE90 after rebound/theme spikes","R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND|R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R9L88_C29_HANKOOKTIRE_2024_TIRE_MARGIN_BRIDGE_POSITIVE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Tire replacement/OE volume and raw-material-cost margin bridge produced strong 90D MFE with low early MAE.", "current_profile_verdict": "current_profile_kept_but_C29_tire_positive_requires_margin_bridge_not_auto_theme_only", "price_source": "Songdaiki/stock-web", "notes": "Source-proxy only; exact as-of margin/revision evidence URL remains pending, so no production weight delta."}
{"row_type": "case", "case_id": "R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "symbol": "003620", "company_name": "KG모빌리티", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "OEM turnaround / volume-recovery watch failed with weak MFE and deep 90D/180D MAE; C29 Stage2 should require margin, mix, and cashflow bridge.", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window is after 2023-04-28 corporate-action/relisting candidate; clean modern tradable window, source-proxy only."}
{"row_type": "case", "case_id": "R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Auto-parts / ADAS / mobility premium capped after the June bounce; weak forward MFE and high MAE support 4B/watch routing.", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Auto parts event-cap counterexample; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE", "case_id": "R9L88_C29_HANKOOKTIRE_2024_TIRE_MARGIN_BRIDGE_POSITIVE", "symbol": "161390", "company_name": "한국타이어앤테크놀로지", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "sector": "mobility_tire", "primary_archetype": "tire_volume_cost_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 45350.0, "evidence_available_at_that_date": "tire volume/replacement demand and raw-material-cost margin bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["replacement_tire_volume", "raw_material_cost_relief", "margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE90", "low_MAE90", "continued_margin_bridge"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_90D_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/161/161390/2024.csv", "profile_path": "atlas/symbol_profiles/161/161390.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 23.04, "MFE_90D_pct": 31.42, "MFE_180D_pct": 31.42, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -4.63, "MAE_90D_pct": -4.63, "MAE_180D_pct": -16.54, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 59600.0, "drawdown_after_peak_pct": -36.49, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_valuation_watch_needed_after_tire_margin_run", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_tire_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L88_C29_161390_2024-01-02_45350", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "case_id": "R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "symbol": "003620", "company_name": "KG모빌리티", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "sector": "OEM_mobility_turnaround", "primary_archetype": "OEM_turnaround_volume_rebound_false_stage2", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-02", "entry_date": "2024-01-02", "entry_price": 8740.0, "evidence_available_at_that_date": "OEM turnaround / sales-volume rebound proxy after restructuring; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["OEM_rebound_watch", "volume_recovery_proxy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE", "deep_MAE", "margin_cashflow_bridge_missing"], "stage4c_evidence_fields": ["turnaround_fade_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003620/2024.csv", "profile_path": "atlas/symbol_profiles/003/003620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.6, "MFE_90D_pct": 1.6, "MFE_180D_pct": 1.6, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.04, "MAE_90D_pct": -34.9, "MAE_180D_pct": -40.27, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-02", "peak_price": 8880.0, "drawdown_after_peak_pct": -41.22, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "weak_MFE_high_MAE_false_stage2_OEM_turnaround_without_margin_bridge", "four_b_evidence_type": ["margin_or_backlog_slowdown", "price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_OEM_rebound_false_positive", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023_relisting_CA", "same_entry_group_id": "R9L88_C29_003620_2024-01-02_8740", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "case_id": "R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "symbol": "204320", "company_name": "HL만도", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "sector": "auto_parts_ADAS_mobility", "primary_archetype": "auto_parts_mobility_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 45600.0, "evidence_available_at_that_date": "auto-parts / ADAS / mobility premium after bounce; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["auto_parts_theme", "ADAS_mobility_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/204/204320/2024.csv", "profile_path": "atlas/symbol_profiles/204/204320.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.75, "MFE_90D_pct": 1.75, "MFE_180D_pct": 1.75, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.57, "MAE_90D_pct": -30.81, "MAE_180D_pct": -32.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 46400.0, "drawdown_after_peak_pct": -33.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_auto_parts_mobility_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R9L88_C29_204320_2024-06-26_45600", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L88_C29_HANKOOKTIRE_2024_TIRE_MARGIN_BRIDGE_POSITIVE", "trigger_id": "R9L88_C29_HANKOOKTIRE_2024_STAGE2_ACTIONABLE_TIRE_MARGIN_BRIDGE", "symbol": "161390", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 45, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 0, "valuation_repricing_score": 50, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "tire_volume_cost_margin_bridge_positive", "MFE_90D_pct": 31.42, "MAE_90D_pct": -4.63, "score_return_alignment_label": "tire_volume_cost_margin_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L88_C29_KGMOBILITY_2024_OEM_REBOUND_FALSE_STAGE2", "trigger_id": "R9L88_C29_KGMOBILITY_2024_STAGE2_FALSE_POSITIVE_OEM_REBOUND", "symbol": "003620", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 65, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "OEM_turnaround_without_margin_bridge_false_stage2", "MFE_90D_pct": 1.6, "MAE_90D_pct": -34.9, "score_return_alignment_label": "OEM_turnaround_without_margin_bridge_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_OEM_rebound_counts_without_volume_mix_margin_cashflow_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R9L88_C29_HLMANDO_2024_AUTO_PARTS_EVENT_CAP_4B", "trigger_id": "R9L88_C29_HLMANDO_2024_STAGE4B_AUTO_PARTS_EVENT_CAP", "symbol": "204320", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 25, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 0, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "auto_parts_mobility_event_cap_4B_guard", "MFE_90D_pct": 1.75, "MAE_90D_pct": -30.81, "score_return_alignment_label": "auto_parts_mobility_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_auto_parts_mobility_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R9", "loop": "88", "large_sector_id": "L3_BATTERY_EV_GREEN_MOBILITY", "canonical_archetype_id": "C29_MOBILITY_VOLUME_MARGIN_OPERATING_LEVERAGE", "fine_archetype_id": "TIRE_MARGIN_BRIDGE_VS_OEM_REBOUND_FALSE_STAGE2_AND_PARTS_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["tire_margin_bridge_positive", "OEM_rebound_false_stage2", "auto_parts_mobility_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
completed_loop = 88
next_round = R10
next_loop = 88
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
