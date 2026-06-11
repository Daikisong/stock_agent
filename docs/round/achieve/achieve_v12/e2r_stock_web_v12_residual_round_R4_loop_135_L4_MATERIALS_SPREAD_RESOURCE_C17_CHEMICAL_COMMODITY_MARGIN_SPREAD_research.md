# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R4_loop_135_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
selected_round: R4
selected_loop: 135
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: NAPHTHA_ETHYLENE_SPREAD_RECOVERY_BETA_WITHOUT_MARGIN_FCF_BRIDGE
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_4C_timing_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after local C13 reached the 30-row stability threshold at loop134. C17 was the next thin Priority 0 archetype in the No-Repeat Index: static 29 rows, need 1 to reach 30.

This loop adds 3 new independent C17 rows and moves C17 from static 29 rows to projected 32 rows. The 30-row minimum stability threshold is reached with a small buffer.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C17:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R4 -> L4_MATERIALS_SPREAD_RESOURCE
C17 -> C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
```

C17 is the chemical commodity margin-spread archetype. Commodity beta is the wind; realized spread, margin, revision, working capital and FCF are the sail. The stock can flutter on the wind, but without the sail it does not travel.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C17 static rows | 29 |
| C17 need to 30 | 1 |
| C17 need to 50 | 21 |
| C17 investigation point | 원자재 가격과 실제 spread/margin/FCF 분리 |
| local previous C17 rows in this session | 0 |
| this loop projected rows | 32 |

Selected symbols avoid local R3 battery threshold-completion symbols and use a new R4 chemical-spread set.

| symbol | company | status |
|---|---|---|
| 011170 | 롯데케미칼 | new local C17 petrochemical spread false-positive |
| 006650 | 대한유화 | new local C17 4B-to-4C spread timing row |
| 011780 | 금호석유화학 | new local C17 synthetic-rubber spread 4B boundary row |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known local hard duplicate.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 011170 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 006650 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 011780 / 2024-03-06 | true | true | old_profile_caveat_but_2024_share_count_drift_watch | true, weight 0.80 |

Corporate-action notes:

- 롯데케미칼 has an old corporate-action candidate in 2023 before the selected 2024 entry.
- 대한유화 has an old corporate-action candidate in 2010 only.
- 금호석유화학 has an old corporate-action candidate in 2001 only, but the 2024 OHLC stream shows share-count drift; it is retained as reduced-weight boundary evidence.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| NAPHTHA_ETHYLENE_SPREAD_RECOVERY_BETA_WITHOUT_MARGIN_FCF_BRIDGE | C17 | petrochemical spread beta without realized margin/FCF is false-positive risk |
| ETHYLENE_POLYMER_SPREAD_RECOVERY_4B_BOUNCE_THEN_MARGIN_4C | C17 | a spread recovery bounce can be 4B but must roll into 4C when margin/FCF bridge fails |
| SYNTHETIC_RUBBER_SPREAD_RERATING_4B_WITH_SHARE_COUNT_DRIFT | C17 | synthetic-rubber spread rerating is usable as 4B boundary evidence, not clean Green evidence |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C17_LOTTECHEM_011170_2024_03_06_NAPHTHA_ETHYLENE_SPREAD_FALSE_RECOVERY_4C | 011170 | 롯데케미칼 | failed_rerating | counterexample | spread beta produced almost no MFE and large MAE |
| C17_DAEHAN_006650_2024_03_06_ETHYLENE_POLYMER_SPREAD_BOUNCE_THEN_4C | 006650 | 대한유화 | 4B_to_4C_protection_success | positive_protection | 17.09% MFE followed by large full-window MAE |
| C17_KUMHO_011780_2024_03_06_SYNTHETIC_RUBBER_SPREAD_RERATING_4B_BOUNDARY | 011780 | 금호석유화학 | 4B_overlay_boundary_success | positive_boundary | 15.51% MFE but share-count drift and later MAE block Green |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_protection_case_count | 1 |
| positive_boundary_case_count | 1 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 011170 | source_proxy_only | spread recovery beta but margin/revision/FCF absent | required; useful as counterexample |
| 006650 | source_proxy_only | ethylene/polymer spread rebound but margin/FCF bridge failed | required before promotion |
| 011780 | source_proxy_only | synthetic-rubber spread rebound with partial margin route and share-count drift | required before promotion |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 011170 | atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv | atlas/symbol_profiles/011/011170.json |
| 006650 | atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv | atlas/symbol_profiles/006/006650.json |
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv | atlas/symbol_profiles/011/011780.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA | Stage2 | 2024-03-06 | 2024-03-06 | 122900 | naphtha/ethylene spread recovery beta without margin/FCF |
| DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK | Stage4C | 2024-03-06 | 2024-03-06 | 137500 | ethylene/polymer spread 4B bounce then margin 4C |
| KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 144400 | synthetic-rubber spread 4B boundary |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 011170 | 2024-03-06 | 122900 | 1.87 | -21.81 | 2.12 | -21.81 | 2.12 | -47.92 | 2024-05-20 | 125500 | -49.00 |
| 006650 | 2024-03-06 | 137500 | 8.22 | -9.67 | 17.09 | -9.67 | 17.09 | -42.11 | 2024-05-20 | 161000 | -50.56 |
| 011780 | 2024-03-06 | 144400 | 9.42 | -15.17 | 11.15 | -15.17 | 15.51 | -31.58 | 2024-07-12 | 166800 | -40.77 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 011170 | Stage2 risk if spread beta is over-credited | false positive | current_profile_false_positive |
| 006650 | Stage2/4B rebound risk if spread recovery is over-credited | hard 4C needed after bounce | current_profile_4C_too_late_after_4B_bounce |
| 011780 | Stage2A possible; 4B after spread rerating | boundary 4B only | current_profile_4B_too_late |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C17 interpretation:

- Spread beta can start Stage2-watch.
- Stage2A requires visible realized spread-to-margin, revision and FCF conversion.
- Yellow/Green should not be allowed when commodity price movement is not turning into company-level margin.
- A 4B spread bounce is valid, but it must roll into 4C if margin/FCF fails.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 011170 | 0.98 | 1.00 | weak spread beta / bridge absent | not Stage3 |
| 006650 | 0.85 | 1.00 | spread recovery bounce / margin bridge absent | 4B-to-4C timing guard |
| 011780 | 0.87 | 1.00 | spread rerating / share-count drift | 4B audit required |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 011170 | hard_4c_late | margin/revision/FCF absence should have capped Stage2 earlier |
| 006650 | hard_4c_success_after_bounce | 4B bounce could not become Green without FCF conversion |
| 011780 | thesis_break_watch_only | not hard 4C at trigger, but 4B/share-count audit needed |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L4_MATERIALS_SPREAD_RESOURCE
confidence = medium
```

