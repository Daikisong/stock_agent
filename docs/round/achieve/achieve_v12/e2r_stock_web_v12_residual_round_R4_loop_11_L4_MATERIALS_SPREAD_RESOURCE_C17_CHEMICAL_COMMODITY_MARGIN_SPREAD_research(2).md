# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R4",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R4",
  "completed_loop": 11,
  "next_round": "R5",
  "next_loop": 11,
  "large_sector_id": "L4_MATERIALS_SPREAD_RESOURCE",
  "canonical_archetype_id": "C17_CHEMICAL_COMMODITY_MARGIN_SPREAD",
  "fine_archetype_id": "NB_LATEX_SPANDEX_PETROCHEM_PRODUCT_SPREAD_CYCLE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression",
    "green_strictness_stress_test",
    "4B_non_price_requirement_stress_test",
    "residual_false_positive_mining"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 5,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 2,
  "diversity_score_summary": "estimated +42; wrong_round_penalty=0; repeated_same_symbol_penalty=0; repeated_same_entry_group_penalty=0; schema_rematerialization_penalty=0",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

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

No production scoring is changed. This MD proposes shadow-only sector/canonical rules.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R4
scheduled_loop = 11
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id = NB_LATEX_SPANDEX_PETROCHEM_PRODUCT_SPREAD_CYCLE
round_schedule_status = valid
round_sector_consistency = pass
```

This file follows the prior R3 loop 11 next state and advances to R4, not to a larger out-of-round gap.

## 3. Previous Coverage / Duplicate Avoidance Check

The immediately preceding loop was R3 / L3 / C14. This loop moves to R4 / L4 and chooses C17 to avoid replaying battery/EV price-path cases. The selected symbols are all new for this loop family.

```text
same_canonical_archetype_research = allowed
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Profile checks:

| symbol | company | profile_path | corporate-action candidates | selected window status |
|---:|---|---|---|---|
| 011780 | 금호석유화학 | atlas/symbol_profiles/011/011780.json | 2001-01-16 | clean for 2021 window |
| 298020 | 효성티앤씨 | atlas/symbol_profiles/298/298020.json | none | clean for 2021 window |
| 011170 | 롯데케미칼 | atlas/symbol_profiles/011/011170.json | 2023-02-13 | clean for 2021 window |
| 051910 | LG화학 | atlas/symbol_profiles/051/051910.json | not used | narrative-only due mixed battery/chemical scope |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false for representative rows
calibration_usable = true for representative rows
```

All representative rows use stock-web tradable shards and are not contaminated by the profile corporate-action candidate dates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| NB_LATEX_SYNTHETIC_RUBBER_SPREAD_SUPERCYCLE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Specialty chemical product spread with visible margin/revision bridge. |
| SPANDEX_UTILIZATION_SPREAD_SUPERCYCLE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Scarce product spread + utilization shock with revision transmission. |
| BASIC_PETROCHEM_NAPHTHA_PRODUCT_SPREAD_FALSE_GREEN | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | Broad chemical beta where raw-material/product spread durability is insufficient. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121 | 011780 | 금호석유화학 | positive structural success | NB latex/synthetic rubber spread was transmitted into margin/revision. |
| R4L11_C17_298020_HYOSUNG_SPANDEX_SPREAD_SUPERCYCLE_20210121 | 298020 | 효성티앤씨 | positive structural success | Spandex utilization/spread scarcity created large and durable rerating. |
| R4L11_C17_011170_LOTTE_BASIC_PETROCHEM_FALSE_GREEN_20210223 | 011170 | 롯데케미칼 | counterexample / failed rerating | Broad petrochemical beta lacked durable product-spread/margin bridge. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 2
4C_case_count = 0
```

C17 is not “chemical is good when the economy reopens.” It is more like a refinery gauge board: one needle is product price, one is input cost, one is utilization, and one is revision. If only the share price needle jumps, the machine can still be empty. 금호석유화학 and 효성티앤씨 had the full gauge board moving. 롯데케미칼 had more of a broad beta move without enough durable spread translation.

## 9. Evidence Source Map

