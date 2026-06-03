# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
scheduled_round = R4
scheduled_loop = 72
completed_round = R4
completed_loop = 72
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION
output_file = e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This loop adds **4** new independent cases, **2** counterexamples, and **2** current-profile residual errors for **R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD**.

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

This loop does not re-prove the global Stage2 bonus or the global price-only blowoff guard. The residual tested here is narrower: **inside C17 chemical commodity spread cycles, commodity/spread headlines should not promote Stage3 unless the spread appears in company-level margin, revision, or cash-flow evidence.**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 72 |
| round_schedule_status | valid |
| round_sector_consistency | pass |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| fine_archetype_id | CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION |
| loop_objective | sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill |

R4 maps to L4 materials/spread/resource. C17 is selected because the previous R4 loop already covered C15 copper-positioning beta; this run shifts to chemical commodity margin-spread evidence and avoids reusing the C15 copper symbol set.

## 3. Previous Coverage / Duplicate Avoidance Check

No stock_agent source code was opened. The current conversation state completed R3/Loop72, so the next sequential slot is R4/Loop72. Prior local residual artifacts show R4/Loop71 used C15 copper spread/positioning symbols. This file therefore selects C17 and a different symbol/evidence family.

```text
scheduled_round = R4
scheduled_loop = 72
previous_completed_round = R3
previous_completed_loop = 72
previous_R4_loop_71_canonical = C15_MATERIAL_SPREAD_SUPERCYCLE
hard_duplicate_policy = canonical_archetype_id + symbol + trigger_type + entry_date
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
```

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "source_name": "FinanceData/marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "tradable_row_count": 14354401,
  "raw_row_count": 15214118,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap"
}
```

Price-source validation status: `usable_for_historical_calibration`. The stock-web manifest reports raw/unadjusted OHLC, a max date of 2026-02-20, and calibration-safe tradable shards with non-tradable/invalid rows removed.

## 5. Historical Eligibility Gate

| symbol | company | profile_path | profile/corporate-action status | 180D calibration window |
|---|---|---|---|---|
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | corporate_action_candidate_count=1, candidate=2001-01-16, clean_2020_2021_window | clean_180D_window |
| 010060 | OCI홀딩스 | atlas/symbol_profiles/010/010060.json | corporate_action_candidates=1999-04-16|2001-05-18|2023-05-30|2023-10-13; clean_2021_180D_window | clean_180D_window |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | corporate_action_candidate=2023-02-13; clean_2021_180D_window | clean_180D_window |
| 006650 | 대한유화 | atlas/symbol_profiles/006/006650.json | corporate_action_candidate=2010-07-13; clean_2021_180D_window | clean_180D_window |

All representative rows have entry dates before the stock-web manifest max date and have 180 trading-day windows available. OCI has 2023 corporate-action candidates, so 2021 calibration windows are unaffected but later 1Y/2Y fields are not used for production calibration in this file.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION
positive path:
  chemical/polysilicon/NB-latex spread expansion
  + reported or strongly inferable company-level margin bridge
  + revision/operating leverage confirmation
  => Stage2-Actionable / possible Stage3-Yellow or Green candidate
counterexample path:
  commodity or reopening spread beta
  + stock relative strength only
  + no company-level margin or revision bridge
  => Stage2-watch or 4B-watch, not Stage3
```

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | is_new_independent_case | independent_evidence_weight | current_profile_verdict |
|---|---|---|---|---|---:|---:|---|
| CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE | 011780 | 금호석유화학 | structural_success | positive | true | 1.0 | current_profile_correct |
| CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL | 010060 | OCI홀딩스 | structural_success | positive | true | 1.0 | current_profile_correct |
| CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3 | 011170 | 롯데케미칼 | false_positive_green | counterexample | true | 1.0 | current_profile_false_positive |
| CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION | 006650 | 대한유화 | 4B_overlay_success | counterexample | true | 1.0 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

```text
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
representative_trigger_count = 4
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 1
```

The positive rows are not generic chemical beta. They require visible spread-to-margin bridge. The counterexamples deliberately keep the commodity/reopening narrative but remove the company-level margin bridge, exposing where the current profile can still be too early.

## 9. Evidence Source Map

