# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R6
loop = 36
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN / LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD / SMALL_INSURER_LOW_FLOAT_VALUEUP_FALSE_POSITIVE / INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD
output_format = one_standalone_markdown_file
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file follows the v12 prompt constraints supplied by the user. fileciteturn735file0

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
```

Applied global axes are treated as already promoted, not re-proposed: Stage2 actionable bonus, Yellow threshold relaxation, stricter Green total/revision requirements, Green cross-evidence buffer, 4B non-price requirement, hard 4C routing, and price-only positive-stage guard. The calibration report explicitly marks these axes as applied and notes that 4B/4C rows do not train positive entry weights. fileciteturn741file0

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
loop = 36
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
primary_archetype = insurance_rate_reserve_capital_return_cycle
loop_objective = coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; 4B_non_price_requirement_stress_test; canonical_archetype_compression
```

The selected scope deliberately follows the prior C21 bank/value-up loop but moves to insurance. The goal is not to prove that “Value-Up worked” generally. The aim is to split true insurance reserve/capital-return rerating from low-PBR policy theme spikes and control-premium event moves.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact review was limited to calibration reports and registries. The ingest summary shows broad R1–R13 coverage and 1,376 aggregate representative rows, but the local artifact search returned no direct C22 insurance-rate/reserve-capital-return hit for 삼성화재 / DB손해보험 / 삼성생명 / 한화생명 / 보험. fileciteturn739file0

```text
auto_selected_coverage_gap = R6/L6 C22 insurance rate/reserve/capital-return cycle under-covered after C21 bank value-up loop
same_canonical_archetype_research = new
reused_case_count = 0
new_symbol_count = 5
minimum_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

The stock-web manifest was read before case work. It reports FinanceData/marcap as the upstream source, raw/unadjusted marcap prices, max_date 2026-02-20, 14,354,401 tradable rows, 15,214,118 raw rows, 5,414 symbols, and the calibration shard root `atlas/ohlcv_tradable_by_symbol_year`. fileciteturn737file0

The schema confirms that tradable shards contain `d,o,h,l,c,v,a,mc,s,m`, raw shards add `rs`, the calibration basis is `tradable_raw`, and MFE/MAE are computed from high/low over forward tradable rows. It also states that calibration requires an entry row, at least 180 forward tradable days, computed 30/90/180D MFE/MAE, and no 180D corporate-action contamination. fileciteturn738file0

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative triggers are historical and have stock-web tradable entry rows. The 180D windows are available because the manifest max_date is 2026-02-20. 2024 windows do not overlap the listed corporate-action candidate dates in the checked symbol profiles.

- 삼성화재 profile: 2024 data available; corporate-action candidate dates are historical 1999/2000 events, not the 2024 window. fileciteturn742file0
- DB손해보험 profile: 2024 data available; corporate-action candidate date is 1999-07-20, not the 2024 window. fileciteturn744file0turn743file0
- 삼성생명 profile: no corporate-action candidate dates. fileciteturn745file0
- 흥국화재 profile: corporate-action candidate dates are pre-2012, not the 2024 window. fileciteturn752file0turn753file0
- 롯데손해보험 profile: last corporate-action candidate date is 2019-10-25, not the 2024 window. fileciteturn747file0turn748file0

## 6. Canonical Archetype Compression Map

```text
C22_INSURANCE_RATE_CYCLE_RESERVE
  ├─ P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN
  │    ├─ 삼성화재
  │    └─ DB손해보험
  ├─ LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD
  │    └─ 삼성생명
  ├─ SMALL_INSURER_LOW_FLOAT_VALUEUP_FALSE_POSITIVE
  │    └─ 흥국화재
  └─ INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD
       └─ 롯데손해보험
```

Compression logic: C22 should not be “insurance stocks rose on Value-Up.” It should be “insurance rerating requires reserve-quality / solvency-buffer / capital-return confirmation; otherwise low-float or event-premium moves stay guarded.”

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | entry_price | MFE90 | MAE90 | MFE180 | MAE180 | current_profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R6L36-C22-000810 | 000810 | 삼성화재 | structural_success | 2024-02-27 | 293500 | 34.07 | -6.3 | 34.07 | -6.3 | current_profile_correct |
| R6L36-C22-005830 | 005830 | DB손해보험 | structural_success | 2024-02-27 | 92000 | 31.2 | -5.98 | 34.78 | -5.98 | current_profile_correct |
| R6L36-C22-032830 | 032830 | 삼성생명 | high_mae_success | 2024-02-27 | 92100 | 17.81 | -16.83 | 20.52 | -16.83 | current_profile_too_early |
| R6L36-C22-000540 | 000540 | 흥국화재 | false_positive_green | 2024-02-27 | 4795 | 5.32 | -23.36 | 5.32 | -33.26 | current_profile_false_positive |
| R6L36-C22-000400 | 000400 | 롯데손해보험 | 4B_overlay_success | 2024-02-27 | 2795 | 46.33 | -3.4 | 46.33 | -31.7 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
mixed_high_mae_case_count = 1
counterexample_count = 2
4B_case_count = 2
4C_case_count = 0
calibration_usable_case_count = 5
new_independent_case_count = 5
```

