# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| round | R6 |
| loop | 19 |
| large_sector_id | L6_FINANCIAL_CAPITAL_RETURN_DIGITAL |
| canonical_archetype_id | C22_INSURANCE_RATE_CYCLE_RESERVE |
| fine_archetype_id | IFRS17_RESERVE_QUALITY_CAPITAL_RETURN |
| output_format | one_standalone_markdown_file |
| production_scoring_changed | false |
| shadow_weight_only | true |
| stock_web_manifest_max_date | 2026-02-20 |


This is not live candidate research and not a `stock_agent` repository patch. It is a standalone historical calibration artifact using Songdaiki/stock-web OHLC rows as the price atlas.

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

The study tests this current profile rather than re-proving it. The residual question is narrower: in insurance, when does a sector-wide value-up / IFRS17 narrative deserve C22 positive promotion, and when is it merely beta, event premium, or local price heat?

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R6
loop = 19
large_sector_id = L6_FINANCIAL_CAPITAL_RETURN_DIGITAL
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
fine_archetype_id = IFRS17_RESERVE_QUALITY_CAPITAL_RETURN
loop_objective = coverage_gap_fill | counterexample_mining | sector_specific_rule_discovery | green_strictness_stress_test | 4B_non_price_requirement_stress_test
```

The selected gap is insurance-specific: C22 can be falsely promoted when the model treats broad sector beta, value-up headlines, or M&A premium as if they were reserve-quality and source-of-earnings confirmation.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts were used only for coverage and duplicate avoidance. The ingest summary reports 398 discovered MDs, 107 parsed result MDs, 1,940 validated trigger rows, 1,376 aggregate representative trigger rows, and 25 duplicate documents. This means a new loop must avoid schema rematerialization and add new independent signal rather than simply rewriting old trigger rows.

No `src/e2r` code was opened. No production scoring patch was written. No live scan was performed.

Novelty gate:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
new_canonical_archetype_count = 0
new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:

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

Manifest fields used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
active_like_symbol_count = 2868
inactive_or_delisted_like_symbol_count = 2546
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

All representative triggers use `tradable_raw` rows, not adjusted prices. Corporate-action candidate windows are blocked if overlapping the 180D calibration window. The historical candidate dates for the selected cases are clean in the 180D windows used here.

## 5. Historical Eligibility Gate

| symbol | company | entry_date | forward_180D_available_by_manifest | 180D corporate-action overlap | calibration_usable |
|---|---|---:|---|---|---|
| 005830 | DB손해보험 | 2023-05-15 | true | false | true |
| 000810 | 삼성화재 | 2024-02-23 | true | false | true |
| 001450 | 현대해상 | 2024-02-23 | true | false | true |
| 000400 | 롯데손해보험 | 2023-09-18 | true | false | true |

Profile checks:

```text
005830 profile: active-like, tradable rows 7762, corporate_action_candidate_dates = [1999-07-20], no overlap.
000810 profile: active-like, tradable rows 7763, corporate_action_candidate_dates = [1999-02-01, 1999-07-05, 2000-02-15], no overlap.
001450 profile: active-like, tradable rows 7761, corporate_action_candidate_dates = [2004-07-13], no overlap.
000400 profile: active-like, tradable rows 7717, corporate_action_candidate_dates = [2001-02-23, 2002-01-28, 2006-05-17, 2012-12-26, 2015-06-25, 2019-10-25], no overlap.
```

## 6. Canonical Archetype Compression Map

| observed fine route | canonical mapping | use in scoring |
|---|---|---|
| IFRS17 reserve quality + source-of-earnings bridge | C22_INSURANCE_RATE_CYCLE_RESERVE | positive promotion allowed when reserve quality is confirmed |
| Value-up / capital-return confirmation with insurer reserve strength | C22_INSURANCE_RATE_CYCLE_RESERVE | positive promotion allowed when capital-return and reserve data align |
| Sector beta without reserve-quality confirmation | C22_INSURANCE_RATE_CYCLE_RESERVE | Stage2 watch only; do not Green |
| M&A/control-premium event spike | C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP or 4B overlay | do not contaminate C22 positive scoring |
| Price-only local peak | 4B overlay only | full 4B requires non-price evidence |

## 7. Case Selection Summary

| case_id | symbol | company | role | independent? | best_trigger | reason |
|---|---|---|---|---|---|---|
| R6L19_C22_005830_DB_IFRS17_RESERVE_QUALITY_20230515 | 005830 | DB손해보험 | structural_success | true | R6L19_T001 | reserve/source-of-earnings bridge matured before formal Green would be safe |
| R6L19_C22_000810_SFMI_CAPITAL_RETURN_20240223 | 000810 | 삼성화재 | structural_success | true | R6L19_T002 | high-quality reserve + capital-return route aligned with rerating |
| R6L19_C22_001450_HYUNDAI_MARINE_RESERVE_QUALITY_GAP_20240223 | 001450 | 현대해상 | failed_rerating | true | R6L19_T003 | sector/value-up beta without sufficient reserve-quality confirmation |
| R6L19_C22_000400_LOTTE_INSURANCE_EVENT_PREMIUM_20230918 | 000400 | 롯데손해보험 | price_moved_without_evidence | true | R6L19_T004 | event/M&A premium, not C22 reserve/rate-cycle evidence |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
calibration_usable_trigger_count = 5
representative_trigger_count = 4
```