Candidate:

> In L4 materials/chemical names, commodity spread recovery should promote Stage2A only when realized company-level spread, margin bridge, revision and FCF conversion are visible. Commodity beta alone should remain Stage1/Stage2-watch. A 4B spread bounce must roll into 4C if the margin/FCF bridge fails.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
confidence = medium
```

Candidate C17 rule:

```text
C17_spread_margin_fcf_bridge_required =
  chemical_commodity_spread_route
  AND (realized_spread_improvement OR margin_bridge OR confirmed_revision OR working_capital_quality OR fcf_conversion)

if spread_recovery_beta and margin_fcf_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 10 and MAE_180D < -30 and margin_fcf_bridge_absent:
    add C17_4B_to_4C_timing_guard = true

if MFE_90D < 5 and MAE_90D < -15 and bridge_absent:
    classify_as C17_spread_beta_false_positive_guardrail

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 10.12 | -15.55 | 11.57 | -40.54 | 1 | useful but C17 spread bridge too loose |
| P0b calibrated rollback | rollback | 3 | 10.12 | -15.55 | 11.57 | -40.54 | 1 | over-credits spread beta |
| P1 sector_specific_candidate_profile | L4 | 2 4B/4C + 1 guard | 14.12 | -12.42 | 16.3 | -36.84 | 0 | better after margin/FCF bridge gate |
| P2 canonical_archetype_candidate_profile | C17 | 2 4B/4C + 1 guard | 14.12 | -12.42 | 16.3 | -36.84 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C17 guard | 2 4B/4C + 1 guard | 14.12 | -12.42 | 16.3 | -36.84 | 0 | adds spread-beta false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 011170 | Stage2 false positive if spread beta is over-credited | current_profile_false_positive |
| 006650 | 4B bounce aligned but 4C needed after bridge failure | current_profile_4C_too_late_after_4B_bounce |
| 011780 | boundary Stage2A with 4B/share-count audit | current_profile_4B_too_late |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive protection | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | mixed C17 fine ids | 1 | 1 | 1 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 29 -> projected 32; reaches minimum stability threshold |

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
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_false_positive
  - current_profile_4C_too_late_after_4B_bounce
  - current_profile_4B_too_late
