# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_96_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 96 is R6 / loop 96. R6 is the L6 financial/capital-return/digital-finance round, and this run fills C21 financial ROE/PBR capital return rather than repeating the immediately preceding R6 loop 95 C22 insurance-rate cycle file or R6 loop 94 C21 top-repeated bank/brokerage symbols.

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
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 96
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 96
```

C21 is a capital-return and ROE/PBR bridge archetype. A financial value-up or low-PBR label is only the bank lobby; the evidence is payout discipline, ROE durability, risk-cost stability, capital policy, operating leverage, valuation discipline and revision.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 51 rows / 19 symbols / good-bad Stage2 22-11 / 4B-4C 7-0
top covered symbols include 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
previous R6 loop-94 C21 symbols avoided: 055550, 006800, 041190
previous R6 loop-95 C22 symbols avoided: 138040, 244920, 211050
previous R5 loop-96 C18 symbols avoided: 005180, 222040, 103840
```

Selected rows avoid hard duplicates and top repeated C21 symbols:

```text
029780 / Stage2-Actionable / 2024-02-01
007330 / Stage2-Actionable / 2024-04-16
377300 / Stage4B / 2024-01-11
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
| 029780 | atlas/symbol_profiles/029/029780.json | no corporate-action candidate |
| 007330 | atlas/symbol_profiles/007/007330.json | selected 2024 window clean after old 1997/2003 CA candidates |
| 377300 | atlas/symbol_profiles/377/377300.json | no corporate-action candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE | 029780 | 2024-02-01 | yes | 180 | yes | yes | true |
| R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2 | 007330 | 2024-04-16 | yes | 180 | yes | yes | true |
| R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B | 377300 | 2024-01-11 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | CARD_DIVIDEND_VALUEUP_ROE_BRIDGE | Positive Stage2 requires dividend/payout visibility, ROE durability, risk-cost stability, capital policy and revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | SAVINGS_BANK_RATE_FALSE_STAGE2 | Savings-bank/rate value-up watch without ROE, credit-cost and capital-return bridge can become false Stage2. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | FINTECH_VALUEUP_EVENT_CAP_4B | Fintech value-up/profitability event premium should route to 4B when transaction-margin and operating-leverage bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE | 029780 | 삼성카드 | positive | Card dividend/value-up and ROE bridge produced clean MFE with controlled MAE. |
| R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2 | 007330 | 푸른저축은행 | counterexample | Savings-bank value-up/rate watch had limited MFE without ROE/credit-cost/capital-return bridge. |
| R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B | 377300 | 카카오페이 | counterexample / 4B | Fintech value-up event premium capped around the January spike and then drew down sharply. |

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
| Samsung Card dividend/value-up ROE bridge | historical public/report proxy | true | true | shadow-only positive |
| Pureun Savings Bank value-up false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Kakao Pay fintech value-up event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 029780 | atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv | atlas/symbol_profiles/029/029780.json |
| 007330 | atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv | atlas/symbol_profiles/007/007330.json |
| 377300 | atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv | atlas/symbol_profiles/377/377300.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE | 029780 | Stage2-Actionable | 2024-02-01 | 34900 | positive | dividend/value-up ROE bridge worked |
| R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH | 007330 | Stage2-Actionable | 2024-04-16 | 9970 | counterexample | savings-bank value-up false Stage2 |
| R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP | 377300 | Stage4B | 2024-01-11 | 58000 | counterexample/4B | fintech value-up event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE | 34900 | 16.05 | -6.16 | 24.07 | -6.16 | 24.07 | -6.16 | 2024-06-13 | 43300 | -15.01 |
| R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH | 9970 | 5.32 | -9.83 | 5.32 | -14.24 | 5.32 | -14.24 | 2024-04-16 | 10500 | -18.57 |
| R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP | 58000 | 3.79 | -24.05 | 3.79 | -45.34 | 3.79 | -55.00 | 2024-01-11 | 60200 | -56.64 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs dividend/payout / ROE / risk-cost / capital policy / revision bridge |
| local_4b_watch_guard | strengthen: bridge-missing savings-bank and fintech value-up premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE financial value-up rows cannot promote without durable capital-return bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether financial value-up narrative becomes payout, ROE and capital policy evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 029780 | good_stage2_with_later_watch | Dividend/ROE bridge produced clean MFE with controlled MAE. |
| 007330 | bad_stage2 | Savings-bank value-up watch lacked ROE/credit-cost/capital-return bridge and had limited MFE. |
| 377300 | good_4B | Fintech value-up event premium capped on the January spike and then suffered deep MAE. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 007330 savings-bank false Stage2 | 0.95 | 0.95 | false Stage2 due missing ROE/credit-cost/capital-return bridge |
| 377300 fintech value-up cap | 0.96 | 0.96 | good full-window 4B timing after January fintech value-up event premium |
| 029780 card dividend bridge | n/a | n/a | positive Stage2, but later financial value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 007330 / 377300
```

