# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_89_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

This loop continues loop 89 after R5. It adds 3 C22 insurance rate/reserve cases: one life-insurance rate/value-up bridge positive, one non-life reserve-risk false Stage2, and one large-cap life-insurance 4B event-cap counterexample.

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
scheduled_round = R6
scheduled_loop = 89
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 89
```

R6 permits L6 financial / capital return / digital finance research. Previous R6 loop-88 used C21, so this loop moves to C22 and tests whether insurance rate/value-up rallies are backed by ROE, reserve, loss-ratio, capital-return, or CSM-style bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE = 37 rows / 12 symbols / good-bad Stage2 10-11 / 4B-4C 2-0
top covered symbols include 000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
previous R6 loop-88 C21 symbols avoided: 086790, 024110, 003530
```

Selected rows avoid those repeated combinations:

```text
088350 / Stage2-Actionable / 2024-01-23
001450 / Stage2-Actionable / 2024-02-01
032830 / Stage4B / 2024-02-28
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
| 088350 | atlas/symbol_profiles/088/088350.json | no corporate-action candidate |
| 001450 | atlas/symbol_profiles/001/001450.json | selected 2024 window clean; CA candidate is 2004-07-13 |
| 032830 | atlas/symbol_profiles/032/032830.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L89_C22_HANWHALIFE_2024_RATE_VALUEUP_BRIDGE_POSITIVE | 088350 | 2024-01-23 | yes | 180 | yes | yes | true |
| R6L89_C22_HYUNDAIMARINE_2024_RESERVE_RISK_FALSE_STAGE2 | 001450 | 2024-02-01 | yes | 180 | yes | yes | true |
| R6L89_C22_SAMSUNGLIFE_2024_LIFE_VALUEUP_EVENT_CAP_4B | 032830 | 2024-02-28 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_INSURANCE_RATE_VALUEUP_BRIDGE | Positive Stage2 requires rate cycle, ROE/PBR, capital-return, CSM, or reserve-release bridge. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | NONLIFE_RESERVE_RISK_FALSE_STAGE2 | Non-life rate/value-up theme can fail if loss-ratio or reserve risk offsets the capital-return story. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_VALUEUP_EVENT_CAP_4B | Large-cap life-insurance value-up premium should route to 4B when event premium matures. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L89_C22_HANWHALIFE_2024_RATE_VALUEUP_BRIDGE_POSITIVE | 088350 | 한화생명 | positive | Rate/value-up bridge produced high MFE with controlled early MAE. |
| R6L89_C22_HYUNDAIMARINE_2024_RESERVE_RISK_FALSE_STAGE2 | 001450 | 현대해상 | counterexample | Non-life rate theme had weak MFE and reserve/loss-ratio risk-like drawdown. |
| R6L89_C22_SAMSUNGLIFE_2024_LIFE_VALUEUP_EVENT_CAP_4B | 032830 | 삼성생명 | counterexample / 4B | Life-insurance value-up premium capped after late-February spike. |

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
| Hanwha Life rate/value-up bridge | historical public/report proxy | true | true | shadow-only positive |
| Hyundai Marine reserve-risk false Stage2 | historical public/report proxy | true | true | false-Stage2 guardrail |
| Samsung Life value-up cap | historical public/report proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 088350 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json |
| 001450 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json |
| 032830 | atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv | atlas/symbol_profiles/032/032830.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE | 088350 | Stage2-Actionable | 2024-01-23 | 2620 | positive | life-insurance rate/value-up bridge worked |
| R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE | 001450 | Stage2-Actionable | 2024-02-01 | 35450 | counterexample | non-life reserve-risk false Stage2 |
| R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP | 032830 | Stage4B | 2024-02-28 | 102900 | counterexample/4B | life-insurance value-up event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE | 2620 | 45.61 | -5.53 | 45.61 | -5.53 | 45.61 | -5.53 | 2024-02-13 | 3815 | -29.23 |
| R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE | 35450 | 3.81 | -13.68 | 3.81 | -14.53 | 3.81 | -14.53 | 2024-02-05 | 36800 | -17.66 |
| R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP | 102900 | 5.44 | -21.96 | 5.44 | -25.56 | 5.44 | -25.56 | 2024-03-08 | 108500 | -29.40 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C22 Stage2 needs rate-to-ROE/capital-return/reserve bridge |
| local_4b_watch_guard | strengthen: insurance value-up/rate premium should route to 4B when reserve/capital bridge is not durable |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is Stage2/4B quality:

| symbol | stage quality | explanation |
|---|---|---|
| 088350 | good_stage2 | Rate/value-up bridge created high MFE with controlled early drawdown. |
| 001450 | bad_stage2 | Non-life reserve/loss-ratio risk offset the rate/value-up theme. |
| 032830 | good_4B | Life-insurance value-up premium capped after the local peak. |

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 001450 non-life reserve false Stage2 | 0.04 | 0.04 | nonlife_rate_theme_false_stage2_due_reserve_risk_and_weak_MFE |
| 032830 life value-up cap | 0.95 | 0.95 | good_event_cap_4B_timing_life_insurance_valueup_premium |
| 088350 rate/value-up bridge | n/a | n/a | positive Stage2, but later valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 001450 / 032830
```

