# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round = R6
scheduled_loop = 15
completed_round = R6
completed_loop = 15
next_round = R7
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN / FINANCIAL_YIELD_CAPITAL_RETURN_STABLE_CASHFLOW / BANK_PRICE_ONLY_LOW_FLOAT_BLOWOFF_GUARD
output_file = e2r_stock_web_v12_residual_round_R6_loop_15_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This MD does not re-prove those global axes. It tests whether C21 needs a canonical-archetype-specific capital-return axis: the market can re-rate financial companies before a classic growth-style revision signal appears, but only when ROE/PBR, explicit shareholder return, capital buffer, and low trust risk form a closed circuit. The counterexample is a low-float bank rally where price was loud but the capital-return circuit was empty.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
round_sector_consistency = pass
loop_objective = coverage_gap_fill, counterexample_mining, residual_missed_structural_mining, sector_specific_rule_discovery, canonical_archetype_compression, 4B_non_price_requirement_stress_test
```

R6 hard gate is satisfied because the file is financial-sector-only. This is not an R13 cross-archetype red-team file and not a live candidate list.

## 3. Previous Coverage / Duplicate Avoidance Check

- The immediately preceding local v12 file completed R5 Loop 15 and set `next_round = R6`, so this execution continues the round cycle rather than jumping to a larger gap.
- Repository search for exact `e2r_stock_web_v12_residual_round_R6_loop_15` and `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN` did not return an existing v12 result in the accessible stock_agent research artifact surface.
- No `src/e2r` code was opened. The stock_agent search was used only for duplicate avoidance.
- Selected symbols are new for this loop: 105560, 029780, 006220. 138040 is included only as a blocked narrative row because the stock-web profile marks corporate-action candidates inside the relevant 180D window.

## 4. Stock-Web OHLC Input / Price Source Validation

| field | value |
| --- | --- |
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
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

Tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`. Raw shard columns are `d,o,h,l,c,v,a,mc,s,m,rs`. The calculation uses `tradable_raw`, not adjusted close.

## 5. Historical Eligibility Gate

| symbol | company | profile | profile_status | price_rows |
| --- | --- | --- | --- | --- |
| 105560 | KB금융 | `atlas/symbol_profiles/105/105560.json` | corp_action_count=0; trading_day_count=4282; latest profile date=2026-02-20 | 2024-02-08 c=67,600; 2024-10-25 h=103,900 |
| 029780 | 삼성카드 | `atlas/symbol_profiles/029/029780.json` | corp_action_count=0; trading_day_count=4598 | 2024-02-02 c=34,800; 2024-08-29 h=46,000 |
| 006220 | 제주은행 | `atlas/symbol_profiles/006/006220.json` | corp_action candidates only before 2019; 2023 window clean | 2023-02-20 c=23,750; 2023-04-19 h=27,850; 2023-10-05 l=7,110 |
| 138040 | 메리츠금융지주 | `atlas/symbol_profiles/138/138040.json` | 2023-02-21 and 2023-04-25 corp-action candidates block 180D window | narrative_only; not used for weight calibration |

Eligibility outcome:

```text
105560 = calibration_usable true; clean 180D window; no corporate-action candidate in profile
029780 = calibration_usable true; clean 180D window; no corporate-action candidate in profile
006220 = calibration_usable true; 2023 window clean; old corporate-action candidates are outside the window
138040 = calibration_usable false; narrative_only because 2023-02-21 and 2023-04-25 corporate-action candidates overlap the 180D window from the 2022 trigger
```

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
| --- | --- | --- |
| KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Banks/financial holding companies can re-rate when ROE/PBR, CET1-like buffer, explicit buyback/cancellation/dividend, and policy optionality line up. |
| FINANCIAL_YIELD_CAPITAL_RETURN_STABLE_CASHFLOW | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Defensive financials with stable cashflow may need Stage2 promotion without growth-stock revision. |
| BANK_PRICE_ONLY_LOW_FLOAT_BLOWOFF_GUARD | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same sector price strength must be routed to guardrail if capital-return evidence is missing. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | current_profile_verdict | calibration_usable |
| --- | --- | --- | --- | --- | --- | --- |
| R6L15-C21-KB-20240208 | 105560 | KB금융 | structural_success | positive | current_profile_too_late | True |
| R6L15-C21-SAMCAR-20240202 | 029780 | 삼성카드 | stage2_promote_candidate | positive | current_profile_missed_structural | True |
| R6L15-C21-JEJU-20230220 | 006220 | 제주은행 | false_positive_green | counterexample | current_profile_correct | True |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 4
representative_trigger_count = 3
new_independent_case_count = 3
new_independent_case_ratio = 1.00
```

The balance is intentionally not “all banks went up.” KB금융 and 삼성카드 represent the two useful C21 paths: policy/ROE/PBR plus explicit return, and stable-yield defensive rerating. 제주은행 is the necessary red wire: if price-only low-float bank momentum is allowed to masquerade as capital-return evidence, the later drawdown overwhelms the temporary MFE.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| R6L15-C21-KB-20240208 | policy/value-up optionality, low-PBR bank relative strength, early return visibility | confirmed financial visibility and multiple public evidence later | none in representative trigger | none |
| R6L15-C21-SAMCAR-20240202 | dividend/cashflow visibility, defensive financial rerating | financial visibility only; not full Green | none in representative trigger | none |
| R6L15-C21-JEJU-20230220 | relative strength only | none | price-only local peak, positioning overheat | thesis-break watch only; no hard 4C evidence |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | entry_price | stock_web_manifest_max_date |
| --- | --- | --- | --- | --- | --- |
| 105560 | `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv` | `atlas/symbol_profiles/105/105560.json` | 2024-02-08 | 67600 | 2026-02-20 |
| 029780 | `atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv` | `atlas/symbol_profiles/029/029780.json` | 2024-02-02 | 34800 | 2026-02-20 |
| 006220 | `atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv` | `atlas/symbol_profiles/006/006220.json` | 2023-02-20 | 23750 | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D_pct | MFE_90D_pct | MFE_180D_pct | MAE_30D_pct | MAE_90D_pct | MAE_180D_pct | peak_date | peak_price | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L15-C21-KB-20240208-S2A | 105560 | Stage2-Actionable | 2024-02-07 | 2024-02-08 | 67600.0 | 16.27 | 23.37 | 53.7 | -11.69 | -11.69 | -11.69 | 2024-10-25 | 103900.0 | current_profile_too_late | True |
| R6L15-C21-KB-20240426-GREEN | 105560 | Stage3-Green-label-comparison | 2024-04-26 | 2024-04-26 | 76000.0 | 9.74 | 21.58 | 36.71 | -5.39 | -5.39 | -5.39 | 2024-10-25 | 103900.0 | current_profile_correct_but_late_vs_stage2_actionable | False |
| R6L15-C21-SAMCAR-20240202-S2A | 029780 | Stage2-Actionable | 2024-02-01 | 2024-02-02 | 34800.0 | 19.11 | 24.43 | 32.18 | -2.87 | -2.87 | -2.87 | 2024-08-29 | 46000.0 | current_profile_missed_structural | True |
| R6L15-C21-JEJU-20230220-PRICEONLY | 006220 | Price-only-blowoff / blocked Stage2 candidate | 2023-02-20 | 2023-02-20 | 23750.0 | 6.95 | 17.26 | 17.26 | -32.63 | -50.23 | -70.06 | 2023-04-19 | 27850.0 | current_profile_correct | True |


## 12. Trigger-Level OHLC Backtest Tables

### Representative triggers

| case | entry | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | peak | outcome |
| --- | --- | ---: | --- | --- | --- | --- | --- |
| KB금융 | 2024-02-08 | 67,600 | +16.27% / -11.69% | +23.37% / -11.69% | +53.70% / -11.69% | 2024-10-25 high 103,900 | early C21 positive; current profile too late |
| 삼성카드 | 2024-02-02 | 34,800 | +19.11% / -2.87% | +24.43% / -2.87% | +32.18% / -2.87% | 2024-08-29 high 46,000 | defensive capital-return positive; current profile missed structural |
| 제주은행 | 2023-02-20 | 23,750 | +6.95% / -32.63% | +17.26% / -50.23% | +17.26% / -70.06% | 2023-04-19 high 27,850 | counterexample; price-only should stay blocked |

The Jeju row is the guardrail anchor. Its later path is like a bridge built from ticker tape: it looked passable only while the crowd was standing on it. Once the crowd left, there was no capital-return steel underneath.

## 13. Current Calibrated Profile Stress Test

| question | KB금융 | 삼성카드 | 제주은행 |
| --- | --- | --- | --- |
| How would current profile judge? | likely waits for stronger confirmed revision/Green | may under-score because growth revision is weak | blocks or downgrades price-only momentum |
| Was judgment aligned with MFE/MAE? | safe but late; +53.70% 180D MFE from Stage2 | under-captures +32.18% 180D MFE with low MAE | correct; -70.06% 180D MAE if promoted |
| Stage2 bonus too high/low? | low for C21 | low for defensive capital-return | appropriate if capital-return evidence missing |
| Yellow threshold 75? | OK | slightly too strict for C21 defensive rerating | should not matter because blocked |
| Green threshold 87/revision 55? | too growth-style if applied mechanically | too strict; should remain Yellow, not Green | blocks positive stage |
| price-only blowoff guard? | not relevant | not relevant | strengthened |
| full 4B non-price requirement? | kept | kept | kept; price-only is watch-only |
| hard 4C routing? | not triggered | not triggered | no hard 4C; thesis-break watch only |

Current profile verdicts:

```text
KB금융 = current_profile_too_late
삼성카드 = current_profile_missed_structural
제주은행 = current_profile_correct
current_profile_error_count = 2
```

## 14. Stage2 / Yellow / Green Comparison

KB금융 has the cleanest lateness audit. Stage2-Actionable entry is 67,600 on 2024-02-08. A later Green-style label-comparison entry at 76,000 on 2024-04-26 gives:

```text
green_lateness_ratio = (76,000 - 67,600) / (103,900 - 67,600) = 0.23
```

A ratio of 0.23 means Green is not catastrophically late, but C21 still has an early actionable zone. For this archetype, the first usable signal is not a semiconductor-style EPS revision burst. It is a capital-allocation rerating compact: ROE/PBR discount + visible capital return + policy optionality + no trust break.

Samsung Card has no confirmed Stage3-Green trigger in this loop. It is a Stage2/Yelow defensive rerating case, not a Green rule-change case.

Jeju has no valid Stage3-Green trigger. Any Green label would be outcome-chasing or price-only inflation.

## 15. 4B Local vs Full-window Timing Audit

| case | 4B evidence type | local proximity | full-window proximity | verdict |
| --- | --- | ---: | ---: | --- |
| KB금융 | not 4B | null | null | no 4B in representative row |
| 삼성카드 | not 4B | null | null | no 4B in representative row |
| 제주은행 | price_only, positioning_overheat | 0.80 | 0.80 | price-only local 4B watch-only; not positive-stage evidence |

The Jeju signal validates the existing full-4B rule: price can identify a local overheat, but without non-price evidence it should not become a full 4B thesis conclusion, and it certainly cannot rescue a positive Stage2/3 label.

## 16. 4C Protection Audit

No hard 4C thesis-break trigger is promoted in this loop. Jeju is marked `thesis_break_watch_only`, because the evidence failure is the absence of C21 capital-return evidence at trigger time, not a later disclosure proving cancellation, accounting break, or forced liquidation.

```text
four_c_protection_label = thesis_break_watch_only for Jeju
hard_4c_success = not_applicable
hard_4c_late = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = unique_case_count within L6 is 3 but the better scope is canonical C21, not all financial sub-sectors. C22 insurance reserve/rate-cycle should be studied separately in another R6 loop.
```

No broad L6 rule should be promoted from this loop. Banks, cards, insurers, securities firms, and digital banks do not share the same capital-return mechanism.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
axis_1 = C21_roe_pbr_capital_return_score
axis_2 = C21_relative_strength_requires_capital_return_anchor
axis_3 = C21_defensive_yield_yellow_not_green
```

