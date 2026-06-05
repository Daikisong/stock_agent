# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R1
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
fine_archetype_id = GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R1_loop_89_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
```

This loop starts loop 89 after R13 loop 88. It adds 3 C02 power-grid / data-center CAPEX cases: one grid/cable order-margin positive, one breaker-equipment high-MAE false Stage2, and one subsea-cable 4B event-cap counterexample.

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
scheduled_loop = 89
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
round_sector_consistency = pass
computed_next_round = R2
computed_next_loop = 89
```

R1 permits L1 industrial / infrastructure / defense / grid research. The previous R1 loop used C05, so this loop moves to C02 and focuses on power-grid / data-center CAPEX residuals.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C02_POWER_GRID_DATACENTER_CAPEX = 22 rows / 12 symbols / good-bad Stage2 11-4 / 4B-4C 2-0
top covered symbols include 000500(3), 006340(3), 033100(3), 001440(2), 017040(2), 189860(2)
previous R1 loop-88 C05 symbols avoided: 028050, 053690, 045100
```

Selected rows avoid those repeated combinations:

```text
103590 / Stage2-Actionable / 2024-02-14
199820 / Stage2-Actionable / 2024-06-28
060370 / Stage4B / 2024-07-10
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
| 103590 | atlas/symbol_profiles/103/103590.json | 2024-02-13 CA candidate blocked; selected 2024-02-14 post-CA entry |
| 199820 | atlas/symbol_profiles/199/199820.json | 2024-05-21 / 2024-06-11 CA candidates blocked; selected 2024-06-28 post-CA entry |
| 060370 | atlas/symbol_profiles/060/060370.json | 2025-08-28 CA candidate outside 180D window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE | 103590 | 2024-02-14 | yes | 180 | yes | post-CA clean | true |
| R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2 | 199820 | 2024-06-28 | yes | 180 | yes | post-CA clean | true |
| R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B | 060370 | 2024-07-10 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C02_POWER_GRID_DATACENTER_CAPEX | GRID_CABLE_ORDER_MARGIN_BRIDGE | Positive Stage2 requires orderbook, capacity, customer/lead-time, and margin bridge. |
| C02_POWER_GRID_DATACENTER_CAPEX | BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2 | Electrical-equipment label without bridge can suffer high-MAE timing failure. |
| C02_POWER_GRID_DATACENTER_CAPEX | SUBSEA_CABLE_EVENT_CAP_4B | Cable/offshore-grid premium can be capped and should route to 4B/watch if bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE | 103590 | 일진전기 | positive | Post-CA grid/cable order-margin path produced very high MFE. |
| R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2 | 199820 | 제일일렉트릭 | counterexample | Initial post-CA theme Stage2 suffered -43% MAE before later recovery. |
| R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B | 060370 | LS마린솔루션 | counterexample / 4B | Subsea-cable theme premium capped and then drew down deeply. |

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
| ILJIN Electric grid/cable bridge | historical public/report proxy | true | true | shadow-only positive |
| Jeil Electric breaker theme | historical public/news proxy | true | true | high-MAE false Stage2 guardrail |
| LS Marine subsea cable cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 103590 | atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv | atlas/symbol_profiles/103/103590.json |
| 199820 | atlas/ohlcv_tradable_by_symbol_year/199/199820/2024.csv; 2025.csv | atlas/symbol_profiles/199/199820.json |
| 060370 | atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv; 2025.csv | atlas/symbol_profiles/060/060370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE | 103590 | Stage2-Actionable | 2024-02-14 | 11780 | positive | grid/cable order-margin bridge worked |
| R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE | 199820 | Stage2-Actionable | 2024-06-28 | 10050 | counterexample | breaker theme high-MAE false initial Stage2 |
| R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP | 060370 | Stage4B | 2024-07-10 | 22700 | counterexample/4B | subsea-cable event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE | 11780 | 90.15 | -12.48 | 156.79 | -12.48 | 156.79 | -12.48 | 2024-05-29 | 30250 | -31.07 |
| R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE | 10050 | 7.86 | -43.28 | 9.45 | -43.28 | 50.45 | -43.28 | 2025-01-17 | 15120 | -38.03 |
| R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP | 22700 | 9.47 | -32.56 | 9.47 | -32.56 | 9.47 | -42.91 | 2024-07-11 | 24850 | -47.85 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C02 Stage2 needs orderbook / margin / capacity / customer bridge |
| local_4b_watch_guard | strengthen: breaker and subsea cable theme premiums should route to 4B watch |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 103590 | good_stage2 | Post-CA grid/cable order-margin bridge produced very high MFE. |
| 199820 | bad_initial_stage2 | First post-CA breaker-theme entry had unacceptable MAE before later retrigger recovery. |
| 060370 | good_4B | Subsea/offshore-grid event premium capped and drew down. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 060370 subsea cable cap | 1.00 | 1.00 | good_full_window_4B_timing_subsea_cable_event_cap |
| 199820 breaker theme | 0.07 | 0.50 | high_MAE_false_initial_stage2_even_though_later_retrigger_recovered |
| 103590 grid/cable bridge | n/a | n/a | positive Stage2; later grid valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 199820 / 060370
```

No hard 4C candidate is proposed. R1 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L1 power-grid/data-center CAPEX cases, Stage2 requires verified orderbook, backlog quality, capacity/lead-time constraint, customer quality, and margin/revision bridge. Grid, cable, breaker, offshore, or data-center label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C02_POWER_GRID_DATACENTER_CAPEX
rule = C02 should split order/margin/CAPA bridge positives from breaker-equipment high-MAE theme entries and subsea-cable event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 58.57 | -29.44 | 0.67 | mixed; C02 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 58.57 | -29.44 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L1 grid bridge required | 2 | 83.12 | -27.88 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C02 bridge vs event-cap split | 2 | 83.12 | -27.88 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing grid themes as positive | 1 | 156.79 | -12.48 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 103590 grid/cable bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 156.79 | -12.48 | grid_cable_order_margin_capacity_positive |
| 199820 breaker theme | 66 | Stage2-Actionable | 54 | Stage1/Watch | 9.45 | -43.28 | breaker_theme_high_MAE_false_initial_stage2 |
| 060370 subsea cable cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 9.47 | -32.56 | subsea_cable_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C02 grid/cable order-margin positive, breaker theme high-MAE false Stage2, and subsea cable event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: grid_cable_order_margin_positive, breaker_theme_high_MAE_false_stage2, subsea_cable_event_cap_4B
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
- C02 grid/data-center CAPEX order-bridge vs theme event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,C02_requires_order_margin_capacity_bridge,0,"C02 Stage2 should require verified orderbook, margin, capacity, lead-time, or customer bridge, not grid/electrical-equipment label alone","ILJIN Electric positive worked; Jeil Electric and LS Marine event/theme rows failed positive-stage promotion or suffered high MAE","R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE|R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE|R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C02_POWER_GRID_DATACENTER_CAPEX,configured,cap_grid_theme_and_subsea_cable_premiums_as_4B_watch,0,"Breaker/electrical-equipment and subsea cable premiums can peak or draw down before durable order/margin bridge appears","Jeil Electric showed high-MAE initial Stage2; LS Marine showed full-window event-cap behavior","R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE|R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Post-CA grid/cable order bridge produced very high 30D/90D/180D MFE, validating C02 only when order/margin/CAPA bridge is visible.", "current_profile_verdict": "current_profile_kept_but_C02_positive_requires_order_margin_capacity_bridge_not_grid_label_only", "price_source": "Songdaiki/stock-web", "notes": "Entry is 2024-02-14, one trading day after 2024-02-13 corporate-action candidate; exact as-of order/margin evidence URLs remain pending."}
{"row_type": "case", "case_id": "R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2", "symbol": "199820", "company_name": "제일일렉트릭", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Selected post-2024-06-11 corporate-action candidate window only.", "independent_evidence_weight": 0.5, "score_price_alignment": "Breaker/electrical-equipment theme spike had severe 30D/90D MAE before later partial recovery; C02 Stage2 timing needs bridge confirmation rather than first theme spike.", "current_profile_verdict": "current_profile_false_positive_if_breaker_theme_counts_without_order_margin_bridge", "price_source": "Songdaiki/stock-web", "notes": "Reduced weight because later recovery existed, but initial high-MAE path is a useful Stage2 timing guardrail."}
{"row_type": "case", "case_id": "R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B", "symbol": "060370", "company_name": "LS마린솔루션", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Subsea cable / offshore grid premium peaked quickly and then drew down deeply; theme premium should route to 4B unless contract/CAPA/margin bridge is verified.", "current_profile_verdict": "current_profile_4B_too_late_if_subsea_cable_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "2025-08-28 CA candidate is outside the selected 180D window; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE", "case_id": "R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE", "symbol": "103590", "company_name": "일진전기", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "sector": "power_grid_cable_transformer", "primary_archetype": "grid_cable_order_margin_capacity_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-13", "entry_date": "2024-02-14", "entry_price": 11780.0, "evidence_available_at_that_date": "grid/cable orderbook, power-equipment capacity and margin bridge proxy; exact as-of URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["grid_cable_orderbook_proxy", "transformer_or_power_equipment_capacity", "margin_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["very_high_MFE30", "very_high_MFE90", "order_margin_capacity_path"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_grid_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/103/103590/2024.csv", "profile_path": "atlas/symbol_profiles/103/103590.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 90.15, "MFE_90D_pct": 156.79, "MFE_180D_pct": 156.79, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -12.48, "MAE_90D_pct": -12.48, "MAE_180D_pct": -12.48, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-29", "peak_price": 30250.0, "drawdown_after_peak_pct": -31.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_grid_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_grid_cable_order_margin_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-02-13_CA_window", "same_entry_group_id": "R1L89_C02_103590_2024-02-14_11780", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE", "case_id": "R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2", "symbol": "199820", "company_name": "제일일렉트릭", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "sector": "breaker_low_voltage_equipment", "primary_archetype": "breaker_theme_spike_without_order_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-28", "entry_date": "2024-06-28", "entry_price": 10050.0, "evidence_available_at_that_date": "breaker/electrical-equipment theme and grid CAPEX proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["breaker_equipment_theme", "grid_CAPEX_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["high_MAE_before_recovery", "order_margin_bridge_missing", "event_spike"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/199/199820/2024.csv|atlas/ohlcv_tradable_by_symbol_year/199/199820/2025.csv", "profile_path": "atlas/symbol_profiles/199/199820.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.86, "MFE_90D_pct": 9.45, "MFE_180D_pct": 50.45, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -43.28, "MAE_90D_pct": -43.28, "MAE_180D_pct": -43.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-17", "peak_price": 15120.0, "drawdown_after_peak_pct": -38.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.07, "four_b_full_window_peak_proximity": 0.5, "four_b_timing_verdict": "high_MAE_false_initial_stage2_even_though_later_retrigger_recovered", "four_b_evidence_type": ["price_only", "positioning_overheat", "order_margin_bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_initial_stage2_high_MAE_breaker_theme_without_bridge", "current_profile_verdict": "current_profile_false_positive_if_breaker_theme_counts_without_order_margin_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_2024-06-11_CA_window", "same_entry_group_id": "R1L89_C02_199820_2024-06-28_10050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "post-CA row only; 2024-05-21 and 2024-06-11 corporate-action candidates blocked from entry selection", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP", "case_id": "R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B", "symbol": "060370", "company_name": "LS마린솔루션", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "sector": "subsea_cable_offshore_grid", "primary_archetype": "subsea_cable_offshore_grid_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-07-10", "entry_date": "2024-07-10", "entry_price": 22700.0, "evidence_available_at_that_date": "subsea cable / offshore grid premium after July spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["subsea_cable_theme", "offshore_grid_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/060/060370/2024.csv|atlas/ohlcv_tradable_by_symbol_year/060/060370/2025.csv", "profile_path": "atlas/symbol_profiles/060/060370.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.47, "MFE_90D_pct": 9.47, "MFE_180D_pct": 9.47, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -32.56, "MAE_90D_pct": -32.56, "MAE_180D_pct": -42.91, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 24850.0, "drawdown_after_peak_pct": -47.85, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_subsea_cable_event_cap", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_subsea_cable_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R1L89_C02_060370_2024-07-10_22700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L89_C02_ILJIN_2024_GRID_CABLE_ORDER_MARGIN_POSITIVE", "trigger_id": "R1L89_C02_ILJIN_2024_STAGE2_ACTIONABLE_GRID_ORDER_MARGIN_BRIDGE", "symbol": "103590", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 60, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "grid_cable_order_margin_capacity_positive", "MFE_90D_pct": 156.79, "MAE_90D_pct": -12.48, "score_return_alignment_label": "grid_cable_order_margin_capacity_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L89_C02_JEIL_2024_BREAKER_EQUIPMENT_HIGH_MAE_FALSE_STAGE2", "trigger_id": "R1L89_C02_JEIL_2024_STAGE2_FALSE_POSITIVE_BREAKER_THEME_HIGH_MAE", "symbol": "199820", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 20, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage1/Watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "breaker_theme_high_MAE_false_initial_stage2", "MFE_90D_pct": 9.45, "MAE_90D_pct": -43.28, "score_return_alignment_label": "breaker_theme_high_MAE_false_initial_stage2", "current_profile_verdict": "current_profile_false_positive_if_breaker_theme_counts_without_order_margin_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L89_C02_LSMARINE_2024_SUBSEA_CABLE_EVENT_CAP_4B", "trigger_id": "R1L89_C02_LSMARINE_2024_STAGE4B_SUBSEA_CABLE_EVENT_CAP", "symbol": "060370", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 30, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 15, "policy_or_regulatory_score": 20, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "subsea_cable_event_cap_4B_guard", "MFE_90D_pct": 9.47, "MAE_90D_pct": -32.56, "score_return_alignment_label": "subsea_cable_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_subsea_cable_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R1", "loop": "89", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C02_POWER_GRID_DATACENTER_CAPEX", "fine_archetype_id": "GRID_CABLE_TRANSFORMER_ORDER_BRIDGE_VS_SUBSEA_AND_BREAKER_THEME_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["grid_cable_order_margin_positive", "breaker_theme_high_MAE_false_stage2", "subsea_cable_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C02_POWER_GRID_DATACENTER_CAPEX","reason":"all selected rows have usable 180D stock-web windows; entries were shifted after corporate-action candidates where needed","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 89
next_round = R2
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
