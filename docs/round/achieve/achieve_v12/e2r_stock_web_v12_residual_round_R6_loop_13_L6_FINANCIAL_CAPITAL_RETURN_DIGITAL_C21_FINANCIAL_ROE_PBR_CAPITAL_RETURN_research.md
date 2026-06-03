# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R6
scheduled_loop: 13
completed_round: R6
completed_loop: 13
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id: BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME
output_file: e2r_stock_web_v12_residual_round_R6_loop_13_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
auto_trading_allowed: false
brokerage_api_allowed: false
round_schedule_status: valid
round_sector_consistency: pass
```

This loop adds 5 new independent cases, 3 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN.

## 1. Current Calibrated Profile Assumption

Current default profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are assumed to be present and are not re-proposed:

```text
stage2_actionable_evidence_bonus = +2.0
stage3_yellow_total_min = 75.0
stage3_green_total_min = 87.0
stage3_green_revision_min = 55.0
stage3_cross_evidence_green_buffer = +1.5
price_only_blowoff_blocks_positive_stage = true
full_4b_requires_non_price_evidence = true
hard_4c_thesis_break_routes_to_4c = true
```

The residual question is narrower: inside financials, when does a low-PBR/value-up move become a real C21 rerating, and when is it just sector beta wearing a bank costume? A bank stock is not re-rated because the ticker rises. It re-rates when the market sees the profit reservoir, the PBR gauge, and a valve that lets minority shareholders receive the pressure through dividends, buybacks, or cancellation.

## 2. Round / Large Sector / Canonical Archetype Scope

| Field | Value |
|---|---|
| scheduled_round | R6 |
| scheduled_loop | 13 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN |
| fine_archetype_id | BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME |
| loop_objective | coverage_gap_fill; counterexample_mining; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test |
| invalid_round_sector_pair | false |
| computed_next_round | R7 |
| computed_next_loop | 13 |

R6 hard gate passes because `R6 -> L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research-artifact access was used only for duplicate avoidance and schedule resolution. The local v12 file set already contains:

```text
R6 loop 10: C22_INSURANCE_RATE_CYCLE_RESERVE
R6 loop 11: C22_INSURANCE_RATE_CYCLE_RESERVE
R6 loop 12: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN with KB금융, 하나금융지주, 카카오뱅크, 제주은행
```

This loop therefore avoids those symbols and trigger families. It adds new C21 evidence through 신한지주, 메리츠금융지주, 기업은행, 카카오페이, and 푸른저축은행.

| Novelty gate | Value |
|---|---:|
| new_independent_case_count | 5 |
| reused_case_count | 0 |
| new_symbol_count | 5 |
| same_archetype_new_symbol_count | 5 |
| same_archetype_new_trigger_family_count | 5 |
| new_independent_case_ratio | 1.00 |
| positive_case_count | 2 |
| counterexample_count | 3 |
| loop_contribution_label | canonical_archetype_rule_candidate |

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web inputs inspected:

```text
atlas/manifest.json
atlas/schema.json
atlas/universe/all_symbols.csv
atlas/symbol_profiles/055/055550.json
atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv
atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv
atlas/ohlcv_tradable_by_symbol_year/138/138040/2025.csv
atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv
atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv
atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv
```

Manifest validation:

| Field | Value |
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
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

The price basis is `tradable_raw`. It is raw/unadjusted marcap OHLC, not split-adjusted total-return data.

## 5. Historical Eligibility Gate

| Symbol | Company | Entry date | 180D forward window | Corporate-action window status | Calibration usable |
|---|---|---|---:|---|---|
| 055550 | 신한지주 | 2024-02-26 | yes | clean_180D_window | true |
| 138040 | 메리츠금융지주 | 2024-06-28 | yes, using 2024 and 2025 shards | clean_180D_window | true |
| 024110 | 기업은행 | 2024-02-26 | yes | clean_180D_window | true |
| 377300 | 카카오페이 | 2024-02-26 | yes | clean_180D_window | true |
| 007330 | 푸른저축은행 | 2024-01-31 | yes | clean_180D_window | true |

No selected representative row is blocked for insufficient forward window or price-source validation failure.

## 6. Canonical Archetype Compression Map

```text
C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
  -> BANK_VALUEUP_ROE_PBR_SHAREHOLDER_RETURN
  -> CAPITAL_RETURN_CADENCE_CONFIRMED_RERATING
  -> POLICY_BANK_UNDERPOWERED_LOW_PBR
  -> DIGITAL_FINANCE_BETA_FALSE_GREEN
  -> LOCAL_BANK_PRICE_ONLY_SPIKE
```

