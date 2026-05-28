# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R11
loop = 13
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
fine_archetype_id = KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_ALIGNMENT
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This is historical residual calibration only. It is not live stock discovery, not an investment recommendation, not a `stock_agent` code patch, and not a production scoring change.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The test is not “does Stage2 beat Green again?” The residual question is narrower: in C31 policy-event cases, when does a public policy programme become an issuer-level rerating signal, and when is it only a low-PBR heat lamp that warms the surface while the actual balance sheet remains cold?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R11
large_sector_id = L10_POLICY_EVENT_CROSS_REDTEAM_MISC
canonical_archetype_id = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
selected_theme = Korea Corporate Value-up Programme, 2024
loop_objective =
  residual_false_positive_mining
  sector_specific_rule_discovery
  canonical_archetype_compression
  counterexample_mining
  coverage_gap_fill
```

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifacts were used only for coverage and duplicate avoidance. The calibration ingest summary shows broad R1-R13 coverage and prior applied global axes; the applied scoring diff already contains the global Stage2/Yellow/Green/4B/4C changes, so this MD does not re-propose those axes.

```text
artifact_check_result = no_duplicate_found_for_C31_Value-up_105560_005380_015760_028260
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
new_canonical_archetype_count = 1
new_trigger_family_count = 3
auto_selected_coverage_gap = R11/L10/C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest fields verified:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

## 5. Historical Eligibility Gate

| symbol | profile_path | entry_date | 180D forward available | corporate_action_window_status | calibration_usable |
|---:|---|---:|---|---|---|
| 105560 | atlas/symbol_profiles/105/105560.json | 2024-02-27 | true | clean_180D_window | true |
| 005380 | atlas/symbol_profiles/005/005380.json | 2024-02-27 | true | clean_180D_window | true |
| 015760 | atlas/symbol_profiles/015/015760.json | 2024-02-27 | true | clean_180D_window | true |
| 028260 | atlas/symbol_profiles/028/028260.json | 2024-02-27 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| KOREA_VALUE_UP_BANK_CAPITAL_RETURN_ALIGNMENT | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy event plus issuer-level capital-return capacity. |
| KOREA_VALUE_UP_AUTO_SHAREHOLDER_RETURN_WITH_OPERATING_SUPPORT | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy event plus later explicit buyback/dividend path and operating margin support. |
| KOREA_VALUE_UP_LOW_PBR_REGULATED_UTILITY_GUARD | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Policy-only low-PBR signal blocked by tariff/debt/regulatory constraint. |
| KOREA_VALUE_UP_HOLDING_COMPANY_GOVERNANCE_DISCOUNT_GUARD | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | Holding-company/chaebol discount does not close merely because a policy programme exists. |

## 7. Case Selection Summary

