# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R6_loop_14_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md
scheduled_round: R6
scheduled_loop: 14
completed_round: R6
completed_loop: 14
next_round: R7
next_loop: 14
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id: C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id: LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R6/L6_FINANCIAL_CAPITAL_RETURN_DIGITAL/C22_INSURANCE_RATE_CYCLE_RESERVE.

## 1. Current Calibrated Profile Assumption

Current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as fixed production assumptions:

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

This MD does not re-prove those axes. It stress-tests their remaining C22 insurance-specific residual error: life insurers can look like ordinary low-PBR/rate-cycle beneficiaries, but their real rerating path depends on CSM quality, K-ICS capital buffer, negative-spread risk, reserve adequacy, and explicit capital-return visibility.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R6
scheduled_loop = 14
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD
```

R6 maps to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`, so the round-sector gate passes.

Why C22 again: R6 loop 12 already covered non-life insurers (`삼성화재`, `DB손해보험`, `현대해상`). This loop deliberately moves to life insurers and uses new symbols: `삼성생명`, `동양생명`, `한화생명`, `미래에셋생명`.

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 registry state available in this work session shows:

```text
R6 loop 10: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
R6 loop 11: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
R6 loop 12: C22_INSURANCE_RATE_CYCLE_RESERVE, non-life insurer set
R6 loop 13: C21_FINANCIAL_ROE_PBR_CAPITAL_RETURN
R5 loop 14: completed, so next scheduled round is R6 loop 14
```

Duplicate gate:

```text
same symbol + same trigger_date + same entry_date + same evidence family = avoided
new independent symbols = 032830, 082640, 088350, 085620
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = not used
```

Previous C22 non-life loop used `000810`, `005830`, `001450`. This loop uses only new life-insurance symbols.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Schema validation:

```text
tradable_shard_columns = d,o,h,l,c,v,a,mc,s,m
raw_shard_columns = d,o,h,l,c,v,a,mc,s,m,rs
MFE_N_pct = (max high from entry_date through N tradable rows / entry_price - 1) * 100
MAE_N_pct = (min low from entry_date through N tradable rows / entry_price - 1) * 100
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
```

## 5. Historical Eligibility Gate

| symbol | profile_path | profile corporate-action caveat | entry_date | 180D window | calibration_usable |
|---|---|---|---:|---:|---:|
| 032830 | atlas/symbol_profiles/032/032830.json | no corporate-action candidate dates | 2024-02-02 | available before manifest max_date | true |
| 082640 | atlas/symbol_profiles/082/082640.json | old candidate: 2017-04-11 only | 2024-02-02 | available before manifest max_date | true |
| 088350 | atlas/symbol_profiles/088/088350.json | no corporate-action candidate dates | 2024-02-02 | available before manifest max_date | true |
| 085620 | atlas/symbol_profiles/085/085620.json | old candidate: 2018-03-23 only | 2024-02-02 | available before manifest max_date | true |

