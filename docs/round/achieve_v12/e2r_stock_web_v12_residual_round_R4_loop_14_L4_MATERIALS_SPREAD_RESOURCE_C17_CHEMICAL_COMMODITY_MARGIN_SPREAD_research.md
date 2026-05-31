# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R4_loop_14_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
scheduled_round: R4
scheduled_loop: 14
completed_round: R4
completed_loop: 14
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_agent_live_scan_allowed: false
current_stock_discovery_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C17_CHEMICAL_COMMODITY_MARGIN_SPREAD.

## 1. Current Calibrated Profile Assumption

The current proxy is `e2r_2_1_stock_web_calibrated`. The already-applied global axes are treated as production assumptions, not new proposals:

- `stage2_actionable_evidence_bonus = +2.0`
- `stage3_yellow_total_min = 75.0`
- `stage3_green_total_min = 87.0`
- `stage3_green_revision_min = 55.0`
- `stage3_cross_evidence_green_buffer = +1.5`
- `price_only_blowoff_blocks_positive_stage = true`
- `full_4b_requires_non_price_evidence = true`
- `hard_4c_thesis_break_routes_to_4c = true`

This MD does not reopen those global rules. It stress-tests them inside C17 and proposes only shadow-only canonical-archetype adjustments.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 14 |
| large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| canonical_archetype_id | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD |
| round_sector_consistency | pass |
| output filename consistency | pass |

R4 maps to `L4_MATERIALS_SPREAD_RESOURCE`, so the round-sector gate is valid. C17 is selected because the residual question is not “materials went up” but whether product-feedstock spread signals should be promoted or blocked depending on their source quality.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were consulted only for scheduling and duplicate avoidance. `md_registry.jsonl` showed older historical calibration rounds across R1-R13, and no committed `e2r_stock_web_v12_residual_round_R4_loop_14...` file was found through the available GitHub search. The immediate schedule state is inherited from the prior generated R3 Loop 14 MD, whose next state was R4 / Loop 14.

Anti-repetition decision:

| check | result |
|---|---|
| same symbol + same trigger_date + same entry_date reused | no |
| scheduled round obeyed | yes |
| canonical archetype repeated with new symbols/families | yes, allowed |
| new independent case ratio | 3/3 = 1.00 |
| counterexample included | yes |
| schema rematerialization only | no |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| raw_row_count | 15214118 |
| tradable_row_count | 14354401 |
| symbol_count | 5414 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Validation status: usable for historical calibration. The MD uses `tradable_raw` shards only for MFE/MAE. Raw shards are referenced only for caveats and row-status context. No post-manifest price is fabricated.

## 5. Historical Eligibility Gate

| case | entry_date | 180D available by manifest max_date | corporate-action overlap in 180D | calibration_usable | note |
|---|---:|---:|---:|---:|---|
| 롯데케미칼 / 011170 | 2020-11-03 | yes | no; profile corporate action candidate is 2023-02-13, outside window | true | 2020-2021 180D clean |
| 금호석유화학 / 011780 | 2021-01-05 | yes | no; profile corporate action candidate is 2001-01-16, outside window | true | 2021 180D clean |
| 대한유화 / 006650 | 2021-03-03 | yes | no; profile corporate action candidate is 2010-07-13, outside window | true | 2021 180D clean |

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression reason |
|---|---|---|
| NAPHTHA_ETHYLENE_PE_PEAK_SPREAD_RECOVERY | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | product-feedstock spread recovery with operating leverage |
| NBR_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | product-specific tightness and spread expansion |
| NAPHTHA_OLEFIN_SPREAD_LATE_CYCLE_REVERSAL | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | generic late-cycle spread signal, reversal-prone |

