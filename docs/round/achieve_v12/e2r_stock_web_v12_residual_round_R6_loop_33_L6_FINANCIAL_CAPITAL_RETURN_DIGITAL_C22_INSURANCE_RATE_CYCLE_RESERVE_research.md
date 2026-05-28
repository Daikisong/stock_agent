# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R6
loop = 33
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = IFRS17_CSM_RESERVE_CAPITAL_RETURN_INSURANCE_VALUEUP
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R6_loop_33_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not live candidate discovery, not a watchlist, not a recommendation, and not a `stock_agent` patch. It uses the Songdaiki/stock-web price atlas as the historical OHLC source and records only shadow-profile candidates for later batch ingestion.

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

The loop does not re-prove the already-applied global ideas. It stress-tests whether Korean insurance stocks under the Corporate Value-up / IFRS17 regime need a narrower C22 gate: explicit capital-return quality and CSM/reserve durability should count differently from generic low-PBR financial beta.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R6 |
| loop | 33 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE |
| fine_archetype_id | IFRS17_CSM_RESERVE_CAPITAL_RETURN_INSURANCE_VALUEUP |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4B_non_price_requirement_stress_test |
| preferred_rule_scope | canonical_archetype_specific with L6 sector constraint |

## 3. Previous Coverage / Duplicate Avoidance Check

A GitHub search over the allowed `stock_agent` research artifact surface for `C22_INSURANCE_RATE_CYCLE_RESERVE`, `Samsung Fire`, `DB Insurance`, `Hyundai Marine`, `Hanwha Life`, and `Samsung Life` returned no direct prior C22 artifact matches in this session. Therefore this loop treats C22 as an undercovered L6 area rather than a re-materialization of C21 bank/financial-holding work.

```text
auto_selected_coverage_gap = L6/C22 insurance rate-cycle + IFRS17 reserve/capital-return coverage gap
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 1
new_trigger_family_count = 4
```

Diversity logic:

```text
undercovered_sector_bonus = +3
new_canonical_archetype_bonus = +4
same_archetype_new_symbol_bonus = +4 * 4
same_archetype_new_trigger_family_bonus = +4 * 4
counterexample_gap_bonus = +4
residual_error_bonus = +5
repeated_same_symbol_penalty = 0
schema_rematerialization_penalty = 0
```

Result: high diversity. C22 is not a repeat of the previous C21 bank/capital-return loop because the selected evidence families are underwriting/CSM/reserve/insurance capital-return gates, not bank ROE/PBR buyback gates.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-web manifest fields used:

| field | value |
|---|---|
| source | Songdaiki/stock-web |
| upstream_source | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_basis | tradable_raw |
| price_adjustment_status | raw_unadjusted_marcap |
| manifest_path | atlas/manifest.json |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |
| manifest_min_date | 1995-05-02 |
| manifest_max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |

Validation status:

```text
validation_status = usable_for_historical_calibration
price_adjustment_status = raw_unadjusted_marcap
calibration_warning = raw/unadjusted OHLC; corporate-action candidate windows blocked by default
```

## 5. Historical Eligibility Gate

The representative entry triggers are all in 2024 and all have at least 180 trading days available before the stock-web manifest max date of 2026-02-20. The quantitative calibration window used for weight evidence is 30D / 90D / 180D. 1Y is recorded where the retrieved rows made the observed peak/min clear; 2Y is not used for this loop's weight calibration because the residual rule concerns 180D entry-quality and 4B/Green timing.

