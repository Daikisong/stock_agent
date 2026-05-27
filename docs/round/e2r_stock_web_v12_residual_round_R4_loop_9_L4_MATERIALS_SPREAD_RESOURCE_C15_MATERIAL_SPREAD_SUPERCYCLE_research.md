# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
round = R4
loop = 9
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = SPANDEX_NB_LATEX_NCC_PDH_PRODUCT_SPREAD_MARGIN_BRIDGE
output_file = e2r_stock_web_v12_residual_round_R4_loop_9_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This file is historical calibration research only. It is not a live candidate scan, investment recommendation, trading signal, or repository patch.

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

The loop does not re-prove those global axes. It stress-tests whether C15 needs a product-spread-specific bridge and a broad-commodity false-Green guard.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R4
loop = 9
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id = SPANDEX_NB_LATEX_NCC_PDH_PRODUCT_SPREAD_MARGIN_BRIDGE
loop_objective = coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; canonical_archetype_compression; green_strictness_stress_test; 4B_non_price_requirement_stress_test
selection_mode = auto_coverage_gap_fill
```

C15 is treated as a material spread archetype, not a contract/backlog archetype. The market mechanism is: raw material or product spread widens -> unit margin expands -> earnings revision accelerates -> valuation rerates. The failure mode is that broad commodity beta or reopening narrative looks similar on price, but the margin bridge never closes.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent artifacts were used only for registry/coverage inspection. The registry shows R4 materials spread loops already exist through loop 8, while recent R9/C29 work was separate mobility volume/margin research. This loop therefore uses `R4 / loop 9` and selects a C15 sub-basket not overlapping the immediately preceding R9/C29 output.

```text
auto_selected_coverage_gap =
  R4/C15 had prior materials-spread coverage, but v12 still needed:
  - product-specific chemical spread positives,
  - broad commodity spread false-Green counterexamples,
  - 4B overlay before Green in capex/debt-heavy commodity names,
  - canonical compression into C15 rather than separate fine-archetype drift.
```

Novelty rule:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 4
required_new_independent_case_ratio = 1.00
```

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest validation:

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
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

Validation note: stock-web is raw/unadjusted. 180D windows are blocked if a corporate-action candidate overlaps. 1Y/2Y fields are marked null if a later corporate-action candidate contaminates the longer window but not the 180D calibration window.

## 5. Historical Eligibility Gate

All representative triggers satisfy:

```text
trigger_date_is_historical = true
entry_date_exists_in_tradable_shard = true
forward_180D_exists_by_manifest_max_date = true
OHLCV_fields_present = true
MFE_30D_90D_180D_calculated = true
MAE_30D_90D_180D_calculated = true
corporate_action_contaminated_180D_window = false
```

Blocked longer windows:

```text
011170 롯데케미칼: profile has 2023-02-13 corporate-action candidate, so 2Y fields are not used for calibration.
011780 금호석유화학: profile has 2001-01-16 candidate, outside tested window; 180D window remains usable.
```

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SPANDEX_SUPPLY_TIGHTNESS_MARGIN_BRIDGE | C15_MATERIAL_SPREAD_SUPERCYCLE | product spread and unit margin bridge replace backlog/order bridge |
| NB_LATEX_RUBBER_SPREAD_SUPERCYCLE | C15_MATERIAL_SPREAD_SUPERCYCLE | product-specific demand shock -> spread -> earnings revision |
| NCC_COMMODITY_SPREAD_VOLUME_WITHOUT_DURABLE_MARGIN | C15_MATERIAL_SPREAD_SUPERCYCLE | same sector, but broad spread narrative without durable margin is counterexample |
| PDH_PP_SPREAD_WITH_CAPEX_EXECUTION_RISK | C15_MATERIAL_SPREAD_SUPERCYCLE | spread narrative must be haircut by capex/plant/debt execution risk |

## 7. Case Selection Summary

| case_id | symbol | company_name | role | entry | MFE90 | MAE90 | MFE180 | MAE180 | current |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE | 298020 | 효성티앤씨 | structural_success | 2020-11-02 @ 155500 | 223.47 | -5.47 | 519.29 | -5.47 | current_profile_too_late |
| R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE | 011780 | 금호석유화학 | structural_success | 2020-08-10 @ 97200 | 61.01 | -4.73 | 207.1 | -4.73 | current_profile_too_late |
| R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN | 011170 | 롯데케미칼 | false_positive_green | 2021-03-02 @ 323500 | 4.48 | -22.72 | 4.48 | -27.36 | current_profile_false_positive |
| R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN | 298000 | 효성화학 | false_positive_green | 2021-04-26 @ 446500 | 6.38 | -30.12 | 6.38 | -47.03 | current_profile_false_positive |


