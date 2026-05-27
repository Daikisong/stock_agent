# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 35
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN / DIGITAL_BANK_VALUEUP_FALSE_POSITIVE / SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE
output_file = e2r_stock_web_v12_residual_round_R6_loop_35_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
production_scoring_changed = false
shadow_weight_only = true
```

This file is historical calibration research only. It is not a live stock recommendation, not a watchlist, and not a repository implementation patch.

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
previous_baseline_reference = e2r_2_0_baseline_reference
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

This loop does not re-prove the already applied Stage2/Green/4B global rules. It stress-tests whether a financial-sector policy event should be promoted when the company-level capital-return bridge is absent.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| round | R6 |
| loop | 35 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN; DIGITAL_BANK_VALUEUP_FALSE_POSITIVE; SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; canonical_archetype_compression |
| selection_mode | auto_coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Connector search against `Songdaiki/stock_agent` for `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`, KB금융, 하나금융지주, 카카오뱅크, 제주은행 returned no directly matching calibration artifacts in the accessible search result set. Therefore this loop is treated as a new C21 coverage fill rather than a schema rematerialization of an existing trigger table.

The immediately previous conversation artifact was C20 beauty/global distribution. This loop deliberately moves to L6/C21 and uses four new symbols.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

| manifest field | value |
|---|---|
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

Primary price basis:

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 5. Historical Eligibility Gate

All representative triggers have entry dates inside stock-web tradable shards and have at least 180 trading days of forward data available. No 2024 entry-to-D+180 window overlaps a listed corporate-action candidate date in the checked symbol profiles. 2Y windows are not used for quantitative calibration because several 2024 entries would require data beyond the manifest max date of 2026-02-20.

| symbol | company | profile path | corporate_action_window_status | calibration use |
|---|---|---|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | clean_180D_window | usable |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | clean_180D_window | usable |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | clean_180D_window | usable |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | clean_180D_window; old corporate-action candidates not in 2024 window | usable |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Policy + low-PBR/ROE + explicit shareholder-return route |
| DIGITAL_BANK_VALUEUP_FALSE_POSITIVE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same sector headline but missing low-PBR/capital-return bridge |
| SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Price-only low-PBR theme; useful as guard, not positive promotion |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best_trigger | current_profile_verdict |
|---|---:|---|---|---|---|---|
| R6L35-C21-KB-20240227 | 105560 | KB금융 | structural_success | positive | R6L35-C21-KB-S2-20240227 | current_profile_correct |
| R6L35-C21-HANA-20240227 | 086790 | 하나금융지주 | structural_success | positive | R6L35-C21-HANA-S2-20240227 | current_profile_correct |
| R6L35-C21-KAKAOBANK-20240227 | 323410 | 카카오뱅크 | failed_rerating | counterexample | R6L35-C21-KAKAOBANK-S2-20240227 | current_profile_false_positive |
| R6L35-C21-JEJUBANK-20240124 | 006220 | 제주은행 | price_moved_without_evidence | counterexample | R6L35-C21-JEJUBANK-S2-20240124 | current_profile_correct |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
```

The balance is intentionally symmetrical: KB금융 and 하나금융지주 test the capital-return-positive branch; 카카오뱅크 and 제주은행 test the policy-beta/theme false-positive branch.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R6L35-C21-KB-20240227 | Value-up policy event; low-PBR bank rerating; relative strength | Q1/shareholder-return confirmation; financial visibility | valuation/positioning overheat near Oct peak | watch only |
| R6L35-C21-HANA-20240227 | Value-up policy event; low-PBR bank rerating; relative strength | Q1/shareholder-return confirmation; financial visibility | valuation/positioning overheat near Oct peak | watch only |
| R6L35-C21-KAKAOBANK-20240227 | Same policy headline, but no low-PBR/capital-return bridge | none strong enough for Green | valuation premium / weak rerating | thesis evidence broken for C21 promotion |
| R6L35-C21-JEJUBANK-20240124 | Low-PBR theme + relative strength | none | price-only local blowoff | hard post-peak drawdown |

