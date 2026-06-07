# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | capital_return_PBR_guardrail | high_MAE_guardrail | canonical_archetype_compression
output_file = e2r_stock_web_v12_residual_round_R6_loop_98_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
```

This file is the corrected final output for this execution. The scheduler state after R5 loop 98 is R6 / loop 98. R6 is the L6 financial / capital-return / digital-finance round, and this run fills C21 financial ROE/PBR capital-return rather than repeating the immediately preceding R6 loop 97 C22 insurance-reserve file or R6 loop 96 C21 symbol set.

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
capital_return_PBR_guardrail = existing_axis_strengthened
high_MAE_guardrail = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
price_only_blowoff_blocks_positive_stage = existing_axis_kept
```

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 98
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
computed_next_round = R7
computed_next_loop = 98
```

C21 is a financial ROE/PBR and capital-return archetype. A value-up or low-PBR label is the bank signboard; the signal becomes useful only when ROE durability, capital buffer, dividend/buyback mechanics, risk-cost discipline and revision are visible.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat hard key used:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No-Repeat snapshot context:

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN = 51 rows / 19 symbols / good-bad Stage2 22-11 / 4B-4C 7-0
top covered symbols include 006220(5), 016360(5), 071050(4), 105560(4), 138040(4), 139130(4)
previous R6 loop-96 C21 symbols avoided: 029780, 007330, 377300
previous R6 loop-97 C22 symbols avoided: 032830, 088350, 000400
previous R5 loop-98 C20 symbols avoided: 114840, 237880, 406820
```

Selected rows avoid hard duplicates and top repeated C21 symbols:

