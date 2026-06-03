# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file = e2r_stock_web_v12_residual_round_R4_loop_13_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md

scheduled_round = R4
scheduled_loop = 13
completed_round = R4
completed_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
computed_next_round = R5
computed_next_loop = 13

large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE

stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
current_stock_discovery_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

One-line contribution:

```text
This loop adds 4 new independent cases, 2 counterexamples, and 3 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.
```

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

This loop does not repeat the already-applied global calibration. It asks a narrower R4/C17 question:

> In chemical/material spread cycles, when does a spread headline become an EPS/margin rerating, and when is it only a tradable commodity-beta rebound?

The mechanism is similar to a refinery crack spread: the visible market price is only the flame. The useful signal is whether heat reaches the boiler as gross margin, inventory discipline, demand persistence, and revisions. C17 should therefore not promote every “spread improved” headline into Green.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
round = R4
loop = 13
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE
```

R4 is mapped to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector pair is valid. This file deliberately avoids R3 battery orderbook and R13 cross-archetype naming.

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible stock_agent source artifacts were treated as coverage/duplicate-avoidance only. No `src/e2r` code was opened. No patch was written.

The immediate local sequence state from the previous generated artifact was:

```text
previous_completed_round = R3
previous_completed_loop = 13
previous_large_sector_id = L3_BATTERY_EV_GREEN_MOBILITY
previous_canonical_archetype_id = C11_BATTERY_ORDERBOOK_RERATING
next_round_from_previous = R4
next_loop_from_previous = 13
```

A repository search for an existing `e2r_stock_web_v12_residual_round_R4_loop_13` result returned no direct duplicate in accessible GitHub search results. The loop therefore proceeds as R4 / Loop 13.

Novelty check:

```text
new_independent_case_count = 4
reused_case_count = 0
new_symbol_count = 4
same_archetype_new_symbol_count = 4
same_archetype_new_trigger_family_count = 6
minimum_new_independent_case_ratio = 1.00
loop_contribution_label = canonical_archetype_rule_candidate
do_not_propose_new_weight_delta = false
```

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest and schema were checked before using price rows. The manifest records `source_name = FinanceData/marcap`, `price_adjustment_status = raw_unadjusted_marcap`, `min_date = 1995-05-02`, `max_date = 2026-02-20`, and `tradable_row_count = 14354401`. It also records the calibration shard root as `atlas/ohlcv_tradable_by_symbol_year` and raw shard root as `atlas/ohlcv_raw_by_symbol_year`. The schema confirms tradable columns `d,o,h,l,c,v,a,mc,s,m` and calibration rules requiring positive OHLCV, entry row existence, 180 forward tradable days, computed MFE/MAE, and clean 180D corporate-action window.

```text
price_data_source = Songdaiki/stock-web
upstream_source = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | first_date | last_date | corporate_action_candidate_dates | 180D trigger window status |
|---|---|---|---:|---:|---|---|
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | 1995-05-02 | 2026-02-20 | 2001-01-16 | clean for 2020/2021 windows |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | 2018-07-13 | 2026-02-20 | none | clean |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | 1995-05-02 | 2026-02-20 | 2023-02-13 | clean for 2021 windows |
| 006650 | 대한유화 | atlas/symbol_profiles/006/006650.json | 1999-08-11 | 2026-02-20 | 2010-07-13 | clean for 2021 windows |

## 5. Historical Eligibility Gate

All representative rows satisfy the v12 eligibility gate:

```text
trigger_date_is_historical = true
entry_date_in_tradable_shard = true
forward_180D_available_by_stock_web_manifest = true
positive_OHLCV_present = true
MFE_30D_90D_180D_computed = true
MAE_30D_90D_180D_computed = true
corporate_action_contaminated_180D_window = false
```

Non-representative rows are label comparison, 4B overlay, or 4C overlay only and are not double-counted in aggregate.

## 6. Canonical Archetype Compression Map

```text
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE
compressed_signal_family =
  1. product_specific_spread_to_margin_bridge
  2. headline_NCC_or_PE_PP_beta
  3. downstream_demand_inventory_confirmation
  4. spread_peak_valuation_positioning_overlay
  5. post_peak_thesis_break_4C_watch
```

C17 is not “chemical stock went up because commodity spread went up.” It is narrower: product price, feedstock cost, utilization, inventory, and demand must form a bridge into EPS revision. Without that bridge, the signal is a wind gauge, not an engine.

## 7. Case Selection Summary

