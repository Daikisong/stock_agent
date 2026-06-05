# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reserve_rate_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_97_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 97 is R6 / loop 97. R6 is the L6 financial/capital-return/digital-finance round, and this run fills C22 insurance rate cycle / reserve rather than repeating the immediately preceding R6 loop 96 C21 financial ROE/PBR capital-return file or R5 loop 97 C19 retail inventory-margin file.

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
reserve_rate_cycle_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 97
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 97
```

C22 is an insurance reserve/rate-cycle bridge archetype. The rate-cycle headline is the actuarial table's first line; the signal becomes usable only when CSM quality, reserve adequacy, solvency/capital buffer, risk cost, return policy and revision survive together.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C22_INSURANCE_RATE_CYCLE_RESERVE = 37 rows / 12 symbols / good-bad Stage2 10-11 / 4B-4C 2-0
top covered symbols include 000370(7), 003690(7), 082640(6), 000540(4), 000810(3), 005830(3)
previous R6 loop-95 C22 symbols avoided: 138040, 244920, 211050
previous R6 loop-96 C21 symbols avoided: 029780, 007330, 377300
previous R5 loop-97 C19 symbols avoided: 023530, 383220, 008770
```

Selected rows avoid hard duplicates and top repeated C22 symbols:

```text
032830 / Stage2-Actionable / 2024-01-25
088350 / Stage2-Actionable / 2024-02-06
000400 / Stage4B / 2024-06-21
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
| 032830 | atlas/symbol_profiles/032/032830.json | no corporate-action candidate |
| 088350 | atlas/symbol_profiles/088/088350.json | no corporate-action candidate |
| 000400 | atlas/symbol_profiles/000/000400.json | selected 2024 window clean after old 2001/2002/2006/2012/2015/2019 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE | 032830 | 2024-01-25 | yes | 180 | yes | yes | true |
| R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2 | 088350 | 2024-02-06 | yes | 180 | yes | yes | true |
| R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B | 000400 | 2024-06-21 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_CSM_RESERVE_VALUEUP_BRIDGE | Positive Stage2 requires CSM quality, reserve adequacy, capital buffer, return policy and revision bridge. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_RATE_SENSITIVITY_FALSE_STAGE2 | Life-insurer rate-cycle watch without CSM/reserve/capital-return bridge can become false Stage2. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_SALE_RESERVE_EVENT_CAP_4B | Insurance sale/reserve event premium should route to 4B when reserve, transaction and capital bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE | 032830 | 삼성생명 | positive | CSM/reserve/value-up bridge produced strong MFE with shallow early MAE. |
| R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2 | 088350 | 한화생명 | counterexample | Life-insurer rate-cycle watch had limited MFE and persistent MAE without reserve/capital-return bridge. |
| R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B | 000400 | 롯데손해보험 | counterexample / 4B | Insurance sale/reserve premium capped after the June spike and then dropped sharply. |

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
| Samsung Life CSM/reserve value-up bridge | historical public/report proxy | true | true | shadow-only positive |
| Hanwha Life rate-cycle false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Lotte Insurance sale/reserve event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 032830 | atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv | atlas/symbol_profiles/032/032830.json |
| 088350 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json |
| 000400 | atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv | atlas/symbol_profiles/000/000400.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE | 032830 | Stage2-Actionable | 2024-01-25 | 63800 | positive | life CSM/reserve value-up bridge worked |
| R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH | 088350 | Stage2-Actionable | 2024-02-06 | 3545 | counterexample | life rate-cycle false Stage2 |
| R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP | 000400 | Stage4B | 2024-06-21 | 4040 | counterexample/4B | insurance sale/reserve event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE | 63800 | 70.06 | -2.35 | 70.06 | -2.35 | 70.06 | -2.35 | 2024-03-08 | 108500 | -29.40 |
| R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH | 3545 | 7.62 | -21.30 | 7.62 | -27.22 | 7.62 | -27.22 | 2024-02-13 | 3815 | -32.37 |
| R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP | 4040 | 1.24 | -37.99 | 1.24 | -37.99 | 1.24 | -37.99 | 2024-06-26 | 4090 | -38.75 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C22 Stage2 needs CSM / reserve / solvency / capital-return / revision bridge |
| reserve_rate_cycle_guardrail | strengthen: rate-cycle labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing life-insurer and insurance sale/reserve premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE insurer rows cannot promote without durable reserve/capital bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether insurance/rate narrative becomes CSM, reserve and capital-return evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 032830 | good_stage2_with_later_watch | CSM/reserve/value-up bridge produced strong MFE with shallow MAE. |
| 088350 | bad_stage2 | Life-insurer rate-cycle watch lacked CSM/reserve/capital-return bridge and then suffered high MAE. |
| 000400 | good_4B | Insurance sale/reserve event premium capped after the June spike and then fell sharply. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 088350 life rate-cycle false Stage2 | 0.93 | 0.93 | false Stage2 due missing CSM/reserve/capital-return bridge |
| 000400 insurance sale/reserve cap | 0.99 | 0.99 | good full-window 4B timing after June insurance sale/reserve premium |
| 032830 life CSM/reserve bridge | n/a | n/a | positive Stage2, but later rate-cycle/value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 088350 / 000400
```