```text
086790 / Stage2-Actionable / 2024-02-06
323410 / Stage2-Actionable / 2024-02-07
003530 / Stage4B / 2024-03-05
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
| 086790 | atlas/symbol_profiles/086/086790.json | no corporate-action candidate |
| 323410 | atlas/symbol_profiles/323/323410.json | no corporate-action candidate |
| 003530 | atlas/symbol_profiles/003/003530.json | selected 2024 window clean after old 1999/2008/2010/2016/2019 CA candidates |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry in shard | forward 180D | OHLC valid | CA clean | calibration_usable |
|---|---|---:|---|---:|---|---|---|
| R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 086790 | 2024-02-06 | yes | 180 | yes | yes | true |
| R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2 | 323410 | 2024-02-07 | yes | 180 | yes | yes | true |
| R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B | 003530 | 2024-03-05 | yes | 180 | yes | yes | true |

## 6. Canonical Archetype Compression Map

| canonical | fine/deep split | meaning |
|---|---|---|
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE | Positive Stage2 requires ROE durability, CET1/capital buffer, dividend/buyback policy, risk-cost discipline and earnings revision bridge. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | DIGITAL_BANK_VALUEUP_FALSE_STAGE2 | Digital-bank value-up watch without ROE/capital-return/NIM/risk-cost bridge can become false Stage2. |
| C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B | Brokerage/digital-asset premium should route to 4B when revenue conversion, ROE and capital-return bridge are missing. |

## 7. Case Selection Summary

| case_id | symbol | company | role | selected reason |
|---|---|---|---|---|
| R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE | 086790 | 하나금융지주 | positive | Bank ROE/PBR and capital-return bridge produced positive 30D/90D/180D MFE with shallow MAE. |
| R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2 | 323410 | 카카오뱅크 | counterexample | Digital-bank value-up watch had limited MFE and high 90D/180D MAE. |
| R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B | 003530 | 한화투자증권 | counterexample / 4B | Brokerage/digital-asset event premium capped near the March spike and then de-rated. |

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
| Hana Financial bank ROE/PBR capital-return bridge | historical public/report proxy | true | true | shadow-only positive |
| KakaoBank digital-bank value-up false Stage2 | historical public/news proxy | true | true | false-Stage2 guardrail |
| Hanwha Investment brokerage/digital-asset event cap | historical public/news proxy | true | true | 4B overlay counterexample |

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json |
| 003530 | atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv | atlas/symbol_profiles/003/003530.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | role | verdict |
|---|---|---|---:|---:|---|---|
| R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE | 086790 | Stage2-Actionable | 2024-02-06 | 54300 | positive | bank ROE/PBR capital-return bridge worked |
| R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH | 323410 | Stage2-Actionable | 2024-02-07 | 28400 | counterexample | digital-bank value-up false Stage2 |
| R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP | 003530 | Stage4B | 2024-03-05 | 4780 | counterexample/4B | brokerage/digital-asset event cap |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE | 54300 | 19.34 | -2.76 | 20.26 | -4.97 | 27.62 | -4.97 | 2024-08-27 | 69300 | -17.89 |
| R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH | 28400 | 9.86 | -3.87 | 9.86 | -26.76 | 9.86 | -34.89 | 2024-02-15 | 31200 | -40.74 |
| R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP | 4780 | 11.51 | -25.42 | 11.51 | -35.15 | 11.51 | -39.96 | 2024-03-05 | 5330 | -46.15 |

## 13. Current Calibrated Profile Stress Test

| axis | outcome |
|---|---|
| stage2_required_bridge | strengthen: C21 Stage2 needs ROE / capital buffer / capital-return policy / NIM or fee-income / risk-cost / revision bridge |
| capital_return_PBR_guardrail | strengthen: low-PBR or value-up labels alone cannot promote positive stage |
| local_4b_watch_guard | strengthen: bridge-missing digital-bank and brokerage/digital-asset premiums should route to 4B watch |
| high_MAE_guardrail | strengthen: high-MAE C21 rows cannot promote without durable capital-return bridge |
| hard_4c_thesis_break_routes_to_4c | keep |
| full_4b_requires_non_price_evidence | keep |
| price_only_blowoff_blocks_positive_stage | keep |

## 14. Stage2 / Yellow / Green / 4B Comparison

No confirmed Stage3-Green row is introduced. The useful split is whether financial value-up narrative becomes ROE, capital-return and revision evidence.

| symbol | stage quality | explanation |
|---|---|---|
| 086790 | good_stage2_with_later_watch | Bank capital-return bridge produced positive MFE with shallow MAE, but later value-up valuation watch remains necessary. |
| 323410 | bad_stage2 | Digital-bank value-up watch lacked explicit capital-return/ROE bridge and suffered high MAE. |
| 003530 | good_4B | Brokerage/digital-asset event premium peaked on the March spike and then drew down. |

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger
```

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | timing verdict |
|---|---:|---:|---|
| 323410 digital-bank false Stage2 | 0.91 | 0.91 | false Stage2 due missing ROE / capital-return / NIM / risk-cost bridge |
| 003530 brokerage digital-asset cap | 0.90 | 0.90 | good full-window 4B timing after brokerage/digital-asset event premium |
| 086790 bank capital-return bridge | n/a | n/a | positive Stage2, but later financial value-up valuation watch required |

## 16. 4C Protection Audit

```text
4C_case_count = 0
four_c_protection_label = thesis_break_watch_only for 323410 / 003530
```