| case_id | symbol | company | case_type | +/- | current profile verdict | alignment |
|---|---:|---|---|---|---|---|
| R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008 | 011780 | 금호석유화학 | structural_success | positive | current_profile_correct | Stage2 margin-bridge signal aligned with large 30D/90D/180D MFE and shallow pre-peak MAE. |
| R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011 | 298020 | 효성티앤씨 | structural_success | positive | current_profile_correct | Spandex supply tightness and margin visibility translated into extreme MFE; later 4B overlay was better than price-only local peak. |
| R4L13_C17_011170_NCC_SPREAD_FALSE_202102 | 011170 | 롯데케미칼 | failed_rerating | counterexample | current_profile_false_positive | Headline petrochemical upcycle / NCC spread optimism generated limited MFE and materially negative 180D MAE. |
| R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102 | 006650 | 대한유화 | high_mae_success | counterexample | current_profile_false_positive | Early MFE existed but the path had high MAE and failed to sustain once PE/PP spread and inventory signals weakened. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 2
4B_case_count = 1
4C_case_count = 1
calibration_usable_case_count = 4
calibration_usable_trigger_count = 7
representative_trigger_count = 4
```

Balance is acceptable for a canonical-archetype rule candidate:

- Positive: product-specific spread translated into margin bridge and revisions: `011780`, `298020`.
- Counterexample: headline NCC / PE-PP spread beta produced false Stage3 or high-MAE path: `011170`, `006650`.
- 4B overlay: `298020` spread-supercycle blowoff near full-window peak.
- 4C watch: `006650` post-peak thesis break after spread deterioration.

## 9. Evidence Source Map

| symbol | trigger family | historical evidence proxy | Stage separation |
|---:|---|---|---|
| 011780 | NB latex / synthetic-rubber margin bridge | 2020 public earnings path and NB-latex spread visibility | Stage2 from margin visibility; Stage3 from confirmed revision |
| 298020 | spandex spread supercycle | spandex supply tightness, margin expansion, and earnings revision path | Stage2 from early spread + RS; 4B from valuation/positioning overheat |
| 011170 | NCC headline upcycle | petrochemical cycle optimism without product-specific demand/inventory confirmation | Stage2 watch only; Green cap proposed |
| 006650 | PE/PP spread rebound | PE/PP/NCC beta with later spread/inventory deterioration | Stage2 watch only; late 4C thesis-break watch |

Long-cycle context: subsequent Korean petrochemical restructuring news and overcapacity coverage support the idea that NCC headline beta can remain structurally impaired even when short-term spread rebounds appear. Reuters reported South Korean petrochemical restructuring and capacity-reduction pressure in 2025/2026, including Lotte Chemical-linked NCC rationalization, which is consistent with the counterexample guard direction.

## 10. Price Data Source Map

| symbol | entry_date | shard_path | profile_path | basis | corporate action status |
|---:|---:|---|---|---|---|
| 011780 | 2020-08-10 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv | atlas/symbol_profiles/011/011780.json | tradable_raw | clean_180D_window |
| 011780 | 2021-01-22 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | tradable_raw | clean_180D_window |
| 298020 | 2020-11-02 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv | atlas/symbol_profiles/298/298020.json | tradable_raw | clean_180D_window |
| 298020 | 2021-07-16 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | atlas/symbol_profiles/298/298020.json | tradable_raw | clean_180D_window |
| 011170 | 2021-02-08 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | tradable_raw | clean_180D_window |
| 006650 | 2021-02-08 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | tradable_raw | clean_180D_window |
| 006650 | 2021-06-24 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | tradable_raw | clean_180D_window |

## 11. Case-by-Case Trigger Grid

Representative rows are aggregate-included. Label-comparison and overlay rows are kept for Stage2/Green/4B/4C timing but not double-counted.

| trigger_id | symbol | type | trigger_date | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | profile verdict | aggregate role |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| R4L13_C17_011780_T_STAGE2_20200807 | 011780 금호석유화학 | Stage2-Actionable | 2020-08-07 | 2020-08-10 | 97,200 | 18.31 | -3.09 | 61.01 | -4.73 | 201.95 | -4.73 | 2021-02-05 / 293,500 | current_profile_correct | representative |
| R4L13_C17_011780_T_GREEN_20210121 | 011780 금호석유화학 | Stage3-Green | 2021-01-21 | 2021-01-22 | 190,500 | 54.07 | -1.57 | 54.07 | -1.57 | 54.07 | -1.57 | 2021-02-05 / 293,500 | current_profile_too_late | label_comparison_only |
| R4L13_C17_298020_T_STAGE2_20201102 | 298020 효성티앤씨 | Stage2-Actionable | 2020-11-02 | 2020-11-02 | 155,500 | 28.94 | -5.47 | 235.69 | -5.47 | 519.29 | -5.47 | 2021-07-16 / 963,000 | current_profile_correct | representative |
| R4L13_C17_298020_T_4B_20210716 | 298020 효성티앤씨 | Stage4B | 2021-07-16 | 2021-07-16 | 881,000 | 9.31 | -18.27 | 9.31 | -40.3 | 9.31 | -45.38 | 2021-07-16 / 963,000 | current_profile_correct | 4B_overlay_only |
| R4L13_C17_011170_T_STAGE2_20210205 | 011170 롯데케미칼 | Stage2-Actionable | 2021-02-05 | 2021-02-08 | 298,000 | 13.42 | -3.86 | 13.42 | -11.07 | 13.42 | -21.81 | 2021-03-02 / 338,000 | current_profile_false_positive | representative |
| R4L13_C17_006650_T_STAGE2_20210208 | 006650 대한유화 | Stage2-Actionable | 2021-02-08 | 2021-02-08 | 313,500 | 29.35 | -4.31 | 29.35 | -22.81 | 29.35 | -33.49 | 2021-02-17 / 405,500 | current_profile_false_positive | representative |
| R4L13_C17_006650_T_4C_20210623 | 006650 대한유화 | Stage4C | 2021-06-23 | 2021-06-24 | 239,500 | 20.46 | -8.77 | 20.46 | -12.94 | 20.46 | -12.94 | 2021-07-20 / 288,500 | current_profile_4C_too_late | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative aggregate rows

| trigger | role | entry | max high used | min low used | interpretation |
|---|---|---:|---:|---:|---|
| 011780 Stage2 | positive | 97,200 | 293,500 | 92,600 | Product-specific NB-latex/synthetic-rubber margin bridge produced large MFE with shallow early MAE. |
| 298020 Stage2 | positive | 155,500 | 963,000 | 147,000 | Spandex spread became a true EPS/revision engine. |
| 011170 Stage2 | counterexample | 298,000 | 338,000 | 233,000 | NCC headline upcycle did not become durable rerating. |
| 006650 Stage2 | counterexample | 313,500 | 405,500 | 208,500 | Early upside existed but failed with high MAE; not a clean Green. |

### 12.2 Main numerical audit

```text
011780 Stage2:
  entry=97,200; MFE_30=18.31%; MAE_30=-3.09%; MFE_90=61.01%; MAE_90=-4.73%; MFE_180=201.95%; MAE_180=-4.73%

