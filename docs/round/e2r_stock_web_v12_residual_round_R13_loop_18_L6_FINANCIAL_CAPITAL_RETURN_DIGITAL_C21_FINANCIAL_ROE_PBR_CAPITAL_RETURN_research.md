# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R13
loop = 18
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY
loop_objective = holdout_validation | residual_false_positive_mining | residual_missed_structural_mining | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | coverage_gap_fill
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

This file is a standalone historical calibration and residual research artifact. It is not a current recommendation list, not a live watchlist, and not a repository patch. The purpose is to test the already-calibrated E2R 2.1 profile against the C21 financial capital-return archetype and isolate sector/canonical-specific residual rules.

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

The test here is not whether the global Stage2 bonus or stricter Green gates were correct in the aggregate. That has already been applied. The residual question is narrower: in Korean financials, the same policy headline can mean two different machines. In one machine, low PBR, recurring ROE, CET1/capital buffer, buyback/cancellation, and payout visibility pull the valuation gear upward. In the other, a bank-like ticker moves with the sector but lacks the capital-return crankshaft; the same policy heat becomes only steam.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R13 |
| loop | 18 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY |
| selected symbols | 105560 KB금융, 086790 하나금융지주, 316140 우리금융지주, 323410 카카오뱅크 |
| primary trigger family | Korea Value-up / capital-return / ROE-PBR re-rating |
| residual focus | distinguish real capital-return compounders from policy-theme-only or premium-growth bank false positives |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were checked only for coverage/duplicate avoidance and applied-axis awareness. The ingest summary showed broad prior coverage across R1-R13, 107 parsed result MDs, 1,940 validated trigger rows, and 1,376 aggregate representative rows. It also showed many rejections from missing/invalid price-source fields, which is why this loop keeps every representative trigger tied to explicit Stock-Web shard/profile paths. The applied scoring diff showed that the main global axes have already been promoted: Stage2 bonus, Yellow relaxation, stricter Green total/revision gates, cross-evidence Green buffer, 4B non-price requirement, and 4C thesis-break routing.

Novelty check: this loop deliberately moves from insurance reserve-rate C22 to financial holding/ROE-PBR capital-return C21. It uses bank holding and online-bank contrast cases rather than repeating insurance cases. All four representative cases are treated as new independent evidence for C21.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema were validated before selecting cases.

| manifest field | observed value |
|---|---:|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema basis: tradable shard columns are `d,o,h,l,c,v,a,mc,s,m`; raw shard adds `rs`. MFE and MAE are computed from raw/unadjusted tradable rows, not adjusted prices. Corporate-action contaminated 180D windows are blocked by default.

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| symbol | company_name | profile_path | first_date | last_date | corporate_action_candidate_count | corporate_action_candidate_dates | 180D status | calibration_usable |
|---|---|---|---:|---:|---:|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | 2008-10-10 | 2026-02-20 | 0 | [] | clean_180D_window | true |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | 2005-12-12 | 2026-02-20 | 0 | [] | clean_180D_window | true |
| 316140 | 우리금융지주 | atlas/symbol_profiles/316/316140.json | 2019-02-13 | 2026-02-20 | 0 | [] | clean_180D_window | true |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | 2021-08-06 | 2026-02-20 | 0 | [] | clean_180D_window | true |