Compression rule: a financial stock can belong to C21 only if the evidence proves both valuation repair and shareholder-transfer mechanism. ROE without capital return is trapped pressure. PBR discount without a credible release valve is only an optically cheap container.

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | best_trigger | current_profile_verdict | notes |
|---|---|---|---|---|---|---|---|
| R6L13_C21_SHINHAN_20240226_VALUEUP_CAPITAL_RETURN_SUCCESS | 055550 | 신한지주 | structural_success | positive | R6L13_C21_SHINHAN_T2A_20240226 | current_profile_correct | Low-PBR bank with public value-up/capital-return optionality and later price confirmation. Entry row 2024-02-26 close 41,350 was checked in stock-web 055/055550/2024.csv. |
| R6L13_C21_MERITZ_20240628_CAPITAL_RETURN_CADENCE_SUCCESS | 138040 | 메리츠금융지주 | structural_success | positive | R6L13_C21_MERITZ_T2A_20240628 | current_profile_too_late | Capital-return cadence and integrated financial-holding model produced a delayed but strong rerating. Entry row 2024-06-28 close 79,100 was checked in stock-web 138/138040/2024.csv. |
| R6L13_C21_IBK_20240226_POLICY_BANK_UNDERPOWERED_RERATING | 024110 | 기업은행 | failed_rerating | counterexample | R6L13_C21_IBK_T2_20240226 | current_profile_false_positive | A value-up/bank-beta move occurred, but policy-bank overhang and weaker minority-shareholder return proof made the rerating shallow. Entry row 2024-02-26 close 13,400 was checked in stock-web 024/024110/2024.csv. |
| R6L13_C21_KAKAOPAY_20240226_DIGITAL_FINANCE_FALSE_GREEN | 377300 | 카카오페이 | false_positive_green | counterexample | R6L13_C21_KAKAOPAY_T2_REJECT_20240226 | current_profile_false_positive | Digital-finance beta could borrow the financial-sector headline, but lacked ROE/PBR repair and capital-return evidence. Entry row 2024-02-26 close 46,600 was checked in stock-web 377/377300/2024.csv. |
| R6L13_C21_PUREUN_20240131_LOCAL_BANK_PRICE_ONLY_SPIKE | 007330 | 푸른저축은행 | price_moved_without_evidence | counterexample | R6L13_C21_PUREUN_T2_REJECT_20240131 | current_profile_correct | Small financial/local-bank theme spike produced large local MFE but no durable ROE/PBR/capital-return proof. Entry row 2024-01-31 close 10,400 was checked in stock-web 007/007330/2024.csv. |


## 8. Positive vs Counterexample Balance

| Metric | Count |
|---|---:|
| positive_structural_success | 2 |
| counterexample_or_failed_rerating | 3 |
| 4B_or_4C_case | 4 overlay/watch labels |
| calibration_usable_case_count | 5 |
| calibration_usable_trigger_count | 7 |
| representative_trigger_count | 5 |

The positive side is Shinhan/Meritz: capital-return credibility and low-PBR repair were visible before the full price path matured. The counterexample side is IBK/KakaoPay/Pureun: either the shareholder-return valve was weak, the stock was not really a low-PBR financial rerating, or the move was a price-only local spike.

## 9. Evidence Source Map

| Case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| 신한지주 | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength; early_revision_signal | financial_visibility; multiple_public_sources; low_red_team_risk | later valuation/positioning overlay | none |
| 메리츠금융지주 | public_event_or_disclosure; relative_strength; financial_visibility; early_revision_signal | confirmed_revision; financial_visibility; low_red_team_risk | later valuation/positioning overlay | none |
| 기업은행 | public_event_or_disclosure; policy_or_regulatory_optionality; relative_strength | weak financial visibility only | policy_bank_overhang | watch only |
| 카카오페이 | relative_strength only | none | price_only_local_peak | thesis_evidence_broken |
| 푸른저축은행 | relative_strength only | none | price_only_local_peak; positioning_overheat | event spike fade |

## 10. Price Data Source Map