| evidence family | used for | source note | scoring usage |
|---|---|---|---|
| NB latex / synthetic rubber spread capture | positive C17 Stage2/Stage3 | 2020 earnings and spread-cycle narrative for 금호석유화학 | promotion allowed when margin bridge is visible |
| Polysilicon spread rebound | positive C17 Stage2/Stage3 | 2021 polysilicon spread and operating-leverage narrative for OCI | promotion allowed when spread capture is visible |
| Reopening / naphtha / commodity beta | counterexample | 2021 chemical reopening and spread optimism for 롯데케미칼 / 대한유화 | watch-only unless margin bridge confirmed |
| Local peak / valuation / positioning overheat | 4B overlay | 2021 post-surge windows for 금호석유화학 and 대한유화 | risk overlay, not positive promotion |
| Stock-web OHLC | all MFE/MAE/peak/drawdown | tradable_raw shards under atlas/ohlcv_tradable_by_symbol_year | quantitative calibration |

## 10. Price Data Source Map

| symbol | shard | profile | entry rows used | profile notes |
|---|---|---|---|---|
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv | atlas/symbol_profiles/011/011780.json | 2020-08-07 | corporate_action_candidate_count=1, candidate=2001-01-16, clean_2020_2021_window |
| 010060 | atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv | atlas/symbol_profiles/010/010060.json | 2021-02-10 | corporate_action_candidates=1999-04-16|2001-05-18|2023-05-30|2023-10-13; clean_2021_180D_window |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | 2021-02-23 | corporate_action_candidate=2023-02-13; clean_2021_180D_window |
| 006650 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | 2021-02-10 | corporate_action_candidate=2010-07-13; clean_2021_180D_window |
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | 2021-05-07 | overlay row |
| 006650 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | 2021-02-16 | overlay row |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | peak_date | peak_price | drawdown_after_peak_pct | current_profile_verdict | aggregate_group_role |
|---|---|---|---|---|---|---:|---:|---:|---|---:|---:|---|---|
| T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE | 011780 | 금호석유화학 | Stage2-Actionable | 2020-08-07 | 2020-08-07 | 94200 | 66.14 | -6.58 | 2021-05-06 | 298500 | -32.16 | current_profile_correct | representative |
| T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING | 010060 | OCI홀딩스 | Stage2-Actionable | 2021-02-10 | 2021-02-10 | 114000 | 21.49 | -5.26 | 2021-10-01 | 169000 | -21.3 | current_profile_correct | representative |
| T011170_STAGE2_20210223_REOPENING_SPREAD_BETA | 011170 | 롯데케미칼 | Stage2-PriceOnlyWatch | 2021-02-23 | 2021-02-23 | 326000 | 3.68 | -21.78 | 2021-03-02 | 338000 | -31.07 | current_profile_false_positive | representative |
| T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF | 006650 | 대한유화 | Stage2-PriceOnlyWatch | 2021-02-10 | 2021-02-10 | 373500 | 8.57 | -21.82 | 2021-02-17 | 405500 | -49.94 | current_profile_false_positive | representative |
| T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY | 011780 | 금호석유화학 | Stage4B-Overlay | 2021-05-07 | 2021-05-07 | 281000 | 6.23 | -27.94 | 2021-05-07 | 298500 | -32.16 | current_profile_4B_too_late | 4B_overlay_only |
| T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY | 006650 | 대한유화 | Stage4B-Overlay | 2021-02-16 | 2021-02-16 | 393500 | 3.05 | -25.79 | 2021-02-17 | 405500 | -49.94 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | MFE_1Y | MAE_1Y | peak_date | peak_price | drawdown_after_peak | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE | 94200 | 22.08 | -6.58 | 66.14 | -6.58 | 216.88 | -6.58 | 216.88 | -31.95 | 2021-05-06 | 298500 | -32.16 | true | true |
| T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING | 114000 | 21.49 | -9.65 | 21.49 | -5.26 | 48.25 | -11.4 | 48.25 | -11.4 | 2021-10-01 | 169000 | -21.3 | true | true |
| T011170_STAGE2_20210223_REOPENING_SPREAD_BETA | 326000 | 3.68 | -11.04 | 3.68 | -21.78 | 3.68 | -28.53 | 3.68 | -31.9 | 2021-03-02 | 338000 | -31.07 | true | true |
| T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF | 373500 | 8.57 | -16.06 | 8.57 | -21.82 | 8.57 | -45.65 | 8.57 | -45.65 | 2021-02-17 | 405500 | -49.94 | true | true |
| T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY | 281000 | 6.23 | -20.82 | 6.23 | -27.94 | 6.23 | -31.85 | None | None | 2021-05-07 | 298500 | -32.16 | true | true |
| T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY | 393500 | 3.05 | -20.33 | 3.05 | -25.79 | 3.05 | -48.41 | None | None | 2021-02-17 | 405500 | -49.94 | true | true |