No hard 4C candidate is introduced in this R6 loop 98 file. The counterexamples are bridge-missing / event-cap rows, not confirmed thesis-break rows.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
rule_scope = sector_specific
rule = In L6 financial ROE/PBR capital-return cases, Stage2 requires verified ROE durability, CET1/capital buffer, dividend/buyback policy, NIM or fee-income durability, risk-cost discipline, and earnings revision bridge. Low-PBR, value-up, digital bank, brokerage, crypto/digital asset or relative-strength label alone remains watch/4B.
proposal_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
rule = C21 should split true ROE/capital-return/revision positives from digital-bank value-up false Stage2 and brokerage/digital-asset event caps. Event-cap rows are 4B overlay/risk calibration, not Stage3-Green promotion evidence.
proposal_status = shadow_only_not_production
```

## 19. Before / After Backtest Comparison

| profile | hypothesis | eligible triggers | avg_MFE90 | avg_MAE90 | false_positive_or_guardrail_rate | verdict |
|---|---|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current profile | 3 | 13.88 | -22.29 | 0.67 | mixed; C21 bridge split needed |
| P0b e2r_2_0_baseline_reference | older baseline | 3 | 13.88 | -22.29 | 0.67 | weaker 4B/Stage2 separation |
| P1 sector_specific_candidate_profile | L6 ROE/capital-return bridge required | 2 | 15.06 | -15.87 | 0.50 | better |
| P2 canonical_archetype_candidate_profile | C21 bridge vs event-cap split | 2 | 15.06 | -15.87 | 0.50 | best explanatory fit |
| P3 counterexample_guard_profile | reject bridge-missing value-up/digital finance themes as positive | 1 | 20.26 | -4.97 | 0.00 | safest but source-proxy blockers remain |

## 20. Score-Return Alignment Matrix

| trigger | score before | stage before | score after | stage after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| 086790 bank capital-return bridge | 66 | Stage2-Watch | 78 | Stage2-Actionable | 20.26 | -4.97 | bank_ROE_PBR_capital_return_positive |
| 323410 digital-bank false | 66 | Stage2-Actionable | 52 | Stage1/Watch | 9.86 | -26.76 | digital_bank_valueup_false_stage2 |
| 003530 brokerage/digital-asset cap | 70 | Stage3-Yellow-like | 54 | Stage4B-watch | 11.51 | -35.15 | brokerage_digital_asset_event_cap_4B_guard |

## 21. Coverage Matrix

```jsonl
{"row_type": "coverage_matrix", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "new_independent_case_count": 3, "reused_case_count": 0, "calibration_usable_trigger_count": 3, "representative_trigger_count": 2, "current_profile_error_count": 2, "sector_rule_candidate": true, "canonical_rule_candidate": true, "coverage_gap_after_this_loop": "Adds R6 loop98 C21: Hana Financial bank ROE/PBR capital-return positive, KakaoBank digital-bank value-up false Stage2, and Hanwha Investment brokerage/digital-asset event-cap 4B while avoiding top repeated C21 and previous R6/R5 loop symbols."}
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
tested_existing_calibrated_axes: stage2_required_bridge, local_4b_watch_guard, capital_return_PBR_guardrail, high_MAE_guardrail, hard_4c_thesis_break_routes_to_4c, full_4b_requires_non_price_evidence, price_only_blowoff_blocks_positive_stage
residual_error_types_found: bank_ROE_PBR_capital_return_positive, digital_bank_valueup_false_stage2, brokerage_digital_asset_event_cap_4B
new_axis_proposed: null
existing_axis_strengthened: stage2_required_bridge, local_4b_watch_guard, capital_return_PBR_guardrail, high_MAE_guardrail
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
shadow_weight,stage2_required_bridge,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,C21_requires_ROE_CET1_capital_return_policy_NIM_risk_cost_revision_bridge,0,"C21 Stage2 should require ROE durability, capital buffer, explicit dividend/buyback or capital-return policy, NIM/fee-income/risk-cost discipline, and earnings revision bridge, not value-up/low-PBR label alone","Hana Financial positive worked; KakaoBank and Hanwha Investment event/watch rows failed positive-stage promotion","R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE|R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH|R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP",3,3,2,low,canonical_shadow_only,"do_not_propose_new_weight_delta=true because source-proxy/evidence-url-pending rows remain"
shadow_weight,local_4b_watch_guard,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,cap_bridge_missing_digital_bank_and_brokerage_event_premiums_as_4B_watch,0,"Digital-bank and brokerage/digital-asset premiums can peak before ROE, NIM, capital-return, revenue conversion and risk-cost bridge is proven","KakaoBank had high MAE after limited value-up bounce; Hanwha Investment showed 4B event-cap behavior after March digital-asset brokerage spike","R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH|R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"4B overlay only; not production"
shadow_weight,high_MAE_guardrail,canonical_archetype,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,configured,block_positive_stage_when_financial_valueup_theme_has_high_or_persistent_MAE_without_capital_return_bridge,0,"High or persistent MAE after bridge-missing C21 entries should block Stage2/Stage3 promotion unless ROE, capital-return and revision evidence survives","KakaoBank MAE90=-26.76 and Hanwha Investment MAE90=-35.15","R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH|R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP",2,2,2,medium,guardrail_shadow_only,"canonical shadow profile only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration", "source_name": "FinanceData/marcap", "tradable_row_count": 14354401, "raw_row_count": 15214118, "symbol_count": 5414, "active_like_symbol_count": 2868, "inactive_or_delisted_like_symbol_count": 2546}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "case_type": "structural_success_with_later_financial_valueup_valuation_watch", "positive_or_counterexample": "positive", "best_trigger": "R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Bank ROE/PBR and capital-return bridge produced positive 30D/90D/180D MFE with shallow early MAE. C21 works when financial value-up narrative maps into ROE durability, CET1/capital buffer, dividend/buyback policy, low PBR re-rating, earnings revision and risk-cost discipline.", "current_profile_verdict": "current_profile_kept_but_C21_positive_requires_ROE_CET1_capital_return_policy_revision_bridge_not_valueup_label_only", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only, so no production weight delta."}
{"row_type": "case", "case_id": "R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "case_type": "failed_rerating_digital_bank_valueup_bridge_missing", "positive_or_counterexample": "counterexample", "best_trigger": "R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Digital-bank / value-up watch had only a short 30D bounce and then persistent high MAE. C21 Stage2 should not be awarded without clear ROE improvement, capital-return policy, margin/NIM or fee-income durability, risk-cost control and revision bridge.", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_valueup_watch_counts_without_ROE_capital_return_NIM_risk_cost_revision_bridge", "price_source": "Songdaiki/stock-web", "notes": "No corporate-action candidate in profile. Source-proxy only."}
{"row_type": "case", "case_id": "R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B", "symbol": "003530", "company_name": "한화투자증권", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "case_type": "event_cap_4b_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "Brokerage / digital-asset event premium capped around the March spike and then de-rated. C21 should route bridge-missing brokerage or digital-asset finance premiums to 4B unless trading-volume revenue conversion, capital allocation, ROE, dividend/buyback policy, risk exposure and revision bridge remain visible.", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_digital_asset_event_premium_not_capped", "price_source": "Songdaiki/stock-web", "notes": "Selected 2024 window clean after old 1999/2008/2010/2016/2019 corporate-action candidates. Source-proxy only."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE", "case_id": "R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "symbol": "086790", "company_name": "하나금융지주", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "sector": "bank_ROE_PBR_valueup_capital_return", "primary_archetype": "ROE_CET1_capital_return_policy_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | capital_return_PBR_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-06", "entry_date": "2024-02-06", "entry_price": 54300.0, "evidence_available_at_that_date": "bank value-up / low-PBR rerating with ROE durability, CET1/capital buffer, dividend/buyback optionality, risk-cost discipline and earnings revision bridge proxy after February base; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_report_proxy", "stage2_evidence_fields": ["ROE_durability_proxy", "CET1_capital_buffer_proxy", "dividend_buyback_policy_proxy", "risk_cost_discipline_proxy", "earnings_revision_bridge_proxy"], "stage3_evidence_fields": ["positive_MFE30", "positive_MFE90", "positive_MFE180", "shallow_MAE90"], "stage4b_evidence_fields": ["later_financial_valueup_valuation_watch", "post_peak_recheck"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv", "profile_path": "atlas/symbol_profiles/086/086790.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.34, "MFE_90D_pct": 20.26, "MFE_180D_pct": 27.62, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -2.76, "MAE_90D_pct": -4.97, "MAE_180D_pct": -4.97, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-27", "peak_price": 69300.0, "drawdown_after_peak_pct": -17.89, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "positive_stage2_but_later_financial_valueup_valuation_4B_watch_needed", "four_b_evidence_type": ["ROE_PBR_capital_return_bridge", "capital_buffer", "valuation_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "good_stage2_bank_ROE_PBR_capital_return_bridge_success", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L98_C21_086790_2024-02-06_54300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH", "case_id": "R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "sector": "digital_bank_valueup_ROE_PBR_watch", "primary_archetype": "digital_bank_valueup_watch_without_ROE_capital_return_NIM_risk_cost_revision_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | capital_return_PBR_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-07", "entry_price": 28400.0, "evidence_available_at_that_date": "digital-bank / financial value-up watch after February policy rerating without confirmed capital-return policy, ROE improvement, NIM/fee-income durability, risk-cost control or revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["digital_bank_valueup_watch", "low_PBR_policy_sympathy", "relative_strength_bounce"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["limited_MFE90", "high_MAE90", "ROE_capital_return_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 9.86, "MFE_90D_pct": 9.86, "MFE_180D_pct": 9.86, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -3.87, "MAE_90D_pct": -26.76, "MAE_180D_pct": -34.89, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-15", "peak_price": 31200.0, "drawdown_after_peak_pct": -40.74, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "digital_bank_valueup_watch_was_false_stage2_due_missing_ROE_capital_return_NIM_risk_cost_revision_bridge", "four_b_evidence_type": ["digital_bank_valueup_premium", "bridge_missing", "high_MAE"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "bad_stage2_digital_bank_valueup_watch_without_ROE_capital_return_bridge", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_valueup_watch_counts_without_ROE_capital_return_NIM_risk_cost_revision_bridge", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_CA_candidate", "same_entry_group_id": "R6L98_C21_323410_2024-02-07_28400", "dedupe_for_aggregate": true, "aggregate_group_role": "representative_false_stage2", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
{"row_type": "trigger", "trigger_id": "R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "case_id": "R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B", "symbol": "003530", "company_name": "한화투자증권", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "sector": "brokerage_digital_asset_trading_revenue_event_premium", "primary_archetype": "brokerage_digital_asset_event_cap_4B", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | capital_return_PBR_guardrail | high_MAE_guardrail | canonical_archetype_compression", "trigger_type": "Stage4B", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 4780.0, "evidence_available_at_that_date": "brokerage / digital-asset event premium without confirmed trading-volume revenue conversion, capital allocation, ROE improvement, shareholder-return policy or risk-exposure revision bridge; exact as-of source URL pending", "evidence_source": "source_proxy_historical_public_news_proxy", "stage2_evidence_fields": ["brokerage_digital_asset_event", "trading_revenue_theme", "relative_strength_spike"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["event_premium_cap", "high_MAE30", "high_MAE90", "ROE_revenue_capital_return_bridge_missing"], "stage4c_evidence_fields": ["thesis_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/003/003530/2024.csv", "profile_path": "atlas/symbol_profiles/003/003530.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 11.51, "MFE_90D_pct": 11.51, "MFE_180D_pct": 11.51, "MFE_1Y_pct": "not_calculated", "MFE_2Y_pct": "not_calculated", "MAE_30D_pct": -25.42, "MAE_90D_pct": -35.15, "MAE_180D_pct": -39.96, "MAE_1Y_pct": "not_calculated", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-05", "peak_price": 5330.0, "drawdown_after_peak_pct": -46.15, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.9, "four_b_full_window_peak_proximity": 0.9, "four_b_timing_verdict": "good_full_window_4B_timing_brokerage_digital_asset_event_cap_due_missing_revenue_ROE_capital_return_bridge", "four_b_evidence_type": ["brokerage_digital_asset_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "event_cap_4B_success_brokerage_digital_asset_event_premium", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_digital_asset_event_premium_not_capped", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_1999_2008_2010_2016_2019_CA", "same_entry_group_id": "R6L98_C21_003530_2024-03-05_4780", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "evidence_url_pending": true, "source_proxy_only": true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L98_C21_HANAFIN_2024_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_POSITIVE", "trigger_id": "R6L98_C21_HANAFIN_2024_STAGE2_ACTIONABLE_BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE", "symbol": "086790", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 65, "customer_quality_score": 45, "policy_or_regulatory_score": 55, "valuation_repricing_score": 55, "execution_risk_score": 45, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Watch", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 55, "margin_bridge_score": 60, "revision_score": 60, "relative_strength_score": 75, "customer_quality_score": 55, "policy_or_regulatory_score": 65, "valuation_repricing_score": 45, "execution_risk_score": 30, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "bank_ROE_PBR_capital_return_positive", "MFE_90D_pct": 20.26, "MAE_90D_pct": -4.97, "score_return_alignment_label": "bank_ROE_PBR_capital_return_positive", "current_profile_verdict": "current_profile_kept_but_source_proxy_blocks_positive_delta"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L98_C21_KAKAOBANK_2024_DIGITAL_BANK_VALUEUP_FALSE_STAGE2", "trigger_id": "R6L98_C21_KAKAOBANK_2024_STAGE2_FALSE_POSITIVE_DIGITAL_BANK_VALUEUP_WATCH", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 5, "backlog_visibility_score": 25, "margin_bridge_score": 25, "revision_score": 25, "relative_strength_score": 65, "customer_quality_score": 30, "policy_or_regulatory_score": 55, "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 35, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 5, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 10, "policy_or_regulatory_score": 20, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 50, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 52, "stage_label_after": "Stage1/Watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "digital_bank_valueup_false_stage2", "MFE_90D_pct": 9.86, "MAE_90D_pct": -26.76, "score_return_alignment_label": "digital_bank_valueup_false_stage2", "current_profile_verdict": "current_profile_false_positive_if_digital_bank_valueup_watch_counts_without_ROE_capital_return_NIM_risk_cost_revision_bridge"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L98_C21_HANWHAINVEST_2024_BROKERAGE_DIGITAL_ASSET_EVENT_CAP_4B", "trigger_id": "R6L98_C21_HANWHAINVEST_2024_STAGE4B_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "symbol": "003530", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 20, "margin_bridge_score": 20, "revision_score": 20, "relative_strength_score": 75, "customer_quality_score": 25, "policy_or_regulatory_score": 35, "valuation_repricing_score": 65, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 5}, "weighted_score_before": 70, "stage_label_before": "Stage3-Yellow-like", "raw_component_scores_after": {"contract_score": 5, "backlog_visibility_score": 5, "margin_bridge_score": 0, "revision_score": 5, "relative_strength_score": 20, "customer_quality_score": 5, "policy_or_regulatory_score": 15, "valuation_repricing_score": 25, "execution_risk_score": 90, "legal_or_contract_risk_score": 60, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10}, "weighted_score_after": 54, "stage_label_after": "Stage4B-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "brokerage_digital_asset_event_cap_4B_guard", "MFE_90D_pct": 11.51, "MAE_90D_pct": -35.15, "score_return_alignment_label": "brokerage_digital_asset_event_cap_4B_guard", "current_profile_verdict": "current_profile_4B_too_late_if_brokerage_digital_asset_event_premium_not_capped"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "98", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_ROE_PBR_CAPITAL_RETURN_BRIDGE_VS_DIGITAL_BANK_VALUEUP_FALSE_STAGE2_AND_BROKERAGE_DIGITAL_ASSET_EVENT_CAP", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 2, "4B_case_count": 1, "4C_case_count": 0, "tested_existing_calibrated_axes": ["stage2_required_bridge", "local_4b_watch_guard", "capital_return_PBR_guardrail", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage", "high_MAE_guardrail"], "residual_error_types_found": ["bank_ROE_PBR_capital_return_positive", "digital_bank_valueup_false_stage2", "brokerage_digital_asset_event_cap_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true, "source_proxy_only_count": 3, "evidence_url_pending_count": 3}
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
- C21 rows need explicit ROE durability, capital buffer, dividend/buyback or capital-return policy, NIM/fee-income durability, risk-cost discipline and earnings revision bridge before positive promotion.
- In C21, bridge-missing financial value-up/digital finance event-premium rows with low MFE or high/persistent MAE should route to 4B/watch, not Stage3.
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

## 27. Next Round State

```text
completed_round = R6
completed_loop = 98
next_round = R7
next_loop = 98
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Main execution prompt: Songdaiki/stock_agent docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- No-repeat index: Songdaiki/stock_agent docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web atlas/manifest.json and per-symbol tradable shards.
- This file contains no investment recommendation and no production scoring change.
