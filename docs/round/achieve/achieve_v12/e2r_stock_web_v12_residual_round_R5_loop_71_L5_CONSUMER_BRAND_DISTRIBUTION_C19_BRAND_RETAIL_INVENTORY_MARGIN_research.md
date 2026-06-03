# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
research_session = post_calibrated_sector_archetype_residual_research
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_format = one_standalone_markdown_file
production_scoring_changed = false
shadow_weight_only = true
scheduled_round = R5
scheduled_loop = 71
completed_round = R5
completed_loop = 71
next_round = R6
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id = BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE
loop_objective = coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_specific_exception
```

This loop adds 3 new independent cases, 2 counterexamples, and 3 residual errors for R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN.

## 1. Current Calibrated Profile Assumption

```text
before_profile_id = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
production_scoring_changed = false
```

Applied global assumptions treated as already present:

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

This research does not re-propose those global axes. It tests whether C19 should require a brand-retail specific bridge: inventory quality, sell-through, and margin conversion before Stage2-Actionable or Green-like treatment.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R5 |
| scheduled_loop | 71 |
| large_sector_id | L5_CONSUMER_BRAND_DISTRIBUTION |
| canonical_archetype_id | C19_BRAND_RETAIL_INVENTORY_MARGIN |
| fine_archetype_id | BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE |
| round_sector_consistency | pass |

R5 is the consumer / distribution / brand round. C19 was selected over C20 because C20 is already heavily covered, while C19 still benefits from additional counterexamples and 4B/4C timing rows.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat rule applied:

```text
Do not reuse the same canonical_archetype_id + symbol + trigger_type + entry_date combination.
Prefer new symbols, new trigger families, counterexamples, 4B/4C paths, or data-quality repairs.
```

Current corpus snapshot used for selection:

```text
C19_BRAND_RETAIL_INVENTORY_MARGIN prior coverage: 39 rows / 8 symbols
prior top covered symbols include UNKNOWN_SYMBOL, 036620, 298540, 383220, 337930
selected symbols in this loop: 111770, 093050, 020000
all selected representative symbols are outside the visible top-covered C19 set
```

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

Stock-Web manifest context:

```text
source_name = FinanceData/marcap
price_adjustment_status = raw_unadjusted_marcap
min_date = 1995-05-02
max_date = 2026-02-20
tradable_row_count = 14354401
raw_row_count = 15214118
symbol_count = 5414
markets = KONEX | KOSDAQ | KOSDAQ GLOBAL | KOSPI
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | 180D window | corporate action window | calibration_usable |
|---|---|---:|---:|---|---|---|
| R5L71-C19-001 | 111770 | 2023-01-02 | 44550 | available | clean_180D_window | true |
| R5L71-C19-002 | 093050 | 2023-02-14 | 18150 | available | clean_180D_window | true |
| R5L71-C19-003 | 020000 | 2023-01-02 | 26000 | available | clean_180D_window | true |
| R5L71-C19-004 | 111770 | 2023-08-16 | 61400 | available | clean_180D_window | true |