No hard 4C candidate is proposed. R6 loop 89 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 insurance cases, Stage2 requires rate-cycle to ROE/PBR, capital-return, reserve release, CSM, loss-ratio improvement, or revision bridge. Insurance/value-up/rate label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
rule = C22 should split life-insurance rate/value-up positives from non-life reserve-risk false Stage2 and life-insurance event-cap rows. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 18.29 | -15.21 | 0.67 | mixed; C22 split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 18.29 | -15.21 | 0.67 | weaker reserve/event-cap guard |
| P1 sector_specific_candidate_profile | L6 insurance bridge required | 2 | 24.71 | -10.03 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C22 bridge vs event-cap split | 2 | 24.71 | -10.03 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing insurance themes as positive | 1 | 45.61 | -5.53 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 088350 rate/value-up bridge | 66 | Stage2-Watch | 74 | Stage2-Actionable | 45.61 | -5.53 | life_insurance_rate_valueup_bridge_positive |
| 001450 reserve false Stage2 | 66 | Stage2-Actionable | 55 | Stage1/Watch | 3.81 | -14.53 | nonlife_reserve_risk_false_stage2 |
| 032830 life value-up cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 5.44 | -25.56 | life_valueup_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C22 life-insurance rate/value-up positive, non-life reserve-risk false Stage2, and large-cap life-insurance value-up event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: life_insurance_rate_valueup_bridge_positive, nonlife_reserve_risk_false_stage2, life_valueup_event_cap_4B
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
- C22 insurance rate-cycle reserve bridge vs event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,C22_requires_rate_ROE_capital_return_or_reserve_bridge,0,"C22 Stage2 should require rate-cycle to ROE/PBR/capital-return/reserve or loss-ratio bridge, not insurance or value-up label alone","Hanwha Life positive worked; Hyundai Marine and Samsung Life event/reserve rows failed positive-stage promotion","R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE|R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE|R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,cap_insurance_valueup_and_reserve_premiums_as_4B_watch,0,"Insurance value-up/rate premiums can peak before reserve, loss-ratio, or capital-return bridge is durable","Samsung Life and Hyundai Marine showed weak MFE90 and material MAE90 after event spikes","R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE|R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP",2,2,2,low,guardrail_shadow_only,"4B overlay only; not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L89_C22_HANWHALIFE_2024_RATE_VALUEUP_BRIDGE_POSITIVE", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Life-insurance rate/value-up/capital-return bridge produced high 30D/90D MFE with controlled early MAE; C22 works when rate cycle and capital policy map into ROE/PBR or reserve-release visibility.", "current_profile_verdict": "current_profile_kept_but_C22_positive_requires_rate_ROE_capital_return_or_reserve_bridge_not_insurance_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate; source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L89_C22_HYUNDAIMARINE_2024_RESERVE_RISK_FALSE_STAGE2", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "case_type": "failed_rerating_reserve_risk", "positive_or_counterexample": "counterexample", "best_trigger": "R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Non-life insurance rate/value-up spike had weak forward MFE and meaningful MAE; C22 Stage2 should not be awarded when reserve/loss-ratio risk offsets rate or capital-return theme.", "current_profile_verdict": "current_profile_false_positive_if_nonlife_rate_theme_counts_without_loss_ratio_reserve_capital_bridge", "price_source": "Songdaiki/stock-web", "notes": "Old 2004 CA candidate only; 2024 window clean. Source-proxy only."}
{"row_type": "case", "case_id": "R6L89_C22_SAMSUNGLIFE_2024_LIFE_VALUEUP_EVENT_CAP_4B", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Large-cap life-insurance value-up premium capped after the late-February spike; low forward MFE and deep drawdown support 4B/watch once policy or capital-return premium matures.", "current_profile_verdict": "current_profile_4B_too_late_if_life_insurance_valueup_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action caveat; source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE", "case_id": "R6L89_C22_HANWHALIFE_2024_RATE_VALUEUP_BRIDGE_POSITIVE", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "sector": "life_insurance_rate_valueup_capital_return", "primary_archetype": "life_insurance_rate_ROE_PBR_capital_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-23", "entry_date": "2024-01-23", "entry_price": 2620.0, "evidence_available_at_that_date": "life-insurance rate cycle / value-up / capital-return and ROE-PBR bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["rate_cycle_tailwind", "ROE_PBR_discount", "capital_return_policy_proxy", "reserve_or_CSM_bridge_proxy", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "controlled_MAE90"], "stage4b_evidence_fields": ["valuation_repricing_watch_after_rate_valueup_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 45.61, "MFE_90D_pct": 45.61, "MFE_180D_pct": 45.61, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -5.53, "MAE_90D_pct": -5.53, "MAE_180D_pct": -5.53, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 3815.0, "drawdown_after_peak_pct": -29.23, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_rate_valueup_valuation_watch_needed", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "policy_event_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_life_insurance_rate_valueup_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L89_C22_088350_2024-01-23_2620", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE", "case_id": "R6L89_C22_HYUNDAIMARINE_2024_RESERVE_RISK_FALSE_STAGE2", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "sector": "nonlife_insurance_rate_reserve", "primary_archetype": "nonlife_rate_theme_without_loss_ratio_reserve_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 35450.0, "evidence_available_at_that_date": "non-life insurance rate/value-up and reserve-risk repricing proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["insurance_rate_theme", "valueup_policy_tailwind", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["weak_MFE90", "loss_ratio_or_reserve_risk", "capital_return_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.81, "MFE_90D_pct": 3.81, "MFE_180D_pct": 3.81, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -13.68, "MAE_90D_pct": -14.53, "MAE_180D_pct": -14.53, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 36800.0, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.04, "four_b_full_window_peak_proximity": 0.04, "four_b_timing_verdict": "nonlife_rate_theme_false_stage2_due_reserve_risk_and_weak_MFE", "four_b_evidence_type": ["valuation_blowoff", "reserve_or_loss_ratio_risk", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_nonlife_rate_theme_without_reserve_bridge", "current_profile_verdict": "current_profile_false_positive_if_nonlife_rate_theme_counts_without_loss_ratio_reserve_capital_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L89_C22_001450_2024-02-01_35450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP", "case_id": "R6L89_C22_SAMSUNGLIFE_2024_LIFE_VALUEUP_EVENT_CAP_4B", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "sector": "life_insurance_valueup_event_cap", "primary_archetype": "life_insurance_valueup_premium_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-28", "entry_date": "2024-02-28", "entry_price": 102900.0, "evidence_available_at_that_date": "large-cap life-insurance value-up / capital-return premium after February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["life_insurance_valueup_premium", "capital_return_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_follow_through", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.44, "MFE_90D_pct": 5.44, "MFE_180D_pct": 5.44, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.96, "MAE_90D_pct": -25.56, "MAE_180D_pct": -25.56, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 108500.0, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "good_event_cap_4B_timing_life_insurance_valueup_premium", "four_b_evidence_type": ["valuation_blowoff", "policy_event_premium", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_not_positive_stage_promotion", "current_profile_verdict": "current_profile_4B_too_late_if_life_insurance_valueup_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L89_C22_032830_2024-02-28_102900", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L89_C22_HANWHALIFE_2024_RATE_VALUEUP_BRIDGE_POSITIVE", "trigger_id": "R6L89_C22_HANWHALIFE_2024_STAGE2_ACTIONABLE_RATE_VALUEUP_BRIDGE", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 50, "revision_score": 50, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 30, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "life_insurance_rate_valueup_bridge_positive", "MFE_90D_pct": 45.61, "MAE_90D_pct": -5.53, "score_return_alignment_label": "life_insurance_rate_valueup_bridge_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L89_C22_HYUNDAIMARINE_2024_RESERVE_RISK_FALSE_STAGE2", "trigger_id": "R6L89_C22_HYUNDAIMARINE_2024_STAGE2_FALSE_POSITIVE_NONLIFE_RATE_RESERVE", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "nonlife_reserve_risk_false_stage2", "MFE_90D_pct": 3.81, "MAE_90D_pct": -14.53, "score_return_alignment_label": "nonlife_reserve_risk_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_nonlife_rate_theme_counts_without_loss_ratio_reserve_capital_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L89_C22_SAMSUNGLIFE_2024_LIFE_VALUEUP_EVENT_CAP_4B", "trigger_id": "R6L89_C22_SAMSUNGLIFE_2024_STAGE4B_LIFE_VALUEUP_PREMIUM_CAP", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 25, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 65, "execution_risk_score": 45, "legal_or_contract_risk_score": 10, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 35, "valuation_repricing_score": 35, "execution_risk_score": 80, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "life_valueup_event_cap_4B_guard", "MFE_90D_pct": 5.44, "MAE_90D_pct": -25.56, "score_return_alignment_label": "life_valueup_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_life_insurance_valueup_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "89", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_VALUEUP_BRIDGE_VS_NONLIFE_RESERVE_AND_LIFE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["life_insurance_rate_valueup_bridge_positive", "nonlife_reserve_risk_false_stage2", "life_valueup_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R6
completed_loop = 89
next_round = R7
next_loop = 89
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