Interpretation: The positive bucket is not “all insurers.” 삼성화재 and DB손해보험 show strong 90D/180D reward with tolerable drawdown. 삼성생명 eventually works but carries high MAE, so a life-insurer duration/solvency guard is useful. 흥국화재 and 롯데손해보험 show why the global price-only guard must stay active inside C22.

## 9. Evidence Source Map

- Market-wide trigger: Korea’s 2024 Corporate Value-up Programme and follow-up incentives were public policy catalysts for low-PBR/capital-return repricing. FT reported the programme announcement on 2024-02-26, and Reuters later reported possible penalties and extra incentives around shareholder-return improvement. citeturn298391news2turn611234news1turn298391news1
- Case evidence split:
  - Positive P&C cases: policy event + sector relative strength + reserve/capital-return bridge.
  - Life-insurer mixed case: policy event + relative strength, but high MAE indicates duration/solvency sensitivity.
  - Small-insurer false positives: policy/theme price reaction without durable reserve or capital-return evidence.
  - Control-premium event case: MFE exists, but price path behaves like 4B/event premium rather than durable rerating.

## 10. Price Data Source Map

| symbol | company | shard | profile | validation |
|---|---|---|---|---|
| 000810 | 삼성화재 | `atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv` | `atlas/symbol_profiles/000/000810.json` | clean 180D 2024 window |
| 005830 | DB손해보험 | `atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv` | `atlas/symbol_profiles/005/005830.json` | clean 180D 2024 window |
| 032830 | 삼성생명 | `atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv` | `atlas/symbol_profiles/032/032830.json` | clean 180D 2024 window |
| 000540 | 흥국화재 | `atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv` | `atlas/symbol_profiles/000/000540.json` | clean 180D 2024 window |
| 000400 | 롯데손해보험 | `atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv` | `atlas/symbol_profiles/000/000400.json` | clean 180D 2024 window |

Representative price rows used for the calculations are visible in the stock-web shards: 삼성화재 2024 OHLC rows include the 2024-02-27 entry and later highs/lows; DB손해보험 rows include 2024-02-27 entry and 2024-08 peak area; 삼성생명 rows include 2024-02-27 entry and the high-MAE path; 흥국화재 rows include the February spike and subsequent drawdown; 롯데손해보험 rows include the June event peak and later collapse. fileciteturn750file0turn751file0turn756file0turn757file0turn758file0turn759file0turn754file0turn755file0turn760file0turn761file0

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | dd | dedupe | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR-000810-20240227-S2A | 000810 | Stage2-Actionable | 2024-02-27 | 293500 | 17.89 | -2.73 | 34.07 | -6.3 | 34.07 | -6.3 | 2024-06-28 | -17.66 | True | representative |
| TR-005830-20240227-S2A | 005830 | Stage2-Actionable | 2024-02-27 | 92000 | 19.57 | -0.98 | 31.2 | -5.98 | 34.78 | -5.98 | 2024-08-22 | -20.08 | True | representative |
| TR-032830-20240227-S2A | 032830 | Stage2-Actionable | 2024-02-27 | 92100 | 17.81 | -3.04 | 17.81 | -16.83 | 20.52 | -16.83 | 2024-11-18 | -14.05 | True | representative |
| TR-000540-20240227-S2A | 000540 | Stage2-Actionable | 2024-02-27 | 4795 | 5.32 | -16.79 | 5.32 | -23.36 | 5.32 | -33.26 | 2024-02-29 | -36.63 | True | representative |
| TR-000400-20240227-S2A | 000400 | Stage2-Actionable | 2024-02-27 | 2795 | 29.87 | -3.4 | 46.33 | -3.4 | 46.33 | -31.7 | 2024-06-26 | -53.32 | True | representative |
| TR-000810-20240516-GREEN-COMP | 000810 | Stage3-Green-label-comparison | 2024-05-16 | 370000 | 2.7 | -10.95 | 6.35 | -12.43 | 17.57 | -12.43 | 2024-12-03 | -16.67 | False | label_comparison_only |
| TR-005830-20240516-GREEN-COMP | 005830 | Stage3-Green-label-comparison | 2024-05-16 | 111500 | 3.5 | -8.97 | 11.21 | -8.97 | 11.21 | -8.97 | 2024-08-22 | -20.08 | False | label_comparison_only |
| TR-032830-20240305-GREEN-COMP | 032830 | Stage3-Yellow-label-comparison | 2024-03-05 | 104500 | 3.83 | -25.36 | 3.83 | -25.36 | 6.22 | -25.36 | 2024-11-18 | -14.05 | False | label_comparison_only |
| TR-005830-20240821-4B | 005830 | 4B-overlay | 2024-08-21 | 123200 | 0.65 | -13.23 | 0.65 | -17.45 | 0.65 | -18.75 | 2024-08-22 | -20.08 | False | 4B_overlay_only |
| TR-000400-20240626-4B | 000400 | 4B-overlay | 2024-06-26 | 4000 | 2.25 | -37.38 | 2.25 | -39.75 | 2.25 | -54.65 | 2024-06-26 | -53.32 | False | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative aggregate triggers only

