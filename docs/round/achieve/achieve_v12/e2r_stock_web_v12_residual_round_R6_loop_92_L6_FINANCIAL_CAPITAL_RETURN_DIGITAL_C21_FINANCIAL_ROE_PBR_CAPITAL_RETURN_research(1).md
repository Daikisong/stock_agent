# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_92_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 92 is R6 / loop 92. It fills C21 financial ROE/PBR/capital-return behavior after prior R6 loop 91 used C22 and R6 loop 90 used C21 with different symbols.

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
scheduled_loop = 92
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 92
```

R6 permits L6 financial / capital-return / digital-finance research. This loop avoids the recent R6 C21/C22 symbol sets and uses a fresh split around regional-bank ROE/capital-return bridge vs brokerage value-up false Stage2 / 4B cap behavior.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 51 rows / 19 symbols / good-bad Stage2 22-11 / 4B-4C 7-0
top covered symbols include 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
previous R6 loop-88 C21 symbols avoided: 086790, 024110, 003530
previous R6 loop-90 C21 symbols avoided: 316140, 001510, 001750
previous R6 loop-91 C22 symbols avoided: 085620, 000540, 000400
previous R5 loop-92 C18 symbols avoided: 004370, 007310, 005610
```

Selected rows avoid hard duplicate keys and top repeated C21 symbols:

```text
175330 / Stage2-Actionable / 2024-01-24
003470 / Stage2-Actionable / 2024-02-19
016610 / Stage4B / 2024-02-23
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
| 175330 | atlas/symbol_profiles/175/175330.json | selected 2024 window clean after old 2014/2015/2018 CA candidates |
| 003470 | atlas/symbol_profiles/003/003470.json | selected 2024 window clean after historical name-change period |
| 016610 | atlas/symbol_profiles/016/016610.json | selected 2024 window clean; 2025 name change outside window |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE | 175330 | 2024-01-24 | yes | 180 | yes | yes | true |
| R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2 | 003470 | 2024-02-19 | yes | 180 | yes | yes | true |
| R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B | 016610 | 2024-02-23 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires ROE durability, capital-return policy, capital buffer, earnings quality, and revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_VALUEUP_FALSE_STAGE2 | Brokerage value-up label without ROE/capital-return bridge can become false Stage2. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_EVENT_CAP_4B | Brokerage capital-return event premium should route to 4B when bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE | 175330 | JB금융지주 | positive | ROE/capital-return/value-up bridge produced high MFE with shallow entry MAE. |
| R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2 | 003470 | 유안타증권 | counterexample | Brokerage value-up spike had near-zero MFE and then persistent MAE. |
| R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B | 016610 | DB증권 | counterexample / 4B | Brokerage value-up event premium capped near the February spike. |

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
| JB Financial regional-bank capital return | historical public/report proxy | true | true | shadow-only positive |
| Yuanta brokerage value-up false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| DB Securities brokerage event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 175330 | atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv | atlas/symbol_profiles/175/175330.json |
| 003470 | atlas/ohlcv_tradable_by_symbol_year/003/003470/2024.csv | atlas/symbol_profiles/003/003470.json |
| 016610 | atlas/ohlcv_tradable_by_symbol_year/016/016610/2024.csv | atlas/symbol_profiles/016/016610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN | 175330 | Stage2-Actionable | 2024-01-24 | 10770 | positive | regional-bank ROE/capital-return bridge worked |
| R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME | 003470 | Stage2-Actionable | 2024-02-19 | 2880 | counterexample | brokerage value-up false Stage2 |
| R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP | 016610 | Stage4B | 2024-02-23 | 4650 | counterexample/4B | brokerage value-up event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN | 10770 | 30.92 | -0.93 | 38.25 | -0.93 | 59.80 | -0.93 | 2024-10-17 | 17210 | not_calculated_within_selected_review_window |
| R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME | 2880 | 0.35 | -9.55 | 0.35 | -10.42 | 0.35 | -13.02 | 2024-02-19 | 2890 | -17.82 |
| R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP | 4650 | 1.08 | -9.78 | 1.08 | -12.69 | 1.08 | -12.69 | 2024-02-23 | 4695 | -17.36 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs ROE / capital-return / CET1-capital buffer / earnings quality / revision bridge |
| local_4b_watch_guard | strengthen: brokerage value-up event premiums should route to 4B watch when bridge is missing |
| high_MAE_guardrail | strengthen: persistent MAE and near-zero MFE rows cannot promote without capital-return bridge |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |
| hard_4c_thesis_break_routes_to_4c | keep; no hard 4C promoted |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green row is introduced. The useful split is ROE/capital-return bridge quality:

| symbol | stage quality | explanation |
|---|---|---|
| 175330 | good_stage2 | ROE/capital-return bridge produced high MFE and shallow drawdown. |
| 003470 | bad_stage2 | Brokerage value-up spike lacked ROE/capital-return bridge and had near-zero MFE. |
| 016610 | good_4B | Brokerage event premium capped near the February spike. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 003470 brokerage value-up false Stage2 | 1.00 | 1.00 | false Stage2 due missing ROE/capital-return bridge |
| 016610 brokerage event cap | 0.99 | 0.99 | good full-window 4B timing |
| 175330 regional-bank bridge | n/a | n/a | positive Stage2, but later financial value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 003470 / 016610
```