All representative entries use 2024-02-26 or the same tradable year. For the 180D window, every selected ticker has a valid entry row, positive OHLCV, at least 180 forward trading rows before the Stock-Web manifest max date, and no profile-level corporate-action candidate inside the representative 180D window.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Financial holding / bank re-rating driven by low PBR, recurring ROE, capital buffer, buyback/cancellation, payout visibility, and policy tailwind. |
| POLICY_THEME_ONLY_BANK_BETA | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same broad policy headline but no durable firm-level capital-return evidence; should not be scored like a structural capital-return case. |
| PREMIUM_DIGITAL_BANK_FALSE_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | A bank ticker with growth/premium valuation but weak capital-return re-rating fit; should be guarded inside C21. |
| LOCAL_PRICE_BLOWOFF_AFTER_VALUE_UP | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Local peak overlay; does not promote positive stage and cannot become full 4B without non-price deterioration. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | best_trigger | current_profile_verdict | why selected |
|---|---|---|---|---|---|---|---|
| C21-L6-018-KB-20240226 | 105560 | KB금융 | structural_success | positive | KB-C21-S2A-20240226 | current_profile_too_late | Strong C21 fit: low-PBR financial holding, shareholder-return narrative, later firm-level capital-return confirmation, large clean 180D MFE. |
| C21-L6-018-HANA-20240226 | 086790 | 하나금융지주 | structural_success | positive | HANA-C21-S2A-20240226 | current_profile_too_late | Similar but weaker than KB; useful for testing whether C21 needs quality scaling rather than all-bank promotion. |
| C21-L6-018-WOORI-20240226 | 316140 | 우리금융지주 | high_mae_success | counterexample | WOORI-C21-S2A-20240226 | current_profile_false_positive | Same broad bank/value-up context, but smaller upside and higher MAE; tests overbroad Stage2 bonus. |
| C21-L6-018-KAKAOBANK-20240226 | 323410 | 카카오뱅크 | false_positive_green | counterexample | KAKAOBANK-C21-S2A-20240226 | current_profile_false_positive | Bank-like ticker moved under theme but lacked C21 capital-return mechanics; severe 180D MAE. |
| C21-L6-018-KB-4B-20241025 | 105560 | KB금융 | 4B_too_early | counterexample overlay | KB-C21-4B-20241025 | current_profile_4B_too_early | Local price blowoff near 2024 high looked like 4B, but without thesis-deterioration evidence it was too early relative to the later 2025 full-window peak. |

## 8. Positive vs Counterexample Balance

| category | count | cases |
|---|---:|---|
| positive_structural_success | 2 | KB금융, 하나금융지주 |
| counterexample_or_failed_rerating | 2 | 우리금융지주, 카카오뱅크 |
| 4B_or_4C_case | 1 | KB금융 2024-10-25 4B overlay |
| calibration_usable_case_count | 4 representative + 1 overlay | all rows usable for timing/price audit; only 4 representative rows enter positive/counter aggregate |
| new_independent_case_ratio | 1.00 | 4 / 4 representative cases new for C21 |

## 9. Evidence Source Map

| evidence_family | trigger_date | source note | stage usage |
|---|---:|---|---|
| Korea Corporate Value-up Programme | 2024-02-26 | Public policy package to encourage shareholder returns / capital efficiency among listed firms; banks and low-PBR financials were direct market beneficiaries. | Stage2 / sector optionality only; not enough for Green by itself. |
| Company-level capital-return plan or buyback/cancellation visibility | 2024 H1-H2 | Firm-specific shareholder-return disclosure, buyback/cancellation, dividend policy, or value-up plan. | Stage3/Green support only when paired with ROE/PBR and recurring earnings. |
| Policy-theme-only bank beta | 2024-02-26 | Broad policy headline without firm-level capital-return mechanism. | Stage2 watch only; should be blocked from Green promotion. |
| Premium digital-bank mismatch | 2024-02-26 | Bank label but valuation/growth profile does not match low-PBR capital-return archetype. | Counterexample guard; do not apply C21 positive boost. |
| Local price blowoff | 2024-10-25 | High local price / event enthusiasm in KB; no confirmed deterioration at that date. | 4B overlay only, not full exit without non-price risk. |

## 10. Price Data Source Map

| symbol | company_name | price_shard_path | profile_path | entry_date(s) used | manifest_max_date |
|---|---|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | 2024-02-26, 2024-10-25 | 2026-02-20 |
| 086790 | 하나금융지주 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | 2024-02-26 | 2026-02-20 |
| 316140 | 우리금융지주 | atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv | atlas/symbol_profiles/316/316140.json | 2024-02-26 | 2026-02-20 |
| 323410 | 카카오뱅크 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | 2024-02-26 | 2026-02-20 |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence | representative? |
|---|---|---|---:|---:|---:|---|---|---|---|---|
| KB-C21-S2A-20240226 | C21-L6-018-KB-20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 62500 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | later capital-return visibility and ROE/PBR confirmation | [] | [] | yes |
| HANA-C21-S2A-20240226 | C21-L6-018-HANA-20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 55400 | policy_or_regulatory_optionality, relative_strength, early_revision_signal | later payout / capital-return visibility | [] | [] | yes |
| WOORI-C21-S2A-20240226 | C21-L6-018-WOORI-20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 14630 | policy_or_regulatory_optionality, sector_beta | weak firm-level conversion | [] | [] | yes |
| KAKAOBANK-C21-S2A-20240226 | C21-L6-018-KAKAOBANK-20240226 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 30150 | policy_or_regulatory_optionality, bank-theme beta | none; valuation/payout mismatch | [] | thesis_evidence_broken | yes |
| KB-C21-4B-20241025 | C21-L6-018-KB-4B-20241025 | Stage4B | 2024-10-25 | 2024-10-25 | 101000 | prior Stage2 evidence | confirmed structural case | price_only_local_peak, valuation_blowoff | [] | no; overlay only |