Selection balance:

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 2
4C_case_count = 2
calibration_usable_case_count = 4
```

## 8. Positive vs Counterexample Balance

Positive cases show explosive MFE with low initial MAE when the spread is product-specific and directly connected to reported or near-term revision evidence.

```text
positive_avg_MFE_90D_pct = 142.24
positive_avg_MAE_90D_pct = -5.1
positive_avg_MFE_180D_pct = 363.19
positive_avg_MAE_180D_pct = -5.1
```

Counterexamples show limited upside and deep drawdown when the evidence is broad commodity beta or capex-heavy execution risk.

```text
counterexample_avg_MFE_90D_pct = 5.43
counterexample_avg_MAE_90D_pct = -26.42
counterexample_avg_MFE_180D_pct = 5.43
counterexample_avg_MAE_180D_pct = -37.2
```

## 9. Evidence Source Map

| case_id | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
|---|---|---|---|---|
| R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE | 스판덱스 수급 tightness, relative strength, early revision | margin bridge, financial visibility | none primary | watch only |
| R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE | NB latex demand shock, relative strength, early revision | margin bridge, financial visibility | valuation/revision fatigue after blowoff | watch only |
| R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN | broad NCC spread narrative, relative strength | weak; multiple public sources but no product bridge | price-only local peak + valuation fatigue | thesis evidence broken |
| R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN | PDH/PP spread/capacity story, relative strength | weak; capex execution not resolved | valuation/positioning/execution risk | thesis evidence broken |

## 10. Price Data Source Map

| symbol | profile_path | tradable_shard_path | corporate action window status |
|---|---|---|---|
| 298020 | atlas/symbol_profiles/298/298020.json | atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv + 2021.csv | clean_180D_window |
| 011780 | atlas/symbol_profiles/011/011780.json | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv + 2021.csv | clean_180D_window; 2001-01-16 candidate outside tested window |
| 011170 | atlas/symbol_profiles/011/011170.json | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | clean_180D_window; 2Y not used due later corporate-action candidate |
| 298000 | atlas/symbol_profiles/298/298000.json | atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 | stage3 | 4B | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L9_C15_298020_T1 | 298020 | Stage2-Actionable | 2020-10-30 | 2020-11-02 | 155500 | public_event_or_disclosure, capacity_or_volume_route, relative_strength, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources |  | structural_success_high_mfe_low_initial_mae |
| R4L9_C15_011780_T1 | 011780 | Stage2-Actionable | 2020-08-07 | 2020-08-10 | 97200 | public_event_or_disclosure, capacity_or_volume_route, relative_strength, early_revision_signal | margin_bridge, financial_visibility, multiple_public_sources, low_red_team_risk | valuation_blowoff, positioning_overheat | structural_success_then_4B_overlay |
| R4L9_C15_011170_T1 | 011170 | Stage3-Green-candidate | 2021-03-02 | 2021-03-02 | 323500 | public_event_or_disclosure, relative_strength | multiple_public_sources | valuation_blowoff, margin_or_backlog_slowdown, price_only_local_peak | failed_rerating_false_positive_green |
| R4L9_C15_298000_T1 | 298000 | Stage3-Green-candidate | 2021-04-26 | 2021-04-26 | 446500 | public_event_or_disclosure, relative_strength, capacity_or_volume_route | multiple_public_sources | valuation_blowoff, positioning_overheat, margin_or_backlog_slowdown | high_mae_false_positive_green |


## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | DD after peak | CA |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R4L9_C15_298020_T1 | 298020 | 155500 | 28.94 | -5.47 | 223.47 | -5.47 | 519.29 | -5.47 | 2021-07-16 / 963000 | -12.46 | clean_180D_window |
| R4L9_C15_011780_T1 | 011780 | 97200 | 18.31 | -1.23 | 61.01 | -4.73 | 207.1 | -4.73 | 2021-05-06 / 298500 | -32.16 | clean_180D_window; 2001-01-16 corporate-action candidate outside tested window |
| R4L9_C15_011170_T1 | 011170 | 323500 | 4.48 | -10.82 | 4.48 | -22.72 | 4.48 | -27.36 | 2021-03-02 / 338000 | -30.47 | clean_180D_window; 2Y contaminated_or_unavailable due 2023-02-13 corporate-action candidate |
| R4L9_C15_298000_T1 | 298000 | 446500 | 4.14 | -30.12 | 6.38 | -30.12 | 6.38 | -47.03 | 2021-07-16 / 475000 | -50.21 | clean_180D_window |


Formula applied:

```text
MFE_N_pct = (max(high from entry_date through N trading days) / entry_price - 1) * 100
MAE_N_pct = (min(low from entry_date through N trading days) / entry_price - 1) * 100
drawdown_after_peak_pct = (min(low after peak_date) / peak_price - 1) * 100
```

## 13. Current Calibrated Profile Stress Test

| case_id | P0 before | P2 after | actual path | verdict | why |
| --- | --- | --- | --- | --- | --- |
| R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE | Stage3-Yellow / 83.5 | Stage3-Green / 88.5 | MFE180 519.29 / MAE180 -5.47 | current_profile_too_late | C15에서는 계약/수주가 아니라 제품 spread가 엔진이다. product-specific spread와 실제 영업이익 레버리지가 동시에 보이면 contract_score 결여를 보완한다. |
| R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE | Stage3-Yellow / 84.0 | Stage3-Green / 89.0 | MFE180 207.1 / MAE180 -4.73 | current_profile_too_late | NB latex처럼 제품 단위 spread가 영업이익 폭발과 닫히면 C15에서는 spread bridge가 사실상 order-book 역할을 한다. |
| R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN | Stage3-Green / 87.5 | Stage2-Actionable/Watch / 72.0 | MFE180 4.48 / MAE180 -27.36 | current_profile_false_positive | Broad NCC narrative와 price strength만으로는 C15 Green을 열지 않는다. 제품별 spread bridge와 revision confirmation이 없으면 counterexample guard가 우선한다. |
| R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN | Stage3-Green / 88.0 | 4B overlay / Stage2-Watch / 70.5 | MFE180 6.38 / MAE180 -47.03 | current_profile_false_positive | C15 spread narrative라도 capex·가동·부채 리스크가 margin bridge보다 크면 Green 승격이 아니라 4B risk overlay가 먼저다. |


Answers to mandatory stress-test questions:

```text
1. current calibrated profile 판단:
   - product-specific positives are too late when it waits for generic Green-level revision confirmation.
   - broad commodity spread candidates can still be false Green if narrative/relative strength is over-read.