## 13. Current Calibrated Profile Stress Test

1. The current profile is correct when it lets 금호석유화학 and OCI enter as positive C17 rows, because the evidence is not just spread price. It is spread-to-margin and revision visibility.
2. The current profile can still be too early for 롯데케미칼 and 대한유화 if relative strength and broad reopening spread optimism are treated as if they were company-specific margin bridge.
3. Stage2 actionable bonus is kept, but in C17 it should apply only after margin bridge evidence, not at commodity headline stage.
4. Yellow 75 and Green 87/55 are kept. No threshold relaxation is proposed.
5. Price-only blowoff guard is strengthened.
6. Full 4B non-price requirement is kept; in C17, margin/revision slowdown after a spread beta surge should count as non-price 4B-watch evidence.
7. Hard 4C routing is kept, but C17 should allow earlier 4C-watch when spread thesis evidence breaks before price fully collapses.

```text
existing_axis_tested = stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | hard_4c_thesis_break_routes_to_4c
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
existing_axis_weakened = null
existing_axis_kept = stage3_yellow_total_min | stage3_green_total_min | stage3_green_revision_min
new_axis_proposed = C17_margin_bridge_required_for_stage3
```

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | proposed Yellow/Green handling | green_lateness_ratio | interpretation |
|---|---:|---|---:|---|
| 011780 금호석유화학 | 94,200 | Stage3 can be promoted after margin/revision bridge | 0.58 | Green late but acceptable because MFE remained very large |
| 010060 OCI | 114,000 | Stage3-Yellow possible after polysilicon margin bridge | 0.41 | Yellow/Green confirmation captures some but not all upside |
| 011170 롯데케미칼 | 326,000 | Stage2-watch only | n/a | generic reopening beta had low MFE and high MAE |
| 006650 대한유화 | 373,500 | Stage2-watch / 4B-watch | n/a | early upside was small versus later drawdown |

## 15. 4B Local vs Full-window Timing Audit

| 4B trigger | symbol | Stage2 entry | 4B entry | peak | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---:|---:|---:|---|
| T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY | 011780 | 94,200 | 281,000 | 298,500 | 0.91 | 0.91 | good_full_window_4B_timing |
| T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY | 006650 | 373,500 | 393,500 | 405,500 | 0.62 | 0.62 | good_early_4B_watch_before_full_drawdown |

The C17 lesson is asymmetrical. A structural spread-to-margin success can run far beyond the first signal, but a commodity-beta surge without margin bridge should be treated as 4B-watch near local peak rather than as fresh Stage3 promotion.

## 16. 4C Protection Audit

Hard 4C is not assigned to the positive 011780/OCI Stage2 entries. For the counterexamples, the protection label is `thesis_break_watch_only` or `hard_4c_late_if_waiting_for_price_break_only`. 대한유화 is the cleanest C17 4C-watch example: the price had only brief MFE but the later 180D MAE approached -46%, so waiting for price-only collapse would be too late.