| trigger_id | symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | dd |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR-000810-20240227-S2A | 000810 | 2024-02-27 | 293500 | 17.89 | -2.73 | 34.07 | -6.3 | 34.07 | -6.3 | 2024-06-28 | -17.66 |
| TR-005830-20240227-S2A | 005830 | 2024-02-27 | 92000 | 19.57 | -0.98 | 31.2 | -5.98 | 34.78 | -5.98 | 2024-08-22 | -20.08 |
| TR-032830-20240227-S2A | 032830 | 2024-02-27 | 92100 | 17.81 | -3.04 | 17.81 | -16.83 | 20.52 | -16.83 | 2024-11-18 | -14.05 |
| TR-000540-20240227-S2A | 000540 | 2024-02-27 | 4795 | 5.32 | -16.79 | 5.32 | -23.36 | 5.32 | -33.26 | 2024-02-29 | -36.63 |
| TR-000400-20240227-S2A | 000400 | 2024-02-27 | 2795 | 29.87 | -3.4 | 46.33 | -3.4 | 46.33 | -31.7 | 2024-06-26 | -53.32 |

### Label-comparison / 4B overlay triggers

| trigger_id | symbol | type | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | dd | role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TR-000810-20240516-GREEN-COMP | 000810 | Stage3-Green-label-comparison | 2024-05-16 | 370000 | 2.7 | -10.95 | 6.35 | -12.43 | 17.57 | -12.43 | 2024-12-03 | -16.67 | label_comparison_only |
| TR-005830-20240516-GREEN-COMP | 005830 | Stage3-Green-label-comparison | 2024-05-16 | 111500 | 3.5 | -8.97 | 11.21 | -8.97 | 11.21 | -8.97 | 2024-08-22 | -20.08 | label_comparison_only |
| TR-032830-20240305-GREEN-COMP | 032830 | Stage3-Yellow-label-comparison | 2024-03-05 | 104500 | 3.83 | -25.36 | 3.83 | -25.36 | 6.22 | -25.36 | 2024-11-18 | -14.05 | label_comparison_only |
| TR-005830-20240821-4B | 005830 | 4B-overlay | 2024-08-21 | 123200 | 0.65 | -13.23 | 0.65 | -17.45 | 0.65 | -18.75 | 2024-08-22 | -20.08 | 4B_overlay_only |
| TR-000400-20240626-4B | 000400 | 4B-overlay | 2024-06-26 | 4000 | 2.25 | -37.38 | 2.25 | -39.75 | 2.25 | -54.65 | 2024-06-26 | -53.32 | 4B_overlay_only |

## 13. Current Calibrated Profile Stress Test

| case | current profile expected behavior | actual path | verdict |
|---|---|---|---|
| 삼성화재 | Stage2-Actionable accepted; Green requires later revision/visibility | High MFE, tolerable MAE | current_profile_correct |
| DB손해보험 | Stage2-Actionable accepted; Green later | High MFE, tolerable MAE | current_profile_correct |
| 삼성생명 | Could over-promote if life duration risk ignored | Positive MFE but -16.83% MAE | current_profile_too_early |
| 흥국화재 | Policy/low-PBR/RS could appear actionable | MFE small, MAE severe | current_profile_false_positive |
| 롯데손해보험 | Event premium could be mistaken as structural | Large MFE then deep drawdown | current_profile_false_positive |

Answers to required stress-test questions:

