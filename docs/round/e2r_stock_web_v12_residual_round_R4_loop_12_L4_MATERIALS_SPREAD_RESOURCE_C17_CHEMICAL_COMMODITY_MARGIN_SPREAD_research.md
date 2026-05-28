# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R4
scheduled_loop: 12
completed_round: R4
completed_loop: 12
next_round: R5
next_loop: 12
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_SPREAD_TO_MARGIN_BRIDGE
output_file: e2r_stock_web_v12_residual_round_R4_loop_12_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 4 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

## 1. Current Calibrated Profile Assumption

Current proxy: `e2r_2_1_stock_web_calibrated`.

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

This file does not re-prove those global axes. It stress-tests them in the commodity-spread domain and proposes a C17-specific shadow rule.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R4
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = CHEMICAL_SPREAD_TO_MARGIN_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | green_strictness_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression
```

R4 is valid for `L4_MATERIALS_SPREAD_RESOURCE`. The selected canonical archetype is C17 because the dominant mechanism is whether commodity spread moves into margin bridge, revision, and sustainable financial visibility.

## 3. Previous Coverage / Duplicate Avoidance Check

Previous v12 local state ended at `R3 / loop 12` with `next_round = R4`. Repository-side v12 files were not found during this run, so the local conversation state is used for schedule continuity.

```text
same_symbol_same_trigger_date_research = avoided
same_canonical_archetype_research = allowed
new_symbol_count = 4
new_trigger_family_count = 4
reused_case_count = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

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
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
schema_path = atlas/schema.json
universe_path = atlas/universe/all_symbols.csv
```

The price basis is `tradable_raw`, not adjusted close. Corporate-action contaminated windows are blocked when overlapping the forward calibration window.

## 5. Historical Eligibility Gate

```text
trigger_date_is_historical = true
entry_date_exists_in_stock_web_tradable_shard = true
forward_180D_available_by_manifest_max_date = true
OHLCV_fields_present = true
corporate_action_contaminated_180D_window = false
calibration_usable_case_count = 4
calibration_usable_trigger_count = 6
```

`011170` has a corporate-action candidate date on `2023-02-13`; the representative entry used here is `2023-03-02`, so the 180D calibration window is after the candidate date and is treated as clean for this study.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression rationale |
|---|---|---|
| SPANDEX_SUPERCYCLE_MARGIN_BRIDGE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Commodity spread turns into margin bridge and revision. |
| NB_LATEX_SYNTHETIC_RUBBER_SPREAD | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Spread and demand shock produce operating leverage. |
| NCC_REOPENING_REBOUND_FALSE_POSITIVE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Headline macro rebound without spread/margin bridge is a C17 counterexample. |
| STANDALONE_NCC_OVER_CAPACITY_GUARD | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Oversupply/utilization risk blocks Stage2 promotion. |

## 7. Case Selection Summary

| case_id | symbol | company_name | case_type | positive_or_counterexample | best_trigger | current_profile_verdict | notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R4L12-C17-HTNC-SPANDEX-2021 | 298020 | 효성티앤씨 | structural_success | positive | R4L12-C17-HTNC-S2-20210104 | current_profile_correct | 스판덱스 가격/스프레드 호황이 실제 이익과 주가 경로로 번역된 positive. 단, 4B는 price-only peak가 아니라 non-price slowdown 확인 필요. |
| R4L12-C17-KKPC-NB-LATEX-2021 | 011780 | 금호석유화학 | structural_success | positive | R4L12-C17-KKPC-S2-20210104 | current_profile_correct | NB latex/synthetic rubber spread and operating leverage produced fast rerating, but peak came quickly; 4B overlay should watch spread normalization. |
| R4L12-C17-LOTTE-NCC-2023 | 011170 | 롯데케미칼 | failed_rerating | counterexample | R4L12-C17-LOTTE-S2-20230302 | current_profile_false_positive | 중국 리오프닝/화학 rebound narrative alone failed because NCC spread, utilization, and margin bridge were not sufficiently confirmed. |
| R4L12-C17-KPIC-NCC-2023 | 006650 | 대한유화 | failed_rerating | counterexample | R4L12-C17-KPIC-S2-20230302 | current_profile_false_positive | standalone NCC rebound narrative lacked durable spread/margin bridge; price path rolled over sharply. |


## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 4
```