No selected representative 180D window overlaps a profile-level corporate-action candidate date.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD | C22_INSURANCE_RATE_CYCLE_RESERVE | Life-insurance cases still belong to the C22 insurance reserve/rate/capital-return family, but require separate CSM/K-ICS/negative-spread guard from non-life insurers. |
| LIFE_INSURANCE_EVENT_PREMIUM_4B_OVERLAY | C22_INSURANCE_RATE_CYCLE_RESERVE | Event/control-premium repricing is an overlay path inside C22, not a new canonical archetype. |
| LIFE_INSURANCE_RATE_BETA_FALSE_POSITIVE | C22_INSURANCE_RATE_CYCLE_RESERVE | Rate-cycle beta alone is a C22 counterexample, not a C21 bank value-up case. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | entry_date | entry_price | MFE_90D | MAE_90D | MFE_180D | MAE_180D | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---|
| R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202 | 032830 | 삼성생명 | structural_success | positive | 2024-02-02 | 78,400 | 38.39 | -6.12 | 38.39 | -6.12 | current_profile_too_late |
| R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202 | 082640 | 동양생명 | high_mae_success | positive | 2024-02-02 | 5,220 | 30.46 | -7.47 | 80.84 | -7.47 | current_profile_4B_too_late |
| R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202 | 088350 | 한화생명 | false_positive_green | counterexample | 2024-02-02 | 3,540 | 7.77 | -27.12 | 7.77 | -27.12 | current_profile_false_positive |
| R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202 | 085620 | 미래에셋생명 | failed_rerating | counterexample | 2024-02-02 | 6,040 | 7.62 | -27.07 | 7.62 | -27.07 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
representative_trigger_count = 4
new_independent_case_count = 4
reused_case_count = 0
```

The balance is intentional. C22 should promote verified CSM/K-ICS/capital-return evidence, but should block the mirage created by low-PBR policy beta or rate-cycle beta when negative-spread risk and reserve quality are unresolved.

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B/4C evidence | evidence source note |
|---|---|---|---|---|
| R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202 | value-up/low-PBR public context, relative strength, policy optionality | financial visibility, verified life-insurer capital-return quality | valuation/positioning overlay | stock-web OHLC + source_proxy issuer IR / earnings / policy evidence family |
| R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202 | event premium plus life-insurer repricing | financial visibility but thinner reserve/capital-return proof | event-premium 4B, later thesis-break watch | stock-web OHLC + source_proxy event/issuer evidence family |
| R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202 | low-PBR/rate-cycle beta | not enough verified CSM/K-ICS/capital-return proof | negative-spread/reserve-quality guard | stock-web OHLC + source_proxy rate-cycle evidence family |
| R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202 | low-PBR/rate-cycle beta | not enough verified CSM/K-ICS/capital-return proof | liquidity/capital-return gap guard | stock-web OHLC + source_proxy rate-cycle evidence family |

## 10. Price Data Source Map

| symbol | company | tradable shard | profile | profile note | observed row note |
|---:|---|---|---|---|---|
| 032830 | 삼성생명 | atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv | atlas/symbol_profiles/032/032830.json | profile has no corporate-action candidate dates; 2024 tested window clean. | Entry close 78,400 on 2024-02-02; 2024-03-08 high 108,500; post-peak low proxy 76,600. |
| 082640 | 동양생명 | atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv | atlas/symbol_profiles/082/082640.json | profile has a corporate-action candidate on 2017-04-11 only; no overlap with 2024 180D window. | Entry close 5,220 on 2024-02-02; 2024-07-31 high 9,440; post-peak low proxy 5,220. |
| 088350 | 한화생명 | atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv | atlas/symbol_profiles/088/088350.json | profile has no corporate-action candidate dates; 2024 tested window clean. | Entry close 3,540 on 2024-02-02; local high 3,815 on 2024-02-13; 180D low proxy 2,580. |
| 085620 | 미래에셋생명 | atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv | atlas/symbol_profiles/085/085620.json | profile has a corporate-action candidate on 2018-03-23 only; no overlap with 2024 180D window. | Entry close 6,040 on 2024-02-02; local high 6,500 on 2024-02-06; 180D low proxy 4,405. |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | current_profile_verdict | dedupe_for_aggregate |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|
| R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS | 032830 | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 78,400 | 38.39 | 38.39 | 38.39 | -6.12 | -6.12 | -6.12 | 2024-03-08 | 108,500 | current_profile_too_late | True |
| R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM | 082640 | Stage2-Actionable | 2024-02-02 | 2024-02-02 | 5,220 | 24.52 | 30.46 | 80.84 | -4.5 | -7.47 | -7.47 | 2024-07-31 | 9,440 | current_profile_4B_too_late | True |
| R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD | 088350 | Stage2-FalsePositive | 2024-02-02 | 2024-02-02 | 3,540 | 7.77 | 7.77 | 7.77 | -15.54 | -27.12 | -27.12 | 2024-02-13 | 3,815 | current_profile_false_positive | True |
| R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY | 085620 | Stage2-FalsePositive | 2024-02-02 | 2024-02-02 | 6,040 | 7.62 | 7.62 | 7.62 | -25.99 | -27.07 | -27.07 | 2024-02-06 | 6,500 | current_profile_false_positive | True |
| R6L14_T02B_DONGLIFE_20240807_4B_EVENT_PREMIUM_OVERLAY | 082640 | Stage4B-overlay | 2024-08-07 | 2024-08-07 | 8,960 | 1.45 | 1.45 | None | -37.83 | None | None | 2024-07-31 | 9,440 | current_profile_4B_too_late | False |

## 12. Trigger-Level OHLC Backtest Tables

Representative triggers included in aggregate:

| symbol | entry | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | below_entry_90D | peak |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 032830 | 2024-02-02 | 78,400 | 38.39 | -6.12 | 38.39 | -6.12 | 38.39 | -6.12 | true | 2024-03-08 / 108,500 |
| 082640 | 2024-02-02 | 5,220 | 24.52 | -4.50 | 30.46 | -7.47 | 80.84 | -7.47 | true | 2024-07-31 / 9,440 |
| 088350 | 2024-02-02 | 3,540 | 7.77 | -15.54 | 7.77 | -27.12 | 7.77 | -27.12 | true | 2024-02-13 / 3,815 |
| 085620 | 2024-02-02 | 6,040 | 7.62 | -25.99 | 7.62 | -27.07 | 7.62 | -27.07 | true | 2024-02-06 / 6,500 |

Aggregate representative rows:

```text
P0 all representative rows:
avg_MFE_90D_pct = 21.06
avg_MAE_90D_pct = -16.95
avg_MFE_180D_pct = 33.66
avg_MAE_180D_pct = -16.95
false_positive_rate = 0.50

