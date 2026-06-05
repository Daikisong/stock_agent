# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R11
scheduled_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R11_loop_87_L10_POLICY_EVENT_CROSS_REDTEAM_MISC_C31_POLICY_SUBSIDY_LEGISLATION_EVENT_research.md
```

This loop adds 3 new independent C31 cases, 2 counterexamples, and 2 current-profile residual errors for R11 / L10 / C31.

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
scheduled_round = R11
scheduled_loop = 87
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
round_sector_consistency = pass
computed_next_round = R12
computed_next_loop = 87
```

R11 is the L10 policy/event round. This loop compresses C31 policy cases into a simple rule: policy subsidy is not enough; the bridge must show order, revenue, utilization, margin, or cashflow conversion. If that bridge is absent, the event premium belongs in Stage2-watch or 4B overlay.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

C31 already has wide symbol coverage, but the selected combination adds a focused IRA / wind / solar / hydrogen split with symbols not listed among the highest-repeat C31 combinations in the No-Repeat snapshot:

```text
112610 / Stage2-Actionable / 2022-08-16
336260 / Stage2-Actionable / 2022-08-11
009830 / Stage4B / 2023-03-31
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

| symbol | profile path | corporate-action status for selected window |
|---|---|---|
| 112610 | atlas/symbol_profiles/112/112610.json | CA candidates are 2021 only; 2022 window clean |
| 336260 | atlas/symbol_profiles/336/336260.json | no corporate-action candidate |
| 009830 | atlas/symbol_profiles/009/009830.json | listed CA candidates are 1999/2008; selected post-2023 structure window treated separately |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R11L87_C31_CSWIND_2022_IRA_ORDER_CASHFLOW_POSITIVE | 112610 | 2022-08-16 | yes | 180 | yes | yes | true |
| R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2 | 336260 | 2022-08-11 | yes | 180 | yes | yes | true |
| R11L87_C31_HSOL_2023_SOLAR_CAPEX_EVENT_CAP_4B | 009830 | 2023-03-31 | yes | 180 | yes | clean-post-restructure | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | IRA_WIND_ORDER_CASHFLOW | Policy event can be positive only when orders/revenue/cashflow conversion is visible. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | HYDROGEN_POLICY_FALSE_STAGE2 | Hydrogen/subsidy headline alone produces high-MAE false positives. |
| C31_POLICY_SUBSIDY_LEGISLATION_EVENT | SOLAR_CAPEX_EVENT_CAP_4B | Solar/manufacturing subsidy + capex premium can be a 4B event cap, not structural Green. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R11L87_C31_CSWIND_2022_IRA_ORDER_CASHFLOW_POSITIVE | 112610 | 씨에스윈드 | positive | Policy-to-order bridge produced positive 90D/180D MFE. |
| R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2 | 336260 | 두산퓨얼셀 | counterexample | Policy spike failed with high MAE. |
| R11L87_C31_HSOL_2023_SOLAR_CAPEX_EVENT_CAP_4B | 009830 | 한화솔루션 | counterexample / 4B | Policy/capex premium peaked early and then drew down. |

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
| CSWind IRA/order bridge | historical public/report proxy | true | true | shadow-only positive |
| Doosan FuelCell hydrogen policy | historical public/report proxy | true | true | shadow-only counterexample |
| Hanwha Solutions solar/capex event | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 112610 | atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv; 2023.csv | atlas/symbol_profiles/112/112610.json |
| 336260 | atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv; 2023.csv | atlas/symbol_profiles/336/336260.json |
| 009830 | atlas/ohlcv_tradable_by_symbol_year/009/009830/2023.csv | atlas/symbol_profiles/009/009830.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW | 112610 | Stage2-Actionable | 2022-08-16 | 65100 | positive | policy-to-order bridge worked |
| R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY | 336260 | Stage2-Actionable | 2022-08-11 | 40350 | counterexample | policy headline false positive |
| R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP | 009830 | Stage4B | 2023-03-31 | 53700 | counterexample/4B | policy/capex event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW | 65100 | 9.06 | -7.83 | 23.66 | -12.90 | 23.66 | -12.90 | 2022-11-28 | 80500 | -15.03 |
| R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY | 40350 | 2.23 | -16.98 | 2.23 | -30.86 | 2.23 | -39.28 | 2022-08-16 | 41250 | -41.45 |
| R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP | 53700 | 6.15 | -17.13 | 6.15 | -29.24 | 6.15 | -49.72 | 2023-03-31 | 57000 | -52.89 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C31 policy requires order/revenue/cashflow conversion |
| local_4b_watch_guard | strengthen: policy/capex event premium should be 4B watch/cap |
| full_4b_requires_non_price_evidence | keep |
| hard_4c_thesis_break_routes_to_4c | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2 policy-quality:

| symbol | Stage2 quality | explanation |
|---|---|---|
| 112610 | good_stage2 | Policy converted toward order/cashflow route; MFE positive. |
| 336260 | bad_stage2 | Policy theme alone produced poor follow-through and high MAE. |
| 009830 | not positive Stage2 | Policy/capex premium behaved like event-cap 4B. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 009830 solar/capex event | 1.00 | 1.00 | good_full_window_4B_timing_policy_event_premium_cap |
| 336260 hydrogen policy spike | 0.00 | 0.00 | policy theme spike was not order conversion |
| 112610 wind order bridge | n/a | n/a | positive Stage2; later valuation watch only |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 009830
```