Candidate rule:

```text
if canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
    Stage2-Actionable may be promoted when at least three of the following are present:
      - ROE/PBR discount or valuation-repricing setup
      - explicit buyback, cancellation, dividend, or return policy visibility
      - capital buffer / regulatory capacity evidence
      - financial visibility without accounting/trust break
      - relative strength vs sector during policy or return catalyst
    But Stage3-Green still requires confirmed return execution or financial visibility.
    If relative strength is present without explicit capital-return evidence:
      route to blocked / 4B-watch-only, not positive Stage2/3.
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | 3 | KB later/strict; SamsungCard weak; Jeju blocked | 23.0 | -7.3 | 34.9 | -7.3 | 0.0 | 2 | 1 | directionally safe but too late for C21 positives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 3 | KB early; SamsungCard early; Jeju may pass as momentum | 21.69 | -21.6 | 34.38 | -28.21 | 0.33 | 0 | 0 | unsafe due Jeju-style high MAE |
| P1_sector_specific_candidate_profile | sector_specific | 3 | KB early; SamsungCard early; Jeju blocked | 23.9 | -7.28 | 42.94 | -7.28 | 0.0 | 0 | 0 | good but needs more L6 sub-sector coverage |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 3 | KB early; SamsungCard early-Yellow; Jeju blocked | 23.9 | -7.28 | 42.94 | -7.28 | 0.0 | 0 | 0 | best fit for this loop |
| P3_counterexample_guard_profile | counterexample_guard | 1 | Jeju blocked | None | None | None | None | 0.0 | 0 | 0 | guardrail preserved |


## 20. Score-Return Alignment Matrix

| trigger_id | before score/stage | after score/stage | 90D MFE/MAE | alignment |
| --- | --- | --- | --- | --- |
| R6L15-C21-KB-20240208-S2A | 82.0 / Stage3-Yellow | 89.5 / Stage3-Green-shadow | +23.37% / -11.69% | aligned but current profile late |
| R6L15-C21-SAMCAR-20240202-S2A | 72.0 / Stage2 | 77.0 / Stage3-Yellow-shadow | +24.43% / -2.87% | aligned as defensive Yellow, not Green |
| R6L15-C21-JEJU-20230220-PRICEONLY | 64.0 / Blocked-PriceOnly | 42.0 / Blocked-4B-watch-only | +17.26% / -50.23% | anti-aligned if promoted; guard is correct |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN / FINANCIAL_YIELD_CAPITAL_RETURN_STABLE_CASHFLOW / BANK_PRICE_ONLY_LOW_FLOAT_BLOWOFF_GUARD | 2 | 1 | 1 | 0 | 3 | 0 | 4 | 3 | 2 | False | True | C21 has initial bank/card/counterexample coverage; still needs insurance C22 separate R6 loop and non-bank digital finance later |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - current_profile_too_late
  - current_profile_missed_structural
  - false_positive_if_relative_strength_only
new_axis_proposed:
  - C21_roe_pbr_capital_return_score
  - C21_relative_strength_requires_capital_return_anchor
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- actual Songdaiki/stock-web 1D OHLC rows were used for entry price, MFE, MAE, peak, and drawdown fields.
- representative triggers are deduplicated by same_entry_group_id.
- 180D windows are clean for the three calibration-usable representative cases.
- current calibrated profile is stress-tested rather than re-proven.
```