P2 canonical guard selected positives:
avg_MFE_90D_pct = 34.42
avg_MAE_90D_pct = -6.79
avg_MFE_180D_pct = 59.62
avg_MAE_180D_pct = -6.79
false_positive_rate = 0.00
```

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated profile likely decision | actual OHLC alignment | verdict |
|---|---|---|---|
| 032830 Samsung Life | Stage3-Yellow / late Green due to general C22 and value-up evidence | good; MFE90 +38.39 with limited MAE | current_profile_too_late |
| 082640 Dongyang Life | Stage3-Yellow, but 4B overlay likely late | positive but required event-premium 4B; drawdown after peak -44.70 | current_profile_4B_too_late |
| 088350 Hanwha Life | could be promoted by low-PBR/rate beta if guard absent | poor; MFE180 +7.77 vs MAE180 -27.12 | current_profile_false_positive |
| 085620 Mirae Asset Life | could be promoted by life-insurance/value-up beta if guard absent | poor; MFE180 +7.62 vs MAE180 -27.07 | current_profile_false_positive |

Applied-axis answers:

```text
stage2_actionable_evidence_bonus: kept, but should not apply to rate beta alone.
stage3_yellow_total_min: kept.
stage3_green_total_min: kept.
stage3_green_revision_min: kept.
stage3_cross_evidence_green_buffer: kept.
price_only_blowoff_blocks_positive_stage: strengthened for life insurers.
full_4b_requires_non_price_evidence: strengthened for event-premium / control-premium rows.
hard_4c_thesis_break_routes_to_4c: strengthened for negative-spread/reserve-quality breakdown.
```

## 14. Stage2 / Yellow / Green Comparison

Samsung Life shows the clean positive: Stage2/Yellow at entry captured the better part of the move, while Green should require verified CSM/K-ICS/capital-return evidence rather than merely price strength.

Dongyang Life shows the dangerous positive: Stage2 entry had large upside, but the later event-premium surge required a 4B overlay. Without that overlay, the model would read the same row as durable insurance rerating even after the market started pricing event/control premium.

Hanwha Life and Mirae Asset Life show the false-positive pair: a life-insurer beta basket can move briefly on policy/rate headlines, but if reserve quality, negative-spread risk, K-ICS buffer, and shareholder-return visibility remain unsupported, the price path looks like a trapdoor rather than an elevator.

## 15. 4B Local vs Full-window Timing Audit

| row | Stage2 entry | 4B or peak reference | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---:|---|
| 032830 | 78,400 | 108,500 | 0.84 | 1.00 | good_full_window_4B_timing_if_non_price_positioning_confirmed |
| 082640 | 5,220 | 8,960 overlay / 9,440 high | 0.89 | 0.89 | good_full_window_4B_timing_if_event_cap_confirmed |
| 088350 | 3,540 | 3,815 local high | 1.00 | 1.00 | price-only local 4B too early without non-price confirmation |
| 085620 | 6,040 | 6,500 local high | 1.00 | 1.00 | price-only local 4B too early without non-price confirmation |

Key split:

```text
If 4B is non-price event/valuation/positioning evidence near full-window proximity: useful.
If 4B is only a local price high: not enough.
```

## 16. 4C Protection Audit

| case | prior peak | post-peak low proxy | drawdown_after_peak_pct | 4C label |
|---|---:|---:|---:|---|
| 032830 | 108,500 | 76,600 | -29.40 | thesis_break_watch_only |
| 082640 | 9,440 | 5,220 | -44.70 | hard_4c_success_after_event_premium_reversal |
| 088350 | 3,815 | 2,580 | -32.37 | hard_4c_success_if_negative_spread_or_capital_return_gap_confirmed |
| 085620 | 6,500 | 4,405 | -32.23 | hard_4c_success_if_liquidity_or_capital_return_gap_confirmed |

C22 life-insurance 4C should not wait for price collapse alone. It should route to watch/4C when the thesis breaks at the reserve, negative-spread, K-ICS, or capital-return layer.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

This loop is not broad enough to change all L6 financial scoring. The evidence is life-insurance-specific and should not spill into banks, brokerages, cards, or digital-finance cases.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Candidate rule:

```text
For C22 life-insurer rows, do not allow low-PBR/rate-cycle beta to promote to Stage3-Yellow/Green unless at least two of the following are explicitly supported:
- verified IFRS17 CSM quality
- K-ICS / capital buffer sufficiency
- capital-return visibility
- reserve-risk / negative-spread risk not deteriorating
- evidence is not only event/control-premium speculation
```

Promotion bonus:

```text
life_insurance_verified_CSM_KICS_capital_return_bonus = +1 shadow
```

Guard:

```text
life_insurance_negative_spread_reserve_guard = +1 shadow blocker
event_premium_4B_overlay_guard = +1 overlay-only
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | alignment |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 4 | 21.06 | -16.95 | 33.66 | -16.95 | 0.5 | 0 | 1 | mixed; good on Samsung/Dongyang, poor on Hanwha/Mirae |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback | 4 | 18.56 | -20.56 | 28.28 | -20.56 | 0.67 | 1 | 2 | worse |
| P1_sector_specific_candidate_profile | sector_specific | life_insurance_verified_CSM_KICS_capital_return_bonus; negative_spread_reserve_guard | 2 | 34.42 | -6.79 | 59.62 | -6.79 | 0.0 | 0 | 1 | improved |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | life_insurance_verified_CSM_KICS_capital_return_bonus; life_insurance_negative_spread_reserve_guard; event_premium_4B_overlay_guard | 2 | 34.42 | -6.79 | 59.62 | -6.79 | 0.0 | 0 | 1 | best |
| P3_counterexample_guard_profile | counterexample_guard | stricter negative-spread/reserve guard | 1 | 38.39 | -6.12 | 38.39 | -6.12 | 0.0 | 1 | 0 | safe but misses event-premium upside |

