# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 100
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP
loop_objective = priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | financial_ROE_PBR_capital_return_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_100_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This file is the corrected final output for this execution. The scheduler is coverage-index-first. A C22 duplicate path was inspected during this run but is not the final artifact because C22 was already finalized immediately before. After C22, the remaining below-50 financial Priority 1 gap is C21. Since R6 loop99 was used locally for C22, this file uses R6 loop100 to avoid local round-loop collision.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_2_rolling_calibrated
previous_baseline_reference = e2r_2_1_stock_web_calibrated
production_scoring_changed = false
shadow_weight_only = true
```

Existing axes tested:

```text
stage2_required_bridge = existing_axis_strengthened
local_4b_watch_guard = existing_axis_strengthened
financial_ROE_PBR_capital_return_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 100
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
coverage_index_override_previous_round = true
```

C21 is a financial ROE/PBR and capital-return archetype. Low PBR is the cheap-looking price tag; the usable signal is whether ROE durability, capital buffer, credit-cost discipline, shareholder-return capacity and revisions turn that tag into cash return.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 48 rows / Priority 1
top covered C21 symbols avoided: 006800, 055550, 086790, 316140, 001510, 039490
recent local Priority 0/1 artifacts accounted for: C08, C09, C01, C07, C06, C10, C14, C11, C02, C13, C19, C27, C12, C24, C28, C17, C23, C03, C16, C04, C05, C15, C18, C20, C25, C26, C22
C22 duplicate inspected during this run discarded from final output
```

Selected rows avoid hard duplicates and add new C21 trigger families:

```text
024110 / Stage2-Actionable / 2024-01-29
323410 / Stage2-Actionable / 2024-01-15
030610 / Stage4B / 2024-02-19
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
| 024110 | atlas/symbol_profiles/024/024110.json | selected 2024 window clean after old 1998/2000/2003 CA candidates |
| 323410 | atlas/symbol_profiles/323/323410.json | no corporate-action candidate |
| 030610 | atlas/symbol_profiles/030/030610.json | selected 2024 window clean after old 2020/2023 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 024110 | 2024-01-29 | yes | 180 | yes | yes | true |
| R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2 | 323410 | 2024-01-15 | yes | 180 | yes | yes | true |
| R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B | 030610 | 2024-02-19 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires ROE durability, capital buffer, credit-cost discipline, shareholder-return capacity and revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | DIGITAL_BANK_VALUATION_FALSE_STAGE2 | Digital-bank PBR watch without ROE/credit-cost/capital-return bridge can become false Stage2. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | SMALLCAP_BROKERAGE_EVENT_CAP_4B | Small-cap brokerage value-up premium should route to 4B when ROE/capital-return bridge is missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 024110 | 기업은행 | positive | Bank value-up ROE/PBR and capital-return bridge produced strong 30D/90D MFE with shallow early MAE. |
| R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2 | 323410 | 카카오뱅크 | counterexample | Digital-bank valuation watch had near-zero MFE and deep MAE without ROE/capital-return bridge. |
| R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B | 030610 | 교보증권 | counterexample / 4B | Small-cap brokerage value-up premium capped after the February spike and faded. |

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
| IBK bank value-up ROE/PBR capital-return bridge | historical public/report proxy | true | true | shadow-only positive |
| KakaoBank digital-bank ROE/PBR false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Kyobo Securities small-cap brokerage value-up cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 024110 | atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv | atlas/symbol_profiles/024/024110.json |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json |
| 030610 | atlas/ohlcv_tradable_by_symbol_year/030/030610/2024.csv | atlas/symbol_profiles/030/030610.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE | 024110 | Stage2-Actionable | 2024-01-29 | 12100 | positive | bank value-up ROE/PBR capital-return bridge worked |
| R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH | 323410 | Stage2-Actionable | 2024-01-15 | 31450 | counterexample | digital-bank ROE/PBR false Stage2 |
| R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP | 030610 | Stage4B | 2024-02-19 | 5640 | counterexample/4B | small-cap brokerage value-up event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE | 12100 | 31.74 | -1.98 | 32.31 | -1.98 | 32.31 | -1.98 | 2024-03-15 | 16010 | -21.05 |
| R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH | 31450 | 0.16 | -15.74 | 0.16 | -30.52 | 0.16 | -36.25 | 2024-01-15 | 31500 | -36.35 |
| R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP | 5640 | 1.42 | -11.88 | 1.42 | -15.87 | 1.42 | -15.87 | 2024-02-20 | 5720 | -17.05 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs ROE durability / capital buffer / credit-cost discipline / dividend-buyback capacity / revision bridge |
| financial_ROE_PBR_capital_return_guardrail | strengthen: value-up or low-PBR label alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing digital-bank and small-cap brokerage premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C21 rows cannot promote without durable ROE/capital-return bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether financial value-up narrative becomes ROE, capital buffer, credit-cost and shareholder-return evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 024110 | good_stage2_with_later_watch | ROE/PBR capital-return bridge produced strong MFE with shallow early MAE, but later bank value-up valuation watch remains necessary. |
| 323410 | bad_stage2 | Digital-bank PBR watch lacked ROE/credit-cost/capital-return bridge and produced near-zero MFE with deep MAE. |
| 030610 | good_4B | Brokerage value-up premium peaked quickly and faded without durable ROE/capital-policy bridge. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 323410 digital-bank false Stage2 | 1.00 | 1.00 | false Stage2 due missing ROE / credit-cost / capital-return bridge |
| 030610 small-cap brokerage cap | 0.99 | 0.99 | good 4B timing after brokerage value-up premium |
| 024110 bank capital-return bridge | n/a | n/a | positive Stage2, but later bank value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = ROE_or_credit_cost_break_watch_only for 323410
four_c_protection_label = ROE_or_capital_policy_break_watch_only for 030610
```