Not validated:

```text
- This is not live candidate discovery.
- This does not inspect stock_agent source code.
- This does not patch production scoring.
- Evidence narratives are research proxies; later batch implementation should attach canonical disclosure/news URLs if promoting rows.
- 1Y/2Y fields are left null in machine-readable rows because this loop's quantitative decision uses 30/90/180D only.
```

Blocked narrative-only:

```text
138040 / 메리츠금융지주 is not used for calibration because stock-web profile reports corporate-action candidate dates 2023-02-21 and 2023-04-25, which contaminate the 180D window from the 2022 capital-return/merger trigger.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"explicit capital-return quality should promote Stage2-Actionable before full earnings revision","KB/SamsungCard captured earlier; Jeju still blocked","R6L15-C21-KB-20240208-S2A|R6L15-C21-SAMCAR-20240202-S2A",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_relative_strength_requires_capital_return_anchor,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"relative strength alone misclassifies Jeju-style bank momentum","blocks high-MAE false positive","R6L15-C21-JEJU-20230220-PRICEONLY",3,3,1,medium,counterexample_guard_shadow,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L15-C21-KB-20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L15-C21-KB-20240208-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early capital-return evidence aligned with 180D MFE, but MAE says capital-buffer sizing matters", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "대표 trigger는 Stage2-Actionable; Green comparison trigger는 dedupe 제외."}
{"row_type": "case", "case_id": "R6L15-C21-SAMCAR-20240202", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "FINANCIAL_YIELD_CAPITAL_RETURN_STABLE_CASHFLOW", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R6L15-C21-SAMCAR-20240202-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "defensive yield/capital-return signal produced positive MFE with limited MAE; should not require growth-stock revision evidence", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "C21 안의 비은행 금융 자본환원 표본."}
{"row_type": "case", "case_id": "R6L15-C21-JEJU-20230220", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_PRICE_ONLY_LOW_FLOAT_BLOWOFF_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L15-C21-JEJU-20230220-PRICEONLY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "relative strength without capital-return evidence produced high MAE and deep post-peak drawdown; should remain blocked", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "반례: C21에서 relative strength 단독은 승격 금지."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L15-C21-KB-20240208-S2A", "case_id": "R6L15-C21-KB-20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN", "sector": "금융지주/은행", "primary_archetype": "ROE/PBR 재평가 + 자사주/소각 + 배당 가시성", "loop_objective": "coverage_gap_fill|sector_specific_rule_discovery|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-07", "evidence_available_at_that_date": "밸류업/저PBR 금융주 재평가 국면에서 은행지주 중 자본비율·ROE·자사주/소각·배당 가시성이 같이 보인 초기 trigger. 사후 가격으로 trigger를 보정하지 않고 다음 거래일 종가를 entry로 사용.", "evidence_source": "historical public disclosure/news/IR evidence family; price verification uses stock-web only", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "financial_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-08", "entry_price": 67600.0, "MFE_30D_pct": 16.27, "MFE_90D_pct": 23.37, "MFE_180D_pct": 53.7, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -11.69, "MAE_90D_pct": -11.69, "MAE_180D_pct": -11.69, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900.0, "drawdown_after_peak_pct": -14.05, "green_lateness_ratio": "label_comparison_available:0.23 using 2024-04-26 Stage3-Green proxy", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "105560-20240208-67600", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L15-C21-KB-20240426-GREEN", "case_id": "R6L15-C21-KB-20240208", "symbol": "105560", "company_name": "KB금융", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "KOREA_VALUE_UP_BANK_ROE_PBR_CAPITAL_RETURN", "sector": "금융지주/은행", "primary_archetype": "ROE/PBR 재평가 + 자사주/소각 + 배당 가시성", "loop_objective": "green_strictness_stress_test", "trigger_type": "Stage3-Green-label-comparison", "trigger_date": "2024-04-26", "evidence_available_at_that_date": "분기 실적/주주환원 기대가 더 명확해진 뒤의 label comparison trigger. 대표 trigger가 아니며 Green lateness 감사용이다.", "evidence_source": "historical public disclosure/news/IR evidence family; price verification uses stock-web only", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv", "profile_path": "atlas/symbol_profiles/105/105560.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-04-26", "entry_price": 76000.0, "MFE_30D_pct": 9.74, "MFE_90D_pct": 21.58, "MFE_180D_pct": 36.71, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -5.39, "MAE_90D_pct": -5.39, "MAE_180D_pct": -5.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-10-25", "peak_price": 103900.0, "drawdown_after_peak_pct": -14.05, "green_lateness_ratio": 0.23, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "label_comparison_only", "current_profile_verdict": "current_profile_correct_but_late_vs_stage2_actionable", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "105560-20240426-76000", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same case label-comparison trigger for green_lateness audit", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L15-C21-SAMCAR-20240202-S2A", "case_id": "R6L15-C21-SAMCAR-20240202", "symbol": "029780", "company_name": "삼성카드", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "FINANCIAL_YIELD_CAPITAL_RETURN_STABLE_CASHFLOW", "sector": "카드/여신금융", "primary_archetype": "배당/자본환원 안정성 + 저PBR 방어적 재평가", "loop_objective": "coverage_gap_fill|residual_missed_structural_mining", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-01", "evidence_available_at_that_date": "고배당·저PBR 금융주 재평가 국면에서 카드사의 안정적 현금흐름/배당 가시성이 반영된 초기 trigger. 성장형 Green이 아니라 defensive rerating 표본으로 사용.", "evidence_source": "historical public disclosure/news/IR evidence family; price verification uses stock-web only", "stage2_evidence_fields": ["public_event_or_disclosure", "financial_visibility", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv", "profile_path": "atlas/symbol_profiles/029/029780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-02", "entry_price": 34800.0, "MFE_30D_pct": 19.11, "MFE_90D_pct": 24.43, "MFE_180D_pct": 32.18, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -2.87, "MAE_90D_pct": -2.87, "MAE_180D_pct": -2.87, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-29", "peak_price": 46000.0, "drawdown_after_peak_pct": -15.0, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "stage2_promote_candidate", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "029780-20240202-34800", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L15-C21-JEJU-20230220-PRICEONLY", "case_id": "R6L15-C21-JEJU-20230220", "symbol": "006220", "company_name": "제주은행", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_PRICE_ONLY_LOW_FLOAT_BLOWOFF_GUARD", "sector": "은행/지방은행", "primary_archetype": "가격 급등·저유동성 테마성 은행주 / capital-return evidence 부재", "loop_objective": "counterexample_mining|stage2_actionable_bonus_stress_test|4B_non_price_requirement_stress_test", "trigger_type": "Price-only-blowoff / blocked Stage2 candidate", "trigger_date": "2023-02-20", "evidence_available_at_that_date": "은행/인터넷은행/저PBR 테마성 급등으로 상대강도는 강했으나, C21의 핵심인 ROE/PBR 개선·명시적 자본환원·소각/배당 업그레이드가 trigger date에 독립 evidence로 충분하지 않았던 반례.", "evidence_source": "historical market narrative; price verification uses stock-web only", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv", "profile_path": "atlas/symbol_profiles/006/006220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-02-20", "entry_price": 23750.0, "MFE_30D_pct": 6.95, "MFE_90D_pct": 17.26, "MFE_180D_pct": 17.26, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -32.63, "MAE_90D_pct": -50.23, "MAE_180D_pct": -70.06, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-04-19", "peak_price": 27850.0, "drawdown_after_peak_pct": -74.47, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.8, "four_b_timing_verdict": "price_only_local_4B_not_full_positive_stage", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green_if_price_only_allowed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006220-20230220-23750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15-C21-KB-20240208", "trigger_id": "R6L15-C21-KB-20240208-S2A", "symbol": "105560", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 15, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 17, "fcf_conversion_score": 8}, "weighted_score_before": 82.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 18, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 16, "valuation_repricing_score": 15, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 24, "fcf_conversion_score": 10}, "weighted_score_after": 89.5, "stage_label_after": "Stage3-Green-shadow", "changed_components": ["roe_pbr_capital_return_score", "fcf_conversion_score"], "component_delta_explanation": "C21에서는 revision보다 CET1/ROE/PBR/explicit return mix가 early rerating을 설명한다.", "MFE_90D_pct": 23.37, "MAE_90D_pct": -11.69, "score_return_alignment_label": "aligned_but_current_profile_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15-C21-SAMCAR-20240202", "trigger_id": "R6L15-C21-SAMCAR-20240202-S2A", "symbol": "029780", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 13, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 16, "fcf_conversion_score": 12}, "weighted_score_before": 72.0, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 6, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 10, "valuation_repricing_score": 13, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 21, "fcf_conversion_score": 14}, "weighted_score_after": 77.0, "stage_label_after": "Stage3-Yellow-shadow", "changed_components": ["roe_pbr_capital_return_score", "fcf_conversion_score"], "component_delta_explanation": "안정 배당/현금흐름형 금융은 성장 revision 없이도 C21 Stage2-Actionable로 인정하되 Green은 보류한다.", "MFE_90D_pct": 24.43, "MAE_90D_pct": -2.87, "score_return_alignment_label": "aligned_defensive_yield_rerating", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L15-C21-JEJU-20230220", "trigger_id": "R6L15-C21-JEJU-20230220-PRICEONLY", "symbol": "006220", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 22, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 8, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 18}, "weighted_score_before": 64.0, "stage_label_before": "Blocked-PriceOnly", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": -18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "fcf_conversion_score": 0, "positioning_overheat_score": 22}, "weighted_score_after": 42.0, "stage_label_after": "Blocked-4B-watch-only", "changed_components": ["relative_strength_score", "policy_or_regulatory_score", "valuation_repricing_score", "execution_risk_score", "positioning_overheat_score"], "component_delta_explanation": "C21에서 capital_return_score가 0이면 relative strength는 positive stage가 아니라 overheat/guardrail evidence다.", "MFE_90D_pct": 17.26, "MAE_90D_pct": -50.23, "score_return_alignment_label": "anti_aligned_false_positive_if_promoted", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"explicit capital-return quality should promote Stage2-Actionable before full earnings revision","KB/SamsungCard captured earlier; Jeju still blocked","R6L15-C21-KB-20240208-S2A|R6L15-C21-SAMCAR-20240202-S2A",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C21_relative_strength_requires_capital_return_anchor,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"relative strength alone misclassifies Jeju-style bank momentum","blocks high-MAE false positive","R6L15-C21-JEJU-20230220-PRICEONLY",3,3,1,medium,counterexample_guard_shadow,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "15", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "scheduled_round": "R6", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_too_late", "current_profile_missed_structural", "false_positive_if_relative_strength_only"], "positive_case_count": 2, "counterexample_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "same_archetype_new_symbol_bonus=12; same_archetype_counterexample_bonus=5; same_archetype_new_trigger_family_bonus=12; new_symbol_bonus=9; counterexample_gap_bonus=4; residual_error_bonus=10; total≈52", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only row

```jsonl
{"row_type": "narrative_only", "case_id": "R6L15-C21-MERITZ-20221122", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "reason": "strong capital-return/merger narrative exists, but stock-web profile lists corporate-action candidate dates 2023-02-21 and 2023-04-25 inside the 180D forward window, so quantitative weight calibration is blocked", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

```text
completed_round = R6
completed_loop = 15
next_round = R7
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-web source files inspected in this loop:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/105/105560.json
atlas/symbol_profiles/029/029780.json
atlas/symbol_profiles/006/006220.json
atlas/symbol_profiles/138/138040.json
atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv
atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv
```

Representative source-row anchors used for OHLC calculations:

```text
KB금융 / 105560:
- 2024-02-08 close 67,600 from atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
- 2024-10-25 high 103,900 from atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv
- profile corp_action_candidate_count = 0 from atlas/symbol_profiles/105/105560.json

삼성카드 / 029780:
- 2024-02-02 close 34,800 from atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv
- 2024-08-29 high 46,000 from atlas/ohlcv_tradable_by_symbol_year/029/029780/2024.csv
- profile corp_action_candidate_count = 0 from atlas/symbol_profiles/029/029780.json

제주은행 / 006220:
- 2023-02-20 close 23,750 from atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv
- 2023-04-19 high 27,850 from atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv
- 2023-10-05 low 7,110 from atlas/ohlcv_tradable_by_symbol_year/006/006220/2023.csv
- 2023 forward window has no corporate-action profile date inside the 180D window

메리츠금융지주 / 138040:
- profile contains corporate-action candidate dates 2023-02-21 and 2023-04-25; therefore narrative_only, not calibration weight input
```