298020 Stage2:
  entry=155,500; MFE_30=28.94%; MAE_30=-5.47%; MFE_90=235.69%; MAE_90=-5.47%; MFE_180=519.29%; MAE_180=-5.47%

011170 Stage2:
  entry=298,000; MFE_30=13.42%; MAE_30=-3.86%; MFE_90=13.42%; MAE_90=-11.07%; MFE_180=13.42%; MAE_180=-21.81%

006650 Stage2:
  entry=313,500; MFE_30=29.35%; MAE_30=-4.31%; MFE_90=29.35%; MAE_90=-22.81%; MFE_180=29.35%; MAE_180=-33.49%
```

## 13. Current Calibrated Profile Stress Test

### 13.1 What current profile gets right

- It correctly rewards early Stage2-actionable evidence when non-price evidence exists.
- It correctly blocks price-only blowoff as a positive stage.
- It correctly requires non-price 4B evidence for full 4B.
- It correctly routes thesis-break evidence to 4C instead of treating it as ordinary volatility.

### 13.2 Residual errors found

```text
current_profile_error_count = 3
residual_error_types_found =
  - headline_NCC_beta_false_positive
  - PE_PP_spread_high_MAE
  - 4C_late_after_spread_break
```

The current profile can still over-score C17 if it sees `relative_strength + public spread headline + generic revision` and fails to ask whether the spread is product-specific, demand-backed, inventory-clean, and margin-visible.

## 14. Stage2 / Yellow / Green Comparison

```text
011780:
  Stage2 entry = 97,200
  Stage3-Green comparison entry = 190,500
  full observed peak after Stage2 = 293,500
  green_lateness_ratio = (190,500 - 97,200) / (293,500 - 97,200) = 0.475
  verdict = Green somewhat late but still useful

298020:
  Stage2 entry = 155,500
  Stage3-Green proxy entry = 389,000
  full observed peak after Stage2 = 963,000
  green_lateness_ratio = (389,000 - 155,500) / (963,000 - 155,500) = 0.289
  verdict = Green not badly late; Stage2 still captured much better R/R

011170 / 006650:
  Green should be capped unless product-specific margin bridge and downstream confirmation exist.
```

Interpretation:

```text
existing_axis_tested = stage3_yellow_total_min / stage3_green_total_min / stage3_green_revision_min
existing_axis_kept = true
new_axis_proposed = C17 product-specific spread-to-margin bridge requirement
```

## 15. 4B Local vs Full-window Timing Audit

Hyosung TNC 4B overlay is the cleanest 4B audit row.

```text
Stage2_Actionable_entry_price = 155,500
Stage4B_entry_price = 881,000
full_window_peak_price_after_Stage2 = 963,000

four_b_full_window_peak_proximity =
  (881,000 - 155,500) / (963,000 - 155,500)
  = 0.898