Positive cases have cleaner reserve/capital-return confirmation. Counterexamples expose two different false-positive routes: weak reserve-quality sector beta and event-premium rerating that belongs outside C22.

## 9. Evidence Source Map

| trigger_id | evidence family | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| R6L19_T001 | IFRS17 reserve/source-of-earnings bridge | public_event_or_disclosure, early_revision_signal, relative_strength | confirmed_revision, financial_visibility, low_red_team_risk | none |
| R6L19_T002 | capital-return + reserve quality | public_event_or_disclosure, policy_or_regulatory_optionality, early_revision_signal | confirmed_revision, financial_visibility, low_red_team_risk | none |
| R6L19_T003 | sector beta with reserve gap | public_event_or_disclosure, policy_or_regulatory_optionality | financial_visibility only | margin_or_backlog_slowdown |
| R6L19_T004 | event premium | public_event_or_disclosure | none | control_premium_or_event_premium, positioning_overheat |
| R6L19_T005 | local price peak overlay | none | none | price_only_local_peak, valuation_blowoff |

## 10. Price Data Source Map

| symbol | company | profile_path | main price shard |
|---|---|---|---|
| 005830 | DB손해보험 | atlas/symbol_profiles/005/005830.json | atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv |
| 000810 | 삼성화재 | atlas/symbol_profiles/000/000810.json | atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv |
| 001450 | 현대해상 | atlas/symbol_profiles/001/001450.json | atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv |
| 000400 | 롯데손해보험 | atlas/symbol_profiles/000/000400.json | atlas/ohlcv_tradable_by_symbol_year/000/000400/2023.csv and 2024.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol / company | trigger_type | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | current verdict | aggregate role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R6L19_T001 | 005830 DB손해보험 | Stage2-Actionable | 2023-05-15 | 76200 | 9.58 | 24.02 | 24.02 | -3.41 | -7.48 | current_profile_too_late | representative |
| R6L19_T002 | 000810 삼성화재 | Stage2-Actionable | 2024-02-23 | 308500 | 12.16 | 27.55 | 27.55 | -7.46 | -11.67 | current_profile_correct | representative |
| R6L19_T003 | 001450 현대해상 | Stage2-Actionable | 2024-02-23 | 34650 | 3.46 | 3.46 | 6.06 | -12.55 | -17.89 | current_profile_false_positive | representative |
| R6L19_T004 | 000400 롯데손해보험 | Stage2-Blocked | 2023-09-18 | 2390 | 35.77 | 35.77 | 68.83 | -7.95 | -7.95 | current_profile_correct | representative |
| R6L19_T005 | 000810 삼성화재 | Stage4B-Overlay | 2024-06-28 | 389000 | 1.03 | 1.03 | 11.83 | -11.31 | -16.71 | current_profile_4B_too_early | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### Representative trigger results

