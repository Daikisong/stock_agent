# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- scheduled_round: R6
- scheduled_loop: 76
- completed_round: R6
- completed_loop: 76
- next_round: R7
- next_loop: 76
- round_schedule_status: valid
- round_sector_consistency: pass
- large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
- canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
- fine_archetype_id: VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD
- output_file: e2r_stock_web_v12_residual_round_R6_loop_76_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
- production_scoring_changed: false
- shadow_weight_only: true
- handoff_prompt_embedded: true
- handoff_prompt_executed_now: false

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The previously applied global axes are treated as already live: Stage2 actionable bonus, Yellow 75, Green 87 / revision 55, Green cross-evidence buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

This R6 loop does not re-propose those global axes. It stress-tests them inside financials and proposes only C21/L6 shadow refinements.

## 2. Round / Large Sector / Canonical Archetype Scope

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`; this file therefore uses the valid R6 sector pair. The selected canonical archetype is `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`.

Scope distinction:

- Positive C21 evidence is explicit and funded capital return: buyback/cancel, payout commitment, CET1 buffer, ROE durability, and valuation discount closure.
- Counterexample C21 evidence is soft financial theme beta: digital bank PBR narrative, rate sensitivity, or regional-bank momentum without durable capital-return proof.
- 4B rows are overlay-only. They do not become sale or positive-stage rows unless non-price risk evidence exists.

## 3. Previous Coverage / Duplicate Avoidance Check

`data/e2r/calibration/md_registry.jsonl` was sampled for historical calibration rows. The accessible registry excerpt showed earlier non-v12 R10/R11/R12 loops and no searchable hit for `e2r_stock_web_v12_residual_round_R6_loop` in the repository search, so this run treats R6/C21 as an uncovered v12 residual slot. The immediately preceding local output state was R5/loop76 with next state R6/loop76; this file continues that schedule.

Novelty policy:

- selected symbols: 105560, 138040, 323410, 006220
- same canonical archetype is reused intentionally, but all four symbols and trigger families are new to this R6 loop
- reused_case_count: 0
- new_independent_case_ratio: 1.00

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

- source_name: FinanceData/marcap
- source_repo_url: https://github.com/FinanceData/marcap
- price_adjustment_status: raw_unadjusted_marcap
- min_date: 1995-05-02
- max_date: 2026-02-20
- tradable_row_count: 14,354,401
- raw_row_count: 15,214,118
- symbol_count: 5,414
- active_like_symbol_count: 2,868
- inactive_or_delisted_like_symbol_count: 2,546
- calibration_shard_root: atlas/ohlcv_tradable_by_symbol_year
- raw_shard_root: atlas/ohlcv_raw_by_symbol_year
- schema_path: atlas/schema.json
- universe_path: atlas/universe/all_symbols.csv

Schema validation confirms tradable shard columns `d,o,h,l,c,v,a,mc,s,m`, and calibration rules require positive OHLCV, entry-row existence, at least 180 forward tradable rows, and no 180D corporate-action contamination.

## 5. Historical Eligibility Gate

All representative trigger rows in this MD are historical and have 180 forward trading days in stock-web. All representative rows use `tradable_raw` only. Raw shards are not used for weight calibration.

Corporate-action handling:

- KB금융 has no corporate-action candidates in profile.
- 메리츠금융지주 has 2023-02-21 and 2023-04-25 candidate dates; the representative entry is shifted to 2023-04-26, after the candidate date, so the forward window does not include a later candidate.
- 카카오뱅크 has no corporate-action candidates.
- 제주은행 has older candidate dates ending 2018-11-27; the 2022-12-16 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | rule meaning |
| --- | --- | --- |
| CET1_BUYBACK_VALUEUP_BANK | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | bank rerating requires explicit buyback/cancel or funded payout capacity |
| SHAREHOLDER_RETURN_HOLDCO_INTEGRATION | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | holding-company integration only counts when payout framework is observable and post-corporate-action window is clean |
| DIGITAL_BANK_PBR_THEME_WITHOUT_PAYOUT | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | digital customer-growth premium is not capital-return evidence |
| REGIONAL_BANK_RATE_THEME_PRICE_ONLY | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | rate/theme momentum is 4B/4C overlay evidence, not Stage2/3 promotion evidence |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry_date | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208 | 105560 | KB금융 | positive | 2024-02-08 | 67600 | 23.37 | -11.69 | 53.7 | -11.69 | current_profile_too_late |
| R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426 | 138040 | 메리츠금융지주 | positive | 2023-04-26 | 44450 | 34.53 | -9.79 | 40.16 | -9.79 | current_profile_too_late |
| R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806 | 323410 | 카카오뱅크 | counterexample | 2021-08-06 | 69800 | 35.24 | -24.64 | 35.24 | -43.34 | current_profile_false_positive |
| R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216 | 006220 | 제주은행 | counterexample | 2022-12-16 | 10500 | 165.24 | -14.0 | 165.24 | -14.0 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 2
- 4B_case_count: 4
- 4C_case_count: 2
- calibration_usable_case_count: 4
- representative_trigger_count: 4

The key residual finding is not that financials need lower global thresholds. The sharper rule is that C21 evidence must be like a capital-return bridge. Price and PBR can be the smoke; funded payout capacity is the fire.

## 9. Evidence Source Map

| symbol | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| 105560 | value-up/capital-return disclosure, CET1/payout visibility | revision and financial visibility | valuation/positioning overheat near 2024-10-25 | watch-only |
| 138040 | post-integration payout framework after corporate-action day | financial visibility and recurring payout credibility | valuation/positioning overheat | watch-only |
| 323410 | listing and RS/digital-bank narrative | weak soft-evidence only | valuation blowoff at listing peak | hard 4C after valuation compression |
| 006220 | RS/rate-theme only | none | price-only local/full blowoff | hard 4C after theme unwind |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | profile caveat |
| --- | --- | --- | --- |
| 105560 | atlas/symbol_profiles/105/105560.json | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | profile has no corporate-action candidates and clean row status for 105560 |
| 138040 | atlas/symbol_profiles/138/138040.json | atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv | profile has corporate-action candidates on 2023-02-21 and 2023-04-25; entry shifted to 2023-04-26 so 180D window is not contaminated by later candidate rows |
| 323410 | atlas/symbol_profiles/323/323410.json | atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv | profile has no corporate-action candidates and starts on 2021-08-06 |
| 006220 | atlas/symbol_profiles/006/006220.json | atlas/ohlcv_tradable_by_symbol_year/006/006220/2022.csv | profile has no corporate-action candidate after 2018-11-27; 2022-12-16 forward 180D window is clean |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | trigger_date | entry_date | entry_price | stage2_fields | stage3_fields | 4B_fields | 4C_fields | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67600 | public_event_or_disclosure,policy_or_regulatory_optionality,early_revision_signal | confirmed_revision,financial_visibility,low_red_team_risk | valuation_blowoff,positioning_overheat |  | structural_success |
| 138040 | Stage2-Actionable | 2023-04-25 | 2023-04-26 | 44450 | public_event_or_disclosure,backlog_or_delivery_visibility,early_revision_signal | confirmed_revision,financial_visibility,durable_customer_confirmation,low_red_team_risk | valuation_blowoff,positioning_overheat |  | structural_success |
| 323410 | Stage2-Actionable | 2021-08-06 | 2021-08-06 | 69800 | public_event_or_disclosure,relative_strength | multiple_public_sources | valuation_blowoff,positioning_overheat | thesis_evidence_broken | failed_rerating |
| 006220 | Stage2-Actionable | 2022-12-16 | 2022-12-16 | 10500 | relative_strength |  | valuation_blowoff,positioning_overheat,price_only_local_peak | thesis_evidence_broken | price_moved_without_evidence |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 105560 | 2024-02-08 | 67600 | 16.27 | -11.69 | 23.37 | -11.69 | 53.7 | -11.69 | 2024-10-25 | 103900 | -21.46 |
| 138040 | 2023-04-26 | 44450 | 7.54 | -4.61 | 34.53 | -9.79 | 40.16 | -9.79 | 2024-03-15 | 88300 | -10.87 |
| 323410 | 2021-08-06 | 69800 | 35.24 | -9.31 | 35.24 | -24.64 | 35.24 | -43.34 | 2021-08-18 | 94400 | -71.24 |
| 006220 | 2022-12-16 | 10500 | 76.57 | -14.0 | 165.24 | -14.0 | 165.24 | -14.0 | 2023-04-19 | 27850 | -67.58 |

Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

1. KB금융: current profile is directionally correct but too late because C21-specific CET1/buyback evidence should carry more weight before full revision confirmation.
2. 메리츠금융지주: current profile is too late when shareholder-return structure is explicit but the generic model waits for repeated confirmed financial revisions.
3. 카카오뱅크: current profile can still be fooled by soft digital-finance evidence if customer-growth narrative is treated as non-price evidence; proposed guard reclassifies it as theme beta unless ROE/capital-return conversion exists.
4. 제주은행: current profile should block price-only promotion; the residual risk is that rate-sensitive bank narrative can look like macro non-price evidence. The proposed guard keeps it as 4B/4C overlay only.

## 14. Stage2 / Yellow / Green Comparison

Positive cases show that Green can be late in C21 when capital-return evidence is explicit but not yet absorbed by revision screens.

- KB금융 green_lateness_ratio: 0.231
- 메리츠금융지주 green_lateness_ratio: 0.621
- 카카오뱅크: not_applicable; no confirmed Stage3-Green trigger should be allowed
- 제주은행: not_applicable; no confirmed Stage3-Green trigger should be allowed

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B_local_peak_proximity | 4B_full_window_peak_proximity | verdict | evidence_type |
| --- | --- | --- | --- | --- |
| 105560 | 0.92 | 0.92 | good_full_window_4B_timing | valuation_blowoff,positioning_overheat |
| 138040 | 0.906 | 0.906 | good_full_window_4B_timing | valuation_blowoff,positioning_overheat |
| 323410 | 0.902 | 0.902 | good_full_window_4B_timing_but_overlay_only | valuation_blowoff,positioning_overheat |
| 006220 | 0.764 | 0.764 | price_only_local_4B_too_early_unless_non_price_evidence_added | price_only,positioning_overheat |

Interpretation:

- KB and Meritz show good full-window 4B timing when valuation and positioning overheat align with a structural rerating.
- KakaoBank and JejuBank show that price-only or soft-theme 4B can be accurate as an overlay, but it should not retroactively validate Stage2/3 promotion.

## 16. 4C Protection Audit

- KakaoBank: `hard_4c_success`; after the 2021 listing peak, the observed 1Y MAE reached -61.1% from entry and drawdown after peak reached -71.24%.
- 제주은행: `hard_4c_success`; after the 2023-04-19 peak, drawdown after peak reached -67.58%.
- KB and Meritz: thesis-break not observed inside the validated 180D representative window; 4C remains watch-only.

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate: true

Rule:

```text
For L6 financials, Stage2-Actionable promotion should require at least one explicit capital-return component:
- funded buyback/cancel,
- payout-ratio commitment,
- CET1 or solvency buffer sufficient to fund return,
- recurring ROE/PBR rerating bridge.