## 20. Score-Return Alignment Matrix

| case | P0 score label | P2 shadow label | return alignment | residual conclusion |
|---|---|---|---|---|
| 032830 | Stage3-Yellow | Stage3-Green-shadow | good positive | current profile too late on verified life-insurer quality |
| 082640 | Stage3-Yellow-low | Stage3-Yellow-high with 4B watch | high MFE but large post-peak drawdown | needs 4B overlay; not pure promotion |
| 088350 | Stage3-Yellow false | Stage2-Watch/Blocked | poor MFE/MAE | block rate-beta-only life insurer |
| 085620 | Stage3-Yellow false | Stage2-Watch/Blocked | poor MFE/MAE | block low-liquidity/value-up beta without proof |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD | 2 | 2 | 1 | 1 | 4 | 0 | 4 | 4 | 3 | false | true | non-life C22 already had coverage; life-insurance C22 now has positive/counterexample balance |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 5
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 5
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
  - life_insurance_rate_beta_false_positive
  - negative_spread_or_reserve_quality_guard_missing
  - event_premium_4B_too_late
  - life_insurance_green_too_late_for_high_quality_CSM_KICS
new_axis_proposed:
  - life_insurance_verified_CSM_KICS_capital_return_bonus
  - life_insurance_negative_spread_reserve_guard
  - event_premium_4B_overlay_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- scheduled round and sector consistency