The fourth row is a 4B overlay audit for a reused symbol but new trigger family. It is not counted as a new independent representative Stage2/Stage3 case.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep sub-archetype | included evidence logic | excluded evidence logic |
|---|---|---|---|
| C19_BRAND_RETAIL_INVENTORY_MARGIN | BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE | sell-through, inventory quality, margin bridge, cash conversion, channel discipline | generic brand heat, low valuation only, short rebound without inventory/margin proof |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_OEM_MARGIN_AND_ORDER_VISIBILITY | margin durability and order visibility in apparel/OEM channel | price-only move or single season restocking |
| C19_BRAND_RETAIL_INVENTORY_MARGIN | DOMESTIC_BRAND_VALUE_TRAP_GUARD | low PBR/PER and brand name without margin proof | Stage2-Actionable upgrade without sell-through |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive_or_counterexample | best_trigger | new_independent |
|---|---|---|---|---|---|---|
| R5L71-C19-001 | 111770 | 영원무역 | structural_success | positive | Stage2-Actionable | true |
| R5L71-C19-002 | 093050 | LF | failed_rerating | counterexample | Stage2 | true |
| R5L71-C19-003 | 020000 | 한섬 | false_positive_green | counterexample | Stage2 | true |
| R5L71-C19-004 | 111770 | 영원무역 | 4B_overlay_success | counterexample_guard | Stage4B | false |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_case_count = 1
4C_case_count = 0
calibration_usable_case_count = 4
representative_stage2_stage3_case_count = 3
```

The positive count is intentionally small. This loop is primarily a counterexample / residual-error addition for C19. Because positive evidence is not yet 2+, any proposed axis remains shadow-only and should not immediately change production scoring.

## 9. Evidence Source Map

| case_id | evidence_available_at_that_date | evidence_source | source_proxy_only | evidence interpretation |
|---|---|---|---|---|
| R5L71-C19-001 | 2023 apparel/OEM margin and order visibility proxy | public report proxy / financial-result proxy | true | strong price alignment when margin/order visibility is visible |
| R5L71-C19-002 | 2023 brand-retail value rebound proxy | public report proxy / price + financial-result proxy | true | low valuation / brand rebound alone did not create durable rerating |
| R5L71-C19-003 | 2023 domestic fashion rebound proxy | public report proxy / price + financial-result proxy | true | inventory/margin uncertainty led to drawdown despite initial bounce |
| R5L71-C19-004 | 2023 post-runup apparel slowdown / margin-risk proxy | public report proxy / price + revision-slowdown proxy | true | 4B overlay needs non-price slowdown evidence, not just local price peak |

## 10. Price Data Source Map

| symbol | profile_path | price_shard_path | entry_date | stock_web_basis |
|---|---|---|---|---|
| 111770 | atlas/symbol_profiles/111/111770.json | atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv | 2023-01-02 | tradable_raw / raw_unadjusted_marcap |
| 093050 | atlas/symbol_profiles/093/093050.json | atlas/ohlcv_tradable_by_symbol_year/093/093050/2023.csv | 2023-02-14 | tradable_raw / raw_unadjusted_marcap |
| 020000 | atlas/symbol_profiles/020/020000.json | atlas/ohlcv_tradable_by_symbol_year/020/020000/2023.csv | 2023-01-02 | tradable_raw / raw_unadjusted_marcap |
| 111770 | atlas/symbol_profiles/111/111770.json | atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv | 2023-08-16 | tradable_raw / raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | trigger_date | entry_date | entry_price | outcome |
|---|---|---|---|---|---:|---|
| R5L71-C19-001-S2A | R5L71-C19-001 | Stage2-Actionable | 2023-01-02 | 2023-01-02 | 44550 | high-MFE positive, later 4B risk |
| R5L71-C19-002-S2 | R5L71-C19-002 | Stage2 | 2023-02-14 | 2023-02-14 | 18150 | low-MFE / high-MAE false positive |
| R5L71-C19-003-S2 | R5L71-C19-003 | Stage2 | 2023-01-02 | 2023-01-02 | 26000 | low-MFE / high-MAE false positive |
| R5L71-C19-004-4B | R5L71-C19-004 | Stage4B | 2023-08-16 | 2023-08-16 | 61400 | 4B overlay useful; not a fresh positive entry |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|
| R5L71-C19-001-S2A | 2.24 | -6.62 | 8.08 | -6.62 | 52.41 | -6.62 | 2023-08-16 | 67900 | -30.85 |
| R5L71-C19-002-S2 | 0.55 | -7.99 | 1.71 | -9.37 | 1.71 | -25.62 | 2023-04-06 | 18460 | -26.87 |
| R5L71-C19-003-S2 | 8.08 | -4.42 | 8.08 | -7.69 | 8.08 | -31.15 | 2023-02-03 | 28100 | -36.30 |
| R5L71-C19-004-4B | 10.59 | -15.96 | 10.59 | -23.53 | 10.59 | -25.00 | 2023-08-16 | 67900 | -30.85 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | explanation |
|---|---|---|
| R5L71-C19-001 | current_profile_missed_structural | C19 positive needs inventory/sell-through/margin bridge; generic brand score would likely under-credit order/margin visibility until price already moved. |
| R5L71-C19-002 | current_profile_false_positive | low valuation and brand-retail rebound could look like Stage2, but actual MFE stayed near zero while MAE expanded. |
| R5L71-C19-003 | current_profile_false_positive | domestic fashion rebound without inventory-quality proof produced weak upside and large 180D drawdown. |
| R5L71-C19-004 | current_profile_4B_too_late | post-runup margin/inventory slowdown should be treated as 4B overlay before the drawdown, not as a new Stage2/Green entry. |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is promoted in this loop. Green strictness is kept. The main finding is that C19 Stage2-Actionable should not rely on low valuation or brand heat alone.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
existing_axis_kept = stage3_green_total_min / stage3_green_revision_min
```

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R5L71-C19-004-4B | 0.78 | 0.78 | revision_slowdown | good_full_window_4B_timing |

