# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 32
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
fine_archetype_id = BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN / DIGITAL_BANK_HIGH_PBR_NO_CAPITAL_RETURN_GUARD / REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
auto_trading_allowed = false
brokerage_api_allowed = false
```

This file is a historical calibration artifact only. It is not a live recommendation, watchlist, or trading instruction.

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

This loop does not re-prove the global Stage2/Green/4B/4C axes. It stress-tests them inside financial capital-return rerating and proposes C21-specific shadow rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
primary_archetype = ROE/PBR capital-return rerating
loop_objective = coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test
```

The selected question is narrow: **low-PBR financials do not all become C21 positives.** The distinction is whether the trigger has a non-price capital-return bridge: ROE/capital ratio discipline, explicit shareholder-return route, and valuation-repricing support. Generic bank beta, high-PBR digital-bank narratives, and regional-bank price squeezes are treated as guards or 4B overlays.

## 3. Previous Coverage / Duplicate Avoidance Check

A repository search over allowed research artifacts found no matching prior C21 rows for the exact symbol set used here: `KB금융 / 하나금융지주 / 카카오뱅크 / 제주은행` with `C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN`. Therefore all four calibration-usable cases are treated as new independent cases.

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest states that the atlas uses FinanceData/marcap as source, `raw_unadjusted_marcap` as adjustment status, `1995-05-02` to `2026-02-20` as date range, and `atlas/ohlcv_tradable_by_symbol_year` as calibration shard root. It also records that zero-volume / invalid rows are excluded from calibration shards and that corporate-action-contaminated windows should be blocked by default.