External context used: Korea’s Corporate Value-up Programme was announced in February 2024 to encourage listed companies to improve shareholder returns and stock prices; subsequent reporting noted market disappointment and possible tougher measures. Company-specific capital-return details are treated as evidence-family proxies for this research MD, not as repository-ingested live signals.

## 10. Price Data Source Map

| symbol | entry year shard | later year shard | profile |
|---:|---|---|---|
| 105560 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/ohlcv_tradable_by_symbol_year/105/105560/2025.csv | atlas/symbol_profiles/105/105560.json |
| 086790 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/ohlcv_tradable_by_symbol_year/086/086790/2025.csv | atlas/symbol_profiles/086/086790.json |
| 323410 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/ohlcv_tradable_by_symbol_year/323/323410/2025.csv | atlas/symbol_profiles/323/323410.json |
| 006220 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | atlas/ohlcv_tradable_by_symbol_year/006/006220/2025.csv | atlas/symbol_profiles/006/006220.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | evidence family | dedupe_for_aggregate |
|---|---|---|---|---|---:|---|---|
| R6L35-C21-KB-S2-20240227 | R6L35-C21-KB-20240227 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 62400 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal, financial_visibility, low_red_team_risk | true |
| R6L35-C21-KB-S3G-20240426 | R6L35-C21-KB-20240227 | Stage3-Green | 2024-04-25 | 2024-04-26 | 76000 | public_event_or_disclosure, policy_or_regulatory_optionality, confirmed_revision, financial_visibility, multiple_public_sources, low_red_team_risk | false |
| R6L35-C21-KB-4B-20241025 | R6L35-C21-KB-20240227 | 4B | 2024-10-25 | 2024-10-25 | 101000 | valuation_blowoff, positioning_overheat | false |
| R6L35-C21-HANA-S2-20240227 | R6L35-C21-HANA-20240227 | Stage2-Actionable | 2024-02-26 | 2024-02-27 | 54700 | public_event_or_disclosure, policy_or_regulatory_optionality, relative_strength, early_revision_signal, financial_visibility, low_red_team_risk | true |
| R6L35-C21-HANA-S3G-20240426 | R6L35-C21-HANA-20240227 | Stage3-Green | 2024-04-26 | 2024-04-26 | 60000 | public_event_or_disclosure, policy_or_regulatory_optionality, confirmed_revision, financial_visibility, multiple_public_sources, low_red_team_risk | false |
| R6L35-C21-KAKAOBANK-S2-20240227 | R6L35-C21-KAKAOBANK-20240227 | Stage2-Actionable-candidate | 2024-02-26 | 2024-02-27 | 29550 | public_event_or_disclosure, policy_or_regulatory_optionality, valuation_blowoff, thesis_evidence_broken | true |
| R6L35-C21-JEJUBANK-S2-20240124 | R6L35-C21-JEJUBANK-20240124 | Stage2-candidate-price-only | 2024-01-24 | 2024-01-24 | 9000 | relative_strength, policy_or_regulatory_optionality, price_only_local_peak, positioning_overheat, thesis_evidence_broken | true |
| R6L35-C21-JEJUBANK-4B-20240419 | R6L35-C21-JEJUBANK-20240124 | 4B | 2024-04-19 | 2024-04-19 | 14910 | price_only_local_peak, positioning_overheat, thesis_evidence_broken | false |


## 12. Trigger-Level OHLC Backtest Tables

Representative and comparison trigger metrics are below. Percent fields use `tradable_raw` OHLC from stock-web.

