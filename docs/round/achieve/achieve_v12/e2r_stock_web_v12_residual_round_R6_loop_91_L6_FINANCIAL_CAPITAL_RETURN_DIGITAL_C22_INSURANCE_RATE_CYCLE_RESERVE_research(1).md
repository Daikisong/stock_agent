# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_91_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 91 is R6 / loop 91. This round uses C22 insurance rate-cycle / reserve / capital policy behavior and avoids the R6 loop 90 C21 symbol set.

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
scheduled_round = R6
scheduled_loop = 91
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 91
```

R6 permits L6 financial / capital-return / digital-finance research. Previous R6 loop 90 used C21 and previous R6 loop 89 used different C22 rows, so this loop uses a new C22 fine split: rate/reserve value-up bridge vs insurance event-cap / false-Stage2 guardrails.

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
previous R6 loop-89 C22 symbols avoided: 088350, 001450, 032830
previous R6 loop-90 C21 symbols avoided: 316140, 001510, 001750
previous R5 loop-91 C20 symbols avoided: 090430, 051900, 097950
```

Selected rows avoid hard duplicates:

```text
085620 / Stage2-Actionable / 2024-01-24
000540 / Stage2-Actionable / 2024-02-14
000400 / Stage4B / 2024-06-26
```

`000540` is a soft expansion because it is already high-coverage in C22; its independent evidence weight is reduced to 0.75.

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
| 085620 | atlas/symbol_profiles/085/085620.json | selected 2024 window clean after 2018-03-23 CA |
| 000540 | atlas/symbol_profiles/000/000540.json | selected 2024 window clean after 2011-or-earlier CA |
| 000400 | atlas/symbol_profiles/000/000400.json | selected 2024 window clean after 2019-or-earlier CA |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L91_C22_MIRAEASSETLIFE_2024_RATE_RESERVE_VALUEUP_BRIDGE_POSITIVE | 085620 | 2024-01-24 | yes | 180 | yes | yes | true |
| R6L91_C22_HEUNGKUKFIRE_2024_FIRE_INSURANCE_VALUEUP_FALSE_STAGE2 | 000540 | 2024-02-14 | yes | 180 | yes | yes | true |
| R6L91_C22_LOTTEINS_2024_INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B | 000400 | 2024-06-26 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE | Positive Stage2 requires rate-cycle, reserve adequacy, capital policy, shareholder return, and earnings/revision bridge. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | FIRE_INSURANCE_FALSE_STAGE2 | Fire-insurance value-up label without reserve/loss-ratio/capital bridge can become high-MAE false Stage2. |
| C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B | M&A/control-premium spike should route to 4B when completed transaction or reserve/capital bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L91_C22_MIRAEASSETLIFE_2024_RATE_RESERVE_VALUEUP_BRIDGE_POSITIVE | 085620 | 미래에셋생명 | positive | Life-insurance rate/reserve bridge had high MFE and shallow MAE. |
| R6L91_C22_HEUNGKUKFIRE_2024_FIRE_INSURANCE_VALUEUP_FALSE_STAGE2 | 000540 | 흥국화재 | counterexample | Fire-insurance value-up spike had deep MAE without durable bridge. |
| R6L91_C22_LOTTEINS_2024_INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B | 000400 | 롯데손해보험 | counterexample / 4B | Insurance M&A/control-premium event capped near late-June spike and drew down. |

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
| Mirae Asset Life rate/reserve bridge | historical public/report proxy | true | true | shadow-only positive |
| Heungkuk Fire value-up false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Lotte Insurance M&A/control cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 085620 | atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv | atlas/symbol_profiles/085/085620.json |
| 000540 | atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv | atlas/symbol_profiles/000/000540.json |
| 000400 | atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv | atlas/symbol_profiles/000/000400.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE | 085620 | Stage2-Actionable | 2024-01-24 | 4415 | positive | life-insurance rate/reserve bridge worked |
| R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP | 000540 | Stage2-Actionable | 2024-02-14 | 5570 | counterexample | fire-insurance value-up false Stage2 |
| R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP | 000400 | Stage4B | 2024-06-26 | 4000 | counterexample/4B | insurance M&A/control event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE | 4415 | 47.23 | -0.68 | 47.23 | -0.68 | 47.23 | -0.68 | 2024-02-06 | 6500 | -30.77 |
| R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP | 5570 | 18.49 | -27.99 | 18.49 | -32.41 | 18.49 | -32.41 | 2024-02-14 | 6600 | -42.95 |
| R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP | 4000 | 2.25 | -37.38 | 2.25 | -45.63 | 2.25 | -45.63 | 2024-06-26 | 4090 | -46.82 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C22 Stage2 needs rate/reserve/loss-ratio/capital-return/revision bridge |
| local_4b_watch_guard | strengthen: insurance M&A and control-premium event spikes should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE insurance/value-up rows cannot promote without capital/reserve bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is reserve/capital bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 085620 | good_stage2 | Rate/reserve/capital bridge produced high MFE with very shallow MAE. |
| 000540 | bad_stage2 | Value-up spike had meaningful MFE but deep drawdown without confirmed reserve/capital bridge. |
| 000400 | good_4B | M&A/control-premium event capped near the late-June spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 000540 fire-insurance false Stage2 | 0.84 | 0.84 | value-up spike was false Stage2 due missing reserve/loss-ratio/capital bridge |
| 000400 M&A/control cap | 1.00 | 1.00 | good full-window 4B timing |
| 085620 rate/reserve bridge | n/a | n/a | positive Stage2, but later insurance value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 000540 / 000400
```

No hard 4C candidate is proposed. R6 loop 91 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 insurance rate-cycle/reserve cases, Stage2 requires verified rate-cycle benefit, reserve adequacy, loss ratio, capital policy, shareholder return, earnings quality, or revision bridge. Insurance, value-up, M&A, control-premium, or low-PBR label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
rule = C22 should split true rate/reserve/capital-return positives from fire-insurance value-up false Stage2 and insurance M&A/control-premium event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 22.66 | -26.24 | 0.67 | mixed; C22 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 22.66 | -26.24 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L6 insurance reserve/capital bridge required | 2 | 32.86 | -16.55 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C22 bridge vs event-cap split | 2 | 32.86 | -16.55 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing insurance themes as positive | 1 | 47.23 | -0.68 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 085620 rate/reserve bridge | 66 | Stage2-Watch | 75 | Stage2-Actionable | 47.23 | -0.68 | life_insurance_rate_reserve_valueup_positive |
| 000540 fire-insurance false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 18.49 | -32.41 | fire_insurance_valueup_false_stage2 |
| 000400 insurance M&A cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 2.25 | -45.63 | insurance_MA_control_premium_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C22 life-insurance rate/reserve value-up positive, fire-insurance value-up false Stage2, and insurance M&A/control-premium event-cap 4B split."}
```

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: life_insurance_rate_reserve_valueup_positive, fire_insurance_valueup_false_stage2, insurance_MA_control_premium_event_cap_4B
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
- C22 insurance rate-cycle/reserve bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,C22_requires_rate_reserve_loss_ratio_capital_return_revision_bridge,0,"C22 Stage2 should require rate-cycle, reserve adequacy, loss ratio, capital policy, shareholder return, or earnings/revision bridge, not insurance/value-up label alone","Mirae Asset Life positive worked; Heungkuk Fire and Lotte Insurance event/theme rows failed positive-stage promotion","R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE|R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP|R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,cap_insurance_valueup_and_MA_control_premiums_as_4B_watch,0,"Insurance value-up, M&A, and control-premium event spikes can peak before reserve/loss-ratio/capital bridge is proven","Heungkuk Fire had high MAE after value-up spike; Lotte Insurance had full-window event-cap behavior","R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP|R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,configured,block_positive_stage_when_insurance_theme_has_high_MAE_without_capital_reserve_bridge,0,"High MAE after an insurance/rate/value-up/control-premium entry should block Stage2/Stage3 promotion unless reserve and capital evidence survives","Heungkuk Fire MAE90=-32.41 and Lotte Insurance MAE90=-45.63","R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP|R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L91_C22_MIRAEASSETLIFE_2024_RATE_RESERVE_VALUEUP_BRIDGE_POSITIVE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Life insurance rate/reserve value-up bridge produced high 30D/90D MFE with shallow MAE. C22 works when low-PBR/rate narrative maps into reserve adequacy, capital policy, shareholder-return, and earnings/revision bridge.", "current_profile_verdict": "current_profile_kept_but_C22_positive_requires_rate_reserve_capital_return_revision_bridge_not_insurance_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2018 corporate-action candidate. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L91_C22_HEUNGKUKFIRE_2024_FIRE_INSURANCE_VALUEUP_FALSE_STAGE2", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "case_type": "failed_rerating_high_mae", "positive_or_counterexample": "counterexample", "best_trigger": "R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "Soft expansion: 000540 appears in C22 coverage, but this row uses a new entry date / fire-insurance value-up false Stage2 family.", "independent_evidence_weight": 0.75, "score_price_alignment": "Fire-insurance value-up / rate-cycle spike had respectable same-day MFE but deep 90D MAE. C22 Stage2 should not be awarded without reserve adequacy, loss-ratio, capital-return, and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_fire_insurance_valueup_theme_counts_without_reserve_loss_ratio_capital_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2011-or-earlier CA candidates. Reduced weight because 000540 is already a high-coverage C22 symbol."}
{"row_type": "case", "case_id": "R6L91_C22_LOTTEINS_2024_INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Insurance M&A/control-premium spike capped around late June and then drew down sharply. C22 should route bridge-missing insurance event premiums to 4B unless completed transaction, capital policy, reserve/loss-ratio, and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_MA_control_premium_event_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2019-or-earlier CA candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE", "case_id": "R6L91_C22_MIRAEASSETLIFE_2024_RATE_RESERVE_VALUEUP_BRIDGE_POSITIVE", "symbol": "085620", "company_name": "미래에셋생명", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "sector": "life_insurance_rate_reserve_valueup", "primary_archetype": "life_insurance_rate_reserve_capital_return_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 4415.0, "evidence_available_at_that_date": "life insurance low-PBR/value-up, rate-cycle, reserve adequacy, capital policy and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["rate_cycle_proxy", "reserve_adequacy_proxy", "capital_policy_bridge", "low_PBR_valueup", "revision_bridge_proxy"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["valuation_watch_after_insurance_valueup_run"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv", "profile_path": "atlas/symbol_profiles/085/085620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 47.23, "MFE_90D_pct": 47.23, "MFE_180D_pct": 47.23, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.68, "MAE_90D_pct": -0.68, "MAE_180D_pct": -0.68, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-06", "peak_price": 6500.0, "drawdown_after_peak_pct": -30.77, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_insurance_valueup_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "insurance_valueup_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_life_insurance_rate_reserve_valueup_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2018_CA", "same_entry_group_id": "R6L91_C22_085620_2024-01-24_4415", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP", "case_id": "R6L91_C22_HEUNGKUKFIRE_2024_FIRE_INSURANCE_VALUEUP_FALSE_STAGE2", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "sector": "fire_insurance_valueup_rate_cycle", "primary_archetype": "fire_insurance_valueup_without_reserve_loss_ratio_capital_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-14", "entry_date": "2024-02-14", "entry_price": 5570.0, "evidence_available_at_that_date": "fire insurance value-up/rate cycle spike, loss-ratio and reserve adequacy watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["fire_insurance_valueup_theme", "rate_cycle_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["deep_MAE90", "reserve_loss_ratio_capital_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 18.49, "MFE_90D_pct": 18.49, "MFE_180D_pct": 18.49, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -27.99, "MAE_90D_pct": -32.41, "MAE_180D_pct": -32.41, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-14", "peak_price": 6600.0, "drawdown_after_peak_pct": -42.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.84, "four_b_full_window_peak_proximity": 0.84, "four_b_timing_verdict": "fire_insurance_valueup_spike_was_false_stage2_due_missing_reserve_loss_ratio_capital_bridge", "four_b_evidence_type": ["insurance_valueup_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_fire_insurance_valueup_without_reserve_loss_ratio_bridge", "current_profile_verdict": "current_profile_false_positive_if_fire_insurance_valueup_theme_counts_without_reserve_loss_ratio_capital_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2011_CA", "same_entry_group_id": "R6L91_C22_000540_2024-02-14_5570", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_soft_expansion", "is_new_independent_case": true, "reuse_reason": "soft_expansion_same_C22_symbol_new_entry_date_and_failure_family", "independent_evidence_weight": 0.75, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP", "case_id": "R6L91_C22_LOTTEINS_2024_INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "sector": "insurance_MA_control_premium_event", "primary_archetype": "insurance_MA_control_premium_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 4000.0, "evidence_available_at_that_date": "insurance M&A/control-premium event and capital-policy expectation after late-June spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["insurance_MA_control_premium", "capital_policy_expectation", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "weak_forward_MFE", "post_peak_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.25, "MFE_90D_pct": 2.25, "MFE_180D_pct": 2.25, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -37.38, "MAE_90D_pct": -45.63, "MAE_180D_pct": -45.63, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090.0, "drawdown_after_peak_pct": -46.82, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_insurance_MA_control_premium_event_cap", "four_b_evidence_type": ["control_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_insurance_MA_control_premium_event", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_MA_control_premium_event_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2019_CA", "same_entry_group_id": "R6L91_C22_000400_2024-06-26_4000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L91_C22_MIRAEASSETLIFE_2024_RATE_RESERVE_VALUEUP_BRIDGE_POSITIVE", "trigger_id": "R6L91_C22_MIRAEASSETLIFE_2024_STAGE2_ACTIONABLE_RATE_RESERVE_VALUEUP_BRIDGE", "symbol": "085620", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 65, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "life_insurance_rate_reserve_valueup_positive", "MFE_90D_pct": 47.23, "MAE_90D_pct": -0.68, "score_return_alignment_label": "life_insurance_rate_reserve_valueup_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L91_C22_HEUNGKUKFIRE_2024_FIRE_INSURANCE_VALUEUP_FALSE_STAGE2", "trigger_id": "R6L91_C22_HEUNGKUKFIRE_2024_STAGE2_FALSE_POSITIVE_FIRE_INSURANCE_VALUEUP", "symbol": "000540", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "fire_insurance_valueup_false_stage2", "MFE_90D_pct": 18.49, "MAE_90D_pct": -32.41, "score_return_alignment_label": "fire_insurance_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_fire_insurance_valueup_theme_counts_without_reserve_loss_ratio_capital_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L91_C22_LOTTEINS_2024_INSURANCE_MA_CONTROL_PREMIUM_EVENT_CAP_4B", "trigger_id": "R6L91_C22_LOTTEINS_2024_STAGE4B_INSURANCE_MA_CONTROL_PREMIUM_CAP", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 20, "policy_or_regulatory_score": 45, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "insurance_MA_control_premium_event_cap_4B_guard", "MFE_90D_pct": 2.25, "MAE_90D_pct": -45.63, "score_return_alignment_label": "insurance_MA_control_premium_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_insurance_MA_control_premium_event_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "91", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_RATE_RESERVE_VALUEUP_BRIDGE_VS_FIRE_INSURANCE_FALSE_STAGE2_AND_INSURANCE_MA_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["life_insurance_rate_reserve_valueup_positive", "fire_insurance_valueup_false_stage2", "insurance_MA_control_premium_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
10. Add tests that bridge-missing C22 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 91
next_round = R7
next_loop = 91
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