## 12. Trigger-Level OHLC Backtest Tables

MFE/MAE are calculated from Stock-Web tradable raw OHLC. Representative rows use entry-date close. Values are rounded to two decimals. 1Y/2Y fields are included for schema completeness but not used for this loop's weight proposal; the quantitative calibration decision is based on clean 30D/90D/180D windows.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | MFE_1Y_pct | MFE_2Y_pct | peak_date_observed | peak_price_observed | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| KB-C21-S2A-20240226 | 62500 | 25.76 | -4.48 | 44.00 | -4.48 | 66.24 | -4.48 | 66.24 | 83.68 | 2024-10-25 | 103900 | true | true |
| HANA-C21-S2A-20240226 | 55400 | 17.69 | -4.69 | 22.38 | -6.86 | 25.09 | -6.86 | 25.09 | 25.09 | 2024-08-27 | 69300 | true | true |
| WOORI-C21-S2A-20240226 | 14630 | 5.95 | -6.08 | 5.95 | -10.12 | 15.93 | -10.12 | 15.93 | 15.93 | 2024-07-29 | 16960 | true | true |
| KAKAOBANK-C21-S2A-20240226 | 30150 | 1.66 | -17.74 | 1.66 | -33.50 | 1.66 | -38.67 | 1.66 | 1.66 | 2024-02-27 | 30650 | true | true |
| KB-C21-4B-20241025 | 101000 | 2.87 | -15.05 | 2.87 | -22.48 | 13.66 | -31.39 | 13.66 | 13.66 | 2025-06-10 | 114800 | true | true |

## 13. Current Calibrated Profile Stress Test

| case_id | expected current profile behavior | actual MFE/MAE alignment | Stage2 bonus | Yellow 75 | Green 87 / revision 55 | price-only blowoff guard | full 4B non-price requirement | hard 4C routing | verdict |
|---|---|---|---|---|---|---|---|---|---|
| C21-L6-018-KB-20240226 | likely Stage2-Actionable, then wait for firm-level Green | Stage2 captured early; Green waiting would lose part of upside | useful but too generic | okay | too strict unless C21 capital-return quality is recognized | appropriate | appropriate | not applicable | current_profile_too_late |
| C21-L6-018-HANA-20240226 | Stage2-Actionable but lower conviction than KB | modest but real MFE; drawdown manageable | useful | okay | should require quality scaling; not equal to KB | appropriate | appropriate | not applicable | current_profile_too_late |
| C21-L6-018-WOORI-20240226 | broad bank Stage2 could overpromote | upside exists, but MAE and weaker conversion make it poor quality | too broad | could be too lenient if sector-only | Green should not trigger without firm-specific capital-return quality | appropriate | appropriate | not applicable | current_profile_false_positive |
| C21-L6-018-KAKAOBANK-20240226 | broad bank/value-up theme could incorrectly score as financial rerating | severe negative MAE and no meaningful upside | excessive if applied without low-PBR capital-return fit | too lenient if sector-only | Green must be blocked | appropriate | appropriate | hard 4C watch is useful | current_profile_false_positive |
| C21-L6-018-KB-4B-20241025 | price-only local 4B would be tempting | local peak was near, but full-window peak later exceeded it | not relevant | not relevant | not relevant | should block positive promotion | should block full 4B without deterioration | not applicable | current_profile_4B_too_early |

Residual finding: C21 needs a quality valve. A broad policy pipe fills all bank tickers with pressure, but only those connected to the capital-return pump convert that pressure into durable MFE. The current global profile has the right skeleton, but C21 needs its own muscles: ROE/PBR discount, explicit shareholder-return action, capital buffer, and payout/buyback durability.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | proxy Green entry | Green entry price | cycle peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---:|---|
| KB금융 | 2024-02-26 / 62500 | 2024-04-26 / 76000 | 76000 | 103900 | 0.33 | Green somewhat late but acceptable if C21 quality boost allows Yellow/Actionable earlier. |
| 하나금융지주 | 2024-02-26 / 55400 | 2024-05-13 / 63600 | 63600 | 69300 | 0.59 | Green late; quality differentiation matters because upside was smaller. |
| 우리금융지주 | 2024-02-26 / 14630 | no confirmed Green | null | 16960 | not_applicable | Sector beta alone should remain Stage2 watch. |
| 카카오뱅크 | 2024-02-26 / 30150 | no confirmed Green | null | 30650 | not_applicable | Green must be blocked; no C21 capital-return setup. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2 base price | Stage4B entry price | local_peak_price_after_Stage2 | full_window_peak_price_after_Stage2 | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | timing verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| KB-C21-4B-20241025 | 62500 | 101000 | 103900 | 114800 | 0.93 | 0.74 | price_only, valuation_blowoff | price_only_local_4B_too_early |