| trigger_id | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R6L35-C21-KB-S2-20240227 | 62400 | 25.96 | -2.4 | 44.23 | -2.4 | 66.51 | -2.4 | 2024-10-25 | 103900 | -26.47 |
| R6L35-C21-KB-S3G-20240426 | 76000 | 9.74 | -5.39 | 21.58 | -5.39 | 36.71 | -5.39 | 2024-10-25 | 103900 | -26.47 |
| R6L35-C21-KB-4B-20241025 | 101000 | 2.87 | -11.98 | 2.87 | -22.08 | 2.87 | -24.36 | 2024-10-25 | 103900 | -26.47 |
| R6L35-C21-HANA-S2-20240227 | 54700 | 19.2 | -3.47 | 23.95 | -5.67 | 26.51 | -5.67 | 2024-10-25 | 69200 | -18.35 |
| R6L35-C21-HANA-S3G-20240426 | 60000 | 8.83 | -5.33 | 13.0 | -5.33 | 15.33 | -5.33 | 2024-10-25 | 69200 | -18.35 |
| R6L35-C21-KAKAOBANK-S2-20240227 | 29550 | 3.72 | -14.38 | 3.72 | -32.15 | 3.72 | -32.42 | 2024-02-27 | 30650 | -34.85 |
| R6L35-C21-JEJUBANK-S2-20240124 | 9000 | 78.33 | -17.0 | 87.78 | -17.0 | 87.78 | -17.0 | 2024-04-19 | 16900 | -60.06 |
| R6L35-C21-JEJUBANK-4B-20240419 | 14910 | 5.9 | -19.45 | 5.9 | -43.39 | 5.9 | -54.73 | 2024-04-19 | 16900 | -60.06 |


Aggregate representative trigger result:

| set | count | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 |
|---|---:|---:|---:|---:|---:|
| all representatives | 4 | 39.92 | -14.3 | 46.13 | -14.37 |
| positive representatives | 2 | 34.09 | -4.04 | 46.51 | -4.04 |
| counterexample representatives | 2 | 45.75 | -24.57 | 45.75 | -24.71 |

Interpretation: KB/Hana did not merely bounce; they sustained 180D positive MFE with limited early MAE. KakaoBank had almost no upside after the common policy event and large downside. JejuBank had large MFE, but it came from a price-only low-PBR theme and later collapsed; it should train the guard, not the positive rule.

## 13. Current Calibrated Profile Stress Test

| case_id | P0 expected judgment | actual path | verdict |
|---|---|---|---|
| R6L35-C21-KB-20240227 | Stage2-Actionable accepted; Green waits for confirmation | MFE180 +66.51 / MAE180 -2.40 | current_profile_correct |
| R6L35-C21-HANA-20240227 | Stage2-Actionable accepted; Green waits for confirmation | MFE180 +26.51 / MAE180 -5.67 | current_profile_correct |
| R6L35-C21-KAKAOBANK-20240227 | Risk of Stage2 overpromotion from sector policy event | MFE180 +3.72 / MAE180 -32.42 | current_profile_false_positive |
| R6L35-C21-JEJUBANK-20240124 | Price-only blowoff guard should block positive stage | MFE90 +87.78 but post-peak drawdown -60.06 | current_profile_correct |

Axis answers:

1. `stage2_actionable_evidence_bonus`: correct for KB/Hana, too permissive for KakaoBank unless C21 capital-return bridge is required.
2. `stage3_yellow_total_min = 75`: kept. It avoids premature Green in KakaoBank/JejuBank.
3. `stage3_green_total_min = 87` and `stage3_green_revision_min = 55`: kept. Green was moderately late in KB/Hana but not disastrous.
4. `price_only_blowoff_blocks_positive_stage`: strengthened by 제주은행.
5. `full_4b_requires_non_price_evidence`: strengthened. 제주은행 local peak is not a structural Stage3 exit; it is a guard overlay.
6. `hard_4c_thesis_break_routes_to_4c`: kept. KakaoBank and 제주은행 show that thesis-break protection matters after C21 evidence fails.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3/Green entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 62,400 | 76,000 | 103,900 | 0.328 | Green somewhat late but still left meaningful upside |
| 하나금융지주 | 54,700 | 60,000 | 69,200 | 0.366 | Green somewhat late; Stage2 was still more efficient |
| 카카오뱅크 | 29,550 | n/a | 30,650 | n/a | no valid Green trigger; policy event failed |
| 제주은행 | 9,000 | n/a | 16,900 | n/a | no valid Green trigger; price-only theme |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | 4B evidence type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R6L35-C21-KB-4B-20241025 | valuation_blowoff; positioning_overheat | 0.930 | 0.930 | good_full_window_4B_timing |
| R6L35-C21-JEJUBANK-4B-20240419 | price_only; positioning_overheat | 0.748 | 0.748 | price_only_local_4B_too_early_without_non_price_evidence |

