# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R5_loop_82_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round: R5
selected_loop: 82
selection_basis: docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_SELLTHROUGH_MARGIN_REORDER_4B_WATCH
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

This loop adds 3 independent cases, 2 C19 brand/retail margin success paths, and 1 inventory-margin bridge counterexample for R5/L5/C19.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C19:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R5 -> L5_CONSUMER_BRAND_DISTRIBUTION
C19 -> C19_BRAND_RETAIL_INVENTORY_MARGIN
```

C19 is the consumer/brand version of a warehouse audit. A brand can report growth, but the signal is not complete until sell-through, inventory, receivables, OPM, and channel quality point in the same direction.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C19 current rows | 24 |
| C19 current symbols | 12 |
| C19 good/bad Stage2 | 5 / 4 |
| C19 4B/4C | 3 / 3 |
| C19 URL pending/proxy | 21 / 15 |
| top covered symbols | 008770, 023530, 031430, 069960, 383220, 020000 |

Selected symbols avoid the C19 top-covered symbols:

| symbol | company | status |
|---|---|---|
| 036620 | 감성코퍼레이션 | new C19 symbol versus top-covered C19 list |
| 093050 | LF | new C19 symbol versus top-covered C19 list |
| 298540 | 더네이쳐홀딩스 | new C19 symbol versus top-covered C19 list |

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
| 036620 / 2024-02-21 | true | true | clean_180D_window | true |
| 093050 / 2024-03-07 | true | true | clean_180D_window | true |
| 298540 / 2024-04-01 | true | true | clean_180D_window | true |

Corporate-action notes:

- 감성코퍼레이션 has corporate-action candidates only in 2000, 2017, and 2018; selected 2024 window is clean.
- LF has zero corporate-action candidates.
- 더네이쳐홀딩스 has corporate-action candidates only in 2021; selected 2024 window is clean.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| APPAREL_BRAND_SELLTHROUGH_MARGIN_REORDER_4B_WATCH | C19 | brand sell-through/margin/reorder route; 4B audit after rerating |
| APPAREL_INVENTORY_MARGIN_CASH_RETURN_STABLE_RERATING | C19 | inventory discipline plus stable margin/low MAE |
| OUTDOOR_BRAND_INVENTORY_MARGIN_BRIDGE_FAIL_FALSE_POSITIVE | C19 | inventory relief narrative without sell-through/OPM bridge |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C19_GAMSUNG_036620_2024_02_21_BRAND_SELLTHROUGH_MARGIN_RERATING | 036620 | 감성코퍼레이션 | 4B_overlay_success | positive | sell-through/margin route produced 65% MFE but required 4B audit |
| C19_LF_093050_2024_03_07_APPAREL_INVENTORY_MARGIN_STABLE_RERATING | 093050 | LF | structural_success | positive | moderate MFE with shallow MAE; useful low-volatility Stage2A case |
| C19_NATURE_298540_2024_04_01_OUTDOOR_BRAND_INVENTORY_MARGIN_FAIL | 298540 | 더네이쳐홀딩스 | failed_rerating | counterexample | inventory recovery narrative had almost no MFE and deep 180D drawdown |

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
| 036620 | source_proxy_only | brand sell-through / margin route; inventory/OPM bridge partial | required before promotion |
| 093050 | source_proxy_only | inventory normalization / margin stability route | required before promotion |
| 298540 | source_proxy_only | brand recovery narrative but sell-through/OPM/receivables bridge absent | required; useful as counterexample |

This loop does not allow price-only evidence to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 036620 | atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv | atlas/symbol_profiles/036/036620.json |
| 093050 | atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv | atlas/symbol_profiles/093/093050.json |
| 298540 | atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv | atlas/symbol_profiles/298/298540.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN | Stage2-Actionable | 2024-02-21 | 2024-02-21 | 2840 | brand sell-through / margin recovery route |
| LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE | Stage2-Actionable | 2024-03-07 | 2024-03-07 | 13640 | apparel inventory normalization / stable margin route |
| NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL | Stage2 | 2024-04-01 | 2024-04-01 | 15780 | outdoor brand recovery without inventory/sell-through bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 036620 | 2024-02-21 | 2840 | 34.68 | -9.51 | 65.14 | -9.51 | 65.14 | -9.51 | 2024-05-24 | 4690 | -26.12 |
| 093050 | 2024-03-07 | 13640 | 14.52 | -3.81 | 22.51 | -3.81 | 22.51 | -4.03 | 2024-05-17 | 16710 | -21.66 |
| 298540 | 2024-04-01 | 15780 | 0.25 | -17.93 | 1.96 | -27.69 | 1.96 | -45.50 | 2024-05-31 | 16090 | -46.55 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 036620 | Stage2A/Yellow possible; 4B after rerating | high MFE then drawdown | current_profile_4B_too_late |
| 093050 | Stage2A acceptable; Green waits for stronger evidence | moderate MFE, shallow MAE | current_profile_correct |
| 298540 | Stage2 risk if brand recovery is over-credited | low MFE and severe 180D MAE | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C19 interpretation:

- Stage2A can work when sell-through, inventory normalization, and OPM route are visible.
- Yellow/Green require verified OPM, inventory quality, receivables, and channel sell-through.
- Brand recovery narratives without those bridges should remain Stage1/Stage2-watch.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 036620 | 1.00 | 1.00 | valuation / positioning | good 4B audit after brand rerating |
| 093050 | 1.00 | 1.00 | moderate valuation repricing | Stage2A ok; Green blocked until OPM/sell-through proof |
| 298540 | 1.00 | 1.00 | weak follow-through / inventory overhang | recovery narrative was not enough for Stage2/Yellow |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 036620 | thesis_break_watch_only | not hard 4C, but 4B cap needed |
| 093050 | thesis_break_watch_only | not hard 4C; low MAE supports watch state |
| 298540 | hard_4c_late | missing inventory/sell-through/OPM bridge should have capped Stage2 earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L5_CONSUMER_BRAND_DISTRIBUTION
confidence = low_to_medium
```