| case | entry | observed high used | observed low used | 90D alignment | 180D alignment |
|---|---:|---:|---:|---|---|
| DB손해보험 | 76,200 | 94,500 on 2023-09-18 | 70,500 | good after early drawdown | good, but Green may arrive late |
| 삼성화재 | 308,500 | 393,500 on 2024-06-28 | 272,500 | good, high-quality positive | good; local 4B needed caution |
| 현대해상 | 34,650 | 36,750 on 2024-07-31 | 28,450 | weak MFE, high MAE | false-positive risk |
| 롯데손해보험 | 2,390 | 4,035 on 2024-04-25 | 2,200 | event-premium MFE, not C22 | should not teach C22 positive scoring |

### Dedupe

```text
same_entry_group_id dedupe:
005830_2023-05-15_76200 -> representative
000810_2024-02-23_308500 -> representative
001450_2024-02-23_34650 -> representative
000400_2023-09-18_2390 -> representative
000810_2024-06-28_389000 -> 4B_overlay_only, not aggregate
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgement | actual result | stress verdict |
|---|---|---|---|
| DB손해보험 | Yellow or cautious Green due IFRS17 transition uncertainty | +24.02% 90D MFE after -7.48% MAE | current_profile_too_late |
| 삼성화재 | Green when reserve/capital-return quality confirmed | +27.55% 90D MFE with -11.67% MAE | current_profile_correct |
| 현대해상 | Yellow/near-Green if sector value-up beta over-credited | +3.46% 90D MFE with -17.89% MAE | current_profile_false_positive |
| 롯데손해보험 | blocked from C22 positive by price/event premium guard | +35.77% 90D MFE, but event-driven | current_profile_correct for C22 |
| 삼성화재 4B overlay | price-only local peak could be called too early | later full-window high appeared | current_profile_4B_too_early if price-only |

Answers to calibrated-axis stress questions:

```text
stage2_actionable_evidence_bonus: kept; useful for DB and Samsung, but must be paired with reserve-quality gate in C22.
stage3_yellow_total_min: kept; Hyundai shows Yellow can still be too generous when sector beta is confused with reserve confirmation.
stage3_green_total_min / revision_min: strengthened within C22; reserve/source-of-earnings confirmation should be explicit.
stage3_cross_evidence_green_buffer: kept; but cross evidence must be qualitative, not simply sector price momentum.
price_only_blowoff_blocks_positive_stage: strengthened; Lotte event MFE should not teach C22 positive promotion.
full_4b_requires_non_price_evidence: strengthened; Samsung 2024-06-28 was local price peak but not full 4B.
hard_4c_thesis_break_routes_to_4c: kept; no hard 4C sample in this loop.
```

## 14. Stage2 / Yellow / Green Comparison

DB and Samsung show that C22 can work well when early Stage2 evidence contains reserve-quality or capital-return confirmation. 현대해상 shows that sector-wide value-up beta without reserve quality is not enough. 롯데손보 shows that even large MFE can be the wrong lesson when it comes from control/event premium.

```text
green_lateness_ratio:
DB손해보험 = not_applicable; no separate confirmed Green trigger row retained.
삼성화재 = 0.406 using 343,000 as later Green-like level and 393,500 full 180D local peak.
현대해상 = not_applicable; proposed guard blocks Green.
롯데손해보험 = not_applicable; event-premium route is not C22 Green.
```

## 15. 4B Local vs Full-window Timing Audit

Samsung 2024-06-28 is the key 4B stress row.

```text
Stage2_Actionable_entry_price = 308500
Stage4B_overlay_entry_price = 389000
local_peak_price_after_Stage2 = 393500
full_observed_peak_price_after_Stage2 = 435000
four_b_local_peak_proximity = 0.947
four_b_full_window_peak_proximity = 0.636
four_b_timing_verdict = price_only_local_4B_too_early
```

This reinforces the existing global rule rather than proposing a global rewrite: price-only local peak can be a risk overlay, but not a full 4B exit unless non-price evidence appears.

## 16. 4C Protection Audit

No clean hard 4C thesis-break sample is promoted in this loop.

```text
four_c_protection_label:
DB손해보험 = thesis_break_watch_only
삼성화재 = thesis_break_watch_only
현대해상 = thesis_break_watch_only
롯데손해보험 = false_break / event-premium route
```

Next C22 work should add a hard 4C reserve-break case, preferably where loss-ratio reserve deterioration or capital adequacy damage became public before a drawdown.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
reason = R6 financial sector is broader than insurance. The observed error is not all financials; it is C22-specific confusion between insurer reserve quality, value-up beta, and event premium.
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
```