| symbol | evidence family | source status | use |
|---:|---|---|---|
| 011780 | NB latex/synthetic rubber spread + revision bridge | public result/news/report summary; exact URL enrichment required | quantitative |
| 298020 | spandex spread/utilization + revision bridge | public result/news/report summary; exact URL enrichment required | quantitative |
| 011170 | broad petrochemical reopening/spread optimism without durable margin bridge | public result/news/report summary; exact URL enrichment required | quantitative counterexample |
| 051910 | mixed chemical/battery valuation | narrative-only | excluded from calibration |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | 2021-01-21 | usable |
| 298020 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv | atlas/symbol_profiles/298/298020.json | 2021-01-21 | usable |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | atlas/symbol_profiles/011/011170.json | 2021-02-23 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 금호석유화학 NB latex/spread | 011780 | Stage3-Green | 2021-01-21 | 186,000 | +57.80% | +60.48% | +60.48% | -2.15% | -2.15% | -4.57% | structural success |
| 효성티앤씨 spandex spread | 298020 | Stage3-Green | 2021-01-21 | 288,500 | +74.35% | +180.76% | +233.80% | -5.55% | -5.55% | -5.55% | structural success |
| 롯데케미칼 broad petrochem beta | 011170 | false Green | 2021-02-23 | 326,000 | +3.68% | +3.68% | +3.68% | -11.04% | -20.40% | -31.29% | failed rerating / false positive |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate:

| metric | 011780 | 298020 | 011170 |
|---|---:|---:|---:|
| entry_price | 186,000 | 288,500 | 326,000 |
| MFE_30D_pct | +57.80 | +74.35 | +3.68 |
| MFE_90D_pct | +60.48 | +180.76 | +3.68 |
| MFE_180D_pct | +60.48 | +233.80 | +3.68 |
| MAE_30D_pct | -2.15 | -5.55 | -11.04 |
| MAE_90D_pct | -2.15 | -5.55 | -20.40 |
| MAE_180D_pct | -4.57 | -5.55 | -31.29 |

Aggregate interpretation:

```text
positive_structural_avg_MFE_90D_pct = 120.62
positive_structural_avg_MAE_90D_pct = -3.85
counterexample_MFE_90D_pct = 3.68
counterexample_MAE_90D_pct = -20.40
```

## 13. Current Calibrated Profile Stress Test

| case | likely current profile behavior | actual OHLC alignment | verdict |
|---|---|---|---|
| 금호석유화학 spread supercycle | likely Stage3-Green if revision and margin bridge recognized | +60.48% MFE90 with -2.15% MAE90 | current_profile_correct |
| 효성티앤씨 spandex supercycle | likely Stage3-Green if product spread/utilization recognized | +180.76% MFE90 with -5.55% MAE90 | current_profile_correct |
| 롯데케미칼 broad petrochem beta | may over-promote if relative strength and reopening beta are over-weighted | only +3.68% MFE90, -20.40% MAE90 | current_profile_false_positive |
| 2021 peak 4B overlays | current profile may wait for reported EPS rollover | high proximity to full-window peaks | current_profile_4B_too_late |

Axis verdict:

```text
stage3_green_total_min = existing_axis_kept
stage3_green_revision_min = existing_axis_weakened only as C17 spread-quality exception
stage3_cross_evidence_green_buffer = existing_axis_strengthened for specialty spread + utilization + revision
price_only_blowoff_blocks_positive_stage = existing_axis_kept
full_4b_requires_non_price_evidence = existing_axis_kept
hard_4c_thesis_break_routes_to_4c = not_primary_tested
```

## 14. Stage2 / Yellow / Green Comparison

C17 requires a stricter distinction between broad chemical beta and product-spread transmission.

```text
Stage2 / Watch:
  commodity or reopening beta; product spread not yet confirmed

Stage3-Yellow:
  product spread improving, but revision bridge or utilization still incomplete

Stage3-Green:
  specialty product spread + utilization/capacity tightness + revision or margin bridge

False Green guard:
  raw-material inflation, generic cyclical beta, or one-off price spike without durable product spread

4B overlay:
  spread rollover / capacity normalization / valuation blowoff / positioning overheat

Hard 4C:
  structural product-spread collapse, accounting trust break, forced liquidity issue, or confirmed thesis break
```

Green lateness:

| case | Stage2-Actionable proxy | Green trigger | peak | green_lateness_ratio | read |
|---|---:|---:|---:|---:|---|
| 011780 | 162,500 | 186,000 | 298,500 | 0.17 | Green not late |
| 298020 | 206,000 | 288,500 | 963,000 | 0.11 | Green not late |
| 011170 | not_applicable | false Green | 338,000 | not_applicable | false positive, not lateness |

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| 011780 2021-05-06 spread peak overlay | 0.98 | 0.98 | good full-window 4B timing if spread rollover evidence exists |
| 298020 2021-07-16 spread peak overlay | 0.88 | 0.88 | good full-window 4B timing if spread rollover evidence exists |
| 011170 2021-02-23 false Green | not_applicable | not_applicable | not a 4B; this is positive-stage guard |

The point is not to sell because a chart is high. The point is that in chemical spread cycles, product-spread rollover can arrive before reported financial revision turns. The dashboard needle turns before the quarterly report prints the smoke.

## 16. 4C Protection Audit

```text
hard_4c_success = not_primary_tested
hard_4c_late = not_primary_tested
false_break = not_primary_tested
thesis_break_watch_only = 4B overlays only
```

C17 this loop is a Green/4B calibration loop, not a hard-4C thesis-break loop.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L4_MATERIALS_SPREAD_RESOURCE
candidate_axis = c17_spread_quality_vs_broad_beta
```

Candidate rule:

```text
In L4 chemical/material spread names, positive-stage promotion should require product-spread durability and utilization or revision bridge. Broad commodity beta or raw-material inflation alone should remain Stage2-Watch/Yellow at most.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
new_axis_proposed:
  - c17_specialty_product_spread_quality_boost
  - c17_broad_chemical_beta_false_green_guard
  - c17_spread_rollover_4b_pre_financial_revision
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | current representative | +81.64 | -9.37 | +99.32 | -13.80 | 0.33 | 0 | 0 | 0.14 | mixed; broad beta false positive remains |
| P0b e2r_2_0_baseline_reference | 3 | current representative | +81.64 | -9.37 | +99.32 | -13.80 | 0.33 | 0 | 1 | 0.14 | too blunt on product spread quality |
| P1 sector_specific_candidate_profile | 3 | C17 spread-quality guard | +120.62 positive / +3.68 blocked | -3.85 positive / -20.40 blocked | +147.14 positive / +3.68 blocked | -5.06 positive / -31.29 blocked | 0.00 | 0 | 0 | 0.14 | better separation |
| P2 canonical_archetype_candidate_profile | 3 | C17 specialty-spread boost + broad-beta guard | +120.62 positive / +3.68 blocked | -3.85 positive / -20.40 blocked | +147.14 positive / +3.68 blocked | -5.06 positive / -31.29 blocked | 0.00 | 0 | 0 | 0.14 | best explanatory fit |
| P3 counterexample_guard_profile | 3 | broad-beta guard only | +81.64 | -9.37 | +99.32 | -13.80 | 0.00 false-Green | 0 | 0 | 0.14 | conservative but safer |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | MFE90/MAE90 | alignment |
|---|---:|---|---:|---|---|---|
| 011780 | 86.0 | Stage3-Yellow_high | 89.0 | Stage3-Green | +60.48 / -2.15 | Green aligned |
| 298020 | 88.0 | Stage3-Green | 92.0 | Stage3-Green_high_conviction | +180.76 / -5.55 | Green aligned |
| 011170 | 76.0 | Stage3-Yellow_or_false_Green | 63.0 | Stage2-Watch_or_4B-risk | +3.68 / -20.40 | false-positive guard aligned |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | NB_LATEX_SPANDEX_PETROCHEM_PRODUCT_SPREAD_CYCLE | 2 | 1 | 2 | 0 | 3 | 0 | 5 | 3 | 2 | true | true | C17 now has specialty-spread positive coverage and broad-chemical-beta counterexample; still needs C15/C16 resource-policy holdouts in later R4 loops. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - specialty_product_spread_green_quality_boost
  - broad_chemical_beta_false_green
  - spread_rollover_4b_before_financial_revision
  - green_threshold_sector_specific_exception
new_axis_proposed:
  - c17_specialty_product_spread_quality_boost
  - c17_broad_chemical_beta_false_green_guard
  - c17_spread_rollover_4b_pre_financial_revision
existing_axis_strengthened:
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
existing_axis_weakened:
  - stage3_green_revision_min, only when product-spread + utilization evidence is independently strong
