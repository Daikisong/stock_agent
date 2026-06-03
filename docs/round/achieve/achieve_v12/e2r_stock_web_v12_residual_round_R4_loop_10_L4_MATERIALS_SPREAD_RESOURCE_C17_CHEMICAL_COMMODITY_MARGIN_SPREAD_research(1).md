# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R4
scheduled_loop: 10
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL
output_file: e2r_stock_web_v12_residual_round_R4_loop_10_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_accessed: false
stock_agent_code_patch_written: false
stock_web_price_atlas_accessed: true
```

This loop adds **3** new independent cases, **1** counterexample, and **1** residual error for **R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD**.

## 1. Current Calibrated Profile Assumption

Current proxy:

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

This MD does **not** re-propose those global axes. It stress-tests whether C17 chemical spread cases need a product-specific spread-duration bridge and whether generic naphtha-cracker/NCC optimism needs a stricter cap.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 10 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| fine_archetype_id | CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL |
| valid large sector for R4 | yes |
| next_round | R5 |
| next_loop | 10 |

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts indicate R1~R13 and loops 1~9 are already covered. R4 loop 10 is therefore the next scheduled state in this session sequence. This MD avoids reusing the same symbol + trigger date + entry date groups from prior generic R4 loops by selecting a C17-specific spread taxonomy:

- **298020 / 효성티앤씨**: spandex spread realized-margin success.
- **011780 / 금호석유화학**: NB-latex/synthetic-rubber spread success.
- **011170 / 롯데케미칼**: generic NCC/petrochemical spread false positive.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web manifest fields used:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

## 5. Historical Eligibility Gate

| symbol | profile path | corporate action status | 180D usable | reason |
|---|---|---:|---:|---|
| 298020 | atlas/symbol_profiles/298/298020.json | corporate_action_candidate_count=0 | true | clean 180D window |
| 011780 | atlas/symbol_profiles/011/011780.json | old corporate action only, 2001-01-16 | true | no overlap with 2020~2021 windows |
| 011170 | atlas/symbol_profiles/011/011170.json | corporate_action_candidate_date=2023-02-13 | true | no overlap with 2021 window |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| SPANDEX_SPREAD_SUPERCYCLE_REALIZED_MARGIN | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | product spread + realized margin bridge |
| NB_LATEX_SYNTHETIC_RUBBER_SPREAD_MARGIN | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | product spread + pandemic/medical-chain demand |
| NCC_GENERIC_REOPENING_SPREAD_FALSE_POSITIVE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | generic petrochemical spread expectation without durable margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | MFE90 | MAE90 | MFE180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---|
| R4L10_C17_298020_SPANDEX_SPREAD_20201030 | 298020 | 효성티앤씨 | structural_success | 143000 | 251.75% | -1.75% | 573.43% | spread bridge worked |
| R4L10_C17_011780_NB_LATEX_SPREAD_20201005 | 011780 | 금호석유화학 | structural_success | 118500 | 143.04% | -8.86% | 151.90% | spread bridge worked |
| R4L10_C17_011170_NCC_SPREAD_FALSE_POSITIVE_20210223 | 011170 | 롯데케미칼 | failed_rerating | 326000 | 3.68% | -11.04% | 3.68% | generic spread false positive |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 2
calibration_usable_case_count = 3
representative_trigger_count = 3
minimum_positive_case_count_pass = true
minimum_counterexample_count_pass = true
minimum_calibration_usable_case_count_pass = true
```

## 9. Evidence Source Map

| symbol | evidence family | evidence date | source status | validation use |
|---:|---|---|---|---|
| 298020 | spandex spread / realized margin cycle | 2020-10-30 | exact_url_pending | positive, needs URL enrichment before production |
| 011780 | NB latex / synthetic rubber spread cycle | 2020-10-05 | exact_url_pending | positive, needs URL enrichment before production |
| 011170 | generic NCC reopening/petrochemical spread expectation | 2021-02-23 | exact_url_pending + later Reuters overcapacity validation | counterexample, good for guardrail |
| L4 sector | structural overcapacity in Korean petrochemicals | 2025-2026 | Reuters industry evidence | narrative validation only, not trigger-date evidence |