| Symbol | Company | Price shard path | Profile path | Entry row anchor |
|---|---|---|---|---|
| 055550 | 신한지주 | atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv | atlas/symbol_profiles/055/055550.json | 2024-02-26 close 41,350 |
| 138040 | 메리츠금융지주 | atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv; 2025.csv | atlas/symbol_profiles/138/138040.json | 2024-06-28 close 79,100 |
| 024110 | 기업은행 | atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv | atlas/symbol_profiles/024/024110.json | 2024-02-26 close 13,400 |
| 377300 | 카카오페이 | atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv | atlas/symbol_profiles/377/377300.json | 2024-02-26 close 46,600 |
| 007330 | 푸른저축은행 | atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv | atlas/symbol_profiles/007/007330.json | 2024-01-31 close 10,400 |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | current_profile_verdict | aggregate_role |
|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| R6L13_C21_SHINHAN_T2A_20240226 | 055550 | 신한지주 | Stage2-Actionable | 2024-02-26 | 2024-02-26 | 41,350 | 24.55% | -3.63% | 31.08% | -3.63% | 56.23% | -3.63% | 2024-08-26 | 64,600 | current_profile_correct | representative |
| R6L13_C21_MERITZ_T2A_20240628 | 138040 | 메리츠금융지주 | Stage2-Actionable | 2024-06-28 | 2024-06-28 | 79,100 | 8.60% | -7.08% | 26.30% | -7.08% | 61.06% | -7.08% | 2025-03-06 | 127,400 | current_profile_too_late | representative |
| R6L13_C21_IBK_T2_20240226 | 024110 | 기업은행 | Stage2-candidate | 2024-02-26 | 2024-02-26 | 13,400 | 11.64% | -3.58% | 11.64% | -3.58% | 11.64% | -4.55% | 2024-03-13 | 14,960 | current_profile_false_positive | representative |
| R6L13_C21_KAKAOPAY_T2_REJECT_20240226 | 377300 | 카카오페이 | Stage2-candidate-rejected | 2024-02-26 | 2024-02-26 | 46,600 | 1.61% | -18.35% | 1.61% | -43.99% | 1.61% | -52.90% | 2024-02-26 | 47,350 | current_profile_false_positive | representative |
| R6L13_C21_PUREUN_T2_REJECT_20240131 | 007330 | 푸른저축은행 | Stage2-candidate-rejected | 2024-01-31 | 2024-01-31 | 10,400 | 41.44% | -17.79% | 41.44% | -17.79% | 41.44% | -30.38% | 2024-02-05 | 14,710 | current_profile_correct | representative |
| R6L13_C21_SHINHAN_T4B_20240826 | 055550 | 신한지주 | Stage4B | 2024-08-26 | 2024-08-26 | 61,400 | 5.21% | -13.84% | 5.21% | -13.84% | 5.21% | -13.84% | 2024-08-26 | 64,600 | current_profile_correct | 4B_overlay_only |
| R6L13_C21_MERITZ_T4B_20250306 | 138040 | 메리츠금융지주 | Stage4B | 2025-03-06 | 2025-03-06 | 127,200 | 0.16% | -15.80% | 0.16% | -15.80% | 0.16% | -15.80% | 2025-03-06 | 127,400 | current_profile_correct | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

Representative-trigger aggregate, deduped by same-entry group:

| Aggregate metric | Value |
|---|---:|
| avg_MFE_90D_pct | 22.41 |
| avg_MAE_90D_pct | -15.21 |
| avg_MFE_180D_pct | 34.40 |
| avg_MAE_180D_pct | -19.71 |
| positive avg_MFE_180D_pct | 58.64 |
| counterexample avg_MAE_180D_pct | -29.28 |

The aggregate is intentionally not used as a buy/sell result. It is used only to calibrate whether evidence families line up with later price paths.

## 13. Current Calibrated Profile Stress Test

| Case | Current profile verdict | Backtest alignment | Residual issue |
|---|---|---|---|
| 신한지주 | current_profile_correct | 90D and 180D MFE aligned with C21 evidence | no new global rule needed |
| 메리츠금융지주 | current_profile_too_late | delayed but large 180D MFE supports earlier C21 recognition | capital-return cadence under-credited |
| 기업은행 | current_profile_false_positive | shallow MFE and policy-bank overhang argue against Green | low-PBR beta overpromoted |
| 카카오페이 | current_profile_false_positive | digital-finance beta failed badly with large MAE | digital-finance beta must be excluded |
| 푸른저축은행 | current_profile_correct | large local MFE but price-only spike faded | price-only guard works |

Stress-test answers:

```text
stage2_actionable_evidence_bonus: useful for Shinhan/Meritz, too generous for IBK/KakaoPay unless C21 proof gates are added.
yellow_threshold_75: too permissive for digital-finance beta and policy-bank overhang.
green_threshold_87 / revision_55: correct globally, but Meritz shows that capital-return cadence can be a non-revision Green-quality signal.
price_only_blowoff_guard: strengthened by Pureun and KakaoPay.
full_4B_non_price_requirement: strengthened; Shinhan/Meritz 4B overlays require valuation/positioning plus non-price context.
hard_4C_routing: kept; counterexamples are thesis-break/watch rows, not pure price rows.
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | Green/revision trigger | green_lateness_ratio | interpretation |
|---|---|---|---:|---|
| 신한지주 | 2024-02-26 / 41,350 | 2024-03-14 / 51,500 proxy confirmation | 0.24 | Green was somewhat late but still captured a large part of the move. |
| 메리츠금융지주 | 2024-06-28 / 79,100 | 2024-08-23~2025-02 proxy confirmation | 0.36 | Current Green strictness risks chasing the move; capital-return cadence deserves earlier C21 credit. |
| 기업은행 | 2024-02-26 / 13,400 | no clean Green trigger | NA | No Green upgrade should occur; low-PBR beta alone did not become a strong rerating. |
| 카카오페이 | 2024-02-26 / 46,600 | none | NA | Digital beta is outside the C21 proof chain. |
| 푸른저축은행 | 2024-01-31 / 10,400 | none | NA | Price-only spike must stay outside Stage2/3 promotion. |


## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local_peak_proximity | full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R6L13_C21_IBK_T2_20240226 | 1.0 | 1.0 | valuation_blowoff;policy_bank_overhang | shallow_local_peak_not_full_4B |
| R6L13_C21_KAKAOPAY_T2_REJECT_20240226 | 1.0 | 1.0 | price_only;valuation_blowoff | price_only_local_4B_too_early_but_rejection_correct |
| R6L13_C21_PUREUN_T2_REJECT_20240131 | 1.0 | 1.0 | price_only;positioning_overheat | price_only_local_4B_not_positive_stage |
| R6L13_C21_SHINHAN_T4B_20240826 | 1.0 | 1.0 | valuation_blowoff;positioning_overheat;capital_return_repricing | good_full_window_4B_timing_after_valueup_rerating |
| R6L13_C21_MERITZ_T4B_20250306 | 1.0 | 1.0 | valuation_blowoff;positioning_overheat;capital_return_repricing | good_full_window_4B_timing_after_delayed_capital_return_rerating |


C21 4B should not be a raw price alarm. Shinhan and Meritz show legitimate 4B overlay after the capital-return rerating matures. Pureun and KakaoPay show the opposite: when the evidence is price-only, 4B is not a mature exit overlay; it is a sign the row should never have been promoted to positive Stage2/3.

## 16. 4C Protection Audit

| Case | 4C label | Protection interpretation |
|---|---|---|
| 카카오페이 | hard_4c_success | Digital-finance beta broke quickly; a C21 gate would prevent promotion before the drawdown. |
| 푸른저축은행 | false_break_or_event_spike_fade | The thesis never matured beyond price; 4C is narrative cleanup, not a late sell signal. |
| 기업은행 | thesis_break_watch_only | Weak capital-return proof and policy-bank overhang cap promotion rather than forcing hard 4C. |
| 신한지주 | not_applicable | No hard thesis break inside the validated window. |
| 메리츠금융지주 | not_applicable | No hard thesis break inside the validated window. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
rule_id = L6_price_only_financial_theme_guard
candidate_delta = +1 guard, not production
```

Within L6, price-only financial-sector rallies should be separated from capital-return reratings. The sector has many optical shortcuts: low nominal PBR, rate sensitivity, digital-finance optionality, local-bank scarcity. These are not equivalent to C21 unless the evidence shows minority shareholder return or durable ROE/PBR repair.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_id = C21_ROE_PBR_capital_return_confirmation_gate
candidate_delta = +1 gate / +1 exclusion
```

Proposed C21 rule:

```text
if canonical_archetype_id == C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN:
    promote Stage2/Yellow only when at least two are present:
        - explicit shareholder-return plan, buyback/cancellation, or payout acceleration
        - ROE/PBR repair narrative tied to financial visibility
        - low accounting/trust risk and no policy-bank minority overhang
    reject or cap if evidence is only:
        - digital-finance beta
        - local-bank price spike
        - generic value-up headline without shareholder-transfer mechanism
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | profile_hypothesis | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | score_return_alignment_verdict |
|---|---|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 = e2r_2_1_stock_web_calibrated_proxy | current | Existing global calibration, no C21-specific beta separation | none | 5 | representative trigger per case | 22.41 | -15.21 | 34.40 | -19.71 | 0.40 | 1 | 1 | 0.30 | 1.00 | 1.00 | good global risk control, but still too permissive on digital-finance and policy-bank beta |
| P0b = e2r_2_0_baseline_reference | rollback | Older profile over-promotes financial-sector price strength | rollback reference | 5 | representative trigger per case | 22.41 | -15.21 | 34.40 | -19.71 | 0.60 | 0 | 2 | 0.45 | 1.00 | 1.00 | worse false positive control |
| P1 = sector_specific_candidate_profile | sector_specific | Add L6 high-MAE and price-only financial beta guard | price_only_financial_beta_penalty | 5 | representative trigger per case | 22.41 | -15.21 | 34.40 | -19.71 | 0.20 | 1 | 1 | 0.30 | 1.00 | 1.00 | better sector-level risk separation |
| P2 = canonical_archetype_candidate_profile | canonical_archetype_specific | Require ROE/PBR repair plus credible minority shareholder return | C21_ROE_PBR_capital_return_gate; digital_finance_beta_exclusion | 5 | representative trigger per case | 22.41 | -15.21 | 34.40 | -19.71 | 0.00 | 0 | 1 | 0.30 | 1.00 | 1.00 | best score-return alignment |
| P3 = counterexample_guard_profile | canonical_archetype_specific | Very conservative: blocks all price-led finance themes until explicit return proof | strong minority-return gate | 5 | representative trigger per case | 22.41 | -15.21 | 34.40 | -19.71 | 0.00 | 1 | 0 | 0.20 | 1.00 | 1.00 | safest, but may delay Shinhan-like Stage2 |