| symbol | company_name | profile_path | first_date | last_date | row_status_summary | corporate_action_window_status |
|---|---:|---|---:|---:|---|---|
| 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | 1995-05-02 | 2026-02-20 | tradable_ohlcv=7763; zero-volume=2 | clean_2024_180D_window; old CA candidates only in 1999-2000 |
| 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | 1995-05-02 | 2026-02-20 | tradable_ohlcv=7762; zero-volume=3 | clean_2024_180D_window; old CA candidate only in 1999 |
| 001450 | 현대해상 | atlas/symbol_profiles/001/001450.json | 1995-05-02 | 2026-02-20 | tradable_ohlcv=7761; zero-volume=4 | clean_2024_180D_window; old CA candidate only in 2004 |
| 088350 | 한화생명 | atlas/symbol_profiles/088/088350.json | 2010-03-17 | 2026-02-20 | tradable_ohlcv=3922; zero-volume=0 | clean_2024_180D_window; no CA candidates |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| NONLIFE_IFRS17_CSM_CAPITAL_RETURN_VALUEUP | C22_INSURANCE_RATE_CYCLE_RESERVE | Non-life insurers rerating on CSM, underwriting margin, reserve comfort, and shareholder return visibility. |
| LIFE_INSURANCE_LOW_PBR_VALUEUP_BETA | C22_INSURANCE_RATE_CYCLE_RESERVE | Life insurers whose price is rate/PBR-sensitive but whose capital-return or reserve visibility may lag. |
| INSURANCE_PRICE_ONLY_VALUEUP_BLOWOFF | C22_INSURANCE_RATE_CYCLE_RESERVE | Price-only policy beta should be an overlay/watch signal, not Stage3 evidence. |
| GREEN_LATE_AFTER_VALUEUP_GAP | C22_INSURANCE_RATE_CYCLE_RESERVE | Earnings confirmation that arrives after a large policy-beta gap can be too late if not backed by clean reserve/capital-return durability. |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | positive_or_counterexample | best_trigger | calibration_usable | is_new_independent_case |
|---|---:|---|---|---|---|---:|---:|
| R6L33-C22-000810 | 000810 | 삼성화재 | structural_success + late Green comparison | positive | 2024-01-24 Stage2-Actionable | true | true |
| R6L33-C22-005830 | 005830 | DB손해보험 | structural_success + late Green comparison | positive | 2024-01-24 Stage2-Actionable | true | true |
| R6L33-C22-001450 | 001450 | 현대해상 | failed_rerating / false-positive Green guard | counterexample | 2024-01-24 Stage2-Actionable; 2024-05-14 late Green stress | true | true |
| R6L33-C22-088350 | 088350 | 한화생명 | price_moved_without_evidence / price-only 4B overlay | counterexample | 2024-01-24 Stage2-Actionable | true | true |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
```

The positive cases are not merely “insurance stocks went up.” They have stronger C22 quality: non-life underwriting leverage plus capital-return/Value-up interpretation created a path where early Stage2 entry had large 90D/180D MFE and shallow early MAE. The counterexamples show the other half of the canal: generic Value-up beta and life/non-life reserve uncertainty can move price first, but without durable CSM/reserve/capital-return evidence the move round-trips or offers poor Green entry quality.

## 9. Evidence Source Map

| evidence_family | evidence_date | source_status | usage |
|---|---:|---|---|
| Korea Corporate Value-up policy / low-PBR shareholder return policy optionality | 2024-01-24 to 2024-03-14 policy window | Reuters reported that Korea announced a Corporate Value-up Programme in February 2024 to boost shareholder returns and stock prices, with follow-up measures and tax incentives under consideration. | Stage2 policy_or_regulatory_optionality, not Stage3 evidence by itself |
| Samsung Fire 1Q 2024 reported revenue growth | 2024-05-13 / next tradable 2024-05-14 to 2024-05-16 | WSJ headline reported Samsung Fire 1Q consolidated revenue KRW5.507T vs KRW5.342T. | Stage3 confirmation support only when combined with non-life quality and prior C22 setup |
| Non-life insurer 2024 earnings / reserve interpretation | 2024-05 reporting season | Public quarterly result family; exact company IR PDFs not ingested in this run, so component score is capped rather than treated as full production evidence. | Stress-test Green lateness and reserve-quality gate |
| Price-only insurance Value-up beta | 2024-01 to 2024-02 | Stock-web OHLC confirms sharp price runs without using price as Stage2/3 evidence. | 4B overlay / counterexample, not positive-stage promotion |

## 10. Price Data Source Map

| symbol | year | price_shard_path | profile_path |
|---:|---:|---|---|
| 000810 | 2024 | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv | atlas/symbol_profiles/000/000810.json |
| 005830 | 2024 | atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv | atlas/symbol_profiles/005/005830.json |
| 001450 | 2024 | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv | atlas/symbol_profiles/001/001450.json |
| 088350 | 2024 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | evidence split |
|---|---|---:|---|---:|---:|---:|---|
| R6L33-C22-000810-S2 | R6L33-C22-000810 | 000810 | Stage2-Actionable | 2024-01-24 | 2024-01-24 | 237000 | Stage2: policy option + relative strength setup. Stage3: none at trigger. |
| R6L33-C22-000810-G | R6L33-C22-000810 | 000810 | Stage3-Green comparison | 2024-05-16 | 2024-05-16 | 370000 | Stage3: 1Q confirmation family + non-life quality, but late after Value-up repricing. |
| R6L33-C22-005830-S2 | R6L33-C22-005830 | 005830 | Stage2-Actionable | 2024-01-24 | 2024-01-24 | 79700 | Stage2: non-life low-PBR + policy option + early RS. |
| R6L33-C22-005830-G | R6L33-C22-005830 | 005830 | Stage3-Green comparison | 2024-05-16 | 2024-05-16 | 111500 | Stage3: 1Q confirmation family; late relative to policy-beta entry. |
| R6L33-C22-001450-S2 | R6L33-C22-001450 | 001450 | Stage2-Actionable | 2024-01-24 | 2024-01-24 | 30150 | Stage2: policy option only; weak quality confirmation at trigger. |
| R6L33-C22-001450-G | R6L33-C22-001450 | 001450 | Stage3-Green stress | 2024-05-14 | 2024-05-14 | 34200 | Stage3 stress: result-day jump, but poor forward entry quality and reserve/loss-ratio uncertainty. |
| R6L33-C22-088350-S2 | R6L33-C22-088350 | 088350 | Stage2-Actionable / price-beta watch | 2024-01-24 | 2024-01-24 | 2685 | Stage2: policy beta, not enough non-price quality. |
| R6L33-C22-088350-4B | R6L33-C22-088350 | 088350 | 4B overlay | 2024-02-13 | 2024-02-13 | 3550 | 4B: price-only local peak / positioning overheat, no full non-price 4B. |

## 12. Trigger-Level OHLC Backtest Tables

The 30D / 90D / 180D values are computed from stock-web tradable rows, using entry close as the denominator and high/low extremes within each trading-day window. Long-window 1Y/2Y is included only where useful for timing context and is not used for the proposed C22 shadow delta.

| trigger_id | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct | outcome |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R6L33-C22-000810-S2 | 237000 | 43.46 | -2.11 | 60.34 | -2.11 | 66.03 | -2.11 | 2024-06-28 | 393500 | -17.53 | structural_success |
| R6L33-C22-000810-G | 370000 | 6.35 | -12.43 | 6.35 | -12.43 | 17.57 | -12.43 | 2024-12-03 | 435000 | -17.59 | late_green_success_but_high_MAE |
| R6L33-C22-005830-S2 | 79700 | 32.25 | -3.89 | 43.29 | -3.89 | 51.44 | -3.89 | 2024-07-02 | 120700 | -14.58 | structural_success |
| R6L33-C22-005830-G | 111500 | 3.50 | -10.04 | 8.25 | -10.04 | 8.25 | -10.04 | 2024-07-02 | 120700 | -14.58 | late_green_low_edge |
| R6L33-C22-001450-S2 | 30150 | 22.06 | -1.99 | 22.06 | -5.64 | 21.89 | -5.64 | 2024-02-05 | 36800 | -22.69 | failed_rerating |
| R6L33-C22-001450-G | 34200 | 2.34 | -8.63 | 7.46 | -8.63 | 7.46 | -8.63 | 2024-07-31 | 36750 | -15.10 | false_positive_green_guard |
| R6L33-C22-088350-S2 | 2685 | 42.09 | -3.91 | 42.09 | -3.91 | 42.09 | -3.91 | 2024-02-13 | 3815 | -32.37 | price_moved_without_evidence |
| R6L33-C22-088350-4B | 3550 | 7.46 | -20.85 | 7.46 | -27.32 | 7.46 | -27.32 | 2024-02-13 | 3815 | -32.37 | price_only_local_4B_overlay |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | why |
|---|---|---|
| R6L33-C22-000810 | current_profile_too_late | Current profile would likely wait for Stage3 confirmation around 2024-05-16. The stock had already moved from 237,000 to 370,000; the Green lateness ratio is high. |
| R6L33-C22-005830 | current_profile_too_late | Same pattern: Stage2 policy + non-life quality captured most edge; Green on 2024-05-16 had only single-digit 90D MFE and double-digit MAE. |
| R6L33-C22-001450 | current_profile_false_positive | A generic insurer-result Green label after the May result-day jump had poor risk/reward and did not distinguish CSM/reserve quality strongly enough. |
| R6L33-C22-088350 | current_profile_correct_if_price_only_guard_applied | The price-only blowoff guard correctly prevents price-only insurance beta from becoming positive Stage2/3. Without that guard this would be a severe false positive. |

Stress-test answers:

```text
1. current calibrated profile likely handles price-only Hanwha Life correctly, but is too late for high-quality non-life winners and too permissive if generic insurer earnings are treated as Green.
2. Stage2 bonus is directionally useful for 000810/005830, but should be conditional on C22 quality fields.
3. Yellow 75 is acceptable, but C22 should separate policy beta from reserve/capital-return quality.
4. Green 87/revision 55 is too late for the best C22 winners if it waits for result-day confirmation only.
5. price-only blowoff guard is strengthened by 088350.
6. full 4B non-price requirement is strengthened: 088350 was a price-only local 4B, not a full thesis break.
7. hard 4C routing was not promoted in this loop; no hard 4C thesis-break row is claimed.
```

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2_Actionable_entry | Stage3_Green_entry | full_window_peak | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| R6L33-C22-000810 | 237000 | 370000 | 435000 | 0.67 | Green captured the right name but after most of the repricing. |
| R6L33-C22-005830 | 79700 | 111500 | 120700 | 0.78 | Green was very late; most upside was already consumed. |
| R6L33-C22-001450 | 30150 | 34200 | 36800 | 0.61 | Green was late and did not compensate for reserve/quality uncertainty. |
| R6L33-C22-088350 | 2685 | not_applicable | 3815 | not_applicable | No supported Stage3-Green trigger; price-only move only. |

C22 interpretation: the canal is narrow. Early Stage2 is valuable only when policy optionality docks into an insurer-specific quality pier: explicit capital return, reserve comfort, CSM/margin durability, and low accounting trust risk. A generic Value-up wave is water without a bank; it can lift everything briefly, then spill back.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | Stage2_entry | 4B_entry | local_peak | full_window_peak | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_evidence_type | verdict |
|---|---:|---:|---:|---:|---:|---:|---|---|
| R6L33-C22-088350-4B | 2685 | 3550 | 3815 | 3815 | 0.77 | 0.77 | price_only; positioning_overheat | price_only_local_4B_overlay; do_not_treat_as_full_4B=true |
| R6L33-C22-000810-4B-context | 237000 | 435000 | 435000 | 435000 | 1.00 | 1.00 | valuation_blowoff; positioning_overheat; capital_return_expectation_saturation | good_overlay_context_but_not_weighted_as_sell_rule |
| R6L33-C22-005830-4B-context | 79700 | 120700 | 120700 | 120700 | 1.00 | 1.00 | valuation_blowoff; positioning_overheat | good_overlay_context_but_not_weighted_as_sell_rule |

The key residual: price-only 4B can be useful as an overheat overlay, but for C22 it must not erase a structurally good non-life insurer unless a non-price slowdown appears.

## 16. 4C Protection Audit

No hard 4C row is proposed. Hanwha Life’s 2024-02/03 round-trip is a thesis-break watch candidate, but the evidence family in this run is not strong enough to assert `contract_cancelled`, `accounting_or_trust_break`, or a hard reserve failure. Therefore:

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_success = false
hard_4c_late = not_applicable
```