The positive cases show that C17 can generate large MFE when spread evidence is already becoming margin and revision evidence. The counterexamples show that a broad reopening/rebound headline is not enough. In C17, the spread is the engine oil; price action is only the sound of the engine. If the oil is not actually flowing into margins, the sound alone is not a signal.

## 9. Evidence Source Map

| case_id | evidence family | evidence source note | scoring use |
|---|---|---|---|
| R4L12-C17-HTNC-SPANDEX-2021 | spandex spread + operating leverage | stock-web OHLC confirmed explosive repricing; product exposure cross-check used | positive structural |
| R4L12-C17-KKPC-NB-LATEX-2021 | NB latex/synthetic rubber spread | stock-web OHLC confirmed rapid repricing; product exposure cross-check used | positive structural |
| R4L12-C17-LOTTE-NCC-2023 | China reopening/NCC rebound headline | stock-web OHLC showed failed rerating; sector overcapacity context used | counterexample |
| R4L12-C17-KPIC-NCC-2023 | standalone NCC rebound headline | stock-web OHLC showed low MFE/high MAE | counterexample |

External context used only as narrative support; quantitative calibration is based on stock-web OHLC rows.

## 10. Price Data Source Map

| symbol | company_name | profile_path | price_shard_path | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | clean_180D_window | True |
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | clean_180D_window | True |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | atlas/ohlcv_tradable_by_symbol_year/011/011170/2023.csv | clean_180D_window_after_2023-02-13_candidate | True |
| 006650 | 대한유화 | atlas/symbol_profiles/006/006650.json | atlas/ohlcv_tradable_by_symbol_year/006/006650/2023.csv | clean_180D_window | True |


## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | company_name | trigger_type | trigger_date | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | trigger_outcome_label | current_profile_verdict | dedupe_for_aggregate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L12-C17-HTNC-S2-20210104 | 298020 | 효성티앤씨 | Stage2-Actionable | 2021-01-04 | 2021-01-04 | 213000 | 280.28 | -3.29 | 352.11 | -3.29 | structural_success_high_MFE | current_profile_correct | True |
| R4L12-C17-HTNC-GREEN-20210325 | 298020 | 효성티앤씨 | Stage3-Green | 2021-03-25 | 2021-03-25 | 591000 | 62.94 | -8.63 | 62.94 | -13.71 | green_valid_but_late | current_profile_too_late | False |
| R4L12-C17-HTNC-4B-20210716 | 298020 | 효성티앤씨 | Stage4B | 2021-07-16 | 2021-07-16 | 881000 | 9.31 | -28.72 | 9.31 | -42.11 | 4B_overlay_success_but_not_full_4B_without_non_price | current_profile_4B_too_early | False |
| R4L12-C17-KKPC-S2-20210104 | 011780 | 금호석유화학 | Stage2-Actionable | 2021-01-04 | 2021-01-04 | 151000 | 97.68 | -5.96 | 97.68 | -5.96 | structural_success_high_MFE | current_profile_correct | True |
| R4L12-C17-LOTTE-S2-20230302 | 011170 | 롯데케미칼 | Stage2-Actionable | 2023-03-02 | 2023-03-02 | 184000 | 5.6 | -18.53 | 5.6 | -31.3 | failed_rerating_low_MFE_high_MAE | current_profile_false_positive | True |
| R4L12-C17-KPIC-S2-20230302 | 006650 | 대한유화 | Stage2-Actionable | 2023-03-02 | 2023-03-02 | 181500 | 2.87 | -28.1 | 2.87 | -28.98 | failed_rerating_low_MFE_high_MAE | current_profile_false_positive | True |


## 12. Trigger-Level OHLC Backtest Tables

Representative trigger backtest:

| trigger_id | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L12-C17-HTNC-S2-20210104 | 2021-01-04 | 213000 | 136.15 | -3.29 | 280.28 | -3.29 | 352.11 | -3.29 | 2021-07-16 | 963000 | -47.04 |
| R4L12-C17-KKPC-S2-20210104 | 2021-01-04 | 151000 | 94.37 | -5.96 | 97.68 | -5.96 | 97.68 | -5.96 | 2021-05-06 | 298500 | -32.16 |
| R4L12-C17-LOTTE-S2-20230302 | 2023-03-02 | 184000 | 5.6 | -6.52 | 5.6 | -18.53 | 5.6 | -31.3 | 2023-03-31 | 194300 | -34.95 |
| R4L12-C17-KPIC-S2-20230302 | 2023-03-02 | 181500 | 2.87 | -15.54 | 2.87 | -28.1 | 2.87 | -28.98 | 2023-03-02 | 186700 | -30.96 |


Label-comparison / overlay trigger backtest:

| trigger_id | trigger_type | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | green_lateness_ratio | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L12-C17-HTNC-GREEN-20210325 | Stage3-Green | 2021-03-25 | 591000 | 62.94 | -8.63 | 0.504 |  |  | not_4B_entry |
| R4L12-C17-HTNC-4B-20210716 | Stage4B | 2021-07-16 | 881000 | 9.31 | -28.72 | not_applicable | 0.891 | 0.891 | price_only_local_4B_needs_non_price_confirmation |


## 13. Current Calibrated Profile Stress Test

| case_id | current profile likely judgment | actual path | verdict |
|---|---|---|---|
| R4L12-C17-HTNC-SPANDEX-2021 | Stage2/Yellow promoted because spread and revision clues align | very high MFE with tolerable early MAE | current_profile_correct |
| R4L12-C17-KKPC-NB-LATEX-2021 | Stage2/Yellow promoted because spread and demand shock align | high MFE but fast peak | current_profile_correct |
| R4L12-C17-LOTTE-NCC-2023 | could be overpromoted if reopening rebound is scored as actionable | low MFE, high MAE | current_profile_false_positive |
| R4L12-C17-KPIC-NCC-2023 | could be overpromoted if standalone NCC rebound is scored as actionable | very low MFE, high MAE | current_profile_false_positive |

```text
stage2_actionable_evidence_bonus = existing_axis_tested / sector-specific overpromotion risk found
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_strengthened for C17
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_strengthened
```

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2_Actionable entry = 2021-01-04 close 213000
Stage3_Green comparison entry = 2021-03-25 close 591000
Stage2 peak = 963000
green_lateness_ratio = (591000 - 213000) / (963000 - 213000) = 0.504
```

Interpretation: C17 Green is valid but meaningfully late in a supercycle. Stage2/Yellow is the economically important entry when spread-to-margin bridge is already visible.

## 15. 4B Local vs Full-window Timing Audit

```text
Stage2 entry = 213000
4B overlay entry = 881000
full-window peak = 963000
four_b_local_peak_proximity = 0.891
four_b_full_window_peak_proximity = 0.891
```

Verdict: price-only local 4B was near the actual peak, but the research rule should not treat it as full 4B unless spread/revision slowdown, inventory pressure, or customer-demand weakening is visible. The existing full 4B non-price requirement is strengthened.

## 16. 4C Protection Audit

| case_id | 4C label | reason |
|---|---|---|
| R4L12-C17-LOTTE-NCC-2023 | hard_4c_success | thesis broke because margin bridge did not follow reopening narrative; MAE_180D was -31.30%. |
| R4L12-C17-KPIC-NCC-2023 | hard_4c_success | standalone NCC rebound failed; MAE_180D was -28.98%. |
| R4L12-C17-HTNC-SPANDEX-2021 | thesis_break_watch_only | 4B was closer than 4C; price-only peak was insufficient for full 4B at trigger time. |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

R4 has broader materials archetypes beyond chemical spread. The evidence is strong enough for a C17 canonical rule candidate, but not broad enough for all L4 materials.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_name = C17_spread_to_margin_bridge_gate
```

Proposed shadow-only rule:

```text
For C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:
    if evidence is only macro reopening / commodity rebound / price bounce:
        cap at Stage2-Watch
    if spread improvement has margin_bridge_score >= 15 and revision_score >= 10:
        allow Stage2-Actionable / Stage3-Yellow
    if revision_score >= 58 proxy and financial visibility is confirmed:
        allow Stage3-Green
    if valuation blowoff is price-only:
        4B-Watch only, not full 4B
```

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | avg_MFE_90D_pct | avg_MAE_90D_pct | false_positive_rate | score_return_alignment_verdict |
| --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy |  | 96.61 | -13.97 | 2/4 | mixed: positive supercycle works, NCC rebound false positives remain |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback_reference_only | 96.61 | -13.97 | 2/4_or_higher | weaker than P0 because NCC rebound would be overpromoted |
| P1_sector_specific_candidate_profile | sector_specific | L4_margin_bridge_required_for_actionable | 96.61 | -13.97 | 0/4_if_guard_applied | better alignment by blocking NCC false positives |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | C17_spread_to_margin_bridge_gate, C17_standalone_NCC_counterexample_guard | 96.61 | -13.97 | 0/4_if_guard_applied | best fit for this loop |
| P3_counterexample_guard_profile | counterexample_guard | price_or_macro_only_rebound_blocks_actionable | 4.23 | -23.32 | 0/2_counterexamples | guard profile catches both counterexamples |


## 20. Score-Return Alignment Matrix

| trigger_id | before_score | before_stage | after_score | after_stage | alignment |
|---|---:|---|---:|---|---|
| R4L12-C17-HTNC-S2-20210104 | 82 | Stage3-Yellow | 89 | Stage3-Green | structural_success_high_MFE |
| R4L12-C17-HTNC-GREEN-20210325 | 91 | Stage3-Green | 91 | Stage3-Green | green_valid_but_late |
| R4L12-C17-HTNC-4B-20210716 | 72 | 4B-Watch | 76 | 4B-Watch | 4B_overlay_success_but_not_full_4B_without_non_price |
| R4L12-C17-KKPC-S2-20210104 | 79 | Stage3-Yellow | 86 | Stage3-Yellow+ | structural_success_high_MFE |
| R4L12-C17-LOTTE-S2-20230302 | 76 | Stage3-Yellow | 63 | Stage2-Watch | failed_rerating_low_MFE_high_MAE |
| R4L12-C17-KPIC-S2-20230302 | 74 | Stage2-Actionable | 59 | Stage2-Watch | failed_rerating_low_MFE_high_MAE |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_SPREAD_TO_MARGIN_BRIDGE | 2 | 2 | 1 | 2 | 4 | 0 | 6 | 4 | 2 | False | True | C17 still needs non-Korea/global commodity holdout, but Korean NCC false-positive gap reduced. |


## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - standalone_NCC_reopening_false_positive
  - spread_headline_without_margin_bridge
  - price_only_4B_peak_needs_non_price_confirmation
new_axis_proposed:
  - C17_spread_to_margin_bridge_gate
  - C17_standalone_NCC_headline_guard