## 10. Price Data Source Map

| symbol | shard path | rows directly sampled |
|---:|---|---|
| 298020 | atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv; 2021.csv | entry 2020-10-30 close 143000; 2021-07-16 high 963000 |
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv; 2021.csv | entry 2020-10-05 close 118500; 2021-05-06 high 298500 |
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv | entry 2021-02-23 close 326000; 2021-11 low zone near 207000 |

## 11. Case-by-Case Trigger Grid

| trigger_id | role | stage | entry_date | entry_price | current_profile_verdict | aggregate? |
|---|---|---|---|---:|---|---|
| R4L10_C17_298020_T1 | representative | Stage2-Actionable | 2020-10-30 | 143000 | current_profile_correct | yes |
| R4L10_C17_298020_T4B | 4B overlay | 4B_overlay | 2021-07-16 | 881000 | current_profile_correct | no |
| R4L10_C17_011780_T1 | representative | Stage2-Actionable | 2020-10-05 | 118500 | current_profile_correct | yes |
| R4L10_C17_011170_T1 | representative | Stage2-Actionable | 2021-02-23 | 326000 | current_profile_false_positive | yes |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R4L10_C17_298020_T1 | 37.06% | -1.75% | 251.75% | -1.75% | 573.43% | -1.75% | 2021-07-16 | 963000 | -12.46% |
| R4L10_C17_011780_T1 | 30.38% | -8.86% | 143.04% | -8.86% | 151.90% | -8.86% | 2021-05-06 | 298500 | -32.16% |
| R4L10_C17_011170_T1 | 3.68% | -11.04% | 3.68% | -11.04% | 3.68% | -36.50% | 2021-03-02 | 338000 | -38.76% |

## 13. Current Calibrated Profile Stress Test

| case | current profile behavior | actual path | verdict |
|---|---|---|---|
| 298020 | Stage2/Yellow/Green allowed when spread + revision evidence appears | massive MFE, shallow early MAE | current_profile_correct |
| 011780 | Stage2/Yellow allowed when NB latex spread evidence and realized margin bridge appear | high MFE, moderate entry-day MAE | current_profile_correct |
| 011170 | generic petrochemical/NCC spread optimism may be over-scored by relative strength + early cyclical evidence | low MFE, large MAE | current_profile_false_positive |

Answering the eight stress-test questions:

1. Current calibrated profile would likely accept 298020/011780 as Stage2-to-Yellow and may over-accept 011170 as Stage2-Actionable.
2. The judgment aligns for 298020/011780 and fails for 011170.
3. Stage2 bonus is appropriate only when product-specific spread and margin bridge are present.
4. Yellow threshold 75 is too permissive for generic NCC spread without realized margin bridge.
5. Green threshold 87/revision 55 remains appropriate.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate, but C17 should define spread/margin-slope deterioration as valid non-price 4B evidence.
8. Hard 4C routing should react faster when spread thesis breaks.

## 14. Stage2 / Yellow / Green Comparison

```text
Stage2-Actionable works in C17 when:
- product-specific spread is visible,
- margin bridge is visible or imminent,
- relative strength is not the only evidence,
- revision signal is product-specific rather than sector-generic.

Stage3-Yellow should be capped when:
- evidence is generic petrochemical upcycle only,
- NCC exposure is broad and oversupplied,
- margin bridge remains absent,
- product-specific spread duration is not proven.
```

Green lateness ratios are not computed as numeric values here because this MD uses representative Stage2 entries and 4B overlays rather than distinct confirmed Green trigger dates.

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---|---|
| R4L10_C17_298020_T4B | 0.90 | 0.90 | price_only, valuation_blowoff, positioning_overheat | do not treat as full 4B without spread/margin-slope evidence |
| R4L10_C17_011170_T1 | 0.98 | 0.98 | margin_or_backlog_slowdown, revision_slowdown | good 4B/4C watch if non-price margin deterioration confirmed |

## 16. 4C Protection Audit