The 4B row is not price-only. It is modeled as a margin/inventory/revision-slowdown overlay. Therefore it supports the existing global rule that full 4B requires non-price evidence.

## 16. 4C Protection Audit

No hard 4C row is promoted. The false-positive rows remain Stage2/4B guard calibration rather than hard thesis-break routing.

```text
four_c_protection_label = thesis_break_watch_only
hard_4c_routing = existing_axis_kept
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
axis = L5_brand_retail_inventory_margin_bridge_required
proposal_type = sector_shadow_only
```

Rule candidate:

```text
For L5 consumer brand/retail rows, Stage2-Actionable should require at least one non-price bridge among sell-through, inventory quality, margin bridge, or cash conversion. Low valuation, brand recognition, or price rebound alone should remain watch-only.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN
axis = C19_inventory_sellthrough_margin_bridge_required
proposal_type = archetype_shadow_only
```

C19-specific compression:

```text
C19 should reward inventory quality and margin conversion more than generic brand heat.
C19 should penalize Stage2 candidates where valuation looks low but inventory/sell-through proof is absent.
C19 4B should be allowed when post-runup evidence shows revision slowdown, margin compression, or inventory risk.
```

## 19. Before / After Backtest Comparison

| profile | eligible_trigger_count | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 5.96 | -7.89 | 20.73 | -21.13 | 0.67 | mixed; two value/rebound traps pass too easily |
| P0b e2r_2_0_baseline_reference | 3 | 5.96 | -7.89 | 20.73 | -21.13 | 0.67 | worse; insufficient non-price bridge discipline |
| P1 sector_specific_candidate_profile | 3 | 8.08 | -6.62 | 52.41 | -6.62 | 0.00 | better but too strict until more positives arrive |
| P2 canonical_archetype_candidate_profile | 3 | 8.08 | -6.62 | 52.41 | -6.62 | 0.00 | useful as C19 shadow guard; not production-ready |
| P3 counterexample_guard_profile | 4 | 7.37 | -13.87 | 18.70 | -22.85 | 0.00 | best for avoiding false positives and enabling 4B overlay |

## 20. Score-Return Alignment Matrix