Proposed C22 shadow rule:

```text
C22 promotion requires at least one explicit reserve/source-of-earnings quality field:
- CSM/reserve quality or source-of-earnings visibility,
- capital-return policy that is supported by solvency/capital adequacy,
- recurring insurance-service result visibility,
- low accounting/trust risk.

Sector-wide value-up, price momentum, or PBR rerating alone cannot promote C22 Green.

M&A/control-premium events in insurers route to C32_GOVERNANCE_CONTROL_PREMIUM_TENDER_CAP or 4B overlay unless reserve-quality evidence independently supports C22.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | hypothesis | eligible_trigger_count | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | avg_four_b_local_peak_proximity | avg_four_b_full_window_peak_proximity | verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | Current profile with global Stock-Web calibration | 4 | 22.7 | -11.25 | 31.61 | -11.25 | 0.25 | 1 | 1 | 0.406 | 0.947 | 0.636 | Mostly correct but still over-credits sector beta in C22 |
| P0b e2r_2_0_baseline_reference | rollback | Older baseline without Stock-Web calibrated guards | 4 | 22.7 | -11.25 | 31.61 | -11.25 | 0.50 | 0 | 2 | 0.55 | 0.947 | 0.636 | Too permissive; event premium and weak reserve cases contaminate positives |
| P1 sector_specific_candidate_profile | L6 sector | Add insurance reserve-quality gate under financial/capital-return sector | 4 | 25.79 selected positives | -9.58 | 25.79 | -9.58 | 0.25 | 0 | 1 | 0.406 | 0.947 | 0.636 | Better, but sector scope still too broad |
| P2 canonical_archetype_candidate_profile | C22 | Require reserve/source-of-earnings quality + capital-return confirmation before Green | 4 | 25.79 selected positives | -9.57 | 25.79 | -9.57 | 0.00 | 0 | 1 | 0.406 | 0.947 | 0.636 | Best alignment; keeps event premium out of C22 positive scoring |
| P3 counterexample_guard_profile | C22 guard | Route event premium and price-only peaks to overlay/C32, not C22 positive | 4 | 25.79 selected positives | -9.57 | 25.79 | -9.57 | 0.00 | 1 | 0 | n/a | 0.947 | 0.636 | Strong guard; may miss early DB-style reserve inflection if too strict |


## 20. Score-Return Alignment Matrix

| group | representative cases | avg_MFE_90D_pct | avg_MAE_90D_pct | interpretation |
|---|---|---:|---:|---|
| C22 reserve/capital-return confirmed positives | DB손해보험, 삼성화재 | 25.79 | -9.57 | strong enough for C22 positive promotion if evidence is explicit |
| C22 weak/false-positive route | 현대해상, 롯데손해보험 | 19.62 | -12.92 | mixed; Lotte MFE is event premium, Hyundai is weak true C22 |
| All representative rows | 4 cases | 22.7 | -11.25 | aggregate hides the mechanism; C22 needs subtype guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | IFRS17_RESERVE_QUALITY_CAPITAL_RETURN | 2 | 2 | 1 | 0 | 4 | 0 | 5 | 4 | 2 | false | true | C22 still needs more 4C reserve-break samples and life-insurance counterexamples |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
same_archetype_new_symbol_count: 4
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4

tested_existing_calibrated_axes:
- stage3_green_revision_min
- stage3_yellow_total_min
- price_only_blowoff_blocks_positive_stage
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
- sector_beta_false_positive
- reserve_quality_gap
- event_premium_misclassification
- price_only_local_4B_too_early

new_axis_proposed:
- c22_reserve_quality_confirmation_gate
- c22_event_premium_no_green_guard
- c22_price_only_local_4b_guard

existing_axis_strengthened:
- stage3_green_revision_min within C22
- price_only_blowoff_blocks_positive_stage within insurer event-premium cases
- full_4b_requires_non_price_evidence within C22

existing_axis_weakened: null
existing_axis_kept:
- stage2_actionable_evidence_bonus
- stage3_yellow_total_min
- hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Historical trigger-level calibration only.
- Stock-Web tradable_raw OHLC rows only.
- 30D / 90D / 180D MFE/MAE.
- C22 shadow-only rule discovery.
- No production scoring mutation.
```