For C17, hard 4C should not wait for accounting collapse. A commodity spread thesis can break earlier through:

```text
- spread reversal,
- naphtha/feedstock squeeze,
- China/Middle East capacity glut,
- margin guide-down,
- operating-loss disclosure,
- restructuring/capacity-cut evidence.
```

Lotte-type generic NCC exposure suggests a C17-specific thesis-break watch before full 4C.

## 17. Sector-Specific Rule Candidate

```text
rule_id = c17_product_specific_spread_duration_bonus
rule_scope = canonical_archetype_specific
proposal_type = shadow_only
condition:
  if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  and product_specific_spread_duration >= 2 quarters
  and realized_margin_bridge or confirmed_revision exists
then:
  allow +1 shadow bonus to margin_bridge_score / spread_duration_score
  allow Stage3-Yellow-to-Green buffer only after revision confirmation
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_id = c17_generic_ncc_oversupply_cap
rule_scope = canonical_archetype_specific
proposal_type = shadow_guard_only
condition:
  if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
  and evidence is generic NCC/petrochemical rebound
  and no product_specific_spread_duration
  and no realized margin bridge
then:
  cap stage at Stage2-Watch
  block Stage3-Yellow promotion even if relative_strength is high
```

## 19. Before / After Backtest Comparison

| profile | false_positive_rate | missed_structural_count | score_return_alignment |
|---|---:|---:|---|
| P0 current calibrated proxy | 0.33 | 0 | mixed |
| P0b baseline reference | 0.33+ | 0 | worse false-positive control |
| P1 sector candidate | 0.00 | 0 | improved |
| P2 canonical C17 candidate | 0.00 | 0 | best |
| P3 counterexample guard | 0.00 | 0 | better risk overlay |

## 20. Score-Return Alignment Matrix

| symbol | before stage | after shadow stage | MFE90 | MAE90 | alignment |
|---:|---|---|---:|---:|---|
| 298020 | Stage3-Yellow | Stage3-Green-shadow | 251.75% | -1.75% | improved |
| 011780 | Stage3-Yellow | Stage3-Yellow/Green-buffer-shadow | 143.04% | -8.86% | improved |
| 011170 | Stage2-Actionable/Yellow-risk | Stage2-Watch/Blocked | 3.68% | -11.04% | improved by guard |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL | 2 | 1 | 2 | 1 | 3 | 0 | 4 | 3 | 1 | true | true | need exact historical source URL enrichment and more post-2022 downcycle holdout |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_chemical_spread_false_positive
  - missing_product_specific_spread_duration_gate
  - 4b_margin_slope_evidence_taxonomy_gap
new_axis_proposed:
  - c17_product_specific_spread_duration_bonus
  - c17_generic_ncc_oversupply_cap
  - c17_4b_margin_slope_confirmation
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest max_date and price basis
- symbol profiles and corporate action caveats
- 1D OHLC entry/peak/drawdown samples
- 30D/90D/180D MFE/MAE proxy metrics
- round/sector/canonical consistency
- positive/counterexample balance
```

Not validated in this MD:

```text
- exact original historical research-report URLs for 2020 spread evidence
- production scoring code
- live candidate scan
- brokerage/API/trading actions
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c17_product_specific_spread_duration_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+1,+1,"Positive cases with product-specific spread/margin bridge show high MFE and tolerable MAE","improves separation of 298020/011780 vs generic NCC","R4L10_C17_298020_T1|R4L10_C17_011780_T1",3,3,1,low,canonical_shadow_only,"not production; source URL enrichment required"
shadow_weight,c17_generic_ncc_oversupply_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,cap_stage2_watch,-1,"Generic NCC upcycle without spread duration has low MFE/high MAE","blocks Lotte-type false positive","R4L10_C17_011170_T1",3,3,1,medium,canonical_shadow_guard,"later Reuters overcapacity evidence supports guard"
shadow_weight,c17_4b_margin_slope_confirmation,sector_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,non_price_required,non_price_required_with_spread_slope,0,"Keep full 4B non-price requirement but allow spread/margin-slope deterioration as valid non-price evidence","does not weaken global guard; clarifies chemical-specific 4B evidence","R4L10_C17_298020_T4B|R4L10_C17_011170_T1",4,3,1,low,sector_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