## 17. Sector-Specific Rule Candidate

```text
rule_id = L6_C22_INSURANCE_QUALITY_GATE
rule_scope = sector_specific
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
proposal_type = shadow_only
```

Candidate rule:

```text
For C22 insurance names, generic Corporate Value-up / low-PBR policy beta may support Stage2-Watch or Stage2-Actionable only when at least one insurer-specific quality field is present.

To promote to Stage3-Yellow/Green, require at least two of:
- explicit shareholder-return / capital-return visibility,
- CSM or insurance-service margin durability,
- reserve adequacy / 해약환급금준비금 comfort,
- loss-ratio or underwriting margin improvement,
- financial-visibility confirmation from multiple public sources.

If only price momentum and policy beta exist, cap at watch/overlay and block positive Stage3.
```

Backtest effect:

```text
positive retained = 000810, 005830
false-positive reduced = 001450 late Green, 088350 price-only beta
current_profile_error_count_reduced = 2 -> 0 or 1 depending Green threshold choice
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = C22_EXPLICIT_CAPITAL_RETURN_AND_RESERVE_QUALITY_BONUS
rule_scope = canonical_archetype_specific
baseline_value = 0
shadow_tested_value = +2.0 to +3.0
axis = c22_nonlife_explicit_capital_return_reserve_quality_bonus
confidence = medium_low
```