```json
{
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

## 5. Historical Eligibility Gate

All four representative rows satisfy the 180-trading-day historical gate.

| symbol | company | profile_path | corporate_action_window_status | forward 180D | calibration_usable | note |
|---:|---|---|---|---:|---|---|
| 105560 | KB금융 | atlas/symbol_profiles/105/105560.json | clean_180D_window | 180 | true | no corporate-action candidate in profile window |
| 086790 | 하나금융지주 | atlas/symbol_profiles/086/086790.json | clean_180D_window | 180 | true | no corporate-action candidate in profile window |
| 323410 | 카카오뱅크 | atlas/symbol_profiles/323/323410.json | clean_180D_window | 180 | true | no corporate-action candidate in profile window |
| 006220 | 제주은행 | atlas/symbol_profiles/006/006220.json | clean_180D_window | 180 | true | historical corporate-action candidates exist, but not in the 2024 entry~D+180 window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression note |
|---|---|---|
| BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Large bank holding-company route where capital-return plan/expectation and low-PBR repricing are aligned. |
| DIGITAL_BANK_HIGH_PBR_NO_CAPITAL_RETURN_GUARD | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Same sector label, but the C21 mechanism is absent; this is a guard path. |
| REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | Low-PBR financial narrative with price squeeze, but no durable capital-return bridge; this is a 4B/4C risk path. |

## 7. Case Selection Summary

| case_id | symbol | company | role | best_trigger | current_profile_verdict | note |
|---|---:|---|---|---|---|---|
| R6L32-C21-KBFG-2024-CAPRETURN | 105560 | KB금융 | positive / structural_success | R6L32-C21-KBFG-STAGE2-2024-01-26 | current_profile_correct | 대형 은행지주 + 명시적 주주환원/자사주·배당 기대 + 저PBR 가치업 베타가 결합된 positive case. |
| R6L32-C21-HANA-2024-CAPRETURN | 086790 | 하나금융지주 | positive / structural_success | R6L32-C21-HANA-STAGE2-2024-01-26 | current_profile_correct | 대형 은행지주 + 배당/자사주 기대 + 저PBR/ROE 재평가가 결합된 positive case. |
| R6L32-C21-KAKAOBANK-2024-HIGHVALUATION | 323410 | 카카오뱅크 | counterexample / failed_rerating | R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26 | current_profile_false_positive | 은행/금융 섹터 beta만으로 C21 positive로 승격하면 안 되는 counterexample. 고PBR·디지털뱅크 성격과 명시적 자본환원 부재가 가격경로를 설명했다. |
| R6L32-C21-JEJUBANK-2024-PRICEONLY | 006220 | 제주은행 | counterexample / price_moved_without_evidence | R6L32-C21-JEJU-PRICEONLY-2024-02-19 | current_profile_false_positive | 저PBR/은행 테마 가격만으로 Stage3를 주면 안 되는 counterexample. 후속 ROE·자본환원·대형지주 수준의 execution evidence가 없어서 급등 후 변동성/낙폭이 컸다. |


## 8. Positive vs Counterexample Balance

| role | count | cases |
|---|---:|---|
| positive_structural_success | 2 | KB금융, 하나금융지주 |
| counterexample_or_failed_rerating | 2 | 카카오뱅크, 제주은행 |
| 4B_or_4C_case | 1 primary + 2 thesis-break labels | 제주은행 4B overlay; 카카오뱅크/제주은행 hard 4C thesis-break labels |

The balance condition is satisfied. This MD can propose shadow-only C21 deltas because it has positive and counterexample cases and at least three calibration-usable cases.

## 9. Evidence Source Map

| evidence family | usage in this loop | source basis |
|---|---|---|
| Korea Corporate Value-up policy context | Sector-wide policy optionality for low-PBR/ROE/capital-return rerating | Public policy/news context: the programme was proposed in February 2024 to address low valuations and encourage shareholder returns. |
| Explicit capital-return / bank holding-company route | Positive differentiation for KB금융 and 하나금융지주 | Company earnings/capital-return disclosures and market-visible shareholder-return expectation; validated by stock-web price response. |
| High-PBR digital-bank guard | Counterexample path for 카카오뱅크 | No comparable low-PBR capital-return bridge; price path showed limited upside and large downside. |
| Regional-bank price-only blowoff | Counterexample and 4B overlay path for 제주은행 | Price/positioning heat without durable non-price C21 evidence. |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis |
|---:|---|---|---|---|
| 105560 | KB금융 | atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv | atlas/symbol_profiles/105/105560.json | tradable_raw |
| 086790 | 하나금융지주 | atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv | atlas/symbol_profiles/086/086790.json | tradable_raw |
| 323410 | 카카오뱅크 | atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv | atlas/symbol_profiles/323/323410.json | tradable_raw |
| 006220 | 제주은행 | atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv | atlas/symbol_profiles/006/006220.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | verdict | aggregate |
|---|---:|---|---|---:|---:|---:|---:|---:|---|---|
| R6L32-C21-KBFG-STAGE2-2024-01-26 | 105560 | Stage2-Actionable | 2024-01-26 | 53800 | 55.02 | -2.42 | 83.09 | -2.42 | current_profile_correct | representative |
| R6L32-C21-KBFG-GREEN-2024-03-14 | 105560 | Stage3-Green-comparison | 2024-03-14 | 78600 | 17.56 | -21.12 | 32.19 | -21.12 | current_profile_too_late | label_comparison_only |
| R6L32-C21-HANA-STAGE2-2024-01-26 | 086790 | Stage2-Actionable | 2024-01-26 | 44850 | 45.6 | -2.68 | 54.52 | -2.68 | current_profile_correct | representative |
| R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26 | 323410 | Stage2-Narrative-Blocked | 2024-01-26 | 29100 | 7.22 | -24.91 | 7.22 | -31.37 | current_profile_false_positive | representative |
| R6L32-C21-JEJU-PRICEONLY-2024-02-19 | 006220 | Stage2-PriceOnly-Blocked | 2024-02-19 | 15240 | 10.89 | -28.08 | 10.89 | -44.62 | current_profile_false_positive | representative |
| R6L32-C21-JEJU-4B-2024-02-19 | 006220 | 4B-overlay | 2024-02-19 | 15240 | 10.89 | -28.08 | 10.89 | -44.62 | current_profile_4B_too_early_if_treated_as_full_exit | 4B_overlay_only |


## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate rows only

| case_id | symbol | entry_date | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R6L32-C21-KBFG-2024-CAPRETURN | 105560 | 2024-01-26 | 53800 | 38.48 | -2.42 | 55.02 | -2.42 | 83.09 | -2.42 | 2024-10-25 | 103900 | -21.17 |
| R6L32-C21-HANA-2024-CAPRETURN | 086790 | 2024-01-26 | 44850 | 37.57 | -2.68 | 45.60 | -2.68 | 54.52 | -2.68 | 2024-08-27 | 69300 | -18.61 |
| R6L32-C21-KAKAOBANK-2024-HIGHVALUATION | 323410 | 2024-01-26 | 29100 | 7.22 | -8.93 | 7.22 | -24.91 | 7.22 | -31.37 | 2024-02-15 | 31200 | -35.99 |
| R6L32-C21-JEJUBANK-2024-PRICEONLY | 006220 | 2024-02-19 | 15240 | 3.15 | -28.94 | 10.89 | -28.08 | 10.89 | -44.62 | 2024-04-19 | 16900 | -50.06 |

Aggregate representative average:

```text
positive_avg_MFE_90D = 50.31
positive_avg_MAE_90D = -2.55
positive_avg_MFE_180D = 68.81
positive_avg_MAE_180D = -2.55
counterexample_avg_MFE_90D = 9.06
counterexample_avg_MAE_90D = -26.50
counterexample_avg_MFE_180D = 9.06
counterexample_avg_MAE_180D = -37.995
```

Interpretation: in C21, the return distribution split is not “financials went up.” It is “financials with explicit capital-return/ROE/PBR bridge were asymmetric; financials with only beta/price/narrative had low sustained MFE and high MAE.”

## 13. Current Calibrated Profile Stress Test

| case | current calibrated profile likely judgment | actual path | verdict |
|---|---|---|---|
| KB금융 | Stage2-Actionable allowed; Stage3 Green only after revision/confirmation | High MFE and low early MAE | current_profile_correct, but Green comparison row shows lateness |
| 하나금융지주 | Stage2-Actionable allowed; Green guarded by evidence | High MFE and low early MAE | current_profile_correct |
| 카카오뱅크 | If generic financial beta is over-weighted, could be Yellow/false positive | Low MFE and large MAE | current_profile_false_positive unless C21 guard exists |
| 제주은행 | If price-only low-PBR squeeze is over-weighted, could be false Stage2/3 | Blowoff, large MAE and drawdown | current_profile_false_positive; should be 4B-risk-only / blocked positive |

Answers to required stress-test questions:

1. Current profile is broadly correct on explicit capital-return bank holding-company positives.
2. It can still be too permissive if generic bank beta is allowed to stand in for C21 evidence.
3. Stage2 bonus is not too high for KB/Hana, but it is too high for KakaoBank/Jeju unless the new guard blocks the evidence family.
4. Yellow threshold 75 is acceptable if C21 component quality is respected; otherwise false Yellow appears in KakaoBank/Jeju.
5. Green threshold 87 and revision 55 are appropriate, but KB comparison shows Green can become late after price has already absorbed much of the upside.
6. Price-only blowoff guard is strengthened by 제주은행.
7. Full 4B non-price requirement is kept: Jeju’s price-only heat is a risk overlay, not a positive full-stage evidence package.
8. Hard 4C routing is strengthened where no capital-return bridge appears and MAE expands.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Stage3/Green comparison entry | full peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| KB금융 | 53800 | 78600 | 103900 | 0.495 | Green captured only about half the Stage2-to-peak move; Stage2 evidence was valuable. |
| 하나금융지주 | 44850 | not separately modeled | 69300 | not_applicable | Stage2 was enough for representative calibration. |
| 카카오뱅크 | blocked | no valid Green | 31200 | not_applicable | No confirmed C21 Green trigger. |
| 제주은행 | blocked | no valid Green | 16900 | not_applicable | Price-only strength must not become Green. |

## 15. 4B Local vs Full-window Timing Audit

| trigger | Stage2/reference price | 4B entry | local peak | full observed peak | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| 제주은행 2024-02-19 | 9000 | 15240 | 16050 | 16900 | 0.885 | 0.790 | Good risk-overlay proximity, but price-only evidence means not full 4B and not positive Stage3. |
| KB금융 | 53800 | not modeled | 103900 | 103900 | null | null | No separate non-price 4B row in this loop. |
| 하나금융지주 | 44850 | not modeled | 69300 | 69300 | null | null | No separate non-price 4B row in this loop. |
| 카카오뱅크 | 29100 | blocked | 31200 | 31200 | null | null | The correct action is positive-stage block, not 4B timing. |

## 16. 4C Protection Audit

| case | 4C label | protection rationale |
|---|---|---|
| 카카오뱅크 | hard_4c_success | No durable C21 capital-return bridge; blocking/4C watch avoids -31.37% 180D MAE from the false positive row. |
| 제주은행 | hard_4c_success | Price-only blowoff with no durable C21 evidence; 4C/blocked label avoids -44.62% 180D MAE. |
| KB금융 | thesis_break_watch_only | No hard 4C event in loop. |
| 하나금융지주 | thesis_break_watch_only | No hard 4C event in loop. |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c21_price_only_regional_bank_4b_overlay
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
proposal = if regional-bank / small-financial price-only blowoff lacks explicit shareholder-return/ROE/PBR bridge, block Stage2/Stage3 promotion and label as 4B-risk-only or narrative-only.
```

