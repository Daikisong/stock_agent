# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R4_loop_72_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
selected_round: R4
selected_loop: 72
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality reinforcement after all C01~C32 archetypes exceeded 80 representative rows
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: REBAR_STEEL_PIPE_SPREAD_REVERSAL_AND_LATE_RESULT_TRAP
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4C_thesis_break_timing_test
  - canonical_archetype_specific_rule_discovery
price_source: Songdaiki/stock-web
price_data_repo: https://github.com/Daikisong/stock-web
stock_web_manifest_max_date: 2026-02-20
price_basis: tradable_raw
price_adjustment_status: raw_unadjusted_marcap
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

One-line contribution: This loop adds **4 new independent cases**, **2 counterexamples**, and **1 residual error** for **L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE**.

## 1. Current Calibrated Profile Assumption

Baseline proxy used in this MD:

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
after_profile_id = proposed_C15_material_spread_shadow_profile
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
shadow_weight_only = true
```

Existing global axes are treated as already applied, not re-proposed globally: Stage2 actionable evidence bonus, Stage3 Yellow/Green thresholds, cross-evidence buffer, price-only blowoff block, full 4B non-price requirement, and hard 4C thesis-break routing.

## 2. Round / Large Sector / Canonical Archetype Scope

- selected_round: `R4`
- large_sector_id: `L4_MATERIALS_SPREAD_RESOURCE`
- canonical_archetype_id: `C15_MATERIAL_SPREAD_SUPERCYCLE`
- fine_archetype_id: `REBAR_STEEL_PIPE_SPREAD_REVERSAL_AND_LATE_RESULT_TRAP`
- Scope thesis: C15 should reward early **demand + spread + margin bridge** in steel/rebar/pipe cycles, but should decay late reported supercycle results when the price cycle has already peaked or when forward spread continuity is missing.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index status used for selection:

- All C01~C32 archetypes are above the old 80-row threshold; the next priority is quality, URL/proxy repair, MFE/MAE completeness, and balance reinforcement.
- C15 is listed under Priority 1 balance reinforcement with the direction: spread reversal and inventory-cycle counterexample repair.
- Displayed C15 top repeated symbols: `005490`, `004020`, `103140`, `018470`, `010130`, `025820`.
- This MD avoids those displayed overused C15 top symbols and selects `084010`, `104700`, and `005010`. `104700` appears twice, but the second row is a different trigger family and different market regime: 2021 early spread-positive Stage2 vs 2024 price/volume/utilization thesis break Stage4C.

Novelty fields:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_trigger_family_count = 3
positive_case_count = 2
counterexample_count = 2
current_profile_error_count = 1
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest fields checked:

```text
source_name = FinanceData/marcap
source_repo_url = https://github.com/FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14,354,401
raw_row_count = 15,214,118
symbol_count = 5,414
active_like_symbol_count = 2,868
inactive_or_delisted_like_symbol_count = 2,546
markets = KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

Tradable shard columns used: `d,o,h,l,c,v,a,mc,s,m`.

Profile / corporate-action checks:

| symbol | profile_path | candidate dates relevant to this MD | 180D status |
|---:|---|---|---|
| 084010 | atlas/symbol_profiles/084/084010.json | 2009-03-11, 2026-01-05, 2026-01-26 | clean for 2021-01-13~D+180 |
| 104700 | atlas/symbol_profiles/104/104700.json | 2018-05-04 | clean for both 2021-01-13~D+180 and 2024-05-17~D+180 |
| 005010 | atlas/symbol_profiles/005/005010.json | 1996-04-30, 2001-07-31, 2002-04-09, 2022-07-13, 2022-12-27 | clean for 2023-04-17~D+180; 2022 actions are before entry |

## 5. Historical Eligibility Gate

All four trigger rows pass the 180-trading-day gate. `104700` 2024 has 30D/90D/180D complete; 2Y is unavailable because the stock-web manifest ends at `2026-02-20`.