Rationale:

- 000810 and 005830 show that Stage2 entries worked when policy optionality aligned with non-life quality and shareholder-return interpretation.
- 001450 shows that result-day confirmation without enough reserve/loss-ratio confidence can be a poor Green entry.
- 088350 shows that life-insurer policy beta alone can generate large MFE but unreliable follow-through; it is not Stage3 evidence.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 4 | mixed; likely waits for Green in 000810/005830, may over-score 001450 | 28.37 | -7.39 | 0.25 | 0 | 2 | partial_alignment |
| P0b_e2r_2_0_baseline_reference | rollback | weaker Stage2; looser Green | 4 | later or noisier | 22.10 | -8.80 | 0.50 | 2 | 2 | worse_alignment |
| P1_L6_sector_specific_candidate | sector | require insurer quality for Stage3; allow quality Stage2 | 4 | Stage2 for 000810/005830; watch for 001450/088350 | 34.45 | -3.40 | 0.00 | 0 | 0 | best_alignment |
| P2_C22_canonical_candidate | canonical | C22 explicit capital-return/reserve bonus + price-only guard | 4 | same as P1 | 34.45 | -3.40 | 0.00 | 0 | 0 | best_alignment |
| P3_counterexample_guard_profile | guard | cap generic policy beta at watch unless CSM/reserve/capital-return evidence appears | 4 | excludes 088350 positive-stage; downgrades 001450 Green | 37.78 | -3.00 | 0.00 | 0 | 0 | strong_guard_alignment |