Reason: 제주은행 showed high volatility and large drawdown after price-only value-up speculation. Its 180D MFE was only 10.89% from the blowoff entry, while 180D MAE was -44.62%.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
axis_1 = c21_explicit_capital_return_quality_bonus
axis_2 = c21_generic_financial_beta_guard
canonical_archetype_id = C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
```

C21 should promote only when the mechanism is explicit: capital return, low-PBR/ROE repricing, and credible financial holding-company execution. It should block high-PBR digital banks and price-only low-PBR squeezes from becoming Stage3 positives.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 4 | KB/Hana/Kakao/Jeju if generic beta not guarded | 29.69 | -14.53 | 38.93 | -21.78 | 0.50 | 0 | 1 | 0.495 | mixed; positives right, counterexamples need C21 guard |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | likely later/less guarded entries | 25.00 | -16.00 | 32.00 | -24.00 | 0.50 | 1 | 1 | 0.60 | weaker than current calibrated proxy |
| P1 sector_specific_candidate_profile | L6 sector | 4 | KB/Hana promoted; Kakao/Jeju blocked | 50.31 | -2.55 | 68.81 | -2.55 | 0.00 | 0 | 1 | 0.495 | improved; removes price-only regional-bank false positives |
| P2 canonical_archetype_candidate_profile | C21 | 4 | explicit capital-return rows only | 50.31 | -2.55 | 68.81 | -2.55 | 0.00 | 0 | 1 | 0.495 | best explanatory alignment |
| P3 counterexample_guard_profile | C21 guard | 4 | KB/Hana selected; Kakao/Jeju narrative-only/4B risk | 50.31 | -2.55 | 68.81 | -2.55 | 0.00 | 0 | 0 for selected positives | null | best risk-adjusted profile |

## 20. Score-Return Alignment Matrix

| trigger_id | score before | label before | score after | label after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R6L32-C21-KBFG-STAGE2-2024-01-26 | 74 | Stage2-Actionable | 78 | Stage2-Actionable+ | 55.02 | -2.42 | aligned |
| R6L32-C21-HANA-STAGE2-2024-01-26 | 73 | Stage2-Actionable | 77 | Stage2-Actionable+ | 45.60 | -2.68 | aligned |
| R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26 | 65 | Yellow-risk | 51 | Blocked/Narrative-only | 7.22 | -24.91 | guard improves alignment |
| R6L32-C21-JEJU-PRICEONLY-2024-02-19 | 67 | Yellow-risk | 45 | Blocked/4B-risk-only | 10.89 | -28.08 | guard improves alignment |
| R6L32-C21-KBFG-GREEN-2024-03-14 | 88 | Stage3-Green | 88 | Stage3-Green-late | 17.56 | -21.12 | confirms Green lateness, not new global rule |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN | BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN / DIGITAL_BANK_HIGH_PBR_NO_CAPITAL_RETURN_GUARD / REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF | 2 | 2 | 1 | 2 | 4 | 0 | 6 | 4 | 3 | true | true | C21 now has positive/counterexample split; next gap is insurance C22 or C21 holdout on Woori/BNK/JB/Meritz. |


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
current_profile_error_count: 3
calibration_usable_case_count: 4
calibration_usable_trigger_count: 6
representative_trigger_count: 4
diversity_score_summary: high; undercovered L6/C21, four new symbols, four new trigger families, positive/counterexample split, and three current-profile residual errors.
auto_selected_coverage_gap: L6/C21 had less residual coverage than R1/R2 and needed C21-specific positive/counterexample split.
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_financial_beta_false_positive; high_pbr_digital_bank_misclassified_as_valueup; regional_bank_price_only_blowoff; green_lateness_after_stage2_for_KB
new_axis_proposed: c21_explicit_capital_return_quality_bonus; c21_generic_financial_beta_guard; c21_price_only_regional_bank_4b_overlay
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profile availability and corporate-action window status
- 2024 tradable OHLC rows for representative trigger windows
- 30D / 90D / 180D MFE and MAE for representative triggers
- positive/counterexample split within C21
- Green lateness comparison for KB금융
- price-only 4B overlay risk for 제주은행
```