No hard 4C candidate is introduced in this R6 loop 97 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 insurance rate-cycle / reserve cases, Stage2 requires verified CSM quality, reserve adequacy, solvency or K-ICS/RBC capital buffer, shareholder-return mechanics, risk-cost discipline, or revision bridge. Insurance, rate-cycle, value-up, sale, reserve, solvency or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
rule = C22 should split true CSM/reserve/capital-return positives from life-rate sensitivity false Stage2 and insurance sale/reserve event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 26.31 | -22.52 | 0.67 | mixed; C22 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 26.31 | -22.52 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L6 reserve/capital-return bridge required | 2 | 38.84 | -14.79 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C22 bridge vs event-cap split | 2 | 38.84 | -14.79 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing insurer rate-cycle themes as positive | 1 | 70.06 | -2.35 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 032830 life CSM/reserve bridge | 66 | Stage2-Watch | 79 | Stage2-Actionable | 70.06 | -2.35 | life_CSM_reserve_valueup_positive |
| 088350 life rate-cycle false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 7.62 | -27.22 | life_rate_sensitivity_false_stage2 |
| 000400 insurance sale/reserve cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.24 | -37.99 | insurance_sale_reserve_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C22 Samsung Life CSM/reserve value-up positive, Hanwha Life rate-sensitivity false Stage2, and Lotte Insurance sale/reserve event-cap 4B while avoiding top repeated C22 and previous R6/R5 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, reserve_rate_cycle_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: life_CSM_reserve_valueup_positive, life_rate_sensitivity_false_stage2, insurance_sale_reserve_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, reserve_rate_cycle_guardrail, high_MAE_guardrail
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
- C22 insurance rate-cycle / reserve bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,C22_requires_CSM_reserve_capital_buffer_return_policy_revision_bridge,0,"C22 Stage2 should require CSM quality, reserve adequacy, capital buffer, solvency/RBC/K-ICS visibility, shareholder-return mechanics, risk-cost discipline, or revision bridge, not insurance/rate-cycle/value-up label alone","Samsung Life positive worked; Hanwha Life and Lotte Insurance event/watch rows failed positive-stage promotion","R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE|R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH|R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,cap_bridge_missing_life_insurer_and_sale_reserve_event_premiums_as_4B_watch,0,"Life-insurer rate-cycle and insurance sale/reserve event premiums can peak before reserve, solvency, risk-cost and capital-return bridge is proven","Hanwha Life had limited MFE and persistent MAE; Lotte Insurance showed clean 4B event-cap behavior after the June sale/reserve spike","R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH|R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,block_positive_stage_when_insurance_rate_cycle_theme_has_high_or_persistent_MAE_without_reserve_bridge,0,"High or persistent MAE after bridge-missing C22 entries should block Stage2/Stage3 promotion unless CSM/reserve/capital-return evidence survives","Hanwha Life MAE90=-27.22 and Lotte Insurance MAE90=-37.99","R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH|R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "case_type": "structural_success_with_later_life_insurance_valueup_rate_cycle_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Life-insurance CSM/reserve/value-up and capital-return bridge produced strong MFE from the January base with shallow early MAE. C22 works when insurer rate-cycle narrative maps into reserve adequacy, CSM quality, capital buffer, shareholder-return policy, risk control and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C22_positive_requires_CSM_reserve_capital_buffer_return_policy_revision_bridge_not_rate_cycle_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "case_type": "failed_rerating_life_insurer_rate_sensitivity_reserve_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Life-insurer rate-cycle / value-up watch after the February spike had only limited follow-through and then a persistent reserve/capital-return drawdown. C22 Stage2 should not be awarded without CSM quality, reserve adequacy, capital buffer, shareholder-return mechanics and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_life_insurer_rate_sensitivity_watch_counts_without_CSM_reserve_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Non-life insurer sale/reserve event premium capped after the June spike and then collapsed through the following trading window. C22 should route bridge-missing insurer sale/reserve premiums to 4B unless reserve adequacy, capital buffer, transaction certainty, solvency, risk cost and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_sale_reserve_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2001/2002/2006/2012/2015/2019 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE", "case_id": "R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "sector": "life_insurance_CSM_reserve_valueup_capital_return", "primary_archetype": "CSM_reserve_capital_buffer_return_policy_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reserve_rate_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "entry_date": "2024-01-25", "entry_price": 63800.0, "evidence_available_at_that_date": "life-insurance CSM/reserve quality, rate-cycle sensitivity, capital buffer, value-up/shareholder-return policy and revision bridge proxy after January low; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["CSM_quality_proxy", "reserve_adequacy_proxy", "capital_buffer_proxy", "shareholder_return_policy_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["very_strong_MFE30", "very_strong_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_life_insurance_valueup_valuation_watch", "rate_cycle_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 70.06, "MFE_90D_pct": 70.06, "MFE_180D_pct": 70.06, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.35, "MAE_90D_pct": -2.35, "MAE_180D_pct": -2.35, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-08", "peak_price": 108500.0, "drawdown_after_peak_pct": -29.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_life_insurance_valueup_valuation_and_rate_cycle_4B_watch_needed", "four_b_evidence_type": ["CSM_reserve_bridge", "capital_return_policy", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_life_insurance_CSM_reserve_valueup_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L97_C22_032830_2024-01-25_63800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH", "case_id": "R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2", "symbol": "088350", "company_name": "한화생명", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "sector": "life_insurer_rate_cycle_reserve_sensitivity_watch", "primary_archetype": "life_insurer_rate_watch_without_CSM_reserve_capital_return_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reserve_rate_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 3545.0, "evidence_available_at_that_date": "life-insurer rate-cycle / value-up watch after February financial rally without confirmed CSM quality, reserve adequacy, solvency buffer, payout mechanics or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["life_rate_cycle_watch", "financial_valueup_sympathy", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "persistent_MAE90", "CSM_reserve_capital_return_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv", "profile_path": "atlas/symbol_profiles/088/088350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.62, "MFE_90D_pct": 7.62, "MFE_180D_pct": 7.62, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -21.3, "MAE_90D_pct": -27.22, "MAE_180D_pct": -27.22, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-13", "peak_price": 3815.0, "drawdown_after_peak_pct": -32.37, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "life_insurer_rate_cycle_watch_was_false_stage2_due_missing_CSM_reserve_capital_return_revision_bridge", "four_b_evidence_type": ["life_insurer_rate_cycle_premium", "bridge_missing", "limited_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_life_insurer_rate_sensitivity_watch_without_reserve_capital_return_bridge", "current_profile_verdict": "current_profile_false_positive_if_life_insurer_rate_sensitivity_watch_counts_without_CSM_reserve_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L97_C22_088350_2024-02-06_3545", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP", "case_id": "R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "sector": "nonlife_insurance_sale_reserve_event_premium", "primary_archetype": "insurance_sale_reserve_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | reserve_rate_cycle_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-21", "entry_date": "2024-06-21", "entry_price": 4040.0, "evidence_available_at_that_date": "non-life insurer sale/reserve event premium after June insurance-equity spike without confirmed transaction certainty, reserve adequacy, solvency buffer, risk-cost or capital-return bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["insurance_sale_event", "reserve_valueup_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "transaction_reserve_capital_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.24, "MFE_90D_pct": 1.24, "MFE_180D_pct": 1.24, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -37.99, "MAE_90D_pct": -37.99, "MAE_180D_pct": -37.99, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090.0, "drawdown_after_peak_pct": -38.75, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_full_window_4B_timing_insurance_sale_reserve_event_cap", "four_b_evidence_type": ["insurance_sale_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_insurance_sale_reserve_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_sale_reserve_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2001_2002_2006_2012_2015_2019_CA", "same_entry_group_id": "R6L97_C22_000400_2024-06-21_4040", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L97_C22_SAMSUNGLIFE_2024_LIFE_CSM_RESERVE_VALUEUP_BRIDGE_POSITIVE", "trigger_id": "R6L97_C22_SAMSUNGLIFE_2024_STAGE2_ACTIONABLE_LIFE_CSM_RESERVE_VALUEUP_BRIDGE", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 30, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 45, "policy_or_regulatory_score": 65, "valuation_repricing_score": 50, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "life_CSM_reserve_valueup_positive", "MFE_90D_pct": 70.06, "MAE_90D_pct": -2.35, "score_return_alignment_label": "life_CSM_reserve_valueup_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L97_C22_HANWHALIFE_2024_LIFE_RATE_SENSITIVITY_FALSE_STAGE2", "trigger_id": "R6L97_C22_HANWHALIFE_2024_STAGE2_FALSE_POSITIVE_LIFE_RATE_SENSITIVITY_RESERVE_WATCH", "symbol": "088350", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "life_rate_sensitivity_false_stage2", "MFE_90D_pct": 7.62, "MAE_90D_pct": -27.22, "score_return_alignment_label": "life_rate_sensitivity_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_life_insurer_rate_sensitivity_watch_counts_without_CSM_reserve_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L97_C22_LOTTEINS_2024_INSURANCE_SALE_RESERVE_EVENT_CAP_4B", "trigger_id": "R6L97_C22_LOTTEINS_2024_STAGE4B_INSURANCE_SALE_RESERVE_EVENT_CAP", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 95, "legal_or_contract_risk_score": 65, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "insurance_sale_reserve_event_cap_4B_guard", "MFE_90D_pct": 1.24, "MAE_90D_pct": -37.99, "score_return_alignment_label": "insurance_sale_reserve_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_sale_reserve_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "97", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_CSM_RESERVE_VALUEUP_BRIDGE_VS_LIFE_INSURER_RATE_SENSITIVITY_FALSE_STAGE2_AND_INSURANCE_SALE_RESERVE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "reserve_rate_cycle_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["life_CSM_reserve_valueup_positive", "life_rate_sensitivity_false_stage2", "insurance_sale_reserve_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- False-positive rows should strengthen bridge requirements, not generate positive promotion.
- C22 rows need explicit CSM quality, reserve adequacy, solvency or K-ICS/RBC capital buffer, shareholder-return mechanics, risk-cost discipline, or revision bridge before positive promotion.
- In C22, bridge-missing insurance/rate-cycle event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C22 insurance rate-cycle/reserve rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 97
next_round = R7
next_loop = 97
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