## 20. Score-Return Alignment Matrix

| trigger_id | before score / label | after score / label | MFE90 / MAE90 | alignment verdict |
|---|---|---|---|---|
| R6L13_C21_SHINHAN_T2A_20240226 | 80 / Stage3-Yellow | 88 / Stage3-Green_candidate | 31.08 / -3.63 | aligned_positive |
| R6L13_C21_MERITZ_T2A_20240628 | 77 / Stage3-Yellow | 94 / Stage3-Green | 26.30 / -7.08 | aligned_positive |
| R6L13_C21_IBK_T2_20240226 | 76 / Stage3-Yellow_false_positive_risk | 61 / Stage2-watch_or_reject | 11.64 / -3.58 | counterexample_or_reject_aligned |
| R6L13_C21_KAKAOPAY_T2_REJECT_20240226 | 75 / Stage3-Yellow_false_positive_risk | 39 / Stage1/2_theme_watch_only | 1.61 / -43.99 | counterexample_or_reject_aligned |
| R6L13_C21_PUREUN_T2_REJECT_20240131 | 69 / Stage2-price_watch | 35 / Stage1/2_price_only_reject | 41.44 / -17.79 | counterexample_or_reject_aligned |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME | 2 | 3 | 2 | 2 | 5 | 0 | 7 | 5 | 3 | true | true | C21 now has non-KB/Hana bank positives plus digital-finance and small-bank counterexamples; C22 remains separately covered by older loops. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - digital_finance_beta_false_positive
  - policy_bank_lowPBR_overpromotion
  - capital_return_cadence_too_late
  - price_only_local_bank_spike
new_axis_proposed:
  - C21_ROE_PBR_capital_return_confirmation_gate
  - C21_digital_finance_beta_exclusion
  - L6_price_only_financial_theme_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level OHLC validation using Songdaiki/stock-web tradable rows.