existing_axis_kept:
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and raw/unadjusted price basis
- profile availability and corporate-action caveats for 011780, 298020, 011170
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE proxy calculations
- clean 180D corporate-action windows for selected quantitative rows
- R4/L4/C17 schedule consistency
```

Not validated:

```text
- production stock_agent source code
- live watchlist or current candidates
- brokerage execution
- exact original disclosure/report URLs for evidence text
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_specialty_product_spread_quality_boost,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+1,+1,"Specialty product spread plus utilization plus revision bridge beat broad chemical beta","011780 and 298020 generated +60.48 pct and +180.76 pct 90D MFE with shallow early MAE","R4L11_T01_KUMHO_20210121_STAGE3_GREEN_SPREAD_REVISION|R4L11_T02_HYOSUNGTNC_20210121_STAGE3_GREEN_SPREAD_REVISION",3,3,1,medium,canonical_shadow_only,"not production; exact evidence URLs needed"
shadow_weight,c17_broad_chemical_beta_false_green_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+1,+1,"Broad petrochemical reopening beta without durable product spread/margin bridge should not reach Green","011170 had only +3.68 pct 90D MFE and -20.40 pct 90D MAE","R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA",3,3,1,medium,guardrail_shadow_only,"cap Green unless product spread durability and margin bridge are both supported"
shadow_weight,c17_spread_rollover_4b_pre_financial_revision,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+0.5,+0.5,"For cyclical chemical spread names, spread rollover and positioning can precede reported EPS rollover","011780 4B proximity 0.98 and 298020 4B proximity 0.88 captured full-window peak zone","R4L11_T01B_KUMHO_20210506_4B_SPREAD_PEAK_OVERLAY|R4L11_T02B_HYOSUNGTNC_20210716_4B_SPREAD_PEAK_OVERLAY",3,3,1,low,sector_shadow_only,"4B overlay only; do not use as standalone positive-stage demotion without non-price spread evidence"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","source_name":"FinanceData/marcap","min_date":"1995-05-02","tradable_row_count":14354401,"raw_row_count":15214118,"symbol_count":5414,"active_like_symbol_count":2868,"inactive_or_delisted_like_symbol_count":2546,"markets":["KONEX","KOSDAQ","KOSDAQ GLOBAL","KOSPI"],"price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SPREAD_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L11_T01_KUMHO_20210121_STAGE3_GREEN_SPREAD_REVISION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Spread expansion plus revision/margin bridge produced high MFE with shallow initial MAE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C17 case: specialty spread, utilization, and revision bridge beat generic chemical beta."}
{"row_type":"case","case_id":"R4L11_C17_298020_HYOSUNG_SPANDEX_SPREAD_SUPERCYCLE_20210121","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_UTILIZATION_SPREAD_SUPERCYCLE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L11_T02_HYOSUNGTNC_20210121_STAGE3_GREEN_SPREAD_REVISION","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Spandex spread/utilization shock had extreme forward MFE and low early MAE.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Positive C17 case: concentrated product spread and utilization mattered more than broad chemical index move."}
{"row_type":"case","case_id":"R4L11_C17_011170_LOTTE_BASIC_PETROCHEM_FALSE_GREEN_20210223","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BASIC_PETROCHEM_NAPHTHA_PRODUCT_SPREAD_FALSE_GREEN","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Broad reopening/chemical beta without durable product spread bridge had weak MFE and large MAE.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Counterexample: raw material inflation and generic spread optimism were not enough for durable Stage3-Green."}
{"row_type":"trigger","trigger_id":"R4L11_T01_KUMHO_20210121_STAGE3_GREEN_SPREAD_REVISION","case_id":"R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SPREAD_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","green_strictness_stress_test","4B_non_price_requirement_stress_test","residual_false_positive_mining"],"trigger_type":"Stage3-Green","trigger_date":"2021-01-21","evidence_available_at_that_date":"NB latex/synthetic rubber spread expansion, utilization pressure, and early revision bridge had become visible in the 2020-2021 chemical upcycle.","evidence_source":"public result/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-21","entry_price":186000,"MFE_30D_pct":57.8,"MFE_90D_pct":60.48,"MFE_180D_pct":60.48,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-2.15,"MAE_90D_pct":-2.15,"MAE_180D_pct":-4.57,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-40.54,"green_lateness_ratio":0.17,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11_011780_20210121_186000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L11_T01B_KUMHO_20210506_4B_SPREAD_PEAK_OVERLAY","case_id":"R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SPREAD_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","green_strictness_stress_test","4B_non_price_requirement_stress_test","residual_false_positive_mining"],"trigger_type":"4B-Overlay-SpreadPeak","trigger_date":"2021-05-06","evidence_available_at_that_date":"Spread-cycle profit was peaking; the equity was already near the observed full-window high.","evidence_source":"public result/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-06","entry_price":296000,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-31.59,"MAE_90D_pct":-39.36,"MAE_180D_pct":-43.24,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-40.54,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing_if_spread_rollover_evidence_exists","four_b_evidence_type":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11_011780_20210506_296000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same positive case, separate 4B timing overlay; not representative for entry aggregate","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R4L11_T02_HYOSUNGTNC_20210121_STAGE3_GREEN_SPREAD_REVISION","case_id":"R4L11_C17_298020_HYOSUNG_SPANDEX_SPREAD_SUPERCYCLE_20210121","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_UTILIZATION_SPREAD_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","green_strictness_stress_test","4B_non_price_requirement_stress_test","residual_false_positive_mining"],"trigger_type":"Stage3-Green","trigger_date":"2021-01-21","evidence_available_at_that_date":"Spandex spread/utilization shock and earnings revision route were visible before the full rerating.","evidence_source":"public result/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-21","entry_price":288500,"MFE_30D_pct":74.35,"MFE_90D_pct":180.76,"MFE_180D_pct":233.8,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.55,"MAE_90D_pct":-5.55,"MAE_180D_pct":-5.55,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-38.42,"green_lateness_ratio":0.11,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11_298020_20210121_288500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L11_T02B_HYOSUNGTNC_20210716_4B_SPREAD_PEAK_OVERLAY","case_id":"R4L11_C17_298020_HYOSUNG_SPANDEX_SPREAD_SUPERCYCLE_20210121","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_UTILIZATION_SPREAD_SUPERCYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","green_strictness_stress_test","4B_non_price_requirement_stress_test","residual_false_positive_mining"],"trigger_type":"4B-Overlay-SpreadPeak","trigger_date":"2021-07-16","evidence_available_at_that_date":"The spandex spread rerating had reached a full-window peak; spread rollover and positioning risk became more important than trailing EPS strength.","evidence_source":"public result/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-07-16","entry_price":881000,"MFE_30D_pct":9.31,"MFE_90D_pct":9.31,"MFE_180D_pct":9.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-18.73,"MAE_90D_pct":-32.69,"MAE_180D_pct":-46.54,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-38.42,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":0.88,"four_b_timing_verdict":"good_full_window_4B_timing_if_spread_rollover_evidence_exists","four_b_evidence_type":["valuation_blowoff","revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11_298020_20210716_881000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same positive case, separate 4B timing overlay; not representative for entry aggregate","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA","case_id":"R4L11_C17_011170_LOTTE_BASIC_PETROCHEM_FALSE_GREEN_20210223","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"BASIC_PETROCHEM_NAPHTHA_PRODUCT_SPREAD_FALSE_GREEN","sector":"소재·스프레드·전략자원","primary_archetype":"CHEMICAL_COMMODITY_MARGIN_SPREAD","loop_objective":["coverage_gap_fill","counterexample_mining","sector_specific_rule_discovery","canonical_archetype_compression","green_strictness_stress_test","4B_non_price_requirement_stress_test","residual_false_positive_mining"],"trigger_type":"Stage3-Green-FalsePositive","trigger_date":"2021-02-23","evidence_available_at_that_date":"Broad reopening chemical beta and petrochemical spread optimism existed, but product-spread durability and margin bridge were insufficient.","evidence_source":"public result/news/report summary; exact original URLs must be enriched before production promotion","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-02-23","entry_price":326000,"MFE_30D_pct":3.68,"MFE_90D_pct":3.68,"MFE_180D_pct":3.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.04,"MAE_90D_pct":-20.4,"MAE_180D_pct":-31.29,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-33.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"false_positive_green_guard_needed","trigger_outcome_label":"failed_rerating","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L11_011170_20210223_326000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11_C17_011780_KUMHO_NB_LATEX_SPREAD_SUPERCYCLE_20210121","trigger_id":"R4L11_T01_KUMHO_20210121_STAGE3_GREEN_SPREAD_REVISION","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":74,"revision_score":62,"relative_strength_score":70,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":82,"utilization_score":76,"inventory_pressure_score":22,"positioning_overheat_score":38,"spread_rollover_risk_score":0},"weighted_score_before":86.0,"stage_label_before":"Stage3-Yellow_high","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":86,"revision_score":68,"relative_strength_score":72,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":64,"execution_risk_score":32,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":92,"utilization_score":84,"inventory_pressure_score":18,"positioning_overheat_score":42,"spread_rollover_risk_score":0},"weighted_score_after":89.0,"stage_label_after":"Stage3-Green","changed_components":["asp_or_spread_score","margin_bridge_score","utilization_score","revision_score"],"component_delta_explanation":"Specialty product spread and utilization made revision evidence higher quality than broad chemical beta.","MFE_90D_pct":60.48,"MAE_90D_pct":-2.15,"score_return_alignment_label":"Green aligned: high MFE / shallow early MAE.","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11_C17_298020_HYOSUNG_SPANDEX_SPREAD_SUPERCYCLE_20210121","trigger_id":"R4L11_T02_HYOSUNGTNC_20210121_STAGE3_GREEN_SPREAD_REVISION","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":78,"revision_score":66,"relative_strength_score":76,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":36,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":88,"utilization_score":86,"inventory_pressure_score":16,"positioning_overheat_score":40,"spread_rollover_risk_score":0},"weighted_score_before":88.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":90,"revision_score":72,"relative_strength_score":82,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":68,"execution_risk_score":34,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":96,"utilization_score":92,"inventory_pressure_score":14,"positioning_overheat_score":44,"spread_rollover_risk_score":0},"weighted_score_after":92.0,"stage_label_after":"Stage3-Green_high_conviction","changed_components":["asp_or_spread_score","utilization_score","revision_score","relative_strength_score"],"component_delta_explanation":"Spandex spread shock and utilization scarcity justify canonical C17 spread-quality boost.","MFE_90D_pct":180.76,"MAE_90D_pct":-5.55,"score_return_alignment_label":"Green aligned: extreme MFE with controlled early MAE.","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L11_C17_011170_LOTTE_BASIC_PETROCHEM_FALSE_GREEN_20210223","trigger_id":"R4L11_T03_LOTTECHEM_20210223_FALSE_GREEN_SPREAD_BETA","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":54,"revision_score":46,"relative_strength_score":62,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":52,"execution_risk_score":48,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":58,"utilization_score":42,"inventory_pressure_score":40,"positioning_overheat_score":46,"spread_rollover_risk_score":0},"weighted_score_before":76.0,"stage_label_before":"Stage3-Yellow_or_false_Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":42,"revision_score":38,"relative_strength_score":48,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":42,"execution_risk_score":64,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":42,"utilization_score":34,"inventory_pressure_score":58,"positioning_overheat_score":52,"spread_rollover_risk_score":70},"weighted_score_after":63.0,"stage_label_after":"Stage2-Watch_or_4B-risk","changed_components":["asp_or_spread_score","margin_bridge_score","execution_risk_score","inventory_pressure_score","spread_rollover_risk_score"],"component_delta_explanation":"Naphtha/raw-material inflation plus broad beta did not prove durable product spread or margin bridge.","MFE_90D_pct":3.68,"MAE_90D_pct":-20.4,"score_return_alignment_label":"False positive avoided by spread-quality guard.","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R4","loop":"11","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["specialty_product_spread_green_quality_boost","broad_chemical_beta_false_green","spread_rollover_4b_before_financial_revision","green_threshold_sector_specific_exception"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R4L11_C17_051910_LGCHEM_MIXED_BATTERY_CHEMICAL_SCOPE_EXCLUDED","symbol":"051910","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"LG화학 is useful for chemical/battery cross-over discussion, but this loop avoids mixed battery valuation contamination and keeps C17 pure chemical spread cases.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 11
next_round = R5
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json.
- 011780 profile: atlas/symbol_profiles/011/011780.json.
- 298020 profile: atlas/symbol_profiles/298/298020.json.
- 011170 profile: atlas/symbol_profiles/011/011170.json.
- 011780 OHLC: atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv and 2021.csv.
- 298020 OHLC: atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv and 2021.csv.
- 011170 OHLC: atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv.
- Evidence-source URLs require enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