2. MFE/MAE alignment:
   - positive rows align only after product-specific spread bridge is recognized.
   - counterexamples align only after broad commodity guard and execution-risk overlay are added.

3. Stage2 bonus:
   - not globally changed; C15 needs evidence interpretation, not extra generic Stage2.

4. Yellow threshold 75:
   - kept; Yellow is fine for broad spread watch and early product spread.

5. Green threshold 87 / revision 55:
   - kept globally; C15-specific spread bridge can satisfy revision-quality equivalence only when margin bridge is observed.

6. price-only blowoff guard:
   - strengthened in C15 because price-only local peaks in commodity stories frequently precede drawdown.

7. full 4B non-price requirement:
   - kept; non-price spread fatigue/capex/debt evidence is required for full 4B, not just a local high.

8. hard 4C routing:
   - kept; C15 4C should wait for thesis break, but watch labels should appear earlier when spread bridge fails.
```

## 14. Stage2 / Yellow / Green Comparison

```text
효성티앤씨:
  Stage2-Actionable entry = 2020-11-02 close 155500
  Green-like confirmed revision proxy = 2021-02-03 close 442500
  full observed peak = 2021-07-16 high 963000
  green_lateness_ratio = 0.355

금호석유화학:
  Stage2-Actionable entry = 2020-08-10 close 97200
  Green-like confirmed revision proxy = 2020-11-05 close 154000
  full observed peak = 2021-05-06 high 298500
  green_lateness_ratio = 0.282

효성화학:
  Stage2 proxy entry = 2021-03-25 close 336500
  late Green candidate = 2021-04-26 close 446500
  full observed peak = 2021-07-16 high 475000
  green_lateness_ratio = 0.794
```

Interpretation:

```text
0.28~0.36 = positives are late but still usable if product spread bridge is real.
0.79 = late Green candidate has already consumed most upside and should be 4B overlay, not positive promotion.
```

## 15. 4B Local vs Full-window Timing Audit

| case | 4B candidate | local proximity | full-window proximity | verdict |
|---|---:|---:|---:|---|
| 금호석유화학 | 2021-04-06 close 250500 | 0.762 | 0.762 | usable if paired with non-price spread/revision fatigue |
| 롯데케미칼 | 2021-03-02 close 323500 | 1.000 | 1.000 | price-only local peak must not become full 4B without margin slowdown evidence |
| 효성화학 | 2021-04-26 close 446500 | 0.794 | 0.794 | good 4B overlay, false Green if promoted |

## 16. 4C Protection Audit

```text
롯데케미칼:
  peak = 338000
  later low = 235000
  drawdown_after_peak_pct = -30.47
  4C label = hard_4c_late_if_waiting_for_price_break

효성화학:
  peak = 475000
  later low = 236500
  drawdown_after_peak_pct = -50.21
  4C label = hard_4c_late_if_waiting_for_price_break