Candidate:

> In L5 consumer brand/retail names, sell-through and OPM evidence can support Stage2A, but Stage3-Yellow/Green should require inventory quality, receivables discipline, and channel sell-through. If a brand recovery story lacks those bridges, cap it at Stage1/Stage2-watch even if valuation appears cheap.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
confidence = low_to_medium
```

Candidate C19 rule:

```text
C19_inventory_margin_bridge_required =
  brand_or_retail_recovery
  AND (sellthrough_evidence OR opm_bridge OR inventory_normalization OR receivables_quality)

if brand_recovery_narrative and inventory_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if MFE_90D > 40 and drawdown_after_peak < -20:
    add C19_peak_proximity_4B_audit = true

if MFE_90D < 10 and MAE_180D < -30:
    classify_as C19_inventory_margin_false_positive_guardrail
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 29.87 | -13.67 | 29.87 | -19.68 | 1 | useful but C19 bridge too loose |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 29.87 | -13.67 | 29.87 | -19.68 | 1 | over-credits brand recovery narrative |
| P1 sector_specific_candidate_profile | L5 | 2 promoted + 1 guard | 43.83 | -6.66 | 43.83 | -6.77 | 0 | better after sell-through/OPM bridge gate |
| P2 canonical_archetype_candidate_profile | C19 | 2 promoted + 1 guard | 43.83 | -6.66 | 43.83 | -6.77 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C19 guard | 2 promoted + 1 guard | 43.83 | -6.66 | 43.83 | -6.77 | 0 | adds inventory-margin false-positive guard |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 036620 | Stage2A aligned; 4B audit late | current_profile_4B_too_late |
| 093050 | Stage2A aligned; Green block appropriate | current_profile_correct |
| 298540 | Stage2 false positive if inventory bridge not enforced | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | mixed C19 fine ids | 2 | 1 | 2 | 1 | 3 | 0 | 3 | 3 | 2 | true | true | 24 -> projected 27 rows; still need 3 to reach 30 |

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
new_axis_proposed: C19_inventory_margin_bridge_required|C19_peak_proximity_4B_audit|C19_inventory_margin_false_positive_guardrail
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
- Uses C19 Priority 0 coverage gap.
- Uses three symbols not in the C19 top-covered symbol list.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"298540 shows brand recovery can fail without sell-through/OPM/inventory bridge","blocks 298540 false positive while preserving 036620/093050 Stage2A","GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN|LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE|NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL",3,3,1,low_to_medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C19_peak_proximity_4B_audit,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"036620 high-MFE brand rerating still needed 4B audit after valuation extension","adds 4B audit after large C19 MFE without converting price-only peaks into full 4B","GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN",1,1,0,low_to_medium,canonical_shadow_only,"4B overlay/risk calibration only"
shadow_weight,C19_inventory_margin_false_positive_guardrail,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"298540 had low MFE and high 180D MAE despite brand recovery narrative","requires sell-through/OPM/receivables bridge before Stage2/Yellow promotion","NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL",1,1,1,low_to_medium,canonical_shadow_only,"false-positive guardrail"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C19_GAMSUNG_036620_2024_02_21_BRAND_SELLTHROUGH_MARGIN_RERATING","symbol":"036620","company_name":"감성코퍼레이션","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_SELLTHROUGH_MARGIN_REORDER_4B_WATCH","case_type":"4B_overlay_success","positive_or_counterexample":"positive","best_trigger":"GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"brand sell-through / margin route captured 65% MFE, but later drawdown requires inventory and 4B audit","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"new C19 symbol versus top-covered C19 list; source_proxy_only evidence requires URL repair"}
{"row_type":"case","case_id":"C19_LF_093050_2024_03_07_APPAREL_INVENTORY_MARGIN_STABLE_RERATING","symbol":"093050","company_name":"LF","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_INVENTORY_MARGIN_CASH_RETURN_STABLE_RERATING","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"moderate MFE with shallow MAE supports C19 Stage2A when inventory/margin risk is controlled","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"new C19 symbol; useful moderate-success case where Green should still require OPM/sell-through proof"}
{"row_type":"case","case_id":"C19_NATURE_298540_2024_04_01_OUTDOOR_BRAND_INVENTORY_MARGIN_FAIL","symbol":"298540","company_name":"더네이쳐홀딩스","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"OUTDOOR_BRAND_INVENTORY_MARGIN_BRIDGE_FAIL_FALSE_POSITIVE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"inventory/margin recovery narrative had only 2% MFE before -45% 180D MAE","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"new C19 symbol; counterexample for brand recovery without sell-through / OPM / receivables bridge"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN","case_id":"C19_GAMSUNG_036620_2024_02_21_BRAND_SELLTHROUGH_MARGIN_RERATING","symbol":"036620","company_name":"감성코퍼레이션","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_BRAND_SELLTHROUGH_MARGIN_REORDER_4B_WATCH","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-21","entry_date":"2024-02-21","entry_price":2840.0,"evidence_available_at_that_date":"source_proxy_only: apparel/outdoor brand sell-through and margin recovery route visible; reorder/inventory/OPM bridge partial; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["brand_sellthrough_route","margin_recovery_route","relative_strength","channel_reorder_route"],"stage3_evidence_fields":["opm_bridge_partial","inventory_quality_pending","receivables_check_pending"],"stage4b_evidence_fields":["valuation_rerating","positioning_overheat","peak_proximity"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv","profile_path":"atlas/symbol_profiles/036/036620.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":34.68,"MFE_90D_pct":65.14,"MFE_180D_pct":65.14,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-9.51,"MAE_90D_pct":-9.51,"MAE_180D_pct":-9.51,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-24","peak_price":4690.0,"drawdown_after_peak_pct":-26.12,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"good_full_window_4B_audit_after_brand_sellthrough_margin_rerating","four_b_evidence_type":["valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_high_mfe_4b_watch","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_036620_2024_02_21_2840","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE","case_id":"C19_LF_093050_2024_03_07_APPAREL_INVENTORY_MARGIN_STABLE_RERATING","symbol":"093050","company_name":"LF","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"APPAREL_INVENTORY_MARGIN_CASH_RETURN_STABLE_RERATING","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-07","entry_date":"2024-03-07","entry_price":13640.0,"evidence_available_at_that_date":"source_proxy_only: apparel inventory normalization / margin stability route with limited drawdown; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["inventory_normalization_route","margin_stability_route","cash_return_support","brand_discount_floor"],"stage3_evidence_fields":["opm_bridge_partial","sellthrough_pending","receivables_check_pending"],"stage4b_evidence_fields":["valuation_repricing_moderate"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv","profile_path":"atlas/symbol_profiles/093/093050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.52,"MFE_90D_pct":22.51,"MFE_180D_pct":22.51,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-3.81,"MAE_90D_pct":-3.81,"MAE_180D_pct":-4.03,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-17","peak_price":16710.0,"drawdown_after_peak_pct":-21.66,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"moderate_rerating_requires_sellthrough_opm_confirmation_before_green","four_b_evidence_type":["moderate_valuation_repricing"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"positive_moderate_mfe_low_mae","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_093050_2024_03_07_13640","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL","case_id":"C19_NATURE_298540_2024_04_01_OUTDOOR_BRAND_INVENTORY_MARGIN_FAIL","symbol":"298540","company_name":"더네이쳐홀딩스","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"OUTDOOR_BRAND_INVENTORY_MARGIN_BRIDGE_FAIL_FALSE_POSITIVE","sector":"consumer / brand / retail distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-04-01","entry_date":"2024-04-01","entry_price":15780.0,"evidence_available_at_that_date":"source_proxy_only: outdoor brand recovery / inventory relief narrative, but sell-through, OPM, receivables, and channel quality bridge absent","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["brand_recovery_narrative","inventory_relief_theme"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["weak_follow_through","valuation_overhang"],"stage4c_evidence_fields":["inventory_bridge_absent","opm_bridge_absent","sellthrough_absent","receivables_quality_pending"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","profile_path":"atlas/symbol_profiles/298/298540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.25,"MFE_90D_pct":1.96,"MFE_180D_pct":1.96,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-17.93,"MAE_90D_pct":-27.69,"MAE_180D_pct":-45.5,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":16090.0,"drawdown_after_peak_pct":-46.55,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"brand_recovery_price_followthrough_failed_without_inventory_sellthrough_bridge","four_b_evidence_type":["weak_follow_through","inventory_overhang"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mfe_high_mae_inventory_margin_fail","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"C19_298540_2024_04_01_15780","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_GAMSUNG_036620_2024_02_21_BRAND_SELLTHROUGH_MARGIN_RERATING","trigger_id":"GAMSUNG_036620_2024_02_21_STAGE2A_BRAND_SELLTHROUGH_MARGIN","symbol":"036620","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow / 4B-watch risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":2,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":8,"customer_quality_score":6,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":71,"stage_label_after":"Stage2-Actionable with inventory/4B audit","changed_components":["valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Brand sell-through route worked, but C19 Yellow/Green requires verified OPM/inventory/receivables bridge.","MFE_90D_pct":65.14,"MAE_90D_pct":-9.51,"score_return_alignment_label":"positive_but_4b_audit_needed","current_profile_verdict":"current_profile_4B_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_LF_093050_2024_03_07_APPAREL_INVENTORY_MARGIN_STABLE_RERATING","trigger_id":"LF_093050_2024_03_07_STAGE2A_APPAREL_INVENTORY_MARGIN_STABLE","symbol":"093050","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":5,"revision_score":3,"relative_strength_score":5,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":66,"stage_label_after":"Stage2-Actionable, Green blocked until sell-through/OPM proof","changed_components":["execution_risk_score"],"component_delta_explanation":"Low MAE and moderate MFE support Stage2A, but this is not structural Green without sell-through and OPM bridge.","MFE_90D_pct":22.51,"MAE_90D_pct":-3.81,"score_return_alignment_label":"stage2_good_green_block_needed","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C19_NATURE_298540_2024_04_01_OUTDOOR_BRAND_INVENTORY_MARGIN_FAIL","trigger_id":"NATURE_298540_2024_04_01_STAGE2_FALSE_POSITIVE_INVENTORY_MARGIN_FAIL","symbol":"298540","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":63,"stage_label_before":"Stage2 false-positive risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":49,"stage_label_after":"Stage1/4C-watch, not Stage2","changed_components":["margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Inventory relief narrative without sell-through/OPM/receivables bridge produced low MFE and severe MAE.","MFE_90D_pct":1.96,"MAE_90D_pct":-27.69,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"82","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_4B_too_late","current_profile_false_positive"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R5
completed_loop = 82
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C12_BATTERY_CUSTOMER_CONTRACT_CALL_OFF_RISK, C13_BATTERY_JV_UTILIZATION_AMPC_IRA, C24_BIO_TRIAL_DATA_EVENT_RISK
```

If this loop is accepted, C19 moves from 24 to a projected 27 rows. It remains below 30-row minimum stability, so a later run can still add 3 more C19 rows, but the next run should re-read the latest No-Repeat Index before selecting another C19 case.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/036/036620/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/093/093050/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/036/036620.json
  - atlas/symbol_profiles/093/093050.json
  - atlas/symbol_profiles/298/298540.json
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