existing_axis_strengthened:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date = 2026-02-20
- profile files for 298020, 011780, 011170, 006650
- tradable OHLC rows for representative windows
- 30D / 90D / 180D MFE and MAE from actual stock-web row excerpts
- duplicate avoidance against local v12 state
```

Not validated:

```text
- live 2026 candidate scan
- stock_agent code implementation
- production scoring patch
- adjusted-price reconciliation
- full external analyst-report text extraction
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_spread_to_margin_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require spread-to-margin bridge before Stage2-Actionable/Green in chemical commodity cycles","blocks LOTTE/KPIC false positives while preserving HTNC/KKPC positives","R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_standalone_NCC_headline_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Standalone NCC reopening/headline rebound without spread confirmation should remain watch-only","reduces false-positive risk in high-overcapacity cycles","R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L12-C17-HTNC-S2-20210104", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "스판덱스 가격/스프레드 호황이 실제 이익과 주가 경로로 번역된 positive. 단, 4B는 price-only peak가 아니라 non-price slowdown 확인 필요."}
{"row_type": "case", "case_id": "R4L12-C17-KKPC-NB-LATEX-2021", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L12-C17-KKPC-S2-20210104", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "NB latex/synthetic rubber spread and operating leverage produced fast rerating, but peak came quickly; 4B overlay should watch spread normalization."}
{"row_type": "case", "case_id": "R4L12-C17-LOTTE-NCC-2023", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L12-C17-LOTTE-S2-20230302", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "중국 리오프닝/화학 rebound narrative alone failed because NCC spread, utilization, and margin bridge were not sufficiently confirmed."}
{"row_type": "case", "case_id": "R4L12-C17-KPIC-NCC-2023", "symbol": "006650", "company_name": "대한유화", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R4L12-C17-KPIC-S2-20230302", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "standalone NCC rebound narrative lacked durable spread/margin bridge; price path rolled over sharply."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L12-C17-HTNC-S2-20210104", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "symbol": "298020", "company_name": "효성티앤씨", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-04", "entry_date": "2021-01-04", "entry_price": 213000, "evidence_available_at_that_date": "스판덱스 가격 상승과 tight supply narrative가 이미 형성되었고, 2021년 초 가격경로가 earnings revision을 선반영하기 시작함.", "evidence_source": "historical public reports + stock-web OHLC validation; company identity/product exposure cross-check via public profile", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "MFE_30D_pct": 136.15, "MFE_90D_pct": 280.28, "MFE_180D_pct": 352.11, "MFE_1Y_pct": 352.11, "MFE_2Y_pct": null, "MAE_30D_pct": -3.29, "MAE_90D_pct": -3.29, "MAE_180D_pct": -3.29, "MAE_1Y_pct": -3.29, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -47.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-HTNC-20210104", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 15, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 17, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "component_delta_explanation": "스프레드가 실제 영업레버리지로 번역되는 증거가 붙을 때 C17에서 Green을 허용.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L12-C17-HTNC-GREEN-20210325", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "symbol": "298020", "company_name": "효성티앤씨", "trigger_type": "Stage3-Green", "trigger_date": "2021-03-25", "entry_date": "2021-03-25", "entry_price": 591000, "evidence_available_at_that_date": "가격경로와 실적 기대가 이미 상당 부분 반영된 뒤의 확인형 Green 후보.", "evidence_source": "stock-web OHLC validation; historical earnings-revision proxy", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "MFE_30D_pct": 29.78, "MFE_90D_pct": 62.94, "MFE_180D_pct": 62.94, "MFE_1Y_pct": 62.94, "MFE_2Y_pct": null, "MAE_30D_pct": -8.63, "MAE_90D_pct": -8.63, "MAE_180D_pct": -13.71, "MAE_1Y_pct": -13.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -47.04, "green_lateness_ratio": 0.504, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_valid_but_late", "current_profile_verdict": "current_profile_too_late", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-HTNC-20210325", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same case green-lateness audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 91, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "component_delta_explanation": "Green 자체는 맞았지만 C17 supercycle에서는 Stage2/Yellow가 경제적으로 더 유효한 진입.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L12-C17-HTNC-4B-20210716", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "symbol": "298020", "company_name": "효성티앤씨", "trigger_type": "Stage4B", "trigger_date": "2021-07-16", "entry_date": "2021-07-16", "entry_price": 881000, "evidence_available_at_that_date": "local blowoff/valuation overheat. non-price slowdown evidence is not treated as fully confirmed at the exact peak.", "evidence_source": "stock-web OHLC validation", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "MFE_30D_pct": 9.31, "MFE_90D_pct": 9.31, "MFE_180D_pct": 9.31, "MFE_1Y_pct": 9.31, "MFE_2Y_pct": null, "MAE_30D_pct": -18.73, "MAE_90D_pct": -28.72, "MAE_180D_pct": -42.11, "MAE_1Y_pct": -42.11, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -47.04, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.891, "four_b_full_window_peak_proximity": 0.891, "four_b_timing_verdict": "price_only_local_4B_needs_non_price_confirmation", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_but_not_full_4B_without_non_price", "current_profile_verdict": "current_profile_4B_too_early", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-HTNC-20210716", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same case 4B overlay timing audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 28, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "4B-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 28, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "4B-Watch", "component_delta_explanation": "가격상 고점 근접은 맞았지만 full 4B에는 spread/revision slowdown 같은 non-price evidence가 필요.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L12-C17-KKPC-S2-20210104", "case_id": "R4L12-C17-KKPC-NB-LATEX-2021", "symbol": "011780", "company_name": "금호석유화학", "trigger_type": "Stage2-Actionable", "trigger_date": "2021-01-04", "entry_date": "2021-01-04", "entry_price": 151000, "evidence_available_at_that_date": "NB latex / synthetic rubber spread narrative and early relative strength.", "evidence_source": "stock-web OHLC validation; synthetic-rubber product exposure cross-check", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "MFE_30D_pct": 94.37, "MFE_90D_pct": 97.68, "MFE_180D_pct": 97.68, "MFE_1Y_pct": 97.68, "MFE_2Y_pct": null, "MAE_30D_pct": -5.96, "MAE_90D_pct": -5.96, "MAE_180D_pct": -5.96, "MAE_1Y_pct": -5.96, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-KKPC-20210104", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow+", "component_delta_explanation": "spread-to-margin bridge가 있으면 Stage2 promotion은 유효하나, Green은 revision quality 확인 후 제한.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L12-C17-LOTTE-S2-20230302", "case_id": "R4L12-C17-LOTTE-NCC-2023", "symbol": "011170", "company_name": "롯데케미칼", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-02", "entry_date": "2023-03-02", "entry_price": 184000, "evidence_available_at_that_date": "China reopening / petrochemical rebound narrative, but no durable NCC spread-to-margin confirmation.", "evidence_source": "stock-web OHLC validation; petrochemical overcapacity context later confirmed by sector restructuring reports", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2023.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "MFE_30D_pct": 5.6, "MFE_90D_pct": 5.6, "MFE_180D_pct": 5.6, "MFE_1Y_pct": 5.6, "MFE_2Y_pct": null, "MAE_30D_pct": -6.52, "MAE_90D_pct": -18.53, "MAE_180D_pct": -31.3, "MAE_1Y_pct": -31.3, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-31", "peak_price": 194300, "drawdown_after_peak_pct": -34.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "corporate_action_window_status": "clean_180D_window_after_2023-02-13_candidate", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-LOTTE-20230302", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 0, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 0, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "headline rebound가 있어도 spread confirmation과 utilization evidence가 없으면 C17 Stage2-Actionable bonus를 제한.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
{"row_type": "trigger", "trigger_id": "R4L12-C17-KPIC-S2-20230302", "case_id": "R4L12-C17-KPIC-NCC-2023", "symbol": "006650", "company_name": "대한유화", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-03-02", "entry_date": "2023-03-02", "entry_price": 181500, "evidence_available_at_that_date": "standalone NCC rebound narrative, but no durable spread or balance-sheet margin bridge confirmation.", "evidence_source": "stock-web OHLC validation; petrochemical overcapacity context", "stage2_evidence_fields": ["policy_or_regulatory_optionality"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006650/2023.csv", "profile_path": "atlas/symbol_profiles/006/006650.json", "MFE_30D_pct": 2.87, "MFE_90D_pct": 2.87, "MFE_180D_pct": 2.87, "MFE_1Y_pct": 2.87, "MFE_2Y_pct": null, "MAE_30D_pct": -15.54, "MAE_90D_pct": -28.1, "MAE_180D_pct": -28.98, "MAE_1Y_pct": -28.98, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-03-02", "peak_price": 186700, "drawdown_after_peak_pct": -30.96, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_entry", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "corporate_action_window_status": "clean_180D_window", "forward_window_trading_days": 180, "calibration_usable": true, "same_entry_group_id": "R4L12-C17-KPIC-20230302", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 0, "execution_risk_score": 19, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage2-Watch", "component_delta_explanation": "순수 spread rebound 기대는 margin bridge evidence 없이 Stage2-Actionable로 올리지 않는다.", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "fine_archetype_id": "CHEMICAL_SPREAD_TO_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "chemical commodity margin spread", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "calibration_block_reasons": []}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "trigger_id": "R4L12-C17-HTNC-S2-20210104", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 15, "relative_strength_score": 14, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 17, "relative_strength_score": 15, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "스프레드가 실제 영업레버리지로 번역되는 증거가 붙을 때 C17에서 Green을 허용.", "MFE_90D_pct": 280.28, "MAE_90D_pct": -3.29, "score_return_alignment_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "trigger_id": "R4L12-C17-HTNC-GREEN-20210325", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 91, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 22, "revision_score": 20, "relative_strength_score": 13, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "Green 자체는 맞았지만 C17 supercycle에서는 Stage2/Yellow가 경제적으로 더 유효한 진입.", "MFE_90D_pct": 62.94, "MAE_90D_pct": -8.63, "score_return_alignment_label": "green_valid_but_late", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-HTNC-SPANDEX-2021", "trigger_id": "R4L12-C17-HTNC-4B-20210716", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 28, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "4B-Watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 28, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 76, "stage_label_after": "4B-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "가격상 고점 근접은 맞았지만 full 4B에는 spread/revision slowdown 같은 non-price evidence가 필요.", "MFE_90D_pct": 9.31, "MAE_90D_pct": -28.72, "score_return_alignment_label": "4B_overlay_success_but_not_full_4B_without_non_price", "current_profile_verdict": "current_profile_4B_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-KKPC-NB-LATEX-2021", "trigger_id": "R4L12-C17-KKPC-S2-20210104", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 12, "relative_strength_score": 13, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 15, "relative_strength_score": 13, "customer_quality_score": 5, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow+", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "spread-to-margin bridge가 있으면 Stage2 promotion은 유효하나, Green은 revision quality 확인 후 제한.", "MFE_90D_pct": 97.68, "MAE_90D_pct": -5.96, "score_return_alignment_label": "structural_success_high_MFE", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-LOTTE-NCC-2023", "trigger_id": "R4L12-C17-LOTTE-S2-20230302", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 2, "relative_strength_score": 8, "customer_quality_score": 0, "policy_or_regulatory_score": 9, "valuation_repricing_score": 0, "execution_risk_score": 13, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 5, "customer_quality_score": 0, "policy_or_regulatory_score": 7, "valuation_repricing_score": 0, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 63, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "headline rebound가 있어도 spread confirmation과 utilization evidence가 없으면 C17 Stage2-Actionable bonus를 제한.", "MFE_90D_pct": 5.6, "MAE_90D_pct": -18.53, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L12-C17-KPIC-NCC-2023", "trigger_id": "R4L12-C17-KPIC-S2-20230302", "symbol": "006650", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 2, "revision_score": 1, "relative_strength_score": 7, "customer_quality_score": 0, "policy_or_regulatory_score": 8, "valuation_repricing_score": 0, "execution_risk_score": 14, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 74, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 4, "customer_quality_score": 0, "policy_or_regulatory_score": 6, "valuation_repricing_score": 0, "execution_risk_score": 19, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 59, "stage_label_after": "Stage2-Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score"], "component_delta_explanation": "순수 spread rebound 기대는 margin bridge evidence 없이 Stage2-Actionable로 올리지 않는다.", "MFE_90D_pct": 2.87, "MAE_90D_pct": -28.1, "score_return_alignment_label": "failed_rerating_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 profile_comparison rows

```jsonl
{"profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "현재 global calibrated profile을 그대로 적용.", "changed_axes": [], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302", "avg_MFE_90D_pct": 96.61, "avg_MAE_90D_pct": -13.97, "avg_MFE_180D_pct": 114.57, "avg_MAE_180D_pct": -17.38, "false_positive_rate": "2/4", "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.504, "avg_four_b_local_peak_proximity": 0.891, "avg_four_b_full_window_peak_proximity": 0.891, "score_return_alignment_verdict": "mixed: positive supercycle works, NCC rebound false positives remain"}
{"profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "baseline reference: weaker guard on price/rebound narratives.", "changed_axes": ["rollback_reference_only"], "changed_thresholds": {}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302", "avg_MFE_90D_pct": 96.61, "avg_MAE_90D_pct": -13.97, "avg_MFE_180D_pct": 114.57, "avg_MAE_180D_pct": -17.38, "false_positive_rate": "2/4_or_higher", "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.504, "avg_four_b_local_peak_proximity": 0.891, "avg_four_b_full_window_peak_proximity": 0.891, "score_return_alignment_verdict": "weaker than P0 because NCC rebound would be overpromoted"}
{"profile_id": "P1_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "L4 소재는 commodity spread headline보다 margin bridge / utilization confirmation을 우선.", "changed_axes": ["L4_margin_bridge_required_for_actionable"], "changed_thresholds": {"stage2_actionable_without_margin_bridge_max": "Stage2-Watch"}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302", "avg_MFE_90D_pct": 96.61, "avg_MAE_90D_pct": -13.97, "avg_MFE_180D_pct": 114.57, "avg_MAE_180D_pct": -17.38, "false_positive_rate": "0/4_if_guard_applied", "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.504, "avg_four_b_local_peak_proximity": 0.891, "avg_four_b_full_window_peak_proximity": 0.891, "score_return_alignment_verdict": "better alignment by blocking NCC false positives"}
{"profile_id": "P2_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C17 requires spread-to-margin bridge + revision confirmation; otherwise rebound narratives remain watch-only.", "changed_axes": ["C17_spread_to_margin_bridge_gate", "C17_standalone_NCC_counterexample_guard"], "changed_thresholds": {"C17_green_revision_min": 58, "C17_actionable_margin_bridge_min": 15}, "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302", "avg_MFE_90D_pct": 96.61, "avg_MAE_90D_pct": -13.97, "avg_MFE_180D_pct": 114.57, "avg_MAE_180D_pct": -17.38, "false_positive_rate": "0/4_if_guard_applied", "missed_structural_count": 0, "late_green_count": 1, "avg_green_lateness_ratio": 0.504, "avg_four_b_local_peak_proximity": 0.891, "avg_four_b_full_window_peak_proximity": 0.891, "score_return_alignment_verdict": "best fit for this loop"}
{"profile_id": "P3_counterexample_guard_profile", "profile_scope": "counterexample_guard", "profile_hypothesis": "If spread recovery is only macro/headline with no margin bridge, no Stage2-Actionable promotion.", "changed_axes": ["price_or_macro_only_rebound_blocks_actionable"], "changed_thresholds": {"headline_rebound_only_score_cap": 63}, "eligible_trigger_count": 2, "selected_entry_trigger_per_case": "R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302", "avg_MFE_90D_pct": 4.23, "avg_MAE_90D_pct": -23.32, "avg_MFE_180D_pct": 4.23, "avg_MAE_180D_pct": -30.14, "false_positive_rate": "0/2_counterexamples", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": "not_applicable", "avg_four_b_local_peak_proximity": "not_applicable", "avg_four_b_full_window_peak_proximity": "not_applicable", "score_return_alignment_verdict": "guard profile catches both counterexamples"}
```

### 25.6 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_spread_to_margin_bridge_gate,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Require spread-to-margin bridge before Stage2-Actionable/Green in chemical commodity cycles","blocks LOTTE/KPIC false positives while preserving HTNC/KKPC positives","R4L12-C17-HTNC-S2-20210104|R4L12-C17-KKPC-S2-20210104|R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_standalone_NCC_headline_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Standalone NCC reopening/headline rebound without spread confirmation should remain watch-only","reduces false-positive risk in high-overcapacity cycles","R4L12-C17-LOTTE-S2-20230302|R4L12-C17-KPIC-S2-20230302",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.7 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "12", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD", "scheduled_round": "R4", "scheduled_loop": "12", "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "positive_case_count": 2, "counterexample_count": 2, "current_profile_error_count": 2, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["standalone_NCC_reopening_false_positive", "spread_headline_without_margin_bridge", "price_only_4B_peak_needs_non_price_confirmation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.8 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R4L12-C17-KOREA-PETROCHEM-RESTRUCTURING-2025","symbol":"MULTI","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"sector_overcapacity_context_after_manifest_window_not_used_for_weight_calibration","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 12
next_round = R5
next_loop = 12
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source notes:

- `atlas/manifest.json`: manifest max_date, row counts, markets, shard roots.
- `atlas/symbol_profiles/298/298020.json`: HTNC profile, zero corporate-action candidates in window.
- `atlas/symbol_profiles/011/011780.json`: KKPC profile, no 2021 corporate-action overlap.
- `atlas/symbol_profiles/011/011170.json`: Lotte profile, 2023-02-13 candidate; representative window starts 2023-03-02.
- `atlas/symbol_profiles/006/006650.json`: KPIC profile, no 2023 corporate-action overlap.
- `atlas/ohlcv_tradable_by_symbol_year/*/*/*.csv`: actual tradable raw OHLC rows.

External context notes:

- Public company and encyclopedia/industry pages were used only to cross-check product exposure.
- Public Reuters sector restructuring context was used only as narrative overcapacity context, not as quantitative calibration evidence.
- No live candidate discovery was performed.