```text
stage2_actionable_evidence_bonus: useful for P&C positives, too broad for small-insurer/event-premium cases without guard.
yellow_threshold_75: acceptable as watch-state, not as automatic positive promotion.
green_threshold_87/revision_55: should remain strict; C22 needs reserve-quality/capital-return bridge to cross Green.
price_only_blowoff_guard: strengthened by 흥국화재 and 롯데손해보험.
full_4B_non_price_requirement: strengthened; DB 4B is better with non-price/revision fatigue, 롯데 is event/control premium overlay.
hard_4C_routing: no hard 4C in this loop; kept unchanged.
```

## 14. Stage2 / Yellow / Green Comparison

```text
삼성화재 Stage3 label comparison green_lateness_ratio = 0.765
DB손해보험 Stage3 label comparison green_lateness_ratio = 0.609
삼성생명 Stage3 label comparison green_lateness_ratio = 0.656 but MAE penalty dominates
흥국화재 / 롯데손해보험 = no confirmed Stage3-Green trigger
```

Interpretation: Green confirmation can still be late in C22. The residual issue is not to loosen Green globally. The residual issue is to add a C22-specific confirmation bonus for P&C insurers where reserve-quality and capital-return evidence are present, while adding guards for life-insurer duration risk and event-premium spikes.

## 15. 4B Local vs Full-window Timing Audit

| trigger | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| TR-005830-20240821-4B | 0.975 | 0.975 | valuation_blowoff; positioning_overheat; revision_slowdown | good_full_window_4B_timing |
| TR-000400-20240626-4B | 0.930 | 0.930 | control_premium_or_event_premium; positioning_overheat; price_only | 4B_overlay_only; not positive-stage evidence |

The 4B rule is strengthened, not weakened. A local peak is not enough; it needs non-price support or event-premium classification.

## 16. 4C Protection Audit

No hard 4C thesis-break row is promoted in this loop. 롯데손해보험 and 흥국화재 have large drawdowns after peak, but the available evidence is better classified as 4B/event-premium overlay and positive-promotion guard, not hard 4C thesis-break.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = c22_insurance_valueup_confirmation_requires_reserve_or_capital_return_bridge
baseline_value = 0
tested_value = +1
proposal_type = sector_shadow_only
```

Candidate: For L6 insurance cases, policy/value-up evidence can create Stage2-Actionable watch status, but Stage3-Green should require at least one of:
1. explicit capital-return / payout / buyback / dividend policy improvement,
2. reserve-quality / K-ICS / solvency buffer confirmation,
3. confirmed earnings/revision bridge from rate/spread/reserve cycle.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Candidate sub-rules:

```text
c22_pnc_quality_capital_return_confirmation_bonus = +1 shadow
c22_life_duration_mae_guard = -1 shadow for premature Green
c22_small_insurer_event_premium_guard = -2 shadow for price-only/event-premium spikes
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible | selected | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | late_green | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0 e2r_2_1_stock_web_calibrated_proxy | global proxy | 5 | all Stage2-Actionable | 26.95 | -11.17 | 27.25 | -17.61 | 40% | 2 | too broad for C22 without reserve/capital-return sub-gates |
| P0b e2r_2_0_baseline_reference | rollback | 5 | mostly policy/RS names | 26.95 | -11.17 | 27.25 | -17.61 | 40%+ | 1 | does not solve small-insurer/event-premium false positives |
| P1 sector_specific_candidate_profile | L6 sector | 5 | P&C positives + guarded life | 27.69 | -9.7 | 29.79 | -9.7 | 0-20% | 2 | better score-return alignment |
| P2 canonical_archetype_candidate_profile | C22 canonical | 5 | 000810,005830; 032830 Yellow only | 32.64 | -6.14 | 34.43 | -6.14 | 0% | 2 | best positive/counterexample separation |
| P3 counterexample_guard_profile | C22 guard | 5 | blocks 000540/000400 positive promotion | 32.64 | -6.14 | 34.43 | -6.14 | 0% | 2 | keeps 4B overlays out of positive entry weights |

## 20. Score-Return Alignment Matrix