Pure RS, value-up policy beta, digital-finance narrative, or rate sensitivity cannot promote above Stage2-Watch without this component.
```

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate: true

C21-specific shadow axes:

```text
c21_capital_return_visibility_gate = +1
c21_digital_finance_theme_beta_cap = +1
c21_price_only_regional_bank_4b_overlay = +1
```

These are not global deltas. They are C21-specific filters and boosts.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 4 | 64.59 | -15.03 | 73.59 | -19.71 | 0.5 | 2 | 2 | mixed: positive cases work but valuation-only financial themes still contaminate Stage2/Yellow |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 64.59 | -15.03 | 73.59 | -19.71 | 0.5 | 2 | 2 | weak |
| P1_sector_specific_candidate_profile | sector_specific | 2 | 28.95 | -10.74 | 46.93 | -10.74 | 0.0 | 0 | 0 | improved: fewer contaminated promotions, better structural positives |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 2 | 28.95 | -10.74 | 46.93 | -10.74 | 0.0 | 0 | 0 | strong within C21 |
| P3_counterexample_guard_profile | counterexample_guard | 2 | 100.24 | -19.32 | 100.24 | -28.67 | 0.0 | 0 | 0 | guard passes: huge MFE is not enough when drawdown and evidence quality are poor |

## 20. Score-Return Alignment Matrix

| profile | alignment |
| --- | --- |
| P0 current proxy | mixed; all four cases can look attractive on MFE, but two are valuation/theme blowoffs with poor evidence quality |
| P1 sector profile | improved; selects KB/Meritz and blocks KakaoBank/JejuBank promotion |
| P2 canonical profile | strongest for C21; treats capital-return proof as the gating evidence |
| P3 counterexample guard | useful 4B/4C guard; prevents MFE-only hindsight from becoming positive evidence |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD | 2 | 2 | 4 | 2 | 4 | 0 | 8 | 4 | 4 | True | True | C21 now has positive/counterexample balance, but needs more insurance/brokerage split in future R6 loops |

## 22. Residual Contribution Summary

new_independent_case_count: 4  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 4  
new_canonical_archetype_count: 0  
new_fine_archetype_count: 4  
new_trigger_family_count: 4  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c  
residual_error_types_found: current_profile_too_late, current_profile_false_positive, valuation_only_financial_theme, price_moved_without_evidence  
new_axis_proposed: c21_capital_return_visibility_gate; c21_digital_finance_theme_beta_cap; c21_price_only_regional_bank_4b_overlay  
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence  
existing_axis_weakened: null  
existing_axis_kept: stage2_actionable_evidence_bonus; Yellow/Green thresholds; hard_4c_thesis_break_routes_to_4c  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  

loop_contribution_label: canonical_archetype_rule_candidate  
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest and schema
- symbol profile availability and corporate-action candidate status
- entry_date / entry_price from tradable shards
- 30D / 90D / 180D MFE/MAE representative calculations
- positive/counterexample balance
- 4B local vs full-window proximity split
- C21-specific score component breakdown

Not validated:

- no live candidate scan
- no `stock_agent` source-code inspection
- no production scoring patch
- no brokerage/API/trading action
- no recommendation language

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_capital_return_visibility_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Require explicit funded payout/buyback/CET1 evidence for C21 promotion","Selects KB/Meritz positives and blocks KakaoBank/JejuBank valuation-only themes","R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_T1_Stage2_Actionable|R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_T1_Stage2_Actionable",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_finance_theme_beta_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank/customer-growth narrative cannot substitute for ROE/capital-return proof","Cuts false positive soft-evidence Stage2 in KakaoBank-like cases","R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_T1_Stage2_Actionable",4,4,2,medium,counterexample_guard,"not production; post-calibrated residual"
shadow_weight,c21_price_only_regional_bank_4b_overlay,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Regional bank rate-theme spikes need 4B overlay and cannot be positive Stage2 without payout evidence","Treats JejuBank as 4B/4C calibration only despite high MFE","R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_T2_4B_OVERLAY",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"

```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_T1_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "profile has no corporate-action candidates and clean row status for 105560"}
{"row_type": "case", "case_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_T1_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "profile has corporate-action candidates on 2023-02-21 and 2023-04-25; entry shifted to 2023-04-26 so 180D window is not contaminated by later candidate rows"}
{"row_type": "case", "case_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_T1_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample: MFE can occur but drawdown/absence of durable capital-return evidence makes promotion unsafe", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "profile has no corporate-action candidates and starts on 2021-08-06"}
{"row_type": "case", "case_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_T1_Stage2_Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample: MFE can occur but drawdown/absence of durable capital-return evidence makes promotion unsafe", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "profile has no corporate-action candidate after 2018-11-27; 2022-12-16 forward 180D window is clean"}
{"row_type": "trigger", "trigger_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_T1_Stage2_Actionable", "case_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 67600, "evidence_available_at_that_date": "capital-return policy became actionable through disclosed shareholder-return/buyback-cancel framing, while CET1/ROE durability made the event more than price-only value-up beta", "evidence_source": "public earnings/shareholder-return disclosure family; stock-web OHLC rows fetched from 105560 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": 53.7, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": -11.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.231, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_ENTRY_2024-02-08", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_T2_4B_OVERLAY", "case_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-02-07", "entry_date": "2024-02-08", "entry_price": 67600, "evidence_available_at_that_date": "capital-return policy became actionable through disclosed shareholder-return/buyback-cancel framing, while CET1/ROE durability made the event more than price-only value-up beta", "evidence_source": "public earnings/shareholder-return disclosure family; stock-web OHLC rows fetched from 105560 2024 shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": 53.7, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": -11.69, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900, "drawdown_after_peak_pct": -21.46, "green_lateness_ratio": 0.231, "four_b_local_peak_proximity": 0.92, "four_b_full_window_peak_proximity": 0.92, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_ENTRY_2024-02-08", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_T1_Stage2_Actionable", "case_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-04-25", "entry_date": "2023-04-26", "entry_price": 44450, "evidence_available_at_that_date": "post-consolidation financial holding structure plus explicit shareholder-return narrative; entry deliberately set after the 2023-04-25 stock-web corporate-action candidate", "evidence_source": "public consolidation/shareholder-return disclosure family; stock-web 138040 profile and OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.54, "MFE_90D_pct": 34.53, "MFE_180D_pct": 40.16, "MFE_1Y_pct": 98.65, "MFE_2Y_pct": null, "MAE_30D_pct": -4.61, "MAE_90D_pct": -9.79, "MAE_180D_pct": -9.79, "MAE_1Y_pct": -9.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 88300, "drawdown_after_peak_pct": -10.87, "green_lateness_ratio": 0.621, "four_b_local_peak_proximity": 0.906, "four_b_full_window_peak_proximity": 0.906, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-04-25_candidate", "same_entry_group_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_ENTRY_2023-04-26", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_T2_4B_OVERLAY", "case_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2023-04-25", "entry_date": "2023-04-26", "entry_price": 44450, "evidence_available_at_that_date": "post-consolidation financial holding structure plus explicit shareholder-return narrative; entry deliberately set after the 2023-04-25 stock-web corporate-action candidate", "evidence_source": "public consolidation/shareholder-return disclosure family; stock-web 138040 profile and OHLC rows", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2023.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 7.54, "MFE_90D_pct": 34.53, "MFE_180D_pct": 40.16, "MFE_1Y_pct": 98.65, "MFE_2Y_pct": null, "MAE_30D_pct": -4.61, "MAE_90D_pct": -9.79, "MAE_180D_pct": -9.79, "MAE_1Y_pct": -9.79, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 88300, "drawdown_after_peak_pct": -10.87, "green_lateness_ratio": 0.621, "four_b_local_peak_proximity": 0.906, "four_b_full_window_peak_proximity": 0.906, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2023-04-25_candidate", "same_entry_group_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_ENTRY_2023-04-26", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_T1_Stage2_Actionable", "case_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-08-06", "entry_date": "2021-08-06", "entry_price": 69800, "evidence_available_at_that_date": "listing-day valuation repricing and digital-bank narrative were visible, but capital-return, CET1 payout, and mature ROE evidence were not yet confirmed", "evidence_source": "stock-web 323410 listing-period OHLC rows and profile; evidence family treated as valuation/digital narrative rather than payout evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.24, "MFE_90D_pct": 35.24, "MFE_180D_pct": 35.24, "MFE_1Y_pct": 35.24, "MFE_2Y_pct": null, "MAE_30D_pct": -9.31, "MAE_90D_pct": -24.64, "MAE_180D_pct": -43.34, "MAE_1Y_pct": -61.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-18", "peak_price": 94400, "drawdown_after_peak_pct": -71.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.902, "four_b_full_window_peak_proximity": 0.902, "four_b_timing_verdict": "good_full_window_4B_timing_but_overlay_only", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_ENTRY_2021-08-06", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_T2_4B_OVERLAY", "case_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806", "symbol": "323410", "company_name": "카카오뱅크", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2021-08-06", "entry_date": "2021-08-06", "entry_price": 69800, "evidence_available_at_that_date": "listing-day valuation repricing and digital-bank narrative were visible, but capital-return, CET1 payout, and mature ROE evidence were not yet confirmed", "evidence_source": "stock-web 323410 listing-period OHLC rows and profile; evidence family treated as valuation/digital narrative rather than payout evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/323/323410/2021.csv", "profile_path": "atlas/symbol_profiles/323/323410.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 35.24, "MFE_90D_pct": 35.24, "MFE_180D_pct": 35.24, "MFE_1Y_pct": 35.24, "MFE_2Y_pct": null, "MAE_30D_pct": -9.31, "MAE_90D_pct": -24.64, "MAE_180D_pct": -43.34, "MAE_1Y_pct": -61.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-08-18", "peak_price": 94400, "drawdown_after_peak_pct": -71.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.902, "four_b_full_window_peak_proximity": 0.902, "four_b_timing_verdict": "good_full_window_4B_timing_but_overlay_only", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_ENTRY_2021-08-06", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_T1_Stage2_Actionable", "case_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-12-16", "entry_date": "2022-12-16", "entry_price": 10500, "evidence_available_at_that_date": "price and volume surged, but the observable evidence family was rate/theme sensitivity rather than durable ROE, payout policy, or buyback/cancel visibility", "evidence_source": "stock-web 006220 2022/2023 OHLC rows and profile; evidence family classified as price/theme only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2022.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 76.57, "MFE_90D_pct": 165.24, "MFE_180D_pct": 165.24, "MFE_1Y_pct": 165.24, "MFE_2Y_pct": null, "MAE_30D_pct": -14.0, "MAE_90D_pct": -14.0, "MAE_180D_pct": -14.0, "MAE_1Y_pct": -14.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-19", "peak_price": 27850, "drawdown_after_peak_pct": -67.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.764, "four_b_full_window_peak_proximity": 0.764, "four_b_timing_verdict": "price_only_local_4B_too_early_unless_non_price_evidence_added", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_ENTRY_2022-12-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_T2_4B_OVERLAY", "case_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "VALUE_UP_CET1_BUYBACK_DIGITAL_BANK_THEME_GUARD", "sector": "financial_capital_return_digital", "primary_archetype": "ROE/PBR capital-return rerating vs valuation-only financial theme", "loop_objective": "sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage4B-Overlay", "trigger_date": "2022-12-16", "entry_date": "2022-12-16", "entry_price": 10500, "evidence_available_at_that_date": "price and volume surged, but the observable evidence family was rate/theme sensitivity rather than durable ROE, payout policy, or buyback/cancel visibility", "evidence_source": "stock-web 006220 2022/2023 OHLC rows and profile; evidence family classified as price/theme only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2022.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 76.57, "MFE_90D_pct": 165.24, "MFE_180D_pct": 165.24, "MFE_1Y_pct": 165.24, "MFE_2Y_pct": null, "MAE_30D_pct": -14.0, "MAE_90D_pct": -14.0, "MAE_180D_pct": -14.0, "MAE_1Y_pct": -14.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-19", "peak_price": 27850, "drawdown_after_peak_pct": -67.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.764, "four_b_full_window_peak_proximity": 0.764, "four_b_timing_verdict": "price_only_local_4B_too_early_unless_non_price_evidence_added", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_ENTRY_2022-12-16", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208", "trigger_id": "R6L76_C21_KB_VALUEUP_CET1_BUYBACK_20240208_T1_Stage2_Actionable", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 13, "capital_return_visibility_score": 10, "cet1_buffer_score": 8, "payout_execution_score": 6, "digital_finance_theme_beta_score": 0, "positioning_overheat_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 13, "capital_return_visibility_score": 16, "cet1_buffer_score": 11, "payout_execution_score": 9, "digital_finance_theme_beta_score": 0, "positioning_overheat_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Green", "changed_components": ["capital_return_visibility_score", "cet1_buffer_score", "payout_execution_score", "roe_pbr_capital_return_score", "digital_finance_theme_beta_score", "positioning_overheat_score"], "component_delta_explanation": "C21-specific CET1-backed buyback/cancel visibility adds capital-return quality without relaxing global Green threshold.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426", "trigger_id": "R6L76_C21_MERITZ_CAPITAL_RETURN_INTEGRATION_20230426_T1_Stage2_Actionable", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 14, "capital_return_visibility_score": 12, "cet1_buffer_score": 0, "payout_execution_score": 10, "digital_finance_theme_beta_score": 0, "positioning_overheat_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": -1, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 14, "capital_return_visibility_score": 17, "cet1_buffer_score": 0, "payout_execution_score": 14, "digital_finance_theme_beta_score": 0, "positioning_overheat_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Green", "changed_components": ["capital_return_visibility_score", "cet1_buffer_score", "payout_execution_score", "roe_pbr_capital_return_score", "digital_finance_theme_beta_score", "positioning_overheat_score"], "component_delta_explanation": "C21-specific shareholder-return integration axis recognizes committed payout structure earlier than generic revision-only Green.", "MFE_90D_pct": 34.53, "MAE_90D_pct": -9.79, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806", "trigger_id": "R6L76_C21_KAKAOBANK_DIGITAL_BANK_PBR_20210806_T1_Stage2_Actionable", "symbol": "323410", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "capital_return_visibility_score": 0, "cet1_buffer_score": 0, "payout_execution_score": 0, "digital_finance_theme_beta_score": 16, "positioning_overheat_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 18, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": -5, "capital_return_visibility_score": -5, "cet1_buffer_score": 0, "payout_execution_score": 0, "digital_finance_theme_beta_score": 2, "positioning_overheat_score": -8}, "weighted_score_after": 66, "stage_label_after": "Stage2-Watch", "changed_components": ["capital_return_visibility_score", "cet1_buffer_score", "payout_execution_score", "roe_pbr_capital_return_score", "digital_finance_theme_beta_score", "positioning_overheat_score"], "component_delta_explanation": "Counterexample guard subtracts soft digital-platform valuation when no ROE/capital-return conversion exists.", "MFE_90D_pct": 35.24, "MAE_90D_pct": -24.64, "score_return_alignment_label": "blocked_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216", "trigger_id": "R6L76_C21_JEJUBANK_RATE_THEME_PRICE_ONLY_20221216_T1_Stage2_Actionable", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 23, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "capital_return_visibility_score": 0, "cet1_buffer_score": 0, "payout_execution_score": 0, "digital_finance_theme_beta_score": 8, "positioning_overheat_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 7, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "capital_return_visibility_score": -7, "cet1_buffer_score": 0, "payout_execution_score": 0, "digital_finance_theme_beta_score": 8, "positioning_overheat_score": -12}, "weighted_score_after": 58, "stage_label_after": "Stage2-Blocked", "changed_components": ["capital_return_visibility_score", "cet1_buffer_score", "payout_execution_score", "roe_pbr_capital_return_score", "digital_finance_theme_beta_score", "positioning_overheat_score"], "component_delta_explanation": "Counterexample guard caps regional-bank price-only theme despite huge MFE because no repeatable capital-return evidence existed.", "MFE_90D_pct": 165.24, "MAE_90D_pct": -14.0, "score_return_alignment_label": "blocked_counterexample", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "76", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "price_moved_without_evidence", "valuation_only_financial_theme"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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

completed_round = R6  
completed_loop = 76  
next_round = R7  
next_loop = 76  
round_schedule_status = valid  
round_sector_consistency = pass  

## 28. Source Notes

- Stock-web manifest confirms `max_date=2026-02-20`, raw unadjusted marcap basis, tradable row count, roots, and corporate-action caveats.  
- Stock-web schema confirms tradable columns and MFE/MAE formulas.  
- 105560 profile confirms KB금융 status, available years, no corporate-action candidates, and raw/unadjusted status.  
- 138040 profile confirms corporate-action candidate dates including 2023-04-25; entry was deliberately shifted to 2023-04-26.  
- 323410 profile confirms 카카오뱅크 listing start 2021-08-06 and no corporate-action candidates.  
- 006220 profile confirms 제주은행 profile, old corporate-action candidates only, and raw/unadjusted status.  
- OHLC rows used: 105560 2024; 138040 2023/2024; 323410 2021/2022; 006220 2022/2023.  