Non-validation scope:

```text
- No current/live recommendation.
- No 2026 live candidate scan.
- No automatic trading.
- No broker integration.
- No stock_agent src/e2r code access.
- No global scoring promotion.
- No investment advice.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_quality_confirmation_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Promote only when reserve/source-of-earnings quality is confirmed, not sector beta alone","Keeps DB/Samsung while blocking Hyundai-type weak confirmation","R6L19_T001|R6L19_T002|R6L19_T003",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_event_premium_no_green_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Route M&A/control-premium insurance spikes to C32/4B overlay unless reserve quality is separately proven","Prevents Lotte-type event MFE from contaminating C22 positive calibration","R6L19_T004",4,4,2,medium,canonical_shadow_only,"not production; event premium can still be tradable but not C22 positive"
shadow_weight,c22_price_only_local_4b_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Local price peak without non-price evidence is overlay-only","Avoids premature 4B exit when full-window peak remains ahead","R6L19_T005",1,0,0,low,overlay_shadow_only,"not production; strengthens existing full_4b_requires_non_price_evidence"

```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R6L19_C22_005830_DB_IFRS17_RESERVE_QUALITY_20230515", "symbol": "005830", "company_name": "DB손해보험", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L19_T001", "score_price_alignment": "reserve-quality and earnings bridge became tradable before formal Green; Stage2/Y-Green split still useful but C22 needs reserve-quality promotion path", "current_profile_verdict": "current_profile_too_late", "notes": "Q1 2023 IFRS17-era reserve/earnings bridge; entry uses next tradable close after the public result window.", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_RESERVE_QUALITY_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R6L19_C22_000810_SFMI_CAPITAL_RETURN_20240223", "symbol": "000810", "company_name": "삼성화재", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L19_T002", "score_price_alignment": "capital-return + high-quality reserve narrative aligned with clean 90D/180D MFE despite volatility", "current_profile_verdict": "current_profile_correct", "notes": "2024 value-up/capital-return and FY2023 result route; 4B overlay separated from positive promotion.", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_RESERVE_QUALITY_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R6L19_C22_001450_HYUNDAI_MARINE_RESERVE_QUALITY_GAP_20240223", "symbol": "001450", "company_name": "현대해상", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R6L19_T003", "score_price_alignment": "sector-wide insurance/value-up label was insufficient; reserve-quality/capital-return gap produced low MFE and high MAE", "current_profile_verdict": "current_profile_false_positive", "notes": "Same insurance macro bucket as winners, but weaker reserve/capital-return evidence did not support Green.", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_RESERVE_QUALITY_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
{"row_type": "case", "case_id": "R6L19_C22_000400_LOTTE_INSURANCE_EVENT_PREMIUM_20230918", "symbol": "000400", "company_name": "롯데손해보험", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L19_T004", "score_price_alignment": "large MFE came from M&A/event premium, not C22 reserve/rate-cycle quality; should be C32/4B overlay, not C22 positive promotion", "current_profile_verdict": "current_profile_correct", "notes": "Event-premium spike is useful as an anti-misclassification counterexample.", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_RESERVE_QUALITY_CAPITAL_RETURN", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "price_source": "Songdaiki/stock-web"}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R6L19_T001", "case_id": "R6L19_C22_005830_DB_IFRS17_RESERVE_QUALITY_20230515", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "IFRS17_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 76200, "evidence_available_at_that_date": "Q1 2023 IFRS17-era public result window; CSM/reserve-quality and earnings visibility became analyzable, but market initially discounted uncertainty.", "evidence_source": "public earnings/disclosure window; stock-web row verification fetched from 2023 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "MFE_30D_pct": 9.58, "MFE_90D_pct": 24.02, "MFE_180D_pct": 24.02, "MFE_1Y_pct": "contaminated_or_unavailable_not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -3.41, "MAE_90D_pct": -7.48, "MAE_180D_pct": -7.48, "MAE_1Y_pct": "contaminated_or_unavailable_not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-09-18", "peak_price": 94500, "drawdown_after_peak_pct": -15.34, "green_lateness_ratio": "not_applicable: no confirmed Stage3-Green trigger row inside this loop", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_mfe_with_moderate_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "005830_2023-05-15_76200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L19_T002", "case_id": "R6L19_C22_000810_SFMI_CAPITAL_RETURN_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "VALUEUP_CAPITAL_RETURN_RESERVE_QUALITY", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 308500, "evidence_available_at_that_date": "FY2023 result/capital-return and value-up interpretation became tradable; reserve quality was viewed as higher than peers.", "evidence_source": "public result/capital-return window; stock-web row verification fetched from 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "MFE_30D_pct": 12.16, "MFE_90D_pct": 27.55, "MFE_180D_pct": 27.55, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -7.46, "MAE_90D_pct": -11.67, "MAE_180D_pct": -11.67, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-06-28", "peak_price": 393500, "drawdown_after_peak_pct": -17.66, "green_lateness_ratio": 0.406, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_quality_capital_return", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000810_2024-02-23_308500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L19_T003", "case_id": "R6L19_C22_001450_HYUNDAI_MARINE_RESERVE_QUALITY_GAP_20240223", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "VALUEUP_BETA_WITH_RESERVE_QUALITY_GAP", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve", "loop_objective": "counterexample_mining|residual_false_positive_mining|sector_specific_rule_discovery", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-22", "entry_date": "2024-02-23", "entry_price": 34650, "evidence_available_at_that_date": "Sector-wide value-up/insurance narrative was available, but reserve quality and capital-return confirmation were weaker than leaders.", "evidence_source": "public sector/value-up and result window; stock-web row verification fetched from 2024 tradable shard", "stage2_evidence_fields": ["public_event_or_disclosure", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "MFE_30D_pct": 3.46, "MFE_90D_pct": 3.46, "MFE_180D_pct": 6.06, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -12.55, "MAE_90D_pct": -17.89, "MAE_180D_pct": -17.89, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 36750, "drawdown_after_peak_pct": -14.29, "green_lateness_ratio": "not_applicable: no valid Green; proposed guard blocks promotion", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_low_mfe_high_mae", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "001450_2024-02-23_34650", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L19_T004", "case_id": "R6L19_C22_000400_LOTTE_INSURANCE_EVENT_PREMIUM_20230918", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "MNA_EVENT_PREMIUM_NOT_RESERVE_CYCLE", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve", "loop_objective": "counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Blocked", "trigger_date": "2023-09-18", "entry_date": "2023-09-18", "entry_price": 2390, "evidence_available_at_that_date": "Insurance M&A/sale event premium appeared, but C22 reserve/rate-cycle evidence was not the driver.", "evidence_source": "public event-premium window; stock-web row verification fetched from 2023/2024 tradable shards", "stage2_evidence_fields": ["public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["control_premium_or_event_premium", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2023.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "MFE_30D_pct": 35.77, "MFE_90D_pct": 35.77, "MFE_180D_pct": 68.83, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -7.95, "MAE_90D_pct": -7.95, "MAE_180D_pct": -7.95, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-04-25", "peak_price": 4035, "drawdown_after_peak_pct": -31.85, "green_lateness_ratio": "not_applicable: not a valid C22 Green; event-premium route belongs to C32/4B overlay", "four_b_local_peak_proximity": 0.515, "four_b_full_window_peak_proximity": 0.267, "four_b_timing_verdict": "price_only_local_4B_too_early_if_no_control_premium_confirmation", "four_b_evidence_type": ["control_premium_or_event_premium", "positioning_overheat"], "four_c_protection_label": "false_break", "trigger_outcome_label": "price_moved_without_c22_evidence_event_premium", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000400_2023-09-18_2390", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
{"row_type": "trigger", "trigger_id": "R6L19_T005", "case_id": "R6L19_C22_000810_SFMI_CAPITAL_RETURN_20240223", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "PRICE_ONLY_LOCAL_4B_OVERLAY", "sector": "금융·자본배분·디지털금융", "primary_archetype": "insurance_rate_cycle_reserve", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2024-06-28", "entry_date": "2024-06-28", "entry_price": 389000, "evidence_available_at_that_date": "Local price/valuation heat after rerating; no independent non-price thesis break on that date.", "evidence_source": "stock-web local peak row; used for 4B overlay timing only", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "MFE_30D_pct": 1.03, "MFE_90D_pct": 1.03, "MFE_180D_pct": 11.83, "MFE_1Y_pct": "not_required", "MFE_2Y_pct": "not_required", "MAE_30D_pct": -11.31, "MAE_90D_pct": -16.71, "MAE_180D_pct": -16.71, "MAE_1Y_pct": "not_required", "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-12-03", "peak_price": 435000, "drawdown_after_peak_pct": -17.47, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.947, "four_b_full_window_peak_proximity": 0.636, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_price_only_local_peak_not_full_4B", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000810_2024-06-28_389000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "same_symbol_new_4B_timing_overlay", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true, "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L19_C22_005830_DB_IFRS17_RESERVE_QUALITY_20230515", "trigger_id": "R6L19_T001", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 55, "relative_strength_score": 45, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 40, "execution_risk_score": 20, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 58, "relative_strength_score": 48, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 43, "execution_risk_score": 15, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 10}, "weighted_score_after": 85, "stage_label_after": "Stage3-Yellow-high / C22-watch-Green", "changed_components": ["reserve_quality_bridge_proxy", "+insurance_source_of_earnings_quality"], "component_delta_explanation": "DB should be promoted faster when reserve quality and source-of-earnings bridge are explicit, but not by lowering global Green threshold.", "MFE_90D_pct": 24.02, "MAE_90D_pct": -7.48, "score_return_alignment_label": "current_profile_too_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L19_C22_000810_SFMI_CAPITAL_RETURN_20240223", "trigger_id": "R6L19_T002", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 60, "relative_strength_score": 58, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 40, "valuation_repricing_score": 55, "execution_risk_score": 10, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 88, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 60, "relative_strength_score": 58, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 42, "valuation_repricing_score": 55, "execution_risk_score": 8, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 8}, "weighted_score_after": 90, "stage_label_after": "Stage3-Green", "changed_components": ["capital_return_confirmation", "+reserve_quality_confirmation"], "component_delta_explanation": "Leader-quality reserve/capital-return evidence remains correctly Green; no global loosening needed.", "MFE_90D_pct": 27.55, "MAE_90D_pct": -11.67, "score_return_alignment_label": "aligned", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L19_C22_001450_HYUNDAI_MARINE_RESERVE_QUALITY_GAP_20240223", "trigger_id": "R6L19_T003", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 45, "relative_strength_score": 35, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 40, "valuation_repricing_score": 35, "execution_risk_score": 35, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": 35, "relative_strength_score": 25, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": 35, "valuation_repricing_score": 25, "execution_risk_score": 50, "legal_or_contract_risk_score": "unknown_or_not_supported", "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": 20}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch / no Green", "changed_components": ["-unconfirmed_reserve_quality", "-sector_beta_only", "+reserve_gap_penalty"], "component_delta_explanation": "The false positive is not the insurance sector itself; it is treating sector/value-up beta as reserve-quality evidence.", "MFE_90D_pct": 3.46, "MAE_90D_pct": -17.89, "score_return_alignment_label": "after_profile_improves_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R6L19_C22_000400_LOTTE_INSURANCE_EVENT_PREMIUM_20230918", "trigger_id": "R6L19_T004", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 70, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 60, "execution_risk_score": 60, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_before": 64, "stage_label_before": "Stage2-Blocked / event-premium", "raw_component_scores_after": {"contract_score": "unknown_or_not_supported", "backlog_visibility_score": "unknown_or_not_supported", "margin_bridge_score": "unknown_or_not_supported", "revision_score": "unknown_or_not_supported", "relative_strength_score": 70, "customer_quality_score": "unknown_or_not_supported", "policy_or_regulatory_score": "unknown_or_not_supported", "valuation_repricing_score": 30, "execution_risk_score": 70, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": "unknown_or_not_supported", "accounting_trust_risk_score": "unknown_or_not_supported"}, "weighted_score_after": 58, "stage_label_after": "C32/Event or 4B-overlay-only", "changed_components": ["event_premium_route", "-C22_promotion"], "component_delta_explanation": "Large MFE is real, but it should not teach C22 positive scoring because the driver is control/event premium.", "MFE_90D_pct": 35.77, "MAE_90D_pct": -7.95, "score_return_alignment_label": "blocked_from_C22_correctly", "current_profile_verdict": "current_profile_correct"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_quality_confirmation_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Promote only when reserve/source-of-earnings quality is confirmed, not sector beta alone","Keeps DB/Samsung while blocking Hyundai-type weak confirmation","R6L19_T001|R6L19_T002|R6L19_T003",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_event_premium_no_green_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Route M&A/control-premium insurance spikes to C32/4B overlay unless reserve quality is separately proven","Prevents Lotte-type event MFE from contaminating C22 positive calibration","R6L19_T004",4,4,2,medium,canonical_shadow_only,"not production; event premium can still be tradable but not C22 positive"
shadow_weight,c22_price_only_local_4b_guard,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Local price peak without non-price evidence is overlay-only","Avoids premature 4B exit when full-window peak remains ahead","R6L19_T005",1,0,0,low,overlay_shadow_only,"not production; strengthens existing full_4b_requires_non_price_evidence"