KB shows a cleaner 4B overlay because the prior Stage2 thesis was valid. 제주은행 shows why price-only peaks should not be interpreted as full 4B from a valid Stage3 thesis; the thesis was never validated.

## 16. 4C Protection Audit

| case | 4C label | protection interpretation |
|---|---|---|
| KB금융 | thesis_break_watch_only | no hard 4C; drawdown after peak is risk overlay, not thesis destruction |
| 하나금융지주 | thesis_break_watch_only | no hard 4C; lower slope than KB but still not a hard break |
| 카카오뱅크 | hard_4c_success | C21 thesis was broken early because policy event lacked capital-return bridge; MAE90 -32.15 |
| 제주은행 | hard_4c_success | price-only theme collapsed after peak; hard protection would have helped once no company-level evidence appeared |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
axis = financial_valueup_policy_event_requires_capital_return_bridge
proposal_type = sector_shadow_only
```

Candidate rule: in L6, a government policy/value-up event should not by itself receive positive Stage2 promotion unless at least one company-level capital-return bridge exists: explicit buyback/cancellation/dividend increase, CET1/capital surplus return plan, ROE/PBR improvement target, or credible management capital allocation plan. Otherwise, policy_event_or_disclosure is a watch catalyst, not positive evidence.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
axis_1 = c21_explicit_capital_return_bridge_required
axis_2 = c21_digital_bank_valueup_guard
axis_3 = c21_small_bank_price_only_theme_guard
```

C21 should separate three visually similar but economically different mechanisms:

- **Bank value-up rerating**: low PBR/ROE + explicit capital return. KB/Hana validate this.
- **Digital-bank policy false positive**: financial label + policy event but no PBR discount/capital-return bridge. KakaoBank is the counterexample.
- **Small-bank theme spike**: low-PBR or M&A-style price response without evidence. 제주은행 is a guard case.

## 19. Before / After Backtest Comparison

| profile | scope | eligible reps | avg_MFE90 | avg_MAE90 | false_positive_rate | missed_structural_count | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | global current | 4 | 39.92 | -14.3 | 0.25 | 0 | good but C21 policy false positive remains |
| P0b e2r_2_0_baseline_reference | old baseline | 4 | 39.92 | -14.3 | 0.50 | 0 | weaker guards; more likely to overpromote Jeju/KakaoBank |
| P1 sector_specific_candidate_profile | L6 sector | 4 | 39.92 | -14.3 | 0.00 | 0 | policy event needs capital-return bridge |
| P2 canonical_archetype_candidate_profile | C21 | 4 | 39.92 | -14.3 | 0.00 | 0 | best explanatory fit |
| P3 counterexample_guard_profile | C21 guard | 4 | 39.92 | -14.3 | 0.00 | 0 | strongest guard; may under-score very early policy beta |

## 20. Score-Return Alignment Matrix