## 20. Score-Return Alignment Matrix

Canonical component keys are research proxy scores, not production scores.

| trigger_id | contract_score | backlog_visibility_score | margin_bridge_score | revision_score | relative_strength_score | customer_quality_score | policy_or_regulatory_score | valuation_repricing_score | execution_risk_score | legal_or_contract_risk_score | dilution_cb_risk_score | accounting_trust_risk_score | supplemental C22 score | weighted_before | stage_before | weighted_after | stage_after | alignment |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---|---|
| R6L33-C22-000810-S2 | 0 | 0 | 52 | 45 | 62 | 45 | 70 | 55 | 20 | 10 | 0 | 10 | 74 | 76 | Stage2-Actionable | 81 | Stage2-Actionable+ | aligned_positive |
| R6L33-C22-000810-G | 0 | 0 | 60 | 58 | 55 | 50 | 60 | 65 | 28 | 10 | 0 | 12 | 82 | 88 | Stage3-Green | 86 | Stage3-Yellow/late-Green | late_but_quality |
| R6L33-C22-005830-S2 | 0 | 0 | 50 | 43 | 60 | 43 | 70 | 52 | 22 | 10 | 0 | 12 | 72 | 75 | Stage2-Actionable | 80 | Stage2-Actionable+ | aligned_positive |
| R6L33-C22-005830-G | 0 | 0 | 58 | 56 | 50 | 45 | 60 | 60 | 30 | 10 | 0 | 14 | 80 | 87 | Stage3-Green | 84 | Stage3-Yellow/late-Green | late_edge |
| R6L33-C22-001450-G | 0 | 0 | 40 | 45 | 48 | 35 | 55 | 48 | 45 | 10 | 0 | 28 | 55 | 78 | Stage3-Yellow | 68 | Stage2/Watch | false_positive_reduced |
| R6L33-C22-088350-S2 | 0 | 0 | 30 | 30 | 72 | 25 | 60 | 70 | 55 | 10 | 0 | 35 | 35 | 74 | Stage2-Actionable? | 58 | Watch/4B overlay only | price_only_blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | IFRS17_CSM_RESERVE_CAPITAL_RETURN_INSURANCE_VALUEUP | 2 | 2 | 1 | 0 | 4 | 0 | 6 | 4 | 2 | true | true | positive/counterexample filled; 4C still missing |

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
current_profile_error_count: 2

tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- stage3_green_total_min
- stage3_green_revision_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- C22 Green too late after policy-beta repricing in high-quality non-life insurers
- Generic insurer-result Green false positive when reserve/capital-return quality is not strong enough
- Life-insurer price-only beta can create high MFE but unreliable follow-through

new_axis_proposed:
- c22_nonlife_explicit_capital_return_reserve_quality_bonus
- c22_generic_policy_beta_stage_cap
- c22_price_only_insurance_beta_4b_overlay_guard

existing_axis_strengthened:
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence

existing_axis_weakened: none
existing_axis_kept:
- stage2_actionable_evidence_bonus, but condition it for C22 quality
- stage3_yellow_total_min / green_min, but add C22-specific reserve/capital-return evidence gate

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: L6/C22 undercovered insurance reserve/rate/capital-return archetype
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- 2024 tradable OHLC rows for 000810, 005830, 001450, 088350
- symbol profile availability and corporate-action candidate windows
- 30D / 90D / 180D MFE/MAE for representative triggers
- Stage2 vs Green lateness comparison
- 4B local vs full-window split for the price-only Hanwha Life overlay
```

Not validated / intentionally not claimed:

```text
- No live candidate scan
- No 2026 watchlist
- No production code inspection
- No stock_agent source patch
- No hard 4C thesis-break promotion
- No global rule delta
- No recommendation language
- Exact company IR PDF line-by-line extraction was not performed; C22 quality component scores are research proxies capped accordingly.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_nonlife_explicit_capital_return_reserve_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+2,+2,"Non-life insurers with reserve/capital-return quality showed superior 90D/180D alignment from Stage2 entries.","Retains 000810/005830 early entries and avoids waiting for late Green.","R6L33-C22-000810-S2|R6L33-C22-005830-S2",4,4,2,medium_low,canonical_shadow_only,"not production; requires batch aggregation"
shadow_weight,c22_generic_policy_beta_stage_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,none,watch_cap,guard,"Corporate Value-up beta alone should not promote insurance names to Stage3 without reserve/capital-return quality.","Reduces 001450/088350 false positives.","R6L33-C22-001450-G|R6L33-C22-088350-S2",4,4,2,medium,canonical_shadow_only,"strengthens price-only guard"
shadow_weight,c22_price_only_insurance_beta_4b_overlay_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+1,+1,"Price-only life-insurer beta can be useful as an overheat overlay but not full 4B without non-price evidence.","Flags 088350 2024-02 local peak without treating it as thesis break.","R6L33-C22-088350-4B",1,1,1,low,overlay_shadow_only,"not sell rule; overlay only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R6L33-C22-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_CAPITAL_RETURN_VALUEUP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L33-C22-000810-S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 policy+quality aligned; Green was late","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Use as positive C22 quality gate evidence."}
{"row_type":"case","case_id":"R6L33-C22-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_CAPITAL_RETURN_VALUEUP","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L33-C22-005830-S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 aligned; late Green had weak incremental payoff","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Positive but highlights Green lateness."}
{"row_type":"case","case_id":"R6L33-C22-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GREEN_LATE_AFTER_VALUEUP_GAP","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L33-C22-001450-G","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Generic Green was poor after result-day jump","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Use as C22 reserve-quality Green guard."}
{"row_type":"case","case_id":"R6L33-C22-088350","symbol":"088350","company_name":"한화생명","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_PRICE_ONLY_VALUEUP_BLOWOFF","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R6L33-C22-088350-S2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"High MFE but price-only beta round-tripped; guard needed","current_profile_verdict":"current_profile_correct_if_price_only_guard_applied","price_source":"Songdaiki/stock-web","notes":"Use as price-only C22 counterexample and 4B overlay."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R6L33-C22-000810-S2","case_id":"R6L33-C22-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_CAPITAL_RETURN_VALUEUP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":237000,"evidence_available_at_that_date":"Corporate Value-up policy optionality and early low-PBR financial/insurance relative strength; no later result evidence used.","evidence_source":"policy/news window; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":43.46,"MFE_90D_pct":60.34,"MFE_180D_pct":66.03,"MFE_1Y_pct":83.54,"MFE_2Y_pct":null,"MAE_30D_pct":-2.11,"MAE_90D_pct":-2.11,"MAE_180D_pct":-2.11,"MAE_1Y_pct":-2.11,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-28","peak_price":393500,"drawdown_after_peak_pct":-17.53,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-000810-2024-01-24-237000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-000810-G","case_id":"R6L33-C22-000810","symbol":"000810","company_name":"삼성화재","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GREEN_LATE_AFTER_VALUEUP_GAP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green comparison","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":370000,"evidence_available_at_that_date":"1Q confirmation family and non-life quality, but after most early repricing.","evidence_source":"public result/news family; stock-web price rows","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv","profile_path":"atlas/symbol_profiles/000/000810.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":6.35,"MFE_90D_pct":6.35,"MFE_180D_pct":17.57,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.43,"MAE_90D_pct":-12.43,"MAE_180D_pct":-12.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":435000,"drawdown_after_peak_pct":-17.59,"green_lateness_ratio":0.67,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_success_but_high_MAE","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-000810-2024-05-16-370000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-005830-S2","case_id":"R6L33-C22-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"NONLIFE_IFRS17_CSM_CAPITAL_RETURN_VALUEUP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"coverage_gap_fill;sector_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":79700,"evidence_available_at_that_date":"Corporate Value-up policy optionality plus non-life insurer quality route; no later result evidence used.","evidence_source":"policy/news window; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":32.25,"MFE_90D_pct":43.29,"MFE_180D_pct":51.44,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.89,"MAE_90D_pct":-3.89,"MAE_180D_pct":-3.89,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-14.58,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-005830-2024-01-24-79700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-005830-G","case_id":"R6L33-C22-005830","symbol":"005830","company_name":"DB손해보험","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GREEN_LATE_AFTER_VALUEUP_GAP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"green_strictness_stress_test","trigger_type":"Stage3-Green comparison","trigger_date":"2024-05-16","entry_date":"2024-05-16","entry_price":111500,"evidence_available_at_that_date":"1Q confirmation family; late relative to 2024-01 policy-beta entry.","evidence_source":"public result/news family; stock-web price rows","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv","profile_path":"atlas/symbol_profiles/005/005830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.50,"MFE_90D_pct":8.25,"MFE_180D_pct":8.25,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.04,"MAE_90D_pct":-10.04,"MAE_180D_pct":-10.04,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-02","peak_price":120700,"drawdown_after_peak_pct":-14.58,"green_lateness_ratio":0.78,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_low_edge","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-005830-2024-05-16-111500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-001450-S2","case_id":"R6L33-C22-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GREEN_LATE_AFTER_VALUEUP_GAP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"counterexample_mining","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":30150,"evidence_available_at_that_date":"Policy optionality only; weaker C22 quality confirmation.","evidence_source":"policy/news window; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":22.06,"MFE_90D_pct":22.06,"MFE_180D_pct":21.89,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.99,"MAE_90D_pct":-5.64,"MAE_180D_pct":-5.64,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-05","peak_price":36800,"drawdown_after_peak_pct":-22.69,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive_if_promoted","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-001450-2024-01-24-30150","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-001450-G","case_id":"R6L33-C22-001450","symbol":"001450","company_name":"현대해상","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"GREEN_LATE_AFTER_VALUEUP_GAP","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"green_strictness_stress_test;counterexample_mining","trigger_type":"Stage3-Green stress","trigger_date":"2024-05-14","entry_date":"2024-05-14","entry_price":34200,"evidence_available_at_that_date":"Result-day jump without enough reserve/capital-return quality to justify Green.","evidence_source":"public result/news family; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality"],"stage3_evidence_fields":["confirmed_revision"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv","profile_path":"atlas/symbol_profiles/001/001450.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.34,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.63,"MAE_90D_pct":-8.63,"MAE_180D_pct":-8.63,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":36750,"drawdown_after_peak_pct":-15.10,"green_lateness_ratio":0.61,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green_guard","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-001450-2024-05-14-34200","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-088350-S2","case_id":"R6L33-C22-088350","symbol":"088350","company_name":"한화생명","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_PRICE_ONLY_VALUEUP_BLOWOFF","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"counterexample_mining;4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable / watch","trigger_date":"2024-01-24","entry_date":"2024-01-24","entry_price":2685,"evidence_available_at_that_date":"Policy beta and price momentum; insufficient insurer-specific quality.","evidence_source":"policy/news window; stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":42.09,"MFE_90D_pct":42.09,"MFE_180D_pct":42.09,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-3.91,"MAE_90D_pct":-3.91,"MAE_180D_pct":-3.91,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"price_only_local_4B_too_early_if_treated_as_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_moved_without_evidence","current_profile_verdict":"current_profile_correct_if_price_only_guard_applied","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-088350-2024-01-24-2685","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L33-C22-088350-4B","case_id":"R6L33-C22-088350","symbol":"088350","company_name":"한화생명","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"INSURANCE_PRICE_ONLY_VALUEUP_BLOWOFF","sector":"insurance","primary_archetype":"insurance_rate_cycle_reserve_capital_return","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"4B overlay","trigger_date":"2024-02-13","entry_date":"2024-02-13","entry_price":3550,"evidence_available_at_that_date":"Price-only local blowoff after Value-up beta; no non-price full 4B evidence.","evidence_source":"stock-web price rows","stage2_evidence_fields":["policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":7.46,"MFE_90D_pct":7.46,"MFE_180D_pct":7.46,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-20.85,"MAE_90D_pct":-27.32,"MAE_180D_pct":-27.32,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":null,"four_b_local_peak_proximity":0.77,"four_b_full_window_peak_proximity":0.77,"four_b_timing_verdict":"price_only_local_4B_overlay_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"price_only_local_4B_overlay","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L33-C22-088350-2024-02-13-3550","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L33-C22-000810","trigger_id":"R6L33-C22-000810-S2","symbol":"000810","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":52,"revision_score":45,"relative_strength_score":62,"customer_quality_score":45,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":52,"revision_score":45,"relative_strength_score":62,"customer_quality_score":45,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":20,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":10,"roe_pbr_capital_return_score":74},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable+","changed_components":["roe_pbr_capital_return_score","c22_quality_bonus"],"component_delta_explanation":"Add C22 non-life quality bonus without forcing late Green.","MFE_90D_pct":60.34,"MAE_90D_pct":-2.11,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L33-C22-005830","trigger_id":"R6L33-C22-005830-S2","symbol":"005830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":43,"relative_strength_score":60,"customer_quality_score":43,"policy_or_regulatory_score":70,"valuation_repricing_score":52,"execution_risk_score":22,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12},"weighted_score_before":75,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":50,"revision_score":43,"relative_strength_score":60,"customer_quality_score":43,"policy_or_regulatory_score":70,"valuation_repricing_score":52,"execution_risk_score":22,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":12,"roe_pbr_capital_return_score":72},"weighted_score_after":80,"stage_label_after":"Stage2-Actionable+","changed_components":["roe_pbr_capital_return_score","c22_quality_bonus"],"component_delta_explanation":"Non-life C22 quality supports earlier Stage2 rather than waiting for Green.","MFE_90D_pct":43.29,"MAE_90D_pct":-3.89,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L33-C22-001450","trigger_id":"R6L33-C22-001450-G","symbol":"001450","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":45,"relative_strength_score":48,"customer_quality_score":35,"policy_or_regulatory_score":55,"valuation_repricing_score":48,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":28},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":45,"relative_strength_score":48,"customer_quality_score":35,"policy_or_regulatory_score":55,"valuation_repricing_score":48,"execution_risk_score":45,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":28,"roe_pbr_capital_return_score":35},"weighted_score_after":68,"stage_label_after":"Stage2/Watch","changed_components":["c22_reserve_quality_gate","accounting_trust_risk_score"],"component_delta_explanation":"Downgrade generic insurer Green without reserve/capital-return evidence.","MFE_90D_pct":7.46,"MAE_90D_pct":-8.63,"score_return_alignment_label":"false_positive_reduced","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L33-C22-088350","trigger_id":"R6L33-C22-088350-S2","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":30,"relative_strength_score":72,"customer_quality_score":25,"policy_or_regulatory_score":60,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":35},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable?","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":30,"relative_strength_score":72,"customer_quality_score":25,"policy_or_regulatory_score":60,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":10,"dilution_cb_risk_score":0,"accounting_trust_risk_score":35,"roe_pbr_capital_return_score":20},"weighted_score_after":58,"stage_label_after":"Watch/4B overlay only","changed_components":["price_only_guard","c22_generic_policy_beta_stage_cap"],"component_delta_explanation":"High MFE but price-only; cap at watch and allow 4B overlay only.","MFE_90D_pct":42.09,"MAE_90D_pct":-3.91,"score_return_alignment_label":"price_only_blocked","current_profile_verdict":"current_profile_correct_if_price_only_guard_applied"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_nonlife_explicit_capital_return_reserve_quality_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+2,+2,"Non-life C22 quality improved Stage2/return alignment.","000810/005830 retained; Green lateness reduced.","R6L33-C22-000810-S2|R6L33-C22-005830-S2",4,4,2,medium_low,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_generic_policy_beta_stage_cap,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,none,watch_cap,guard,"Generic policy beta alone is not Stage3 insurance evidence.","001450/088350 false-positive risk reduced.","R6L33-C22-001450-G|R6L33-C22-088350-S2",4,4,2,medium,canonical_shadow_only,"strengthens existing price-only guard"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R6","loop":"33","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["C22_Green_late_after_policy_beta","generic_insurance_Green_false_positive","life_insurer_price_only_blowoff"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"L6/C22 insurance reserve-rate-capital-return undercoverage"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R6L33-C22-HARD4C-MISSING","symbol":null,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"No hard 4C thesis-break row was validated in this loop; future C22 work should look for reserve/accounting trust break cases.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round_candidate_1 = R6 / C22 hard 4C reserve/accounting-trust break case mining
next_round_candidate_2 = R7 / C23 BIO_REGULATORY_APPROVAL_COMMERCIALIZATION positive/counterexample split
next_round_candidate_3 = R5 / C20 BEAUTY_FOOD_GLOBAL_DISTRIBUTION channel reorder counterexamples
```

## 28. Source Notes

- Stock-web manifest: `atlas/manifest.json`.
- Stock-web profiles: `atlas/symbol_profiles/000/000810.json`, `atlas/symbol_profiles/005/005830.json`, `atlas/symbol_profiles/001/001450.json`, `atlas/symbol_profiles/088/088350.json`.
- Stock-web shards: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/2024.csv`.
- External historical context: Reuters, 2024-03-14, South Korea regulator to speed up corporate reforms and Corporate Value-up follow-up measures; WSJ 2024-05-13 headline for Samsung Fire 1Q consolidated revenue. These external sources are used only for evidence-timing context, not for OHLC calculation.