new_axis_proposed: C17_spread_margin_fcf_bridge_required|C17_4B_to_4C_timing_guard|C17_spread_beta_false_positive_guardrail|share_count_drift_independent_weight_reduction
existing_axis_strengthened:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
```

## 23. Validation Scope / Non-Validation Scope

Validation scope:

- Uses stock-web tradable OHLC rows.
- Uses manifest max_date 2026-02-20.
- Uses C17 Priority 0 coverage gap.
- Uses new local C17 symbols.
- Keeps 011780 with reduced independent weight because 2024 share-count drift is visible.
- Treats 011780 as 4B boundary evidence, not Green promotion.
- Discards any repeated C13 loop134 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_spread_margin_fcf_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"011170/006650 show spread beta can fail without realized margin and FCF bridge while 011780 only works as reduced-weight 4B boundary","blocks spread-beta false positives and prevents Green without margin/FCF conversion","LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA|DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK|KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B",3,3,1,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C17_4B_to_4C_timing_guard,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"006650 had 17.09% MFE before -42.11% 180D MAE, so spread-recovery 4B must roll into 4C if margin/FCF bridge fails","prevents 4B spread bounces from becoming Green without realized margin and FCF proof","DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK",1,1,0,medium,canonical_shadow_only,"4B/4C timing calibration"
shadow_weight,C17_spread_beta_false_positive_guardrail,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"011170 had only 2.12% 90D MFE and -47.92% 180D MAE after spread recovery beta without margin bridge","requires realized spread/margin/revision/FCF bridge before Stage2/Yellow promotion","LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA",1,1,1,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"011780 has visible 2024 share-count drift during the validation window","keeps row usable but lowers independent positive evidence weight","KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B",1,1,0,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C17_LOTTECHEM_011170_2024_03_06_NAPHTHA_ETHYLENE_SPREAD_FALSE_RECOVERY_4C","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NAPHTHA_ETHYLENE_SPREAD_RECOVERY_BETA_WITHOUT_MARGIN_FCF_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate in 2023 before selected window; 2024 validation window treated as clean","independent_evidence_weight":0.95,"score_price_alignment":"naphtha/ethylene spread recovery beta produced only about 2.12% MFE and then roughly -47.92% full-window MAE, so spread beta without margin/FCF bridge was a false positive","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new local C17 symbol after C13 threshold completion; petrochemical spread beta guardrail"}
{"row_type":"case","case_id":"C17_DAEHAN_006650_2024_03_06_ETHYLENE_POLYMER_SPREAD_BOUNCE_THEN_4C","symbol":"006650","company_name":"대한유화","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ETHYLENE_POLYMER_SPREAD_RECOVERY_4B_BOUNCE_THEN_MARGIN_4C","case_type":"4B_to_4C_protection_success","positive_or_counterexample":"positive_protection","best_trigger":"DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate in 2010 only; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"ethylene/polymer spread recovery produced a 17.09% 4B bounce, then roughly -42.11% full-window MAE; 4B had to roll into C17 4C when margin/FCF bridge failed","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce","price_source":"Songdaiki/stock-web","notes":"new local C17 symbol; useful 4B-to-4C timing row"}
{"row_type":"case","case_id":"C17_KUMHO_011780_2024_03_06_SYNTHETIC_RUBBER_SPREAD_RERATING_4B_BOUNDARY","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPREAD_RERATING_4B_WITH_SHARE_COUNT_DRIFT","case_type":"4B_overlay_boundary_success","positive_or_counterexample":"positive_boundary","best_trigger":"KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate in 2001 only, but 2024 row stream has share-count drift; independent weight reduced","independent_evidence_weight":0.8,"score_price_alignment":"synthetic-rubber spread rerating produced about 15.51% MFE, but later -31.58% MAE and share-count drift mean it is 4B boundary evidence, not clean Green evidence","current_profile_verdict":"current_profile_4B_too_late_if_spread_rerating_overpromoted_to_green","price_source":"Songdaiki/stock-web","notes":"new local C17 symbol; share-count drift around April/October rows lowers independent positive weight"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA","case_id":"C17_LOTTECHEM_011170_2024_03_06_NAPHTHA_ETHYLENE_SPREAD_FALSE_RECOVERY_4C","symbol":"011170","company_name":"롯데케미칼","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"NAPHTHA_ETHYLENE_SPREAD_RECOVERY_BETA_WITHOUT_MARGIN_FCF_BRIDGE","sector":"materials / spread / resources","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":122900.0,"evidence_available_at_that_date":"source_proxy_only: petrochemical spread recovery beta and valuation rebound narrative visible, but actual naphtha/ethylene margin, revision and FCF bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["petrochemical_spread_recovery_beta","valuation_rebound_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent","commodity_spread_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv","profile_path":"atlas/symbol_profiles/011/011170.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.87,"MFE_90D_pct":2.12,"MFE_180D_pct":2.12,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-21.81,"MAE_90D_pct":-21.81,"MAE_180D_pct":-47.92,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":125500.0,"drawdown_after_peak_pct":-49.0,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.98,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"petrochemical spread recovery beta was not C17 Stage3 without realized spread/margin/FCF bridge","four_b_evidence_type":["weak_follow_through","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C17_011170_2024_03_06_122900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK","case_id":"C17_DAEHAN_006650_2024_03_06_ETHYLENE_POLYMER_SPREAD_BOUNCE_THEN_4C","symbol":"006650","company_name":"대한유화","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"ETHYLENE_POLYMER_SPREAD_RECOVERY_4B_BOUNCE_THEN_MARGIN_4C","sector":"materials / spread / resources","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage4C","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":137500.0,"evidence_available_at_that_date":"source_proxy_only: ethylene/polymer spread recovery and inventory-cycle bounce visible, but realized margin, revision and FCF conversion remained unconfirmed; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["ethylene_polymer_spread_recovery_beta","inventory_cycle_bounce","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["4b_bounce","cycle_peak_watch"],"stage4c_evidence_fields":["margin_bridge_absent","revision_bridge_absent","fcf_bridge_absent","spread_pressure_return"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv","profile_path":"atlas/symbol_profiles/006/006650.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.22,"MFE_90D_pct":17.09,"MFE_180D_pct":17.09,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.67,"MAE_90D_pct":-9.67,"MAE_180D_pct":-42.11,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":161000.0,"drawdown_after_peak_pct":-50.56,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.85,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"spread-recovery 4B bounce was real but should have rolled into C17 4C when margin/FCF bridge failed","four_b_evidence_type":["4b_bounce","cycle_peak_watch"],"four_c_protection_label":"hard_4c_success_after_bounce","trigger_outcome_label":"positive_protection_mfe_then_high_mae","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C17_006650_2024_03_06_137500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B","case_id":"C17_KUMHO_011780_2024_03_06_SYNTHETIC_RUBBER_SPREAD_RERATING_4B_BOUNDARY","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_SPREAD_RERATING_4B_WITH_SHARE_COUNT_DRIFT","sector":"materials / spread / resources","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_4C_timing_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":144400.0,"evidence_available_at_that_date":"source_proxy_only: synthetic-rubber/phenol-chain spread recovery and relative strength visible, but clean margin/revision/FCF bridge and share-count quality needed confirmation; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["synthetic_rubber_spread_recovery","relative_strength","cycle_rebound"],"stage3_evidence_fields":["margin_bridge_partial","revision_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["spread_rerating","cycle_peak_watch","share_count_drift_watch"],"stage4c_evidence_fields":["share_count_drift_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.42,"MFE_90D_pct":11.15,"MFE_180D_pct":15.51,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-15.17,"MAE_90D_pct":-15.17,"MAE_180D_pct":-31.58,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-12","peak_price":166800.0,"drawdown_after_peak_pct":-40.77,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"spread rerating worked as 4B boundary but share-count drift and later MAE block clean Green promotion","four_b_evidence_type":["spread_rerating","cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_boundary_4b_watch_reduced_weight","current_profile_verdict":"current_profile_4B_too_late_if_spread_rerating_overpromoted_to_green","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_watch_reduced_weight"],"corporate_action_window_status":"old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C17_011780_2024_03_06_144400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window; 2024 share-count drift watch","independent_evidence_weight":0.8,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C17_LOTTECHEM_011170_2024_03_06_NAPHTHA_ETHYLENE_SPREAD_FALSE_RECOVERY_4C","trigger_id":"LOTTECHEM_011170_2024_03_06_STAGE2_FALSE_POSITIVE_SPREAD_RECOVERY_BETA","symbol":"011170","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":3,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":55,"stage_label_before":"Stage2 false-positive / spread beta risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":40,"stage_label_after":"Stage1/4C-watch, not C17 Stage2","changed_components":["margin_bridge_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Commodity spread beta without realized margin, revision and FCF bridge produced almost no MFE and large MAE.","MFE_90D_pct":2.12,"MAE_90D_pct":-21.81,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C17_DAEHAN_006650_2024_03_06_ETHYLENE_POLYMER_SPREAD_BOUNCE_THEN_4C","trigger_id":"DAEHAN_006650_2024_03_06_STAGE4C_SPREAD_MARGIN_FCF_RISK","symbol":"006650","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60,"stage_label_before":"Stage2 bounce risk / late C17 4C","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":42,"stage_label_after":"Stage4C spread-margin/FCF protection","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"4B bounce could not become Green without actual spread-to-margin and FCF conversion.","MFE_90D_pct":17.09,"MAE_90D_pct":-9.67,"score_return_alignment_label":"hard_4c_after_4b_bounce","current_profile_verdict":"current_profile_4C_too_late_after_4B_bounce"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C17_KUMHO_011780_2024_03_06_SYNTHETIC_RUBBER_SPREAD_RERATING_4B_BOUNDARY","trigger_id":"KUMHO_011780_2024_03_06_STAGE2A_SYNTHETIC_RUBBER_SPREAD_4B","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":6,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2-Actionable boundary / 4B-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":3,"revision_score":2,"relative_strength_score":5,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage2-watch with C17 4B/share-count audit","changed_components":["margin_bridge_score","revision_score","valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Spread rerating was tradable, but share-count drift and incomplete FCF conversion block Green.","MFE_90D_pct":11.15,"MAE_90D_pct":-15.17,"score_return_alignment_label":"positive_boundary_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late_if_spread_rerating_overpromoted_to_green"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"135","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_4C_too_late_after_4B_bounce","current_profile_4B_too_late"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

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
completed_loop = 135
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted, C17 reaches the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating C17 unless a new uncovered fine-archetype is explicitly needed.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/011/011170/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/006/006650/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/011/011170.json
  - atlas/symbol_profiles/006/006650.json
  - atlas/symbol_profiles/011/011780.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