No hard 4C candidate is proposed. R6 loop 92 is about Stage2 bridge quality and 4B event-cap timing.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial ROE/PBR/capital-return cases, Stage2 requires verified ROE durability, shareholder-return policy, CET1/capital buffer, earnings quality, or revision bridge. Low-PBR, value-up, brokerage, bank, or financial label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split true ROE/capital-return positives from brokerage value-up false Stage2 and brokerage capital-return event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 13.23 | -8.01 | 0.67 | mixed; C21 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 13.23 | -8.01 | 0.67 | weaker bridge/event-cap guard |
| P1 sector_specific_candidate_profile | L6 ROE/capital-return bridge required | 2 | 19.30 | -5.68 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 19.30 | -5.68 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing financial value-up themes as positive | 1 | 38.25 | -0.93 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 175330 regional-bank capital-return bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 38.25 | -0.93 | regional_bank_ROE_capital_return_positive |
| 003470 brokerage value-up false | 66 | Stage2-Actionable | 53 | Stage1/Watch | 0.35 | -10.42 | brokerage_valueup_false_stage2 |
| 016610 brokerage event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.08 | -12.69 | brokerage_capital_return_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C21 regional-bank ROE/capital-return positive, brokerage value-up false Stage2, and brokerage capital-return event-cap 4B split using non-top-covered symbols."}
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
residual_error_types_found: regional_bank_ROE_capital_return_positive, brokerage_valueup_false_stage2, brokerage_capital_return_event_cap_4B
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
- C21 financial ROE/PBR/capital-return bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_ROE_capital_return_CET1_earnings_revision_bridge,0,"C21 Stage2 should require ROE durability, shareholder-return policy, capital buffer, earnings quality, or revision bridge, not low-PBR/value-up/financial label alone","JB Financial positive worked; Yuanta Securities and DB Securities theme/event rows failed positive-stage promotion","R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN|R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME|R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_bridge_missing_brokerage_valueup_event_premiums_as_4B_watch,0,"Brokerage value-up/capital-return premiums can peak before ROE and shareholder-return bridge is proven","Yuanta had near-zero forward MFE after value-up spike; DB Securities showed event-cap behavior after February spike","R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME|R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,block_positive_stage_when_financial_valueup_has_high_or_persistent_MAE_without_ROE_bridge,0,"Persistent MAE after bridge-missing financial value-up entries should block Stage2/Stage3 promotion unless capital-return and ROE evidence survives","Yuanta MAE90=-10.42 and DB Securities MAE90=-12.69 with very low forward MFE","R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME|R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "case_type": "structural_success_with_later_valueup_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Regional bank ROE / low-PBR / capital-return bridge produced strong MFE with shallow entry MAE. C21 works when value-up narrative maps into ROE durability, payout/buyback policy, CET1/capital buffer, earnings quality, and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_ROE_capital_return_earnings_quality_bridge_not_lowPBR_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2014/2015/2018 CA candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2", "symbol": "003470", "company_name": "유안타증권", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "case_type": "failed_rerating_brokerage_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brokerage value-up / PBR catch-up watch had very limited forward MFE after the February spike and then persistent MAE. C21 Stage2 should not be awarded without ROE improvement, capital-return policy, earnings quality, and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old name-change history; no 2024 CA caveat used. Source-proxy only."}
{"row_type": "case", "case_id": "R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B", "symbol": "016610", "company_name": "DB증권", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brokerage capital-return / value-up event premium capped around the February spike and then lost trend support. C21 should route bridge-missing brokerage event premiums to 4B unless shareholder-return policy, ROE, earnings quality and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_capital_return_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean; 2025 name change is outside window. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN", "case_id": "R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE", "symbol": "175330", "company_name": "JB금융지주", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "sector": "regional_bank_ROE_PBR_capital_return", "primary_archetype": "regional_bank_ROE_payout_buyback_CET1_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-24", "entry_date": "2024-01-24", "entry_price": 10770.0, "evidence_available_at_that_date": "regional bank low-PBR value-up, ROE durability, payout/buyback policy, CET1/capital buffer and revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["ROE_durability_proxy", "capital_return_policy_proxy", "CET1_capital_buffer_proxy", "earnings_quality_revision_bridge", "relative_strength_reversal"], "stage3_evidence_fields": ["high_MFE30", "high_MFE90", "shallow_MAE90"], "stage4b_evidence_fields": ["later_valueup_valuation_watch", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/175/175330/2024.csv", "profile_path": "atlas/symbol_profiles/175/175330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 30.92, "MFE_90D_pct": 38.25, "MFE_180D_pct": 59.8, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -0.93, "MAE_90D_pct": -0.93, "MAE_180D_pct": -0.93, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-17", "peak_price": 17210.0, "drawdown_after_peak_pct": "not_calculated_within_selected_review_window", "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_financial_valueup_valuation_watch_needed", "four_b_evidence_type": ["valuation_repricing", "positioning_overheat", "financial_valueup_premium"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_regional_bank_ROE_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_CA", "same_entry_group_id": "R6L92_C21_175330_2024-01-24_10770", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME", "case_id": "R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2", "symbol": "003470", "company_name": "유안타증권", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "sector": "brokerage_valueup_PBR_catchup_theme", "primary_archetype": "brokerage_valueup_theme_without_ROE_capital_return_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 2880.0, "evidence_available_at_that_date": "brokerage value-up/PBR catch-up theme and retail trading recovery watch proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_valueup_theme", "PBR_catchup_watch", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "ROE_capital_return_revision_bridge_missing", "post_spike_drawdown"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003470/2024.csv", "profile_path": "atlas/symbol_profiles/003/003470.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.35, "MFE_90D_pct": 0.35, "MFE_180D_pct": 0.35, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.55, "MAE_90D_pct": -10.42, "MAE_180D_pct": -13.02, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 2890.0, "drawdown_after_peak_pct": -17.82, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "brokerage_valueup_theme_spike_was_false_stage2_due_missing_ROE_capital_return_bridge", "four_b_evidence_type": ["brokerage_valueup_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_brokerage_valueup_theme_without_ROE_capital_return_bridge", "current_profile_verdict": "current_profile_false_positive_if_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_2024_CA", "same_entry_group_id": "R6L92_C21_003470_2024-02-19_2880", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP", "case_id": "R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B", "symbol": "016610", "company_name": "DB증권", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "sector": "brokerage_capital_return_valueup_event_premium", "primary_archetype": "brokerage_capital_return_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-23", "entry_date": "2024-02-23", "entry_price": 4650.0, "evidence_available_at_that_date": "brokerage capital-return / value-up event premium after February spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_capital_return_theme", "valueup_event_premium", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "ROE_capital_return_bridge_recheck", "post_event_range_failure"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/016/016610/2024.csv", "profile_path": "atlas/symbol_profiles/016/016610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.08, "MFE_90D_pct": 1.08, "MFE_180D_pct": 1.08, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.78, "MAE_90D_pct": -12.69, "MAE_180D_pct": -12.69, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-23", "peak_price": 4695.0, "drawdown_after_peak_pct": -17.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_full_window_4B_timing_brokerage_capital_return_event_cap", "four_b_evidence_type": ["brokerage_valueup_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_brokerage_capital_return_valueup_premium", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_capital_return_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_before_2025_name_change", "same_entry_group_id": "R6L92_C21_016610_2024-02-23_4650", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L92_C21_JBFG_2024_REGIONAL_BANK_ROE_CAPITAL_RETURN_POSITIVE", "trigger_id": "R6L92_C21_JBFG_2024_STAGE2_ACTIONABLE_REGIONAL_BANK_ROE_CAPITAL_RETURN", "symbol": "175330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 60, "valuation_repricing_score": 55, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "regional_bank_ROE_capital_return_positive", "MFE_90D_pct": 38.25, "MAE_90D_pct": -0.93, "score_return_alignment_label": "regional_bank_ROE_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L92_C21_YUANTA_2024_BROKERAGE_VALUEUP_FALSE_STAGE2", "trigger_id": "R6L92_C21_YUANTA_2024_STAGE2_FALSE_POSITIVE_BROKERAGE_VALUEUP_THEME", "symbol": "003470", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 53, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "brokerage_valueup_false_stage2", "MFE_90D_pct": 0.35, "MAE_90D_pct": -10.42, "score_return_alignment_label": "brokerage_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_brokerage_valueup_theme_counts_without_ROE_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L92_C21_DBSEC_2024_BROKERAGE_CAPITAL_RETURN_EVENT_CAP_4B", "trigger_id": "R6L92_C21_DBSEC_2024_STAGE4B_BROKERAGE_CAPITAL_RETURN_EVENT_CAP", "symbol": "016610", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 70, "customer_quality_score": 25, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 30, "valuation_repricing_score": 25, "execution_risk_score": 80, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "brokerage_capital_return_event_cap_4B_guard", "MFE_90D_pct": 1.08, "MAE_90D_pct": -12.69, "score_return_alignment_label": "brokerage_capital_return_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_capital_return_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "92", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "REGIONAL_BANK_ROE_CAPITAL_RETURN_BRIDGE_VS_BROKERAGE_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["regional_bank_ROE_capital_return_positive", "brokerage_valueup_false_stage2", "brokerage_capital_return_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
10. Add tests that bridge-missing C21 rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 92
next_round = R7
next_loop = 92
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