```

This is not merely a local price peak. The 4B evidence had valuation and positioning overheat after a fully translated margin/revision supercycle. Therefore:

```text
four_b_timing_verdict = good_full_window_4B_timing
four_b_evidence_type = valuation_blowoff | positioning_overheat
existing_axis_strengthened = full_4b_requires_non_price_evidence
```

## 16. 4C Protection Audit

Daehan Yuhwa 4C watch is a late but still useful protection row.

```text
prior_peak_price = 405,500
Stage4C_watch_entry_price = 239,500
post_4C_low_used = 208,500

max_drawdown_after_peak_from_prior_stage = (208,500 / 405,500 - 1) = -48.58%
MAE_90D_after_4C = (208,500 / 239,500 - 1) = -12.94%

four_c_protection_score_proxy =
  1 - 12.94 / 48.58
  = 0.734
```

Label:

```text
four_c_protection_label = hard_4c_late
existing_axis_strengthened = hard_4c_thesis_break_routes_to_4c
```

The 4C signal did not save the whole peak-to-trough path. It did, however, define that the prior Stage2/Yellow thesis had degraded and should stop being treated as a normal pullback.

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = false
```

Reason: all cases sit inside C17. This is not enough to propose a full L4-wide rule for C15 steel/material spreads or C16 strategic resource policy supply. Sector-level promotion should wait for C15/C16 loops.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
rule_scope = canonical_archetype_specific
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

Proposed C17 shadow rule:

```text
C17_product_spread_to_margin_bridge_required:
  Promote C17 to Stage3-Yellow/Green only when the spread is product-specific and visibly flows into gross margin, operating profit revision, or utilization economics.

C17_headline_NCC_beta_green_cap:
  If evidence is only generic NCC / naphtha / PE / PP spread improvement plus price relative strength, cap at Stage2-watch or Stage2-Actionable. Do not promote to Green.

C17_demand_inventory_guard:
  Require downstream demand/inventory confirmation for commodity chemical spread signals. If inventory/demand is unsupported or reversing, add execution-risk penalty.

C17_non_price_4B_spread_peak_overlay:
  4B in spread supercycles is valid near full-window peak only when valuation/positioning/revision-slowdown evidence exists. Price-only local peaks remain watch-only.
```

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FP rate | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | default_current_proxy | 4 | 84.87 | -11.52 | 191.0 | -16.88 | 0.5 | positive paths aligned, but NCC/PE-PP headline spread caused false positives |
| P0b_e2r_2_0_baseline_reference | rollback_reference | 4 | 84.87 | -11.52 | 191.0 | -16.88 | 0.5 | missed early structural spreads and did not protect late-cycle chemical beta |
| P1_sector_specific_candidate_profile | sector_specific | 4 | 84.87 | -11.52 | 191.0 | -16.88 | 0.5 | not enough cross-C15/C16 validation for sector-wide rule |
| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 4 | 84.87 | -11.52 | 191.0 | -16.88 | 0.0 | best alignment: positives preserved, false Stage3 labels capped to watch |
| P3_counterexample_guard_profile | canonical_archetype_guard | 2 | 21.39 | -16.94 | 21.39 | -27.65 | 0.0 | counterexample guard improves downside filtering |

## 20. Score-Return Alignment Matrix

| trigger_id | before label | after label | MFE90 | MAE90 | alignment |
|---|---|---|---:|---:|---|
| R4L13_C17_011780_T_STAGE2_20200807 | Stage3-Yellow | Stage3-Yellow | 61.01 | -4.73 | keep positive |
| R4L13_C17_011780_T_GREEN_20210121 | Stage3-Green | Stage3-Green | 54.07 | -1.57 | Green usable but late |
| R4L13_C17_298020_T_STAGE2_20201102 | Stage3-Yellow | Stage3-Yellow | 235.69 | -5.47 | keep positive |
| R4L13_C17_298020_T_4B_20210716 | Stage3-Green_with_4B_watch | Stage4B-overlay | 9.31 | -40.30 | 4B overlay improves risk timing |
| R4L13_C17_011170_T_STAGE2_20210205 | Stage3-Yellow | Stage2-watch | 13.42 | -11.07 | false positive reduced |
| R4L13_C17_006650_T_STAGE2_20210208 | Stage3-Yellow | Stage2-watch | 29.35 | -22.81 | high-MAE false positive reduced |
| R4L13_C17_006650_T_4C_20210623 | Stage2-watch | Stage4C | 20.46 | -12.94 | late 4C watch |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE | 2 | 2 | 1 | 1 | 4 | 0 | 7 | 4 | 3 | false | true | C17 now has balanced positive/counterexample coverage; C15/C16 still need separate R4 loops. |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 6

tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

residual_error_types_found:
  - headline_NCC_beta_false_positive
  - PE_PP_spread_high_MAE
  - Green_confirmation_lateness
  - 4C_late_after_spread_break

new_axis_proposed:
  - C17_product_spread_to_margin_bridge_required
  - C17_headline_NCC_beta_green_cap
  - C17_demand_inventory_guard
  - C17_non_price_4B_spread_peak_overlay