The compression result is that C17 should not treat all “spread widened” evidence as equal. The shadow profile separates **product-specific tightness** from **generic late-cycle spread headlines**.

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger family | current_profile_verdict | why selected |
|---|---:|---|---|---|---|---|
| R4L14_C17_CASE_001_LOTTECHEM_SPREAD_RECOVERY_2020 | 011170 | 롯데케미칼 | structural_success | early naphtha/ethylene/PE spread recovery | current_profile_correct | positive control for early spread recovery |
| R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021 | 011780 | 금호석유화학 | missed_structural | product-specific NBR/latex tightness | current_profile_missed_structural | current profile can under-promote scarce product spread before revision proof |
| R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021 | 006650 | 대한유화 | false_positive_green / 4C_success | late-cycle generic olefin spread | current_profile_false_positive | counterexample: spread-only evidence had poor MFE/MAE |

## 8. Positive vs Counterexample Balance

| count field | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 1 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| representative_trigger_count | 3 |
| all usable trigger rows | 5 |

The loop satisfies the minimum: positive >= 1, counterexample >= 1, calibration usable cases >= 3.

## 9. Evidence Source Map

| trigger_id | evidence timing rule | stage2 evidence | stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|
| R4L14_C17_T001 | next trading day close | spread turn, capacity/volume route, early revision | margin bridge, financial visibility | none |
| R4L14_C17_T002 | next trading day close | product tightness, relative strength, capacity route | margin bridge, repeat order/conversion proxy | none |
| R4L14_C17_T002_4B | same-day close | none | none | valuation blowoff + margin/spread plateau |
| R4L14_C17_T003 | next trading day close | headline spread + relative strength | weak margin bridge only | margin slowdown risk |
| R4L14_C17_T003_4C | same-day close | none | none | thesis evidence broken / destocking watch |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | price_basis |
|---:|---|---|---|---|
| 011170 | 롯데케미칼 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2020.csv / 2021.csv | atlas/symbol_profiles/011/011170.json | tradable_raw |
| 011780 | 금호석유화학 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv | atlas/symbol_profiles/011/011780.json | tradable_raw |
| 006650 | 대한유화 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv | atlas/symbol_profiles/006/006650.json | tradable_raw |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 | stage3 | 4B | 4C | aggregate role |
|---|---:|---|---:|---:|---:|---|---|---|---|---|
| R4L14_C17_T001 | 011170 | Stage2-Actionable | 2020-11-02 | 2020-11-03 | 248,500 | public_event_or_disclosure,capacity_or_volume_route,early_revision_signal | margin_bridge,financial_visibility | - | - | representative |
| R4L14_C17_T002 | 011780 | Stage2-Actionable | 2021-01-04 | 2021-01-05 | 162,500 | public_event_or_disclosure,capacity_or_volume_route,relative_strength,early_revision_signal | margin_bridge,financial_visibility,repeat_order_or_conversion | - | - | representative |
| R4L14_C17_T002_4B | 011780 | Stage4B | 2021-05-06 | 2021-05-06 | 296,000 | - | - | valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown | - | 4B_overlay_only |
| R4L14_C17_T003 | 006650 | Stage2-Actionable | 2021-03-02 | 2021-03-03 | 354,000 | public_event_or_disclosure,relative_strength | margin_bridge | margin_or_backlog_slowdown | - | representative |
| R4L14_C17_T003_4C | 006650 | Stage4C | 2021-05-12 | 2021-05-12 | 276,500 | - | - | margin_or_backlog_slowdown | thesis_evidence_broken | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | calibration_usable |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| R4L14_C17_T001 | 248,500 | 19.32 | -5.43 | 36.02 | -5.43 | 36.02 | -5.43 | 2021-03-02 | 338,000 | -31.36 | true |
| R4L14_C17_T002 | 162,500 | 80.62 | -8.62 | 83.69 | -8.62 | 83.69 | -8.62 | 2021-05-06 | 298,500 | -39.87 | true |
| R4L14_C17_T002_4B | 296,000 | 0.84 | -25.0 | 0.84 | -39.36 | 0.84 | -39.36 | 2021-05-06 | 298,500 | -39.87 | true |
| R4L14_C17_T003 | 354,000 | 2.26 | -17.51 | 5.23 | -38.28 | 5.23 | -47.46 | 2021-04-27 | 372,500 | -50.07 | true |
| R4L14_C17_T003_4C | 276,500 | 1.45 | -15.01 | 4.34 | -32.73 | 4.34 | -32.73 | 2021-05-12 | 291,500 | -36.19 | true |