| symbol | before score / label | after score / label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| 000810 | 82 / Stage3-Yellow | 88 / Stage3-Green | 34.07 | -6.30 | improves positive separation |
| 005830 | 80 / Stage3-Yellow | 87 / Stage3-Green | 31.20 | -5.98 | improves positive separation |
| 032830 | 76 / Stage3-Yellow | 72 / Stage3-Yellow_guarded | 17.81 | -16.83 | avoids premature Green |
| 000540 | 66 / Stage2 watch | 54 / Blocked-positive | 5.32 | -23.36 | removes false positive |
| 000400 | 72 / Stage2 watch | 58 / 4B-overlay-only | 46.33 | -3.40 / -31.70 180D | keeps event premium out of positive weights |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN / LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD / SMALL_INSURER_LOW_FLOAT_VALUEUP_FALSE_POSITIVE / INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD | 2 | 2 | 2 | 0 | 5 | 0 | 9 | 5 | 3 | True | True | C22 now has positive P&C, high-MAE life, small-insurer false-positive, and event-premium 4B coverage; needs holdout across 2023/2025 insurance cycles. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
same_archetype_new_symbol_count: 5
same_archetype_new_trigger_family_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 4
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - life_insurer_high_mae_green_too_early
  - small_insurer_policy_theme_false_positive
  - control_premium_event_4B_not_positive_stage
new_axis_proposed:
  - c22_pnc_quality_capital_return_confirmation_bonus
  - c22_life_duration_mae_guard
  - c22_small_insurer_event_premium_guard
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- Stock-web manifest/schema fields.
- Symbol profile availability and corporate-action candidate window check.
- Actual 2024 tradable OHLC rows for entry/peak/drawdown calculations.
- 30D/90D/180D MFE/MAE research calculations.
- Positive/counterexample balance and dedupe fields.

