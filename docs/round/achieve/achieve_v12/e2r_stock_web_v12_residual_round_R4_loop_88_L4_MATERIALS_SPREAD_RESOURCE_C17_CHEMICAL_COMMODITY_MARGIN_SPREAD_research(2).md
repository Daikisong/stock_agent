# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R4_loop_88_L4_MATERIALS_SPREAD_RESOURCE_C17_CHEMICAL_COMMODITY_MARGIN_SPREAD_research.md
selected_round: R4
selected_loop: 88
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
fine_archetype_id: SYNTHETIC_RUBBER_BD_SPREAD_MARGIN_RERATING_4B_WATCH
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - 4B_non_price_requirement_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This loop adds 3 independent cases, 2 C17 chemical-spread success paths, and 1 realized-spread/margin-bridge counterexample for R4/L4/C17.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

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

C17 is the chemical/commodity spread conversion archetype. The price of the underlying commodity is only the weather. The calibration body is realized spread, feedstock cost, inventory timing, OPM, EPS revision, and FCF.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C17 current rows | 29 |
| C17 current symbols | 15 |
| C17 good/bad Stage2 | 8 / 6 |
| C17 4B/4C | 3 / 3 |
| C17 URL pending/proxy | 26 / 21 |
| top covered symbols | 009830, 011170, 010060, 298000, 001340, 002380 |

Selected symbols avoid the C17 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 011780 | 금호석유화학 | new C17 symbol versus top-covered C17 list |
| 014830 | 유니드 | new C17 symbol versus top-covered C17 list |
| 093370 | 후성 | new C17 symbol versus top-covered C17 list |

Hard duplicate key checked:

```text
canonical_archetype_id + symbol + trigger_type + entry_date
```

No selected row is a known hard duplicate from the available No-Repeat summary.

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

| case | entry row exists | >=180 forward trading days | 180D corporate-action window | calibration usable |
|---|---:|---:|---|---:|
| 011780 / 2024-01-29 | true | true | clean_180D_window | true |
| 014830 / 2024-01-25 | true | true | clean_180D_window | true |
| 093370 / 2024-02-15 | true | true | clean_180D_window | true |

Corporate-action notes:

- 금호석유화학 has a corporate-action candidate only in 2001; selected 2024 window is clean.
- 유니드 has corporate-action candidates in 2015 and 2022; selected 2024 window is clean.
- 후성 has zero corporate-action candidates.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| SYNTHETIC_RUBBER_BD_SPREAD_MARGIN_RERATING_4B_WATCH | C17 | rubber/feedstock spread recovery can support Stage2A, but realized margin/FCF must follow |
| CAUSTIC_POTASH_SPREAD_MARGIN_RERATING_4B_WATCH | C17 | caustic/potash spread rerating can work, but post-peak drawdown requires 4B audit |
| FLUOROCHEMICAL_REFRIGERANT_ELECTROLYTE_SPREAD_BRIDGE_ABSENT | C17 | spread narrative without realized margin bridge is a false-positive route |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C17_KUMHOPETRO_011780_2024_01_29_SYNTHETIC_RUBBER_SPREAD_RERATING | 011780 | 금호석유화학 | 4B_overlay_success | positive | synthetic-rubber spread route produced 30%+ MFE, then peak drawdown |
| C17_UNID_014830_2024_01_25_CAUSTIC_POTASH_SPREAD_RERATING | 014830 | 유니드 | high_mfe_success | positive | caustic/potash spread route produced ~58% MFE, then spread-cycle drawdown |
| C17_FOOSUNG_093370_2024_02_15_FLUOROCHEMICAL_SPREAD_FALSE_POSITIVE | 093370 | 후성 | failed_rerating | counterexample | spread recovery narrative had only 2% MFE and high MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 1 |
| 4B_case_count | 2 |
| 4C_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |

Minimum conditions pass:

```text
positive_case_count >= 1
counterexample_count >= 1
calibration_usable_case_count >= 3
new_independent_case_ratio = 1.00
```

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 011780 | source_proxy_only | synthetic-rubber/feedstock spread route; realized margin bridge partial | required before promotion |
| 014830 | source_proxy_only | caustic/potash spread route; realized price/FCF bridge partial | required before promotion |
| 093370 | source_proxy_only | fluorochemical/refrigerant/electrolyte spread narrative but realized bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 011780 | atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv | atlas/symbol_profiles/011/011780.json |
| 014830 | atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv | atlas/symbol_profiles/014/014830.json |
| 093370 | atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv | atlas/symbol_profiles/093/093370.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD | Stage2-Actionable | 2024-01-29 | 2024-01-29 | 125400 | synthetic-rubber/feedstock spread recovery |
| UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD | Stage2-Actionable | 2024-01-25 | 2024-01-25 | 74900 | caustic/potash spread and chemical margin rebound |
| FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD | Stage2 | 2024-02-15 | 2024-02-15 | 9050 | fluorochemical spread narrative without realized margin bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 011780 | 2024-01-29 | 125400 | 30.70 | -8.13 | 30.70 | -8.13 | 33.17 | -8.13 | 2024-07-15 | 167000 | -27.72 |
| 014830 | 2024-01-25 | 74900 | 12.15 | -8.94 | 58.48 | -8.94 | 58.48 | -8.94 | 2024-06-11 | 118700 | -41.70 |
| 093370 | 2024-02-15 | 9050 | 2.10 | -14.14 | 2.10 | -23.76 | 2.10 | -26.85 | 2024-02-16 | 9240 | -28.35 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 011780 | Stage2A/Yellow possible; 4B after spread rerating | useful MFE then cycle drawdown | current_profile_4B_too_late |
| 014830 | Stage2A/Yellow possible; 4B after high MFE | high MFE then large post-peak drawdown | current_profile_4B_too_late |
| 093370 | Stage2 risk if spread narrative is over-credited | low MFE and high MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C17 interpretation:

- Stage2A can work when commodity spread route and relative strength align.
- Yellow/Green require realized spread, margin bridge, revision, and FCF conversion.
- Chemical beta without realized margin conversion should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 011780 | 1.00 | 1.00 | spread cycle / valuation | good 4B audit after synthetic-rubber spread rerating |
| 014830 | 1.00 | 1.00 | spread cycle / valuation | good 4B audit after caustic/potash spread rerating |
| 093370 | 1.00 | 1.00 | weak follow-through / spread bridge absent | not Stage3 without realized margin bridge |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 011780 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 014830 | thesis_break_watch_only | not hard 4C, but spread/FCF audit needed |
| 093370 | hard_4c_late | realized spread/margin bridge absence should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L4_MATERIALS_SPREAD_RESOURCE
confidence = low_to_medium
```

Candidate:

> In L4 chemical commodity names, feedstock or product-price spread narratives can open Stage2A, but Stage3-Yellow/Green should require realized spread, OPM, EPS revision, and FCF conversion. Without that bridge, commodity beta should be capped at Stage1/Stage2-watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C17_CHEMICAL_COMMODITY_MARGIN_SPREAD
confidence = low_to_medium
```

Candidate C17 rule:

```text
C17_realized_margin_bridge_required =
  chemical_or_commodity_spread_narrative
  AND (realized_spread OR opm_bridge OR confirmed_revision OR fcf_conversion)

if spread_narrative and realized_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 30 and drawdown_after_peak < -25:
    add C17_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_90D < -20:
    classify_as C17_spread_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 30.43 | -13.61 | 31.25 | -14.64 | 1 | useful but C17 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 30.43 | -13.61 | 31.25 | -14.64 | 1 | over-credits commodity spread beta |
| P1 sector_specific_candidate_profile | L4 | 2 promoted + 1 guard | 44.59 | -8.54 | 45.83 | -8.54 | 0 | better after realized-margin bridge gate |
| P2 canonical_archetype_candidate_profile | C17 | 2 promoted + 1 guard | 44.59 | -8.54 | 45.83 | -8.54 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C17 guard | 2 promoted + 1 guard | 44.59 | -8.54 | 45.83 | -8.54 | 0 | adds spread false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 011780 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 014830 | Stage2A aligned; 4B/FCF audit late | current_profile_4B_too_late |
| 093370 | Stage2 false positive if spread bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L4_MATERIALS_SPREAD_RESOURCE | C17_CHEMICAL_COMMODITY_MARGIN_SPREAD | mixed C17 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 3 | true | true | 29 -> projected 32 rows; reaches minimum stability threshold |

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
  - current_profile_4B_too_late
  - current_profile_false_positive
new_axis_proposed: C17_realized_margin_bridge_required|C17_peak_proximity_4B_audit|C17_spread_false_positive_guardrail
existing_axis_strengthened:
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
- Uses clean 180D windows.
- Uses C17 Priority 0 coverage gap.
- Uses three symbols not in the C17 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C17_realized_margin_bridge_required,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"093370 shows spread narrative can fail without realized margin bridge while 011780/014830 worked only as Stage2A with 4B audit","blocks 093370 false positive while preserving 011780/014830 Stage2A","KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD|UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD|FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C17_peak_proximity_4B_audit,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"011780/014830 spread reratings still needed 4B audit after cycle peak and drawdown","adds 4B audit after large C17 MFE when realized margin/FCF bridge remains partial","KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD|UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD",2,2,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C17_spread_false_positive_guardrail,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C17_CHEMICAL_COMMODITY_MARGIN_SPREAD,0,1,+1,"093370 had low MFE and high MAE despite chemical spread recovery narrative","requires realized spread/OPM/FCF bridge before Stage2/Yellow promotion","FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C17_KUMHOPETRO_011780_2024_01_29_SYNTHETIC_RUBBER_SPREAD_RERATING","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_BD_SPREAD_MARGIN_RERATING_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"synthetic-rubber/chemical spread route captured 30%+ MFE, but later peak-to-trough drawdown required 4B margin-spread audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C17 symbol versus top-covered list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C17_UNID_014830_2024_01_25_CAUSTIC_POTASH_SPREAD_RERATING","symbol":"014830","company_name":"유니드","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CAUSTIC_POTASH_SPREAD_MARGIN_RERATING_4B_WATCH","case_type":"high_mfe_success","positive_or_counterexample":"positive","best_trigger":"UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"caustic/potash margin-spread route captured ~58% MFE, but post-peak drawdown shows Stage3 requires realized spread/FCF bridge","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C17 symbol; source_proxy_only evidence"}
{"row_type":"case","case_id":"C17_FOOSUNG_093370_2024_02_15_FLUOROCHEMICAL_SPREAD_FALSE_POSITIVE","symbol":"093370","company_name":"후성","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"FLUOROCHEMICAL_REFRIGERANT_ELECTROLYTE_SPREAD_BRIDGE_ABSENT","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"fluorochemical/refrigerant/electrolyte spread narrative produced only ~2% MFE before high MAE because realized spread and margin bridge did not appear","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C17 symbol; counterexample for chemical spread beta without realized margin conversion"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD","case_id":"C17_KUMHOPETRO_011780_2024_01_29_SYNTHETIC_RUBBER_SPREAD_RERATING","symbol":"011780","company_name":"금호석유화학","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"SYNTHETIC_RUBBER_BD_SPREAD_MARGIN_RERATING_4B_WATCH","sector":"materials / chemical commodity spread","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-29","entry_date":"2024-01-29","entry_price":125400.0,"evidence_available_at_that_date":"source_proxy_only: synthetic rubber / butadiene spread recovery, chemical-cycle margin route, and relative-strength rerating visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["synthetic_rubber_spread_route","bd_feedstock_spread_route","chemical_cycle_recovery","relative_strength"],"stage3_evidence_fields":["realized_spread_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","spread_cycle_peak_watch","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv","profile_path":"atlas/symbol_profiles/011/011780.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":30.7,"MFE_90D_pct":30.7,"MFE_180D_pct":33.17,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.13,"MAE_90D_pct":-8.13,"MAE_180D_pct":-8.13,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-15","peak_price":167000.0,"drawdown_after_peak_pct":-27.72,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_audit_after_synthetic_rubber_spread_rerating","four_b_evidence_type":["valuation_rerating","spread_cycle_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_mfe_with_4b_drawdown","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_011780_2024_01_29_125400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD","case_id":"C17_UNID_014830_2024_01_25_CAUSTIC_POTASH_SPREAD_RERATING","symbol":"014830","company_name":"유니드","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"CAUSTIC_POTASH_SPREAD_MARGIN_RERATING_4B_WATCH","sector":"materials / chemical commodity spread","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-25","entry_date":"2024-01-25","entry_price":74900.0,"evidence_available_at_that_date":"source_proxy_only: caustic/potash spread recovery, chemical margin rebound, and export-price route visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["caustic_potash_spread_route","chemical_margin_rebound","relative_strength"],"stage3_evidence_fields":["realized_price_bridge_partial","margin_bridge_pending","fcf_conversion_pending"],"stage4b_evidence_fields":["valuation_rerating","spread_peak_watch","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv","profile_path":"atlas/symbol_profiles/014/014830.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":12.15,"MFE_90D_pct":58.48,"MFE_180D_pct":58.48,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.94,"MAE_90D_pct":-8.94,"MAE_180D_pct":-8.94,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-06-11","peak_price":118700.0,"drawdown_after_peak_pct":-41.7,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_4B_audit_after_caustic_potash_spread_rerating","four_b_evidence_type":["valuation_rerating","spread_peak_watch"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_014830_2024_01_25_74900","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD","case_id":"C17_FOOSUNG_093370_2024_02_15_FLUOROCHEMICAL_SPREAD_FALSE_POSITIVE","symbol":"093370","company_name":"후성","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","fine_archetype_id":"FLUOROCHEMICAL_REFRIGERANT_ELECTROLYTE_SPREAD_BRIDGE_ABSENT","sector":"materials / chemical commodity spread","primary_archetype":"chemical_commodity_margin_spread","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-02-15","entry_date":"2024-02-15","entry_price":9050.0,"evidence_available_at_that_date":"source_proxy_only: fluorochemical/refrigerant/electrolyte spread recovery narrative and commodity beta visible, but realized spread, margin, and cash bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["fluorochemical_spread_narrative","commodity_beta","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","spread_bridge_absent"],"stage4c_evidence_fields":["realized_spread_absent","margin_bridge_absent","inventory_or_price_pressure"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv","profile_path":"atlas/symbol_profiles/093/093370.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.1,"MFE_90D_pct":2.1,"MFE_180D_pct":2.1,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-14.14,"MAE_90D_pct":-23.76,"MAE_180D_pct":-26.85,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-02-16","peak_price":9240.0,"drawdown_after_peak_pct":-28.35,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"spread_recovery_narrative_not_stage3_without_realized_margin_bridge","four_b_evidence_type":["weak_follow_through","spread_bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_spread_bridge_absent","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C17_093370_2024_02_15_9050","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_KUMHOPETRO_011780_2024_01_29_SYNTHETIC_RUBBER_SPREAD_RERATING","trigger_id":"KUMHOPETRO_011780_2024_01_29_STAGE2A_SYNTHETIC_RUBBER_SPREAD","symbol":"011780","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":6,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":73,"stage_label_before":"Stage2-Actionable / Yellow-watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":4,"relative_strength_score":8,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67,"stage_label_after":"Stage2-Actionable with spread/4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Chemical spread rerating worked, but C17 Yellow/Green needs realized spread, margin, and FCF proof before ignoring peak proximity.","MFE_90D_pct":30.7,"MAE_90D_pct":-8.13,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_UNID_014830_2024_01_25_CAUSTIC_POTASH_SPREAD_RERATING","trigger_id":"UNID_014830_2024_01_25_STAGE2A_CAUSTIC_POTASH_SPREAD","symbol":"014830","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":9,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable with realized-spread/FCF audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"High MFE validates the spread route, but post-peak drawdown says valuation must decay unless realized margin/FCF bridge is confirmed.","MFE_90D_pct":58.48,"MAE_90D_pct":-8.94,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C17_FOOSUNG_093370_2024_02_15_FLUOROCHEMICAL_SPREAD_FALSE_POSITIVE","trigger_id":"FOOSUNG_093370_2024_02_15_STAGE2_FALSE_POSITIVE_FLUOROCHEMICAL_SPREAD","symbol":"093370","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":1,"relative_strength_score":5,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":61,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":48,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Chemical commodity beta without realized spread/margin bridge produced low MFE and high MAE; C17 should not promote this to Stage2.","MFE_90D_pct":2.1,"MAE_90D_pct":-23.76,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"88","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C17_CHEMICAL_COMMODITY_MARGIN_SPREAD","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_loop = 88
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C23_BIO_REGULATORY_APPROVAL_COMMERCIALIZATION, C02_POWER_GRID_DATACENTER_CAPEX, C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C11_BATTERY_ORDERBOOK_RERATING
```

If this loop is accepted, C17 moves from 29 to a projected 32 rows and reaches the minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C17 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/011/011780/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/014/014830/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/093/093370/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/011/011780.json
  - atlas/symbol_profiles/014/014830.json
  - atlas/symbol_profiles/093/093370.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