| case_id | calibration_usable | forward_window_trading_days | 30/90/180 MFE/MAE complete | corporate_action_window_status |
|---|---|---:|---|---|
| C15-084010-20210112-SA | true | 180 | yes | clean_180D_window |
| C15-104700-20210112-SA | true | 180 | yes | clean_180D_window |
| C15-005010-20230414-SG | true | 180 | yes | clean_180D_window |
| C15-104700-20240516-4C | true | 180 | yes | clean_180D_window |

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id candidates compressed here:
- REBAR_DEMAND_SCRAP_SPREAD_EARLY_BRIDGE
- REBAR_MARGIN_MIX_EARLY_BRIDGE
- STEEL_PIPE_OCTG_LATE_RESULT_TRAP
- REBAR_PRICE_VOLUME_UTILIZATION_BREAK_4C
```

Compression rule: all rows are C15 because the causal engine is material spread and inventory-cycle transmission. The split is not by product name but by timing: early forward bridge vs late reported result vs thesis break.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger | evidence | price result summary |
|---|---:|---|---|---|---|---|
| C15-084010-20210112-SA | 084010 | 대한제강 | positive / structural_success | Stage2-Actionable 2021-01-12 -> entry 2021-01-13 | Rebar demand recovery and scrap-price pass-through/spread bridge; 2021 revenue and operating-profit improvement forecast. | MFE90 120.87%, MAE90 -9.57%, MFE180 123.48%, MAE180 -9.57% |
| C15-104700-20210112-SA | 104700 | 한국철강 | positive / structural_success | Stage2-Actionable 2021-01-12 -> entry 2021-01-13 | Rebar demand recovery, scrap price pass-through, discontinued low-margin forging business, and operating margin forecast improvement. | MFE90 93.71%, MAE90 -2.8%, MFE180 93.71%, MAE180 -2.8% |
| C15-005010-20230414-SG | 005010 | 휴스틸 | counterexample / false_positive_green | Stage3-Green 2023-04-14 -> entry 2023-04-17 | Reported 2022 record revenue/operating profit, 28% OPM, and export uplift from US/Canada energy pipe demand. | MFE90 3.82%, MAE90 -32.79%, MFE180 3.82%, MAE180 -36.54% |
| C15-104700-20240516-4C | 104700 | 한국철강 | counterexample / 4C_success | Stage4C 2024-05-16 -> entry 2024-05-17 | Q1 operating profit down 93.8%, selling price down, utilization down, construction downturn cited. | MFE90 1.19%, MAE90 -37.53%, MFE180 1.19%, MAE180 -37.53% |

## 8. Positive vs Counterexample Balance

| bucket | count | cases | aggregate read |
|---|---:|---|---|
| positive_structural_success | 2 | 084010, 104700 2021 | avg MFE90 107.29%, avg MAE90 -6.19%; early demand+spread bridge worked |
| counterexample_or_failed_rerating | 2 | 005010 2023, 104700 2024 | avg MFE90 2.5%, avg MAE90 -35.16%; late-result and thesis-break rows should not be promoted |
| 4B_or_4C_case | 1 hard 4C + 1 4B-watch diagnostic | 104700 2024 / 005010 2023 | 4C protected from severe long-side MAE; late Green had peak proximity 1.0 and should be watched, not promoted |

## 9. Evidence Source Map

| source_id | type | url | used_for | directness |
|---|---|---|---|---|
| SRC-FERRO-20210112 | article/report summary | https://www.ferrotimes.com/news/articleView.html?idxno=9393 | 대한제강/한국철강 2021 rebar demand and scrap spread early bridge | direct article with report-derived details |
| SRC-HUSTEEL-20230414 | company press page | https://www.husteel.com/pr/press/view.hu?page=1&perPageNum=10&pk_id=205 | 휴스틸 reported record result / export pipe spread late Green test | direct company page |
| SRC-SNM-20240516 | industry article | https://www.snmnews.com/news/articleView.html?idxno=535189 | 한국철강 Q1 2024 operating-profit collapse, ASP/utilization break | direct article citing FSS-submitted data |

## 10. Price Data Source Map

| symbol | years loaded | stock-web shard path |
|---:|---|---|
| 084010 | 2021, 2022, 2023 | atlas/ohlcv_tradable_by_symbol_year/084/084010/*.csv |
| 104700 | 2021, 2022, 2023, 2024, 2025 | atlas/ohlcv_tradable_by_symbol_year/104/104700/*.csv |
| 005010 | 2023, 2024, 2025 | atlas/ohlcv_tradable_by_symbol_year/005/005010/*.csv |

Entry price rule used: if evidence publication time was after close or not explicitly tradable, entry was the next stock-web tradable day close.

## 11. Case-by-Case Trigger Grid

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C15-084010-20210112-SA | 084010 | Stage2-Actionable | 2021-01-12 | 2021-01-13 | 11500 | 24.35 | 120.87 | 123.48 | -9.57 | -9.57 | -9.57 | 2021-06-28 | 25700 | -24.32 | current_profile_correct |
| C15-104700-20210112-SA | 104700 | Stage2-Actionable | 2021-01-12 | 2021-01-13 | 7150 | 22.38 | 93.71 | 93.71 | -2.8 | -2.8 | -2.8 | 2021-04-27 | 13850 | -37.62 | current_profile_correct |
| C15-005010-20230414-SG | 005010 | Stage3-Green | 2023-04-14 | 2023-04-17 | 7060 | 3.82 | 3.82 | 3.82 | -15.01 | -32.79 | -36.54 | 2023-04-17 | 7330 | -38.88 | current_profile_false_positive |
| C15-104700-20240516-4C | 104700 | Stage4C | 2024-05-16 | 2024-05-17 | 11750 | 1.19 | 1.19 | 1.19 | -22.38 | -37.53 | -37.53 | 2024-05-17 | 11890 | -38.27 | current_profile_correct |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Entry OHLCV rows

| case_id | entry_date | o | h | l | c | v | amount | market_cap | shares | market |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| C15-084010-20210112-SA | 2021-01-13 | 11450 | 11800 | 11350 | 11500 | 131008 | 1513778000 | 283437441000 | 24646734 | KOSPI |
| C15-104700-20210112-SA | 2021-01-13 | 7100 | 7150 | 6950 | 7150 | 458613 | 3232337500 | 329257500000 | 46050000 | KOSPI |
| C15-005010-20230414-SG | 2023-04-17 | 7160 | 7330 | 7010 | 7060 | 5366144 | 38572534240 | 396687809500 | 56188075 | KOSPI |
| C15-104700-20240516-4C | 2024-05-17 | 11800 | 11890 | 11680 | 11750 | 284508 | 3345843310 | 498787500000 | 42450000 | KOSPI |

### 12.2 Forward path result

| case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak | verdict |
|---|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|
| C15-084010-20210112-SA | 084010 | Stage2-Actionable | 2021-01-12 | 2021-01-13 | 11500 | 24.35 | 120.87 | 123.48 | -9.57 | -9.57 | -9.57 | 2021-06-28 | 25700 | -24.32 | current_profile_correct |
| C15-104700-20210112-SA | 104700 | Stage2-Actionable | 2021-01-12 | 2021-01-13 | 7150 | 22.38 | 93.71 | 93.71 | -2.8 | -2.8 | -2.8 | 2021-04-27 | 13850 | -37.62 | current_profile_correct |
| C15-005010-20230414-SG | 005010 | Stage3-Green | 2023-04-14 | 2023-04-17 | 7060 | 3.82 | 3.82 | 3.82 | -15.01 | -32.79 | -36.54 | 2023-04-17 | 7330 | -38.88 | current_profile_false_positive |
| C15-104700-20240516-4C | 104700 | Stage4C | 2024-05-16 | 2024-05-17 | 11750 | 1.19 | 1.19 | 1.19 | -22.38 | -37.53 | -37.53 | 2024-05-17 | 11890 | -38.27 | current_profile_correct |

## 13. Current Calibrated Profile Stress Test

| case_id | current calibrated proxy behavior | actual path | stress verdict |
|---|---|---|---|
| C15-084010-20210112-SA | Stage2-Actionable allowed because non-price demand/spread bridge exists | MFE90 120.87%, MAE90 -9.57% | current_profile_correct |
| C15-104700-20210112-SA | Stage2-Actionable allowed because demand/margin bridge exists | MFE90 93.71%, MAE90 -2.80% | current_profile_correct |
| C15-005010-20230414-SG | Stage3-Green risk: record result and margin proof may over-score if no late-result decay | MFE90 3.82%, MAE90 -32.79% | current_profile_false_positive |
| C15-104700-20240516-4C | Hard thesis-break route should trigger after profit/price/utilization collapse | MFE90 1.19%, MAE90 -37.53% | current_profile_correct |

Answers to required calibrated-axis questions:

1. Stage2 actionable bonus was appropriate for the two 2021 rebar cases because the bridge was forward-looking, not price-only.
2. Yellow/Green thresholds are not the main residual error; the C15-specific problem is that a late reported supercycle can still accumulate enough confirmed-evidence score to look Green.
3. Green threshold 87/revision 55 is not loosened. It needs a C15 late-result decay or forward spread-continuity gate.
4. Price-only blowoff guard remains appropriate. 005010 shows that even non-price evidence can be too late if it is merely a post-peak annual-result confirmation.
5. Full 4B non-price requirement remains appropriate; the 005010 row is a 4B watch diagnostic, not a full 4B sell rule.
6. Hard 4C routing is strengthened for C15 when price, volume/utilization, and operating margin all break together.

## 14. Stage2 / Yellow / Green Comparison

| stage | C15 interpretation from this loop | result |
|---|---|---|
| Stage2-Actionable | Demand + spread + margin bridge before the realized result | Worked in 084010/104700 2021 |
| Stage3-Yellow | Confirmed earnings without forward spread durability | Should stay cautious if the price cycle is mature |
| Stage3-Green | Requires confirmed earnings plus forward spread continuity, not just record prior-year result | 005010 late Green would be false positive |
| Stage4C | Simultaneous realized margin collapse, selling-price fall, utilization drop, and demand slowdown | 104700 2024 protected correctly |

## 15. 4B Local vs Full-window Timing Audit

`005010` is not written as a full 4B trigger row, but it is a useful 4B watch diagnostic. The next-trading-day entry after the company press page was the same observed 180D peak date.

```text
005010 diagnostic four_b_local_peak_proximity = 1.0
005010 diagnostic four_b_full_window_peak_proximity = 1.0
verdict = late_green_at_full_window_peak_watch
```

Interpretation: C15 should not convert post-peak record-result evidence into Green without forward spread-continuity proof. The evidence is real, but the stage is late.

## 16. 4C Protection Audit

`104700` 2024 is a hard 4C success row.

```text
trigger_date = 2024-05-16
entry_date = 2024-05-17
MFE_30D_pct = 1.19
MAE_30D_pct = -22.38
MFE_90D_pct = 1.19
MAE_90D_pct = -37.53
MFE_180D_pct = 1.19
MAE_180D_pct = -37.53
four_c_protection_label = hard_4c_success
```

The 4C trigger is not just “bad earnings.” It is a material-spread thesis break: selling price fell, construction demand was weak, operating margin collapsed, and utilization dropped.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = canonical_archetype_specific
rule_name = C15_forward_spread_bridge_and_late_result_decay
```