- R6/C21 sector-archetype residual calibration.
- Stage2/Y/G/4B/4C label stress testing.
- Shadow-only sector/canonical rule proposal.
```

Non-validation scope:

```text
- No live stock discovery.
- No current recommendation.
- No stock_agent source-code access.
- No production scoring patch.
- No brokerage or auto-trading connection.
- No new price route discovery outside stock-web.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C21_ROE_PBR_capital_return_confirmation_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Promote only when low-PBR/ROE repair is paired with credible minority-shareholder return proof.,Preserves Shinhan/Meritz positives while rejecting IBK/KakaoPay/Pureun false positives.,R6L13_C21_SHINHAN_T2A_20240226|R6L13_C21_MERITZ_T2A_20240628,5,5,3,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C21_digital_finance_beta_exclusion,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Digital-finance optionality is not C21 evidence unless it creates ROE/PBR repair plus capital return.,Blocks KakaoPay false Green risk.,R6L13_C21_KAKAOPAY_T2_REJECT_20240226,5,5,3,medium,canonical_guard_shadow_only,not production; post-calibrated residual
shadow_weight,L6_price_only_financial_theme_guard,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Small financial/local-bank price spikes can have high MFE but should not promote Stage2/3 without non-price evidence.,Keeps Pureun as price-moved-without-evidence rather than structural positive.,R6L13_C21_PUREUN_T2_REJECT_20240131,5,5,3,low,sector_shadow_only,not production; post-calibrated residual
shadow_weight,C21_policy_bank_overhang_penalty,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,1,+1,Policy-bank ownership/overhang caps C21 promotion when minority-return proof is shallow.,Reduces IBK false-positive risk.,R6L13_C21_IBK_T2_20240226,5,5,3,low,canonical_guard_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L13_C21_SHINHAN_20240226_VALUEUP_CAPITAL_RETURN_SUCCESS", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L13_C21_SHINHAN_T2A_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR bank with public value-up/capital-return optionality and later price confirmation. Entry row 2024-02-26 close 41,350 was checked in stock-web 055/055550/2024.csv."}
{"row_type": "case", "case_id": "R6L13_C21_MERITZ_20240628_CAPITAL_RETURN_CADENCE_SUCCESS", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L13_C21_MERITZ_T2A_20240628", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "Capital-return cadence and integrated financial-holding model produced a delayed but strong rerating. Entry row 2024-06-28 close 79,100 was checked in stock-web 138/138040/2024.csv."}
{"row_type": "case", "case_id": "R6L13_C21_IBK_20240226_POLICY_BANK_UNDERPOWERED_RERATING", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L13_C21_IBK_T2_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "A value-up/bank-beta move occurred, but policy-bank overhang and weaker minority-shareholder return proof made the rerating shallow. Entry row 2024-02-26 close 13,400 was checked in stock-web 024/024110/2024.csv."}
{"row_type": "case", "case_id": "R6L13_C21_KAKAOPAY_20240226_DIGITAL_FINANCE_FALSE_GREEN", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L13_C21_KAKAOPAY_T2_REJECT_20240226", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_aligned", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Digital-finance beta could borrow the financial-sector headline, but lacked ROE/PBR repair and capital-return evidence. Entry row 2024-02-26 close 46,600 was checked in stock-web 377/377300/2024.csv."}
{"row_type": "case", "case_id": "R6L13_C21_PUREUN_20240131_LOCAL_BANK_PRICE_ONLY_SPIKE", "symbol": "007330", "company_name": "푸른저축은행", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L13_C21_PUREUN_T2_REJECT_20240131", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Small financial/local-bank theme spike produced large local MFE but no durable ROE/PBR/capital-return proof. Entry row 2024-01-31 close 10,400 was checked in stock-web 007/007330/2024.csv."}
{"row_type": "trigger", "trigger_id": "R6L13_C21_SHINHAN_T2A_20240226", "case_id": "R6L13_C21_SHINHAN_20240226_VALUEUP_CAPITAL_RETURN_SUCCESS", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Korea value-up policy signal plus bank low-PBR rerating setup; capital-return credibility was visible enough for Stage2 but not yet a pure Green revision event.", "evidence_source": "public policy/value-up event; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 41350, "MFE_30D_pct": 24.55, "MFE_90D_pct": 31.08, "MFE_180D_pct": 56.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.63, "MAE_90D_pct": -3.63, "MAE_180D_pct": -3.63, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -18.11, "green_lateness_ratio": 0.24, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_SHINHAN_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L13_C21_MERITZ_T2A_20240628", "case_id": "R6L13_C21_MERITZ_20240628_CAPITAL_RETURN_CADENCE_SUCCESS", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-06-28", "evidence_available_at_that_date": "Capital-return cadence and holding-company integration were already known; June entry tests whether C21 should reward confirmed capital-return machinery even before a later revision chase.", "evidence_source": "public capital-return/shareholder-return narrative; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv and 2025.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "financial_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-06-28", "entry_price": 79100, "MFE_30D_pct": 8.6, "MFE_90D_pct": 26.3, "MFE_180D_pct": 61.06, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.08, "MAE_90D_pct": -7.08, "MAE_180D_pct": -7.08, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-06", "peak_price": 127400, "drawdown_after_peak_pct": -15.93, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_structural_success_delayed", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_MERITZ_20240628", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L13_C21_IBK_T2_20240226", "case_id": "R6L13_C21_IBK_20240226_POLICY_BANK_UNDERPOWERED_RERATING", "symbol": "024110", "company_name": "기업은행", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-candidate", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Low-PBR and bank/value-up basket exposure existed, but minority shareholder return proof was weaker and policy-bank overhang stayed material.", "evidence_source": "public value-up/bank basket event; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["policy_bank_overhang"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/024/024110/2024.csv", "profile_path": "atlas/symbol_profiles/024/024110.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 13400, "MFE_30D_pct": 11.64, "MFE_90D_pct": 11.64, "MFE_180D_pct": 11.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.58, "MAE_90D_pct": -3.58, "MAE_180D_pct": -4.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-13", "peak_price": 14960, "drawdown_after_peak_pct": -14.51, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "shallow_local_peak_not_full_4B", "four_b_evidence_type": ["valuation_blowoff", "policy_bank_overhang"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_underpowered", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_IBK_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L13_C21_KAKAOPAY_T2_REJECT_20240226", "case_id": "R6L13_C21_KAKAOPAY_20240226_DIGITAL_FINANCE_FALSE_GREEN", "symbol": "377300", "company_name": "카카오페이", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2024-02-26", "evidence_available_at_that_date": "Digital-finance beta and fintech optionality were present, but no low-PBR ROE repair or capital-return channel existed.", "evidence_source": "public fintech/digital-finance narrative; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/377/377300/2024.csv", "profile_path": "atlas/symbol_profiles/377/377300.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-26", "entry_price": 46600, "MFE_30D_pct": 1.61, "MFE_90D_pct": 1.61, "MFE_180D_pct": 1.61, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.35, "MAE_90D_pct": -43.99, "MAE_180D_pct": -52.9, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-26", "peak_price": 47350, "drawdown_after_peak_pct": -53.64, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_but_rejection_correct", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_KAKAOPAY_20240226", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L13_C21_PUREUN_T2_REJECT_20240131", "case_id": "R6L13_C21_PUREUN_20240131_LOCAL_BANK_PRICE_ONLY_SPIKE", "symbol": "007330", "company_name": "푸른저축은행", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-candidate-rejected", "trigger_date": "2024-01-31", "evidence_available_at_that_date": "Local bank/small financial stock price spike existed, but no ROE/PBR repair, capital return, or durable earnings bridge was available.", "evidence_source": "price-only local-bank theme; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/007/007330/2024.csv", "profile_path": "atlas/symbol_profiles/007/007330.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-31", "entry_price": 10400, "MFE_30D_pct": 41.44, "MFE_90D_pct": 41.44, "MFE_180D_pct": 41.44, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.79, "MAE_90D_pct": -17.79, "MAE_180D_pct": -30.38, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 14710, "drawdown_after_peak_pct": -43.1, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_not_positive_stage", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "false_break_or_event_spike_fade", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_PUREUN_20240131", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R6L13_C21_SHINHAN_T4B_20240826", "case_id": "R6L13_C21_SHINHAN_20240226_VALUEUP_CAPITAL_RETURN_SUCCESS", "symbol": "055550", "company_name": "신한지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2024-08-26", "evidence_available_at_that_date": "Korea value-up policy signal plus bank low-PBR rerating setup; capital-return credibility was visible enough for Stage2 but not yet a pure Green revision event.", "evidence_source": "public policy/value-up event; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_return_repricing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/055/055550/2024.csv", "profile_path": "atlas/symbol_profiles/055/055550.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-08-26", "entry_price": 61400, "MFE_30D_pct": 5.21, "MFE_90D_pct": 5.21, "MFE_180D_pct": 5.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.84, "MAE_90D_pct": -13.84, "MAE_180D_pct": -13.84, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-26", "peak_price": 64600, "drawdown_after_peak_pct": -18.11, "green_lateness_ratio": 0.24, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_after_valueup_rerating", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_return_repricing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_SHINHAN_20240826_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "R6L13_C21_MERITZ_T4B_20250306", "case_id": "R6L13_C21_MERITZ_20240628_CAPITAL_RETURN_CADENCE_SUCCESS", "symbol": "138040", "company_name": "메리츠금융지주", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "fine_archetype_id": "BANK_VALUEUP_CAPITAL_RETURN_VS_DIGITAL_FINANCE_THEME", "sector": "financial_capital_return_digital", "primary_archetype": "ROE_PBR_capital_return_vs_digital_finance_theme", "loop_objective": "coverage_gap_fill|counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery|canonical_archetype_compression|4B_non_price_requirement_stress_test", "trigger_type": "Stage4B", "trigger_date": "2025-03-06", "evidence_available_at_that_date": "Capital-return cadence and holding-company integration were already known; June entry tests whether C21 should reward confirmed capital-return machinery even before a later revision chase.", "evidence_source": "public capital-return/shareholder-return narrative; stock-web rows checked in atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv and 2025.csv", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "capital_return_repricing"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/138/138040/2024.csv", "profile_path": "atlas/symbol_profiles/138/138040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2025-03-06", "entry_price": 127200, "MFE_30D_pct": 0.16, "MFE_90D_pct": 0.16, "MFE_180D_pct": 0.16, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.8, "MAE_90D_pct": -15.8, "MAE_180D_pct": -15.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-06", "peak_price": 127400, "drawdown_after_peak_pct": -15.93, "green_lateness_ratio": 0.36, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "good_full_window_4B_timing_after_delayed_capital_return_rerating", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "capital_return_repricing"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G_MERITZ_20250306_4B", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L13_C21_SHINHAN_20240226_VALUEUP_CAPITAL_RETURN_SUCCESS", "trigger_id": "R6L13_C21_SHINHAN_T2A_20240226", "symbol": "055550", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 9, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 18, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 12, "policy_bank_overhang_score": 0, "price_only_theme_score": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 11, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 15, "valuation_repricing_score": 15, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 23, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 16, "policy_bank_overhang_score": 0, "price_only_theme_score": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green_candidate", "changed_components": ["roe_pbr_capital_return_score", "minority_shareholder_return_score", "digital_finance_beta_score", "policy_bank_overhang_score", "price_only_theme_score"], "component_delta_explanation": "C21 capital-return credibility gate lifts Shinhan from Yellow to low Green without changing global thresholds.", "MFE_90D_pct": 31.08, "MAE_90D_pct": -3.63, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L13_C21_MERITZ_20240628_CAPITAL_RETURN_CADENCE_SUCCESS", "trigger_id": "R6L13_C21_MERITZ_T2A_20240628", "symbol": "138040", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 14, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 20, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 15, "policy_bank_overhang_score": 0, "price_only_theme_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 17, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 25, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 19, "policy_bank_overhang_score": 0, "price_only_theme_score": 0}, "weighted_score_after": 94, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "minority_shareholder_return_score", "digital_finance_beta_score", "policy_bank_overhang_score", "price_only_theme_score"], "component_delta_explanation": "Confirmed capital-return cadence deserves canonical C21 promotion even if the immediate 30D MFE is modest.", "MFE_90D_pct": 26.3, "MAE_90D_pct": -7.08, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L13_C21_IBK_20240226_POLICY_BANK_UNDERPOWERED_RERATING", "trigger_id": "R6L13_C21_IBK_T2_20240226", "symbol": "024110", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 14, "valuation_repricing_score": 12, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 12, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 6, "policy_bank_overhang_score": 8, "price_only_theme_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 13, "valuation_repricing_score": 10, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 8, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 4, "policy_bank_overhang_score": 18, "price_only_theme_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage2-watch_or_reject", "changed_components": ["roe_pbr_capital_return_score", "minority_shareholder_return_score", "digital_finance_beta_score", "policy_bank_overhang_score", "price_only_theme_score"], "component_delta_explanation": "Policy-bank overhang and weak minority-return proof should cap Stage2 promotion.", "MFE_90D_pct": 11.64, "MAE_90D_pct": -3.58, "score_return_alignment_label": "counterexample_or_reject_aligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L13_C21_KAKAOPAY_20240226_DIGITAL_FINANCE_FALSE_GREEN", "trigger_id": "R6L13_C21_KAKAOPAY_T2_REJECT_20240226", "symbol": "377300", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "digital_finance_beta_score": 20, "minority_shareholder_return_score": 0, "policy_bank_overhang_score": 0, "price_only_theme_score": 12}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 3, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "digital_finance_beta_score": 8, "minority_shareholder_return_score": 0, "policy_bank_overhang_score": 0, "price_only_theme_score": 18}, "weighted_score_after": 39, "stage_label_after": "Stage1/2_theme_watch_only", "changed_components": ["roe_pbr_capital_return_score", "minority_shareholder_return_score", "digital_finance_beta_score", "policy_bank_overhang_score", "price_only_theme_score"], "component_delta_explanation": "Digital-finance beta must not be treated as C21 capital-return evidence.", "MFE_90D_pct": 1.61, "MAE_90D_pct": -43.99, "score_return_alignment_label": "counterexample_or_reject_aligned", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L13_C21_PUREUN_20240131_LOCAL_BANK_PRICE_ONLY_SPIKE", "trigger_id": "R6L13_C21_PUREUN_T2_REJECT_20240131", "symbol": "007330", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 20, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 0, "policy_bank_overhang_score": 0, "price_only_theme_score": 25}, "weighted_score_before": 69, "stage_label_before": "Stage2-price_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 2, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "roe_pbr_capital_return_score": 0, "digital_finance_beta_score": 0, "minority_shareholder_return_score": 0, "policy_bank_overhang_score": 0, "price_only_theme_score": 30}, "weighted_score_after": 35, "stage_label_after": "Stage1/2_price_only_reject", "changed_components": ["roe_pbr_capital_return_score", "minority_shareholder_return_score", "digital_finance_beta_score", "policy_bank_overhang_score", "price_only_theme_score"], "component_delta_explanation": "Large MFE without non-price capital-return evidence should remain a rejected price-only spike.", "MFE_90D_pct": 41.44, "MAE_90D_pct": -17.79, "score_return_alignment_label": "counterexample_or_reject_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "residual_contribution", "round": "R6", "loop": "13", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "new_trigger_family_count": 5, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["digital_finance_beta_false_positive", "policy_bank_lowPBR_overpromotion", "capital_return_cadence_too_late", "price_only_local_bank_spike"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_round = R6
completed_loop = 13
next_round = R7
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

This research file used stock-web as the price atlas, not as a live-market scanner. The inspected manifest records `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, and `calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year`. The trigger rows use six-digit Korean tickers and raw/unadjusted OHLCV rows from the listed shard paths.