- stock-web manifest max_date = 2026-02-20
- actual stock-web tradable OHLC rows for entry/high/low/peak points
- symbol profile corporate-action window caveats
- 30D/90D/180D representative MFE/MAE
- positive/counterexample balance
- same-entry dedupe rules
- 4B local/full-window split
```

Not validated:

```text
- current live stock attractiveness
- production scoring code
- brokerage execution
- current watchlist
- exact source URL enrichment for every historical non-price evidence row
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,life_insurance_verified_CSM_KICS_capital_return_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+1,+1,"Reward life insurers only when CSM/K-ICS/capital-return visibility is verified, not when low-PBR/rate beta appears alone.","Keeps Samsung Life and Dongyang positive while preventing rate-beta-only false positives.","R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS|R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,life_insurance_negative_spread_reserve_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+1,+1,"Block Green when negative-spread / reserve quality / capital return visibility is unresolved.","Reduces Hanwha Life and Mirae Asset Life false-positive Stage2/Yellow candidates with high MAE.", "R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD|R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY",4,4,2,medium,canonical_shadow_only,"not production; guardrail"
shadow_weight,event_premium_4B_overlay_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+1,+1,"If event/control-premium repricing outruns CSM/capital-return proof, add 4B overlay rather than upgrading positive score.","Dongyang post-peak drawdown shows 4B/4C timing value.", "R6L14_T02B_DONGLIFE_20240807_4B_EVENT_PREMIUM_OVERLAY",1,1,0,low,overlay_shadow_only,"4B overlay; not representative positive entry"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"life_insurance_CSM_KICS_capital_return_rerating_success","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Entry close 78,400 on 2024-02-02; 2024-03-08 high 108,500; post-peak low proxy 76,600. profile has no corporate-action candidate dates; 2024 tested window clean."}
{"row_type":"case","case_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202","symbol":"082640","company_name":"동양생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"life_insurance_event_premium_success_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Entry close 5,220 on 2024-02-02; 2024-07-31 high 9,440; post-peak low proxy 5,220. profile has a corporate-action candidate on 2017-04-11 only; no overlap with 2024 180D window."}
{"row_type":"case","case_id":"R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202","symbol":"088350","company_name":"한화생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"rate_beta_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Entry close 3,540 on 2024-02-02; local high 3,815 on 2024-02-13; 180D low proxy 2,580. profile has no corporate-action candidate dates; 2024 tested window clean."}
{"row_type":"case","case_id":"R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"thin_liquidity_life_insurer_beta_failed_rerating","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Entry close 6,040 on 2024-02-02; local high 6,500 on 2024-02-06; 180D low proxy 4,405. profile has a corporate-action candidate on 2018-03-23 only; no overlap with 2024 180D window."}
{"row_type":"trigger","trigger_id":"R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS","case_id":"R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202","symbol":"032830","company_name":"삼성생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","sector":"금융·자본배분·디지털금융","primary_archetype":"life-insurance IFRS17/CSM/K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","evidence_available_at_that_date":"2024 value-up/low-PBR policy context plus life-insurer IFRS17 CSM/K-ICS and capital-return visibility. Positive case because the price path rewarded verified balance-sheet/capital-return quality rather than rate beta alone.","evidence_source":"stock-web OHLC row validation + source_proxy: issuer IR / earnings / value-up policy evidence family; exact URL enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","multiple_public_sources","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv","profile_path":"atlas/symbol_profiles/032/032830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":78400,"MFE_30D_pct":38.39,"MFE_90D_pct":38.39,"MFE_180D_pct":38.39,"MFE_1Y_pct":38.39,"MFE_2Y_pct":null,"MAE_30D_pct":-6.12,"MAE_90D_pct":-6.12,"MAE_180D_pct":-6.12,"MAE_1Y_pct":-6.12,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-08","peak_price":108500,"drawdown_after_peak_pct":-29.4,"green_lateness_ratio":0.28,"four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_positioning_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"life_insurance_CSM_KICS_capital_return_rerating_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202|2024-02-02|78400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM","case_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202","symbol":"082640","company_name":"동양생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","sector":"금융·자본배분·디지털금융","primary_archetype":"life-insurance IFRS17/CSM/K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-02","evidence_available_at_that_date":"Life-insurance capital/event premium case: strong 180D MFE, but the same path produced a sharp post-peak drawdown. This is useful because C22 should not only promote; it should add a 4B overlay when event premium outruns reserve/capital-return proof.","evidence_source":"stock-web OHLC row validation + source_proxy: issuer/event/IR evidence family; exact URL enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv","profile_path":"atlas/symbol_profiles/082/082640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":5220,"MFE_30D_pct":24.52,"MFE_90D_pct":30.46,"MFE_180D_pct":80.84,"MFE_1Y_pct":80.84,"MFE_2Y_pct":null,"MAE_30D_pct":-4.5,"MAE_90D_pct":-7.47,"MAE_180D_pct":-7.47,"MAE_1Y_pct":-16.19,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":9440,"drawdown_after_peak_pct":-44.7,"green_lateness_ratio":0.45,"four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_full_window_4B_timing_if_event_premium_and_reserve_quality_non_price_evidence_exist","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_after_event_premium_reversal","trigger_outcome_label":"life_insurance_event_premium_success_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_2017_corporate_action_not_overlapping","same_entry_group_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202|2024-02-02|5220","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD","case_id":"R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202","symbol":"088350","company_name":"한화생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","sector":"금융·자본배분·디지털금융","primary_archetype":"life-insurance IFRS17/CSM/K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-02","evidence_available_at_that_date":"Counterexample: low-PBR/value-up and rate-cycle beta alone produced poor MFE/MAE alignment. C22 needs a negative-spread/reserve-quality gate before life-insurer beta is promoted.","evidence_source":"stock-web OHLC row validation + source_proxy: value-up/rate-cycle evidence family; exact URL enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv","profile_path":"atlas/symbol_profiles/088/088350.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":3540,"MFE_30D_pct":7.77,"MFE_90D_pct":7.77,"MFE_180D_pct":7.77,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.54,"MAE_90D_pct":-27.12,"MAE_180D_pct":-27.12,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-13","peak_price":3815,"drawdown_after_peak_pct":-32.37,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_confirmation","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_success_if_negative_spread_or_capital_return_gap_confirmed","trigger_outcome_label":"rate_beta_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202|2024-02-02|3540","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY","case_id":"R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202","symbol":"085620","company_name":"미래에셋생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","sector":"금융·자본배분·디지털금융","primary_archetype":"life-insurance IFRS17/CSM/K-ICS rate-cycle reserve/capital-return","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|canonical_archetype_compression","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-02-02","evidence_available_at_that_date":"Counterexample: life-insurance beta and one-off value-up rally without durable CSM/K-ICS/capital-return proof gave high MAE and no sustained rerating.","evidence_source":"stock-web OHLC row validation + source_proxy: value-up/rate-cycle evidence family; exact URL enrichment before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv","profile_path":"atlas/symbol_profiles/085/085620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-02","entry_price":6040,"MFE_30D_pct":7.62,"MFE_90D_pct":7.62,"MFE_180D_pct":7.62,"MFE_1Y_pct":7.62,"MFE_2Y_pct":null,"MAE_30D_pct":-25.99,"MAE_90D_pct":-27.07,"MAE_180D_pct":-27.07,"MAE_1Y_pct":-27.07,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-06","peak_price":6500,"drawdown_after_peak_pct":-32.23,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early_without_non_price_confirmation","four_b_evidence_type":["price_only","valuation_blowoff"],"four_c_protection_label":"hard_4c_success_if_liquidity_or_capital_return_gap_confirmed","trigger_outcome_label":"thin_liquidity_life_insurer_beta_failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_2018_corporate_action_not_overlapping","same_entry_group_id":"R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202|2024-02-02|6040","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R6L14_T02B_DONGLIFE_20240807_4B_EVENT_PREMIUM_OVERLAY","case_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202","symbol":"082640","company_name":"동양생명","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","fine_archetype_id":"LIFE_INSURANCE_IFRS17_CSM_KICS_CAPITAL_RETURN_AND_NEGATIVE_SPREAD_GUARD","sector":"금융·자본배분·디지털금융","primary_archetype":"life-insurance event-premium 4B overlay","loop_objective":"4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage4B-overlay","trigger_date":"2024-08-07","evidence_available_at_that_date":"Observed event-premium extension after the earlier C22 life-insurer rerating. This is an overlay row only: it calibrates 4B timing and should not be treated as a fresh positive entry.","evidence_source":"stock-web observed price path; non-price event-premium/positioning evidence must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","explicit_event_cap"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv","profile_path":"atlas/symbol_profiles/082/082640.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-07","entry_price":8960,"MFE_30D_pct":1.45,"MFE_90D_pct":1.45,"MFE_180D_pct":null,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-37.83,"MAE_90D_pct":null,"MAE_180D_pct":null,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-31","peak_price":9440,"drawdown_after_peak_pct":-44.7,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_event_cap_confirmed","four_b_evidence_type":["valuation_blowoff","positioning_overheat","control_premium_or_event_premium"],"four_c_protection_label":"hard_4c_success_after_event_premium_reversal","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":false,"forward_window_trading_days":90,"calibration_block_reasons":["overlay_not_representative_entry","not_used_for_positive_weight_calibration"],"corporate_action_window_status":"clean_observed_window_old_2017_action_not_overlapping","same_entry_group_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202|2024-08-07|8960","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_different_trigger_family_4B_overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202","trigger_id":"R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":74,"kics_capital_buffer_score":76,"reserve_risk_score":24,"shareholder_return_visibility_score":70,"negative_spread_risk_score":22,"life_insurer_capital_return_score":72},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":88,"kics_capital_buffer_score":86,"reserve_risk_score":18,"shareholder_return_visibility_score":86,"negative_spread_risk_score":16,"life_insurer_capital_return_score":88},"weighted_score_after":89,"stage_label_after":"Stage3-Green-shadow","changed_components":["ifrs17_csm_quality_score","kics_capital_buffer_score","shareholder_return_visibility_score","negative_spread_risk_score","life_insurer_capital_return_score"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":38.39,"MAE_90D_pct":-6.12,"score_return_alignment_label":"life_insurance_CSM_KICS_capital_return_rerating_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"c22_life_insurance_csm_kics_negative_spread_shadow_profile","case_id":"R6L14_C22_032830_SAMSUNGLIFE_LIFE_CSM_KICS_CAPITAL_RETURN_20240202","trigger_id":"R6L14_T01_SAMSUNGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_KICS","symbol":"032830","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":74,"kics_capital_buffer_score":76,"reserve_risk_score":24,"shareholder_return_visibility_score":70,"negative_spread_risk_score":22,"life_insurer_capital_return_score":72},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":88,"kics_capital_buffer_score":86,"reserve_risk_score":18,"shareholder_return_visibility_score":86,"negative_spread_risk_score":16,"life_insurer_capital_return_score":88},"weighted_score_after":89,"stage_label_after":"Stage3-Green-shadow","changed_components":["ifrs17_csm_quality_score","kics_capital_buffer_score","shareholder_return_visibility_score","negative_spread_risk_score","life_insurer_capital_return_score"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":38.39,"MAE_90D_pct":-6.12,"score_return_alignment_label":"life_insurance_CSM_KICS_capital_return_rerating_success","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202","trigger_id":"R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM","symbol":"082640","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":60,"kics_capital_buffer_score":58,"reserve_risk_score":42,"shareholder_return_visibility_score":54,"negative_spread_risk_score":36,"life_insurer_capital_return_score":56,"event_premium_score":74},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow-low","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":66,"kics_capital_buffer_score":64,"reserve_risk_score":48,"shareholder_return_visibility_score":60,"negative_spread_risk_score":42,"life_insurer_capital_return_score":62,"event_premium_score":82,"event_premium_overheat_guard":78},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-high_with_4B_watch","changed_components":["event_premium_score","event_premium_overheat_guard","reserve_risk_score","life_insurer_capital_return_score"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":30.46,"MAE_90D_pct":-7.47,"score_return_alignment_label":"life_insurance_event_premium_success_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"c22_life_insurance_csm_kics_negative_spread_shadow_profile","case_id":"R6L14_C22_082640_DONGLIFE_M_AND_A_LIFE_RESERVE_4B_20240202","trigger_id":"R6L14_T02_DONGLIFE_20240202_STAGE2_ACTIONABLE_LIFE_CSM_EVENT_PREMIUM","symbol":"082640","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":60,"kics_capital_buffer_score":58,"reserve_risk_score":42,"shareholder_return_visibility_score":54,"negative_spread_risk_score":36,"life_insurer_capital_return_score":56,"event_premium_score":74},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow-low","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":66,"kics_capital_buffer_score":64,"reserve_risk_score":48,"shareholder_return_visibility_score":60,"negative_spread_risk_score":42,"life_insurer_capital_return_score":62,"event_premium_score":82,"event_premium_overheat_guard":78},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow-high_with_4B_watch","changed_components":["event_premium_score","event_premium_overheat_guard","reserve_risk_score","life_insurer_capital_return_score"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":30.46,"MAE_90D_pct":-7.47,"score_return_alignment_label":"life_insurance_event_premium_success_but_4B_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202","trigger_id":"R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":42,"kics_capital_buffer_score":48,"reserve_risk_score":68,"shareholder_return_visibility_score":34,"negative_spread_risk_score":72,"life_insurer_capital_return_score":30,"rate_cycle_tailwind_score":78},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":34,"kics_capital_buffer_score":42,"reserve_risk_score":82,"shareholder_return_visibility_score":24,"negative_spread_risk_score":86,"life_insurer_capital_return_score":20,"rate_cycle_tailwind_score":60,"life_insurance_beta_without_csm_penalty":-14},"weighted_score_after":58,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["negative_spread_risk_score","reserve_risk_score","shareholder_return_visibility_score","life_insurance_beta_without_csm_penalty"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":7.77,"MAE_90D_pct":-27.12,"score_return_alignment_label":"rate_beta_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"c22_life_insurance_csm_kics_negative_spread_shadow_profile","case_id":"R6L14_C22_088350_HANWHALIFE_RATE_BETA_NEGATIVE_SPREAD_FALSEPOSITIVE_20240202","trigger_id":"R6L14_T03_HANWHALIFE_20240202_FALSE_STAGE2_RATE_BETA_NEGATIVE_SPREAD_GUARD","symbol":"088350","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":42,"kics_capital_buffer_score":48,"reserve_risk_score":68,"shareholder_return_visibility_score":34,"negative_spread_risk_score":72,"life_insurer_capital_return_score":30,"rate_cycle_tailwind_score":78},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":34,"kics_capital_buffer_score":42,"reserve_risk_score":82,"shareholder_return_visibility_score":24,"negative_spread_risk_score":86,"life_insurer_capital_return_score":20,"rate_cycle_tailwind_score":60,"life_insurance_beta_without_csm_penalty":-14},"weighted_score_after":58,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["negative_spread_risk_score","reserve_risk_score","shareholder_return_visibility_score","life_insurance_beta_without_csm_penalty"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":7.77,"MAE_90D_pct":-27.12,"score_return_alignment_label":"rate_beta_false_positive_high_MAE","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202","trigger_id":"R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":38,"kics_capital_buffer_score":44,"reserve_risk_score":60,"shareholder_return_visibility_score":28,"negative_spread_risk_score":64,"life_insurer_capital_return_score":24,"liquidity_quality_score":32},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":30,"kics_capital_buffer_score":38,"reserve_risk_score":74,"shareholder_return_visibility_score":20,"negative_spread_risk_score":76,"life_insurer_capital_return_score":16,"liquidity_quality_score":22,"life_insurance_beta_without_csm_penalty":-16},"weighted_score_after":56,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["negative_spread_risk_score","reserve_risk_score","shareholder_return_visibility_score","liquidity_quality_score","life_insurance_beta_without_csm_penalty"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":7.62,"MAE_90D_pct":-27.07,"score_return_alignment_label":"thin_liquidity_life_insurer_beta_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"c22_life_insurance_csm_kics_negative_spread_shadow_profile","case_id":"R6L14_C22_085620_MIRAEASSETLIFE_LOW_LIQUIDITY_LIFE_BETA_FALSEPOSITIVE_20240202","trigger_id":"R6L14_T04_MIRAEASSETLIFE_20240202_FALSE_STAGE2_LIFE_BETA_LOW_LIQUIDITY","symbol":"085620","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":38,"kics_capital_buffer_score":44,"reserve_risk_score":60,"shareholder_return_visibility_score":28,"negative_spread_risk_score":64,"life_insurer_capital_return_score":24,"liquidity_quality_score":32},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow_false","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":0,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"ifrs17_csm_quality_score":30,"kics_capital_buffer_score":38,"reserve_risk_score":74,"shareholder_return_visibility_score":20,"negative_spread_risk_score":76,"life_insurer_capital_return_score":16,"liquidity_quality_score":22,"life_insurance_beta_without_csm_penalty":-16},"weighted_score_after":56,"stage_label_after":"Stage2-Watch_or_blocked","changed_components":["negative_spread_risk_score","reserve_risk_score","shareholder_return_visibility_score","liquidity_quality_score","life_insurance_beta_without_csm_penalty"],"component_delta_explanation":"C22 life-insurance shadow separates verified IFRS17/CSM/K-ICS/capital-return visibility from generic rate-cycle or low-PBR beta, and adds negative-spread / reserve-risk guards.","MFE_90D_pct":7.62,"MAE_90D_pct":-27.07,"score_return_alignment_label":"thin_liquidity_life_insurer_beta_failed_rerating","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R6","loop":"14","scheduled_round":"R6","scheduled_loop":14,"round_schedule_status":"valid","round_sector_consistency":"pass","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":5,"new_trigger_family_count":5,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["life_insurance_rate_beta_false_positive","negative_spread_or_reserve_quality_guard_missing","event_premium_4B_too_late","life_insurance_green_too_late_for_high_quality_CSM_KICS"],"diversity_score_summary":"same_archetype_new_symbol +16; same_archetype_counterexample +10; new_trigger_family +20; new_regime +3; residual_error +15; wrong_round_penalty 0; estimated +64","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 14
next_round = R7
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files accessed or validated for this MD:

```text
manifest = atlas/manifest.json
schema = atlas/schema.json
profiles:
  - atlas/symbol_profiles/032/032830.json
  - atlas/symbol_profiles/082/082640.json
  - atlas/symbol_profiles/088/088350.json
  - atlas/symbol_profiles/085/085620.json
tradable shards:
  - atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/032/032830/2025.csv
  - atlas/ohlcv_tradable_by_symbol_year/082/082640/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/082/082640/2025.csv
  - atlas/ohlcv_tradable_by_symbol_year/088/088350/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/085/085620/2024.csv
```

The research uses raw/unadjusted OHLC. Corporate actions are not adjusted; non-overlapping old candidate dates are noted, and 2024 tested windows are treated as calibration-usable.