Not validated:

```text
- live 2026 candidate scan
- production scoring code
- stock_agent src/e2r implementation
- brokerage API behavior
- modified-adjusted price series
- exact intraday disclosure timestamps
- full 2Y quantitative calibration fields; 2Y fields are present but not used for this loop's weight proposal
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_capital_return_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"Reward explicit buyback/cancellation/dividend-policy route only when ROE/PBR bridge is supported","Positive KB/Hana rows had avg MFE_180D 68.81% with avg MAE_180D -2.55%","R6L32-C21-KBFG-STAGE2-2024-01-26|R6L32-C21-HANA-STAGE2-2024-01-26",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_generic_financial_beta_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-3,-3,"Block Stage3 promotion when financial-sector beta lacks explicit capital-return/ROE/PBR bridge","KakaoBank and Jeju price/narrative rows had low sustained MFE and large MAE/drawdown","R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26|R6L32-C21-JEJU-PRICEONLY-2024-02-19",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_price_only_regional_bank_4b_overlay,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"Treat regional-bank low-PBR blowoff as risk overlay, not positive Stage2/Stage3","Jeju row showed MFE_180D 10.89% but MAE_180D -44.62% and drawdown after peak -50.06%","R6L32-C21-JEJU-4B-2024-02-19",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### JSONL

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R6L32-C21-KBFG-2024-CAPRETURN","symbol":"105560","company_name":"KB금융","case_type":"structural_success","positive_or_counterexample":"positive","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","best_trigger":"R6L32-C21-KBFG-STAGE2-2024-01-26","notes":"대형 은행지주 + 명시적 주주환원/자사주·배당 기대 + 저PBR 가치업 베타가 결합된 positive case.","current_profile_verdict":"current_profile_correct","score_price_alignment":"positive_score_aligned_with_high_MFE_low_initial_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"case","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R6L32-C21-HANA-2024-CAPRETURN","symbol":"086790","company_name":"하나금융지주","case_type":"structural_success","positive_or_counterexample":"positive","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","best_trigger":"R6L32-C21-HANA-STAGE2-2024-01-26","notes":"대형 은행지주 + 배당/자사주 기대 + 저PBR/ROE 재평가가 결합된 positive case.","current_profile_verdict":"current_profile_correct","score_price_alignment":"positive_score_aligned_with_high_MFE_low_initial_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"case","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R6L32-C21-KAKAOBANK-2024-HIGHVALUATION","symbol":"323410","company_name":"카카오뱅크","case_type":"failed_rerating","positive_or_counterexample":"counterexample","fine_archetype_id":"DIGITAL_BANK_HIGH_PBR_NO_CAPITAL_RETURN_GUARD","best_trigger":"R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26","notes":"은행/금융 섹터 beta만으로 C21 positive로 승격하면 안 되는 counterexample. 고PBR·디지털뱅크 성격과 명시적 자본환원 부재가 가격경로를 설명했다.","current_profile_verdict":"current_profile_false_positive","score_price_alignment":"generic_financial_beta_misaligned_without_capital_return_quality","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"case","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","case_id":"R6L32-C21-JEJUBANK-2024-PRICEONLY","symbol":"006220","company_name":"제주은행","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","fine_archetype_id":"REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF","best_trigger":"R6L32-C21-JEJU-PRICEONLY-2024-02-19","notes":"저PBR/은행 테마 가격만으로 Stage3를 주면 안 되는 counterexample. 후속 ROE·자본환원·대형지주 수준의 execution evidence가 없어서 급등 후 변동성/낙폭이 컸다.","current_profile_verdict":"current_profile_false_positive","score_price_alignment":"price_only_blowoff_misaligned_with_sustained_rerating","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"price_source":"Songdaiki/stock-web"}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-KBFG-STAGE2-2024-01-26","case_id":"R6L32-C21-KBFG-2024-CAPRETURN","symbol":"105560","company_name":"KB금융","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":53800,"evidence_available_at_that_date":"FY2023 earnings / shareholder-return expectation plus Korea Value-up bank rerating setup; entry uses same-day close because price reaction was tradable intraday/close. Evidence is non-price: bank holding-company capital-return route + low-PBR policy optionality.","evidence_source":"Company earnings/capital-return disclosures and Korea Corporate Value-up policy context; stock-web OHLC shard 105/105560/2024.csv.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","early_revision_signal","relative_strength"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":38.48,"MFE_90D_pct":55.02,"MFE_180D_pct":83.09,"MFE_1Y_pct":93.12,"MFE_2Y_pct":null,"MAE_30D_pct":-2.42,"MAE_90D_pct":-2.42,"MAE_180D_pct":-2.42,"MAE_1Y_pct":-2.42,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-21.17,"green_lateness_ratio":"not_applicable; Stage2 representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","same_entry_group_id":"KBFG-2024-01-26-53800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","calibration_usable":true}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-KBFG-GREEN-2024-03-14","case_id":"R6L32-C21-KBFG-2024-CAPRETURN","symbol":"105560","company_name":"KB금융","trigger_type":"Stage3-Green-comparison","trigger_date":"2024-03-14","entry_date":"2024-03-14","entry_price":78600,"evidence_available_at_that_date":"Price/revision confirmation and sector leadership had become clearer by mid-March. This row exists only to audit Green lateness after Stage2.","evidence_source":"stock-web OHLC shard 105/105560/2024.csv plus public value-up policy context.","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":0.0,"MFE_90D_pct":17.56,"MFE_180D_pct":32.19,"MFE_1Y_pct":32.19,"MFE_2Y_pct":null,"MAE_30D_pct":-21.12,"MAE_90D_pct":-21.12,"MAE_180D_pct":-21.12,"MAE_1Y_pct":-21.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-25","peak_price":103900,"drawdown_after_peak_pct":-21.17,"green_lateness_ratio":0.495,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"late_green_higher_MAE_than_stage2","current_profile_verdict":"current_profile_too_late","same_entry_group_id":"KBFG-2024-03-14-78600","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv","profile_path":"atlas/symbol_profiles/105/105560.json","calibration_usable":true}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-HANA-STAGE2-2024-01-26","case_id":"R6L32-C21-HANA-2024-CAPRETURN","symbol":"086790","company_name":"하나금융지주","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":44850,"evidence_available_at_that_date":"FY2023 earnings / shareholder-return expectation plus low-PBR value-up bank rerating setup. Evidence is non-price: bank holding-company capital-return route + policy optionality.","evidence_source":"Company earnings/capital-return disclosures and Korea Corporate Value-up policy context; stock-web OHLC shard 086/086790/2024.csv.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":37.57,"MFE_90D_pct":45.6,"MFE_180D_pct":54.52,"MFE_1Y_pct":54.52,"MFE_2Y_pct":null,"MAE_30D_pct":-2.68,"MAE_90D_pct":-2.68,"MAE_180D_pct":-2.68,"MAE_1Y_pct":-2.68,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-08-27","peak_price":69300,"drawdown_after_peak_pct":-18.61,"green_lateness_ratio":"not_applicable; Stage2 representative","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_MFE_low_MAE","current_profile_verdict":"current_profile_correct","same_entry_group_id":"HANA-2024-01-26-44850","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"BANK_VALUEUP_EXPLICIT_CAPITAL_RETURN","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/086/086790/2024.csv","profile_path":"atlas/symbol_profiles/086/086790.json","calibration_usable":true}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26","case_id":"R6L32-C21-KAKAOBANK-2024-HIGHVALUATION","symbol":"323410","company_name":"카카오뱅크","trigger_type":"Stage2-Narrative-Blocked","trigger_date":"2024-01-26","entry_date":"2024-01-26","entry_price":29100,"evidence_available_at_that_date":"Financial-sector/value-up beta existed, but the C21-specific capital-return evidence was weak: high-PBR digital bank profile, no low-PBR capital-return rerating bridge comparable to large bank holding companies.","evidence_source":"Korea Corporate Value-up policy context; stock-web OHLC shard 323/323410/2024.csv.","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":7.22,"MFE_90D_pct":7.22,"MFE_180D_pct":7.22,"MFE_1Y_pct":7.22,"MFE_2Y_pct":null,"MAE_30D_pct":-8.93,"MAE_90D_pct":-24.91,"MAE_180D_pct":-31.37,"MAE_1Y_pct":-31.37,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-15","peak_price":31200,"drawdown_after_peak_pct":-35.99,"green_lateness_ratio":"not_applicable; no confirmed Stage3-Green trigger","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"blocked_positive_stage_due_to_no_capital_return_bridge","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"failed_rerating_high_MAE_low_MFE","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"KAKAOBANK-2024-01-26-29100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"DIGITAL_BANK_HIGH_PBR_NO_CAPITAL_RETURN_GUARD","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/323/323410/2024.csv","profile_path":"atlas/symbol_profiles/323/323410.json","calibration_usable":true}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-JEJU-PRICEONLY-2024-02-19","case_id":"R6L32-C21-JEJUBANK-2024-PRICEONLY","symbol":"006220","company_name":"제주은행","trigger_type":"Stage2-PriceOnly-Blocked","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":15240,"evidence_available_at_that_date":"Regional-bank/low-PBR price spike existed, but no robust C21 evidence package: no durable ROE/capital-return bridge, no repeated public capital-return plan, no large-bank holding-company capital discipline.","evidence_source":"Korea Corporate Value-up policy context; stock-web OHLC shard 006/006220/2024.csv.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":3.15,"MFE_90D_pct":10.89,"MFE_180D_pct":10.89,"MFE_1Y_pct":10.89,"MFE_2Y_pct":null,"MAE_30D_pct":-28.94,"MAE_90D_pct":-28.08,"MAE_180D_pct":-44.62,"MAE_1Y_pct":-44.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-50.06,"green_lateness_ratio":"not_applicable; no confirmed Stage3-Green trigger","four_b_local_peak_proximity":0.885,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"price_only_not_full_4B_without_non_price_evidence","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"price_only_blowoff_counterexample","current_profile_verdict":"current_profile_false_positive","same_entry_group_id":"JEJU-2024-02-19-15240","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","calibration_usable":true}
{"row_type":"trigger","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","sector":"Financials","primary_archetype":"ROE/PBR capital-return rerating","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","green_strictness_stress_test","4B_non_price_requirement_stress_test","4C_thesis_break_timing_test"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","trigger_id":"R6L32-C21-JEJU-4B-2024-02-19","case_id":"R6L32-C21-JEJUBANK-2024-PRICEONLY","symbol":"006220","company_name":"제주은행","trigger_type":"4B-overlay","trigger_date":"2024-02-19","entry_date":"2024-02-19","entry_price":15240,"evidence_available_at_that_date":"Same entry as price-only blocked row. It calibrates the 4B overlay: price/positioning heat can warn, but should not become a positive Stage3 signal without non-price evidence.","evidence_source":"stock-web OHLC shard 006/006220/2024.csv.","stage2_evidence_fields":["relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"MFE_30D_pct":3.15,"MFE_90D_pct":10.89,"MFE_180D_pct":10.89,"MFE_1Y_pct":10.89,"MFE_2Y_pct":null,"MAE_30D_pct":-28.94,"MAE_90D_pct":-28.08,"MAE_180D_pct":-44.62,"MAE_1Y_pct":-44.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-19","peak_price":16900,"drawdown_after_peak_pct":-50.06,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.885,"four_b_full_window_peak_proximity":0.79,"four_b_timing_verdict":"risk_overlay_only_not_full_positive_stage","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success_for_risk_not_entry","current_profile_verdict":"current_profile_4B_too_early_if_treated_as_full_exit","same_entry_group_id":"JEJU-2024-02-19-15240","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_entry_group_4B_overlay_calibration","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","fine_archetype_id":"REGIONAL_BANK_PRICE_ONLY_VALUEUP_BLOWOFF","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006220/2024.csv","profile_path":"atlas/symbol_profiles/006/006220.json","calibration_usable":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-KBFG-2024-CAPRETURN","trigger_id":"R6L32-C21-KBFG-STAGE2-2024-01-26","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":11,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":13,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":13,"relative_strength_score":13,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":14,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":78,"stage_label_after":"Stage2-Actionable+","changed_components":["revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":55.02,"MAE_90D_pct":-2.42,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-KBFG-2024-CAPRETURN","trigger_id":"R6L32-C21-KBFG-GREEN-2024-03-14","symbol":"105560","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":88,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":14,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":15,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88,"stage_label_after":"Stage3-Green-late","changed_components":["revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":17.56,"MAE_90D_pct":-21.12,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-HANA-2024-CAPRETURN","trigger_id":"R6L32-C21-HANA-STAGE2-2024-01-26","symbol":"086790","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":10,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":12,"valuation_repricing_score":13,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":12,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":13,"valuation_repricing_score":14,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable+","changed_components":["revision_score","relative_strength_score","policy_or_regulatory_score","valuation_repricing_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":45.6,"MAE_90D_pct":-2.68,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-KAKAOBANK-2024-HIGHVALUATION","trigger_id":"R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26","symbol":"323410","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":8,"valuation_repricing_score":4,"execution_risk_score":-6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":5,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":-6,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":51,"stage_label_after":"Blocked/Narrative-only","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":7.22,"MAE_90D_pct":-24.91,"score_return_alignment_label":"misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-JEJUBANK-2024-PRICEONLY","trigger_id":"R6L32-C21-JEJU-PRICEONLY-2024-02-19","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":67,"stage_label_before":"Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":-8,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":45,"stage_label_after":"Blocked/4B-risk-only","changed_components":["relative_strength_score","policy_or_regulatory_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":10.89,"MAE_90D_pct":-28.08,"score_return_alignment_label":"misaligned_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L32-C21-JEJUBANK-2024-PRICEONLY","trigger_id":"R6L32-C21-JEJU-4B-2024-02-19","symbol":"006220","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":15,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":0,"stage_label_before":"4B-overlay","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":0,"stage_label_after":"4B-overlay-risk-only","changed_components":["relative_strength_score","execution_risk_score"],"component_delta_explanation":"C21-specific shadow profile rewards explicit capital-return/ROE/PBR bridge and penalizes generic bank beta, high-PBR digital-bank narrative, and price-only regional-bank blowoff.","MFE_90D_pct":10.89,"MAE_90D_pct":-28.08,"score_return_alignment_label":"misaligned_before_guard","current_profile_verdict":"current_profile_4B_too_early_if_treated_as_full_exit"}
{"row_type":"residual_contribution","round":"R6","loop":"32","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_financial_beta_false_positive","high_pbr_digital_bank_misclassified_as_valueup","regional_bank_price_only_blowoff","green_lateness_after_stage2_for_KB"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L6/C21 had less post-calibrated residual coverage than R1/R2 and needed positive/counterexample split for low-PBR financial capital-return rerating."}
```