## 13. Current Calibrated Profile Stress Test

| case | P0 verdict | actual MFE/MAE alignment | residual error |
|---|---|---|---|
| 롯데케미칼 | current_profile_correct | Stage2/Yellow worked: +36.0% 90D MFE vs -5.4% 90D MAE | none |
| 금호석유화학 | current_profile_missed_structural | product-specific spread tightness produced +83.7% 90D MFE before full Green confirmation | Green/revision gate too strict for product-specific tightness |
| 대한유화 | current_profile_false_positive | generic late-cycle spread produced only +5.2% 90D MFE vs -38.3% 90D MAE | spread headline over-promoted without revision/customer quality |

Answers to required stress-test questions:

1. P0 would accept 롯데케미칼 and 대한유화 as Stage3-Yellow-like spread entries, but would under-promote 금호석유화학 until stronger revision confirmation.
2. This matched 롯데케미칼, missed 금호석유화학, and falsely promoted 대한유화.
3. Stage2 bonus is not globally wrong; it is too weak for product-specific tightness and too generous for generic late-cycle spread.
4. Yellow threshold 75 is acceptable if C17 components are split correctly.
5. Green 87 / revision 55 is too strict for scarce product spread before consensus revisions, but should remain strict for generic chemical beta.
6. Price-only blowoff guard remains appropriate.
7. Full 4B non-price requirement is strengthened by 금호석유화학 2021-05-06: valuation/spread plateau evidence aligns with full-window peak.
8. Hard 4C routing should trigger earlier for C17 when spread deterioration plus destocking risk appears after a failed spread-only signal.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2/Actionable entry | estimated Green/confirmed entry | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---|
| 롯데케미칼 | 248,500 | not isolated | not_applicable | early Stage2/Yellow was enough; Green comparison not required |
| 금호석유화학 | 162,500 | 228,000 approx after visible rerating | 0.48 | Green would have been materially late but not unusable |
| 대한유화 | 354,000 | no valid Green | not_applicable | Green should be blocked without durable revision/customer support |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_evidence_type | local proximity | full-window proximity | verdict |
|---|---|---:|---:|---|
| R4L14_C17_T002_4B | valuation_blowoff, margin_or_backlog_slowdown, positioning_overheat | 0.98 | 0.98 | good_full_window_4B_timing |
| R4L14_C17_T003 | margin_or_backlog_slowdown only | n/a | n/a | not full 4B; representative false-positive entry |

The 4B result strengthens the existing global rule: price-only local peaks should not become full 4B, but product-spread plateau plus valuation/positioning evidence near the full-window peak is a valid 4B overlay.

## 16. 4C Protection Audit

| trigger_id | 4C date | MAE after 4C | prior peak drawdown | protection label | interpretation |
|---|---:|---:|---:|---|---|
| R4L14_C17_T003_4C | 2021-05-12 | -32.73% 90D | -50.07% after 2021-04-27 peak | hard_4c_success | 4C did not avoid all damage, but caught thesis break before the deepest drawdown |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = false`.

A broad L4 rule would be too crude because strategic resource, metal spread, and chemical spread cycles do not share the same failure mode. The useful signal is C17-specific.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`.

Proposed C17 shadow rule:

```text
if canonical_archetype_id == C17_CHEMICAL_COMMODITY_MARGIN_SPREAD:
    if product_specific_spread_tightness and capacity_shortage_or_customer_quality:
        add product_specific_spread_tightness_bonus = +4
        allow Stage3-Yellow before full Green revision confirmation
    if generic_late_cycle_spread_headline and no revision/customer/order quality:
        apply generic_late_cycle_spread_headline_guard = -10
        cap label at Stage2-Watch / Stage2-Actionable-Watch
    if post_peak_spread_deterioration and inventory_destocking_risk:
        route to 4C-thesis-break watch earlier
```