No hard 4C candidate is introduced in this C21 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial ROE/PBR capital-return cases, Stage2 requires verified ROE durability, capital buffer, credit-cost discipline, dividend/buyback capacity and revision bridge. Value-up, low-PBR, digital bank, brokerage beta or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split true ROE/capital-return positives from digital-bank false Stage2 and small-cap brokerage event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current profile | 3 | 11.30 | -16.12 | 0.67 | mixed; C21 ROE/capital-return bridge split needed |
| P0b e2r_2_1_stock_web_calibrated_reference | older calibrated baseline | 3 | 11.30 | -16.12 | 0.67 | weaker C21 bridge split |
| P1 sector_specific_candidate_profile | L6 ROE/capital-return bridge required | 2 | 16.24 | -8.93 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 16.24 | -8.93 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing financial value-up themes as positive | 1 | 32.31 | -1.98 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 024110 bank value-up bridge | 66 | Stage2-Watch | 80 | Stage2-Actionable | 32.31 | -1.98 | financial_ROE_PBR_capital_return_positive |
| 323410 digital-bank false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 0.16 | -30.52 | digital_bank_false_stage2 |
| 030610 brokerage event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 1.42 | -15.87 | smallcap_brokerage_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "C21 is the remaining thin Priority 1 financial capital-return archetype after local supplementation of C22 and the other Priority 1 families. This run adds IBK, KakaoBank and Kyobo Securities while avoiding top-covered C21 symbols 006800, 055550, 086790, 316140, 001510 and 039490."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, financial_ROE_PBR_capital_return_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: financial_ROE_PBR_capital_return_positive, digital_bank_false_stage2, smallcap_brokerage_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, financial_ROE_PBR_capital_return_guardrail, high_MAE_guardrail
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: priority1_canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-web tradable raw OHLC path
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- corporate-action window cleanliness
- C21 financial ROE/PBR capital-return bridge vs false Stage2 / event-cap split
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_ROE_capital_buffer_credit_cost_capital_return_revision_bridge,0,"C21 Stage2 should require ROE durability, capital buffer or CET1 quality, credit-cost discipline, dividend/buyback capacity and revision bridge, not value-up/PBR label alone","IBK positive worked; KakaoBank and Kyobo Securities event/watch rows failed positive-stage promotion","R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE|R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH|R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_bridge_missing_digital_bank_and_smallcap_brokerage_valueup_premiums_as_4B_watch,0,"Digital-bank and small-cap brokerage value-up premiums can peak before ROE, credit-cost, capital policy and revision bridge is proven","KakaoBank had near-zero MFE and deep MAE after January digital-bank PBR watch; Kyobo Securities showed 4B event-cap behavior after February value-up premium","R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH|R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,block_positive_stage_when_financial_valueup_theme_has_high_or_persistent_MAE_without_ROE_capital_return_bridge,0,"High or persistent MAE after bridge-missing C21 entries should block Stage2/Stage3 promotion unless ROE, capital buffer and capital-return evidence survives","KakaoBank MAE90=-30.52 and Kyobo Securities MAE90=-15.87","R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH|R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "case_type": "structural_success_with_later_bank_valueup_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bank value-up / ROE-PBR / dividend and capital-return bridge produced strong 30D/90D MFE from the late-January base with shallow MAE. C21 works when financial value-up is tied to ROE durability, NIM/credit-cost discipline, CET1 or capital buffer, dividend/buyback capacity, valuation gap and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_ROE_CET1_credit_cost_capital_return_revision_bridge_not_valueup_PBR_label_only", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1998/2000/2003 corporate-action candidates. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "case_type": "failed_rerating_digital_bank_ROE_PBR_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital-bank ROE/PBR recovery watch near the January spike had almost no forward MFE and then persistent MAE. C21 Stage2 should not be awarded without ROE durability, deposit/loan growth quality, credit-cost control, capital-return path, platform monetization and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_PBR_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B", "symbol": "030610", "company_name": "교보증권", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Small-cap brokerage value-up/PBR event premium capped after the February spike and then faded. C21 should route bridge-missing brokerage value-up premiums to 4B unless brokerage ROE quality, trading/IB revenue durability, capital policy, dividend/buyback capacity and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_smallcap_brokerage_valueup_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 2020/2023 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE", "case_id": "R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "sector": "bank_valueup_ROE_PBR_dividend_capital_return", "primary_archetype": "ROE_CET1_credit_cost_capital_return_revision_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | financial_ROE_PBR_capital_return_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-29", "entry_date": "2024-01-29", "entry_price": 12100.0, "evidence_available_at_that_date": "bank value-up / low-PBR rerating, ROE durability, dividend/capital-return capacity, capital-buffer and revision bridge proxy after late-January base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["ROE_durability_proxy", "CET1_or_capital_buffer_proxy", "credit_cost_discipline_proxy", "dividend_buyback_capacity_proxy", "revision_bridge_proxy"], "stage3_evidence_fields": ["strong_MFE30", "strong_MFE90", "shallow_initial_MAE"], "stage4b_evidence_fields": ["later_bank_valueup_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 31.74, "MFE_90D_pct": 32.31, "MFE_180D_pct": 32.31, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -1.98, "MAE_90D_pct": -1.98, "MAE_180D_pct": -1.98, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 16010.0, "drawdown_after_peak_pct": -21.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_bank_valueup_valuation_4B_watch_needed", "four_b_evidence_type": ["bank_ROE_PBR_capital_return_bridge", "credit_cost_CET1", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_bank_valueup_ROE_PBR_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1998_2000_2003_CA", "same_entry_group_id": "R6L100_C21_024110_2024-01-29_12100", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH", "case_id": "R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "sector": "digital_bank_ROE_PBR_capital_return_watch", "primary_archetype": "digital_bank_PBR_watch_without_ROE_credit_cost_capital_return_bridge", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | financial_ROE_PBR_capital_return_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-15", "entry_date": "2024-01-15", "entry_price": 31450.0, "evidence_available_at_that_date": "digital bank / financial value-up / PBR recovery watch after January spike without confirmed ROE durability, credit-cost control, deposit-loan quality, platform monetization, capital-return or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_bank_PBR_watch", "platform_bank_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["near_zero_MFE90", "deep_MAE90", "ROE_credit_cost_capital_return_bridge_missing"], "stage4c_evidence_fields": ["ROE_or_credit_cost_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.16, "MFE_90D_pct": 0.16, "MFE_180D_pct": 0.16, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -15.74, "MAE_90D_pct": -30.52, "MAE_180D_pct": -36.25, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-15", "peak_price": 31500.0, "drawdown_after_peak_pct": -36.35, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "digital_bank_ROE_PBR_watch_was_false_stage2_due_missing_ROE_credit_cost_capital_return_revision_bridge", "four_b_evidence_type": ["digital_bank_PBR_premium", "bridge_missing", "near_zero_MFE_deep_MAE"], "four_c_protection_label": "ROE_or_credit_cost_break_watch_only", "trigger_outcome_label": "bad_stage2_digital_bank_ROE_PBR_watch_without_capital_return_bridge", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_PBR_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L100_C21_323410_2024-01-15_31450", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP", "case_id": "R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B", "symbol": "030610", "company_name": "교보증권", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "sector": "smallcap_brokerage_ROE_PBR_valueup_event_premium", "primary_archetype": "smallcap_brokerage_valueup_event_cap_4B", "loop_objective": "priority1_to_50_fill | coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | financial_ROE_PBR_capital_return_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-02-19", "entry_date": "2024-02-19", "entry_price": 5640.0, "evidence_available_at_that_date": "small-cap brokerage value-up / low-PBR event premium without confirmed sustainable brokerage ROE, trading/IB revenue durability, dividend/buyback capacity, capital policy or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_valueup_event", "low_PBR_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "low_MFE90", "meaningful_MAE90", "ROE_capital_return_bridge_recheck"], "stage4c_evidence_fields": ["ROE_or_capital_policy_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/030/030610/2024.csv", "profile_path": "atlas/symbol_profiles/030/030610.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.42, "MFE_90D_pct": 1.42, "MFE_180D_pct": 1.42, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -11.88, "MAE_90D_pct": -15.87, "MAE_180D_pct": -15.87, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-20", "peak_price": 5720.0, "drawdown_after_peak_pct": -17.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.99, "four_b_full_window_peak_proximity": 0.99, "four_b_timing_verdict": "good_full_window_4B_timing_smallcap_brokerage_valueup_event_cap_due_missing_ROE_capital_return_bridge", "four_b_evidence_type": ["smallcap_brokerage_valueup_event_premium", "positioning_overheat", "bridge_missing"], "four_c_protection_label": "ROE_or_capital_policy_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_smallcap_brokerage_valueup_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_smallcap_brokerage_valueup_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2020_2023_CA", "same_entry_group_id": "R6L100_C21_030610_2024-02-19_5640", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R6L100_C21_IBK_2024_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "trigger_id": "R6L100_C21_IBK_2024_STAGE2_ACTIONABLE_BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 30, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 60, "customer_quality_score": 45, "policy_or_regulatory_score": 40, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 40, "backlog_visibility_score": 55, "margin_bridge_score": 65, "revision_score": 60, "relative_strength_score": 80, "customer_quality_score": 65, "policy_or_regulatory_score": 50, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "customer_quality_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "bank_ROE_PBR_capital_return_positive", "MFE_90D_pct": 32.31, "MAE_90D_pct": -1.98, "score_return_alignment_label": "financial_ROE_PBR_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R6L100_C21_KAKAOBANK_2024_DIGITAL_BANK_ROE_PBR_FALSE_STAGE2", "trigger_id": "R6L100_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_ROE_PBR_WATCH", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 15, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 25, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 15, "customer_quality_score": 10, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_bank_ROE_PBR_false_stage2", "MFE_90D_pct": 0.16, "MAE_90D_pct": -30.52, "score_return_alignment_label": "digital_bank_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_PBR_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_2_rolling_calibrated_proxy", "case_id": "R6L100_C21_KYOBOSECU_2024_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP_4B", "trigger_id": "R6L100_C21_KYOBOSECU_2024_STAGE4B_SMALLCAP_BROKERAGE_VALUEUP_EVENT_CAP", "symbol": "030610", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 20, "policy_or_regulatory_score": 35, "valuation_repricing_score": 60, "execution_risk_score": 65, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 85, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "smallcap_brokerage_valueup_event_cap_4B_guard", "MFE_90D_pct": 1.42, "MAE_90D_pct": -15.87, "score_return_alignment_label": "smallcap_brokerage_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_smallcap_brokerage_valueup_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "100", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUATION_FALSE_STAGE2_AND_SMALLCAP_BROKERAGE_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "financial_ROE_PBR_capital_return_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["financial_ROE_PBR_capital_return_positive", "digital_bank_false_stage2", "smallcap_brokerage_event_cap_4B"], "loop_contribution_label": "priority1_canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
```

### 25.6 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all selected rows have usable 180D stock-web windows; no narrative-only price row required","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied calibrated profile.

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
- C21 rows need explicit ROE durability, capital buffer, credit-cost discipline, dividend/buyback capacity and revision bridge before positive promotion.
- In C21, bridge-missing financial value-up rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C21 financial ROE/PBR capital-return rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Selection State

```text
completed_round = R6
completed_loop = 100
completed_canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
coverage_scheduler_status = coverage_index_first
next_selection_rule = re-read V12_Research_No_Repeat_Index.md Priority 1 and local supplements
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