No hard 4C candidate is introduced in this R6 loop 96 file. The counterexamples are bridge-missing / event-cap rows, not hard thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial ROE/PBR capital-return cases, Stage2 requires verified dividend/payout visibility, ROE durability, risk-cost stability, capital-return policy, operating leverage, valuation discipline, or revision bridge. Value-up, PBR, savings-bank, fintech, rate, dividend or platform-profitability label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split true payout/ROE/capital-policy positives from savings-bank value-up false Stage2 and fintech profitability event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 11.06 | -21.91 | 0.67 | mixed; C21 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 11.06 | -21.91 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L6 payout/ROE/capital-policy bridge required | 2 | 14.70 | -10.20 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 14.70 | -10.20 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing financial value-up themes as positive | 1 | 24.07 | -6.16 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 029780 card dividend bridge | 66 | Stage2-Watch | 76 | Stage2-Actionable | 24.07 | -6.16 | card_dividend_valueup_ROE_positive |
| 007330 savings-bank false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 5.32 | -14.24 | savings_bank_valueup_false_stage2 |
| 377300 fintech event cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 3.79 | -45.34 | fintech_valueup_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds C21 Samsung Card dividend/value-up ROE positive, Pureun Savings Bank value-up false Stage2, and Kakao Pay fintech value-up event-cap 4B while avoiding top repeated C21 and previous R6/R5 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: card_dividend_valueup_ROE_positive, savings_bank_valueup_false_stage2, fintech_valueup_event_cap_4B
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_dividend_payout_ROE_risk_cost_capital_policy_revision_bridge,0,"C21 Stage2 should require dividend/payout visibility, ROE durability, risk-cost stability, capital policy, valuation discipline, or revision bridge, not financial value-up/PBR label alone","Samsung Card positive worked; Pureun Savings Bank and Kakao Pay event/watch rows failed positive-stage promotion","R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE|R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH|R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_bridge_missing_savings_bank_and_fintech_valueup_event_premiums_as_4B_watch,0,"Savings-bank and fintech value-up premiums can peak before ROE, risk-cost, capital-return and operating-leverage bridge is proven","Pureun Savings Bank had limited MFE after value-up watch; Kakao Pay showed 4B event-cap behavior after the January fintech spike","R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH|R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,block_positive_stage_when_financial_valueup_theme_has_high_or_persistent_MAE_without_capital_return_bridge,0,"High or persistent MAE after bridge-missing C21 entries should block Stage2/Stage3 promotion unless ROE, payout, risk-cost and capital policy evidence survives","Pureun Savings Bank MAE90=-14.24 and Kakao Pay MAE90=-45.34","R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH|R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "case_type": "structural_success_with_later_financial_valueup_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Credit-card dividend/value-up and stable ROE bridge produced a clean 30D/90D/180D MFE path with controlled MAE. C21 works when the financial ROE/PBR capital-return narrative maps into dividend visibility, payout discipline, risk-cost stability, ROE durability, capital policy and revision bridge.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_dividend_payout_ROE_risk_cost_capital_policy_revision_bridge_not_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2", "symbol": "007330", "company_name": "푸른저축은행", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "case_type": "failed_rerating_savings_bank_rate_valueup_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Savings-bank rate/value-up watch had a short MFE burst but did not prove durable ROE, credit-cost, capital-return or revision bridge. C21 Stage2 should not be awarded without real shareholder-return mechanics and balance-sheet quality.", "current_profile_verdict": "current_profile_false_positive_if_savings_bank_rate_valueup_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1997/2003 corporate-action candidates. Source-proxy only."}
{"row_type": "case", "case_id": "R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Fintech/value-up profitability event premium capped around the January spike and then suffered deep MAE. C21 should route bridge-missing fintech value-up event premiums to 4B unless transaction-margin, user monetization, operating leverage, capital policy, valuation discipline and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_fintech_valueup_profitability_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE", "case_id": "R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "sector": "credit_card_dividend_valueup_ROE_capital_return", "primary_archetype": "dividend_payout_ROE_risk_cost_capital_policy_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 34900.0, "evidence_available_at_that_date": "credit-card dividend/value-up, payout visibility, risk-cost stability, capital-return policy and ROE/PBR revision bridge proxy; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["dividend_payout_proxy", "ROE_durability_proxy", "risk_cost_stability_proxy", "capital_return_policy_proxy", "PBR_discount_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "positive_MFE180", "controlled_MAE90"], "stage4b_evidence_fields": ["later_financial_valueup_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv", "profile_path": "atlas/symbol_profiles/029/029780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.05, "MFE_90D_pct": 24.07, "MFE_180D_pct": 24.07, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -6.16, "MAE_90D_pct": -6.16, "MAE_180D_pct": -6.16, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-13", "peak_price": 43300.0, "drawdown_after_peak_pct": -15.01, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_financial_valueup_valuation_4B_watch_needed", "four_b_evidence_type": ["dividend_ROE_bridge", "capital_return_policy", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_card_dividend_valueup_ROE_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L96_C21_029780_2024-02-01_34900", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH", "case_id": "R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2", "symbol": "007330", "company_name": "푸른저축은행", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "sector": "savings_bank_rate_valueup_ROE_watch", "primary_archetype": "savings_bank_rate_valueup_watch_without_ROE_credit_cost_capital_return_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-16", "entry_date": "2024-04-16", "entry_price": 9970.0, "evidence_available_at_that_date": "savings-bank rate/value-up watch without confirmed ROE durability, credit-cost stability, payout mechanics or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["savings_bank_rate_watch", "financial_valueup_sympathy", "relative_strength_watch"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "credit_cost_capital_return_bridge_missing", "post_watch_drift"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv", "profile_path": "atlas/symbol_profiles/007/007330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.32, "MFE_90D_pct": 5.32, "MFE_180D_pct": 5.32, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -9.83, "MAE_90D_pct": -14.24, "MAE_180D_pct": -14.24, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-16", "peak_price": 10500.0, "drawdown_after_peak_pct": -18.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.95, "four_b_full_window_peak_proximity": 0.95, "four_b_timing_verdict": "savings_bank_valueup_watch_was_false_stage2_due_missing_ROE_credit_cost_capital_return_bridge", "four_b_evidence_type": ["financial_valueup_sympathy", "bridge_missing", "limited_MFE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_savings_bank_rate_valueup_watch_without_ROE_credit_cost_bridge", "current_profile_verdict": "current_profile_false_positive_if_savings_bank_rate_valueup_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1997_2003_CA", "same_entry_group_id": "R6L96_C21_007330_2024-04-16_9970", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP", "case_id": "R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "sector": "fintech_valueup_profitability_event_premium", "primary_archetype": "fintech_valueup_profitability_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-01-11", "entry_date": "2024-01-11", "entry_price": 58000.0, "evidence_available_at_that_date": "fintech/value-up profitability event premium after January financial-platform spike; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["fintech_valueup_event", "platform_profitability_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "deep_MAE30", "deep_MAE90", "transaction_margin_operating_leverage_bridge_recheck"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv", "profile_path": "atlas/symbol_profiles/377/377300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.79, "MFE_90D_pct": 3.79, "MFE_180D_pct": 3.79, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -24.05, "MAE_90D_pct": -45.34, "MAE_180D_pct": -55.0, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-01-11", "peak_price": 60200.0, "drawdown_after_peak_pct": -56.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.96, "four_b_full_window_peak_proximity": 0.96, "four_b_timing_verdict": "good_full_window_4B_timing_fintech_valueup_profitability_event_cap", "four_b_evidence_type": ["fintech_valueup_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_fintech_valueup_profitability_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_fintech_valueup_profitability_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L96_C21_377300_2024-01-11_58000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L96_C21_SAMSUNGCARD_2024_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_POSITIVE", "trigger_id": "R6L96_C21_SAMSUNGCARD_2024_STAGE2_ACTIONABLE_CARD_DIVIDEND_VALUEUP_ROE_BRIDGE", "symbol": "029780", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 35, "policy_or_regulatory_score": 50, "valuation_repricing_score": 60, "execution_risk_score": 50, "legal_or_contract_risk_score": 25, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 45, "margin_bridge_score": 55, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 45, "policy_or_regulatory_score": 60, "valuation_repricing_score": 50, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "execution_risk_score"], "component_delta_explanation": "card_dividend_valueup_ROE_positive", "MFE_90D_pct": 24.07, "MAE_90D_pct": -6.16, "score_return_alignment_label": "card_dividend_valueup_ROE_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L96_C21_PUREUNSB_2024_SAVINGS_BANK_RATE_VALUEUP_FALSE_STAGE2", "trigger_id": "R6L96_C21_PUREUNSB_2024_STAGE2_FALSE_POSITIVE_SAVINGS_BANK_RATE_VALUEUP_WATCH", "symbol": "007330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 20, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 20, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 25, "customer_quality_score": 10, "policy_or_regulatory_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 75, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "savings_bank_valueup_false_stage2", "MFE_90D_pct": 5.32, "MAE_90D_pct": -14.24, "score_return_alignment_label": "savings_bank_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_savings_bank_rate_valueup_watch_counts_without_ROE_credit_cost_capital_return_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L96_C21_KAKAOPAY_2024_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP_4B", "trigger_id": "R6L96_C21_KAKAOPAY_2024_STAGE4B_FINTECH_VALUEUP_PROFITABILITY_EVENT_CAP", "symbol": "377300", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 70, "customer_quality_score": 15, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "fintech_valueup_profitability_event_cap_4B_guard", "MFE_90D_pct": 3.79, "MAE_90D_pct": -45.34, "score_return_alignment_label": "fintech_valueup_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_fintech_valueup_profitability_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "96", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "CARD_DIVIDEND_VALUEUP_ROE_BRIDGE_VS_SAVINGS_BANK_RATE_FALSE_STAGE2_AND_FINTECH_VALUEUP_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["card_dividend_valueup_ROE_positive", "savings_bank_valueup_false_stage2", "fintech_valueup_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C21 rows need explicit dividend/payout visibility, ROE durability, risk-cost stability, capital-return policy, valuation discipline, operating leverage or revision bridge before positive promotion.
- In C21, bridge-missing value-up/fintech event-premium rows with low MFE/high MAE should route to 4B/watch, not Stage3.
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
10. Add tests that bridge-missing C21 financial value-up rows cannot promote positive stages.

### Expected output

- Concise implementation summary.
- Rows accepted/rejected.
- New sector/canonical archetype coverage.
- Existing axis strengthened/weakened/kept.
- No investment recommendation language.

## 27. Next Round State

```text
completed_round = R6
completed_loop = 96
next_round = R7
next_loop = 96
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