Candidate rule:

- Promote early C15 Stage2 when evidence links demand visibility, spread/pass-through, and margin bridge before earnings are fully reflected.
- Decay C15 Stage3-Green if the evidence is only a late annual/quarterly result and the price row is at or near the full-window peak.
- Route to hard 4C when realized result deterioration is accompanied by selling-price fall, volume/utilization fall, and demand-cycle break.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
candidate_axes:
  forward_spread_demand_bridge: +1
  late_reported_supercycle_decay: -2
  price_volume_utilization_break_to_4c: +1
rule_scope = canonical_archetype_specific
confidence = medium_low
```

Why not global: this behavior is specific to commodity/material spread cycles. A software recurring-revenue Green or bank capital-return Green should not inherit the same late-result decay structure without separate evidence.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | default | 4 | all rows evaluated as observed | 54.9 | -20.67 | 55.55 | -21.61 | 0.25 | 0 | 1 | mixed; positive Stage2 rows good, late Green bad |
| P0b e2r_2_0_baseline_reference | rollback reference | 4 | looser Green risk | 54.9 | -20.67 | 55.55 | -21.61 | 0.25+ | 0 | 1 | worse risk of late-result promotion |
| P1 sector_specific_candidate_profile | L4 sector | 3 | two Stage2 positives + one 4C protection | 71.92 | -16.63 | 72.79 | -16.63 | 0.0 | 0 | 0 | better by blocking 005010 late Green |
| P2 canonical_C15_candidate_profile | C15 canonical | 4 | keep positives, decay late Green, harden 4C | 107.29 positive-only | -6.19 positive-only | 108.59 positive-only | -6.19 positive-only | 0.0 | 0 | 0 | best C15-specific alignment |
| P3 counterexample_guard_profile | guardrail | 2 | 005010 blocked / 104700 4C hard-routed | 2.5 | -35.16 | 2.5 | -37.03 | 0.0 | not_applicable | 0 | guardrail correctly captures low-upside/high-MAE rows |

## 20. Score-Return Alignment Matrix

| case_id | raw score before -> after | stage before -> after | MFE90/MAE90 | alignment |
|---|---|---|---|---|
| C15-084010-20210112-SA | 78 -> 82 | Stage2-Actionable -> Stage2-Actionable | 120.87 / -9.57 | early spread/demand bridge aligned with high 90D/180D MFE and low MAE |
| C15-104700-20210112-SA | 76 -> 81 | Stage2-Actionable -> Stage2-Actionable | 93.71 / -2.8 | forward demand and margin mix aligned with very high 90D/180D MFE and shallow MAE |
| C15-005010-20230414-SG | 89 -> 69 | Stage3-Green -> Stage2-Watch | 3.82 / -32.79 | reported supercycle evidence arrived at/near full-window peak; 90D/180D upside was small and MAE was large |
| C15-104700-20240516-4C | 62 -> 44 | Stage4B-Watch -> Stage4C | 1.19 / -37.53 | 4C thesis break matched low upside and severe 30D/90D/180D downside for long exposure |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | REBAR_STEEL_PIPE_SPREAD_REVERSAL_AND_LATE_RESULT_TRAP | 2 | 2 | 1 | 1 | 4 | 0 | 4 | 4 | 1 | yes | yes | C15 balance improves by adding 2 positives, 2 counterexamples, 1 late-Green false positive, and 1 4C protection row. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - late_reported_supercycle_green_false_positive
new_axis_proposed:
  - C15_forward_spread_demand_bridge
  - C15_late_reported_supercycle_decay
  - C15_price_volume_utilization_break_to_4c
existing_axis_strengthened:
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: C15 material spread timing rule can roll up to L4 after more non-steel materials validation
canonical_archetype_rule_candidate: C15_forward_spread_bridge_and_late_result_decay
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Actual stock-web tradable_raw OHLCV rows for entry dates.
- 30D/90D/180D MFE and MAE from entry close using stock-web high/low rows.
- 1Y/2Y when forward rows exist before stock-web manifest max date.
- Corporate-action candidate overlap against profile-level candidate dates.
- Evidence timing rule: unknown or after-close publication uses next-trading-day close.

Not validated / not done:

- No stock_agent source code was opened.
- No production scoring patch was written.
- No live/current candidate scan was performed.
- No brokerage/API/trading action was performed.
- Registry JSONL was not required for scoring here; selected_loop follows the latest visible C15/R4 loop context and should be renamed if a higher C15 loop already exists in a newer repository registry snapshot.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,forward_spread_demand_bridge,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Demand+spread+margin bridge before realized earnings can stay Stage2-Actionable","Preserved 084010/104700 early 2021 positives: avg MFE90 107.29%, avg MAE90 -6.19%","C15-R4L72-084010-20210112-SA-01|C15-R4L72-104700-20210112-SA-01",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,late_reported_supercycle_decay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,-2,-2,"Reported supercycle result at/near peak without forward spread continuity should not promote Green","Blocked 005010 late Green false positive: MFE90 3.82%, MAE90 -32.79%","C15-R4L72-005010-20230414-SG-01",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,price_volume_utilization_break_to_4c,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+1,"Simultaneous price, profit, and utilization collapse is thesis break, not just 4B watch","104700 4C row had MFE90 1.19%, MAE90 -37.53% after next-day entry","C15-R4L72-104700-20240516-4C-01",1,1,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Daikisong/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"C15-084010-20210112-SA","symbol":"084010","company_name":"대한제강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_DEMAND_SCRAP_SPREAD_EARLY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"early spread/demand bridge aligned with high 90D/180D MFE and low MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C15 example: forward demand plus spread bridge came before the strongest part of the rerating."}
{"row_type":"case","case_id":"C15-104700-20210112-SA","symbol":"104700","company_name":"한국철강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_MARGIN_MIX_EARLY_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"forward demand and margin mix aligned with very high 90D/180D MFE and shallow MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C15 example: the signal is not commodity price alone; it is demand visibility plus margin mix."}
{"row_type":"case","case_id":"C15-005010-20230414-SG","symbol":"005010","company_name":"휴스틸","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_OCTG_LATE_RESULT_TRAP","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage3-Green","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"reported supercycle evidence arrived at/near full-window peak; 90D/180D upside was small and MAE was large","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: realized record result is not enough for C15 Green if forward spread continuity and inventory-cycle durability are absent."}
{"row_type":"case","case_id":"C15-104700-20240516-4C","symbol":"104700","company_name":"한국철강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_PRICE_VOLUME_UTILIZATION_BREAK_4C","case_type":"4C_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4C","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"4C thesis break matched low upside and severe 30D/90D/180D downside for long exposure","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Counterexample/protection row: simultaneous price, margin, and utilization break should route to hard 4C rather than delayed 4B watch."}
{"row_type":"trigger","trigger_id":"C15-R4L72-084010-20210112-SA-01","case_id":"C15-084010-20210112-SA","symbol":"084010","company_name":"대한제강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_DEMAND_SCRAP_SPREAD_EARLY_BRIDGE","sector":"steel/rebar","primary_archetype":"material spread supercycle","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-12","evidence_available_at_that_date":"2021-01-12 FerroTimes article summarizing Hyundai Motor Securities view; next-trading-day entry used because publication time is not a tradable timestamp.","evidence_source":"https://www.ferrotimes.com/news/articleView.html?idxno=9393","stage2_evidence_fields":["public_event_or_disclosure","margin_bridge","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Daikisong/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/084/084010/2021.csv|2022.csv|2023.csv","profile_path":"atlas/symbol_profiles/084/084010.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-13","entry_price":11500.0,"entry_ohlcv_row":{"d":"2021-01-13","o":11450.0,"h":11800.0,"l":11350.0,"c":11500.0,"v":131008.0,"a":1513778000.0,"mc":283437441000.0,"s":24646734,"m":"KOSPI"},"MFE_30D_pct":24.35,"MFE_90D_pct":120.87,"MFE_180D_pct":123.48,"MFE_1Y_pct":123.48,"MFE_2Y_pct":131.3,"MAE_30D_pct":-9.57,"MAE_90D_pct":-9.57,"MAE_180D_pct":-9.57,"MAE_1Y_pct":-9.57,"MAE_2Y_pct":-12.17,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-06-28","peak_price":25700.0,"drawdown_after_peak_pct":-24.32,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"rebar_demand_scrap_spread_stage2_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates=2009-03-11,2026-01-05,2026-01-26","same_entry_group_id":"C15-084010-20210113","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15-R4L72-104700-20210112-SA-01","case_id":"C15-104700-20210112-SA","symbol":"104700","company_name":"한국철강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_MARGIN_MIX_EARLY_BRIDGE","sector":"steel/rebar","primary_archetype":"material spread supercycle","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-12","evidence_available_at_that_date":"2021-01-12 FerroTimes article; next-trading-day entry used because publication time is not a tradable timestamp.","evidence_source":"https://www.ferrotimes.com/news/articleView.html?idxno=9393","stage2_evidence_fields":["public_event_or_disclosure","margin_bridge","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":[],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Daikisong/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/104/104700/2021.csv|2022.csv|2023.csv","profile_path":"atlas/symbol_profiles/104/104700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-13","entry_price":7150.0,"entry_ohlcv_row":{"d":"2021-01-13","o":7100.0,"h":7150.0,"l":6950.0,"c":7150.0,"v":458613.0,"a":3232337500.0,"mc":329257500000.0,"s":46050000,"m":"KOSPI"},"MFE_30D_pct":22.38,"MFE_90D_pct":93.71,"MFE_180D_pct":93.71,"MFE_1Y_pct":93.71,"MFE_2Y_pct":93.71,"MAE_30D_pct":-2.8,"MAE_90D_pct":-2.8,"MAE_180D_pct":-2.8,"MAE_1Y_pct":-2.8,"MAE_2Y_pct":-22.38,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-04-27","peak_price":13850.0,"drawdown_after_peak_pct":-37.62,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"rebar_margin_mix_stage2_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates=2018-05-04","same_entry_group_id":"C15-104700-20210113","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15-R4L72-005010-20230414-SG-01","case_id":"C15-005010-20230414-SG","symbol":"005010","company_name":"휴스틸","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"STEEL_PIPE_OCTG_LATE_RESULT_TRAP","sector":"steel pipe/OCTG","primary_archetype":"material spread supercycle","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage3-Green","trigger_date":"2023-04-14","evidence_available_at_that_date":"2023-04-14 company press page; next-trading-day entry used because publication time is not a tradable timestamp.","evidence_source":"https://www.husteel.com/pr/press/view.hu?page=1&perPageNum=10&pk_id=205","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Daikisong/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005010/2023.csv|2024.csv|2025.csv","profile_path":"atlas/symbol_profiles/005/005010.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2023-04-17","entry_price":7060.0,"entry_ohlcv_row":{"d":"2023-04-17","o":7160.0,"h":7330.0,"l":7010.0,"c":7060.0,"v":5366144.0,"a":38572534240.0,"mc":396687809500.0,"s":56188075,"m":"KOSPI"},"MFE_30D_pct":3.82,"MFE_90D_pct":3.82,"MFE_180D_pct":3.82,"MFE_1Y_pct":3.82,"MFE_2Y_pct":3.82,"MAE_30D_pct":-15.01,"MAE_90D_pct":-32.79,"MAE_180D_pct":-36.54,"MAE_1Y_pct":-39.52,"MAE_2Y_pct":-51.13,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-17","peak_price":7330.0,"drawdown_after_peak_pct":-38.88,"green_lateness_ratio":null,"four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"late_green_at_full_window_peak_watch","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_reported_pipe_spread_green_false_positive","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates include 2022-07-13 and 2022-12-27 before entry, none inside entry~D+180","same_entry_group_id":"C15-005010-20230417","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C15-R4L72-104700-20240516-4C-01","case_id":"C15-104700-20240516-4C","symbol":"104700","company_name":"한국철강","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"REBAR_PRICE_VOLUME_UTILIZATION_BREAK_4C","sector":"steel/rebar","primary_archetype":"material spread supercycle","loop_objective":"coverage_gap_fill|counterexample_mining|4C_thesis_break_timing_test|canonical_archetype_specific_rule_discovery","trigger_type":"Stage4C","trigger_date":"2024-05-16","evidence_available_at_that_date":"2024-05-16 16:15 article; next-trading-day entry used.","evidence_source":"https://www.snmnews.com/news/articleView.html?idxno=535189","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Daikisong/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/104/104700/2024.csv|2025.csv","profile_path":"atlas/symbol_profiles/104/104700.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-17","entry_price":11750.0,"entry_ohlcv_row":{"d":"2024-05-17","o":11800.0,"h":11890.0,"l":11680.0,"c":11750.0,"v":284508.0,"a":3345843310.0,"mc":498787500000.0,"s":42450000,"m":"KOSPI"},"MFE_30D_pct":1.19,"MFE_90D_pct":1.19,"MFE_180D_pct":1.19,"MFE_1Y_pct":1.19,"MFE_2Y_pct":null,"MAE_30D_pct":-22.38,"MAE_90D_pct":-37.53,"MAE_180D_pct":-37.53,"MAE_1Y_pct":-38.3,"MAE_2Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":11890.0,"drawdown_after_peak_pct":-38.27,"green_lateness_ratio":null,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"rebar_price_volume_utilization_break_4c_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; profile corporate_action_candidate_dates=2018-05-04","same_entry_group_id":"C15-104700-20240517","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C15_shadow","case_id":"C15-084010-20210112-SA","trigger_id":"C15-R4L72-084010-20210112-SA-01","symbol":"084010","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":18,"revision_score":10,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":20,"margin_bridge_score":22,"revision_score":11,"relative_strength_score":11,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"C15-specific bridge gives credit only when demand and input-cost pass-through are stated before the price cycle matures.","MFE_90D_pct":120.87,"MAE_90D_pct":-9.57,"score_return_alignment_label":"early spread/demand bridge aligned with high 90D/180D MFE and low MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C15_shadow","case_id":"C15-104700-20210112-SA","trigger_id":"C15-R4L72-104700-20210112-SA-01","symbol":"104700","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":16,"margin_bridge_score":17,"revision_score":9,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":18,"margin_bridge_score":22,"revision_score":10,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":81,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","backlog_visibility_score","execution_risk_score"],"component_delta_explanation":"Demand plus margin-mix bridge is stronger than a price-only commodity move.","MFE_90D_pct":93.71,"MAE_90D_pct":-2.8,"score_return_alignment_label":"forward demand and margin mix aligned with very high 90D/180D MFE and shallow MAE","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C15_shadow","case_id":"C15-005010-20230414-SG","trigger_id":"C15-R4L72-005010-20230414-SG-01","symbol":"005010","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":24,"revision_score":20,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":14,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":89,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":16,"revision_score":10,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":12,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":69,"stage_label_after":"Stage2-Watch","changed_components":["margin_bridge_score","revision_score","relative_strength_score","execution_risk_score"],"component_delta_explanation":"Late-result decay and missing forward spread-continuity evidence cut Green; high execution/inventory-cycle risk is raised.","MFE_90D_pct":3.82,"MAE_90D_pct":-32.79,"score_return_alignment_label":"reported supercycle evidence arrived at/near full-window peak; 90D/180D upside was small and MAE was large","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy_to_C15_shadow","case_id":"C15-104700-20240516-4C","trigger_id":"C15-R4L72-104700-20240516-4C-01","symbol":"104700","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":2,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":62,"stage_label_before":"Stage4B-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":28,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":2},"weighted_score_after":44,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","revision_score","execution_risk_score"],"component_delta_explanation":"Simultaneous selling-price, demand/utilization, and profit collapse is thesis break, not mere overheat.","MFE_90D_pct":1.19,"MAE_90D_pct":-37.53,"score_return_alignment_label":"4C thesis break matched low upside and severe 30D/90D/180D downside for long exposure","current_profile_verdict":"current_profile_correct"}
{"row_type":"residual_contribution","round":"R4","loop":"72","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","price_only_blowoff_blocks_positive_stage","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["late_reported_supercycle_green_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas. These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row. Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: `atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv`.
- Symbol profile pattern: `atlas/symbol_profiles/<prefix>/<ticker>.json`.

### Rules

- Use only `calibration_usable=true` rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless `independent_evidence_weight > 0`.
- Do not treat `schema_rematerialization_only` or `duplicate_low_value_loop` as new evidence.
- Do not apply global deltas unless multiple large_sector_id values support the same direction.
- Prefer sector_specific or canonical_archetype_specific shadow profiles.
- Positive score promotion requires non-price evidence and clean 180D MFE/MAE.
- 4B rows are overlay/risk calibration only.
- 4C rows are thesis-break/protection calibration only.
- Price-only rows cannot promote Stage2/Stage3.
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

```yaml
completed_round: R4
completed_loop: 72
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 1 balance/quality reinforcement
next_recommended_archetypes:
  - C05_EPC_MEGA_CONTRACT_MARGIN_GAP
  - C01_ORDER_BACKLOG_MARGIN_BRIDGE
  - C13_BATTERY_JV_UTILIZATION_AMPC_IRA
  - C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE
  - C15_MATERIAL_SPREAD_SUPERCYCLE_URL_PROXY_REPAIR
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
```

## 28. Source Notes

Primary prompt and index:

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt`
- `docs/core/V12_Research_No_Repeat_Index.md`

Stock-Web:

- `atlas/manifest.json`
- `atlas/schema.json`
- `atlas/symbol_profiles/084/084010.json`
- `atlas/symbol_profiles/104/104700.json`
- `atlas/symbol_profiles/005/005010.json`
- `atlas/ohlcv_tradable_by_symbol_year/084/084010/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/084/084010/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/084/084010/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/104/104700/2021.csv`
- `atlas/ohlcv_tradable_by_symbol_year/104/104700/2022.csv`
- `atlas/ohlcv_tradable_by_symbol_year/104/104700/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/104/104700/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/104/104700/2025.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005010/2023.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005010/2024.csv`
- `atlas/ohlcv_tradable_by_symbol_year/005/005010/2025.csv`

Evidence URLs:

- FerroTimes, 2021 rebar demand/spread report summary: `https://www.ferrotimes.com/news/articleView.html?idxno=9393`
- Husteel company press page: `https://www.husteel.com/pr/press/view.hu?page=1&perPageNum=10&pk_id=205`
- Steel & Metal News, Korea Steel Q1 2024 deterioration: `https://www.snmnews.com/news/articleView.html?idxno=535189`