No hard 4C candidate is proposed. This loop is about policy/event premium cap and Stage2 bridge quality.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L10 policy/subsidy cases, Stage2 requires a verified conversion bridge: order, revenue, utilization, margin, or cashflow. Policy headline or subsidy language alone remains watch-only.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
rule = C31 should split policy events into conversion-positive cases and event-premium-cap cases. Capex-heavy subsidy stories without margin/cashflow evidence route to 4B watch.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 10.68 | -24.33 | 0.67 | mixed, policy bridge needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 10.68 | -24.33 | 0.67 | weaker event-premium cap |
| P1 sector_specific_candidate_profile | L10 conversion bridge required | 2 | 12.95 | -21.88 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C31 conversion vs event cap split | 2 | 12.95 | -21.88 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject policy headline and capex premium as positive | 1 | 23.66 | -12.90 | 0.00 | safest but evidence URL blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 112610 wind/IRA | 66 | Stage2-Watch | 72 | Stage2-Actionable | 23.66 | -12.90 | policy_to_order_cashflow_positive |
| 336260 hydrogen | 67 | Stage2-Actionable | 53 | Stage1/Watch | 2.23 | -30.86 | policy_headline_false_positive |
| 009830 solar/capex | 70 | Stage3-Yellow-like | 56 | Stage4B-watch | 6.15 | -29.24 | policy_capex_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C31 IRA/wind positive, hydrogen-policy false Stage2, and solar-capex event-cap 4B split."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, full_4b_requires_non_price_evidence
residual_error_types_found: policy_headline_false_stage2, policy_capex_event_premium_cap, policy_to_order_cashflow_positive_exception
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
- C31 policy conversion vs policy headline vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,policy_requires_cashflow_conversion_bridge,0,"C31 Stage2 should require order/revenue/cashflow conversion, not policy headline alone","CSWind worked; Doosan FuelCell failed","R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW|R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY",2,2,1,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,configured,cap_policy_capex_event_premium_as_4B_watch,0,"Policy/capex event premiums can be early local/full peaks when cashflow conversion is missing","Hanwha Solutions 2023 peaked at trigger and drew down sharply","R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP",1,1,1,low,guardrail_shadow_only,"event premium belongs in 4B overlay calibration"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "symbol_count": 5414}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R11L87_C31_CSWIND_2022_IRA_ORDER_CASHFLOW_POSITIVE", "symbol": "112610", "company_name": "씨에스윈드", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Policy tailwind worked only where wind-tower order/cashflow conversion was visible; 90D MFE and 180D MFE were positive with moderate MAE.", "current_profile_verdict": "current_profile_kept_but_C31_should_require_order_cashflow_conversion_not_policy_headline_only", "price_source": "Songdaiki/stock-web", "notes": "Historical policy/order conversion proxy; exact as-of URL verification remains pending, so no production delta."}
{"row_type": "case", "case_id": "R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Hydrogen policy/event spike had almost no follow-through and high MAE; policy headline alone should not receive Stage2 bonus.", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_revenue_order_bridge", "price_source": "Songdaiki/stock-web", "notes": "Counterexample for hydrogen-policy event without durable revenue/order conversion."}
{"row_type": "case", "case_id": "R11L87_C31_HSOL_2023_SOLAR_CAPEX_EVENT_CAP_4B", "symbol": "009830", "company_name": "한화솔루션", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Solar/IRA manufacturing-policy premium peaked early and then drew down sharply; capex/subsidy headline should route to 4B watch unless margin/cashflow conversion is verified.", "current_profile_verdict": "current_profile_4B_too_late_if_policy_capex_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Post-2023 corporate-structure price window used; exact event URL pending, so shadow-only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW", "case_id": "R11L87_C31_CSWIND_2022_IRA_ORDER_CASHFLOW_POSITIVE", "symbol": "112610", "company_name": "씨에스윈드", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "sector": "policy_wind_renewables", "primary_archetype": "IRA_wind_order_cashflow_conversion", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-16", "entry_date": "2022-08-16", "entry_price": 65100.0, "evidence_available_at_that_date": "IRA/wind policy tailwind plus tower order-conversion proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["policy_subsidy_tailwind", "order_conversion_proxy", "customer_project_visibility", "relative_strength"], "stage3_evidence_fields": ["90D_MFE_positive", "policy_to_order_bridge"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_policy_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/112/112610/2022.csv|atlas/ohlcv_tradable_by_symbol_year/112/112610/2023.csv", "profile_path": "atlas/symbol_profiles/112/112610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.06, "MFE_90D_pct": 23.66, "MFE_180D_pct": 23.66, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -7.83, "MAE_90D_pct": -12.9, "MAE_180D_pct": -12.9, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-11-28", "peak_price": 80500.0, "drawdown_after_peak_pct": -15.03, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "policy_positive_but_needs_order_cashflow_bridge", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_policy_to_order_conversion", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L87_C31_CSWIND_2022_2022-08-16_65100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "case_id": "R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "symbol": "336260", "company_name": "두산퓨얼셀", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "sector": "policy_hydrogen_fuelcell", "primary_archetype": "hydrogen_policy_without_order_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-08-11", "entry_date": "2022-08-11", "entry_price": 40350.0, "evidence_available_at_that_date": "hydrogen policy / fuel-cell thematic event proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["hydrogen_policy_headline", "theme_relative_strength", "subsidy_expectation"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_follow_through", "policy_to_revenue_gap", "high_MAE"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/336/336260/2022.csv|atlas/ohlcv_tradable_by_symbol_year/336/336260/2023.csv", "profile_path": "atlas/symbol_profiles/336/336260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.23, "MFE_90D_pct": 2.23, "MFE_180D_pct": 2.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -16.98, "MAE_90D_pct": -30.86, "MAE_180D_pct": -39.28, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-08-16", "peak_price": 41250.0, "drawdown_after_peak_pct": -41.45, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.0, "four_b_full_window_peak_proximity": 0.0, "four_b_timing_verdict": "policy_theme_spike_was_not_order_conversion", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "bad_stage2_policy_headline_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R11L87_C31_DSFUEL_2022_2022-08-11_40350", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP", "case_id": "R11L87_C31_HSOL_2023_SOLAR_CAPEX_EVENT_CAP_4B", "symbol": "009830", "company_name": "한화솔루션", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "sector": "policy_solar_manufacturing", "primary_archetype": "solar_policy_capex_event_cap_4b", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2023-03-31", "entry_date": "2023-03-31", "entry_price": 53700.0, "evidence_available_at_that_date": "solar/IRA manufacturing capacity policy and capex-premium proxy after post-structure price window", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["IRA_solar_policy", "manufacturing_capacity_policy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["capex_burden", "policy_premium_cap", "margin_conversion_gap", "post_peak_drawdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/009/009830/2023.csv", "profile_path": "atlas/symbol_profiles/009/009830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 6.15, "MFE_90D_pct": 6.15, "MFE_180D_pct": 6.15, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -17.13, "MAE_90D_pct": -29.24, "MAE_180D_pct": -49.72, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-31", "peak_price": 57000.0, "drawdown_after_peak_pct": -52.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_policy_event_premium_cap", "four_b_evidence_type": ["valuation_blowoff", "capital_raise_or_overhang", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "policy_capex_event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_policy_capex_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_post_restructure_180D_window", "same_entry_group_id": "R11L87_C31_HSOL_2023_2023-03-31_53700", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L87_C31_CSWIND_2022_IRA_ORDER_CASHFLOW_POSITIVE", "trigger_id": "R11L87_C31_CSWIND_2022_STAGE2_ACTIONABLE_IRA_ORDER_CASHFLOW", "symbol": "112610", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 45, "margin_bridge_score": 35, "revision_score": 45, "relative_strength_score": 55, "customer_quality_score": 20, "policy_or_regulatory_score": 75, "valuation_repricing_score": 45, "execution_risk_score": 35, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 45, "backlog_visibility_score": 55, "margin_bridge_score": 45, "revision_score": 50, "relative_strength_score": 55, "customer_quality_score": 20, "policy_or_regulatory_score": 70, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "policy_to_order_cashflow_positive", "MFE_90D_pct": 23.66, "MAE_90D_pct": -12.9, "score_return_alignment_label": "policy_to_order_cashflow_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L87_C31_DSFUEL_2022_HYDROGEN_POLICY_FALSE_STAGE2", "trigger_id": "R11L87_C31_DSFUEL_2022_STAGE2_FALSE_POSITIVE_HYDROGEN_POLICY", "symbol": "336260", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 65, "customer_quality_score": 5, "policy_or_regulatory_score": 80, "valuation_repricing_score": 55, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "customer_quality_score": 5, "policy_or_regulatory_score": 55, "valuation_repricing_score": 35, "execution_risk_score": 75, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "policy_headline_false_positive", "MFE_90D_pct": 2.23, "MAE_90D_pct": -30.86, "score_return_alignment_label": "policy_headline_false_positive", "current_profile_verdict": "current_profile_false_positive_if_policy_score_counts_without_order_revenue_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R11L87_C31_HSOL_2023_SOLAR_CAPEX_EVENT_CAP_4B", "trigger_id": "R11L87_C31_HSOL_2023_STAGE4B_SOLAR_POLICY_CAPEX_EVENT_CAP", "symbol": "009830", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 10, "revision_score": 25, "relative_strength_score": 75, "customer_quality_score": 10, "policy_or_regulatory_score": 80, "valuation_repricing_score": 65, "execution_risk_score": 55, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 20, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 5, "revision_score": 20, "relative_strength_score": 35, "customer_quality_score": 10, "policy_or_regulatory_score": 60, "valuation_repricing_score": 40, "execution_risk_score": 75, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 30, "accounting_trust_risk_score": 0}, "weighted_score_after": 56, "stage_label_after": "Stage4B-watch", "changed_components": ["policy_or_regulatory_score", "margin_bridge_score", "relative_strength_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "policy_capex_event_cap_4B_guard", "MFE_90D_pct": 6.15, "MAE_90D_pct": -29.24, "score_return_alignment_label": "policy_capex_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_policy_capex_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R11", "loop": "87", "large_sector_id": "L10_POLICY_EVENT_CROSS_REDTEAM_MISC", "canonical_archetype_id": "C31_POLICY_SUBSIDY_LEGISLATION_EVENT", "fine_archetype_id": "IRA_WIND_SOLAR_HYDROGEN_POLICY_CASHFLOW_CONVERSION_VS_EVENT_PREMIUM_FADE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["policy_headline_false_stage2", "policy_capex_event_premium_cap", "policy_to_order_cashflow_positive_exception"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 87
next_round = R12
next_loop = 87
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