```

4C should not replace 4B. The earlier useful signal is 4B overlay from non-price fatigue/execution risk; hard 4C only arrives after thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L4_materials_product_specific_spread_bridge
candidate_rule =
  In L4 materials, product-specific spread + margin bridge + early/confirmed revision can compensate for absent contract/backlog evidence.
  Broad commodity or reopening spread narrative without product-level tightness remains Stage2/Watch even if relative strength is high.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C15_MATERIAL_SPREAD_SUPERCYCLE

new_axis_proposed:
  c15_product_specific_spread_bridge_bonus
  c15_broad_commodity_without_product_bridge_guard
  c15_capex_debt_execution_risk_overlay

not_global:
  true
```

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | FP rate | verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P0_e2r_2_1_stock_web_calibrated_proxy | current_proxy | none | 4 | 73.83 | -15.76 | 184.31 | -21.15 | 2/4 if broad spread narrative is allowed to Green | mixed; positives too late, counterexamples too permissive |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback reference only | 4 | 73.83 | -15.76 | 184.31 | -21.15 | 2/4 or worse | worse false-positive control |
| P1_L4_sector_specific_candidate_profile | sector_specific | c15_product_specific_spread_bridge_bonus; c15_broad_commodity_guard | 4 | 142.24 | -5.1 | 363.19 | -5.1 | 0/2 promoted rows | improved; positive basket has high MFE and low initial MAE |
| P2_C15_canonical_archetype_candidate_profile | canonical_archetype_specific | c15_product_specific_spread_bridge_required; c15_volume_without_spread_guard | 4 | 142.24 | -5.1 | 363.19 | -5.1 | 0/2 promoted rows | best explanatory fit |
| P3_counterexample_guard_profile | canonical_archetype_specific_guard | c15_broad_spread_false_green_guard; c15_capex_debt_execution_risk_penalty | 4 | 5.43 | -26.42 | 5.43 | -37.2 | 0/2 after guard | improved downside protection |


## 20. Score-Return Alignment Matrix

| bucket | selected rows | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | alignment |
|---|---:|---:|---:|---:|---:|---|
| Product-specific spread positives | 2 | 142.24 | -5.1 | 363.19 | -5.1 | strong positive alignment |
| Broad spread / execution-risk counterexamples | 2 | 5.43 | -26.42 | 5.43 | -37.2 | guard needed |
| All representative rows under P0 | 4 | 73.83 | -15.76 | 184.31 | -21.15 | mixed |

## 21. Coverage Matrix

```json
{
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE",
  "fine_archetype_id": "SPANDEX_NB_LATEX_NCC_PDH_PRODUCT_SPREAD_MARGIN_BRIDGE",
  "positive_case_count": 2,
  "counterexample_count": 2,
  "4B_case_count": 2,
  "4C_case_count": 2,
  "new_independent_case_count": 4,
  "reused_case_count": 0,
  "calibration_usable_trigger_count": 4,
  "representative_trigger_count": 4,
  "current_profile_error_count": 4,
  "sector_rule_candidate": true,
  "canonical_rule_candidate": true,
  "coverage_gap_after_this_loop": "C15 still needs non-ferrous/steel holdout; product-specific chemical spread coverage improved."
}
```

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

positive_case_count: 2
counterexample_count: 2
current_profile_error_count: 4

tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - stage3_green_total_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence

residual_error_types_found:
  - current_profile_too_late
  - current_profile_false_positive
  - 4B_overlay_needed_before_Green

new_axis_proposed:
  - c15_product_specific_spread_bridge_bonus
  - c15_broad_commodity_without_product_bridge_guard
  - c15_capex_debt_execution_risk_overlay

existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage in C15
  - full_4b_requires_non_price_evidence in C15
  - stage3_green_revision_min interpreted through product-spread bridge in C15

existing_axis_weakened: null
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - hard_4c_thesis_break_routes_to_4c

sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null

loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and source fields
- profile availability and corporate-action status for 298020, 011780, 011170, 298000
- tradable shard OHLC entry/peak/low rows used for 30D/90D/180D calculations
- positive/counterexample balance
- sector/canonical-archetype shadow-only rule proposals
```

Not validated:

```text
- live candidate scan
- production scoring code
- brokerage/trading execution
- intraday disclosure timestamps
- revised/adjusted price series
- exact official analyst consensus history
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_product_specific_spread_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+3,제품별 spread tightness와 실제 margin/revision bridge가 동시에 확인되면 수주/계약 부재를 보완,positive rows avg MFE_180 363.19% vs avg MAE_180 -5.1%,R4L9_C15_298020_T1|R4L9_C15_011780_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c15_broad_commodity_without_product_bridge_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,-6,"NCC/PDH broad narrative only, product spread bridge 미확인, revision 결여 시 Green 차단",counterexamples avg MFE_90 5.43% vs avg MAE_90 -26.42%,R4L9_C15_011170_T1|R4L9_C15_298000_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c15_capex_debt_execution_risk_overlay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+risk_overlay,spread upcycle라도 capex/gas/feedstock/plant execution risk가 크면 positive stage가 아니라 4B overlay,효성화학 late Green candidate: MFE_90 +6.38% vs MAE_90 -30.12%,R4L9_C15_298000_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type": "case", "case_id": "R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "SPANDEX_SUPPLY_TIGHTNESS_MARGIN_BRIDGE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L9_C15_298020_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "C15에서는 계약/수주가 아니라 제품 spread가 엔진이다. product-specific spread와 실제 영업이익 레버리지가 동시에 보이면 contract_score 결여를 보완한다."}
{"row_type": "case", "case_id": "R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NB_LATEX_RUBBER_SPREAD_SUPERCYCLE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R4L9_C15_011780_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "NB latex처럼 제품 단위 spread가 영업이익 폭발과 닫히면 C15에서는 spread bridge가 사실상 order-book 역할을 한다."}
{"row_type": "case", "case_id": "R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NCC_COMMODITY_SPREAD_VOLUME_WITHOUT_DURABLE_MARGIN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L9_C15_011170_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample_after_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Broad NCC narrative와 price strength만으로는 C15 Green을 열지 않는다. 제품별 spread bridge와 revision confirmation이 없으면 counterexample guard가 우선한다."}
{"row_type": "case", "case_id": "R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN", "symbol": "298000", "company_name": "효성화학", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "PDH_PP_SPREAD_WITH_CAPEX_EXECUTION_RISK", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R4L9_C15_298000_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_counterexample_after_guard", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "C15 spread narrative라도 capex·가동·부채 리스크가 margin bridge보다 크면 Green 승격이 아니라 4B risk overlay가 먼저다."}
```

### 25.3 trigger rows

```jsonl
{"row_type": "trigger", "trigger_id": "R4L9_C15_298020_T1", "case_id": "R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE", "symbol": "298020", "company_name": "효성티앤씨", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "SPANDEX_SUPPLY_TIGHTNESS_MARGIN_BRIDGE", "sector": "소재·스프레드·전략자원", "primary_archetype": "product_specific_spread_margin_bridge", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-10-30", "evidence_available_at_that_date": "3Q20 이후 스판덱스 수급 타이트와 판매단가/원가 spread 개선이 영업이익 레버리지로 연결되는 국면. 장중 시각은 확정하지 않고 다음 stock-web tradable close를 entry로 사용했다.", "evidence_source": "company quarterly-result/news-report family; stock-web OHLC rows: 2020-11-02 close 155500, 2021-02-03 high 503000, 2021-07-16 high 963000", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv + 2021.csv", "profile_path": "atlas/symbol_profiles/298/298020.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-11-02", "entry_price": 155500, "MFE_30D_pct": 28.94, "MFE_90D_pct": 223.47, "MFE_180D_pct": 519.29, "MFE_1Y_pct": 519.29, "MFE_2Y_pct": 519.29, "MAE_30D_pct": -5.47, "MAE_90D_pct": -5.47, "MAE_180D_pct": -5.47, "MAE_1Y_pct": -5.47, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-07-16", "peak_price": 963000, "drawdown_after_peak_pct": -12.46, "green_lateness_ratio": 0.355, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B_case", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_high_mfe_low_initial_mae", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L9_C15_298020_2020-11-02_155500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L9_C15_011780_T1", "case_id": "R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE", "symbol": "011780", "company_name": "금호석유화학", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NB_LATEX_RUBBER_SPREAD_SUPERCYCLE", "sector": "소재·스프레드·전략자원", "primary_archetype": "product_specific_spread_margin_bridge", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2020-08-07", "evidence_available_at_that_date": "COVID-era glove/NB latex demand, 합성고무 제품 spread, Q2/Q3 earnings beat 계열. 장마감·시각 불확실성 때문에 다음 tradable close를 entry로 사용했다.", "evidence_source": "company quarterly-result/news-report family; stock-web OHLC rows: 2020-08-10 close 97200, 2020-11-06 high 156500, 2021-05-06 high 298500", "stage2_evidence_fields": ["public_event_or_disclosure", "capacity_or_volume_route", "relative_strength", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv + 2021.csv", "profile_path": "atlas/symbol_profiles/011/011780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2020-08-10", "entry_price": 97200, "MFE_30D_pct": 18.31, "MFE_90D_pct": 61.01, "MFE_180D_pct": 207.1, "MFE_1Y_pct": 207.1, "MFE_2Y_pct": null, "MAE_30D_pct": -1.23, "MAE_90D_pct": -4.73, "MAE_180D_pct": -4.73, "MAE_1Y_pct": -4.73, "below_entry_price_flag_30D": false, "below_entry_price_flag_90D": false, "peak_date": "2021-05-06", "peak_price": 298500, "drawdown_after_peak_pct": -32.16, "green_lateness_ratio": 0.282, "four_b_local_peak_proximity": 0.762, "four_b_full_window_peak_proximity": 0.762, "four_b_timing_verdict": "good_full_window_4B_timing_if_nonprice_spread_fatigue_exists", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "revision_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "structural_success_then_4B_overlay", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2001-01-16 corporate-action candidate outside tested window", "same_entry_group_id": "R4L9_C15_011780_2020-08-10_97200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L9_C15_011170_T1", "case_id": "R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN", "symbol": "011170", "company_name": "롯데케미칼", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "NCC_COMMODITY_SPREAD_VOLUME_WITHOUT_DURABLE_MARGIN", "sector": "소재·스프레드·전략자원", "primary_archetype": "broad_commodity_spread_without_durable_margin", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green-candidate", "trigger_date": "2021-03-02", "evidence_available_at_that_date": "NCC/석유화학 spread 반등과 경기재개 narrative는 있었지만 제품별 tightness와 영업이익 revision bridge가 닫히지 않은 후보. 당일 종가를 사용했다.", "evidence_source": "sector news/report family; stock-web OHLC rows: 2021-03-02 close 323500/high 338000, 2021-07-09 low 250000, 2021-10-05 low 235000", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv", "profile_path": "atlas/symbol_profiles/011/011170.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-03-02", "entry_price": 323500, "MFE_30D_pct": 4.48, "MFE_90D_pct": 4.48, "MFE_180D_pct": 4.48, "MFE_1Y_pct": 4.48, "MFE_2Y_pct": null, "MAE_30D_pct": -10.82, "MAE_90D_pct": -22.72, "MAE_180D_pct": -27.36, "MAE_1Y_pct": -27.36, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-03-02", "peak_price": 338000, "drawdown_after_peak_pct": -30.47, "green_lateness_ratio": null, "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early_unless_margin_slowdown_confirmed", "four_b_evidence_type": ["price_only", "valuation_blowoff", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_break", "trigger_outcome_label": "failed_rerating_false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; 2Y contaminated_or_unavailable due 2023-02-13 corporate-action candidate", "same_entry_group_id": "R4L9_C15_011170_2021-03-02_323500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R4L9_C15_298000_T1", "case_id": "R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN", "symbol": "298000", "company_name": "효성화학", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "fine_archetype_id": "PDH_PP_SPREAD_WITH_CAPEX_EXECUTION_RISK", "sector": "소재·스프레드·전략자원", "primary_archetype": "commodity_spread_with_execution_debt_risk", "loop_objective": "coverage_gap_fill;counterexample_mining;sector_specific_rule_discovery;canonical_archetype_compression;green_strictness_stress_test;4B_non_price_requirement_stress_test", "trigger_type": "Stage3-Green-candidate", "trigger_date": "2021-04-26", "evidence_available_at_that_date": "PDH/PP spread와 베트남 증설 기대가 price에 선반영된 late Green 후보. 그러나 capex·가동·원가·부채 리스크가 함께 존재해 positive promotion보다 4B overlay가 먼저 필요한 케이스.", "evidence_source": "sector/news/report family; stock-web OHLC rows: 2021-04-26 close 446500/high 465000, 2021-07-16 high 475000, 2021-11-11 low 236500", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv", "profile_path": "atlas/symbol_profiles/298/298000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-04-26", "entry_price": 446500, "MFE_30D_pct": 4.14, "MFE_90D_pct": 6.38, "MFE_180D_pct": 6.38, "MFE_1Y_pct": 6.38, "MFE_2Y_pct": null, "MAE_30D_pct": -30.12, "MAE_90D_pct": -30.12, "MAE_180D_pct": -47.03, "MAE_1Y_pct": -47.03, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-07-16", "peak_price": 475000, "drawdown_after_peak_pct": -50.21, "green_lateness_ratio": 0.794, "four_b_local_peak_proximity": 0.794, "four_b_full_window_peak_proximity": 0.794, "four_b_timing_verdict": "good_full_window_4B_timing_if_execution_risk_used; false_positive_if_treated_as_Green", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_late_if_waiting_for_price_break", "trigger_outcome_label": "high_mae_false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R4L9_C15_298000_2021-04-26_446500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L9_C15_298020_SPANDEX_SPREAD_POSITIVE", "trigger_id": "R4L9_C15_298020_T1", "symbol": "298020", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 45, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 18, "product_specific_spread_score": 18}, "weighted_score_before": 83.5, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 47, "relative_strength_score": 14, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 20, "product_specific_spread_score": 21}, "weighted_score_after": 88.5, "stage_label_after": "Stage3-Green", "changed_components": ["product_specific_spread_score", "asp_or_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C15에서는 계약/수주가 아니라 제품 spread가 엔진이다. product-specific spread와 실제 영업이익 레버리지가 동시에 보이면 contract_score 결여를 보완한다.", "MFE_90D_pct": 223.47, "MAE_90D_pct": -5.47, "score_return_alignment_label": "aligned_after_shadow_profile", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L9_C15_011780_NB_LATEX_SPREAD_POSITIVE", "trigger_id": "R4L9_C15_011780_T1", "symbol": "011780", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 19, "revision_score": 47, "relative_strength_score": 13, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 20, "product_specific_spread_score": 20}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 21, "revision_score": 49, "relative_strength_score": 13, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 5, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 23, "product_specific_spread_score": 22}, "weighted_score_after": 89.0, "stage_label_after": "Stage3-Green", "changed_components": ["product_specific_spread_score", "asp_or_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "NB latex처럼 제품 단위 spread가 영업이익 폭발과 닫히면 C15에서는 spread bridge가 사실상 order-book 역할을 한다.", "MFE_90D_pct": 61.01, "MAE_90D_pct": -4.73, "score_return_alignment_label": "aligned_after_shadow_profile", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L9_C15_011170_NCC_SPREAD_FALSE_GREEN", "trigger_id": "R4L9_C15_011170_T1", "symbol": "011170", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 36, "relative_strength_score": 15, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 8, "product_specific_spread_score": 5}, "weighted_score_before": 87.5, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 8, "revision_score": 34, "relative_strength_score": 15, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 12, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 5, "product_specific_spread_score": 3}, "weighted_score_after": 72.0, "stage_label_after": "Stage2-Actionable/Watch", "changed_components": ["product_specific_spread_score", "asp_or_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "Broad NCC narrative와 price strength만으로는 C15 Green을 열지 않는다. 제품별 spread bridge와 revision confirmation이 없으면 counterexample guard가 우선한다.", "MFE_90D_pct": 4.48, "MAE_90D_pct": -22.72, "score_return_alignment_label": "aligned_after_shadow_profile", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R4L9_C15_298000_PDH_PP_LATE_FALSE_GREEN", "trigger_id": "R4L9_C15_298000_T1", "symbol": "298000", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 12, "revision_score": 38, "relative_strength_score": 17, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 15, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 10, "product_specific_spread_score": 7}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 10, "revision_score": 34, "relative_strength_score": 15, "customer_quality_score": 2, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 18, "legal_or_contract_risk_score": 4, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "asp_or_spread_score": 7, "product_specific_spread_score": 5}, "weighted_score_after": 70.5, "stage_label_after": "4B overlay / Stage2-Watch", "changed_components": ["product_specific_spread_score", "asp_or_spread_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C15 spread narrative라도 capex·가동·부채 리스크가 margin bridge보다 크면 Green 승격이 아니라 4B risk overlay가 먼저다.", "MFE_90D_pct": 6.38, "MAE_90D_pct": -30.12, "score_return_alignment_label": "aligned_after_shadow_profile", "current_profile_verdict": "current_profile_false_positive"}
```

### 25.5 profile_comparison rows

```jsonl
{"row_type": "profile_comparison", "profile_id": "P0_e2r_2_1_stock_web_calibrated_proxy", "profile_scope": "current_proxy", "profile_hypothesis": "현 calibrated profile; global thresholds already applied", "changed_axes": "none", "changed_thresholds": "stage3_yellow_total_min=75, stage3_green_total_min=87, stage3_green_revision_min=55", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "all representative rows", "avg_MFE_90D_pct": 73.83, "avg_MAE_90D_pct": -15.76, "avg_MFE_180D_pct": 184.31, "avg_MAE_180D_pct": -21.15, "false_positive_rate": "2/4 if broad spread narrative is allowed to Green", "missed_structural_count": 2, "late_green_count": 2, "avg_green_lateness_ratio": 0.477, "avg_four_b_local_peak_proximity": 0.852, "avg_four_b_full_window_peak_proximity": 0.852, "score_return_alignment_verdict": "mixed; positives too late, counterexamples too permissive"}
{"row_type": "profile_comparison", "profile_id": "P0b_e2r_2_0_baseline_reference", "profile_scope": "rollback_reference", "profile_hypothesis": "pre-calibrated looser Green threshold and weaker price-only guard", "changed_axes": "rollback reference only", "changed_thresholds": "earlier Green; weaker non-price gate", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "all representative rows", "avg_MFE_90D_pct": 73.83, "avg_MAE_90D_pct": -15.76, "avg_MFE_180D_pct": 184.31, "avg_MAE_180D_pct": -21.15, "false_positive_rate": "2/4 or worse", "missed_structural_count": 1, "late_green_count": 1, "avg_green_lateness_ratio": 0.45, "avg_four_b_local_peak_proximity": 0.92, "avg_four_b_full_window_peak_proximity": 0.92, "score_return_alignment_verdict": "worse false-positive control"}
{"row_type": "profile_comparison", "profile_id": "P1_L4_sector_specific_candidate_profile", "profile_scope": "sector_specific", "profile_hypothesis": "소재 spread sector에서 product-specific spread + margin bridge가 contract/backlog 결여를 보완", "changed_axes": "c15_product_specific_spread_bridge_bonus; c15_broad_commodity_guard", "changed_thresholds": "no global threshold change; sector/archetype shadow only", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "효성티앤씨, 금호석유화학 promote; 롯데케미칼, 효성화학 guard", "avg_MFE_90D_pct": 142.24, "avg_MAE_90D_pct": -5.1, "avg_MFE_180D_pct": 363.19, "avg_MAE_180D_pct": -5.1, "false_positive_rate": "0/2 promoted rows", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.319, "avg_four_b_local_peak_proximity": 0.762, "avg_four_b_full_window_peak_proximity": 0.762, "score_return_alignment_verdict": "improved; positive basket has high MFE and low initial MAE"}
{"row_type": "profile_comparison", "profile_id": "P2_C15_canonical_archetype_candidate_profile", "profile_scope": "canonical_archetype_specific", "profile_hypothesis": "C15 Green requires product-level spread bridge and confirmed/early revision; broad commodity beta remains Stage2/Watch", "changed_axes": "c15_product_specific_spread_bridge_required; c15_volume_without_spread_guard", "changed_thresholds": "Green not lowered globally; revision/spread bridge interpreted by archetype", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "same as P1", "avg_MFE_90D_pct": 142.24, "avg_MAE_90D_pct": -5.1, "avg_MFE_180D_pct": 363.19, "avg_MAE_180D_pct": -5.1, "false_positive_rate": "0/2 promoted rows", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.319, "avg_four_b_local_peak_proximity": 0.778, "avg_four_b_full_window_peak_proximity": 0.778, "score_return_alignment_verdict": "best explanatory fit"}
{"row_type": "profile_comparison", "profile_id": "P3_counterexample_guard_profile", "profile_scope": "canonical_archetype_specific_guard", "profile_hypothesis": "price/sector narrative + broad spread without product bridge cannot promote positive stage; capex/debt execution risk becomes 4B overlay", "changed_axes": "c15_broad_spread_false_green_guard; c15_capex_debt_execution_risk_penalty", "changed_thresholds": "no global threshold change", "eligible_trigger_count": 4, "selected_entry_trigger_per_case": "blocks 롯데케미칼/효성화학 Green", "avg_MFE_90D_pct": 5.43, "avg_MAE_90D_pct": -26.42, "avg_MFE_180D_pct": 5.43, "avg_MAE_180D_pct": -37.2, "false_positive_rate": "0/2 after guard", "missed_structural_count": 0, "late_green_count": 0, "avg_green_lateness_ratio": 0.794, "avg_four_b_local_peak_proximity": 0.897, "avg_four_b_full_window_peak_proximity": 0.897, "score_return_alignment_verdict": "improved downside protection"}
```

### 25.6 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_product_specific_spread_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+3,제품별 spread tightness와 실제 margin/revision bridge가 동시에 확인되면 수주/계약 부재를 보완,positive rows avg MFE_180 363.19% vs avg MAE_180 -5.1%,R4L9_C15_298020_T1|R4L9_C15_011780_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c15_broad_commodity_without_product_bridge_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,-6,"NCC/PDH broad narrative only, product spread bridge 미확인, revision 결여 시 Green 차단",counterexamples avg MFE_90 5.43% vs avg MAE_90 -26.42%,R4L9_C15_011170_T1|R4L9_C15_298000_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
shadow_weight,c15_capex_debt_execution_risk_overlay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,1,+risk_overlay,spread upcycle라도 capex/gas/feedstock/plant execution risk가 크면 positive stage가 아니라 4B overlay,효성화학 late Green candidate: MFE_90 +6.38% vs MAE_90 -30.12%,R4L9_C15_298000_T1,4,4,2,medium,archetype_shadow_only,not production; post-calibrated residual
```

### 25.7 residual_contribution row

```jsonl
{"row_type": "residual_contribution", "round": "R4", "loop": "9", "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE", "canonical_archetype_id": "C15_MATERIAL_SPREAD_SUPERCYCLE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 4, "new_canonical_archetype_count": 0, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage3_green_revision_min", "stage3_green_total_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence"], "residual_error_types_found": ["current_profile_too_late", "current_profile_false_positive", "4B_overlay_needed_before_Green"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "auto_selected_coverage_gap": "R4/C15 loops existed through loop 8, but C15-specific product-spread positive/counterexample compression still needed under v12 naming and anti-repetition rules."}
```

### 25.8 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"no narrative-only case needed; all representative cases have clean 180D windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R8 / C27_CONTENT_IP_GLOBAL_MONETIZATION holdout or R6 / C22_INSURANCE_RATE_CYCLE_RESERVE residual counterexamples
reason = R4/C15 now has product-spread positives and broad-spread counterexamples; next useful coverage is under-researched non-R1/R2 sectors.
```

## 28. Source Notes

```text
stock-web manifest:
  atlas/manifest.json
  max_date = 2026-02-20
  price_basis = tradable_raw
  price_adjustment_status = raw_unadjusted_marcap

stock_agent duplicate-avoidance artifact:
  data/e2r/calibration/md_registry.jsonl
  R4 loops observed through loop 8
  trigger_rows_representative.jsonl was empty in fetched range, so duplicate avoidance used registry plus new symbol/trigger-family selection.

stock-web profiles:
  atlas/symbol_profiles/298/298020.json
  atlas/symbol_profiles/011/011780.json
  atlas/symbol_profiles/011/011170.json
  atlas/symbol_profiles/298/298000.json

stock-web tradable shards:
  atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv
  atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv
  atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv
  atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv
  atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv
  atlas/ohlcv_tradable_by_symbol_year/298/298000/2021.csv
```