```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "19", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "stage3_yellow_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["sector_beta_false_positive", "reserve_quality_gap", "event_premium_misclassification", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R6/C22 보험 rate/reserve cycle에서 reserve-quality/capital-return confirmation과 event premium false positive 분리 부족"}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"future_C22_hard_4C_reserve_break_needed","symbol":"000000","large_sector_id":"L6_FINANCIAL_CAPITAL_RETURN_DIGITAL","canonical_archetype_id":"C22_INSURANCE_RATE_CYCLE_RESERVE","reason":"No clean hard 4C reserve-break case added in this loop; next C22 loop should target reserve adequacy/capital adequacy thesis break.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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

Recommended next loop:

```text
next_round = R8
large_sector_id = L8_PLATFORM_CONTENT_SW_SECURITY
canonical_archetype_id = C28_SOFTWARE_SECURITY_CONTRACT_RETENTION
reason = undercovered non-manufacturing software/security retention archetype; useful counterexamples likely exist where headline cyber/security narrative lacks renewal/retention proof.
```

Alternative next loop:

```text
next_round = R6
canonical_archetype_id = C22_INSURANCE_RATE_CYCLE_RESERVE
objective = hard_4C_thesis_break_timing_test
reason = this loop has no clean hard 4C reserve-break case.
```

## 28. Source Notes

Stock-Web and research-artifact files inspected:

```text
stock_agent artifact:
- reports/e2r_calibration/ingest_summary.md

stock-web price atlas:
- atlas/manifest.json
- atlas/symbol_profiles/005/005830.json
- atlas/symbol_profiles/000/000810.json
- atlas/symbol_profiles/001/001450.json
- atlas/symbol_profiles/000/000400.json
- atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/001/001450/2024.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000400/2023.csv
- atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv
```

Key row anchors used for backtest calculations:

```text
DB손해보험: 2023-05-15 close 76,200; observed highs 83,500 and 94,500; observed lows 73,600 and 70,500.
삼성화재: 2024-02-23 close 308,500; observed high 393,500 on 2024-06-28; local 4B overlay close 389,000; later observed high 435,000 on 2024-12-03 for full-window stress.
현대해상: 2024-02-23 close 34,650; observed high 36,750; observed low 28,450.
롯데손해보험: 2023-09-18 close 2,390; observed local high 3,245; later event high 4,035; observed low 2,200.
```