Not validated:
- Live candidate status.
- Current recommendations.
- Broker execution.
- `stock_agent` source code behavior.
- Production scoring implementation.
- Exact analyst consensus EPS values. Score components are research proxies only.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_pnc_quality_capital_return_confirmation_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,+1,+1,"P&C insurers with reserve quality + explicit capital-return bridge had high MFE and tolerable MAE","selected positives avg MFE90 32.64 / avg MAE90 -6.14","TR-000810-20240227-S2A|TR-005830-20240227-S2A",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_life_duration_mae_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-1,-1,"Life insurers can show positive MFE but high MAE without K-ICS/duration buffer confirmation","Samsung Life +20.52 MFE180 but -16.83 MAE90/180","TR-032830-20240227-S2A|TR-032830-20240305-GREEN-COMP",2,1,1,low,canonical_shadow_only,"guard Green, do not block Yellow"
shadow_weight,c22_small_insurer_event_premium_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,-2,-2,"Small insurer price-only or event-premium spikes produced large drawdowns after peak","Heungkuk MAE180 -33.26; Lotte drawdown after peak -53.32","TR-000540-20240227-S2A|TR-000400-20240227-S2A|TR-000400-20240626-4B",3,2,2,medium,canonical_shadow_only,"strengthens price-only blowoff and non-price 4B guard"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R6L36-C22-000810", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR-000810-20240227-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_score_return_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Value-Up 정책 노출만이 아니라 손보/P&C의 준비금 안정성, 자본환원 기대, ROE/PBR 리레이팅이 동시에 닫힌 positive."}
{"row_type": "case", "case_id": "R6L36-C22-005830", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "TR-005830-20240227-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_score_return_aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "손보 업종 내 자본효율·주주환원·준비금 신뢰가 함께 작동한 사례. 4B는 가격만이 아니라 리레이팅 포화/포지셔닝 과열 overlay로 봐야 한다."}
{"row_type": "case", "case_id": "R6L36-C22-032830", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD", "case_type": "high_mae_success", "positive_or_counterexample": "mixed", "best_trigger": "TR-032830-20240227-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "return_positive_but_mae_penalty", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "결과적으로 상승했지만 생보 duration/금리·준비금 민감도가 높은 MAE를 만들었다. Green 승격에는 K-ICS/준비금 buffer 확인이 더 필요."}
{"row_type": "case", "case_id": "R6L36-C22-000540", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_LOW_FLOAT_VALUEUP_FALSE_POSITIVE", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "TR-000540-20240227-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "policy_theme_not_structural", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "정책·저PBR 테마와 단기 급등만으로 Stage3를 만들면 실패한다. 준비금/자본환원/ROE bridge가 닫히지 않았다."}
{"row_type": "case", "case_id": "R6L36-C22-000400", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "TR-000400-20240227-S2A", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "event_premium_not_structural_rerating", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "M&A/control-premium 기대가 MFE를 크게 만들었지만 이후 붕괴가 커서 positive entry가 아니라 4B/event overlay로 분리해야 한다."}
{"row_type": "trigger", "trigger_id": "TR-000810-20240227-S2A", "case_id": "R6L36-C22-000810", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 293500, "evidence_available_at_that_date": "Korea Corporate Value-up Programme / low-PBR capital-return policy became public; insurance sector repricing candidate identified. Company-level reserve/capital-return confirmation varies by case.", "evidence_source": "public_policy_event_plus_case_specific_historical_evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.89, "MFE_90D_pct": 34.07, "MFE_180D_pct": 34.07, "MFE_1Y_pct": 48.21, "MFE_2Y_pct": 110.56, "MAE_30D_pct": -2.73, "MAE_90D_pct": -6.3, "MAE_180D_pct": -6.3, "MAE_1Y_pct": -6.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-000810-20240227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-005830-20240227-S2A", "case_id": "R6L36-C22-005830", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 92000, "evidence_available_at_that_date": "Korea Corporate Value-up Programme / low-PBR capital-return policy became public; insurance sector repricing candidate identified. Company-level reserve/capital-return confirmation varies by case.", "evidence_source": "public_policy_event_plus_case_specific_historical_evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 19.57, "MFE_90D_pct": 31.2, "MFE_180D_pct": 34.78, "MFE_1Y_pct": 34.78, "MFE_2Y_pct": 109.02, "MAE_30D_pct": -0.98, "MAE_90D_pct": -5.98, "MAE_180D_pct": -5.98, "MAE_1Y_pct": -5.98, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -20.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-005830-20240227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-032830-20240227-S2A", "case_id": "R6L36-C22-032830", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 92100, "evidence_available_at_that_date": "Korea Corporate Value-up Programme / low-PBR capital-return policy became public; insurance sector repricing candidate identified. Company-level reserve/capital-return confirmation varies by case.", "evidence_source": "public_policy_event_plus_case_specific_historical_evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 17.81, "MFE_90D_pct": 17.81, "MFE_180D_pct": 20.52, "MFE_1Y_pct": 20.52, "MFE_2Y_pct": 137.78, "MAE_30D_pct": -3.04, "MAE_90D_pct": -16.83, "MAE_180D_pct": -16.83, "MAE_1Y_pct": -16.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-18", "peak_price": 111000, "drawdown_after_peak_pct": -14.05, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-032830-20240227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-000540-20240227-S2A", "case_id": "R6L36-C22-000540", "symbol": "000540", "company_name": "흥국화재", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "SMALL_INSURER_LOW_FLOAT_VALUEUP_FALSE_POSITIVE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 4795, "evidence_available_at_that_date": "Korea Corporate Value-up Programme / low-PBR capital-return policy became public; insurance sector repricing candidate identified. Company-level reserve/capital-return confirmation varies by case.", "evidence_source": "public_policy_event_plus_case_specific_historical_evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000540/2024.csv", "profile_path": "atlas/symbol_profiles/000/000540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 5.32, "MFE_90D_pct": 5.32, "MFE_180D_pct": 5.32, "MFE_1Y_pct": 23.05, "MFE_2Y_pct": 20.13, "MAE_30D_pct": -16.79, "MAE_90D_pct": -23.36, "MAE_180D_pct": -33.26, "MAE_1Y_pct": -38.89, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-29", "peak_price": 5050, "drawdown_after_peak_pct": -36.63, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-000540-20240227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-000400-20240227-S2A", "case_id": "R6L36-C22-000400", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-26", "entry_date": "2024-02-27", "entry_price": 2795, "evidence_available_at_that_date": "Korea Corporate Value-up Programme / low-PBR capital-return policy became public; insurance sector repricing candidate identified. Company-level reserve/capital-return confirmation varies by case.", "evidence_source": "public_policy_event_plus_case_specific_historical_evidence", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 29.87, "MFE_90D_pct": 46.33, "MFE_180D_pct": 46.33, "MFE_1Y_pct": 46.33, "MFE_2Y_pct": -9.66, "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MAE_180D_pct": -31.7, "MAE_1Y_pct": -35.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090, "drawdown_after_peak_pct": -53.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium_4B_then_thesis_decay", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-000400-20240227", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "TR-000810-20240516-GREEN-COMP", "case_id": "R6L36-C22-000810", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green-label-comparison", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 370000, "evidence_available_at_that_date": "Label comparison / overlay trigger selected after historical confirmation or risk overlay evidence became visible.", "evidence_source": "historical_public_context_and_stock_web_price_path", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.7, "MFE_90D_pct": 6.35, "MFE_180D_pct": 17.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -10.95, "MAE_90D_pct": -12.43, "MAE_180D_pct": -12.43, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 435000, "drawdown_after_peak_pct": -16.67, "green_lateness_ratio": 0.765, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_but_still_positive", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-000810-20240516", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR-005830-20240516-GREEN-COMP", "case_id": "R6L36-C22-005830", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green-label-comparison", "trigger_date": "2024-05-16", "entry_date": "2024-05-16", "entry_price": 111500, "evidence_available_at_that_date": "Label comparison / overlay trigger selected after historical confirmation or risk overlay evidence became visible.", "evidence_source": "historical_public_context_and_stock_web_price_path", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.5, "MFE_90D_pct": 11.21, "MFE_180D_pct": 11.21, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.97, "MAE_90D_pct": -8.97, "MAE_180D_pct": -8.97, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -20.08, "green_lateness_ratio": 0.609, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_late_but_valid", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-005830-20240516", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR-032830-20240305-GREEN-COMP", "case_id": "R6L36-C22-032830", "symbol": "032830", "company_name": "삼성생명", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "LIFE_INSURANCE_VALUEUP_DURATION_MAE_GUARD", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Yellow-label-comparison", "trigger_date": "2024-03-05", "entry_date": "2024-03-05", "entry_price": 104500, "evidence_available_at_that_date": "Label comparison / overlay trigger selected after historical confirmation or risk overlay evidence became visible.", "evidence_source": "historical_public_context_and_stock_web_price_path", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["relative_strength", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/032/032830/2024.csv", "profile_path": "atlas/symbol_profiles/032/032830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 3.83, "MFE_90D_pct": 3.83, "MFE_180D_pct": 6.22, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -25.36, "MAE_90D_pct": -25.36, "MAE_180D_pct": -25.36, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-11-18", "peak_price": 111000, "drawdown_after_peak_pct": -14.05, "green_lateness_ratio": 0.656, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": null, "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_too_early_high_mae", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-032830-20240305", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR-005830-20240821-4B", "case_id": "R6L36-C22-005830", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "P_AND_C_INSURANCE_VALUEUP_RESERVE_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "4B-overlay", "trigger_date": "2024-08-21", "entry_date": "2024-08-21", "entry_price": 123200, "evidence_available_at_that_date": "Label comparison / overlay trigger selected after historical confirmation or risk overlay evidence became visible.", "evidence_source": "historical_public_context_and_stock_web_price_path", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.65, "MFE_90D_pct": 0.65, "MFE_180D_pct": 0.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.23, "MAE_90D_pct": -17.45, "MAE_180D_pct": -18.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-22", "peak_price": 124000, "drawdown_after_peak_pct": -20.08, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.975, "four_b_full_window_peak_proximity": 0.975, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-005830-20240821", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "TR-000400-20240626-4B", "case_id": "R6L36-C22-000400", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_CONTROL_PREMIUM_EVENT_4B_GUARD", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_reserve_capital_return_cycle", "loop_objective": "green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "4B-overlay", "trigger_date": "2024-06-26", "entry_date": "2024-06-26", "entry_price": 4000, "evidence_available_at_that_date": "Label comparison / overlay trigger selected after historical confirmation or risk overlay evidence became visible.", "evidence_source": "historical_public_context_and_stock_web_price_path", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "positioning_overheat", "price_only"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 2.25, "MFE_90D_pct": 2.25, "MFE_180D_pct": 2.25, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.38, "MAE_90D_pct": -39.75, "MAE_180D_pct": -54.65, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-26", "peak_price": 4090, "drawdown_after_peak_pct": -53.32, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.93, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat", "price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "event_premium_4B_then_thesis_decay", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG-000400-20240626", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": null, "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L36-C22-000810", "trigger_id": "TR-000810-20240227-S2A", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 13, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 14, "k_ics_buffer_score": 9, "roe_pbr_capital_return_score": 12, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 13, "revision_score": 16, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 13, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 16, "k_ics_buffer_score": 9, "roe_pbr_capital_return_score": 16, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": 0}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "reserve_quality_score"], "component_delta_explanation": "P&C insurer with explicit reserve-quality/capital-return bridge gets C22 confirmation bonus; not a global threshold change.", "MFE_90D_pct": 34.07, "MAE_90D_pct": -6.3, "score_return_alignment_label": "positive_score_return_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L36-C22-005830", "trigger_id": "TR-005830-20240227-S2A", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 13, "k_ics_buffer_score": 8, "roe_pbr_capital_return_score": 12, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": 0}, "weighted_score_before": 80, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 15, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 15, "k_ics_buffer_score": 8, "roe_pbr_capital_return_score": 16, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": 0}, "weighted_score_after": 87, "stage_label_after": "Stage3-Green", "changed_components": ["roe_pbr_capital_return_score", "reserve_quality_score"], "component_delta_explanation": "P&C insurer with explicit reserve-quality/capital-return bridge gets C22 confirmation bonus; not a global threshold change.", "MFE_90D_pct": 31.2, "MAE_90D_pct": -5.98, "score_return_alignment_label": "positive_score_return_aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L36-C22-032830", "trigger_id": "TR-032830-20240227-S2A", "symbol": "032830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 6, "k_ics_buffer_score": 5, "roe_pbr_capital_return_score": 10, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": -10}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 10, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 11, "execution_risk_score": -8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 6, "k_ics_buffer_score": 5, "roe_pbr_capital_return_score": 10, "event_premium_score": 0, "positioning_overheat_score": 0, "life_duration_sensitivity_risk": -14}, "weighted_score_after": 72, "stage_label_after": "Stage3-Yellow_guarded", "changed_components": ["life_duration_sensitivity_risk"], "component_delta_explanation": "Life insurer duration/interest-rate sensitivity guard prevents premature Green despite positive later MFE.", "MFE_90D_pct": 17.81, "MAE_90D_pct": -16.83, "score_return_alignment_label": "return_positive_but_mae_penalty", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L36-C22-000540", "trigger_id": "TR-000540-20240227-S2A", "symbol": "000540", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 2, "k_ics_buffer_score": 1, "roe_pbr_capital_return_score": 3, "event_premium_score": 0, "positioning_overheat_score": -8, "life_duration_sensitivity_risk": 0}, "weighted_score_before": 66, "stage_label_before": "Stage2-Actionable_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 3, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 8, "execution_risk_score": -14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 2, "k_ics_buffer_score": 1, "roe_pbr_capital_return_score": 3, "event_premium_score": 0, "positioning_overheat_score": -12, "life_duration_sensitivity_risk": 0}, "weighted_score_after": 54, "stage_label_after": "Blocked-positive", "changed_components": ["event_premium_score", "positioning_overheat_score"], "component_delta_explanation": "Small-insurer or control-premium/event-price spike cannot promote positive Stage2/Stage3 without reserve/capital-return confirmation.", "MFE_90D_pct": 5.32, "MAE_90D_pct": -23.36, "score_return_alignment_label": "policy_theme_not_structural", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L36-C22-000400", "trigger_id": "TR-000400-20240227-S2A", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -15, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 2, "k_ics_buffer_score": 1, "roe_pbr_capital_return_score": 0, "event_premium_score": 18, "positioning_overheat_score": -10, "life_duration_sensitivity_risk": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 2, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 12, "execution_risk_score": -15, "legal_or_contract_risk_score": -4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 2, "k_ics_buffer_score": 1, "roe_pbr_capital_return_score": 0, "event_premium_score": 4, "positioning_overheat_score": -14, "life_duration_sensitivity_risk": 0}, "weighted_score_after": 58, "stage_label_after": "4B-overlay-only", "changed_components": ["event_premium_score", "positioning_overheat_score"], "component_delta_explanation": "Small-insurer or control-premium/event-price spike cannot promote positive Stage2/Stage3 without reserve/capital-return confirmation.", "MFE_90D_pct": 46.33, "MAE_90D_pct": -3.4, "score_return_alignment_label": "event_premium_not_structural_rerating", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R6", "loop": "36", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_canonical_archetype_count": 1, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["life_insurer_high_mae_green_too_early", "small_insurer_policy_theme_false_positive", "control_premium_event_4B_not_positive_stage"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R6/L6 C22 insurance rate/reserve/capital-return cycle under-covered after C21 bank value-up loop"}
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
next_round = R6 / C22 holdout validation, or R7 / C23 if moving to bio approval commercialization
suggested_holdout = 2023-2025 insurance C22 cases with explicit K-ICS / reserve / payout evidence
do_not_repeat = 2024-02-27 same-entry Value-Up trigger for these same symbols unless used for holdout with independent_evidence_weight=0
```

## 28. Source Notes

- Prompt basis: v12 user prompt. fileciteturn735file0
- Stock-web manifest and schema: raw/unadjusted marcap, tradable_raw calibration basis, max_date 2026-02-20. fileciteturn737file0turn738file0
- Existing calibrated profile axes: applied report. fileciteturn741file0
- Stock-web price/profile rows used: 삼성화재, DB손해보험, 삼성생명, 흥국화재, 롯데손해보험. fileciteturn742file0turn750file0turn751file0turn744file0turn743file0turn756file0turn757file0turn745file0turn758file0turn759file0turn752file0turn753file0turn754file0turn755file0turn747file0turn748file0turn760file0turn761file0
- Public policy event context: Korea Corporate Value-up Programme and follow-up incentives. citeturn298391news2turn611234news1turn298391news1