| case_id | symbol | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
|---|---:|---|---:|---:|---:|---:|---:|---|
| R11L13_C31_KVU_KB_105560_20240226 | 105560 | structural_success / positive | 62400 | 44.23 | -2.4 | 66.51 | -2.4 | current_profile_correct |
| R11L13_C31_KVU_HYUNDAI_005380_20240226 | 005380 | high_mae_success / positive | 238500 | 25.58 | -10.06 | 25.58 | -17.27 | current_profile_correct |
| R11L13_C31_KVU_KEPCO_015760_20240226 | 015760 | false_positive_green / counterexample | 24200 | 5.17 | -21.45 | 5.17 | -22.4 | current_profile_false_positive |
| R11L13_C31_KVU_SCT_028260_20240226 | 028260 | failed_rerating / counterexample | 147400 | 15.88 | -12.14 | 15.88 | -21.44 | current_profile_false_positive |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 4
minimum_new_independent_case_ratio = 1.00
```

The case set intentionally pairs the same policy event with opposite transmission quality. KB금융 and 현대차 turn the policy event into issuer-level capital allocation. 한국전력 and 삼성물산 show why a broad low-PBR label can be a mirage: the headline points at value, but the balance sheet, tariff regime, or governance discount decides whether value can actually be released.

## 9. Evidence Source Map

| case_id | trigger_date | evidence available at trigger | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---:|---|---|---|---|---|
| R11L13_C31_KVU_KB_105560_20240226 | 2024-02-26 | Corporate Value-up programme and low-PBR shareholder-return expectation. | policy event, early revision, issuer capital-return ability | financial visibility, low red-team risk | later valuation/positioning overheat | none |
| R11L13_C31_KVU_HYUNDAI_005380_20240226 | 2024-02-26 | Corporate Value-up programme and auto low-PBR repricing. | policy event, relative strength, early revision | operating support; later explicit shareholder-return policy | later positioning overheat | none |
| R11L13_C31_KVU_KEPCO_015760_20240226 | 2024-02-26 | Corporate Value-up programme and low-PBR utility narrative. | policy event only | none | tariff/debt/regulatory block; event cap | none |
| R11L13_C31_KVU_SCT_028260_20240226 | 2024-02-26 | Corporate Value-up programme and holding-company low-PBR narrative. | policy event and relative strength | none | governance discount/event cap | none |

## 10. Price Data Source Map

| symbol | company | shard | profile | entry row |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-27 close 62,400 |
| 005380 | 현대차 | atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv | atlas/symbol_profiles/005/005380.json | 2024-02-27 close 238,500 |
| 015760 | 한국전력 | atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv | atlas/symbol_profiles/015/015760.json | 2024-02-27 close 24,200 |
| 028260 | 삼성물산 | atlas/ohlcv_tradable_by_symbol_year/028/028260/2024.csv | atlas/symbol_profiles/028/028260.json | 2024-02-27 close 147,400 |

## 11. Case-by-Case Trigger Grid

| case_id | symbol | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
|---|---:|---|---:|---:|---:|---:|---:|---|
| R11L13_C31_KVU_KB_105560_20240226 | 105560 | structural_success / positive | 62400 | 44.23 | -2.4 | 66.51 | -2.4 | current_profile_correct |
| R11L13_C31_KVU_HYUNDAI_005380_20240226 | 005380 | high_mae_success / positive | 238500 | 25.58 | -10.06 | 25.58 | -17.27 | current_profile_correct |
| R11L13_C31_KVU_KEPCO_015760_20240226 | 015760 | false_positive_green / counterexample | 24200 | 5.17 | -21.45 | 5.17 | -22.4 | current_profile_false_positive |
| R11L13_C31_KVU_SCT_028260_20240226 | 028260 | failed_rerating / counterexample | 147400 | 15.88 | -12.14 | 15.88 | -21.44 | current_profile_false_positive |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| R11L13_C31_KVU_KB_105560_STAGE2A_20240226 | 2024-02-27 | 62400 | 25.96 | -2.4 | 44.23 | -2.4 | 66.51 | -2.4 | 2024-10-25 | 103900 | -15.01 |
| R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226 | 2024-02-27 | 238500 | 9.01 | -10.06 | 25.58 | -10.06 | 25.58 | -17.27 | 2024-06-28 | 299500 | -34.12 |
| R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226 | 2024-02-27 | 24200 | 5.17 | -12.81 | 5.17 | -21.45 | 5.17 | -22.4 | 2024-03-14 | 25450 | -26.21 |
| R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226 | 2024-02-27 | 147400 | 15.88 | -0.27 | 15.88 | -12.14 | 15.88 | -21.44 | 2024-03-14 | 170800 | -32.2 |


Calculation basis:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
entry_date = 2024-02-27 next tradable close, because the 2024-02-26 policy package had uncertain intraday actionability for all issuers.
price_basis = tradable_raw
```

## 13. Current Calibrated Profile Stress Test

| case_id | expected current profile behavior | actual path | verdict |
|---|---|---|---|
| KB금융 | Stage2-Actionable → Yellow/near-Green when capital-return capacity is visible. | MFE180 +66.51%, MAE180 -2.40%. | current_profile_correct |
| 현대차 | Stage2-Actionable positive, but high-MAE risk after policy rally. | MFE180 +25.58%, MAE180 -17.27%. | current_profile_correct |
| 한국전력 | May be over-promoted if policy/low-PBR label is treated as enough evidence. | MFE180 +5.17%, MAE180 -22.40%. | current_profile_false_positive |
| 삼성물산 | May be over-promoted if holding-company discount is treated as mechanically unlockable. | MFE180 +15.88%, MAE180 -21.44%. | current_profile_false_positive |