The 2024-10-25 KB row looked like a local 4B because the stock reached 103,900 intraday and closed 101,000. But full-window proximity was lower, and later 2025 highs were above the local blowoff. Without non-price deterioration such as revision slowdown, capital-return disappointment, CET1 pressure, or regulatory/legal block, the local peak should be an overlay, not a full 4B exit.

## 16. 4C Protection Audit

| case_id | 4C signal | four_c_protection_label | note |
|---|---|---|---|
| C21-L6-018-KAKAOBANK-20240226 | capital-return thesis mismatch and continued drawdown after theme entry | thesis_break_watch_only | This is not a hard accounting break, but it is a C21 thesis mismatch. A premium digital-bank valuation without shareholder-return evidence should not receive C21 positive promotion. |
| C21-L6-018-KB-20240226 | none | not_applicable | No thesis break during representative 180D window. |
| C21-L6-018-HANA-20240226 | none | not_applicable | No hard thesis break; moderate drawdown was within sector volatility. |
| C21-L6-018-WOORI-20240226 | weak conversion | thesis_break_watch_only | Not hard 4C, but weak quality should cap Stage3 promotion. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
candidate_rule_id = L6_C21_CAPITAL_RETURN_QUALITY_GATE
```

Rule candidate:

1. In L6 financials, broad policy evidence can create Stage2 watch/Actionable only when accompanied by at least one of: low-PBR/ROE mismatch, explicit shareholder-return plan, buyback/cancellation, dividend/payout visibility, CET1/capital buffer, or recurring earnings visibility.
2. Do not give the full Stage2-actionable evidence bonus to financial tickers that only share the sector label but lack capital-return mechanics.
3. A bank-like ticker with premium valuation and no shareholder-return route should be treated as `policy_theme_only` or `premium_bank_false_positive`, not as a C21 structural rerating candidate.
4. For L6 C21, 4B cannot be price-only. It needs non-price deterioration: capital-return disappointment, regulatory/legal cap, revision slowdown, CET1/capital pressure, overhang, or explicit event cap.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
candidate_rule_id = C21_ROE_PBR_SHAREHOLDER_RETURN_COMPONENTS
```

Proposed C21-specific research proxy components:

| component | direction | reason |
|---|---:|---|
| roe_pbr_capital_return_score | +0 to +3 | Distinguishes low-PBR financials with visible capital-return path from sector beta. |
| shareholder_return_action_score | +0 to +3 | Buyback/cancellation/dividend/payout plan has higher signal quality than policy headline alone. |
| capital_buffer_score | +0 to +2 | CET1/capital capacity is the bridge between intent and executable return. |
| policy_theme_only_guard | -0 to -3 | Penalizes policy-only cases without firm-level capital-return route. |
| premium_bank_false_positive_guard | -0 to -4 | Blocks digital/premium bank cases from low-PBR capital-return archetype scoring. |
| c21_price_only_4b_guard | keep / strengthen | Local price peaks cannot become full 4B without non-price deterioration. |

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | global current | Existing Stage2 bonus catches policy tailwind but lacks C21 quality distinction | 4 | 17.50 | -13.74 | 27.23 | -15.04 | 0.50 | 2 | 2 | mixed_alignment |
| P0b_e2r_2_0_baseline_reference | global old | Old baseline waits for stronger confirmation and misses early re-rating | 4 | 17.50 | -13.74 | 27.23 | -15.04 | 0.25 | 2 | 2 | late_but_safer |
| P1_L6_sector_specific_candidate_profile | L6 | Apply C21 quality gate inside financials; policy-only cases stay watch-only | 4 | 32.19 selected positives | -5.67 selected positives | 45.67 selected positives | -5.67 selected positives | 0.25 | 0 | 1 | improved_alignment |
| P2_C21_canonical_candidate_profile | C21 | Add ROE/PBR + shareholder-return action + capital buffer components | 4 | 33.19 selected positives | -5.67 selected positives | 45.67 selected positives | -5.67 selected positives | 0.25 | 0 | 1 | best_shadow_alignment |
| P3_counterexample_guard_profile | C21 guard | Block premium-bank / policy-only sector beta from Stage3 | 4 | 32.19 selected positives | -5.67 selected positives | 45.67 selected positives | -5.67 selected positives | 0.00 if guard enforced | 0 | 1 | improved_false_positive_control |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | MFE_90D_pct | MAE_90D_pct | score_return_alignment_label |
|---|---:|---|---:|---|---:|---:|---|
| C21-L6-018-KB-20240226 | 76 | Stage3-Yellow | 84 | Stage2-Actionable / near-Green shadow | 44.00 | -4.48 | aligned_after_quality_boost |
| C21-L6-018-HANA-20240226 | 74 | Stage2-Actionable | 79 | Stage3-Yellow shadow | 22.38 | -6.86 | moderately_aligned_after_quality_boost |
| C21-L6-018-WOORI-20240226 | 73 | Stage2-Actionable | 66 | Stage2-Watch | 5.95 | -10.12 | improved_by_guard |
| C21-L6-018-KAKAOBANK-20240226 | 71 | Stage2-Actionable false positive | 54 | Blocked / Watch-only | 1.66 | -33.50 | guard_correct |
| C21-L6-018-KB-4B-20241025 | risk overlay | price-only local 4B temptation | overlay only | 4B_watch_not_full | 2.87 | -22.48 | full_4B_guard_correct |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY | 2 | 2 | 1 | 1 watch-only | 4 | 0 | 5 | 4 | 5 | true | true | C21 now has positive/counterexample balance; next gap is insurance vs bank cross-profile reconciliation and non-bank brokerage/holding-company holdout. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [sector_policy_theme_false_positive, premium_bank_false_positive, C21_quality_gate_missing, price_only_local_4B_too_early, Green_lateness_in_capital_return_compounder]
new_axis_proposed: [c21_roe_pbr_capital_return_score, c21_shareholder_return_action_score, c21_policy_theme_only_guard, c21_premium_bank_false_positive_guard, c21_price_only_4b_guard]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, stage3_cross_evidence_green_buffer]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest/schema presence and max_date.
- Profile-level corporate-action window status for selected tickers.
- Actual 2024 tradable OHLC rows for entry, MFE/MAE, local peak, and 180D calibration windows.
- Representative trigger dedupe by case/entry.
- C21-specific positive/counterexample split.
- 4B local-vs-full-window separation.

Not validated:

- No live candidate scan.
- No current investment recommendation.
- No brokerage API or auto-trading path.
- No stock_agent `src/e2r` code inspection.
- No production scoring change.
- No attempt to repair or adjust raw/unadjusted OHLC for dividends, splits, or other corporate actions beyond profile contamination checks.
- No exact total-return adjustment; all price metrics are raw price-only MFE/MAE.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"Low-PBR financials with visible shareholder-return route produced materially better 90D/180D MFE than policy-only cases.","Improves KB/Hana alignment without promoting KakaoBank.","KB-C21-S2A-20240226|HANA-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_shareholder_return_action_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"Firm-level buyback/cancellation/dividend visibility is the missing mechanism between policy headline and rerating.","Raises quality cases toward Yellow/Green shadow.","KB-C21-S2A-20240226|HANA-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_policy_theme_only_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-2,-2,"Sector-wide value-up headlines overpromote weak conversion cases.","Caps Woori-style sector beta at Watch/low Stage2 unless firm-level capital return appears.","WOORI-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_premium_bank_false_positive_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-4,-4,"Premium digital-bank valuation lacks low-PBR capital-return re-rating mechanics and produced severe MAE.","Blocks KakaoBank-style false positives from C21 promotion.","KAKAOBANK-C21-S2A-20240226",4,4,2,high,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_price_only_4b_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,keep_or_strengthen,+0,"Price-only local peak in KB was too early relative to later full-window peak.","Keeps 4B as overlay unless non-price deterioration exists.","KB-C21-4B-20241025",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C21-L6-018-KB-20240226","symbol":"105560","company_name":"KB금융","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"KB-C21-S2A-20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned_after_quality_boost","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Strong C21 positive: low-PBR financial holding plus capital-return route; clean 180D MFE."}
{"row_type":"case","case_id":"C21-L6-018-HANA-20240226","symbol":"086790","company_name":"하나금융지주","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"HANA-C21-S2A-20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"moderately_aligned_after_quality_boost","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive but weaker than KB; supports quality-scaled C21 scoring."}
{"row_type":"case","case_id":"C21-L6-018-WOORI-20240226","symbol":"316140","company_name":"우리금융지주","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"POLICY_THEME_ONLY_BANK_BETA","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"WOORI-C21-S2A-20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"improved_by_guard","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Weak conversion and higher MAE; should not score like best C21 capital-return compounders."}
{"row_type":"case","case_id":"C21-L6-018-KAKAOBANK-20240226","symbol":"323410","company_name":"카카오뱅크","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"PREMIUM_DIGITAL_BANK_FALSE_POSITIVE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"KAKAOBANK-C21-S2A-20240226","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"guard_correct","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Bank label but no C21 low-PBR capital-return mechanics; severe 180D MAE."}
{"row_type":"case","case_id":"C21-L6-018-KB-4B-20241025","symbol":"105560","company_name":"KB금융","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOCAL_PRICE_BLOWOFF_AFTER_VALUE_UP","case_type":"4B_too_early","positive_or_counterexample":"counterexample_overlay","best_trigger":"KB-C21-4B-20241025","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"score_price_alignment":"full_4B_guard_correct","current_profile_verdict":"current_profile_4B_too_early","price_source":"Songdaiki/stock-web","notes":"Local blowoff near 2024 high; full 4B should require non-price deterioration."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KB-C21-S2A-20240226","case_id":"C21-L6-018-KB-20240226","symbol":"105560","company_name":"KB금융","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"holdout_validation|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Value-up policy package plus low-PBR bank/financial holding rerating setup; firm-level capital-return visibility added later.","evidence_source":"public policy and company disclosure/news map; Stock-Web OHLC for price","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","repeat_order_or_conversion","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":62500,"MFE_30D_pct":25.76,"MFE_90D_pct":44.0,"MFE_180D_pct":66.24,"MFE_1Y_pct":66.24,"MFE_2Y_pct":83.68,"MAE_30D_pct":-4.48,"MAE_90D_pct":-4.48,"MAE_180D_pct":-4.48,"MAE_1Y_pct":-4.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-33.3,"green_lateness_ratio":0.33,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C21-L6-018-KB-20240226__2024-02-26__62500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"HANA-C21-S2A-20240226","case_id":"C21-L6-018-HANA-20240226","symbol":"086790","company_name":"하나금융지주","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUE_UP_ROE_PBR_CAPITAL_RETURN_QUALITY","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"holdout_validation|sector_specific_rule_discovery|coverage_gap_fill","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Korea Value-up policy plus bank capital-return rerating setup; later firm-specific shareholder-return visibility.","evidence_source":"public policy and company disclosure/news map; Stock-Web OHLC for price","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":55400,"MFE_30D_pct":17.69,"MFE_90D_pct":22.38,"MFE_180D_pct":25.09,"MFE_1Y_pct":25.09,"MFE_2Y_pct":25.09,"MAE_30D_pct":-4.69,"MAE_90D_pct":-6.86,"MAE_180D_pct":-6.86,"MAE_1Y_pct":-6.86,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-25.69,"green_lateness_ratio":0.59,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C21-L6-018-HANA-20240226__2024-02-26__55400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"WOORI-C21-S2A-20240226","case_id":"C21-L6-018-WOORI-20240226","symbol":"316140","company_name":"우리금융지주","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"POLICY_THEME_ONLY_BANK_BETA","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"residual_false_positive_mining|counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Broad bank/value-up policy beta, but weaker firm-level capital-return conversion versus top positives.","evidence_source":"public policy/news map; Stock-Web OHLC for price","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv","profile_path":"atlas/symbol_profiles/316/316140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":14630,"MFE_30D_pct":5.95,"MFE_90D_pct":5.95,"MFE_180D_pct":15.93,"MFE_1Y_pct":15.93,"MFE_2Y_pct":15.93,"MAE_30D_pct":-6.08,"MAE_90D_pct":-10.12,"MAE_180D_pct":-10.12,"MAE_1Y_pct":-10.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-29","peak_price":16960,"drawdown_after_peak_pct":-22.29,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C21-L6-018-WOORI-20240226__2024-02-26__14630","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KAKAOBANK-C21-S2A-20240226","case_id":"C21-L6-018-KAKAOBANK-20240226","symbol":"323410","company_name":"카카오뱅크","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"PREMIUM_DIGITAL_BANK_FALSE_POSITIVE","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating","loop_objective":"residual_false_positive_mining|counterexample_mining|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Bank-label policy beta, but premium digital-bank valuation lacks low-PBR capital-return mechanics.","evidence_source":"public policy/news map; Stock-Web OHLC for price","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-26","entry_price":30150,"MFE_30D_pct":1.66,"MFE_90D_pct":1.66,"MFE_180D_pct":1.66,"MFE_1Y_pct":1.66,"MFE_2Y_pct":1.66,"MAE_30D_pct":-17.74,"MAE_90D_pct":-33.50,"MAE_180D_pct":-38.67,"MAE_1Y_pct":-38.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-39.67,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C21-L6-018-KAKAOBANK-20240226__2024-02-26__30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KB-C21-4B-20241025","case_id":"C21-L6-018-KB-4B-20241025","symbol":"105560","company_name":"KB금융","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"LOCAL_PRICE_BLOWOFF_AFTER_VALUE_UP","sector":"금융·자본배분·디지털금융","primary_archetype":"ROE/PBR capital return rerating 4B overlay","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2024-10-25","evidence_available_at_that_date":"Local price blowoff after C21 rerating; no hard thesis deterioration available at trigger date.","evidence_source":"Stock-Web OHLC for price; public event/news map for non-price status","stage2_evidence_fields":[],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":101000,"MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":13.66,"MFE_1Y_pct":13.66,"MFE_2Y_pct":13.66,"MAE_30D_pct":-15.05,"MAE_90D_pct":-22.48,"MAE_180D_pct":-31.39,"MAE_1Y_pct":-31.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-06-10","peak_price":114800,"drawdown_after_peak_pct":-31.39,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.74,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_too_early","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C21-L6-018-KB-4B-20241025__2024-10-25__101000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C21-L6-018-KB-20240226","trigger_id":"KB-C21-S2A-20240226","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":16,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":"unknown_or_not_supported","shareholder_return_action_score":"unknown_or_not_supported","capital_buffer_score":"unknown_or_not_supported"},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":18,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":8,"shareholder_return_action_score":6,"capital_buffer_score":4},"weighted_score_after":84,"stage_label_after":"Stage2-Actionable / near-Green shadow","changed_components":["roe_pbr_capital_return_score","shareholder_return_action_score","capital_buffer_score"],"component_delta_explanation":"C21 quality components recognize low-PBR capital-return mechanics before full Green confirmation.","MFE_90D_pct":44.0,"MAE_90D_pct":-4.48,"score_return_alignment_label":"aligned_after_quality_boost","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C21-L6-018-HANA-20240226","trigger_id":"HANA-C21-S2A-20240226","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":15,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":"unknown_or_not_supported","shareholder_return_action_score":"unknown_or_not_supported","capital_buffer_score":"unknown_or_not_supported"},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":17,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":6,"shareholder_return_action_score":4,"capital_buffer_score":3},"weighted_score_after":79,"stage_label_after":"Stage3-Yellow shadow","changed_components":["roe_pbr_capital_return_score","shareholder_return_action_score","capital_buffer_score"],"component_delta_explanation":"Positive but lower-conviction C21 rerating; quality scaling prevents treating it as identical to KB.","MFE_90D_pct":22.38,"MAE_90D_pct":-6.86,"score_return_alignment_label":"moderately_aligned_after_quality_boost","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C21-L6-018-WOORI-20240226","trigger_id":"WOORI-C21-S2A-20240226","symbol":"316140","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":6,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":12,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":"unknown_or_not_supported","shareholder_return_action_score":"unknown_or_not_supported","capital_buffer_score":"unknown_or_not_supported"},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":5,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":14,"valuation_repricing_score":10,"execution_risk_score":10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":2,"shareholder_return_action_score":1,"capital_buffer_score":1,"policy_theme_only_guard":-7},"weighted_score_after":66,"stage_label_after":"Stage2-Watch","changed_components":["policy_theme_only_guard","roe_pbr_capital_return_score"],"component_delta_explanation":"Sector policy headline alone overpromotes; weak MFE/MAE supports guard.","MFE_90D_pct":5.95,"MAE_90D_pct":-10.12,"score_return_alignment_label":"improved_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C21-L6-018-KAKAOBANK-20240226","trigger_id":"KAKAOBANK-C21-S2A-20240226","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":4,"relative_strength_score":4,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":10,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":"unknown_or_not_supported","shareholder_return_action_score":"unknown_or_not_supported","capital_buffer_score":"unknown_or_not_supported"},"weighted_score_before":71,"stage_label_before":"Stage2-Actionable false positive","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":2,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":10,"valuation_repricing_score":4,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"roe_pbr_capital_return_score":0,"shareholder_return_action_score":0,"capital_buffer_score":0,"premium_bank_false_positive_guard":-14},"weighted_score_after":54,"stage_label_after":"Blocked / Watch-only","changed_components":["premium_bank_false_positive_guard","policy_theme_only_guard","execution_risk_score"],"component_delta_explanation":"Premium digital-bank mismatch should block C21 positive promotion.","MFE_90D_pct":1.66,"MAE_90D_pct":-33.5,"score_return_alignment_label":"guard_correct","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C21-L6-018-KB-4B-20241025","trigger_id":"KB-C21-4B-20241025","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":20,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":16},"weighted_score_before":"risk_overlay","stage_label_before":"Stage4B price-only temptation","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":18,"valuation_repricing_score":20,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"positioning_overheat_score":16,"c21_price_only_4b_guard":-10},"weighted_score_after":"overlay_only","stage_label_after":"4B-watch-not-full","changed_components":["c21_price_only_4b_guard"],"component_delta_explanation":"Local peak proximity was high but full-window proximity was lower; no non-price deterioration.","MFE_90D_pct":2.87,"MAE_90D_pct":-22.48,"score_return_alignment_label":"full_4B_guard_correct","current_profile_verdict":"current_profile_4B_too_early"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_roe_pbr_capital_return_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"Low-PBR financials with visible shareholder-return route produced materially better 90D/180D MFE than policy-only cases.","Improves KB/Hana alignment without promoting KakaoBank.","KB-C21-S2A-20240226|HANA-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_shareholder_return_action_score,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+2,+2,"Firm-level buyback/cancellation/dividend visibility is the missing mechanism between policy headline and rerating.","Raises quality cases toward Yellow/Green shadow.","KB-C21-S2A-20240226|HANA-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_policy_theme_only_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-2,-2,"Sector-wide value-up headlines overpromote weak conversion cases.","Caps Woori-style sector beta at Watch/low Stage2 unless firm-level capital return appears.","WOORI-C21-S2A-20240226",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_premium_bank_false_positive_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-4,-4,"Premium digital-bank valuation lacks low-PBR capital-return re-rating mechanics and produced severe MAE.","Blocks KakaoBank-style false positives from C21 promotion.","KAKAOBANK-C21-S2A-20240226",4,4,2,high,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_price_only_4b_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,keep_or_strengthen,+0,"Price-only local peak in KB was too early relative to later full-window peak.","Keeps 4B as overlay unless non-price deterioration exists.","KB-C21-4B-20241025",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"18","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["sector_policy_theme_false_positive","premium_bank_false_positive","C21_quality_gate_missing","price_only_local_4B_too_early","Green_lateness_in_capital_return_compounder"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"all_selected_representative_rows_have_clean_180D_forward_windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/&lt;prefix&gt;/&lt;ticker&gt;/&lt;year&gt;.csv.
- Symbol profile pattern: atlas/symbol_profiles/&lt;prefix&gt;/&lt;ticker&gt;.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight &gt; 0.
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
next_round = R13_loop_19_L6_nonbank_brokerage_capital_return_or_batch_implementation
candidate_next_archetypes = [C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_nonbank_holdout, C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP, L6_C21_vs_C22_cross_profile_merge]
carry_forward_rules = [c21_roe_pbr_capital_return_score, c21_shareholder_return_action_score, c21_policy_theme_only_guard, c21_premium_bank_false_positive_guard, c21_price_only_4b_guard]
```

## 28. Source Notes

- Songdaiki/stock-web manifest: atlas/manifest.json.
- Songdaiki/stock-web schema: atlas/schema.json.
- Songdaiki/stock-web symbol profiles: 105560, 086790, 316140, 323410.
- Songdaiki/stock-web 2024 tradable OHLC shards: atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv, atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv, atlas/ohlcv_tradable_by_symbol_year/316/316140/2024.csv, atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv.
- Policy/event source map used for evidence labelling: Korea Corporate Value-up Programme public announcements and follow-up reporting in 2024; company-level capital-return and shareholder-return disclosures/news used as qualitative evidence map only, not as live screening.
- All price calculations use raw/unadjusted Stock-Web OHLC and should not be interpreted as total-return backtests.