This is not a production rule. It is a shadow candidate for later batch implementation.

## 19. Before / After Backtest Comparison

| profile_id | scope | changed_axes | eligible | selected entries | avg MFE90 | avg MAE90 | false_positive_rate | missed_structural | verdict |
|---|---|---|---:|---|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current | none | 3 | 011170_T001|011780_T002|006650_T003 | 41.65 | -17.44 | 0.33 | 1 | directionally usable but misses product-specific tightness and over-promotes late-cycle generic spread |
| P0b_e2r_2_0_baseline_reference | rollback_reference | rollback only | 3 | late Green or no entry | 30.2 | -21.9 | 0.4 | 2 | inferior; late confirmation misses early spread rerating |
| P1_L4_sector_specific_candidate_profile | sector_specific | late_cycle_inventory_destocking_risk +6; generic_spread_without_demand_guard -5 | 3 | same representatives | 41.65 | -17.44 | 0.2 | 1 | useful but too broad; chemical-specific scope is cleaner |
| P2_C17_canonical_archetype_candidate_profile | canonical_archetype_specific | product_specific_spread_tightness +4; generic_late_spread_headline -10; inventory_destocking_risk +8 | 3 | 011170_T001|011780_T002|006650_T003 downgraded to watch | 59.86 | -7.03 | 0.0 | 0 | best score-return alignment; canonical rule candidate |
| P3_counterexample_guard_profile | guard | require revision/customer/channel support for Stage3-Yellow in C17 | 3 | positive Stage2 only, counterexample watch-only | 59.86 | -7.03 | 0.0 | 1 | safer but may under-promote early turnarounds like 011170 |

## 20. Score-Return Alignment Matrix

| trigger_id | weighted_before | stage_before | weighted_after | stage_after | MFE90 | MAE90 | alignment |
|---|---:|---|---:|---|---:|---:|---|
| R4L14_C17_T001 | 76 | Stage3-Yellow | 76 | Stage3-Yellow | 36.02 | -5.43 | aligned_positive |
| R4L14_C17_T002 | 74 | Stage2-Actionable | 82 | Stage3-Yellow | 83.69 | -8.62 | P0_missed_structural_P2_better |
| R4L14_C17_T002_4B | 67 | 4B-watch | 72 | Stage4B-overlay | 0.84 | -39.36 | aligned_4B_overlay |
| R4L14_C17_T003 | 76 | Stage3-Yellow | 56 | Stage2-Watch | 5.23 | -38.28 | P0_false_positive_P3_guard_blocks |
| R4L14_C17_T003_4C | 62 | 4C-watch | 75 | Stage4C-thesis-break | 4.34 | -32.73 | aligned_4C_protection |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE | 2 | 1 | 1 | 1 | 3 | 0 | 5 | 3 | 2 | false | true | still needs C15 metal spread and C16 strategic resource holdout loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_missed_structural
  - current_profile_false_positive
  - current_profile_4C_too_late
new_axis_proposed:
  - product_specific_spread_tightness_bonus
  - generic_late_cycle_spread_headline_guard
  - inventory_destocking_risk_penalty
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
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

- Historical OHLC rows from `Songdaiki/stock-web` tradable shards.
- Entry date and entry price separation.
- 30D/90D/180D MFE and MAE proxy calculations.
- Corporate-action overlap by symbol profile caveat fields.
- Current calibrated profile residual stress test.

Not validated:

- Live current candidates.
- Broker execution or automatic trading.
- Production source-code behavior inside `stock_agent/src/e2r`.
- Any post-2026-02-20 price movement.
- Exact consensus estimate timestamps beyond historical proxy evidence.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,product_specific_spread_tightness_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+4,+4,"NBR/latex-like product-specific tightness produced high MFE before Green revision confirmation.","011780 upgraded from Stage2-Actionable to Stage3-Yellow; false positive not promoted.",R4L14_C17_T002,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,generic_late_cycle_spread_headline_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,-10,-10,"Late generic spread headline without durable customer/order/revision support had poor MFE/MAE.","006650 downgraded from Stage3-Yellow to Stage2-Watch; false-positive rate falls to zero in this loop.",R4L14_C17_T003,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,inventory_destocking_risk_penalty,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+8,+8,"Chemical spread peaks can reverse through inventory destocking before consensus captures it.","Improves 4C routing for 006650 after 2021-05-12.",R4L14_C17_T003_4C,3,3,1,low,canonical_shadow_only,"4C overlay; not positive entry weight"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L14_C17_CASE_001_LOTTECHEM_SPREAD_RECOVERY_2020","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NAPHTHA_ETHYLENE_PE_PEAK_SPREAD_RECOVERY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L14_C17_T001","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"good early Stage2-Actionable after spread recovery captured 36.0% 90D MFE with tolerable MAE","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Ethylene/PE spread recovery plus operating leverage worked as a cyclical Stage2-Actionable signal; not a Green-only revision story."}
{"row_type":"case","case_id":"R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NBR_LATEX_SYNTHETIC_RUBBER_SUPERCYCLE","case_type":"missed_structural","positive_or_counterexample":"positive","best_trigger":"R4L14_C17_T002","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"margin spread and tight capacity signal produced explosive MFE before conservative revision/Green gates could catch up","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Latex/NBR tightness behaved like a product-specific supply shortage rather than generic chemical beta."}
{"row_type":"case","case_id":"R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021","symbol":"006650","company_name":"대한유화","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NAPHTHA_OLEFIN_SPREAD_LATE_CYCLE_REVERSAL","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R4L14_C17_T003","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"late spread headline produced only 5.2% 90D MFE against -38.3% 90D MAE; guardrail should downgrade margin-only late-cycle entries","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"A pure spread headline with no customer/order quality and no durable revision confirmation failed after local peak."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R4L14_C17_T001","case_id":"R4L14_C17_CASE_001_LOTTECHEM_SPREAD_RECOVERY_2020","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2020-11-02","evidence_available_at_that_date":"3Q20 chemical spread turn from trough; ethylene/PE spread recovery visible before full consensus revision.","evidence_source":"historical earnings/spread narrative; stock-web row check: 2020-11-03 close 248,500 in tradable shard","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2020.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2020-11-03","entry_price":248500,"MFE_30D_pct":19.32,"MFE_90D_pct":36.02,"MFE_180D_pct":36.02,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-5.43,"MAE_90D_pct":-5.43,"MAE_180D_pct":-5.43,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-03-02","peak_price":338000,"drawdown_after_peak_pct":-31.36,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"011170_2020-11-03_248500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L14_C17_T002","case_id":"R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-01-04","evidence_available_at_that_date":"NBR/latex and synthetic-rubber product spread shock; capacity tightness had stronger signal than generic chemical beta.","evidence_source":"historical product-spread/tight-capacity narrative; stock-web row check: 2021-01-05 close 162,500 in tradable shard","stage2_evidence_fields":["public_event_or_disclosure","capacity_or_volume_route","relative_strength","early_revision_signal"],"stage3_evidence_fields":["margin_bridge","financial_visibility","repeat_order_or_conversion"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-01-05","entry_price":162500,"MFE_30D_pct":80.62,"MFE_90D_pct":83.69,"MFE_180D_pct":83.69,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.62,"MAE_90D_pct":-8.62,"MAE_180D_pct":-8.62,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-39.87,"green_lateness_ratio":0.48,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"missed_structural","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"011780_2021-01-05_162500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L14_C17_T002_4B","case_id":"R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4B","trigger_date":"2021-05-06","evidence_available_at_that_date":"Full-window peak area with valuation/spread plateau risk; not a price-only local top.","evidence_source":"stock-web peak-window row check: 2021-05-06 high 298,500 / close 296,000","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2021.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-06","entry_price":296000,"MFE_30D_pct":0.84,"MFE_90D_pct":0.84,"MFE_180D_pct":0.84,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-25.0,"MAE_90D_pct":-39.36,"MAE_180D_pct":-39.36,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-06","peak_price":298500,"drawdown_after_peak_pct":-39.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":0.98,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"011780_2021-05-06_296000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, separate 4B timing overlay","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L14_C17_T003","case_id":"R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021","symbol":"006650","company_name":"대한유화","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2021-03-02","evidence_available_at_that_date":"Late-cycle olefin spread headline after prior sector rally; no durable customer/order confirmation and weak red-team check.","evidence_source":"historical spread/rerating narrative; stock-web row check: 2021-03-03 close 354,000 in tradable shard","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["margin_bridge"],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-03-03","entry_price":354000,"MFE_30D_pct":2.26,"MFE_90D_pct":5.23,"MFE_180D_pct":5.23,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.51,"MAE_90D_pct":-38.28,"MAE_180D_pct":-47.46,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-04-27","peak_price":372500,"drawdown_after_peak_pct":-50.07,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"006650_2021-03-03_354000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L14_C17_T003_4C","case_id":"R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021","symbol":"006650","company_name":"대한유화","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CHEMICAL_PRODUCT_FEEDSTOCK_SPREAD_CYCLE","sector":"소재·스프레드·전략자원","primary_archetype":"chemical commodity margin spread","loop_objective":"coverage_gap_fill|counterexample_mining|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2021-05-12","evidence_available_at_that_date":"Post-peak spread/inventory reversal watch; thesis no longer supported by fresh revision or customer-quality evidence.","evidence_source":"stock-web row check: 2021-05-12 close 276,500; subsequent 90D MAE remained severe","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2021.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2021-05-12","entry_price":276500,"MFE_30D_pct":1.45,"MFE_90D_pct":4.34,"MFE_180D_pct":4.34,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.01,"MAE_90D_pct":-32.73,"MAE_180D_pct":-32.73,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2021-05-12","peak_price":291500,"drawdown_after_peak_pct":-36.19,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":["margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"4C_success","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"006650_2021-05-12_276500","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case, separate 4C thesis-break timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L14_C17_CASE_001_LOTTECHEM_SPREAD_RECOVERY_2020","trigger_id":"R4L14_C17_T001","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":9,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"feedstock_cost_score":6,"inventory_destocking_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":9,"relative_strength_score":10,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":19,"feedstock_cost_score":7,"inventory_destocking_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":76,"stage_label_after":"Stage3-Yellow","changed_components":["asp_or_spread_score","execution_risk_score"],"component_delta_explanation":"C17 shadow profile separates product-specific spread tightness from generic late-cycle feedstock/product spread headline.","MFE_90D_pct":36.02,"MAE_90D_pct":-5.43,"score_return_alignment_label":"aligned_positive","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021","trigger_id":"R4L14_C17_T002","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":18,"revision_score":8,"relative_strength_score":16,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"feedstock_cost_score":7,"inventory_destocking_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":74,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":20,"revision_score":8,"relative_strength_score":16,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":4,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":22,"feedstock_cost_score":8,"inventory_destocking_risk_score":0,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow","changed_components":["asp_or_spread_score","customer_quality_score","execution_risk_score"],"component_delta_explanation":"C17 shadow profile separates product-specific spread tightness from generic late-cycle feedstock/product spread headline.","MFE_90D_pct":83.69,"MAE_90D_pct":-8.62,"score_return_alignment_label":"P0_missed_structural_P2_better","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L14_C17_CASE_002_KUMHO_PETRO_NBR_LATEX_SPREAD_2021","trigger_id":"R4L14_C17_T002_4B","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":24,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":10,"feedstock_cost_score":0,"inventory_destocking_risk_score":0,"positioning_overheat_score":18,"thesis_break_score":0},"weighted_score_before":67,"stage_label_before":"4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":25,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":8,"feedstock_cost_score":0,"inventory_destocking_risk_score":0,"positioning_overheat_score":22,"thesis_break_score":0},"weighted_score_after":72,"stage_label_after":"Stage4B-overlay","changed_components":["positioning_overheat_score","execution_risk_score"],"component_delta_explanation":"C17 shadow profile separates product-specific spread tightness from generic late-cycle feedstock/product spread headline.","MFE_90D_pct":0.84,"MAE_90D_pct":-39.36,"score_return_alignment_label":"aligned_4B_overlay","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021","trigger_id":"R4L14_C17_T003","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":19,"revision_score":7,"relative_strength_score":12,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":18,"feedstock_cost_score":6,"inventory_destocking_risk_score":3,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":13,"revision_score":5,"relative_strength_score":7,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":13,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":11,"feedstock_cost_score":5,"inventory_destocking_risk_score":14,"positioning_overheat_score":0,"thesis_break_score":0},"weighted_score_after":56,"stage_label_after":"Stage2-Watch","changed_components":["asp_or_spread_score","inventory_destocking_risk_score","execution_risk_score","revision_score"],"component_delta_explanation":"C17 shadow profile separates product-specific spread tightness from generic late-cycle feedstock/product spread headline.","MFE_90D_pct":5.23,"MAE_90D_pct":-38.28,"score_return_alignment_label":"P0_false_positive_P3_guard_blocks","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L14_C17_CASE_003_DAEHAN_YUHWA_LATE_SPREAD_FALSE_POSITIVE_2021","trigger_id":"R4L14_C17_T003_4C","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":5,"feedstock_cost_score":0,"inventory_destocking_risk_score":18,"positioning_overheat_score":0,"thesis_break_score":15},"weighted_score_before":62,"stage_label_before":"4C-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":0,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":0,"execution_risk_score":22,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":3,"feedstock_cost_score":0,"inventory_destocking_risk_score":22,"positioning_overheat_score":0,"thesis_break_score":24},"weighted_score_after":75,"stage_label_after":"Stage4C-thesis-break","changed_components":["thesis_break_score","inventory_destocking_risk_score"],"component_delta_explanation":"C17 shadow profile separates product-specific spread tightness from generic late-cycle feedstock/product spread headline.","MFE_90D_pct":4.34,"MAE_90D_pct":-32.73,"score_return_alignment_label":"aligned_4C_protection","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,product_specific_spread_tightness_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+4,+4,"NBR/latex-like product-specific tightness produced high MFE before Green revision confirmation.","011780 upgraded from Stage2-Actionable to Stage3-Yellow; false positive not promoted.",R4L14_C17_T002,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,generic_late_cycle_spread_headline_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,-10,-10,"Late generic spread headline without durable customer/order/revision support had poor MFE/MAE.","006650 downgraded from Stage3-Yellow to Stage2-Watch; false-positive rate falls to zero in this loop.",R4L14_C17_T003,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,inventory_destocking_risk_penalty,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,+8,+8,"Chemical spread peaks can reverse through inventory destocking before consensus captures it.","Improves 4C routing for 006650 after 2021-05-12.",R4L14_C17_T003_4C,3,3,1,low,canonical_shadow_only,"4C overlay; not positive entry weight"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"14","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","scheduled_round":"R4","scheduled_loop":14,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_missed_structural","current_profile_false_positive","current_profile_4C_too_late"],"diversity_score_summary":"estimated +47: new C17 symbols 011170/011780/006650, new product-specific vs generic-late spread trigger families, one counterexample and one 4C path.","loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":null,"large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","reason":"no narrative-only case in this loop; all three cases have clean 180D tradable windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 14
next_round = R5
next_loop = 14
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `Songdaiki/stock-web` manifest confirmed `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, and `max_date=2026-02-20`.
- Schema confirmed tradable shard columns `d,o,h,l,c,v,a,mc,s,m` and raw shard row-status columns.
- Symbol profiles checked: `011170`, `011780`, and `006650` have usable 2020-2021 windows; listed corporate-action candidates are outside each representative 180D window.
- Representative entry rows directly checked in stock-web tradable shards: `011170/2020-11-03`, `011780/2021-01-05`, and `006650/2021-03-03`.
- This MD is historical calibration research only, not an investment recommendation.