Axis tests:

```text
stage2_actionable_evidence_bonus = existing_axis_tested / kept
stage3_yellow_total_min = existing_axis_tested / kept
stage3_green_total_min = existing_axis_tested / kept
stage3_green_revision_min = existing_axis_tested / kept
stage3_cross_evidence_green_buffer = existing_axis_tested / kept
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened within C31
full_4b_requires_non_price_evidence = existing_axis_strengthened within C31
hard_4c_thesis_break_routes_to_4c = existing_axis_kept, but no hard 4C found in this loop
```

## 14. Stage2 / Yellow / Green Comparison

There is no clean confirmed Stage3-Green trigger at 2024-02-26 for the counterexamples. For KB금융 and 현대차, Stage2-Actionable is valid before full issuer-level filings, but C31 should not promote to full Green until the issuer-level capital-return plan, ROE/profitability, or dividend/buyback capacity is visible.

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger on 2024-02-26; this loop tests policy-event Stage2/Yellows and false-positive Green prevention.
```

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | full observed-cycle peak | 4B evidence type | verdict |
|---|---:|---:|---|---|
| KB금융 | 2024-10-25 103,900 | 2024-10-25 103,900 | valuation_blowoff, positioning_overheat | 4B overlay only; not part of entry calibration |
| 현대차 | 2024-06-28 299,500 | 2024-06-28 299,500 | positioning_overheat, drawdown after peak | 4B overlay useful; high drawdown after positive MFE |
| 한국전력 | 2024-03-14 25,450 | 2024-03-14 25,450 | legal_or_regulatory_block, event_cap | good local 4B risk overlay; not full 4C |
| 삼성물산 | 2024-03-14 170,800 | 2024-03-14 170,800 | event_cap, governance-discount persistence | good local 4B risk overlay; not full 4C |

## 16. 4C Protection Audit

No hard 4C is proposed in this loop. The counterexamples are not thesis-break events like delisting, accounting fraud, forced liquidation, trial failure, or contract cancellation. They are policy-event non-transmission failures. Therefore they train 4B/counterexample guardrails, not hard 4C.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = case set is single large_sector_id L10; rule is better scoped to canonical_archetype_id C31, not all L10 policy/event cases.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
canonical_rule_id = c31_policy_event_requires_issuer_level_transmission
scope = C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

Candidate rule:

> In C31, a public policy, subsidy, index, legislation, or regulator speech can produce Stage2-Actionable only. It may not promote to Yellow/Green unless issuer-level transmission is visible: capital return, binding incentive, revenue/profit conversion, permitted tariff/pass-through, or balance-sheet repair. Low-PBR/policy narrative without issuer-level transmission should be capped at Stage2-Watch and may receive 4B overlay after local price overheat.

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | score-return alignment |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 22.72 | -11.51 | 28.29 | -15.89 | 0.50 | mixed; policy-only cases can still over-promote |
| P0b e2r_2_0_baseline_reference | 4 | 22.72 | -11.51 | 28.29 | -15.89 | 0.50 | worse; too willing to treat broad event as positive |
| P1 sector_specific_candidate_profile | 4 | 22.72 | -11.51 | 28.29 | -15.89 | 0.50 | no sector-wide rule proposed |
| P2 canonical_archetype_candidate_profile | 4 | 34.91 positive bucket / 10.53 counter bucket | -6.23 positive bucket / -16.80 counter bucket | 46.05 positive / 10.53 counter | -9.84 positive / -21.92 counter | 0.00 after guard | improved by issuer-level-transmission gate |
| P3 counterexample_guard_profile | 2 counterexamples | 10.53 | -16.80 | 10.53 | -21.92 | 0.00 after cap | policy-only low-PBR cases capped at Stage2-Watch/4B overlay |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| KB금융 | 84.0 | Stage3-Yellow | 88.5 | Stage3-Green-shadow | Strong: +66.51% MFE180 with shallow MAE |
| 현대차 | 85.0 | Stage3-Yellow | 88.0 | Stage3-Green-shadow-with-high-MAE-flag | Positive but volatile: +25.58% MFE180 / -17.27% MAE180 |
| 한국전력 | 77.0 | Stage3-Yellow false-positive risk | 63.0 | Stage2-Watch / 4B-risk-overlay | Better: avoids +5.17% MFE / -22.40% MAE false Green |
| 삼성물산 | 78.0 | Stage3-Yellow false-positive risk | 64.0 | Stage2-Watch / 4B-risk-overlay | Better: avoids local-rally-only false promotion |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L10_POLICY_EVENT_CROSS_REDTEAM_MISC | C31_POLICY_SUBSIDY_LEGISLATION_EVENT | KOREA_VALUE_UP_POLICY_CAPITAL_RETURN_ALIGNMENT | 2 | 2 | 2 | 0 | 4 | 0 | 4 | 4 | 2 | false | true | C31 now has issuer-level positive and policy-only counterexample balance; next gap is C32 governance/control-premium tender-cap. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - policy_only_low_pbr_false_positive
  - issuer_level_capital_return_gap
  - regulated_utility_balance_sheet_constraint
  - holding_company_governance_discount_not_closed
new_axis_proposed:
  - c31_issuer_level_capital_return_required
  - c31_policy_only_low_pbr_guard
  - c31_4b_event_detail_disappointment_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence within C31
  - price_only_blowoff_blocks_positive_stage within C31
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: R11/L10/C31_POLICY_SUBSIDY_LEGISLATION_EVENT
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- historical trigger date = 2024-02-26
- next-trading-day entry = 2024-02-27 close
- stock-web tradable_raw rows used
- 30D / 90D / 180D MFE/MAE calculated
- clean 180D corporate-action windows checked via symbol profiles
- C31 positive/counterexample separation tested
```