```text
four_c_protection_label_011170 = thesis_break_watch_only
four_c_protection_label_006650 = hard_4c_late_if_waiting_for_price_break_only
hard_4c_success = not_quantified_as_exit_signal
4C_watch_rule = margin_bridge_absent + spread_beta_reversal + post-peak drawdown risk
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
rule = In L4 materials/spread/resource, commodity spread or reopening beta cannot by itself promote Stage3; require company-level spread capture, margin bridge, revision signal, or FCF route.
backtest_effect = keeps 011780/010060 positive rows, blocks 011170/006650 false Stage3 promotion.
confidence = medium
production_status = shadow_only
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
rule = C17 positive promotion requires commodity spread -> company margin/revision bridge; commodity beta without bridge is Stage2-watch or 4B-watch.
changed_axis = C17_margin_bridge_required_for_stage3
existing_axis_strengthened = price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence
new_axis_proposed = C17_margin_bridge_required_for_stage3
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | 4 | 23.97 | -13.86 | 69.34 | -21.04 | 0.5 | mixed; over-promotes commodity beta in two cases |
| P0b_e2r_2_0_baseline_reference | rollback | 4 | 23.97 | -13.86 | 69.34 | -21.04 | 0.75 | too permissive for commodity beta |
| P1_L4_commodity_spread_margin_bridge_shadow | sector_specific | 4 | 43.79 | -5.92 | 132.57 | -8.99 | 0.0 | improves positive/counterexample separation |
| P2_C17_margin_bridge_required_shadow | canonical_archetype_specific | 4 | 43.79 | -5.92 | 132.57 | -8.99 | 0.0 | best C17 compression candidate |
| P3_C17_counterexample_guard_profile | counterexample_guard | 6 | 20.68 | -18.56 | 47.78 | -28.78 | 0.0 | best risk overlay timing |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after score/stage | MFE90 | MAE90 | alignment verdict |
|---|---|---|---:|---:|---|
| CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE | 78 / Stage3-Yellow | 84 / Stage3-Green candidate / structural spread success | 66.14 | -6.58 | structural_margin_spread_success |
| CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL | 75 / Stage3-Yellow edge | 80 / Stage3-Yellow/Green bridge candidate | 21.49 | -5.26 | structural_spread_success_with_moderate_MAE |
| CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3 | 79 / Stage3-Yellow false-positive risk | 64 / Stage2-watch / 4B-watch; no Stage3 without realized margin bridge | 3.68 | -21.78 | low_MFE_high_MAE_false_positive_stage3_candidate |
| CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION | 77 / Stage3-Yellow false-positive risk | 62 / Stage2-watch / 4B-watch; Green blocked | 8.57 | -21.82 | brief_MFE_large_drawdown_false_positive_promotion |

The after profile improves alignment by keeping the two margin-bridge positives eligible while forcing the two beta-only rows into watch/4B status. This is a canonical-archetype compression, not a global threshold change.

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION | 2 | 2 | 2 | 1 | 4 | 0 | 6 | 4 | 2 | true | true | C17 now has bridge-vs-beta split; future loops should validate holdout in commodity chemicals and solar polysilicon separately |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: [stage2_actionable_evidence_bonus, stage3_yellow_total_min, stage3_green_total_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence]
residual_error_types_found: [commodity_beta_false_stage3, margin_bridge_missing_false_positive, 4B_overlay_too_late_when_waiting_for_price_break]
new_axis_proposed: C17_margin_bridge_required_for_stage3
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 current-profile residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

## 23. Validation Scope / Non-Validation Scope

Validation scope: historical trigger-level OHLC calibration using Songdaiki/stock-web tradable shards, C17 chemical commodity spread cases, 2020~2021 historical triggers, 30D/90D/180D MFE/MAE, profile/corporate-action window checks, and shadow-only score simulation.

Non-validation scope: no live scan, no current watchlist, no investment recommendation, no stock_agent source-code inspection, no production scoring patch, no broker/API use, and no new price-route discovery.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_margin_bridge_required_for_stage3,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,false,true,+1,Spread narrative promotes only when company-level margin/revision bridge is present.,keeps 011780/010060 positives while blocking 011170/006650 false positives,T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE|T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING|T011170_STAGE2_20210223_REOPENING_SPREAD_BETA|T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C17_commodity_beta_4B_watch_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,absent,present,+1,"Commodity/reopening beta with local peak proximity and no bridge should become 4B-watch, not Stage3.",improves peak-risk timing in 011780 overlay and 006650 false promotion,T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY|T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY,2,2,1,medium_low,sector_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_margin_spread_success", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "2020-08 earnings/spread window showed NB latex and synthetic-rubber spread capture moving into reported margin bridge, not merely commodity price beta."}
{"row_type": "case", "case_id": "CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_spread_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Polysilicon price/spread rebound was accompanied by company-level operating leverage and later price strength; this is a C17 positive when spread capture is explicit."}
{"row_type": "case", "case_id": "CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "T011170_STAGE2_20210223_REOPENING_SPREAD_BETA", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_false_positive_stage3_candidate", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Reopening/naphtha-spread optimism and stock relative strength existed, but company-level margin bridge was weaker and later MAE overwhelmed the small MFE."}
{"row_type": "case", "case_id": "CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "case_type": "4B_overlay_success", "positive_or_counterexample": "counterexample", "best_trigger": "T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "brief_MFE_large_drawdown_false_positive_promotion", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Sharp spread/reopening beta created immediate upside but lacked durable margin/revision bridge; the same window became a 4B/4C watch rather than a structural Stage3 entry."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE", "case_id": "CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_synthetic_rubber_latex", "primary_archetype": "NB_latex_margin_bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-08-07", "evidence_available_at_that_date": "2020-08 earnings/spread window showed NB latex and synthetic-rubber spread capture moving into reported margin bridge, not merely commodity price beta.", "evidence_source": "2020 earnings/spread public narrative; stock-web 011780 2020/2021 tradable rows and symbol profile verified.", "stage2_evidence_fields": ["public_event_or_disclosure", "margin_bridge", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-07", "entry_price": 94200, "MFE_30D_pct": 22.08, "MFE_90D_pct": 66.14, "MFE_180D_pct": 216.88, "MFE_1Y_pct": 216.88, "MFE_2Y_pct": null, "MAE_30D_pct": -6.58, "MAE_90D_pct": -6.58, "MAE_180D_pct": -6.58, "MAE_1Y_pct": -31.95, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": 0.58, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_representative_stage2", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_margin_spread_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G011780_2020-08-07_94200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING", "case_id": "CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL", "symbol": "010060", "company_name": "OCI홀딩스", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_polysilicon", "primary_archetype": "polysilicon_spread_margin_bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-02-10", "evidence_available_at_that_date": "Polysilicon price/spread rebound was accompanied by company-level operating leverage and later price strength; this is a C17 positive when spread capture is explicit.", "evidence_source": "2021 polysilicon spread/earnings public narrative; stock-web 010060 2021 tradable rows and symbol profile verified.", "stage2_evidence_fields": ["public_event_or_disclosure", "margin_bridge", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010060/2021.csv", "profile_path": "atlas/symbol_profiles/010/010060.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-10", "entry_price": 114000, "MFE_30D_pct": 21.49, "MFE_90D_pct": 21.49, "MFE_180D_pct": 48.25, "MFE_1Y_pct": 48.25, "MFE_2Y_pct": null, "MAE_30D_pct": -9.65, "MAE_90D_pct": -5.26, "MAE_180D_pct": -11.4, "MAE_1Y_pct": -11.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-10-01", "peak_price": 169000, "drawdown_after_peak_pct": -21.3, "green_lateness_ratio": 0.41, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_representative_stage2", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_spread_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G010060_2021-02-10_114000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T011170_STAGE2_20210223_REOPENING_SPREAD_BETA", "case_id": "CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_naphtha_basic_chemicals", "primary_archetype": "reopening_spread_beta_without_margin_bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill", "trigger_type": "Stage2-PriceOnlyWatch", "trigger_date": "2021-02-23", "evidence_available_at_that_date": "Reopening/naphtha-spread optimism and stock relative strength existed, but company-level margin bridge was weaker and later MAE overwhelmed the small MFE.", "evidence_source": "2021 reopening/spread narrative; stock-web 011170 2021 tradable rows and symbol profile verified.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-23", "entry_price": 326000, "MFE_30D_pct": 3.68, "MFE_90D_pct": 3.68, "MFE_180D_pct": 3.68, "MFE_1Y_pct": 3.68, "MFE_2Y_pct": null, "MAE_30D_pct": -11.04, "MAE_90D_pct": -21.78, "MAE_180D_pct": -28.53, "MAE_1Y_pct": -31.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-02", "peak_price": 338000, "drawdown_after_peak_pct": -31.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.67, "four_b_full_window_peak_proximity": 0.67, "four_b_timing_verdict": "commodity_beta_should_shift_to_4B_watch_not_stage3", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "low_MFE_high_MAE_false_positive_stage3_candidate", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G011170_2021-02-23_326000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF", "case_id": "CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_naphtha_basic_chemicals", "primary_archetype": "spread_beta_blowoff_without_durable_margin_bridge", "loop_objective": "sector_specific_rule_discovery | canonical_archetype_compression | counterexample_mining | 4B_non_price_requirement_stress_test | coverage_gap_fill", "trigger_type": "Stage2-PriceOnlyWatch", "trigger_date": "2021-02-10", "evidence_available_at_that_date": "Sharp spread/reopening beta created immediate upside but lacked durable margin/revision bridge; the same window became a 4B/4C watch rather than a structural Stage3 entry.", "evidence_source": "2021 chemical spread/reopening public narrative; stock-web 006650 2021 tradable rows and symbol profile verified.", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-10", "entry_price": 373500, "MFE_30D_pct": 8.57, "MFE_90D_pct": 8.57, "MFE_180D_pct": 8.57, "MFE_1Y_pct": 8.57, "MFE_2Y_pct": null, "MAE_30D_pct": -16.06, "MAE_90D_pct": -21.82, "MAE_180D_pct": -45.65, "MAE_1Y_pct": -45.65, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.62, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "good_4B_watch_if_margin_bridge_fails", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_break_only", "trigger_outcome_label": "brief_MFE_large_drawdown_false_positive_promotion", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G006650_2021-02-10_373500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY", "case_id": "CASE_R4L72_C17_011780_KUMHO_4B_POST_PEAK_OVERLAY", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_synthetic_rubber_latex", "primary_archetype": "NB_latex_peak_4B_overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2021-05-07", "evidence_available_at_that_date": "After the structural success, valuation/revision saturation and local peak proximity turned the case into a 4B overlay rather than a fresh Stage3 entry.", "evidence_source": "2021 peak/earnings saturation public narrative; stock-web 011780 2021 tradable rows.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-07", "entry_price": 281000, "MFE_30D_pct": 6.23, "MFE_90D_pct": 6.23, "MFE_180D_pct": 6.23, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.82, "MAE_90D_pct": -27.94, "MAE_180D_pct": -31.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-07", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.91, "four_b_full_window_peak_proximity": 0.91, "four_b_timing_verdict": "good_full_window_4B_timing", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G011780_20210507_281000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY", "case_id": "CASE_R4L72_C17_006650_DAEHAN_4B_OVERLAY", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_MARGIN_BRIDGE_VS_COMMODITY_BETA_FALSE_PROMOTION", "sector": "chemical_naphtha_basic_chemicals", "primary_archetype": "spread_beta_peak_4B_overlay", "loop_objective": "4B_non_price_requirement_stress_test", "trigger_type": "Stage4B-Overlay", "trigger_date": "2021-02-16", "evidence_available_at_that_date": "Post-surge entry near the same local peak with no durable margin/revision bridge; useful as 4B risk overlay, not as a positive Stage3 row.", "evidence_source": "2021 chemical beta blowoff public narrative; stock-web 006650 2021 tradable rows.", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-02-16", "entry_price": 393500, "MFE_30D_pct": 3.05, "MFE_90D_pct": 3.05, "MFE_180D_pct": 3.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -20.33, "MAE_90D_pct": -25.79, "MAE_180D_pct": -48.41, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-02-17", "peak_price": 405500, "drawdown_after_peak_pct": -49.94, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.62, "four_b_full_window_peak_proximity": 0.62, "four_b_timing_verdict": "good_early_4B_watch_before_full_drawdown", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "G006650_20210216_393500", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R4L72_C17_011780_KUMHO_NB_LATEX_STRUCTURAL_MARGIN_BRIDGE", "trigger_id": "T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 16, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 2, "margin_bridge_score": 22, "revision_score": 17, "relative_strength_score": 11, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 84, "stage_label_after": "Stage3-Green candidate / structural spread success", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile raises weight only when commodity spread is observed in company-level margin/revision bridge; price/reopening beta alone is capped and routed to 4B-watch.", "MFE_90D_pct": 66.14, "MAE_90D_pct": -6.58, "score_return_alignment_label": "structural_margin_spread_success", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R4L72_C17_010060_OCI_POLYSILICON_SPREAD_STRUCTURAL", "trigger_id": "T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING", "symbol": "010060", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 11, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 11, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 75, "stage_label_before": "Stage3-Yellow edge", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 20, "revision_score": 14, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 9, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 80, "stage_label_after": "Stage3-Yellow/Green bridge candidate", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile raises weight only when commodity spread is observed in company-level margin/revision bridge; price/reopening beta alone is capped and routed to 4B-watch.", "MFE_90D_pct": 21.49, "MAE_90D_pct": -5.26, "score_return_alignment_label": "structural_spread_success_with_moderate_MAE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R4L72_C17_011170_LOTTECHEM_REOPENING_SPREAD_BETA_FALSE_STAGE3", "trigger_id": "T011170_STAGE2_20210223_REOPENING_SPREAD_BETA", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 8, "relative_strength_score": 16, "customer_quality_score": 0, "policy_or_regulatory_score": 2, "valuation_repricing_score": 12, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 4, "relative_strength_score": 9, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 20, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 64, "stage_label_after": "Stage2-watch / 4B-watch; no Stage3 without realized margin bridge", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile raises weight only when commodity spread is observed in company-level margin/revision bridge; price/reopening beta alone is capped and routed to 4B-watch.", "MFE_90D_pct": 3.68, "MAE_90D_pct": -21.78, "score_return_alignment_label": "low_MFE_high_MAE_false_positive_stage3_candidate", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "CASE_R4L72_C17_006650_DAEHAN_REOPENING_SPREAD_BLOWOFF_FALSE_PROMOTION", "trigger_id": "T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 7, "relative_strength_score": 18, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 14, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow false-positive risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 3, "relative_strength_score": 10, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 6, "execution_risk_score": 23, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 62, "stage_label_after": "Stage2-watch / 4B-watch; Green blocked", "changed_components": ["margin_bridge_score", "revision_score", "relative_strength_score", "valuation_repricing_score", "execution_risk_score"], "component_delta_explanation": "C17 shadow profile raises weight only when commodity spread is observed in company-level margin/revision bridge; price/reopening beta alone is capped and routed to 4B-watch.", "MFE_90D_pct": 8.57, "MAE_90D_pct": -21.82, "score_return_alignment_label": "brief_MFE_large_drawdown_false_positive_promotion", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_margin_bridge_required_for_stage3,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,false,true,+1,Spread narrative promotes only when company-level margin/revision bridge is present.,keeps 011780/010060 positives while blocking 011170/006650 false positives,T011780_STAGE2_20200807_NB_LATEX_MARGIN_BRIDGE|T010060_STAGE2_20210210_POLYSILICON_SPREAD_REPRICING|T011170_STAGE2_20210223_REOPENING_SPREAD_BETA|T006650_STAGE2_20210210_SPREAD_BETA_BLOWOFF,4,4,2,medium,canonical_shadow_only,not production; post-calibrated residual
shadow_weight,C17_commodity_beta_4B_watch_guard,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,absent,present,+1,"Commodity/reopening beta with local peak proximity and no bridge should become 4B-watch, not Stage3.",improves peak-risk timing in 011780 overlay and 006650 false promotion,T011780_4B_20210507_NB_LATEX_PEAK_OVERLAY|T006650_4B_20210216_SPREAD_BETA_PEAK_OVERLAY,2,2,1,medium_low,sector_shadow_only,not production; post-calibrated residual
```

### 25.6 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "72", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["commodity_beta_false_stage3", "margin_bridge_missing_false_positive", "4B_overlay_too_late_when_waiting_for_price_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type": "narrative_only", "case_id": "C17_future_holdout_solar_polysilicon_2022_2023", "symbol": null, "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "reason": "future holdout for polysilicon and solar chemical spread cycles; not used for current weight calibration", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_round = R4
completed_loop = 72
next_round = R5
next_loop = 72
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-web manifest checked: atlas/manifest.json, generated_at 2026-05-21, max_date 2026-02-20, tradable_row_count 14,354,401, raw_unadjusted_marcap.
- Symbol profiles checked for 011780, 010060, 011170, and 006650.
- Representative OHLC rows checked from stock-web tradable shards for 2020 and 2021 windows.
- All evidence labels are research-proxy historical labels; before implementation, repository ingestion should replace narrative source notes with exact filing/news links if available.
- This file is not an investment recommendation and is not a production scoring patch.