| case_id | weighted_score_before | stage_label_before | weighted_score_after | stage_label_after | score_return_alignment |
|---|---:|---|---:|---|---|
| R5L71-C19-001 | 72 | Stage2 | 77 | Stage2-Actionable | improved; recognizes margin/order visibility |
| R5L71-C19-002 | 68 | Stage2 | 58 | Stage1/Watch | improved; blocks value-trap false Stage2 |
| R5L71-C19-003 | 66 | Stage2 | 55 | Stage1/Watch | improved; blocks rebound-without-inventory-proof |
| R5L71-C19-004 | 74 | Stage3-Yellow/4A watch | 4B-watch | Stage4B-watch | improved; recognizes non-price 4B overlay |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE | 1 | 2 | 1 | 0 | 3 | 1 | 4 | 3 | 3 | true | true | positive_count still thin; needs 1~2 additional non-overlapping positives |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids: R5L71-C19-004
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus | price_only_blowoff_blocks_positive_stage | full_4b_requires_non_price_evidence | stage3_green_total_min | stage3_green_revision_min
residual_error_types_found: current_profile_false_positive | current_profile_missed_structural | current_profile_4B_too_late
new_axis_proposed: C19_inventory_sellthrough_margin_bridge_required_shadow_only
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage for C19 value/rebound traps; full_4b_requires_non_price_evidence for C19 post-runup slowdown
existing_axis_weakened: null
existing_axis_kept: stage3_green_total_min | stage3_green_revision_min | hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: counterexample_added
do_not_propose_new_weight_delta: true
```

Reason for `do_not_propose_new_weight_delta=true`: this loop is useful for shadow ledger expansion, but evidence is source-proxy-heavy and contains only one positive structural success. It should strengthen the C19 guardrail ledger rather than immediately alter runtime production weights.

## 23. Validation Scope / Non-Validation Scope

Validation scope:

```text
- Stock-Web tradable raw OHLC rows
- entry_date / entry_price
- MFE/MAE 30D/90D/180D
- same_entry_group_id and dedupe flags
- R5/L5/C19 round-sector-canonical consistency
```

Non-validation scope:

```text
- no live candidate discovery
- no production scoring update
- no broker API or automated trading
- no global threshold relaxation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_sellthrough_margin_bridge_required,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,not_configured,require_inventory_or_margin_bridge,guardrail_only,"C19 false positives were value/brand rebound rows without inventory or margin proof","Blocks 2 false positives while preserving 1 positive and 1 non-price 4B overlay","R5L71-C19-001-S2A|R5L71-C19-002-S2|R5L71-C19-003-S2|R5L71-C19-004-4B",4,3,2,low,canonical_shadow_only,"not production; source proxy-heavy; keep in v12 ledger"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R5L71-C19-001","symbol":"111770","company_name":"영원무역","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"Stage2-Actionable","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive_alignment_after_margin_order_visibility","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"C19 positive requires margin/order visibility, not generic brand heat."}
{"row_type":"case","case_id":"R5L71-C19-002","symbol":"093050","company_name":"LF","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Low valuation / brand rebound without inventory or sell-through proof failed."}
{"row_type":"case","case_id":"R5L71-C19-003","symbol":"020000","company_name":"한섬","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"Stage2","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Domestic fashion rebound lacked inventory/margin proof."}
{"row_type":"case","case_id":"R5L71-C19-004","symbol":"111770","company_name":"영원무역","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","case_type":"4B_overlay_success","positive_or_counterexample":"counterexample","best_trigger":"Stage4B","calibration_usable":true,"is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing","independent_evidence_weight":0.25,"score_price_alignment":"4B_overlay_alignment","current_profile_verdict":"current_profile_4B_too_late","price_source":"Songdaiki/stock-web","notes":"Same symbol reused only for a distinct 4B timing family."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R5L71-C19-001-S2A","case_id":"R5L71-C19-001","symbol":"111770","company_name":"영원무역","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-01-02","entry_date":"2023-01-02","entry_price":44550,"evidence_available_at_that_date":"apparel_oem_margin_and_order_visibility_proxy","evidence_source":"public_report_proxy;financial_result_proxy","stage2_evidence_fields":["financial_visibility","margin_bridge","order_visibility"],"stage3_evidence_fields":["confirmed_revision_proxy","margin_bridge","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv","profile_path":"atlas/symbol_profiles/111/111770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":2.24,"MFE_90D_pct":8.08,"MFE_180D_pct":52.41,"MFE_1Y_pct":52.41,"MFE_2Y_pct":null,"MAE_30D_pct":-6.62,"MAE_90D_pct":-6.62,"MAE_180D_pct":-6.62,"MAE_1Y_pct":-6.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-16","peak_price":67900,"drawdown_after_peak_pct":-30.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mfe_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L71-C19-001-111770-20230102","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"R5L71-C19-002-S2","case_id":"R5L71-C19-002","symbol":"093050","company_name":"LF","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"counterexample_mining|stage2_actionable_bonus_stress_test","trigger_type":"Stage2","trigger_date":"2023-02-14","entry_date":"2023-02-14","entry_price":18150,"evidence_available_at_that_date":"brand_retail_low_valuation_rebound_proxy","evidence_source":"public_report_proxy;price_and_financial_result_proxy","stage2_evidence_fields":["valuation_repricing","relative_strength"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/093/093050/2023.csv","profile_path":"atlas/symbol_profiles/093/093050.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":0.55,"MFE_90D_pct":1.71,"MFE_180D_pct":1.71,"MFE_1Y_pct":1.71,"MFE_2Y_pct":null,"MAE_30D_pct":-7.99,"MAE_90D_pct":-9.37,"MAE_180D_pct":-25.62,"MAE_1Y_pct":-25.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-04-06","peak_price":18460,"drawdown_after_peak_pct":-26.87,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"failed_rerating_low_mfe_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L71-C19-002-093050-20230214","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"R5L71-C19-003-S2","case_id":"R5L71-C19-003","symbol":"020000","company_name":"한섬","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"counterexample_mining|green_strictness_stress_test","trigger_type":"Stage2","trigger_date":"2023-01-02","entry_date":"2023-01-02","entry_price":26000,"evidence_available_at_that_date":"domestic_fashion_rebound_without_inventory_proof_proxy","evidence_source":"public_report_proxy;price_and_financial_result_proxy","stage2_evidence_fields":["relative_strength","valuation_repricing"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["inventory_or_margin_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/020/020000/2023.csv","profile_path":"atlas/symbol_profiles/020/020000.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":8.08,"MFE_90D_pct":8.08,"MFE_180D_pct":8.08,"MFE_1Y_pct":8.08,"MFE_2Y_pct":null,"MAE_30D_pct":-4.42,"MAE_90D_pct":-7.69,"MAE_180D_pct":-31.15,"MAE_1Y_pct":-31.15,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-02-03","peak_price":28100,"drawdown_after_peak_pct":-36.30,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":null,"four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_candidate_high_mae","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L71-C19-003-020000-20230102","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":true}
{"row_type":"trigger","trigger_id":"R5L71-C19-004-4B","case_id":"R5L71-C19-004","symbol":"111770","company_name":"영원무역","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","sector":"consumer_brand_distribution","primary_archetype":"brand_retail_inventory_margin","loop_objective":"4B_non_price_requirement_stress_test","trigger_type":"Stage4B","trigger_date":"2023-08-16","entry_date":"2023-08-16","entry_price":61400,"evidence_available_at_that_date":"post_runup_margin_revision_slowdown_proxy","evidence_source":"public_report_proxy;revision_slowdown_proxy","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/111/111770/2023.csv","profile_path":"atlas/symbol_profiles/111/111770.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":10.59,"MFE_90D_pct":10.59,"MFE_180D_pct":10.59,"MFE_1Y_pct":10.59,"MFE_2Y_pct":null,"MAE_30D_pct":-15.96,"MAE_90D_pct":-23.53,"MAE_180D_pct":-25.00,"MAE_1Y_pct":-25.00,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2023-08-16","peak_price":67900,"drawdown_after_peak_pct":-30.85,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.78,"four_b_full_window_peak_proximity":0.78,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R5L71-C19-004-111770-20230816","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same_symbol_new_trigger_family_4B_timing","independent_evidence_weight":0.25,"do_not_count_as_new_case":false,"evidence_url_pending":false,"source_proxy_only":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L71-C19-001","trigger_id":"R5L71-C19-001-S2A","symbol":"111770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":35,"margin_bridge_score":70,"revision_score":62,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":20,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":72,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":40,"margin_bridge_score":82,"revision_score":70,"relative_strength_score":55,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":18,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":77,"stage_label_after":"Stage2-Actionable","changed_components":["margin_bridge_score","revision_score"],"component_delta_explanation":"C19 positive credit comes from margin/order visibility, not generic brand heat.","MFE_90D_pct":8.08,"MAE_90D_pct":-6.62,"score_return_alignment_label":"improved_positive_alignment","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L71-C19-002","trigger_id":"R5L71-C19-002-S2","symbol":"093050","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":50,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":75,"execution_risk_score":55,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":68,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":5,"revision_score":15,"relative_strength_score":35,"customer_quality_score":30,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":70,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":58,"stage_label_after":"Stage1/Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Low valuation without inventory/sell-through proof should not become C19 Stage2.","MFE_90D_pct":1.71,"MAE_90D_pct":-9.37,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L71-C19-003","trigger_id":"R5L71-C19-003-S2","symbol":"020000","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":10,"margin_bridge_score":20,"revision_score":25,"relative_strength_score":52,"customer_quality_score":40,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":50,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":66,"stage_label_before":"Stage2","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":5,"margin_bridge_score":8,"revision_score":18,"relative_strength_score":40,"customer_quality_score":35,"policy_or_regulatory_score":0,"valuation_repricing_score":50,"execution_risk_score":72,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":55,"stage_label_after":"Stage1/Watch","changed_components":["margin_bridge_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Inventory and domestic demand risk override generic valuation rebound.","MFE_90D_pct":8.08,"MAE_90D_pct":-7.69,"score_return_alignment_label":"false_positive_blocked","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R5L71-C19-004","trigger_id":"R5L71-C19-004-4B","symbol":"111770","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":25,"margin_bridge_score":35,"revision_score":40,"relative_strength_score":88,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":65,"execution_risk_score":65,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":74,"stage_label_before":"Stage3-Yellow/4A-watch","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":20,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":88,"customer_quality_score":45,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":82,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":64,"stage_label_after":"Stage4B-watch","changed_components":["revision_score","margin_bridge_score","execution_risk_score"],"component_delta_explanation":"Post-runup slowdown evidence changes the row from fresh positive to 4B overlay.","MFE_90D_pct":10.59,"MAE_90D_pct":-23.53,"score_return_alignment_label":"4B_overlay_alignment","current_profile_verdict":"current_profile_4B_too_late"}
```

### 25.5 shadow_weight row

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_sellthrough_margin_bridge_required,canonical_archetype,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,not_configured,require_inventory_or_margin_bridge,guardrail_only,"C19 false positives were value/brand rebound rows without inventory or margin proof","Blocks 2 false positives while preserving 1 positive and 1 non-price 4B overlay","R5L71-C19-001-S2A|R5L71-C19-002-S2|R5L71-C19-003-S2|R5L71-C19-004-4B",4,3,2,low,canonical_shadow_only,"not production; source proxy-heavy; keep in v12 ledger"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"71","large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"BRAND_RETAIL_INVENTORY_SELLTHROUGH_MARGIN_BRIDGE","new_independent_case_count":3,"reused_case_count":1,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","stage3_green_total_min","stage3_green_revision_min"],"residual_error_types_found":["current_profile_false_positive","current_profile_missed_structural","current_profile_4B_too_late"],"loop_contribution_label":"counterexample_added","do_not_propose_new_weight_delta":true,"diversity_score_summary":"same_archetype_new_symbol_bonus=+12; counterexample_gap_bonus=+8; residual_error_bonus=+15; same_archetype_new_trigger_family_bonus=+12; wrong_round_penalty=0; repeated_same_trigger_date_penalty=0; net=high"}
```

### 25.7 narrative_only row

```jsonl
{"row_type":"narrative_only","case_id":"R5L71-C19-NARRATIVE","symbol":null,"large_sector_id":"L5_CONSUMER_BRAND_DISTRIBUTION","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","reason":"source proxy evidence should be replaced by exact report/disclosure URLs before production promotion","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 71
next_round = R6
next_loop = 71
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
Source: Songdaiki/stock-web
Manifest max date: 2026-02-20
Price basis: tradable_raw
Price adjustment status: raw_unadjusted_marcap
Rows are historical calibration rows, not live candidate recommendations.
Evidence URLs should be repaired in later data-quality work before any production promotion.
```