### CSV shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c21_explicit_capital_return_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"Reward explicit buyback/cancellation/dividend-policy route only when ROE/PBR bridge is supported","Positive KB/Hana rows had avg MFE_180D 68.81% with avg MAE_180D -2.55%","R6L32-C21-KBFG-STAGE2-2024-01-26|R6L32-C21-HANA-STAGE2-2024-01-26",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_generic_financial_beta_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,-3,-3,"Block Stage3 promotion when financial-sector beta lacks explicit capital-return/ROE/PBR bridge","KakaoBank and Jeju price/narrative rows had low sustained MFE and large MAE/drawdown","R6L32-C21-KAKAOBANK-BLOCKED-2024-01-26|R6L32-C21-JEJU-PRICEONLY-2024-02-19",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c21_price_only_regional_bank_4b_overlay,sector_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN,0,+1,+1,"Treat regional-bank low-PBR blowoff as risk overlay, not positive Stage2/Stage3","Jeju row showed MFE_180D 10.89% but MAE_180D -44.62% and drawdown after peak -50.06%","R6L32-C21-JEJU-4B-2024-02-19",4,4,2,medium,sector_shadow_only,"not production; post-calibrated residual"
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
next_round = R6 / C22_INSURANCE_RATE_CYCLE_RESERVE or R6 / C21 holdout validation
recommended_holdout_symbols = Woori Financial, BNK Financial, JB Financial, Meritz Financial, Samsung Fire & Marine, DB Insurance
next_objective = separate durable capital-return rerating from insurance/accounting-cycle false positives and bank beta without explicit capital-return execution
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`, generated at 2026-05-21, max_date 2026-02-20, price adjustment status `raw_unadjusted_marcap`.
- Stock-Web symbol profiles used: `105560`, `086790`, `323410`, `006220`.
- Stock-Web OHLC shards used: `atlas/ohlcv_tradable_by_symbol_year/105/105560/2024.csv`, `086/086790/2024.csv`, `323/323410/2024.csv`, `006/006220/2024.csv`.
- Policy context: Korea Corporate Value-up Programme, announced/proposed in February 2024 and followed by guidelines/incentives through 2024; used only as historical evidence context, not as current candidate discovery.