| trigger_id | P0 score label | proposed label | return alignment |
|---|---|---|---|
| R6L35-C21-KB-S2-20240227 | Stage2-Actionable / 78.0 | Stage2-Actionable / 80.0 | aligned_positive |
| R6L35-C21-HANA-S2-20240227 | Stage2-Actionable / 76.0 | Stage2-Actionable / 78.0 | aligned_positive |
| R6L35-C21-KAKAOBANK-S2-20240227 | Stage2-Actionable / 74.0 | Watch/Blocked / 56.0 | false_positive_reduced |
| R6L35-C21-JEJUBANK-S2-20240124 | Stage2-candidate / 68.0 | Price-only/4B-watch / 44.0 | price_only_guard_kept |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | mixed C21 financial value-up | 2 | 2 | 2 | 2 | 4 | 0 | 8 | 4 | 1 | true | true | still needs insurance/holding-company cross-check and more 4C hard-break cases |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 3
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 1
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c]
residual_error_types_found: [policy_event_overpromotion_without_capital_return_bridge, digital_bank_valueup_false_positive]
new_axis_proposed: [c21_explicit_capital_return_bridge_required, c21_digital_bank_valueup_guard, c21_small_bank_price_only_theme_guard]
existing_axis_strengthened: [price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
existing_axis_weakened: []
existing_axis_kept: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, stage3_green_revision_min, hard_4c_thesis_break_routes_to_4c]
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L6/C21 financial value-up capital-return positive/counterexample coverage
diversity_score_summary: high; all four cases are new symbols in C21, with two positives, two counterexamples, and one current-profile residual false positive.
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- stock-web manifest max date and price basis.
- symbol profile availability and corporate-action candidate status.
- 2024 tradable OHLC rows for representative and comparison trigger windows.
- 30D/90D/180D MFE/MAE calculations using `tradable_raw` OHLC.
- same_entry_group/dedupe logic for aggregate metrics.

Not validated:

- no production scoring code was opened.
- no `src/e2r` files were inspected.
- no live scan was run.
- no current investment recommendation is made.
- company disclosure ingestion was not automated; evidence families are historical research labels for calibration only.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_capital_return_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Value-up policy headline works only when paired with low-PBR/ROE and explicit capital-return route","KB/Hana positive retained; KakaoBank false positive blocked",R6L35-C21-KB-S2-20240227|R6L35-C21-HANA-S2-20240227|R6L35-C21-KAKAOBANK-S2-20240227,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_bank_valueup_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank PBR premium without payout bridge is not the same as value-up capital-return rerating","KakaoBank MFE90 3.72 vs MAE90 -32.15",R6L35-C21-KAKAOBANK-S2-20240227,1,1,1,medium,counterexample_guard,"not production"
shadow_weight,c21_small_bank_price_only_theme_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Small-bank low-PBR theme spike can show large MFE but should route to 4B/4C guard unless company evidence appears","JejuBank MFE90 87.78 but post-peak drawdown -60.06",R6L35-C21-JEJUBANK-S2-20240124|R6L35-C21-JEJUBANK-4B-20240419,1,1,1,low,counterexample_guard,"not production"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L35-C21-KB-20240227","symbol":"105560","company_name":"KB금융","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L35-C21-KB-S2-20240227","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Value-up policy moved the whole sector, but KB had bank-scale ROE/PBR discount plus visible capital-return route; the later Q1/shareholder-return trigger did not replace the Stage2 entry, it only confirmed it."}
{"row_type":"case","case_id":"R6L35-C21-HANA-20240227","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L35-C21-HANA-S2-20240227","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Similar sector rerating channel, but lower 180D slope than KB; still validates capital-return-supported bank rerating rather than pure policy beta."}
{"row_type":"case","case_id":"R6L35-C21-KAKAOBANK-20240227","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_VALUEUP_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L35-C21-KAKAOBANK-S2-20240227","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_false_positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Same value-up headline and financial-sector bucket, but no low-PBR/capital-return bridge. P0 can over-score this if policy_event + financial label are allowed to stand in for actual capital return."}
{"row_type":"case","case_id":"R6L35-C21-JEJUBANK-20240124","symbol":"006220","company_name":"제주은행","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L35-C21-JEJUBANK-S2-20240124","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"current_profile_correct","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Huge price response before durable capital-return evidence. Useful for strengthening price-only/local-peak guard inside C21, not for promoting positive scoring."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L35-C21-KB-S2-20240227","case_id":"R6L35-C21-KB-20240227","symbol":"105560","company_name":"KB금융","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Corporate Value-up Programme policy event plus low-PBR bank rerating route; entry next tradable close because timing/detail was not treated as a confirmed intraday company-specific disclosure.","evidence_source":"Reuters/FSC policy event; stock-web 105560 2024 tradable shard; KB company IR/Q1 shareholder-return context used as later confirmation only.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":62400,"MFE_30D_pct":25.96,"MFE_90D_pct":44.23,"MFE_180D_pct":66.51,"MFE_1Y_pct":66.51,"MFE_2Y_pct":null,"MAE_30D_pct":-2.4,"MAE_90D_pct":-2.4,"MAE_180D_pct":-2.4,"MAE_1Y_pct":-2.4,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-KB-20240227-62400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-KB-S3G-20240426","case_id":"R6L35-C21-KB-20240227","symbol":"105560","company_name":"KB금융","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-25","evidence_available_at_that_date":"Q1 result/shareholder-return confirmation after the policy-stage entry; treated as confirmation trigger, not new representative entry.","evidence_source":"Company earnings/shareholder-return disclosure family; stock-web 105560 2024 tradable shard.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":76000,"MFE_30D_pct":9.74,"MFE_90D_pct":21.58,"MFE_180D_pct":36.71,"MFE_1Y_pct":36.71,"MFE_2Y_pct":null,"MAE_30D_pct":-5.39,"MAE_90D_pct":-5.39,"MAE_180D_pct":-5.39,"MAE_1Y_pct":-5.39,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":0.328,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_but_useful_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-KB-20240426-76000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-KB-4B-20241025","case_id":"R6L35-C21-KB-20240227","symbol":"105560","company_name":"KB금융","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-10-25","evidence_available_at_that_date":"Valuation/repricing fatigue and local overheat near full-window high; overlay only, not thesis break.","evidence_source":"stock-web price path + valuation/positioning overlay proxy; non-price 4B evidence not strong enough for hard exit.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-10-25","entry_price":101000,"MFE_30D_pct":2.87,"MFE_90D_pct":2.87,"MFE_180D_pct":2.87,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.98,"MAE_90D_pct":-22.08,"MAE_180D_pct":-24.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-26.47,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.93,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-KB-20241025-101000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-HANA-S2-20240227","case_id":"R6L35-C21-HANA-20240227","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-26","evidence_available_at_that_date":"Value-up policy event plus bank low-PBR/ROE rerating route; later capital-return evidence confirms but does not redefine entry.","evidence_source":"Reuters/FSC policy event; stock-web 086790 2024 tradable shard; company IR/shareholder-return context later confirmation.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":54700,"MFE_30D_pct":19.2,"MFE_90D_pct":23.95,"MFE_180D_pct":26.51,"MFE_1Y_pct":26.51,"MFE_2Y_pct":null,"MAE_30D_pct":-3.47,"MAE_90D_pct":-5.67,"MAE_180D_pct":-5.67,"MAE_1Y_pct":-5.67,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200,"drawdown_after_peak_pct":-18.35,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-HANA-20240227-54700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-HANA-S3G-20240426","case_id":"R6L35-C21-HANA-20240227","symbol":"086790","company_name":"하나금융지주","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-26","evidence_available_at_that_date":"Q1/shareholder-return confirmation; Stage3 comparator only.","evidence_source":"Company earnings/shareholder-return disclosure family; stock-web 086790 2024 tradable shard.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":60000,"MFE_30D_pct":8.83,"MFE_90D_pct":13.0,"MFE_180D_pct":15.33,"MFE_1Y_pct":15.33,"MFE_2Y_pct":null,"MAE_30D_pct":-5.33,"MAE_90D_pct":-5.33,"MAE_180D_pct":-5.33,"MAE_1Y_pct":-5.33,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":69200,"drawdown_after_peak_pct":-18.35,"green_lateness_ratio":0.366,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_but_useful_green","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-HANA-20240426-60000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-KAKAOBANK-S2-20240227","case_id":"R6L35-C21-KAKAOBANK-20240227","symbol":"323410","company_name":"카카오뱅크","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"DIGITAL_BANK_VALUEUP_FALSE_POSITIVE","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable-candidate","trigger_date":"2024-02-26","evidence_available_at_that_date":"Same financial-sector value-up headline, but no low-PBR capital-return bridge; this is the residual false-positive test.","evidence_source":"Reuters/FSC policy event; stock-web 323410 2024 tradable shard; absence-of-capital-return treated as guard evidence.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-27","entry_price":29550,"MFE_30D_pct":3.72,"MFE_90D_pct":3.72,"MFE_180D_pct":3.72,"MFE_1Y_pct":3.72,"MFE_2Y_pct":null,"MAE_30D_pct":-14.38,"MAE_90D_pct":-32.15,"MAE_180D_pct":-32.42,"MAE_1Y_pct":-32.42,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-27","peak_price":30650,"drawdown_after_peak_pct":-34.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_for_failed_rerating","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-KAKAOBANK-20240227-29550","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-JEJUBANK-S2-20240124","case_id":"R6L35-C21-JEJUBANK-20240124","symbol":"006220","company_name":"제주은행","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"Stage2-candidate-price-only","trigger_date":"2024-01-24","evidence_available_at_that_date":"Low-PBR/value-up bank theme surge; no durable company-level capital-return plan at trigger date.","evidence_source":"stock-web 006220 2024 tradable shard; policy-theme context; no company-specific capital-return evidence used for promotion.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-24","entry_price":9000,"MFE_30D_pct":78.33,"MFE_90D_pct":87.78,"MFE_180D_pct":87.78,"MFE_1Y_pct":87.78,"MFE_2Y_pct":null,"MAE_30D_pct":-17.0,"MAE_90D_pct":-17.0,"MAE_180D_pct":-17.0,"MAE_1Y_pct":-25.0,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-60.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.893,"four_b_full_window_peak_proximity":0.893,"four_b_timing_verdict":"price_only_local_4B_requires_guard","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-JEJUBANK-20240124-9000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L35-C21-JEJUBANK-4B-20240419","case_id":"R6L35-C21-JEJUBANK-20240124","symbol":"006220","company_name":"제주은행","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","fine_archetype_id":"SMALL_BANK_LOW_PBR_THEME_PRICE_SPIKE","sector":"financials","primary_archetype":"ROE_PBR_CAPITAL_RETURN_VALUEUP","loop_objective":"coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test","trigger_type":"4B","trigger_date":"2024-04-19","evidence_available_at_that_date":"Price-only blowoff after multiple theme spikes; no non-price capital-return evidence, so this is overlay/guard, not a full structural exit from a valid Stage3.","evidence_source":"stock-web 006220 2024 tradable shard.","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-19","entry_price":14910,"MFE_30D_pct":5.9,"MFE_90D_pct":5.9,"MFE_180D_pct":5.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-19.45,"MAE_90D_pct":-43.39,"MAE_180D_pct":-54.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-60.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.748,"four_b_full_window_peak_proximity":0.748,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L35-C21-JEJUBANK-20240419-14910","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"P0_to_P2_c21_shadow","case_id":"R6L35-C21-KB-20240227","trigger_id":"R6L35-C21-KB-S2-20240227","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":45,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":65,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":70,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":80.0,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","revision_score"],"component_delta_explanation":"C21 shadow adds explicit capital-return intensity only when policy event is paired with bank ROE/PBR rerating and visible shareholder-return route.","MFE_90D_pct":44.23,"MAE_90D_pct":-2.4,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0_to_P2_c21_shadow","case_id":"R6L35-C21-HANA-20240227","trigger_id":"R6L35-C21-HANA-S2-20240227","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":45,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":65,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":50,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":75,"valuation_repricing_score":70,"execution_risk_score":15,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78.0,"stage_label_after":"Stage2-Actionable","changed_components":["valuation_repricing_score","revision_score"],"component_delta_explanation":"C21 shadow adds explicit capital-return intensity only when policy event is paired with bank ROE/PBR rerating and visible shareholder-return route.","MFE_90D_pct":23.95,"MAE_90D_pct":-5.67,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"P0_to_P2_c21_shadow","case_id":"R6L35-C21-KAKAOBANK-20240227","trigger_id":"R6L35-C21-KAKAOBANK-S2-20240227","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":45,"valuation_repricing_score":25,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":56.0,"stage_label_after":"Watch/Blocked","changed_components":["policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Digital-bank premium without low-PBR/capital-return bridge is blocked from C21 promotion.","MFE_90D_pct":3.72,"MAE_90D_pct":-32.15,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"P0_to_P2_c21_shadow","case_id":"R6L35-C21-JEJUBANK-20240124","trigger_id":"R6L35-C21-JEJUBANK-S2-20240124","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":85,"customer_quality_score":0,"policy_or_regulatory_score":60,"valuation_repricing_score":35,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68.0,"stage_label_before":"Stage2-candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":45,"customer_quality_score":0,"policy_or_regulatory_score":30,"valuation_repricing_score":15,"execution_risk_score":85,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":44.0,"stage_label_after":"Price-only/4B-watch","changed_components":["relative_strength_score","policy_or_regulatory_score","execution_risk_score"],"component_delta_explanation":"Small-bank low-PBR theme can move violently, but missing capital-return evidence turns it into 4B/4C guard evidence, not positive Stage2.","MFE_90D_pct":87.78,"MAE_90D_pct":-17.0,"score_return_alignment_label":"price_only_guard_kept","current_profile_verdict":"current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_capital_return_bridge_required,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Value-up policy headline works only when paired with low-PBR/ROE and explicit capital-return route","KB/Hana positive retained; KakaoBank false positive blocked",R6L35-C21-KB-S2-20240227|R6L35-C21-HANA-S2-20240227|R6L35-C21-KAKAOBANK-S2-20240227,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_digital_bank_valueup_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Digital-bank PBR premium without payout bridge is not the same as value-up capital-return rerating","KakaoBank MFE90 3.72 vs MAE90 -32.15",R6L35-C21-KAKAOBANK-S2-20240227,1,1,1,medium,counterexample_guard,"not production"
shadow_weight,c21_small_bank_price_only_theme_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,"Small-bank low-PBR theme spike can show large MFE but should route to 4B/4C guard unless company evidence appears","JejuBank MFE90 87.78 but post-peak drawdown -60.06",R6L35-C21-JEJUBANK-S2-20240124|R6L35-C21-JEJUBANK-4B-20240419,1,1,1,low,counterexample_guard,"not production"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"35","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence"],"residual_error_types_found":["policy_event_overpromotion_without_capital_return_bridge","digital_bank_valueup_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L6/C21 financial value-up capital-return positive/counterexample coverage"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L35-C21-FUTURE-INSURANCE-HOLDOUT","symbol":"000000","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","reason":"insurance_or_holding_company_cross_check_not_included_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
recommended_next_round = R6 / C22_INSURANCE_RATE_CYCLE_RESERVE or C21 insurance/holding-company holdout
reason = C21 now has bank/digital-bank/small-bank coverage, but still needs insurance-style capital-return and reserve-cycle cross-checks.
carry_forward_guard = C21 policy event requires company-level capital-return bridge.
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, max_date `2026-02-20`.
- Stock-Web profiles checked: `105560`, `086790`, `323410`, `006220`.
- Stock-Web 2024 tradable shards used for entry and 180D windows.
- Reuters/FSC public value-up programme reporting was used as historical policy-event context.
- This file intentionally avoids current/live candidate scanning and does not modify production scoring.