existing_axis_strengthened:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c

existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- Historical trigger-level OHLC from Songdaiki/stock-web tradable shards
- Representative trigger MFE/MAE 30D/90D/180D
- 4B full-window versus local-window proximity for 298020
- 4C protection proxy for 006650
- Round/sector/canonical consistency
- Positive/counterexample balance
```

Not validated:

```text
- No stock_agent source code inspection
- No production scoring change
- No live candidate scan
- No current investment recommendation
- No full R4/C15/C16 sector-wide conclusion
- No brokerage API / trading execution
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_product_spread_to_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Positive C17 cases had product-specific margin bridge; headline NCC/PE-PP cases had high MAE or false positive behavior.","Caps false Stage3-Yellow labels while preserving 011780/298020 positives.","R4L13_C17_011780_T_STAGE2_20200807|R4L13_C17_298020_T_STAGE2_20201102|R4L13_C17_011170_T_STAGE2_20210205|R4L13_C17_006650_T_STAGE2_20210208",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_headline_NCC_beta_green_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"NCC headline upcycle without inventory/demand bridge produced limited MFE and larger MAE in 011170/006650.","Blocks Green promotion for commodity-beta spread rallies.","R4L13_C17_011170_T_STAGE2_20210205|R4L13_C17_006650_T_STAGE2_20210208",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_non_price_4B_spread_peak_overlay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"298020 4B overlay near full-window high performed better when supported by valuation/positioning overheat, not just local price peak.","Improves 4B timing audit for spread supercycles.","R4L13_C17_298020_T_4B_20210716",1,1,0,low,canonical_shadow_only,"4B overlay/risk only"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L13_C17_011780_T_STAGE2_20200807","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 margin-bridge signal aligned with large 30D/90D/180D MFE and shallow pre-peak MAE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"NB-latex/synthetic-rubber margin bridge became visible before consensus Green; high MFE with low early MAE supports keeping Stage2-Actionable path but not lowering Green gate."}
{"row_type":"case","case_id":"R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L13_C17_298020_T_STAGE2_20201102","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Spandex supply tightness and margin visibility translated into extreme MFE; later 4B overlay was better than price-only local peak.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spandex cycle showed order/price/margin bridge, not just commodity price beta."}
{"row_type":"case","case_id":"R4L13_C17_011170_NCC_SPREAD_FALSE_202102","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L13_C17_011170_T_STAGE2_20210205","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Headline petrochemical upcycle / NCC spread optimism generated limited MFE and materially negative 180D MAE.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Large integrated NCC name did not re-rate structurally without product-specific margin bridge and demand/inventory confirmation."}
{"row_type":"case","case_id":"R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102","symbol":"006650","company_name":"대한유화","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","case_type":"high_mae_success","positive_or_counterexample":"counterexample","best_trigger":"R4L13_C17_006650_T_STAGE2_20210208","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Early MFE existed but the path had high MAE and failed to sustain once PE/PP spread and inventory signals weakened.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"This case separates trading beta from durable C17 rerating; 4C watch would have reduced late-cycle damage."}
```

### 25.3 trigger rows

```jsonl
{"trigger_id":"R4L13_C17_011780_T_STAGE2_20200807","case_id":"R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008","symbol":"011780","company_name":"금호석유화학","trigger_type":"Stage2-Actionable","trigger_date":"2020-08-07","entry_date":"2020-08-10","entry_price":97200,"evidence_available_at_that_date":"2Q/3Q 2020 public earnings path: NB-latex and synthetic rubber spread visibility; early revision and margin bridge visible before full consensus confirmation.","evidence_source":"company quarterly earnings / public broker coverage proxy; price rows verified from Stock-Web 011780 2020-08-07~2021-02-05","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":18.31,"MFE_90D_pct":61.01,"MFE_180D_pct":201.95,"MFE_1Y_pct":201.95,"MFE_2Y_pct":201.95,"MAE_30D_pct":-3.09,"MAE_90D_pct":-4.73,"MAE_180D_pct":-4.73,"MAE_1Y_pct":-4.73,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-05","peak_price":293500,"drawdown_after_peak_pct":-68.45,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_011780_20200810_97200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_011780_T_GREEN_20210121","case_id":"R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008","symbol":"011780","company_name":"금호석유화학","trigger_type":"Stage3-Green","trigger_date":"2021-01-21","entry_date":"2021-01-22","entry_price":190500,"evidence_available_at_that_date":"Public price/margin and earnings confirmation had become broad; Green confirmation arrived after material Stage2 upside.","evidence_source":"public earnings / broad consensus proxy; price rows verified from Stock-Web 011780 2021-01-21~2021-02-05","stage2_evidence_fields":["relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":54.07,"MFE_90D_pct":54.07,"MFE_180D_pct":54.07,"MFE_1Y_pct":54.07,"MFE_2Y_pct":54.07,"MAE_30D_pct":-1.57,"MAE_90D_pct":-1.57,"MAE_180D_pct":-1.57,"MAE_1Y_pct":-1.57,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-05","peak_price":293500,"drawdown_after_peak_pct":-68.45,"green_lateness_ratio":0.475,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"late_green_but_still_positive","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_011780_20210122_190500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case; Stage3-Green lateness comparison","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_298020_T_STAGE2_20201102","case_id":"R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011","symbol":"298020","company_name":"효성티앤씨","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-02","entry_date":"2020-11-02","entry_price":155500,"evidence_available_at_that_date":"Spandex supply tightness and margin bridge were visible in public earnings/industry coverage; relative strength confirmed early before full Green.","evidence_source":"company quarterly earnings / spandex spread public coverage proxy; price rows verified from Stock-Web 298020 2020-11-02~2021-07-16","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"MFE_30D_pct":28.94,"MFE_90D_pct":235.69,"MFE_180D_pct":519.29,"MFE_1Y_pct":519.29,"MFE_2Y_pct":519.29,"MAE_30D_pct":-5.47,"MAE_90D_pct":-5.47,"MAE_180D_pct":-5.47,"MAE_1Y_pct":-5.47,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-45.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_298020_20201102_155500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_298020_T_4B_20210716","case_id":"R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011","symbol":"298020","company_name":"효성티앤씨","trigger_type":"Stage4B","trigger_date":"2021-07-16","entry_date":"2021-07-16","entry_price":881000,"evidence_available_at_that_date":"Spandex-cycle valuation and positioning overheat after extreme rerating; price made full-window high intraday while later MAE deteriorated sharply.","evidence_source":"public valuation/price-cycle watch proxy; price rows verified from Stock-Web 298020 2021-07-16~2021-11-12","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"MFE_30D_pct":9.31,"MFE_90D_pct":9.31,"MFE_180D_pct":9.31,"MFE_1Y_pct":9.31,"MFE_2Y_pct":9.31,"MAE_30D_pct":-18.27,"MAE_90D_pct":-40.3,"MAE_180D_pct":-45.38,"MAE_1Y_pct":-45.38,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-45.38,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.898,"four_b_full_window_peak_proximity":0.898,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_298020_20210716_881000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; 4B full-window timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_011170_T_STAGE2_20210205","case_id":"R4L13_C17_011170_NCC_SPREAD_FALSE_202102","symbol":"011170","company_name":"롯데케미칼","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-05","entry_date":"2021-02-08","entry_price":298000,"evidence_available_at_that_date":"Headline NCC upcycle / petrochemical spread optimism without durable product-specific margin bridge and inventory confirmation.","evidence_source":"public earnings/upcycle coverage proxy; price rows verified from Stock-Web 011170 2021-02-05~2021-08-20","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"MFE_30D_pct":13.42,"MFE_90D_pct":13.42,"MFE_180D_pct":13.42,"MFE_1Y_pct":13.42,"MFE_2Y_pct":13.42,"MAE_30D_pct":-3.86,"MAE_90D_pct":-11.07,"MAE_180D_pct":-21.81,"MAE_1Y_pct":-21.81,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-31.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_011170_20210208_298000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_006650_T_STAGE2_20210208","case_id":"R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102","symbol":"006650","company_name":"대한유화","trigger_type":"Stage2-Actionable","trigger_date":"2021-02-08","entry_date":"2021-02-08","entry_price":313500,"evidence_available_at_that_date":"PE/PP spread and NCC beta improved, but evidence did not yet prove durable demand/inventory balance.","evidence_source":"public petrochemical spread coverage proxy; price rows verified from Stock-Web 006650 2021-02-08~2021-08-20","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":29.35,"MFE_90D_pct":29.35,"MFE_180D_pct":29.35,"MFE_1Y_pct":29.35,"MFE_2Y_pct":29.35,"MAE_30D_pct":-4.31,"MAE_90D_pct":-22.81,"MAE_180D_pct":-33.49,"MAE_1Y_pct":-33.49,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-02-17","peak_price":405500,"drawdown_after_peak_pct":-48.58,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_006650_20210208_313500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
{"trigger_id":"R4L13_C17_006650_T_4C_20210623","case_id":"R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102","symbol":"006650","company_name":"대한유화","trigger_type":"Stage4C","trigger_date":"2021-06-23","entry_date":"2021-06-24","entry_price":239500,"evidence_available_at_that_date":"Post-peak PE/PP and NCC thesis deterioration watch; price path had already broken below the initial rerating base.","evidence_source":"public spread deterioration proxy; price rows verified from Stock-Web 006650 2021-06-23~2021-08-20","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"MFE_30D_pct":20.46,"MFE_90D_pct":20.46,"MFE_180D_pct":20.46,"MFE_1Y_pct":20.46,"MFE_2Y_pct":20.46,"MAE_30D_pct":-8.77,"MAE_90D_pct":-12.94,"MAE_180D_pct":-12.94,"MAE_1Y_pct":-12.94,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-20","peak_price":288500,"drawdown_after_peak_pct":-27.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"4C_late","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L13_C17_006650_20210624_239500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case; 4C thesis-break timing audit","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"row_type":"trigger","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_NB_LATEX_SPANDEX_PE_PP_SPREAD_MARGIN_BRIDGE","sector":"materials/chemicals","primary_archetype":"chemical commodity spread to margin bridge","loop_objective":"sector_specific_rule_discovery|canonical_archetype_compression|counterexample_mining|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20"}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008","trigger_id":"R4L13_C17_011780_T_STAGE2_20200807","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":36,"revision_score":18,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":40,"revision_score":20,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":-3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":61.01,"MAE_90D_pct":-4.73,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_011780_NB_LATEX_MARGIN_BRIDGE_202008","trigger_id":"R4L13_C17_011780_T_GREEN_20210121","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":42,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":91,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":42,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":91,"stage_label_after":"Stage3-Green","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":54.07,"MAE_90D_pct":-1.57,"score_return_alignment_label":"residual_error_or_late_overlay","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011","trigger_id":"R4L13_C17_298020_T_STAGE2_20201102","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":38,"revision_score":20,"relative_strength_score":17,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":81,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":22,"relative_strength_score":17,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":86,"stage_label_after":"Stage3-Yellow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":235.69,"MAE_90D_pct":-5.47,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_298020_SPANDEX_SUPERCYCLE_202011","trigger_id":"R4L13_C17_298020_T_4B_20210716","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":48,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":25,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":96,"stage_label_before":"Stage3-Green_with_4B_watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":45,"revision_score":48,"relative_strength_score":20,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":32,"execution_risk_score":-10,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":96,"stage_label_after":"Stage4B-overlay","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":9.31,"MAE_90D_pct":-40.3,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_011170_NCC_SPREAD_FALSE_202102","trigger_id":"R4L13_C17_011170_T_STAGE2_20210205","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":14,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":10,"relative_strength_score":14,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":-13,"legal_or_contract_risk_score":-2,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":13.42,"MAE_90D_pct":-11.07,"score_return_alignment_label":"residual_error_or_late_overlay","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102","trigger_id":"R4L13_C17_006650_T_STAGE2_20210208","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":14,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":10,"execution_risk_score":-8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":10,"revision_score":8,"relative_strength_score":16,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":-14,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-watch","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":29.35,"MAE_90D_pct":-22.81,"score_return_alignment_label":"residual_error_or_late_overlay","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L13_C17_006650_PE_PP_SPREAD_FALSE_202102","trigger_id":"R4L13_C17_006650_T_4C_20210623","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":-5,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":42,"stage_label_before":"Stage2-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":-8,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":-25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":31,"stage_label_after":"Stage4C","changed_components":["margin_bridge_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C17 shadow profile rewards product-specific spread-to-margin bridge and penalizes headline NCC/commodity beta without demand/inventory confirmation.","MFE_90D_pct":20.46,"MAE_90D_pct":-12.94,"score_return_alignment_label":"residual_error_or_late_overlay","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 profile aggregate rows

```jsonl
{"row_type":"aggregate_profile","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"default_current_proxy","profile_hypothesis":"Current calibrated profile with global Stage2/Green/4B/4C changes.","changed_axes":"none","changed_thresholds":"none","eligible_trigger_count":4,"selected_entry_trigger_per_case":"011780:2020-08-10|298020:2020-11-02|011170:2021-02-08|006650:2021-02-08","avg_MFE_90D_pct":84.87,"avg_MAE_90D_pct":-11.52,"avg_MFE_180D_pct":191.0,"avg_MAE_180D_pct":-16.88,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.382,"avg_four_b_local_peak_proximity":0.898,"avg_four_b_full_window_peak_proximity":0.898,"score_return_alignment_verdict":"positive paths aligned, but NCC/PE-PP headline spread caused false positives"}
{"row_type":"aggregate_profile","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline would tend to label Stage2 later and ignore some 4B/4C protection.","changed_axes":"rollback","changed_thresholds":"older thresholds","eligible_trigger_count":4,"selected_entry_trigger_per_case":"same representative rows","avg_MFE_90D_pct":84.87,"avg_MAE_90D_pct":-11.52,"avg_MFE_180D_pct":191.0,"avg_MAE_180D_pct":-16.88,"false_positive_rate":0.5,"missed_structural_count":1,"late_green_count":2,"avg_green_lateness_ratio":0.45,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"missed early structural spreads and did not protect late-cycle chemical beta"}
{"row_type":"aggregate_profile","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"L4 materials broadly require spread-to-margin bridge; however sample is C17-heavy, so no sector-wide delta yet.","changed_axes":"no sector delta","changed_thresholds":"none","eligible_trigger_count":4,"selected_entry_trigger_per_case":"same representative rows","avg_MFE_90D_pct":84.87,"avg_MAE_90D_pct":-11.52,"avg_MFE_180D_pct":191.0,"avg_MAE_180D_pct":-16.88,"false_positive_rate":0.5,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.382,"avg_four_b_local_peak_proximity":0.898,"avg_four_b_full_window_peak_proximity":0.898,"score_return_alignment_verdict":"not enough cross-C15/C16 validation for sector-wide rule"}
{"row_type":"aggregate_profile","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 should promote only product-specific spread-to-margin bridge plus demand/inventory confirmation; headline NCC beta is capped.","changed_axes":"C17_product_spread_margin_bridge_required|C17_headline_NCC_beta_cap|C17_inventory_demand_guard","changed_thresholds":"Green requires margin_bridge>=38 and revision>=20 or confirmed product spread persistence","eligible_trigger_count":4,"selected_entry_trigger_per_case":"same representative rows","avg_MFE_90D_pct":84.87,"avg_MAE_90D_pct":-11.52,"avg_MFE_180D_pct":191.0,"avg_MAE_180D_pct":-16.88,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":0.382,"avg_four_b_local_peak_proximity":0.898,"avg_four_b_full_window_peak_proximity":0.898,"score_return_alignment_verdict":"best alignment: positives preserved, false Stage3 labels capped to watch"}
{"row_type":"aggregate_profile","profile_id":"P3_counterexample_guard_profile","profile_scope":"canonical_archetype_guard","profile_hypothesis":"If evidence is only NCC headline beta or short-lived PE/PP rebound, cap at Stage2-watch unless inventory/demand bridge confirms.","changed_axes":"execution_risk_penalty_for_unconfirmed_spread|demand_inventory_guard","changed_thresholds":"Stage3-Yellow blocked when margin_bridge<20 and execution_risk<-10","eligible_trigger_count":2,"selected_entry_trigger_per_case":"011170:2021-02-08|006650:2021-02-08","avg_MFE_90D_pct":21.39,"avg_MAE_90D_pct":-16.94,"avg_MFE_180D_pct":21.39,"avg_MAE_180D_pct":-27.65,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":null,"avg_four_b_local_peak_proximity":null,"avg_four_b_full_window_peak_proximity":null,"score_return_alignment_verdict":"counterexample guard improves downside filtering"}
```

### 25.6 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_product_spread_to_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"Positive C17 cases had product-specific margin bridge; headline NCC/PE-PP cases had high MAE or false positive behavior.","Caps false Stage3-Yellow labels while preserving 011780/298020 positives.","R4L13_C17_011780_T_STAGE2_20200807|R4L13_C17_298020_T_STAGE2_20201102|R4L13_C17_011170_T_STAGE2_20210205|R4L13_C17_006650_T_STAGE2_20210208",4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_headline_NCC_beta_green_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"NCC headline upcycle without inventory/demand bridge produced limited MFE and larger MAE in 011170/006650.","Blocks Green promotion for commodity-beta spread rallies.","R4L13_C17_011170_T_STAGE2_20210205|R4L13_C17_006650_T_STAGE2_20210208",2,2,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C17_non_price_4B_spread_peak_overlay,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"298020 4B overlay near full-window high performed better when supported by valuation/positioning overheat, not just local price peak.","Improves 4B timing audit for spread supercycles.","R4L13_C17_298020_T_4B_20210716",1,1,0,low,canonical_shadow_only,"4B overlay/risk only"
```

### 25.7 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"13","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","scheduled_round":"R4","scheduled_loop":13,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":4,"reused_case_count":0,"new_symbol_count":4,"same_archetype_new_symbol_count":4,"same_archetype_new_trigger_family_count":6,"new_trigger_family_count":6,"positive_case_count":2,"counterexample_count":2,"current_profile_error_count":3,"diversity_score_summary":"new_symbol +12; same_archetype_new_symbol +16; new_trigger_family +24; counterexample_gap +8; residual_error +15; wrong_round_penalty 0; estimated +75","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["headline_NCC_beta_false_positive","PE_PP_spread_high_MAE","Green_confirmation_lateness","4C_late_after_spread_break"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R4
completed_loop = 13
next_round = R5
next_loop = 13
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

Stock-Web source files inspected during this loop:

```text
atlas/manifest.json
atlas/schema.json
atlas/symbol_profiles/011/011780.json
atlas/symbol_profiles/298/298020.json
atlas/symbol_profiles/011/011170.json
atlas/symbol_profiles/006/006650.json
atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv
atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv
atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv
atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv
atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv
atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv
```

External context used only as narrative context, not as price data:

```text
Reuters petrochemical overcapacity / Korean restructuring coverage, 2025-2026.
Wikipedia pages for broad company identity were treated as low-weight background only.
```

Caveat:

```text
All OHLC values are raw/unadjusted marcap-derived rows. This MD is not investment advice and does not scan current stocks.
```