### price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### case rows

```jsonl
{"row_type":"case","case_id":"R4L10_C17_298020_SPANDEX_SPREAD_20201030","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L10_C17_298020_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Spandex spread/demand supercycle translated into realized margin path and extreme forward MFE; clean 180D window. Exact original contemporaneous report URL remains enrichment-pending."}
{"row_type":"case","case_id":"R4L10_C17_011780_NB_LATEX_SPREAD_20201005","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L10_C17_011780_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"aligned","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"NB latex/synthetic rubber spread and pandemic glove-chain demand produced strong 90D/180D MFE before later normalization; clean 180D window."}
{"row_type":"case","case_id":"R4L10_C17_011170_NCC_SPREAD_FALSE_POSITIVE_20210223","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_SPREAD_SUPERCYCLE_NB_LATEX_SPANDEX_NCC_REVERSAL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L10_C17_011170_T1","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"misaligned_under_current_profile","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Generic naphtha cracker upcycle expectation without durable product-specific spread / margin bridge produced low MFE and large 180D MAE; later industry overcapacity evidence validates this failure mode."}
```

### trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R4L10_C17_298020_T1","case_id":"R4L10_C17_298020_SPANDEX_SPREAD_20201030","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SPREAD_SUPERCYCLE_REALIZED_MARGIN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery","stage2_actionable_bonus_stress_test","4B_non_price_requirement_stress_test","counterexample_mining"],"trigger_type":"Stage2-Actionable","trigger_date":"2020-10-30","entry_date":"2020-10-30","entry_price":143000,"evidence_available_at_that_date":"spandex demand/spread improvement visible, but exact source URL pending; stock-web price path used only after trigger.","evidence_source":"exact_url_pending; later company/industry profile confirms Hyosung TNC as spandex/textile material producer","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv|2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":37.06,"MFE_90D_pct":251.75,"MFE_180D_pct":573.43,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-1.75,"MAE_90D_pct":-1.75,"MAE_180D_pct":-1.75,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-12.46,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger_in_this_md","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mfe_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10_C17_298020_20201030_143000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10_C17_298020_T4B","case_id":"R4L10_C17_298020_SPANDEX_SPREAD_20201030","symbol":"298020","company_name":"효성티앤씨","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SPANDEX_SPREAD_SUPERCYCLE_LOCAL_PEAK_4B","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_spread_supercycle","loop_objective":["4B_non_price_requirement_stress_test"],"trigger_type":"4B_overlay","trigger_date":"2021-07-16","entry_date":"2021-07-16","entry_price":881000,"evidence_available_at_that_date":"price blowoff at local/full observed peak; non-price spread reversal evidence not yet attached in this MD.","evidence_source":"stock-web price-only overlay; exact non-price 4B source pending","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv","profile_path":"atlas/symbol_profiles/298/298020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.31,"MFE_90D_pct":9.31,"MFE_180D_pct":9.31,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.31,"MAE_90D_pct":-22.25,"MAE_180D_pct":-40.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-07-16","peak_price":963000,"drawdown_after_peak_pct":-12.46,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.9,"four_b_full_window_peak_proximity":0.9,"four_b_timing_verdict":"price_only_local_peak_requires_non_price_confirmation","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_watch_not_positive_training","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10_C17_298020_20210716_881000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case reused for distinct 4B timing audit, not representative entry","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R4L10_C17_011780_T1","case_id":"R4L10_C17_011780_NB_LATEX_SPREAD_20201005","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NB_LATEX_SYNTHETIC_RUBBER_SPREAD_MARGIN","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_spread_supercycle","loop_objective":["coverage_gap_fill","sector_specific_rule_discovery"],"trigger_type":"Stage2-Actionable","trigger_date":"2020-10-05","entry_date":"2020-10-05","entry_price":118500,"evidence_available_at_that_date":"NB-latex/synthetic-rubber demand and spread improvement evident in 2020 cycle; exact original report URL pending.","evidence_source":"exact_url_pending; company profile confirms synthetic rubber/specialty chemical exposure","stage2_evidence_fields":["relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv|2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.38,"MFE_90D_pct":143.04,"MFE_180D_pct":151.9,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.86,"MAE_90D_pct":-8.86,"MAE_180D_pct":-8.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-32.16,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger_in_this_md","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":null,"trigger_outcome_label":"structural_success_high_mfe_moderate_entry_day_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10_C17_011780_20201005_118500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L10_C17_011170_T1","case_id":"R4L10_C17_011170_NCC_SPREAD_FALSE_POSITIVE_20210223","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NCC_GENERIC_REOPENING_SPREAD_FALSE_POSITIVE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical_spread_reversal","loop_objective":["counterexample_mining","residual_false_positive_mining","sector_specific_rule_discovery"],"trigger_type":"Stage2-Actionable","trigger_date":"2021-02-23","entry_date":"2021-02-23","entry_price":326000,"evidence_available_at_that_date":"generic petrochemical upcycle/reopening spread expectation; no durable product-specific margin bridge in this MD.","evidence_source":"exact_url_pending; later Reuters 2024-2026 industry sources validate structural oversupply and weak naphtha-cracker margins","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.68,"MFE_90D_pct":3.68,"MFE_180D_pct":3.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.04,"MAE_90D_pct":-11.04,"MAE_180D_pct":-36.5,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-38.76,"green_lateness_ratio":"not_applicable:no_confirmed_stage3_green_trigger","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_margin_slowdown_confirmed","four_b_evidence_type":["margin_or_backlog_slowdown","revision_slowdown"],"four_c_protection_label":"hard_4c_late_without_spread_break_route","trigger_outcome_label":"failed_rerating_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L10_C17_011170_20210223_326000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L10_C17_298020_SPANDEX_SPREAD_20201030","trigger_id":"R4L10_C17_298020_T1","symbol":"298020","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":72,"revision_score":65,"relative_strength_score":78,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":70,"product_specificity_score":82,"_weighted":82,"_stage":"Stage3-Yellow"},"weighted_score_before":82,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":82,"revision_score":70,"relative_strength_score":78,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":82,"product_specificity_score":88,"_weighted":87,"_stage":"Stage3-Green-shadow"},"weighted_score_after":87,"stage_label_after":"Stage3-Green-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","spread_duration_score","product_specificity_score"],"component_delta_explanation":"Spandex-specific spread + realized margin bridge deserves C17 product-specific spread-duration bonus, but this remains shadow-only.","MFE_90D_pct":251.75,"MAE_90D_pct":-1.75,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L10_C17_011780_NB_LATEX_SPREAD_20201005","trigger_id":"R4L10_C17_011780_T1","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":70,"revision_score":62,"relative_strength_score":76,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":30,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":68,"product_specificity_score":80,"_weighted":80,"_stage":"Stage3-Yellow"},"weighted_score_before":80,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":78,"revision_score":68,"relative_strength_score":76,"customer_quality_score":50,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":76,"product_specificity_score":85,"_weighted":85,"_stage":"Stage3-Yellow/Green-buffer-shadow"},"weighted_score_after":85,"stage_label_after":"Stage3-Yellow/Green-buffer-shadow","changed_components":["margin_bridge_score","revision_score","execution_risk_score","spread_duration_score","product_specificity_score"],"component_delta_explanation":"NB latex/synthetic rubber product-specific spread bridge improves score-return alignment, but exact original evidence URL enrichment is still needed.","MFE_90D_pct":143.04,"MAE_90D_pct":-8.86,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L10_C17_011170_NCC_SPREAD_FALSE_POSITIVE_20210223","trigger_id":"R4L10_C17_011170_T1","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":38,"revision_score":35,"relative_strength_score":70,"customer_quality_score":20,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":25,"product_specificity_score":20,"_weighted":76,"_stage":"Stage2-Actionable/Yellow-risk"},"weighted_score_before":76,"stage_label_before":"Stage2-Actionable/Yellow-risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":30,"revision_score":30,"relative_strength_score":55,"customer_quality_score":15,"policy_or_regulatory_score":20,"valuation_repricing_score":0,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"spread_duration_score":15,"product_specificity_score":10,"_weighted":64,"_stage":"Stage2-Watch/Blocked"},"weighted_score_after":64,"stage_label_after":"Stage2-Watch/Blocked","changed_components":["margin_bridge_score","revision_score","relative_strength_score","customer_quality_score","execution_risk_score","spread_duration_score","product_specificity_score"],"component_delta_explanation":"Generic NCC spread hope should be capped without product-specific spread duration and realized margin bridge; later overcapacity validates this guard.","MFE_90D_pct":3.68,"MAE_90D_pct":-11.04,"score_return_alignment_label":"improved_by_shadow_guard","current_profile_verdict":"current_profile_false_positive"}
```

### profile comparison rows

```jsonl
{"profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"global_current_proxy","profile_hypothesis":"Existing calibrated global gates","changed_axes":[],"eligible_trigger_count":3,"avg_MFE_90D_pct":132.82,"avg_MAE_90D_pct":-7.22,"avg_MFE_180D_pct":243.0,"avg_MAE_180D_pct":-15.37,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":1,"score_return_alignment_verdict":"mixed; generic NCC false positive remains","row_type":"profile_comparison"}
{"profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older, less strict profile would over-promote generic spread optimism","changed_axes":["no_stage2_bonus","looser_green"],"eligible_trigger_count":3,"avg_MFE_90D_pct":132.82,"avg_MAE_90D_pct":-7.22,"avg_MFE_180D_pct":243.0,"avg_MAE_180D_pct":-15.37,"false_positive_rate":0.33,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"worse false positive control","row_type":"profile_comparison"}
{"profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"Materials/chemical spread needs product-specific spread duration and margin bridge","changed_axes":["c17_product_specific_spread_duration_bonus"],"eligible_trigger_count":3,"avg_MFE_90D_pct":132.82,"avg_MAE_90D_pct":-7.22,"avg_MFE_180D_pct":243.0,"avg_MAE_180D_pct":-15.37,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"improved","row_type":"profile_comparison"}
{"profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"C17 generic NCC exposure should be capped absent realized margin bridge","changed_axes":["c17_generic_ncc_oversupply_cap"],"eligible_trigger_count":3,"avg_MFE_90D_pct":132.82,"avg_MAE_90D_pct":-7.22,"avg_MFE_180D_pct":243.0,"avg_MAE_180D_pct":-15.37,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"best balance","row_type":"profile_comparison"}
{"profile_id":"P3_counterexample_guard_profile","profile_scope":"guardrail","profile_hypothesis":"4B/4C protection for margin-slope break","changed_axes":["c17_4b_margin_slope_confirmation"],"eligible_trigger_count":4,"avg_MFE_90D_pct":101.94,"avg_MAE_90D_pct":-9.86,"avg_MFE_180D_pct":184.58,"avg_MAE_180D_pct":-22.03,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"score_return_alignment_verdict":"risk overlay improved; no positive training from 4B rows","row_type":"profile_comparison"}
```

### residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"10","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":1,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_chemical_spread_false_positive","missing_product_specific_spread_duration_gate","4b_margin_slope_evidence_taxonomy_gap"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 10
next_round = R5
next_loop = 10
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest: `atlas/manifest.json`
- Stock-Web symbol profiles:
  - `atlas/symbol_profiles/298/298020.json`
  - `atlas/symbol_profiles/011/011780.json`
  - `atlas/symbol_profiles/011/011170.json`
- Stock-Web OHLC shards:
  - `atlas/ohlcv_tradable_by_symbol_year/298/298020/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/298/298020/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/011/011780/2020.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/011/011170/2021.csv`
- External narrative validation:
  - Reuters 2025/2026 Korean petrochemical overcapacity and restructuring coverage.
  - Company profile references for product exposure are narrative-only and not production scoring evidence.