Not validated:

```text
- live 2026 candidates
- broker API execution
- current watchlist
- production scoring code
- exact intraday disclosure-time actionability
- tax-law implementation as a legal conclusion
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_issuer_level_capital_return_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy event should promote only when issuer-level buyback/dividend/ROE or self-funded capital return path exists.","Improves KB/Hyundai vs KEPCO/Samsung C&T separation","R11L13_C31_KVU_KB_105560_STAGE2A_20240226|R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226|R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226|R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_only_low_pbr_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Low PBR plus government programme is not enough when regulated utility debt/tariff or holding-company governance discount remains unresolved.","Reduces false positive Stage3-Yellow/Green on KEPCO and Samsung C&T",R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226|R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226,2,2,2,medium,canonical_shadow_guard,"not production; post-calibrated residual"
shadow_weight,c31_4b_event_detail_disappointment_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"If details remain voluntary/non-binding after policy rally, classify as 4B overlay not full positive continuation.","Improves local peak interpretation for policy-only rerating",R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226|R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226,2,2,2,low,canonical_shadow_guard,"requires more holdout cases"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R11L13_C31_KVU_KB_105560_20240226","symbol":"105560","company_name":"KB금융","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_ALIGNMENT","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_KVU_KB_105560_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"strong_positive_alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Clean stock-web profile; no corporate action candidate dates in 180D window."}
{"row_type":"case","case_id":"R11L13_C31_KVU_HYUNDAI_005380_20240226","symbol":"005380","company_name":"현대차","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_AUTO_SHAREHOLDER_RETURN_WITH_OPERATING_SUPPORT","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_but_high_mae","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Clean 180D corporate-action window; old profile has only 1998-1999 corporate-action candidates."}
{"row_type":"case","case_id":"R11L13_C31_KVU_KEPCO_015760_20240226","symbol":"015760","company_name":"한국전력","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_LOW_PBR_REGULATED_UTILITY_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"No corporate action candidates; clean 180D window."}
{"row_type":"case","case_id":"R11L13_C31_KVU_SCT_028260_20240226","symbol":"028260","company_name":"삼성물산","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_HOLDING_COMPANY_GOVERNANCE_DISCOUNT_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"2015 corporate-action candidate only; clean 180D window for 2024 trigger."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R11L13_C31_KVU_KB_105560_STAGE2A_20240226","case_id":"R11L13_C31_KVU_KB_105560_20240226","symbol":"105560","company_name":"KB금융","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_BANK_CAPITAL_RETURN_ALIGNMENT","sector":"정책·지정학·재난·이벤트","primary_archetype":"Korea Corporate Value-up policy event / issuer-level capital-return transmission","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"2024-02-26 Corporate Value-up package; low-PBR banks were explicitly connected to shareholder-return policy expectations. Case requires issuer-level ROE/capital-return ability, not policy label alone.","evidence_source":"Reuters/FT/FSC Value-up coverage; issuer capital-return history treated as issuer-level confirmation.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":62400,"MFE_30D_pct":25.96,"MFE_90D_pct":44.23,"MFE_180D_pct":66.51,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.4,"MAE_90D_pct":-2.4,"MAE_180D_pct":-2.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-15.01,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_for_positive_entry","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"policy_plus_issuer_capital_return_structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_KVU_KB_105560_20240226::2024-02-27::62400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226","case_id":"R11L13_C31_KVU_HYUNDAI_005380_20240226","symbol":"005380","company_name":"현대차","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_AUTO_SHAREHOLDER_RETURN_WITH_OPERATING_SUPPORT","sector":"정책·지정학·재난·이벤트","primary_archetype":"Korea Corporate Value-up policy event / issuer-level capital-return transmission","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Policy event aligned with automaker low-PBR repricing; later investor-day buyback/dividend plan confirmed issuer-level shareholder-return path.","evidence_source":"Corporate Value-up coverage plus Reuters 2024-08-28 Hyundai investor-day shareholder-return report.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","confirmed_revision","low_red_team_risk"],"stage4b_evidence_fields":["positioning_overheat","valuation_blowoff"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005380/2024.csv","profile_path":"atlas/symbol_profiles/005/005380.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":238500,"MFE_30D_pct":9.01,"MFE_90D_pct":25.58,"MFE_180D_pct":25.58,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.06,"MAE_90D_pct":-10.06,"MAE_180D_pct":-17.27,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":299500,"drawdown_after_peak_pct":-34.12,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_primary_for_positive_entry","four_b_evidence_type":["positioning_overheat","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"positive_but_high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_KVU_HYUNDAI_005380_20240226::2024-02-27::238500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226","case_id":"R11L13_C31_KVU_KEPCO_015760_20240226","symbol":"015760","company_name":"한국전력","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_LOW_PBR_REGULATED_UTILITY_GUARD","sector":"정책·지정학·재난·이벤트","primary_archetype":"Korea Corporate Value-up policy event / issuer-level capital-return transmission","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Low-PBR policy theme existed, but regulated tariff/debt constraints made shareholder-return transmission weak; policy event did not close into issuer-level capital allocation.","evidence_source":"Corporate Value-up coverage plus KEPCO regulated-utility context; stock-web path shows early local peak then large MAE.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","legal_or_regulatory_block","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/015/015760/2024.csv","profile_path":"atlas/symbol_profiles/015/015760.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":24200,"MFE_30D_pct":5.17,"MFE_90D_pct":5.17,"MFE_180D_pct":5.17,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.81,"MAE_90D_pct":-21.45,"MAE_180D_pct":-22.4,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":25450,"drawdown_after_peak_pct":-26.21,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_risk_overlay_not_full_4C","four_b_evidence_type":["explicit_event_cap","legal_or_regulatory_block","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"policy_theme_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_KVU_KEPCO_015760_20240226::2024-02-27::24200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226","case_id":"R11L13_C31_KVU_SCT_028260_20240226","symbol":"028260","company_name":"삼성물산","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","fine_archetype_id":"KOREA_VALUE_UP_HOLDING_COMPANY_GOVERNANCE_DISCOUNT_GUARD","sector":"정책·지정학·재난·이벤트","primary_archetype":"Korea Corporate Value-up policy event / issuer-level capital-return transmission","loop_objective":"residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Holding-company low-PBR rerating occurred early, but policy event did not force governance/holding-company discount closure; after local peak, path rolled into deep drawdown.","evidence_source":"Corporate Value-up coverage; stock-web 2024 row path confirms local peak and later 180D MAE.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["explicit_event_cap","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/028/028260/2024.csv","profile_path":"atlas/symbol_profiles/028/028260.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":147400,"MFE_30D_pct":15.88,"MFE_90D_pct":15.88,"MFE_180D_pct":15.88,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-0.27,"MAE_90D_pct":-12.14,"MAE_180D_pct":-21.44,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-14","peak_price":170800,"drawdown_after_peak_pct":-32.2,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_local_4B_risk_overlay_not_full_4C","four_b_evidence_type":["explicit_event_cap","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"holding_company_policy_rerating_failed","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R11L13_C31_KVU_SCT_028260_20240226::2024-02-27::147400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KVU_KB_105560_20240226","trigger_id":"R11L13_C31_KVU_KB_105560_STAGE2A_20240226","symbol":"105560","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":58,"relative_strength_score":69,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":72,"execution_risk_score":16,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":84.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":22,"revision_score":64,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":75,"execution_risk_score":12,"legal_or_contract_risk_score":6,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green-shadow","changed_components":["revision_score","margin_bridge_score","execution_risk_score","policy_or_regulatory_score"],"component_delta_explanation":"C31 shadow profile rewards issuer-level capital-return implementation; caps policy-only low-PBR rerating when utility tariff/debt or holding-company governance discount remains unresolved.","MFE_90D_pct":44.23,"MAE_90D_pct":-2.4,"score_return_alignment_label":"strong_positive_alignment","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KVU_HYUNDAI_005380_20240226","trigger_id":"R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226","symbol":"005380","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":24,"revision_score":61,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":78,"valuation_repricing_score":74,"execution_risk_score":24,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_before":85.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":28,"revision_score":66,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":80,"valuation_repricing_score":76,"execution_risk_score":22,"legal_or_contract_risk_score":8,"dilution_cb_risk_score":0,"accounting_trust_risk_score":4},"weighted_score_after":88.0,"stage_label_after":"Stage3-Green-shadow-with-high-MAE-flag","changed_components":["revision_score","margin_bridge_score","relative_strength_score"],"component_delta_explanation":"C31 shadow profile rewards issuer-level capital-return implementation; caps policy-only low-PBR rerating when utility tariff/debt or holding-company governance discount remains unresolved.","MFE_90D_pct":25.58,"MAE_90D_pct":-10.06,"score_return_alignment_label":"positive_alignment_but_high_mae","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KVU_KEPCO_015760_20240226","trigger_id":"R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226","symbol":"015760","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":30,"relative_strength_score":42,"customer_quality_score":0,"policy_or_regulatory_score":76,"valuation_repricing_score":78,"execution_risk_score":58,"legal_or_contract_risk_score":52,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":77.0,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":22,"relative_strength_score":34,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":48,"execution_risk_score":70,"legal_or_contract_risk_score":68,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch / 4B-risk-overlay","changed_components":["valuation_repricing_score","policy_or_regulatory_score","execution_risk_score","legal_or_contract_risk_score"],"component_delta_explanation":"C31 shadow profile rewards issuer-level capital-return implementation; caps policy-only low-PBR rerating when utility tariff/debt or holding-company governance discount remains unresolved.","MFE_90D_pct":5.17,"MAE_90D_pct":-21.45,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R11L13_C31_KVU_SCT_028260_20240226","trigger_id":"R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226","symbol":"028260","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":36,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":74,"valuation_repricing_score":76,"execution_risk_score":34,"legal_or_contract_risk_score":42,"dilution_cb_risk_score":0,"accounting_trust_risk_score":8},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow_false_positive_risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":28,"relative_strength_score":48,"customer_quality_score":0,"policy_or_regulatory_score":58,"valuation_repricing_score":52,"execution_risk_score":52,"legal_or_contract_risk_score":58,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_after":64.0,"stage_label_after":"Stage2-Watch / 4B-risk-overlay","changed_components":["valuation_repricing_score","policy_or_regulatory_score","legal_or_contract_risk_score"],"component_delta_explanation":"C31 shadow profile rewards issuer-level capital-return implementation; caps policy-only low-PBR rerating when utility tariff/debt or holding-company governance discount remains unresolved.","MFE_90D_pct":15.88,"MAE_90D_pct":-12.14,"score_return_alignment_label":"counterexample_guard_improves_alignment","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c31_issuer_level_capital_return_required,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Policy event should promote only when issuer-level buyback/dividend/ROE or self-funded capital return path exists.","Improves KB/Hyundai vs KEPCO/Samsung C&T separation","R11L13_C31_KVU_KB_105560_STAGE2A_20240226|R11L13_C31_KVU_HYUNDAI_005380_STAGE2A_20240226|R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226|R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c31_policy_only_low_pbr_guard,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"Low PBR plus government programme is not enough when regulated utility debt/tariff or holding-company governance discount remains unresolved.","Reduces false positive Stage3-Yellow/Green on KEPCO and Samsung C&T",R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226|R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226,2,2,2,medium,canonical_shadow_guard,"not production; post-calibrated residual"
shadow_weight,c31_4b_event_detail_disappointment_overlay,canonical_archetype_specific,L10_POLICY_EVENT_CROSS_REDTEAM_MISC,C31_POLICY_SUBSIDY_LEGISLATION_EVENT,0,1,+1,"If details remain voluntary/non-binding after policy rally, classify as 4B overlay not full positive continuation.","Improves local peak interpretation for policy-only rerating",R11L13_C31_KVU_SCT_028260_STAGE2A_FALSE_20240226|R11L13_C31_KVU_KEPCO_015760_STAGE2A_FALSE_20240226,2,2,2,low,canonical_shadow_guard,"requires more holdout cases"

```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R11","loop":"13","large_sector_id":"L10_POLICY_EVENT_CROSS_REDTEAM_MISC","canonical_archetype_id":"C31_POLICY_SUBSIDY_LEGISLATION_EVENT","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":1,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["policy_only_low_pbr_false_positive","issuer_level_capital_return_gap","holding_company_governance_discount_not_closed","regulated_utility_balance_sheet_constraint"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R11/L10/C31 undercovered policy-event residual; prior search found no matching C31+Value-up+symbol artifact in allowed research files."}
```

### 25.7 narrative_only rows

```jsonl
```

No narrative-only rows in this loop. All four cases have clean 180D stock-web windows.

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
next_round = R13_C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP
reason = C31 now has one balanced policy-event residual file; C32 remains a natural next event-driven archetype for tender/control-premium cap vs follow-on drawdown.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max_date `2026-02-20`, raw/unadjusted FinanceData/marcap, tradable shard root `atlas/ohlcv_tradable_by_symbol_year`.
- Stock-Web schema: `atlas/schema.json`, tradable columns `d,o,h,l,c,v,a,mc,s,m`; calibration basis `tradable_raw`; corporate-action-contaminated windows blocked by default.
- Allowed stock_agent artifacts checked: `reports/e2r_calibration/ingest_summary.md`, `reports/e2r_calibration/applied_scoring_diff.md`; GitHub search over allowed artifacts found no duplicate C31 Value-up symbol set.
- External evidence map used for event timing:
  - Reuters, 2024-02-28, FSS considering penalties for firms failing to boost shareholder returns after Value-up package.
  - Reuters, 2024-05-02, voluntary guidelines for Corporate Value-up; noted lack of binding measures and muted market reaction.
  - Reuters, 2024-08-28, Hyundai investor day: buyback/dividend/shareholder-return plan.
  - FT, 2024-02-26, Korean reform package and Value-up index/tax-incentive framing.
